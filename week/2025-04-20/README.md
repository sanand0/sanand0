## Big Visuals, Smooth AI Flows, & Admin Power in APIs

A week of immersive data storytelling, neat AI-powered coding tools, and fresh backend features to power your AI apps.

### [antipodes](https://github.com/sanand0/antipodes)

Show exactly where you'd dig if you tunneled through Earth, fine-tuning the map for tricky countries and sharing key insights.

- **Fixed and enhanced GeoJSON links:** Updated the README with precise links to [geojson.io visualization](https://geojson.io/#data=data:text/x-url,https%3A%2F%2Fraw.githubusercontent.com%2Fsanand0%2Fantipodes%2Frefs%2Fheads%2Fmain%2Fantipodal_ocean.geojson) for interactive maps ([0bc0e24](https://github.com/sanand0/antipodes/commit/0bc0e2461c5b90736655a12cd439d781d138034e), [1be41a3](https://github.com/sanand0/antipodes/commit/1be41a3a3177a3dd4bf8540a646a85f7b794f88a)).
- **Added output GeoJSON to repo:** Removed `.geojson` from .gitignore ensuring antipodal ocean data is tracked ([1be41a3](https://github.com/sanand0/antipodes/commit/1be41a3a3177a3dd4bf8540a646a85f7b794f88a)).
- **Shared key learnings:** Explained why you should "ask for output, not code," warned about edge cases (like countries straddling prime meridian), and praised mature geospatial tools like [fiona](https://pypi.org/project/fiona) and [shapely](https://pypi.org/project/shapely/) for concise computations ([7165261](https://github.com/sanand0/antipodes/commit/7165261412c7e087c7a28fd3d865f2ae811816f0)).

Yes, discovering countries’ Earth's flip-sides was _that_ tricky.

### [aipipe](https://github.com/sanand0/aipipe)

The backend gatekeeper: API key sharing, usage tracking, and now some shiny admin-only controls.

- **Added Admin APIs & Permissions:** Admins can now view all users' usage (`GET /admin/usage`) and generate JWT tokens for any user (`GET /admin/token?email=…`). The server blocks non-admins from these endpoints ([2174d40](https://github.com/sanand0/aipipe/commit/2174d405e407d057b85ee4e418733263f7ccaf9b)).
- **Enable cost overwrites via POST:** Admins can set or correct daily costs per user for precise billing via `POST /admin/cost` with `{email,date,cost}` body ([3ad673f](https://github.com/sanand0/aipipe/commit/3ad673f6c215b2a73b634c16d57fcfab10622c35)).
- **Refined cost calculation and token management:** Fixed token salt handling and cost computations for OpenAI models to reflect accurate charges ([3ad673f](https://github.com/sanand0/aipipe/commit/3ad673f6c215b2a73b634c16d57fcfab10622c35), [b8faba6](https://github.com/sanand0/aipipe/commit/b8faba6dd52866bf74e96f934db131813a1df98b)).
- **Improved JS utils & request logic:** Utility functions for headers management and CORS added; requests now properly filtered and forwarded ([src/utils.js](https://github.com/sanand0/aipipe/commit/2174d405e407d057b85ee4e418733263f7ccaf9b#diff-...), [src/worker.js](https://github.com/sanand0/aipipe/commit/2174d405e407d057b85ee4e418733263f7ccaf9b#diff-...)).
- **Extensive testing:** Added admin API tests verifying authorized/unauthorized access, token generation, usage retrieval, and cost overwriting ([test/test.js](https://github.com/sanand0/aipipe/commit/2174d405e407d057b85ee4e418733263f7ccaf9b#diff-...)).

Because behind every smooth front-end LLM call, there's an admin waving the budget wand.

### [autoimprove](https://github.com/sanand0/autoimprove)

Build web apps that get _better, and better, and better..._ all thanks to persistent LLM upgrades.

- **Added stunning animated SVGs:** Now experiment with dynamic cosmic explosions with swirling, pulsing lines and sparks—all generated and highly improved step-by-step by GPT-4.1 Nano ([33c4d98](https://github.com/sanand0/autoimprove/commit/33c4d980ddc334cbc5b489b3096f53e4b1a5e04c)).
- **Revised README and demos:** Smoother introduction and deeper observations of LLM-driven improvements including detailed app evolution and shimmering new ideas ([be9cbd6](https://github.com/sanand0/autoimprove/commit/be9cbd67e142a7a3d411146060b34a95476728aa), [c8be007](https://github.com/sanand0/autoimprove/commit/c8be0071641d79d34dde0733a9f83db5ed1fdb36)).
- **Upgraded demos:** Interactive fractals, particle systems, shapes, clocks, and dashboards enhanced dramatically, exploring advanced visual and UX styles—all scripted and improved by focused AI prompts.
- **Configured app list and metadata:** Replaced old demo paths with current app JSONs and icons for a sleek, easy-to-browse interactive showcase ([config.json](https://github.com/sanand0/autoimprove/commit/c8be007...)).

LLMs impressed by adding sparkly animated SVGs and cosmic chaos. So of course, that’s a thing now.

### [eliminationgame](https://github.com/sanand0/eliminationgame)

LLMs playing “Survivor” with cutthroat drama — visualized, detailed, and insightful.

- **Full blog-style rewrite:** Documented progress and lessons in a detailed guide. Shared key takeaways from using LLMs for design, ideation, prototyping, and coding ([88e6892](https://github.com/sanand0/eliminationgame/commit/88e68928af3b63febb375cf3bdd54b13e511ac17)).
- **Scaffolded navigation & timeline:** Created a clean navbar and timeline interface with URL sync for step-based viewing ([50a377b](https://github.com/sanand0/eliminationgame/commit/50a377b)).
- **Data structure planning:** Designed a comprehensive timeline-of-snapshots model to keep game state and events clear and easy to render ([22b6035](https://github.com/sanand0/eliminationgame/commit/22b6035)).
- **Alliances & Voting tables:** Rendered concise, color-coded tables using Bootstrap classes and badges; handled active and eliminated player visual states to clarify alliances and votes ([bcc4b32](https://github.com/sanand0/eliminationgame/commit/bcc4b32), [75206f9](https://github.com/sanand0/eliminationgame/commit/75206f9)).
- **Chat messaging:** Rendered dynamic, elegant chat histories for all conversation types with tooltips and structured formatting, improving clarity and engagement ([9903e9f](https://github.com/sanand0/eliminationgame/commit/9903e9f)).
- **Enhanced UI & stage visualization:** Refined the game stage with well-placed player circles, model labels, action arrows with meaningful colors, and a central message panel with elegant wrapping ([91e001b](https://github.com/sanand0/eliminationgame/commit/91e001b), [a36f65a](https://github.com/sanand0/eliminationgame/commit/a36f65a), [17d3217](https://github.com/sanand0/eliminationgame/commit/17d3217)).
- **Polished with manual tweaks:** Adjusted arrow positioning, player opacity on elimination, clickable chat to navigate steps, and final presentation refinements for a smooth user experience ([5888294](https://github.com/sanand0/eliminationgame/commit/5888294), [5eb607f](https://github.com/sanand0/eliminationgame/commit/5eb607f), [fd8bb7e](https://github.com/sanand0/eliminationgame/commit/fd8bb7e)).

Yes, let AI drama unfold on screen faster than real TV — Octagon ready!

### [scripts](https://github.com/sanand0/scripts)

Your machine’s workflow ninja with the usual tweaks for smooth Unix touch.

- **Switched back to X11 from Wayland:** Updated docs to reflect defaulting from Wayland to X11 due to Wayland issues with tools like rofi and autokey, plus refined 4-finger gesture commands and notes ([96df53a](https://github.com/sanand0/scripts/commit/96df53a283705a1c9f1a205dfe224d54af3767d0)).

Sometimes the fancy new tech is just a tease, and simple X11 still rules.

### [llmviz](https://github.com/sanand0/llmviz)

See your LLM chat’s wild hallucinations laid out in colorful token form.

- **Switched to GPT 4.1 Nano & aipipe API:** Updated code to fetch using AI Pipe tokens for secure, streamlined embedding and switched system prompt to none for pure model output ([c37e646](https://github.com/sanand0/llmviz/commit/c37e64627c2abb78ed28bed0981e1bbc7014b329)).
- **Simplified interface:** Removed old system message prompt and adjusted UI for simplified user input, supporting transparency on token selection and probabilities.

Hallucinations don't stand a chance when you map their every pixel.

### [sanand0.github.io](https://github.com/sanand0/sanand0.github.io)

Another round of freshness for the homepage’s tools showcase.

- **Auto refresh every Sunday:** Added scheduled GitHub Actions trigger to update repos weekly without fuss ([203d79f](https://github.com/sanand0/sanand0.github.io/commit/203d79f24be9ac92aae0a60576602b47f7454d63)).
- **Stars & improved links:** Joined repo stargazers with links targeting homepage URLs where available, giving a cleaner, more appetizing look to the project cards ([af809b1](https://github.com/sanand0/sanand0.github.io/commit/af809b146fa0372e4da547c920c9b7d27d00de2d), [9924a01](https://github.com/sanand0/sanand0.github.io/commit/9924a01d9118f5cd6db8f1130d42a7ef97c34d7e)).
- **Show repos grouped by topic:** Added a new script to load, group, and display public repos by topic with collapsible sections and date-sorted entries for better discovery ([0932f2e](https://github.com/sanand0/sanand0.github.io/commit/0932f2efe3ad6c950c20b2ed7534ef27d8fff304), [update.js](https://github.com/sanand0/sanand0.github.io/commit/update.js) new file).

Now it’s easier to find your favorite repo hiding in plain sight.

### [jinjaauth](https://github.com/sanand0/jinjaauth)

Securely serve Jinja2 templates with Google sign-in, cleaned up for easier usage.

- **Convert.py cleanup:** Stop copying `app.py` during static HTML conversion to Jinja since `uv` runtime uses the raw URL. Use `uv run` with raw GitHub URLs for latest versions ([2939079](https://github.com/sanand0/jinjaauth/commit/2939079ced349e9d448832822ccbca4b43bbf65c), README update).
- **CLI clarity:** Highlight running conversion and app with uv via direct URL calls now recommended for ease.

Hosting private HTML just got simpler & a little less spooky.

## Suggested Next Steps

- Test the new [admin APIs in AIPipe](https://github.com/sanand0/aipipe) on your instance. Perfect for you if you want fine-grained cost control.
- Play with the [autoimprove](https://github.com/sanand0/autoimprove) animated SVG experiments; try tweaking the prompts with latest GPT-4.1 Nano.
- Dive into the [eliminationgame](https://github.com/sanand0/eliminationgame) visualization source and fork your own LLM-driven social drama with the modular data structure.
- Consider showing your machine workflow setup from `scripts` to a friend — trust us, going back to X11 has its perks.
- Experiment with `llmviz`’s new GPT-4.1 Nano logs to understand exactly how your LLM is hallucinating or not.
- Update your personal site home repo display with the new topic grouping and star count — it’s a nice touch!
- For website security demos, try the latest [jinjaauth](https://github.com/sanand0/jinjaauth) with uv URL runs for fastest feedback.
