## AI Pipes, APIs, and New Tools: A Week of Streamlining and Exploration

This week’s work drove smoother user experiences with clearer APIs, smarter interfaces, and tools that think for themselves. The big theme: modular design and thoughtful user control beat bloat and magic.

### [sanand0/aipipe](https://github.com/sanand0/aipipe)

_User-friendly API proxying and playground scripting shine through modularity and bug fixes this week, making debugging and usage easier than ever._

- **Added robust HTTP proxy support** for any URL, bypassing CORS limits while preserving successful headers and removing duplicates safely ([7362846](https://github.com/sanand0/aipipe/commit/7362846)). No more CORS headaches for front-end apps! Takeaway: Proxies can be handy but need careful header hygiene to avoid issues.
- **Refactored playground JavaScript into a dedicated ES module** to keep code clear and maintainable ([d95f2bd](https://github.com/sanand0/aipipe/commit/d95f2bd)). The UI now feels snappier and less cluttered. Takeaway: Splitting UI logic into modules prevents monolithic scripts that challenge future updates.
- **Enforced linting automatically before publishing** to catch style and syntax glitches early ([c3b639d](https://github.com/sanand0/aipipe/commit/c3b639d)). Clean code is happy code! Takeaway: Automating style checks improves consistency and long-term maintenance.
- **Improved token profile extraction** by fixing a subtle bug with URL query param counting ([d95f2bd](https://github.com/sanand0/aipipe/commit/d95f2bd)). This prevents losing other URL parameters after login. Takeaway: Even simple utilities deserve thorough testing.
- **Introduced detailed automated tests for proxy functionality** covering timeouts, header stripping, CORS, and error cases ([test/test.js](https://github.com/sanand0/aipipe/blob/main/test/test.js)). Tested code is trustworthy. Takeaway: Capturing edge cases prevents surprising failures later.

### [sanand0/apiagent](https://github.com/sanand0/apiagent)

_APIs speak naturally now with smarter retry controls and expanded Google Workspace integration, making data easy to ask for and act on._

- **Built a configurable retry mechanism for conversations**, letting users set how many attempts to make before stopping or continuing via a button ([fa17aa5](https://github.com/sanand0/apiagent/commit/fa17aa5)). More control means fewer dead ends in tricky API calls. Takeaway: Expose retry logic to users for better error handling.
- **Added a “Continue” button after max attempts** to allow manual conversation extension, improving UX when complex queries need extra tries ([fa17aa5](https://github.com/sanand0/apiagent/commit/fa17aa5)). Takeaway: Sometimes user patience beats automation.
- **Integrated Google Workspace APIs with OAuth support**, enabling interactions with Gmail, Calendar, and Drive seamlessly ([5ef1dcf](https://github.com/sanand0/apiagent/commit/5ef1dcf)). Now you can query email or calendar data as naturally as asking a friend. Takeaway: OAuth on demand beats upfront overhead.
- **Lazy loads Google OAuth client script and binds sign-in button dynamically** to avoid unnecessary load if unused ([b425825](https://github.com/sanand0/apiagent/commit/b425825)). Efficient resource loading helps page performance. Takeaway: Load code only when needed.
- **Persisted form token inputs securely and restored them** on page reload for a smoother authentication experience ([90b2ee9](https://github.com/sanand0/apiagent/commit/90b2ee9)). Takeaway: Saving tokens behind the scenes is a user time-saver.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Tiny utilities got trimmed and tuned, now they save more dynamic form states and convert one-liners faster — a little cleanup with big time savings._

- **Added an “unbrace” Fish abbreviation to remove braces from simple JS blocks** with a jscodeshift transform, trimming verbosity in common coding patterns ([223d1ff](https://github.com/sanand0/scripts/commit/223d1ff)). Yes, you really needed another Fish abbr. Takeaway: Micro-optimizations compound daily.
- **Fixed dynamic form saves to preserve values of removed fields** by merging stored data with current inputs on save ([3191125](https://github.com/sanand0/scripts/commit/3191125)). Form values persist even if DOM changes! Takeaway: Don’t lose state when UI elements dynamically appear and disappear.
- **Enhanced AI coding style rules** with practical advice: favor deduplication over modularity, keep configs in separate files, place least-used code at the bottom — very librarian of you! ([764c177](https://github.com/sanand0/scripts/commit/764c177)). Takeaway: Readers appreciate well-ordered, purposeful code.
- **Added handy ‘ascii’ abbreviation to convert Unicode to ASCII** using anyascii via a one-liner Pipeline ([5ea8493](https://github.com/sanand0/scripts/commit/5ea8493)). Great for sanitizing pasted text from ChatGPT outputs. Takeaway: Small tools increase command line mojo.

### [sanand0/tools](https://github.com/sanand0/tools)

_Another batch of nimble single-page apps enhanced—speak text, extract hacker news links, and explore Google suggestions with AI-powered magic._

- **Launched SpeakMD**, a tool to convert Markdown into conversational narration scripts with live streaming of AI output and read-aloud support ([9c7ccac](https://github.com/sanand0/tools/commit/9c7ccac)). Turn dry docs into something you’d actually want to hear. Takeaway: AI + audio accessibility is the new reading.
- **Added Google Suggest Explorer** displaying localized search autocomplete results and generating witty AI insights across countries ([66c296f](https://github.com/sanand0/tools/commit/66c296f)). Now you can see how the world Google-searches differently. Takeaway: Data visualization + humor = irresistible.
- **Refactored Google Suggest app’s JS for clarity and reusability**, encapsulating common patterns like JSONP calls, cache management, and UI updates into clean functions ([39b4cfb](https://github.com/sanand0/tools/commit/39b4cfb)). Code quality boosts future feature speed. Takeaway: Modular code is readable code.
- **Implemented a Hacker News Links Extractor** producing Markdown lists of news article URLs with proper filtering and link text extraction ([9cc834e](https://github.com/sanand0/tools/commit/9cc834e)). Perfect for quick content curation. Takeaway: Extract useful nuggets automatically.
- **Sanitized HTML outputs across tools with DOMPurify** to prevent injection issues ([a66b053](https://github.com/sanand0/tools/commit/a66b053)). Make XSS vulnerabilities a thing of the past. Takeaway: Safety first, even on sandboxed pages.

### [sanand0/aws-rag](https://github.com/sanand0/aws-rag)

_Your personal RAG system just grew up: a unified CLI and FastAPI app with hybrid search and smart text chunking on fast OpenSearch clusters._

- **Implemented a mature RAG-aware system combining CLI commands and API endpoints** with document chunking, vector indexing, and hybrid BM25+k-NN search ([e26c4b0](https://github.com/sanand0/aws-rag/commit/e26c4b0)). Search your docs with semantic power! Takeaway: Unified interfaces improve user choice.
- **Added advanced query rewriting, sub-question breaking, and HyDE (Hypothetical Document Embeddings) for better recall** ([e26c4b0](https://github.com/sanand0/aws-rag/commit/e26c4b0)). Think AND retrieve, not just search. Takeaway: Break down complex queries for smarter results.
- **Incorporated comprehensive error handling with tracebacks** and detailed README instructions for local Docker testing and AWS deployment ([e26c4b0](https://github.com/sanand0/aws-rag/commit/e26c4b0)). Self-host with confidence. Takeaway: Good docs are the unsung hero of dev experience.
- **Used OpenSearch’s k-NN vector indexes with tuned parameters for fast, accurate retrieval** ([README](https://github.com/sanand0/aws-rag/blob/main/README.md)). Vector search is now standard, not special. Takeaway: Invest in good index settings early.

### [sanand0/llmevals](https://github.com/sanand0/llmevals)

_Prompt patterns put to the test: Reasoning nudges work slightly, but emotions and praise mostly don’t move the needle._

- **Added a public experiment showing that “think step by step” prompts help some models more than emotional or incentive-based ones** ([ecfe94f3](https://github.com/sanand0/llmevals/commit/ecfe94f3)). Facts > feelings for LLM math. Takeaway: Stick to logic, not drama, in prompting.
- **Collected detailed prompt-performance data across 40 LLMs and multiple styles** with significance testing (p~0.06 for reasoning effect) ([README](https://github.com/sanand0/llmevals/blob/main/emotion-prompts/README.md)). Data > anecdotes. Takeaway: Test your prompts, don't guess.
- **Shared summary analysis and example models that truly benefit from reasoning prompts**—some models even regress when “reasoning” is forced. Takeaway: No one size fits all, try before you buy prompt techniques.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_Personal weight transformation story now with polished page details and favicon — marrying narrative with data visualizations._

- **Added a site-wide favicon for polish and brand identity** ([aa079e06](https://github.com/sanand0/datastories/commit/aa079e06)). It’s the little things that tell users you care. Takeaway: Bless your site with favicon love.
- **Improved README text and consistency with clear plan updates** detailing successful fasting journey and prompt usage ([aa079e06](https://github.com/sanand0/datastories/commit/aa079e06)). Storytelling matters. Takeaway: Good docs engage readers emotionally.
- **Protected data viz HTML with a favicon for better browser UIs** ([aa079e06](https://github.com/sanand0/datastories/commit/aa079e06)). Takeaway: Make project URLs look trustworthy.

## Lessons

- **Refactor to clarity:** Splitting code into modules and small reusable functions pays off in easier maintenance and testing, even in front-end scripts.
- **User control boosts UX:** Adding options like retry counts or OAuth buttons loaded on-demand improves flexibility and responsiveness.
- **Don’t underestimate caching:** Cache keys and invalidation matter for interactive apps depending on API speed and cost.
- **Test discovered bugs:** Writing tests for both edge cases and everyday usage exposes hidden assumptions and avoids regressions.
- **Prompt experiment data > hype:** What feels persuasive or emotional may not move LLM output quality; logic guides wins quietly.

## Suggestions

- Measure the latency impact of the proxy improvements in aigpipe, and see whether further header tweaks or compression might help.
- Expand Google Workspace agent support with other Google APIs (Drive metadata, Docs, Sheets) to offer richer interactions.
- Extract common UI patterns from the various tool frontends (like loading states and error toasts) into a shared small library.
- Add user analytics (opt-in, privacy-first) to measure which prompt variants or tools are most used in the evals and apiagent projects.
- Perform a full audit and security review on all OAuth flows in apiagent to ensure tokens and redirects are tightly controlled.
- Add image and table read-aloud improvements to SpeakMD, such as inflection prompts or alternate voice characters.
- Consider baseline metrics for scripts loading times and test coverage gaps in new and legacy tools to identify bottlenecks.
- Integrate AWS RAG with a minimal front-end that supports new CLI commands and lets users visualize search history or ranking explanations.
