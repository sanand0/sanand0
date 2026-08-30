## A week of polishing skills, stabilizing agents, and a surprising amount of analytics

Small fixes and big signals: better local tools, clearer agent rules, more robust embedding pipelines, and a lot of site telemetry. The key lesson: invest in small, testable safety and observability steps now; they pay back during long-running agent work.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Operational rules and small utilities that make agents and day-to-day work behave predictably._

- **Tightened system-skill guidance.** Expanded the system skill template and imagegen rules to clarify when to use built-in tools versus CLI fallback ([9409654](https://github.com/sanand0/scripts/commit/940965490ce241ea3e4f7d4b5ea0adba8b209ce0)). 28 Aug 2026. Takeaway: explicit guardrails reduce accidental downgrades to weaker models.
- **Prompt usage reporting.** Added `prompt use` to show recent prompt frequencies and JSONL output for tooling ([ff306b7](https://github.com/sanand0/scripts/commit/ff306b763ba3d6d30802a8e01256700d927bd1fb)). 28 Aug 2026. Takeaway: measure prompt reuse to spot stale or duplicated prompts.
- **Bounded bash concurrency for MCP.** Run up to four concurrent bash tool calls via a ThreadPoolExecutor so MCP doesn't block the event loop ([977ded8](https://github.com/sanand0/scripts/commit/977ded8dfd6636e5f53390f6efa32b18e8ccfeab)). 24 Aug 2026. Takeaway: bounded parallelism keeps tools fast and predictable.
- **Rename handling & script renames.** Support script renames (transcribe_calls.py → call) and count uses under new names with tests ([70d8cf7](https://github.com/sanand0/scripts/commit/70d8cf7ac1d0c799cbcf47409dfc880f559cdb47)). 26 Aug 2026. Takeaway: map historical names to current ones for accurate usage metrics.
- **Wry aside:** Yes, you needed clearer imagegen rules. The model will still ask to use gpt-image-1.5 for hair.

### [sanand0/blog](https://github.com/sanand0/blog)

	Content updates, redirects for talks, and prompt/skill polish across the site.

- **Published top prompts post.** Added "My Top 5 Prompts in August 2026" and usage counts ([5276afaa](https://github.com/sanand0/blog/commit/5276afaa4a5a24080fbdec8608bbe4e5a882ab8f)). 28 Aug 2026. Takeaway: small, shareable post formats get reused quickly.
- **Moved talks out and redirect fixes.** Redirected /blog/talks to talks.s-anand.net and tightened 404/search behavior ([fcb3518](https://github.com/sanand0/blog/commit/fcb3518157648243f2c042d0ad0ac8148a2a3fd3)). 26 Aug 2026. Takeaway: keep public catalogs canonical and use redirects for legacy links.
- **New talk-topic prompt fragment.** Added a reusable "Talk topic suggestions" fragment for ideation ([98190155](https://github.com/sanand0/blog/commit/98190155a11db6205ed240b2b52734fd0d792e09)). 28 Aug 2026. Takeaway: capture ideation prompts as small, testable skills.
- **Stability & verification guidance.** Added stability-check and verification-gate guidance for analyses and agent output ([2c4f89c8](https://github.com/sanand0/blog/commit/2c4f89c8adb2532d1f16b8c19fa4ab3cc74123ad)). 24 Aug 2026. Takeaway: plan forks and re-runs before trusting conclusions.
- **Wry aside:** Yes, the 404 now searches for your typo. The internet forgives less than we do.

### [sanand0/talks](https://github.com/sanand0/talks)

	New talk published, site polish, and analytics injection for the talks site.

- **Published "AI Unboxed — Vibe Coding".** Added the full story, transcript, and site artifacts for the 22 Aug talk ([83961986](https://github.com/sanand0/talks/commit/83961986c3a747e3692b89e31f943386155afc52)). 26 Aug 2026. Takeaway: ship the talk assets immediately; they become research fodder.
- **Added GoatCounter analytics.** Injected a lightweight analytics snippet into generated HTML ([4a4596e3](https://github.com/sanand0/talks/commit/4a4596e3c1a5411ef8a99e4c231dde7600f16ced)). 26 Aug 2026. Takeaway: small privacy-respecting metrics beat no metrics.
- **Deployed and cleaned UI.** Updated dark-mode, removed inline styles, and adjusted README build steps before deployment ([adee649e](https://github.com/sanand0/talks/commit/adee649e9a16859ecfce3ddf7a6266e4fb4701f9)). 24 Aug 2026. Takeaway: cleanup reduces friction when publishing many talks.
- **Wry aside:** Yes, a talk page can use a room map and comic art. People love that.

### [sanand0/tools](https://github.com/sanand0/tools)

- **Improved ChatGPT scraper.** Rewrote scraper to capture scroll-loaded messages, timestamps, and provide a stable extraction API ([4ba3955](https://github.com/sanand0/tools/commit/4ba3955f394efd2a71962d9831ade04e9232a089)). 26 Aug 2026. Takeaway: scraping modern UIs needs scroll + timestamp strategies.
- **Added copy-links and text-fragment bookmarklets.** Bookmarklet UI to copy all links or a URL+text fragment ([227e8a54](https://github.com/sanand0/tools/commit/227e8a5410358dafc9cee1f7acfcfaded7ecd282)). 23 Aug 2026. Takeaway: small browser helpers save minutes, which cumulate.
- **Added GoatCounter analytics.** Injected analytics to public HTML during deploy ([e66f3d56](https://github.com/sanand0/tools/commit/e66f3d563594ca19eae9d3464dd641893f725b1e)). 26 Aug 2026. Takeaway: consistent telemetry across small tools helps prioritize work.
- **Wry aside:** Yes, browsers already have text-fragment handling. But a friendly bookmarklet is faster.

### [sanand0/embedumap](https://github.com/sanand0/embedumap)

_Embedding, UMAP maps, and more robust cache handling._

- **Portable embedding cache.** Look up cache hits by content hash so embeddings survive moved CSV paths ([eb6ec2c](https://github.com/sanand0/embedumap/commit/eb6ec2ce13e8e2a29b757f83c5ee0abab87c6465)). 27 Aug 2026. Takeaway: cache keys by content, not path.
- **Checkpoint embedding batches.** Store each successful batch to resume after partial failures ([c0ac947a](https://github.com/sanand0/embedumap/commit/c0ac947a4ce9d3274c3a60bae946c03eb5ac0ffc)). 27 Aug 2026. Takeaway: checkpoint long processes to recover from mid-run errors.
- **Wry aside:** Yes, UMAP needs fewer mysterious seeds and more reproducible checkpoints.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Tracking LLM cost × quality frontier._

- **Model data refreshed.** Updated ELO/leaderboard snapshots and adjusted last-updated date ([1576c49](https://github.com/sanand0/llmpricing/commit/1576c491e6f10e5b5740f8eea327f16c3c7e672b)). 23 Aug 2026. Takeaway: leaderboards move quickly—pin dates.
- **Added GoatCounter.** Lightweight analytics added to pages ([11a5899](https://github.com/sanand0/llmpricing/commit/11a5899270beb24fb3ba815d80d9e934c7f9f1c2)). 26 Aug 2026. Takeaway: even benchmarking pages deserve simple usage signals.
- **Wry aside:** The frontier changes faster than your last benchmark script.

### [sanand0/til](https://github.com/sanand0/til)

_Things learned notes, kept live._

- **Weekly notes updated.** TIL entries added about DuckDB 2.0, ffmpeg, and practical prompts ([6bb4899](https://github.com/sanand0/til/commit/6bb48995c60b1a01a39901944029f19634b05d60)). 23 Aug 2026. Takeaway: capture tiny wins; they compound into a long-term memory store.
- **Wry aside:** Yes, DuckDB is getting invasive. In a good way.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Podcast automation and weekly digests._

- **Weekly podcast episode file.** Updated the podcast script assets and episode notes for 23 Aug 2026 ([8eb9876](https://github.com/sanand0/generative-ai-group/commit/8eb987646b8e39ea2ceaae126fc5284a21b43643)). 23 Aug 2026. Takeaway: audio pipelines benefit from consistent source formats and clear transcripts.
- **Wry aside:** Yes, a weekly audio digest is just an asynchronous meeting.

### [sanand0/anand-skill-mcp](https://github.com/sanand0/anand-skill-mcp)

_Server exposing local SKILL.md as MCP tools._

- **Dynamic discovery of skills.** Build script now discovers skills under scripts/blog folders, avoiding manual lists ([6d6709e](https://github.com/sanand0/anand-skill-mcp/commit/6d6709ece66f7438ec86d66103514b2de6107b49)). 26 Aug 2026. Takeaway: auto-discovery keeps deployed connectors up-to-date.
- **Wry aside:** Yes, skills should be folders, not magic incantations.

### internal-courses/cs1002

_Course repo tweaks and deploy prompts._

- **Deploy & prompt edits.** Redirected repo pushes and added deploy notes in prompts for course analysis ([4d185a9](https://github.com/internal-courses/cs1002/commit/4d185a9cc78fc0126876d3ecd591b76ca99947fb)). 28 Aug 2026. Takeaway: keep deployment targets explicit in course repos.
- **Wry aside:** Push carefully — your CI will thank you.

### Site telemetry rollouts (many repos)

_A consistent change across many public sites: adding GoatCounter._

- **Injected lightweight analytics.** Several sites received GoatCounter snippets during deploys: talks, tools, llmdemos, llmpricing, imdb, datastories, llmartstyle, sanand0.github.io, llmmath, and tools-in-data-science-public (see commits like [4a4596e](https://github.com/sanand0/talks/commit/4a4596e3c1a5411ef8a99e4c231dde7600f16ced), [e66f3d5](https://github.com/sanand0/tools/commit/e66f3d563594ca19eae9d3464dd641893f725b1e), etc.). 24–26 Aug 2026. Takeaway: instrument publicly useful pages before guessing which features matter.
- **Wry aside:** Finally, numbers that don't sell your users' privacy.

## Lessons

- Small observability beats guesswork. Add minimal metrics before redesigning features.
- Cache by content, not path. Portability prevents repeated re-computation.
- Bound concurrency for blocking tools. Event-loop-friendly dispatch avoids large outages.
- Capture stable agent behavior with explicit rules. Clear fallback policies avoid silent downgrades.
- Ship talk assets and small posts early. They become shared artifacts, not one-offs.

## Suggestions

- Add a single telemetry dashboard aggregating the new GoatCounter signals. Start with page views and top referrers.
- Add a short checklist for skills that will be published to MCP: name, description, quick test case, and privacy note.
- For embedumap: surface a small resume/retry indicator in the UI when batch checkpoints exist.
- For prompt tools: schedule a monthly "prompt-census" job to surface unused prompts for cleanup.
- For agent harnesses: add a tiny "compaction policy" experiment that summarizes old context and measures effect on cost and latency.

If you want, I can draft the telemetry dashboard queries or open PR patches for the top three suggestions.