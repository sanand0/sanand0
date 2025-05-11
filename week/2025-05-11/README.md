## LLM Safety Nets & Practical Data Workflows

This week brings clearer LLM evaluation results, new videos for easier setup, and practical guides for data crawling and conversion. Plus, tools to help you use LLMs affordably and reliably in your projects.

### [sanand0/llmevals](https://github.com/sanand0/llmevals)

Understanding how to trust unreliable language models just got clearer and more visual.

- **New double-checking evaluation article:** Added a detailed guide showing how using multiple LLMs together drastically cuts hallucinations, with a real customer-support dataset example. See the main article and code at [f35e758](https://github.com/sanand0/llmevals/commit/f35e758).
- **Accurate error vs effort calculations:** Replaced rough best-fit curves with exact disagreement and error stats, showing realistic quality/effort tradeoffs when double- or triple-checking LLM outputs ([4979640](https://github.com/sanand0/llmevals/commit/4979640710ed2636a10b746ea9e92a895de3842c)).
- **Effort-error plot added:** Visualized how model agreement improves accuracy at the cost of extra human effort ([e9edeba](https://github.com/sanand0/llmevals/commit/e9edebaf1e079c7401fa5b2a0f51b01003119945), [4f3a6a9](https://github.com/sanand0/llmevals/commit/4f3a6a9b8de06f8ce78805e25b5d09c627f53326)).
- **Interactive evaluation UI:** A new clean HTML page with tables, graphs, and popovers helps explore LLM performance. (Yes, human-in-the-loop just got fancier.) ([f35e758](https://github.com/sanand0/llmevals/commit/f35e758))
- **Setup instructions simplified:** Cloning and running promptfoo to evaluate is straightforward, lowering the barrier to try multi-model checks yourself ([f35e758](https://github.com/sanand0/llmevals/commit/f35e758)).

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

Your all-in-one IITM data science toolbox just got more organized, visual, and practical.

- **Sidebar numbered modules:** Each course module on the sidebar now shows a handy number (1–7), making it easier to track progress and plan studies ([427b688](https://github.com/sanand0/tools-in-data-science-public/commit/427b6882eb8fca72f192fc6f6e245f586e3bb555)). Because a numbered list makes everything feel more official.
- **Win10 WSL install video added:** A 12-minute visual guide to quickly getting WSL set up on Windows, complementing existing bash tutorials ([fd5a69c](https://github.com/sanand0/tools-in-data-science-public/commit/fd5a69ca9efd2dbccf0d63d7241471d8343727a9)).
- **Guidance on OpenAI API keys for LLM CLI:** Clear tips for TDS students on where to find and how to set `OPENAI_API_KEY` to use command-line LLM tools ([bf920b9](https://github.com/sanand0/tools-in-data-science-public/commit/bf920b9a1bb19d3d85ccd07ca83bdd19377273fc)).
- **Crawling and Markdown conversion added:** New docs on website crawling with wget, plus converting HTML and PDF files to Markdown with tools like defuddle-cli and pandoc ([crawling-cli.md](https://github.com/sanand0/tools-in-data-science-public/blob/HEAD/crawling-cli.md), [convert-html-to-markdown.md](https://github.com/sanand0/tools-in-data-science-public/blob/HEAD/convert-html-to-markdown.md), [convert-pdfs-to-markdown.md](https://github.com/sanand0/tools-in-data-science-public/blob/HEAD/convert-pdfs-to-markdown.md)). Helpful for when you want your data clean and LLM-friendly.
- **Updated course schedule and links:** Adjusted graded assignments due dates and improved instructions for finding announcements ([cc995485](https://github.com/sanand0/tools-in-data-science-public/commit/cc9954859f0ad1ab2fcdbd5337bbfe02de5888dd)).

### [sanand0/temp-iitm-bs-rag](https://github.com/sanand0/temp-iitm-bs-rag)

Building a scalable retriever-augmented generation (RAG) system with Google Cloud SQL and FastAPI gets smoother.

- **Dockerfile upgrade:** Base image updated from Python 3.11 to 3.13 slim; uv runtime added for better async support ([aa5b962](https://github.com/sanand0/temp-iitm-bs-rag/commit/aa5b962b44322dd6a25c7904664c6311894f3652)).
- **Google Cloud SQL setup precision:** Environment variable fixes and expanded setup instructions for instance, DB, user, and connection ([bf60eff](https://github.com/sanand0/temp-iitm-bs-rag/commit/bf60efff46f552e44c742d522cb3e4c607c5f1a8)).
- **Full README overhaul:** Detailed step-by-step for env vars, crawling with wget, chunking Markdown files, PostgreSQL vector extension, hybrid search, FastAPI app running and deployment to Google Cloud Run, plus example queries ([5b38ecf](https://github.com/sanand0/temp-iitm-bs-rag/commit/5b38ecf7a11a43d0445ef7dd9b7e6126bb76477e)).
- **FastAPI app improvements:** Cleaner asyncpg pool setup including `pgvector` extension registration; improved search and answer endpoints ([6211856](https://github.com/sanand0/temp-iitm-bs-rag/commit/6211856a06d956f1103299dd3b60c2bc4dac5d9e)).
- **Added script to upload chunks:** Python script to batch-upload content chunks via REST API with asyncio and aiohttp ([README](https://github.com/sanand0/temp-iitm-bs-rag) and [upload_chunks.py](https://github.com/sanand0/temp-iitm-bs-rag/blob/main/upload_chunks.py)).

### [sanand0/aipipe](https://github.com/sanand0/aipipe)

Get discounted, easy access to OpenAI and OpenRouter APIs without backend headaches.

- **OpenAI embeddings API support:** Added proxying of OpenAI embedding requests through AI Pipe, enabling embeddings at low cost with your AI Pipe token ([e264778](https://github.com/sanand0/aipipe/commit/e2647783bf5ad92958a408003a475282d97ba2d6)).
- **Improved HTTP headers:** Send `HTTP-Referer` and `X-Title` headers to OpenRouter so usage is trackable and identifiable in their dashboard ([e12526c](https://github.com/sanand0/aipipe/commit/e12526c7f3314c9223b3b7c0b9974ec4f55bd3e0)).
- **Enhanced docs and example usage:** Clearer instructions on setting `OPENAI_API_KEY` and `OPENAI_BASE_URL` for API-compatible apps, illustrated with curl and `llm` CLI examples ([8461f85](https://github.com/sanand0/aipipe/commit/8461f85c6f22b1fa58e17c796c8da7a8f0f8d7ac)).
- **Updated GitHub stars and references for competitors:** Keeps the README current in the fast-moving LLM router ecosystem ([56ce4df](https://github.com/sanand0/aipipe/commit/56ce4dfdd196c0b60fb71dc42fbc74403840ca81)).

### [sanand0/til](https://github.com/sanand0/til)

Fresh notes and new LLM learnings drop for May 2025.

- **New LLM insights:** Reports on Ollama chatbot comparisons, Nvidia's math model, voice quality of Dia TTS, practical reasoning model benefits, and a fresh crop of open-source computer use agents ([7d9444e](https://github.com/sanand0/til/commit/7d9444e24f479b2f3d5d7ce03f73c0410246402c)).
- **Updated general tips:** Includes utilities like `ngrok` tricks, GitHub Codespaces commands, and reflections on AI adoption speed and human-AI workflow changes.
- **Emphasis on practical use:** Notes about polite AI use effects and new reasoning abilities in LLMs, without losing sight that these models still mess up occasionally. (Because y’all needed another Fish abbr, right?)

## Suggested Next Steps

- In llmevals, expand to other datasets and explore automated model combination strategies for reduced human overhead.
- For tools-in-data-science-public, consider adding live demos or a screencast walkthrough of the crawling and conversion pipelines.
- In the temp-iitm-bs-rag repo, deploy an example instance publicly for student experimentation.
- For aipipe, add client library snippets in popular languages (Python, JS) showing easy integration.
- In til, structure notes for easier search or tagging using your new vector/RAG methods from temp-iitm-bs-rag.

This batch is all about grounding your AI workflows in proven facts, smooth dev environments, and practical tooling that saves time and money. Happy hacking!