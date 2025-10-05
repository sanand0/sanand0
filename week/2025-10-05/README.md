## A week of data stories, smoother tools, and agent-first UX

This week shipped big, readable storytelling pieces and a flurry of developer ergonomics. The main lesson: make data humane and developer flow frictionless.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Crafted browser-history stories that turn private logs into gentle, publishable narratives while calling out privacy risks._

- **New browser-history suite (04 Oct 2025):** Added a full set of stories and specs ([b7d6541](https://github.com/sanand0/datastories/commit/b7d6541654adf68dede16c362de359492fbcd032)). Files include [browser-history/README.md](https://github.com/sanand0/datastories/blob/main/browser-history/README.md) and story folders. Why it matters: it turns raw history into reusable CSVs and visual specs so readers can feel their attention patterns. Takeaway: structure data before you visualise it; the prompts and CSVs carry most of the reproducibility.
- **Attention Clock viz & data (04 Oct 2025):** Published [attention-clock/index.html](https://github.com/sanand0/datastories/blob/main/browser-history/attention-clock/index.html) plus CSVs. This gives a circadian view of focus. Takeaway: hourly aggregates make personal rhythm visible without exposing raw traces.
- **Privacy review & guidance (04 Oct 2025):** Added [leaks.md](https://github.com/sanand0/datastories/blob/main/browser-history/leaks.md) that flags high-risk files and suggests anonymization steps. Takeaway: always audit PII and aggregate before publishing—screenshots often leak the most.

(Aside: yes, your calendar shows up more than you thought.)

### [sanand0/tools](https://github.com/sanand0/tools)

_A steady stream of small, browser-focused tools and quality-of-life fixes for the utility site._

- **Bootstrap Theme Picker (02 Oct 2025):** Added a bookmarklet-based theme picker with UI and tests ([5d75372](https://github.com/sanand0/tools/commit/5d7537281f9f8cef784e98267336a05d53beeae8), [b9ded98](https://github.com/sanand0/tools/commit/b9ded98d27574727e02034c2833534517ca33fda)). Files: `bootstrappicker/index.html`, `bootstrappicker/bootstrappicker.min.js`. Why it matters: lets you preview Bootstrap palettes live without rebuilding CSS. Takeaway: small interactive bookmarklets reduce design guesswork.
- **Polish and tests (02 Oct 2025):** Fixed palette updates and expanded presets; added `bootstrappicker.test.js` for UI behavior ([63d7591](https://github.com/sanand0/tools/commit/63d75917ab7465e07b51ce746c23e038a71a4897)). Takeaway: ship with tests — browser quirks bite later.
- **Recall & scraper fixes (28 Sep 2025):** Removed contenteditable from recall cards and tightened WhatsApp scraper reaction parsing ([9af9783](https://github.com/sanand0/tools/commit/9af97832c41e101f67c16c82c5d98fcfc9364b73), [9db3d7b](https://github.com/sanand0/tools/commit/9db3d7bf570c7068ecc6ff36acc6c0ba3631b94d)). Why it matters: safer rendering and cleaner scraped text. Takeaway: small UX fixes save confusion when tools are used by many.

(Aside: another bookmarklet? The web is full of them — and now prettier.)

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_Course and teaching material updates that reflect current AI tooling and course runtime changes._

- **Added Jules & Codex Workspace notes (03 Oct 2025):** Documented Google’s Jules and OpenAI Codex Workspace ([c12ac42](https://github.com/sanand0/tools-in-data-science-public/commit/c12ac421a4431faa017fe74d5f0c7a2f2ab27e42)). Why it matters: gives students modern, multi-agent and collaborative coding tool references. Takeaway: keep course tooling notes current; novices need pointers more than theory.
- **Project spec & GA3 soft-launch (03 Oct 2025):** Revised Project 1 spec for LLM-powered code deployment and added GA3 links ([d83c9ef](https://github.com/sanand0/tools-in-data-science-public/commit/d83c9ef2e578db7fe97c2656e6e04f0d5b65205d), [c92f136](https://github.com/sanand0/tools-in-data-science-public/commit/c92f13669dc1fb2f215c4bad03fdda5c51b2cca0)). Files: `project-llm-code-deployment.md`. Takeaway: tests and signature-based requests help automate grading while teaching secure workflows.
- **CLI tool notes (03 Oct 2025):** Added GitHub Copilot CLI to the module list ([bab2bdf](https://github.com/sanand0/tools-in-data-science-public/commit/bab2bdfe2154a30eddf3efde437983a12e47f0f1)). Takeaway: include both vendor and open tools so students can compare trade-offs.

(Aside: yes, students will copy-paste faster than you expect. Use authentication guards.)

### [sanand0/scripts](https://github.com/sanand0/scripts)

A big week of shell polish and small developer utilities to make data-handling and logs painless.

- **Modular CLI jq utilities (29 Sep 2025):** Extracted log processors into standalone `.jq` scripts: `codexlog.jq`, `claudelog.jq`, `jsonpaths.jq`, `whatsappthread.jq` and added `pdbhook/sitecustomize.py` for post-mortem debugging ([be99595](https://github.com/sanand0/scripts/commit/be99595e062dcff91ad5797af454e1901910aabc)). Why it matters: makes log conversion and inspection one-liners. Takeaway: keep parsing logic scriptable and versioned.
- **Large setup.fish refactor (28–29 Sep 2025):** Overhauled shell aliases and removed inline jq functions now provided by scripts ([cc32366](https://github.com/sanand0/scripts/commit/cc32366059db4a614a0956442986977043b38548)). Takeaway: move long helpers out of dotfiles into testable scripts.
- **New githubscore and helper tools (early Oct commits):** Added `githubscore.py` and other productivity scripts to evaluate GitHub presence and process logs (`codexlist`, `codexlog.jq`) ([githubscore commit added in this run]). Why it matters: automates repetitive repo audits and session summaries. Takeaway: small CLIs scale your own attention.

(Aside: your shell will never stop evolving. That’s fine — it’s cheaper than suffering.)

### [sanand0/tdsdata](https://github.com/sanand0/tdsdata)

_Easy synthetic data for demos and pages._

- **Fake JSON table generator (03 Oct 2025):** Added `json_table.py` to generate reproducible fake JSON datasets and wired it into the deployment workflow (`.github/workflows/deploy.yml`) ([7785a79](https://github.com/sanand0/tdsdata/commit/7785a79202b5df01886023051b87efb0e6728610)). Why it matters: deterministic test data for examples and demos. Takeaway: generate demo data at deploy-time, not in repo, to keep VCS light.

(Aside: yes, fifty files of fake names are more useful than one perfect CSV.)

### [sanand0/llmagent](https://github.com/sanand0/llmagent)

_A rapid series of UX and tool rendering upgrades for agent debugging and streaming._

- **Streaming UI & real-time rendering (29 Sep 2025):** Switched to incremental, streaming UI for agent responses and tool events ([9641560](https://github.com/sanand0/llmagent/commit/96415606879ca6f5e1529f4f38bf1ad6b36249e2)). Why it matters: users see progress and tool calls as they happen. Takeaway: streaming = trust + faster iteration.
- **Custom tool rendering (01 Oct 2025):** Tools now expose `render` and `renderResults` to show neat HTML summaries instead of raw JSON ([eebb6d5](https://github.com/sanand0/llmagent/commit/eebb6d55a1692e5b7f415d492f2d5214862567c7)). Files: `tools.js`. Takeaway: present tool outputs in human form; it speeds reviews.
- **Google Search tool & saveform (29 Sep 2025 / 01 Oct 2025):** Added `google_search` tool plus UI fields and form persistence via `saveform` ([8794ab2](https://github.com/sanand0/llmagent/commit/8794ab2a98109fa3473a70e744c6acf8d7f3a186), [47120fa](https://github.com/sanand0/llmagent/commit/47120fa29b9c3f5408dab3ab1166993884070908)). Why it matters: agents gain web access and the UI remembers settings. Takeaway: keep environment binding explicit and local to the form.

(Aside: watching an agent think is oddly calming. Also diagnostic.)

### [sanand0/prompts](https://github.com/sanand0/prompts)

_Brief but useful additions that sharpen prompt library for teaching and production._

- **New prompts added (28 Sep 2025):** Added `afterslides-appendix.md`, `developer-styles.md`, and `ideator.md` for slide appendices, coding styles, and idea synthesis ([5bca960](https://github.com/sanand0/prompts/commit/5bca960a621c335363c9c9fbf78c3416532e5627)). Why it matters: prompts become reusable building blocks for content and code. Takeaway: collect prompts as reproducible templates.
- **Refined call transcript analysis (28 Sep 2025):** Improved `analyze-call-recording.md` to include Persona and stricter fact-check guidance. Takeaway: add structure for empathy and verification when analyzing conversations.

(Aside: yes, you can have too many templates. Just don’t delete the useful ones.)

### [sanand0/til](https://github.com/sanand0/til)

_Notes and TIL updates reflecting fast-moving LLM and tooling trends._

- **Updated LLM and tooling notes (28–29 Sep 2025):** Captured LLM benchmark trends, Dayflow, Code Mode, Copilot CLI, and `selectolax` as a fast HTML parser ([74e9a8c](https://github.com/sanand0/til/commit/74e9a8c2f42c11ba59f9f50613dc2d740fce49e8)). Why it matters: bookmarks for future research and engineering tasks. Takeaway: keep a short public brain for patterns you’ll forget otherwise.
- **Practical shell & git tips:** Added pure-bash tricks and `git worktree` commands. Takeaway: small shell moves multiply productivity.

(Aside: a TIL is just an IOU to your future self.)

### [sanand0/saveform](https://github.com/sanand0/saveform)

_Small but thoughtful library improvements to make saved form state safer._

- **dropEmpty option & tests (29 Sep 2025):** Add `dropEmpty` to delete keys with empty strings and updated tests and README ([d4bbe5b](https://github.com/sanand0/saveform/commit/d4bbe5be79107262150ce4fd1442c1d9525eb2f1), [a077ef7](https://github.com/sanand0/saveform/commit/a077ef7b0619d7c904f7c3b76101adc85c360c6e)). Why it matters: lets users reset saved values by clearing the field. Takeaway: small options reduce surprising persisted state.
- **Release 1.4.0 & npmrc (29 Sep 2025):** Bumped version and set `package-lock=false` to avoid lockfile churn. Takeaway: be deliberate about package consumer expectations.

(Aside: clearing a field should be a reset, not a zombie value.)

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Podcast pipeline tweaks to prefer the newest model outputs and cleaner prompts._

- **Upgrade to gpt-5-mini and output parsing fix (28 Sep 2025):** Switched model and extract final output from the last `result["output"]` entry ([140277b](https://github.com/sanand0/generative-ai-group/commit/140277b64ede359fdbdf68debc2d47720cc9e4e6)). Why it matters: avoids mixing reasoning traces with final text. Takeaway: adapt parsing when model output formats change.
- **Script simplification & new episode (28 Sep 2025):** Updated prompt and generated episode text and logs; added `podcast-2025-09-28.md`. Takeaway: small prompt edits yield better broadcast-ready scripts.

(Aside: the model upgrade is like swapping mics mid-podcast — clear, but mind the gain.)

## Lessons

- Small, reusable artifacts win. Modular scripts, prompt templates, and CSV specs scale better than monolith changes.  
- Present data in human form. Aggregation and friendly rendering (tool results, summaries) accelerate understanding and safe publication.  
- Stream early, ship often. Streaming agent UI and incremental feedback make debugging and trust much easier.  
- Privacy is a feature. Auditing and anonymizing before publishing avoids later regrets.  
- Tests matter for tiny UIs. Adding simple UI tests prevents regressions in bookmarklets and modal UIs.

## Suggestions

- Redact and aggregate any high-risk browser-history artifacts before public demos. Consider automated domain grouping and redaction pipeline.  
- Add an explicit privacy/consent note and anonymize examples in datastories READMEs.  
- Convert key jq scripts into tiny Go/TS CLIs for cross-platform portability and add release builds.  
- Add a small playbook showing how to reproduce the agent UI locally with a sample Google API key and saved form config.  
- For the Bootstrap picker, add a small visual regression test (screenshot diff) to catch CSS variable regressions.  

If you want, I can draft a short privacy checklist for publishing the browser-history stories and a checklist to harden the agent UI for external demos.