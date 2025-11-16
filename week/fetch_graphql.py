#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "httpx",
#     "tqdm",
#     "python-dateutil",
# ]
# ///
"""
Fetch GitHub commits using GraphQL API.
This approach works for historical data (beyond 30-day Events API limit).
"""
import argparse
import base64
import httpx
import json
import os
from datetime import datetime, timedelta
from dateutil.parser import isoparse
from dateutil.tz import UTC
from fnmatch import fnmatch
from pathlib import Path
from tqdm import tqdm


def http_request(method, url, **kwargs):
    """Make HTTP request with error body printing for debugging."""
    response = httpx.request(method, url, **kwargs)
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
              isPrivate
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
    """Fetch commits for a repository within a date range using REST API."""
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
        if r.status_code == 404:  # Repo not accessible
            break
        try:
            r.raise_for_status()
        except httpx.HTTPStatusError:
            tqdm.write(f"HTTP {r.status_code} error for {url}")
            tqdm.write(f"Response body: {r.text[:500]}")
            raise
        page = r.json()
        commits.extend(page)
        # Parse Link header for next URL
        link_header = r.headers.get("link", "")
        next_url = None
        for part in link_header.split(","):
            if 'rel="next"' in part:
                next_url = part.split(";")[0].strip().strip("<>")
                break
        url = next_url
        params = {}  # params are in the URL for subsequent pages
    return commits


def fetch_repo_details(repos, headers):
    """Fetch repository details including description, topics and README."""
    details = {}
    for repo in tqdm(set(repos), desc="Get repo details"):
        try:
            info = http_request("GET", f"https://api.github.com/repos/{repo}", headers=headers).json()
            readme_resp = http_request(
                "GET", f"https://api.github.com/repos/{repo}/readme", headers=headers
            ).json()
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
    keep_each = max_lines // 2
    start = lines[:keep_each]
    end = lines[-keep_each:]
    skipped = len(lines) - max_lines
    return "\n".join(start + [f"\n... [{skipped} lines truncated] ...\n"] + end)


def is_binary_patch(patch):
    """Check if patch contains binary/generated content."""
    if not patch or len(patch) < 200:
        return False
    if patch.count("AAAA") > 5 or patch.count("////") > 5:
        return True
    for line in patch.splitlines()[:10]:
        if len(line) > 500:
            return True
    return False


def summarize_files(files, skip_files, max_files=12, max_patch_lines=50):
    """Summarize file changes, limiting number of files and patch size."""
    if not files:
        return []

    def file_importance(f):
        name = f.get("filename", "")
        if any(name.endswith(ext) for ext in [".py", ".js", ".ts", ".go", ".rs", ".java", ".c", ".cpp"]):
            priority = 0
        elif any(name.endswith(ext) for ext in [".md", ".txt", ".rst"]):
            priority = 1
        elif any(name.endswith(ext) for ext in [".json", ".yaml", ".toml", ".xml"]):
            priority = 2
        else:
            priority = 3
        return (priority, -f.get("changes", 0))

    sorted_files = sorted(files, key=file_importance)

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
        result.append({
            "filename": f["filename"],
            "additions": f.get("additions", 0),
            "deletions": f.get("deletions", 0),
            "changes": f.get("changes", 0),
            "patch": patch,
        })

    if len(files) > max_files:
        remaining = files[max_files:]
        result.append({
            "filename": f"... and {len(remaining)} more files",
            "additions": sum(f.get("additions", 0) for f in remaining),
            "deletions": sum(f.get("deletions", 0) for f in remaining),
            "changes": sum(f.get("changes", 0) for f in remaining),
            "patch": "",
        })

    return result


def fetch_github_activity_graphql(user, since, until, headers, skip_repos, skip_files):
    """Fetch GitHub activity using GraphQL to discover repos, REST for commit details."""
    activity = []
    seen_commits = set()

    # Step 1: Use GraphQL to discover repos with contributions in date range
    print(f"Fetching contributed repos for {user} from {since.date()} to {until.date()}...")
    contributed_repos = fetch_contributed_repos(user, since, until, headers)

    # Filter out skipped repos
    repos = [repo for repo, count in contributed_repos if repo not in skip_repos]
    print(f"Found {len(repos)} repos with contributions (filtered from {len(contributed_repos)})")

    for repo, count in contributed_repos:
        if repo not in skip_repos:
            print(f"  {repo}: {count} commits")

    # Step 2: Fetch actual commits from each repo
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

            # Skip commits not by this user
            if author_login != user and committer_login != user:
                continue

            # Fetch full commit details
            try:
                url = f"https://api.github.com/repos/{repo}/commits/{sha}"
                r = http_request("GET", url, headers=headers)
                cj = r.json()
            except (httpx.HTTPStatusError, json.JSONDecodeError) as e:
                tqdm.write(f"Error fetching commit {sha}: {e}")
                continue

            activity.append({
                "type": "commit",
                "repo.name": repo,
                "created_at": cj["commit"]["author"]["date"],
                "sha": sha,
                "message": cj["commit"]["message"],
                "files": summarize_files(cj.get("files", []), skip_files),
            })

    return activity, repos


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN environment variable required")

    # Default end date is latest Sunday ON OR BEFORE today, UTC.
    today = datetime.now(UTC)
    end = today.replace(hour=0, minute=0, second=0, microsecond=0)
    end = (end - timedelta(days=(end.weekday() + 1) % 7)).date().isoformat()

    p = argparse.ArgumentParser(description="Fetch GitHub activity using GraphQL API")
    p.add_argument("-u", "--user", required=True, help="GitHub username")
    p.add_argument("-e", "--end", default=end, help="End date, excluded (default: latest Sunday)")
    p.add_argument("-s", "--start", help="Start date (default: end date - 7 days)")
    p.add_argument("-o", "--output", help="Output JSON file (default: {end}/context.json)")
    args = p.parse_args()

    # Parse dates
    until = isoparse(args.end)
    if until.tzinfo is None:
        until = until.replace(tzinfo=UTC)

    if args.start is None:
        since = until - timedelta(days=7)
    else:
        since = isoparse(args.start)
        if since.tzinfo is None:
            since = since.replace(tzinfo=UTC)

    # Load config
    script_dir = Path(__file__).parent
    import tomllib
    with open(script_dir / "config.toml", "rb") as f:
        config = tomllib.load(f)

    skip_repos = config.get("skip-repos", [])
    skip_files = config.get("skip-files", [])

    # Set up output path
    if args.output:
        output_path = Path(args.output)
    else:
        week_dir = script_dir / args.end
        week_dir.mkdir(exist_ok=True)
        output_path = week_dir / "context.json"

    headers = {"Authorization": f"Bearer {token}"}

    # Fetch activity
    activity, repos = fetch_github_activity_graphql(
        args.user, since, until, headers, skip_repos, skip_files
    )

    # Fetch repo details
    context = fetch_repo_details(repos, headers)

    # Save context
    with open(output_path, "w") as f:
        json.dump([activity, repos, context], f, indent=2)

    # Summary
    print(f"\nResults saved to {output_path}")
    print(f"  Total commits: {len(activity)}")
    print(f"  Total repos: {len(repos)}")
    print(f"  File size: {output_path.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
