## Maps, radars, and smaller but useful tooling wins this week

A week of polishing interactive maps, shipping a Technology Radar, and tightening content and publishing plumbing. The big lesson: small UX and API safety fixes turn prototypes into repeatable tools.

### [sanand0/embedumap](https://github.com/sanand0/embedumap)

_Embedumap grew from a neat demo into a shareable, media-friendly map with LLM smarts, caching, and tidy UI controls._

- **Standalone CLI + renderer:** Implemented the CLI, packaged core pipeline, and added a standalone HTML renderer ([0f055e5](https://github.com/sanand0/embedumap/commit/0f055e5cf3978bfbd3c60a11dd5169f32954f439)) on 30 Mar 2026; this makes it trivial to run the tool from any machine. Takeaway: make the fast path obvious — a single command wins adoption.
- **Resumable cache, audio, and cluster naming:** Added a local DuckDB cache, audio-column support, and optional Gemini cluster names ([8d831ad](https://github.com/sanand0/embedumap/commit/8d831ad9b9492b8ea6cf956930f0b5c71ee9c786)) on 30 Mar 2026; embeddings reuse cuts API cost and adds audio-first maps. Takeaway: cache cheaply and locally; it pays many times over.
- **Shareable state & bar chart overlay:** Made filters, timeline, and bar chart bookmarkable and live-updating, plus one-line-per-modified-file output for reproducible builds ([5f3227c](https://github.com/sanand0/embedumap/commit/5f3227c8e68a8d62d99690727831f7d1f00350a0)) on 31 Mar 2026; share links preserve UI state. Takeaway: if users can bookmark it, they will.
- **Interactive timeline, brushing, and accessibility fixes:** Fixed timeline drag, brush visibility, keyboard focus outlines, and drag capture for smooth interactions ([bc99ea3](https://github.com/sanand0/embedumap/commit/bc99ea3bf0bf7751d957640e329e22ed3b3cd706) and [fdeebbb](https://github.com/sanand0/embedumap/commit/fdeebbb53b32d6dec5cc3aa560bc3a1aeba4b117)) on 31 Mar 2026; interactions now feel robust. Takeaway: small UX fixes reduce confusion fast. (Yes, the selection box really needed to appear.)
- **Axis interpretation via Gemini:** Ask Gemini to give human axis labels instead of “UMAP 1/2” and add CLI flags to opt out ([697fe2c](https://github.com/sanand0/embedumap/commit/697fe2cafe96854dc7fc515e8a080d0ee9d37e39)) on 31 Mar 2026; axes now communicate meaning to viewers. Takeaway: a good label beats a clever projection every time.

### [sanand0/tools](https://github.com/sanand0/tools)

_New tools and UI polish: a full Technology Radar, smarter radar UI, and a handy scroller bookmarklet._

- **Technology Radar app:** Added a full, production-ready radar app with data generation scripts and mock datasets ([0083944](https://github.com/sanand0/tools/commit/00839445cd84cfd6aa108cbfb28407ceeae27c12)) on 04 Apr 2026; ships with 100 and 2000 node mocks. Takeaway: useful demos scale when they include realistic test data.
- **Radar UI improvements:** Bootstrap multi-select tag dropdowns, tag-click filters, per-ring badges, legend row, and font-scale CSS variables ([7e072ba](https://github.com/sanand0/tools/commit/7e072ba8c28a202731c569aadffd2bbaf0e21efb)) on 04 Apr 2026; filters feel less clunky. Takeaway: small CSS and interaction tweaks improve discoverability dramatically.
- **Scroller bookmarklet with tests:** Added a polished scroller bookmarklet, preview page, minified bundle, and automated tests ([fc31c61](https://github.com/sanand0/tools/commit/fc31c61a1516d5255e735eb2ef7e1722ebc343df)) on 01 Apr 2026; drag-to-bookmark and preview make installation easy. Takeaway: users will install useful tiny tools if setup is frictionless. (Yes, another bookmarklet — but this one scrolls while you sip coffee.)
- **JSON→CSV nested support:** json2csv now flattens nested objects and expands arrays into rows ([1656664](https://github.com/sanand0/tools/commit/165666473a7ebc0551d91e2dd3940b4ae16d5696)) on 04 Apr 2026; better for real-world JSON. Takeaway: practical tools win when they tolerate messy inputs.

### [sanand0/blog](https://github.com/sanand0/blog)

_Small but important publishing improvements and new posts to make research easier to trace._

- **Add AI policies post & reclassify an advice item:** New post about AI policies across universities and a tiny reclassify in advice text ([e2bd658](https://github.com/sanand0/blog/commit/e2bd6581f99b1db1e39408246b8393b79059489c)) on 04 Apr 2026; research is now discoverable on the main blog. Takeaway: surface research where readers will find it.
- **Raw Markdown alternate link:** Emit <link rel="alternate" type="text/markdown"> headers pointing to raw GitHub markdown ([e831839](https://github.com/sanand0/blog/commit/e831839e9d1fdf2ea271390ebdad48013d118011)) on 03 Apr 2026; lets tools and readers fetch the source easily. Takeaway: make source access deliberate and automatable.
- **New posts & audio notes:** Added posts about ElevenLabs voice cloning and TDS reflections, with audio embeds and examples ([643ae18](https://github.com/sanand0/blog/commit/643ae18b00e3a3b956c86cb8aca1b9dd387a7da2)) on 29 Mar 2026; more real experiments published. Takeaway: publish experiments promptly while details stay fresh.

### [sanand0/datastories](https://github.com/sanand0/datastories)

    Big additions to the data story catalog and new research pages.

- **AI-policies data story:** Added a full story and the supporting JSON dataset covering AI policies of 25 universities ([1870b7d](https://github.com/sanand0/datastories/commit/1870b7d3dbc243b34370659a6565349b991e9994)) on 03 Apr 2026; includes index.html and prompts used. Takeaway: publish both narrative and raw data together for trust and reuse.
- **TDS Project 1 analysis and gallery:** Added the student project analysis, gallery, and thumbnails to share findings and image evals ([e0253a2](https://github.com/sanand0/datastories/commit/e0253a2decadcd54bb8f4f5877a196e2e2f72329)) on 03 Apr 2026; visual assets and interactive gallery included. Takeaway: show results, not just PDFs.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Podcast tooling and import/splitting robustness for WhatsApp group transcripts._

- **Podcast script updates:** New weekly podcast scripts and improved narration files ([05c8f0b](https://github.com/sanand0/generative-ai-group/commit/05c8f0bb45004f23e2b6a9b19f07744cf164986c)) on 29 Mar 2026; content reads like a polished digest. Takeaway: structure yields repeatable episodes.
- **Safer splitting + integrity checks:** Make message splitting idempotent, verify no messages are lost, and print only modified file paths ([533391f](https://github.com/sanand0/generative-ai-group/commit/533391f26e225fd1ce62273abf4ff6626329482a)) on 29 Mar 2026; prevents silent data loss. Takeaway: always verify automated merges — checks beat blind trust.
- **Better API error debugging:** Podcast TTS and script calls now print API error bodies to stderr for debugging ([533391f](https://github.com/sanand0/generative-ai-group/commit/533391f26e225fd1ce62273abf4ff6626329482a)) on 29 Mar 2026; makes failures actionable. Takeaway: surface the raw error early.

### [sanand0/llmartstyle](https://github.com/sanand0/llmartstyle)

_Map-focused style additions and per-category model control for image generation._

- **Map styles & per-category models:** Added a dedicated `map` category, several historical map prompts, and per-category model lists ([6e45260](https://github.com/sanand0/llmartstyle/commit/6e45260d45f90db410aa14a9b93b9ad130d43a08)) on 03 Apr 2026; generation now targets appropriate models per style. Takeaway: match model to task; one-size-fits-all wastes tokens.
- **Release-aware uploader:** Changed uploader to create one GitHub release per style and upload only allowed-model PNGs for that style ([6e45260](https://github.com/sanand0/llmartstyle/commit/6e45260d45f90db410aa14a9b93b9ad130d43a08)) on 03 Apr 2026; keeps releases manageable. Takeaway: design storage and release strategy before you generate thousands of images. (Yes, GitHub releases do have limits.)
- **Docs and README updates:** Notes on model selection, PNG→WEBP conversion, and generation commands updated in README. Takeaway: document the intended workflow, not just the commands.

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

_Scripted discovery prompts and curated demo entries._

- **Updated discovery prompts and config:** Added prompts to scan GitHub for new demo pages and extended config.json entries ([5f94276](https://github.com/sanand0/llmdemos/commit/5f94276fd1c22640a231cc2e5dbde340626333a7)) on 02 Apr 2026; automates demo discovery. Takeaway: make the vetting step explicit and repeatable.

### [sanand0/journalists](https://github.com/sanand0/journalists)

_Writing templates and brief for short-form flaps._

- **Add TOI flaps briefing and examples:** New flap prompts and multiple ready-to-publish flap drafts for current stories ([5737382](https://github.com/sanand0/journalists/commit/57373828a41a78d21c4f8bdffa59d2a177c99bfa)) on 01 Apr 2026; helps produce tight, evidence-backed copy quickly. Takeaway: a template plus proof points equals reliable short-form journalism.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Streamlined ELO updates and visualization tweaks._

- **Add update_elo.py CLI:** Big new script to apply TSV ELO updates, match models, and write elo.csv ([52fdffc](https://github.com/sanand0/llmpricing/commit/52fdffcd9abca411b7f0362e25d2664c1a847733)) on 01 Apr 2026; makes leaderboard updates simple. Takeaway: scripted updates keep data current and auditable.
- **Visualization improvements:** Ignore models lacking ELO scores and remove noisy tooltip fields ([52fdffc](https://github.com/sanand0/llmpricing/commit/52fdffcd9abca411b7f0362e25d2664c1a847733)) on 01 Apr 2026; chart tooltips are cleaner. Takeaway: simpler tooltips help readers focus on what's important.
- **ELO refresh and CSV bump:** Rewrote elo.csv with curated updates and bumped README guidance for running updates. Takeaway: keep the canonical data and the script in sync.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_New agent skills, image-gen fallbacks, and safer environment notes._

- **Imagegen skill + CLI fallback:** Added a full image-gen skill, a documented fallback CLI, samples, and Apache-2.0 license for assets ([3eb7857](https://github.com/sanand0/scripts/commit/3eb7857887228d5db7a527f330fe6f6e755b5561)) on 31 Mar 2026; ships safe defaults and guidance. Takeaway: give users a safe, documented escape hatch.
- **Plugin-creator skill:** Scaffolder and marketplace helper to create normalized plugin manifests and marketplace entries ([3eb7857](https://github.com/sanand0/scripts/commit/3eb7857887228d5db7a527f330fe6f6e755b5561)) on 31 Mar 2026; speeds plugin discovery and testing. Takeaway: make the boring scaffolding boringly correct.
- **Tooling & environment tweaks:** Added uv-uvx tips, model recommendations, and safer dev.sh volume defaults. Takeaway: document sensitive mounts and defaults to avoid accidental leaks.

### [sanand0/til](https://github.com/sanand0/til)

_Notes, trending repos, and fresh ideas recorded._

- **Add Mar notes and trending repos:** New dated notes, ideas, and 29 Mar 2026 trending repo list ([dd11b56](https://github.com/sanand0/til/commit/dd11b561fc374406db7e2847cdbab77809a8563f)) on 29 Mar 2026; keeps the idea backlog alive and searchable. Takeaway: capture ideas now; regret missing them later.

### [sanand0/uvx-static-assets-test](https://github.com/sanand0/uvx-static-assets-test)

_Minimal proof that uvx can run a package from GitHub and access packaged static assets._

- **Smallest uvx proof:** Simplified the repo to a tiny script that reads a packaged messages.txt, and documented findings ([b7ebc90](https://github.com/sanand0/uvx-static-assets-test/commit/b7ebc909216dac50ecafea66ebd3be2db28001c4)) on 30 Mar 2026; shows how to ship assets via data-files. Takeaway: small, explicit proofs are great for platform trust.

## Lessons

- Ship an obvious path. A single CLI command and a standalone HTML vastly reduce friction.
- Local caches near outputs are low-cost, high-benefit. Use them before adding complexity.
- Make state sharable. Bookmarkable URLs and minimal URL state reduce user setup time.
- Surface errors early. Printing raw API bodies saves many hours of debugging.
- Document fallback vs built-in paths clearly. Users and reviewers must know the difference.

## Suggestions

- Embedumap: add a small benchmark doc showing before/after caching, and a demo script to validate axis labels on very small and very skewed datasets.
- Tools: publish the Technology Radar as a release and add a short how-to for contributors to add nodes. Also ship the scroller bookmarklet as a release asset and add install instructions.
- Data stories & blog: link datasets from posts using the new raw-Markdown header, and add an automated check in CI to ensure sourcePath headers exist.
- Scripts/agents: add automated security checks for imagegen CLI network calls and a small integration test matrix for the plugin scaffolder.
- llmpricing: add unit tests for update_elo.py and schedule periodic runs (GitHub Action) to keep ELO and cost data fresh.
- General: add a short "what changed" changelog file per repo when making UI or data-schema changes. It helps downstream users upgrade safely.

If you want, I can:

- Draft a small README badge and quick demo command for embedumap.
- Create a GitHub Action skeleton to run update_elo.py weekly.
- Produce a one-page release note for the Technology Radar and scroller bookmarklet.
