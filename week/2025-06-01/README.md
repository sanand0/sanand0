## New AI Tools, Cloud Diagrams, and Better Dark Theme Controls

This week saw launches of neat demos and tutorials, updates to dark theme toggles, powerful open-source cloud icons for PlantUML, and killer enhancements to GitHub user data tools. Also, the IITM Tools in Data Science course got crucial fixes, while an AWS-AI combo added smarter answers with citations.

### [sanand0/tools](https://github.com/sanand0/tools)

New tools and major enhancements make data handling and GitHub interaction smoother and friendlier.

- **GitHub User Data Extractor revamped:** Now you can input usernames with or without '@', full URLs, and GitHub Pages links. It neatly formats dates, numbers, adds clickable links, and displays avatars as images ([b1b5ed4](https://github.com/sanand0/tools/commit/b1b5ed43ae3cb8cfe92e3c59fc8ba964b48ad72a)). Yes, you really needed another GitHub abbr, but this one’s practical.
- **JSON to CSV converter improved:** Auto-detects JSON type (array or object) and preserves key order in output for more intuitive results ([afbaef6](https://github.com/sanand0/tools/commit/afbaef62b09f00712f87471e731467161998bc49)). No more scrambling your columns!
- **GitHubStars tool gets example input:** Paste example markdown links and see live updates on star counts right away ([7aea2b6](https://github.com/sanand0/tools/commit/7aea2b60ec3a935e97bcb67b1518b097810bea46)).
- **UI tweaks for larger demo grid:** Added support for 4 columns on extra-large screens to avoid lonely widows in your demos gallery ([0c2c0de](https://github.com/sanand0/llmdemos/commit/0c2c0dee6b04e6af8eb8b43f287558d0043e8bbc)).
- **Preparing for broader repo search in podcast tool:** Created a branch to accept GitHub repo search queries, a superset of just usernames ([see related PR](https://github.com/sanand0/tools/pull/6)).

### [sanand0/tutorials](https://github.com/sanand0/tutorials)

If PlantUML diagrams have been a chore, not anymore.

- **New PlantUML architecture diagram tutorial:** How to guide ChatGPT to create cloud architecture diagrams using official AWS, Azure, and GCP icons. Includes a handy bash script to generate those icon includes ([3b22f54](https://github.com/sanand0/tutorials/commit/3b22f54e776a5812682383165c930b6e4cfc495f), [d9437f8](https://github.com/sanand0/tutorials/commit/d9437f8d7f51804792690e442bb7af06ee85a28d)). Now you’ll have cloud diagrams that actually look like clouds, not just boxes.
- **Improved prompt and instructions:** The README now carefully guides you step-by-step, plus fixes minor errors to keep you on track.

### [sanand0/bootstrap-dark-theme](https://github.com/sanand0/bootstrap-dark-theme)

Your dark theme toggler got smarter and safer.

- **Treat unknown themes as ‘auto’:** If someone tries an unsupported theme value, it falls back to using the system preference instead of showing an error ([f506d4cb](https://github.com/sanand0/bootstrap-dark-theme/commit/f506d4cb1ba68fe2a89ca9dbea5569673b5b2d38)). Because sometimes you don’t want humans typing random theme names.
- **Added tests:** Automated tests in Vitest verify theme behavior across light, dark, auto, and invalid values ([dark-theme.test.js](https://github.com/sanand0/bootstrap-dark-theme/blob/main/dark-theme.test.js)).
- **New example HTML:** A fully working standalone demo page with Bootstrap 5.3 and dropdown button to toggle themes is included ([dark-theme.html](https://github.com/sanand0/bootstrap-dark-theme/blob/main/dark-theme.html)).

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

The online Data Science course materials remain polished and up to date.

- **Corrected relative links in 2025 Jan content:** Updated many file and sidebar URLs to use correct paths for the May 2025 semester project 1 notes release ([d186af1](https://github.com/sanand0/tools-in-data-science-public/commit/d186af121f780ce839106a006c8cf2abbadb5610)). Less broken links, more learning!
- **Moved virtual TA project images into ‘images/’ directory:** Keeps the repository tidier and references consistent ([de969a3](https://github.com/sanand0/tools-in-data-science-public/commit/de969a3895b1d53d8e1d5ba8500e77efe37f8534)).
- **Removed confusing note about GA3 preponement:** The graded assignment 3 submission date stays as June 1, 2025 ([c04fb74](https://github.com/sanand0/tools-in-data-science-public/commit/c04fb74e1357db847fab47c90ee22ba9b1fa105b)).
- **Minor typo fix:** Fixes an important sentence about GitHub Pages on the course site ([13d50dd](https://github.com/sanand0/tools-in-data-science-public/commit/13d50dd9f29f6eaa60c9205ba5d9df3881c17b8e)).

### [sanand0/topictrends](https://github.com/sanand0/topictrends)

New repo alert! A fresh start tracking scholarly topic trends with AI help.

- **Repository created and initial commit:** This app uses Large Language Models to interpret data trends in simple English ([55c0ad6](https://github.com/sanand0/topictrends/commit/55c0ad6cc647dc2751c2bf70ab4b0808fb763ccd)).
- **Interpretation panel added:** Now you can ask the LLM to summarize and explain topic trends from arXiv data with a customizable prompt. The output is neatly rendered with markdown ([55c0ad6](https://github.com/sanand0/topictrends/commit/55c0ad6cc647dc2751c2bf70ab4b0808fb763ccd)).
- **User interface improvements:** Prompt text area expanded, default prompt filled, and interpretation UI toggles on demand. Slides your papers into plain English territory in style.

### [sanand0/personagen](https://github.com/sanand0/personagen)

Fresh setup to generate synthetic personas for marketing surveys and testing.

- **New repository created:** This tool uses LLMs to automatically create market research audience personas ([create event](https://github.com/sanand0/personagen/commit/initial)). Because who has time to make up personas anymore? Let the AI do the imagining.

### [sanand0/apiagent](https://github.com/sanand0/apiagent)

Your natural language API querying tool keeps growing smarter and more integrated.

- **Added Google Analytics API support:** Query web traffic and user behavior data directly via natural language ([fe779f89](https://github.com/sanand0/apiagent/commit/fe779f8974373b857b0e420b834e0997cab95c76)). Great for getting quick insights from your analytics without diving into the dashboard.
- **Integrated OpenAlex alongside Crossref API:** Query scholarly works via multiple APIs transparently in one chat experience ([0fae636](https://github.com/sanand0/apiagent/commit/0fae636e75dd11d39510fef1938ee594e6a070fd)). If you’re serious about academic data, this makes it easier.
- **Added status display of current fetches:** When the app talks to an API, you see which page it’s fetching, boosting transparency and user feedback ([0fae636](https://github.com/sanand0/apiagent/commit/0fae636e75dd11d39510fef1938ee594e6a070fd)).
- **Graceful error reporting in LLM calls:** Instead of crashing, errors now display in the chat flow helping you debug or refine your query ([7bf16c15](https://github.com/sanand0/apiagent/commit/7bf16c15dc04b6edc894553360d176b7f6585ef6)).

### [sanand0/aws-rag](https://github.com/sanand0/aws-rag)

Sharpened the retrieval augmented generation (RAG) on AWS with better answers and full stack.

- **New OpenSearch indexing Python scripts:** Added powerful tools to chunk, index, and embed Markdown or text docs for vector search on OpenSearch ([index.py](https://github.com/sanand0/aws-rag/blob/main/index.py), c05659e). Because your vector DB needs a strong librarian.
- **Hybrid search with query rewriting and embeddings:** Uses GPT-4 to rewrite queries and craft sub-questions, then runs hybrid BM25+k-NN search ([search.py](https://github.com/sanand0/aws-rag/blob/main/search.py), 99b5d31). Makes your searches smarter, like a bit of sleight-of-hand behind the scenes.
- **Add answer generation with citations:** Retrieves relevant documents and prompts GPT to answer based on them, including citations with cross-references for trustworthiness ([9dc1cf0](https://github.com/sanand0/aws-rag/commit/9dc1cf06a70a8e4c570461841e958b61cb8673fd)). Finally, an AI that can say “I got this from source #3.”
- **Terraform plus Docker for deployment:** Infra now includes OpenSearch domain with secure basic auth, builds container image with Docker, managing via tofu CLI ([main.tf](https://github.com/sanand0/aws-rag/blob/main/main.tf), dd2c19d). Deploy with confidence on AWS.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

Your favorite Generative AI WhatsApp group’s podcast automation just got tighter on date alignment.

- **Correct podcast week range:** The podcast folders now correspond exactly to the Sunday they’re released and cover the full prior week to Saturday, avoiding future data leakage ([fe01430](https://github.com/sanand0/generative-ai-group/commit/fe01430c3c375a5286846f4a29239d703d5cf76d)). Half the mystery of “Did this episode cover last week or this week?” solved.

## Suggested Next Steps

- Bundle the PlantUML tutorials with your cloud diagrams for easier shareable architecture docs.
- Try out the enhanced GitHub User Data Extractor for packing rich user profiles effortlessly.
- Explore integrating the AWS RAG setup with your own document datasets — citations on demand!
- Experiment with the Topic Trends app and feed it some arXiv data for research insights.
- If you’re building UI themes, steal a look at the Bootstrap-dark-theme’s neat fallback logic and tests.
- Join the Tools in Data Science public course or use it for teaching future data pros.
- And maybe… build your own tiny API agent with that new Google Analytics integration?
