## A week of better pipelines, richer stories, and more agent-friendly tools

We focused on shipping durable automation, reproducible research, and content pipelines. The biggest lesson: glue tooling and clear I/O beat heroic one-off hacks.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Turn messy WhatsApp exports into weekly, testable podcast inputs so you can automate reliably and avoid leaking raw data._

- **Weekly podcast scripts added.** Added many weekly podcast transcripts and episode files to create a reproducible show archive ([4bd7819](https://github.com/sanand0/generative-ai-group/commit/4bd7819cda22b6c6c5984c213d6705b6af111de7)) on 28 Mar 2026. Takeaway: keep final scripts in repo, not raw exports.
- **Split/merge WhatsApp exports.** New tool `split_whatsapp_messages.py` merges and writes weekly shards ([4a9cd4a](https://github.com/sanand0/generative-ai-group/commit/4a9cd4ae9310e5b5f0871b874b39abd2c040bce5)), plus tests (28 Mar 2026). Takeaway: shard early; small files reduce accidental reprocessing.
- **Safe dry-run & structured flow.** Podcast generator gained a dry-run mode and now consumes week folders rather than one giant file ([4a9cd4a](https://github.com/sanand0/generative-ai-group/commit/4a9cd4ae9310e5b5f0871b874b39abd2c040bce5)), 28 Mar 2026. Takeaway: build a no-API dry-run to validate pipelines without cost.
- Aside: yes, you really needed nicer weekly files. Humans and agents both hate big JSON blobs.

### [sanand0/talks](https://github.com/sanand0/talks)

_More automated storytelling: skills to convert slides and transcripts into magazine-style HTML pages._

- **Talk-story Claude skill added.** New `.claude/skills/talk-story/` with generation guide and PDF→image scripts ([ba73a8a](https://github.com/sanand0/talks/commit/ba73a8ace2b9cbdf6b34c257a154d639c2992646)), 26 Mar 2026. Takeaway: ship structured skills so a skill can be audited and re-run.
- **Large, polished talk pages.** Added Rob Schrauwen TUG talk HTML, sketchnote, and transcript pages ([2a9d623](https://github.com/sanand0/talks/commit/2a9d623d43bd15f1c3bd1f7eee06f0d5f1a54827)), 23 Mar 2026. Takeaway: publish final HTML alongside source transcripts.
- **Multi-model drafts and comparisons.** Generated Minimax and GPT-5.4-mini variants and a comparison note ([52ad2aa](https://github.com/sanand0/talks/commit/52ad2aa775cd4e0f1e0ad8e6199ce7754a2663ac), [0cd128a](https://github.com/sanand0/talks/commit/0cd128a4b2caa2d8e5f1dfd011c5bf13e05524f9)), 24 Mar 2026. Takeaway: keep model outputs side-by-side to judge quality vs cost.
- Aside: another automated talk generator — because one more skill never hurts. (Well, sometimes it does.)

### [sanand0/blog](https://github.com/sanand0/blog)

_Notes, prompts, and experiments to make posts reproducible and to capture model comparisons._

- **New posts and prompts added.** Added "Hack of the Day" case study, Polya audit writeup, and prompt fragments ([e481c59](https://github.com/sanand0/blog/commit/e481c59382f3f7db1cd10bb399d019661c5437ce)), 28 Mar 2026. Takeaway: publish experiments and prompts alongside posts for reproducibility.
- **Nav JSON & client-side footer.** Build emits nav.json and footer now renders client-side for consistent site nav ([b6c547a](https://github.com/sanand0/blog/commit/b6c547abe2ebc5394e3f6cb260d59defbef58780)), 23 Mar 2026. Takeaway: canonical single-source navigation avoids template drift.
- **Deploy policy tightened.** GitHub Pages now deploys only from main, reducing accidental builds ([7c8ef00](https://github.com/sanand0/blog/commit/7c8ef0099462e08e4e8e6309c7447d747c4a5087)), 24 Mar 2026. Takeaway: restrict CI triggers to reduce cost and surprises.
- Aside: yes, more site plumbing — boring, but you’ll thank yourself later.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Data narratives and reproducible analysis: added the Polya audit story and improved GitHub-usage analysis._

- **Polya Audit interactive story.** Added the full Polya-for-AI data story and assets ([73afe09](https://github.com/sanand0/datastories/commit/73afe092bc16edcf89c3d59f76a6291164d06af5)), 27 Mar 2026. Takeaway: bundle results, visuals, and narrative in one deployable folder.
- **GitHub usage study & scripts.** New repo analysis scripts and a full write-up about "vibe coding" impacts ([0284d2f](https://github.com/sanand0/datastories/commit/0284d2fe56f71bfe99d90720fef61fa219800414)), 23 Mar 2026. Takeaway: ship code with claims so others can verify.
- **Sketchnotes and thumbnails fixed.** Small asset swaps and readme updates to match published pages ([057aef6](https://github.com/sanand0/datastories/commit/057aef6c8bcc9ccb6adcc2bbf4e54e71f284fd61)), 23 Mar 2026. Takeaway: visuals matter for reach.
- Aside: yes, another interactive story — but this one has tests.

### [sanand0/research](https://github.com/sanand0/research)

> Research scripts that make reproducible experiments easier to run and share.

- **Polya heuristics experiment.** Added a full experiment suite to test Pólya heuristics on math benchmarks ([8dc54b8](https://github.com/sanand0/research/commit/8dc54b81698a8e9c7b088cef4064016c616032a8)), 27 Mar 2026. Takeaway: encode experiments as runnable scripts, not notebooks.
- **Tamil music-history tooling.** Large set of scripts to crawl, enrich, and embed Tamil song metadata and audio ([2e2c8c6](https://github.com/sanand0/research/commit/2e2c8c6d9babc7dc9d419c39b575741ef8ef0d0f)), 25 Mar 2026. Takeaway: when you scrape cultural data, add verification and manual checks.
- Aside: research is now a set of reproducible programs, not a drawer of ad-hoc scripts.

### [sanand0/journalists](https://github.com/sanand0/journalists)

_Publishing SOPs and verification checklists to make data cards safe to publish._

- **Verification SOPs for MOSPI PLFS cards.** Added detailed fact-check workflows for each card ([bd06aa4](https://github.com/sanand0/journalists/commit/bd06aa4c643cf7f2c96ff9c91d61449daf0b610c)), 25 Mar 2026. Takeaway: each visual needs a short, runnable verification checklist.
- **Hack of the Day card triage.** Marked many cards accepted/rejected and added review timestamps in cards.json ([6916051](https://github.com/sanand0/journalists/commit/6916051fb6bdc2283f66100d2736e72dc9a7b02a)), 24 Mar 2026. Takeaway: track editorial status in data so automation respects it.
- Aside: no surprises — an editor’s work is mostly yes/no and glue.

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

_Small demo collection: better CSV exports and simpler upload to spreadsheets._

- **Simplify demo CSV export.** `generate_demos_csv.py` now builds an “open demos” CSV and supports uploading helpers ([8866e42](https://github.com/sanand0/llmdemos/commit/8866e42f9082684db0710dbb6ab8adaab933377e)), 24 Mar 2026. Takeaway: make publishing flows scriptable and idempotent.
- **GitHub discover sync script.** `sync_github_demos.py` added discover and brand-config helpers ([50ac876](https://github.com/sanand0/llmdemos/commit/50ac8763fb6e754bbefb9447f20cceb6e53dd5cb)), 24 Mar 2026. Takeaway: centralize discovery to avoid manual drift.
- Aside: yes, uploading demos to Sheets is thrilling Saturday-night engineering.

### [sanand0/tools](https://github.com/sanand0/tools)

_Useful bookmarklets and tiny web tools for real tasks._

- **Google Meet Captions bookmarklet.** New tool scrapes Google Meet captions and copies Markdown; includes tests ([159b47a](https://github.com/sanand0/tools/commit/159b47a575d587b1eab8ba7daa747417b7d4bc33)), 24 Mar 2026. Takeaway: small utilities unlock big workflows.
- **Markdown View popup bookmarklet.** Adds mdview for quick preview of selected Markdown ([5a63df7](https://github.com/sanand0/tools/commit/5a63df7baebbb28abf42ff587a965b4750355ac0)), 24 Mar 2026. Takeaway: local preview beats copying into an editor.
- Aside: yes, one more bookmarklet. Drag it to your bar and stop pasting into Notepad.

### [sanand0/datazoo](https://github.com/sanand0/datazoo)

_Playful, interactive data demos and the Datasaurus gallery._

- **Published gh-pages and index.** Moved zoo.html to index and published the gh-pages site ([d8e0e84](https://github.com/sanand0/datazoo/commit/d8e0e84f2843742cffb32a90e954e8274c29d1ec)), 23 Mar 2026. Takeaway: make demos addressable at root for sharing.
- **Post-mortem and UI tweaks.** Documented experiments and mobile fixes in notes ([6eed874](https://github.com/sanand0/datazoo/commit/6eed87413eb7519b437fa7a28420260124bc75a9)), 23 Mar 2026. Takeaway: short post-mortems reduce repeat mistakes.
- Aside: animals with identical stats are still eerily persuasive.

### [sanand0/aipipe](https://github.com/sanand0/aipipe)

_Pricing updates so the gateway knows new model costs._

- **New model pricing added.** Added GPT-5.4 and Gemini 3.1 pricing entries to pricing.json ([70bedeb](https://github.com/sanand0/aipipe/commit/70bedeb804ed1fbd3f73f619009f823bab0606df)), 27 Mar 2026. Takeaway: keep gateway price tables current to prevent billing surprises.
- Aside: yes, the pricing table needs constant babysitting.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_Course housekeeping and hands-on project links for students._

- **Project 2 details added.** Added picoCTF sign-up and classroom link to README ([8495cfa](https://github.com/sanand0/tools-in-data-science-public/commit/8495cfa0bacc85f2e71420c40202d10b895e1ff7)), 26 Mar 2026. Takeaway: make student onboarding a one-click path.
- Aside: yes, students love a clear first task.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Agent skills, transcription tooling, and dev ergonomics._

- **Transcribe CLI and tests.** Added `transcribe_calls.py` with robust chunking, pricing checks, and tests ([f08ffd1](https://github.com/sanand0/scripts/commit/f08ffd11e221c5a9ef58d5da814aaad9985bd422)), 24 Mar 2026. Takeaway: transcribe as a CLI with dry-run and pricing to avoid surprises.
- **New agent SKILL docs.** Added `linkedin-cdp` and `interactive-storytelling` SKILL.md for safer automation and design patterns ([f08ffd1](https://github.com/sanand0/scripts/commit/f08ffd11e221c5a9ef58d5da814aaad9985bd422)), 24 Mar 2026. Takeaway: document guardrails before you let agents act.
- Aside: ask before you automate someone’s LinkedIn.

### [araffin/datasaurust](https://github.com/araffin/datasaurust)

_Small but important Rust fix for fresh clones._

- **Create log dirs robustly.** Switch from `create_dir` to `create_dir_all` to avoid failures on fresh clones ([d10300a](https://github.com/araffin/datasaurust/commit/d10300afa3fca4a755e6c135c07eb2b9a458b404)), 22 Mar 2026. Takeaway: prefer idempotent dir creation in build tools.
- Aside: tiny change, huge developer happiness.

## Lessons

- Automate ingest early. Small, correct shards beat one giant file every time.
- Ship executable experiments. Code + data + tests make claims verifiable.
- Document guardrails for agentic automation before running it.
- Dry-run modes save money and avoid noisy failures.
- Make publishing steps scriptable and idempotent.

## Suggestions

- Add a tiny CI smoke test that runs each repo’s dry-run modes. It catches plumbing breakages cheaply.
- For podcast/WhatsApp: encrypt or redact raw exports before they touch CI or shared disks.
- For research experiments: publish a tiny reproducibility README listing exact commands and minimal inputs.
- For talk/story skills: add an accessibility checklist step to the generation pipeline.
- For transcriptions: add a quick local audio-quality precheck to reject low-SNR files before API calls.

If you want, I can draft the small CI job templates for live dry-runs, or open PR checklists for agent-safety and publishing SOPs.