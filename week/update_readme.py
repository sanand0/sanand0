#!/usr/bin/env python3
"""Update README.md with recent activity from week/ summaries."""
from pathlib import Path
from datetime import datetime

root = Path(__file__).parent.parent
weeks = sorted(
    [d for d in (root / "week").iterdir() if d.is_dir() and d.name.startswith("20")],
    key=lambda d: d.name,
    reverse=True,
)

lines = []
for week in weeks:
    readme = week / "README.md"
    if not readme.exists():
        continue
    title = readme.read_text().split("\n")[0].lstrip("# ").strip()
    date = datetime.strptime(week.name, "%Y-%m-%d").strftime("%d %b %Y")
    podcast = f"https://github.com/sanand0/sanand0/releases/download/main/podcast-{week.name}.mp3"
    lines.append(f"- [{date}](week/{week.name}/): {title} [🎙️ Podcast]({podcast})")

content = root / "README.md"
text = content.read_text()
start, end = "<!-- ACTIVITY START -->", "<!-- ACTIVITY END -->"
if start in text and end in text:
    before = text[: text.index(start) + len(start)]
    after = text[text.index(end) :]
    content.write_text(before + "\n" + "\n".join(lines) + "\n" + after)
    print(f"Updated {len(lines)} entries")
else:
    print(f"Add {start} and {end} markers to README.md")
