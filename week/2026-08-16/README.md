## A week of tidy tooling, fresher models, and sharper publications

Small, practical upgrades across scripts, tests, and content made agent workflows safer and more repeatable. The big lesson: invest in small developer UX and test isolation; they compound into fewer surprises.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Cleaner CLIs, safer scrapers, and a few infra upgrades that make daily automation quieter and less surprising (yes, you really needed another prompt picker)._

- **Prompt picker rewritten in Python.** Replaced the long Bash picker with a tested Python CLI (`prompt`) and new tests ([cced8f3](https://github.com/sanand0/scripts/commit/cced8f3e300a807b398d68299c575daf65253095)). This removes fragile shell parsing and makes fuzzy-filtering pipeline-friendly. (15 Aug 2026) Takeaway: prefer readable, testable CLIs over fragile shell one-liners.
- **Archived dead code and moved helpers to single scripts.** Archived unused functions and moved the old Vite pages helper into a standalone `pages` script ([2e5053f](https://github.com/sanand0/scripts/commit/2e5053fb1a6dbd257ad351e4bdda8edd9eb6a6e2)). This shrinks setup.fish and isolates the implementation. (15 Aug 2026) Takeaway: archive, don't hoard; it speeds maintenance.
- **Run-once scheduler with desktop notifications.** Added `run-at` with systemd timers and `notify-send` notifications on completion/failure ([eb02544](https://github.com/sanand0/scripts/commit/eb0254405382f298250f4b39963468680dd24244), [cddf986](https://github.com/sanand0/scripts/commit/cddf986bac1a06f88c3e05a393c9525cb2073108)). Tests cover scheduling, clearing, and notifications. (11 Aug 2026) Takeaway: small UX feedback (desktop notify) saves you from opening logs.
- **Backups & scrapers tightened.** Large maintenance pass for LinkedIn and WhatsApp scrapers fixed CDP handling, resource cleanup, and error messages ([c45c7aa](https://github.com/sanand0/scripts/commit/c45c7aa33ab12e418c8052272b9f7ed683b4b74a), [d73e423](https://github.com/sanand0/scripts/commit/d73e423bd20255ed7495eaf283f27aeff952608c)). Better DOM capture and safer page close reduce leaks. (15 Aug 2026) Takeaway: reliable scraping needs explicit cleanup and clear error paths.
- **Model defaults, pricing, and test hygiene.** Upgraded Gemini defaults and local pricing, made summarizer prefer GPT-5.6 Luna or OpenAI paths, and tightened tests/justfile to avoid accidental paid calls ([6a35a2b](https://github.com/sanand0/scripts/commit/6a35a2b5e72c3d918e5029bd29ad186dad7ec449), [24423fef](https://github.com/sanand0/scripts/commit/24423fef7536547926647e5dbc3cb0c04b8d6480), [69c68ec](https://github.com/sanand0/scripts/commit/69c68ec16b49aac2b97679f1fb4b8106de36a1bb)). Tests now run via `just test` and guard paid APIs. (11–15 Aug 2026) Takeaway: pin defaults and make tests explicitly cheap and offline-safe.

### [sanand0/blog](https://github.com/sanand0/blog)

_Content growth plus clearer steer metadata for long-lived guidance._

- **New posts and updates.** Added several short posts and content (Ask AI email experiment, dancing note, tea perspective, comic prompts) and updated metadata ([4d23144](https://github.com/sanand0/blog/commit/4d23144864659c0e09bf5a37f4bffcbf03f81bf1), [8626e9b](https://github.com/sanand0/blog/commit/8626e9ba8295fbf5e9f01ada0396baf2faf6bbbd)). These broaden experiments and diary-style writing. (10–14 Aug 2026) Takeaway: small, regular posts keep readers and experiments visible.
- **Skill file gains versioning and expiry.** `anand-objectives/SKILL.md` now includes version, expiry, and review cadence ([f09ec6d](https://github.com/sanand0/blog/commit/f09ec6dfcbd5e1529baa4f4e6d788cf6f62a1462)). This documents when the steer should be rechecked. (15 Aug 2026) Takeaway: treat long-lived instruction files as mutable, with explicit review dates.
- **Guardrails tightened in prompts.** Email-reply prompt updated to require clarifying questions for material facts ([8626e9b](https://github.com/sanand0/blog/commit/8626e9ba8295fbf5e9f01ada0396baf2faf6bbbd)). This shifts agent behavior from blind drafting to safer, clarifying-first drafting. (14 Aug 2026) Takeaway: push clarifying questions into the prompt when consequences matter.

### [sanand0/talks](https://github.com/sanand0/talks)

	New talk write-ups and polished class pages to make talks reusable.

- **TDS AMA page and analysis.** Added the full AMA page, transcript, chat logs, and prep analysis for the Tools in Data Science AMA ([c460ddb](https://github.com/sanand0/talks/commit/c460ddba2b1c732edfb9840eefe97372a86530eb)). The page bundles transcripts, audio, and prep notes. (10 Aug 2026) Takeaway: publish raw artifacts so post-event value compounds.
- **IITM ED data-visualization class published.** Full page, transcript, links, and media were added for the IITM guest hour ([b888363](https://github.com/sanand0/talks/commit/b8883639f8940b52d0565023e8e9c12ec7dd0f66)). The page is ready for sharing. (13 Aug 2026) Takeaway: faculty talks make great reproducible artifacts.
- **Event pages refined.** Tweaks to the Data Hack Summit page improved narrative and verification examples ([4a3cb26](https://github.com/sanand0/talks/commit/4a3cb2685bf10256147c85baa00264c401ffd44e)). Tiny editorial fixes made the lessons clearer. (10 Aug 2026) Takeaway: small editorial passes increase educational clarity.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_New stories and extraction tools to surface oddities in public data._

- **Gramener Glassdoor dossier.** Added a full dossier with extraction scripts, cached JSON, and an interactive index page ([bc7a06e](https://github.com/sanand0/datastories/commit/bc7a06e08273c5f623b2ce1d917030957d46bb10)). Tests verify counts and merges. (09 Aug 2026) Takeaway: combine page scraping and API capture for richer, auditable data.
- **Embassy vs GDP story.** New embassy scatter story added with an interactive SVG and search filtering ([988b553](https://github.com/sanand0/datastories/commit/988b553f050b1b5de6f77e3bc8ef47b18c492e32)). It highlights diplomatic outliers by GDP. (15 Aug 2026) Takeaway: simple scatter plots reveal policy oddities people notice.
- **Config and README updated.** The site config now lists the new stories and screenshots for easy navigation ([988b553](https://github.com/sanand0/datastories/commit/988b553f050b1b5de6f77e3bc8ef47b18c492e32)). (15 Aug 2026) Takeaway: keep index metadata in sync with new outputs.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Benchmark housekeeping so model cost-quality tallies stay accurate._

- **Model ELO and stats updates.** Updated `elo.csv` and model list to reflect recent leaderboard changes and GPT-5.6 stats ([1ad2abe](https://github.com/sanand0/llmpricing/commit/1ad2abe33dd222a2e5357613a85d4e847509610c), [b61db10](https://github.com/sanand0/llmpricing/commit/b61db103a4b52f89c84cd02f9c977338d49bac04)). This keeps the frontier calculation correct. (09–12 Aug 2026) Takeaway: keep data and assumptions aligned with leaderboards.

### [sanand0/imdb](https://github.com/sanand0/imdb)

_Smarter visual cues for exploring films._

- **Dynamic outliers and year tooltip.** `script.js` now computes visible outliers after filters change, and the tooltip shows year before title ([00cd4aa](https://github.com/sanand0/imdb/commit/00cd4aa2678444b02f4320b206102b3e6c55878c)). This makes the UI more exploratory and the top table clearer. (12 Aug 2026) Takeaway: small UI shifts guide better exploration.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_More polished weekly podcast content for the WhatsApp group digest._

- **Podcast episode draft updated.** Weekly show script and notes were added for the 09 Aug 2026 episode, plus a tiny release helper in `justfile` ([21789be](https://github.com/sanand0/generative-ai-group/commit/21789be2c01c53da6050e05a5a954b7bf1e3755d)). The script organizes highlights and takeaways. (09 Aug 2026) Takeaway: keep reproducible show notes with audio links for distribution.

### [sanand0/til](https://github.com/sanand0/til)

_Weekly learnings expanded and timestamped for later review._

- **LLMs notes updated.** The `llms.md` entry added multiple recent lessons about agents, permissions, and loop engineering ([dabff9d](https://github.com/sanand0/til/commit/dabff9d196d8ae7aa35ede7f2c454134a3e66ed9)). These capture operational insights from recent experiments. (09 Aug 2026) Takeaway: write small notes fast; they'll guide future design choices.

### [sanand0/tools](https://github.com/sanand0/tools)

_Scrapers can now export human-friendly Markdown and JSON._

- **Scrapers export Markdown and JSON.** Several scraper bundles gained copy controls, Markdown exporters, and tests for the new flow ([70bca84](https://github.com/sanand0/tools/commit/70bca84d3ee684cd96085096fa8c5667bbf526f3)). Tests assert the markdown content and clipboard behavior. (09 Aug 2026) Takeaway: let users copy readable exports to speed sharing and review.

## Lessons

- Small UX fixes compound. A friendlier CLI, a notification, or a tighter tooltip prevents hours of friction.
- Tests must explicitly avoid paid APIs. Make offline, cheap, and isolated test flows the default.
- Archive early. Moving unused helpers to an archive reduces cognitive load and risk.
- Treat model defaults and pricing as config, not hard code. Push migration notes and review dates.
- Publish artifacts (transcripts, audio, data exports). Public artifacts make verification and reuse simple.

## Suggestions

- Add a CI step that runs the new prompt-picker tests and blocks changes that call paid endpoints.
- Publish changelogs for model-default and pricing changes. Make model-default rollouts explicit.
- Add a small dashboard for `run-at` jobs and recent notifications. One glance should show failures.
- For scrapers, add a small integration test that runs with a cached DOM snapshot. That prevents live scraping regressions.
- For datastories, schedule a short audit pass to verify source licenses and add compact provenance notes.
- Measure user pain points: log how often `prompt` falls back to printing instead of copy-paste. Fix the common case first.

If you want, I can convert these suggestions into a short issue template and a prioritised todo list for the next week.