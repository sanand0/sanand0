## A week of making AI content honest, local data useful, and backups reliably boring

This week focused on visible AI disclosure, safer local data tooling, and quieter, more repeatable automation. The key lesson: make generated outputs easy to find, and make your pipelines easy to trust.

### [sanand0/blog](https://github.com/sanand0/blog)

_You want readers and agents to know when AI helped, and for posts to be easier for other tools to find and reuse._

- **Visual AI disclosure UI.** Injected an AI badge, tooltip, and footer via [f98ea18](https://github.com/sanand0/blog/commit/f98ea184aa16e11debcbb60533ffc37f21c73d95) and styled it in [static/custom.css](https://github.com/sanand0/blog/blob/main/static/custom.css). This makes AI-generated sections obvious across light/dark themes. Takeaway: clear signals build trust and reduce surprise.
- **Mark AI text at render time.** The JS now reads generic `data-ai-*` attributes and renders disclaimers ([f98ea18](https://github.com/sanand0/blog/commit/f98ea184aa16e11debcbb60533ffc37f21c73d95) — see [static/js/site.js](https://github.com/sanand0/blog/blob/main/static/js/site.js)). That future-proofs attribution. Takeaway: automate metadata consumption, not manual stamping.
- **New AI and enterprise posts published.** Added enterprise and AI workflow posts ([f98ea18](https://github.com/sanand0/blog/commit/f98ea184aa16e11debcbb60533ffc37f21c73d95), [213a788](https://github.com/sanand0/blog/commit/213a788e809057eccbf0a5674958cc4de43720f6), [96d024e](https://github.com/sanand0/blog/commit/96d024e32a0df0fa0ff0b58be25c8bfd8966e567)). They explain model routing, deprecations, and making content agent-consumable. Takeaway: publish the workflow, not just the result.
- **Reusable prompts and meeting-prep system prompt.** Reworked prompt fragments and moved the Chief-of-Staff prompt into [pages/prompts/meeting-preparation.md](https://github.com/sanand0/blog/blob/main/pages/prompts/meeting-preparation.md) ([3a9398](https://github.com/sanand0/blog/commit/3a9398af9061047f977dce93e78990e766a013d7)). This makes meeting prep reproducible. Takeaway: separate system prompts from ad-hoc text.
- **Editorial metadata and discoverability fixes.** Added descriptions and keywords across posts to help humans and agents find content ([213a788](https://github.com/sanand0/blog/commit/213a788e809057eccbf0a5674958cc4de43720f6), [3a9398](https://github.com/sanand0/blog/commit/3a9398af9061047f977dce93e78990e766a013d7)). Takeaway: small frontmatter saves hours later.

(Yes, the site now politely tells readers when a robot whispered in its ear.)

### [sanand0/scripts](https://github.com/sanand0/scripts)

_Make local data reliable and machine-friendly. Then your agents stop guessing and start helping._

- **WhatsApp backup and daily-activities automation.** Added a robust incremental WhatsApp scraper and made activities fill missing days through yesterday ([915c9e0](https://github.com/sanand0/scripts/commit/915c9e0b35a66e276d63f2fdaffd1af36ae77497), 17 May 2026). Files: [backupwhatsapp.py](https://github.com/sanand0/scripts/blob/main/backupwhatsapp.py). This preserves chat history and avoids repeating work. Takeaway: make backups idempotent.
- **LinkedIn scraper and calendar free-slot helper.** Added `backuplinkedin.py` and `freeslots.py` to export posts and suggest meeting times ([a8f5fb9](https://github.com/sanand0/scripts/commit/a8f5fb9eb5640b828618a33f2c89252e67664487), 20 May 2026). These fill common gaps in export and scheduling workflows. Takeaway: automate annoying, repeatable chores.
- **Google connections scraper and smarter summarizer.** `googleconnections.py` lists account-connected apps, and `summarize.py` now skips trivial transcripts and processes newest files first ([deb4c1e](https://github.com/sanand0/scripts/commit/deb4c1ecbc93e03511ca264ce14d2977d01b7d90), 20 May 2026). This saves API calls and surfaces risky app permissions. Takeaway: filter early, act later.
- **Podcast robustness and sensible defaults.** Tests and code now derive MP3 names from Markdown basenames and log full Gemini responses on errors ([a8f5fb9](https://github.com/sanand0/scripts/commit/a8f5fb9eb5640b828618a33f2c89252e67664487)). That aids debugging when TTS fails. Takeaway: predictable file names simplify pipelines.
- **Quieter backups and safer deletions in meet backups.** Improved backupmeet/backupgoogle behavior to avoid noisy keyring logs and delete only when safe ([a8f5fb9](https://github.com/sanand0/scripts/commit/a8f5fb9eb5640b828618a33f2c89252e67664487), [4071a2a](https://github.com/sanand0/scripts/commit/4071a2a795817177789531aeb1dd2ed8bb732199)). Takeaway: make automated jobs safe to run often.

(If you love silence, you will love these changes.)

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Maintain a weekly podcast pipeline so conversations become listenable artifacts._

- **Updated weekly podcast script.** Added the May 17 episode transcript and cleaned host dialogue ([168eb59](https://github.com/sanand0/generative-ai-group/commit/168eb598870098ca0058ac480aa4e79ba4a295e8), 17 May 2026). This keeps the audio generator fed with fresh scripts. Takeaway: short publishing loops keep shows timely.
- **Cleaner two-host formatting for narration.** The transcript style favors rapid TTS conversion and simple editing. That reduces post-production time. Takeaway: write for the pipeline, not just the page.

(Yes, you really needed another episode to explain agent plumbing.)

### [sanand0/talks](https://github.com/sanand0/talks)

_Conference and workshop artifacts become repeatable assets when captured thoughtfully._

- **Added IIM Alumni SG workshop materials.** Uploaded slides, transcripts, and long-form chat logs for the 23 May workshop ([f825cfa](https://github.com/sanand0/talks/commit/f825cfa2fc74733e8b5b957a48abc40224d67706), 23 May 2026). These files enable repurposing into posts and prompts. Takeaway: capture raw sources to make derivative content trivial.
- **Prompts and narrative drafts included.** The folder includes prompts.md and story drafts for reuse in future workshops and content. That shortens prep for follow-ups. Takeaway: ship the recipe, not just the dish.

(Bring snacks to long workshops. And a backup HDMI cable.)

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Keep the model cost/quality frontier current so teams route wisely._

- **Frontier data refreshed.** Updated ELO and pricing data and bumped the README "Last updated" date ([9d6aa55](https://github.com/sanand0/llmpricing/commit/9d6aa551253da12fe83472a7effd57e8239d8094), 21 May 2026). This keeps model comparisons actionable. Takeaway: stale benchmarking misleads production choices.
- **Bulk ELO CSV updates.** The leaderboard dataset (`elo.csv`) received a large refresh, making pareto calculations more accurate. Takeaway: recompute frontiers after provider changes.

(Yes, the frontier moved again. Surprise.)

### [sanand0/til](https://github.com/sanand0/til)

(Notes that are slightly less ephemeral than the internet.)

- **Harden trending fetch and refresh notes.** Rewrote `trending-repos.sh` to detect tools, isolate temp workspaces, and fail fast when missing deps ([993ccd2](https://github.com/sanand0/til/commit/993ccd232a63de26effc7de4e52f19a05365c8d5), 17 May 2026). This makes weekly repo pulls reliable. Takeaway: make periodic jobs explicit about their runtime needs.
- **Update TIL entries and trending TSV.** Added May notes and refreshed `trending-repos.tsv` for May 17. That preserves provenance for future recall. Takeaway: small maintenance avoids future archaeology.

(Yes, trending lists deserve careful temp-file hygiene.)

## Lessons

- Label generated content visibly. Small visual cues reduce confusion and legal risk.  
- Make local data agent-ready. Exported, timestamped, and deduplicated files unlock reliable automation.  
- Filter early. Skip trivial inputs to save API costs and human time.  
- Prefer predictable defaults. Deterministic file names and idempotent backups simplify pipelines.  
- Log the right things. Quiet logs for normal runs, full dumps on failures for debugging.  
- Frontiers move fast. Recompute model routing and cost analyses after provider changes.

## Suggestions

- Test the AI badge visually in both themes and on small screens. Add a tiny automated visual diff (asciinema or Percy) for regressions.  
- Add a unit/integration test that validates `section[ai-disclosure]` insertion and footer text. Fail CI on regressions.  
- Add a lightweight privacy checklist for any local-data tool that touches calendars, WhatsApp, or LinkedIn. Include retention and redaction rules.  
- Create a small benchmark that measures "completed-task cost" across a few routing options. Automate it and record results in llmpricing.  
- Add a daily-activities CI job that runs on a small sample dataset to catch regressions in summarize/skipping logic.  
- Consider adding a one-click "revoke app access" link in googleconnections output (documentation link to the Google account page). Practical and calming.