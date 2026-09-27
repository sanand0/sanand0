## A week of polishing interfaces, fixing infra surprises, and turning experiments into stable workflows.

This week was about repairing what we already use, not chasing shiny new toys. Small fixes and tighter tests kept systems reliable and made future experiments repeatable.

### [sanand0/blog](https://github.com/sanand0/blog)

_Keeping the public writing engine tidy so readers (and search bots) find the right thing at the right time._

- **Fix legacy URL & indexing bugs (26 Sep 2026):** Adjusted archive generation and aliases to preserve legacy links and set day pages noindex ([eb9466f5](https://github.com/sanand0/blog/commit/eb9466f5ca16657c697ba7eb7656d22a9f8d550f)). Takeaway: preserving old URLs saves reader confusion.
- **New posts & notes added (26 Sep 2026):** Added essays on Remote Desktop Commander ([f15bf21](https://github.com/sanand0/blog/commit/f15bf21f8415aa7f395aa0669321f36636f17852)) and GPT Image 2.5 Flare quality tests ([8fd50f7](https://github.com/sanand0/blog/commit/8fd50f771f6f9e8645e84fa8bd733f0f507f422e)). Takeaway: short, clear experiments make model trade-offs tangible.
- **Editorial cleanups and assets (26 Sep 2026):** Polished speaker/talk pages, updated prompts and images ([0b14c2c](https://github.com/sanand0/blog/commit/0b14c2c91e92b0594a01c4e5a8bdbda31bce022a)). Takeaway: small presentation fixes greatly improve credibility. (Yes, another photo tweak — we needed it.)

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Secure local tooling and agent plumbing so automation can run without surprise breakages._

- **LocalMCP2 tunnel & mcpserver improvements (21–26 Sep 2026):** Added robust tunnel lifecycle, stateless/http options, and readiness checks ([6b78cc2](https://github.com/sanand0/scripts/commit/6b78cc28ed8ecc8dfeac7d23f96f07a1a812d291), [5cfe690](https://github.com/sanand0/scripts/commit/5cfe690d422f6a5a3d2427ff59cbfb44a9404640)). Takeaway: treat external tunnel runtimes as first-class, flaky resources.
- **LocalMCP2 server polish & tests (21 Sep 2026):** Hardened mcpserver.py, added async-safe file saves, better logging and many tests ([8302d62](https://github.com/sanand0/scripts/commit/8302d6266b295887e295d58cb6dd87a70c4828f7), [018f2c3](https://github.com/sanand0/scripts/commit/018f2c3288f0db985a678d8a396af9157d597950)). Takeaway: heavy testing turns an experimental tool into a safe primitive.
- **UX & small tools (22–26 Sep 2026):** New espanso shortcuts, cctop install, bash/fish helper tweaks, and many system-skill updates ([a65e64f](https://github.com/sanand0/scripts/commit/a65e64fb3b096d959c66f358945daedf5b4fa4f6)). Takeaway: micro-ergonomics matter because people use them every day. (Yes, four hyphens for an em-dash — nostalgia wins.)

### [sanand0/talks](https://github.com/sanand0/talks)

_More workshops and better story tooling so sessions scale from liveliness to repeatability._

- **New talks + prompts + assets (24 Sep 2026):** Added IIS talk package with transcript, context, and prompt links ([a87dc91](https://github.com/sanand0/talks/commit/a87dc9166eefe395a29857a29a9b8a1cb964643e)). Takeaway: store transcripts and prompts for repeatable lessons.
- **Talk-story skill hardening (20 Sep 2026):** Updated generation guides and SKILL.md to avoid stale examples and fix layout bugs ([5b287b6](https://github.com/sanand0/talks/commit/5b287b688b716f0db38f94eb3a1d2cba8da92244)). Takeaway: prefer rules over fragile samples when generating pages.
- **New event pages and prompt links (19–24 Sep 2026):** Added Shree Niketan and IIS workshop content and comic assets ([df01482](https://github.com/sanand0/talks/commit/df01482e6dfb350004199c08b12ccd7e459cb092)). Takeaway: pre-pack talks so you can reuse them without friction. (Yes, the comic page survives another edit.)

### [sanand0/llmartstyle](https://github.com/sanand0/llmartstyle)

_Making generated art gallery deployment predictable and small._

- **Add GPT Image 2.5 Flare thumbnails & WebP flow (25 Sep 2026):** Added Flare thumbnails and verify pixel-dimension checks to avoid bad thumbnails ([b267eb9](https://github.com/sanand0/llmartstyle/commit/b267eb99b9eb92359a092b190299174660f93af7)). Takeaway: auto-generated images need size checks.
- **Simplify WebP deploy & use release WebP assets (25 Sep 2026):** Streamlined generate/upload flow and switched modal images to WebP release assets ([0a3850b](https://github.com/sanand0/llmartstyle/commit/0a3850b0a02835ab0ddce00410a8c43d5c585671), [80aa0f7](https://github.com/sanand0/llmartstyle/commit/80aa0f741cf021051c46f131c061fae5ba8942e7)). Takeaway: separate thumbnail vs full-size life cycles.
- **Document workflow & justfile (25 Sep 2026):** Better README and simple justfile targets for build/deploy ([6e69564](https://github.com/sanand0/llmartstyle/commit/6e695640f9296713227f5484abc7325434c880c7)). Takeaway: docs save you on the next deploy. (Yes, WebP again — less bytes, more smugness.)

### [sanand0/llmevals](https://github.com/sanand0/llmevals)

> _Short experiments, clear results — and fewer surprises._

- **Add GPT Image 2.5 Flare quality benchmark (25 Sep 2026):** Small tool + article to show when quality tiers matter ([ec0c9ee](https://github.com/sanand0/llmevals/commit/ec0c9ee3465aa14cb81929f05fdfa167b33be167)). Takeaway: low/medium often suffice; test on large-detail crops.
- **Lazy-load Flare images & page fixes (25 Sep 2026):** Reduced page load and improved UX for comparisons ([931eb28](https://github.com/sanand0/llmevals/commit/931eb2810d659bced50790c5e2a9150a1500dcaf)). Takeaway: make evidence light to explore.
- **Title and content polish (25 Sep 2026):** Minor copy fix and index update ([c0b4e03](https://github.com/sanand0/llmevals/commit/c0b4e034c8ff9c76670fd28123ea9dbd4bedc314)). Takeaway: readable findings travel farther.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Small data maintenance to keep the frontier chart accurate._

- **ELO & model updates (20 Sep 2026):** Updated elo.csv and model set to reflect current data ([8cbe39d](https://github.com/sanand0/llmpricing/commit/8cbe39d00c1c59a93a8aa7d7e626ed58bd363718)). Takeaway: leaderboards move fast, automate refresh.
- **Skip uncertain end dates (20 Sep 2026):** Cleaned ambiguous time windows to avoid spurious changes ([64d1fc1](https://github.com/sanand0/llmpricing/commit/64d1fc1f432a350e144859eb0cc5dd9b96f8b0b1)). Takeaway: prefer fewer, accurate points.

### [sanand0/private-research](https://github.com/sanand0/private-research)

_Broader experiments and demo builds to keep prototypes repeatable._

- **Optum products demo & data plumbing (22 Sep 2026):** Large UI/story demo updates and added owner-validation pack ingest ([4809cfd](https://github.com/sanand0/private-research/commit/4809cfd7e856230a35ab0378e9227cd97acd12a4)). Takeaway: package examples with testable evidence.
- **ChatGPT workshop archives & automations (10 Sep 2026):** Added scripts and notes for scheduled tasks and workshop artifacts ([eea17fd](https://github.com/sanand0/private-research/commit/eea17fdc4b7576b7b42f71cb73d6f38dddb55d4e)). Takeaway: make "teach sessions" reproducible.
- **Many generated case-study materials (various):** Reproducible generators for demos and lessons. Takeaway: always seed the generator.

### [sanand0/tools](https://github.com/sanand0/tools)

_Maintain scrapers and small web utilities that power other workflows._

- **ChatGPT & Claude scrapers fixed (21–26 Sep 2026):** Updated DOM parsing, tests, and controls for both scrapers ([93f440d](https://github.com/sanand0/tools/commit/93f440d812d798f479925fc3d4de25d622d6e121), [6f4a53b](https://github.com/sanand0/tools/commit/6f4a53b1669175dd59a01b555466b31ad8537637)). Takeaway: UIs move, tests protect you.
- **AIScrapers tests & fixtures (21–26 Sep 2026):** Extended fixtures and unit tests to cover new DOM shapes ([93f440d...](https://github.com/sanand0/tools/commit/93f440d812d798f479925fc3d4de25d622d6e121)). Takeaway: test-first scraping avoids surprises.
- **Small utilities & prompt updates (26 Sep 2026):** Prompted updates and test hardening for reliability ([6f4a53b](https://github.com/sanand0/tools/commit/6f4a53b1669175dd59a01b555466b31ad8537637)). Takeaway: scrape only what you need.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Making weekly podcast generation resilient and cheaper._

- **Revamp podcast workflow (26 Sep 2026):** Switched to GPT-6 Luna for script and Gemini 3.8 Flash Lite for TTS, plus resumable chunking and caching ([5878b29](https://github.com/sanand0/generative-ai-group/commit/5878b29f5a9aa7944e1604b22a73cda1c757a326)). Takeaway: chunked TTS + cache = predictable cost.
- **New episode and content (20 Sep 2026):** Added a polished show script for week of 20 Sep ([6ec9da7](https://github.com/sanand0/generative-ai-group/commit/6ec9da726641791b720a22dd91d1867a7e6cf9fb)). Takeaway: script-first helps quality control.
- **Tests updated for new models (26 Sep 2026):** Adjusted tests to assert new model/format metadata and dry-run returns ([6f4a53b...tests](https://github.com/sanand0/generative-ai-group/commit/6f4a53b1669175dd59a01b555466b31ad8537637)). Takeaway: tests prevent silent API-compat regressions.

### [sanand0/codex-model-switcher-rust](https://github.com/sanand0/codex-model-switcher-rust)

_Turning a Windows tool into a cross-platform, well-tested Rust service._

- **Major cross-platform build & GUI (22 Sep 2026):** Added proxy, GUI, credential store, tests, packaging helpers and many modules ([e5f5428](https://github.com/sanand0/codex-model-switcher-rust/commit/e5f5428ea9a2d8672918ad6f2b5285f8edad0855)). Takeaway: keep core logic OS-agnostic; adapt lifecycle per OS.
- **Network & credential hardening (22 Sep 2026):** Safe proxy headers, stateless HTTP option, credential abstraction and local fallbacks ([src/credential.rs](https://github.com/sanand0/codex-model-switcher-rust/blob/main/src/credential.rs)). Takeaway: credentials are the bottleneck for cross-platform UX.
- **Packaging and reproducible build scripts (22 Sep 2026):** Added package.py and tests for native artifacts. Takeaway: release artifacts must be reproducible and testable. (Yes, the Windows installer can wait.)

### [sanand0/sutd-tds-proposal-2026-09-21](https://github.com/sanand0/sutd-tds-proposal-2026-09-21)

_Making an academic analysis reproducible and distributable._

- **Pipeline & executable steps (22 Sep 2026):** Turned each pipeline step into deterministic scripts and package-local tooling ([de4bf9a](https://github.com/sanand0/sutd-tds-proposal-2026-09-21/commit/de4bf9ab7d40e4daf6ae46ef988c7f0c9eb15983)). Takeaway: reproducible pipelines make reviews credible.
- **One-command quickstart and packaging (22 Sep 2026):** Added prepare/package-local and detailed run steps. Takeaway: ship data bundles with precise commands.

### [sanand0/llms-in-finance-book](https://github.com/sanand0/llms-in-finance-book)

_Applying editorial rigor across chapters._

- **Apply BPB review rules across chapters (21 Sep 2026):** Enforced chapter structure, DOCX style guidance, and validation scripts ([314e592](https://github.com/sanand0/llms-in-finance-book/commit/314e5921a076b4d07f4d6e40bb0fba79fe7372d8)). Takeaway: consistent formatting prevents review churn.
- **Validation & tooling (21 Sep 2026):** Added validate-preliminary-draft.py and editorial rules for authors. Takeaway: automated checks catch style regressions early.
- **Chapter rewrites and prompts (21 Sep 2026):** Reworked outline and prompts to match publisher expectations. Takeaway: align writing with production requirements.

### [sanand0/infra](https://github.com/sanand0/infra)

_Fixing hardware and packaging surprises: crucial but dull work that prevents noisy outages._

- **NVIDIA/kernel investigations & docs (21 Sep 2026):** Added diagnostics, upgrade notes, and safe advice for a mixed-kernel NVIDIA state ([34264e1](https://github.com/sanand0/infra/commit/34264e112ce4e2fe96781ee2df7b47f04f267b04)). Takeaway: never reboot without a recovery path.
- **Large infra archives and troubleshooting scripts (20–21 Sep 2026):** Captured long diagnostic traces and repair scripts for reproducibility ([2026-08-20-diagnostics-v1.txt](https://github.com/sanand0/infra/blob/main/docker-nvidia-issue/2026-08-20-diagnostics-v1.txt)). Takeaway: trace-first debugging saves hours.
- **Advice & README guides (21 Sep 2026):** Documented step-by-step safe repair options and when to call vendor service. Takeaway: minimal-change fixes first, escalations next.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Curation and small ETL so public stories stay accurate and easy to rebuild._

- **Glassdoor pipeline robustness (21 Sep 2026):** Made capture and extract idempotent, atomic file writes, and added tests ([d3e633d commit set](https://github.com/sanand0/datastories/commit/d3e633de925426fc72b9940d17ec1a50a00edaf7)). Takeaway: fragile scrapers need atomic saves.
- **Update scripts & README (21 Sep 2026):** Added update_glassdoor.py and clear README for maintainers. Takeaway: doc the scrape lifecycle.
- **Tests & fixtures (21 Sep 2026):** New fixtures to track modern DOM shapes and avoid breakages. Takeaway: catch UI drift early.

### [sanand0/case-studies](https://github.com/sanand0/case-studies)

_Reproducible instructional packs for workshops and exercises._

- **Large generator & validation additions (20–22 Sep 2026):** Added multiple case generators (customs, DTH, design-impact, consumer-products) and validation scripts to ensure non-leakage ([e5e98cf](https://github.com/sanand0/case-studies/commit/e5e98cf29fab63b45681faf233ecde92a3cf4761)). Takeaway: seeded generators keep exercises fair.
- **Instructor guides + manifests (20–22 Sep 2026):** Built README and validation reports for instructors. Takeaway: pack authorship = reproducibility.
- **Automated checks and reproducible seeds:** Ensure builds are deterministic for grading repeatability. Takeaway: test your tests.

### [sanand0/research](https://github.com/sanand0/research)

_Quick verification notes and small independent experiments._

- **Cyphral Distich provenance check (20 Sep 2026):** Reproduced Fable/Claude plaintext vs 1834 scan and flagged a provenance gap with 1653 source ([cb293e5](https://github.com/sanand0/research/commit/cb293e5e3224a09171219447e0d94698abbd6636)). Takeaway: verify both model output and source provenance.
- **Small verification script + CSV outputs:** Emit coordinate CSV for transparency. Takeaway: experiments should publish minimal reproducible artifacts.

### [sanand0/til](https://github.com/sanand0/til)

_Short notes to remember useful links and facts._

- **Weekly captures & links (20–22 Sep 2026):** Added quick items about Cloudflare quick tunnels, Anthropic protein funding, and model benchmarking links ([2285fbd](https://github.com/sanand0/til/commit/2285fbd09f02b4190e8e5fd3ca95f417848a9bf1)). Takeaway: small links accumulate into big reference.

## Lessons

- Test first, then fix: UI and infra drift are inevitable. Tests and idempotent writes save hours.  
- Treat external runtimes (tunnels, proxies, skill runtimes) as flaky components. Add readiness, health checks, and clear restart semantics.  
- Chunking + cache beats "bigger model" economics for long-running multimodal tasks (podcast TTS, image generation).  
- Reproducibility wins for teaching: seeded generators + validation scripts make exercises fair and reviewable.  
- Verify both model answers and source provenance; a correct-looking output can rest on a non-existent historical source.

## Suggestions

- Automate end-to-end smoke tests for LocalMCP2 and model switcher proxies on startup. Add health dashboards that can auto-repair the managed runtime.  
- Add a small “safety checklist” runner for infra upgrades: preflight package diffs, kernel-module parity, and a non-destructive rollback plan.  
- For generated-media repos, add a tiny “verify thumbnail size” CI job. It avoids stale thumbnails breaking pages.  
- Turn the podcast chunking/cache pattern into a reusable library across projects. It’s useful for many TTS tasks.  
- For teaching packs, add a short instructor checklist that runs validate scripts and lists any human-only artifacts before opening the room.

If you want, I can: (1) generate a compact checklist for LocalMCP2 runbooks, (2) open a small PR template for infra kernel-driver upgrades, or (3) produce a before/after cost calc for switching podcast TTS tiers. Which would help most?