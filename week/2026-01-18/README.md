## A week of better archives, new tools, and clearer notes

This week focused on turning ephemeral conversations into reusable artifacts. The key lesson: capture first, refine later.

### [sanand0/talks](https://github.com/sanand0/talks)

_Turn workshops into durable, searchable pages so anyone can replay or reuse your material (yes, another workshop page, but this one is useful)._

- **Complete story page added:** Created a long-form talk page with styling and interactive bits. See the page commit [4067761](https://github.com/sanand0/talks/commit/4067761e1cbf16362541473886414717232b7c52) and the file [index.html](https://github.com/sanand0/talks/blob/main/2026-01-11-nptel-vibe-coding-workshop/index.html). This gives readers a single place to read and embed media. Takeaway: build a single canonical landing page for each talk. (11 Jan 2026)

- **Full transcript and supporting notes:** Added the workshop transcript, tools notes, and auxiliary pages. See [adeb8a4](https://github.com/sanand0/talks/commit/adeb8a4edef116cf8ff35cad06c870a4c9882737) and [transcript.md](https://github.com/sanand0/talks/blob/main/2026-01-11-nptel-vibe-coding-workshop/transcript.md). This makes quotes searchable and re-usable for posts or captions. Takeaway: always publish transcripts alongside recordings. (11 Jan 2026)

- **Chat, attendance, and video fixups:** Added chat export, attendance TSV, and swapped to the correct YouTube video. See [4dacece](https://github.com/sanand0/talks/commit/4dacececfa82d55b4ebfc3fc7bc57c9079644fc6), plus [chat.txt](https://github.com/sanand0/talks/blob/main/2026-01-11-nptel-vibe-coding-workshop/chat.txt) and [attendance.tsv](https://github.com/sanand0/talks/blob/main/2026-01-11-nptel-vibe-coding-workshop/attendance.tsv). This fixes embed reliability and surfaces live Q&A. Takeaway: sync media IDs, chat, and attendance for a trustworthy record. (12 Jan 2026)

### [sanand0/tools](https://github.com/sanand0/tools)

_Make ephemeral chat usable. The Gemini scraper turns transient conversations into editable Markdown._

- **New Gemini conversation exporter:** Added a console script to export Gemini conversations as Markdown with YAML frontmatter. See commit [434b37f](https://github.com/sanand0/tools/commit/434b37fe7d48c85911fde31965cc90fb5ae2c466) and file [geminiscraper/geminiscraper.js](https://github.com/sanand0/tools/blob/main/geminiscraper/geminiscraper.js). It preserves lists, code blocks, and "thinking" sections. Takeaway: copyable console scripts are a practical workaround when bookmarklets fail. (11 Jan 2026)

- **Polished UI for the script:** Added [geminiscraper/index.html](https://github.com/sanand0/tools/blob/main/geminiscraper/index.html) and a loader [geminiscraper/script.js](https://github.com/sanand0/tools/blob/main/geminiscraper/script.js) so users can read, highlight, and copy the script. See [434b37f](https://github.com/sanand0/tools/commit/434b37fe7d48c85911fde31965cc90fb5ae2c466). This lowers friction for non-developers. Takeaway: ship a tiny UX around paste-in-console workflows. (11 Jan 2026)

- **Catalog update:** Added the tool to the tools list and JSON manifest. See [tools.json](https://github.com/sanand0/tools/blob/main/tools.json) change in [434b37f](https://github.com/sanand0/tools/commit/434b37fe7d48c85911fde31965cc90fb5ae2c466). Visitors can now discover the scraper from the main site. Takeaway: update indexes when you add tools. (11 Jan 2026)

### [sanand0/til](https://github.com/sanand0/til)

_Notes grew more actionable this week. Small, frequent updates keep ideas usable later (yes, tidy notes beat messy brilliance)._

- **Many Jan 2026 notes added:** Expanded `til.md` with tax-residency guidance, AVIF notes, tooling tips, and more. See commit [b412a88](https://github.com/sanand0/til/commit/b412a8868abef9c20ae04e23e4fd488528b0ee61) and [til.md](https://github.com/sanand0/til/blob/main/til.md). These are practical reference points for future decisions. Takeaway: capture practical answers when you find them. (11 Jan 2026)

- **New app ideas and LLM notes:** Added `apps.md` TODOs and a `llms.md` entry about CLIProxyAPI (`router-for.me`). See [b412a88](https://github.com/sanand0/til/commit/b412a8868abef9c20ae04e23e4fd488528b0ee61) and [apps.md](https://github.com/sanand0/til/blob/main/apps.md). These notes include commands and measurables. Takeaway: jot concrete commands and metrics so ideas are runnable later. (11 Jan 2026)

- **Course and formatting tidy-ups:** Updated `tds-jan-2026.md` and cleaned dates and formatting. See [b412a88](https://github.com/sanand0/til/commit/b412a8868abef9c20ae04e23e4fd488528b0ee61). This reduces friction when publishing notes. Takeaway: small format fixes save time when you publish. (11 Jan 2026)

### [sanand0/tutorials](https://github.com/sanand0/tutorials)

_Refocused guides and added a short, practical tutorial on LLMFoundry keys (yes, secrets deserve a how-to)._

- **LLM Foundry API key guide:** Added step-by-step instructions to configure LLM Foundry API keys. See commit [18fd7c6](https://github.com/sanand0/tutorials/commit/18fd7c6f17a0a9109e467c493810f372ae6c5e84) and [llmfoundry-api-key/README.md](https://github.com/sanand0/tutorials/blob/main/llmfoundry-api-key/README.md). This helps apps that accept OpenAI-compatible keys connect to LLM Foundry. Takeaway: short config guides unlock more tooling for readers. (15 Jan 2026)

- **Migrated long-form content to the blog:** Shrunk large READMEs and added pointers to blog posts for mapscii and short-code. See [18fd7c6](https://github.com/sanand0/tutorials/commit/18fd7c6f17a0a9109e467c493810f372ae6c5e84). This keeps the repo focused and avoids duplication. Takeaway: keep code repos lean and put long essays on a blog. (15 Jan 2026)

- **Minor formatting and README updates:** Cleaned a few READMEs and added the new tutorial to the index. See [18fd7c6](https://github.com/sanand0/tutorials/commit/18fd7c6f17a0a9109e467c493810f372ae6c5e84). This improves discoverability. Takeaway: update your index when content moves. (15 Jan 2026)

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Stories backed by reproducible data win readers. This new investigation turns AI reviews into a tight narrative._

- **New investigative story published:** Added "Can AI Replace Human Paper Reviewers?" with a long-form interactive page. See commit [9f3539b](https://github.com/sanand0/datastories/commit/9f3539b6d4a572ced1efc19bde387eb554c9f5e0) and [index.html](https://github.com/sanand0/datastories/blob/main/ai-agents-for-science/index.html). The story explains patterns and oddities in AI reviews. Takeaway: pair narrative with data to make surprising findings stick. (13 Jan 2026)

- **Reproducible scraping and analysis toolbox:** Added `scrape.py` to fetch reviews from OpenReview, plus `prompts.md` documenting analysis prompts. See [9f3539b](https://github.com/sanand0/datastories/commit/9f3539b6d4a572ced1efc19bde387eb554c9f5e0) and [ai-agents-for-science/scrape.py](https://github.com/sanand0/datastories/blob/main/ai-agents-for-science/scrape.py). This makes the investigation reproducible. Takeaway: ship the data and the code together. (13 Jan 2026)

- **Site metadata and listing updated:** Added story entry to `config.json` and README so the site shows the new piece. See [9f3539b](https://github.com/sanand0/datastories/commit/9f3539b6d4a572ced1efc19bde387eb554c9f5e0) and [config.json](https://github.com/sanand0/datastories/blob/main/config.json). That helps discovery and archival. Takeaway: update manifests when you publish. (13 Jan 2026)

## Lessons

- Capture first, refine later. Raw transcripts and chats unlock reuse.
- Ship small UX around technical work. A copy-button matters.
- Make stories reproducible by shipping scraping code and data.
- Keep indexes and manifests in sync with content. Broken links waste trust.
- Move long essays to a blog to keep code repos tidy.

## Suggestions

- Add basic tests and CI for geminiscraper parsing across conversation variants.
- Add an accessibility-friendly transcript download (plain text and timestamps).
- Add a short privacy note and consent checklist for scraped chat data.
- Add a small script to auto-validate talk page media IDs and links before publishing.
- Publish a lightweight dataset README for the AI-review story explaining licensing and reuse.
