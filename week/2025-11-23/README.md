## A week of data stories, research pushes, and tooling polish — shipping reproducible analysis and safer defaults.

This week reinforced one lesson: ship evidence, then be ruthless about skepticism. Small infra and prompt tweaks made big downstream gains in reliability.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Crafted public data stories and honest meta‑critiques so readers see both findings and how those findings evolved._

- **Michelin deep‑dive launched (21 Nov 2025).** Added an interactive story, datasets, analysis scripts and a candid three‑stage critique ([dd80010](https://github.com/sanand0/datastories/commit/dd80010fca8ecc8bb6496d6a80ea12dbd241828c)), with files like [`michelin/index.html`](https://github.com/sanand0/datastories/blob/main/michelin/index.html). Takeaway: publish both results and your doubts — it builds trust.
- **Course exam improvements story (19 Nov 2025).** Published iterative meta‑learnings and recommendations for student assessment ([f33eb35](https://github.com/sanand0/datastories/commit/f33eb35ac1d20bbf2e0bef77b408f1af8f309488)), including `tds-improvements/summary.md`. Takeaway: corrective cycles produce stronger, actionable pedagogy.
- **Frontiers scrollytelling polished (18 Nov 2025).** Rewrote interaction logic and visuals, fixed treemap UX, added sources ([e98718d](https://github.com/sanand0/datastories/commit/e98718de0a64be27f893e913baf146ad4867b961)), see [`frontiers-2024/index.html`](https://github.com/sanand0/datastories/blob/main/frontiers-2024/index.html). Takeaway: small UX fixes remove the “why was that broken?” noise.
- **AI‑resistance chart and narrative (19 Nov 2025).** Added Figure 4 interactive plot and scrollytelling scaffold ([2ceb73](https://github.com/sanand0/datastories/commit/2ceb73385e0a83b75367d6be66f1122c80bd5c2d)), files under `ai-resistance/`. Takeaway: make data explorable — brushing + narrative beats surprise readers.

Yes, you really needed another NYT-style scrolly. Second aside: the meta‑critique is the best part.

### [sanand0/scientific-research](https://github.com/sanand0/scientific-research)

_Practical, reproducible research pipelines delivered for domain problems and strategy decisions._

- **Clarivate HCR investigation (21 Nov 2025).** Deep analysis, corrections, and reproducible scripts added ([cbd65b2](https://github.com/sanand0/scientific-research/commit/cbd65b2b302a7f4929b70d3f574f4b679d4b8752)); see `clarivate-highly-cited-researchers/`. Takeaway: small sample biases can flip headlines — verify with official stats.
- **Tariff × ecommerce research updated (21 Nov 2025).** Expanded topics to 29 and added consumer‑nationalism category ([30bc3bde](https://github.com/sanand0/scientific-research/commit/30bc3bde375d91608e62a0dda2869c9757f7e63a)), `tariff-ecommerce-research/README.md`. Takeaway: policy shifts + platforms create new natural experiments.
- **Dye discovery pipeline completed (19 Nov 2025).** Virtual screening found 3 novel anthraquinone candidates and reproducible analysis ([f4bbc4c4](https://github.com/sanand0/scientific-research/commit/f4bbc4c4a3048e019c06df02b2138724eeecccc4)), see `dye-discovery-acceleration/`. Takeaway: combine domain heuristics + fast ML to cut lab cycles.
- **STM publishing strategy & revision (19 Nov 2025).** Rewrote conclusions after self‑critique; added scenario analysis and timeline (`stm-publishing-future/`) ([f7866926](https://github.com/sanand0/scientific-research/commit/f786692615c0b8aa12cb0e228697d2561c488659)). Takeaway: be skeptical of disruption narratives; incumbents adapt.

Wry aside: yes, academic publishing still surprises us — mostly by not collapsing.

### [sanand0/research](https://github.com/sanand0/research)

(More tactical research and utilities — scraping, datasets, and small apps.)

- **Jakarta schools contact spreadsheet (22 Nov 2025).** Compiled 105 private K‑12 schools with contacts and documented data quality ([576078f](https://github.com/sanand0/research/commit/576078fed89d833a04b2b77be025da7a68ed321d)), `jakarta-schools/`. Takeaway: honest data quality notes save outreach embarrassment.
- **Repeated‑letter words analysis (22 Nov 2025).** Exhaustive scan of 370K words, 333 exceed >50% same letter, plus Gardner/Munroe‑style articles ([0215d97](https://github.com/sanand0/research/commit/0215d972ef4e43b0a2e08e448281532b6e96045d)), `repeated-letter-words/`. Takeaway: playful analysis can be surprisingly rigorous.
- **India data professionals (19 Nov 2025).** Collected ~790 GitHub profiles, analysis and export scripts ([e02018d6](https://github.com/sanand0/research/commit/e02018d6ed247c908cb15dae08f8180960caa253)), `india-data-professionals/`. Takeaway: public APIs give rapid, high‑ROI talent signals.
- **Word‑file splitter GUI (19 Nov 2025).** Cross‑platform Python app, tests and fixtures included ([5c825fa6](https://github.com/sanand0/research/commit/5c825fa63d27876ef0cf4d2b3e563e7e758fb86c)), `word-file-splitter-gui/`. Takeaway: small desktop tools still beat manual drudgery.

Yes, even glossary puzzles can be a legitimate research deliverable.

### [sanand0/google-datachat](https://github.com/sanand0/google-datachat)

_Tighter prompts, more datasets, and faster LLM choices for chat→SQL workflows._

- **Add Boiler dataset (20 Nov 2025).** Support for `straive-datachat.data.boiler` added to `config.js` ([b61ab6c](https://github.com/sanand0/google-datachat/commit/b61ab6c2a92ac35322104f711e62edb358fa73f8)), enabling industrial telemetry queries. Takeaway: more datasets mean more useful queries.
- **Use faster nano realtime models for short ctx (20 Nov 2025).** Switched to lower‑latency models in ctx.waitUntil to respect 30s limits ([896fedd](https://github.com/sanand0/google-datachat/commit/896fedd9d00bed39ac66a2c099cefc6dc3ccd074)). Takeaway: pick models to match time budgets.
- **POST /chat returns plain text (20 Nov 2025).** Simpler endpoint for text queries, with worker improvements ([9c9c306](https://github.com/sanand0/google-datachat/commit/9c9c3062a97b67ababc52f9e6bb20f69fd9fcff1)). Takeaway: small API ergonomics boosts adoption.
- **Prompt & BigQuery robustness (20 Nov 2025).** Prompt tweaks and safer BigQuery parsing added (`config.js`, [4856c83](https://github.com/sanand0/google-datachat/commit/4856c8309b90311323fb39895c8382344668f475)). Takeaway: better error handling reduces debugging time.

Wry aside: yes, another dataset = another 30 mins of SQL prompts to tune.

### [sanand0/aipipe](https://github.com/sanand0/aipipe)

_More flexible billing and new pricing support for audio workflows._

- **Native provider key passthrough (17 Nov 2025).** Added support to accept native OpenAI/Gemini/OpenRouter keys and bypass AIPipe budgeting ([fb3ae0d](https://github.com/sanand0/aipipe/commit/fb3ae0d19d9fe730306025bb30ababf84663fe20)), with tests. Takeaway: give advanced users full control while guarding admin endpoints.
- **Audio token pricing & new models (16 Nov 2025).** Updated pricing.json and token accounting to include audio tokens and new models ([ccfaf0c](https://github.com/sanand0/aipipe/commit/ccfaf0c42d7e7c17a4912b2c8bc892697732d922)). Takeaway: accurate cost attribution for TTS/transcribe prevents surprises.

Light aside: yes, audio costs still make people blink.

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

_Showcase expanded with recent demos and RFP work._

- **Add recent demos (17 Nov 2025).** Indexed new demos like the Tata Trust RFP visualization and animated insights ([449c541](https://github.com/sanand0/llmdemos/commit/449c541313a9644f10df684ecf08f9f2d2b48472)). Takeaway: keep demo list fresh — it opens opportunity doors.

### [sanand0/tools](https://github.com/sanand0/tools)

_Helper utilities got reliability and extraction fixes for WhatsApp scraping._

- **Fix emoji extraction (21 Nov 2025).** Updated scraper to read emoji from img alt/data‑plain‑text, improving text fidelity ([472623a](https://github.com/sanand0/tools/commit/472623af6448e2f84686f549f8d9e65da4c2e04b)). Takeaway: preserve emoji — they carry meaning.
- **Author phone and inheritance bug fix (16 Nov 2025).** Extract phone from data‑pre‑plain‑text and avoid wrong author inheritance ([53c6fb8](https://github.com/sanand0/tools/commit/53c6fb8d22fee9dede82db4178f33e1f34ad7913)). Takeaway: small parsing rules avoid big misattributions.

Aside: yes, WhatsApp HTML continues to be its own special dialect.

### [sanand0/agentworkflow](https://github.com/sanand0/agentworkflow)

_Formalized agent workflows and practical coding conventions._

- **Add JSON workflow schema (18 Nov 2025).** Published a schema for multi‑agent LLM workflows, nodes, and outputs (`notes/workflow.md`) ([3dd62d6](https://github.com/sanand0/agentworkflow/commit/3dd62d644a9904b739d704720245e67a82848996)). Takeaway: schema-first workflows make automation auditable.
- **Developer conventions & libs in AGENTS.md.** Added preferred libs and best practices for small, testable agents. Takeaway: shared style reduces friction across agents.

Wry aside: yes, more schemas. We love schemas (and hate bugs).

### [sanand0/prompts](https://github.com/sanand0/prompts)

_Cleaned and consolidated prompt styles for coding and creative work._

- **Consolidate developer styles into styles.md (16 Nov 2025).** Replaced old file with richer, single‑source styles and added art styles for image prompts ([772b62b](https://github.com/sanand0/prompts/commit/772b62b9c70f4db0c2e2a37bcb4a45b51db88346)). Takeaway: centralize voice/style snippets for reproducible LLM output.
- **Clarified transcription prompt title.** Renamed to “Transcribe call recording” for clarity. Takeaway: tiny label changes save confusion.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Turned WhatsApp threads into a tidy weekly podcast episode._

- **Updated podcast episode (16 Nov 2025).** Polished the two‑host transcript and tips; saved episode markdown ([5d711f8](https://github.com/sanand0/generative-ai-group/commit/5d711f859087d75fc203062a181fd114636157bd)). Takeaway: social threads are great raw material for curated audio.
- **Refreshed message dataset push.** Replaced/updated `gen-ai-messages.json` with cleaned exports. Takeaway: data hygiene improves downstream generation.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Smoother machine setup, Wayland gestures, and service management._

- **Revamp setup docs & tooling (16 Nov 2025).** Major updates to Linux and Android setup, Wayland gestures (`touchegg.conf`), systemd rclone services, and safer shell defaults ([29be5c4](https://github.com/sanand0/scripts/commit/29be5c4d79b5d75e96677aa1a850d273833caea8)). Takeaway: provisioning clarity saves hours later.
- **Prompt-driven commit flow and prompt loader.** `setup.fish` now integrates LLM commit prompts and prompt lookup. Takeaway: make commit messages useful again.

Light aside: yes, one more machine setup doc — but this one boots reliably.

### [sanand0/til](https://github.com/sanand0/til)

_Notes and TILs expanded across dev, AI, and productivity topics._

- **Bulk Nov 2025 notes added (16 Nov 2025).** Many LLM, tooling, and life‑hack notes; `llms.md`, `til.md`, and `trending-repos.tsv` updated ([bde3929](https://github.com/sanand0/til/commit/bde39294bfcdc324ee4f48813793797f81bc65cd)). Takeaway: short, dated notes accumulate into a valuable searchable corpus.

### [sanand0/imdbscrape](https://github.com/sanand0/imdbscrape)

_Snapshot and scraper fixes to keep time‑series movie data current._

- **Add latest scraped Top‑250 data (16 Nov 2025).** Committed new snapshot `imdb-top250-2025-11-16.json` ([016e54d](https://github.com/sanand0/imdbscrape/commit/016e54d69b5247bc49cdbd39280f268c6f177209)). Takeaway: fresh snapshots let you reason about rank drift.

## Lessons

- Ship reproducible artifacts (data + code + narrative). Readers trust analysis with code and caveats.  
- Small infra improvements (model choice, dataset wiring, parsing tweaks) produce outsized reliability wins.  
- Publish your critiques. Honest, iterative correction increases credibility and surfaces new questions.  
- Automate tests for pipeline correctness before subjective evaluation. Objective checks catch regressions fast.

## Suggestions

- For data stories: add a short reproducibility badge on each index (e.g., "Repro: run analyze.py").  
- For research pipelines: add CI smoke tests that run minimal end‑to‑end flows (one small query, one plot render).  
- For LLM apps: baseline model‑latency tests and a "budget safe mode" that falls back to the cheapest acceptable model.  
- For tooling: capture canonical parsing examples (WhatsApp) as unit tests to prevent regression from UI changes.  
- Audit the large docs additions (til/scripts) for typos and TSV machine‑compatibility before publishing (I can prepare that tidy patch).

If you want, I can produce a 1‑page reproducibility checklist for the Michelin story and a short CI recipe to run its analyze→visualize pipeline automatically.