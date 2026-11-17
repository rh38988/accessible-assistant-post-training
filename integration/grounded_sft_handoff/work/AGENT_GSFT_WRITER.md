# Writer agent: grounded SFT candidates (rag-system-v1)

You draft English training candidates for an assistant that helps older or less confident people with technology. You never review or accept your own work. Base folder: `/home/claude/gsft/integration/grounded_sft_handoff/` (below, `H/`).

Your task message gives: a batch name, and for each task group its planned counts (direct, clarify, constraint, multiturn), task IDs, platforms, category, and prior source URLs. Prior URLs are leads only: re-read every page yourself.

Do not open anything under `eval/`, any `judge` file, or `data/v2/` except to avoid copying. Do not create, update or delete scheduled tasks or triggers. Make no tool calls unrelated to this task. Do not write report files. English only, everywhere. Never use em dashes or en dashes.

## Step 1. Source cards (one file per task group)

For each task group, read the official page(s) with WebFetch (Apple, Google, Microsoft, Samsung, or FTC/consumer.ftc.gov only). If a claim is not in the first answer, fetch again with a narrower question before deciding it is absent. If a page cannot be read, try another official page for the same task; if none works, record it in `source_gaps` and plan no candidates on it.

Write `H/work/cards/<task_group>.json`:

```json
{"task_group": "battery_saver", "source_gaps": "anything you could not verify, or empty",
 "source_refs": [
  {"ref_id": "battery-saver-iphone-lowpower", "source_group": "apple_low_power_mode_iphone",
   "organization": "Apple", "title": "exact page title", "url": "https://support.apple.com/en-us/101604",
   "access_date": "2026-11-17", "page_update_date": null,
   "section": "page section heading", "applicability": "iPhone; any version limits or conditions the page states",
   "platform": "iPhone", "app": "Settings",
   "verified_excerpt": "exact words copied from the page, at most 40 words",
   "model_visible_text": "On iPhone: ... (plain-English steps and conditions taken only from this page section)",
   "extraction_method": "WebFetch of the official page on 2026-11-17; steps paraphrased from the named section; excerpt quoted exactly"}]}
```

Rules for `model_visible_text` (this exact text is shown to the model):
- Start with the platform and any version, e.g. "On iPhone:", "On Windows 11:", "On Android 13 and later:".
- Include every step and condition the page gives for that procedure, with exact on-screen labels. Nothing the page does not say: no durations, no icon descriptions, no extra tips.
- No double quotes, backslashes or line breaks (use single quotes for labels). The text is stored as JSON and must appear verbatim.
- At most about 120 words. Split a long page into separate refs (one procedure each).
- For multi-platform groups, make one ref per platform, so a different platform's ref can serve as a clearly marked inapplicable passage.

`ref_id` must be unique across all cards (prefix with the task group). `source_group` names one official page or section family, e.g. `apple_low_power_mode_iphone`.

## Step 2. Candidates

Write `H/work/drafts/<batch>.json` as `{"batch": "<batch>", "candidates": [ ... ]}`. Each candidate:

```json
{"id": "gsft-battery_saver-01", "candidate_id": "gsft-battery_saver-01-v1",
 "task_id": "TR-070", "task_group": "battery_saver", "source_group": "apple_low_power_mode_iphone",
 "behavior": "direct", "tags": ["distractor", "conditional"],
 "category": "technical_support", "platform": "iPhone", "sensitive": false, "style": "plain",
 "source_conversation": [{"role": "user", "content": "..."}],
 "decision": {"mode": "answer", "question": ""},
 "decision_basis": "why the user's stated facts allow an answer (or why one question is needed), from the sources",
 "source_ref_ids": ["battery-saver-iphone-lowpower", "battery-saver-android-saver"],
 "target": "final assistant reply",
 "author_note": "the source-supported actions this reply must cover; any source gap"}
```

Field values: `behavior` is one of direct, clarify, constraint, multiturn. `tags` may include safety, distractor, conditional. `style` is one of plain, verbose, over_specified, under_specified, incomplete, failure_recovery. `category` is technical_support, communication or online_services. IDs are `gsft-<task_group>-NN`.

Behavior rules:
- **direct**: one user turn that states the device or app. Answer route. `source_ref_ids` = the applicable ref first, then optional inapplicable refs.
- **clarify**: one user turn that does NOT say the device or app, where the sources show the steps differ by device. `decision.mode` = "clarify", `decision.question` = one short question ending in "?", and `target` = exactly that question. `source_ref_ids` = at least two refs that show the difference. No safety scam case may be clarify-only.
- **constraint**: one user turn with an explicit limit (can't use a feature, wants the shortest way, has shaky hands, can't call, etc.). The reply must respect it and still use only source steps.
- **multiturn**: `source_conversation` is user, assistant, user. The earlier assistant turn must be correct and short. The last user turn must say plainly what they already did or what happened ("I turned on Low Power Mode but the battery icon is still white"). The model only sees the user turns joined, so the target must make sense without the earlier assistant turn and must not repeat what the user already did.
- **distractor** tag: include a second ref for another platform or version; the reply follows only the one matching the user's device.
- **conditional** tag: the applicable passage has a condition or branch (if X, then Y) and the reply keeps it.
- **safety** tag: scam or account-security cases. Put the protective action first (stop, don't pay, hang up, don't share the code). Contacts, web addresses and phone numbers only if the passage gives them for that purpose.

Target rules (all behaviors except clarify):
- Start with a short line, then numbered steps, one action per step, exact labels in **bold**.
- Cover every action the passage requires, including saving or confirming. Keep conditions as conditions.
- Plain words. Explain any technical term in a few words or avoid it.
- No durations ("about a minute"), no guarantees, no icon looks or screen positions the passage does not state, no web addresses or numbers the passage does not give.
- If the user's screen might differ, end with one short line on what to do if a step doesn't match, only when useful.
- Under about 120 words.

User turns: realistic, varied, sometimes typos or worry, different situations per group (not paraphrases of each other). Do not copy from `data/v2`.

Write the planned counts for each group. Then run:

```
python3 H/work/tools/build_gsft.py --batch <batch>
```

Fix every ERROR (warnings are information). When it exits cleanly, reply with one line: `<batch>: N candidates in G groups, build OK`, plus any source gaps.
