Alex: Hello and welcome to Anand’s Weekly Codecast for the week of 11 May 2025!

Maya: We’re Alex and Maya, and today we’ll walk you through the highlights of Anand’s commits this week.

Alex: First up, improvements in the data science tools course content.

Maya: There's now a helpful new video guide showing how to install Windows Subsystem for Linux on Windows 10.

Alex: That’s great because setting up a UNIX-like shell on Windows is often a roadblock for beginners.

Maya: Exactly. The video makes that less intimidating. They also numbered the course modules on the sidebar.

Alex: Organizing content visually helps students get a clearer roadmap of what they need to learn next.

Maya: In addition, guidance was added on how students can obtain and use their OpenAI API keys for LLM work.

Alex: That’s a practical addition to ensure learners can get hands-on experience with LLM APIs without confusion.

Maya: And they're reminding students that the 'llm cmd' feature requires installing the plugin first. Little clarifications like this save a lot of frustration.

Alex: Speaking of LLMs, let's talk about the exciting updates in the large language model evaluations.

Maya: Anand’s team added a detailed article and interactive webpage on "Dealing with Hallucinations by Double-checking" LLM responses.

Alex: Hallucinations are when LLMs confidently provide wrong info, so this approach is about running queries through multiple models.

Maya: Right, by cross-checking predictions from different LLMs and reviewing disagreements, you can drastically cut error rates.

Alex: What surprised me is the math: Two models double-checking reduces errors from about 14% to roughly 4%, with 87% automation saved.

Maya: And adding more models improves accuracy further but with diminishing returns – it's about balancing effort and error risk.

Alex: The fascinating insight is that errors made by different LLMs are mostly independent, so relying on multiple 'unreliable' models makes the system very reliable.

Maya: They even dropped a consistently poor model to keep quality high – shows the importance of monitoring model performance in ensembles.

Alex: Plus, the article includes code and a dataset to reproduce these findings. Transparency and reproducibility matter!

Maya: Also, an image illustrating how effort increases roughly linearly with more models but error diminishes towards zero was added for clarity.

Alex: This is a perfect example of using multiple imperfect tools together to get a near-perfect result. Human reviews only slip in when models disagree, saving lots of time.

Maya: Now, switching gears, there's a major breakthrough in the Retrieval Augmented Generation (RAG) project relying on Google Cloud SQL.

Alex: Yes! They revamped the backend code to use Python 3.13, with asyncpg managing a Postgres DB enhanced with a vector search extension.

Maya: This vector search enables embedding-based similarity lookups, combined with classic text search for efficient hybrid retrieval.

Alex: What’s brilliant is the design of a hybrid_search function mixing TF-IDF style text relevance and cosine similarity on embeddings.

Maya: This mix helps capture relevant documents even when keywords don’t match exactly but the meaning is similar.

Alex: There's a detailed setup guide with Google Cloud CLI commands to configure the database and indexes, even a hybrid scoring function written in SQL.

Maya: The FastAPI app supports uploading chunks of text, generates embeddings with OpenAI API, stores them, and queries with that hybrid method.

Alex: They even added an answer endpoint that fetches relevant chunks and prompts an LLM to create grounded answers citing source text.

Maya: Plus, there’s a thorough README on deploying this as a Cloud Run service with full local testing instructions. Impressive end-to-end design.

Alex: I love how well it integrates modern vector search with familiar Postgres infrastructure.

Maya: They also improved the Docker setup, upgraded dependencies, and tweaked code style for better maintainability.

Alex: Lastly, the AI Pipe project got a nice update.

Maya: Yeah, they enabled full support for OpenAI embeddings API via the AI Pipe proxy.

Alex: That means you can call OpenAI embedding endpoints through AI Pipe, keeping usage within budget and tracking costs.

Maya: Plus, they improved headers sent to OpenRouter so it can identify the app source, helping monitor usage better.

Alex: The README got more examples, showing how to set `OPENAI_API_KEY` and `OPENAI_BASE_URL` to use AI Pipe from curl or the `llm` CLI.

Maya: Their test suite was expanded to verify embedding API requests and cost calculations too. Robust testing is always a plus.

Alex: So, a tip for listeners: If you’re juggling multiple LLM models, try incorporating double-checking in your workflows to catch hallucinations early.

Maya: Exactly! Alex, how would you apply that in your projects or daily coding?

Alex: I'd run critical queries through two or more models and only flag for review when they disagree. It’s a smart shortcut to higher accuracy without excessive manual checks.

Maya: That’s a great approach! Remember, small tweaks like double-checking and organizing learning paths can have big impact.

Alex: And don’t forget to explore and optimize your tooling options—they often pay off.

Maya: That’s all for this week on Anand’s Weekly Codecast.

Alex: See you next time!