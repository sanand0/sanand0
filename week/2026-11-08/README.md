## Safer Tools, Better Tests, and More Useful Learning

This week’s work made everyday tools safer, easier to use, and more honest about what their results prove. The strongest lesson: test the whole workflow, including the assumptions and checks around it.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_The scripts now handle cross-platform edge cases, streamline daily tasks, and make agent workflows easier to inspect; yes, another picker._

- **Windows-safe transcript saves** (07 Nov 2026): The [atomic writer](https://github.com/sanand0/scripts/blob/main/call) now closes temporary files before replacing notes, with a regression test in [test_call.py](https://github.com/sanand0/scripts/blob/main/tests/test_call.py) ([commit](https://github.com/sanand0/scripts/commit/f92f26dcfa4d232a54238473d66c621e8115bc36)). Takeaway: test file replacement on the operating systems you support.
- **Resumable ChatGPT exports** (06 Nov 2026): Added [`chatgpt-export`](https://github.com/sanand0/scripts/blob/main/chatgpt-export) for large downloads that can resume and verify their archives ([commit](https://github.com/sanand0/scripts/commit/b8c830a2325916e0a72297c3aecdb358b9cf21cf)). Takeaway: make long transfers resumable, then verify the finished file.
- **Handier machine workflows** (05–06 Nov 2026): Added a [Plutonium sync shortcut](https://github.com/sanand0/scripts/blob/main/setup.fish), improved [Linux window controls](https://github.com/sanand0/scripts/blob/main/setup/linux.md), and documented a clearer [transcription workflow](https://github.com/sanand0/scripts/blob/main/agents/anand-laptops/SKILL.md) ([sync](https://github.com/sanand0/scripts/commit/da2f4b773be9c336e16d7bb77fc8fa507f8542f8), [setup](https://github.com/sanand0/scripts/commit/153b4d2818e5a39a8ef1613c94916d48f42ffee8), [workflow](https://github.com/sanand0/scripts/commit/e6322444014890b976a6852b5aa46119f25dc92e)). Takeaway: put repeated steps behind simple, documented commands.
- **Better agent-session review** (03–04 Nov 2026): [`agentlog.py`](https://github.com/sanand0/scripts/blob/main/agentlog.py) can extract prompts and resume sessions; updated guidance protects validation, accessibility, and security ([feature](https://github.com/sanand0/scripts/commit/6ca6ffd76c566c8f693ad5d5c64cc62f5435a59e), [safety rules](https://github.com/sanand0/scripts/commit/6f576032b0e3963b7cc7c595567a9296ebf9e817)). Takeaway: keep useful shortcuts, but never shortcut checks that prevent harm.
- **Picker and media fixes** (03 Nov 2026): Rofi actions gained clearer choices and broader tests, while video compression now shows progress and thermal pauses ([Rofi](https://github.com/sanand0/scripts/commit/6b07917a4e90c28e1c2ccba4109574c19a6d1301), [compression](https://github.com/sanand0/scripts/commit/5a9aa95d07cf7a9b8484b2047b80a22b37ad8808)). Takeaway: visible progress makes background work easier to trust.

### [sanand0/blog](https://github.com/sanand0/blog)

_The blog turns real work and classroom experiments into practical lessons; apparently even toenails can become a case study._

- **Agent skills from real usage** (02–06 Nov 2026): New guides cover specifying and checking agent work, reviewing outputs, selection bias, and exploring options before settling on an approach ([specify and verify](https://github.com/sanand0/blog/commit/a31b72b99af799b378576ba01e5d7d3d1d7b57cd), [review](https://github.com/sanand0/blog/commit/cb45c8217f605f4406576d8e638fb052c915e0ce), [selection checks](https://github.com/sanand0/blog/commit/2960a09c714afab052b0c27823b4cac8dcb493e8), [possibility scan](https://github.com/sanand0/blog/commit/bdab6aa4876d4e48cc0dbf8929b5142b91a2286b)). Takeaway: build reusable advice from observed successes and failures.
- **A student-story experiment** (07 Nov 2026): A new post compares originality, understanding, and preference in wordless picture stories ([post](https://github.com/sanand0/blog/commit/936a0f60887f08b7a3e0f92ebe27937f79992f13)). Takeaway: measure different outcomes separately; one score rarely tells the whole story.
- **More talk and project write-ups** (02–07 Nov 2026): Added posts on visualization teaching, AI review, creative work, and productivity ([talks](https://github.com/sanand0/blog/commit/555afa3f7225cc49a420b71f6334575a412d212c), [innovations](https://github.com/sanand0/blog/commit/880264bb18cef93851b336b2590d8e8df9b78f49), [other posts](https://github.com/sanand0/blog/commit/e53effb8156d0cc17af808f8457667b7d7920462)). Takeaway: explain the evidence and its limits alongside the conclusion.
- **Sharper prompts and notes** (07 Nov 2026): Updated a weekly course-analysis prompt and added practical actions to a book list ([prompt](https://github.com/sanand0/blog/commit/70fda81805513ee4e9d7fa047e68e77a0652a7cb)). Takeaway: turn reading into small, testable next steps.

### [sanand0/private-research](https://github.com/sanand0/private-research)

_The research work emphasizes careful evidence and reproducible checks; a good reminder that “the button worked” is not a full study._

- **A practical guide to mid-run steering** (07 Nov 2026): Archived browser trials with a decision guide, event evidence, and clear limits on what the tests show ([guide](https://github.com/sanand0/private-research/commit/c43bb5eee7c21911109f14fd8b9d2f45d88803f0)). Takeaway: define what counts as proof before running an experiment.
- **Speaker-labeling experiments** (06 Nov 2026): Added tools to compare diarization methods against held-out speech and labeled captions ([research](https://github.com/sanand0/private-research/commit/e44b8056b028c8ac237c709db637eb414dd79e72)). Takeaway: keep calibration data separate from the data used to judge results.
- **Agent-time analysis** (06 Nov 2026): Added an analysis of agent turns and session lengths, including data-quality checks ([report](https://github.com/sanand0/private-research/commit/2ec986dbbe0e56646cc92ee5b0363d6c80507014)). Takeaway: publish measurement rules with summaries, not just headline numbers.

### [sanand0/exam](https://github.com/sanand0/exam)

_Exam changes make grading rules clearer and receipts more reliable; even a zero can be a valid result._

- **Picture Stories grades explained** (07 Nov 2026): Clarified the creator-heavy score split and how signed results reach the exam ([instructions](https://github.com/sanand0/exam/commit/b6e2d33808c4ba242f33698425c84b0ae08f9c68)). Takeaway: show learners how each part of a score is calculated.
- **Valid zero-score receipts accepted** (07 Nov 2026): The exam now accepts an authentic Picture Stories receipt even when it records zero marks ([code and test](https://github.com/sanand0/exam/commit/51c46c9facd2d1897ed3b71f2922f090ee0fd0c6)). Takeaway: separate proof that a receipt is genuine from the score it contains.
- **A short podcast exercise added** (07 Nov 2026): Added an independent, time-limited set of activities, including one ungraded prediction task ([assessment](https://github.com/sanand0/exam/commit/fd10a98ea0fd5e7fd7ada5a3864e516bd9ba9178)). Takeaway: state clearly which activities count toward grades.

### [sanand0/tailrun](https://github.com/sanand0/tailrun)

_Tailrun grew into a private browser-tools runner with uploads, logs, and tighter boundaries; one server is enough trouble already._

- **Standalone tools dashboard** (07 Nov 2026): Added a private command runner, job history, a YouTube tool, and a remote text editor ([initial app](https://github.com/sanand0/tailrun/commit/957594ff3e5c07b5c0383fdcd4991558b2107158)). Takeaway: keep powerful tools behind a private, authenticated service.
- **Audio and video transcription** (07 Nov 2026): Added uploads that convert recordings and save transcripts, with tests for file types and output handling ([feature](https://github.com/sanand0/tailrun/commit/795024438db49aebd4d781da742b7fe59dd72dfc)). Takeaway: validate uploads before processing them.
- **One private route for app and API** (07 Nov 2026): Consolidated delivery behind Tailscale Serve and restricted which files the server can expose ([deployment](https://github.com/sanand0/tailrun/commit/d855de068584ef7eb2aabdeb23a32c90b93cb4cc)). Takeaway: reduce deployment parts, but keep static-file access allowlisted.
- **More compact job history** (07 Nov 2026): Job rows now take less space, and the new setup has browser tests ([UI](https://github.com/sanand0/tailrun/commit/feb34ec28916b4c25289a678ac00ec284872db47)). Takeaway: make frequent status checks quick to scan.

### [sanand0/talks](https://github.com/sanand0/talks)

_The talks now carry their evidence into pages people can revisit; transcripts are useful, but videos still settle what happened._

- **A class on testing designs and apps** (04 Nov 2026): Published a teaching session with its transcript, recordings, and examples ([talk](https://github.com/sanand0/talks/commit/00dadd330086b897ae3272793fb46b54c403adba)). Takeaway: ask learners to state what they would test and what failure looks like.
- **A course-design discussion** (02 Nov 2026): Added a session about teaching when agents can solve exam tasks ([talk](https://github.com/sanand0/talks/commit/8fc4998078807ab21dc901a65ed3fd82f55e4738)). Takeaway: assess useful judgment, not just whether a task resists automation.
- **A workshop on checking AI cheaply** (25 Oct 2026): Published a session about spending limited review effort wisely ([talk](https://github.com/sanand0/talks/commit/56bc79d3a096f8aba970717042aed9def2f8d274)). Takeaway: compare review cost with the harm a mistake could cause.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_The model chart now explains its labels and gaps more carefully; a missing price is better than pretend precision._

- **Model data refreshed** (01 Nov 2026): Updated the model list and comparison data ([data update](https://github.com/sanand0/llmpricing/commit/85e29e89754a28b9f13353102a4b337a98bf2ef0)). Takeaway: keep comparisons current and preserve a defensible source for each value.
- **Chart dates update with builds** (01 Nov 2026): The build now updates the README date and has a fallback when `just` is unavailable ([build update](https://github.com/sanand0/llmpricing/commit/a680bc84e09a56e281fe73a400346cd8f32e5b5a)). Takeaway: automate small freshness details so they do not drift.
- **Clearer intelligence labels** (01 Nov 2026): Renamed chart levels and fixed empty categories that broke the page ([chart fix](https://github.com/sanand0/llmpricing/commit/39f8b1fb79fcb009f0ca15c71e9c7727153ad050)). Takeaway: test boundary cases, including categories with no matching data.

### [sanand0/homework](https://github.com/sanand0/homework)

_The Mistake Lab turns common maths errors into short experiments; apparently wrong answers can be excellent teaching assistants._

- **Three interactive maths lessons** (03 Nov 2026): Added fraction, percentage, and equation activities for middle-school learners ([lessons](https://github.com/sanand0/homework/commit/32aa5dd0e2d9607c4f594f7267310581990d51ee)). Takeaway: build each lesson around one misconception learners can test.
- **A consistent learning path** (03 Nov 2026): Shared tools support prediction, hands-on experiments, explanation, and fresh practice ([shared library](https://github.com/sanand0/homework/blob/main/assets/lib.js)). Takeaway: ask learners to transfer an idea to a new example.
- **A simpler static deployment** (03 Nov 2026): Added `.nojekyll` so GitHub Pages serves the site without Jekyll processing ([deployment change](https://github.com/sanand0/homework/commit/c9ea899ebe41e04a98e0ea3e7b58318f354fa2d3)). Takeaway: use the simplest hosting setup that fits the product.

### [sanand0/liveform-data](https://github.com/sanand0/liveform-data)

_The classroom form now gathers both predictions and peer feedback; recording audio is not the same as automatically transcribing it._

- **A broader classroom form** (04 Nov 2026): Added questions about chart checks, visual comparisons, and testing phone apps ([form](https://github.com/sanand0/liveform-data/commit/af2130f823bd86d077508c0bd7cf53fe968bf69b)). Takeaway: collect a learner’s reason, not only their choice.
- **Peer feedback made actionable** (04 Nov 2026): Added short audio reviews and a transcript workflow that skips existing transcripts ([workflow](https://github.com/sanand0/liveform-data/commit/af2130f823bd86d077508c0bd7cf53fe968bf69b)). Takeaway: document what happens to recordings after students submit them.
- **Setup instructions clarified** (04 Nov 2026): Documented how to run the form and why it needs Linux or WSL ([setup notes](https://github.com/sanand0/liveform-data/commit/dfd4b41c4ae34b454811790d59c02d0a22cc924d)). Takeaway: put platform limits beside the run command.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_The course now offers learners a compact guide for AI tools and links assessment dates directly; good guidance still needs current rules._

- **A guide for course-aware AI help** (02 Nov 2026): Added a guidebook with course context, tool advice, and reminders to protect private records ([guide](https://github.com/sanand0/tools-in-data-science-public/commit/0fa3a570dc86b850c30edbf66c00e79bf9b8fa98)). Takeaway: give AI useful context, but make current instructions take priority.
- **GA4 dates and link published** (04 Nov 2026): Updated the September term schedule and linked learners to the exam ([schedule](https://github.com/sanand0/tools-in-data-science-public/commit/f07e303017be599bbf0a8a8f3abe0167fe84b78e)). Takeaway: link schedules to the live destination, not just a label.
- **A safer shared course reference** (02 Nov 2026): The guide warns against exposing tokens, student records, and unreleased answers ([guidebook](https://github.com/sanand0/tools-in-data-science-public/blob/main/2026-09/guidebook.md)). Takeaway: treat privacy rules as part of course instructions.

### [sanand0/datastories](https://github.com/sanand0/datastories)

_The new building chart makes a familiar comparison less obvious; floors and height, it turns out, do not always agree._

- **An atlas of tall buildings** (07 Nov 2026): Added an interactive view of 4,121 buildings, with filters and comparisons ([story](https://github.com/sanand0/datastories/commit/73cd5ff8596cb798f6779eded3c0082c052b8b6e)). Takeaway: show the records behind an unusual comparison.
- **An outlier-focused visual story** (07 Nov 2026): The page highlights how building height can diverge from floor count ([visualization](https://github.com/sanand0/datastories/blob/main/building-height/index.html)). Takeaway: let readers inspect exceptions, not just the average.
- **Story catalog updated** (07 Nov 2026): Added the new story to the project index and build configuration ([catalog](https://github.com/sanand0/datastories/commit/73cd5ff8596cb798f6779eded3c0082c052b8b6e)). Takeaway: update discovery pages whenever you publish a new feature.

### [sanand0/til](https://github.com/sanand0/til)

_The weekly notes mix new ideas with corrections; updating a belief is often more useful than collecting another link._

- **A fresh week of learning notes** (01 Nov 2026): Added reflections on model limits, agent workflows, and chocolate ([notes](https://github.com/sanand0/til/commit/6b3670b9ac957c8b81f418f9fd848f8b19853149)). Takeaway: record what surprised you, not only what you read.
- **Claims corrected with evidence** (01 Nov 2026): Added notes that narrow claims about visual AI, originality, and scientific reproduction ([corrections](https://github.com/sanand0/til/commit/6b3670b9ac957c8b81f418f9fd848f8b19853149)). Takeaway: leave a visible trail when evidence changes your conclusion.
- **Practical questions captured** (01 Nov 2026): Added questions about teaching, grading, and evaluating agent-made work ([questions](https://github.com/sanand0/til/commit/6b3670b9ac957c8b81f418f9fd848f8b19853149)). Takeaway: turn recurring questions into reusable checks.

### [sanand0/convergence-event-comic](https://github.com/sanand0/convergence-event-comic)

_The new comic viewer makes a long illustrated story easier to read on phones; zooming is not a luxury when panels get tiny._

- **A dedicated comic reader** (07 Nov 2026): Added an introduction, closing page, and sequential viewer for the comic artwork ([viewer](https://github.com/sanand0/convergence-event-comic/commit/11934a6ef3b7295dc5348564108c44129f0e190f)). Takeaway: give long visual stories a clear beginning and end.
- **Easier mobile navigation** (07 Nov 2026): The reader supports zooming and quick movement between pages ([viewer code](https://github.com/sanand0/convergence-event-comic/blob/main/comic/index.html)). Takeaway: design for the screen readers actually use.
- **Page state is easier to revisit** (07 Nov 2026): Page links and navigation help readers return to a specific point ([viewer code](https://github.com/sanand0/convergence-event-comic/blob/main/comic/index.html)). Takeaway: make useful reading positions shareable.

### [sanand0/tds-network-games](https://github.com/sanand0/tds-network-games)

_The game’s new scoring gives story creation more weight than reviewing; rubrics are easier to trust when their math is visible._

- **Creator work counts for 80%** (07 Nov 2026): Picture Stories now weights creation more heavily than reader work ([scoring code](https://github.com/sanand0/tds-network-games/commit/f35046e67c1796d4d2fb54394e8015577bfd86da)). Takeaway: publish weighting rules before grades arrive.
- **Separate role scores exposed** (07 Nov 2026): Creator and reader scores now each use a ten-point scale ([tests](https://github.com/sanand0/tds-network-games/commit/f35046e67c1796d4d2fb54394e8015577bfd86da)). Takeaway: test hand-worked examples when changing score formulas.
- **Anonymous face-review service added** (07 Nov 2026): A new service records pairwise reviews and signs participation receipts ([service](https://github.com/sanand0/tds-network-games/commit/27b485f353f946784a0a2d98f1a3ff17dd24ca66)). Takeaway: keep identity and review data out of public-facing views.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_The podcast workflow can now draw from a synced WhatsApp archive; one less manual export, one more reason to check the source._

- **WhatsApp archive import** (01 Nov 2026): Added a `wacli` extractor to fetch and sort messages for podcast creation ([extractor](https://github.com/sanand0/generative-ai-group/commit/47254178e30048c17d8f0f1e961c1484586b59ea)). Takeaway: automate data collection where the source system offers a stable interface.
- **Paged results handled safely** (01 Nov 2026): The extractor follows cursors and tests message mapping across pages ([tests](https://github.com/sanand0/generative-ai-group/commit/47254178e30048c17d8f0f1e961c1484586b59ea)). Takeaway: test pagination so large exports do not quietly lose data.
- **A new weekly episode generated** (01 Nov 2026): Published a podcast script covering the week’s AI discussions ([episode](https://github.com/sanand0/generative-ai-group/commit/b3b45997964435fa3f0f7a2c0102d8cfdfcc0e90)). Takeaway: distinguish group observations from claims that need outside evidence.

### [sanand0/infra](https://github.com/sanand0/infra)

_The disk audit treats storage as a recurring system problem, not a heroic once-a-year cleanup; caches do love a comeback._

- **Disk use mapped in detail** (05 Nov 2026): Added a report ranking cleanup options by space saved, effort, and risk ([report](https://github.com/sanand0/infra/commit/a0534563b7e3d5dffb2cc58728429ed61d044d0d)). Takeaway: measure storage before deleting files.
- **Recurring housekeeping added** (05 Nov 2026): The new tasks support scans, previews, cleanup, and a weekly timer ([tasks](https://github.com/sanand0/infra/blob/main/disk-space/justfile)). Takeaway: automate safe cleanup and preview destructive steps.
- **Regrowth made visible** (05 Nov 2026): The report tracks fast-growing caches and suggests ways to limit repeated buildup ([findings](https://github.com/sanand0/infra/commit/a0534563b7e3d5dffb2cc58728429ed61d044d0d)). Takeaway: fix the source of growth, not just the latest pile.

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

_The demo catalog grew by many examples, but each new entry still needs a human check; “listed” does not mean “verified.”_

- **New demos added to the catalog** (03 Nov 2026): Added examples spanning audio, research, governance, and other AI applications ([catalog update](https://github.com/sanand0/llmdemos/commit/78c968d7c8bb467b0c800dc18bdf6ead8100df82)). Takeaway: group demos around what users can learn or try.
- **Unreviewed entries flagged** (03 Nov 2026): New items are marked for later human review ([configuration](https://github.com/sanand0/llmdemos/blob/main/config.json)). Takeaway: distinguish new submissions from reviewed recommendations.
- **Repository references refreshed** (03 Nov 2026): Updated a contributor reference while refreshing the demo list ([README change](https://github.com/sanand0/llmdemos/commit/78c968d7c8bb467b0c800dc18bdf6ead8100df82)). Takeaway: verify ownership and links when curating community projects.

## Lessons

- **Test the boundaries:** Cross-platform file replacement, empty chart categories, valid zero scores, and failed uploads all deserve direct tests.
- **Separate proof from quality:** A valid receipt proves authenticity or participation; it does not prove a high score or good judgment.
- **Make methods visible:** Clear rubrics, data limits, and evidence trails help readers understand what results really mean.
- **Automate repeated work carefully:** Shortcuts, scheduled cleanup, and archive imports save effort when they remain testable and safe.

## Suggestions

- Add automated browser checks for Tailrun’s upload, access-control, and static-file routes before relying on the new deployment.
- Audit the Picture Stories scoring distribution after the weighting change, and explain any surprising effects to learners.
- Give new demos a lightweight review checklist for link health, privacy, accessibility, and evidence behind their claims.
- Track disk use over several weeks to confirm the cleanup timer slows cache growth without removing useful work.