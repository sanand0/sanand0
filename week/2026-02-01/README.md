## Notes, demos, course updates, and sturdier parsers — a week of tidy documentation and safer tooling.

Two themes: preserve knowledge, and make small tools behave predictably. Capturing ideas and adding tests pays back tenfold later.

### [sanand0/til](https://github.com/sanand0/til)

_This update preserves fresh ideas, course measurement tasks, and a dated snapshot of trending projects for later follow-up._ (Yes, another book list. It helps future you avoid the same search.)

- **Updated January notes:** Saved many new links and insights in `til.md`. See [1c5f245](https://github.com/sanand0/til/commit/1c5f24540757615e8d97fd20d677ebe88ece7928) and the file [til.md](https://github.com/sanand0/til/blob/main/til.md). Why it matters: you won’t lose references and can follow threads later. Takeaway: a small, dated log beats lost browser tabs. (25 Jan 2026)
- **New app ideas and tidy checklist:** Added and cleaned app ideas in `apps.md`. See [1c5f245](https://github.com/sanand0/til/commit/1c5f24540757615e8d97fd20d677ebe88ece7928) and [apps.md](https://github.com/sanand0/til/blob/main/apps.md). Why it matters: clearer tasks speed future prototyping. Takeaway: mark things done to reduce scanning friction. (25 Jan 2026)
- **Course instrumentation notes:** Added an Instrumentation checklist in `tds-jan-2026.md`. See [1c5f245](https://github.com/sanand0/til/commit/1c5f24540757615e8d97fd20d677ebe88ece7928) and [tds-jan-2026.md](https://github.com/sanand0/til/blob/main/tds-jan-2026.md). Why it matters: measuring “Ask AI” clicks enables evidence-driven teaching. Takeaway: instrument before you optimize. (25 Jan 2026)
- **Trending snapshot:** Recorded the 2026-01-25 trending list in `trending-repos.tsv`. See [1c5f245](https://github.com/sanand0/til/commit/1c5f24540757615e8d97fd20d677ebe88ece7928) and [trending-repos.tsv](https://github.com/sanand0/til/blob/main/trending-repos.tsv). Why it matters: preserves a date-stamped ecosystem view. Takeaway: snapshots make future trend analysis possible. (25 Jan 2026)

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_The course site got a Jan 2026 refresh, clearer navigation, and a linked grading document for students._ (No, the AI won't grade you — but the docs will help you pass.)

- **Course README refreshed:** Rewrote the top-level README to reflect Jan 2026 course framing. See [51117d9](https://github.com/sanand0/tools-in-data-science-public/commit/51117d90b35342a68e83700951e26635e221ed71) and [README.md](https://github.com/sanand0/tools-in-data-science-public/blob/main/README.md). Why it matters: clearer goals and expectations improve student outcomes. Takeaway: lead with why before how. (25 Jan 2026)
- **Added full Sep 2025 term materials:** Added a 2025-09 content folder and sidebar entries. See [51117d9](https://github.com/sanand0/tools-in-data-science-public/commit/51117d90b35342a68e83700951e26635e221ed71) and [2025-09/README.md](https://github.com/sanand0/tools-in-data-science-public/blob/main/2025-09/README.md). Why it matters: makes prior term content discoverable. Takeaway: keep archives navigable. (25 Jan 2026)
- **Linked grading document:** Exposed the Jan 2026 grading doc in the README. See [4df9e20](https://github.com/sanand0/tools-in-data-science-public/commit/4df9e20e9eac70203dae8304d5dc19d2fa579956) and the [Grading Document link](https://github.com/sanand0/tools-in-data-science-public/blob/main/README.md). Why it matters: students get transparent grading rules. Takeaway: public grading reduces confusion and appeals. (28 Jan 2026)

### [sanand0/slidecompress](https://github.com/sanand0/slidecompress)

_The compressor is more robust now, and failures no longer crash the run._ (PPTs hide giant images like squirrels hoard nuts.)

- **Handle compression failures:** Added error handling and pass-through size tracking in `slidecompress.py`. See [1cc06bb](https://github.com/sanand0/slidecompress/commit/1cc06bb032f97bbdaed20f64c613acd416ede935) and [slidecompress.py](https://github.com/sanand0/slidecompress/blob/main/slidecompress.py). Why it matters: the tool reports errors and continues instead of aborting. Takeaway: fail-safe handling saves time on large batches. (29 Jan 2026)
- **Consistent KB reporting:** Normalized size printing to kilobytes for clearer output. See [1cc06bb](https://github.com/sanand0/slidecompress/commit/1cc06bb032f97bbdaed20f64c613acd416ede935) and [slidecompress.py](https://github.com/sanand0/slidecompress/blob/main/slidecompress.py). Why it matters: easier to read compression summaries at a glance. Takeaway: consistent units reduce cognitive friction. (29 Jan 2026)

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

The demo index grew with several interactive projects and fixed a broken SVG demo URL. (Yes, you needed more demos. Browsers love variety.)

- **Added new demos:** Inserted many new demos into `config.json`. See [6324865](https://github.com/sanand0/llmdemos/commit/6324865713397db74ffec7b7280020d7d5a130d1) and [config.json](https://github.com/sanand0/llmdemos/blob/main/config.json). Why it matters: gives visitors fresh, real-world LLM examples to explore. Takeaway: curated demos speed learning and inspiration. (27 Jan 2026)
- **Fixed demo URL:** Corrected the SVG Animator URL. See [6324865](https://github.com/sanand0/llmdemos/commit/6324865713397db74ffec7b7280020d7d5a130d1) and the changed line in [config.json](https://github.com/sanand0/llmdemos/blob/main/config.json). Why it matters: fewer 404s and smoother demos. Takeaway: small link fixes improve first impressions. (27 Jan 2026)

### [sanand0/tools](https://github.com/sanand0/tools)

_The Gemini scraping parser now treats tables and blocks correctly and adds tests to lock behavior._ (Finally, tables stop eating footers.)

- **Convert HTML tables to Markdown:** `geminiscraper.js` now turns <table> into Markdown tables. See [93a7166](https://github.com/sanand0/tools/commit/93a71663b20c17b331d8b7a805dd9d75adcf226c) and [geminiscraper/geminiscraper.js](https://github.com/sanand0/tools/blob/main/geminiscraper/geminiscraper.js). Why it matters: exported notes keep readable tables instead of broken blobs. Takeaway: preserve structure when scraping. (27 Jan 2026)
- **Block detection and whitespace fixes:** Added block detection, heading handling, and trimmed trailing spaces in the parser. See [93a7166](https://github.com/sanand0/tools/commit/93a71663b20c17b331d8b7a805dd9d75adcf226c) and [geminiscraper/geminiscraper.js](https://github.com/sanand0/tools/blob/main/geminiscraper/geminiscraper.js). Why it matters: keeps logical separation between elements. Takeaway: clear blocks make downstream processing reliable. (27 Jan 2026)
- **User text normalization:** Normalized multi-paragraph user input into predictable Markdown. See [93a7166](https://github.com/sanand0/tools/commit/93a71663b20c17b331d8b7a805dd9d75adcf226c) and [geminiscraper/geminiscraper.js](https://github.com/sanand0/tools/blob/main/geminiscraper/geminiscraper.js). Why it matters: reduces noise when feeding scraped text to LLMs. Takeaway: canonical input beats ad-hoc fixes later. (27 Jan 2026)
- **Tests and fixtures added:** New unit tests and HTML fixtures lock table and paragraph behavior. See [93a7166](https://github.com/sanand0/tools/commit/93a71663b20c17b331d8b7a805dd9d75adcf226c), [geminiscraper.test.js](https://github.com/sanand0/tools/blob/main/geminiscraper/geminiscraper.test.js), and fixtures. Why it matters: prevents regressions and documents expected outputs. Takeaway: tests are the cheapest long-term bug insurance. (27 Jan 2026)

## Lessons

- Capture ideas immediately. A dated note beats memory and browser chaos.
- Instrument usage before optimization. Metrics reveal where to focus.
- Small UX fixes (links, units, whitespace) multiply in value over time.
- Make scrapers preserve structure, not just text. It helps downstream tasks.
- Add tests while behavior is fresh. Tests save future debugging time.

## Suggestions

- For til: convert high-value note links into TODO issues for follow-up experiments.
- For the course repo: publish a short changelog for students summarizing grading changes.
- For slidecompress: add an optional verbose/log file for batch runs to review failures later.
- For llmdemos: add thumbnails and a short tag filter to help users find relevant demos.
- For geminiscraper: add an edge-case fixture for nested tables and for tables with colspan.
- Across repos: add lightweight CI checks that run the new geminiscraper tests and verify README links.
