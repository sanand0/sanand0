## A Week of Smarter AI Tools, Visual Storytelling, and Cleaner Workflows

This week’s updates polish AI-driven coding workflows, simplify diagramming in presentations, and tidy up your shell setup. Plus, a sleek browser bookmarklet generator helps you rewrite text on the fly with AI.

### [marked-smartart](https://github.com/krishna-gramener/marked-smartart)

_Turn your Marp slides into eye-catching SmartArt presentations with pyramids, chevrons, and Venn diagrams all blended into one simple syntax._

- **Unified Marp plugin:** Merged separate diagram plugins into a single `smartart-plugin.js` using modular JS modules for pyramid, chevron, and Venn diagrams ([4c219fe](https://github.com/krishna-gramener/marked-smartart/commit/4c219fe)). Your markdown stays cleaner, and future updates get easier.
- **Rich styling & embedding:** Configure width, height, font size, and colors directly in markdown blocks, with HTML content support inside shapes for custom looks ([README examples](https://github.com/krishna-gramener/marked-smartart/blob/4c219fe73c10fee3f464f891ed4515b4c884bf40/tests/smartart-demo.md)).
- **Web UI to preview slides:** A new frontend app lets you input markdown and instantly see your Marp slides rendered with these diagrams—all done in browser with web containers ([index.html](https://github.com/krishna-gramener/marked-smartart/blob/4c219fe73c10fee3f464f891ed4515b4c884bf40/index.html), [script.js](https://github.com/krishna-gramener/marked-smartart/blob/4c219fe73c10fee3f464f891ed4515b4c884bf40/script.js)).
- **Modern JS syntax:** Switched to ES modules and import/export syntax for cleaner, more maintainable code across all diagram processors ([pyramid.js](https://github.com/krishna-gramener/marked-smartart/blob/4c219fe73c10fee3f464f891ed4515b4c884bf40/pyramid.js)).
- **Automated presentation tests:** Added comprehensive markdown + HTML test cases for all diagrams to spot regressions and share usage examples.

Because your Marp slides _insist_ on being more colorful and interactive. Yes, another reason to outshine that tedious slideshow next week!

### [rewriter](https://github.com/sanand0/rewriter)

_Create personalized AI-powered bookmarklets that rewrite selected text on any website, making your writing smoother and clearer instantly._

- **Complete UI makeover:** Dramatically simplified and modularized the bookmarklet generator; replaced FontAwesome with Bootstrap Icons; trimmed CSS in favor of Bootstrap classes ([dd20d34f](https://github.com/sanand0/rewriter/commit/dd20d34f8d3cf72095a7a73ce112b9750704131f)).
- **Use case cards:** Added curated clickable examples like “Sales Email Enhancer” and “Tech Doc Simplifier” that instantly fill in prompts and instructions for quick setup ([index.html](https://github.com/sanand0/rewriter/blob/dd20d34f8d3cf72095a7a73ce112b9750704131f/index.html)).
- **Persistent API config:** Saved API Base, Key and Model in localStorage for easy reuse; added test connection button with loading and success/error feedback ([index.html](https://github.com/sanand0/rewriter/blob/dd20d34f8d3cf72095a7a73ce112b9750704131f/index.html)).
- **Smooth prompt filling:** Clicking a use-case card updates form fields smoothly with highlight animations and scroll, making workflow more delightful.
- **License & docs:** Added clean MIT license and a thorough README explaining setup, use cases, real-world benefits, and developer instructions ([README.md](https://github.com/sanand0/rewriter/blob/dd20d34f8d3cf72095a7a73ce112b9750704131f/README.md)).

If your emails aren’t shiny enough yet, this AI-powered polish tool is your new best friend. Because every browser needs a magic wand.

### [scripts](https://github.com/sanand0/scripts)

_Sharper shell setup and utilities to speed up your coding, AI tool usage, and Linux/Windows integration._

- **Fish shell improvements:** Switched `.env` loading to use `source` for compatibility with Fish and Bash shells, simplifying environment management ([3382754](https://github.com/sanand0/scripts/commit/33827542abd75497b6ed57efabb77d1422a1160e)).
- **Abbreviations for common tools:** Added convenient abbreviations for mail, calendar tools (e.g., `cmdg`, `gcalcli`), and new CLI utils like `md2rtf` to convert markdown to RTF via clipboard ([fe7f63b](https://github.com/sanand0/scripts/commit/fe7f63bc930f9ec26f6bd4f224ee2b4af8864b4d)).
- **Linux setup fixes:** Reverted remote debugging to use X11 instead of Wayland for better compatibility; updated QuickShot and other utilities; tweaked gesture shortcuts for media control and window navigation ([96df53a](https://github.com/sanand0/scripts/commit/96df53a283705a1c9f1a205dfe224d54af3767d0)).
- **Enhanced command aliases:** Replaced slow Fish functions with abbreviations for performance gain; moved tmux mouse mode to `.tmux.conf`; improved code style guides in README to boost AI code generation accuracy ([90d34b7](https://github.com/sanand0/scripts/commit/90d34b7239197d69c3502d1e847b79dd503c1b72)).
- **Utility expansion:** Added alias for `datasette` CLI and updated LLM model default instructions for smoother AI interactions.

Yes, you didn’t know you needed `md2rtf` in your life — until you did.

### [llmmath](https://github.com/sanand0/llmmath)

_An informal but fascinating look at how well large language models multiply big numbers — revealing surprising reasoning strategies._

- **Documentation polish:** Clarified the question list, improved formatting, and restructured reasoning explanations for easier reading ([211341ea](https://github.com/sanand0/llmmath/commit/211341eace5081b87b5aa56e99c0c65f0e370e4e)).
- **Added OpenAI API instructions:** Reminded users to set up their OpenAI key along with OpenRouter keys for running evaluations smoothly ([3d56261](https://github.com/sanand0/llmmath/commit/3d5626118729782625a21515342ff32827e85fd7)).
- **Updated web interface:** New user-friendly index page highlights key results — OpenAI’s reasoning models scored 6 out of 7, others varied widely, with detailed mental math traces included ([index.html](https://github.com/sanand0/llmmath/commit/211341ea)).
- **Showcased reasoning strategies:** Noted that top models used human-like decomposition methods, breaking down multiplications stepwise instead of direct brute computation.
- **Broad model coverage:** Evaluated 50 LLMs including OpenAI, Gemini, Anthropic, DeepSeek, Google, Amazon, and Meta models, useful if you’re curious which AI can handle math best.

Impress your friends: “My AI can multiply bigger numbers than your calculator. Probably.”

### [sanand0.github.io](https://github.com/sanand0/sanand0.github.io)

_Find your favorites faster: now with daily refresh and topics-based repo grouping for improved browsing._

- **Switched to daily updates:** Auto-deploy workflow now triggers every day for fresher repo data ([2a70836](https://github.com/sanand0/sanand0.github.io/commit/2a708364cf12d08651ed3a1153174c5fa31e1b6b)).
- **Dynamic topic groups:** Introduced an accordion sidebar to filter repos by their topics (like “llm”, “tool”, etc.) for faster discovery ([update.js](https://github.com/sanand0/sanand0.github.io/commit/update.js)).
- **Enhanced repo cards:** Repos now display dates created/updated and star counts; they can be filtered by topic, last updated, and creation date with handy counts shown next to each filter.
- **Modern responsive layout:** Sidebar with sticky filters and grid repo cards elegantly adapt to screen sizes for mobile and desktop use.
- **Cleaned index.html:** Replaced outdated static HTML with a refined template serving dynamic repo lists and filtering UI.

Less digging, more finding — yes, your next project is hiding... somewhere here.

## Suggested Next Steps

- Try creating a engaging Marp presentation with unified SmartArt diagrams. Show off your pyramid, chevron, and Venn skills.
- Generate and install a Rewriter bookmarklet for your daily writing polish — sales, support, or just general finesse.
- Test the revamped shell setups from scripts on your Linux or Mac machine for a smoother, faster terminal experience.
- Explore LLMMath’s surprising model behaviors; maybe share the clever mental math tricks from OpenAI’s top machines.
- Update your personal homepage with the latest topic-driven repo organization, making sure visitors find your gems easily.
- Keep an eye on evolving admin APIs in AI backend tools for better cost tracking and usage management in your projects.
