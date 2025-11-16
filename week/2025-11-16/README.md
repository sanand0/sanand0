## A week of proposal polishing, token-by-token streaming, and tiny playable worlds

Big push to finish a professional RFP response, while research and infra work tightened LLM tooling and streaming. The key lesson: create reproducible artifacts (PDFs, CVs, builds, logs) so AI-driven speed becomes reliable speed.

### [sanand0/tata-trust-data-visualization-rfp-2025](https://github.com/sanand0/tata-trust-data-visualization-rfp-2025)

_Cleaning the proposal, build, and process made the submission auditable and repeatable._ (Yes, you needed another CI tweak.)

- **Complete proposal pack:** Added the technical proposal, compliance checklist, and pre-submission review ([7bb863d](https://github.com/sanand0/tata-trust-data-visualization-rfp-2025/commit/7bb863dacd33794bccfac62f1755a4039fcef769)) on 12 Nov 2025. This turns scattered docs into submission-ready PDFs. Takeaway: a single repo bundle helps reviewers and auditors.
- **Switched to npm-based Eleventy build and CI:** Replaced the earlier MkDocs flow and moved build to repo root ([a582615](https://github.com/sanand0/tata-trust-data-visualization-rfp-2025/commit/a582615ac1f8d6cc712d114dfcd3036aef66a086)) on 12 Nov 2025; added GitHub Actions for Pages ([3100c74](https://github.com/sanand0/tata-trust-data-visualization-rfp-2025/commit/3100c74ae82b633332304b7167bbc89de1238f48)) same day. Now builds are reproducible from CI. Takeaway: standardizing the toolchain avoids last-minute surprises.
- **Polished process and metrics:** Fixed hero metrics and links, and reconciled process notes ([b19f37a](https://github.com/sanand0/tata-trust-data-visualization-rfp-2025/commit/b19f37a01f666fd3b29671a63dea4f31d3064198)) on 13 Nov 2025. Accurate claims matter for credibility. Takeaway: keep the process doc as the single source of truth.
- **Automated CV generation and compiled company info:** Added a ReportLab CV generator ([69de4ed](https://github.com/sanand0/tata-trust-data-visualization-rfp-2025/commit/69de4ed6ed83573bb09ce0dcae5caf69b5726daa)) and collated signatory/company details ([0068302](https://github.com/sanand0/tata-trust-data-visualization-rfp-2025/commit/006830219e1991ed9a1eba27eeaeae9632ebcd92)) on 14 Nov 2025. This reduced manual annex work. Takeaway: automate browned-paperwork; sanitize before committing.
- **Gap checklist & tooling wishlist:** Large info-needed and tooling wish-list docs added ([5126987](https://github.com/sanand0/tata-trust-data-visualization-rfp-2025/commit/5126987d782b51ba2ec7edc05f38ac2f93e13031)) on 13 Nov 2025. This gives a clear owner map for missing items. Takeaway: explicit gaps speed final submission.

### [sanand0/research](https://github.com/sanand0/research)

_This week focused on making LLM streaming and content extraction reliable and measurable._ (Token-by-token: yes, it feels theatrical.)

- **Token-by-token Codex streaming:** Built a FastAPI + token wrapper for Codex CLI, enabling word/char streaming and a typewriter UI ([036e140](https://github.com/sanand0/research/commit/036e1407544b2b6968dc22d503dffe7e2630fc67)) on 11 Nov 2025. It turns cumulative CLI events into smooth tokens. Takeaway: delta-tracking makes streaming usable.
- **FastAPI Codex streaming server & UI:** Added a production-ready streaming wrapper and web UI to run Codex in the browser ([dd243d6](https://github.com/sanand0/research/commit/dd243d6d0d64bdecc0880dd6dae143e8b08c4034)) on 10 Nov 2025. Helps demos and debugging without Node SDKs. Takeaway: lightweight Python wrappers unlock experiment speed.
- **Readability extractor evaluation:** Compared 11 HTML→Markdown extractors; recommended Mozilla Readability + Turndown for heading-ID fidelity ([36ad1f2](https://github.com/sanand0/research/commit/36ad1f2d1e1b19fcf8e95e8029c271889c647bf4)) on 11 Nov 2025. This preserves stable headings for RAG. Takeaway: extraction accuracy beats blind tool swapping.
- **Practical notes and artifacts:** Many supporting scripts and detailed reports landed (benchmarks, tests, UIs). See summary edits and README tweaks ([97d47fc](https://github.com/sanand0/research/commit/97d47fcb88a906224b2138011b6177136b64b316)) on 11 Nov 2025. Takeaway: publish reproducible research artifacts.

### [sanand0/prompts](https://github.com/sanand0/prompts)

_More prompts to generate data, diagrams, and fragments—so LLMs return useful, testable outputs._ (Yes, another prompt. You're welcome.)

- **Added practical new prompts:** Added fake-data, reusable fragments, and a mermaid architecture prompt ([595830d](https://github.com/sanand0/prompts/commit/595830d1e3bb4505a0f363aaf7312007fec78889)) on 12 Nov 2025. These speed prototyping and architecture docs. Takeaway: templated prompts reduce iteration time.
- **Mutual-fund and WhatsApp updates:** Added a mutual-fund analysis prompt and clarified WhatsApp extraction tooling ([404b0d8](https://github.com/sanand0/prompts/commit/404b0d817f2341bbde9453a9008176302d37b4ca)) on 10 Nov 2025. More financial and messaging utilities. Takeaway: add examples and tools so prompts are actionable.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Infrastructure scripts tightened agent skills, dev containers, and helper tooling._ (Yes, shell > Python today.)

- **Agent and dev tool refresh:** Reworked skills management, added gitget.sh for sparse clones, and codextools.py for Codex log analysis ([c7617a0](https://github.com/sanand0/scripts/commit/c7617a02611df50b8de7b512f56f036e5496261b)) on 10 Nov 2025. This automates skill imports and log audits. Takeaway: small scripts save hours later.
- **Dev container & uv tooling standardized:** Consolidated uv virtualenv install paths and clarified GH_TOKEN forwarding in the dev Dockerfile and docs ([c7617a0](https://github.com/sanand0/scripts/commit/c7617a02611df50b8de7b512f56f036e5496261b)) on 10 Nov 2025. Helps consistent local builds. Takeaway: a shared dev image reduces onboarding friction.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Weekly newsletter turned podcast episode that turns group chat into a crisp digest._ (Yes, you can skip the thread and listen.)

- **Weekly podcast write-up and outputs:** Published a compact, action-focused podcast for week of 09 Nov 2025 and exported messages for audio builds ([2d0d720](https://github.com/sanand0/generative-ai-group/commit/2d0d720b4928e5af0db173d69b7d3dcc4eb845ac)) on 10 Nov 2025. This packages community insights for reuse. Takeaway: weekly synthesis scales community signal.

### [sanand0/talks](https://github.com/sanand0/talks)

_New slides and resources for the "Applied Vibe Coding" talk, with a shared spreadsheet to collect attendee profiles._ (Yes, slides and a spreadsheet walk into a Zoom.)

- **Added Applied Vibe Coding talk and materials:** New slide deck and supporting README were added ([3e463eb](https://github.com/sanand0/talks/commit/3e463eb41f6a813d833c36b336e676ed0083bf9b)) on 15 Nov 2025. Makes talk materials public. Takeaway: publish materials immediately for reuse.
- **Linked signup/attendance spreadsheet:** Added a spreadsheet link to slides and README ([b3621c5](https://github.com/sanand0/talks/commit/b3621c5491a27827c7631da6c25489e403b13756)) on 15 Nov 2025. That smooths follow-up. Takeaway: simple forms speed outreach.
- **Typos & polish:** Minor copy fixes for clarity ([53f4e24](https://github.com/sanand0/talks/commit/53f4e241091279157b59da4aa2ec8f9f895273ea)) on 15 Nov 2025. Takeaway: polish matters.

### [sanand0/dogfight-codex](https://github.com/sanand0/dogfight-codex)

_A small Three.js arcade demo with tests — games remain great fast prototypes._ (Yes, that jet needs a runway.)

- **Arcade jet demo with tests:** Added a Three.js jet demo plus unit tests and CI-friendly scaffolding ([235c6dd](https://github.com/sanand0/dogfight-codex/commit/235c6ddba40485a9e03d2ce1fe5cddde54d89323)) on 15 Nov 2025. Test coverage makes iteration safe. Takeaway: prototype + tests = confidence.

### [sanand0/dogfight-copilot](https://github.com/sanand0/dogfight-copilot)

_A full 3D flight game implemented with Three.js, ready to play in the browser._ (Yes, arcade flight beats meetings.)

- **Complete 3D flight game:** Implemented a full game loop, HUD, particles, and audio ([7fce3d2](https://github.com/sanand0/dogfight-copilot/commit/7fce3d27619b3a6e739411d5c4bd66b4e31e1c56)) on 15 Nov 2025. It’s a neat, self-contained demo. Takeaway: games are excellent integration tests for graphics and audio stacks.

### [sanand0/dogfight-jules](https://github.com/sanand0/dogfight-jules)

_Another browser flight prototype — small experiments multiply learning._ (Yes, pilots like multiple jets.)

- **3D browser-based flight game:** Added main.js and assets to run a simple Three.js flight demo ([6d73d76](https://github.com/sanand0/dogfight-jules/commit/6d73d76cc44d534ca8a4530e3ab3e998ccd898e1)) on 15 Nov 2025. Quick way to test WebGL pipelines. Takeaway: keep demos focused and shallow.

### [sanand0/test](https://github.com/sanand0/test)

_Quick game builds for the browser — snake is playable and documented._ (Yes, a tiny time-sink that’s wholesome.)

- **Ship a full Snake game:** Added snake.html and polished README for quick play offline ([c9863e8](https://github.com/sanand0/test/commit/c9863e8ce4541c1416db62803a1a33429f1831af)) on 15 Nov 2025. Instant demo, no install. Takeaway: small demos are great delivery units.

### [sanand0/til](https://github.com/sanand0/til)

_Weekly notes captured LLM trends, persuasion tactics, and useful tools._ (Yes, a long brain-dump.)

- **Updated LLM & human-centred notes:** Added insights on Claude, Gemini, Toon format, and persuasion tactics from "How to build a cult" ([ad060d6](https://github.com/sanand0/til/commit/ad060d6b8a6cd5070c553c96b5fcbb0657f0a70f)) on 10 Nov 2025. Takeaway: cross-domain reading spurs better prompts.
- **Curated trending repos:** Pruned and reclassified watchlist entries for focus and relevance. Takeaway: watch fewer, deeper projects.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_Small but crucial change: link to the course ROE for students._ (Yes, exam links belong in READMEs.)

- **Added ROE link and clarified exam refs:** Updated README with R OE link and references ([72d0e44](https://github.com/sanand0/tools-in-data-science-public/commit/72d0e4436472590f4ced5cc84fea12e60040148b)) on 09 Nov 2025. Helps students find the exam resource. Takeaway: course docs must make critical deadlines obvious.

### [sanand0/share-to-clipboard](https://github.com/sanand0/share-to-clipboard)

_Initial scaffolding and license for a small utility repo._ (A tiny repo, but licences matter.)

- **Initial commit + MIT license:** Bootstrapped repo with license ([989fdc0](https://github.com/sanand0/share-to-clipboard/commit/989fdc09d3345ddcbcc328c81dbb85b84677167f)) on 15 Nov 2025. Takeaway: start small, license early.

## Lessons

- Artifacts beat memory: commit PDFs, CSVs, CVs, and generated code. Artifacts make AI work repeatable.  
- Automate boring annexes: scripts that produce CVs, checklists, and builds pay back immediately.  
- Token streaming needs delta-tracking: word-level streaming yields good UX with manageable overhead.  
- Standardize the build once, not later: a single npm/Eleventy flow avoided last-minute mismatches.  
- Test prototypes early: even small demos (games, visualizations) benefit from tests and CI.

## Suggestions

- Finalize the RFP bundle: run the full build + PDF export and a quick audit checklist against the RFP. (Attach final sanitized CVs before submission.)  
- Add a “golden output” test: commit a few canonical outputs (example HTML/PDF, sample CV) and add CI checks to detect accidental drift.  
- Instrument streaming: add small telemetry to token-stream endpoints (token rates, latency) to pick sensible default granularities.  
- Turn prompt recipes into tests: add unit tests that assert a prompt produces structured output for sample inputs.  
- Triage the trending list: keep only 8-12 repos in active watch; archive the rest with a short reason (time saved weekly).