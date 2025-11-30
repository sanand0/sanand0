## A week of stories, tools, and tidy wiring — content, conversion, and cleaner infra.

Small projects got clearer structure. Large data stories and tutorials landed. The week’s lesson: make content discoverable and code reusable.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Updates made the TDS story clearer, added historical versions, and tightened many data scripts for consistency._

- **TDS story renamed and expanded (29 Nov 2025).** Updated the project title and content to "The Cliff" and linked the gate analysis. See commits [4e78bfb](https://github.com/sanand0/datastories/commit/4e78bfbb86bcc25fbd405bd772c4ec7e16cc65dc) and [715bb00](https://github.com/sanand0/datastories/commit/715bb0014d82676e7e02bf5da66b0e3855a3bd13). Takeaway: keep an old version handy when narratives change, so readers can compare conclusions easily. (Yes, another rename.)

- **Added per-week marks distribution and screenshot (29 Nov 2025).** Inserted a full HTML story and screenshot for the TDS Project 2 data dive. See [41f9e3b](https://github.com/sanand0/datastories/commit/41f9e3b949b3c35fb250e4d81067b5362d3c1b89). Takeaway: visuals plus raw distributions help readers trust numeric claims.

- **New Market Mix Modeling story (27 Nov 2025).** Published a long-form interactive piece on saturation and spend efficiency. See [950abf8](https://github.com/sanand0/datastories/commit/950abf8060a8e2468b963a886521d1d8a962cc80). Takeaway: policy guidance in data stories is more persuasive with visual experiments.

- **Code & lint tidy across scripts (29 Nov 2025).** Large style and whitespace cleanups plus safer file handling in many scrapers. See [5bd3acb](https://github.com/sanand0/datastories/commit/5bd3acb4d91662f94ddab9ebef82509d6279e727). Takeaway: small lint and formatting fixes reduce cognitive load when revisiting analysis code.

### [sanand0/tools](https://github.com/sanand0/tools)

_Shared utilities got centralized, Unicoder gained reverse conversion, and repo tools became more modular._

- **Centralized download helper (27 Nov 2025).** Moved file->DataURL logic to [common/download.js]. See [c6d1316](https://github.com/sanand0/tools/commit/c6d131615e381af0071bd64688e274b3e60aca6e). Takeaway: pull repeated utilities into common modules to avoid copy/paste.

- **Bidirectional Unicoder: Unicode ↔ Markdown (26 Nov 2025).** Added reverse conversion, tests, and UI for Unicode→Markdown. See [41de615](https://github.com/sanand0/tools/commit/41de615e096a36b0250ca46fa09bf46ff7d102bb). Takeaway: supporting the inverse flow saves users time when cleaning pasted styled text. (Yes, your terminal can be fancy and useful.)

- **Extract GitHub activity client and editable context (25 Nov 2025).** New activity client for safer fetching, truncation, and progress. See [b7bde07](https://github.com/sanand0/tools/commit/b7bde073bd02def2bfabcf3d80430430f7039270). Takeaway: encapsulate API fetching so UIs can focus on presentation and retries.

### [sanand0/prompts](https://github.com/sanand0/prompts)

_Reorganized and expanded the "Developer Styles" prompt library for many writing and coding contexts._

- **Major rework and expansion (24 Nov 2025).** Reorganized sources, added many voice profiles and new categories. See [5c0c0be](https://github.com/sanand0/prompts/commit/5c0c0bed10b813a442c86291c2184db38fa8c893) and file [styles.md](https://github.com/sanand0/prompts/blob/main/styles.md). Takeaway: a clear prompt taxonomy speeds reuse and keeps style guidance consistent. (No, you don’t need another style guide—just this one.)

- **Added non-fiction and practical categories.** New entries cover educational content, feedback, research synthesis, and client house styles. See the updated [styles.md](https://github.com/sanand0/prompts/commit/5c0c0bed10b813a442c86291c2184db38fa8c893). Takeaway: split modes (content vs code) for sharper prompts.

- **Trimmed long examples and improved discoverability.** Reduced noise and added per-section quick-links. Takeaway: fewer, focused examples beat long unstructured lists.

### [sanand0/scripts](https://github.com/sanand0/scripts)

:System and workflow ergonomics landed: a terminal LLM chat helper, PDF tooling docs, GNOME tweaks, and container updates.

- **New terminal chat helper (24 Nov 2025).** Added a Playwright-based `chat` script to run LLM queries via a running browser. See [f110323](https://github.com/sanand0/scripts/commit/f110323276b4e2f530aed82adf7d59eee6054c37) and file [chat](https://github.com/sanand0/scripts/blob/main/chat). Takeaway: a quick terminal-to-web bridge speeds throwaway experiments.

- **PDF tooling docs and installs (24 Nov 2025).** Documented pdfcpu usage and added it to installation notes. See [f110323](https://github.com/sanand0/scripts/commit/f110323276b4e2f530aed82adf7d59eee6054c37) and [agents/tooldocs/pdfcpu.md](https://github.com/sanand0/scripts/blob/main/agents/tooldocs/pdfcpu.md). Takeaway: keep handy CLI recipes for repeatable file work.

- **GNOME, dev container, and setup polish (24 Nov 2025).** Many gsettings tweaks, dev.dockerfile refinements, and setup.fish updates. See [f110323](https://github.com/sanand0/scripts/commit/f110323276b4e2f530aed82adf7d59eee6054c37). Takeaway: documenting system tweaks prevents future breakage. (Yes, opinionated defaults are included—review before applying.)

- **Touch/gesture and service improvements.** Added touchegg config and safer service masks. Takeaway: small system defaults boost daily ergonomics.

### [sanand0/til](https://github.com/sanand0/til)

_Notes and tip collections got refreshed with November updates on tools and LLM practices._

- **Nov notes added (24 Nov 2025).** Added CLI tools, practical tips, and fixes to llms.md and til.md. See [5138d08](https://github.com/sanand0/til/commit/5138d08b26432e1ce5a565318790061170d09223). Takeaway: capture small operational tips immediately; they compound.

- **LLM workflow clarifications and tool recommendations.** Added agent workflow patterns and model guidance. See [llms.md commit](https://github.com/sanand0/til/commit/5138d08b26432e1ce5a565318790061170d09223). Takeaway: codify recurring patterns to shorten onboarding.

- **Refreshed trending repos list (24 Nov 2025).** Updated ordering and deduped entries in trending-repos.tsv. Takeaway: keep curated lists tidy so they stay useful for discovery.

### [sanand0/tutorials](https://github.com/sanand0/tutorials)

_New tutorials: terminal map rendering, and principles for writing shorter code._

- **Mapscii rendering tutorial (26 Nov 2025).** Added a deep explainer on Braille rendering, triangulation, and rasterization. See [2511104c](https://github.com/sanand0/tutorials/commit/2511104c8a8444feb89b0a9fdf8ab952254e6ed1) and [mapscii-rendering/README.md](https://github.com/sanand0/tutorials/blob/main/mapscii-rendering/README.md). Takeaway: terminal graphics can be high-fidelity with clever glyph tricks.

- **Short code tutorial (26 Nov 2025).** Published refactoring principles used to shrink and clarify Unicoder code. See [cd4dfdf](https://github.com/sanand0/tutorials/commit/cd4dfdf900eb8993d19d625e43bebcb626b058e5) and [short-code/README.md](https://github.com/sanand0/tutorials/blob/main/short-code/README.md). Takeaway: prefer data-driven design and modern syntax over long conditionals.

- **Added tutorial links to README.** Both tutorials now appear in the top-level index. Takeaway: surface new learning artifacts so readers find them.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_A course repo received a small but important scheduling/endpoint note for Project 2._

- **Project 2 API URL and schedule added (29 Nov 2025).** Documented project endpoint and activation time in project-llm-analysis-quiz.md. See [28dfdf6](https://github.com/sanand0/tools-in-data-science-public/commit/28dfdf6361a91065ed001da928cd169af9102eb5). Takeaway: announce live endpoints and windows early to avoid confusion.

- **Clarified warning and timing.** The README now signals a time-limited endpoint. Takeaway: make ephemeral resources explicit.

- **Small doc tweak, big practical impact.** Students now have exact URL and time. Takeaway: reduce friction before evaluation windows.

### [sanand0/hypoforge](https://github.com/sanand0/hypoforge)

_Prompts and schemas centralized to make experiment presets reusable in the UI._

- **Central config for prompts and schemas (26 Nov 2025).** Added config.js and wired it into script/UI. See [d811ecd](https://github.com/sanand0/hypoforge/commit/d811ecd6a3e21126056e58d0c3efc5e8fac10b25). Takeaway: central config reduces duplication and eases switching presets.

- **UI now seeds analysis prompt from config.** The textarea populates with sensible defaults. Takeaway: fewer accidental blank prompts equals faster experiments.

- **Prepared for modeling presets later.** Modeling placeholders exist but are off by default. Takeaway: scaffold future features now, implement later.

### [sanand0/datachat](https://github.com/sanand0/datachat)

_Short compatibility change to the LLM choice for better prompt behavior._

- **Switched model to gpt-4.1-mini (24 Nov 2025).** Reverted from gpt-5-mini and removed temperature. See [b86e97a](https://github.com/sanand0/datachat/commit/b86e97a7c422764127ecd2894784e97319836e3d). Takeaway: pick stable models for predictable behavior and compatibility.

- **Dropped temperature parameter for compatibility.** Ensures consistent outputs across providers. Takeaway: remove unsupported knobs when moving models.

- **Keeps JSON-schema response support intact.** The JSON schema plumbing remains. Takeaway: maintain structured outputs while changing models.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Weekly podcast updated and message archive refreshed for recent group activity._

- **Weekly podcast episode updated (23 Nov 2025).** Added episode markdown with shows notes and tips. See [5e2c691](https://github.com/sanand0/generative-ai-group/commit/5e2c691d2a4ceb270c3589573eb0943fde2e255f) and file [2025-11-23/podcast-2025-11-23.md](https://github.com/sanand0/generative-ai-group/blob/main/2025-11-23/podcast-2025-11-23.md). Takeaway: distill group threads into short podcasts to surface signals fast.

- **Large message archive changes (23 Nov 2025).** Updated gen-ai-messages.json with many additions. See the commit in the same [5e2c691](https://github.com/sanand0/generative-ai-group/commit/5e2c691d2a4ceb270c3589573eb0943fde2e255f). Takeaway: keep raw transcripts to enable reproducible episodes and retrospectives.

- **Practical episode takeaways now explicit.** The episode lists tooling and deployment advice. Takeaway: concrete suggestions help listeners take action quickly.

## Lessons

- Small UI seeds matter: prefill prompts and editable context speeds experiments.
- Centralize repeated logic: shared helpers reduce bugs and friction.
- Version content, not just files: keep old story versions for auditability.
- Test bidirectional flows early: users paste styled text often.
- Document ephemeral endpoints and schedules to avoid live-day chaos.

## Suggestions

- Add a small script that publishes diffs of story changes automatically. That makes narrative edits auditable.
- Add an integration test for Unicoder round-trip conversions in CI. Catch regressions early.
- Expose a UI toggle in githubsummary to switch the context JSON presets. It helps reviewers tweak prompts safely.
- For tutorials, add a short runnable demo (codesandbox or minimal Docker) so readers can reproduce outputs quickly.
- Schedule a one-page "what changed" doc per course project before each live window to reduce student support load.