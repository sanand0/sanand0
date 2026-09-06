## A week of careful publishing, safer agents, and practical demos

Small, durable wins this week: posts, experiment pages, and tools that make verification, reproducibility, and cross-source context easy. The key lesson: build things that survive human review and noisy inputs.

### [sanand0/blog](https://github.com/sanand0/blog)

_Content-driven changes made the site easier to use and easier to regenerate programmatically—publishable evidence beats vague notes._

- **New keynote post:** Added "How I Verify And Delegate to AI" with examples and embeds ([3f3c625](https://github.com/sanand0/blog/commit/3f3c625)), 05 Sep 2026. It turns talk notes into reproducible verification techniques. Takeaway: publish your workflow logs; others reuse them.
- **Question pipeline:** Added a generator + page for "Questions I am asked" and TIL wiring ([b2cc913](https://github.com/sanand0/blog/commit/b2cc9131)), 31 Aug 2026. It converts dated rows into weekly posts and TIL updates automatically. Takeaway: canonical source → deterministic output reduces edit errors.
- **Prompt & style tightening:** Tweaked writing-style SKILL and prompt fragments for clearer LLM smells ([216606b](https://github.com/sanand0/blog/commit/216606b9) + [216606b changes]), 30 Aug 2026. This trims over-earnest phrasing and keeps outputs usable. Takeaway: make your style rules machine- and human-friendly.
- **Small fresh posts & fixes:** Added "Swearing at passwords" ([5bc9c6e](https://github.com/sanand0/blog/commit/5bc9c6e3)), fixed breadcrumb schema test ([15b1ec4](https://github.com/sanand0/blog/commit/15b1ec4)), 31 Aug / 30 Aug 2026. Little posts and test fixes keep the archive honest. Takeaway: commit small readable artifacts often. (Yes, another blog post — someone had to do it.)

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Local tooling grew a local context index, hardened agent infra, and fixed fragile scrapers._

- **Local cross-source index:** Added a deterministic SQLite context index with CLI and tests ([7cfbab6](https://github.com/sanand0/scripts/commit/7cfbab6610dca44be43c16b748c439ab111222cc)), 05 Sep 2026. Query emails, chats, transcripts and get source-preserving locators. Takeaway: index before you claim facts.
- **System agent tooling:** Large improvements to the system-agent scripts, validators, and imagegen helpers ([d48f2de](https://github.com/sanand0/scripts/commit/d48f2decdcae4f539f90b87d39f6f35eb69a4a68)), 05 Sep 2026. Better parsing, args, and error messages for robust skill/plugin creation. Takeaway: validation up front saves debugging time.
- **Backup & scraper resilience:** Fixed WhatsApp backup to avoid virtualized-row bugs and added regression tests ([cbeb6c1](https://github.com/sanand0/scripts/commit/cbeb6c19f4291f9c8cc00eb30649d0fa5a7e1655)), 05 Sep 2026. Now recovers image-only messages and logs runs. Takeaway: scrapers must assume virtualized DOMs are lying.
- **Cleaner transcripts & speaker extraction:** Improved speaker detection and metadata filters in summarizer ([9240180](https://github.com/sanand0/scripts/commit/92401804850a637802df5ecd8e07d3ee54d0b61a)), 02 Sep 2026. Avoids treating "Team" or "Speaker 1" as real names. Takeaway: filter roles before you make people lists. (Less guessing, more human names. Good.)

### [sanand0/private-research](https://github.com/sanand0/private-research)

[Private work; public deploys noted] Built a demo-grade Optum portfolio model, deployed VIA talk pages, and shipped a CSAT analysis build.

- **Optum portfolio:** Added a deterministic portfolio build, analysis, and interactive demo scripts ([382e5b2](https://github.com/sanand0/private-research/commit/382e5b2aac734c5e93beda307f922d31af1fbe26)), 05 Sep 2026. Outputs CSVs, SQLite and demo data for a producible story. Takeaway: make messy enterprise inputs deterministic for repeatable analysis.
- **Deployed portfolio demo:** Added simple deploy justfile for r2 storage ([3f1fb8d](https://github.com/sanand0/private-research/commit/3f1fb8dd6ea78e499a9c86de1f2015bfdf442d18)), 05 Sep 2026. One command pushes demo artifacts to r2. Takeaway: deployment shortcuts make demos shareable.
- **CSAT build & site:** Added a reproducible CSAT builder and templates ([3af659c](https://github.com/sanand0/private-research/commit/3af659c3563973f8b00bae5f5974d51a24fb2556)), 02 Sep 2026. Generates rich interactive HTML and stats for stakeholder review. Takeaway: bake analysis into a single reproducible script.

(Wry aside: yes, you get another demo. This one argues with spreadsheets.)

### [sanand0/research](https://github.com/sanand0/research)

Experimental labs: video experiments with Gemini Omni, WebMCP exploration, and improved writing-style tooling.

- **Gemini Omni experiments:** Added the Omni 1.1 Flash experiments, prompts, and cost ledger ([ea5022e](https://github.com/sanand0/research/commit/ea5022e14d37bf75bdc073d7643c36ef2525c4ed)), 05 Sep 2026. Scripts generate, assemble, and estimate API cost for transparent edits and motion transfer. Takeaway: keep per-run cost and provenance with every generated asset.
- **WebMCP exploration:** Added long-run WebMCP workflows, failure modes, and repro scripts ([ea5022e](https://github.com/sanand0/research/commit/ea5022e14d37bf75bdc073d7643c36ef2525c4ed)), 05 Sep 2026. Shows tool discovery races and file handoff limits. Takeaway: prefer semantic tools but broker artifacts at the host.
- **LLM writing-style tooling:** Improved scoring UI, judgments, and front-end for style experiments ([392716b](https://github.com/sanand0/research/commit/392716bfe98aaa9c28f77d9e1e31e25dd83a11ae)), 31 Aug 2026. Adds scoring script and judge UI to measure writing axes. Takeaway: instrument taste with measurable axes, not anecdotes.

### [sanand0/talks](https://github.com/sanand0/talks)

Conference-first workflow: survey, live visualizations, and verification checklists for the Jio Convergence keynote.

- **Convergence talk pages:** Added live survey, visuals, and talk notes for Jio Institute Convergence ([ee701a3](https://github.com/sanand0/talks/commit/ee701a30b0a13598b0a80b15783b96b70eb7cda2)), 03 Sep 2026. This includes survey results and interactive pages. Takeaway: run quick audience surveys; they make live talks practical.
- **Formatting & logistics tweaks:** Fixed chat formatting and copy phrasing ([c64b1eb](https://github.com/sanand0/talks/commit/c64b1eb8987f55db51d13a7e9a7221afed177668)), 05 Sep 2026. Small edits that avoid awkward ChatGPT markup on the page. Takeaway: tiny wording fixes avoid big confusion on stage.
- **Logistics polishing:** Minor README rewordings for travel, internet, and badge notes ([f96710a](https://github.com/sanand0/talks/commit/f96710a3cf3f9ef4604607a3cd3559e54bb72838)), 03 Sep 2026. Makes event ops smoother. Takeaway: make logistics friction minimal; speakers remember the friction, not the talk.

Light aside: yes, there is now a survey link and you might get asked one question from it.

### [sanand0/til](https://github.com/sanand0/til)

_Notes updated to reflect recent research and benchmarks._

- **TIL updates:** Added notes/update to LLMS and weekly TIL entries ([801d0be](https://github.com/sanand0/til/commit/801d0beebd33e5986ff147b172620038744481f9)), 30 Aug 2026. Kept public weekly learnings in sync. Takeaway: commit learning as soon as it's fresh.

### [sanand0/straivex-skills](https://github.com/sanand0/straivex-skills)

_A small new repo for StraiveX skills and CI mirroring._

- **Repo bootstrapped:** Created initial README and lightweight content ([d39475f](https://github.com/sanand0/straivex-skills/commit/d39475f7930daafcc720596db67753fb18bf346a)), 03 Sep 2026. Takeaway: start small; iterate publicly.
- **Added CI mirroring:** GitLab job to mirror GitHub branches/tags ([8fbc1ea](https://github.com/sanand0/straivex-skills/commit/8fbc1eaa6b2fd55c07178f439bbbc53941adb075)), 03 Sep 2026. Keeps mirrors honest. Takeaway: automating mirrors reduces accidental drift.
- **Tiny doc tweaks:** Minor README edits ([dad5713](https://github.com/sanand0/straivex-skills/commit/dad571369f7595cb31dcdc65630dee0e0fb04f53)), 04 Sep 2026. Takeaway: documentation is cheap insurance.

### [sanand0/contractanalysis](https://github.com/sanand0/contractanalysis)

_Site housekeeping and deployment fixes._

- **Pages deploy change:** Removed CNAME to deploy under GitHub Pages (`ae9fb36`) 03 Sep 2026. This unblocks serving at sanand0.github.io/contractanalysis. Takeaway: small DNS cleanups avoid long waits. (Yes, DNS is still magic.)

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Podcast and weekly digest maintenance._

- **Updated podcast notes:** Added the August digest episode and show notes ([6452e35](https://github.com/sanand0/generative-ai-group/commit/6452e3558cc04fbb828a84e09482f2bf544bf295)), 30 Aug 2026. Keeps the weekly audio narrative fresh. Takeaway: small media updates keep community momentum.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Tighter model updates, robust UI, and pareto analysis fixes._

- **Robust updater & tests:** Improved elo updater, added tests, and made expiry handling conservative ([9007e9d](https://github.com/sanand0/llmpricing/commit/9007e9d3678739171ab4a4a8a33487035491833f)), 30 Aug 2026. Now refuses malformed end dates and preserves known ends. Takeaway: prefer conservative changes over silent guesses.
- **Better Pareto UI & tests:** Added pareto logic, front-end ordering, and tests ([9007e9d additions]), 30 Aug 2026. Ensures the plot draws recent models on top and computes dominance correctly. Takeaway: visual layers matter; paint newest, compute exact.
- **Narrative & data refresh:** Updated narrative timeline and build flow, migrated to `just build` ([README changes]), 30 Aug 2026. Takeaway: make the update path scriptable and repeatable.

## Lessons

- Build for verification first. Instrument everything with provenance, tests, and resumable state.
- Small UX fixes compound. Correct ordering, paint layers, and sticky headings matter for human comprehension.
- Index and normalize local context before trust: a fast SQLite index beats ad-hoc greps.
- Prefer deterministic artifacts (CSV, JSONL, MP4 + metadata). They let you replay, debug, and audit.
- Automate conservative defaults. Don’t infer expiry or overwrite authoritative fields silently.

## Suggestions

- For blog: add a short, automated smoke test that verifies all new embeds load (iframes, images). It finds broken pages early.
- For scripts: run a weekly context-rebuild on a low-cost schedule and output a freshness report to Slack or email.
- For research demos: publish a small "how to reproduce" README with the exact model seed, prompt, and cost summary next to every output.
- For talks: convert the audience survey into a compact CSV pipeline that feeds the live visuals. Store a verified copy of responses in the context index.
- For llmpricing: add a nightly dry-run of update pipeline that checks only diffs and posts a changelog PR for human approval.

If you want, I can: (A) render a short "how-to" that walks through reproducing one video experiment, (B) draft the GitHub Actions workflow to run blog smoke tests, or (C) expand any repo section into a one-page changelog suitable for release notes. Which would help most?