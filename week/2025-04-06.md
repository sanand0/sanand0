## Smarter Tools, Smoother Deployments, and Fresh Scripts

This week features new tools for code similarity, Google Fit data, and quote comparisons. Plus, deployment pipelines got a trim, and Fish shell setup gains a new friend.

### [sanand0/scripts](https://github.com/sanand0/scripts)

Shell helpers get background launches and organized new utilities, including a handy Fish shell tweak. Yes, you really needed another Fish abbr.

- **Background launches in `rofi-files.sh`:** Changed `open` to run via `setsid` so apps like VLC open without blocking Rofi ([0c36a89](https://github.com/sanand0/scripts/commit/0c36a895d63baa812e821dd75ea0ed7bcbf926a5), `rofi-files.sh`).
- **Added Atuín support:** Fish shell startup script now initializes [atuin](https://atuin.sh) if installed for enhanced shell history ([0c36a89](https://github.com/sanand0/scripts/commit/0c36a895d63baa812e821dd75ea0ed7bcbf926a5), `setup.fish`).
- **Imported old useful bash scripts:** Added `chars` (finds non-ASCII chars per line) and `rgb` (converts RGB to hex and vice versa) scripts for text and color manipulation ([4a45c5f](https://github.com/sanand0/scripts/commit/4a45c5f89943e23e5f0bd04b391d86bff8d81bd8)).
- **New alias for `icdiff`:** Fish aliases now include `icdiff` wrapped with offline modes to speed up diffing ([4a45c5f](https://github.com/sanand0/scripts/commit/4a45c5f89943e23e5f0bd04b391d86bff8d81bd8), `setup.fish`).
- **Data visualization with `viz.py`:** Introduced Python script to render CSV data into HTML reports using customizable templates and sparklines ([4a45c5f](https://github.com/sanand0/scripts/commit/4a45c5f89943e23e5f0bd04b391d86bff8d81bd8), `viz.py`). Perfect for quick insights without heavy tooling.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

Big leap in academic coding fairness and cleanup of code similarity metrics. Because cheating detection never sleeps.

- **Project 1 code similarity evaluator:** Added `similarity.py` to score Python code similarity across repos using MinHash fingerprints and Jaccard index, helping flag overly similar submissions ([4e8b784](https://github.com/sanand0/tools-in-data-science-public/commit/4e8b7846d7c80aaa4b31f74ed9f1cc7203ece56a), `project-1/similarity.py`).
- **Robustness fixes:** Tweaked directory exclusions to skip more environment folders like those ending with `env` to avoid noise in code walks ([c7df7cf](https://github.com/sanand0/tools-in-data-science-public/commit/c7df7cfe040ca4f7b2be58758dd1be63dac66508), `similarity.py`).
- **Removed unused tqdm:** Simplified code by dropping progress bar dependencies, plus added debug prints for listing Python files in each directory ([8e1f4d4](https://github.com/sanand0/tools-in-data-science-public/commit/8e1f4d4cb92033070c9d4ccd2d2007f423019314), `similarity.py`).
- **Major refactor of similarity script:** Reworked AST docstring removal, tokenization, and minhash generation for accuracy and better error handling. Now supports robust Python 3.12+ ([73b4fc6](https://github.com/sanand0/tools-in-data-science-public/commit/73b4fc6d05acfdc5ea99128f215b56227cbaaea2), `similarity.py`).
- **Documentation update:** Added mention of the new similarity tool in README for Project 1 context ([4e8b784](https://github.com/sanand0/tools-in-data-science-public/commit/4e8b7846d7c80aaa4b31f74ed9f1cc7203ece56a), `project-1/README.md`).

### [sanand0/llms-in-education](https://github.com/sanand0/llms-in-education)

Deployment workflows got a spring cleaning for greater simplicity and stability. Because less is more, even for CI.

- **Simplified GitHub Actions deployment:** Removed unnecessary steps and permissions, streamlining the deploy pipeline to use fewer explicit commands ([eb497f3](https://github.com/sanand0/llms-in-education/commit/eb497f3d03eca13e4104cdceb44d66fa00cfad11), `.github/workflows/deploy.yml`).

### [sanand0/llmhallucinations](https://github.com/sanand0/llmhallucinations)

Deployment setup matches other repos for consistency, shedding clutter.

- **Clean GitHub Actions deploy workflow:** Removed redundant steps and tightened permissions, ensuring smooth page deployment ([488ca7e](https://github.com/sanand0/llmhallucinations/commit/488ca7e80f3482b52c00b03894215075f2396a28), `.github/workflows/deploy.yml`).

### [sanand0/til](https://github.com/sanand0/til)

More than just deployment pruning; updated notes continue the great AI and tech knowledge-sharing streak.

- **Streamlined deployment workflow:** Merged build and deploy steps to reduce overlap and updated permission scopes ([cf48d4a](https://github.com/sanand0/til/commit/cf48d4a26aacae850a1bbdc77139f3adef9487a1), `.github/workflows/deploy.yml`).
- **Extensive knowledge note updates:** Added detailed AI use case breakdowns, trends in multimodal models, agent platforms, and reflections on evolving app markets ([030322e](https://github.com/sanand0/til/commit/030322e67ccfec7aa81ad4187bb361dd22de7626), `llms.md` and `til.md`).

### [sanand0/tools](https://github.com/sanand0/tools)

New playgrounds freshen up the site. Competition in quotes, new fitness insights, and icon fixes round out the week.

- **Add Google Fit activity summary page:** Upload your exported `.tcx` files and get a neat table of sports activities by date. Handy for folks tracking workouts or just curious about data visualization ([051ecc3](https://github.com/sanand0/tools/commit/051ecc33e084fc48ec6bfa43c1305b32c1ca3e55), `googlefit/index.html`).
- **Integrate Google Fit tool in menu:** Updated `tools.json` to show the new Google Fit summary tool with icon and description ([051ecc3](https://github.com/sanand0/tools/commit/051ecc33e084fc48ec6bfa43c1305b32c1ca3e55), `tools.json`).
- **Launch 'Quotes arena':** A fun interactive web app to compare quotes from different AI models and track win records with local storage. If debating quotes was a sport, this would be the stadium ([c1a45af](https://github.com/sanand0/tools/commit/c1a45af61aad94ed5b2cd8bb8f969f3e7d38c4fe), `quotesarena/index.html` & `quotesarena/quotes.csv`).
- **Add icon for Quotes arena:** Corrected navigation display with a snappy quote icon ([b38db86](https://github.com/sanand0/tools/commit/b38db8643b048c401bf90aafa1b28752a1ca4d65), `tools.json`).

### [sanand0/webfeatures](https://github.com/sanand0/webfeatures)

Scheduling your deployments? Now tidier and safer.

- **Refactor deployment workflows:** Scheduled monthly scrapes and manual triggers combined, with cleaner permissions and fewer steps ([349d4b5](https://github.com/sanand0/webfeatures/commit/349d4b5b9016bab7624699ba090baa7be6c8d06d), `.github/workflows/deploy.yml`).
- **Merged duplicate workflow updates:** Aligned all deploy workflow files for consistency and rights reduction ([69a2e39](https://github.com/sanand0/webfeatures/commit/69a2e393eb307921fbdccc4d62c058bb4ac39472), `.github/workflows/deploy.yml`).
- **Fixed minor duplicate changes:** Combined commits cleanly removing duplicated cron trigger declarations ([88586c0](https://github.com/sanand0/webfeatures/commit/88586c089b6f157bc5edc226779b87ae634a3962), `.github/workflows/deploy.yml`).

### [sanand0/quizzes](https://github.com/sanand0/quizzes)

Quizzes repo hears "less is more" with build pipeline refinement.

- **Simplify deployment workflow:** Sped up and consolidated GitHub Actions deploy steps for quizzes repo as for others, cutting unnecessary tasks ([06b1fd7](https://github.com/sanand0/quizzes/commit/06b1fd79a689dacf95927f3d13319a5e47e5d4be), `.github/workflows/deploy.yml`).

## Suggested Next Steps

- Add automated benchmarks to measure startup improvements with new Fish init changes.
- Extend `similarity.py` with web UI or GitHub Action to flag code similarities in merge requests.
- Enhance Google Fit app with charts or export options.
- Integrate `quotesarena` voting results into a leaderboard or persistent server.
- Apply deployment workflow simplifications consistently across other repos to reduce maintenance overhead.