## A week of polishing tools, posts, and agent-ready benchmarks

Small infra wins and focused features made developer workflows friendlier and models easier to evaluate. The key lesson: make telemetry and doc changes first — they payoff when things break or need auditing.

### [sanand0/scripts](https://github.com/sanand0/scripts)

_This week focused on making scripts auditable, smaller, and safer—so tools actually help you recover and reproduce work._

- **Record model + cost in transcripts.** transcribe_calls now writes `model:` and `cost:` into note frontmatter, so transcripts carry exact billing and model metadata. See [fbd7958](https://github.com/sanand0/scripts/commit/fbd7958bf40da02bcc7bf8c920edc45235c271cd) (01 Aug 2026). Takeaway: store provenance with data; it saves forensic time later.
- **Archive unused Fish helpers.** Cleaned setup.fish and moved rarely used functions to `archive/` to reduce startup clutter. See [8b38efe](https://github.com/sanand0/scripts/commit/8b38efe80bad56e25d4d5fa10e6c5389284835b5) (31 Jul 2026). Takeaway: small shell cleanups speed daily development.
- **Make clipboard tools observable.** rofi-clip and rofi-prompts now log activations to ~/.local/share/sanand-scripts/*.tsv. See [4cbad7d](https://github.com/sanand0/scripts/commit/4cbad7dd65a60e2322a0ec70a74a35fdf7fc15f7) (30 Jul 2026). Takeaway: log UI actions to learn what people actually use.
- **Smarter text normalization.** rofi-clip’s anyascii step now handles em-dashes and bullets more robustly. See [f0345a0](https://github.com/sanand0/scripts/commit/f0345a0586605fd26e0d7e5b587ad6f6c50b1b51) (31 Jul 2026). Takeaway: sanitize early to avoid downstream surprises in copy/paste.
- **New tooling and server improvements.** Added fish_usage.py to profile Fish functions, tightened mcpserver to ignore unknown params, and improved htmlemail to accept HTML inputs. See [758183b](https://github.com/sanand0/scripts/commit/758183bc4a9b71634fe2a4c6875b78e0f9a6b776) (31 Jul 2026), [401b116](https://github.com/sanand0/scripts/commit/401b11614f558cca6379403d0f406d123d6c590c) (29 Jul 2026), and [d10945d](https://github.com/sanand0/scripts/commit/d10945d75c98f1da932f8de7e1e0e668738d7dbb) (29 Jul 2026). Takeaway: prefer small, testable server changes that fail gracefully.

(Yes, you really needed another log file. It helps.)

### [sanand0/blog](https://github.com/sanand0/blog)

_New posts and prompt recipes to make agent workflows and LLM strategy visible and reusable._

- **Agent experience post.** Published "Agent Experience is the new User Experience." It frames agent-focused design patterns. See [d795a31](https://github.com/sanand0/blog/commit/d795a3126d03eb2c374493e1d073a517f6030d6e) (01 Aug 2026). Takeaway: design artifacts for agents, not merely humans.
- **LLM cost-vs-capability story.** Added an analysis post and embedded the LLM Pricing interactive chart. See [828d83c](https://github.com/sanand0/blog/commit/828d83c1469d54f79ab222d42d4806e0c7ca2735) (01 Aug 2026). Takeaway: visualize cost and capability to pick models smartly.
- **Email-as-agent writeup.** Long-form writeup on turning email into a trusted AI assistant. See [d31b8dc](https://github.com/sanand0/blog/commit/d31b8dce4ff8bdcc9e4d03fd76b7c6c5c6342516) (27 Jul 2026). Takeaway: start with a few context-rich people to bootstrap adoption.
- **Prompt/product updates.** Added and refined many prompt templates and publishing metadata. See [ddc0ce3](https://github.com/sanand0/blog/commit/ddc0ce31295c6d948999dcd3c85f7ef4097639e3) (01 Aug 2026). Takeaway: keep copy and prompts close to content for consistent reuse.

(Yes, another blog post. This one buys forward compatibility with agents.)

### [sanand0/research](https://github.com/sanand0/research)

_Experiments and evidence on how prompting affects model reasoning._

- **Evidence: simplifying writing can hurt thinking.** Added experiments and evals showing "Answer in ASD-STE100" reduced model thinking quality. See [6000a1c](https://github.com/sanand0/research/commit/6000a1ca14bf813963ad868193f3250a4bfd62b9) (01 Aug 2026) and supporting evals [54025f7](https://github.com/sanand0/research/commit/54025f78b44f21ab9b84221e449ff23912c358f9) (01 Aug 2026). Takeaway: simplicity constraints can trade clarity for lost depth.
- **Docs and reproducibility.** Added prompt templating script and many result artifacts for reproducible review. See [2411bf0](https://github.com/sanand0/research/commit/2411bf08f3e79509dec492cff92439dac4637fd8) (01 Aug 2026). Takeaway: publish raw evals to make claims testable.

(A reminder: "simpler" is not always "better" for deep reasoning.)

### [sanand0/llmpricing](https://github.com/sanand0/llmpricing)

_New visual and automation pieces for tracking LLM cost and capability._

- **Intelligence cost curves page.** Added a new "Intelligence" chart and assets for cost curves. See [0787213](https://github.com/sanand0/llmpricing/commit/0787213e7e5cfe5e14d84a6ce508132c06df4968) (01 Aug 2026). Takeaway: separate views help spot strategic model moves.
- **Screenshot automation.** New CLI to capture chart screenshots for model-evolution videos. See [20bcd21](https://github.com/sanand0/llmpricing/commit/20bcd2140482c9608c94300919e84233ec661648) (01 Aug 2026). Takeaway: scripted screenshots make narrative videos reproducible.
- **Model price updates.** Updated model pricing and ELO snapshot. See [51c8ba1](https://github.com/sanand0/llmpricing/commit/51c8ba1d032b3038bf7f5ca48018a42ff2403891) (26 Jul 2026). Takeaway: keep pricing fresh—frontier changes fast.

(Yes, graphs again. But graphs win arguments.)

### [sanand0/tabnotes](https://github.com/sanand0/tabnotes)

-Fixes to restore logic and a small UI/launch-mode UX change.

- **Fix restart recovery.** Reconciler now drops provisional snapshot-less tabs and recovers real records reliably. See [e26555c](https://github.com/sanand0/tabnotes/commit/e26555c9037d717e3295399c9dde1e31529152e0) (27 Jul 2026). Takeaway: prioritize robust restore paths to avoid data drift after crashes.
- **Release & UX defaults.** Bumped to v0.1.2, defaulted toolbar launch to "tab", and added a launch-mode setting. See [6554e2c](https://github.com/sanand0/tabnotes/commit/6554e2cd9d278e679d54564385d484621c08dd7c) (27 Jul 2026). Takeaway: match defaults to actual usage patterns.
- **Better prompts and tests.** Updated prompts for crash scenarios and strengthened reconciliation tests. See [64d5414](https://github.com/sanand0/tabnotes/commit/64d541484b27fa29b4a9e4fa6d8d71b0c9a88f29) (27 Jul 2026). Takeaway: add tests that replicate the worst restart behaviors.

(Yes, side-panel lovers, the tab option is for you.)

### [sanand0/aipipe](https://github.com/sanand0/aipipe)

_Updated provider pricing so hosted tokens reflect new models and rates._

- **Add recent GPT 5.x pricing.** Added gpt-5.5 and gpt-5.6 tiers including luna/terra/sol entries. See [5adcd6b](https://github.com/sanand0/aipipe/commit/5adcd6bd2629883f9fe5748e04a4e2a827ef4c7e) (01 Aug 2026). Takeaway: update pricing quickly to avoid wrong cost estimates in apps.

(Yes, prices keep changing. Automate checks next.)

### [sanand0/anand-skill-mcp](https://github.com/sanand0/anand-skill-mcp)

_Published an embeddable MCP worker that exposes local SKILL.md files as tools._

- **Create static MCP worker toolchain.** Added build.py, README, and Wrangler config to embed SKILL.md files into a Cloudflare Worker. See [308f16a](https://github.com/sanand0/anand-skill-mcp/commit/308f16a6a0a31a0bf322913717a55f546cf8cad3) (31 Jul 2026). Takeaway: exporting skills as tools makes them callable by agents without runtime files.

(Yes, stateless workers are deliciously simple.)

### [sanand0/liveform](https://github.com/sanand0/liveform)

_More flexible forms: randomized choices, audience segments, and a pinned QR UI._

- **Question randomization and segmentation.** Opt-in `randomize: true` for choice questions and segmenting alternatives by email. See [0562408](https://github.com/sanand0/liveform/commit/05624084b9548845e828762819a7cba50a7d0a02) (29 Jul 2026). Takeaway: keep experiment design in the form, not the client.
- **Pinned QR and UI tweaks.** Add QR pinning toggle, compact respondent count, and better results UI. See [0562408](https://github.com/sanand0/liveform/commit/05624084b9548845e828762819a7cba50a7d0a02) (29 Jul 2026). Takeaway: small UI affordances reduce friction in workshops.
- **Sample form and safe defaults.** Replace heavy example forms with a compact sample form and dummy responses. See [2f4b028](https://github.com/sanand0/liveform/commit/2f4b0285cb8b38c57b82bc7c83c4d7a8ab099f05) (08 Jul 2026). Takeaway: ship a minimal example that’s safe to run locally.

(Yes, pin that QR — it beats everyone shouting the code.)

### [sanand0/til](https://github.com/sanand0/til)

_New weekly notes and trending repo updates._

- **Add TIL and trending updates.** New TIL entries and refreshed trending repos dataset. See [7043193](https://github.com/sanand0/til/commit/70431930237f02c3e973193a222e1d8d95337ec3) (27 Jul 2026). Takeaway: keep a steady, small cadence of notes; they compound.

(Inevitable: you learned something. Record it.)

## Lessons

- Log first, fix later. Small telemetry makes debugging cheap and safe.
- Metadata travels with data. Embed model, cost, and provenance in artifacts.
- Simplicity prompts can reduce depth. Test prompt constraints for thinking loss.
- Reproducible visuals matter. Scripts that capture charts enable narrative videos.
- Defaults should match real usage. Tiny UX changes cut support noise.

## Suggestions

- Add automated checks that surface inconsistent frontmatter (missing model/cost). This prevents silent billing drift.
- For the simplification experiment, run a small blinded human evaluation to confirm the metric-driven finding.
- In llmpricing, add a nightly scraper for provider prices and a simple alert when frontier shifts occur.
- In tabnotes, instrument a minimal telemetry toggle to measure how often users prefer "tab" vs "side-panel".
- In liveform, consider a lightweight A/B analysis pipeline to measure randomization/segment effects on respondent balance.

If you want, I can draft the short changelog lines for each repo ready to paste into release notes.