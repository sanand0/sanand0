# Generate Weekly Summaries

This script generates AI summaries of your GitHub activity by analyzing commits between two dates (defaulting to the most recent Sunday-to-Saturday period). It creates both a written summary and an AI-generated podcast.

[Podcast](https://github.com/sanand0/sanand0/releases/download/main/podcast.xml)

## Setup Requirements

1. [uv](https://github.com/astral-sh/uv) for Python package management: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. [ffmpeg](https://ffmpeg.org/) for audio processing: `sudo apt install ffmpeg` (Ubuntu/Debian)

Add these environment variables to `.env` at the root of this repo:

```bash
GITHUB_TOKEN=...    # To read GitHub repo. https://github.com/settings/tokens
OPENAI_API_KEY=...  # To generate summary. https://platform.openai.com/api-keys
GEMINI_API_KEY=...  # To generate podcast. https://aistudio.google.com/api-keys
```

## Usage

Basic usage:

```bash
uv run summary.py -u <github-username> -n <name>
```

Options:

- `-u, --user`: GitHub username (required)
- `-n, --name`: Name to address by (required)
- `-e, --end`: End date in YYYY-MM-DD format (default: most recent Sunday)
- `-s, --start`: Start date in YYYY-MM-DD format (default: end date - 7 days)
- `-t, --token`: GitHub token (default: $GITHUB_TOKEN)

Examples:

```bash
# Get last week's summary. Generates from previous Sunday till latest Saturday EOD, UTC
uv run summary.py -u sanand0 -n "Anand"

# Get specific date range, UTC
uv run summary.py -u sanand0 -n "Anand" -s 2024-01-01 -e 2024-01-07
```

## Generated Files

For each run, the script creates a directory named after the end date (e.g., `2025-05-04/`) containing:

- `${week}/README.md`: Written summary of GitHub activity
- `${week}/podcast.md`: Script for the podcast
- `${week}/*.opus`: Individual audio files for each line in the podcast. Not committed
- `${week}/podcast.mp3`: Final concatenated podcast. Not committed, uploaded to GitHub releases

When re-running, only missing files are re-generated.
This allows for incremental updates and prevents unnecessary API calls when files already exist.

The files are released on GitHub releases at <https://github.com/sanand0/sanand0/releases/tag/main> created via:

```bash
gh release create main --title "Codecast" --notes "Auto-generated podcast"
```

To upload all, run:

```bash
npx -y pretty-quick
gh release upload main --clobber */podcast-*.mp3
gh release upload main --clobber podcast.xml
```

Or to upload a single release:

```bash
npx -y pretty-quick
WEEK=... gh release upload main $WEEK/podcast-$WEEK.mp3
gh release upload main --clobber podcast.xml
```

Update [../README.md](../README.md):

```bash
uv run update_readme.py
```

This updates the `<!-- ACTIVITY START -->` to `<!-- ACTIVITY END -->` section in `README.md` with all weekly summaries.
