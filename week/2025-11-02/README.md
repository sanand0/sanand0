## A week of course polish, UI themes, and scraping tools — small changes, big clarity wins.

This week focused on course content, presentation tooling, and practical scraping/agent improvements. The key lesson: clear docs and tight defaults save far more time than clever code.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_Clarified Project 2 and replaced a module with richer, LLM-driven course content so students hit real-world workflows._

- **Project 2 fleshed out and hardened.** Updated instructions, sample payload, and demo endpoint. See commits [7a497c2](https://github.com/sanand0/tools-in-data-science-public/commit/7a497c2aa4ddf71f807b584178941f429245bbfe) (29 Oct 2025) and [50f632e](https://github.com/sanand0/tools-in-data-science-public/commit/50f632e78bc861f6d6f5d997d8c37454a55a5cf4) (01 Nov 2025). Files: [project-llm-analysis-quiz.md](https://github.com/sanand0/tools-in-data-science-public/blob/7a497c2aa4ddf71f807b584178941f429245bbfe/project-llm-analysis-quiz.md). Takeaway: clear test vectors and a demo URL reduce student confusion and grading friction.
- **Security and API guidance tightened.** Prompts now state HTTPS preference and verify secrets; endpoints must return 403 on bad secrets ([365f6fa](https://github.com/sanand0/tools-in-data-science-public/commit/365f6fab06fe61c132368574c50dae7cbed63342), 01 Nov 2025). File: [project-llm-analysis-quiz.md](https://github.com/sanand0/tools-in-data-science-public/blob/365f6fab06fe61c132368574c50dae7cbed63342/project-llm-analysis-quiz.md). Takeaway: explicit security checks avoid flaky automated grading.
- **Curriculum overhaul: Vibe Analysis, scraping, Datasette.** Replaced ChatGPT module with _Vibe Analysis_ and added LLM scraping + Datasette guides ([11f3c4b](https://github.com/sanand0/tools-in-data-science-public/commit/11f3c4b8fe4cd4f3ff430e1547e998dff44f39b6), 28 Oct 2025). Files: [vibe-analysis.md](https://github.com/sanand0/tools-in-data-science-public/blob/11f3c4b8fe4cd4f3ff430e1547e998dff44f39b6/vibe-analysis.md), [llm-website-scraping.md](https://github.com/sanand0/tools-in-data-science-public/blob/11f3c4b8fe4cd4f3ff430e1547e998dff44f39b6/llm-website-scraping.md). Takeaway: course content that models modern workflows is worth more than perfect slides.

Aside: yes, students will still try to deploy on the last night.

### [sanand0/marpessa](https://github.com/sanand0/marpessa)

_More flexible slide layouts and hidden-transcript support make presentations easier and cleaner._

- **New layout utilities & header/footer justify.** Added `columns-justify` and consistent padding variables to tidy multi-column layouts ([1c626c3](https://github.com/sanand0/marpessa/commit/1c626c37fdb857c60e079837f1cfa8444763318d), 30 Oct 2025). Files: [README.md](https://github.com/sanand0/marpessa/blob/1c626c37fdb857c60e079837f1cfa8444763318d/README.md), [marpessa.css](https://github.com/sanand0/marpessa/blob/1c626c37fdb857c60e079837f1cfa8444763318d/marpessa.css). Takeaway: small layout utilities avoid slide-by-slide CSS hacks.
- **Add hidden <transcript> tag.** New tag hides transcripts in slides but keeps them in Markdown viewers ([eaaa8f7](https://github.com/sanand0/marpessa/commit/eaaa8f764fda67bdb1b78011dca7211d7f475fdb), 30 Oct 2025). Files: [README.md](https://github.com/sanand0/marpessa/blob/eaaa8f764fda67bdb1b78011dca7211d7f475fdb/README.md), [marpessa.css](https://github.com/sanand0/marpessa/blob/eaaa8f764fda67bdb1b78011dca7211d7f475fdb/marpessa.css). Takeaway: keep slide visuals minimal while preserving full text for accessibility and notes.
- **Font sizing, CI fixes, and build automation.** Added `.small-*` classes, corrected GitHub Action build command, and added theme and deploy assets ([44f4f65](https://github.com/sanand0/marpessa/commit/44f4f65746b88f0b07155247acc249c694d8e31f), 29 Oct 2025) plus deploy flow ([c828df1](https://github.com/sanand0/marpessa/commit/c828df10bb53c97e9f3f80164a7c3242ac1bb133), 29 Oct 2025). Files: [.github/workflows/deploy.yml](https://github.com/sanand0/marpessa/blob/c828df10bb53c97e9f3f80164a7c3242ac1bb133/.github/workflows/deploy.yml). Takeaway: shipping themes means automating the build and keeping the CLI command correct.

Aside: yes, another CSS variable. It helps.

### [sanand0/talks](https://github.com/sanand0/talks)

(Slides now use the new Marp theme; data viz materials expanded.)

_Standardized slide builds and bundled a comprehensive LLM visualization kit._

- **Apply Marpessa theme and refactor build.** Download theme dynamically and centralize build into setup.sh; ignore downloaded theme in git ([a1e77d8](https://github.com/sanand0/talks/commit/a1e77d845932579fe46f73067a1af8e551e92ef1), 30 Oct 2025). Files: [setup.sh](https://github.com/sanand0/talks/blob/a1e77d845932579fe46f73067a1af8e551e92ef1/setup.sh). Takeaway: reproducible builds mean fewer "works on my machine" slides.
- **Add LLM Data Visualization materials.** New demos, notebooks, and scripts for SOM, UMAP, and novel viz concepts ([fb41e6f](https://github.com/sanand0/talks/commit/fb41e6fb0c42d5a620d381aba517137a90aad9d1), 30 Oct 2025). Files: [2025-10-29-llm-data-visualization/README.md](https://github.com/sanand0/talks/blob/fb41e6fb0c42d5a620d381aba517137a90aad9d1/2025-10-29-llm-data-visualization/README.md). Takeaway: ship runnable examples so talks double as tutorials.
- **Large, reproducible examples included.** Complete datasets, generation scripts, and classroom kits added for teaching. See the CLAUDE/SOM packages under the talk folder. Takeaway: if you teach, include ready-to-run demos so students don't wrestle with installs.

Aside: slides now wear a theme; slides look smarter than the speaker sometimes.

### [sanand0/scripts](https://github.com/sanand0/scripts)

Major tooling polish: CLI fixes, agent docs, and dev container improvements.

_This week tightened CLI UX, updated agent docs, and hardened developer workflows._

- **Gmail CLI refactor to async + JSONL.** Rewrote `gmail.py` to use AsyncClient, stream results, and produce JSONL option ([e035855](https://github.com/sanand0/scripts/commit/e035855bf38d1b41effe39a412d7fb3a19305822), 01 Nov 2025). File: [gmail.py](https://github.com/sanand0/scripts/blob/e035855bf38d1b41effe39a412d7fb3a19305822/gmail.py). Takeaway: streaming avoids memory bloat and simplifies piping.
- **Agent SKILLs and AGENTS.md cleanup.** Trimmed remote skill links, clarified AGENTS.md, and added devtools SKILL ([e035855](https://github.com/sanand0/scripts/commit/e035855bf38d1b41effe39a412d7fb3a19305822), 01 Nov 2025). Files: [agents/AGENTS.md](https://github.com/sanand0/scripts/blob/e035855bf38d1b41effe39a412d7fb3a19305822/agents/AGENTS.md). Takeaway: central, concise agent docs reduce onboarding friction.
- **Dev container and tooling improvements.** Big dev.sh and dev docker tweaks, whisper integration, mise tool updates, and robust google OAuth handling ([3e89ddb](https://github.com/sanand0/scripts/commit/3e89ddb964df23b8a3f1a1ee003c8b9f023dff40), 26 Oct 2025). Files: [dev.sh](https://github.com/sanand0/scripts/blob/3e89ddb964df23b8a3f1a1ee003c8b9f023dff40/dev.sh), [google_oauth.py](https://github.com/sanand0/scripts/blob/3e89ddb964df23b8a3f1a1ee003c8b9f023dff40/google_oauth.py). Takeaway: pre-baked environments save hours later.

Aside: yes, your dev container wants your GPU and way too many mounts.

### [sanand0/tools](https://github.com/sanand0/tools)

New scraper for X (Twitter); tests and verification included.

_Adds an X thread bookmarklet, tests, and verification scripts for reliable scraping._

- **X Thread Scraper bookmarklet.** New `xscraper` tool extracts a tweet and replies to JSON, drops ads, computes buzz/keep scores ([f4a2a3e](https://github.com/sanand0/tools/commit/f4a2a3e44d71530abe7ae8d23fc6a77187056d62), 26 Oct 2025). Files: [xscraper/xscraper.js](https://github.com/sanand0/tools/blob/f4a2a3e44d71530abe7ae8d23fc6a77187056d62/xscraper/xscraper.js), [xscraper/index.html](https://github.com/sanand0/tools/blob/f4a2a3e44d71530abe7ae8d23fc6a77187056d62/xscraper/index.html). Takeaway: bookmarklets remain the fastest way to scrape in-browser without extensions.
- **Tests and verification via Chrome DevTools.** Added fixture HTML, Vitest tests, and a CDP-based verify script ([f4a2a3e](https://github.com/sanand0/tools/commit/f4a2a3e44d71530abe7ae8d23fc6a77187056d62), 26 Oct 2025). Files: [xscraper/verify.mjs](https://github.com/sanand0/tools/blob/f4a2a3e44d71530abe7ae8d23fc6a77187056d62/xscraper/verify.mjs). Takeaway: automated in-browser verification prevents brittle bookmarklets.
- **Prompts and README updates.** Documented prompts for scraping and added tool entries to site index ([e92a558](https://github.com/sanand0/tools/commit/e92a558d75434d5b62366301fc7e5836cb98dd54), 26 Oct 2025). Files: [xscraper/prompts.md](https://github.com/sanand0/tools/blob/e92a558d75434d5b62366301fc7e5836cb98dd54/xscraper/prompts.md). Takeaway: capture prompts and test cases for reproducibility.

Aside: Thread scraper name changed to “❌ Thread Scraper” — dramatic, but clear.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Podcast script refresh; week digest improved for clarity and action._

- **New weekly podcast episode content.** Polished script for 26 Oct 2025 episode with actionable tips on agents and latency ([189bb73](https://github.com/sanand0/generative-ai-group/commit/189bb7316d76f5d07e603ad2fd509ca467af5edd), 26 Oct 2025). File: [2025-10-26/podcast-2025-10-26.md](https://github.com/sanand0/generative-ai-group/blob/189bb7316d76f5d07e603ad2fd509ca467af5edd/2025-10-26/podcast-2025-10-26.md). Takeaway: make dense threads audible with clear ops tips.
- **Large message import updated.** gen-ai-messages.json grew to capture threads for episodes (massive append) ([189bb73], 26 Oct 2025). File: [gen-ai-messages.json](https://github.com/sanand0/generative-ai-group/blob/189bb7316d76f5d07e603ad2fd509ca467af5edd/gen-ai-messages.json). Takeaway: keep raw transcripts versioned but treat them as data, not prose.

Aside: yes, someone will say “this episode saved my latency budget.”

### [sanand0/tutorials](https://github.com/sanand0/tutorials)

_Config examples expanded to support Azure, Gemini, OpenRouter in Codex LLM Foundry._

_More provider profiles make switching trivial for experimenters._

- **Add Azure / Gemini / OpenRouter configs.** Example `config.toml` now shows multiple LLM Foundry profiles and Azure default ([1249fa6b](https://github.com/sanand0/tutorials/commit/1249fa6b21d9b8427b65fa72dc946d3effd37cc4), 27 Oct 2025). File: [codex-llmfoundry/README.md](https://github.com/sanand0/tutorials/blob/1249fa6b21d9b8427b65fa72dc946d3effd37cc4/codex-llmfoundry/README.md). Takeaway: concrete examples reduce integration friction.
- **Clarify Azure as default example.** Makes on-ramp smoother for folks with Azure deployments ([c02d6f1](https://github.com/sanand0/tutorials/commit/c02d6f12ceef241189619f43f5fbbf7b31f7b765), 27 Oct 2025). Takeaway: pick a sane default to prevent copy-paste mistakes.

Aside: yes, “llmfoundry_openai” renamed — your config file appreciates it.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Experiment added to measure OpenAI prompt caching behavior._

- **Prompt caching experiment repository.** Added scripts to run and analyze caching tests, plus README and data ([c84e7b6](https://github.com/sanand0/datastories/commit/c84e7b6ce1e31c98a4abab81f2bcdc3497be9c7a), 01 Nov 2025). Files: [openai-caching/scripts/run_cache_eval.py](https://github.com/sanand0/datastories/blob/c84e7b6ce1e31c98a4abab81f2bcdc3497be9c7a/openai-caching/scripts/run_cache_eval.py). Takeaway: run controlled experiments to validate platform docs.
- **Findings and summary added.** README and summary show variable lag and TTL behavior in caches. File: [openai-caching/README.md](https://github.com/sanand0/datastories/blob/c84e7b6ce1e31c98a4abab81f2bcdc3497be9c7a/openai-caching/README.md). Takeaway: document empirical caveats; docs rarely match every edge case.

Aside: yes, prompt caching exists — but it sometimes naps.

### [sanand0/videohighlights](https://github.com/sanand0/videohighlights)

_Minor docs polish for transcript extraction._

_More explicit setup steps for transcript pipeline and groq-whisper usage._

- **Clarify transcript pipeline commands.** Added llm groq-whisper example and key setup step ([a0973cc](https://github.com/sanand0/videohighlights/commit/a0973cc5b400ac5bcadd046e6f0cb90c21ed5278), 30 Oct 2025). File: [README.md](https://github.com/sanand0/videohighlights/blob/a0973cc5b400ac5bcadd046e6f0cb90c21ed5278/README.md). Takeaway: small doc lines avoid large setup headaches.

Aside: no, your audio files won't transcribe themselves.

### [sanand0/prompts](https://github.com/sanand0/prompts)

_Sharper guidance for call-recording analysis prompts._

_More explicit "missed statements" checks and prioritized experiments._

- **Tighten call recording analysis prompt.** Now asks reviewers to check missed statements even at conversation end, and to evaluate ten ideas and pick three ([3da142a](https://github.com/sanand0/prompts/commit/3da142a319b93762ca5e3af9977271915a02017e), 26 Oct 2025). File: [analyze-call-recording.md](https://github.com/sanand0/prompts/blob/3da142a319b93762ca5e3af9977271915a02017e/analyze-call-recording.md). Takeaway: more explicit instructions yield better, actionable outputs.

Aside: yes, the prompts now nag more politely.

### [sanand0/til](https://github.com/sanand0/til)

_Weekly learnings and repo curation updates keep the notes fresh._

- **October notes and trending repos updated.** Added LLM & agent insights, refined trending-repos.tsv statuses ([bc4ece2](https://github.com/sanand0/til/commit/bc4ece2023579fb512f50237929451e9af889549), 26 Oct 2025). Files: [llms.md](https://github.com/sanand0/til/blob/bc4ece2023579fb512f50237929451e9af889549/llms.md), [trending-repos.tsv](https://github.com/sanand0/til/blob/bc4ece2023579fb512f50237929451e9af889549/trending-repos.tsv). Takeaway: a tidy notes repo keeps institutional memory searchable.

Aside: yes, trending repos got a little judgmental.

## Lessons

- Small docs beats clever code. Clear examples and demo endpoints cut support time dramatically.
- Automate verification for brittle UI glue like bookmarklets and slide builds.
- Defaults matter. A sane default profile or HTTPS preference prevents many support tickets.
- Empirical testing uncovers platform quirks. Run small experiments to validate documentation assumptions.
- Keep reproducible demos with data and scripts for teaching and evaluation.

## Suggestions

- Add a short checklist and CI lint for course project submissions (format, HTTPS, license). That reduces manual grading work.
- For Marpessa: publish a tiny gallery page showing columns-justify and transcript use cases.
- Add a lightweight smoke test for xscraper deploys using the verify.mjs CDP flow in CI.
- Consolidate agent SKILLs into a single searchable JSON for programmatic injection into agent configs.
- Convert the OpenAI caching experiment outputs into a simple dashboard (CSV → small HTML) to visualize TTL and latency trends.

If you want, I can draft the checklist for Project 2, a sample smoke-test workflow for xscraper, or a short CI job to generate Marp pages. Which would help most next?