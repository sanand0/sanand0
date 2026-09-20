## A week of cataloguing, calm UX fixes, and sharper LLM checks

Small releases and big datasets landed this week. The lesson: automate the boring bits, then stress-test the hard bits.

### [sanand0/blog](https://github.com/sanand0/blog)

_This week focused on turning talks into posts, tuning prompt fragments, and adding practical writeups so readers can act faster._

- **Bulk talk posts added.** Generated many talk posts and a deterministic talk generator (`scripts/talks.py`) to avoid manual edits ([5e125b6](https://github.com/sanand0/blog/commit/5e125b677154350d9e012bf9608ac60116cdf01e), 19 Sep 2026). This makes publishing repeatable and reviewable. Takeaway: one source of truth beats ad-hoc file edits.
- **Prompt & AI-advice edits.** Small but useful copy and structure fixes in prompts and advice pages ([b4a2166](https://github.com/sanand0/blog/commit/b4a2166ea71ec13d88c12c96dc5d4b8a1b63ec22), 19 Sep 2026). Rules tightened for diarization and fragments. Takeaway: clear prompts reduce downstream surprises.
- **New posts: case notes and practical fixes.** Added posts like the India Fast Track story and several talk writeups ([0c05281](https://github.com/sanand0/blog/commit/0c05281cfd36074b35cbd70fb68e37d0db3524ab), 18 Sep 2026; [6b4cf19](https://github.com/sanand0/blog/commit/6b4cf199776e2d7cf5ba802effff669c4283a132), 18 Sep 2026). These are short, actionable reads for visitors. Takeaway: small, true stories help readers quicker than long essays.
- **Improve fake-data skill & case study prompts.** Revised guidance and sanity checks in fake data and case-study prompts ([2c92538](https://github.com/sanand0/blog/commit/2c925387fde362f1486c78752d243f2933976c6e), 18 Sep 2026). It forces seeded checks and multi-seed robustness. Takeaway: simulate mechanisms, not outcomes.

(Yes, the blog now ships more scripts than a startup. That’s by design.)

### [sanand0/talks](https://github.com/sanand0/talks)

_Moved the talk catalog to a tidy single source and added tooling to generate site entries reliably._

- **Single config source.** Switched to `config.json` as the canonical talks source and generated the README from it ([17a0c0c](https://github.com/sanand0/talks/commit/17a0c0cc264a69388bc58a68f80e722c66ab1f8e), 15 Sep 2026). This simplifies updates and prevents drift. Takeaway: one JSON file is much easier to audit than scattered markdown.
- **Generator + index tooling.** Added `generate.mjs`, `enhance-index.mjs`, and a build step to render HTML from the config ([17a0c0c], 15 Sep 2026). It auto-inserts icons and consistent dates. Takeaway: automation keeps presentation consistent.
- **Skill docs: update config.json not README.** Agent skill guidance now edits `config.json` and runs `just build` rather than patching generated files ([2f6bcb2](https://github.com/sanand0/talks/commit/2f6bcb293353a625c7e6fbeb6dcad95e43b56850), 18 Sep 2026). That preserves regeneration semantics. Takeaway: teach agents to edit source, not derived artifacts.

(Yes, one more build script. It earns its keep.)

### [sanand0/llmevals](https://github.com/sanand0/llmevals)

This repo grew into a proper evaluation pipeline. Expect sharper model claims and empirical guardrails.

- **Jev BANKING77 benchmark added.** Full runner, analyzer, data, and report for Jev vs frontier LLMs were added ([2c7a29f](https://github.com/sanand0/llmevals/commit/2c7a29ff39c719de7451f6a16efa4cfac3b9ae9d), 18 Sep 2026). It produces results.jsonl, summary.json, CSVs, and an index page. Takeaway: freeze inputs and cache outputs for reproducible comparisons.
- **Logprob experiment and holdout added.** Scripts to capture first-token logprobs, calibrate them, and run a 2,310-case prospective holdout were added ([eceb01c](https://github.com/sanand0/llmevals/commit/eceb01c8d647c9af465ffefb016e4075f5236757), 16 Sep 2026). The holdout validated a 5% routing cutoff. Takeaway: validate thresholds on fresh data before deploying automation.
- **Add provenance note.** Linked the ChatGPT source for the Jev analysis to aid reproducibility ([3f03e83](https://github.com/sanand0/llmevals/commit/3f03e83cf04985f7b10843b787cdf3cbc946aeb4), 18 Sep 2026). Takeaway: track where narrative text came from.

(Yes, logprobs are messy. They still help rank risk.)

### [sanand0/llmviz](https://github.com/sanand0/llmviz)

_Small UX and deploy fixes to make the demo easier to open and use._

- **Add “Open app in new tab” link.** README now links to a standalone app page for quick demos ([92d7148](https://github.com/sanand0/llmviz/commit/92d714833877c414be2d33f56fa0c55950747551), 14 Sep 2026). Takeaway: lower friction demos get more eyeballs.
- **Fix AI Pipe redirect encoding.** Properly encode redirect URLs when sending users to AI Pipe login ([5a1b4b7](https://github.com/sanand0/llmviz/commit/5a1b4b70f6a1f383820d6fa4e3065e2319880d5e), 14 Sep 2026). That prevents broken redirects. Takeaway: encode user input before weaving it into URLs.

(Yes, always URL-encode. You will thank the browser later.)

### [sanand0/liveform](https://github.com/sanand0/liveform)

_This week focused on presenter UX and safe, auditable presenter edits._

- **Preserve viewport on updates.** Implemented anchor capture/restore to avoid scrolling users to top on updates, plus a browser smoke test ([76b6464](https://github.com/sanand0/liveform/commit/76b64645cfa5b9bca89515b63878bcd5c583b3f2), 13 Sep 2026). This keeps respondents in place while the form updates. Takeaway: small UX fixes vastly reduce live-session friction.
- **Show/Hide presenter control persisted to YAML.** Added show/hide visibility control in results UI, server endpoints, and safe YAML edits with conflict checks ([db4da63](https://github.com/sanand0/liveform/commit/db4da6345ac1b90afeaf7329c8a9c0673836a093), 13 Sep 2026). Writes fail with 409 on stale edits. Takeaway: persist presenter changes atomically and test for races.
- **Tests & auth checks.** Added tests to ensure only allowed presenters can toggle visibility and that audience clients stay consistent. ([db4da63], 13 Sep 2026). Takeaway: test the admin paths; people will click buttons you forgot to protect.

(Yes, presenters now get a big, tempting “Show” button. Use it wisely.)

### [sanand0/generative-ai-group](https://github.com/sanand0/generative-ai-group)

_Updated weekly podcast transcripts and extended the digest content._

- **Podcast transcript updates.** Rewrote and extended the weekly digest transcript and notes for 13 Sep 2026 ([7bd808b](https://github.com/sanand0/generative-ai-group/commit/7bd808b549b288e3e7955203050805a839670f3a), 13 Sep 2026). The piece highlights verification culture and agentic math claims. Takeaway: public threads make good source material, but verify before amplifying.
- **Compact draft added.** Also checked in a shorter episode draft version for quick sharing ([fc06b8e](https://github.com/sanand0/generative-ai-group/commit/fc06b8edaab755d944c67bdf0f94b028d8a27731), 13 Sep 2026). Takeaway: keep long and short versions handy for different channels.

(Yes, a podcast about podcasts. Meta and useful.)

### [sanand0/tools](https://github.com/sanand0/tools)

_Added a new bookmarklet to capture ChatGPT sidebar chat links for faster research exports._

- **ChatGPT sidebar scraper.** New bookmarklet scrapes chat titles and URLs from ChatGPT sidebar, with Markdown/JSON copy options and tests ([b50add3](https://github.com/sanand0/tools/commit/b50add33518ae73a6e6d3b242b3e39a3e170feae), 18 Sep 2026). It supports scrolling to reveal virtualized items. Takeaway: small tools save minutes that add up to hours.
- **Landing page and docs updated.** The aiscrapers page and tests got matching updates so users discover the new tool easily ([b50add3], 18 Sep 2026). Takeaway: ship the UI and the tests together.

(Yes, another bookmarklet. Because copy-paste is still a feature.)

### [sanand0/aipipe](https://github.com/sanand0/aipipe)

_A small but important auth/redirect fix for trusted GitHub Pages flows._

- **Allow trusted GitHub Pages redirect.** Login redirects now allow a trusted origin (sanand0.github.io) in addition to same-origin ([ac2ca50](https://github.com/sanand0/aipipe/commit/ac2ca501e094f5c70e3530b16efc829f5b149194), 14 Sep 2026). This enables smoother integrations. Takeaway: whitelist trusted origins when same-origin is too strict.

(Yes, one more exception to the same-origin club.)

### [sanand0/til](https://github.com/sanand0/til)

_Weekly notes updated with firmware, forecasting, and browser observations._

- **TIL updates.** Added September notes on firmware reverse-engineering, agent risks, and browser-in-the-cloud quirks ([51abe30](https://github.com/sanand0/til/commit/51abe307071975cd91f0c3a945ac10a73382bbb4), 14 Sep 2026). Takeaway: write short notes; you’ll find them later when you need them.

(Yes, the fridge may be listening. Treat it like a colleague.)

### [sanand0/llmrandom](https://github.com/sanand0/llmrandom)

_Re-ran the classic “pick a number” experiment with newer models and added a resumable runner._

- **Reran with newer models.** Added a robust runner and resumed experiment with GPT-4.1 Nano and GPT-5.6 Luna ([6b85caa](https://github.com/sanand0/llmrandom/commit/6b85caacbd8f7091a41971c4acd4a6f7e7e2a495), 14 Sep 2026). Results and README updates show strong modal preferences. Takeaway: randomness in LLMs is model-shaped, not uniform.
- **Checkpointed results.json.** The script saves after each response so runs resume safely. Cost summary included. Takeaway: checkpoint writes make long API runs robust.

(Yes, models are reliably unreliable.)

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_Small data refresh to keep the frontier updated._

- **Model updates.** Updated `elo.csv` and model rankings to reflect recent leaderboard shifts ([ed20fd3](https://github.com/sanand0/llmpricing/commit/ed20fd3113714d51ac817363e657dc4092202b81), 13 Sep 2026). Takeaway: refresh the frontier often; prices and quality move fast.

(No, the cost curve did not pause for lunch.)

## Lessons

- Reproducibility matters. Freeze inputs, cache outputs, and write deterministic generators for talk posts and benchmarks.
- Validate on holdouts. A threshold that looks good on development can fail in production.
- UX wins are cheap. Preserving scroll position and simple presenter controls make live workshops less stressful.
- Source-as-authority beats patching outputs. Teach tools and agents to edit the canonical file, not derived artifacts.
- Small tooling multiplies productivity. Bookmarklets, scrapers, and short automation scripts save real time.

## Suggestions

- For talks: run the generator on your local talks config and preview with `just build`. Add a small CI job that checks `config.json` edits.
- For llmevals: publish the Jev index page and the logprob holdout summary as a short note. Add a clear README summary for non-technical readers.
- For liveform: run an integrated smoke test in a real small session. Add an audit log for presenter show/hide actions.
- For tools: add a tiny demo gif on the aiscrapers page showing sidebar scroll + copy, to reduce friction for new users.
- For llmrandom: produce a one-page visual summary (histograms by model/temperature) for quicker sharing.
- Consider an automated weekly task: run `just site` for evaluation repos and push a short summary to a private notes file.

If you want, I can:
- Draft a short blog post highlighting the Jev benchmark results for non-technical readers.
- Create a one-page demo that walks users through `just build` for talks and how to preview changes locally.