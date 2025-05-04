## Diverse Tech & Code Demos With Fancy Visuals and Practical Setup Tips

This week’s updates bring polished new demos, a sleek SmartArt presentation plugin, deeper AI coding insights, and practical system setup improvements. Plus, there’s a snake game with powerups, a luxurious analog clock, and an LBS eBook published in an hour!

### [sanand0/an-lbs-exchange-program](https://github.com/sanand0/an-lbs-exchange-program)

*Get a step-by-step guide to publish your own eBook on Amazon in about an hour.*

- **Official Amazon book launch:** Added valid Amazon purchase link and included the generated [ePub book file](https://github.com/sanand0/an-lbs-exchange-program/commit/9c2b759) for direct reading or republishing.
- **Streamlined publishing instructions:** Polished the README with explicit KDP URLs, cover design process using ChatGPT, and publisher tips.
- **Cover preview that links to Amazon:** The cover image now clicks through to the Amazon page, letting interested readers see the book instantly.
  
Yes, you really needed another guide on publishing an eBook fast. But this one makes it delightfully straightforward.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

*Fixes for smooth deployment of cost-quality LLM comparisons on GitHub Pages.*

- **Simplified domain management:** Removed obsolete `CNAME` file to unblock deployment errors ([9985d8f](https://github.com/sanand0/llmpricing/commit/9985d8f)).
- **Reliable long-term hosting:** Ensures that updated frontends for comparing LLM pricing and quality remain accessible.

This won’t make LLM pricing cheaper, but it will keep your visual explorations live and pristine.

### [sanand0/marked-smartart](https://github.com/krishna-gramener/marked-smartart)

*Craft gorgeous Marp presentation diagrams with Pyramid, Chevron, and Venn charts using special markdown code blocks.*

- **Marp engine plugin added:** Unified engine `smartart-plugin.js` now renders custom diagram blocks seamlessly ([33b3da8](https://github.com/sanand0/marked-smartart/commit/33b3da8)).
- **Replaced old individual plugins:** Removed the previous `pyramid-marked-plugin.js`, `chevron-marked-plugin.js`, and `venn-marked-plugin.js` in favor of modular, maintainable JS modules (`pyramid.js`, `chevron.js`, `venn.js`).
- **Extended README with usage details:** Complete usage examples for diagrams, options for size and font, color handling differences, multi-diagram slides, and browser compatibility.
- **Automated test expansions:** Added improved markdown + HTML test cases showing side-by-side Pyramid, Chevron, and Venn diagrams ([tests/test-marp-diagrams.md](tests/test-marp-diagrams.md)).

Because your Marp slides *needed* one more way to outshine everyone else’s.

### [sanand0/scripts](https://github.com/sanand0/scripts)

*Better command line and system setups for faster coding, AI tool usage, and cleaner Windows/Linux integration.*

- **Added Gramex virtualenv to path:** Both bash and fish setup scripts now include Gramex in PATH for easy access ([dc97538](https://github.com/sanand0/scripts/commit/dc97538)).
- **Linux setup notes updated:** Added Foliate fix on Wayland, new Gnome keyboard shortcuts for Guake and Warp terminals, and removed out-of-date Warp skip note ([dc97538](https://github.com/sanand0/scripts/commit/dc97538)).
- **Introduced AI code editor instructions:** Added detailed rules for Python and JavaScript coding styles to speed up AI assistance with code generation ([b51ac19](https://github.com/sanand0/scripts/commit/b51ac19)).
- **Alias additions:** Added datasette alias for easier shell access ([6f2bc6f](https://github.com/sanand0/scripts/commit/6f2bc6f)) along with improved LLM model defaults in instructions.
- **Misc fixes:** Use full paths over alias for uvx to ensure commands run in current directory ([45b1730](https://github.com/sanand0/scripts/commit/45b1730)) and enabled fish shell fnm environment ([3f487c7](https://github.com/sanand0/scripts/commit/3f487c7)).

No manual setup drudgery, just clean paths and sharper AI workflows.

### [sanand0/autoimprove](https://github.com/sanand0/autoimprove)

*Watch code grow from a simple circle drawer to a fully interactive design toolkit with repeated AI improvements.*

- **New demos & improved UI folding:** Added `games.json` to showcase multiple code-driven demos and enhanced collapsible code+explanation UI ([264c757](https://github.com/sanand0/autoimprove/commit/264c757), [fd0ff08](https://github.com/sanand0/autoimprove/commit/fd0ff08)).
- **Interactive circle evolution:** Initial static circle script transforms into a drag-and-drop, resizable, color-tweakable, pulse+spin interactive canvas (#264c757).
- **Clean UX and coloring syncing:** Real mouse pointer sync for paint brushes and better organized controls with reset, pulse and spin features.
- **Enhanced code output display:** Collapsible sections for easier reading of generated code and explanations ([259bfc4](https://github.com/sanand0/autoimprove/commit/259bfc4)).

AI-assisted coding has never been so hands-on and pretty.

### [sanand0/eliminationgame](https://github.com/sanand0/eliminationgame)

*LLMs chat & survive as if in a Survivor-style game, visualized with insight into their alliances and strategies.*

- **User documentation added:** Detailed README and PROCESS.md outline LLM visualization steps, with screenshots and narrated development flow ([25ac7d1](https://github.com/sanand0/eliminationgame/commit/25ac7d1), [8d72c7b](https://github.com/sanand0/eliminationgame/commit/8d72c7b)).
- **UI & hash improvements:** Streamlines URL-driven navigation (slider and dropdown sync), clean hover highlights, clickable conversation rows, and better table row marking ([fd8bb7e](https://github.com/sanand0/eliminationgame/commit/fd8bb7e)).
- **Visual polish:** Adds distinct green and red alliance/voting arrows, grey conversation lines, faded eliminated player indicators, and improved coloring.
- **Interaction enhancements:** Allows clicking chat or table rows to jump to respective steps, enhancing gameplay review.
  
If LLMs ever got voted off the island, this app would be how you spot the mastermind.

## Suggested Next Steps

- For the new [marked-smartart](https://github.com/krishna-gramener/marked-smartart), try converting sample Marp presentations to activate these fresh diagrams.
- Record a demo slideshow combining Pyramid, Chevron, and Venn diagrams to wow your colleagues.
- Explore the [autoimprove](https://github.com/sanand0/autoimprove) demos to see how AI-refined scripts evolve iteratively.
- Test Fish and Bash shell setups from [scripts](https://github.com/sanand0/scripts) on your machines to speed up AI tool executions.
- Dive into the [eliminationgame](https://github.com/sanand0/eliminationgame) visualization and try jumping between steps using chat or table links for insights.
- Consider adding more AI-generated interactive web apps to [tools](https://github.com/sanand0/tools) for your personal toolkit.