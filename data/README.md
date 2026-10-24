# Data

Owner: **Data Lead**

Training examples live in JSON Lines files (`.jsonl`): one JSON object per line.

- `pilot/` : the small pilot batch (start here, about 50 examples)
- `train/` : the full training set once the pilot is reviewed

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

## Pilot v1 (`pilot/pilot_v1.jsonl`)

20 examples drafted by Claude on 2026-10-24. **All need team review before training.**

- 8 underspecified (40%), 12 fully specified; 3 in zh-TW (15%); 6 sensitive
- User messages follow the task types and phrasing styles of:
  - **ElderBench** (Sharifi et al. / arXiv 2609.04850): everyday phone tasks, phrased the way older adults speak
  - **OATS** (Shomee et al. / arXiv 2601.10018): verbose, over-specified, under-specified, and incomplete requests
  - **GrandGuard** (arXiv 2605.20203): risks specific to older users, such as scams and privacy
- Every reply's steps were checked against the cited official page on the access date
- Review checklist: tone, step accuracy against the source, and whether clarifying questions are actually needed

## Rules

- **Only the last assistant turn is trained on.** Earlier turns are context. For a multi-turn example, make sure the final assistant reply is the behavior you want to teach.
- **Target ratio:** about 40% `underspecified`, 60% `fully_specified`. The validator prints the current ratio. Keep it the same as the eval set.
- **Underspecified examples** should usually ask one short clarifying question, not guess.
- **Fully specified examples** should answer directly. Asking an unnecessary question is a mistake we measure.
- **No leakage:** do not write training examples for the exact tasks used in `eval/scenarios/`. Coordinate with the Evaluation Lead.
