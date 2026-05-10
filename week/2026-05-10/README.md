## A week of demos, data grabs, and cleaner docs — small tooling that makes big reproducible wins.

This week focused on turning experiments into reproducible workflows. The dominant theme: instrument raw sources, ship verifiable outputs, and keep demos predictable for users.

### [sanand0/d3-wordcloud](https://github.com/sanand0/d3-wordcloud)

_Cleaner layout state and smoother demos make word clouds reliable, interactive, and easier to reuse in pages and experiments._

- **Refactored internal state for clarity.** Renamed persistent layout variables and clarified incremental-placement state in [src/index.js]([771a4a3](https://github.com/sanand0/d3-wordcloud/commit/771a4a3634c075b8eb9dd13c379e6b17bfce13f4)) (04 May 2026). This reduces accidental bugs when adding words. Takeaway: clear names avoid confusing side effects.
- **Slider + debounce for incremental demos.** Added a coalesced slider input and debounce helper in [index.html]([771a4a3](https://github.com/sanand0/d3-wordcloud/commit/771a4a3634c075b8eb9dd13c379e6b17bfce13f4)) (04 May 2026). The demo now adds words smoothly without thrashing layout. Takeaway: debounce UI inputs to keep layout work sane.
- **Stable, seeded prefixes for reproducible demos.** Introduced stable-word-count sliders and deterministic render sequences in [index.html]([9a8438f](https://github.com/sanand0/d3-wordcloud/commit/9a8438fc0986f4050650e084f1aa02458841294e)) (04 May 2026). Users see repeatable layouts for the same seed. Takeaway: make demos deterministic for easier debugging and sharing.
- **Sharper transitions and livelier palettes.** Tuned transitions and swapped to Turbo colors in [index.html]([9e72c58](https://github.com/sanand0/d3-wordcloud/commit/9e72c5800cde7a7b64b7f963d1667caf8354513b)) (04 May 2026). Word entry feels smoother and clearer. Takeaway: good motion and contrast improve comprehension.
- **Doc + style review for D3 alignment.** Added a Bostock-style review and prompts in [mbostock-review.md]([33fcd6b](https://github.com/sanand0/d3-wordcloud/commit/33fcd6b4238aace27036b5525296953249152225)) and [prompts.md]([771a4a3](https://github.com/sanand0/d3-wordcloud/commit/771a4a3634c075b8eb9dd13c379e6b17bfce13f4)) (04 May 2026). The notes nudge smaller public surface and testability. Takeaway: align demos with D3 conventions to help other devs reuse your layout.
- Wry aside: Yes, you really needed another slider. But it makes the demo behave.

### [sanand0/journalists](https://github.com/sanand0/journalists)

_Bigger data grabs, verified cards, and publish-ready drafts make reporting faster and safer._

- **Built a resumable NCRB PDF downloader.** Added `download_ncrb_pdfs.py` with tests and manifest ([fa512d3](https://github.com/sanand0/journalists/commit/fa512d3155f419a0b07866690ce0aa84f245f38b)) (08 May 2026). It caches files and writes an inventory for reproducible runs. Takeaway: preserve raw sources and manifests first.
- **Published multiple NCRB story angles.** Added two rounds of analysis and publish-ready notes in `data/ncrb/analysis/v1.md` ([4acfaa6](https://github.com/sanand0/journalists/commit/4acfaa6aa18712b2bb5cb8ba6b7229307325bd71), [18314dd](https://github.com/sanand0/journalists/commit/18314dd4667274f9b870a689c9825aee721507fb)) (08 May 2026). The pieces surface anomalies reporters can chase. Takeaway: pre-digging tables creates high-leverage story leads.
- **Ship a verified Citizen Survey pipeline and cards.** Added download, convert, and 60/60 verification tests plus 6 SVG data cards (`data/citizen-survey/`) ([0fc6ae3](https://github.com/sanand0/journalists/commit/0fc6ae33ee160a18366343412731fa67c89af812)) (02 May 2026). Each card includes SOPs and verification checks. Takeaway: verification SOPs cut the risk of publishing errors.
- Wry aside: Yes, verification is tedious — and journalists will thank you later.

### [sanand0/blog](https://github.com/sanand0/blog)

_Centralized visual provenance and clearer prompt fragments make generated illustrations traceable and higher quality._

- **Centralized image provenance and prompts.** Annotated image sources and refreshed prompt fragments in `pages/prompts/fragments.md` ([6ddaee6](https://github.com/sanand0/blog/commit/6ddaee6055ab93103a0c0b8d607473e917586682), [d8af009](https://github.com/sanand0/blog/commit/d8af0094c082ec10811df0f670d1c19f1d007e58)) (07 May 2026). This keeps attribution near assets. Takeaway: attach provenance to assets, not buried in prose.
- **Added practical posts and tooling notes.** New posts cover unresolved questions and minimal redirect tracking (`posts/2026/*`) ([6ddaee6], [d8af009]) (07 May 2026). They document reusable infra and idea scaffolds. Takeaway: short operational posts scale your practice.
- **Housekeeping and duplicates removed.** Cleaned a duplicate post and polished pages for better metadata (`31696cf`) (04 May 2026). Small edits improve site hygiene. Takeaway: prune content to reduce noise.
- Wry aside: Yes, another prompt fragment — prompt hygiene is a hobby now.

### [sanand0/til](https://github.com/sanand0/til)

_Updated notes, fresh learnings, and repo cleanup keep your weekly memory useful and lean._

- **Add May 2026 notes and roadmap tweaks.** New entries across `til.md`, `llms.md`, and `ideator.md` update learnings and links ([2a2cff1](https://github.com/sanand0/til/commit/2a2cff131ad3fb3e4b32105ddb0572be4b67f5db)) (03 May 2026). This keeps personal notes topical. Takeaway: frequent small edits beat sporadic big rewrites.
- **Removed stale draft to reduce clutter.** Deleted `tds-jan-2026.md` to avoid outdated drafts ([2a2cff1]) (03 May 2026). Takeaway: remove old drafts to preserve focus and reduce maintenance friction.
- Wry aside: Yes, fewer drafts = less guilt.

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

_Catalog automation and curated demos make discovery and maintenance repeatable._

- **Add AGENTS.md to document automation.** New guide shows commands and safe flows for updating demos (`AGENTS.md`) ([51aa177](https://github.com/sanand0/llmdemos/commit/51aa177cbb1842f88ee925093bdd035081d05aaa)) (05 May 2026). It standardizes "how to add demos". Takeaway: document operations so updates scale.
- **Expanded demos list and config entries.** Added new demo entries and templates to `config.json` ([8cbf0c1](https://github.com/sanand0/llmdemos/commit/8cbf0c10f5c163ac52b6da2ef263a07e0ddcf899)) (05 May 2026). New items are marked `reviewed:false`. Takeaway: mark unreviewed items explicitly to avoid accidental trust.
- Wry aside: Yes, another demo. The web needed it.

### [sanand0/scripts](https://github.com/sanand0/scripts)

=Preserve frontmatter, add force mode, and include useful OS tooling.=

- **Preserve frontmatter formatting in summarize.** `summarize.py` now inserts new keys without reformatting existing YAML ([30024f5](https://github.com/sanand0/scripts/commit/30024f585ec32bd9972804eee06bab4660d9d0c4)) (03 May 2026). It also adds a force mode for full re-serialize. Takeaway: avoid noisy formatting diffs.
- **Add LocalSend to setup.** Added LocalSend flatpak to `setup/linux.md` for easy LAN file sharing ([30024f5]) (03 May 2026). Takeaway: include small, high-utility tools in setup docs.
- Wry aside: Yes, YAML style is a hill worth defending.

### [sanand0/tools](https://github.com/sanand0/tools)

_Make slides embeddable with a ready HTML template for consistent rendering._

- **Document slide → HTML conversion.** Added a rendering template and usage notes in `slide/README.md` ([0eb8124](https://github.com/sanand0/tools/commit/0eb81245d2267c5504c756e6a850d0d80712a2cf)) (08 May 2026). The snippet uses CSS variables for safe embedding. Takeaway: ship a copy-paste embed to reduce friction.
- Wry aside: Now your slide can be a landing page. Tactical.

### [sanand0/publisher-impact-factor](https://github.com/sanand0/publisher-impact-factor)

_Bring OpenAlex data into a bounded, queryable demo dataset for analyses._

- **Add OpenAlex downloader + pipeline.** `download_openalex.py` fetches bounded OpenAlex data, writes JSONL/Parquet, and builds a DuckDB (`download_openalex.py`, `README.md`) ([d70da61](https://github.com/sanand0/publisher-impact-factor/commit/d70da61e25aacee77f591ae15ba7a30fed6c6dfc)) (07 May 2026). It includes caching and progress. Takeaway: create bounded snapshots to enable fast, reproducible analyses.
- Wry aside: Yes, a polite data harvester for journals.

### [sanand0/llmartstyle](https://github.com/sanand0/llmartstyle)

_Expanded the style catalog so experiments cover more visual grammar._

- **Add more test styles and a new 'text2' category.** Updated `config.json` and README to include new styles and prompt variants ([51e29b2](https://github.com/sanand0/llmartstyle/commit/51e29b2cf218505577fb7adc1831a524c66cc742)) (07 May 2026). This broadens coverage for testing image models. Takeaway: wider style sets reveal model weaknesses.
- Wry aside: Because the world needs one more illustration prompt set.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Turn chat threads into a tidy weekly podcast script with production notes._

- **Produce a weekly podcast script/transcript.** Added `2026-05-03/podcast-2026-05-03.md` summarizing practical threads and production lessons ([2ed2e06](https://github.com/sanand0/generative-ai-group/commit/2ed2e06168995d537b7b052123243036405e9a2f)) (03 May 2026). The script focuses on structured extraction and validation. Takeaway: curate threads into short, usable audio artifacts.
- Wry aside: WhatsApp chaos, now radio-ready.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Keep LLM cost/quality tracking accurate by updating model lifecycles._

- **Update deprecation notes and Elo table.** Updated `prompt.md` and refreshed `elo.csv` to reflect model end dates and changes ([10e9dc1](https://github.com/sanand0/llmpricing/commit/10e9dc12184aa91e7f63676dd12164314f99695c)) (03 May 2026). This prevents comparing against retired models. Takeaway: track model lifecycle to keep cost/quality charts valid.
- Wry aside: Models retire faster than your old phone.

### [sanand0/talks](https://github.com/sanand0/talks)

_Small README polish to improve discoverability._

- **Add a concise repo description.** One-line summary added to `README.md` for clarity ([d14a540](https://github.com/sanand0/talks/commit/d14a5402198aa542410bdd6ea5e710fe7af716d8)) (03 May 2026). Takeaway: tiny README edits improve discoverability.
- Wry aside: Yes, README length matters.

## Lessons

- Small infra wins compound. Instrumenting downloads and caching unlocks faster analysis and safer publishing.
- Determinism matters for demos. Seeded layouts and debounced controls make examples reproducible and sharable.
- Documentation is part of the product. Short how-to files and SOPs reduce future mistakes and speed handoffs.
- Preserve human intent. Avoid automatic reformatting that creates noisy diffs and obscures real changes.
- Verify, then publish. Build simple verification scripts for any data-driven graphic before public release.

## Suggestions

- Prioritize a tiny CI job that runs the citizen-survey verification and d3 demo smoke tests on push. This prevents regressions in demos and charts.
- Add a lightweight demo audit checklist (seed + smoke run + screenshots) for d3-wordcloud and llmdemos entries.
- For journalists: wire the NCRB downloader to a small DuckDB/SQL view and publish a reproducible query kit for editors.
- For blog images: add an assets manifest (image → prompt → provenance → model) and surface it in the CMS for editors.
- Record a 30s screencast (asciinema or short WebM) showing the d3-wordcloud slider and seeded replay. It quantifies the UX and helps reviewers.
- Consider a cross-repo "playback" script that replays demo seeds across the d3, llmartstyle, and llmdemos configs for continuous visual tests.

If you want, I can draft the CI job examples, or generate the DuckDB schema SQL for the NCRB/OpenAlex outputs next.