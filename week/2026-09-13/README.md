## A week of shipping ducts, pages, and clearer defaults

A string of tooling fixes and new docs made local dev life quieter and public sites richer. The big lesson: small infra polish and clear UX guardrails make daily workflows reliable.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Cleaner agent rules, safer media workflows, and better tests so your laptop actually does what you asked it to do._

- **VLC playback logging added:** Added a user systemd service and script to append played-track URLs to `~/.local/share/sanand-scripts/vlc-history.tsv` ([49ebfce6](https://github.com/sanand0/scripts/commit/49ebfce6e8058beac870454746f825de8915eadc), [services/vlc-history.service](https://github.com/sanand0/scripts/commit/49ebfce6e8058beac870454746f825de8915eadc)). (12 Sep 2026) Takeaway: persistent user services make simple observability painless.
- **Make VLC logging robust:** Switched playerctl/dbus reconnection logic and improved play-music to open URIs reliably ([2875d39](https://github.com/sanand0/scripts/commit/2875d390665308b865bf8d0e559b3233628e94bb), [services/vlc-history.sh](https://github.com/sanand0/scripts/commit/2875d390665308b865bf8d0e559b3233628e94bb)). (12 Sep 2026) Takeaway: handle process restarts; flaky pipes bite you at 3am.
- **Quick music queue from rofi:** New play-music script enqueues the chosen file plus ten random MP3s, wired into rofi-files.sh ([5171565](https://github.com/sanand0/scripts/commit/5171565719aa006ce8916ddc881f729ac525b2de), [play-music](https://github.com/sanand0/scripts/commit/5171565719aa006ce8916ddc881f729ac525b2de)). (12 Sep 2026) Takeaway: tiny UX wins compound with frequent use.
- **Transcribe tool: multi-file and force semantics:** `call` now accepts multiple audios and `--force` skips cached chunks, with tests updated ([e7cc2da](https://github.com/sanand0/scripts/commit/e7cc2da60871b6d3d186a96ca7016c90554f13af), [b719319](https://github.com/sanand0/scripts/commit/b719319e6f4526224f1ca8e8fd85a70eff175919)). (10 Sep 2026) Takeaway: explicit cache-control keeps reruns predictable.
- **Timestamps and warnings improved:** New timestamp tool makes chunk timestamps cumulative and adds line-numbered warnings to help editors ([59a81b9](https://github.com/sanand0/scripts/commit/59a81b97f0e7a1a167a7085296c6fc0c51be012d), [timestamp.py tests](https://github.com/sanand0/scripts/commit/59a81b97f0e7a1a167a7085296c6fc0c51be012d)). (07 Sep 2026) Takeaway: better diagnostics save manual firefighting later.
- **Agent logs & compatibility:** agentlog.py now understands newer Codex/Claude session schemas and shows rate-limit windows, improving search and markdown exports ([afc0093](https://github.com/sanand0/scripts/commit/afc0093720b70f70261d8afe784dc4fc5c8e4c70), [be30c8d](https://github.com/sanand0/scripts/commit/be30c8d1a244a07c6a91b93c373531e98972e31d)). (08 Sep 2026) Takeaway: include backward-compat parsing in logs to avoid invisible data loss.  
(Yes, you really needed another small CLI tweak. Welcome to infrastructure.)

### [sanand0/talks](https://github.com/sanand0/talks)

_Clearer course pages and day-by-day notes, plus embedded video and Japanese translations._

- **Day 5 published:** Full Day 5 content, Japanese translation, and site updates went live ([f9075c4](https://github.com/sanand0/talks/commit/f9075c43cfda0e15897f85f0d214e299f395eb03)). (12 Sep 2026) Takeaway: finish-line content cements the week’s lessons for students and viewers.
- **Day 4 and day-to-day edits:** Day 4 site, transcript, and JA translation updated, with interactive transcript popups ([458dc32](https://github.com/sanand0/talks/commit/458dc325e7252a28920a02aa5eded8430f2eb315)). (10 Sep 2026) Takeaway: small UX touches on transcripts greatly help re-use.
- **Embed keynote video:** Added Jio Convergence keynote embed and caption, making the talk discoverable ([f3e1272](https://github.com/sanand0/talks/commit/f3e1272791e0f37e2bf8a8457b1921873c15b0a9)). (10 Sep 2026) Takeaway: one iframe saves many "where's the video?" emails.  
(Yes, more HTML. The web still wins at publishing.)

### [sanand0/aibuilders](https://github.com/sanand0/aibuilders)

_A living notes site for AI builders, with validators, ingestion, and many new notes from two sessions._

- **Built the site and validators:** New validate/check scripts plus a complete build pipeline for notes and sessions ([c76e20f](https://github.com/sanand0/aibuilders/commit/c76e20f14008f15a4133c9109ac8b8553eef1b1a)). (07 Sep 2026) Takeaway: invest in validators early to keep content honest and automatable.
- **Rename articles→notes and UX polish:** Normalize naming, use 30-second summaries on the home page, and tighten style checks ([b871f7b](https://github.com/sanand0/aibuilders/commit/b871f7b4d5c978de0afb225db6bf65df354cf15b)). (07 Sep 2026) Takeaway: consistent names reduce surprise and plumbing errors.
- **Add session #2 and many vetted notes:** Ingested AI Builders Network #2, added 20+ vetted notes capturing reproducible patterns ([273807b](https://github.com/sanand0/aibuilders/commit/273807b41c1087df8a991b7577d711b523e4b9f3)). (11 Sep 2026) Takeaway: structure claims and replayable experiments, not verbatim meeting transcripts.
- **Stronger transcript and site checks:** Improved transcript-verification and site tests, preventing stale links and root-relative URL bugs ([80c6baf](https://github.com/sanand0/aibuilders/commit/80c6baf6b0206a8fe4b3fff440db431d0741df61)). (10 Sep 2026) Takeaway: make the CI check the things that hurt you most in production.  
(Yes, another validator — your future self will high-five you.)

### [sanand0/blog](https://github.com/sanand0/blog)

> _Make fewer mistakes? Publish them automatically._

_Automated “Mistakes I made” publishing and a raft of content edits and fixes._

- **Automate the "Mistakes I made" flow:** New script extracts weekly corrections from notes into a public page and TIL posts ([056b8c5](https://github.com/sanand0/blog/commit/056b8c570b99bc81b7155de88d986c120c4968ea), [pages/mistakes-i-made.md](https://github.com/sanand0/blog/commit/056b8c570b99bc81b7155de88d986c120c4968ea)). (06 Sep 2026) Takeaway: publishing your own errors speeds learning and builds trust.
- **Add GPT Image 2.5 benchmark post:** New write-up comparing colorization results and artifacts ([c6831cd](https://github.com/sanand0/blog/commit/c6831cdc10fe157237b707a25a88ae3801a243bb)). (09 Sep 2026) Takeaway: pick personally meaningful micro-benchmarks for reliable signal.
- **Mass housekeeping:** Filled missing post titles and updated TIL/trending lists for better discoverability ([eedcc69](https://github.com/sanand0/blog/commit/eedcc6983b089643565d5af6a474d02f5d6b8e11), [a4e7fd4](https://github.com/sanand0/til/commit/a4e7fd4f14aa6c25ac93d3747417f210703570a1)). (06–09 Sep 2026) Takeaway: tidy metadata so search and feeds behave.

(Yes, you should publish mistakes. No, it won’t ruin you.)

### [sanand0/llmevals](https://github.com/sanand0/llmevals)

_Calibration experiments so you do fewer dumb auto-pass decisions._

- **Add confidence-calibration benchmark:** Full BANKING77 analysis with runner scripts, pairwise prompt variants, and input-length experiments ([1eda0ed](https://github.com/sanand0/llmevals/commit/1eda0ed3abb69d025c24aca599522d183abdf307)). (09 Sep 2026) Takeaway: don’t auto-skip human review without measured, task-specific calibration.

### [sanand0/research](https://github.com/sanand0/research)

_Quick public data app checking Singapore train timing claims against official sources._

- **New Singapore train timings app:** Resumable download scripts, site, tests, and `data/app-data.json` for browser exploration ([befa4f7](https://github.com/sanand0/research/commit/befa4f7fcd9a6bcf1ca42f31987389050be93d4)). (07 Sep 2026) Takeaway: if you publish claims, ship the data and the validation script.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_A weekly podcast script export from group chat, now polished and published._

- **Podcast episode draft updated:** New episode MD covering routing, agents, and practicality ([1029afe](https://github.com/sanand0/generative-ai-group/commit/1029afe031b06b3e9145a4dea17151e7c61c017a)). (06 Sep 2026) Takeaway: turn conversation logs into short, usable summaries for busy listeners.

### [sanand0/liveform](https://github.com/sanand0/liveform)

_Short surveys that behave sanely: support for “Other” choices end-to-end._

- **Other-choice support end-to-end:** Frontend toggles, hidden text input, server canonicalization, validators, and tests added ([5e7d8b2](https://github.com/sanand0/liveform/commit/5e7d8b200765fa026832f4d1904f25d267505c6c)). (07 Sep 2026) Takeaway: explicit tagging and length limits make free-text choices safe and analyzable.  
(Yes, people will type very creative other values. You were warned.)

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Small but important: model ELO updated for the frontier analysis._

- **Update model leaderboard snapshots:** Refreshed ELO CSV to reflect current frontier models and comparisons ([75aec88](https://github.com/sanand0/llmpricing/commit/75aec883629335c36938864a17b7cbafcc06799a)). (06 Sep 2026) Takeaway: keep benchmarks current; stale leaderboards mislead choices.

## Lessons

- Small infra work (validators, user services, tests) yields outsized reliability gains. Ship the guardrails first.
- Measure before you auto-skip humans. Confidence looks useful only when calibrated against your tasks.
- Prefer reproducible artifacts: scripts, sample data, and one-line check commands. They make claims auditable.
- UX beats feature toyness. A rofi->play queue and a seekable transcript help real users far more than one more model.
- Publish errors. Making corrections public sharpens judgment and reduces repeated mistakes.

## Suggestions

- For scripts and agent tooling: add a short README badge linking to the unit-test command and a one-liner to rebuild validators.
- For confidence calibration: run the baseline on a small historical holdout per client before any production auto-pass threshold.
- For talks/site: capture a quick audio/video clip of the Day 5 highlights for social sharing.
- For aibuilders: schedule an automated weekly ingest from Meet/Drive with a shadow-mode validator to surface missing evidence URLs.
- For liveform: add a simple analytics event when users supply Other answers so you can watch emergent patterns before aggregating them.

If you want, I can convert this into individual release notes per repo, or produce a short tweeted thread summarizing the top three wins. Which would help more this week?