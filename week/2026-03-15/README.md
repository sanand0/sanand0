## A week of teachable traces, safer prompts, and prettier SVGs

Agents, classroom replays, and news-card tooling got production polish. The key lesson: make outputs observable, chunked, and easy to reuse.

### [sanand0/blog](https://github.com/sanand0/blog)

_More teaching artifacts and practical AI advice so readers can act, not just admire technical cleverness._

- **New exam post (13 Mar 2026).** Added "Cracking online exams with coding agents" ([ae54087](https://github.com/sanand0/blog/commit/ae54087e11039338e7a3db7b00670b6e6bbee0ce)), file: posts/2026/cracking-online-exams-with-coding-agents.md. Shows how coding agents reveal what exams actually test. Takeaway: ask "What skill is this really testing?" before you grade.
- **Agent-era playbook & digital-exhaust (12 Mar 2026).** Added pages/digital-exhaust.md and pages/ai-advice.md ([457b8a6](https://github.com/sanand0/blog/commit/457b8a64adf395bc8f2cc3573de18568a2541024)), plus practical posts on screencast workflows. Helps teams treat context as an asset. Takeaway: collect small, useful context; it compounds into trusted agent memory.
- **Comic styles & prompt fragments (10 Mar 2026).** New gallery post and clearer single-panel prompt guidance ([03e8df1](https://github.com/sanand0/blog/commit/03e8df115ad02c04f78ef44247db54be33d788fb)), files: posts/2026/llm-comic-styles.md, pages/prompts/fragments.md. Also recorded safety edits to avoid copyrighted cues. Takeaway: iterate prompts, and rewrite only the stereotyping lines.
- **Teaching experiments and labs (8–9 Mar 2026).** Added game-playing-agent labs and a directional-feedback teaching pattern ([5ec9282](https://github.com/sanand0/blog/commit/5ec9282633852ac4028d86ad5fcd332aaa1345cc), [0b98554](https://github.com/sanand0/blog/commit/0b985545cb6ae88b5a702e528938887efccc28bf)). Includes practical prompts and curriculum notes. Takeaway: use agents to prototype exercises, but keep the learning loop human-led.

(Yes, you really needed one more comic prompt. It will save you ten design meetings.)

### [sanand0/journalists](https://github.com/sanand0/journalists)

_Vector-first graphics, robust templates, and a newsroom-friendly export flow._

- **SVG-first redesign and fonts (13 Mar 2026).** Added Poynter Agate fonts and rewrote SVG templates for native, editable SVGs ([36d20f7](https://github.com/sanand0/journalists/commit/36d20f73d411cdf6c0c22031c69e024e4740e6f4)). This simplifies Illustrator and browser workflows. Takeaway: prefer native SVGs for portability and editing.
- **Footer, QR, and template fixes (13 Mar 2026).** Fixed QR labels, footer color rules, and drop shadows across templates ([f16e91d](https://github.com/sanand0/journalists/commit/f16e91dab65986142541af5712ff293ae0313640)). Improves contrast and print readiness. Takeaway: small layout details wreck production if not consistent.
- **MOSPI PLFS data workspace & social cards (13 Mar 2026).** Added data/mospi-plfs, analysis scripts, and many generated SVGs ([0622324](https://github.com/sanand0/journalists/commit/0622324f1d5edb030b19b9dd9f7adc4ae9a109a4)). Ready-to-share story packages and CSV outputs live here. Takeaway: bundle data, insights, and finished graphics together for reproducible reporting.
- **Hack-of-the-Day UI & metadata uplift (12 Mar 2026).** Introduced template picker, format toggle, indexing, and bookmarkable sort/filter ([a673b62](https://github.com/sanand0/journalists/commit/a673b62f86461656f737e4a3c8e9f505e025caf2)). Now downloads name files predictably. Takeaway: treat cards as data, not images.

(Yes, you really needed another SVG template. But now the QR actually scans.)

### [sanand0/pyoppe](https://github.com/sanand0/pyoppe)

(Teaching analytics) Replays that educators can narrate, plus tighter test-case reviews.

- **Classroom replay slideshow (11 Mar 2026).** Added analysis/replays-v3.html, with syntax highlighting, annotations, and bookmarkable slides ([6fc9d7f](https://github.com/sanand0/pyoppe/commit/6fc9d7ff82d95eec3fcc3928f3e9c175615ce26f)). Teachers can scrub to moments and see mental-model notes. Takeaway: turn traces into teachable narratives, not raw logs.
- **Rewrite narratives with educator focus (11 Mar 2026).** Rewrote seven replay narratives to highlight interventions and testing cues ([5585027](https://github.com/sanand0/pyoppe/commit/55850274ad1fa423e098afdbe334a7493b21e3c1)). Slides now suggest concrete classroom moves. Takeaway: annotate why students err, then suggest a single next exercise.
- **Cluster revision analysis (11 Mar 2026).** Added analysis that compares revised testcases to earlier findings ([758e5d](https://github.com/sanand0/pyoppe/commit/758e5df01a3f4ddf9d97372bf621df71373b0559)), file: analysis/new-clusters-2026-03-11/analysis.md. It lists missed opportunities and priorities. Takeaway: public testcases should surface edge cases, not hide them.
- **Promote narrated replays to front page (11 Mar 2026).** Replaced the replay link with the new narrated slideshow in index.html ([ce14491](https://github.com/sanand0/pyoppe/commit/ce144911727fc9b11f7877baf4ed4d3322fdfa6f)). That surfaces teaching artifacts to stakeholders. Takeaway: put educator-facing artifacts where decision-makers will see them.

(Yes, you really needed synchronized annotations. Students will thank you later.)

### [sanand0/scripts](https://github.com/sanand0/scripts)

(Dev environment and agent tooling) Big investment in developer ergonomics and a new docs skill.

- **OpenAI-docs skill and references (14 Mar 2026).** Added agents/.system/openai-docs with SKILL.md and reference materials ([7e1dc00](https://github.com/sanand0/scripts/commit/7e1dc00d7e1fa36a9949a1e061c1b529928cc175)). Use it for authoritative model guidance. Takeaway: prefer official docs over ad-hoc web scraping.
- **Codextags and parsing tooling (14 Mar 2026).** Added codextags.py, tests, and parsing improvements to tag coding sessions and surface recommendations. This aids analysis and triage. Takeaway: index session metadata early to find repeat failures.
- **Better dev container and forward-testing guidance.** Improved dev.dockerfile, dev.sh, and SKILL.md advice for safer skill authoring. Those changes reduce environment drift. Takeaway: fix the environment once; agents stop failing on missing tools.

(Yes, you really needed another helper script. It saves three hours a week.)

### [sanand0/datastories](https://github.com/sanand0/datastories)

_A new reproducible security story and multiple stylistic writeups._

- **Added "Crack the Prompt" story and session artifacts (13 Mar 2026).** New landing and three detailed session logs plus stylistic writeups ([04a634e](https://github.com/sanand0/datastories/commit/04a634e0f8f51cf28ab91ce6dd64371f017c8060)). Readers can replay the agent steps and read multiple commentary styles. Takeaway: publish raw traces plus narrative to make security lessons concrete.
- **Multiple narrative voices and index (13 Mar 2026).** Included Randall Munroe, Feynman, and Gladwell styled pieces for the same event. That shows different angles for the same data. Takeaway: frame the same evidence for varied audiences.

(Yes, you wanted three rhetorical lenses. Choose your favorite.)

### [sanand0/llmartstyle](https://github.com/sanand0/llmartstyle)

_Experimented with many comic prompts and hardened generation against policy/quota issues._

- **Comic-styles matrix and generation safety (10 Mar 2026).** Added new comic style prompts to config.json and improved generator error handling ([046fdc6](https://github.com/sanand0/llmartstyle/commit/046fdc6b10114b7d5d4d5d0ee21e4ec92c66ffe5)). It detects policy blocks and quota signals. Takeaway: treat model rejections as data, and rewrite only the offending tokens.
- **Performance and ordering tweaks (10 Mar 2026).** Lazy-loading and model-column reordering for better UX ([ac44f01](https://github.com/sanand0/llmartstyle/commit/ac44f01112e582380ef50288ac8a618b3b144e0d)). That speeds page loads and surfaces the best models first. Takeaway: small UX fixes make large galleries actually usable.

(Yes, another cat gallery. But now it politely handles policy hiccups.)

### [sanand0/llmdemos](https://github.com/sanand0/llmdemos)

_Curated LLM demos and a tidy build workflow._

- **Added and curated new demos (13 Mar 2026).** Updated config.json with several new demos and flags for unreviewed items ([fd3f712](https://github.com/sanand0/llmdemos/commit/fd3f712d7adaa4f7bd12f4f7240822024a5e05cf)). This surfaces interesting projects for reviewers. Takeaway: mark new items unreviewed, then review incrementally.
- **Undeploy note and deploy tweaks (13 Mar 2026).** Cleaned README and removed the stale CNAME to "undeploy" the GitHub Pages host ([3996614](https://github.com/sanand0/llmdemos/commit/39966145762c3f189b4e6a4414e1ec771f6b2a95)). Keeps the public site accurate. Takeaway: update deployment metadata when hosting decisions change.

(Yes, another demo list. But it's hand-curated this time.)

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_More context for the cost-vs-quality picture, plus a scrollytelling narrative._

- **Narrative scrollytelling added (10 Mar 2026).** New story JSON and scrolly glue in script.js ([467474a](https://github.com/sanand0/llmpricing/commit/467474abd9ebdb3051ba016ddc95bfed7da556c6)). It animates months and highlights models. Takeaway: narrate the dataset rather than just charting points.
- **ELO annotations for lay audiences (09 Mar 2026).** Added academic analogies for Elo ranges, making scores relatable ([adf9676](https://github.com/sanand0/llmpricing/commit/adf9676e6dcf0c6208a7c223e489d71938567ca4)). That helps non-experts pick models. Takeaway: convert technical scales into everyday metaphors.
- **Updated models, pricing, and CSVs (09 Mar 2026).** Reworked elo.csv and README updates to reflect March data ([f5c3189](https://github.com/sanand0/llmpricing/commit/f5c31892c79bbb929174cf2ad959e74419abe592)). That keeps the frontier accurate. Takeaway: refresh data often; costs change fast.

(Yes, comparing a Bible's token count to model cost is still a great way to get attention.)

### [sanand0/talks](https://github.com/sanand0/talks)

_New talks and transcripts landed._

- **PyConf Hyderabad talk added (15 Mar 2026).** Published a fresh talk page for "How Students Learn Python" and updated README ([88b3574](https://github.com/sanand0/talks/commit/88b3574f49d3f7676407b7e742966eca4fd2f078)). Good for course materials. Takeaway: bundle slides and assets with the talk.
- **NIE AI Roadmap talk (12 Mar 2026).** Added a long transcript, prompts, sketchnote, and story pages ([8f2218d](https://github.com/sanand0/talks/commit/8f2218d6170551689ead399518ee66c88aa66f14)). Makes reuse and sharing easier. Takeaway: transcripts plus sketchnotes scale teaching reach.
- **MIT license for talks repo.** Added LICENSE for clear reuse terms. Takeaway: a permissive license lowers friction for reuse.

(Yes, slides and sketchnotes—both necessary. One is short, the other lies.)

### [sanand0/schoolai](https://github.com/sanand0/schoolai)

_MIT license and a clearer README to onboard demo viewers._

- **Docs and license (08 Mar 2026).** Added README.md and LICENSE to describe demos and quick start (python3 -m http.server). Takeaway: clear docs remove friction for demo trials.

(Yes, the README counts as a deliverable. People use it.)

## Lessons

- Chunk big generation jobs. Large single-shot edits stall models like Claude. Save incremental edits often.
- Make artifacts first-class data. Cards, stories, and replays should be exportable, indexable, and versioned.
- Teach with traces. Narrated, timestamped replays convert noise into pedagogy.
- Prefer native formats. Native SVGs and small, testable JSONs reduce post-production cost.
- Treat policies as signals. Image blocks and model rejections are diagnosable data points, not failures.

## Suggestions

- Add small CI checks: render one SVG, run replay HTML smoke-tests, and lint narrative JSON.
- Run before/after teaching pilots for a couple of replays. Measure time saved per intervention.
- Publish a short "how we verify prompts" checklist from pyoppe and scripts. Use it in course grading rubrics.
- Turn narrative JSONs into live scrolly templates. Reuse across llmpricing, datastories, and blog stories.
- Audit public testcases for unintentionally hidden edge cases. Use pyoppe's analysis to add the missing public tests.

If you want, I can
- generate the roundup as separate short tweets per repo, or
- open PR checklists for the top three suggested CI tests. Which would help most next?