## A week of sharable slides, cleaner course pages, and new data stories

This week focused on making tools and teaching assets more shareable and visible. The key lesson: small UX fixes plus clear messaging multiply usefulness.

### [sanand0/tools](https://github.com/sanand0/tools)

_Turned a throwaway slide into a tiny, shareable slide studio—bookmarkable, image-friendly, and delightful to tweak. Yes, you really needed another slide editor._

- **Interactive slide editor:** Added a full-featured editor with Markdown, 12 fonts, live preview, and URL-stored configs ([ca6429e](https://github.com/sanand0/tools/commit/ca6429e4837fd61515aedac64e30686803860a3b); see slide/index.html and slide/README.md). This makes creating and sharing title slides instant. Takeaway: save state in the URL for frictionless sharing.
- **Background image reliability:** Replaced the deprecated Unsplash Source approach with direct image-URL support ([ca6429e](https://github.com/sanand0/tools/commit/ca6429e4837fd61515aedac64e30686803860a3b); slide/README.md). Users can paste any image URL from Unsplash, Pexels, or Pixabay. Takeaway: prefer stable inputs over brittle third-party endpoints.
- **Polish: favicon and better tab titles:** Added a favicon and convert Markdown to plain text for document.title ([0d4bed5](https://github.com/sanand0/tools/commit/0d4bed5b46eb611ba3e55e2e8dc9fa9dc0a0af27); see slide/index.html). Tabs now show readable titles when you open many slides. Takeaway: tiny UI touches improve discoverability.
- **Micro-linting for consistency:** Minor script tidy-up in colortable/script.js to reduce visual noise ([ca6429e](https://github.com/sanand0/tools/commit/ca6429e4837fd61515aedac64e30686803860a3b)). Cleaner code helps future edits. Takeaway: small refactors prevent big merge headaches later.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_Brought clarity to course messaging and schedules so students know what to do next. No, you can't learn the course from slides alone—intentional design, not laziness._

- **Clarified "no course content" stance:** Reworked README to emphasize that the course teaches via challenges, not static content ([375cbbe](https://github.com/sanand0/tools-in-data-science-public/commit/375cbbe43cba82c3092b225eaa11f3f381046f89); README.md). That sets correct expectations for auditors and students. Takeaway: clear messaging saves dozens of support emails.
- **Published Project 1 link and schedule fix:** Updated the roadmap and added a live Project 1 URL, shifting dates slightly ([9425a6](https://github.com/sanand0/tools-in-data-science-public/commit/9425a633c0c735b005f91da9e20c7221de67a20c); README.md). Students can now access assignments directly. Takeaway: surface deadlines and links prominently.
- **Polite UX nudge in contact guidance:** Restructured contact instructions to prefer AI/TAs before instructors ([9425a6](https://github.com/sanand0/tools-in-data-science-public/commit/9425a633c0c735b005f91da9e20c7221de67a20c)). This reduces unnecessary escalations. Takeaway: tell people the right sequence to ask for help.

### [sanand0/talks](https://github.com/sanand0/talks)

_Converted a live talk into a lasting, multimedia artifact with visuals, code, and notes. Yes, talk pages now include sketchnotes—because slides need personality._

- **Published the AMAT DT Day talk page:** Added a full talk site with slides, graceful styling, and interactive effects ([31b9552](https://github.com/sanand0/talks/commit/31b955252c218e4ebe603472f7a0f2feb86f0149); see 2026-02-11-amat-dt-day/index.html). This keeps the talk searchable and referenceable. Takeaway: web-first talks outlive ephemeral slides.
- **Added sketchnote asset and embed:** Included a sketchnote image and enlarged placement in the story ([7a7669a](https://github.com/sanand0/talks/commit/7a7669a050948a6d819a56b0b3d2f67724e47a04); see 2026-02-11-amat-dt-day/repetitive-tasks.webp). Visual summaries help non-technical readers. Takeaway: a single image raises engagement quickly.
- **Packed in code, transcript, and data story:** Added script.js, transcript.md, audio.opus, and a weekly-report data story ([31b9552](https://github.com/sanand0/talks/commit/31b955252c218e4ebe603472f7a0f2feb86f0149); files: script.js, transcript.md, weekly-report-data-story.html). The talk now doubles as a teaching module. Takeaway: combine talk, code, and data for reusability.

### [sanand0/blog](https://github.com/sanand0/blog)

_Kept course announcements timely and trimmed heavy assets to speed builds. Yes, smaller repos are happier repos._

- **GA1 announcement and GA1 post:** Added a GA1 release post and FAQs so students know deadlines ([c103b1a](https://github.com/sanand0/blog/commit/c103b1aa9184b89b9171a2ef219b753cbe9cc899); see posts/2006/tds-jan-2026-ga1-released.md). That reduces confusion during deadline churn. Takeaway: publish short notices close to dates.
- **Fix front-matter and prune images:** Standardized front-matter keys and removed bulky image binaries ([c103b1a](https://github.com/sanand0/blog/commit/c103b1aa9184b89b9171a2ef219b753cbe9cc899); updated posts and assets). Builds get faster and links stay valid. Takeaway: prefer CDN-hosted images to reduce repo bloat.
- **Corrected post dating/location:** Moved a TDS post into 2026 for correct chronology ([97de585](https://github.com/sanand0/blog/commit/97de5854f82ef3933023442932d82c97be95721a)). Readers now see current context. Takeaway: keep archives tidy; dates matter for discoverability.

### [sanand0/datastories](https://github.com/sanand0/datastories)

(Interactive data journalism grown a little larger this week.) _Added deep-dive stories and automated prompts. Yes, researchers get nervous when you say 'retraction'._

- **Two new stories:** Added "Retraction Watch" and "Researcher of the Future" with interactive pages ([ad99556](https://github.com/sanand0/datastories/commit/ad99556d86b2b59c848ea00334a0b3ff57825fec); see retraction-watch/index.html and researcher-of-the-future/index.html). These surface surprising, actionable data narratives. Takeaway: timely datasets make compelling stories.
- **Included analysis data and prompts:** Committed analysis_data.json and prompt templates, and updated config to include new stories ([ad99556](https://github.com/sanand0/datastories/commit/ad99556d86b2b59c848ea00334a0b3ff57825fec); retraction-watch/analysis_data.json). This supports reproducibility. Takeaway: ship data, code, and narrative together.
- **Ignore raw CSVs but keep derivations:** Added .gitignore entries for raw retraction CSVs to avoid huge files and leaked data ([ad99556](https://github.com/sanand0/datastories/commit/ad99556d86b2b59c848ea00334a0b3ff57825fec)). Keeps repo lightweight. Takeaway: commit derived artifacts, not the raw dump.

### [sanand0/til](https://github.com/sanand0/til)

_Sharpened course-facing checklists and added a student prompt template. Yes, teaching students to ask AI is a curriculum move._

- **Student prompt template added:** Added a pasteable prompt pattern to tds-jan-2026.md to help students generate learning prompts ([2382855](https://github.com/sanand0/til/commit/2382855c31946d43c1ac120986e0e7a11e420447); tds-jan-2026.md). This lowers the barrier to useful AI queries. Takeaway: teach prompt patterns, not magic words.
- **Checklist and notes tidy-up:** Marked progress items as done and added short TIL entries about tooling and workflows ([2382855](https://github.com/sanand0/til/commit/2382855c31946d43c1ac120986e0e7a11e420447); til.md, apps.md). Docs now reflect reality. Takeaway: accurate docs reduce onboarding friction.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Kept the LLM cost-quality frontier fresh. Yes, cost plots deserve fresh data._

- **Refreshed data and timestamp:** Updated the leaderboard timestamp and replaced elo.csv with new scores and pricing ([bf0d9f7](https://github.com/sanand0/llmpricing/commit/bf0d9f781734ec826217471365785e9881c40878); README.md, elo.csv). Users see current model tradeoffs. Takeaway: label data with the last updated date.
- **Larger CSV refresh:** Rewrote elo.csv with broader coverage and corrections ([bf0d9f7](https://github.com/sanand0/llmpricing/commit/bf0d9f781734ec826217471365785e9881c40878)). That improves frontier accuracy. Takeaway: re-run data pulls regularly for decision confidence.

## Lessons

- Small UX changes pay back massively in discoverability and reuse.
- Store state in URLs for easy sharing and reproducibility.
- Clear documentation prevents repeated questions.
- Ship data + code + narrative together for trustworthy stories.
- Teach students prompt patterns, not tricks.

## Suggestions

- Add a tiny automated smoke test for slide URLs. Fail fast when image URLs 404.
- Expose a simple JSON API for talks pages (title, audio, slides). Enables embeds.
- For datastories, add checksum or provenance notes for large datasets.
- Run a repo-size audit and remove other bulky binaries; prefer CDN hosting.
- In the course repo, add an “I’m stuck” flowchart to reduce instructor interrupts.