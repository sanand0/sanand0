## Busy June with Data Prep, API Upgrades, and New Tools

This week’s work revealed that clear data prep pays off, multiple APIs rock with unified token support, and meshing markdown and CSV tools ease data handling. New utilities and podcast updates show how LLMs continue to enrich workflows in various domains.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_Sharpen your data science fundamentals with high-impact, practical tutorials and updated course timelines for a smoother learning experience._

- **Updated Project 1 and GA4 deadlines:** Postponed the Project 1 submission date from 14 Jun to 18 Jun, and delayed the release of Graded Assignment 4 until 14 Jun to better align with student pacing ([09c99c2](https://github.com/sanand0/tools-in-data-science-public/commit/09c99c25ae9b175ae926ea023d0d5bdcfadfec36), 14 Jun 2025). Takeaway: Timely revisions to deadlines can relieve stress and help manage student workload effectively.

- **Added comprehensive DuckDB data preparation tutorial:** A full tutorial covering sample datasets, messy CSVs, big CSV handling, exploratory analysis, and conversion tasks offers hands-on SQL examples for real-world data cleaning ([0f7c090](https://github.com/sanand0/tools-in-data-science-public/commit/0f7c0901e73da9bb642c76ac8badba2d1867a7a9), 12 Jun 2025). Takeaway: Grounding learning with practical, curated datasets boosts mastery and confidence in complex tools.

- **Streamlined sidebar navigation and lessons:** Removed duplicate entries and cleaned the sidebar to keep navigation simple and consistent ([4ae80c7](https://github.com/sanand0/tools-in-data-science-public/commit/4ae80c7085bb11b0033d206e68441fce841391a4), 12 Jun 2025). Takeaway: A clean doc structure reduces confusion—always audit nav elements after content updates.

### [sanand0/tools](https://github.com/sanand0/tools)

_Piling on powerful LLM-driven and data utilities that simplify workflows for developers and data scientists alike._

- **Released LLM-filled-in-the-blank tool:** Introduced an interactive app to blank words in sentences and observe LLM predictions and token probabilities, with support for multiple models and streaming results ([1a8363e](https://github.com/sanand0/tools/commit/1a8363ec028d484f7fe83fcbc2528660ed79795b), 9 Jun 2025). Takeaway: Hands-on explorations of model behavior foster better prompt engineering and trust in LLM outputs.

- **Added markdown table to CSV converter:** A new tool extracts the first markdown table, converts it to CSV, drops links and images, and offers download or Excel copy options—perfect for swift data reuse ([33f057e](https://github.com/sanand0/tools/commit/33f057e0f6bc5b489df6f2c1876ec6ecce38f850), 10 Jun 2025). Takeaway: Bridge the content-structure gap; enable quick transformations between documentation and data formats.

- **Introduced CSV Table Joiner:** This web app merges multiple CSV tables on their first column, handling duplicates by overwriting earlier values, simplifying common data consolidation steps ([bb91208](https://github.com/sanand0/tools/commit/bb91208c605524c3b68aa80424388c6a2e7d04c8), 10 Jun 2025). Takeaway: Making it easy to combine datasets empowers users to avoid manual and error-prone Excel wrangling.

- **Enhanced page2md tool to preserve SVGs:** Improved the markdown conversion to retain SVG images as inline HTML for better document fidelity, especially from modern web apps like ChatGPT ([20d195f](https://github.com/sanand0/tools/commit/20d195f765d06939648c50883d044167fad2b203), 10 Jun 2025). Takeaway: Details matter; preserving visuals improves capture quality and downstream usage.

- **Built Google Tasks Exporter app:** Users can authenticate, fetch, export as CSV, copy in Excel or Markdown, and batch delete completed tasks—all with a user-friendly UI and local token persistence ([00a0359](https://github.com/sanand0/tools/commit/00a03599a5a42d554beb1481b667fff32a1e4723), 10 Jun 2025). Takeaway: Small web apps with OAuth and smooth data export seriously boost productivity.

- **Unified and improved API agent token handling:** Refactored API parameter inputs to allow multiple tokens and parameters per API, improving flexibility for complex environment setups ([ba67c3e](https://github.com/sanand0/apiagent/commit/ba67c3eeae305912d0606e2333484d2002776574), 12 Jun 2025). Takeaway: Accommodate diverse API authentication needs via scalable config patterns—less guesswork for users.

### [sanand0/linkedin](https://github.com/sanand0/linkedin)

_Transform your LinkedIn posts and comments into a sleek, browsable HTML archive with seamless GitHub Pages deployment._

- **Launched LinkedIn archive generator:** Added Node.js tool to convert LinkedIn's CSV exports of posts and comments into monthly HTML pages, an RSS feed, and clean Bootstrap styling for easy navigation ([13afdcd](https://github.com/sanand0/linkedin/commit/13afdcd1871ec54f6a938cb916abd0dbacf26d50), 13 Jun 2025). Takeaway: Unlock your social content for own reference or sharing by converting raw exports into neat, searchable archives.

- **Automated GitHub Actions workflow:** Added deploy pipeline to build and publish the archive to GitHub Pages on push, reducing manual overhead ([ffcdc3a](https://github.com/sanand0/linkedin/commit/ffcdc3a89e6b1eb04c9323d060c0388ff1e0e803), 13 Jun 2025). Takeaway: Continuous deployment keeps your archive fresh without any friction.

### [sanand0/samsara-vehicle-scraper](https://github.com/sanand0/samsara-vehicle-scraper)

_Command-line utility to backfill and analyze your fleet's rich vehicle telemetry effortlessly._

- **Initial stable release:** Scrapes paginated historical telematics data from Samsara’s API, caches JSON by date and stat type, and transforms it into time-aligned CSV with guaranteed column order ([3362bac](https://github.com/sanand0/samsara-vehicle-scraper/commit/3362bacf80c28a38322314b55579464b758529b5), 8 Jun 2025). Takeaway: Automate tedious API pagination for reliable bulk data extraction and downstream analysis.

- **Optimized parsing for memory and performance:** Improved `parse.py` to process stats by type, merging pivoted tables in sequence to reduce RAM usage and handle large datasets efficiently ([ba4c28a](https://github.com/sanand0/samsara-vehicle-scraper/commit/ba4c28a8906415156e39dacbbef969f88f1c8681), 10 Jun 2025). Takeaway: Stepwise processing wins for big data: partition workloads logically before merging results.

### [sanand0/tdsdata](https://github.com/sanand0/tdsdata)

_Furnishing practical datasets and tools to power data science courses and experimentation._

- **Improved crawl_html for web scraping tests:** Added stability with sorted sets and connected graph structure produced via `networkx` graph models, ensuring every file is reachable with structured cross-links ([4d45989](https://github.com/sanand0/tdsdata/commit/4d4598990564b892f97a9276bbffc7a7a6106584), 11 Jun 2025). Takeaway: Guarantee graph connectivity and reproducibility in test datasets to avoid surprises.

- **Published HTML table generator:** Released `html_table.py` to produce 30 randomized English word tables (50x10) for testing scraping and data extraction tools, with environment-seeded randomness ([c6c4275](https://github.com/sanand0/tdsdata/commit/c6c42756fbb7fb37d667304af635bbd1349b00e7), 11 Jun 2025). Takeaway: Synthetic yet realistic table data aids robust testing without hammering live sources.

- **Added a small JS table demo:** Swinging towards frontend demos, a JS-rich table renderer offers interaction and variable seed control for random data generation ([1c8796d](https://github.com/sanand0/tdsdata/commit/1c8796d33007db5aac1f2a74cb5f3c3827bad774), 11 Jun 2025). Takeaway: Lightweight interactive demos can supplement static datasets for richer learning.

### [sanand0/asyncsse](https://github.com/sanand0/asyncsse)

_Parse Server-Sent Events streams as async iterables with robust error handling — in under 1 KB._

- **Complete doc rewrite and improved error signaling:** Demo usage now clearly shows how errors during streaming yield `{error: ...}` objects; updated handling examples and full field support for multi-part SSE events included ([912ff59](https://github.com/sanand0/asyncsse/commit/912ff59fec1c3bf9c224d0b0df4501695e456303), 9 Jun 2025). Takeaway: Clear documentation around edge cases prevents misusage and makes streaming tooling predictable.

### [sanand0/llmevals](https://github.com/sanand0/llmevals)

_Revealing how LLMs behave when you try to override their system prompts—alignment isn’t a given._

- **Published comprehensive system prompt override evaluations:** Ran 36 models through user prompts that try to bypass system instruction, revealing varying compliance from perfect (Google Gemini Pro) to near-zero (some Llama versions) ([98b093f](https://github.com/sanand0/llmevals/commit/98b093ff6bba3010d64460fbd18590dab02de2da), 9 Jun 2025). Takeaway: Treat system prompts as fragile; build external validation and plan for prompt-injection vectors.

- **Explored temperature’s impact on override fidelity:** Slight performance shifts observed at 0.7 temperature; bigger isn’t always better, and some distilled models regress in alignment ([9381c7d](https://github.com/sanand0/llmevals/commit/9381c7d29564b2b9ec17a2940f00b1ad0146271f), 10 Jun 2025). Takeaway: Tuning parameters affects safety and robustness; test before updating models.

## Lessons

- **Encapsulate complexity:** Complex APIs and data pipelines benefit from layered, modular tools that offer clear interfaces and cache/batch mechanisms.

- **Unified inputs are a boon:** Consolidating tokens and API parameter inputs simplifies user experience and development, especially with multiple integrations.

- **Version changes demand deadline sanity checks:** When content or schedules shift, promptly updating timelines reduces confusion and aligns expectations.

- **Make data transformations accessible:** Bridging formats like Markdown to CSV or combining CSVs removes tedious manual work and boosts productivity.

- **Test LLMs thoroughly prior to deployment:** Prompt override and temperature make or break LLM alignment safety. Always validate!

- **Documentation and examples are half the work:** Rich, up-to-date docs and real usage examples empower adoption and minimize support hassles.

## Suggestions

- Instrument tracking of start-to-finish pipeline runtimes for the Samsara scraper to quantify gains from the optimized parser.

- Add error boundary UI & recovery in asyncSSE tooling for real-time apps consuming SSE streams—maybe leverage reconnection hints (`retry`).

- Expand LLM fill-in-the-blank tools with multi-token blanking and across multiple concurrent models for horseshoe-shaped sampling.

- Consider filtering or consolidating dead/behind-the-scenes tokens in the API agent’s multi-token input UI for cleaner UX.

- Experiment with embedding and video storage RAG demos (as referenced in notes)—might be a novel data retrieval workaround for mobile.

- Automate monthly refreshing or snapshots in the LinkedIn archive to reduce manual update steps further.

Yes, this week really needed a whole new Fish abbr for mkdir + cd! Small conveniences stack up like micro-optimizations do.
