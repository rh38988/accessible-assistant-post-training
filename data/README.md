# Data

Owner: **Data Lead**

Training examples live in JSON Lines files (`.jsonl`): one JSON object per line.

- `tasks/` : the training task sheet (`train_tasks.csv`, made by `scripts/task_lists.py`)
- `pilot/` : pilot v1, 20 examples
- `train/` : train v1, 384 examples in 5 batches
- `drafting/` : the specs used to draft train v1

Run the validator before every commit:

```bash
python scripts/validate_data.py --kind train data/pilot/sample.jsonl
```

## Training example schema

```json
{
  "id": "ex-0001",
  "messages": [
    {"role": "user", "content": "How do I make the words bigger on my phone?"},
    {"role": "assistant", "content": "I can help with that. Is your phone an iPhone or an Android phone?"}
  ],
  "specification": "underspecified",
  "category": "technical_support",
  "platform": "unknown",
  "language": "en",
  "sensitive": false,
  "sources": [
    {"title": "Apple Support: Adjust text size", "url": "https://support.apple.com/...", "accessed": "2026-10-24"}
  ],
  "author": "data-lead",
  "reviewed": false
}
```

| Field | Values | Notes |
|---|---|---|
| `id` | unique string | Never reuse an id |
| `messages` | list of `{role, content}` | Roles alternate `user` / `assistant`, starting with `user`, ending with `assistant`. No `system` message: we want this to be the model's default behavior. |
| `specification` | `underspecified` or `fully_specified` | Underspecified = missing a detail needed to answer correctly (device, app, goal, current step). Use the **same definition** as the eval scenarios. |
| `category` | `communication`, `online_services`, `technical_support` | |
| `platform` | free text, e.g. `iOS 18`, `Android 15`, `Windows 11`, `LINE`, `unknown` | Use `unknown` when the user did not say |
| `language` | `en` or `zh-TW` | |
| `sensitive` | `true` / `false` | `true` for payments, passwords, privacy, scams, account recovery. These get an extra review. |
| `sources` | list with `title`, `url`, `accessed` (YYYY-MM-DD) | Required. Where the steps came from. |
| `author` | string | Who wrote or revised the example. `claude-draft` = drafted by Claude, not yet edited by the team |
| `reviewed` | `true` / `false` | Set `true` only after a second team member checks it |
| `inspired_by` | *optional:* `OATS`, `ElderBench`, `GrandGuard`, `original` | Which dataset's task type or phrasing style the user message follows. Messages are written fresh, not copied, because none of these datasets states a license. |
| `style` | *optional:* `plain`, `verbose`, `over_specified`, `under_specified`, `incomplete` | How the user phrases the request (OATS categories) |

## Train v1 (`train/batch_01.jsonl` to `train/batch_05.jsonl`)

384 examples drafted by Claude on 2026-10-24: 4 examples for each of 96 training tasks (TR-021 to TR-116 in `tasks/train_tasks.csv`). With pilot v1, the total is **404 examples**.

- 39% underspecified, 15% zh-TW, 106 sensitive
- Every fully specified answer was checked against a readable official page (Apple, Google, Microsoft, Zoom, FTC, LINE, Taiwan police / 165). Pages that couldn't be read led to the task being swapped out, not guessed.
- zh-TW tasks use only LINE and 165 / police sources, because those pages show the exact Chinese button names. Google and Apple pages returned English labels.
- Each example has a `task_id`. Task types never overlap with `eval/tasks/eval_tasks.csv`.
- How the drafts were generated: `data/drafting/README.md`

**Review checklist for each example:**
1. Steps match the cited source, with button names exactly as written there
2. One action per step; plain language
3. A clarifying question only when the answer really depends on the missing detail
4. Sensitive tasks: safe advice, no requests for passwords or codes, points to official contacts
5. Then set `reviewed: true` and change `author` if you rewrote it

## Pilot v1 (`pilot/pilot_v1.jsonl`)

20 examples drafted by Claude on 2026-10-24. **All need team review before training.**

- 8 underspecified (40%), 12 fully specified; 3 in zh-TW (15%); 6 sensitive
- User messages follow the task types and phrasing styles of:
  - **ElderBench** (arXiv 2609.04850): everyday phone tasks, phrased the way older adults speak
  - **OATS** (Sharifi, Shomee, Medya & Chattopadhyay / arXiv 2601.10018): verbose, over-specified, under-specified, and incomplete requests
  - **GrandGuard** (arXiv 2605.20203): risks specific to older users, such as scams and privacy
- Every reply's steps were checked against the cited official page on the access date
- Review checklist: tone, step accuracy against the source, and whether clarifying questions are actually needed

## Rules

- **Only the last assistant turn is trained on.** Earlier turns are context. For a multi-turn example, make sure the final assistant reply is the behavior you want to teach.
- **Target ratio:** about 40% `underspecified`, 60% `fully_specified`. The validator prints the current ratio. Keep it the same as the eval set.
- **Underspecified examples** should usually ask one short clarifying question, not guess.
- **Fully specified examples** should answer directly. Asking an unnecessary question is a mistake we measure.
- **No leakage:** do not write training examples for the exact tasks used in `eval/scenarios/`. Coordinate with the Evaluation Lead.
