## A week of new demos, calmer ops, and louder voice tools

Small web apps got bigger. Course content and scripts tightened for reproducible, testable work.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Story-first visuals make data feel obvious. The week added a rich, interactive Bollywood box-office story and the scrapers that feed it._

- **New Bollywood story page.** Added a full D3-based interactive page, README, and screenshot ([6add28a](https://github.com/sanand0/datastories/commit/6add28a323321e8e9ad0d1458dfd2642bbd70e9d)) (27 Sep 2025). It gives a friendly, inflation‑adjusted view of top films. Takeaway: visuals + narrative reveal patterns faster than raw tables.
- **Data scraped from Wikipedia.** Added scraper, CSV, and parsing prompts ([14da032](https://github.com/sanand0/datastories/commit/14da0328aa9a1e3859ef44d5f6b3b055bb507f77)) (27 Sep 2025). It normalizes gross numbers into crores for consistent charts. Takeaway: clean, auditable collection beats guessing later.
- **Handy project README + inflation data.** Documented methods and included inflation.csv + prompts ([e549b89](https://github.com/sanand0/datastories/commit/e549b893f80cf40fca2cff59f4eb0ebe7c3103f3)) (27 Sep 2025). Users can run locally or inspect provenance. Takeaway: documenting data provenance prevents future “where did this number come from?” headaches. (Yes, another movie viz. Someone had to do it.)

### [sanand0/scripts](https://github.com/sanand0/scripts)

_More voice, less friction. Big refactors added voice-to-LLM shortcuts, systemd services, and a focused file-index cache._

- **Voice → LLM → paste flow.** New scripts (ask, askpaste.sh, askwin) and refinements let you record, convert, and paste LLM output into the active window ([acab6a2](https://github.com/sanand0/scripts/commit/acab6a27e1c888f0c9eaf7fe2e96f882ba2629b0)) (21 Sep 2025). That removes manual copy/paste steps. Takeaway: cut repetition with a tiny UI that thinks for you.
- **Systemd services & timers.** Added services/setup.sh and timers for trending repos and file-index updates ([acab6a2], files under services/) (21 Sep 2025). Now tasks run reliably and can catch up after sleep. Takeaway: move cron-style jobs into systemd timers for more robust scheduling.
- **Central file cache + rofi integration.** New update-files script and cache location (~/.cache/sanand-scripts) plus rofi-files.sh updates ([acab6a2]) (21 Sep 2025). fzf/rofi stays fast on huge mounts. Takeaway: caching + clear paths scale UI tools without heroic hacks. (No, you don’t need another grep; use ugrep.)

### [sanand0/til](https://github.com/sanand0/til)

_Notes and curricula got neater. New core concepts, trending repo tooling, and content moves make the weekly knowledge feed sturdier._

- **Creative-ideas & content reshuffle.** Moved Oblique Strategies into creative-ideas and expanded brainstorming notes ([43628ba](https://github.com/sanand0/til/commit/43628ba72400451d20076df12dec823f08482c5b)) (27 Sep 2025). Takeaway: group ideas where people actually look for them.
- **Weekly trending repos script and TSV.** Added trending-repos.sh and populated trending-repos.tsv for weekly snapshots ([37dbb1c](https://github.com/sanand0/til/commit/37dbb1c41526c50aed2f7bd6f1a106f634f140af)) (21 Sep 2025). It fetches and merges language-specific trends. Takeaway: automated trend captures save manual hunting.
- **Fresh notes & housekeeping.** Multiple daily updates across llms.md, til.md, ideator.md to keep learnings current (Sep 2025). Takeaway: small, frequent updates keep the knowledge repo useful.

### [sanand0/prompts](https://github.com/sanand0/prompts)

_Prompts matured into a discoverable library. New metadata and higher-quality templates will make reuse easier._

- **New prompts and metadata.** Added ChatGPT custom-instructions and core-concepts prompts; updated README for discoverability ([85b3070](https://github.com/sanand0/prompts/commit/85b3070210bd559364c127fe61cc2558efcf0ee4)) (21 Sep 2025). Takeaway: findability multiplies prompt reuse.
- **Refined evaluation & review prompts.** Tightened evaluate-technology and review-article prompts for clearer, citation-first outputs ([85b3070]) (21 Sep 2025). Takeaway: prompts should demand verifiable claims, not just confident prose.
- **Developer-styles expansion.** Added richer “mimic dev” materials and expert-review notes for applying coding styles programmatically (commits across 26–27 Sep 2025). Takeaway: style-guided agents speed consistent code generation. (Yes, another prompt for another model. It helps.)

### [sanand0/tools](https://github.com/sanand0/tools)

More single‑page apps and demos landed. Playlist maker, voicebot, and deploy tweaks pushed the toolset forward.

- **Findsongs playlist builder added.** New single-page app with streaming LLM calls, tests, and UI ([c3c0471](https://github.com/sanand0/tools/commit/c3c047177ff89d990fc7fea9eda7354a6a367c0b)) (27 Sep 2025). Tests validate model schema and YouTube lookups. Takeaway: structure response formats (json_schema) to make UI wiring trivial.
- **Iterated on LLM calls and credential UX.** Several commits refined prompt handling, streaming, and provider configuration ([5e0572c](https://github.com/sanand0/tools/commit/5e0572cedbaa48c0b86195ffa5f933d7f8a919a6) and [8a16b55](https://github.com/sanand0/tools/commit/8a16b55d47fb60308ec93878fde4b95f819c026d)) (27 Sep 2025). Takeaway: keep credentials and provider UIs consistent across tools.
- **Voicebot: realtime audio demo.** New Voicebot UI and realtime client (WebRTC + OpenAI-style session flow) added ([ac00478](https://github.com/sanand0/tools/commit/ac00478dd3a06b375390603d828494b993ac8d2a)) (23 Sep 2025). It records, connects to a realtime LLM, and plays remote audio. Takeaway: realtime demos reveal UX gaps early; keep them minimal and auditable. (Yes, you needed another voice toy. It’s useful.)

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

Course materials tightened, re-ordered, and expanded. New guides for deployment and AI coding appeared.

- **Reordered modules and dates.** Swapped Deployment Tools before AI Coding; updated GA2/GA3 dates to match ([83b744a](https://github.com/sanand0/tools-in-data-science-public/commit/83b744aa7f20ec0227c9beec9f8a193d97db8dc8)) (23 Sep 2025). Takeaway: put deployment first when coding assignments need deploy skills.
- **Hugging Face Spaces Docker guide.** Added a full Docker Spaces walkthrough for students and deploy examples ([359ec93](https://github.com/sanand0/tools-in-data-science-public/commit/359ec93fd5eb3aaa379de3bd5dfb69bc91352b2c)) (06 Sep 2025 / surfaced 22 Sep 2025). Takeaway: teach deploy patterns with concrete, runnable steps.
- **Expanded AI coding tests & tools modules.** Added ai-coding-tests.md and ai-coding-tools.md with guidance on premortem TDD, scorecards, property testing, and agent toolchains ([ccd135c](https://github.com/sanand0/tools-in-data-science-public/commit/ccd135cfa10d0b28eae55bad81493099fd40a3a4)) (22 Sep 2025). Takeaway: make generated code testable before it lands.

### [sanand0/llmevals](https://github.com/sanand0/llmevals)

_Exploring “style” transfer for code agents and inviting expert-style reviews._

- **Developer-style mimicking experiments.** Added many sample checkouts written in famous authors’ styles and a prompting pipeline to generate them ([dbb0660](https://github.com/sanand0/llmevals/commit/dbb066076f9768d62e15bb06f9336998ceb10171)) (26 Sep 2025). Takeaway: style-based templates are a fast way to explore alternative APIs.
- **Expert review & refactor notes.** Added an expert-review workflow and notes to apply “panel of experts” refactors to repos ([7cf269b](https://github.com/sanand0/llmevals/commit/7cf269b1a110e8232ee9aa80d3b15d6c61da8716)) (27 Sep 2025). Takeaway: use well-scoped expert prompts for targeted refactors, not wild rewrites.
- **Tiny utility additions.** Small code samples (e.g., checkout machines) to test style transfer. Takeaway: small tasks surface differences clearly.

### [sanand0/llmagent](https://github.com/sanand0/llmagent)

_More general agents and safer tool schemas. Shifted from a single multiply tool to runnable JS execution._

- **Generalize the agent config.** Agent is now an “Executor agent” that bundles tools, not a single-purpose calculator ([a0485f4](https://github.com/sanand0/llmagent/commit/a0485f42c276623c6795d4a22731589cac1c5875)) (26 Sep 2025). Takeaway: agents should be configurable collections, not hard-coded cases.
- **Replace multiply tool with js runner.** Removed zod dependency and added js_code tool that executes async JS safely in a function ([4495eb3](https://github.com/sanand0/llmagent/commit/4495eb32c8c96c58b99222d45dc6453d9b222e74)) (26 Sep 2025). Takeaway: giving agents a small, well-documented execution surface unlocks richer demos.
- **Improve UI logs and history rendering.** More robust response rendering for multi-part history and audio/text parts ([54fd4c4](https://github.com/sanand0/llmagent/commit/54fd4c4f89fa2522cd6926345ced12b3e6b320ca)) (26 Sep 2025). Takeaway: show history not just final output; it's the debugging gold.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Podcast automation and weekly outputs got refreshed._

- **Updated weekly podcast generation.** New episode markdown, expanded transcript, and updated gen-ai message dump for 21 Sep output ([a419901](https://github.com/sanand0/generative-ai-group/commit/a41990131ac84615ce900cd2ab6159b1c19114e1)) (21 Sep 2025). Takeaway: automated pipelines pay off—publish faster and more reliably.
- **Improved podcast scripts and metadata.** The repo now stores heavy JSONL messages and polished episode notes. Takeaway: keep source data and final artifacts together for reproducible episodes.

### [sanand0/talks](https://github.com/sanand0/talks)

_New talks added and presentation pages refined. LLM Trends talk is now published._

- **Added “LLM Trends” talk.** Full Marp slides, transcript, and visuals for 22 Sep talk ([d233f4a](https://github.com/sanand0/talks/commit/d233f4a60f0c940864be62cfe6943b6fd3e2c76d)) (22 Sep 2025). Takeaway: slides + transcript = durable learning artifacts.
- **New conference talks added.** Kiran’s “Homelabbing” and Zainab’s IndiaFOSS talk added, with videos and QR codes ([4e1e583](https://github.com/sanand0/talks/commit/4e1e5839145ce855958d7cd4569965ab2545a646), [ff0f876](https://github.com/sanand0/talks/commit/ff0f876dacc73d9bc8ed511d57fae610828bf012)) (25 Sep & 22 Sep 2025). Takeaway: publishing everything makes talks useful again—QR codes help show-and-tell.
- **Presentation UX tweaks.** Slides now reveal as fragments and made layout tweaks for clarity. Takeaway: small display fixes improve live demos considerably.

### [sanand0/aipipe](https://github.com/sanand0/aipipe)

_Smaller but important ops change for safer defaults._

- **Don’t commit config.js; ship config.example.js.** Renamed config.example and update worker to fallback to example if config missing ([bb40f6a](https://github.com/sanand0/aipipe/commit/bb40f6a82f34ec3ef0108037e600be41776957ad)) (25 Sep 2025). Also added src/config.js to .gitignore. Takeaway: stop leaking secrets and make local setup clear.
- **README updates & test fixes.** Docs now instruct copying example config and tests import the example config. Takeaway: smoother onboarding for self-hosters.

## Lessons

- Small UX work compounds. Automating mundane steps (file caches, timers, credential dialogs) converts friction into flow. Ship the tiny helpers.
- Structure LLM outputs. Using structured response formats (json_schema) makes UI wiring deterministic and testable.
- Teach deploy before code. If students must deploy, teach deployment first. The course reorder shows that sequencing matters.
- Tests-first for AI code. Premortem tests, scorecards, and selectors make agent output reliable.
- Reproducible configs matter. Don’t commit secrets. Provide examples and fallbacks.

## Suggestions

- Add CI checks that run the new scorecard tests for tools and web demos. Start with lightweight tests for findsongs and voicebot.
- Measure outcomes: record tool usage, startup time (Fish abbrs), and rofi latency before/after caching.
- Harden voice workflows: add explicit prompt logging and consent prompts before audio is sent to providers.
- Teach one reproducible deploy example in course: app → Docker Space (Hugging Face) → CI. Students can follow an end-to-end template.
- Audit tooling debt: run a quick pass to ensure all new scripts have exec bits, small README snippets, and licenses.

If you want, I can:
- produce a short changelog-only version for GitHub releases, or
- extract the new prompts into a single downloadable ZIP for students.