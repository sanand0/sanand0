## A week of talks, teachable analytics, and site-level machine smarts

This week focused on turning talks into full, interactive web pages and turning exam logs into TA playbooks. The big lesson: shipping usable artifacts (pages, playbooks, maps) beats endless planning.

### [sanand0/talks](https://github.com/sanand0/talks)

_The talk repo grew from slides to full, interactive web experiences that audiences and committees can actually use._

- **Many new talk pages published.** Added full pages, transcripts, audio, and sketchnotes for several events ([6003fb2](https://github.com/sanand0/talks/commit/6003fb2067b9763bdea3fd522948e1223feebbbf), [009a214](https://github.com/sanand0/talks/commit/009a214259f50afb35a0f750a3f7b156441cbde1), [b68fd47](https://github.com/sanand0/talks/commit/b68fd475b0defd9be318d517e5469e9c5f922181)). These pages embed videos, audio, and transcript popups so readers can jump right in. Takeaway: make content first-class and clickable, not just a ZIP file.
- **Interactive critique and media embeds.** The Chennai Design Festival page now includes an interactive chart critique iframe and video embeds ([6003fb2](https://github.com/sanand0/talks/commit/6003fb2067b9763bdea3fd522948e1223feebbbf)). That turns a slide into a living demo. Takeaway: show, don’t just tell.
- **Governance & idea catalogs for IITM work.** Built idea galleries, sortable tables, and a v2 interactive narrative for the Academic Council work ([b32f6d0](https://github.com/sanand0/talks/commit/b32f6d081a243467d23e55773e6c876fcbd4abd8), [a4ccc33](https://github.com/sanand0/talks/commit/a4ccc33e6b534853ae28d7ed5584b982cfc38193)). These make committee choices evidence-driven. Takeaway: committees act on clarity, not rhetoric.
- **Panel & verification talks packaged for reuse.** Added PyConf panel material and a Verifiable Agents story with slide assets and an email summary ([e88a418](https://github.com/sanand0/talks/commit/e88a418b922d282cf3be9357752dfede844dc477), [605668e](https://github.com/sanand0/talks/commit/605668ed90d55827bf10b6928e59f0c8ccb1af9e)). These are ready for outreach and governance use. Takeaway: one-page summaries + assets scale outreach.
- **UI polish and small fixes.** Tweaked the ideas table UI and prompts to make pages linkable, searchable, and keyboard-friendly ([c45b0e2](https://github.com/sanand0/talks/commit/c45b0e272708f82be50a1c48f10791bd0fee8e46), [aa4a2ac](https://github.com/sanand0/talks/commit/aa4a2ac68d6a7243a8f609054d4561084847d2d0)). Yes, the site now answers your keyboard nav habit. Takeaway: small UX fixes multiply usefulness.

Aside: Yes, you really needed another interactive idea table. Make it searchable.

### [sanand0/pyoppe](https://github.com/sanand0/pyoppe)

_Moving from raw exam logs to practical TA playbooks and stage-ready replay artifacts._

- **TA playbook generator added.** New v2 scripts create actionable TA packs and CSVs (`v2-analysis/generate_learning_support.py`) and a compact HTML playbook ([497943b](https://github.com/sanand0/pyoppe/commit/497943b340b8dca2a940a9298e1dff0c112b07a9), [v2-analysis/learning-support.md](https://github.com/sanand0/pyoppe/commit/497943b340b8dca2a940a9298e1dff0c112b07a9)). TAs get a prioritized queue and clear tasks. Takeaway: turn logs into “do this now” lists.
- **Replay and slides tooling for talks.** Added scripts to extract exemplar replays and build PyConf slide assets ([a97a6ca](https://github.com/sanand0/pyoppe/commit/a97a6ca90686926fde991042da09123c6e6042c0), [analysis/replays.md](https://github.com/sanand0/pyoppe/commit/a97a6ca90686926fde991042da09123c6e6042c0)). That gave the PyConf talk concrete, watchable examples. Takeaway: real student traces make the argument stick.
- **Markdown lint & cleanup.** Large lint pass cleaned code blocks and formatting for readability ([755b608](https://github.com/sanand0/pyoppe/commit/755b6082fb9cf0dc150d68eaed29aa5a420ab2a9)). The docs are now safer to parse and reuse. Takeaway: clean text is reusable data.

Aside: Yes, showing a student’s typo on stage is educational, not cruel. Be kind in the narration.

### [sanand0/blog](https://github.com/sanand0/blog)

_An embeddings pipeline and an interactive blog map make the archive explorable._

- **Embeddings pipeline and tools added.** New scripts generate Gemini embeddings, cache in DuckDB, export parquet, and support incremental runs ([analysis/embeddings/embeddings.py](https://github.com/sanand0/blog/commit/f7094511d9af401c011afb1cd263e77f287e29c7)). This lets you re-run only changed files. Takeaway: incremental pipelines save time and money.
- **Analysis and blogmap generator.** Added analysis, PCA→UMAP→KMeans flow, and a stable blogmap JSON for the interactive map ([analysis/embeddings/analyze_embeddings.py](https://github.com/sanand0/blog/commit/f7094511d9af401c011afb1cd263e77f287e29c7), [analysis/embeddings/blogmap.py](https://github.com/sanand0/blog/commit/f7094511d9af401c011afb1cd263e77f287e29c7)). This produced the blog embeddings map shown on the site. Takeaway: visual maps reveal archive drift fast.
- **New posts and site links.** Added posts and small site edits to surface the embedding work and new demos ([posts/2026/blog-embeddings-map.md](https://github.com/sanand0/blog/commit/f7094511d9af401c011afb1cd263e77f287e29c7)). Visitors can now explore the map interactively. Takeaway: show research and code together.

Aside: Yes, you do want PCA before UMAP. It calms the beast.

### [sanand0/til](https://github.com/sanand0/til)

_Notes, tasks, and the weekly snapshot got a tidy refresh for March._

- **Updated learning notes and examples.** Added March TIL entries, CLI fixes, and tool observations in llms.md and til.md ([bd13fb2](https://github.com/sanand0/til/commit/bd13fb2b96689bee4b0c4ea27fd36cddd7a016af)). This keeps the running notebook current. Takeaway: tidy notes avoid re-solving yesterday’s problems.
- **Tasks and trending snapshot refreshed.** Marked a few tasks done and updated trending-repos.tsv to March 2026 data. That keeps triage accurate for weekly work. Takeaway: keep the TODOs honest and the snapshot fresh.

Aside: The “ubi -> github” swap in examples is the kind of small save that stops future confusion. Do it.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_New novel visualizations pack adds three thoughtful, interactive charts._

- **Three novel dataviz slide deck.** Added a titled deck with code, prompts, and a full interactive page for three new chart designs ([c86fa43](https://github.com/sanand0/datastories/commit/c86fa437ffb4dab7fde7c9bd55b2cf5a79a6b7ee), [novel-dataviz/index.html](https://github.com/sanand0/datastories/commit/c86fa437ffb4dab7fde7c9bd55b2cf5a79a6b7ee)). Each chart includes synthetic data and design notes. Takeaway: novel encodings need good examples to persuade.
- **README and site link updated.** The main README now links the story and screenshot for easy discovery. Takeaway: surface new work prominently.

Aside: Yes, design is partly taste and partly a lab exercise. Show both.

### [sanand0/apiagent](https://github.com/sanand0/apiagent)

_A small but practical addition: a FRED API demo + model-quality toggle for recoverability tests._

- **FRED API demo added.** Integrated the FRED (St. Louis Fed) endpoints into the demo agent, with example prompts and transforms ([eb2a0d4](https://github.com/sanand0/apiagent/commit/eb2a0d4286b2a6ef708b56216a487db16ab7e80a), [config.js](https://github.com/sanand0/apiagent/commit/eb2a0d4286b2a6ef708b56216a487db16ab7e80a)). Users can query economic time series directly. Takeaway: practical demos make API agents believable.
- **Cheap vs Good model toggle.** UI toggle to simulate first-attempt failure and second-attempt recovery for teaching model resilience ([e19e0ae](https://github.com/sanand0/apiagent/commit/e19e0ae708586e98c10ddc37b852aa21c8009537)). Great for slides and demos. Takeaway: show graceful recovery patterns in demos.

Aside: Breaking the first run on purpose is a good teaching hack. Humans find it honest.

### [sanand0/tools](https://github.com/sanand0/tools)

_Title-slide editor polish: independent title/subtitle scaling, tests, and favicon tweaks._

- **Independent title/subtitle scales.** Slide editor now supports separate log-scale sliders for title and subtitle ([bafb71c](https://github.com/sanand0/tools/commit/bafb71c6c5858dc3ca808a481b9138a968dacdc5), [slide/index.html](https://github.com/sanand0/tools/commit/bafb71c6c5858dc3ca808a481b9138a968dacdc5)). That helps speakers tune framing quickly. Takeaway: small controls reduce slide fiddling.
- **Test & CI hygiene.** Added a unit test to validate font scaling and favicon behavior ([bafb71c](https://github.com/sanand0/tools/commit/bafb71c6c5858dc3ca808a481b9138a968dacdc5), [slide/slide.test.js](https://github.com/sanand0/tools/commit/bafb71c6c5858dc3ca808a481b9138a968dacdc5)). This prevents regressions. Takeaway: test the stuff you tweak most.
- **README and UX updates.** Docs now show examples for independent scales and usage tips. Takeaway: document UI choices for others.

Aside: Yes, slider math is boring, but your keynote will look better.

### [sanand0/sanand0.github.io](https://github.com/sanand0/sanand0.github.io)

_Tiny but strategic: verified site ownership with Google Search Console meta tag._

- **Google Search Console verification.** Added the verification meta tag to the site template ([12f000b](https://github.com/sanand0/sanand0.github.io/commit/12f000bdf5c2b2a29041b9ccdada6779499e7449)). This enables search indexing and visibility checks. Takeaway: small publish ops unlock big distribution.

Aside: Yes, meta tags still win internet arguments with search engines.

## Lessons

- Ship artifacts people can act on. Pages, CSVs, and playbooks create momentum.  
- Make UIs that reveal, not hide. Interactive embeds and popups turn passive reports into tools.  
- Incremental pipelines scale. Cache embeddings and re-run only deltas.  
- Teach by failing. Simulated first-run failures make demos more instructive.  
- Clean docs are code. Linting and README updates pay dividends for downstream analysis.

## Suggestions

- Publish the TA playbook CSVs and a short how-to for TAs this week. Make them actionable email attachments.  
- Hook the embeddings pipeline into a nightly job and publish the blogmap.json to the live site. Add a small cache-busting version.  
- Add a smoke test for talk pages that ensures transcript popups and video embeds load without horizontal scroll.  
- Turn the FRED demo into a short tutorial notebook. Walk through one analysis (e.g., yield curve) and link it from the talk pages.  
- Add a tiny analytics dashboard for the learning-support pages: clicks, downloads, and TA feedback form. Use that to refine thresholds.  
- Consolidate prompts.md fragments into one “talk-to-website” recipe so future talk pages follow the same deploy pattern.

If you want, I can draft the TA email template and the CI job for nightly embeddings next.