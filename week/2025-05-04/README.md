## Big Launches in AI Controls, Shell Tweaks, and Data Science Tools

This week brings polished diagram tools, smarter browser text rewrites, shell path smoothing, and detailed LLM math tests. Plus, upgrades to course content and deeper API support accelerated your AI and dev workflows.

### [scripts](https://github.com/sanand0/scripts)

Smooth out your Fish shell path and speed up Node.js usage with smarter setups.

- **Permanent PATH setup:** Replaced temporary `fish_add_path` with persistent Fish lines using `set -gx PATH "$PATH:<dir>"` for all script and virtualenv folders ([9481289](https://github.com/sanand0/scripts/commit/948128916eb35b28e806e4aaaa3db6c074dddaf4), 03 May 2025).
- **Run Node via fnm lazily:** Delayed Node.js environment loading by booting `fnm` only on demand via `abbr` commands for `node`, `npm`, and `npx`—cuts shell startup overhead ([4a34f07](https://github.com/sanand0/scripts/commit/4a34f0740c12cdfde4d9ed88719909e5f70e8395), 01 May 2025).
- **Add `micro` editor to Linux setup:** Switched default editor in shell setup to `micro` for a fast, modern terminal editor experience ([c384fa1](https://github.com/sanand0/scripts/commit/c384fa1261eca64445359cada02f83d65f031104), 01 May 2025).
- **Add `git-uncommitted` script:** New handy Bash script lists first-level directories that are not fully in Git, helping spot code not yet pushed ([a0eac90](https://github.com/sanand0/scripts/commit/a0eac900142116249fb73d36382479d9cd7ead7b), 01 May 2025).
- **Fix gcalcli agenda range:** Changed calendar agenda lookup to show 2 full days instead of 1, so you don't miss upcoming events ([be10e92](https://github.com/sanand0/scripts/commit/be10e92c0ae9752f9bc4e7f7ad5e6f1de6a364e3), 27 Apr 2025).

Yes, you really needed another Fish abbr trick to stop loading heavy shells early.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

Evolving course materials and detailed new modules prep you better for data science challenges.

- **LLM content expanded:** Added full notes on advanced image generation & editing APIs from Google Gemini 2.0 Flash and OpenAI's GPT Image 1, plus new TTS APIs from OpenAI and Gemini speech studio ([47cc884](https://github.com/sanand0/tools-in-data-science-public/commit/47cc884cae26689892b2ed8b5772de2b88f5ccfd), 03 May 2025).
- **Embrace open access:** Clarified that course content and evaluations are public, and anyone can audit them (though with restricted access to participation or certification) ([7b7682b](https://github.com/sanand0/tools-in-data-science-public/commit/7b7682b3554e47beca79316788b2cc5a6e890412), 01 May 2025).
- **Add GitHub Codespaces & Google Auth guides:** New practical tutorials on cloud-powered development and secure Google-based login for APIs ([c381021](https://github.com/sanand0/tools-in-data-science-public/commit/c3810212c50461474364c08c633bdef716c3f4b4), 29 Apr 2025).
- **Prepare May 2025 content:** Added new detailed modules on dbt for data transformation, AI-assisted code editing with GitHub Copilot, and more embedded LLM chapters ([0f7a01c](https://github.com/sanand0/tools-in-data-science-public/commit/0f7a01c83cd07292147430da268a53db024fda91), 28 Apr 2025).
- **Refine course schedule & links:** Updated timelines, Discourse discussion links for graded assignments, and cleaned up the overview ([fac16bd](https://github.com/sanand0/tools-in-data-science-public/commit/fac16bd9202c8681b45b314feceeb2cbc4df3a2b), 01 May 2025).

Anyone can audit this course—but please don't use the chat GPT answer key. Actually, who am I kidding? They do.

### [sanand0/llmmath](https://github.com/sanand0/llmmath)

How well do LLMs handle mind-boggling multiplications? Most can at least fake it to impress.

- **Added Grok 3 models:** Included x-ai's Grok 3 variants in testing, rounding out 50 models from OpenAI, Anthropic, Google, Meta, and Amazon ([a6da776](https://github.com/sanand0/llmmath/commit/a6da7768cfda8b5e15d985c2fa1bb09aba680c79), 27 Apr 2025).
- **Popovers for reasoning details:** Latch on to each test result to see the underlying reasoning steps right in hover popups—make math evaluation just a little less boring ([a6da776](https://github.com/sanand0/llmmath/commit/a6da7768cfda8b5e15d985c2fa1bb09aba680c79), 27 Apr 2025).
- **Cleaned setup instructions:** Clear commands and updated promptfoo usage for easy local test runs with multiple providers ([a6da776](https://github.com/sanand0/llmmath/commit/a6da7768cfda8b5e15d985c2fa1bb09aba680c79), 27 Apr 2025).
- **OpenAI reasoning models lead:** OpenAI's top reasoning LLMs score 6/7, missing only the 9-digit challenge; most others lag behind ([a6da776](https://github.com/sanand0/llmmath/commit/a6da7768cfda8b5e15d985c2fa1bb09aba680c79), 27 Apr 2025).
- **Public dashboard live:** Check model scores and reasoning traces at [sanand0.github.io/llmmath](https://sanand0.github.io/llmmath/), your new favorite mental calculator arena.

Turns out LLMs might not be math whizzes — but they can definitely talk the talk.

### [sanand0/assessor](https://github.com/sanand0/assessor)

Review your legal docs faster with AI-powered clause analysis—and relax knowing the code is solid.

- **Code cleanup & security:** Added MIT license, cleaned up PROMPT usage, introduced client-side file validation, text sanitization, and size limits to prevent bad inputs or crashes ([6e9608d](https://github.com/sanand0/assessor/commit/6e9608dd27993ed3fdffb6457c0cdd7f3e4f9c72), 22 Apr 2025).
- **Lazy-load PDF & DOCX libs:** Now loads PDF.js and Mammoth.js only when a file of the relevant type is used, shrinking startup time and memory footprint.
- **Improved UI & UX:** Checkbox clauses, updated Bootstrap UI, better error feedback via toasts, and sanitized text in status tables prevent nasty surprises ([6e9608d](https://github.com/sanand0/assessor/commit/6e9608dd27993ed3fdffb6457c0cdd7f3e4f9c72), 22 Apr 2025).
- **Smooth text & file conversion:** Dynamic file-to-text parsing supports PDF, DOCX, and plain text, ensuring flexible input processing ([6e9608d](https://github.com/sanand0/assessor/commit/6e9608dd27993ed3fdffb6457c0cdd7f3e4f9c72), 22 Apr 2025).
- **Helpful TODO & docs:** Listed upcoming features for keyboard navigation and improved use cases—yes, it's still evolving, one pull request at a time ([23f23d8](https://github.com/sanand0/assessor/commit/23f23d8026870e8327b0bc2bb07b410c26149554), 01 May 2025).

All built with LLMs themselves—because handing AI the reins requires that AI knows how to manage horses.

### [sanand0/asyncllm](https://github.com/sanand0/asyncllm)

Your favorite LLM streaming library just got more responsive and flexible with wider API support.

- **OpenAI Responses API:** Now supports the new OpenAI Responses Streaming API alongside Chat Completion style APIs, letting you receive responses and function calls seamlessly ([623cd31](https://github.com/sanand0/asyncllm/commit/623cd3184d58c49cd8400f84f860e079d08ac70e), 23 Apr 2025).
- **Adapters polish:** Refined Anthropic and Gemini adapter documentation—same code smoothly converts OpenAI requests to other vendor formats.
- **Enhanced function calling:** Supports streaming of incremental function call arguments for OpenAI's new API format, making tool integration more reliable ([623cd31](https://github.com/sanand0/asyncllm/commit/623cd3184d58c49cd8400f84f860e079d08ac70e), 23 Apr 2025).
- **Better error detection:** Catches and yields errors from any provider or HTTP fetch failures without breaking your stream.
- **Robust tests & docs:** Coverage includes OpenAI Responses streaming scenarios with multiple tool calls, ensuring your integrations won't break in production.

In a streaming world, patience is not a virtue — it’s just a solid API feature.

### [sanand0/til](https://github.com/sanand0/til)

Cleaned up markdown formatting and polished documentation so your weekly insights stay sharp and glitch-free.

- **Fix strikethrough glitches:** Changed `~` style ranges to dash `-` to prevent unwanted strikethroughs in mixed number ranges ([4183994](https://github.com/sanand0/til/commit/41839944e67e55c56cbe5bce13ff409555c6bb31), 01 May 2025).
- **Refined readme details:** Corrected description for the convert.js script behavior — it now notes it runs to most recent Saturday midnight instead of just a GitHub action.
- **Added older notes update:** Small text fixes and clarifications keep your “things I learned” collection tight and easy to scan ([21af860](https://github.com/sanand0/til/commit/21af8608c3a3ef9991fb80da5a917b5558413f5f), 27 Apr 2025).

Because people might read your notes, especially when you swore you’d never open that Markdown again.

### [sanand0/sanand0](https://github.com/sanand0/sanand0)

Your personal homepage gets clearer weekly summaries and smarter repo grouping for easier browsing and automation.

- **Better week titles:** Updated recent week archive titles and text to highlight exciting AI visuals, smooth admin APIs, and handy shell enhancements ([10e5286](https://github.com/sanand0/sanand0/commit/10e5286e212b6576e9621a2c8ce0cb3093246068), 27 Apr 2025).
- **Improved archive readability:** Enhanced summary formatting with polished links and clearer context to make your weekly changelog more user-friendly ([ec46bcd](https://github.com/sanand0/sanand0/commit/ec46bcdb774182b511152e3571af231359c9a957), 26 Apr 2025).
- **Automated repo tagging:** Added icon support and auto-grouped repos by topic to your homepage, cleaning up the UI and improving discoverability ([2977461](https://github.com/sanand0/sanand0.github.io/commit/297746116c3f9a48bbb88296761b7ee08bb6ebff), 27 Apr 2025).
- **Encourage API tests like `aipipe`:** Reminders to explore new administrative endpoints for better token & usage control.
- **Practical next steps:** Includes crafting demo Marp presentations, creating rewriting bookmarklets, and studying mental math evaluation data.

If you’re not automating your homepage updates, what are you even doing?

### [sanand0/tools](https://github.com/sanand0/tools)

Making small but mighty web apps more versatile with fresh GitHub stars integration and user-focused prompt enhancements.

- **GitHub Stars Tool:** Introduced a new web tool that replaces bare repo links in Markdown with star count, last pushed date, and repo name—a quick way to spot hot projects ([1779f43](https://github.com/sanand0/tools/commit/1779f4345071336e84ff470f5e97425cf12f3e92), 28 Apr 2025).
- **Prompting GitPicker:** Added a roadmap document outlining next features for your GitHub users filter app, including smarter LLM-based weighting and flexible input/formats ([1779f43](https://github.com/sanand0/tools/commit/1779f4345071336e84ff470f5e97425cf12f3e92), 28 Apr 2025).
- **UI polishing:** GitHub Stars app uses Bootstrap for sleek, responsive interface and lit-html for efficient updates.
- **Markdown link rewriting:** Transforms Markdown text with repo URLs into informative links enriched by real-time GitHub data.
- **Supports optional GitHub token:** Your GitHub API token usage can speed up lookups and avoid rate limits.

More stars, less guessing: finally a shiny upgrade for your README links.

## Suggested Next Steps

- Test creating a Marp slide deck with the unified `marked-smartart` plugin showcasing Pyramid, Chevron, and Venn diagrams together.
- Generate a personal rewriter bookmarklet with your API key—start polishing your web pages on the fly!
- Deploy the optimized Fish and Linux shell setup scripts to your computers for quicker, smoother AI and coding workflows.
- Dig into the `llmmath` dashboard to identify the best LLMs for your reasoning or math-heavy tasks.
- Explore `aipipe`'s admin APIs to better manage your AI token limits and user cost monitoring.
- Expand your tool suite with AI interactive demos from `autoimprove` and `eliminationgame`.
- Keep building on the `assessor` project—dynamic document review with AI is just getting started.