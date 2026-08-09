## A week of making archives, agents, and talks friendlier to both humans and models

This week focused on turning a large blog archive into useful, testable data for agents. The practical lesson: measure first, reorganize only when evidence shows gains.

### [sanand0/blog](https://github.com/sanand0/blog)

_Improve discoverability and agent friendliness while keeping the site static and verifiable._

- **Canonical corpus export for agents.** Added a deterministic export that writes a one-record-per-page JSONL corpus. See [ee52d98](https://github.com/sanand0/blog/commit/ee52d982af962a24f93404009e2f53d3bb3a2f84) (10 Jul 2026). This gives agents a stable entry point for citations and indexing. Takeaway: build a canonical export before you change content.
- **Search that doesn’t bloat pages.** Added Pagefind-based site search and a /blog/search page. See [e1106b6](https://github.com/sanand0/blog/commit/e1106b6ecb27fc9d4fb2c87fabb3345cb7fb0ef9) (10 Jul 2026). The search UI loads only where needed, keeping other pages fast. Takeaway: keep heavy JS off most pages.
- **Make related-posts and embeddings robust.** Moved related-post generation offline and tightened embedding cache integrity. See [17b6b2e](https://github.com/sanand0/blog/commit/17b6b2ed0d4b27bb6b6858aceda592c53ca71c40) and [dbfbfd2](https://github.com/sanand0/blog/commit/dbfbfd2ec374ad24fc829e6967f2a59ed53d4d06) (11 Jul 2026). This ensures reruns skip old vectors and related links are deterministic. Takeaway: version your cache hashes.
- **Canonical tags and a review queue.** Generated a reviewable tag vocabulary and added a review/promote workflow. See [91efc8f](https://github.com/sanand0/blog/commit/91efc8ffa53bcac91c3f5c7b3f0240f6971a002c) (10 Jul 2026) and tag migration [8897dbc](https://github.com/sanand0/blog/commit/8897dbcded2a0a5bc9fceb0c2c01f27aca12fb56) (10 Jul 2026). New proposed tags live in metadata-tag-proposals.yml for human review. Takeaway: treat vocabulary changes as reviewable data, not blind mass edits.
- **Agent exports & media docs.** Wrote agent-facing exports (tags.json, llms.txt) and documented embedding of audio/video/iframes. See [2061b43](https://github.com/sanand0/blog/commit/2061b436b2de64c48e0000fa88d6a2fcad36772c) (10 Jul 2026) and [f6596ed](https://github.com/sanand0/blog/commit/f6596ed8d921b366b82b6b845547bdfdd3084e5c) (11 Jul 2026). This makes the blog usable both by humans and by agent pipelines. Takeaway: publish a tiny agent-friendly manifest alongside human pages.

Yes, another tag system, but this one asks humans before rewriting hundreds of files.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Make local tooling safer, observable, and agent-ready._

- **Persist proposed blog tags for review.** Summarize now records tag proposals and writes a ledger for human promotion. See [846e238](https://github.com/sanand0/scripts/commit/846e238fd885b514797f9c068e2a8a09c70b6c50) (11 Jul 2026). That stops automatic, opaque tag rewrites. Takeaway: when ML suggests taxonomy, log proposals first.
- **Use canonical tag vocabulary in summarize.** Summarize now reads metadata-tags.yml and suggests canonical tags. See [bb983fa](https://github.com/sanand0/scripts/commit/bb983fa6a687523002cf2de1090bb8d6859c7936) (10 Jul 2026). It reduces noisy synonyms and proposed-tag churn. Takeaway: prefer a single source of truth for taxonomies.
- **Ask AI only for missing fields.** The updater now requests just the absent metadata fields from the model. See [6fbf850](https://github.com/sanand0/scripts/commit/6fbf850b68ff4a501c2e50b3fcde93f52bd85847) (10 Jul 2026). This saves tokens and reduces accidental overwrites. Takeaway: ask for delta updates, not full rewrites.
- **New helpers and observability.** Added emailai, musictag, edge_tabs, and structured observability for the MCP server. See [338b7a2](https://github.com/sanand0/scripts/commit/338b7a215f504be91bd852a94e5b963a98ef8b25) (10 Jul 2026) and [e706f9e](https://github.com/sanand0/scripts/commit/e706f9ef20f67fd686c8870a0015fb37a365f82e) (05 Jul 2026). These tools help capture state, tabs, and safe email prompts. Takeaway: surface structured logs before you add dashboards.

Yes, you needed another CLI named emailai. It saves typing later.

### [sanand0/talks](https://github.com/sanand0/talks)

_Tell richer talk stories and make the storytelling skill repeatable and testable._

- **Publish Fifth Elephant workshop materials.** Added full workshop pages, transcripts, prompts, and collation artifacts. See [226a620](https://github.com/sanand0/talks/commit/226a6208889bf3d2bb1fb24d923d9298ec3fc81d) and the follow-up [14fa6a3](https://github.com/sanand0/talks/commit/14fa6a3e5bd4696fdc9ad28931e1fcd114795feb) (11 Jul 2026). The site links original chats and includes audit notes. Takeaway: publish reproducible workshop artifacts.
- **Polish the talk-story skill and templates.** Tightened the .claude skill and added a prompt template. See [12f2179](https://github.com/sanand0/talks/commit/12f217975bee2d30e0d4c00bc673f193f248eb16) (11 Jul 2026). It standardizes QA checks and popup rules. Takeaway: encode common fixes into the skill to avoid repeat edits.
- **Add VizChitra and school sessions.** Added the VizChitra dialogue and a school-teachers story. See [380a41f](https://github.com/sanand0/talks/commit/380a41f2cb1b784d90e3c6d552985cabb5803095) (11 Jul 2026). These include transcripts and prompts for reproducible narratives. Takeaway: publish talks as data, not as memory.

A wry aside: yes, talk pages need checklists. Turns out people fix the same CSS bugs every time.

### [sanand0/tools](https://github.com/sanand0/tools)

_Bookmarklets and tiny web utilities made more robust for real meetings and scrapers._

- **Teams captions and major meetcaptions rewrite.** Added Teams caption capture, polished UI, and tests. See [0a20f91](https://github.com/sanand0/tools/commit/0a20f915932a4cc27885ab2e675058f25fdd1a59) (08 Jul 2026). The tool writes readable markdown with timestamps. Takeaway: local-first caption tooling beats remote-only workflows.
- **LinkedIn invite scraper fixes.** Improved parsing and reduced false positives. See [0a20f91](https://github.com/sanand0/tools/commit/0a20f915932a4cc27885ab2e675058f25fdd1a59) (08 Jul 2026). Tests guard against layout quirks. Takeaway: scrape with structural fallbacks, not brittle class names.
- **Dropped noisy lint tasks.** Removed lint steps from package.json. See [9b73375](https://github.com/sanand0/tools/commit/9b73375d2ec9cc90cd3f0ec6c621a7a1eb6f9384) (08 Jul 2026). The repo prefers practical tests over auto-fixes. Takeaway: keep CI focused on what actually breaks.

Yes, the web needed another bookmarklet. But this one saves a meeting transcript.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Make small map stories that show a human moment with data._

- **Interactive map story: The Fourteen-Minute Walk.** Added a scrollytelling map with KML routes. See [3b0de6f](https://github.com/sanand0/datastories/commit/3b0de6fc18514bf097cc446d8763da788a6c4684) (11 Jul 2026). The story traces an ordinary walk turned long by security checks. Takeaway: maps plus narrative reveal friction in everyday systems.

Yes, maps win arguments. Also sandwiches.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Keep the LLM cost-quality frontier current for practical model choices._

- **Refresh pricing snapshot and narrative.** Updated elo.csv, narrative.json, and README. See [4627c9e](https://github.com/sanand0/llmpricing/commit/4627c9eeb3940aeec3328b08b9157f778da760a6) (05 Jul 2026). It reflects tiered models and an “agentic split” in recommendations. Takeaway: revisit cost/quality analyses frequently.

Yes, the frontier keeps moving. Document it.

## Lessons

- Measure and export canonical data before reorganizing it. A stable corpus helps both humans and agents.
- Prefer small, reviewable changes to big automated rewrites. Humans should promote new tags.
- Ask models for deltas, not full rewrites. Save tokens and reduce accidental churn.
- Keep heavy UI scripts off ordinary pages. Load search only where needed.
- Invest in lightweight observability early. Structured logs make audits and experiments possible.

## Suggestions

- Blog: run the tag promotion workflow on a small batch. Then run the full related-post rebuild and check sitemap diffs. Publish llms.txt and tags.json to help agents discover content.
- Scripts: add a CI job that validates metadata-tag-proposals.yml and runs tag_proposals.promote in dry-run mode. Add end-to-end tests for emailai with a sandbox Gmail account.
- Talks: finish the QA pass for the new talk pages. Verify quote attributions and run the talk-story skill’s checklist before publishing.
- Tools: add a tiny smoke test in CI that runs the caption bookmarklets against the fixture pages. Re-enable a narrow lint step (format-only) or a pre-commit hook for new files.
- Datastories: run mobile accessibility checks on the new map story. Add simple perf budgets for map tiles.
- LLMPricing: automate the leaderboard update via the documented download script and commit narrative changes when scores shift.

If you want, I can draft the small CI jobs and a one-command checklist to run these next steps.