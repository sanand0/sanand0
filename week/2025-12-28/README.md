## A week of data stories, model pipelines, and handy tooling — ship the story, not just the chart.

Two clear lessons this week: bundle your data, code, and narrative. And automate the boring parts so the next story ships faster.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_You can turn messy emotion labels into a reproducible story and a working model pipeline at the same time._

- **New interactive story added.** Added "The Ambiguous Song" site and visuals, including `index.html` and `script.js` for Chart.js visuals ([d23b50d](https://github.com/sanand0/datastories/commit/d23b50df6755334ca7bcd8f27899b863307baec9)). (25 Dec 2025) It gives readers an explorable front end for the Emotify results. Takeaway: ship the narrative and the app together so people can explore results themselves. (Yes, you really needed another music demo.)

- **Full reproducible modeling pipeline.** Added feature extraction, model training, and importance analysis scripts (`extract_features.py`, `train_models.py`, `feature_importance.py`, `build_story_data.py`) ([3f5357d](https://github.com/sanand0/datastories/commit/3f5357d6489be1294f68d1e0139922570d7a9961)). (25 Dec 2025) These create CSV artifacts and metrics so the story is traceable from audio to numbers. Takeaway: provide runnable scripts so others can verify and extend the analysis.

- **Data, metrics, and audio bundled.** Added `data/story.json`, `artifacts/metrics.csv`, `data/audio/*.opus`, and `emotify/SUMMARY.md` ([d23b50d](https://github.com/sanand0/datastories/commit/d23b50df6755334ca7bcd8f27899b863307baec9), [3f5357d](https://github.com/sanand0/datastories/commit/3f5357d6489be1294f68d1e0139922570d7a9961)). (25 Dec 2025) Readers and reviewers can reproduce charts and hear examples. Takeaway: include compact artifacts to make reviews fast and honest.

- **Small polish and doc fixes.** Linted and tightened markdown and narrative language in `SUMMARY.md` and `prompt.md` ([bd22b45](https://github.com/sanand0/datastories/commit/bd22b455630e24ab370dd357c5d9851f1cb5c98d)). (25 Dec 2025) This improves clarity and external links. Takeaway: small editorial fixes pay off for reader trust.

### [sanand0/llm-music](https://github.com/sanand0/llm-music)

_An evaluation playground showing where an LLM hears music like humans — and where it stumbles._

- **Interactive Gemini vs Emotify visualization.** Added a full visualization site (`index.html`, `script.js`, D3 visuals) and frontend copy ([526b45f](https://github.com/sanand0/datastories/commit/526b45f2fe6be82f569b2eeae32443478dc33b16)). (24 Dec 2025) It juxtaposes Gemini predictions against human ratings. Takeaway: side-by-side comparisons reveal systematic gaps faster than tables.

- **Batch analysis tooling for Gemini.** Added `music.py` to call Gemini via OpenRouter and save `gemini_output.json` ([526b45f](https://github.com/sanand0/datastories/commit/526b45f2fe6be82f569b2eeae32443478dc33b16)). (24 Dec 2025) The script resumes runs and creates comparison CSVs. Takeaway: make model calls resumable to avoid wasted API spend.

- **Prompts, docs, and ground truth included.** Added detailed `prompts.md`, `README.md`, and `truth.json` alongside example outputs (`means_comparison.csv`) ([526b45f](https://github.com/sanand0/datastories/commit/526b45f2fe6be82f569b2eeae32443478dc33b16)). (24 Dec 2025) This helps others audit prompt design and results. Takeaway: publish prompts and truth data with results for honest replication. (Also: yes, LLMs argue about music.)

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

_A small catalog update that points users to fresh, live demos they can try._

- **New demos added to the catalog.** Updated README and `config.json` to include recent demos, including the new music stories ([01e2b37](https://github.com/sanand0/llmdemos/commit/01e2b37e95ec9be2d736143f653edaccc0e5e39a)). (25 Dec 2025) Users can discover interactive experiments quickly. Takeaway: curate live demos to lower the friction for exploration.

### [sanand0/prompts](https://github.com/sanand0/prompts)

_Better prompt hygiene and practical guidance make prompts safer and more reuseable._

- **New presentation styles and checklist.** Expanded `styles.md` with a large Presentations section and templates ([f4a500e](https://github.com/sanand0/prompts/commit/f4a500ecaaa151bf5b7830a82732abc5b266ad3e)). (21 Dec 2025) It gives diverse slide and storytelling patterns to pick from. Takeaway: reuseable patterns speed slide authoring.

- **Prompt fragments for ambiguity and checks.** Added "Handling ambiguity" and "Double-checking" fragments in `fragments.md` ([f4a500e](https://github.com/sanand0/prompts/commit/f4a500ecaaa151bf5b7830a82732abc5b266ad3e)). (21 Dec 2025) They encourage clarifying questions and self-scan for weak claims. Takeaway: make uncertainty explicit to avoid brittle outputs.

- **Ideator scoring tweak.** Increased candidate count and added feasibility scoring in `ideator.md` ([f4a500e](https://github.com/sanand0/prompts/commit/f4a500ecaaa151bf5b7830a82732abc5b266ad3e)). (21 Dec 2025) This nudges more exploration and pragmatic selection. Takeaway: explicit feasibility helps pick realistic winners.

### [sanand0/scripts](https://github.com/sanand0/scripts)

	Big developer-tooling push. New skills, packaging, and dev tooling landed.

- **New agent skills and templates.** Added `plan`, `skill-creator`, and `skill-installer` systems plus helper scripts (`init_skill.py`, `install-skill-from-github.py`, `create_plan.py`) ([56047c8](https://github.com/sanand0/scripts/commit/56047c84b48d0280561ec6c3b6b6e3e3ca7b3ba2)). (21 Dec 2025) These give a repeatable path for building and publishing skills locally. Takeaway: standardize templates to reduce onboarding friction.

- **Better dev tooling and logs.** Replaced old Claude log tools with a new `claudelog` renderer and added Playwright dev checks (`agents/devtools/check-page.*`) ([56047c8](https://github.com/sanand0/scripts/commit/56047c84b48d0280561ec6c3b6b6e3e3ca7b3ba2)). (21 Dec 2025) That makes debugging reproducible and nicer. Takeaway: invest in readable logs and lightweight checks.

- **Dev container and PDF tooling updates.** Dev Dockerfile, Playwright, and a PDF skill were added; many helper utilities were included ([56047c8](https://github.com/sanand0/scripts/commit/56047c84b48d0280561ec6c3b6b6e3e3ca7b3ba2)). (21 Dec 2025) This speeds local testing and automates PDF handling. Takeaway: match the dev environment to the tasks to reduce friction.

### [sanand0/til](https://github.com/sanand0/til)

_A set of quick learnings and references to make future work faster and less annoying._

- **December notes and practical snippets.** Added Dec 2025 entries to `til.md` and `llms.md` covering TTS favorites, audio tricks, and reasoning feedback notes ([e77093b](https://github.com/sanand0/til/commit/e77093b9f9bb7dabd134ed7fa3642634e7cab462)). (21 Dec 2025) The notes include commands, links, and process ideas you can reuse. Takeaway: short reproducible notes save hours later.

## Lessons

- Bundle story + data + pipeline. It makes claims verifiable and reduces follow-up back-and-forth.
- Ship runnable scripts. Reproducible artifacts beat long prose descriptions.
- Document prompts, prompts-in-practice, and expected outputs. Transparency prevents guessing games.
- Small dev tools (logs, resume behavior) save money and frustration on long runs.
- Curate demos aggressively. Live examples lower the barrier to understanding.

## Suggestions

- Deploy both Emotify and llm-music to GitHub Pages with a small CDN for audio. This makes demos frictionless.
- Add CI checks that run the pipeline on a tiny sample. Catch regressions early and keep metrics current.
- Add a README badge linking to a short reproducibility checklist and a minimal "how to run" snippet.
- Optimize audio sizes and lazy-load clips to cut page load time on mobile.
- Add lightweight unit tests for `extract_features.py` and `train_models.py` (use tiny fixtures).
- Publish the prompt versions used for each Gemini call as immutable artifacts alongside outputs.
- For scripts/agents: add an integration test that installs a curated skill and runs its quick-validate script.

If you want, I can draft the short GitHub Pages deploy workflow, a tiny CI YAML for the pipeline sample, or a one-page reproducibility checklist to include in each story.