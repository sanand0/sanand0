## A week of making web scraps polite, meetings readable, and podcasts smaller.

Two themes ran through the work: capture more useful context, and make tools robust for real pages. When your data is local, small tooling wins compound into big productivity gains.

### [sanand0/tools](https://github.com/sanand0/tools)

_One-line wins: more resilient web bookmarklets and scrapers so your AI context stops failing at the next DOM change._

- **ChatGPT & Claude scrapers added.** New browser scripts extract and copy full conversations as Markdown; see the commit [6f948ba](https://github.com/sanand0/tools/commit/6f948baabf306b19883a5da1d4c97cc4bf3a3745). (16 May 2026) Takeaway: make scraping self-contained and copy-first to avoid fragile installs.
- **Unified bookmarklet loader.** The page loader now builds multiple bookmarklets and maps buttons to scrapers, see [script update](https://github.com/sanand0/tools/commit/6f948baabf306b19883a5da1d4c97cc4bf3a3745#diff-). (16 May 2026) Takeaway: one UI to rule them avoids accidental wrong-tool clicks.
- **Google Meet recorder streams to disk.** Recorder panel, stable writes, and in-place updates were added in [61b1a66](https://github.com/sanand0/tools/commit/61b1a66683dd0be1f7d6fbccaaa3cdf56231d9c0). (15 May 2026) Takeaway: finalise files on stop; otherwise Chrome leaves a .crswap stub.
- **LinkedIn and WhatsApp scrapers hardened.** New LinkedIn profile scraping and stable invitationMonth logic landed ([74607ec](https://github.com/sanand0/tools/commit/74607ecb24d8e90eb7bf8e7a0cba24f598886ed3), [9f605d3](https://github.com/sanand0/tools/commit/9f605d326167e6f0d1f313a311401634649129ad)), plus WhatsApp row fixes ([5c35617](https://github.com/sanand0/tools/commit/5c3561747607ebf73b44a350ac230a714a0d58f4)). (11–13 May 2026) Takeaway: prefer best-guess months and explicit tests over brittle string parsing.

Yes, you really needed another scraper. Tests now cover varied fixtures so future DOM churn bites less.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_This week the scripts repo focused on reliability and small performance wins for local tooling and audio workflows._

- **Podcast defaults to compact MP3 and parallel generation.** Podcast tool now prefers .mp3, adds -j parallelism, and caches by format. See [f229d8d](https://github.com/sanand0/scripts/commit/f229d8d57b6517b1630754ba0ddff1c6e5914388). (16 May 2026) Takeaway: smaller files and parallelism cut wall time and storage.
- **Environment fallback for API keys.** Tools now load GEMINI_API_KEY from CWD, then script .env. See changes in [f229d8d](https://github.com/sanand0/scripts/commit/f229d8d57b6517b1630754ba0ddff1c6e5914388) and transcribe updates. (16 May 2026) Takeaway: predictable credential lookup makes CI and local runs less fragile.
- **Activities and Google backup CLIs.** New utilities capture daily activity TSVs and back up Google mail/calendar/chat. See [882dde4](https://github.com/sanand0/scripts/commit/882dde471a88f9c1f45de09eb743b3f57d0f798e). (14 May 2026) Takeaway: local, structured exports let agents reason over real context.
- **History, Drive log, and image tooling.** Edge history sync, gws drive-change logs, and chroma-key image helpers arrived in [9c3b5f6](https://github.com/sanand0/scripts/commit/9c3b5f63f28ee1a9ca0aa5672cb24dcf0a671c1e). (13 May 2026) Takeaway: make your evidence searchable before you ask an agent to use it.

Wry aside: yes, the world needed a tiny CLI to make meetings audible and podcasts cheap.

### [sanand0/publisher-impact-factor](https://github.com/sanand0/publisher-impact-factor)

_The research site became a shareable report hub — clearer pages and a public landing page for data stories._

- **Public reports & landing site published.** A docs-based site and index page were added; preview at https://sanand0.github.io/publisher-impact-factor/ and commit [9e1b634](https://github.com/sanand0/publisher-impact-factor/commit/9e1b634e7121e4d3c4feb2c2c3ec4ed7a3f78cbb). (11 May 2026) Takeaway: a simple site makes analysis shareable without bespoke ops.
- **Per-publisher neuroscience reports added.** Individual HTML reports for Springer, Elsevier, PLOS, OUP, and Wiley were committed in [def195b](https://github.com/sanand0/publisher-impact-factor/commit/def195b36c16c2cc0d015b1a912a91b414d0a8af). (10 May 2026) Takeaway: focused narratives translate data into concrete editorial moves.
- **MIT license applied.** Repository now includes an MIT license (commit [0525363](https://github.com/sanand0/publisher-impact-factor/commit/052536310c911ad1f1815cdc899756a193a07636)). (10 May 2026) Takeaway: shareable analysis gets fewer distribution hassles.
- **Design & theme tweaks.** Styling and theme glue landed to support light/dark modes and consistent branding. See [9e1b634](https://github.com/sanand0/publisher-impact-factor/commit/9e1b634e7121e4d3c4feb2c2c3ec4ed7a3f78cbb). (11 May 2026) Takeaway: readable visuals speed client buy-in.

A wry nudge: yes, publishers do want charts. They want fewer bad journals even more.

### [sanand0/blog](https://github.com/sanand0/blog)

_New posts and style prompts to turn local capture into readable essays._

- **Local MCP post added.** A post explains using a local MCP as a context hub and tradeoffs. See [1944607](https://github.com/sanand0/blog/commit/194460704dd60fca423abf3a0c7262ea063ea8f1). (16 May 2026) Takeaway: local context plus supervised tools beats blind uploads.
- **Google Meet recorder post.** Documentation and rationale for the Meet captions recorder were added in [296ef96](https://github.com/sanand0/blog/commit/296ef969a16dd7a1b2d74b90abc303854d9b94f5). (16 May 2026) Takeaway: small tools that stabilise captions unlock downstream agent work.
- **Prompt library & style updates.** Blog prompts and fragments were expanded so future content stays consistent. See [ef170a1](https://github.com/sanand0/blog/commit/ef170a1354565d44a15250cdd19258ccb575c80a). (15 May 2026) Takeaway: codified voice + templates speed repeatable writing.
- **Minor fixes and sample embeds.** Added remote markdown rendering examples and site polish. (15–16 May 2026) Takeaway: reproducible posts make demos easier.

Wry aside: yes, another “how I do things” post — but this one makes minutes actually useful.

### [sanand0/talks](https://github.com/sanand0/talks)

_One tidy upload: a recent Gramener talk with transcript, sketchnote, and prompts._

- **Gramener All Hands talk added.** Full page, sketchnote, and prompts for "Agents are the New Software" landed in [812cd0a](https://github.com/sanand0/talks/commit/812cd0aa9234f7345d9fdec1f9d66f42df43118a). (16 May 2026) Takeaway: publish talks with transcripts for searchable context.
- **README updated.** The talks index now links to the new Gramener item. See same commit. (16 May 2026) Takeaway: small site housekeeping avoids future "where was that talk?" queries.
- **Remote markdown embeds.** Index shows linked resources and preloads prompt fragments for readers. Takeaway: provide context links near the content.

Yes, another talk. But now it’s actionable research fodder.

### [sanand0/research](https://github.com/sanand0/research)

_A new dataset and careful method notes for measuring FOSS grant outcomes._

- **FOSS United outcomes added.** Project TSVs, evidence, and methodology live in repo commit [ffac152](https://github.com/sanand0/research/commit/ffac1526cb86aa3874c5ef361166d313bad9844a). (15 May 2026) Takeaway: public, evidence-first datasets help donors decide follow-ups.
- **Methodology.md explains boundaries.** The write-up clarifies inclusion rules and limits. See same commit. (15 May 2026) Takeaway: conservative claims protect credibility.
- **Gap inventory & prompts.** Prompts to reconcile public data with internal records are included. Takeaway: ask implementers for ground truth before conclusions.

Wry aside: yes, spreadsheets again — but this one decides funding.

### [sanand0/til](https://github.com/sanand0/til)

_Small housekeeping: prune noise and refresh living notes._

- **Pruned stale notes and refreshed trends.** Removed apps.md clutter and updated llms/til notes and trending repos. See [0b9f610](https://github.com/sanand0/til/commit/0b9f6100d9579a4d2e74e7b6e08cbd8e29dc1108). (10 May 2026) Takeaway: prune to keep discovery fast.
- **Added current tool hits and tips.** New entries on tools and small ergonomics updates keep the repo useful. Takeaway: small notes beat big forgotten documents.

Yes, fewer ideas, better focus.

## Lessons

- Capture-first beats perfect parsing. Make the page copyable and local before trying to normalise it.
- Tests and fixtures pay dividends. Real HTML fixtures caught fragile selectors early.
- Small UX defaults matter: mp3 defaults, env fallbacks, and parallelism reduce friction.
- Local context is the scarce asset. Make meetings, mail, and browser history agent-readable.
- Prefer conservative metadata. Mark uncertain values (e.g., "2026-05?") instead of lying.

## Suggestions

- Add lightweight CI that runs the new scraper tests on headless fixtures nightly.
- Record a short demo (asciinema or short video) for the Meet recorder and podcast pipeline.
- For the tools scrapers, add an automated selector resilience checklist (ARIA-first, fallbacks).
- In scripts, surface a single CLI to report which GEMINI_API_KEY source was used at runtime.
- Publish a short "how to reuse this data" page that shows an agent reading Meet transcripts, notes, and podcast metadata together.

If you want, I can draft the demo README for the Meet recorder and a one-page "how to feed local context to an agent" playbook next.