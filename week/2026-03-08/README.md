## A week of building show-and-tell: demos, replays, and practical AI tooling that teachers and devs can actually use.

Small, repeatable infra (better docs, CI tweaks, upload scripts) unlocked bigger demos. When data, demos, and a tidy script meet, stakeholders start understanding instead of guessing.

### [sanand0/rustom](https://github.com/sanand0/rustom)

_Crafted a tiny multimedia studio in Rust so your terminal can render art, music, and dashboards in real time._

- **New procedural terminal cosmos:** Added the core Rust Aurora app and CLI instructions ([a00df0f](https://github.com/sanand0/rustom/commit/a00df0f779228c24fd46ee44669d2fd3eea03737)) with presets and terminal-aware defaults. Why it matters: quick visual playgrounds help test rendering ideas. Takeaway: small demos make abstract visuals tangible.
- **Cinematic renderer, parallelized:** Implemented LumenForge path tracer and parallel worker threads ([c4af459](https://github.com/sanand0/rustom/commit/c4af459302889d2e49719879eda4d7f39d5c34db)); documented `--threads` ([4206440](https://github.com/sanand0/rustom/commit/4206440a822eb4a815ede9b038619824ae48f004)). Why it matters: faster renders, usable on desktops. Takeaway: parallelism buys real productivity.
- **Procedural music engine:** Built SonicLoom to generate WAV tracks and export arrangement JSON ([3f49a65](https://github.com/sanand0/rustom/commit/3f49a65acdad75dab8840d655d7703c2034da4c3)), and added `--arrangement-out` docs ([872f438](https://github.com/sanand0/rustom/commit/872f4380a8a113cc09628e5eddbb4c332f77876a)). Why it matters: reproducible generative audio for demos and scoring. Takeaway: data + audio metadata = replayable art.
- **High‑FPS TUI ops dashboard:** Scaffoled and shipped PrismDash, a modern Ratatui dashboard binary ([c22d45a](https://github.com/sanand0/rustom/commit/c22d45a7ff8249b0dda0502c7d7ada7209d23119)) and full feature implementation ([a6fb1cf](https://github.com/sanand0/rustom/commit/a6fb1cf0e11631f3ccb033e96fe657f27edc3533)). Docs updated to show usage and session prompts ([414043f](https://github.com/sanand0/rustom/commit/414043fbf5e8921cf22d8e997bc6235b578e2df4)). Why it matters: operations-style demos help non-engineers grasp telemetry. Takeaway: ship one interactive thing, and people understand the rest. (Yes, you really needed another terminal toy.)

### [sanand0/pyoppe](https://github.com/sanand0/pyoppe)

_Brought student coding replays, narratives, and teachable targeting into reproducible analysis artifacts._

- **Interactive replay gallery:** Added an asciinema cast generator and a replay catalog ([a3f9dbe](https://github.com/sanand0/pyoppe/commit/a3f9dbe1cd2f7e7b8c3a56c7729dc54d0032a6b9)) plus massive `analysis/replays.html` and synchronized JSON narratives ([8653380](https://github.com/sanand0/pyoppe/commit/86533808f25c58c0f99e345b759e8f532ec5fac0)), 05 Mar 2026. Why it matters: you can “watch” students, not just chart them. Takeaway: time-aligned examples teach diagnosis.
- **Replay reliability fixes:** Fixed player initialization race and CRLF frame output for better playback portability ([4f88180](https://github.com/sanand0/pyoppe/commit/4f88180ed0e46e893607e0e7cb29c7cd224584cd), [d760f22](https://github.com/sanand0/pyoppe/commit/d760f22dd7a8c0c8f3e59cd6923ea7edb2a92f10)), 05 Mar 2026. Why it matters: stable replays are shareable across OSes. Takeaway: small EOL and mount fixes avoid big demo friction.
- **Teachable segmentation + tracked CSV:** Added a process-first teachable classifier and published `analysis/teachable.csv` in git for story pages ([3bcab33](https://github.com/sanand0/pyoppe/commit/3bcab33cf671460c9f8268aa52a78aa952a81840), [46d60a3](https://github.com/sanand0/pyoppe/commit/46d60a31b9ea536804cc338cae59678c5dbbb4ab)), 04 Mar 2026. Why it matters: operational lists for mentors become reproducible. Takeaway: commit the canonical CSV you depend on.
- **Behavioral analyses and AGENTS guidance:** Added thrashers language analysis (`thrashers_language.py`) and rewritten buddy-program evaluation in lay terms; added AGENTS.md with reproducibility rules ([b0c0894](https://github.com/sanand0/pyoppe/commit/b0c0894bdba6b94a436bfb6c9d686f2d6e37cac8), [9fd711e](https://github.com/sanand0/pyoppe/commit/9fd711e16dd5787a1a7ae3c4710e136d0c9b9d0e)), 04–05 Mar 2026. Why it matters: analyses now recommend operational fixes. Takeaway: pair analysis with clear actionables.

### [sanand0/blog](https://github.com/sanand0/blog)

_New posts and site polish to capture experiments and educational findings._

- **Nano Banana Paradox case study:** Added a long-form Gemini image-generation post and expert critique ([ca96dac](https://github.com/sanand0/blog/commit/ca96dac0961b7a9941c783bedd03e462656353dd)), 07 Mar 2026. Why it matters: documents model failure modes and prompt lessons. Takeaway: publish experiments with images and critique.
- **Which LLMs get you better grades:** Added an empirical post comparing student outcomes by model ([25f513b](https://github.com/sanand0/blog/commit/25f513b9b118d34180c5439df43c41e51f55cec9)), 06 Mar 2026. Why it matters: instructors get actionable correlations. Takeaway: model choice often correlates with outcomes.
- **Prompt library and docs reorg:** Reworked prompt fragments and examples for reuse ([b2a4903](https://github.com/sanand0/blog/commit/b2a49034ec171550dcbe59232eeec98fa9c477f0)), 05 Mar 2026. Why it matters: makes prompt reuse faster. Takeaway: tidy fragments, less copy-paste.

### [sanand0/talks](https://github.com/sanand0/talks)

>A lot of narrative polishing: transcripts, sketchnotes, and formatted talk pages for reuse.

- **Vibe Coding for Humanities page:** Published a Malcolm-Gladwell style narrative, sketchnote, video embed, and six takeaways ([4cdf4fc](https://github.com/sanand0/talks/commit/4cdf4fc60c524d7bf9b86d1990ce15f911a0fb21)), 05 Mar 2026. Why it matters: turns a workshop into a long-lived resource. Takeaway: a good transcript + design = reusable teaching artifact.
- **Added Rajen Makhijani talks and transcripts:** Imported two Rajen talks with full transcripts and HTML pages ([ca838ac](https://github.com/sanand0/talks/commit/ca838acbd32a8c9d5b66fef25b6261d3d442f20e)), 05 Mar 2026. Why it matters: preserves interviews and makes them searchable. Takeaway: small metadata work multiplies discoverability.
- **Deploy & ignore policy tweaks:** Flipped per-directory ignores and updated Pages workflow to run setup.sh ([d2c52bc](https://github.com/sanand0/talks/commit/d2c52bc07e5ffb2baa4300b9c7c44116c85cbf28), [524652b](https://github.com/sanand0/talks/commit/524652b45d99eb70427a450717e4aa1e44813844)), 04 Mar 2026. Why it matters: predictable deploys and included HTML. Takeaway: CI and ignores deserve careful thought.

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

>Polished the demo site and automated publishing hooks for Pages.

- **Modern template and search UI:** Overhauled the static template with responsive hero, search, and badges ([82b3f6b](https://github.com/sanand0/llmdemos/commit/82b3f6be7bce5fce1c91ef1e501f921287cafabb)), 05 Mar 2026. Why it matters: visitors find demos faster. Takeaway: small UX upgrades improve demo conversion.
- **Generate demos.csv at build time:** Added a uv script and CI step to produce demos.csv for Pages builds ([30a79c8](https://github.com/sanand0/llmdemos/commit/30a79c8b1dd8a1efc90fddd3232994cf1e7b368d)), 05 Mar 2026. Why it matters: keeps the catalog in sync. Takeaway: generate, don’t hand-edit.
- **Metadata refresh + .env ignore:** Large config refresh and safe .env ignore ([e4f8294](https://github.com/sanand0/llmdemos/commit/e4f82942ef35ca52903dc687896727c61efe724d), [944cafc](https://github.com/sanand0/llmdemos/commit/944cafc9b72fd40f42712a367a7c08500edb9440)), 05 Mar 2026. Why it matters: clearer demo metadata and no leaked secrets. Takeaway: curate metadata early.

### [sanand0/journalists](https://github.com/sanand0/journalists)

>Experimented with data-led news graphics and reporter prompts.

- **Investigative West Bengal piece:** Drafted a deep story about voter-roll revision and reporting flags ([83cb4fe](https://github.com/sanand0/journalists/commit/83cb4feb14230688b2d28cc12a3edb834a6e575d)), 02 Mar 2026. Why it matters: shows how AI-sourced drafts can scaffold reporting. Takeaway: use AI as a research assistant, not a publisher.
- **Statnostics infographics experiments:** Built multiple poster-style visual drafts and prompt experiments for compact data narratives ([3302788](https://github.com/sanand0/journalists/commit/3302788429777d8ecf55a47b5d7f149e6edce1de)), 02 Mar 2026. Why it matters: fast-turn visual tests clarify narrative hooks. Takeaway: keep graphics minimalist for shareability.
- **Prompt & tooling scaffolding:** Added research prompts and automation notes for story selection and follow-ups. Why it matters: reproducible reporting workflows scale faster. Takeaway: templates speed editorial judgment.

### [sanand0/schoolai](https://github.com/sanand0/schoolai)

>Built a demo-grade financial-aid intake pipeline and a playable front-end.

- **Financial-aid demo dataset + UI:** Added synthetic applicant bundles, a demo dataset, and heavy UI scripting for simulated replay and intake ([6ce5b7c](https://github.com/sanand0/schoolai/commit/6ce5b7cc83fd4c162c2d4a184b9d0125e5aa3484)), 02 Mar 2026. Why it matters: concrete demos help administrators see value. Takeaway: realistic synthetic data makes conversations practical.
- **Homepage and prompt improvements:** Added home-page prompts and UX guidance for demos ([6b65cca](https://github.com/sanand0/schoolai/commit/6b65cca02875c7afa777b8c171cd56340d2794e4)), 02 Mar 2026. Why it matters: better narratives sell pilot ideas. Takeaway: start with one clear workflow for stakeholders.

### [sanand0/llmartstyle](https://github.com/sanand0/llmartstyle)

>Iterated on image-generation tooling and release ergonomics for art prompts.

- **Nano‑banana‑2 (Gemini) support + UI polish:** Added Gemini nano-banana-2 model, hover previews, and modal keyboard nav ([da921b9](https://github.com/sanand0/llmartstyle/commit/da921b9f2a7be487df2640e1ae53677c63bf142d)), 06 Mar 2026. Why it matters: new model yields distinct styles. Takeaway: keep UI nimble for large image grids.
- **Selective release uploader:** Added upload.sh and docs for uploading only new assets to releases ([ce9ceb8](https://github.com/sanand0/llmartstyle/commit/ce9ceb8009b4fb5a2dc72d4143cdb55b2a8f9585)), 06 Mar 2026. Why it matters: avoids repeatedly reuploading large assets. Takeaway: small release tools save bandwidth and time.

### [sanand0/datastories](https://github.com/sanand0/datastories)

>More automated storytelling: interview→transcript→deck, plus a Codex session audit.

- **Codex-session gap analysis:** Added a large analysis pipeline and a narrative report showing adoption gaps across 903 sessions ([8b7c712](https://github.com/sanand0/datastories/commit/8b7c71230900698ec424ba7e888f4deb74ac6ac6)), 01 Mar 2026. Why it matters: identifies how users miss new features. Takeaway: measure usage before coaching.
- **Decktation: auto-slide from audio:** Added a transcript-to-deck pipeline and three slide exports (Claude/Gemini/Codex variants) ([445d5bb](https://github.com/sanand0/datastories/commit/445d5bbae6009044e5e72bbdad9b9af53af8a354)), 05 Mar 2026. Why it matters: turns interviews into board-ready decks. Takeaway: automation shrinks prep time for stakeholder briefings.

### [sanand0/scripts](https://github.com/sanand0/scripts)

>Desktop ergonomics and agent workflows got a lot more keyboard-friendly.

- **Rofi clipboard & prompt pickers:** Added rofi-clip.sh and rofi-prompts.sh for fast clipboard transforms and prompt insertion ([e0049d7](https://github.com/sanand0/scripts/commit/e0049d7b79d142e23b64fe9ce2c2a383ca8250a6)), 02 Mar 2026. Why it matters: reduces repetitive copy-paste. Takeaway: muscle-memory shortcuts multiply productivity.
- **Keybinding & setup updates:** Updated setup.fish, media keys, and agent guidance; removed duplicate scripts and centralized transforms ([e0049d7](https://github.com/sanand0/scripts/commit/e0049d7b79d142e23b64fe9ce2c2a383ca8250a6)), 02 Mar 2026. Why it matters: consistent UX across machines reduces onboarding friction. Takeaway: standardize the small stuff.
- **Security & dev tweaks:** Improved dev image secret handling and container defaults. Why it matters: safer local builds. Takeaway: keep secrets out of layers.

### [sanand0/til](https://github.com/sanand0/til)

_Notes and discovery snapshots to seed ideas and weekly writing._

- **Weekly updates & trending snapshot:** Added Feb–Mar notes and a fresh trending-repos.tsv snapshot ([6e0482e](https://github.com/sanand0/til/commit/6e0482e434a3b405cf9cccd5257323c445379aea)), 01 Mar 2026. Why it matters: preserves sparks before they go cold. Takeaway: a small dated file beats a forgotten idea.

## Lessons

- Ship small, observable demos. A single interactive example beats a thousand slides.
- Automate publishing pipelines early. Generated artifacts (CSV, demos.csv) reduce manual drift.
- Playbooks > guesswork. Pair analysis with reproducible steps and a “what to do next” list.
- UX fixes are high leverage. Tiny player/CRLF and README fixes remove demo friction fast.
- Teachability beats raw scores. Process-first segmentation finds students you can help now.

## Suggestions

- Record short demo walkthroughs (30–60s) for prismdash, sonicloom, and replays. Use asciinema or screencast.
- Add end-to-end smoke tests for replay pages (load rec → sync → highlight). CI catchers prevent regressions.
- For SchoolAI, run a 1‑week pilot with 5 advisors and the teachable CSV; measure handoff time.
- For llmartstyle, add automated perceptual checks (thumbnail diff) before uploads to avoid bad artifacts.
- Capture a “before/after” of Fish startup and rofi shortcuts to measure real UX wins.

If you want, I can draft the short demo scripts (what to record and what to narrate) for prismdash, replays, and the financial-aid flows.