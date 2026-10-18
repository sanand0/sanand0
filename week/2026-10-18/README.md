## This week, safer automation came from clearer boundaries, better evidence, and useful small tools.

Across exams, AI workflows, and personal utilities, the strongest changes made systems easier to trust and use. The recurring lesson: verify important outcomes on the server, keep evidence close, and make the next step clear.

### [sanand0/exam](https://github.com/sanand0/exam)

_The exam now checks real work and protects student data; “I recorded it” finally needs an actual recording._

- **Authenticated audio offers:** Added Human Exchange recording and server-side audio checks tied to the student and question ([dbddd5f](https://github.com/sanand0/exam/commit/dbddd5fb688a91b05921c873f1b47dbbd08ca8a5)). This prevents typed claims from replacing uploads. Takeaway: verify important actions against the system that performed them.
- **Safer question links:** Bound short-lived launch tokens to specific markets and questions ([ac8565d](https://github.com/sanand0/exam/commit/ac8565d91b55f904f26ebc9c221ca3f3f0b6a396)). Students now get clearer warnings about sharing codes. Takeaway: limit each credential to one job and explain its risks.
- **Preview before grading:** Added a separate grading window, so students can read and draft before checks open ([99bbeb7](https://github.com/sanand0/exam/commit/99bbeb77e56a92a281321824f32364eeb420bae6)). The server enforces the schedule. Takeaway: treat browser controls as help, not security.
- **Private results, clearer saves:** Restricted answer access, restored authenticated downloads, and returned the score actually saved ([52b8786](https://github.com/sanand0/exam/commit/52b878608b99715d17c4b6156513077d858bb97f), [70c40a7](https://github.com/sanand0/exam/commit/70c40a7b296b10e3f3341f5b3363f561f26987c6), [33770be](https://github.com/sanand0/exam/commit/33770bec37996ca739349e718997c2274af4549d)). Takeaway: return receipts that match stored results.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Tiny scripts now survive failures, phone swaps, and overheated laptops—three classic plot twists._

- **Persistent usage readings:** The AI usage panel restores its last good values after restarts, while Claude usage uses existing credentials ([12ee88e](https://github.com/sanand0/scripts/commit/12ee88ea699fce91d3ce9c127c2f9c1e196ca6ef), [4097c0d](https://github.com/sanand0/scripts/commit/4097c0deb41b53c65e530f5c96572845c11128dd)). Takeaway: keep useful old data visible when fresh checks fail.
- **Phone music sync:** Added resumable Android music syncing, with safe reporting and optional deletion of extra MP3s ([748442f](https://github.com/sanand0/scripts/commit/748442ff1ba318acdb1c8db2c271b01fd6e39b4e)). Takeaway: make destructive cleanup opt-in.
- **Monthly Google backups:** Split archives by month, migrated existing files, and added another account to scheduled backups ([419f9f0](https://github.com/sanand0/scripts/commit/419f9f07b1dafbeea4300493b32b46a1197475fa)). Takeaway: partition growing archives and make migrations repeatable.
- **Gentler local tools:** Limited ffmpeg read speed to reduce heat and mounted all scripts read-only in development containers ([276a983](https://github.com/sanand0/scripts/commit/276a983a8afe142cc1edfab63e4483d802fa3e4f), [7861e53](https://github.com/sanand0/scripts/commit/7861e5321b411aac77bdb04ae6d8f28b25e7ebd3)). Takeaway: set resource limits before your laptop sets them for you.

### [sanand0/llms-in-finance-book](https://github.com/sanand0/llms-in-finance-book)

_The book’s new chapters favor evidence over impressive-sounding claims. Legal work is hard enough without invented certainty._

- **Expanded the manuscript:** Added drafts on credit, banking research, fund operations, insurance claims, and contract policy checks ([3d8d6f5](https://github.com/sanand0/llms-in-finance-book/commit/3d8d6f53d5247a8c78302162693f203f513e0ad1), [38e3935](https://github.com/sanand0/llms-in-finance-book/commit/38e39357b794912465839083c7b477399911e8c4), [38b95f0](https://github.com/sanand0/llms-in-finance-book/commit/38b95f0477fa5ba578d5ba7b2bb831ef7bd7daa0), [660261a](https://github.com/sanand0/llms-in-finance-book/commit/660261aa949a9941205dd3f9d0337b6fc50296a1), [6ef6eac](https://github.com/sanand0/llms-in-finance-book/commit/6ef6eaced2e6144ee1b17e306f8c9165b11cd28b)). Takeaway: build each chapter around a distinct finance problem.
- **Added skeptical reviews:** Checked chapter claims, examples, privacy, and regulatory details against source dossiers ([c4631c7](https://github.com/sanand0/llms-in-finance-book/commit/c4631c70efe2236cbaadfc4eb33cc17b2ab516c9), [20e675b](https://github.com/sanand0/llms-in-finance-book/commit/20e675b3598058daa4a2175fddebd06b97b19951), [92a6121](https://github.com/sanand0/llms-in-finance-book/commit/92a61215d8bd6fbd5ccb3baa51bb510ae0d83988), [ae9c419](https://github.com/sanand0/llms-in-finance-book/commit/ae9c4190b95d98685a9645fa8db693ca383a2a8f), [0fc9196](https://github.com/sanand0/llms-in-finance-book/commit/0fc919649430941abe3e4cb2fcaeb7de62301cf8)). Takeaway: review claims as carefully as prose.
- **Set a staged workflow:** Added runbooks that defer companion exercises and images until the chapters are complete ([c8991fb](https://github.com/sanand0/llms-in-finance-book/commit/c8991fb3711976331a34e6d24f81f0426b6446ff)). Takeaway: separate manuscript work from later production assets.

### [sanand0/blog](https://github.com/sanand0/blog)

_This week’s writing asks what exams should teach when agents can help—and what still counts as learning._

- **Exam design principles:** Published a post on testing learning, answer-sharing, reusable solvers, cheating, and evaluation ([3aec396](https://github.com/sanand0/blog/commit/3aec396dddf938a0dbf3523cc1a4e14f6f0a38b3), [2181ac8](https://github.com/sanand0/blog/commit/2181ac84ecb458e63b4a86b59782f10a82be41e5)). Takeaway: test whether a question teaches the skill it claims to measure.
- **Weekly learning, in public:** Added notes on Python, browser transcription, model experiments, and lessons from mistakes ([8f340a0](https://github.com/sanand0/blog/commit/8f340a00c3c5d36abf039897c40ab3a1578e6cc0)). Takeaway: publish observations with enough context to revisit them.
- **Sharper advice and stories:** Updated AI advice and added posts on translation workflows and a playful Scrabble reconstruction ([c4631b6](https://github.com/sanand0/blog/commit/c4631b62f0c85a50e7de653aec875e40e894e37a), [fafbaa8](https://github.com/sanand0/blog/commit/fafbaa81668995c95674727ec32bc71caf44437b), [477f7fd](https://github.com/sanand0/blog/commit/477f7fd98cc48c4ee3afc76f4cbe9deaa9586a6e)). Takeaway: use examples to make abstract advice memorable.

### [sanand0/tds-evidence-exchange](https://github.com/sanand0/tds-evidence-exchange)

_A classroom marketplace game is becoming a careful test of evidence, cooperation, and grading—not just a pile of invoices._

- **Built the evidence game:** Added a Worker platform, deterministic case generation, student guides, and evidence retrieval with signed codes ([18c54b6](https://github.com/sanand0/tds-evidence-exchange/commit/18c54b606cc7f9fecbd1c6dfd3fb742bf752d1cd), [e1439e9](https://github.com/sanand0/tds-evidence-exchange/commit/e1439e952ae38f20dfd1612c159d4f10f5b47544), [a4e9c87](https://github.com/sanand0/tds-evidence-exchange/commit/a4e9c8797727367246ce744f41e86aa29935565d)). Takeaway: make evidence traceable from student action to review.
- **Added submission and defense:** Students can submit decisions, explain reasoning, and respond to later evidence, including audio ([f2408a5](https://github.com/sanand0/tds-evidence-exchange/commit/f2408a543407ffa2257d414ae4e0db83df49e0c8)). Takeaway: assess both the answer and how it changes when evidence changes.
- **Tested the game in staging:** Added isolated runs, calibration tools, and protections against exposing answer keys ([10c5e23](https://github.com/sanand0/tds-evidence-exchange/commit/10c5e23dc91817d1cdbd5a769229cfd8a13bcf4a), [fe4863c](https://github.com/sanand0/tds-evidence-exchange/commit/fe4863c1dc7694acd2971cb5a8ffffbc3849369e)). Takeaway: test realistic flows without using live student records.
- **Refined grading and recovery:** Improved evidence checks, case recovery, and the final review process across later calibration rounds ([05ec546](https://github.com/sanand0/tds-evidence-exchange/commit/05ec54622081b69bde32e0c4d299320f0921f958)). Takeaway: calibrate the scorer against edge cases before treating scores as meaningful.

### [sanand0/talks](https://github.com/sanand0/talks)

_Three archival talks now have richer story pages. History still benefits from a good link and a less-confident caption._

- **Published three talk stories:** Added pages for election visualizations, educational opportunity, and multimodal actor search ([d00bda4](https://github.com/sanand0/talks/commit/d00bda4fe5810e92c976fb26eb0d6912fd13396f), [6ca1a97](https://github.com/sanand0/talks/commit/6ca1a978243924a5f42976310b2f974957dd876a), [341aa9d](https://github.com/sanand0/talks/commit/341aa9df97bd213b0c80f1c84a27fb8d756ebe4d)). Takeaway: connect a talk’s claims to the sources readers can inspect.
- **Prepared transcript and research records:** Added transcripts, source notes, and careful checks on dates, claims, and video choices ([d981cf6](https://github.com/sanand0/talks/commit/d981cf65d1cde9a02e25b7a5f2264f037e4e0d68), [2a9ff83](https://github.com/sanand0/talks/commit/2a9ff83ed9a6d80ba7306e2b6c326dc272b49a22)). Takeaway: distinguish what speakers said from what later research supports.
- **Made archive entries easier to use:** Linked story pages, transcripts, and verified audio while preserving existing catalog titles ([6ca1a97](https://github.com/sanand0/talks/commit/6ca1a978243924a5f42976310b2f974957dd876a)). Takeaway: keep stable archive metadata separate from creative page headlines.
- **Added a new course-design story:** Published a public account of designing exams for learning with agents and peers ([b57df17](https://github.com/sanand0/talks/commit/b57df170e570a33352da0dd08e9722fc944ac590)). Takeaway: show the design debate, not only the polished result.

### [sanand0/tds-network-games](https://github.com/sanand0/tds-network-games)

_Launch tokens now know which question they belong to. Apparently, a token that opens every door is a feature only until it isn’t._

- **Scoped exam access:** Bound prediction sessions and audio submissions to signed, question-specific tokens ([2b1c1ac](https://github.com/sanand0/tds-network-games/commit/2b1c1ac9913779e7b9c4eb0840d6bd90296003af)). Takeaway: bind credentials to the exact resource they should access.
- **Timed audio submissions:** Added question-level opening and closing times, plus a two-minute upload grace period ([2b1c1ac](https://github.com/sanand0/tds-network-games/commit/2b1c1ac9913779e7b9c4eb0840d6bd90296003af)). Takeaway: enforce deadlines on the server and document the grace rule.
- **Built a detailed cost market:** Added a weekly AI Pipe prediction market with 17 settlement ranges and rolling-feed safeguards ([6a98830](https://github.com/sanand0/tds-network-games/commit/6a98830a9865371078d21d6c1f29e29c866956b1)). Takeaway: preserve source dates and missing data when turning live feeds into scores.
- **Added Human Exchange recordings:** Created a timed offer question, practice mode, and browser tests for the recording flow ([f3d76a3](https://github.com/sanand0/tds-network-games/commit/f3d76a3b3f60123b130c5f2a1b704c5a3f565353)). Takeaway: test recording, retries, and deadlines together.

### [sanand0/infra](https://github.com/sanand0/infra)

_This week’s infra work ranged from why a machine shut down to how a phone can become a well-documented test device._

- **Found a thermal shutdown:** Documented a confirmed critical-temperature shutdown while keeping the earlier crash’s exact cause uncertain ([341aa9d](https://github.com/sanand0/infra/commit/341aa9df97bd213b0c80f1c84a27fb8d756ebe4d)). Takeaway: separate confirmed evidence from the most plausible explanation.
- **Benchmarked phone-control tools:** Added repeatable tests comparing Android MCP tools on task success, speed, cost, and device cleanup ([6a05533](https://github.com/sanand0/infra/commit/6a055330f8857b083d1a705c77f5baf6b50fcbea)). Takeaway: compare tools against real tasks, not feature lists.
- **Documented Android file transfer:** Recorded a tested way to locate an MTP phone mount and safely copy music files ([1b3496e](https://github.com/sanand0/infra/commit/1b3496eb781282a05d16658d002cd85e33a44440)). Takeaway: verify copy procedures on a small sample first.
- **Investigated GNOME recovery:** Traced an extension startup failure to a duplicate user-installed extension and documented a rollback path ([a4fd57b](https://github.com/sanand0/infra/commit/a4fd57bab104fa7e3ca7ea0c360a336413e6e7f9)). Takeaway: diagnose the underlying trigger before automating a restart.

### [sanand0/tools](https://github.com/sanand0/tools)

_The utilities got more useful in small ways: darker mail, more music controls, and a workaround for Meet’s picky file picker._

- **Improved dark mode:** Added themes for Gmail messages and formatting surfaces, with tests for varied content ([b53fe5f](https://github.com/sanand0/tools/commit/b53fe5ffd8d4bcce05ae90c08e8448e64b267cc1), [8c9f85f](https://github.com/sanand0/tools/commit/8c9f85f76fc85f51e83dac47e81bb7d0a87c3387)). Takeaway: scope visual changes narrowly and test real page states.
- **Added Meet MP4 backgrounds:** Created a bookmarklet that extends Google Meet’s upload filter and documents its unofficial nature ([9de79d2](https://github.com/sanand0/tools/commit/9de79d2245e8c2ba37c54f8efd2b89a5bd3e18b5)). Takeaway: label browser workarounds as fragile, not official support.
- **Refined local music playback:** Replaced native seeking with keyboard-friendly controls and expanded tests for playback behavior ([54f1ec0](https://github.com/sanand0/tools/commit/54f1ec0e4776f29a0afd160f455c7df28aca1bbb)). Takeaway: test interactions, not just whether a control appears.
- **Added Wallhop:** Added a small bookmarklet to open a page through Wallhop for a one-time read ([944cb4d](https://github.com/sanand0/tools/commit/944cb4d6a6cc70f663e4e1d02273aa2984faca72)). Takeaway: keep single-purpose tools simple to install and explain.

### [sanand0/research](https://github.com/sanand0/research)

_The experiments now include a mobile sensor lab and a game walkthrough. Curiosity remains a surprisingly good test plan._

- **Built a mobile capability monitor:** Added an offline page for checking browser sensors, media, permissions, and device APIs ([2b6036c](https://github.com/sanand0/research/commit/2b6036c4cd309aaea2a4a2f199525a36adeb21ee)). Takeaway: report device and permission limits alongside readings.
- **Made Python’s game explorable:** Added an upstream-derived walkthrough with reference solutions and browser checks ([473f8c9](https://github.com/sanand0/research/commit/473f8c92be5aa1caf532e942352d5fd3703e0bf7)). Takeaway: pin source versions when turning software into a learning guide.
- **Compared constrained runtimes:** Built one JSON inspection service for native, scratch Docker, WASI, and other runtime experiments ([4d8ae4e](https://github.com/sanand0/research/commit/4d8ae4e4155014228617c44ea57ea21e2a4c28f6)). Native, Docker, and WASI passed; other environments still need host setup. Takeaway: report blocked tests as blocked, not passed.
- **Refreshed research indexes:** Added the new mobile experiment to the project catalog ([2b6036c](https://github.com/sanand0/research/commit/2b6036c4cd309aaea2a4a2f199525a36adeb21ee)). Takeaway: keep discovery pages current as experiments grow.

### [sanand0/llmevals](https://github.com/sanand0/llmevals)

_The multiplication benchmark reaches 50 digits, where token budgets sometimes become the plot._

- **Tested large-number multiplication:** Added a reproducible evaluation across models, operand sizes, and output limits ([73f5356](https://github.com/sanand0/llmevals/commit/73f535601da5d9d27d3328ee1b4791f3d5b6854b)). Takeaway: separate math mistakes from empty or failed responses.
- **Made runs resumable:** Stored each attempt so interrupted evaluations can resume without repeating successful calls ([73f5356](https://github.com/sanand0/llmevals/commit/73f535601da5d9d27d3328ee1b4791f3d5b6854b)). Takeaway: key cached results by the exact prompt and test case.
- **Added cost-aware reporting:** Recorded a dated price snapshot and generated summaries from raw responses ([73f5356](https://github.com/sanand0/llmevals/commit/73f535601da5d9d27d3328ee1b4791f3d5b6854b)). Takeaway: label price estimates with their source and date.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Leaderboard updates now say what changed, which is more helpful than “trust us, the chart moved.”_

- **Recovered leaderboard downloads:** Replaced the browser automation path with direct Chrome DevTools Protocol handling and clearer timeouts ([6243bd3](https://github.com/sanand0/llmpricing/commit/6243bd3756f8de4e1760fe2f32810b3967638e52)). Takeaway: report connection failures separately from page-load failures.
- **Improved update visibility:** Added a change summary for added, edited, removed, and unchanged model rows ([6243bd3](https://github.com/sanand0/llmpricing/commit/6243bd3756f8de4e1760fe2f32810b3967638e52)). Takeaway: make automated data changes easy to review.
- **Added offline tests:** Covered download errors and row updates without requiring live leaderboard requests ([6243bd3](https://github.com/sanand0/llmpricing/commit/6243bd3756f8de4e1760fe2f32810b3967638e52)). Takeaway: test failure paths before the next scheduled refresh.

### [sanand0/til](https://github.com/sanand0/til)

_This week’s notes capture a useful mix of ideas, small discoveries, and one very human laptop-cooling strategy._

- **Collected new AI observations:** Added notes on reusable examples, coding agents, transcription, and model infrastructure ([0703959](https://github.com/sanand0/til/commit/0703959302622e20b45b09d6c8fd3b7d9deaa523)). Takeaway: record a thought while its source is still easy to find.
- **Added Python 3.15 learnings:** Summarized frozen dictionaries, unpacking comprehensions, UTF-8 defaults, lazy imports, and sentinels ([0703959](https://github.com/sanand0/til/commit/0703959302622e20b45b09d6c8fd3b7d9deaa523)). Takeaway: link language notes to their proposals.
- **Refreshed weekly trending repositories:** Added a new snapshot with repository descriptions and counts ([0703959](https://github.com/sanand0/til/commit/0703959302622e20b45b09d6c8fd3b7d9deaa523)). Takeaway: date snapshots so fast-moving lists stay interpretable.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_The weekly podcast tackled reasoning claims and tool evaluations. Yes, apparently benchmark debates now get a two-host show._

- **Published a new episode:** Added the podcast script for the week ending 11 October ([ec1c4ec](https://github.com/sanand0/generative-ai-group/commit/ec1c4ecbc76af6712ca585938f3dd8fd97883f0e)). Takeaway: keep the release tied to a clear week-ending date.
- **Explained symbolic checks:** The episode discusses pairing language models with explicit facts and rules for verifiable work ([ec1c4ec](https://github.com/sanand0/generative-ai-group/commit/ec1c4ecbc76af6712ca585938f3dd8fd97883f0e)). Takeaway: use rules where the evidence supports precise checks.
- **Kept claims qualified:** The script distinguishes small benchmark results and reported experiences from broad conclusions ([ec1c4ec](https://github.com/sanand0/generative-ai-group/commit/ec1c4ecbc76af6712ca585938f3dd8fd97883f0e)). Takeaway: say what a test measured before sharing its winner.

### [sanand0/aipipe](https://github.com/sanand0/aipipe)

_A public usage feed makes a prediction market possible without turning user-level billing data public._

- **Published UTC usage snapshots:** Added a scheduled, six-hourly JSON report covering seven days of provider costs and token counts ([c1e17e9](https://github.com/sanand0/aipipe/commit/c1e17e95995cb680ef588de3317d3c0d75b87a81)). Takeaway: publish dated aggregates for time-sensitive comparisons.
- **Protected user privacy:** The report shares counts and totals, not individual emails, while excluding free and native-key usage ([c1e17e9](https://github.com/sanand0/aipipe/commit/c1e17e95995cb680ef588de3317d3c0d75b87a81)). Takeaway: define what public metrics include and exclude.
- **Tested reporting edge cases:** Added checks for provider totals, scheduled snapshots, and streamed usage records ([c1e17e9](https://github.com/sanand0/aipipe/commit/c1e17e95995cb680ef588de3317d3c0d75b87a81)). Takeaway: preserve the last meaningful usage event when streams end with empty data.

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

_The demo catalog grew again. Review flags are a sensible counterweight to a list that grows faster than anyone can inspect it._

- **Added new demos:** Expanded the catalog across finance, coding, media, and AI agents ([975274f](https://github.com/sanand0/llmdemos/commit/975274fa8782eedcc79082ba24806e725c508fed)). Takeaway: show the actual demo and its source repository.
- **Marked entries for review:** New additions are flagged for human checking before they are treated as approved examples ([975274f](https://github.com/sanand0/llmdemos/commit/975274fa8782eedcc79082ba24806e725c508fed)). Takeaway: make review status visible in growing catalogs.
- **Recorded branding metadata:** Added fields to distinguish branded projects from general demos ([975274f](https://github.com/sanand0/llmdemos/commit/975274fa8782eedcc79082ba24806e725c508fed)). Takeaway: track provenance and affiliations as structured data.

### [sanand0/aibuilders](https://github.com/sanand0/aibuilders)

_The discussion archive now links claims, notes, and video moments more tightly. A transcript clock that disagrees with the video is not a small detail._

- **Added the fourth network session:** Created session notes and claims for a discussion on reusable tools, product benchmarks, and spatial simulations ([5906a74](https://github.com/sanand0/aibuilders/commit/5906a74543de381c0f6f9525db48392d9a76a7be)). Takeaway: preserve evidence before writing summaries.
- **Aligned transcript timestamps:** Added a migration tool that corrects transcript offsets without shifting already-correct claim timestamps ([5906a74](https://github.com/sanand0/aibuilders/commit/5906a74543de381c0f6f9525db48392d9a76a7be)). Takeaway: keep time corrections explicit and repeat-safe.
- **Validated captured screenshots:** Added checks linking video frames to structured evidence and playable timestamps ([5906a74](https://github.com/sanand0/aibuilders/commit/5906a74543de381c0f6f9525db48392d9a76a7be)). Takeaway: make every screenshot traceable to its source moment.

## Lessons

- **Trust needs an independent check:** A server-confirmed recording, saved-score receipt, or source-linked claim is stronger than a polished interface.
- **Measure the whole workflow:** Include missing outputs, delays, costs, privacy, and failure recovery—not only successful model answers.
- **Treat uncertain evidence honestly:** A blocked runtime, unverified dataset, or inconclusive incident should stay labeled that way.
- **Make automation reviewable:** Change summaries, dated snapshots, explicit scopes, and reproducible tests help people spot mistakes early.
- **Small tools benefit from guardrails:** Safe defaults, optional deletion, scoped credentials, and bounded resource use prevent avoidable trouble.

## Suggestions

- **Finish the exam grading-window workflow:** Add instructor checks for reused server-side question IDs and run an end-to-end preview-to-grading test.
- **Calibrate before using the exchange game for decisions:** Review scoring against independent examples, then record what the test does and does not establish.
- **Complete the book’s remaining chapters:** Extend the validator and build steps before treating new chapters as fully checked.
- **Add a continuous data-integrity check:** Validate public usage snapshots, leaderboard changes, and catalog links automatically after updates.
- **Document recovery and privacy limits:** State retention periods, rollback steps, and credential risks beside the relevant tools and workflows.