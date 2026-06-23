## A week of polishing forms, talks, prompts, and scrapers — making workshops, writing, and experiments more reliable and useful.

Small, targeted work paid off: faster polls, longer sessions, clearer counts, and richer artifacts. The week’s lesson: invest in tiny infrastructure wins; they multiply productivity and trust.

### [liveform](https://github.com/sanand0/liveform)

_Better workshop UX and robustness so presenters run fewer recovery steps and everyone sees live totals without noise._

- **Per-question live counts:** Returned answer totals from the server and cached them in the store ([87b2f86](https://github.com/sanand0/liveform/commit/87b2f86a04eff577368f4106f336c12a25d6cd6f), 16 Jun 2026). UI badges show counts without re-reading the TSV. Takeaway: show verified totals, not guesses, to build trust quickly.
- **Smarter polling that pauses when unfocused:** Front-end avoids polling when the tab is hidden and checks immediately on focus ([a2fe133](https://github.com/sanand0/liveform/commit/a2fe133a77950c9223b14ef1754914e241da0f5f), 16 Jun 2026). Tests cover the focus/visibility flow. Takeaway: reduce server load by being polite to the browser.
- **Keep sessions valid across restarts:** Added a local session secret and signed session tokens so logins last ~24 hours ([0a5663e](https://github.com/sanand0/liveform/commit/0a5663e73ef684a195a2a10558b6072e66985791), 16 Jun 2026). Tests validate cross-restart session survival. Takeaway: short-lived sessions cost user attention; persistable secrets help workshops run longer.
- **UI refinements and new form:** Repositioned the small answer-count badge under the question number and added a datastack demo form ([daf4d4d](https://github.com/sanand0/liveform/commit/daf4d4d7efac0822ada41fc319a85a2ec4f9a2bf), 16 Jun 2026; [17ebfb3](https://github.com/sanand0/liveform/commit/17ebfb3b78d2ea41f18d13d043e18c77ea88012d), 16 Jun 2026). Yes, the little number now behaves. Takeaway: small visual changes ease scanning and classroom flow.

### [blog](https://github.com/sanand0/blog)

_More reusable prompts, clearer metadata, and new posts so content is easier to find and reuse._

- **Added reusable AI lenses and skills:** New SKILL.md lenses (e.g., anand-objectives, evidence-provenance) and many prompt fragments were added ([9763887](https://github.com/sanand0/blog/commit/9763887917a006c8aa76b4fc60ed2202548bab6f), 20 Jun 2026). These steer outputs toward artifacts and verification. Takeaway: encode answer-style rules once and reuse them.
- **Published new posts and workshop recaps:** Added event write-ups and a hands-on post on agents solving small data questions ([9763887](https://github.com/sanand0/blog/commit/9763887917a006c8aa76b4fc60ed2202548bab6f), 20 Jun 2026; [4593e65](https://github.com/sanand0/blog/commit/4593e6519a51a397374cff51a3555dc549e15226), 16 Jun 2026). Each has metadata for discovery. Takeaway: publish demos and results fast; readers learn from concrete artifacts.
- **Content and SEO cleanup:** Added descriptions, keywords, lastmod fixes, and removed an obsolete fake-data page ([9763887], 20 Jun 2026; [f6854f1](https://github.com/sanand0/blog/commit/f6854f102680623a7b82fcc9c544b7496b3acfb9), 16 Jun 2026). The site build extracts metadata more reliably. Takeaway: good metadata means content actually gets found.

(Wry aside: yes, another "skill" file — but it will earn you hours back.)

### [talks](https://github.com/sanand0/talks)

(More polished talks, transcripts, and handouts so a single session yields many lasting artifacts.)

- **Added EQT talk site and assets:** Full page, transcript, and analysis for "The Data Stack for an Agentic World" ([294a1b7](https://github.com/sanand0/talks/commit/294a1b761b5a7c492826155d2796d36a770f14cb), 16 Jun 2026). Includes downloadable slides and survey analysis. Takeaway: capture talks as linked artifacts to reuse in consulting or teaching.
- **Bulked up workshop content:** Added the "Data Stories with AI" and "Let AI Take Your Exams" folders, transcripts, analysis, and prompts ([9de226a](https://github.com/sanand0/talks/commit/9de226aef6c62711d314b1dfa4971269e6a908bd), 14 Jun 2026; [db9b56d](https://github.com/sanand0/talks/commit/db9b56d6ed144505a3f1047a9cfe621afd01ad26), 14 Jun 2026; [db9b56d earlier], 12 Jun 2026). Each talk now has narrative, slides, and data. Takeaway: make talks reproducible by bundling transcripts, prompts, and outputs.
- **Cosmetic layout fixes:** Added margins and improved embedded media spacing ([10a71b2](https://github.com/sanand0/talks/commit/10a71b212bfebfc033313e5589c28f504ab851df), 14 Jun 2026). Takeaway: small layout fixes reduce friction when embedding media.

(Wry aside: the slides now have margins, so your screenshots look less guilty.)

### [tools](https://github.com/sanand0/tools)

_Fix scrapers so saved chats keep attachments and the hidden reasoning._

- **Capture user attachments:** Scraper now detects top-level attachment nodes and exports them as Markdown attachments ([668977a](https://github.com/sanand0/tools/commit/668977a566e5ca76e8a574f301fcdddcc6492a9b), 20 Jun 2026). Tests confirm the fixture extraction. Takeaway: preserve uploaded files; they often contain the signal.
- **Better reasoning extraction:** Improved handling of thought/worked toggles and inline reasoning snapshots ([0b342b0](https://github.com/sanand0/tools/commit/0b342b085a335cb7eddcddec259bff432a2cb653), 14 Jun 2026). Now code snippets and tool traces appear in outputs. Takeaway: keep the chain-of-thought for audit and teaching.
- **Updated tests and fixtures:** Tests assert richer output, including code blocks and reasoning panels, improving reliability. Takeaway: tests catch edge cases so HTML quirks don't silently break exports.

(Wry aside: your TSV uploads will no longer vanish into the ether.)

### [llmpricing](https://github.com/sanand0/llmpricing)

_Keep the LMArena scraping and CSV upkeep smoother with scripted updates and clearer deprecation notes._

- **Add one-line download script:** New `download.py` automates CDP scraping from LMArena into TSV/JSON ([6be0b3f](https://github.com/sanand0/llmpricing/commit/6be0b3f7f5b5161ca41f6dfcfa9f2b9f20921222), 20 Jun 2026). It supports headless CDP runs on localhost:9222. Takeaway: automating brittle scraping saves hours.
- **Update README and deprecations:** Clarified deprecation notes and update flow, plus an `update.sh` orchestrator ([92882f9](https://github.com/sanand0/llmpricing/commit/92882f98cfe43bf07631217e277597ca27f2f7c9), 20 Jun 2026). Takeaway: document the brittle parts so future you isn't surprised.
- **Refresh elo.csv:** Updated ELO export and replaced stale rows to reflect current leaderboards (20 Jun 2026 commits). Takeaway: keep source-of-truth CSVs tidy and dated.

(Wry aside: scraping leaderboard pages is still more engineering than it sounds.)

### [llmmath](https://github.com/sanand0/llmmath)

_Expanded math benchmarks and made the results sortable and date-aware._

- **New model runs and dates:** Added newer models, recording eval dates in model-dates.json ([71ec80a](https://github.com/sanand0/llmmath/commit/71ec80ac9b0636bdffd8dd7835b6a96c3cdacd35), 15 Jun 2026). UI shows when each model was tested. Takeaway: date columns prevent stale comparisons.
- **Eval automation and incremental updates:** Introduced update-models.js and new-models.txt to add models without rerunning existing tests. Takeaway: incremental evals save tokens and time.
- **Sortable web UI:** index.html and scripts now let you sort by date and score, and show summary notes about recent perfect scores ([71ec80a], 15 Jun 2026). Takeaway: sortable tables make exploration fast and obvious.

(Wry aside: yes, apparently some models finally learned long multiplication.)

### [til](https://github.com/sanand0/til)

_Notes and trends updated so weekly learning and repo lists stay fresh._

- **Add June notes:** Appended recent LLMS observations and small tooling tips to `llms.md` and `til.md` (15 Jun 2026). Takeaway: small notes compound into a readable knowledge base.
- **Refresh trending repos TSV:** Updated `trending-repos.tsv` with June entries across languages (15 Jun 2026). Takeaway: track trends before they become noise.

(Wry aside: weekly TIL beats weekly panic.)

### [prompts](https://github.com/sanand0/prompts)

_Repository migrated into the blog to centralize prompt collections._

- **Repository migration:** README now points to the blog prompts folder, consolidating prompts with site content ([6d2c917](https://github.com/sanand0/prompts/commit/6d2c91752029b799e791d173f38adadec733bb08), 20 Jun 2026). Takeaway: central content reduces duplication and version drift.

(Wry aside: yes, the prompts are finally moving home.)

## Lessons

- Small infra fixes yield big UX wins. Less polling, persistent sessions, and cached counts save time and attention.
- Capture artifacts, not just outputs. Transcripts, prompts, attachments, and provenance make experiments reusable.
- Automate brittle processes incrementally. Scripts that only add missing models or scrape once are cheaper than full reruns.
- Date your experiments. Tests and eval dates avoid wrong conclusions from stale data.
- Tests that simulate real UI quirks prevent fragile scrapers and exporters.

## Suggestions

- Liveform: add a lightweight metrics endpoint for aggregated real-time telemetry and a README example for workshop hosts.
- Tools: convert the scraper’s attachment extraction into an explicit export directory and zip manifest for downstream archival.
- Blog/talks: add a short "one-click demo" section in talk pages that reproduces the key data transformation steps.
- llmmath/llmpricing: store run provenance (env, provider IDs) alongside results to make audits and replays trivial.
- All repos: add a short CHANGELOG.md for user-facing changes, dated and one-line, so readers skim updates quickly.