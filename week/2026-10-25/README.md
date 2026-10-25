## A Week of Safer Tools, Richer Games, and Better Checks

This week’s work turned practical friction into clearer workflows, richer classroom projects, and stronger checks against mistakes. The common lesson: useful systems need both good ideas and ways to verify what they actually do.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_The scripts repo made everyday tasks safer and more portable—because apparently one transcription command wasn’t enough._

- **Transcribe without the ceremony:** Added a small audio-to-Markdown CLI and switched call transcripts to a model reported as 14% cheaper ([e006105](https://github.com/sanand0/scripts/commit/e006105), [`transcribe`](https://github.com/sanand0/scripts/blob/main/transcribe)). Takeaway: give common tasks a simple, well-tested entry point.
- **Back up the whole Documents folder:** Reworked the hourly Windows backup to copy changed files while preserving destination-only files ([121f2fc](https://github.com/sanand0/scripts/commit/121f2fc), [sync script](https://github.com/sanand0/scripts/blob/main/services/sync-plutonium.sh)). Takeaway: make backup rules explicit before widening their scope.
- **Keep heavy work in check:** Video compression now pauses when the GPU gets hot and resumes after cooling ([3d6d7aa](https://github.com/sanand0/scripts/commit/3d6d7aa), [`setup.fish`](https://github.com/sanand0/scripts/blob/main/setup.fish)). Takeaway: add safety limits around long-running hardware jobs.
- **Make the edges less brittle:** Added subtitle extraction, safer Windows JSON output, and a cheaper transcription default ([b3d4164](https://github.com/sanand0/scripts/commit/b3d4164), [19d5db3](https://github.com/sanand0/scripts/commit/19d5db3), [e006105](https://github.com/sanand0/scripts/commit/e006105)). Takeaway: test across real platforms, not just the machine that wrote the code.

### [sanand0/exam](https://github.com/sanand0/exam)

_Exams gained new creative tasks and tougher audit cases; grading now has fewer places to shrug and guess._

- **Add face-morph assignments:** Students now create a short face-morph video and rank ten face pairs, with server-side assignments and input checks ([52389d1](https://github.com/sanand0/exam/commit/52389d1), [question files](https://github.com/sanand0/exam/tree/main/src)). Takeaway: keep personal assignments stable and validate submissions at the boundary.
- **Add a picture-story game:** Project 1 now accepts a signed final game receipt and applies its score after the round closes ([d3bf08e](https://github.com/sanand0/exam/commit/d3bf08e), [validator](https://github.com/sanand0/exam/blob/main/src/a-trading-picture-story.js)). Takeaway: bind receipts to the student, game, round, and configuration.
- **Make audit questions harder to game:** Fresh cases now vary their evidence and counterfactuals instead of rewarding one familiar pattern ([5fb9072](https://github.com/sanand0/exam/commit/5fb9072), [31c8a81](https://github.com/sanand0/exam/commit/31c8a81)). Takeaway: vary test cases while keeping their structure fair.
- **Put checking limits in the system:** Per-question check budgets now apply on the server, with clearer feedback in the exam interface ([b9e65cf](https://github.com/sanand0/exam/commit/b9e65cf)). Takeaway: enforce important rules where users cannot bypass them.

### [sanand0/tds-network-games](https://github.com/sanand0/tds-network-games)

_The game platform grew new classroom experiences and more consistent data tools—yes, phones are now part of the curriculum._

- **Launch Picture Stories:** Students submit wordless pictures, narrate classmates’ stories, and rank them; private media and signed receipts support the workflow ([effd547](https://github.com/sanand0/tds-network-games/commit/effd547), [game code](https://github.com/sanand0/tds-network-games/tree/main/src/trading/games/picture-story)). Takeaway: design privacy and scoring into the game from the start.
- **Add Human Exchange:** Students trade services through staged orders, held credits, and confirmed delivery ([01c074a](https://github.com/sanand0/tds-network-games/commit/01c074a), [game code](https://github.com/sanand0/tds-network-games/tree/main/src/trading/games/human-exchange)). Takeaway: model each step of a real-world exchange, including refunds.
- **Help Air Ink recover from sensor trouble:** Calibration now shows live sensor health and clearer recovery steps ([3867cdc](https://github.com/sanand0/tds-network-games/commit/3867cdc), [sensor-health module](https://github.com/sanand0/tds-network-games/blob/main/public/motion/air-ink/sensor-health.js)). Takeaway: explain what the device observes before asking users to troubleshoot.
- **Standardize private data sync:** Added a read-only trading-ledger sync and aligned its options with other dataset tools ([5c34ef1](https://github.com/sanand0/tds-network-games/commit/5c34ef1), [`DATA-SYNC.md`](https://github.com/sanand0/tds-network-games/blob/main/DATA-SYNC.md)). Takeaway: make dry runs and integrity checks standard for sensitive exports.

### [sanand0/mobile-games](https://github.com/sanand0/mobile-games)

_Three collaborative phone games now have a shared home, so the phones can stop pretending they’re just for scrolling._

- **Give the games a front door:** Added a responsive home page, game summaries, filters, and a GitHub Pages publishing workflow ([9df3289](https://github.com/sanand0/mobile-games/commit/9df3289), [home page](https://github.com/sanand0/mobile-games/blob/main/index.html)). Takeaway: put a simple guide in front of a growing set of experiments.
- **Turn a crowd into handwriting:** Human Pixels assigns each phone one letter and combines the strokes into a shared paragraph ([6827335](https://github.com/sanand0/mobile-games/commit/6827335), [game](https://github.com/sanand0/mobile-games/tree/main/human-pixels)). Takeaway: make each participant’s small action contribute to a visible result.
- **Make humming a group instrument:** Voice Choir detects pitch locally and turns many phones into a shared choir, without uploading voices ([c15fbe0](https://github.com/sanand0/mobile-games/commit/c15fbe0), [game guide](https://github.com/sanand0/mobile-games/tree/main/voice-choir)). Takeaway: process sensitive signals on the device when possible.

### [sanand0/talks](https://github.com/sanand0/talks)

_Talk pages gained more ways to watch, listen, and follow along—because one format rarely suits every audience._

- **Add video alongside the AIPL audio:** Embedded the full session and explained why its timing differs from the audio transcript ([c3c6bb9](https://github.com/sanand0/talks/commit/c3c6bb9), [talk page](https://github.com/sanand0/talks/tree/main/2026-10-18-aipl-when-do-you-let-ai-act)). Takeaway: label media differences instead of implying timelines match.
- **Publish a new course-design session:** Added a transcript, captions, and a story page focused on how assessment ideas meet implementation ([df29d39](https://github.com/sanand0/talks/commit/df29d39), [session files](https://github.com/sanand0/talks/tree/main/2026-10-19-tds-ideation)). Takeaway: pair media with text that helps readers navigate it.
- **Bring older talks back into the archive:** Added recordings, transcripts, and source materials for talks dating back to 2012 ([06a0028](https://github.com/sanand0/talks/commit/06a0028)). Takeaway: preserve original sources when making an archive easier to explore.

### [sanand0/tools](https://github.com/sanand0/tools)

_The tools collection added better capture and recovery; apparently even a recording button needs a library._

- **Record video as well as audio:** The recorder now supports camera and screen capture, small video settings, keyboard controls, and a browsable library ([58ed4a5](https://github.com/sanand0/tools/commit/58ed4a5), [recorder](https://github.com/sanand0/tools/tree/main/record)). Takeaway: design capture tools around how people save and revisit their work.
- **Back up image-only AI replies safely:** The ChatGPT scraper now retains generated-image replies without opening their previews ([58ed4a5](https://github.com/sanand0/tools/commit/58ed4a5), [scraper](https://github.com/sanand0/tools/blob/main/aiscrapers/chatgptscraper.js)). Takeaway: extract passively when interacting could change the page.
- **Recover music-folder access in one click:** Library alerts now include a reconnect action when browser permissions expire ([8da90f5](https://github.com/sanand0/tools/commit/8da90f5), [music player](https://github.com/sanand0/tools/blob/main/music/script.js)). Takeaway: put recovery beside the error that needs it.

### [sanand0/private-research](https://github.com/sanand0/private-research)

_The neuron-research note separates measured laptop behavior from estimates—an unusual but welcome refusal to invent a result._

- **Map a practical first experiment:** The report recommends starting with a small model and a matching published feature dataset ([bfa9cab](https://github.com/sanand0/private-research/commit/bfa9cab), [research report](https://github.com/sanand0/private-research/blob/main/llm-neuron-features/RESEARCH.md)). Takeaway: choose tools with existing, matching evidence before building new infrastructure.
- **Measure before promising:** Added short local model benchmarks with settings and timing counters ([bfa9cab](https://github.com/sanand0/private-research/commit/bfa9cab), [benchmark data](https://github.com/sanand0/private-research/blob/main/llm-neuron-features/benchmark-results.json)). Takeaway: publish the conditions alongside performance numbers.
- **Mark the limits clearly:** The report says no neuron was mapped and distinguishes human-time estimates from measured generation speed ([bfa9cab](https://github.com/sanand0/private-research/commit/bfa9cab), [scope notes](https://github.com/sanand0/private-research/blob/main/llm-neuron-features/notes.md)). Takeaway: say what an experiment did not establish.

### [sanand0/tools-in-data-science-public](https://github.com/sanand0/tools-in-data-science-public)

_Course dates and links caught up with reality; calendars, too, need version control._

- **Fix the Week 3 link and dates:** GA3 now links to its exam page and shows its updated 21 Oct start date ([7a4230a](https://github.com/sanand0/tools-in-data-science-public/commit/7a4230a)). Takeaway: check that links and schedules agree before publishing.
- **Extend the GA3 deadline:** The course page now gives students until 31 Oct ([d1e8078](https://github.com/sanand0/tools-in-data-science-public/commit/d1e8078)). Takeaway: update the source of truth when deadlines change.
- **Extend Project 1 as well:** The listed P1 deadline moved to 17 Nov ([0abf4ed](https://github.com/sanand0/tools-in-data-science-public/commit/0abf4ed)). Takeaway: review nearby dates when changing one assessment schedule.

### [sanand0/blog](https://github.com/sanand0/blog)

_The blog shared new experiments and weekly notes, with corrections that make the technical claims more trustworthy._

- **Showcase practical AI demos:** A roundup connects 3D world building, video analysis, and small models supported by rules ([0c38aee](https://github.com/sanand0/blog/commit/0c38aee), [post](https://github.com/sanand0/blog/blob/main/posts/2026/innovations-19-oct-2026.md)). Takeaway: explain what a demo can do and where it still fails.
- **Turn the week into useful notes:** Added observations about browser privacy, AI tools, and shifting model capabilities ([4f8ee6e](https://github.com/sanand0/blog/commit/4f8ee6e), [weekly post](https://github.com/sanand0/blog/blob/main/posts/2026/things-i-learned-18-oct-2026.md)). Takeaway: keep short notes while the details are fresh.
- **Correct public claims:** Added explicit fixes for errors and overstatements from talks ([4f8ee6e](https://github.com/sanand0/blog/commit/4f8ee6e), [corrections](https://github.com/sanand0/blog/blob/main/pages/mistakes-i-made.md)). Takeaway: correct the record where readers will find the original claim.

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

_One demo link changed, but its name, destination, and branding now tell the same story._

- **Point PersonaGen to its maintained home:** Updated the title, repository, and GitHub Pages links, while keeping its review and branding notes ([9332e4e](https://github.com/sanand0/llmdemos/commit/9332e4e), [`config.json`](https://github.com/sanand0/llmdemos/blob/main/config.json)). Takeaway: keep directory metadata aligned with the actual project.

### [sanand0/til](https://github.com/sanand0/til)

_The notes gained fresh observations and a little cleanup; typo patrol remains undefeated._

- **Capture new AI observations:** Added notes on agent use, model behavior, and changing software workflows ([350f307](https://github.com/sanand0/til/commit/350f307), [`llms.md`](https://github.com/sanand0/til/blob/main/llms.md)). Takeaway: label impressions as provisional when they come from limited use.
- **Record practical discoveries:** Added notes on fonts, privacy, and everyday decision-making ([350f307](https://github.com/sanand0/til/commit/350f307), [`til.md`](https://github.com/sanand0/til/blob/main/til.md)). Takeaway: save useful details in a form that is easy to revisit.
- **Keep the notes readable:** Corrected a small spelling issue while updating the entries ([350f307](https://github.com/sanand0/til/commit/350f307)). Takeaway: quick editing makes a growing notes file easier to trust.

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Model comparisons got safer matches and fewer made-up dates; charts should not possess prophetic powers._

- **Match model names carefully:** Added explicit aliases to join known leaderboard name variants without broadly merging different models ([bddc399](https://github.com/sanand0/llmpricing/commit/bddc399), [`update_elo.py`](https://github.com/sanand0/llmpricing/blob/main/update_elo.py)). Takeaway: prefer narrow aliases over fuzzy rules for identity matching.
- **Avoid duplicate rows:** Normalized identifiers and added checks that reject duplicate model names ([bddc399](https://github.com/sanand0/llmpricing/commit/bddc399)). Takeaway: validate uniqueness before updating a comparison dataset.
- **Stop guessing launch dates:** Models without a verified launch month now appear only in the latest chart period ([bddc399](https://github.com/sanand0/llmpricing/commit/bddc399), [chart logic](https://github.com/sanand0/llmpricing/blob/main/script.js)). Takeaway: represent missing data as missing, not as a convenient guess.

### [sanand0/liveform](https://github.com/sanand0/liveform)

_Live forms can now widen a text box without losing answers; multiline feedback has been waiting patiently._

- **Allow text fields to grow:** Forms can change a single-line field to a multiline field while keeping existing answers ([cef096b](https://github.com/sanand0/liveform/commit/cef096b), [config handling](https://github.com/sanand0/liveform/blob/main/src/liveform/config.py)). Takeaway: allow only conversions that preserve stored answers.
- **Protect against lossy reversals:** Changing back to a single-line field remains blocked because it could strip line breaks ([cef096b](https://github.com/sanand0/liveform/commit/cef096b)). Takeaway: consider what data might be lost before permitting schema changes.
- **Prove the change survives:** Tests cover live answers, stored response files, and restarts; the README explains validation behavior ([cef096b](https://github.com/sanand0/liveform/commit/cef096b), [tests](https://github.com/sanand0/liveform/tree/main/tests)). Takeaway: test both the active session and what happens after restart.

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_The weekly podcast script covers model choices, calibration, and infrastructure—quite a lot of chat for one episode._

- **Turn the conversation into a podcast script:** Added a dialogue about decision models, adapting existing models, and checking their probabilities ([97eece4](https://github.com/sanand0/generative-ai-group/commit/97eece4), [script](https://github.com/sanand0/generative-ai-group/blob/main/2026-10-18/podcast-2026-10-18.md)). Takeaway: keep model claims tied to specific tasks and evidence.
- **Balance performance with practical needs:** The script discusses local deployment, privacy, latency, and fallback needs ([97eece4](https://github.com/sanand0/generative-ai-group/commit/97eece4)). Takeaway: choose models using the real operating constraints, not benchmark scores alone.
- **Leave uncertainty in the story:** The discussion treats reliability and infrastructure risks as questions to investigate, not settled facts ([97eece4](https://github.com/sanand0/generative-ai-group/commit/97eece4)). Takeaway: distinguish informed concerns from proven outcomes.

## Lessons

- **Make verification part of the product:** From exam receipts to backup checks, users need evidence that a task completed correctly.
- **Preserve data by default:** Safe migrations, read-only syncs, and honest missing values prevent quiet damage.
- **Show users what the system knows:** Sensor diagnostics, useful error recovery, and clear media timing turn hidden problems into fixable ones.
- **Test the real boundary:** Platform differences, changing schemas, and adversarial examples reveal failures that happy paths miss.

## Suggestions

- Pilot Picture Stories and Human Exchange with small groups before relying on their scoring or completion flows.
- Add device-based testing for Air Ink and Voice Choir; simulations cannot replace real phones and real sensors.
- Document the Documents backup’s overwrite rules and test restore steps, not just successful copies.
- Recheck course deadlines and model-price data as their source information changes.