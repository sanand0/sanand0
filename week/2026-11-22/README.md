## Safer Backups, Better Evidence & Tools That Explain Themselves

This week’s changes made backups more trustworthy, tools easier to use, and research more careful about what its evidence can show. The common lesson: keep the original data, test the edge cases, and make uncertainty visible.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_This toolbox gained safer backups, clearer service checks, and sturdier media tools; apparently, even backups need backups._

- **More complete chat backups:** On 19–20 Nov 2026, [`chatcli backup`](https://github.com/sanand0/scripts/commit/779cc79) and [stream recovery](https://github.com/sanand0/scripts/commit/c22db62) can recover conversations from captured pages and completed streams. Takeaway: keep multiple evidence sources, but only combine them when their links are proven.
- **Cleaner podcast audio:** On 20 Nov 2026, [podcast caching](https://github.com/sanand0/scripts/commit/2489cbb) stores lossless segments before final encoding, preventing quality loss and accumulated gaps. Takeaway: cache intermediate work in a format that preserves the source.
- **Service problems made visible:** On 18 Nov 2026, [servicestatus](https://github.com/sanand0/scripts/commit/68e92fc) summarizes scheduled jobs, while [sync fixes](https://github.com/sanand0/scripts/commit/030b721) wait for network recovery. Takeaway: report failures where they happen, and treat temporary outages differently from broken jobs.
- **Fewer cross-device surprises:** On 18–20 Nov 2026, [Google backup](https://github.com/sanand0/scripts/commit/920fe1c) handles Unicode separators, [Plutonium sync](https://github.com/sanand0/scripts/commit/3fc6f7e) fixes file access, and [Tailscale Drive](https://github.com/sanand0/scripts/commit/4571a71) shares a folder. Takeaway: test file formats and permissions on the systems that actually use them.
- **Safer, clearer daily tools:** On 16–18 Nov 2026, [call](https://github.com/sanand0/scripts/commit/636325c) checks inputs early, [meetcall](https://github.com/sanand0/scripts/commit/e83dd85) explains inaccessible links, and [wabackup](https://github.com/sanand0/scripts/commit/271ae90) improves progress logs. Takeaway: fail early and tell users what they can do next.

### [sanand0/anand-chrome-tools](https://github.com/sanand0/anand-chrome-tools)

_The browser can now remember more of your work; no, it still cannot remember where you put that tab._

- **Passive conversation capture:** On 18–19 Nov 2026, [local ChatGPT and Claude backups](https://github.com/sanand0/anand-chrome-tools/commit/f0d58e7) save data the pages already receive, with separate opt-in controls. Takeaway: make data capture explicit and avoid extra requests when existing traffic will do.
- **Better recovery, fewer review chores:** On 19–20 Nov 2026, [capture reliability](https://github.com/sanand0/anand-chrome-tools/commit/43b98a1) records generation evidence, while [snapshot handling](https://github.com/sanand0/anand-chrome-tools/commit/5532b50) accepts newer complete data and removes manual review. Takeaway: preserve raw evidence, then automate only decisions supported by clear rules.
- **Annotations stay tied to work:** On 16 Nov 2026, [annotations](https://github.com/sanand0/anand-chrome-tools/commit/c10adbb) add notes to emails, calendar events, and chats; [tab titles](https://github.com/sanand0/anand-chrome-tools/commit/719b03b) separate custom labels from page titles. Takeaway: attach reminders to stable item IDs, not changing screen positions.

### [sanand0/talks](https://github.com/sanand0/talks)

_Recorded talks now come with richer ways to revisit them. The video player gets a speaking role, too._

- **An older talk gets video:** On 18 Nov 2026, [the AI Empirically talk](https://github.com/sanand0/talks/commit/7b65947) gained a video player, time links, and a smoother audio fallback. Takeaway: check captions and media timing together when combining recordings.
- **A new story about verification:** On 17–18 Nov 2026, [the SUTD talk](https://github.com/sanand0/talks/commit/466e695) and [its companion page](https://github.com/sanand0/talks/commit/7b65947) present a class on testing AI work and questioning test results. Takeaway: make the reasoning and evidence accessible after the live event.
- **More teaching material, not just slides:** On 15–16 Nov 2026, [the AIPL talk](https://github.com/sanand0/talks/commit/431de19) and [TDS ideation talk](https://github.com/sanand0/talks/commit/463a93e) added transcripts, sources, and interactive stories. Takeaway: pair a compelling narrative with links readers can inspect.

### [sanand0/skills](https://github.com/sanand0/skills)

_A new meeting-prep guide helps agents get ready; at last, someone wrote down what “be prepared” means._

- **A practical meeting-prep skill:** On 21 Nov 2026, [meeting-prep](https://github.com/sanand0/skills/commit/cd56385) prompts agents to find the meeting’s purpose, likely questions, and useful evidence. Takeaway: lead with what someone needs to know before they walk in.
- **A clearer laptop map:** On 21 Nov 2026, [anand-laptops](https://github.com/sanand0/skills/commit/cd56385) now maps common file locations without implying the machines are identical. Takeaway: document useful paths while leaving room for real differences.
- **Better skill discovery:** On 21 Nov 2026, the [skills index](https://github.com/sanand0/skills/commit/cd56385) lists the new guide and updates descriptions. Takeaway: a reusable tool works only if users can tell when to use it.

### [sanand0/tools](https://github.com/sanand0/tools)

_Conversation exports now keep more context, while repository data points at the right branch. Tiny links, large consequences._

- **Timestamps in prompt exports:** On 18 Nov 2026, [AI scrapers](https://github.com/sanand0/tools/commit/e1f9568) include available prompt times in Singapore time. Takeaway: carry timestamps with extracted content so readers can follow the conversation.
- **Readable plugin mentions:** On 18 Nov 2026, the [ChatGPT scraper](https://github.com/sanand0/tools/commit/e1f9568) turns long plugin links into simple `@Plugin Name` labels. Takeaway: simplify technical links without discarding the meaning users need.
- **Trending data from the current branch:** On 20 Nov 2026, [trending repositories](https://github.com/sanand0/tools/commit/9938c8e) switched its data source to `til`’s main branch. Takeaway: verify branch names whenever one project reads another project’s files.

### [sanand0/blog](https://github.com/sanand0/blog)

_The site got new ideas, images, and talk notes; the prompt fragments are learning to tell jokes, too._

- **A take on guardian agents:** On 16 Nov 2026, [a new post](https://github.com/sanand0/blog/commit/5dd4c74) argues for pairing specialized models with firm controls and independent review. Takeaway: separate an agent’s actions from the systems that check them.
- **Talks become readable stories:** On 15 Nov 2026, [a TDS talk post](https://github.com/sanand0/blog/commit/db6daee) and [weekly learning notes](https://github.com/sanand0/blog/commit/db6daee) added summaries and links. Takeaway: publish enough context for readers who missed the event.
- **Better comic prompts and article images:** On 16 Nov 2026, [image updates](https://github.com/sanand0/blog/commit/38bb3f8) added comic guidance and illustrations. Takeaway: give visual prompts a clear purpose, not just a preferred style.

### [sanand0/til](https://github.com/sanand0/til)

_One small discovery joined a growing list, and the weekly repository chart got a fresh batch of data._

- **A new learning note:** On 15 Nov 2026, [`til.md`](https://github.com/sanand0/til/blob/1da9da6/til.md) recorded a tea discovery. Takeaway: capture small observations while they are still fresh.
- **New LLM notes:** On 15 Nov 2026, [`llms.md`](https://github.com/sanand0/til/blob/1da9da6/llms.md) received six additions. Takeaway: keep a running notebook rather than relying on memory.
- **A fresh trending-repository snapshot:** On 15 Nov 2026, [`trending-repos.tsv`](https://github.com/sanand0/til/blob/1da9da6/trending-repos.tsv) added the week’s results. Takeaway: date snapshots so changing rankings stay interpretable.

### [sanand0/research](https://github.com/sanand0/research)

_One project catalogues a browser trick; another checks exercise form. Apparently, “looks right” benefits from receipts._

- **A guide to HTML in Canvas:** On 21 Nov 2026, [a new catalog](https://github.com/sanand0/research/commit/17e8fdef) explains techniques from an explainer and 15 demos. Takeaway: pair each technical trick with an example of where it could help.
- **A visible exercise-form lab:** On 19 Nov 2026, [push-up analysis](https://github.com/sanand0/research/commit/603b44d) compares pose models and displays joint angles over video. Takeaway: show evidence beside a score so people can check the judgment.
- **Results tested across methods:** On 19 Nov 2026, the [comparison](https://github.com/sanand0/research/commit/603b44d) checks several pose models, an ensemble, and a vision model. Takeaway: compare alternatives on the same examples before picking a default.

### [sanand0/infra](https://github.com/sanand0/infra)

_One investigation says to protect the data first; another explains why a music downloader can pick the wrong song._

- **Crash findings, with uncertainty intact:** On 20 Nov 2026, [the investigation](https://github.com/sanand0/infra/commit/ce7611e) documents disk errors but says the precise crash cause remains unknown. Takeaway: separate confirmed evidence from plausible explanations.
- **A concrete hardware warning:** On 20 Nov 2026, the [crash report](https://github.com/sanand0/infra/blob/ce7611e/system-crash/README.md) recommends backing up work and servicing the drive. Takeaway: act on repeated storage errors before they become data loss.
- **Safer music-download choices:** On 16 Nov 2026, [spotDL guidance](https://github.com/sanand0/infra/commit/4c5f1e5) explains automatic matching and direct video selection. Takeaway: verify the recording before downloading when the match matters.

### [sanand0/exam](https://github.com/sanand0/exam)

_An exam question now invites students to design the next question. The grading rubric has joined the experiment._

- **A prompt for better assessment ideas:** On 15 Nov 2026, [the ROE question](https://github.com/sanand0/exam/commit/61d58e2) asks for engaging tasks that need human input and can be graded automatically. Takeaway: state what good work must show before asking people to create it.
- **A separate live-game exam:** On 15 Nov 2026, [the AIPL Food Court exam](https://github.com/sanand0/exam/commit/61d58e2) validates signed results for its own scheduled sessions. Takeaway: bind submissions to the right activity and time window.
- **Quiz-aware grading:** On 15 Nov 2026, [receipt validation](https://github.com/sanand0/exam/blob/61d58e2/src/a-food-court-discount.js) now handles distinct exam IDs and schedules. Takeaway: pass context through every layer that validates a result.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_The price chart now waits for the real table, not the page’s loading skeleton. A patient scraper is a useful scraper._

- **Find columns by labels:** On 15 Nov 2026, [the downloader](https://github.com/sanand0/llmpricing/commit/b563cf9) locates model, score, and price columns by their headers. Takeaway: depend on meaningful labels instead of fixed column positions.
- **Better timeout clues:** On 15 Nov 2026, [download errors](https://github.com/sanand0/llmpricing/blob/b563cf9/download.py) now include the page title and missing data. Takeaway: include the last useful state in timeout messages.
- **A refreshed model comparison:** On 15 Nov 2026, [pricing data and docs](https://github.com/sanand0/llmpricing/commit/b563cf9) were updated alongside the more robust download path. Takeaway: keep data refreshes and their collection method documented together.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_The weekly podcast script weighs claims instead of repeating them unchallenged. Even a good story needs footnotes in spirit._

- **A new weekly group digest:** On 15 Nov 2026, [the podcast script](https://github.com/sanand0/generative-ai-group/commit/06702cd) added a two-host review of the week’s AI discussions. Takeaway: organize a digest around the ideas people can use, not a list of links.
- **Claims get useful caveats:** On 15 Nov 2026, the [script](https://github.com/sanand0/generative-ai-group/blob/06702cd/2026-11-15/podcast-2026-11-15.md) distinguishes reported findings from forecasts and disputed claims. Takeaway: label uncertainty before it turns into confident-sounding misinformation.
- **Practical lessons close the episode:** On 15 Nov 2026, the [closing dialogue](https://github.com/sanand0/generative-ai-group/blob/06702cd/2026-11-15/podcast-2026-11-15.md) returns to testing claims and limiting agent access. Takeaway: end a roundup with a habit listeners can apply.

### [sanand0/chatgpt-to-markdown](https://github.com/sanand0/chatgpt-to-markdown)

_A new renderer turns native conversation data into readable Markdown; JSON no longer has to be anyone’s bedtime reading._

- **Render captured snapshots:** On 19 Nov 2026, [`renderSnapshot`](https://github.com/sanand0/chatgpt-to-markdown/commit/03774cd) became a public API for complete native ChatGPT conversations. Takeaway: expose useful transformations as small, documented functions.
- **Follow the active conversation branch:** On 19 Nov 2026, [snapshot rendering](https://github.com/sanand0/chatgpt-to-markdown/blob/03774cd/chatgpt-to-markdown.js) preserves branch order and rejects incomplete captures. Takeaway: validate completeness before presenting a transcript as final.
- **Keep useful context in the export:** On 19 Nov 2026, [the renderer](https://github.com/sanand0/chatgpt-to-markdown/blob/03774cd/chatgpt-to-markdown.js) retains citations, timestamps, attachment labels, and image entries. Takeaway: preserve what readers need even when linked files are unavailable.

### [sanand0/llms-in-finance-book](https://github.com/sanand0/llms-in-finance-book)

_The book gained a full set of figures and a repeatable export path. The images now have their own paperwork._

- **Figures planned across chapters:** On 19 Nov 2026, [figure notes](https://github.com/sanand0/llms-in-finance-book/commit/b5f41f9) added placements, lead-ins, and captions. Takeaway: write the figure’s job before drawing it.
- **Reusable artwork files:** On 19 Nov 2026, [figure assets](https://github.com/sanand0/llms-in-finance-book/tree/b5f41f9/figures) include WebP images and supporting source formats. Takeaway: keep editable masters alongside files used in the book.
- **Repeatable Word exports:** On 19 Nov 2026, [the figure build](https://github.com/sanand0/llms-in-finance-book/blob/b5f41f9/justfile) converts WebP images for Word and packages the figures. Takeaway: automate format conversion instead of relying on manual cleanup.

### [sanand0/lightwell](https://github.com/sanand0/lightwell)

_Lightwell turns a browser camera into a small studio; yes, the camera now has a backstage crew._

- **A browser camera studio:** On 20 Nov 2026, [Lightwell](https://github.com/sanand0/lightwell/commit/1b85147) added a camera extension for changing the video sent to calls. Takeaway: make the output preview visible before sending it anywhere.
- **Mix and arrange scene layers:** On 20 Nov 2026, [the studio](https://github.com/sanand0/lightwell/blob/1b85147/studio.js) lets users combine camera, text, images, and drawings. Takeaway: keep source layers editable so users can adjust a scene later.
- **Test and document browser behavior:** On 20 Nov 2026, [browser tests](https://github.com/sanand0/lightwell/tree/1b85147/test) cover camera capture, while the [install guide](https://github.com/sanand0/lightwell/blob/1b85147/README.md) explains setup. Takeaway: test permissions and device behavior, not just the rendered picture.

### [sanand0/liveform](https://github.com/sanand0/liveform)

_Liveform now allows more question changes before responses arrive; the form gets a little room to grow up._

- **Flexible field changes before answers:** On 21 Nov 2026, [field conversion](https://github.com/sanand0/liveform/commit/3828446) allows field types to change before the first response. Takeaway: relax constraints when no user data is at risk.
- **Compact choice lists:** On 21 Nov 2026, [select presentation](https://github.com/sanand0/liveform/blob/3828446/README.md) adds dropdowns for single-choice questions without changing saved values. Takeaway: treat visual presentation separately from response meaning.
- **Safer live submissions:** On 21 Nov 2026, [submission checks](https://github.com/sanand0/liveform/blob/3828446/src/liveform/server.py) detect form changes before saving answers. Takeaway: check that the form still matches the page users submitted.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_The next course activity now has dates and a direct link; students need one less scavenger hunt._

- **GA5 dates updated:** On 16 Nov 2026, [the term schedule](https://github.com/sanand0/tools-in-data-science-public/commit/bcdcf14) moved the activity to 16–27 Nov. Takeaway: keep dates and linked assessments in the same update.
- **Direct exam access:** On 16 Nov 2026, the [course page](https://github.com/sanand0/tools-in-data-science-public/blob/bcdcf14/2026-09/README.md) now links to the GA5 exam. Takeaway: put the next action beside the schedule.
- **A clearer student path:** On 16 Nov 2026, the [updated table](https://github.com/sanand0/tools-in-data-science-public/blob/bcdcf14/2026-09/README.md) connects the activity, dates, and exam. Takeaway: make course logistics answer “what, when, and where” at a glance.

### [sanand0/private-research](https://github.com/sanand0/private-research)

_This research project emphasizes careful checks and limits; the numbers can wait until the evidence earns them._

- **A broad study inventory:** On 17 Nov 2026, [the TDS learning study](https://github.com/sanand0/private-research/commit/f5b4532) assembled course archives, scores, and game records. Takeaway: define the data sources before deciding what they prove.
- **Claims challenged and revised:** On 17 Nov 2026, the [analysis](https://github.com/sanand0/private-research/tree/f5b4532/2026-11-tds-learning) includes replication and adversarial checks. Takeaway: invite a serious attempt to disprove the headline finding.
- **A next experiment, not a sweeping claim:** On 17 Nov 2026, [the research plan](https://github.com/sanand0/private-research/tree/f5b4532/2026-11-tds-learning) proposes a prospective test with power analysis. Takeaway: turn uncertain findings into a testable next step.

## Lessons

- **Preserve evidence before interpreting it:** raw captures, complete source files, and visible proof make later checks possible.
- **Be precise about what changed:** a newer file, a successful test, and a proven result are different things.
- **Design for recovery:** atomic writes, backups, and clear failure messages reduce the cost of mistakes.
- **Make tools explain themselves:** good docs, useful logs, and direct links help people act without extra digging.
- **Measure the claim you care about:** a score or proxy can be useful without proving learning, quality, or cause.

## Suggestions

- Add an end-to-end test that turns a captured conversation into Markdown, then checks missing pages, edits, images, and citations.
- Track backup freshness and recovery status across scheduled jobs, so a successful run does not hide stale data.
- Test Lightwell with real meeting platforms and document any browser permission limits users encounter.
- For research projects, publish a concise methods note that separates verified results from open questions.