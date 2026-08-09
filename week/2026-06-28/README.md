## A week of stories, skins, and safety nets

Small, practical wins this week: better metadata for discoverability, tighter prompt guidance, a few new data stories, and sturdier infra for agent workflows. The biggest lesson: verification and clear metadata pay off across writing, data, and code.

### [sanand0/blog](https://github.com/sanand0/blog)

_Cleaner prompts, richer post metadata, and timely posts make content easier to find and harder to misread._

- **New reporting and essays:** Added bounty‑agents and related long reads (`bounty-hunting-agent-ecosystem.md`) and expanded the investigation on 24 Jun 2026 and 25 Jun 2026 ([803f17d](https://github.com/sanand0/blog/commit/803f17dbced1820a473e0f4322bba169a41a1fb4), [6a2e48d](https://github.com/sanand0/blog/commit/6a2e48d0f08a4db27d18d8325ca11de189c7aa21)). These posts map automated PR behaviors and bounty honeypots. Takeaway: publish evidence and links so technical stories stay actionable.
- **Data + verification posts:** Published IMF forecast analysis and a Z3 verification note to explain tools and decisions ([6a5c996](https://github.com/sanand0/blog/commit/6a5c9963ea2dcbfb61e6b08e29c8f87ba72e9ef5), [4231ac5](https://github.com/sanand0/blog/commit/4231ac52122b4ff6b10c54e320af1bb2f17c8d4e)). They show how AI and formal tools find real bugs. Takeaway: show both method and artifacts for reproducibility.
- **Prompt & style tightening:** Refined comic prompt and LLM‑smells checklist for clearer generation and fewer formulaic outputs on 26–27 Jun 2026 ([1f0535f](https://github.com/sanand0/blog/commit/1f0535fef1bd6434b0b28804ef8fbb41ae1d8d91), [eefed1b](https://github.com/sanand0/blog/commit/eefed1bdea5a8edcc33c516cc8371d15c8e6430d)). This encourages plain, human phrasing. Takeaway: precise style rules improve generation quality and reduce revision time.
- **SEO and metadata:** Added descriptions, keywords, and LinkedIn links across many posts to improve discovery (multiple commits: 21–26 Jun 2026). See examples in `posts/2026/` ([6d07d5f](https://github.com/sanand0/blog/commit/6d07d5fb5bd43724d3232b43e7623e9b1c36401c)). Takeaway: small metadata fields amplify reach and make sharing simple.  
- Aside: Yes, another prompt polish change was warranted. Good prompts age like fine code, not fruit.

### [sanand0/private.s-anand.net](https://github.com/sanand0/private.s-anand.net)

_Safe, tiny Cloudflare Worker for private file serving with Google OAuth and tests._

- **Initial Worker and tests (23 Jun 2026):** Added a compact Worker, test suite, and README ([0daecbe](https://github.com/sanand0/private.s-anand.net/commit/0daecbea6287bed1f6d46bdf1b90319f409b0494)). It serves R2 files and enforces `.auth.json` policies. Takeaway: small, well-tested servers simplify secure hosting.
- **Docs and deploy fixes (23 Jun 2026):** Cleaned up README and wrangler commands, removing stray `rtk` tokens ([b0099fe](https://github.com/sanand0/private.s-anand.net/commit/b0099fef78725e6b3619e0d158a162694566dc63)). This reduces friction when running locally. Takeaway: brief docs avoid deployment footguns.
- **Added Google Auth note (23 Jun 2026):** Documented OAuth client link and secrets guidance ([b0fda43](https://github.com/sanand0/private.s-anand.net/commit/b0fda43a91cbae6f26492e9b1a072ac133e7f8ec)). Helps debugging sign-in problems. Takeaway: capture the exact OAuth console link to save time.  
- Aside: the code purposely avoids fancy Cloudflare features. Minimalism is a security feature.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Data stories and tools for sharing reproducible visual narratives._

- **New bounty-hunting story (24 Jun 2026):** Added a deep interactive piece showing how agents farm bounties (`bounty-hunting-agents/`) ([d686b46](https://github.com/sanand0/datastories/commit/d686b46f674c27a120d3b8beedadd8af728edc72)). It links analysis, chat logs, and visual output. Takeaway: couple narrative with raw evidence for credibility.
- **IMF forecast errors (22 Jun 2026):** Published IMF WEO forecast-error visualization and data artifacts ([b49a77e](https://github.com/sanand0/datastories/commit/b49a77e0f07018cabf3dbe2e9635f718c6831481)). Readers can interact and inspect permalinks. Takeaway: interactive views beat static charts for trust and exploration.
- **Rainy‑seasons atlas + bookmarkable URLs (25–27 Jun 2026):** Added a full `rainy-seasons/` story and made controls bookmarkable ([9e1862c](https://github.com/sanand0/datastories/commit/9e1862c2e75bf7af564cd63cf930c9961d4d99d0), [b231b70](https://github.com/sanand0/datastories/commit/b231b70a468b2328d6637eaaecae74a17351b5d8)). Now URL state encodes city and sort. Takeaway: stateful permalinks increase shareability and testing.  
- Aside: umbrellas and charts — who knew they'd pair so well?

### [sanand0/research](https://github.com/sanand0/research)

_Code and experiments that back the data stories and investigations._

- **Rainy-seasons pipeline (25 Jun 2026):** Added code to build the city-month master and story pages (`rainy-seasons/`) ([965687f](https://github.com/sanand0/research/commit/965687fdc13579edf3d2f4e5ff9d45cb94a93a7a)). This automates data prep and HTML generation. Takeaway: keep research code reproducible and colocated with story outputs.
- **Fiverr agent scanner (24 Jun 2026):** Added scripts to find agent‑amenable gigs and sample results (`fiverr-agent/`) ([8e6b849](https://github.com/sanand0/research/commit/8e6b849cd9833299305733845c4eff53e1e3537f)). Good for spotting repeatable paid tasks. Takeaway: map real tasks before automating them.
- **Large NFL rules research (22 Jun 2026):** Big suite of scripts to parse, analyze, and narrate rule changes (`nfl-rules/`) ([2ceaca3](https://github.com/sanand0/research/commit/2ceaca34c98d736dbedeb235adce73858bfccc9d)). Outputs CSVs, reports, and plots. Takeaway: build an analysis funnel — parse, canonicalize, analyze, narrate.  
- Aside: yes, football rules make great governance case studies.

### [pydata/xarray](https://github.com/pydata/xarray)

_Maintaining correctness in a widely used N‑D array library._

- **Bugfix: RangeIndex.linspace num=1 (24 Jun 2026):** Fixed a corner-case where linspace with num=1 miscomputed endpoints ([49d4a85](https://github.com/pydata/xarray/commit/49d4a85a8c33de7b6c18ec38162afb629c602576)). Added test to prevent regressions. Takeaway: add focused tests for small but critical edge cases.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Productivity scripts, CLIs, and resilient automation for day-to-day work._

- **New CLIs and timers (24 Jun 2026):** Added `chatgpt` CDP CLI and `timers` helper for quick workflows ([e9b10f4](https://github.com/sanand0/scripts/commit/e9b10f4c75c9f24acff6f046f19ecd9be63a043c)). These speed prompt prep and timer lookups. Takeaway: small CLIs shrink cognitive load.
- **Robust transcription and caching:** Hardened `transcribe_calls.py` with chunk caching, resume support, and a fast `--list-changes` mode ([e9b10f4](https://github.com/sanand0/scripts/commit/e9b10f4c75c9f24acff6f046f19ecd9be63a043c)). Tests cover cache and resume. Takeaway: make long jobs resumeable and observable.
- **Safer automation and logs:** Trim oversized logs, add safer restart flows, and default to patching only recent reports ([e9b10f4](https://github.com/sanand0/scripts/commit/e9b10f4c75c9f24acff6f046f19ecd9be63a043c)). This keeps logs readable and cron jobs reliable. Takeaway: guardrails beat heroic fixes.  
- Aside: finally, a timer tool that respects your inability to remember timers.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Keeping the model cost/quality frontier current._

- **Model data refresh (25 Jun 2026):** Updated `elo.csv` and README timestamp to 24 Jun 2026 to reflect refreshed model ELOs and pricing ([cc250b6](https://github.com/sanand0/llmpricing/commit/cc250b6ed040f74a884b1fff687ab214f70c8e3d)). Takeaway: keep benchmark data fresh; decisions depend on it.

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

_Catalog of demos and quick discovery for demos with GitHub Pages._

- **Demo list refresh (23 Jun 2026):** Reordered and added new demos in `config.json` and README, including several new entries ([45fd074](https://github.com/sanand0/llmdemos/commit/45fd0741da446896272e7e3a48fecd52a1841a6a)). Takeaway: curate demos actively to keep discovery useful and current.  
- Aside: yes, demos multiply like rabbits. Curate ruthlessly.

### [sanand0/tools](https://github.com/sanand0/tools)

.Small web tools and bookmarklets that speed specific tasks.

- **Fix Ideator dark mode (21 Jun 2026):** CSS tweaks and HTML class fix to make the Ideator readable in dark themes (`ideator/index.html`, `ideator/prompts.md`) ([d0da2d5](https://github.com/sanand0/tools/commit/d0da2d5f3cda4e302b6020abc5e5c9cd90131b06)). Takeaway: small UI fixes improve daily usability a lot.  
- Aside: dark mode bugs are stealthy like gum on your shoe.

### [sanand0/talks](https://github.com/sanand0/talks)

_Slides, transcripts, and workshop materials._

- **AI Unboxed workshop materials (21 Jun 2026):** Added transcript, talk plan, Claude prompts, and verification notes for the IIM Alumni workshop (`2026-06-20-ai-unboxed-tools-workflows/`) ([0c077f3](https://github.com/sanand0/talks/commit/0c077f3ddf46b2767eeafb2011cc866d76ee98b8)). These are ready for reuse. Takeaway: capture transcripts and prompts to re-run workshops later.  
- Aside: transcripts are the gift that keeps on giving.

## Lessons

- Verification beats opinion. Formal checks, re‑derivation, or external evidence catch real issues.  
- Metadata is leverage. Tiny front matter fields widen discoverability fast.  
- Make brittle things resumeable. Caching and chunking save hours on long jobs.  
- Publish artifacts with stories. Raw data, scripts, and URLs make claims believable.  
- Agents are a double-edged sword. They automate work but create new trust and security costs.

## Suggestions

- Add lightweight CI for datastories to validate permalink state and data payloads.  
- Expand xarray tests to cover other RangeIndex edge cases and add a changelog note.  
- In private.s-anand.net, add an integration test for OAuth callback flows in CI.  
- For the bounty‑agent research, publish a short mitigation checklist for maintainers.  
- Add telemetry for the new CLIs to measure saved time and common failure modes.  
- Consolidate blog post metadata as a small schema and validate it on commit.

If you want, I can: draft the maintainers' checklist for bounty PRs, wire a CI job for rainy‑seasons, or produce a one‑page deploy playbook for the Cloudflare Worker. Which would you like first?