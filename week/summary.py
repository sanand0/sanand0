#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "google-genai>=2.25",
#     "openai>=3",
#     "httpx",
#     "python-dateutil",
#     "python-dotenv",
#     "tqdm",
# ]
# ///

"""Summarizes Github activity --user from last Sunday till most recent Saturday (UTC)"""

import argparse
import base64
import hashlib
import json
import os
import re
import subprocess
import tempfile
from datetime import datetime, timedelta
from fnmatch import fnmatch
from pathlib import Path

import httpx
import tomllib
from dateutil.parser import isoparse
from dateutil.tz import UTC
from dotenv import load_dotenv
from google import genai
from openai import OpenAI
from tqdm import tqdm


def http_request(method, url, timeout=300, **kwargs):
    """Make HTTP request with error body printing for debugging."""
    response = httpx.request(method, url, timeout=timeout, **kwargs)
    try:
        response.raise_for_status()
    except httpx.HTTPStatusError:
        tqdm.write(f"HTTP {response.status_code} error for {url}")
        tqdm.write(f"Response body: {response.text[:500]}")
        raise
    return response


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
            tqdm.write(f"HTTP {r.status_code} error for {url}")
            tqdm.write(f"Response body: {r.text[:500]}")
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


def get_activity_summary(system_prompt, activity, repo_context):
    context_json = json.dumps(repo_context, indent=2)
    payload = {
        "model": "gpt-5-mini",
        "input": [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"Repository Context:\n{context_json}\n\nCommits:\n{activity}",
            },
        ],
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
    }

    response = http_request(
        "POST", "https://api.openai.com/v1/responses", headers=headers, json=payload
    )
    result = response.json()
    cost = result["usage"]["input_tokens"] * 0.4 + result["usage"]["output_tokens"] * 1.6
    # Use last .output entry - first few have reasoning
    return cost, result["output"][-1]["content"][0]["text"]


DIALOGUE_FORMAT = {
    "type": "json_schema",
    "name": "podcast_dialogue",
    "strict": True,
    "schema": {
        "type": "object",
        "properties": {
            "turns": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "speaker": {"type": "string", "enum": ["Alex", "Maya"]},
                        "text": {"type": "string"},
                        "style": {"type": "string"},
                        "new_section": {"type": "boolean"},
                    },
                    "required": ["speaker", "text", "style", "new_section"],
                    "additionalProperties": False,
                },
            }
        },
        "required": ["turns"],
        "additionalProperties": False,
    },
}
AUDIO_MIME = "audio/l16"
LEGACY_EVENTS = {"[laughs]": "<laugh>", "[short pause]": "<short pause>", "[sighs]": "<sigh>"}
LEGACY_STYLES = {"excited": "excited", "whispers": "whispering"}


def api_key(env, _llm_key):
    """Return a required API key loaded from the environment or .env."""
    if value := os.getenv(env):
        return value
    raise ValueError(f"{env} is not set")


def podcast_cache_dir():
    """Return the restartable cache directory for podcast model calls."""
    return Path.home() / ".cache" / "sanand0-week-podcast"


def digest(*parts):
    return hashlib.sha256("\0".join(parts).encode()).hexdigest()[:20]


def format_dialogue(turns):
    """Serialize structured dialogue to the human-readable podcast Markdown file."""
    lines = []
    for turn in turns:
        if turn.get("new_section") and lines:
            lines.append("")
        style = f"[style: {turn['style'].strip()}] " if turn["style"].strip() else ""
        lines.append(f"{turn['speaker']}: {style}{turn['text'].strip()}")
    return "\n".join(lines) + "\n"


def parse_dialogue(script, speakers):
    """Parse generated or historical speaker-labelled scripts into structured turns."""
    if not script.strip():
        raise ValueError("script is empty")
    speaker_re = re.compile(
        rf"^(?P<speaker>{'|'.join(re.escape(name) for name in speakers)}):\s*(?P<text>.*)$"
    )
    turns = []
    for line_no, raw_line in enumerate(script.splitlines(), 1):
        line = raw_line.strip()
        if not line:
            continue
        match = speaker_re.match(line)
        if not match:
            if not turns:
                raise ValueError(f"line {line_no} must begin with one of: {', '.join(speakers)}")
            turns[-1]["text"] += " " + line
            continue

        text = match.group("text").strip()
        for old, new in LEGACY_EVENTS.items():
            text = text.replace(old, new)

        style = ""
        style_match = re.match(r"^\[style:\s*(.+?)\]\s*(.*)$", text)
        if style_match:
            style, text = style_match.groups()
        else:
            legacy_match = re.match(r"^\[([^\]]+)\]\s*(.*)$", text)
            if legacy_match and legacy_match.group(1).lower() in LEGACY_STYLES:
                style = LEGACY_STYLES[legacy_match.group(1).lower()]
                text = legacy_match.group(2)

        if not text:
            raise ValueError(f"speaker {match.group('speaker')} has an empty turn")
        turns.append({"speaker": match.group("speaker"), "text": text, "style": style})
    return turns


def get_podcast_script(activity, repo_context, config, name, week):
    """Generate the Weekly Codecast with GPT-6 Luna structured output."""
    repos = {item["repo.name"] for item in activity}
    target_words = max(1_200, min(2_400, 100 * len(repos) + 30 * len(activity)))
    week_label = datetime.fromisoformat(week).strftime("%d %B %Y")
    prompt = (
        config["podcast"]
        .replace("$NAME", name)
        .replace("$WEEK", week_label)
        .replace("$TARGET_WORDS", f"{target_words:,}")
    )
    source = json.dumps(
        {"repository_context": repo_context, "activity": activity},
        ensure_ascii=False,
        separators=(",", ":"),
    )
    model = config.get("openai", {}).get("model", "gpt-6-luna")
    cache = podcast_cache_dir()
    cache.mkdir(parents=True, exist_ok=True)
    path = cache / f"dialogue-{digest(model, prompt, source, json.dumps(DIALOGUE_FORMAT, sort_keys=True))}.json"

    if path.exists():
        turns = json.loads(path.read_text(encoding="utf-8"))["turns"]
    else:
        print(f"Generating dialogue with {model}...", flush=True)
        response = OpenAI(api_key=api_key("OPENAI_API_KEY", "openai")).responses.create(
            model=model,
            input=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": source},
            ],
            text={"format": DIALOGUE_FORMAT},
        )
        result = json.loads(response.output_text)
        path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        turns = result["turns"]
    return format_dialogue(turns)


def speaker_voices(config):
    voices = {
        item["name"]: item["voice_name"] for item in config.get("gemini", {}).get("speakers", [])
    }
    if not voices:
        raise ValueError("config.toml must define [[gemini.speakers]] entries")
    return voices


def build_speech_content(turns):
    """Build Gemini Interactions content, adding style only when explicitly useful."""
    content = []
    for turn in turns:
        metadata = {"type": "speech_metadata", "speaker": turn["speaker"]}
        if turn["style"].strip():
            metadata["style"] = turn["style"].strip()
        content.append({"type": "text", "text": turn["text"], "annotations": [metadata]})
    return content


def audio_plan(script, config):
    """Validate a script and return the configured TTS execution plan."""
    gemini = config["gemini"]
    voices = speaker_voices(config)
    turns = parse_dialogue(script, list(voices))
    chunk_size = int(gemini.get("chunk_size", 10))
    if chunk_size < 1:
        raise ValueError("gemini.chunk_size must be >= 1")
    return {
        "model": gemini.get("model", "gemini-3.8-flash-lite-tts"),
        "sample_rate": int(gemini.get("sample_rate", 24_000)),
        "chunk_size": chunk_size,
        "turn_count": len(turns),
        "chunk_count": (len(turns) + chunk_size - 1) // chunk_size,
        "speaker_names": list(dict.fromkeys(turn["speaker"] for turn in turns)),
        "voices": voices,
        "turns": turns,
    }


def synthesize_chunk(client, turns, plan):
    interaction = client.interactions.create(
        model=plan["model"],
        input=[{"type": "user_input", "content": build_speech_content(turns)}],
        response_format={
            "type": "audio",
            "mime_type": AUDIO_MIME,
            "sample_rate": plan["sample_rate"],
        },
        generation_config={
            "speech_config": {
                "mode": "conversational",
                "speakers": [
                    {"speaker": speaker, "voice": voice}
                    for speaker, voice in plan["voices"].items()
                ],
            }
        },
    )
    return base64.b64decode(interaction.output_audio.data)


def generate_audio_from_script(script, output_path, config):
    """Generate podcast audio in restartable multi-turn chunks, then encode MP3 once."""
    plan = audio_plan(script, config)
    cache = podcast_cache_dir()
    cache.mkdir(parents=True, exist_ok=True)
    client = None
    pcm_paths = []
    turns = plan["turns"]

    for index, offset in enumerate(range(0, len(turns), plan["chunk_size"]), 1):
        chunk = turns[offset : offset + plan["chunk_size"]]
        chunk_json = json.dumps(chunk, sort_keys=True)
        path = cache / (
            "audio-"
            + digest(
                plan["model"],
                json.dumps(plan["voices"], sort_keys=True),
                AUDIO_MIME,
                str(plan["sample_rate"]),
                chunk_json,
            )
            + ".pcm"
        )
        if not path.exists():
            print(f"Synthesizing chunk {index}/{plan['chunk_count']} with {plan['model']}...", flush=True)
            client = client or genai.Client(api_key=api_key("GEMINI_API_KEY", "gemini"))
            path.write_bytes(synthesize_chunk(client, chunk, plan))
        pcm_paths.append(path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix=".pcm") as pcm:
        for path in pcm_paths:
            pcm.write(path.read_bytes())
        pcm.flush()
        subprocess.run(
            [
                "ffmpeg",
                "-hide_banner",
                "-loglevel",
                "error",
                "-y",
                "-f",
                "s16le",
                "-ar",
                str(plan["sample_rate"]),
                "-ac",
                "1",
                "-i",
                pcm.name,
                "-c:a",
                "libmp3lame",
                "-q:a",
                "4",
                str(output_path),
            ],
            check=True,
        )
    return output_path


def get_podcast_gemini(script, target, config):
    """Generate the weekly podcast MP3 with configurable Gemini 3.8 TTS."""
    output_path = target / f"podcast-{target.name}.mp3"
    if not output_path.exists():
        generate_audio_from_script(script, output_path, config)
    return output_path


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
    """Generate code review using GPT-5.1-Codex."""
    diff_json = json.dumps(net_diff, indent=2)
    payload = {
        "model": "gpt-5.1-codex",
        "input": [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"Code changes to review:\n{diff_json}",
            },
        ],
        "reasoning": {"effort": "medium"},  # Adjust reasoning effort for code review
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
    }

    url = "https://api.openai.com/v1/responses"
    response = http_request("POST", url, headers=headers, json=payload)
    result = response.json()
    # GPT-5.1-Codex pricing: $1.25/M input, $10/M output
    cost = result["usage"]["input_tokens"] * 1.25 + result["usage"]["output_tokens"] * 10.0
    # Use last .output entry - first few have reasoning
    return cost, result["output"][-1]["content"][0]["text"]


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


def update_prompt(prompt, until, args):
    return (
        prompt.replace("$USER", args.user)
        .replace("$NAME", args.name)
        .replace("$WEEK", until.strftime("%d %B %Y"))
    )


def main():
    token = os.environ.get("GITHUB_TOKEN")

    # Default end date is latest Sunday ON OR BEFORE today, UTC.
    # Commits are taken from the previous Sunday to the next Saturday, UTC.
    today = datetime.now(UTC)
    end = today.replace(hour=0, minute=0, second=0, microsecond=0)
    end = (end - timedelta(days=(end.weekday() + 1) % 7)).date().isoformat()

    p = argparse.ArgumentParser()
    p.add_argument("-u", "--user", required=True)
    p.add_argument("-n", "--name", required=True)
    p.add_argument("-e", "--end", default=end, help="End date, excluded (default: latest Sunday)")
    p.add_argument("-s", "--start", help="Start date (default: end date - 7 days)")
    p.add_argument("-t", "--token", default=token, help="GitHub token (default: $GITHUB_TOKEN)")
    args = p.parse_args()

    # parse dates, default naive => UTC
    until = isoparse(args.end)
    if until.tzinfo is None:
        until = until.replace(tzinfo=UTC)

    # Set end date based on start date if not provided
    if args.start is None:
        since = until - timedelta(days=7)
        args.start = since.isoformat()[:10]
    else:
        since = isoparse(args.start)
        if since.tzinfo is None:
            since = since.replace(tzinfo=UTC)

    script_dir = Path(__file__).parent
    with open(script_dir / "config.toml", "rb") as f:
        config = tomllib.load(f)

    week_dir = script_dir / (args.end if args.user == "sanand0" else f"{args.user}-{args.end}")
    week_dir.mkdir(exist_ok=True)
    summary_filename = week_dir / "README.md"
    context_filename = week_dir / "context.json"
    podcast_filename = week_dir / f"podcast-{args.end}.md"
    podcast_output = week_dir / f"podcast-{args.end}.mp3"
    code_review_filename = week_dir / "code-review.md"

    if (
        not summary_filename.exists()
        or not podcast_filename.exists()
        or not code_review_filename.exists()
    ):
        headers = {"Authorization": f"Bearer {args.token}"} if args.token else {}
        if not context_filename.exists():
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
            with open(context_filename, "w") as f:
                json.dump([activity, repos, context], f)
        else:
            with open(context_filename, "r") as f:
                (activity, repos, context) = json.load(f)
        input = json.dumps(activity, indent=2)
        if not summary_filename.exists():
            prompt = update_prompt(config["summary"], until, args)
            cost, summary = get_activity_summary(prompt, input, context)
            print(f"Summary: {cost / 1e4:,.1f}c")
            with open(summary_filename, "w") as f:
                f.write(summary)
        if not podcast_filename.exists():
            podcast = get_podcast_script(activity, context, config, args.name, args.end)
            with open(podcast_filename, "w") as f:
                f.write(podcast)
        # Generate code review (independent of podcast/summary)
        if not code_review_filename.exists():
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
                    print(f"Code Review: {cost / 1e4:,.1f}c")
                    with open(code_review_filename, "w") as f:
                        f.write(review)
                else:
                    print("No code changes found for review")
            else:
                print("No reviewable files found for code review")
    if not podcast_output.exists():
        get_podcast_gemini(podcast_filename.read_text(), week_dir, config)

    # Get all directories beginning with "20" only if it contains podcast script
    weeks = [
        d.name
        for d in script_dir.iterdir()
        if d.is_dir() and d.name.startswith("20") and (d / f"podcast-{d.name}.md").exists()
    ]
    generate_podcast(weeks, script_dir)


if __name__ == "__main__":
    load_dotenv()
    main()
