## Upgraded LLM Math Displays, Data Science Tools, and WhatsApp Thread Views

This week brings slicker data tables, expanded AI course content, handy WhatsApp utilities, and richer tools setup. It’s a roundup of upgrades that make data science, coding, and message scrapes more insightful and usable.

### [sanand0/llmmath](https://github.com/sanand0/llmmath)

_LLM multiplication results got a style and info refresh for clearer insights and easier reading._

- **Rich interactive tables:** The main page now shows model scores with right-aligned text and color-coded backgrounds from red to green for easy accuracy spotting, thanks to a concise rewrite split into a modular `script.js` ([09d3ac6](https://github.com/sanand0/llmmath/commit/09d3ac6d47e1c840fe110a7d8512008f5d986618)).
- **Popover details:** Hover cells reveal numbered lists of all model responses or errors for each multiplication, offering more transparency on how LLMs answered.
- **Accurate stats counting:** Multiplications now run five times each, improving stats fidelity and overall accuracy calculations ([f9cc4c5](https://github.com/sanand0/llmmath/commit/f9cc4c5d3aa7335f0810cbd5c699db576112b179)).
- **Clear column renaming:** The first column is now “Model” instead of a vague “m”, and the “%Win” cell disables wrapping for neater tables.
- **Minimal and modern code:** Uses ESM imports from D3, and bootstrap popovers for UX; the overhaul makes the script concise, readable, and visually crisp.

Yes, you really needed another level of polish on LLM math tables!

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_The official IITM Tools in Data Science course content receives timely updates and important clarifications._

- **Expanded teaching assistants roster:** Added two new TAs to the README, helping you get more hands-on support during the course ([066078b](https://github.com/sanand0/tools-in-data-science-public/commit/066078be7c1b2ac3f61f24a8925a048130a89cb9)).
- **LLM Agents content introduced:** Added comprehensive lecture notes and code for building autonomous agents that intelligently reason, act, and learn—demonstrated by a command-line Python agent executing code on your behalf ([8e93540](https://github.com/sanand0/tools-in-data-science-public/commit/8e935405d7f1a000bd11db34874d1d8265eec03f)).
- **Project 1 points fixed:** Content links now point to the correct Jan 2025 term materials, reducing confusion ([890689c](https://github.com/sanand0/tools-in-data-science-public/commit/890689c629972cfd505da2ae2de4e75772fd3b90)).
- **Improved learning workflow:** Rewrote example commands to use correct LLM CLI flags, promoting smoother hands-on experience ([720e4bd](https://github.com/sanand0/tools-in-data-science-public/commit/720e4bd002e3738cd5f81d5c723cbb2b16858ee8)).
- **Prettier reformat:** Project 1 documentation reformatted for better readability ([27562d8](https://github.com/sanand0/tools-in-data-science-public/commit/27562d8413a5efe5b659a4977187e233d7fe65cd)).

Turns out some AI agent tutoring is exactly what you needed for your data science hustle.

### [sanand0/tools](https://github.com/sanand0/tools)

_WhatsApp scraping and viewing gains new tools for deeper chat analysis._

- **WhatsApp scraper bookmarklet added:** Open any chat and capture the entire message log as JSON, including quoted messages for context. Copy it straight to clipboard for archiving or analysis ([9af824b](https://github.com/sanand0/tools/commit/9af824b38e0c4db57eed0f7547a99b2f2a3de002)).
- **WhatsApp thread viewer:** Paste scraped JSON into this new tool to see messages in neat threaded conversations, revealing reply hierarchies and quoted replies (perfect for untangling long chats) ([4535667](https://github.com/sanand0/tools/commit/453566794ab696b9c0bcfa9d21dc945d656ba760)).
- **Refined scraper:** The scraper nicely extracts quoted author names, message IDs, and handles system messages cleanly, improving accuracy for the viewer ([5c05948](https://github.com/sanand0/cyborg-scraping/commit/5c05948588afecc6e1943fe8017325a3f0072190) + [bf34a72](https://github.com/sanand0/cyborg-scraping/commit/bf34a72d34f1888cf77d38c99df487e412243b67)).
- **Cyborg Scraping archive:** The old scrapers repo now points users to the tools repo with better bookmarklets, paving the way forward ([ce157d9](https://github.com/sanand0/cyborg-scraping/commit/ce157d99accb5809144afc58d254417d4ec216a6)).
- **UI finesse:** Fixed bookmarklet title spacing for cleaner appearance ([cdeaf62](https://github.com/sanand0/tools/commit/cdeaf62f8d51e5c237360a257bbe221f54d28170)).

You never thought WhatsApp threads could look this organized, did you?

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Shell setup and productivity tweaks smooth daily coding life._

- **Conda prompt removed:** Simplified prompt by ditching unused Conda environment indicator ([897a96c](https://github.com/sanand0/scripts/commit/897a96cbaad325ae1b7da581e4eaf1f4bdac7d3b)).
- **Fish shell setup cleaned:** Migrated node version manager and lmstudio to main Fish setup. Also added Google Cloud SDK to path for easy CLI usage ([897a96c](https://github.com/sanand0/scripts/commit/897a96cbaad325ae1b7da581e4eaf1f4bdac7d3b)).
- **Fixed variable names in `chars` script:** Avoid confusion by clearly using distinct names for line content and line number ([98e52b8](https://github.com/sanand0/scripts/commit/98e52b8a25971d65efc36f4eb5b2ccc7ed49e67f)).
- **Markdown converter `md2html` upgraded:** Uses GitHub Flavored Markdown with extensions like bracketed spans, fenced divs, subscripts, and superscripts for richer HTML output ([4a8c6c0](https://github.com/sanand0/scripts/commit/4a8c6c0a8c1aef3e558a515e40516291a224fa15)).
- **Linux setup updated:** Added new apps like Opera, ffmpeg, w3m, Google Cloud SDK, PostgreSQL, Supabase, VLC, and Ollama models in setup doc ([897a96c](https://github.com/sanand0/scripts/commit/897a96cbaad325ae1b7da581e4eaf1f4bdac7d3b)).

Less clutter, more power in your terminal. Ah, the sweet smell of effective scripts.

### [sanand0/llmentityextractor](https://github.com/sanand0/llmentityextractor)

_Entity extraction API polished with better docs and smoother deployment._

- **Secure token handling:** Moved LLMFOUNDRY API token from request header to Cloudflare environment variable, simplifying authorization ([5e431e5](https://github.com/sanand0/llmentityextractor/commit/5e431e5119d368c11e40d45890a28cba4ea3e650)).
- **Expanded README:** Added detailed deployment instructions, live curl examples with expected JSON outputs, and Swagger UI docs introduction for easier developer onboarding ([97ae7be](https://github.com/sanand0/llmentityextractor/commit/97ae7be8e8da2d70ef9c19a973170b6e17d2b4b5), [e10d936](https://github.com/sanand0/llmentityextractor/commit/e10d9365100818757e76e48ff7fea8eb02e84bce)).
- **Interactive Swagger UI:** Hosted Swagger UI directly within the worker, letting you explore API docs visually at `/docs` ([97ae7be8](https://github.com/sanand0/llmentityextractor/commit/97ae7be8e8da2d70ef9c19a973170b6e17d2b4b5)).
- **Updated worker code:** Improved code structure for handling CORS, extracting JSON, and serving docs, with neat error handling and consistent responses ([e10d936](https://github.com/sanand0/llmentityextractor/commit/e10d9365100818757e76e48ff7fea8eb02e84bce)).

JWT tokens are so last year – environment variables FTW!

### [sanand0/sanand0.github.io](https://github.com/sanand0/sanand0.github.io)

_A personal repo portfolio enhanced with better repo link handling and topic filtering._

- **Fixed repo footer links:** Cards now link correctly to repo main pages, while clicking card bodies opens homepages if available ([8f972d1](https://github.com/sanand0/sanand0.github.io/commit/8f972d15cb22408d823d915d7b40bda6aec2bb42)).
- **Show repos without topics:** Previously hidden repos with no topics are now displayed under an “(other)” category to avoid confusion ([9a42c9c](https://github.com/sanand0/sanand0.github.io/commit/9a42c9c622f3cc3af90a4d732937cf9682e9fa83)).

A portfolio repo that finally stops playing hide-and-seek.

## Suggested Next Steps

- Capture and share a screencast demo of the new LLM multiplication table UI to showcase its slick new visuals.
- Develop a tutorial video on building and deploying the LLM command-line agent from the new tools-in-data-science material.
- Write a blog post guiding on how to scrape and visualize WhatsApp threads using the new scraper and thread viewer tools.
- Explore automating your shell environment updates with scripts that integrate the updated Fish and bash setups from `scripts`.
- Add more interactive examples in the entity extractor Swagger UI to attract developer users and get feedback.
