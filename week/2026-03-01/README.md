## A week of turning messy student code into stories, demos, and deployable analysis

This week focused on turning raw exam events into structured error narratives and reproducible pipelines. The key lesson: structured exports plus small interactive UIs turn deep analysis into actionable recommendations.

### [sanand0/pyoppe](https://github.com/sanand0/pyoppe)

_Catalog errors, model student process, and ship stakeholder-ready narratives so non-technical teams can act on results._

- **Structured error export & UI.** Wrote a large structured export and narrative UI ([errors.json](https://github.com/sanand0/pyoppe/blob/main/analysis/errors.json), [errors.html](https://github.com/sanand0/pyoppe/blob/main/analysis/errors.html)) in commit [0f5b975](https://github.com/sanand0/pyoppe/commit/0f5b9757345238055d9846c910b0d685f5dfabb1) (24 Feb 2026). This turns Markdown clusters into queryable JSON and an interactive report. Takeaway: export once; build many UIs from the same canonical JSON.

- **Error-cluster writeup and hygiene.** Added 50+ per-cluster markdown reports and cleanup in commit [c339ed9](https://github.com/sanand0/pyoppe/commit/c339ed9e9d4a1c7199e29a5ff83258d24c63f3ab) (23 Feb 2026). These give question-level examples and reproducible snippets for reviewers. Takeaway: real examples make abstract failure modes fixable.

- **Archetype timelines & examples.** Built [analysis/build_archetype_timelines.py] and committed timelines plus JSON ([44524ce](https://github.com/sanand0/pyoppe/commit/44524ce001df5b8db642ee79c80428a6f17e82a6)) (24 Feb 2026). This extracts student timeline examples for each archetype. Takeaway: show one concrete timeline; stakeholders stop arguing about labels.

- **End-to-end pipeline and stakeholder report.** Added stepwise analysis scripts (Steps 1–10) and a one‑page stakeholder report ([analysis/REPORT.md]) in [3063a7f](https://github.com/sanand0/pyoppe/commit/3063a7fc6791f75321564f937964cdea87d26fae) (22 Feb 2026). This packages psychometrics, process, and redesign guidance. Takeaway: packaging analysis as a reproducible pipeline makes handoffs smooth. (Yes, you really needed another REPORT.)

### [sanand0/datastories](https://github.com/sanand0/datastories)

_A small, interactive demo that shows how LLMs can help migrate SQL workloads and explain impact._

- **SQL-migration interactive demo.** Added a standalone demo with payload and UI files ([index.html], [app.js], [demo-data.js]) in commits [0891e4e](https://github.com/sanand0/datastories/commit/0891e4e4f1a04bc5b7a0abd7e21124139a5b632a) and [d5e4914](https://github.com/sanand0/datastories/commit/d5e4914fb73b0f93f27735fe4eeb018a0b30f8a0) (28 Feb 2026). The demo walks through MSSQL→MySQL conversions with verification. Takeaway: demos turn abstract migration risks into concrete decisions.

- **Scripted demo data.** Included realistic per-script metadata and execution stats ([sql-migration/script-sql-data.js]). This supports the conversion narrative and risk flags. Takeaway: synthetic telemetry helps prioritize hardest scripts first.

- **Doc and README for clients.** Added README and run instructions (see [sql-migration/README.md]). This makes local demos trivial to run. Takeaway: ship a one-command demo to close client meetings faster. (Who doesn’t love a shiny migration map?)

### [sanand0/til](https://github.com/sanand0/til)

_Keep learnings discoverable and the discovery list fresh so small ideas don’t evaporate._

- **Weekly notes and tasks updated.** Added Feb 2026 notes and small app todos in commit [a7a97f7](https://github.com/sanand0/til/commit/a7a97f7eff0b4bb3a1b0e5a7b0638617b095ecdf) (22 Feb 2026). This keeps short experiments and owners visible. Takeaway: short dated TILs beat forgotten half-formed ideas.

- **Trending repos refresh.** Updated [trending-repos.tsv] with a fresh snapshot (22 Feb 2026). This keeps the repo-discovery feed useful. Takeaway: curate often; discovery loses value fast. (Yes, you really needed another trending list.)

- **Apps TODO hygiene.** Fixed ownership and formatting in apps.md to avoid future confusion. Takeaway: single-line fixes prevent busywork later.

### [sanand0/schoolai](https://github.com/sanand0/schoolai)

_Build realistic demos and realtime triage UI to show product value quickly to education teams._

- **Synthetic credit‑checking dataset and render pipeline.** Added strict-schema generators and rendering scripts ([scripts/generate_synthetic_bundles.py], render manifests) in commit [eb1b120](https://github.com/sanand0/schoolai/commit/eb1b120adf620a6fa06adbe0c089c1683433e78b) (24 Feb 2026). It creates mixed-format applicant bundles for demoing document ingestion. Takeaway: realistic synthetic data beats hand-wavy slides.

- **Realtime triage agent UI and dataset.** Added a full triage dashboard, styling, and streaming messages in commit [81d5ec8](https://github.com/sanand0/schoolai/commit/81d5ec895863921d449c7299e0054e4cc59d1039) (24 Feb 2026). The app simulates omnichannel intake and auto‑drafts. Takeaway: a working front end sells ideas faster than a design doc. (Also: the demo loves streaming chaos.)

- **Preview assets and manifests.** Included render manifests and contact sheets for reviewers. Takeaway: include visual artifacts for non-technical stakeholders.

### [sanand0/blog](https://github.com/sanand0/blog)

_Add content and tidy taxonomy so readers find practical pieces quickly._

- **New practical posts.** Added posts on explanations, repurposing writing, and transcripts ([memorable-explanations], [repurposing-blog-posts-for-talks], [transcript-ai-ded-interviews]) in [8a264c7](https://github.com/sanand0/blog/commit/8a264c7546a426347e59dc5290ccffa536b6c5a6) (23 Feb 2026). These give short, actionable workflows. Takeaway: small how-tos scale better than long essays.

- **Category standardization & prompt fragments.** Standardized categories (many historical posts moved from "links" → "games") and added a reusable prompt fragment for sketchnotes ([pages/prompts/fragments.md]). Takeaway: consistent taxonomy improves findability.

- **Minor corrections and book list update.** Fixed a timing claim and appended a book to reading lists. Takeaway: fix small factual drifts early.

## Lessons

- Structure first, UI second. A canonical JSON export lets many visualizations and narratives reuse the same truth.  
- Show, don’t tell. Concrete student timelines and example submissions persuade stakeholders faster than aggregate stats.  
- Reproducible scripts matter. Packaging each analysis step as a script (Steps 1–10) reduces drag for reruns and audits.  
- Synthetic realism sells demos. High-quality synthetic bundles and realistic telemetry enable safe product demos.  
- Small docs and curated lists compound. Weekly notes and a fresh trending list keep idea flow healthy.

## Suggestions

- For pyoppe: run the LLM-based syntax‑repair arm on a sample (Track A/B) and record measurable recovery rates. Add a tiny CI job to validate errors.json schema on each run.  
- For datastories: add a minimal static server (or GitHub Pages demo) for the SQL migration story to make it clickable during pitches. Add stepwise "show me risk" toggles.  
- For schoolai: produce a 60–90s demo video of the triage stream and one credit‑check flow. Add privacy redaction tests for synthetic bundles.  
- For til & blog: automate weekly publishing of TIL notes and trending repos, and add a small test that flags malformed note date lines.  
- General: capture a short README in each analysis output folder documenting required inputs and runtime cost (RAM/CPU, expected wall time). This lowers the bar for collaborators.

If you want, I can draft the short demo script (30–90s) for the triage UI, or write the PR checklist to add CI checks for pyoppe’s error JSON schema. Which would help most next?