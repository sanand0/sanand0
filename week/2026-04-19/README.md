## A week of data stories, agent plumbing, and safer observability

Small projects added big features: richer data narratives, tighter agent logs, and pragmatic observability. The key lesson: invest in explainability and provenance, not just flashy models.

### [sanand0/ed-sales-ops](https://github.com/sanand0/ed-sales-ops)

_This week turned a demo dataset into a demo-ready Sales Leadership Copilot, with narrative data stories and runnable UI for execs._

- **Single-page Sales Copilot added.** Added the SPA with three decision workflows and animated visualizations ([0002970](https://github.com/sanand0/ed-sales-ops/commit/00029704906983dbadfc418c85560998c205030b), 13 Apr 2026). It gives leaders pipeline, renewals, and whitespace views for quick decisions. Takeaway: focus on clear workflows, not generic dashboards.
- **Rich preprocessing and huge processed data.** Committed a new `preprocess.py` and large processed JSONs ([0002970](https://github.com/sanand0/ed-sales-ops/commit/00029704906983dbadfc418c85560998c205030b), 13 Apr 2026). The script aggregates CSVs into explainable JSON for the UI. Takeaway: precompute evidence so the UI remains fast and traceable.
- **Field Intelligence tab: Gladwell-style stories.** Added a narrative "Field Intelligence" tab, animated SVGs, and story data from `summary.json` ([9017e68](https://github.com/sanand0/ed-sales-ops/commit/9017e684f97c60c9edd0380c28495ef34a08b14c), 14 Apr 2026). It pairs prose, captions, and action callouts for execs. Takeaway: stories convert metrics into action.
- **Realistic demo data and scenarios.** Added synthetic base data, transcripts, and canned scenarios to make demos believable ([5a30a30](https://github.com/sanand0/ed-sales-ops/commit/5a30a30a69a03769255c5b6a54c786ab3f36d290), 13 Apr 2026). This avoids hand-waving in live demos. Takeaway: good data beats clever slides. (Yes, you really needed another Gladwell-style anecdote.)

### [sanand0/journalists](https://github.com/sanand0/journalists)

_More rigorous data journalism plumbing this week: downloaders, analyzers, verification SOPs, and shiny cards._

- **Full UN data pipeline added.** Added robust downloaders and a v3 analysis script to build reproducible tables ([be4b796](https://github.com/sanand0/journalists/commit/be4b7966c48bc4fc3141e4b78563bf70e5975134), 14 Apr 2026). It lets you fetch SDG slices and compute the card numbers. Takeaway: automating data ingest reduces verification friction.
- **Ten Statoistics cards and SOPs.** Added render scripts, SVG cards, and verification SOP markdown for UN v3 cards ([60e612c](https://github.com/sanand0/journalists/commit/60e612ca3f7dde6c42869fd958a75891879d364b), 14 Apr 2026; [56d459f](https://github.com/sanand0/journalists/commit/56d459fc6d2539bcabc1151b49ed8b0ac01979d5), 14 Apr 2026). Each card ships with a checklist for fact-checking. Takeaway: pair visuals with verifiable checks.
- **Process page + audio narrative.** Added a long process explanation and an accompanying audio narrative ([c513f02](https://github.com/sanand0/journalists/commit/c513f02b005bd0e37a82b6b3ea10df4306440962), 15 Apr 2026). That explains how cards are produced and audited. Takeaway: explain the pipeline so readers trust the output. (Tiny SVGs, big trust.)

### [sanand0/scripts](https://github.com/sanand0/scripts)

The agent and tooling repo got better logging, a new audit CLI, and improved transcript metadata.

- **Copilot session-state surfaced.** Copilot logs now include supplemental session-state events and collapsed assistant details in output ([aee0ce9](https://github.com/sanand0/scripts/commit/aee0ce9bc89e6b98cffb438167b30505177db009), 16 Apr 2026). Tests ensure tool calls, reasoning, and hooks appear. Takeaway: surface provenance in logs without cluttering the narrative.
- **New skilluse CLI to audit SKILL.md reads.** Added `skilluse.py` plus tests to detect which SKILL.md files agents read ([ddf6800](https://github.com/sanand0/scripts/commit/ddf68001b5af94c86287c0a40925e2bc15294f07), 12 Apr 2026). It streams results and supports filters. Takeaway: auditing agent behavior helps close the loop on tool reliability.
- **Keep transcript prompts.** `transcribe_calls.py` now preserves an optional user prompt in front-matter ([ddf6800](https://github.com/sanand0/scripts/commit/ddf68001b5af94c86287c0a40925e2bc15294f07), 12 Apr 2026). That preserves decision context. Takeaway: small metadata saves confusion later. (Now your copilot remembers its memory. You do too.)

### [sanand0/aipipe](https://github.com/sanand0/aipipe)

Added user-level observability so provider calls carry accountable metadata.

- **Email observability in requests.** OpenAI/OpenRouter requests now include the user email and store flags in test flows ([61be389](https://github.com/sanand0/aipipe/commit/61be3893d0c941e95ca32a9dcfedd96ec82de1ef), 13 Apr 2026). Tests assert metadata presence. Takeaway: per-user metadata helps debug and bill sensibly.
- **Cloudflare observability toggles.** Wrangler config now exposes observability flags for logs and traces ([f800c4c](https://github.com/sanand0/aipipe/commit/f800c4ca7363eb8986368abab508ec822547a7d3), 14 Apr 2026). Toggle before turning data capture on. Takeaway: make observability a controlled setting. (Yes, AIPipe will politely tell providers who asked.)

### [sanand0/blog](https://github.com/sanand0/blog)

A bundle of posts, experiments, and reusable prompts landed, focused on media and agent practices.

- **New and updated posts.** Added posts on agent-skill usage, Gemini-derived media, and narrative songs ([c39b4f](https://github.com/sanand0/blog/commit/c39b4fb8497867598b6b735bbeef4196cfef9846), 18 Apr 2026). They show practical media pipelines and usage stats. Takeaway: document experiments so readers can reproduce them.
- **Prompts, fragments, and advice updates.** Added a song prompt fragment and reorganized advice and book clusters ([c39b4f](https://github.com/sanand0/blog/commit/c39b4fb8497867598b6b735bbeef4196cfef9846), 18 Apr 2026). These are reusable building blocks. Takeaway: small prompt recipes speed future work.

### [sanand0/datastories](https://github.com/sanand0/datastories)

Small, focused tooling to derive scores for a classroom dataset.

- **Generate per-student scores CSV.** Added `generate_scores_csv.py` and wired it into the pipeline ([ff25e46](https://github.com/sanand0/datastories/commit/ff25e463e8fe5aecc3b6f0a6083237efdf7f0ded), 15 Apr 2026). It creates a reproducible `analysis/scores.csv`. Takeaway: automate grading so results remain auditable.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

A weekly podcast update for an internal AI group got refreshed content.

- **Updated weekly podcast transcript.** Added the April 12, 2026 episode transcript with key threads like local models and harness design ([d9817c2](https://github.com/sanand0/generative-ai-group/commit/d9817c26fb63c645de5663d5e3781255a7f63853), 12 Apr 2026). It preserves useful community advice. Takeaway: make discussions skimmable for later reuse.

### [sanand0/imdbscrape](https://github.com/sanand0/imdbscrape)

The daily IMDb scraper hit real-world anti-bot limits; the schedule is paused with a clear post-mortem.

- **Stopped automated scraping; wrote post-mortem.** Documented why the scraper failed and disabled scheduled runs ([49493b4](https://github.com/sanand0/imdbscrape/commit/49493b40e7955ffa22ee46dfa11b862d498d8f0d), 12 Apr 2026). The README explains AWS WAF and practical options. Takeaway: when assumptions change, document choices and pause automation. (Sometimes "stop" is progress.)

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

Small but crucial fixes to handle missing or zero cost data.

- **Robust CPMI handling and filtering.** Updated UI filtering to ignore zero or missing CPMI and adjusted updater to leave blank CPMI when non-positive ([76dcd22](https://github.com/sanand0/llmpricing/commit/76dcd22f9b63f247dcd4cc74d5ce35aa7d1014ef), 12 Apr 2026). This prevents runtime errors and hides meaningless points. Takeaway: sanitize inputs early to keep visuals stable.

## Lessons

- Explainability scales adoption. Embed narratives, evidence, and checklists with every insight.
- Small metadata wins. Preserving prompts, emails, and session events pays off for audits.
- Precompute heavy work. UI responsiveness depends on smart preprocessing.
- Instrument, but gate it. Observability is useful, but enable it deliberately.
- When external systems change, write a readable post-mortem. It saves future guesswork.
- Tests and ML-aware logging reduce finger-pointing across services.

## Suggestions

- For ed-sales-ops: add CSV→JSON versioning and a lightweight viewer for the `story_data`. Keep story fragments editable by non-devs.
- For journalists: add a small HTML preview and one-click verify button that runs the v3 analyzers in a sandbox.
- For scripts: merge shared log parsing helpers into a single library used by both agentlog and skilluse. Reduce duplication now, refactor later.
- For aipipe: add an opt-in dashboard showing aggregated per-user usage and privacy controls before enabling store=true.
- For imdbscrape: pick a sustainable source (official dataset or licensed API) before reintroducing automation.
- For llmpricing: add unit tests for zero/missing CPMI cases and a nightly sanity check that flags unusual changes.

If you want, I can draft a short README checklist for any repo above (preprocess steps, deploy notes, and review checklist). Which one should I do first?