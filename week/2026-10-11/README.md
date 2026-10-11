## A week of tightening fences: verification beats surprise features

Small changes kept many systems running. The big lesson: make outputs auditable, not just prettier.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Care for your tools like you care for your data pipeline: fixes, safer auth, and tidy music tooling._

- **Cleaner tag tooling & CSV parity (09 Oct 2026).** Fixed ID3/MP4 write/read bugs and COMM cleanup in [a0f2ae2](https://github.com/sanand0/scripts/commit/a0f2ae24ee98d2f106f187e5d0bf9f2db848528e) touching musictag.py and tests. Takeaway: preserve mtimes and round-trip multi-value fields.  
- **Rewrote invites acceptor to Python (08 Oct 2026).** Replaced brittle bash with a safer Python flow in [8089710](https://github.com/sanand0/scripts/commit/8089710a97448218872f8b7cd643bde7ac025bf8) so mail sweeps and retries are explicit. Takeaway: prefer clearer control flow for email/calendar automation.  
- **Edge/CDP, media keys, and history consolidation (05–06 Oct 2026).** Added open/reuse tab, media history to ~/Music/music-history.tsv, and global justfile in [45a5005](https://github.com/sanand0/scripts/commit/45a50058ef20f2d1eeb9a3660ca9f611f13f90d1) / [67490b7](https://github.com/sanand0/scripts/commit/67490b738e3946c7ea43b6091b079048f9380b03). Takeaway: surface your defaults; small UX bets compound. (Yes, you really needed another Fish abbr.)

### [sanand0/anand-chrome-tools](https://github.com/sanand0/anand-chrome-tools)

_The palette grew up: durable logs, title-based bookmarklet counts, and better UX._

- **Local action logs & settings UI (07 Oct 2026).** Added FileSystem handles, settings UI, and daily JSONL export in [7b61c49](https://github.com/sanand0/anand-chrome-tools/commit/7b61c49d6bf8bb2872097045a995f07258472329). Takeaway: persist intent, not just events — it speeds audits later.  
- **Use bookmarklet title as key (08 Oct 2026).** Migrate usage keys to title-based keys to handle deleted/recreated bookmarks in [427b257](https://github.com/sanand0/anand-chrome-tools/commit/427b257f3e48b05c48453080e2cddac6385de752). Takeaway: keys should follow human identity, not fragile ids.  
- **New palette features and injection-on-demand (05–06 Oct 2026).** Inject UI on demand, add new-tab-right, keep input in light DOM for host shortcuts in [393139c](https://github.com/sanand0/anand-chrome-tools/commit/393139cc1c5b8115b8130aa44069d48e8b25e62f) and [10340ba](https://github.com/sanand0/anand-chrome-tools/commit/10340ba02a3a4e58ca44a5e75b84d32b987738b5). Takeaway: small accessibility fixes avoid big surprise breakage. (Yes, a palette that doesn’t steal Enter is a feature.)

### [sanand0/tools](https://github.com/sanand0/tools)

Lots of UX and offline-first work across music, scrapers, and conversation capture.

- **Music: offline shell & robust player (06 Oct 2026).** Added service-worker offline shell and UI hooks in [89e4631](https://github.com/sanand0/tools/commit/89e46318121ec62c5d56b14ff2fc2103848b3e2f). Takeaway: offline-first protects flight-mode workflows.  
- **Music: similarity, history, and media-key changes (05–08 Oct 2026).** Excluded recent tracks from similarity, switched history path to ~/Music/music-history.tsv, and integrated a Music web app in [2b25f30](https://github.com/sanand0/tools/commit/2b25f30f016549cdf1f6ea4647ee704e9606f43c). Takeaway: local-first history is more robust than hidden caches.  
- **AI scrapers: preserve rich ChatGPT components (08 Oct 2026).** Extract structured parts (metrics, code, actions) and JSON parts for readable export in [bc13d66](https://github.com/sanand0/tools/commit/bc13d666e3e162f695b4049f943fed6e1495cf3c). Takeaway: keep the structure, so downstream tools can trust semantics. (Yes, models now hand you a table and a footnote.)

### [sanand0/research](https://github.com/sanand0/research)

Big reproducible experiments and CAD/bench work landed this week.

- **Engineering-drawing CAD benchmark + reproducible scripts (07 Oct 2026).** Added FreeCAD scripting, renderers, and a reproducible CAD-bench workflow in [3016cd9](https://github.com/sanand0/research/commit/3016cd930374358ed6206405115b08aeaf55f910). Takeaway: require executable tests, not just pretty renders.  
- **Clef latency and practical deployment notes (04 Oct 2026).** Measured REST vs Worker-binding and updated cost/latency economics in [b843fbb](https://github.com/sanand0/research/commit/b843fbb6efa4b21eb6e2082e0cb495501e3e9419). Takeaway: worker-bindings and warm connections beat chasing HTTP/3 for steady-state inference.  
- **P-hacking headline-factory investigations (04 Oct 2026).** Added NHANES/HRS exploratory scans and tests in [f1235193](https://github.com/sanand0/research/commit/f1235193ddb7068ee089c53dc1d92ac8ed42b6e6). Takeaway: run the same model across a family of comparable exposures before praising a single headline.

### [sanand0/blog](https://github.com/sanand0/blog)

New posts, fixes, and related-post tooling.

- **New posts: course orientation and evaluation pieces (10 Oct 2026).** Added TDS orientation and confidence-calibration posts in [4290d33](https://github.com/sanand0/blog/commit/4290d334f8ff52a9ca1baaf6389dd90ef8906e66) and [fcf6292](https://github.com/sanand0/blog/commit/fcf6292528c005f06cfdea573938311bf302ab85). Takeaway: surface practical classroom lessons promptly.  
- **Related-post ranking: safe YAML loader + sparse neighbor speedups (08 Oct 2026).** Switched to C-backed YAML loader and skip disjoint tag pairs to speed ranking in [c693a86](https://github.com/sanand0/blog/commit/c693a86277a8f4d38da741f408e5dba1d37b088d). Takeaway: pick robust toolchains for file parsing. (Yes, Python’s libyaml helps.)  
- **Tiny fixes: prompts, metadata, and Composer note for VLC (early Oct).** Small editorial and metadata improvements in [551e81b](https://github.com/sanand0/blog/commit/551e81bf6b732851e5c89fe2ca821ecef0b84403). Takeaway: keep the content pipeline smooth.

### [sanand0/talks](https://github.com/sanand0/talks)

Lots of talk pages and new event pages for ED/TDS workshops.

- **Two IITM talks added and transcripted (10 Oct 2026).** Published “Looks Right. Isn’t.” and TDS orientation pages in [2a28fda](https://github.com/sanand0/talks/commit/2a28fda4293a54769d424ca158ca8d4f45f7357f) and [4290d33 in blog]. Takeaway: post video + transcripts fast for reuse.  
- **Improved pages: aspect, chapter highlight, and bio split (08 Oct 2026).** Better video sizing and chapter in-view hints in [071ea40](https://github.com/sanand0/talks/commit/071ea40b43bc37c28bc9a4db304bcb65c618ebd4). Takeaway: small UI fixes dramatically improve navigation.  
- **Pinned builds and CI caching for reproducible HTML (08 Oct 2026).** Pin npm tooling and cache in CI in [1e9171f](https://github.com/sanand0/talks/commit/1e9171f93c2b80b67b099d94a42dc98f2b8799da). Takeaway: pin build tools to avoid surprising regressions.

### [sanand0/exam](https://github.com/sanand0/exam)

Backup, archive, and safer DB storage changes for production exams.

- **Add Cloudflare D1 download + normalize TDS scores (10 Oct 2026).** New downloader script `dumps/final_scores/download.py` in [9b7f7c6](https://github.com/sanand0/exam/commit/9b7f7c6db0a94b22ddd21a6859f5a115c55f4d38). Takeaway: pin data exports and document assumptions.  
- **Durable-object archive, gzip results, and admin tools (08–10 Oct 2026).** Big archive, gzip-in-DB storage, and archive restore/prune tooling in [ac6b21a](https://github.com/sanand0/exam/commit/ac6b21a876b0ceb0ee4221fa0c7faefb650a2fac) and [06395ed](https://github.com/sanand0/exam/commit/06395ed12b85a89466cb364bbf7b5d065509f52d). Takeaway: compress large payloads and keep transparent APIs. (Yes, old TEXT rows stay readable.)  
- **Incremental Discourse refresh and safe package/export helpers (05–08 Oct 2026).** `dumps/update_discourse.py` and safe archive scripts in [06395ed](https://github.com/sanand0/exam/commit/06395ed12b85a89466cb364bbf7b5d065509f52d). Takeaway: sync forum dumps without thrashing the source.

### [sanand0/llmevals](https://github.com/sanand0/llmevals)

Decision models, Clef, and dataset additions.

- **Extended JEV benchmark with more decision models (08 Oct 2026).** Added Perplexity Decider, Liquid d1, Kev 4B, and Mercury Decide in [427b257](https://github.com/sanand0/llmevals/commit/427b257f3e48b05c48453080e2cddac6385de752). Takeaway: include multiple Decisions-style models for fair comparison.  
- **Clef + OpenAI Decisions experiments (07–08 Oct 2026).** Runner now calls cloud decisions and compares latency, cost, and calibration in [715e704](https://github.com/sanand0/llmevals/commit/715e704f70f10b997d3eb5ac5141dc5cd8516fd2). Takeaway: measure end-to-end latency, not only model-time.  
- **Visual report updates and cost handling (08 Oct 2026).** Charts show free vs paid buckets and cost-per-1k tokens in [427b257](https://github.com/sanand0/llmevals/commit/427b257f3e48b05c48453080e2cddac6385de752). Takeaway: split free vs paid to avoid misleading cost axes.

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

Curated demo updates and new links.

- **New demos added and catalog expansions (08–09 Oct 2026).** Added confidence-calibration, dream room, finance pageindex, and several research demos in [918b2d4](https://github.com/sanand0/llmdemos/commit/918b2d452cc067c81924ae0a2143e13bd66e027b) and [c50471b](https://github.com/sanand0/llmdemos/commit/c50471bf34b6a91c0a82f7b4118ba04a3e203381). Takeaway: a demo index is cheap content that surfaces useful experiments.  
- **Keep provenance with prompts.md (05–09 Oct 2026).** Each demo gets a short provenance prompt in [ba81513](https://github.com/sanand0/llmdemos/commit/ba815137a717a285ec6dd2330c266c9dbab4eb23). Takeaway: store the how and why with the what.

### [sanand0/whatsllm](https://github.com/sanand0/whatsllm)

Webhook hardened, dashboard, and DB migration for WhatsApp events.

- **Webhook rewrite + dashboard with D1 logging (07 Oct 2026).** Migrated to robust Worker that logs raw webhooks and adds a Basic-Auth dashboard in [d2e0df8](https://github.com/sanand0/whatsllm/commit/d2e0df85d95abe96b4e056b506771d068550de64). Takeaway: separate capture from action; dashboards help triage.  
- **SQL migrations and stored message table (04 Oct 2026).** Added webhook_requests, message_replies, and message extraction SQL in migrations [migrations/0001](https://github.com/sanand0/whatsllm/commit/...) and [0002]. Takeaway: structure schema for safe retry and replay.  
- **Dropper/cleanups and scrapped helper modules removed.** Removed fragile prototypes in favor of single Worker flow. Takeaway: keep the attack surface small.

### [sanand0/case-studies (assembly-line)](https://github.com/sanand0/case-studies)

A large reproducible industrial case study landed.

- **Full reproducible assembly-line case and student package (05 Oct 2026).** Added generator, validator, replay, and packager in [31ce366](https://github.com/sanand0/case-studies/commit/31ce366abe71fcaf0924e99d5d1caadc3df2f65c). Takeaway: teach verification with runnable evidence, not slides.  
- **Instructor rubrics and blind expected outputs.** Clear, testable anchors for graders in exercise folders. Takeaway: graders must see verification, not just prose.  
- **Packaging enforces offline HTML replay and leak scans.** Student ZIPs are audit-friendly and offline. Takeaway: reproducibility includes offline playback.

## Lessons

- Verify, don’t just prettify. Pretty visuals or confident labels mean little without runnable checks.  
- Persist intent and provenance. Local files, JSONL logs, or compressed DB blobs make audits possible.  
- Prefer small, clear automation rewrites over clever one-liners. Readability avoids repeated incidents.  
- Design for the reader(s). Humans and agents read differently; build for both.  
- Keep experiment scaffolding reproducible. Save seeds, scripts, and validation receipts.

## Suggestions

- Add tiny smoke tests that exercise “open & play” flows for each talk/demo page. Record a shallow screenshot diff.  
- Track “what-to-trust” checks for each AI output: quick checklist a reviewer can run in two minutes. Add to README.  
- For archives and DB migrations, add a one-command dry-run that prints counts and bytes before any delete. Automate a weekly backup snapshot.  
- Convert key dashboards to exportable, signed monthly snapshots for audits. Log checksums and retention policy.  
- For demos and case studies, record a 2‑minute video showing how to verify the example end‑to‑end. That saves reviewers time.

If you want, I can render a compact checklist for each repo above, or produce the raw commit-link list as a machine-readable changelog.