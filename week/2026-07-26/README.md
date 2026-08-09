## A week of durable demos, safer recovery, and clearer skills

This week focused on reproducible evidence and safe defaults. The most useful pattern: turn assumptions into tests, not guesses.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Clean tools, clearer prompts, and safer file handling make everyday automation trustworthy and auditable._

- **Full-text mail index added (25 Jul 2026).** Added [mailindex.py](https://github.com/sanand0/scripts/commit/660a56e1091026a1ca48915d5a89749eab94e972) to build a compact, resumable SQLite FTS index for ~/Documents/Mail/*.mbox. It makes decades of mail searchable locally and fast. Takeaway: index once, search forever; prefer local, verifiable search over ad hoc greps.
- **Transcript summaries get "what‑I‑missed" (20–22 Jul 2026).** Improved [summarize.py]([58b9b76](https://github.com/sanand0/scripts/commit/58b9b7646e73ba2fc0fd1c30940ea8b4aa94e497)) and related prompts ([266650d](https://github.com/sanand0/scripts/commit/266650da7e24b23db760f14ef4d7e84a9d2dbf63)). The tool now flags high‑leverage missed bids and cleans anchors before re-running. Takeaway: make post‑meeting AI checks conservative and audit‑friendly.
- **Music tagger fixes and safer writes (20 Jul 2026).** `musictag.py` now warns when `--write` is required and deletes old APEv2 tags when applying fixes ([5196be5](https://github.com/sanand0/scripts/commit/5196be557752c6054d22fa52d3fdc84e33bbc618), [c8cf84d](https://github.com/sanand0/scripts/commit/c8cf84d38a861a923e271ba779a47b0199fd16b5)). Tests added prevent regressions. Takeaway: make destructive actions explicit and test the clean path.
- **Tooling, agent skills, and small UX touches (19–22 Jul 2026).** Doc tweaks in [mcpserver.py](https://github.com/sanand0/scripts/commit/03e6bb3ea9bf1d5b7cee073b6c6577fa37546e57), espanso snippets, agent SKILL updates, and a daily script now captures all Edge tabs ([78659af](https://github.com/sanand0/scripts/commit/78659af273cc5dd3596603bfd5b39eaf29c63f92)). Yes, you really needed another espanso trigger. Takeaway: polish small tools; they compound into big time savings.

### [sanand0/blog](https://github.com/sanand0/blog)

_Moving tacit agent skills into explicit, copyable prompts makes workflows repeatable and inspectable._

- **Prompts replaced skills for talk flows (24 Jul 2026).** Switched talk-prep and workshop-followup from SKILL to prompt format ([6ef81df](https://github.com/sanand0/blog/commit/6ef81df472f7437302b05f6b71d6027283438b7c), [780aa1d](https://github.com/sanand0/blog/commit/780aa1d2883a15f1e996184f58b2e15fd8b150fb)). That keeps the behavior portable across LLMs and easier to audit. Takeaway: prefer explicit prompts for reproducible agent behavior.
- **New verification and reframing skills (19–21 Jul 2026).** Added a [verification‑gate](https://github.com/sanand0/blog/commit/89633e6ca27dab1a3c0342a08420f4cbf9b03707) and a `reframe-question` skill with evals to catch bad reframes. These guardrails reduce surprise failures. Takeaway: add lightweight verification steps to every nontrivial output.
- **Content and metadata grooming (17–23 Jul 2026).** Updated prompt pages, migrated email-reply to a prompt, and published a new TIL post and follow-ups ([adc310a](https://github.com/sanand0/blog/commit/adc310a1d5e97507ee52d03075a7e23e12dfce4a), [33bdb50](https://github.com/sanand0/blog/commit/33bdb50f2d0e80d585f6feaafbcd5243af6df429)). The site now has clearer dates and classes for prompt pages. Takeaway: documentation is part of the product; tidy it when behavior changes.

Aside: yes, prompts make good policy documents too.

### [sanand0/tabnotes](https://github.com/sanand0/tabnotes)

A practical demo in reproducible form: local-first data, conservative recovery, and recorded evidence.

- **Release v0.1.1 (21 Jul 2026).** Bumped [manifest/package/release workflow](https://github.com/sanand0/tabnotes/commit/a1c463584d6b9be0e6051d15be78bb0cea35e7f5) and published the tested build. The release reflects a crash-recovery fix found during capture. Takeaway: release only what you can verify end‑to‑end.
- **Reproducible submission assets and video pipeline (21 Jul 2026).** Added a full `submission-assets/` package and video tooling ([d5cad73](https://github.com/sanand0/tabnotes/commit/d5cad73b6b0fc43a03b434d6b7dcaab54fb06369)). Scripts generate synthetic fixtures, capture the real extension in an isolated profile, compose images, and stitch narration. Takeaway: reproducible demos beat handwaved screenshots in credibility.
- **Fix crash/close race and reconcilers (21 Jul 2026).** Converge close actions and reconcile restored tabs after a crash with tests ([d999dde](https://github.com/sanand0/tabnotes/commit/d999dde4238443e3464091bf7a274cab47f0165a), [d8a55be](https://github.com/sanand0/tabnotes/commit/d8a55becbb0138d05bdcc61172fe6b09535c9df5)). The UI exposes a "Recover restored tabs" button. Takeaway: visible uncertainty wins over quiet incorrect auto‑matches.
- **Document the Build Week story (21 Jul 2026).** README and prompts document the design invariants, tests, and audit results ([25d21f3](https://github.com/sanand0/tabnotes/commit/25d21f39ddbc847611a9d89ed886b399862895db)). The repo ships both product screenshots and provenance. Takeaway: ship evidence, not claims.

Wry aside: the demo was captured in an isolated profile. Please don't show your real bookmarks on camera.

### [sanand0/tools](https://github.com/sanand0/tools)

Small web apps got nicer defaults and useful bookmarklets.

- **Slide editor gains themes and compact controls (24 Jul 2026).** Added pre‑designed themes, independent title/subtitle fonts, and layout tweaks ([2ad96f0](https://github.com/sanand0/tools/commit/2ad96f01edd5ddce00fc7f43e4b0d671b453aa9d)). The editor fits without vertical scroll. Takeaway: small UI tweaks cut friction for quick, beautiful slides.
- **GMail bookmarklet with tests (24 Jul 2026).** Added a bookmarklet to copy Subject and expanded From lines and a test suite ([7c7bd4a](https://github.com/sanand0/tools/commit/7c7bd4a7c597bab540a809ae0be36b17fc998007)). It shows a transient copied notification. Takeaway: ship tiny utilities with tests.

Aside: yes, a bookmarklet still feels magical in 2026.

### [sanand0/til](https://github.com/sanand0/til)

Notes and trending picks updated with practical heuristics.

- **Weekly notes updated (20 Jul 2026).** Added learnings on AI, tooling, and prompt strategy ([c6e3e5a](https://github.com/sanand0/til/commit/c6e3e5a2cd18fc7a94f456ba5a431638a7ce9e9e)). Short, actionable items help future memory. Takeaway: capture small lessons immediately while they're vivid.
- **Trending repos refreshed.** Updated `trending-repos.tsv` to reflect recent tooling and libraries. Takeaway: automate weekly repo sweeps to surface tool drift.

### [sanand0/research](https://github.com/sanand0/research)

Docs and pages deployed; writing‑style experiments iterated.

- **Deployed site and fine-tuned examples (19 Jul 2026).** Pushed the site live and tweaked `llm-writing-style` content ([b4cd489](https://github.com/sanand0/research/commit/b4cd489f10a2bce7cf085eaca8c7894c793d69aa)). Public examples make evaluation easier. Takeaway: publishing reproducible examples invites external critique and faster iteration.
- **Small copy and navigation fixes.** Polished README entries and ordering for clarity. Takeaway: make research easy to browse, not only to read.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

Data refresh to keep model frontier charts current.

- **Updated leaderboard data (19 Jul 2026).** Refreshed `elo.csv` and bumped README date to 19 Jul 2026 ([ae3a1b1](https://github.com/sanand0/llmpricing/commit/ae3a1b1df6af5d7866aa62c6703863194030baf0)). This keeps cost/quality charts relevant. Takeaway: chart stale data and it misleads decisions; update regularly.

## Lessons

- Reproducibility beats polished claims. Recording evidence (fixtures, tests, captures) prevents "works on my machine" stories.  
- Prefer conservative automated decisions. Visible ambiguity is safer than invisible guessing.  
- Turn high‑risk edits into explicit writes behind a confirmation flag. Warning + test prevents accidental data loss.  
- Convert tacit skills into explicit prompts and verification gates. That makes agent behavior auditable.  
- Small UX tweaks and theme presets dramatically reduce friction for repetitive tasks.

## Suggestions

- Add CI checks that run the Tabnotes capture/verify pipeline on a hermetic runner. Automate the PII/audit and image verification.  
- Integrate mailindex.py into daily workflows and add a small web UI or CLI query wrapper with examples. Benchmark typical queries.  
- Expand summarize.py tests to cover real transcripts and measure before/after user time saved. Log false positives.  
- Teach the verification‑gate by example: add runnable checklists to key prompts (email‑reply, talk‑prep). Ship one automated end‑to‑end eval per skill.  
- For the slide themes and bookmarklets, add simple accessibility checks (contrast, font sizes) in automated tests.  
- Keep publishing research artifacts (live pages + datasets) with clear provenance and a small "how to reproduce" script.

If you want, I can turn any of the Suggestions into a checklist with exact commands and PR templates.