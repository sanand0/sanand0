## Docs-to-Hugo, cleaner course UX, and lots of tiny fixes — a week of polishing infra and notes.

This week focused on migrating docs to a sturdier build, tightening navigation, and capturing recent learnings. The big lesson: automate repeatable site work, and treat docs like running code.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_Course site migration and navigation work that makes multi-term archives reliable and easy to navigate for students and instructors._ Yes, you really needed another theme toggle — and now it survives refreshes.

- **Full Docsify → Hugo migration:** Replaced Docsify with a scripted Hugo scaffold and GitHub Pages workflow so the course runs as a stable static site; see [8587bdc](https://github.com/sanand0/tools-in-data-science-public/commit/8587bdcf8afbbc5f6b2fbae94921e043bcc62ed8). Takeaway: automate the conversion to reduce manual drift and future maintenance.
- **Automated course detection & sidebar normalization:** Added regex-based course prefix detection, dynamic sidebar generation, and robust prev/next logic; see [168f698](https://github.com/sanand0/tools-in-data-science-public/commit/168f69827c121307c9b1186afc7c2f0b9b71fa7f) (templates + setup.sh). Takeaway: derive navigation from content, not hand edits.
- **Build pipeline & GitHub Pages CI:** New setup.sh to assemble a transient Hugo site and workflow to build/deploy `public/`; see [8587bdc](https://github.com/sanand0/tools-in-data-science-public/commit/8587bdcf8afbbc5f6b2fbae94921e043bcc62ed8) and [.github/workflows/deploy-pages.yml](https://github.com/sanand0/tools-in-data-science-public/commit/8587bdcf8afbbc5f6b2fbae94921e043bcc62ed8). (07 Feb 2026) Takeaway: keep build artifacts out of source and make deploys repeatable.
- **UX polish & theme toggle; active link highlighting:** Add persisted theme button, CSS, and JS to mark current sidebar link; see [168f698](https://github.com/sanand0/tools-in-data-science-public/commit/168f69827c121307c9b1186afc7c2f0b9b71fa7f) (menu-after.html, _custom.scss). (07 Feb 2026) Takeaway: small UX bits cut confusion for students navigating many course terms.
- **Content hygiene and schedule fixes:** Linting and doc cleanups across many pages; fixed exam URL and ROE date alignment ([1861048](https://github.com/sanand0/tools-in-data-science-public/commit/1861048eb2dea9c2d3998214ea7cd1e66ca34c22), 07 Feb 2026; [0b08f56](https://github.com/sanand0/tools-in-data-science-public/commit/0b08f56df5675ce10a5b84933eee0ec338ac3fc8), 06 Feb 2026; [bc2a0d4](https://github.com/sanand0/tools-in-data-science-public/commit/bc2a0d4366df94997552fe902f816c3aabe85fdf), 02 Feb 2026). Takeaway: keep public schedules and links canonical; small doc fixes avoid big student confusion.

### [sanand0/blog](https://github.com/sanand0/blog)

_New posts, clearer prompts, and provenance notes that make content reproducible and easier to search._ The blog got both essays and surgical edits. Minor vanity: yes, another take on AI pedagogy.

- **Migration write-up and migration artifacts:** Added a long-form post documenting the Docsify→Hugo migration and included the exact commits and fixes; see [abcf470](https://github.com/sanand0/blog/commit/abcf470fb5173edc073189c60e32592c4d6d1009) (post: migrating-tds-from-docsify-to-hugo.md). (07 Feb 2026) Takeaway: documenting migrations saves future rework and helps others copy your script.
- **New essays on AI and work:** Published “RIP, Data Engineers” and other commentary on how AI shifts roles; see [abcf470](https://github.com/sanand0/blog/commit/abcf470fb5173edc073189c60e32592c4d6d1009) (posts/rip-data-engineers.md). (07 Feb 2026) Takeaway: capture hypothesis and examples early — they make good debate fuel.
- **Career advice and visualization posts:** Added a practical career-advice page and an IMDb visualization about Indian TV; see [85c1677](https://github.com/sanand0/blog/commit/85c1677185dfdcb763f64e0d21ce7fd090e55ea4) (03–04 Feb 2026). Takeaway: short, actionable pages are high-ROI for readers.
- **Gemini OCR results and cleanup:** Added Gemini OCR benchmarking and cleaned several posts; see [db87a90](https://github.com/sanand0/blog/commit/db87a90b03e57b5da8534918842b7ba83bc76e77) (02 Feb 2026). Takeaway: publish benchmarks with examples and costs so others can reproduce.
- **Transcription prompt tightened:** Require speaker + timestamp paragraph format for call transcriptions; see [abcf470](https://github.com/sanand0/blog/commit/abcf470fb5173edc073189c60e32592c4d6d1009) (pages/prompts/transcribe-call-recording.md). (07 Feb 2026) Takeaway: small prompt rules save huge manual cleanup later.

### [sanand0/til](https://github.com/sanand0/til)

_Daily learning notes and project backlog additions to make ideas actionable and assign owners._ Notes grew into tasks, which is the real progress.

- **New Feb notes and project tasks:** Added Jan/Feb 2026 entries, owner-assigned app ideas, and project notes; see [bfd8a49](https://github.com/sanand0/til/commit/bfd8a49c81718a3fa914ee1a7f056e918e9aef7d) (llms.md, apps.md, til.md). (01 Feb 2026) Takeaway: pair ideas with owners to avoid perpetual note rot.
- **LLM tooling recipes captured:** HAR→automation, Qwen3-TTS setup, and executable Markdown ideas were recorded; see [bfd8a49](https://github.com/sanand0/til/commit/bfd8a49c81718a3fa914ee1a7f056e918e9aef7d). Takeaway: codify small reproducible workflows for future reuse.
- **Course instrumentation notes:** Documented Ask-AI button, sendBeacon usage, and score tracking for course experiments; see [bfd8a49](https://github.com/sanand0/til/commit/bfd8a49c81718a3fa914ee1a7f056e918e9aef7d). Takeaway: instrument first, analyze later.

### [sanand0/tools](https://github.com/sanand0/tools)

_A small UI tool improvement that makes table colorization flexible for rows or columns._ Yes, spreadsheets deserve good fashion choices.

- **Added coloring modes (rows/columns/table):** Implemented per-row and per-column color scales and UI controls; see [6aaea49](https://github.com/sanand0/tools/commit/6aaea4900353da3813c4f72ec76b77779bcbb242) (colortable/index.html, script.js). (02 Feb 2026) Takeaway: match UI options to user mental model (per-row or per-column).
- **Tests updated for new modes:** Expanded unit tests to cover the new coloring modes; see [6aaea49](https://github.com/sanand0/tools/commit/6aaea4900353da3813c4f72ec76b77779bcbb242) (colortable/colortable.test.js). Takeaway: update tests with features to avoid regressions.
- **Graceful input handling:** Disabled ranges when per-row/column auto-scaling applies, improving UX; see [6aaea49](https://github.com/sanand0/tools/commit/6aaea4900353da3813c4f72ec76b77779bcbb242). Takeaway: prefer predictable defaults and disable irrelevant controls.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_This repo had no code changes this week but remains a useful reference for LLM cost/quality trade-offs._

- **No commits this week:** Core pricing data unchanged. (No new commits) Takeaway: consider a small weekly script to refresh leaderboards automatically.

## Lessons

- Automate boring conversions. A scripted Docsify→Hugo pipeline removed manual steps and future friction.
- Treat docs like code. Templates, tests, and CI keep content reliable across terms.
- Capture small process rules early. Prompt rules, instrumentation, and owner assignments avoid long manual fixes.
- Small UX moves matter. Theme toggles and active link highlights drastically reduce navigation confusion.
- Publish reproducible artifacts. Posts that include commits and commands let others copy your work.

## Suggestions

- Run the new Hugo build locally and record a short before/after demo (asciinema). It proves the migration worked.
- Add a tiny smoke-test CI step that checks sidebar-nav sanity after setup.sh runs.
- Export a short “how to restore” note for the migration, with exact commands and expected outputs.
- For the course site, add link-level analytics for the Ask-AI button (server-side or beacon) to measure usage.
- For the blog, convert the long migration post into a checklist script (one-liner patch) so others can repeat it.