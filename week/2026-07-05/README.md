## A week of making data visible, auditable, and agent-ready

This week was about surfacing signals and histories so tools and humans can trust each other. The key lesson: audit trails and small UX toggles pay back tenfold.

### [sanand0/imdb](https://github.com/sanand0/imdb)

_Capture the edges so you can study the outliers later; small UI controls make big analysis easier._  
- **Export outliers and history:** On 30 Jun 2026 the refresh script now computes outliers and writes `outliers.csv` plus weekly `outliers/YYYY.tsv` ([6dbdccf](https://github.com/sanand0/imdb/commit/6dbdccf83d7cc8d0a5fb74f404430c1338437c4b)). Takeaway: store derived data so trends survive refactors.  
- **Client-side toggle & highlight:** On 30 Jun 2026 the UI gained an Outliers checkbox and cell styling (`index.html` [5032030c](https://github.com/sanand0/imdb/commit/5032030c721ae9c704bce3f5718d8cc2b30d0f4b), `style.css` [4022859](https://github.com/sanand0/imdb/commit/40228594c67ac6c928235438f1386b0e35ad76da), `script.js` [2e8ee32](https://github.com/sanand0/imdb/commit/2e8ee3219c786f13aa6e83662884e23154eab858)). Takeaway: easy toggles let users explore without blowing up defaults. (Yes, you really needed another checkbox.)  
- **Persist outliers to a data branch:** On 30 Jun 2026 CI now appends outlier files and can push to a `data` branch, keeping history out of `main` (`.github/workflows/deploy.yml` [2e8ee32](https://github.com/sanand0/imdb/commit/2e8ee3219c786f13aa6e83662884e23154eab858) and cond change [4396944](https://github.com/sanand0/imdb/commit/43969443c473ac110ce967e92617411b23764023)). Takeaway: separate historical data from site code to reduce risk.

### [sanand0/blog](https://github.com/sanand0/blog)

_More experiments, clearer prompts, and better meta-guides so agents and humans act the same way._  
- **Published detector experiments:** On 01 Jul 2026 new variants of an essay were added for ChatGPT, Claude, and human-read versions (`pages/notes` and `posts/2026/...`) ([cde62ba](https://github.com/sanand0/blog/commit/cde62ba516af767284049dadf9f4c0baa4e18fbc)). Takeaway: publish side-by-side variants to learn how detectors behave.  
- **New prompts and meeting-ready skills:** On 01 Jul 2026 added `pages/prompts/about-updates.md` and meeting-summary skill for crisp, answer-first notes ([45ff12d](https://github.com/sanand0/blog/commit/45ff12dee5c617d6ef27abcd9865077877146479)). Takeaway: standardize short, actionable formats for faster decisions.  
- **Blind-spot lens and workshop copy:** On 30 Jun 2026 added a `blind-spot` skill and polished the agent-data workshop post (`pages/skills`, `posts/2026/...`) ([25490fa](https://github.com/sanand0/blog/commit/25490fa70c774192e70de93378ca35b0b668f03c)). Takeaway: force omissions into the output, not into a side note. (Yes, another SKILL file.)

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Better local tooling, richer observability, and safer backups for brittle scrapers and agents._  
- **git-size now sizes staged files:** On 03 Jul 2026 the tool reports staged changes by default and adds `--all` to size tracked files (`git-size` + prompt) ([8883c56](https://github.com/sanand0/scripts/commit/8883c56022000ec67ea07a4bc7d4c2fb4b9bca34)). Takeaway: inspect what you will actually commit, not the whole tree.  
- **Run observability for scrapers and CDP IDs:** On 03 Jul 2026 LinkedIn and WhatsApp backups now log spans, selector counts, anomalies, and save DOM outlines; `chatgpt` prints CDP target IDs for agent monitoring (`backuplinkedin.py`, `backupwhatsapp.py`, `chatgpt`) ([44120db](https://github.com/sanand0/scripts/commit/44120dbbc3967f7717237c7f99765d411e457d0a)). Takeaway: log minimal debug artifacts to speed fixes when scrapers break. (They will break.)  
- **Add backup CLIs and save fixes:** On 01 Jul 2026 added `aboutmerge.py`, `backuptwitter.py`, and improved `chatgpt --save` behavior so transcripts are captured after the assistant returns ([2db79dc](https://github.com/sanand0/scripts/commit/2db79dc8bf99d19e4b7822e277c83f80bb22c18b)). Takeaway: make backups idempotent and reviewable.

### [sanand0/liveform](https://github.com/sanand0/liveform)

> _Serve editable surveys locally and accept richer inputs for live workshops._  
- **File uploads support:** On 28 Jun 2026 added server and client handling for `field: file`, validation, size/accept checks, and tests (`src/liveform/uploads.py`, `src/liveform/config.py`, `tests/...`) ([d5a1ec4](https://github.com/sanand0/liveform/commit/d5a1ec4b1d3ce3b131f17584c2c9c7535e268b77)). Takeaway: validate on both client and server before saving.  
- **New workshop form with audio upload:** On 02 Jul 2026 added `iimb2026july` form that accepts audio uploads and stores them beside the form (`forms/iimb2026july/form.yaml`) ([8d16483](https://github.com/sanand0/liveform/commit/8d16483dc0bb7983ed98ec559443576ee24defa8)). Takeaway: capture richer responses, but cap sizes strictly. (Yes, we now take your podcast.)  
- **More workshop forms and tests:** On 28 Jun 2026 added `aiunboxed2` and improved end-to-end tests to cover multipart uploads (`forms/aiunboxed2`, `tests/test_server.py`) ([2294016](https://github.com/sanand0/liveform/commit/2294016ab5114268c56fbf4c534d42a66feffcb9)). Takeaway: test uploads early to avoid 500s in a room full of people.

### [sanand0/talks](https://github.com/sanand0/talks)

_Make workshop visuals printable and reproducible as posters for in-person rooms._  
- **Add VizChitra poster generator:** On 03 Jul 2026 added build scripts that capture SVGs, embed images, and produce A3-ready HTML and PDFs (`build_posters.py`, `verify_posters.py`) ([65613a6](https://github.com/sanand0/talks/commit/65613a69eae267647baa5f8093fe7153789a7498)). Takeaway: automate poster builds so slides and prints match.  
- **Layout and CSS tweaks:** On 03 Jul 2026 improved fit classes and page CSS for statnostics and other posters (`build_posters.py` updates and `01-statnostics.html`) ([d6c3297](https://github.com/sanand0/talks/commit/d6c32978ef40605860b2724d222401045eff8683)). Takeaway: keep print CSS separate from web CSS to avoid surprises. (Yes, center vertically.)

### [sanand0/private.s-anand.net](https://github.com/sanand0/private.s-anand.net)

_Minimal private file server with immediate, private logs in D1 for safe auditing._  
- **Add D1 access logging and tests:** On 30 Jun 2026 added a D1 schema, migrations, test harness, and query examples (`migrations/0001_access_log.sql`, tests, `wrangler.toml`) ([ef8d9d0](https://github.com/sanand0/private.s-anand.net/commit/ef8d9d0aa4df01b714f472e731c69511f1a0968d)). Takeaway: keep logs local and queryable without third-party analytics.  
- **Simplify logging flow:** On 30 Jun 2026 refactored request handling and logging to pass structured access objects to the logger (`src/index.js`) ([d04b930](https://github.com/sanand0/private.s-anand.net/commit/d04b93003074e9a78c7d6e0b7974eea4b8c6f63f)). Takeaway: pass a small object, not the whole request, into async log tasks. (No vendor required.)

### [sanand0/aipipe](https://github.com/sanand0/aipipe)

_Keep billing honest and predictable even when APIs return unknown model strings._  
- **Bill using requested model fallback:** On 30 Jun 2026 providers now fallback to the requested model pricing when responses contain unknown model names (`src/providers.js` tests) ([c0185ab](https://github.com/sanand0/aipipe/commit/c0185ab41dd5f1dfcc27eaef218f5af965570006)). Takeaway: bill defensively to avoid free leak paths.  
- **Pass requestedModel through worker:** On 30 Jun 2026 the worker threads `requestedModel` to provider cost code and tests now cover unknown response models (`src/worker.js`, tests) ([02bacaf](https://github.com/sanand0/aipipe/commit/02bacafc2d7338c41f841d3fe289f596818b3313)). Takeaway: keep request intent with the billing pipeline. (No mystery free lunches.)

### [sanand0/til](https://github.com/sanand0/til)

_Notes and small ops: fewer builds, cleaner redirects, and an updated weekly snapshot._  
- **Replace deploy workflow with redirect page:** On 28 Jun 2026 removed the Pages deploy workflow and added a simple redirect `index.html` to the blog TIL category ([2e73dd9](https://github.com/sanand0/til/commit/2e73dd993226ea4c81e8f0a4f1ed2811453dd4d0)). Takeaway: stop running work you don't need.  
- **Refresh weekly notes and trends:** On 28 Jun 2026 updated `til.md`, `llms.md`, and `trending-repos.tsv` with new items and snapshots (`395cb33` includes `trending-repos.tsv`) ([395cb33](https://github.com/sanand0/til/commit/395cb3398784e7f51321eb42ea1e8ff6915f50a7)). Takeaway: snapshot trends weekly so you can roll back and compare.

## Lessons

- Audit trails matter. Small logs speed debugging and audits.  
- Store derived data separately. History trumps ephemeral caches.  
- Surface choices in the UI. Toggles help exploration without losing defaults.  
- Test observability. Capture compact, privacy-safe artifacts for flaky scrapers.  
- Bill defensively. Charge for requested models when responses are ambiguous.  
- Prefer small, repeatable assets over ad-hoc fixes. They compound.

## Suggestions

- Wire a quick dashboard (DuckDB or sqlite) over `imdb/outliers/` for weekly summaries.  
- Add a retention policy for scraper trace zips to bound disk use.  
- Add a small health-check endpoint that validates scraper selectors nightly.  
- For private.s-anand.net, add a compact viewer for recent D1 logs with filters.  
- For blog experiments, add A/B recording of detector outcomes to measure drift.  
- Run an asciinema demo for git-size and poster build flows to document UX changes.

If you want, I can turn any of the suggestions into a PR template or a checklist to run next.