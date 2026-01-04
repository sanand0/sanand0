## A tidy January: content centralization, cleanup, and prettier pages

This week was about moving content to one canonical place, removing stale bits, and polishing UI for readers. The key lesson: centralize where it matters, remove what you don't use, and make the output delightful.

### [sanand0/blog](https://github.com/sanand0/blog)

_Consolidated site content and layout tweaks make the blog easier to maintain and nicer to read._

- **Prompts migrated into the site.** Dozens of prompt pages moved under pages/prompts and replaced elsewhere with redirects; see the big migration commit ([61392ee](https://github.com/sanand0/blog/commit/61392ee781ff77e9914b0a1a68b852f46d0a66e8)). (02 Jan 2026) Takeaway: Serve one canonical copy to avoid drift and duplication.
- **Enabled code-copy UI and wrapped code styling.** Turned on ShowCodeCopyButtons and added .wrap-code CSS for wrapped code blocks ([61392ee](https://github.com/sanand0/blog/commit/61392ee781ff77e9914b0a1a68b852f46d0a66e8), file: layouts/static/custom.css). (02 Jan 2026) Takeaway: Small UX bits make code snippets actually usable.
- **Footer and link normalization.** Footer now lists only pages under pages/, and many internal links moved to /blog/ paths ([61392ee](https://github.com/sanand0/blog/commit/61392ee781ff77e9914b0a1a68b852f46d0a66e8)). (02 Jan 2026) Takeaway: Keep content location consistent so navs and lists stay accurate.
- **Major migration from WordPress to Hugo.** Added README, GitHub Pages deploy workflow, assets, and initial Hugo layout ([aaa6ab7](https://github.com/sanand0/blog/commit/aaa6ab719100dbd485ac99a541b76be77059c6e7)). (31 Dec 2025) Takeaway: Static site moves simplify hosting and versioning — check CI Hugo version compatibility.
- Wry aside: Yes, you really needed another collection of prompt pages. But now they live where the site serves them.

### [sanand0/talks](https://github.com/sanand0/talks)

_Moved tooling out of talk repos to avoid duplication and simplify usage._

- **slide.py moved to scripts.** Removed the local slide runner and updated docs to reference the scripts repo ([2c20c4a](https://github.com/sanand0/talks/commit/2c20c4a36536c2965fcec4180365fd83d632e0df)). (02 Jan 2026) Takeaway: Keep reusable scripts in a shared repo, not copied across talks.
- **Docs updated to call the shared script.** References in README/slide docs now point at the scripts repo link. (02 Jan 2026) Takeaway: One source of truth makes demos easier to run.
- Wry aside: Slides are now homeless no more — they live with the scripts.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Cleanup and simplification: removed unused agent skills and old mounts, and tweaked setup helpers._

- **Removed the “plan” system skill and helpers.** Deleted agents/.system/plan and its scripts, docs, and license ([91d6e34](https://github.com/sanand0/scripts/commit/91d6e34fbb69fa7ef4f57a507fb211e2eeb145f4)). (28 Dec 2025) Takeaway: Remove unused features to reduce maintenance and security surface.
- **Dropped Hetzner rclone mount services.** Removed rclone-hetzner.service and weekly updater, and cleaned README mentions ([91d6e34](https://github.com/sanand0/scripts/commit/91d6e34fbb69fa7ef4f57a507fb211e2eeb145f4)). (28 Dec 2025) Takeaway: If you stop managing a remote mount, remove its automation and docs.
- **Shell and setup tweaks.** Added webp-lossless helper, notes about R2, and removed old rclone steps from setup/linux.md ([91d6e34](https://github.com/sanand0/scripts/commit/91d6e34fbb69fa7ef4f57a507fb211e2eeb145f4)). (28 Dec 2025) Takeaway: Keep setup docs aligned with what your scripts actually do.
- **Dev/tooling updates.** Bumped some package hints and added delta to dev.dockerfile to help diffs. (28 Dec 2025) Takeaway: Small developer ergonomics upgrades pay back often.
- Wry aside: The agent lost its planning module — which means fewer half-baked TODOs on disk.

### [sanand0/til](https://github.com/sanand0/til)

_Notes and course planning expanded, keeping weekly learnings and course ideas in one place._

- **Added TDS Jan 2026 notes.** New tds-jan-2026.md collects strand ideas and course tweaks for January ([1b87801](https://github.com/sanand0/til/commit/1b878019d6a6a62e4a92078d58cbf8c31bd0f256)). (28 Dec 2025) Takeaway: Capture course scaffolding early to iterate faster.
- **Big update to til.md.** Added December book notes, tooling tips, and TIL entries for rclone/xz/ty/npm and more ([1b87801](https://github.com/sanand0/til/commit/1b878019d6a6a62e4a92078d58cbf8c31bd0f256)). (28 Dec 2025) Takeaway: Keep notes searchable and timestamped for later reuse.
- **Trending repos and apps refreshed.** Updated trending-repos.tsv and apps.md with new entries and annotations ([1b87801](https://github.com/sanand0/til/commit/1b878019d6a6a62e4a92078d58cbf8c31bd0f256)). (28 Dec 2025) Takeaway: Weekly tracking surfaces new tools worth testing.
- Wry aside: More book lists. Because “read later” is the internet’s favorite hobby.

### [sanand0/prompts](https://github.com/sanand0/prompts)

_Prompts got clearer, and most content moved into the blog’s live pages._

- **Prompts migrated into blog/live pages.** Replaced local prompt files with short redirects to the blog live pages ([eb693aa](https://github.com/sanand0/prompts/commit/eb693aadedff349ddc98e7dbab8c32612bf89653)). (31 Dec 2025) Takeaway: Central hosting reduces duplication and fixes drift.
- **Refined custom instructions and fragments.** Improved ChatGPT instructions and added fragments like Book-summary, LinkedIn, and Sketchnote ([ffbb386](https://github.com/sanand0/prompts/commit/ffbb386cb32e379066f4f237467fdbd00e59ee03)). (28 Dec 2025) Takeaway: Positive, example-driven prompts are easier for models to follow.
- **Replaced large prompt contents with pointers.** README now points to blog/live pages for canonical content ([eb693aa](https://github.com/sanand0/prompts/commit/eb693aadedff349ddc98e7dbab8c32612bf89653)). (31 Dec 2025) Takeaway: One canonical URL means fewer stale forks.
- Wry aside: Prompts moved house — update bookmarks before your agent asks three times.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_New investigative story added, plus a nicer home page and card layout._

- **Added the Jamnagar Chokepoint story.** New interactive data story and analysis files added under exim/ (script, analysis, story drafts) ([8fd0baf](https://github.com/sanand0/datastories/commit/8fd0bafb13065e8da356d76b19b8c3fce68898d3)). (01 Jan 2026) Takeaway: Pairing LLM analysis with interactive viz fast-tracks publishable narratives.
- **Improved home page design and metadata.** Added fonts, card layout, dates, and screenshot metadata in config.json and index.html ([8f54200](https://github.com/sanand0/datastories/commit/8f542001fbdd948bcc5d1e46bf68f5c95608e5cb)). (01 Jan 2026) Takeaway: Small visual changes improve discoverability and trust.
- **Script and assets for the story.** Heavy-lift JS and content files landed, so expect richer interactivity and bigger payloads. See exim/script.js and ANALYSIS.md ([8fd0baf](https://github.com/sanand0/datastories/commit/8fd0bafb13065e8da356d76b19b8c3fce68898d3)). (01 Jan 2026) Takeaway: Large data stories need a regen workflow and asset audit.
- Wry aside: Port drama makes for great data storytelling. Who knew customs could be so suspenseful?

### [sanand0/tools](https://github.com/sanand0/tools)

/UI polish, mobile layout, and small UX tweaks across tools and icons._

- **Made Trending Repos mobile-friendly.** Added responsive card layout, mobile sort UI, and touch-friendly interactions ([8270776](https://github.com/sanand0/tools/commit/8270776d031a1f80992244b70dab2d7820d86514)). (01 Jan 2026) Takeaway: Desktop tables don’t cut it on phones; test on real devices.
- **Updated favicons and left ideator model unspecified.** Swapped icon data URLs and removed hardcoded model param in ideator script ([d0590bc](https://github.com/sanand0/tools/commit/d0590bcb520a1034adb172009f4d773840aac56d)). (01 Jan 2026) Takeaway: Avoid hardcoding model ids so frontend links stay flexible.
- **Tweaked Trending Repos title and small text fixes.** Title simplified for clarity and small UI polish applied ([bf51146](https://github.com/sanand0/tools/commit/bf511467b8d69c5e2e7e7aabfb9f2ccd5356c03d)). (01 Jan 2026) Takeaway: Tiny copy changes improve scanning.
- Wry aside: Yes, people browse repos on phones. Optimize for thumbs.

### [sanand0/tutorials](https://github.com/sanand0/tutorials)

_Clearer LLM profile examples and provider config snippets for easier setup._

- **Expanded README config examples.** Added OpenAI and OpenRouter profiles and noted Azure needs deployment names ([70345ed](https://github.com/sanand0/tutorials/commit/70345ed562190ac69b4528b11beb5f8508841875)). (02 Jan 2026) Takeaway: Clear examples reduce onboarding friction.
- **Added wire_api and model fields for llmfoundry profiles.** Provided example env var names and base_url hints for each provider. (02 Jan 2026) Takeaway: Show exact env var names to avoid subtle runtime failures.
- **Included a CLI test hint.** Small commented snippet demonstrates testing profiles with codex locally. (02 Jan 2026) Takeaway: Quick smoke tests catch config issues early.
- Wry aside: Azure wants deployment names, because cloud UX enjoys puzzles.

## Lessons

- Centralize content that changes often. One canonical source saves link rot.
- Remove unused automation and features. Dead code hides risk.
- Small UX fixes (code-copy, wrap, favicons) raise practical usability a lot.
- Data stories need both rigorous analysis and web performance checks.
- Keep developer docs and config examples explicit. Environment var names matter.

## Suggestions

- Verify the blog CI runs the Hugo version that supports fileExists and File.Path. Add a CI check.  
- Add redirects or update external links that pointed to old prompt files. Confirm sitemap updates.  
- For datastories, add an asset-size audit and lazy-load heavy viz scripts. Measure page load.  
- Add a short note in scripts/README about removed Hetzner services, and a rollback plan if needed.  
- Run a mobile accessibility and performance pass on Trending Repos and Datastories (Lighthouse).  
- Add a tiny smoke test that opens a few migrated prompt pages to confirm page params and footer listing.  

If you want, I can draft the CI check snippet for Hugo version verification, and a short checklist to verify the blog footer lists new pages correctly.