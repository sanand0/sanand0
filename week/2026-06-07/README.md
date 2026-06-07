## A week of writing, safety, and tooling: tighten defaults, test parsers, and document runtime state.

This week focused on clarity: clearer defaults, better docs, and more robust scrapers and backups. Small UX and infra fixes made the system safer and easier to run.

### [sanand0/blog](https://github.com/sanand0/blog)

_Crisp posts and fresher prompt guidance make big ideas and small hacks easier to find and reuse._

- **New long essay on AI bottlenecks.** Added a long-form post explaining how AI bottlenecks shift across coding, agents, and docs ([adb08b0](https://github.com/sanand0/blog/commit/adb08b0ef560d8332f39982fc4f9b7e03b259e18)). 05 Jun 2026. This helps readers judge progress and evaluate model claims practically. Takeaway: frame technical advances by the bottlenecks they move, not just by headlines. (Yes, another AI essay — but it's useful.)
- **Short notes and travel anecdote.** Published a compact prompt-vs-code note and an Indigo flight anecdote ([adb08b0](https://github.com/sanand0/blog/commit/adb08b0ef560d8332f39982fc4f9b7e03b259e18)). 05 Jun 2026. These posts show practical wins from tiny experiments and human observation. Takeaway: small, concrete stories teach more than abstract claims.
- **Playbook for skills when juniors vanish.** Added "No juniors, no experts?" and captured changing AI opinions ([c819da4](https://github.com/sanand0/blog/commit/c819da4883295b7470c6a5292001217188503c96)). 05 Jun 2026. It gives a clear framework: switch, enforce, or level-up skill strategies. Takeaway: choose training based on the cost of being wrong.
- **Better prompts and metadata for discovery.** Expanded prompts, tools lists, and enriched post metadata for SEO and clarity ([fb21607](https://github.com/sanand0/blog/commit/fb216071032f93f4e8b643758f4ea6457510251d), [e8d79af](https://github.com/sanand0/blog/commit/e8d79af34258177ddf9e42c2abfa580b71407c43)). 02–03 Jun 2026. This improves searchability and makes prompts usable. Takeaway: small metadata changes multiply discoverability.

### [sanand0/auth-pages](https://github.com/sanand0/auth-pages)

_Make secure static hosting simple to run and safe by default._

- **Initial secure static pages bundle.** Added a Docker+nginx+Pomerium app with scripts and README ([f54222e](https://github.com/sanand0/auth-pages/commit/f54222e13bcb2fa099246527e52d9058fe23a830)). 05 Jun 2026. You can run public mode immediately and switch to Google-auth protected mode later. Takeaway: ship a safe, minimal default that scales to secure mode.
- **Simplify secure gateway and nginx fronting.** Reworked nginx configs, entrypoint, and compile script for clearer ports and binds ([549e44c](https://github.com/sanand0/auth-pages/commit/549e44c8e23ad89f4935e7dd7965f112ca61cc86)). 05 Jun 2026. The container now fronts Pomerium with nginx and binds services to localhost. Takeaway: explicit local binds reduce surprising exposure.
- **Document Pomerium databroker files and logout UI.** Added docs explaining data/databroker runtime files and a logout link in the sample site ([32c2012](https://github.com/sanand0/auth-pages/commit/32c2012fe39f166e0f74a1888b2b2bcf9741e2aa)). 05 Jun 2026. This explains what RocksDB-like files mean and how to reset them safely. Takeaway: document runtime artifacts so operators don't panic.

(Yes, you really needed a README entry about RocksDB files. Future-you will thank present-you.)

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Short-form episode notes turn chat threads into listenable, searchable artifacts._

- **Weekly podcast episode added.** Composed the 31 May 2026 digest transcript for the group podcast ([78c9a56](https://github.com/sanand0/generative-ai-group/commit/78c9a56df0f9b9652b411bd05c37538240694ddd)). 31 May 2026. It summarizes cost, harness, and tooling conversations for easy reuse. Takeaway: distilling chat threads into episodes focuses product and cost debates.

### [sanand0/til](https://github.com/sanand0/til)

_Keep notes and trend signals fresh so small discoveries stay useful._

- **Add May notes and refresh trends.** Updated core-concepts, recent TIL entries, and refreshed trending repos TSV ([7f30241](https://github.com/sanand0/til/commit/7f302419e65c6f5b5c395e0e38dfc1b04e76ec82)). 31 May 2026. This preserves ephemeral insights and captures ecosystem signals. Takeaway: weekly housekeeping keeps knowledge leverageable.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_More complete activity logs and safer backups make daily automation trustworthy._

- **Personal-email & activities integration.** Added personal-email support and patched activity reports to include personal mail ([d9fde4f](https://github.com/sanand0/scripts/commit/d9fde4f5f169c1d465603e0cd6095db3fcdabad3)). 06 Jun 2026. This closes gaps between work and personal logs. Takeaway: include all accounts to avoid blind spots.
- **More reliable backups and transcription order.** Improved WhatsApp incremental scans, transcribe ordering (newest-first), and file mtimes ([d9fde4f](https://github.com/sanand0/scripts/commit/d9fde4f5f169c1d465603e0cd6095db3fcdabad3)). 06 Jun 2026. Reruns miss less and are deterministic. Takeaway: deterministic ordering makes retries safe.
- **New helper commands and skills; docs & dev updates.** Added git-size, backuplinkedin, livetranscribe, agent skills, and dev container tweaks ([d9fde4f](https://github.com/sanand0/scripts/commit/d9fde4f5f169c1d465603e0cd6095db3fcdabad3)). 06 Jun 2026. These shorten common flows and integrate skills with agents. Takeaway: small CLI helpers multiply productivity.

(Yes, your activity logger now knows your other email. No excuses for missing logs.)

### [sanand0/journalists](https://github.com/sanand0/journalists)

> Small publishing UX lifts for sharing and verification.

- **Add SVG download button to statnostics.** Added a download action and adjusted styles ([cdfa61e](https://github.com/sanand0/journalists/commit/cdfa61e0a1854b56c1aa83d283f7286512186147)). 04 Jun 2026. Users can save visuals for verification or reuse. Takeaway: make verification frictionless.
- **Expanded Hack of the Day content.** Added many new cards and tips to the gallery ([ef94df5](https://github.com/sanand0/journalists/commit/ef94df595c73c26bbf631e508ce7b230bb731ec6)). 04 Jun 2026. More bite-sized safety tips for readers. Takeaway: small, repeated tips scale audience value.

### [sanand0/research](https://github.com/sanand0/research)

_Run rigorous, reproducible experiments to compare models and behaviours._

- **LLM vs Stockfish chess-evaluation harness.** Added an evaluation CLI, dataset builders, and tests ([2a9dd9](https://github.com/sanand0/research/commit/2a9dd917600e62959b53c9fad124d34c634c56d9)). 05 Jun 2026. It runs LLMs against Elo-limited Stockfish and logs structured artifacts. Takeaway: reproducible benchmarks reveal practical model tradeoffs.
- **Update games summary after runs.** Recorded more games and usage stats ([e4e2c6](https://github.com/sanand0/research/commit/e4e2c67450b1f2f773c9aca3a1bb01dc431eca27)). 05 Jun 2026. Tracking tokens and outcomes helps cost-performance analysis. Takeaway: log cost alongside accuracy to guide deployment.

### [sanand0/tools](https://github.com/sanand0/tools)

_User-facing tools got sturdier parsing and richer color controls._

- **Colortable: Markdown, currency, reverse scale, and tests.** Added Markdown parsing, currency handling, reverse-scale option, grouped D3 scales, and tests ([8e670d7](https://github.com/sanand0/tools/commit/8e670d7c5e991d94244bf95c87dfcd0ff097b928)). 01 Jun 2026. This widens supported inputs and stabilizes behavior. Takeaway: add tests before UI changes.
- **LinkedIn invite scraper robustness.** Fixed description extraction and common-org heuristics; added tests ([7f83d4c](https://github.com/sanand0/tools/commit/7f83d4cdcae6a5e22cbbf40f8eeee3abdb5d8aeb)). 31 May 2026. Scraping now skips noise like "wants to connect." Takeaway: prefer structural cues over naive text slicing.

(Yes, the scraper now ignores the LinkedIn theater and finds real signals.)

### [sanand0/llmartstyle](https://github.com/sanand0/llmartstyle)

_Prune configurations to match supported generation endpoints._

- **Trim model list to current backends.** Removed legacy image model entries and kept current picks ([74a9e9](https://github.com/sanand0/llmartstyle/commit/74a9e96f4229151f1773f0399828fbc99950e894)). 03 Jun 2026. This avoids broken generation pipelines. Takeaway: prune configs to reduce surprises.

## Lessons

- Default-to-sane: Safe defaults and clear docs prevent operator mistakes.  
- Test-first UI: Add tests before feature work for stable front-end behavior.  
- Log cost with accuracy: Track tokens and latency as first-class experiment outputs.  
- Small content wins: Short posts and metadata improve discoverability fast.  
- Document runtime state: Explain generated runtime files and reset steps.  
- Include full context: Personal accounts and deterministic ordering reduce blind spots.

## Suggestions

- Blog: Add short TL;DRs and social excerpts for new essays to increase reach.  
- Auth-pages: Add a healthcheck and CI that validates secure/public startup and databroker recreation.  
- Scripts: Add unit tests in CI for activities.py patch flow and backupwhatsapp edge cases.  
- Tools: Deploy colortable and linkedinscraper updates to the live tools site; add an E2E smoke test.  
- Research: Publish a reproducible run manifest and sample PGNs from chess-evaluation.  
- Journalists: Export new cards as CSV to enable batch translations and syndication.  
- llmartstyle: Run a fresh image generation sweep with the trimmed models and archive removed-model outputs.  

If you want, I can draft the small CI job examples for auth-pages and scripts next.