## A week of polishing agents, fixing build breaks, and making search useful

Small fixes and content additions unlocked better reliability across sites, local tools, and agent workflows. The main lesson: tiny, well-tested changes to infra and UX buy far more developer time than chasing bigger rewrites.

### [sanand0/blog](https://github.com/sanand0/blog)

_Stabilized the site build, made the 404 page useful, and added new "skills" and posts that make AI work repeatable._

- **Hugo upgraded to fix CI builds (18 Jul 2026):** Bumped GitHub Actions install to Hugo 0.164 to avoid template errors ([af531b1](https://github.com/sanand0/blog/commit/af531b136b730d36c13c379b3fe9d24abff078c5)). This unblocks GitHub Pages builds. Takeaway: keep toolchain versions current to avoid subtle template breakage.
- **Turned 404 into a search entry point (18 Jul 2026):** Added a reusable partial and wiring so 404 pages host Pagefind search and pre-populate queries ([c03da47](https://github.com/sanand0/blog/commit/c03da47b65b365d03f03656ed57ebd3b0dd993d7)). Now broken links help users find content. Takeaway: a helpful 404 is better than a pretty one.
- **Ensure GitHub Pages uses root 404 (18 Jul 2026):** Copied built blog/404.html to public/ in setup.sh and added tests to assert equality ([19d8e01](https://github.com/sanand0/blog/commit/19d8e017542009dd1e8b9121218571696babccb5)). Prevents deployment mismatches. Takeaway: test the final artifact, not just templates.
- **Fix slug and export corpus URL logic (17 Jul 2026):** Deterministic slug handling and public URL generation fixed canonical links used by exports and related-posts ([15cfbb1](https://github.com/sanand0/blog/commit/15cfbb14ac47b0c3f15f34f75601a0fdd220eedc)). Keeps search and links stable. Takeaway: URL bugs leak into search and analytics.
- **Added practical skills and posts (16–17 Jul 2026):** New SKILLs like email-reply and workshop-followup, plus posts (scrollytelling, tacit knowledge) to make agent workflows reproducible ([2121552](https://github.com/sanand0/blog/commit/212155255bb3f19d53f95a5dbf7e3d1edc186572), [b3494a2](https://github.com/sanand0/blog/commit/b3494a214efac12f0293ce6ae5e614426c66292f)). These document procedures agents should follow. Takeaway: codifying skills pays off when you reuse agents.

(Yes, a 404 that searches for your typo is basically a helpful fortune cookie. Also: test the whole output, not only templates.)

### [sanand0/scripts](https://github.com/sanand0/scripts)

-Massive polish across browser tooling, agents, and the local MCP server to support richer agent workflows._

- **Refactored edge_tabs -> edge subcommands (13 Jul 2026):** Replaced edge_tabs.py with `edge tabs` and `edge md` subcommands and added tests ([223125e](https://github.com/sanand0/scripts/commit/223125ec2ec143c938b3e44634ce77a296e37a91)). This simplifies tab querying and Markdown extraction. Takeaway: small CLI ergonomics improve daily flow a lot.
- **Support multiple Edge profiles and CDP workflow (17 Jul 2026):** Added DEFAULT_PROFILES, multi-profile loading, and CDP ID joining so tools work with a dedicated CDP profile ([e6540a7](https://github.com/sanand0/scripts/commit/e6540a7f1b893ac909c79863db20bd45ce164936)). Helps avoid clashing with default profiles. Takeaway: isolate remote-debugging profiles to be reliable.
- **Speed and UX tweaks for rofi-chrome-tabs (17 Jul 2026):** Switched rofi script to use `edge tabs --json --cdp-url` and enriched output with CDP IDs ([bdb15c4](https://github.com/sanand0/scripts/commit/bdb15c43420de4f773a97f1c6589d552001b8670)). Faster and shows sleeping tabs. Takeaway: prefer existing tooling over fragile direct CDP fiddles.
- **Add `read` tool to mcpserver for binaries and metadata (17 Jul 2026):** Implemented a read tool that returns file chunks, encoding, MIME, and metadata, plus tests ([f991ee1](https://github.com/sanand0/scripts/commit/f991ee145bc9042075057c34e4e3fd996e843b05)). Enables agents to fetch images and PDFs safely. Takeaway: tools need structured outputs, not free-form text.
- **Archive and consolidate agent SKILLs, plus detection fixes (16 Jul 2026):** Moved many SKILLs to blog and improved skill-detection logic to find more uses across sessions ([98b0d57](https://github.com/sanand0/scripts/commit/98b0d5741a3ecb9d6464d8b8f9f1d31a7d0193b8), [d469603](https://github.com/sanand0/scripts/commit/d469603d793cdd098155582506495339b5d728d9)). Less duplication, clearer ownership. Takeaway: single source of truth avoids divergence.

(Wry aside: yes, there is now a "CDP profile for people who like CDP." Best practice: document it.)

### [sanand0/tabnotes](https://github.com/sanand0/tabnotes)

_From an experiment to a usable MV3 side-panel with better matching and release automation._

- **Added user guide and release automation (18 Jul 2026):** New README for end users plus a GitHub Actions workflow to build ZIP releases ([ccfc052](https://github.com/sanand0/tabnotes/commit/ccfc0521fa5a2ac4bfddcf42841c0873ae24c1e6)). Makes publishing easier. Takeaway: document and automate releases early.
- **Simplified restart matching rules (18 Jul 2026):** Reduced fragile weighted heuristics to exact URL+title or neighbour-aware partial matches ([bf2b56a](https://github.com/sanand0/tabnotes/commit/bf2b56aaf2b445882cef0fd8f5f77cc0a4a1eb99)). Fewer false attachments. Takeaway: simpler, higher-confidence rules beat brittle score sums.
- **UI polish: status icons and throttle viewed marking (17 Jul 2026):** Added compact status icons and a throttle before marking tabs viewed ([dcaeeb1](https://github.com/sanand0/tabnotes/commit/dcaeeb1ff858673b2301c6d6df8aab25d0e81973)). Reduces noise and accidental state changes. Takeaway: defensive UI prevents misleading writes.
- **Built durable Tabnotes MV3 table and tests (13 Jul 2026):** Complete side-panel app, table engine, serialization, and many tests to handle large datasets ([6a6603d](https://github.com/sanand0/tabnotes/commit/6a6603d59faf9c7d6e53c188e0b7fdc38066a964)). Feels production-ready. Takeaway: invest in tests for tricky browser lifecycle cases.

(Yes, saving tabs is secretly a civic duty. Also: favor conservative auto-actions.)

### [sanand0/research](https://github.com/sanand0/research)

> Research artifacts and experiments that evolve into reusable prompts and interfaces.

- **Published LLM writing-style results and viewer (18 Jul 2026):** Added results.json, index.html, and a small Python updater for missing outputs ([8d73d7b](https://github.com/sanand0/research/commit/8d73d7b01ad4ce7f7a83e3386153932462e1670f)). Makes cross-model style comparisons browsable. Takeaway: make evaluation outputs explorable.
- **Iterated ideation protocol and evaluation (15 Jul 2026):** Added prompt tooling, large result sets, and README improvements for protocol optimization ([2af0d1d](https://github.com/sanand0/research/commit/2af0d1dfb5dab7f818d12b9b7e94535572998db5), [6055a99](https://github.com/sanand0/research/commit/6055a99321bec0c93cc6b236867d19b973d77b8c)). Now captures trade-offs between creativity and practicality. Takeaway: evaluate protocols, not only outputs.
- **Better docs and lessons from experiments (15 Jul 2026):** Clarified workflows and practical rubrics for iterating prompts and skills. Short, testable guidance. Takeaway: document the how-to, not only the result.

(Side note: yes, output comparisons are addictive. Resist adding too many models at once.)

### [sanand0/tools](https://github.com/sanand0/tools)

_A set of small web tools and scrapers; fixed a scraping gap to capture writing blocks._

- **ChatGPT scraper: capture writing blocks (18 Jul 2026):** Fixed the DOM selector logic so editable writing blocks are preserved in extracted markdown ([071933d](https://github.com/sanand0/tools/commit/071933d8164d8ca3d9952acb5d15f918becd0148)). Tests now assert captured paragraphs. Takeaway: small DOM edits yield much richer archived content.

(Yes, scrapers still need love. And tests save you from pages that "look" the same but hide text.)

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Podcast generator and pipeline improvements to keep audio scripts coherent week-to-week._

- **Pass previous two podcasts as context (14 Jul 2026):** Podcast script generator now loads the last two episode scripts as context-only blocks ([26bbdd0](https://github.com/sanand0/generative-ai-group/commit/26bbdd051469f0f07447b8d1044967492adea3b0)). Tests ensure context is passed but not repeated. Takeaway: use prior episodes for continuity without rehashing content.
- **Tighter test coverage and sample episodes added:** Many sample md scripts and tests to validate dry-run behavior and API error paths. This reduces surprises when generating audio. Takeaway: test generation end-to-end before spending TTS budget.

(Wry aside: yes, podcasters now need version control and unit tests.)

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Small but important extractor fix to keep leaderboard scraping robust._

- **Fix multi-line model cell extraction (12 Jul 2026):** Adjusted the CDP JS extractor to take the first line of model cells, avoiding multi-line noise ([4783069](https://github.com/sanand0/llmpricing/commit/47830692b4565127b88ed9f50eb8ffa3b6e320cc)). Updated notes and re-ran updates. Takeaway: resilient scrapers must handle small upstream HTML shifts.

(Yes, leaderboards are a moving target. Add sanity checks.)

## Lessons

- Small infra updates prevent big breaks. Upgrade CI and test the built artifact.  
- Make falling-back UX (404/search) actively useful. Users thank you later.  
- Prefer simple, high-confidence matching rules over complex scoring. Simplicity reduces mistakes.  
- Tools need structured outputs (metadata) not only raw text. Design tool contracts.  
- Tests and sample artifacts catch regressions early. Automate release paths where possible.  
- Context helps agents, but pass it as reference-only. Don’t let models repeat the past.  
- Scrapers and extractors must tolerate HTML layout drift. Use first-line or stable fields.

## Suggestions

- Blog: run a full Hugo build on CI with 0.164 and add a smoke test that renders the homepage and 404.  
- Scripts: add a tiny benchmark comparing `edge tabs` vs CDP calls to measure the 80ms gap. Add docs for the CDP profile.  
- Tabnotes: run a small real-user trial for restart matching and collect mismatch examples. Add an end-to-end CDP test in CI.  
- Research: instrument the LLM style viewer to let readers flag preferred styles. Collect that feedback.  
- Tools: add a regression test for chatgptscraper against a saved CDP HTML sample.  
- Generative-ai-group: add a lightweight golden-set test to ensure "do not repeat" rules hold over releases.  
- llmpricing: schedule weekly runs and alert on unexpected TSV shape changes.

If you want, I can draft the small CI job snippets and example tests to implement the top suggestions.