## A week of polishing skills, docs, and tiny tools that actually get used

This week focused on turning tacit prompt wisdom into reusable SKILLs and small utilities. The work makes course assignments, agent metadata, and everyday authoring tasks repeatable and testable.

### [sanand0/til](https://github.com/sanand0/til)

_Updated course notes and app trackers so teaching moves from ideas to runnable assignments, and your weekly snapshot is preserved._ (Yes, more checklist items. Someone has to love CSVs.)

- **Expanded course assignments.** Updated TDS problems and added server-side skeletons in [tds-jan-2026.md](https://github.com/sanand0/til/blob/3c063cef58ac71c556615a75bc1b03a347ea9c0d/tds-jan-2026.md) via commit [3c063ce](https://github.com/sanand0/til/commit/3c063cef58ac71c556615a75bc1b03a347ea9c0d) (15 Feb 2026); this gives concrete, testable student tasks. Takeaway: Ship small, runnable tasks so students can actually build and validate work.

- **Marked app progress and added live links.** apps.md now records demos and progress, with links to examples in the repo ([apps.md](https://github.com/sanand0/til/blob/3c063cef58ac71c556615a75bc1b03a347ea9c0d/apps.md)) via [3c063ce] (15 Feb 2026). Takeaway: A link beats a TODO every time.

- **Snapshot of trending repos.** Appended a weekly snapshot to [trending-repos.tsv](https://github.com/sanand0/til/blob/3c063cef58ac71c556615a75bc1b03a347ea9c0d/trending-repos.tsv) in [3c063ce] (15 Feb 2026), preserving research context. Takeaway: Record the data you used; context decays fast.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Documentation and tooling converge: SKILLs, metadata generators, and editor utilities make authoring and agent work predictable._ (Yes, your receipts finally get tidy filenames.)

- **Packed SKILL guidance for analysts and storytellers.** Added `agents/data-analysis/SKILL.md` and `agents/data-story/SKILL.md` to capture investigative and narrative rules in [4e514e2](https://github.com/sanand0/scripts/commit/4e514e2128f25b78b3a7b0ad5324887b4d96161c) (21 Feb 2026). This turns prompt heuristics into reusable artifacts. Takeaway: Codify judgment so agents and humans make similar decisions.

- **Automated skill UI metadata.** Added `generate_openai_yaml.py` and hooked it into `init_skill.py` to produce `agents/openai.yaml` automatically in [4434579](https://github.com/sanand0/scripts/commit/4434579fb30e4e6b84ad9ecc6baa264b9f42b6cf) (21 Feb 2026). This standardizes UI-facing fields and validates lengths. Takeaway: Make metadata generation deterministic to avoid surprise UI bugs.

- **Authoring and clipboard tooling.** Added `clean_markdown.py`, `striplinks.py`, and clipboard helpers in [4434579] (21 Feb 2026). They normalize lists, strip links/images, and speed copy→Markdown workflows. Takeaway: Small editor tools save hours when writing weekly notes.

- **Practical utilities and transcripts.** Added `rename_receipts.py` for robust PDF renaming and improved `consolidate_transcripts.py` to write monthly files in [4434579] (21 Feb 2026). These tidy archives and automate monotony. Takeaway: Automate low-value, repetitive tasks so you can focus on insight.

- **Installer/listing and UX tweaks.** Renamed `list-curated-skills.py` → `list-skills.py`, added installer metadata, icons, and a few environment tweaks (setup/linux.md) in [4434579] (21 Feb 2026). That helps discovery and developer setup. Takeaway: Make install surfaces obvious to reduce friction for new skill authors.

### [sanand0/talks](https://github.com/sanand0/talks)

_New talk page, transcript, and a production-ready narrative prompt let talks be shared and re-used._ (Yes, the HTML is longer than some essays.)

- **Published a full talk page.** Added `2026-01-20-agentic-ai-in-action-deloitte/index.html` and assets in commit [4384e10](https://github.com/sanand0/talks/commit/4384e109757b9ea9f90a60c961e1eb10d585397f) (20 Feb 2026). The page bundles sketchnote, audio, and embeds for easy sharing. Takeaway: A single tidy page makes dissemination trivial.

- **Added transcript for accessibility and search.** Committed `transcript.md` for the Deloitte talk in [4384e10] (20 Feb 2026), making quotes and highlights reusable. Takeaway: Transcripts unlock clipping, quoting, and repurposing.

- **Saved the narrative prompt.** `prompt.md` stores the generation prompt and instructions in [4384e10] (20 Feb 2026). That preserves reproducibility for future write-ups. Takeaway: Save the prompt that produced the good prose.

### [sanand0/image-filters](https://github.com/sanand0/image-filters)

_A sandbox to let agents and CLI filters invent new image looks, backed by reproducible tools and inputs._ (Yes, yet another place for imagemagick to misbehave.)

- **Seeded the project with discovery prompts.** Added `prompts.md` describing agent-driven filter exploration in [71084dc](https://github.com/sanand0/image-filters/commit/71084dc47aa1391fc2fbb4bb2a7027724244fc5e) (18 Feb 2026). It frames multi-agent experiments and validation needs. Takeaway: Define experiments before you run dozens of noisy variations.

- **Provided reproducible tool notes and inputs.** README documents installing Fred's ImageMagick scripts and GMIC, and inputs were added in [71084dc] (18 Feb 2026). That makes experiments runnable for others. Takeaway: Ship the inputs and install notes alongside ideas.

### [sanand0/tools](https://github.com/sanand0/tools)

> A lightweight web utility added: Ask AI for instant, shareable redirects to different AI chat engines.\_ (Yes, the internet needed a one-click "ask" button.)

- **New Ask AI tool.** Added `askai/index.html` and `script.js` to redirect queries to chosen providers in commit [971aac7](https://github.com/sanand0/tools/commit/971aac738f6907c38fccabefc250c64afaaaa7de) (15 Feb 2026). It supports provider choice and instant redirects. Takeaway: Small, dependable UX accelerates experimentation.

- **UX, tests, and sharing.** Added `askai/askai.test.js` tests and a copy-link feature; updated `tools.json` to list the tool in [971aac7] (15 Feb 2026). The tests codify expected redirect behavior. Takeaway: Test small UI flows to avoid surprise redirects.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_Student-facing course repo now links recordings directly to Drive for easier access._ (Yes, students will actually find recordings now.)

- **Linked Meet recordings.** Replaced the prior video link with a Google Drive recordings folder in README via [d5cfdd5](https://github.com/sanand0/tools-in-data-science-public/commit/d5cfdd5c0d12eaca13ada5c4bffe5d7b499c97f7) (15 Feb 2026). This reduces friction for students looking for session videos. Takeaway: Make materials discoverable where students already look.

## Lessons

- Convert tacit prompts into formal SKILLs. That increases reuse and auditability.
- Automate boring metadata work. Deterministic metadata eliminates UI surprises.
- Small editor tools compound. Clipboard and markdown fixes save hours weekly.
- Make assignments runnable. Concrete server-side tasks improve assessment fidelity.
- Ship inputs and install instructions. Experiments need reproducible environments.

## Suggestions

- Add CI that validates and regenerates openai.yaml on PRs. It prevents metadata drift.
- Run a demo showing a generated SKILL in the UI. A live screenshot uncovers UX gaps.
- Add unit tests for clean_markdown and rename_receipts. Tests reduce regressions.
- Wire TDS assignments to a simple auto-grader harness. Start with hash-validated answers.
- In image-filters, run one automated agent loop and store outputs under versioned folders. That produces a repeatable experiment trail.
