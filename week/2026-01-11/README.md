## Videos, data stories, and smarter tools — a week of polish, new content, and AI-powered rewrites.

This week focused on shipping content and tightening tooling. The key lesson: small infra and UX fixes multiply into bigger discoverability wins.

### [sanand0/talks](https://github.com/sanand0/talks)

_Added videos, slides, and better navigation so talks are easier to browse and reuse. Yes, another video index — but now with better icons and copies of originals._

- **Added talk videos and icons (09 Jan 2026):** Updated the main [README.md](https://github.com/sanand0/talks/blob/main/README.md) to show video icons and added links. See [3b86b10](https://github.com/sanand0/talks/commit/3b86b10ce027c528a7000c3ee278e6e1d35e7e16). Takeaway: small UX signals make content easier to scan.
- **Imported The Hindu webinar (04 Jan 2026):** Added full webinar page and images at [2024-10-19-ai-in-education-webinar/README.md](https://github.com/sanand0/talks/blob/main/2024-10-19-ai-in-education-webinar/README.md). See [0838c93](https://github.com/sanand0/talks/commit/0838c93e5b957fe63be152bbf259283b8beb1e38). Takeaway: canonical pages reduce broken links.
- **Backfilled past videos (04 Jan 2026):** Added many historical video links and adjusted [index.html](https://github.com/sanand0/talks/blob/main/index.html) styles. See [d27eb34](https://github.com/sanand0/talks/commit/d27eb348d23d8828e37620da3dda6c3f7b866bb8). Takeaway: completeness increases reuse and citation.
- **Updated Q&A transcript (04 Jan 2026):** Improved the social-code analysis transcript at [2025-08-11-social-code-analysis/transcript.md](https://github.com/sanand0/talks/blob/main/2025-08-11-social-code-analysis/transcript.md). See [520a468](https://github.com/sanand0/talks/commit/520a468efe0fbf39b9f45ad15303c7208959c25a). Takeaway: transcripts increase accessibility and searchability.

### [sanand0/tools](https://github.com/sanand0/tools)

_Rewrote a major tool to use Claude, updated test tooling, and unified UI patterns across tools. Yes, Claude now helps brainstorm — consider it the new intern._

- **Rewrote Ideator with Claude (09 Jan 2026):** Replaced the ideator logic and UI. See [5febf11](https://github.com/sanand0/tools/commit/5febf11565ee5c25472d7f9452053ab151ec7942) and files like [ideator/script.js](https://github.com/sanand0/tools/blob/main/ideator/script.js) and [ideator/index.html](https://github.com/sanand0/tools/blob/main/ideator/index.html). Takeaway: swapping models improves idea quality fast.
- **Bumped Playwright (09 Jan 2026):** Upgraded dev dependency in [package.json](https://github.com/sanand0/tools/blob/main/package.json) for test reliability. See [b10fb97](https://github.com/sanand0/tools/commit/b10fb9726bbe36ddb8005c1dfdbd5ff888a0b78b). Takeaway: keep test libs current to avoid CI flakes.
- **Standardized navbar guidance (09 Jan 2026):** Clarified pattern in [AGENTS.md](https://github.com/sanand0/tools/blob/main/AGENTS.md). See [2836480](https://github.com/sanand0/tools/commit/2836480d9360ddd094a536448e58e6f68e8efa73). Takeaway: consistent UI reduces maintenance and cognitive load.

### [sanand0/til](https://github.com/sanand0/til)

	Documented fresh LLM notes, added CLI tool picks, and refreshed the weekly trending list. Your CLI backpack expanded this week.

- **Added Jan 2026 LLM notes (04 Jan 2026):** New section in [llms.md](https://github.com/sanand0/til/blob/live/llms.md) covering eval behavior and context compaction. See [0c8b5b0](https://github.com/sanand0/til/commit/0c8b5b090f65f942119058e2b4f3700dc6dd8ee7). Takeaway: record small LLM tricks before you forget them.
- **Expanded TIL entries (04 Jan 2026):** Added CLI tool recommendations and book notes in [til.md](https://github.com/sanand0/til/blob/live/til.md). See [0c8b5b0](https://github.com/sanand0/til/commit/0c8b5b090f65f942119058e2b4f3700dc6dd8ee7). Takeaway: curate tools you actually use, not everything shiny.
- **Refreshed trending repos (04 Jan 2026):** Updated [trending-repos.tsv](https://github.com/sanand0/til/blob/live/trending-repos.tsv). See [0c8b5b0](https://github.com/sanand0/til/commit/0c8b5b090f65f942119058e2b4f3700dc6dd8ee7). Takeaway: keep your watchlist current to avoid chasing dead ends.

### [sanand0/eslint-plugin-template](https://github.com/sanand0/eslint-plugin-template)

_A small security and version bump to keep publishing safe. Not glamorous, but quietly important._

- **Run npm audit and bump version (08 Jan 2026):** Updated [package.json](https://github.com/sanand0/eslint-plugin-template/blob/main/package.json) and [package-lock.json](https://github.com/sanand0/eslint-plugin-template/blob/main/package-lock.json). See [8bf3c49](https://github.com/sanand0/eslint-plugin-template/commit/8bf3c49c1b5bb938c5bd928d276dd2bf1d907132). Takeaway: fix vulnerabilities early to avoid downstream trouble.
- **Version increment (08 Jan 2026):** Package now at 0.7.3. See same commit. Takeaway: a tiny version bump signals safe publishing.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Launched a full investigative story and analysis pipeline about hidden package dependency risk. Surprise: obscure packages can be surprisingly central._

- **Added "The Invisible Infrastructure" story (08 Jan 2026):** New site at [package-usage/index.html](https://github.com/sanand0/datastories/blob/main/package-usage/index.html). See [9c523e6](https://github.com/sanand0/datastories/commit/9c523e6ee477e5b84d37547d08d60cfeb8d4a7f7). Takeaway: stories need both code and narrative.
- **Included analysis code and fetchers (08 Jan 2026):** Added [run_analyses.py](https://github.com/sanand0/datastories/blob/main/package-usage/run_analyses.py) and [fetch_libraries.py](https://github.com/sanand0/datastories/blob/main/package-usage/fetch_libraries.py). See [9c523e6](https://github.com/sanand0/datastories/commit/9c523e6ee477e5b84d37547d08d60cfeb8d4a7f7). Takeaway: ship reproducible analysis with stories.
- **Bundled analysis outputs (08 Jan 2026):** Added large CSVs under [package-usage/analysis_results/](https://github.com/sanand0/datastories/tree/main/package-usage/analysis_results). See same commit. Takeaway: include evidence to build trust.
- **Updated site config and story list (08 Jan 2026):** Added the story to root [README.md](https://github.com/sanand0/datastories/blob/main/README.md) and [config.json](https://github.com/sanand0/datastories/blob/main/config.json). See same commit. Takeaway: surface new work where readers look.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Added a terminal slide viewer and refined machine setup docs. Terminal slides: for the developer who secretly misses PowerPoint._

- **Added terminal Markdown slide viewer (04 Jan 2026):** New [slide.py](https://github.com/sanand0/scripts/blob/main/slide.py) with rich rendering. See [ffe442e](https://github.com/sanand0/scripts/commit/ffe442e4a4e22b2af8596deab5c4af2c56f56c93). Takeaway: lightweight tools speed demos.
- **Updated setup and tool abbreviations (04 Jan 2026):** Edited [setup.fish](https://github.com/sanand0/scripts/blob/main/setup.fish) and [setup/linux.md](https://github.com/sanand0/scripts/blob/main/setup/linux.md). See same commit. Takeaway: small shell niceties save hours.
- **Docs and agent tooling tweaks (04 Jan 2026):** Improved agents docs and preferred libs in [agents/code/SKILL.md](https://github.com/sanand0/scripts/blob/main/agents/code/SKILL.md). See same commit. Takeaway: document conventions to avoid future bike-shedding.

### [sanand0/ai-in-education-webinar](https://github.com/sanand0/ai-in-education-webinar)

_Redirected the standalone webinar site into the central talks hub. One click and you're in the right place._

- **Redirected site to talks (04 Jan 2026):** Replaced [index.html](https://github.com/sanand0/ai-in-education-webinar/blob/main/index.html) with a redirect to the talks page. See [c44520e](https://github.com/sanand0/ai-in-education-webinar/commit/c44520e6add9aa8e41ec7243bed4fae1d49786a9). Takeaway: avoid scattered pages by centralizing content.
- **Cleaned README (04 Jan 2026):** Removed old docs and pointed to talks repo. Same commit. Takeaway: redirects reduce bit-rot.

### [sanand0/blog](https://github.com/sanand0/blog)

	Bulk content push and build fixes. Expect more posts, lists, and improved RSS behavior. Your RSS feed will be busier.

- **Added lists, quotes, and new posts (04 Jan 2026):** New pages under [pages/lists/](https://github.com/sanand0/blog/tree/main/pages/lists) and posts like [migrating-my-blog-from-wordpress-to-hugo.md](https://github.com/sanand0/blog/blob/main/posts/2026/migrating-my-blog-from-wordpress-to-hugo.md). See [c8d553c](https://github.com/sanand0/blog/commit/c8d553c995cf2834acd8381ac92d66ade558f470). Takeaway: frequent, small content additions keep sites alive.
- **Fixed build and RSS logic (04 Jan 2026):** Improved [scripts/build_content.py](https://github.com/sanand0/blog/blob/main/scripts/build_content.py) date handling and RSS templates. See same commit. Takeaway: robust build scripts avoid bad deploys.
- **Styling and favicon tweaks (04 Jan 2026):** CSS and SVG favicon fixes for better emoji rendering. See same commit. Takeaway: small visual fixes improve polish.

## Lessons

- Show and link evidence. Stories with code and data gain credibility.  
- Maintainability beats clever hacks. Small refactors avoid future friction.  
- Ship content with reproducible analysis. Readers trust reproducible outputs.  
- Keep dev tooling current. CI and test libs rot fast without updates.  
- Centralize content. Redirects and canonical pages reduce fragmentation.

## Suggestions

- Add short release notes for major content pushes, with highlights and TL;DRs.  
- For Ideator, add a simple A/B test comparing outputs from Claude and other models.  
- Publish a tiny reproducibility README for the package-usage analysis. Link scripts, data, and commands.  
- Add CI checks for the talks repo to verify video links and slides exist.  
- Run a quick audit on large CSVs in datastories to see if they can be trimmed or zipped before publishing.

If you want, I can draft the reproducibility README for package-usage or a one-paragraph announcement for the new story.