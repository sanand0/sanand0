## A week of small, useful tools and tidy content—scrapers got sturdier and the site got smarter.

The big lesson: make scrapers reliable, and make bookmarklets easy to use. Small, tested tools give outsized value when they work across pages and browsers.

### [sanand0/tools](https://github.com/sanand0/tools)

_Practical web utilities and bookmarklets got real improvements—more reliable scraping, new tools, and cleaner UI for users and maintainers._

- **Copy Links bookmarklet (24 Jan 2026).** Added a drag-to-bookmarklet UI and page script to copy every URL and embedded asset as TSV ([93d7eec](https://github.com/sanand0/tools/commit/93d7eecc6ea5b615eeb8cece612e6d941e6d4603)). Files: [copylinks/index.html](https://github.com/sanand0/tools/blob/main/copylinks/index.html) and [copylinks/copylinks.js](https://github.com/sanand0/tools/blob/main/copylinks/copylinks.js). Takeaway: make data-export tools easy to drag-and-run for quick archiving. (Yes, you really needed another bookmarklet.)
- **Color Table Builder (22 Jan 2026).** Added an interactive tool to paste delimited tables and output colored, semantic HTML with copy-to-clipboard and unit tests ([09ad622](https://github.com/sanand0/tools/commit/09ad622f1bfb662a5203593836ef765b99839e8a)). Core files: [colortable/script.js](https://github.com/sanand0/tools/blob/main/colortable/script.js) and [colortable/index.html](https://github.com/sanand0/tools/blob/main/colortable/index.html). Takeaway: small data-transforms plus good defaults beat manual styling every time.
- **Gemini scraper: modular, safer, and thought-aware (20–24 Jan 2026).** Refactored the scraper into a testable module, standardized bookmarklet UI, added safe clipboard fallbacks, and auto-expanded collapsed “thoughts” before scraping ([4e753f5](https://github.com/sanand0/tools/commit/4e753f5bf3e0dcff9a4fef88fa3b0cf9c8a66ec2), [11de66e](https://github.com/sanand0/tools/commit/11de66ebce094a8a6315ef3e321f2cb31e3b16fb), [3e1c0b3](https://github.com/sanand0/tools/commit/3e1c0b3f9cdf72526e9cb064d7b8dac01d8c3d7c)). File: [geminiscraper/geminiscraper.js](https://github.com/sanand0/tools/blob/main/geminiscraper/geminiscraper.js). Takeaway: expand dynamic UI parts before scraping, then wait a beat—async scrapers must be patient.
- **Unicoder improvements: safer decoding and better code handling (20 Jan 2026).** Improved entity decoding for code blocks, rendered <hr> as markdown dashes, and avoided HTML injection in output ([42b83e7](https://github.com/sanand0/tools/commit/42b83e74ada0428d2bced18478e195e173240bdb), [50d6c4a](https://github.com/sanand0/tools/commit/50d6c4a46442db2730447dbc35355ba7b681e809)). Files: [unicoder/script.js](https://github.com/sanand0/tools/blob/main/unicoder/script.js) and tests. Takeaway: treat code differently than prose when converting formats.
- **Polish, ESM move, lint & UI standardization (18–24 Jan 2026).** Standardized page layouts, moved tools to ESM, adjusted lint order, and fixed small quoting/format issues to pass linters ([4e753f5](https://github.com/sanand0/tools/commit/4e753f5bf3e0dcff9a4fef88fa3b0cf9c8a66ec2), [3c5761b](https://github.com/sanand0/tools/commit/3c5761be6223c826dd5e43d4e4eb76617f37799e)). Example: [tools.js→tools.mjs rename in README](https://github.com/sanand0/tools/commit/3c5761be6223c826dd5e43d4e4eb76617f37799e). Takeaway: consistent modules and a lint pass reduce surprising runtime issues.

### [sanand0/blog](https://github.com/sanand0/blog)

_Content and assets moved toward a stable CDN and new posts landed, improving reliability and discoverability._

- **Migrate assets and add new posts (22 Jan 2026).** Moved images to the files CDN, added long-form notes and a Gemini image analysis post ([2ba4a6c](https://github.com/sanand0/blog/commit/2ba4a6cd272fc7bae970c9e4c7716a14af2ff2af)). Files include new posts and many updated image links. Takeaway: serve media from a consistent host to avoid broken embeds.
- **Gemini Scraper post and wrap-code notes (20 Jan 2026).** Added a post describing the Gemini conversation scraper and documented the frontmatter `classes: wrap-code` to wrap long code blocks ([2c99fbd](https://github.com/sanand0/blog/commit/2c99fbd1a3f62e01eb66e23287d306af58fa91c2)). Takeaway: document little CMS tricks; they save future confusion.
- **New content and housekeeping (19 Jan 2026).** Added essays (Baba Is You), travel updater, pre-mortem prompt fragments, and fixed many internal links and embeds for HTTPS ([8fc7895](https://github.com/sanand0/blog/commit/8fc7895f8d1ec4fd06f993384a3ccf5223e9e0cc), [ddbb187](https://github.com/sanand0/blog/commit/ddbb1872d618e0b08d6c3b833892699c0d97f4d3)). Files: [scripts/where.py](https://github.com/sanand0/blog/blob/main/scripts/where.py) and [pages/where.md](https://github.com/sanand0/blog/blob/main/pages/where.md). Takeaway: automate small content updates to avoid manual drift.
- **Travel updater: safer file checks (19 Jan 2026).** scripts/where.py now checks for Dropbox CSV presence before reading, avoiding crashes ([8810b91](https://github.com/sanand0/blog/commit/8810b918f7f5f986bd51adb7a0c39d55384f31af)). Takeaway: fail gracefully when external files are missing.

### [sanand0/chatgpt-to-markdown](https://github.com/sanand0/chatgpt-to-markdown)

_Exported chat metadata got richer so saved conversations link back to their origin._

- **Claude metadata & release prep (22 Jan 2026).** Add clickable Claude link and Updated timestamp in generated Markdown, adjust tests, and bump version to 1.12.0 ([7fcc32b](https://github.com/sanand0/chatgpt-to-markdown/commit/7fcc32b3c8f02721e66f4d3e13ea333943396497)). Files: [claude-to-markdown.js](https://github.com/sanand0/chatgpt-to-markdown/blob/main/claude-to-markdown.js) and tests. Takeaway: include direct links and updated dates for better provenance and re-use.

### [sanand0/til](https://github.com/sanand0/til)

_Class notes and course plans grew clearer, with a full TDS Jan 2026 curriculum draft and updated learning notes._

- **TDS curriculum and notes updates (18 Jan 2026).** Added prompt patterns, a full proposed course TOC, and many supporting notes for Tools in Data Science Jan 2026 ([658688b](https://github.com/sanand0/til/commit/658688b56f39926afb3e009802ecd4fa616f54e7)). File: [tds-jan-2026.md](https://github.com/sanand0/til/blob/live/tds-jan-2026.md) (live branch). Takeaway: explicit prompt patterns and owner names speed course handoffs.
- **TILs and repo trends refreshed (18 Jan 2026).** Added weekly TILs and refreshed trending repo lists used for teaching and demos ([658688b](https://github.com/sanand0/til/commit/658688b56f39926afb3e009802ecd4fa616f54e7)). Takeaway: keep a short, living log for material reuse and demos.

## Lessons

- Small tools that just work beat ambitious but flaky features. Users value reliability.
- Bookmarklets still win for ad-hoc scraping and portability. Make them drag-friendly and test clipboard fallbacks.
- Expand dynamic UI elements before scraping. Async content needs waits or polling.
- Treat code and prose differently when converting formats. Preserve literal tags in code blocks.
- Centralize assets on a CDN to avoid broken links and mixed-content issues.

## Suggestions

- Add a tiny CI job that runs the scraper modules in a headless browser. Catch async expansion regressions early.
- Add unit/integration tests for copylinks (simulate pages with assets). Ensure clipboard fallbacks work in CI.
- Run an accessibility contrast check on Color Table Builder outputs. Ship an "export accessible table" option.
- Record short asciinema or webm demos for each bookmarklet. Users copy faster from examples.
- Automate site build preview that runs setup.sh, including scripts/where.py, before pushing content changes.
