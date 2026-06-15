## A week of making things findable, usable, and runnable—on the web and in class.

Small ergonomics paid off this week. Better metadata, clearer UI, and a few automation scripts made content easier to find and forms easier to use.

### [sanand0/blog](https://github.com/sanand0/blog)

_Improved discoverability and fresher content so readers and search engines find the right thing faster._  
- **Add SEO metadata (12 Jun 2026):** Added descriptions and keywords site-wide and a metadata index via [d55bd0](https://github.com/sanand0/blog/commit/d55bd04f519a04fdb752a9f8390ca6e4212165cb). See e.g. [posts/2026/let-ai-take-your-exams.md](https://github.com/sanand0/blog/blob/main/posts/2026/let-ai-take-your-exams.md). Takeaway: small frontmatter boosts link previews and search clicks. (Yes, more meta fields.)
- **New posts and announcements (13 Jun 2026 / 08 Jun 2026):** Published a graduation speech and several workshop posts via [a0d641d](https://github.com/sanand0/blog/commit/a0d641d46a689295cd2c7a451406f92d2aefc5b4) and [2c17712](https://github.com/sanand0/blog/commit/2c177129186bbf94c7b29a05d89c4fb00ec98a1d). Read: [make-5-new-friends-today.md](https://github.com/sanand0/blog/blob/main/posts/2026/make-5-new-friends-today.md). Takeaway: publish while fresh to capture interest and contextual search traffic.
- **Curated link roundups and essays (07 Jun 2026):** Added an “Oh shit” GenAI roundup and a visual-AI post ([de6b12d](https://github.com/sanand0/blog/commit/de6b12d36618702255a7dde0f191897ba7308677), [76811eb](https://github.com/sanand0/blog/commit/76811eb021d204ba1f2e7822b07cd5c08f8a26ed)). Takeaway: link roundups make discovery fast and show practical context.
- **Build and content tooling (07 Jun 2026):** Documented TIL automation, LinkedIn mapping, and added a `description` task in `justfile` ([0f8333e](https://github.com/sanand0/blog/commit/0f8333eb9c7e5d490be84a618fb083186912a68a)). Takeaway: treat generated artifacts as first-class and keep source authoritative.
- **Style tweaks for metadata (12 Jun 2026):** Make post descriptions render as secondary text via theme CSS ([d55bd0](https://github.com/sanand0/blog/commit/d55bd04f519a04fdb752a9f8390ca6e4212165cb), file: `themes/PaperMod/assets/css/common/post-single.css`). Takeaway: small visual cues help readers scan.

### [sanand0/liveform](https://github.com/sanand0/liveform)

_Make classroom surveys tiny to run and easy to share, so students actually use them._  
- **Initial app and test suite (12 Jun 2026):** Launched FastAPI app, CLI, storage, and many tests in the initial commit [4bdf12d](https://github.com/sanand0/liveform/commit/4bdf12d5ed523adb9a7a3f557a98187e52e8f74a). See `src/liveform/` for server, store, and tests. Takeaway: ship fast with tests to avoid regressions.
- **Homepage and forwarded-origin links (13 Jun 2026):** Serve a latest-form landing page and use forwarded origins for QR and links ([d11dd1c](https://github.com/sanand0/liveform/commit/d11dd1c30d14c1a10dcc6d4dbdf39ef6af48313a)). File: `src/liveform/assets.py`. Takeaway: small host-aware fixes cut support friction.
- **Question numbers and sensible defaults (13 Jun 2026):** Add sequential question numbers in the UI and default field types when `field` is omitted ([e656f5c](https://github.com/sanand0/liveform/commit/e656f5c473138eabc976d5e74dadb2d5dedd426d); see `src/liveform/assets.py`, `src/liveform/config.py`). Takeaway: reduce YAML noise and make forms easier to author.
- **Event-ready forms for workshops (12–13 Jun 2026):** Add `forms/aistories/form.yaml` and `forms/aiexam/form.yaml` for two workshops ([aeae024](https://github.com/sanand0/liveform/commit/aeae0242da7e0757dce5fb1a183a11a61848ca76), [895b276](https://github.com/sanand0/liveform/commit/895b27695c85e3cf53248c712141dd4e734d3e83)). Takeaway: shipping event-specific forms speeds classroom feedback loops. (Yes, you really needed another form YAML.)

### [sanand0/talks](https://github.com/sanand0/talks)

_Notes and artifacts from workshops, plus a small interactive techniques atlas._  
- **Workshop materials and transcripts (11 Jun 2026):** Added full workshop site, transcripts, and demos for the Engineering Design talk ([7719c5b](https://github.com/sanand0/talks/commit/7719c5b5b5ddb6c0a763772ac8dca0e9988cda33)). See `2026-06-11-engineering-design-iitm/index.html`. Takeaway: publish talks with code and transcripts for reuse.
- **Data-stories technique atlas (07 Jun 2026):** Added an interactive `techniques.html` and `techniques.jsonl` for the Data Stories workshop ([5bd3f19](https://github.com/sanand0/talks/commit/5bd3f195339c47a31a53b1bbe5183c3566b8496f)). Takeaway: interactive indexes help learners pick experiments faster.
- **Prompt guidance and careful fact-check notes:** Prompt files and correction notes live alongside the talks (`prompts.md`). Takeaway: keep prompt and revision notes with the talk artifacts. (A few quote fixes saved some blushes.)

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

(Simple automations for a messy podcast flow.)  
- **Podcast automation targets (07 Jun 2026):** Added a `justfile` with `build` and `deploy` targets to standardize week builds and releases ([1ffd8e3](https://github.com/sanand0/generative-ai-group/commit/1ffd8e3b3d4b12de066e172b6aeb6a276a6f6b42)). Takeaway: one-command builds reduce uploader mistakes.
- **Episode content update (07 Jun 2026):** Added the week’s episode notes at `2026-06-07/podcast-2026-06-07.md` ([c2122d1](https://github.com/sanand0/generative-ai-group/commit/c2122d1c8bae033788f2fa23e7e002bd640ca418)). Takeaway: keep show notes with the release to speed syndication.

### [sanand0/research](https://github.com/sanand0/research)

_Prototypes that test the bounds of visual and mesh-based research._  
- **3D mesh experiments for skull and jaw fit (11 Jun 2026):** Add `3dmesh` experiments, readers, and visualization outputs ([ccf6f90](https://github.com/sanand0/research/commit/ccf6f9069cc029c710765a7e4544e7c8de95e6ca)). See `3dmesh/README.md` and `head_ct_skull_experiment.py`. Takeaway: prototypes expose practical limits fast, and catch assumptions early.

### [sanand0/chatgpt-to-markdown](https://github.com/sanand0/chatgpt-to-markdown)

_Make exported chat archives human-friendly and link attachments cleanly._  
- **Support archive directories and sharded exports (11 Jun 2026):** CLI now accepts an archive dir and reads `export_manifest.json` ([e5b620e](https://github.com/sanand0/chatgpt-to-markdown/commit/e5b620e398767021548851229e3559dff421c068)). Takeaway: handle real-world exports, not just ideal cases.
- **Richer Markdown formatting (11 Jun 2026):** Collapse reasoning into details, convert citation markers, and add model/flag metadata ([e5b620e](https://github.com/sanand0/chatgpt-to-markdown/commit/e5b620e398767021548851229e3559dff421c068)). Takeaway: cleaner markdown is easier to scan and archive.
- **CLI reliability and tests (11 Jun 2026):** Ensure streamed processing finishes before exit and add archive tests (`chatgpt-to-markdown-cli.test.js`). Takeaway: avoid truncated exports and flaky scripts.

### [sanand0/til](https://github.com/sanand0/til)

_Keeping weekly notes and trending snapshots up to date._  
- **June notes and trending refresh (07 Jun 2026):** Add June LLM notes, TIL updates, and refresh `trending-repos.tsv` with June data ([82d2f4f](https://github.com/sanand0/til/commit/82d2f4f6805e4aa524650ebb5f559b8943e2f896)). Takeaway: small, regular updates keep the research trail usable.

## Lessons

- Small discoverability wins matter. Add concise metadata early.  
- Tests and smoke checks prevent UI regressions across deployments.  
- Default sensible configs reduce author friction and YAML noise.  
- One-command builds scale manual work and make releases reliable.  
- Publish artifacts (transcripts, prompts, visuals) alongside code. They help others reproduce results.

## Suggestions

- Measure the SEO lift from new frontmatter. Track clicks and impressions.  
- Add lightweight analytics to the liveform homepage for mobile vs desktop.  
- Wire podcast deploy into CI for automated weekly releases.  
- Add an accessibility pass for forms (ARIA labels, keyboard flow).  
- Convert the techniques atlas to a static JSON API for reuse across talks.