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
import requests
import json
import os
import base64
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


def fetch_github_commits(user, since, until, headers):
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
    return result['usage'], result["output"][0]["content"][0]["text"]


def main():
    token = os.environ.get("GITHUB_TOKEN")

    # Default start date is latest Sunday BEFORE today.
    # Commits are taken from the previous Sunday to the next Saturday, UTC.
    today = datetime.now(UTC)
    end = today.replace(hour=0, minute=0, second=0, microsecond=0)
    end = (end - timedelta(days=end.weekday() + 1)).date().isoformat()

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
    with open(script_dir / "prompt.md") as f:
        system_prompt = f.read().strip()

    summary_filename = script_dir / f"{args.end}.md"
    if not os.path.exists(summary_filename):
        headers = {"Authorization": f"Bearer {args.token}"} if args.token else {}
        commits, repos = fetch_github_commits(args.user, since, until, headers)
        context = fetch_repo_details(repos, headers)
        usage, summary = get_commit_summary(system_prompt, json.dumps(commits, indent=2), context)
        with open(summary_filename, "w") as f:
            f.write(summary)
        print("Usage", json.dumps(usage, indent=2))


if __name__ == "__main__":
    main()
