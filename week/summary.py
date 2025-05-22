# Usage: uv run summary.py -u <user>
# Summarizes Github activity for a user from last Sunday till most recent Saturday

#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "jmespath",
#     "python-dateutil",
#     "requests",
#     "tqdm",
# ]
# ///
import argparse
import base64
import jmespath
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


def fetch_github_activity(user, since, until, headers, skip_repos, fields):
    """Fetch and process GitHub events for a user within a date range."""
    evs = fetch_events(user, headers, since)
    activity = []
    repos = set()

    for ev in tqdm(evs, desc="Get events"):
        ts = isoparse(ev["created_at"])
        if not (since <= ts < until):
            continue

        repo = ev["repo"]["name"]
        if repo in skip_repos:
            continue
        repos.add(repo)

        if ev["type"] in fields:
            info = {}
            for path in fields[ev["type"]]:
                val = jmespath.search(path, ev)
                info[path] = ", ".join(val) if isinstance(val, list) else val
            activity.append(info)

        if ev["type"] != "PushEvent":
            continue

        for c in ev["payload"]["commits"]:
            try:
                url = f"https://api.github.com/repos/{repo}/commits/{c['sha']}"
                r = requests.get(url, headers=headers)
                r.raise_for_status()
                cj = r.json()
            except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
                tqdm.write(str(e))
                continue
            activity.append(
                {
                    "type": "commit",
                    "repo.name": repo,
                    "created_at": cj["commit"]["author"]["date"],
                    "sha": c["sha"],
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

    return activity, list(repos)


def get_activity_summary(system_prompt, activity, repo_context):
    context_json = json.dumps(repo_context, indent=2)
    payload = {
        "model": "gpt-4.1-mini",
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
    podcast = target / f"podcast-{target.name}.mp3"
    concat = f"ffmpeg -y -f concat -i {list_file} -safe 0 -c:a libmp3lame -qscale:a 5 -ar 44100 -ac 1 -id3v2_version 3 {podcast}"
    os.system(concat)
    list_file.unlink()


def generate_podcast(weeks, script_dir):
    output_path = script_dir / "podcast.xml"
    base_url = "https://github.com/sanand0/sanand0/releases/download/main"
    title = "Anand's Weekly Codecast"
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
        .replace("$WEEK", until.strftime("%d %b %Y"))
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
    if not summary_filename.exists() or not podcast_filename.exists():
        headers = {"Authorization": f"Bearer {args.token}"} if args.token else {}
        if not context_filename.exists():
            activity, repos = fetch_github_activity(
                args.user,
                since,
                until,
                headers,
                skip_repos=config["skip-repos"],
                fields=config["github_fields"],
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
            prompt = update_prompt(config["podcast"], until, args)
            cost, podcast = get_activity_summary(prompt, input, context)
            print(f"Podcast: {cost / 1e4:,.1f}c")
            with open(podcast_filename, "w") as f:
                f.write(podcast)
    if not podcast_output.exists():
        get_podcast(podcast_filename.read_text(), week_dir, config)

    # Get all directories beginning with "20" only if it contains podcast script
    weeks = [
        d.name
        for d in script_dir.iterdir()
        if d.is_dir() and d.name.startswith("20") and (d / f"podcast-{d.name}.md").exists()
    ]
    generate_podcast(weeks, script_dir)


if __name__ == "__main__":
    main()
