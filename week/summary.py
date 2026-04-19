#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "httpx",
#     "python-dateutil",
#     "python-dotenv",
#     "tqdm",
# ]
# ///

"""Summarizes Github activity --user from last Sunday till most recent Saturday (UTC)"""

import base64
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import tomllib
from datetime import datetime, timedelta
from dataclasses import dataclass
from fnmatch import fnmatch
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

import httpx
from dateutil.parser import isoparse
from dateutil.tz import UTC
from dotenv import load_dotenv
from tqdm import tqdm

COMMAND_WEEKLY = "weekly"
COMMAND_TTS_SCRIPT = "tts-script"
DEFAULT_GEMINI_MODEL = "gemini-3.1-flash-tts-preview"
RETRYABLE_STATUS_CODES = {500, 502, 503, 504}


@dataclass(frozen=True)
class SpeakerConfig:
    """Speaker metadata used to validate scripts and build Gemini voice settings."""

    name: str
    voice_name: str
    profile: str = ""


@dataclass(frozen=True)
class WeekPaths:
    """File locations for one weekly run."""

    week: str
    week_dir: Path
    summary: Path
    context: Path
    podcast_script: Path
    code_review: Path
    audio: Path


def log_http_error(url: str, response: httpx.Response) -> None:
    """Print compact HTTP error details for debugging."""
    tqdm.write(f"HTTP {response.status_code} error for {url}")
    tqdm.write(f"Response body: {response.text[:500]}")


def http_request(method, url, timeout=300, retries=1, retry_statuses=(), **kwargs):
    """Make HTTP request with error body printing for debugging."""
    response = None
    for attempt in range(1, retries + 1):
        response = httpx.request(method, url, timeout=timeout, **kwargs)
        try:
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError:
            log_http_error(url, response)
            if response.status_code not in retry_statuses or attempt == retries:
                raise
            time.sleep(attempt)

    raise RuntimeError(f"request loop ended unexpectedly for {url}")


def graphql_query(query, variables, headers):
    """Execute a GraphQL query against GitHub API."""
    response = http_request(
        "POST",
        "https://api.github.com/graphql",
        json={"query": query, "variables": variables},
        headers=headers,
    )
    result = response.json()
    if "errors" in result:
        raise Exception(f"GraphQL errors: {result['errors']}")
    return result["data"]


def fetch_contributed_repos(user, since, until, headers):
    """Fetch list of repos user contributed to in date range using GraphQL."""
    query = """
    query($user: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $user) {
        contributionsCollection(from: $from, to: $to) {
          commitContributionsByRepository(maxRepositories: 100) {
            repository {
              nameWithOwner
            }
            contributions {
              totalCount
            }
          }
        }
      }
    }
    """
    variables = {
        "user": user,
        "from": since.isoformat(),
        "to": until.isoformat(),
    }

    data = graphql_query(query, variables, headers)
    repos = []
    for item in data["user"]["contributionsCollection"]["commitContributionsByRepository"]:
        repo_name = item["repository"]["nameWithOwner"]
        commit_count = item["contributions"]["totalCount"]
        repos.append((repo_name, commit_count))

    return repos


def fetch_repo_commits(repo, since, until, headers):
    """Fetch commits for a repository within a date range using the REST API."""
    url = f"https://api.github.com/repos/{repo}/commits"
    params = {
        "since": since.isoformat(),
        "until": until.isoformat(),
        "per_page": 100,
    }
    commits = []
    while url:
        r = httpx.get(url, headers=headers, params=params)
        if r.status_code == 409:  # Empty repository
            break
        try:
            r.raise_for_status()
        except httpx.HTTPStatusError:
            log_http_error(url, r)
            raise
        page = r.json()
        commits.extend(page)
        url = r.headers.get("link", "")
        # Parse Link header for next URL
        next_url = None
        for part in url.split(","):
            if 'rel="next"' in part:
                next_url = part.split(";")[0].strip().strip("<>")
                break
        url = next_url
        params = {}  # params are in the URL for subsequent pages
    return commits


def fetch_repo_details(repos, headers):
    """Fetch repository details including description, topics and README."""
    details = {}
    for repo in tqdm(set(repos), desc="Get repos"):
        try:
            repo_url = f"https://api.github.com/repos/{repo}"
            info = http_request("GET", repo_url, headers=headers).json()
            readme_url = f"https://api.github.com/repos/{repo}/readme"
            readme_resp = http_request("GET", readme_url, headers=headers).json()
            readme = base64.b64decode(readme_resp.get("content", "")).decode("utf-8", "ignore")
            # Truncate README to first 2000 chars to save space while keeping key info
            if len(readme) > 2000:
                readme = readme[:2000] + "\n... [README truncated]"
            details[repo] = {
                "description": info.get("description", ""),
                "topics": info.get("topics", []),
                "readme": readme,
            }
        except Exception as e:
            tqdm.write(f"Error fetching {repo}: {e}")
    return details


def truncate_patch(patch, max_lines=50):
    """Truncate patch in the middle to keep start and end context."""
    if not patch:
        return ""
    lines = patch.splitlines()
    if len(lines) <= max_lines:
        return patch
    # Keep first and last portions, truncate middle
    keep_each = max_lines // 2
    start = lines[:keep_each]
    end = lines[-keep_each:]
    skipped = len(lines) - max_lines
    return "\n".join(start + [f"\n... [{skipped} lines truncated] ...\n"] + end)


def is_binary_patch(patch):
    """Check if patch contains binary/generated content (base64, minified, etc.)."""
    if not patch or len(patch) < 200:
        return False
    # Check for base64-like patterns
    if patch.count("AAAA") > 5 or patch.count("////") > 5:
        return True
    # Check for very long lines (minified JS/CSS)
    for line in patch.splitlines()[:10]:
        if len(line) > 500:
            return True
    return False


def summarize_files(files, config, skip_files, max_files=12, max_patch_lines=50):
    """Summarize file changes, limiting number of files and patch size."""
    if not files:
        return []

    # Sort files by priority: code files first, then by changes
    def file_priority(f):
        name = f.get("filename", "")
        for priority, exts in enumerate(config["source_priority"]):
            if any(name.endswith(ext) for ext in exts):
                return (priority, -f.get("changes", 0))
        return (len(config["source_priority"]), -f.get("changes", 0))

    sorted_files = sorted(files, key=file_priority)

    result = []
    for f in sorted_files[:max_files]:
        should_skip_patch = any(fnmatch(f["filename"], pattern) for pattern in skip_files)
        raw_patch = f.get("patch", "")
        if should_skip_patch:
            patch = "..."
        elif is_binary_patch(raw_patch):
            patch = "[binary/generated content]"
        else:
            patch = truncate_patch(raw_patch, max_patch_lines)
        update = {
            "filename": f["filename"],
            "additions": f.get("additions", 0),
            "deletions": f.get("deletions", 0),
            "changes": f.get("changes", 0),
            "patch": patch,
        }
        result.append(update)

    if len(files) > max_files:
        # Add summary of remaining files
        remaining = files[max_files:]
        update = {
            "filename": f"... and {len(remaining)} more files",
            "additions": sum(f.get("additions", 0) for f in remaining),
            "deletions": sum(f.get("deletions", 0) for f in remaining),
            "changes": sum(f.get("changes", 0) for f in remaining),
            "patch": "",
        }
        result.append(update)

    return result


def fetch_github_activity(user, since, until, headers, config, skip_repos, skip_files):
    """Fetch and process GitHub activity using GraphQL to discover repos, REST for commit details."""
    activity = []
    seen_commits = set()

    # Use GraphQL to discover repos with contributions in date range
    # This works for historical data beyond 30-day Events API limit
    contributed_repos = fetch_contributed_repos(user, since, until, headers)

    # Filter out skipped repos
    repos = [repo for repo, count in contributed_repos if repo not in skip_repos]
    tqdm.write(f"Found {len(repos)} repos with contributions")

    # Fetch actual commits from each repo
    for repo in tqdm(repos, desc="Get commits"):
        try:
            commits = fetch_repo_commits(repo, since, until, headers)
        except httpx.HTTPStatusError as e:
            tqdm.write(f"Error fetching commits for {repo}: {e}")
            continue

        for commit_info in commits:
            sha = commit_info["sha"]
            if sha in seen_commits:
                continue
            seen_commits.add(sha)

            # Check if this commit was authored by the user
            author_login = commit_info.get("author", {})
            if author_login:
                author_login = author_login.get("login", "")
            committer_login = commit_info.get("committer", {})
            if committer_login:
                committer_login = committer_login.get("login", "")

            # Skip commits not by this user (e.g., merge commits from others)
            if author_login != user and committer_login != user:
                continue

            # Fetch full commit details (includes file changes)
            try:
                url = f"https://api.github.com/repos/{repo}/commits/{sha}"
                r = http_request("GET", url, headers=headers)
                cj = r.json()
            except (httpx.HTTPStatusError, json.JSONDecodeError) as e:
                tqdm.write(f"Error fetching commit {sha}: {e}")
                continue

            activity.append(
                {
                    "type": "commit",
                    "repo.name": repo,
                    "created_at": cj["commit"]["author"]["date"],
                    "sha": sha,
                    "message": cj["commit"]["message"],
                    "files": summarize_files(cj.get("files", []), config, skip_files),
                }
            )

    return activity, repos


def get_openai_text(
    *,
    model: str,
    system_prompt: str,
    user_content: str,
    input_rate: float,
    output_rate: float,
    reasoning: Dict[str, Any] | None = None,
) -> Tuple[float, str]:
    """Call the OpenAI Responses API and return cost plus final text output."""
    payload = {
        "model": model,
        "input": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
    }
    if reasoning:
        payload["reasoning"] = reasoning

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
    }

    response = http_request(
        "POST", "https://api.openai.com/v1/responses", headers=headers, json=payload
    )
    result = response.json()
    cost = result["usage"]["input_tokens"] * input_rate + result["usage"]["output_tokens"] * output_rate
    return cost, result["output"][-1]["content"][0]["text"]


def get_activity_summary(system_prompt, activity, repo_context):
    context_json = json.dumps(repo_context, indent=2)
    return get_openai_text(
        model="gpt-5.4-mini",
        system_prompt=system_prompt,
        user_content=f"Repository Context:\n{context_json}\n\nCommits:\n{activity}",
        input_rate=0.4,
        output_rate=1.6,
    )


def truncate_patch_for_review(patch, file_type, max_code_lines=500, max_data_lines=50):
    """Truncate patch based on file type - more lines for code, fewer for data/docs."""
    if not patch:
        return ""
    lines = patch.splitlines()
    max_lines = max_code_lines if file_type == "code" else max_data_lines
    if len(lines) <= max_lines:
        return patch
    # Keep first and last portions, truncate middle
    keep_each = max_lines // 2
    start = lines[:keep_each]
    end = lines[-keep_each:]
    skipped = len(lines) - max_lines
    return "\n".join(start + [f"\n... [{skipped} lines truncated] ...\n"] + end)


def filter_code_files(activity, code_extensions, data_extensions, doc_extensions):
    """Filter activity to include code, data, and doc files with appropriate truncation."""
    filtered_activity = []

    for commit in activity:
        # Filter files to include reviewable files
        reviewable_files = []
        for f in commit.get("files", []):
            filename = f.get("filename", "")
            patch = f.get("patch", "")

            # Skip if no patch or trivial
            if not patch or patch in ["...", "[binary/generated content]"]:
                continue

            # Determine file type and truncate appropriately
            if any(filename.endswith(ext) for ext in code_extensions):
                file_type = "code"
            elif any(filename.endswith(ext) for ext in data_extensions):
                file_type = "data"
            elif any(filename.endswith(ext) for ext in doc_extensions):
                file_type = "doc"
            else:
                continue  # Skip other file types

            # Truncate patch based on file type
            truncated_patch = truncate_patch_for_review(patch, file_type)
            new_file = f.copy()
            new_file["patch"] = truncated_patch
            new_file["file_type"] = file_type
            reviewable_files.append(new_file)

        if reviewable_files:
            filtered_commit = commit.copy()
            filtered_commit["files"] = reviewable_files
            filtered_activity.append(filtered_commit)

    return filtered_activity


def compute_net_diff(activity):
    """Compute NET diff per repo - aggregate all file changes across commits."""
    repo_diffs = {}

    for commit in activity:
        repo = commit.get("repo.name", "")
        if repo not in repo_diffs:
            repo_diffs[repo] = {"files": {}, "commits": []}

        commit = {
            "sha": commit.get("sha", ""),
            "message": commit.get("message", ""),
            "date": commit.get("created_at", ""),
        }
        repo_diffs[repo]["commits"].append(commit)

        # Aggregate file changes - later patches override earlier ones for same file
        for f in commit.get("files", []):
            filename = f["filename"]
            if filename not in repo_diffs[repo]["files"]:
                repo_diffs[repo]["files"][filename] = {
                    "patches": [],
                    "total_additions": 0,
                    "total_deletions": 0,
                }
            repo_diffs[repo]["files"][filename]["patches"].append(f.get("patch", ""))
            repo_diffs[repo]["files"][filename]["total_additions"] += f.get("additions", 0)
            repo_diffs[repo]["files"][filename]["total_deletions"] += f.get("deletions", 0)

    # Format for review - combine patches for each file
    review_data = {}
    for repo, data in repo_diffs.items():
        review_data[repo] = {
            "commits": data["commits"],
            "files": {},
        }
        for filename, file_data in data["files"].items():
            # Combine all patches for this file (shows evolution)
            combined_patch = "\n---\n".join(p for p in file_data["patches"] if p)
            review_data[repo]["files"][filename] = {
                "net_additions": file_data["total_additions"],
                "net_deletions": file_data["total_deletions"],
                "patches": combined_patch,
            }

    return review_data


def get_code_review(system_prompt, net_diff):
    """Generate code review using GPT-5.4."""
    diff_json = json.dumps(net_diff, indent=2)
    return get_openai_text(
        model="gpt-5.4",
        system_prompt=system_prompt,
        user_content=f"Code changes to review:\n{diff_json}",
        input_rate=1.25,
        output_rate=10.0,
        reasoning={"effort": "medium"},
    )


def collapse_whitespace(text: str) -> str:
    """Collapse internal whitespace to keep prompt scaffolding compact."""
    return re.sub(r"\s+", " ", text.strip())


def load_gemini_speakers(config: Dict[str, Any]) -> List[SpeakerConfig]:
    """Load Gemini speaker definitions from config.toml."""
    speaker_items = config.get("gemini", {}).get("speakers")
    if not isinstance(speaker_items, list) or not speaker_items:
        raise ValueError("config.toml must define `[[gemini.speakers]]` entries")

    speakers = [
        SpeakerConfig(
            name=item["name"],
            voice_name=item["voice_name"],
            profile=str(item.get("profile", "")).strip(),
        )
        for item in speaker_items
    ]
    if len(speakers) > 2:
        raise ValueError("Gemini multi-speaker TTS supports at most 2 speakers")
    return speakers


def normalize_script(script: str, allowed_speakers: Sequence[str]) -> Tuple[str, List[str]]:
    """
    Normalize a speaker-labeled transcript into one utterance per line.

    Each non-empty line must either start with `Speaker:` or continue the previous speaker's text.
    """

    if not script.strip():
        raise ValueError("script is empty")

    speaker_pattern = re.compile(
        rf"^(?P<speaker>{'|'.join(re.escape(name) for name in allowed_speakers)}):\s*(?P<text>.*)$"
    )
    generic_label_pattern = re.compile(r"^(?P<label>[^:\s][^:]{0,80}):\s*(?P<text>.*)$")

    utterances: List[Dict[str, str]] = []
    current: Dict[str, str] | None = None

    for index, raw_line in enumerate(script.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue

        speaker_match = speaker_pattern.match(line)
        if speaker_match:
            current = {
                "speaker": speaker_match.group("speaker"),
                "text": speaker_match.group("text").strip(),
            }
            utterances.append(current)
            continue

        generic_match = generic_label_pattern.match(line)
        if generic_match:
            raise ValueError(
                f"line {index} uses unsupported speaker {generic_match.group('label')!r}; "
                f"expected one of {', '.join(allowed_speakers)}"
            )

        if current is None:
            raise ValueError(
                f"line {index} must begin with a speaker label like {allowed_speakers[0]}:"
            )

        if current["text"]:
            current["text"] += " " + line
        else:
            current["text"] = line

    if not utterances:
        raise ValueError("script has no speaker lines")

    used_speakers: List[str] = []
    normalized_lines: List[str] = []
    for utterance in utterances:
        text = utterance["text"].strip()
        if not text:
            raise ValueError(f"speaker {utterance['speaker']} has an empty line in the script")
        normalized_lines.append(f"{utterance['speaker']}: {text}")
        if utterance["speaker"] not in used_speakers:
            used_speakers.append(utterance["speaker"])

    return "\n".join(normalized_lines), used_speakers


def build_tts_prompt(script: str, speakers: Sequence[SpeakerConfig], config: Dict[str, Any]) -> str:
    """Build a Gemini TTS prompt that keeps directions out of the spoken transcript."""
    sections = [
        "Synthesize speech for the following podcast conversation.",
        "Do not read these instructions aloud.",
        "Respect the speaker labels exactly as written.",
        "Honor inline audio tags such as [excited], [laughs], [whispers], and [short pause].",
        "Only speak the transcript under the TRANSCRIPT heading.",
    ]

    podcast_style = collapse_whitespace(str(config.get("podcast_style", "")))
    if podcast_style:
        sections.append(podcast_style)

    speaker_profiles = [
        f"{speaker.name}: {collapse_whitespace(speaker.profile)}"
        for speaker in speakers
        if speaker.profile.strip()
    ]
    if speaker_profiles:
        sections.append("Speaker guidance:")
        sections.extend(speaker_profiles)

    sections.append("TRANSCRIPT")
    sections.append(script.strip())
    return "\n".join(sections)


def build_gemini_request(
    script: str, config: Dict[str, Any]
) -> Tuple[Dict[str, Any], str, List[SpeakerConfig]]:
    """Build the Gemini TTS request payload for a validated speaker script."""
    all_speakers = load_gemini_speakers(config)
    normalized_script, used_speakers = normalize_script(
        script,
        [speaker.name for speaker in all_speakers],
    )
    active_speakers = [speaker for speaker in all_speakers if speaker.name in used_speakers]

    payload = {
        "model": config.get("gemini", {}).get("model", DEFAULT_GEMINI_MODEL),
        "contents": [
            {
                "role": "user",
                "parts": [{"text": build_tts_prompt(normalized_script, active_speakers, config)}],
            }
        ],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {
                "multiSpeakerVoiceConfig": {
                    "speakerVoiceConfigs": [
                        {
                            "speaker": speaker.name,
                            "voiceConfig": {
                                "prebuiltVoiceConfig": {"voiceName": speaker.voice_name}
                            },
                        }
                        for speaker in active_speakers
                    ]
                }
            },
        },
    }
    return payload, normalized_script, active_speakers


def request_gemini_audio(payload: Dict[str, Any]) -> bytes:
    """Call the Gemini TTS endpoint and return raw PCM bytes."""
    if not os.environ.get("GEMINI_API_KEY"):
        raise ValueError("GEMINI_API_KEY is not set")

    headers = {
        "x-goog-api-key": os.environ["GEMINI_API_KEY"],
        "Content-Type": "application/json",
    }
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{payload['model']}:generateContent"
    )
    response = http_request(
        "POST",
        url,
        headers=headers,
        json=payload,
        timeout=300,
        retries=3,
        retry_statuses=RETRYABLE_STATUS_CODES,
    )
    result = response.json()
    audio_b64 = result["candidates"][0]["content"]["parts"][0]["inlineData"]["data"]
    return base64.b64decode(audio_b64)


def render_pcm_as_mp3(audio_pcm: bytes, output_path: Path, config: Dict[str, Any]) -> Path:
    """Convert raw 24kHz mono PCM from Gemini into the configured audio format."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pcm_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            delete=False, suffix=".pcm", dir=output_path.parent
        ) as temp_file:
            temp_file.write(audio_pcm)
            pcm_path = Path(temp_file.name)

        ffmpeg_args = [
            arg.format(pcm=pcm_path, output=output_path)
            for arg in config["gemini"]["ffmpeg_command"]
        ]
        subprocess.run(ffmpeg_args, check=True)
    finally:
        if pcm_path and pcm_path.exists():
            pcm_path.unlink()

    return output_path


def generate_audio_from_script(
    script: str,
    output_path: Path,
    config: Dict[str, Any],
    *,
    dry_run: bool = False,
) -> Dict[str, Any]:
    """Generate audio for a speaker-labeled podcast script."""
    payload, normalized_script, speakers = build_gemini_request(script, config)
    result = {
        "command": COMMAND_TTS_SCRIPT,
        "audio_path": str(output_path.resolve()),
        "speaker_names": [speaker.name for speaker in speakers],
        "model": payload["model"],
        "normalized_script": normalized_script,
    }

    if dry_run:
        result["status"] = "dry-run"
        return result

    audio_pcm = request_gemini_audio(payload)
    render_pcm_as_mp3(audio_pcm, output_path, config)
    result["status"] = "ok"
    return result


def generate_podcast(weeks, script_dir):
    output_path = script_dir / "podcast.xml"
    base_url = "https://github.com/sanand0/sanand0/releases/download/main"
    title = "Anand's Weekly Code Cast"
    link = "https://github.com/sanand0/sanand0"
    description = "Weekly audio summaries of Anand's commits to GitHub."
    now = datetime.now(UTC).strftime("%a, %d %b %Y %H:%M:%S GMT")

    # build each <item>
    items_xml = []
    for week in sorted(weeks, reverse=True):
        url = f"{base_url}/podcast-{week}.mp3"
        # RFC-822 pubDate at midnight UTC on the week start
        pub = datetime.strptime(week, "%Y-%m-%d").strftime("%a, %d %b %Y 00:00:00 GMT")
        # Load script
        md_path = script_dir / week / f"podcast-{week}.md"
        description_cdata = f"<![CDATA[\n{md_path.read_text(encoding='utf-8')}\n]]>"

        items_xml.append(f"""  <item>
    <title>Week of {week}</title>
    <enclosure url="{url}" length="0" type="audio/mpeg"/>
    <guid>{url}</guid>
    <pubDate>{pub}</pubDate>
    <description>{description_cdata}</description>
  </item>""")

    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>{title}</title>
  <link>{link}</link>
  <description>{description}</description>
  <lastBuildDate>{now}</lastBuildDate>
{chr(10).join(items_xml)}
</channel>
</rss>"""

    output_path.write_text(rss, encoding="utf-8")


def load_config(script_dir: Path) -> Dict[str, Any]:
    """Load config.toml from the project root."""
    with open(script_dir / "config.toml", "rb") as f:
        return tomllib.load(f)


def default_end_date() -> str:
    """Return the latest Sunday on or before today in UTC as YYYY-MM-DD."""
    today = datetime.now(UTC)
    end = today.replace(hour=0, minute=0, second=0, microsecond=0)
    end = end - timedelta(days=(end.weekday() + 1) % 7)
    return end.date().isoformat()


def build_week_paths(script_dir: Path, user: str, week: str) -> WeekPaths:
    """Resolve the file layout for a weekly summary run."""
    week_dir = script_dir / (week if user == "sanand0" else f"{user}-{week}")
    return WeekPaths(
        week=week,
        week_dir=week_dir,
        summary=week_dir / "README.md",
        context=week_dir / "context.json",
        podcast_script=week_dir / f"podcast-{week}.md",
        code_review=week_dir / "code-review.md",
        audio=week_dir / f"podcast-{week}.mp3",
    )


def load_params(path: str | None) -> Dict[str, Any]:
    """Load command parameters from JSON, optionally from stdin when path is `-`."""
    if not path:
        return {}

    raw = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    params = json.loads(raw)
    if not isinstance(params, dict):
        raise ValueError("--params must contain a JSON object")
    return params


def validate_params(params: Dict[str, Any], allowed_keys: Sequence[str]) -> None:
    """Reject unexpected JSON parameters so agent callers fail fast."""
    unknown_keys = sorted(set(params) - set(allowed_keys))
    if unknown_keys:
        raise ValueError(f"unsupported params keys: {', '.join(unknown_keys)}")


def resolve_output_format(args: argparse.Namespace) -> str:
    """Resolve text vs JSON output. Non-TTY defaults to JSON for agent callers."""
    if args.json:
        return "json"
    if args.format:
        return args.format
    return "text" if sys.stdout.isatty() else "json"


def describe_cli() -> Dict[str, Any]:
    """Return a machine-readable description of the CLI interface."""
    return {
        "name": "summary.py",
        "description": "Generate weekly GitHub summaries, podcast scripts, and Gemini TTS audio.",
        "env": ["GITHUB_TOKEN", "OPENAI_API_KEY", "GEMINI_API_KEY"],
        "commands": {
            COMMAND_WEEKLY: {
                "description": "Fetch GitHub activity for a week and generate summary, script, review, audio, and RSS.",
                "params": {
                    "user": {"type": "string", "required": True},
                    "name": {"type": "string", "required": True},
                    "end": {"type": "string", "optional": True},
                    "start": {"type": "string", "optional": True},
                    "token": {"type": "string", "optional": True},
                    "dry_run": {"type": "boolean", "default": False},
                    "format": {"type": "string", "enum": ["text", "json"]},
                },
            },
            COMMAND_TTS_SCRIPT: {
                "description": "Generate audio directly from a speaker-labeled script file or inline script text.",
                "params": {
                    "script_file": {"type": "string", "optional": True},
                    "script": {"type": "string", "optional": True},
                    "audio_out": {"type": "string", "optional": True},
                    "dry_run": {"type": "boolean", "default": False},
                    "format": {"type": "string", "enum": ["text", "json"]},
                },
            },
        },
    }


def emit_result(result: Dict[str, Any], output_format: str) -> None:
    """Print CLI results in text or JSON form."""
    if output_format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    if result.get("command") == COMMAND_WEEKLY:
        if result["status"] == "dry-run":
            print(result["summary"])
        else:
            if "summary_cost_cents" in result:
                print(f"Summary: {result['summary_cost_cents']}c")
            if "podcast_cost_cents" in result:
                print(f"Podcast script: {result['podcast_cost_cents']}c")
            if "code_review_cost_cents" in result:
                print(f"Code review: {result['code_review_cost_cents']}c")
            print(f"Audio: {result['audio_path']}")
            print(f"RSS: {result['rss_path']}")
        return

    if result.get("command") == COMMAND_TTS_SCRIPT:
        if result["status"] == "dry-run":
            print(
                f"Dry run validated {', '.join(result['speaker_names'])} script. "
                f"Would write {result['audio_path']}"
            )
        else:
            print(
                f"Generated audio at {result['audio_path']} using {', '.join(result['speaker_names'])}."
            )
        return

    print(json.dumps(result, ensure_ascii=False, indent=2))


def update_prompt(prompt, until, args):
    return (
        prompt.replace("$USER", args.user)
        .replace("$NAME", args.name)
        .replace("$WEEK", until.strftime("%d %B %Y"))
    )


def resolve_script_input(
    *,
    script_file: str | None,
    script_text: str | None,
) -> Tuple[str, str]:
    """Resolve exactly one script input source."""
    if bool(script_file) == bool(script_text):
        raise ValueError("provide exactly one of --script-file or --script-text")

    if script_file:
        if script_file == "-":
            return sys.stdin.read(), "stdin"
        path = Path(script_file)
        return path.read_text(encoding="utf-8"), str(path.resolve())

    return script_text or "", "inline"


def describe_week_run(paths: WeekPaths) -> str:
    """Describe what the weekly run will verify or create."""
    return (
        f"Week {paths.week}: "
        f"context.json={'present' if paths.context.exists() else 'missing'}, "
        f"README.md={'present' if paths.summary.exists() else 'missing'}, "
        f"podcast-{paths.week}.md={'present' if paths.podcast_script.exists() else 'missing'}, "
        f"code-review.md={'present' if paths.code_review.exists() else 'missing'}, "
        f"podcast-{paths.week}.mp3={'present' if paths.audio.exists() else 'missing'}"
    )


def run_tts_script(
    script_dir: Path,
    *,
    script_file: str | None,
    script_text: str | None,
    audio_out: str | None,
    dry_run: bool,
) -> Dict[str, Any]:
    """Run the script-to-audio workflow for manual testing or ad hoc generation."""
    config = load_config(script_dir)
    script, source = resolve_script_input(script_file=script_file, script_text=script_text)

    if audio_out:
        output_path = Path(audio_out)
    elif script_file and script_file != "-":
        output_path = Path(script_file).with_suffix(".mp3")
    else:
        raise ValueError("--audio-out is required when using --script-text or stdin")

    result = generate_audio_from_script(script, output_path, config, dry_run=dry_run)
    result["script_source"] = source
    return result


def run_weekly(args: argparse.Namespace, script_dir: Path, config: Dict[str, Any]) -> Dict[str, Any]:
    """Run the weekly GitHub activity -> summary -> script -> audio workflow."""
    if not args.user:
        raise ValueError("--user is required for `weekly`")
    if not args.name:
        raise ValueError("--name is required for `weekly`")

    until = isoparse(args.end)
    if until.tzinfo is None:
        until = until.replace(tzinfo=UTC)

    if args.start is None:
        since = until - timedelta(days=7)
        args.start = since.isoformat()[:10]
    else:
        since = isoparse(args.start)
        if since.tzinfo is None:
            since = since.replace(tzinfo=UTC)

    week = args.end
    paths = build_week_paths(script_dir, args.user, week)

    result: Dict[str, Any] = {
        "command": COMMAND_WEEKLY,
        "week": week,
        "week_dir": str(paths.week_dir.resolve()),
        "summary_path": str(paths.summary.resolve()),
        "context_path": str(paths.context.resolve()),
        "podcast_script_path": str(paths.podcast_script.resolve()),
        "code_review_path": str(paths.code_review.resolve()),
        "audio_path": str(paths.audio.resolve()),
    }

    if args.dry_run:
        result["status"] = "dry-run"
        result["summary"] = describe_week_run(paths)
        return result

    paths.week_dir.mkdir(exist_ok=True)
    headers = {"Authorization": f"Bearer {args.token}"} if args.token else {}
    needs_generated_text = not paths.summary.exists() or not paths.podcast_script.exists() or not paths.code_review.exists()

    if needs_generated_text:
        if not paths.context.exists():
            activity, repos = fetch_github_activity(
                args.user,
                since,
                until,
                headers,
                config,
                skip_repos=config["skip-repos"],
                skip_files=config["skip-files"],
            )
            context = fetch_repo_details(repos, headers)
            paths.context.write_text(json.dumps([activity, repos, context]), encoding="utf-8")
        else:
            activity, repos, context = json.loads(paths.context.read_text(encoding="utf-8"))

        activity_json = json.dumps(activity, indent=2)

        if not paths.summary.exists():
            prompt = update_prompt(config["summary"], until, args)
            cost, summary = get_activity_summary(prompt, activity_json, context)
            paths.summary.write_text(summary, encoding="utf-8")
            result["summary_cost_cents"] = round(cost / 1e4, 4)

        if not paths.podcast_script.exists():
            prompt = update_prompt(config["podcast"], until, args)
            cost, podcast = get_activity_summary(prompt, activity_json, context)
            paths.podcast_script.write_text(podcast, encoding="utf-8")
            result["podcast_cost_cents"] = round(cost / 1e4, 4)

        if not paths.code_review.exists():
            code_activity = filter_code_files(
                activity,
                config.get("code-extensions", []),
                config.get("data-extensions", []),
                config.get("doc-extensions", []),
            )
            if code_activity:
                net_diff = compute_net_diff(code_activity)
                if net_diff:
                    prompt = update_prompt(config["code-review"], until, args)
                    cost, review = get_code_review(prompt, net_diff)
                    paths.code_review.write_text(review, encoding="utf-8")
                    result["code_review_cost_cents"] = round(cost / 1e4, 4)

    if not paths.audio.exists():
        generate_audio_from_script(
            paths.podcast_script.read_text(encoding="utf-8"),
            paths.audio,
            config,
        )

    weeks = [
        d.name
        for d in script_dir.iterdir()
        if d.is_dir() and d.name.startswith("20") and (d / f"podcast-{d.name}.md").exists()
    ]
    generate_podcast(weeks, script_dir)
    result["rss_path"] = str((script_dir / "podcast.xml").resolve())
    result["status"] = "ok"
    return result


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser."""
    parser = argparse.ArgumentParser(
        description=(
            "Generate weekly GitHub summaries and podcast audio, or synthesize "
            "audio directly from a speaker-labeled script."
        )
    )
    parser.add_argument(
        "command",
        nargs="?",
        choices=[COMMAND_WEEKLY, COMMAND_TTS_SCRIPT],
        default=COMMAND_WEEKLY,
        help="`weekly` fetches GitHub activity; `tts-script` turns a script into audio",
    )
    parser.add_argument("-u", "--user", help="GitHub username for `weekly`")
    parser.add_argument("-n", "--name", help="Display name for `weekly` prompts")
    parser.add_argument(
        "-e",
        "--end",
        default=default_end_date(),
        help="End date in YYYY-MM-DD format (default: latest Sunday)",
    )
    parser.add_argument("-s", "--start", help="Start date in YYYY-MM-DD format (default: end date - 7 days)")
    parser.add_argument(
        "-t",
        "--token",
        default=os.environ.get("GITHUB_TOKEN"),
        help="GitHub token (default: $GITHUB_TOKEN)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate inputs and planned outputs without writing files or calling APIs",
    )
    parser.add_argument("--params", help="Read command parameters from a JSON object file, or `-` for stdin")
    parser.add_argument("--format", choices=["text", "json"], help="Output format. Defaults to JSON for non-TTY callers.")
    parser.add_argument("--json", action="store_true", help="Shortcut for `--format json`")
    parser.add_argument("--describe", action="store_true", help="Print a machine-readable CLI schema as JSON and exit")
    parser.add_argument("--script-file", help="Path to a speaker-labeled script for `tts-script`, or `-` for stdin")
    parser.add_argument("--script-text", help="Inline speaker-labeled script text for `tts-script`")
    parser.add_argument("--audio-out", help="Output audio path for `tts-script`. Defaults to the script filename with `.mp3`.")
    return parser


def main(argv: List[str] | None = None, *, script_dir: Path | None = None) -> int:
    """Run the CLI."""
    load_dotenv()
    args = build_parser().parse_args(argv)
    output_format = resolve_output_format(args)
    script_dir = script_dir or Path(__file__).parent

    if args.describe:
        emit_result(describe_cli(), "json")
        return 0

    params = load_params(args.params)

    try:
        if args.command == COMMAND_WEEKLY:
            validate_params(params, ["dry_run", "end", "name", "start", "token", "user"])
            args.user = args.user or params.get("user")
            args.name = args.name or params.get("name")
            args.end = params.get("end", args.end)
            args.start = args.start or params.get("start")
            args.token = args.token or params.get("token")
            args.dry_run = bool(params.get("dry_run", args.dry_run))
            result = run_weekly(args, script_dir, load_config(script_dir))
        else:
            validate_params(params, ["audio_out", "dry_run", "script", "script_file"])
            result = run_tts_script(
                script_dir,
                script_file=args.script_file or params.get("script_file"),
                script_text=args.script_text or params.get("script"),
                audio_out=args.audio_out or params.get("audio_out"),
                dry_run=bool(params.get("dry_run", args.dry_run)),
            )
    except Exception as exc:
        emit_result(
            {"command": args.command, "status": "error", "error": str(exc)},
            output_format,
        )
        return 1

    emit_result(result, output_format)
    return 0


if __name__ == "__main__":
    main()
