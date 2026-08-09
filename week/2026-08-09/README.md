## A week of polishing agent tooling, live apps, and prompt craft — make agents useful, observable, and reviewable.

Small wins across many repos made agent workflows safer and easier to inspect. The main lesson: instrument early, test the user surface, and prefer small predictable contracts over magic.

### [sanand0/blog](https://github.com/sanand0/blog)

_Updated posts, tighter skills, and faster LinkedIn mapping make writing and reuse less fragile and easier to automate._

- **New long-form posts.** Added AI workflow stories like "AI tax returns 2026" and "MCP vs Shell" to the site ([3df517a](https://github.com/sanand0/blog/commit/3df517a6e862a3636ab174912096241a18105982), 04 Aug 2026; [4d5ccd1](https://github.com/sanand0/blog/commit/4d5ccd1a6d4e855321c804325bd03bff3f3d8908), 08 Aug 2026). They document practical agent+expert flows and experiments. Takeaway: publish the whole workflow so readers can reuse the pattern.

- **Refined prompt fragments & skills.** Tightened many SKILL.md and prompt fragments for clearer, smaller guidance ([c465a78](https://github.com/sanand0/blog/commit/c465a78b220c4da650c5dd902810338ac888445b), 08 Aug 2026; [b1d3406](https://github.com/sanand0/blog/commit/b1d340609c1014eda02acb239f78a9463b160ce9), 03 Aug 2026). This reduces noise in agent prompts. Takeaway: smaller, precise skills scale better.

- **Faster, reviewable LinkedIn→blog mapper.** Made the mapper use overrides, strip HTML before scoring, and add an overrides TSV for manual review ([8b34b73](https://github.com/sanand0/blog/commit/8b34b731360b2f526a7db36195b59e6ade6aa3cc), 02 Aug 2026). It prints review rows and preserves decisions. Takeaway: automate tactically, and keep a small human-review bucket.

- **Front-matter hygiene and metadata fixes.** Added tags, metadata, and linked posts to LinkedIn where helpful (multiple edits across Aug 2–8). These make discovery and reuse easier. Takeaway: small metadata fixes compound into better search and reuse.

(Yes, another post about agents — you needed that.)

### [sanand0/scripts](https://github.com/sanand0/scripts)

.Stronger MCP server observability, tool schemas, and agent-friendly CLI tweaks make safe agent tooling practical.

- **Large mcpserver refactor and tool logging.** Reworked mcpserver.py to return structured results, log events compactly, and persist per-call logs; tests updated accordingly ([3b9f687](https://github.com/sanand0/scripts/commit/3b9f68724d209adf5653481f820d285d7f1b2c56), 04 Aug 2026; [43c5a91](https://github.com/sanand0/scripts/commit/43c5a910dfeb8fe7586ee43d3100c5b287505e42), 04 Aug 2026). This improves auditability for agent runs. Takeaway: structured logs let agents and humans verify behavior later.

- **Log all tools and fix ChatGPT compatibility.** Added openai/fileParams, annotations, and richer schemas for save_file/download_file and bash tools ([43c5a91], 04 Aug 2026). Tests now assert tool shapes. Takeaway: explicit tool contracts reduce surprising failures.

- **Install and runtime updates.** Add opencode and correct Codex package installs in setup docs ([90c6a8e](https://github.com/sanand0/scripts/commit/90c6a8ec74d029ea42d56ea67e90fec4a2040b4f), 06 Aug 2026; [1fccdd8](https://github.com/sanand0/scripts/commit/1fccdd8c0b9d6ebb8270c140579043fe0427e27d), 02 Aug 2026). These keep local agent tooling current. Takeaway: pin the right runtimes to avoid "it works on my machine" surprises.

- **Observability & dev docs for model upgrades.** Added long guidance for safe model migrations and prompting practices for new GPT families ([1fccdd8…], 02 Aug 2026). Takeaway: upgrade with small experiments and explicit validation checks.

- **Small UX/ops tweaks.** GPU ffmpeg alias, devtools skill favoring API replay over DOM scraping, and agent-friendly CLI notes improve day-to-day use ([e5c715c](https://github.com/sanand0/scripts/commit/e5c715cd5a97524585c9fc5c295ddcc6e9dee8ff), 02 Aug 2026; [272e814](https://github.com/sanand0/scripts/commit/272e8147f29f33249a01370e4b5a1f7d69941754), 04 Aug 2026). Takeaway: prefer server APIs over brittle DOM scraping.

(One more MCP tweak — because logs are cheaper than guesswork.)

### [sanand0/tools](https://github.com/sanand0/tools)

_New UI niceties, a big multi-user grid, and polish for slide editing improve live tools._

- **LiveGrid: a live multi-user prioritization grid.** Added a Firestore-backed LiveGrid app with import, share, QR, and offline behavior ([15b6f6e](https://github.com/sanand0/tools/commit/15b6f6eb76eed9cea55bdd26b939032b4a6359fb), 04 Aug 2026). It syncs rooms by UUID and supports import. Takeaway: small static apps can give big synchronous value with Firestore.

- **Slide editor: include subtitle in window title and modal improvements.** Made document.title include text-extracted subtitle, normalize markdown, and close modal on Escape ([7ea9a4a](https://github.com/sanand0/tools/commit/7ea9a4af0c576718b8ca548669ed34a50d78542f), 07 Aug 2026). Tests added. Takeaway: show key context where it’s visible — the window title is an easy win.

- **WhatNext modernized and drag bug fixed.** Simplified DOM helpers, fixed hash handling and drag placement, and tightened UX copy ([f0507dd](https://github.com/sanand0/tools/commit/f0507ddb100f1cd6801b72c330d6fad435663a2d), 04 Aug 2026). Takeaway: small DOM fixes remove large, confusing cursor offsets.

- **Styling and accessibility polish.** Improved slide body styles and favicon behavior for previews ([a6cba0f](https://github.com/sanand0/tools/commit/a6cba0f1ab75e60198930ff9e9bfcb7b597970f0), 04 Aug 2026). Takeaway: good defaults reduce follow-up fixes.

(Live grids: because "what next" needs to be shared, fast.)

### [sanand0/llmartstyle](https://github.com/sanand0/llmartstyle)

_Reordered and expanded art-style prompts to surface the most liked styles first._

- **Re-ordered comic styles to surface favorites first.** Moved preferred styles up for quicker access in the generator ([04b5b4d](https://github.com/sanand0/llmartstyle/commit/04b5b4d1157f193daf716a8b8c3e110a07e3c185), 08 Aug 2026). Takeaway: ordering matters when discovery is manual.

- **Added rich black-and-white comic styles.** Added many engraving, stipple, and horror line styles for B/W outputs ([6b52049](https://github.com/sanand0/llmartstyle/commit/6b52049a087b1cd35f38060db274da4dab637ed1), 08 Aug 2026). Takeaway: explicit style prompts reduce trial-and-error.

(Yes, another art style list. Your feed will thank you.)

### [sanand0/liveform](https://github.com/sanand0/liveform)

.Live survey UX, embedding configuration, and editable answers make workshops smoother.

- **Allow editing of survey answers.** Forms now render update flows and the backend honors an editable flag ([40da566](https://github.com/sanand0/liveform/commit/40da566160657bce688fb353009b1ee749bf2e94), 07 Aug 2026). Tests cover submit/update flows. Takeaway: let users fix submissions; audit trails keep results reliable.

- **Load .env and theme toggle for results.** CLI now reads .env (without overriding env), and results pages gained a light/dark toggle ([261dfed](https://github.com/sanand0/liveform/commit/261dfedb7215df4692e8c785987367c23426dc2b), 07 Aug 2026). Tests ensure dotenv and credential precedence. Takeaway: local .env lets safe testing and reproducible runs.

- **Embedding provider selection and warnings.** Results code picks Gemini first, then OpenAI, and warns when keys are missing ([261dfed], 07 Aug 2026). Tests check graceful degradation when embeddings are disabled. Takeaway: prefer stable providers but fail loud and safe if creds are missing.

- **Results UI improvements (brush, strokes, accessibility).** Map brushing, thin strokes, and pause behavior improve exploratory visuals and keyboard control (tests and CSS updates). Takeaway: small UX affordances make data exploration sane.

(Editable answers because humans make better decisions with a second try.)

### [sanand0/talks](https://github.com/sanand0/talks)

_New talks and workshop artifacts added, including transcripts and a Data Hack Summit page._

- **Added Data Hack Summit talk page and assets.** Uploaded transcript, prompts, HTML page, audio, and a comic page for the 07 Aug 2026 talk ([796e159](https://github.com/sanand0/talks/commit/796e15970e753cbe50d419c1720dc67dd4b49a32), 07 Aug 2026). Takeaway: publish full resources so others can reuse slides, transcripts, and comic explainers.

- **AI Unboxed workshop material added.** Large set of chat logs, transcripts, and saved bundles for the 25 Jul 2026 workshop were added ([86d2d2f](https://github.com/sanand0/talks/commit/86d2d2fbabdafd2b468dd22629dcea8a0dc57cfe), 03 Aug 2026). Takeaway: keep raw chat logs and artifacts for reproducible talk prep.

(If a talk falls in the forest and no code is published, did it happen? Not here.)

### [sanand0/til](https://github.com/sanand0/til)

_Weekly notes and curated learnings capture fast-moving tool updates and practical takes._

- **Updated TIL and LLMS notes.** Added Aug notes on transcription pricing, ruff rules, video codecs, and benchmarks ([2f59c41](https://github.com/sanand0/til/commit/2f59c4190e62a113df484c5e101ea29daeccf6e6), 03 Aug 2026). Takeaway: tiny notes help you remember why you tried something.

- **Expanded references and citations.** Linked practical posts and tools for easier follow-up. Takeaway: keep links near the insight so next steps are obvious.

(Yes, another list of curiosities. You’ll read one and then try a tool.)

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Podcast episode updates keep the weekly digest current and easier to republish._

- **Updated podcast episode content.** Added the 02 Aug 2026 digest transcript and show notes for the Generative AI Group ([adbcaa7](https://github.com/sanand0/generative-ai-group/commit/adbcaa7d794834da89dbde8af80d71abaff2152f), 02 Aug 2026). Takeaway: keep audio+show notes synced.

(Yes, the world needs another useful weekly summary.)

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Model frontier data refreshed so pricing and ELO charts stay current._

- **Leaderboard and models updated.** Bumped last-updated date and refreshed elo.csv with current model entries ([d13082d](https://github.com/sanand0/llmpricing/commit/d13082dd54cad998ef230d358d80fb730a6d7b60), 02 Aug 2026). Takeaway: refresh data often to keep cost-vs-quality choices actionable.

(Yes, the frontier keeps moving. Refresh the graph and breathe.)

## Lessons

- Instrument before you trust. Structured logs and small per-call artifacts make debugging simple.
- Small UX fixes multiply. Tiny title, modal, or stroke changes improve real user flow.
- Prefer explicit contracts for tools. Tool schemas and annotations prevent silent failures.
- Fail visibly for missing credentials. Warn loudly, degrade gracefully.
- Publish the whole workflow. Data, chats, tests, and prompts make results reproducible.

## Suggestions

- Add a small audit dashboard for mcpserver events. Include recent sessions, errors, and save_file/download_file metadata.
- Run a short user test for LiveGrid and slide title UX with 3 non-technical participants. Watch where they click first.
- Add a compact migration checklist for model upgrades in scripts and blog repos. Automate the “run representative evals” step.
- In liveform, add a per-form revision log for edited answers to ease audit trails.
- For llmpricing, schedule an automated weekly scrape and snapshot commit to keep the frontier chart fresh.

If you want, I can draft the mcpserver dashboard mockup or a short checklist for model upgrades next.