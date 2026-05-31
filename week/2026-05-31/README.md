## A week of tightening prompts, adding checks, and rescuing fragile data

Small, careful changes this week made tools safer, content clearer, and data stories more actionable. The key lesson: verification and reproducible scaffolds beat ad‑hoc fixes.

### [sanand0/blog](https://github.com/sanand0/blog)

_More explainers, better prompts, and a clearer verification story so readers can trust and reuse outputs._  
(Yes, you really needed both an "Add a Verify Button" and a "Retire the Verify Button." Fine, both exist.)

- **Verification strategy sharpened.** Added two essays that define a user-visible "Verify" button and when to replace it with sampling/monitoring ([20ec1d2](https://github.com/sanand0/blog/commit/20ec1d2b3f636e4c4365bce8a30b7af4c7ad9888), 30 May 2026). This explains practical verification steps for journalists and product teams. Takeaway: give readers a runnable check, not a slogan.
- **Meeting‑prep prompts tightened.** Refined the meeting-prep system prompt and agenda framing in several edits ([553b8bc](https://github.com/sanand0/blog/commit/553b8bc160e659ecf2ef104f359c8288ed22f9b6), [2014650](https://github.com/sanand0/blog/commit/20146501f66946e72e757ade394279110f504153), 28–30 May 2026). The cards now target concrete decisions and sources. Takeaway: smaller briefing cards beat long unfocused ones.
- **New posts and metadata for discovery.** Published TDS feedback and AI-agent ROI ([2501872](https://github.com/sanand0/blog/commit/25018726346c231534dcabdba586c1c7ce381102), 30 May 2026), a chess experiment ([7cc6127](https://github.com/sanand0/blog/commit/7cc6127c50bdb739104f1fe401cb84b9162b8ce2), 28 May 2026), and several data posts ([14156b0](https://github.com/sanand0/blog/commit/14156b0475a6feb727d83e6448f2a54f481c9573), 26 May 2026). Front matter now improves indexing. Takeaway: tidy metadata makes content findable.
- **Style guide and prompt fragments updated.** The Anand blog style got clearer rules and "LLM Smells" fragments for less sloganeering ([20ec1d2](https://github.com/sanand0/blog/commit/20ec1d2b3f636e4c4365bce8a30b7af4c7ad9888), 30 May 2026). This reduces fluff and keeps examples concrete. Takeaway: define bad patterns so writers avoid them.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Data narratives grew with interactive visualizers and a hard look at Wikipedia's hidden single points of failure._  
(Yes, one of the biggest risks to Wikipedia is a Polish statistics bureau. Who knew?)

- **Added "What If a Website Just Died?"** A full data story and UI detailing domain-level citation fragility ([a4cb998](https://github.com/sanand0/datastories/commit/a4cb998fffe9b1940fb19e411397c5cefd243332), 28 May 2026). It shows which domains would break many pages. Takeaway: surprise single points of failure hide in niche data sources.
- **Interactive Erdos unit visualizer.** New single-page visualizer compares grid vs the model construction ([29a4811](https://github.com/sanand0/datastories/commit/29a481140d8f13ae3e861158634be74f4215d632), 26 May 2026). It helps readers feel how unit links scale with points. Takeaway: interactive demos turn abstract math into intuition.
- **Documented longest-common-substring process.** Added process notes and the LCS story for repeated Wikipedia paragraphs ([f8046a9](https://github.com/sanand0/datastories/commit/f8046a9e2cca1afdd24ab8f0185cb3093ea7d167), 26 May 2026). It explains tooling and reproducible steps. Takeaway: publish methods with stories so results are reproducible.

### [sanand0/scripts](https://github.com/sanand0/scripts)

Scaffolding and ingestion tools got more resilient, testable, and patchable.  
(You thought your WhatsApp scraper would be simple. Cute.)

- **Plugin creator and validator added.** `validate_plugin.py`, improved scaffolds, and a cachebuster tool help generate correct plugins ([21b6bce](https://github.com/sanand0/scripts/commit/21b6bce79c42fbfea1d2cc71650aa195ea4c441d), 30 May 2026). This prevents malformed manifests. Takeaway: validate machine‑generated manifests before publishing.
- **WhatsApp backup and history safety.** Backups now keep a `.history/*.history.jsonl` archive and record conflict metadata ([7be4485](https://github.com/sanand0/scripts/commit/7be44855ac6063a364163181585b8eb5721fc469), 25 May 2026). The script no longer silently loses earlier data. Takeaway: always preserve prior data when scrapers drift.
- **Patchable daily activities and chunked transcription.** `activities.py` gained patching for late WhatsApp rows, and `transcribe_calls.py` now passes bounded context between chunks ([48a095e](https://github.com/sanand0/scripts/commit/48a095e0a956841a8e395345d31f79b1ae99d4a6), 25–30 May 2026). This improves continuity and incremental updates. Takeaway: design pipelines to accept late data gracefully.

### [sanand0/tools](https://github.com/sanand0/tools)

Small web tools and scrapers got usability and extraction fixes.  
(Yes, the askai page now distinguishes "copy" from "open"—because your clipboard deserves options.)

- **AskAI: separate select, copy, and open flows.** UI and tests updated so buttons pick provider, copy links, or open a new tab ([8a25211](https://github.com/sanand0/tools/commit/8a25211210ded5a9335b1c899204af407660b544), 30 May 2026). That reduces accidental navigations. Takeaway: separate selection from action.
- **Improved AI scrapers for ChatGPT/Gemini/Claude.** Scrapers now clean titles, preserve code blocks, and strip noisy UI bits ([4c56155](https://github.com/sanand0/tools/commit/4c561552d816ef5811881636c3166875d3a5bff3), 28 May 2026). Tests confirm better markup extraction. Takeaway: robust scrapers make agent audits practical.
- **More demos and updated tooling list.** Updated `config.json` and demo metadata for fresher recommendations ([8511bc5](https://github.com/sanand0/llmdemos/commit/8511bc582db8a9d4aa50fac558ac683a855d5de0), 28 May 2026). The site now references newer demos and versions. Takeaway: curating is useful maintenance work.

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

The demo index refreshed and the recommended Codex model bumped to 5.5.  
(Yes, the README now expects a slightly smarter robot.)

- **Demo list refreshed.** Added several new demos and bumped the Codex example to GPT‑5.5 in README ([8511bc5](https://github.com/sanand0/llmdemos/commit/8511bc582db8a9d4aa50fac558ac683a855d5de0), 28 May 2026). This surfaces new community projects. Takeaway: keep discovery lists current; people build fast.
- **Config expanded for new entries.** `config.json` now contains richer metadata for each demo. This helps automated site builds. Takeaway: metadata enables automated publishing.

### [sanand0/agents](https://github.com/sanand0/agents)

A minimal tools list landed so agents can find local helpers.  
(Agent onboarding: now with fewer surprises.)

- **Basic AGENTS.md committed.** Lists core CLI tools like fd, rg, git, duckdb ([85e875f](https://github.com/sanand0/agents/commit/85e875f59dd3f9a783d789c4b6b7a85b0b4f9f13), 26 May 2026). This documents available skills. Takeaway: explicit tool lists speed agent setup.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

Podcast automation added a weekly episode transcript.  
(Yes, the podcast now has its own commit hydration ritual.)

- **Weekly episode added.** Published the 24 May 2026 episode script and notes ([488ebf1](https://github.com/sanand0/generative-ai-group/commit/488ebf17c9ec3088edaed7f4a9a02c75cd72dd0d), 24 May 2026). This feeds the podcast generator pipeline. Takeaway: keep raw scripts alongside produced audio for traceability.

### [sanand0/til](https://github.com/sanand0/til)

May notes and TILs were added to capture quick learnings.  
(Short notes, long memory.)

- **May 2026 notes added.** New entries cover LLM usage, transcription quality, and practical commands ([faffccd](https://github.com/sanand0/til/commit/faffccd380fee4ec36a3a390c32bbc271b3d5930), 25 May 2026). This enriches weekly TILs. Takeaway: small notes compound into a searchable knowledge base.

## Lessons

- Verification scales only if it moves from 100% inspection to sampling, monitoring, and independent validation. Build the checks into pipelines.  
- Preserve raw data and add lightweight history archives. Scrapers drift; history saves you from silent data loss.  
- Tight prompts and concrete briefing forms beat long, fuzzy instructions. Make the one-liner and opener count.  
- Validate generated artifacts (plugin manifests, marketplace entries) programmatically before publishing. Human review alone is brittle.  
- Interactive demos and reproducible process notes turn curiosity into actionable follow-ups.

## Suggestions

- Automate tiny verify endpoints: for numeric claims produce a one-click SQL or JSON check. Ship that as the first MVP of the "Verify" button.  
- Add a CI job that runs plugin manifest validation (run validate_plugin.py) on new plugin scaffolds. Fail fast on placeholders.  
- Add an automated audit that warns when scraper output would overwrite older content; surface diffs to a human reviewer.  
- For data stories, publish a small reproducibility artifact: a Dockerfile or notebook that re-runs the core extraction with sample data.  
- Measure user impact of meeting‑prep changes: capture reading time and whether meetings ended with decisions. If not, iterate.  

If you want, I can draft the tiny SQL/JS snippet that powers a "Verify" link for numeric cards, or open a checklist PR template for the plugin creator CI. Which should I build first?