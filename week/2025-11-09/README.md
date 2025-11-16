## A week of polishing course infrastructure, scrapers, and LLM tooling.

Small, focused updates made course delivery smoother, added scrapers and tests, and tightened LLM UX and docs. The key lesson: invest a little time in tooling now to save a lot of friction later.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_Kept the course engine running: clearer deadlines, better live-session tooling, and more student-facing links. Yes, the FAQ script finally learned to chunk videos — your students will thank you._  

- **Project 2 deadline clarified.** Updated the schedule and added an explicit live evaluation slot. See [3aa156d](https://github.com/sanand0/tools-in-data-science-public/commit/3aa156d7879b4217a8a696667f0376e86b43302b) (README.md). Takeaway: explicit dates reduce last-minute panic.
- **Robust live-session FAQ pipeline.** Rewrote and documented live-sessions/faq.sh to chunk long videos and cache outputs. See [6c10e6a](https://github.com/sanand0/tools-in-data-science-public/commit/6c10e6a15986263c292dbb1f446d38710fcc4088) (live-sessions/faq.sh). Takeaway: chunk long media to avoid brittle long-run jobs.
- **Bulk-imported live session transcripts.** Added multiple session FAQs and playlist entries for reproducible caching. See [6c10e6a](https://github.com/sanand0/tools-in-data-science-public/commit/6c10e6a15986263c292dbb1f446d38710fcc4088) (live-sessions/*.md, playlist.tsv) — 02 Nov 2025. Takeaway: cached transcripts make reruns cheap.
- **Student resources & course links.** Added community solutions and small project tweaks. See [691b040](https://github.com/sanand0/tools-in-data-science-public/commit/691b040a3b60bd83adbd12a6634f3b166fc9d23e) and [507fb50](https://github.com/sanand0/tools-in-data-science-public/commit/507fb50eb47806c53b393f7ae8a233e741e0c513) (README.md, project-llm-analysis-quiz.md). Takeaway: quick links reduce help requests.

### [sanand0/talks](https://github.com/sanand0/talks)

_Added and corrected talk material so talks are discoverable and accurate for reuse. Yes, slides still get renamed in mysterious ways._  

- **New LLM Psychology podcast deck.** Added full Marp slides and transcript. See [eb1d2aa](https://github.com/sanand0/talks/commit/eb1d2aa9e48efe6adeffbe736b8f48786d0175b2) (2025-11-06-llm-psychology/README.md). Takeaway: publish slides with transcripts for accessible reuse.
- **Fix PPTX slide links.** Normalized filenames so Office web viewer links work. See [b1d345e](https://github.com/sanand0/talks/commit/b1d345ee28028185985acfed0eac4b3fcda2a25f) (README.md) — 06 Nov 2025. Takeaway: predictable release filenames save confused click-throughs.
- **Add Diagram Chasing talk and errata.** Imported talk slides and corrected metadata. See [d2af9f8](https://github.com/sanand0/talks/commit/d2af9f822dd2607cbf486ccb63b752b5cf72874a) and [8442104](https://github.com/sanand0/talks/commit/8442104e14e86706fba490f36685aaf61472bbda). Takeaway: keep event credits and links tidy.

### [sanand0/tools](https://github.com/sanand0/tools)

(Selection of small app improvements, plus a new Discourse scraper.) _More bookmarklets and one more “useful toy.” Yes, another scraper — but this one copies whole threads._  

- **Discourse Thread Scraper added.** New bookmarklet, UI, tests, and build script. See [2f9c473](https://github.com/sanand0/tools/commit/2f9c473659377190af95e59aa32f78d9ea5f7d06) (discoursescraper/**). Takeaway: one-click thread dumps speed research and archiving.
- **Trending labels renamed.** Made status labels clearer in UI. See [db22226](https://github.com/sanand0/tools/commit/db22226fcba358f82d8a000ff7e020cbc2645760) (trending-repos/script.js) — 05 Nov 2025. Takeaway: tiny wording changes cut cognitive load.
- **Added external tools listing.** Linked Simon Willison’s Terminal-to-HTML tool. See [249745f](https://github.com/sanand0/tools/commit/249745f4021c8a58ac2fac90d647c84c4d7ca986) (README.md, tools.json). Takeaway: curated references avoid reinventing wheels.
- **Discoursescraper unit tests and CI helpers.** Included tests and fixtures for reliable scraping. See [2f9c473](https://github.com/sanand0/tools/commit/2f9c473659377190af95e59aa32f78d9ea5f7d06) (discoursescraper/*.test.js). Takeaway: tests make bookmarklets usable at scale.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Tooling and developer ergonomics got a tidy upgrade. Yes, pre-commit will nag you — in a kind way._  

- **Pre-commit and dev smoke tests.** Added .pre-commit-config.yaml and dev.test.sh. See [f9beb41](https://github.com/sanand0/scripts/commit/f9beb41a983fca56f9f359e05a8cbec3bf1abe0c) — 02 Nov 2025. Takeaway: automated checks catch regressions early.
- **Session list filters and truncation.** claude/codex/copilot list scripts now accept a filter and truncate messages. See [f9beb41](https://github.com/sanand0/scripts/commit/f9beb41a983fca56f9f359e05a8cbec3bf1abe0c) (claudelist, codexlist, copilotlist). Takeaway: searchable session logs save time.
- **Cache guideline for agents.** Documented caching LLM/API calls in .cache/. See [bea7117](https://github.com/sanand0/scripts/commit/bea711776710314e2de398c22a19034da8b1bf69) (agents/code/SKILL.md) — 03 Nov 2025. Takeaway: cache in loops to cut cost and latency.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Updated pricing and model frontier data so your cost-quality chart stays current._  

- **Updated models and pricing data.** Big refresh to elo.csv. See [097ee78](https://github.com/sanand0/llmpricing/commit/097ee7843fc28b6e5278539a2caef19afd99127e) — 03 Nov 2025. Takeaway: frontier moves fast; refresh often.
- **Updated "last updated" date.** README date reflects the refresh. See [ce19161](https://github.com/sanand0/llmpricing/commit/ce19161d88b6bc2a9b1437f4fcc0e08aa4b97ccb). Takeaway: date stamps build trust.
- **(Implicit) model frontier remains the dashboard’s key artifact.** Use the CSV to regenerate charts. See commit above. Takeaway: keep raw CSV source authoritative.

### [sanand0/policyascode](https://github.com/sanand0/policyascode)

_Made validation discoverable and added sample documents to speed testing. No, you don't have to handcraft failing docs anymore._  

- **Generate sample documents feature.** UI button generates a likely-pass and a likely-fail sample. See [a7189a9](https://github.com/sanand0/policyascode/commit/a7189a93dfd7c55815be16da3c5c1638c0d91653) (script.js, components.js, config.json) — 07 Nov 2025. Takeaway: sample docs speed QA and reduce guesswork.
- **Moved storage clear control.** Made Clear All easier to find next to Ingest/Consolidate. See [a7189a9](https://github.com/sanand0/policyascode/commit/a7189a93dfd7c55815be16da3c5c1638c0d91653) (components.js). Takeaway: surface destructive actions carefully.
- **Improved validation table UX.** Added clearer row coloring and render fixes. See [a7189a9](https://github.com/sanand0/policyascode/commit/a7189a93dfd7c55815be16da3c5c1638c0d91653) (components.js). Takeaway: color helps triage.

### [sanand0/hypoforge](https://github.com/sanand0/hypoforge)

_Improved statistical feedback and allowed re-tests to iterate faster. Yes, p-values are back in fashion._  

- **Show p-value in UI.** Display p-values alongside hypothesis outcomes. See [f4ba2af](https://github.com/sanand0/hypoforge/commit/f4ba2afba882c41c87561cb19a4cc843d85d16c0) (script.js) — 07 Nov 2025. Takeaway: add numbers, not just green/red.
- **Allow re-testing.** Users can re-run tests without page reload. See [f4ba2af](https://github.com/sanand0/hypoforge/commit/f4ba2afba882c41c87561cb19a4cc843d85d16c0) (script.js). Takeaway: fast iteration is essential for data exploration.
- **Better LLM config integration.** Wire up provider UI hooks for experiments. See [f4ba2af](https://github.com/sanand0/hypoforge/commit/f4ba2afba882c41c87561cb19a4cc843d85d16c0). Takeaway: keep LLM toggles discoverable.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_New data story on classroom Copilot logs helps design better labs. Yes, small assignments reveal big patterns._  

- **Add TDS GitHub Copilot logs story.** New narrative and TL;DRs about OS, models, and verification. See [781cbb9](https://github.com/sanand0/datastories/commit/781cbb961c5b954128e62f995a73256a439b6785) (tds-github-copilot/README.md) — 07 Nov 2025. Takeaway: logs are real feedback; analyze them.
- **Updated site index.** Linked the new story from root README. See [781cbb9](https://github.com/sanand0/datastories/commit/781cbb961c5b954128e62f995a73256a439b6785). Takeaway: surface insights where readers land.

### [sanand0/aipipe](https://github.com/sanand0/aipipe)

_Tests got cleaner. The service stays testable without flakiness._  

- **Refactor tests.** Reworked cloud-worker tests into vitest style and helpers. See [8eee484](https://github.com/sanand0/aipipe/commit/8eee48460e6149626d5deb7373f93098e39f0210) (tests/**) — 05 Nov 2025. Takeaway: solid test harnesses reduce deployment surprises.
- **Removed brittle monolithic test file.** Split responsibilities into smaller tests. See [8eee484](https://github.com/sanand0/aipipe/commit/8eee48460e6149626d5deb7373f93098e39f0210). Takeaway: smaller tests isolate failures.

### [sanand0/discourse-scrape](https://github.com/sanand0/discourse-scrape)

_First working version released for syncing Discourse topics to local JSON and Markdown. Yes, now you can archive a whole course forum._  

- **Initial scraper CLI.** scrape.py fetches topics and writes per-thread JSON. See [b2344b8](https://github.com/sanand0/discourse-scrape/commit/b2344b8dab6055fc8c26fd80a4e94cdcf5aeb090) (scrape.py) — 04 Nov 2025. Takeaway: local archives prevent disappearing discussions.
- **Markdown converter.** md.py renders JSON exports to LLM-friendly Markdown. See [b2344b8](https://github.com/sanand0/discourse-scrape/commit/b2344b8dab6055fc8c26fd80a4e94cdcf5aeb090) (md.py). Takeaway: Markdown mirrors enable quick summarization.
- **Docs and .gitignore.** Added README and ignore rules for exports. See [b2344b8](https://github.com/sanand0/discourse-scrape/commit/b2344b8dab6055fc8c26fd80a4e94cdcf5aeb090). Takeaway: document first-run config to reduce support load.

### [sanand0/prompts](https://github.com/sanand0/prompts)

_Words got clearer and slide conventions tightened. Yes, your prompts now scold semicolons._  

- **Slide and style edits.** afterslides.md increased heading prominence and clarified guidance. See [ec5b352](https://github.com/sanand0/prompts/commit/ec5b3523480465f4ff6a3935fdbc360799cd7692) (afterslides.md) — 03 Nov 2025. Takeaway: clear prompt rules produce consistent outputs.
- **ChatGPT custom instructions refined.** Added mental models and actionable guidance. See [ec5b352](https://github.com/sanand0/prompts/commit/ec5b3523480465f4ff6a3935fdbc360799cd7692) (chatgpt-custom-instructions.md). Takeaway: tell LLMs how you want reasoning framed.
- **Slightly stricter prose rules.** Discourage telegraphic fragments and ambiguous punctuation. See [ec5b352](https://github.com/sanand0/prompts/commit/ec5b3523480465f4ff6a3935fdbc360799cd7692). Takeaway: style constraints improve downstream usability.

### [sanand0/apiagent](https://github.com/sanand0/apiagent)

_Gave the Google demo write access and clarified scopes. Yes, your calendar agent can now create events (responsibly)._  

- **Grant calendar write access.** Demo config now enables Gmail modify and Calendar write scopes. See [e56b01c](https://github.com/sanand0/apiagent/commit/e56b01c00d34a6d572cddb6739bbf9b7ffa58242) (config.js) — 03 Nov 2025. Takeaway: demos should match real permissions.
- **Update prompts to note write level.** Demo text now reflects read+write access. See [e56b01c](https://github.com/sanand0/apiagent/commit/e56b01c00d34a6d572cddb6739bbf9b7ffa58242). Takeaway: be explicit about capabilities.

### [sanand0/til](https://github.com/sanand0/til)

_Notes and tips got a freshness pass, with practical LLM and tooling pointers. Yes, you can now find Gemini CLI tips on that page._  

- **LLM agent and CLI notes expanded.** Added Gemini, caching, HAR-to-LLM notes. See [1dd2ab6](https://github.com/sanand0/til/commit/1dd2ab659add88bb383524284b7e3befca0efdbc) (llms.md) — 03 Nov 2025. Takeaway: operational notes reduce time-to-first-success.
- **Trending repos refreshed.** Updated TSV and scripts to reflect current trends. See [1dd2ab6](https://github.com/sanand0/til/commit/1dd2ab659add88bb383524284b7e3befca0efdbc). Takeaway: keep your weekly signals current.

### [sanand0/asyncsse](https://github.com/sanand0/asyncsse)

_Add a warning to prefer a maintained SSE parser. Yes, being tiny isn't always best._  

- **Recommend parse-sse.** README now warns users to prefer parse-sse for standards compliance. See [b9020b2](https://github.com/sanand0/asyncsse/commit/b9020b25082d808993dcc18ad422b49a117ad51d) — 03 Nov 2025. Takeaway: recommend maintained libraries for critical pieces.

### [sanand0/openai-tts-cost](https://github.com/sanand0/openai-tts-cost)

_Added a working cost analysis for OpenAI TTS models and an experiment report. Yes, TTS pricing is delightfully confusing._  

- **Initial TTS cost report.** Added experiments, tables, and comparisons. See [68f25dc](https://github.com/sanand0/openai-tts-cost/commit/68f25dc8322a0c55bc89d2695927607817d79476) (README.md) — 02 Nov 2025. Takeaway: measure with a real sample, not just provider docs.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Tweaked podcast generation to use clearer dates and a different TTS model. Yes, podcasts prefer human-sounding audio._  

- **Script date format and TTS model change.** Replaced week formatting and switched to tts-1. See [31744d8](https://github.com/sanand0/generative-ai-group/commit/31744d80170fd400403a36bb9ac3972c01b61a0c) (podcast.py) — 02 Nov 2025. Takeaway: readable dates and stable TTS choices reduce surprises.
- **Generated podcast episode added.** New week episode markdown and raw messages. See [31744d8](https://github.com/sanand0/generative-ai-group/commit/31744d80170fd400403a36bb9ac3972c01b61a0c) (2025-11-02/*). Takeaway: weekly automation pays dividends in audience trust.

## Lessons

- Small UX and docs work scales. A clear date, a helpful badge, or a sample document prevents dozens of support messages.
- Cache LLM and HTTP calls in loops. You will save money and speed up reruns.
- Tests and pre-commit hooks catch regressions early. Invest three hours now.
- Prefer well-maintained libraries for standards work. Tiny is cute, but maintained is useful.
- Surface destructive actions and permissions clearly. Users will click things.

## Suggestions

- Run the updated faq.sh on the playlist and confirm chunking works with ffmpeg overlap. Measure runtime. (Follow [6c10e6a](https://github.com/sanand0/tools-in-data-science-public/commit/6c10e6a15986263c292dbb1f446d38710fcc4088).)
- Publish the Discourse bookmarklet build and a short demo GIF. Add a quick test case from course threads. (See [2f9c473](https://github.com/sanand0/tools/commit/2f9c473659377190af95e59aa32f78d9ea5f7d06).)
- Add CI step for policyascode sample-doc generation. Validate JSON schema from config/samples. (See [a7189a9](https://github.com/sanand0/policyascode/commit/a7189a93dfd7c55815be16da3c5c1638c0d91653).)
- Run dev.test.sh in CI or as a local preflight for contributors. It will surface missing tools early. (See [f9beb41](https://github.com/sanand0/scripts/commit/f9beb41a983fca56f9f359e05a8cbec3bf1abe0c).)
- Add a short “how to reproduce” block to the TTS cost report with exact commands and a tiny audio sample. That will make comparisons reproducible. (See [68f25dc](https://github.com/sanand0/openai-tts-cost/commit/68f25dc8322a0c55bc89d2695927607817d79476).)

If you want, I can draft the short demo README for the Discourse scraper or a runnable checklist for running faq.sh end-to-end.