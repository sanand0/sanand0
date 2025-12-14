## A week of stories, tooling, and tidy fixes — shipping better docs, demos, and data narratives.

Small wins stacked up: new talks and data stories, readable prompts, media tooling, and a few UX fixes. The lesson: shipping clear outputs (sites, scripts, tests) makes research and teaching reusable.

### [sanand0/talks](https://github.com/sanand0/talks)

_Workshop pages and full talk artifacts make presentations searchable and reusable. Yes, you really needed another sketchnote._

- **New workshop site:** Added a polished workshop landing page for "Mining Digital Exhaust" and interactive reveal effects. See [5724a2a](https://github.com/sanand0/talks/commit/5724a2a6b95458fee04f557efc66b9bfbc3ef96d) (08 Dec 2025). Takeaway: a neat landing page makes reuse and teaching far easier.
- **Resources panel:** Linked prompt templates, CDP cheatsheets, and post-mortem templates into the footer for quick access. See [d200bce](https://github.com/sanand0/talks/commit/d200bce0aa4d0fb38e5ebc2cdabfb65fd4c5a38e) (09 Dec 2025) and the updated file [index.html](https://github.com/sanand0/talks/blob/main/2025-12-06-mining-digital-exhaust/index.html). Takeaway: bundle helpful links so learners don’t hunt for them later.
- **New talk added:** Published the HR talk "AI First Thinking for HR Professionals" and updated the talks index. See [79baf5f](https://github.com/sanand0/talks/commit/79baf5f03a895873502ef636fb2bea5f9f02ff18) (10 Dec 2025) and the talk README. Takeaway: commit full talk artifacts (slides, transcript, sketchnote) for evergreen value.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Data stories convert messy logs into clear narratives and charts that readers can act on. Also: yes, your weight chart is dramatic._

- **New personal data story:** Added "The Ruler-Straight Disappearing Act" with full HTML and screenshot. See [ab0a485](https://github.com/sanand0/datastories/commit/ab0a4857257d9aae7bae57c77d4ba66b9348d6b9) (10 Dec 2025) and [weight-2025-12/index.html](https://github.com/sanand0/datastories/blob/main/weight-2025-12/index.html). Takeaway: small, honest datasets tell compelling stories if you visualize changepoints.
- **Promptfight detail expansion:** Added win-rate viz and timing charts to the promptfight page. See [7a9cf11](https://github.com/sanand0/datastories/commit/7a9cf11ee4aa82ee5d8eb40dd86e2c40d7127998) (10 Dec 2025). Takeaway: sprinkle summary charts into long analyses to speed comprehension.
- **New narrative on prompt battles:** Published "The Command Paradox" story with full UI and screenshots. See [bd0c807](https://github.com/sanand0/datastories/commit/bd0c807ec59c93fbdf0b7d2494a2d3ee66407971) (10 Dec 2025) and [promptfight/index.html](https://github.com/sanand0/datastories/blob/main/promptfight/index.html). Takeaway: framing technical results as stories boosts reader attention.

### [sanand0/prompts](https://github.com/sanand0/prompts)

_Clearer prompt fragments and style catalog make reuse faster and safer. Also: mark the unclear bits, please._

- **New prompt fragments:** Added re-usable fragments like "Brainstorming" and "Malcolm Gladwell Style". See [61d6d95](https://github.com/sanand0/prompts/commit/61d6d951d063ecc20b16c977004262c354a5e50e) (07 Dec 2025) and [fragments.md](https://github.com/sanand0/prompts/blob/main/fragments.md). Takeaway: small prompt snippets speed iteration and reduce prompt rot.
- **New writing styles:** Expanded author-style catalog with Robinson, Le Guin, Mitchell, and others. See [61d6d95](https://github.com/sanand0/prompts/commit/61d6d951d063ecc20b16c977004262c354a5e50e) (07 Dec 2025) and [styles.md](https://github.com/sanand0/prompts/blob/main/styles.md). Takeaway: codify styles so output tone stays consistent across projects.
- **Transcription and eval tweaks:** Added a "Transcript" header and a rule to mark unclear audio as "[UNCLEAR]". See [61d6d95](https://github.com/sanand0/prompts/commit/61d6d951d063ecc20b16c977004262c354a5e50e) (07 Dec 2025) and [transcribe-talk.md](https://github.com/sanand0/prompts/blob/main/transcribe-talk.md). Takeaway: explicit markers reduce downstream editing time.

### [sanand0/scripts](https://github.com/sanand0/scripts)

.Tools to make media, demos, and daily ops reproducible. Also: yes, a tiny mdgrep saved a surprising amount of time.

- **Add audiosync CLI:** New tool aligns phone audio with screen recordings using cross-correlation and ffmpeg. See [ae59887](https://github.com/sanand0/scripts/commit/ae5988718b93398e900ff63aa53c4920b15f3b3b) (07 Dec 2025) and [audiosync.py](https://github.com/sanand0/scripts/blob/main/audiosync.py). Takeaway: clean audio sync removes a major editing bottleneck.
- **Shell tweaks and mdgrep:** Changed videorecord default to 1920x1200 and added mdgrep for markdown block search. See [ae59887](https://github.com/sanand0/scripts/commit/ae5988718b93398e900ff63aa53c4920b15f3b3b) (07 Dec 2025) and [setup.fish](https://github.com/sanand0/scripts/blob/main/setup.fish). Takeaway: small CLI helpers compound into big time savings.
- **Dev tooling bump & docs:** Bumped @openai/codex in dev.dockerfile and improved agent docs. See [ae59887](https://github.com/sanand0/scripts/commit/ae5988718b93398e900ff63aa53c4920b15f3b3b) (07 Dec 2025). Takeaway: keep toolchains current and document expected paths.

### [sanand0/til](https://github.com/sanand0/til)

_Notes and deep dives help keep learning public and repeatable. Bonus: a careful langextract teardown just landed._

- **LangExtract deep-dive:** New long analysis of google/langextract, chunking, and production gaps. See [1965e69](https://github.com/sanand0/til/commit/1965e69609257903a7322be66d2bd2688ffe4427) (07 Dec 2025) and [docs/google-langextract.md](https://github.com/sanand0/til/blob/main/docs/google-langextract.md). Takeaway: simple ideas hide non-trivial production work.
- **Updated LLM notes and ideas:** Added Dec 2025 LLM notes and many seed ideas in ideator.md and llms.md. See [1965e69](https://github.com/sanand0/til/commit/1965e69609257903a7322be66d2bd2688ffe4427) (07 Dec 2025). Takeaway: capturing fleeting insights prevents regret later.
- **New TIL entries:** Added short, actionable TIL items for tools and techniques. See [1965e69](https://github.com/sanand0/til/commit/1965e69609257903a7322be66d2bd2688ffe4427) (07 Dec 2025) and [til.md](https://github.com/sanand0/til/blob/main/til.md). Takeaway: weekly notes are the best low-friction docs.

### [sanand0/tools](https://github.com/sanand0/tools)

_Small web tools make daily work easier. Also: yes, the HN bookmarklet is a tiny delight._

- **HN bookmarklet tool:** Added "Hacker News Thread Markdown" bookmarklet, tests, and UI. See [5d85998](https://github.com/sanand0/tools/commit/5d8599840578a31918af52cdd7be8611a15a9fed) (08 Dec 2025) and [hnmd/index.html](https://github.com/sanand0/tools/blob/main/hnmd/index.html). Takeaway: one-click exports save hours of manual copy-paste.
- **Numbered thread IDs:** Improved thread numbering and tests to produce IDs like 1.1.2 for nesting. See [3b8e874](https://github.com/sanand0/tools/commit/3b8e8748231e8df3d14c10f3e0114fde406c70f7) (11 Dec 2025) and [hnmd/bookmarklet.js](https://github.com/sanand0/tools/blob/main/hnmd/bookmarklet.js). Takeaway: small UX details make output easier to reference.
- **Minor navbar fix:** Updated the GitHub navbar link to the correct org path. See [5f74d1b](https://github.com/sanand0/tools/commit/5f74d1bb10d084f18459d68e876d552469a03622) (13 Dec 2025). Takeaway: polish matters for first impressions.

### [sanand0/llmartstyle](https://github.com/sanand0/llmartstyle)

_Category selection and batch generation turn a demo into a usable asset pipeline. Also: lots of gorgeous thumbnails._

- **Category-aware UI:** Added multi-category config and a category selector to the site. See [80354bd](https://github.com/sanand0/llmartstyle/commit/80354bdbe70785541036eef639f10b541acc8d80) (11 Dec 2025) and [index.html](https://github.com/sanand0/llmartstyle/blob/main/index.html). Takeaway: categories cut cognitive load for browsing many styles.
- **Batch generator & dotenv:** Generator now supports dotenv, multiple categories, and skips existing images. See [80354bd](https://github.com/sanand0/llmartstyle/commit/80354bdbe70785541036eef639f10b541acc8d80) and [generate_images.py](https://github.com/sanand0/llmartstyle/blob/main/generate_images.py). Takeaway: make automated pipelines idempotent to save API costs.
- **Many generated images:** Added dozens of .webp outputs and config expansion. See [80354bd](https://github.com/sanand0/llmartstyle/commit/80354bdbe70785541036eef639f10b541acc8d80) and [config.json](https://github.com/sanand0/llmartstyle/blob/main/config.json). Takeaway: automating diversity helps pick promising directions faster.

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

_Showcasing demos makes discovery easier. Also: new demos just hit the index._

- **Two demos added:** Registered "Parallel Editing Experiment" and "Agent Builder" in demos config. See [2155acf](https://github.com/sanand0/llmdemos/commit/2155acfdd0ea82575ad17ff41e443fb88386bf88) (11 Dec 2025) and [config.json](https://github.com/sanand0/llmdemos/blob/main/config.json). Takeaway: surface new demos so others can try and link easily.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_Assessments and scoring code help scale fair grading for prompt-security exercises. Also: grading logic is documented._

- **Eval & scoring toolkit:** Added evaluation.py with multiple scoring schemes for the prompt duel quiz. See [5dc0095](https://github.com/sanand0/tools-in-data-science-public/commit/5dc00954854ff600b0f003df2486a8775a91e5d2) (10 Dec 2025) and [project-llm-analysis-quiz/evaluation.py](https://github.com/sanand0/tools-in-data-science-public/blob/main/project-llm-analysis-quiz/evaluation.py). Takeaway: ship multiple scoring views to handle edge cases fairly.
- **Prompt duel runner:** Added promptfight.py to automate pairwise duels and log leaks. See [5dc0095](https://github.com/sanand0/tools-in-data-science-public/commit/5dc00954854ff600b0f003df2486a8775a91e5d2) (10 Dec 2025) and [promptfight.py](https://github.com/sanand0/tools-in-data-science-public/blob/main/project-llm-analysis-quiz/promptfight.py). Takeaway: reproducible logs make grading defensible.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Turned weekly chat threads into podcast-ready scripts and episode pages. Also: lots of raw chat data now committed (handle with care)._

- **New episode draft:** Added the 07 Dec 2025 episode draft and structure for hosts and tips. See [a798198](https://github.com/sanand0/generative-ai-group/commit/a798198686886bcbcfd5bf6048bcdc5abbda3914) (07 Dec 2025) and [2025-12-07/podcast-2025-12-07.md](https://github.com/sanand0/generative-ai-group/blob/main/2025-12-07/podcast-2025-12-07.md). Takeaway: a short scripted draft accelerates audio production.
- **Large chat ingest:** Committed an updated gen-ai-messages.json export to support thread parsing. See [a798198](https://github.com/sanand0/generative-ai-group/commit/a798198686886bcbcfd5bf6048bcdc5abbda3914) and [gen-ai-messages.json](https://github.com/sanand0/generative-ai-group/blob/main/gen-ai-messages.json). Takeaway: keep raw exports out of public repos when they contain personal data.

### [sindresorhus/trash](https://github.com/sindresorhus/trash)

_A cross-platform trash tool tightened to the XDG spec on Linux. Also: specs deserve exact links._

- **XDG .trashinfo encoding:** Encode the Path in .trashinfo with URI encoding per spec. See [b848409](https://github.com/sindresorhus/trash/commit/b848409ecaa5874e2b1300e47c25eed8bf5fc6fa) (07 Dec 2025) and [lib/linux.js](https://github.com/sindresorhus/trash/blob/main/lib/linux.js). Takeaway: follow platform specs to avoid subtle restore bugs.
- **Tests and docs updated:** Adjusted tests and the Readme XDG link to the official spec. See [b848409](https://github.com/sindresorhus/trash/commit/b848409ecaa5874e2b1300e47c25eed8bf5fc6fa) (07 Dec 2025). Takeaway: test changes lock in cross-platform behavior.

## Lessons

- Ship outputs, not just prototypes. Pages, transcripts, and READMEs multiply impact.
- Small UX fixes matter. Tiny helpers (mdgrep, numbered comment IDs) save hours.
- Make data narratives re-runnable. Idempotent generators cut API cost and drift.
- Document grading and evaluation logic for fairness and auditability.
- Mark unclear or sensitive data explicitly to avoid accidental leaks.

## Suggestions

- Add CI checks for the HN bookmarklet and audiosync to prevent regressions.
- Move audiosync into a small Python package and publish usage examples.
- Automate weekly podcast generation with a scheduled workflow and a dry-run flag.
- Add a privacy checklist before committing chat exports to any public repo.
- Run a quick usability test on the llmartstyle category selector and thumbnail sizes.
- Fix the "Whet" typo in evaluate-technology.md and add a tiny lint rule for docs.
