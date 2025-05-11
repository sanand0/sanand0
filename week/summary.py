# Usage: uv run summary.py -u <user>
# Summarizes Github commits for a user from last Sunday till most recent Saturday

#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "python-dateutil",
#     "requests",
#     "tqdm",
# ]
# ///
import argparse
import base64
import json
import os
import requests
import tomllib
from dateutil.parser import isoparse
from dateutil.tz import UTC
from tqdm import tqdm
from datetime import datetime, timedelta
from pathlib import Path


def fetch_events(user, headers, since):
    url = f"https://api.github.com/users/{user}/events/public"
    events = []
    while url:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        page = r.json()
        events.extend(page)
        # stop if all events on this page are before our start
        if all(isoparse(ev["created_at"]) < since for ev in page):
            break
        url = r.links.get("next", {}).get("url")
    return events


def fetch_repo_details(repos, headers):
    """Fetch repository details including description, topics and README."""
    details = {}
    for repo in tqdm(set(repos), desc="Get repos"):
        try:
            info = requests.get(f"https://api.github.com/repos/{repo}", headers=headers).json()
            readme_resp = requests.get(
                f"https://api.github.com/repos/{repo}/readme", headers=headers
            ).json()
            details[repo] = {
                "description": info.get("description", ""),
                "topics": info.get("topics", []),
                "readme": base64.b64decode(readme_resp.get("content", "")).decode(
                    "utf-8", "ignore"
                ),
            }
        except Exception as e:
            tqdm.write(f"Error fetching {repo}: {e}")
    return details


def fetch_github_commits(user, since, until, headers, skip_repos):
    """Fetch and process GitHub commits for a user within a date range."""
    evs = fetch_events(user, headers, since)
    commits = []
    repos = set()

    for ev in tqdm(evs, desc="Get commits"):
        if ev["type"] != "PushEvent":
            continue
        ts = isoparse(ev["created_at"])
        if not (since <= ts < until):
            continue

        repo = ev["repo"]["name"]
        if repo in skip_repos:
            continue
        repos.add(repo)
        for c in ev["payload"]["commits"]:
            try:
                url = f"https://api.github.com/repos/{repo}/commits/{c['sha']}"
                r = requests.get(url, headers=headers)
                r.raise_for_status()
                cj = r.json()
            except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
                tqdm.write(str(e))
                continue
            commits.append(
                {
                    "repo": repo,
                    "sha": c["sha"],
                    "date": cj["commit"]["author"]["date"],
                    "message": cj["commit"]["message"],
                    "files": [
                        {
                            "filename": f["filename"],
                            "additions": f["additions"],
                            "deletions": f["deletions"],
                            "changes": f["changes"],
                            "patch": f.get("patch", ""),
                        }
                        for f in cj.get("files", [])
                    ],
                }
            )

    return commits, list(repos)


def get_commit_summary(system_prompt, commits_json, repo_context):
    context_json = json.dumps(repo_context, indent=2)
    payload = {
        "model": "gpt-4.1-mini",
        "input": [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"Repository Context:\n{context_json}\n\nCommits:\n{commits_json}",
            },
        ],
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
    }

    response = requests.post("https://api.openai.com/v1/responses", headers=headers, json=payload)
    response.raise_for_status()
    result = response.json()
    cost = result["usage"]["input_tokens"] * 0.4 + result["usage"]["output_tokens"] * 1.6
    return cost, result["output"][0]["content"][0]["text"]


def get_podcast(script, target, config):
    """Generate speech files for each line in the podcast script."""
    speakers = {k: v for k, v in config.items() if isinstance(v, dict) and "voice" in v}
    headers = {
        "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
        "Content-Type": "application/json",
    }

    lines = [ln.strip() for ln in script.splitlines() if ln.strip()]
    filenames = []
    for line in tqdm(lines, desc="Get speech"):
        # Skip lines without valid speaker
        speaker = next((s for s in speakers if line.startswith(f"{s}:")), None)
        if speaker is None:
            continue
        podcast_filename = target / f"{len(filenames) + 1:03d}.opus"
        filenames.append(podcast_filename)
        if podcast_filename.exists():
            continue
        text = line[len(speaker) + 1 :].strip()
        body = {
            "model": "gpt-4o-mini-tts",
            "input": text,
            "voice": speakers[speaker]["voice"],
            "instructions": speakers[speaker]["instructions"],
            "response_format": "opus",
        }
        r = requests.post("https://api.openai.com/v1/audio/speech", headers=headers, json=body)
        r.raise_for_status()
        with open(podcast_filename, "wb") as f:
            f.write(r.content)

    # Concatenate all audio files
    list_file = target / "list.txt"
    list_file.write_text("\n".join(f"file '{f.name}'" for f in filenames))
    # -safe 0 allows for absolute paths
    # -c:a libmp3lame uses the LAME MP3 encoder
    # -qscale:a 5 is about 96 kbps. Lower values have higher quality and size
    # -ar 44100 sets sample rate to 44.1 kHz (standard for podcasts)
    # -ac 1 downmix to mono to halve file size at no loss
    # -id3v2_version 3 sets ID3v2.3 tags for compatibility with most players
    concat = f"ffmpeg -y -f concat -i {list_file} -safe 0 -c:a libmp3lame -qscale:a 5 -ar 44100 -ac 1 -id3v2_version 3 {target / 'podcast.mp3'}"
    os.system(concat)
    # Upload to https://s-anand.net/files/codecast-yyyy-mm-dd.mp3
    upload = f"rsync -avzP {target / 'podcast.mp3'} sanand@s-anand.net:~/www/files/codecast-{target.name}.mp3"
    os.system(upload)
    list_file.unlink()


def main():
    token = os.environ.get("GITHUB_TOKEN")

    # Default end date is latest Sunday ON OR BEFORE today, UTC.
    # Commits are taken from the previous Sunday to the next Saturday, UTC.
    today = datetime.now(UTC)
    end = today.replace(hour=0, minute=0, second=0, microsecond=0)
    end = (end - timedelta(days=(end.weekday() + 1) % 7)).date().isoformat()

    p = argparse.ArgumentParser()
    p.add_argument("-u", "--user", required=True)
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

    week_dir = script_dir / args.end
    week_dir.mkdir(exist_ok=True)
    summary_filename = week_dir / "README.md"
    context_filename = week_dir / "context.json"
    podcast_filename = week_dir / "podcast.md"
    podcast_output = week_dir / "podcast.mp3"
    if not summary_filename.exists() or not podcast_filename.exists():
        headers = {"Authorization": f"Bearer {args.token}"} if args.token else {}
        if not context_filename.exists():
            commits, repos = fetch_github_commits(
                args.user, since, until, headers, skip_repos=config["skip-repos"]
            )
            context = fetch_repo_details(repos, headers)
            with open(context_filename, "w") as f:
                json.dump([commits, repos, context], f)
        else:
            with open(context_filename, "r") as f:
                (commits, repos, context) = json.load(f)
        input = json.dumps(commits, indent=2)
        if not summary_filename.exists():
            cost, summary = get_commit_summary(config["summary"], input, context)
            print(f"Summary: {cost / 1e4:,.1f}c")
            with open(summary_filename, "w") as f:
                f.write(summary)
        if not podcast_filename.exists():
            prompt = config["podcast"].replace("$WEEK", until.strftime("%d %b %Y"))
            cost, podcast = get_commit_summary(prompt, input, context)
            print(f"Podcast: {cost / 1e4:,.1f}c")
            with open(podcast_filename, "w") as f:
                f.write(podcast)
    if not podcast_output.exists():
        get_podcast(podcast_filename.read_text(), week_dir, config)


if __name__ == "__main__":
    main()
