# Rule scan agent instructions

You check training examples against the spot-check rules and list problems for a person to review.
You do not edit any example and you do not decide keep or reject.

## Read first
1. `/home/claude/accessible-assistant-post-training/data/v2/SPOT_CHECK_RULES_v1.md` (rules R1 to R14, severities, and what not to flag).
2. Your input: `/home/claude/accessible-assistant-post-training/data/v2/rule_scan/input/part_XX.md` (XX is given in your task). It holds about 50 examples. Each has an id, task, platform, scenario, sources, and the conversation. Only the last assistant turn is trained, but earlier turns can also break a rule (for example R7, a clarifying question about the wrong thing).

## How to judge
- Work from the conversation text. Do not fetch web pages.
- Flag only clear cases. If you are unsure, do not flag. A short, correct reply with no problem gets no flag.
- R9 and R13 are about claims. If the claim looks too broad or too precise but you can only confirm it from the source page, still flag it, and set `needs_source_check` to true.
- Use at most 3 rules per example. Pick the most important.
- Read the "Not a problem" list in the rules file before flagging.

## Output
Write one file with the Write tool:
`/home/claude/accessible-assistant-post-training/data/v2/rule_scan/out/part_XX.jsonl`

One JSON object per line, one line for every id in your input, in input order, including ids with no problem:

{"id": "tr001-a", "flags": []}
{"id": "tr001-b", "flags": [{"rule": "R4", "severity": "low", "quote": "turn on RCS chats", "reason": "RCS is not explained", "suggestion": "Add a short plain explanation, for example 'RCS chats (a newer kind of text message)', or drop the term", "needs_source_check": false}]}

- `quote`: the exact words from the reply (under 20 words) that show the problem.
- `reason` and `suggestion`: one sentence each, plain English, no em dashes.
- `severity`: use the rule's severity from the rules file.

Then run:
`python3 /home/claude/accessible-assistant-post-training/data/v2/tools/check_scan.py XX`
If it prints errors, fix your file and run it again until it prints OK.

## Do not
- Do not edit any file except your output file.
- Do not create, update, or delete scheduled tasks or triggers. Make no tool calls unrelated to this task.
- Do not write report .md files.

Reply when done with one line: `part XX: N examples, M flagged, checker OK`.
