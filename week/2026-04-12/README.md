## A week of dashboards, data cards, and production-ready AI toys

Small projects grew up this week — more tests, clearer UX, and reproducible data work. The key lesson: ship readable artifacts and tests so others can reuse your work quickly.

### [sanand0/aidashboard](https://github.com/sanand0/aidashboard)

_Stable static dashboards and reproducible synthetic data make demos useful to teams and Copilot agents._

- **Synthetic data generator & tests added.** Added `scripts/generate_data.py` and unit tests so the dashboard can be regenerated and validated ([d889505](https://github.com/sanand0/aidashboard/commit/d8895054b578d3fc580b86382e3c05a3bfb851f3), 10 Apr 2026). This makes local demos deterministic and testable. Takeaway: prefer reproducible fixtures over hand-edited JSON.
- **7-day moving average on trends.** Implemented MA overlay and chart plumbing in `site/index.html` (see [d35e82b](https://github.com/sanand0/aidashboard/commit/d35e82bc12559350798057dbd4849c92dc8610df), 10 Apr 2026). The chart now shows raw and smoothed series for backlog and SLA. Takeaway: smoothing helps spot system-level shifts without hiding volatility.
- **Pages + deploy automation.** Initial site, GitHub Pages workflow, and Copilot-friendly instructions landed ([903f417](https://github.com/sanand0/aidashboard/commit/903f417510ec1743a30536b3099e59cee4b9c790), 10 Apr 2026). Added tests and a simple README for maintainers. Takeaway: ship a tiny CI + docs bundle to make demos low-friction. (Yes, a static dashboard still needs a tiny amount of Ops.)

### [sanand0/talks](https://github.com/sanand0/talks)

_More talks, transcripts, and activity extraction — making presentations reproducible and remixable._

- **LBSNAA workshop site and transcript.** Published the full LBSNAA workshop page and transcript ([30ff0d7](https://github.com/sanand0/talks/commit/30ff0d70759b061f4655f8e697c72a2e46f521ae), 08 Apr 2026). The HTML includes audio and prompts. Takeaway: publishing complete artifacts preserves context for reuse.
- **Added Debjani Ghosh talk.** Added transcript and attendant prompts for the Straive workshop series ([6fee9d0](https://github.com/sanand0/talks/commit/6fee9d0759964326905e0f94e51157c1da163be6), 08 Apr 2026). This exposes speaker Q&A and sourced quotes. Takeaway: transcripts power searchable lessons and quotes.
- **Synthesis: activities & prompts.** Created analysis pages (activities.md, prompts.md) across many talks to catalog live workshop exercises ([bbedb0f](https://github.com/sanand0/talks/commit/bbedb0fa8b6e914d85db000b9e66861879d9a17c), 08 Apr 2026). This standardizes "what we did" into testable steps. Takeaway: capture actions, not just slides, to make workshops repeatable.
- **Hack-of-the-day story & web features.** Polished the Times of India case study and interactive pages for March work ([fb3d78f](https://github.com/sanand0/talks/commit/fb3d78fb3dbe5be2e7a8ff5c97a487ad80851d10), 06 Apr 2026). The page is built as single-file HTML with popups. Takeaway: single-file artifacts are easy to host and verify. (Yes, another long HTML file — but it survives without a build step.)

### [sanand0/journalists](https://github.com/sanand0/journalists)

_Print-to-web conversions, MOSPI data cards, and verification SOPs for publishable journalism._

- **Flap-to-HTML SKILL & outputs.** Added a full SKILL.md and three converted flap HTML pages for Times of India use ([4fec2597](https://github.com/sanand0/journalists/commit/4fec2597b4bf6abc5c486b71774ebf8a6540c4d4), 10 Apr 2026). The notes explain pitfalls like hiding content with `opacity:0`. Takeaway: convert print to web with explicit rules, not guesswork.
- **MOSPI PLFS v4 analysis and CSV outputs.** Added `v4/analyze.py`, insights, and many outputs for verification ([0d0c407](https://github.com/sanand0/journalists/commit/0d0c40734b17b8a0c31e8e7301be480756004fc3), 10 Apr 2026). This creates reproducible CSVs behind each data card. Takeaway: ship code + CSVs so reporters can re-run analyses.
- **Rendered cards and gallery.** Added SVG cards, Playwright render script, and an index gallery with verification popups ([fced73b8](https://github.com/sanand0/journalists/commit/fced73b880df702e2a839a258a40bc709d42187e), 10 Apr 2026). Each card links to a SOP for fact-checking. Takeaway: pair visuals with verification checklists to reduce editorial risk.
- **New flaps gallery & index.** Built `flaps/print-to-online/index.html` and multiple story pages ready for CMS paste ([f0957ab](https://github.com/sanand0/journalists/commit/f0957abc104006a1f2f576673bf7acfac18cc888), 10 Apr 2026). The gallery includes screenshots and notes. Takeaway: bundles that include screenshots speed review cycles. (Also: PDFs are sneaky; always test screenshots.)

### [sanand0/blog](https://github.com/sanand0/blog)

.Documents and short essays capturing experiments, sketchnotes, and workshop tactics.

- **AI experiments & sketchnote recipes.** Added an "AI Experiments" page and a Gemini sketchnotes how-to post ([a5f8fd0](https://github.com/sanand0/blog/commit/a5f8fd02d5f4ec26f96afbcbc82472a842baaae0), 11 Apr 2026). The posts capture prompts and workflows for reuse. Takeaway: centralize micro-experiments for quick workshop prep.
- **New workshop posts and provenance fixes.** Added posts about using AI in workshops and appended provenance links to earlier palmistry notes ([649c21a](https://github.com/sanand0/blog/commit/649c21af2f0c023a1f5d7855c565048dc50b2cb5), 09 Apr 2026). This keeps artifacts auditable. Takeaway: small provenance links pay off later.
- **Three practical essays added.** Flight mode, a generated vote-of-thanks song, and improvisational speaking notes joined the blog ([adb5377](https://github.com/sanand0/blog/commit/adb53778ac52dddd4b7efc8f6f35a066300056c1), 05 Apr 2026). Each includes media and examples. Takeaway: publish concrete examples with media for immediate re-use.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_New CLI tooling: agent log consolidation and live transcription for reproducible agent experiments._

- **agentlog: unified agent logs CLI.** Added `agentlog.py`, tests, and prompt docs to read logs for Copilot/Claude/Codex ([555f977](https://github.com/sanand0/scripts/commit/555f97781a8ccb864ed21bc7e936017ed0bb9c3d), 10 Apr 2026). It standardizes ls, md, and search behaviors. Takeaway: one tool to rule your logs reduces maintenance and speeds audits.
- **livetranscribe: watch-and-transcribe .opus.** Added `livetranscribe` CLI that watches a growing .opus file and streams Gemini Live transcripts ([555f977](https://github.com/sanand0/scripts/commit/555f97781a8ccb864ed21bc7e936017ed0bb9c3d), 10 Apr 2026). It supports overlap, session restarts, and json/text outputs. Takeaway: test harnesses are worth adding early for live workflows.
- **UX & dev hardening.** Updated rofi-clip helpers, dev container security, and tests. These small ops changes avoid accidental secrets exposure. Takeaway: lock the dev surface early; it's a cheap insurance policy.

### [sanand0/tools](https://github.com/sanand0/tools)

.Small web tools and bookmarklets got a practical addition: a self-research prompt launcher.

- **Research Me tool added.** New researchme app prepares a comprehensive dossier prompt for ChatGPT/Claude ([8d75af5](https://github.com/sanand0/tools/commit/8d75af5f53af4199f3ebd2bebffea024781570ba), 06 Apr 2026). It pre-fills and opens providers with a long, evidence-focused prompt. Takeaway: templated prompts speed deep research.
- **Removed model query param.** Simplified provider URLs to avoid hard-coding models in `script.js` ([642cdef](https://github.com/sanand0/tools/commit/642cdef7aa032b7ba4f5c73e1be5eea55cfac7da), 06 Apr 2026). That keeps links resilient when providers change. Takeaway: prefer provider-agnostic prompts over pinned query params. (Yes, less brittle links are boring but practical.)

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Larger data packages and reproducible analysis for journalistic stories._

- **AI policies expanded to 30 universities.** Merged five more university records and refreshed the site copy and visuals ([cc14c40](https://github.com/sanand0/datastories/commit/cc14c40da2549159025808c488392da63e07eb65), 09 Apr 2026). The story now compares 30 institutions. Takeaway: adding more data tightens claims and surfaces edge cases.
- **New software-engineering skill page.** Added a long essay on amenability of engineering tasks to LLM feedback loops ([cc14c40](https://github.com/sanand0/datastories/commit/cc14c40da2549159025808c488392da63e07eb65), 09 Apr 2026). It frames where human judgment matters most. Takeaway: map technique to impact, not just novelty.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Podcast notes and short weekly summaries keep the community in sync._

- **Weekly digest episode posted.** Added `podcast-2026-04-05.md` summarizing agentic tools, privacy, and transcription tool comparisons ([901b870](https://github.com/sanand0/generative-ai-group/commit/901b8704481a2d21d5879f5516186e23f36a9b63), 07 Apr 2026). It captures practical tool pros/cons and tips. Takeaway: short written digests make asynchronous updates useful. (Also: people love tool lists.)

### [sanand0/til](https://github.com/sanand0/til)

_Short, dated notes to capture tiny experiments and system tweaks._

- **April notes and tooling tips.** Added Apr 2026 entries about GNOME tweaks, git-restore-mtime, script usages, and EARS requirements format ([750ea6b](https://github.com/sanand0/til/commit/750ea6b19dfa91dd30ffd217aba42c9bc5e2e480), 07 Apr 2026). These are quick, actionable reminders. Takeaway: small ops tips saved now prevent later friction.

## Lessons

- Ship code + data + tests together. Tests let others run and trust your demo.
- Small UX wins matter. Little defaults and prompts lower adoption friction.
- Capture provenance. Record the prompt, audio, and CSV that produced a claim.
- Prefer simple, reproducible artifacts over clever, untestable demos.
- Automate verification for visuals. Pair each chart with a checklist.

## Suggestions

- Add a tiny CI job that runs key scripts and tests across these repos weekly.
- For journalists: add simple `reproduce.sh` wrappers that write one-line commands.
- Scripts: publish agentlog output schema and a small viewer for quick audits.
- Tools: let Research Me optionally save a local prompt snapshot for audit.
- Talks: extract a canonical JSON per talk (transcript, timestamped audio, assets). Use it for automated sketchnotes and TTS demos.