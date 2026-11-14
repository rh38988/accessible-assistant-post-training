# Fill instructions v1: add examples to existing tasks

Read `data/v2/GENERATION_SPEC_v1.md` first. Everything there applies. This file adds the rules for extending tasks that already have examples.

You are given one existing spec file, `data/v2/specs/ex<K>.py`. It holds the existing examples for about 13 tasks. Treat it as read-only. You write a NEW file, `data/v2/specs/fx<K>.py`, that contains only the new examples.

## What to add

Goal: every task ends up with exactly 6 examples, each a different scenario.

- **Task with examples a, b, c, d** (most tasks): add `e` (constraint) and `r` (failure_recovery). For safety tasks (`"sensitive": True` scam topics), `r` is the `already_acted` scenario (2 messages are enough, style `failure_recovery`).
- **Task that already has `r`**: add only what is missing to reach 6.
- **Task with a single pilot example** (its id looks like `pilot-0NN`, suffix `p`): add 5 examples so that the task covers these scenarios once each, counting the pilot example as whichever scenario it already is:
  - device or app task: direct (`a`), direct_messy (`c`), missing_info (`b`), followup (`d`), constraint (`e`), failure_recovery (`r`)
  - safety task: direct (`a`), direct_messy (`c`), constraint (`e`), already_acted (`r`), helper (`f`), prevention (`g`)
  - If the pilot example is already a missing-information example, write the followup so that it starts with the pilot example's exact user message and exact clarifying question.
  - If the task's platform is `unknown` (the pilot user did not name a device), write the direct examples for the device or app that the cited source covers, and say that device in the user message.

Use suffixes that are not already used in that task. The builder creates ids as `tr<NNN>-<suffix>`.

## How to write them

1. For each task, WebFetch the cited source page(s) yourself and write `source_notes`, exactly as in the generation spec. Do not rely on the existing examples for facts: they are unreviewed drafts and may contain mistakes.
2. In your file, repeat each task's `task_id`, `task_type`, `task`, `platform`, `category`, `sensitive`, and `source` exactly as in the existing file. Put only your new examples in `examples`.
3. Every new opening message must be clearly different from the existing examples in the same task (the builder checks this). Only a followup reuses a missing-information opening.
4. The first assistant message of a failure-recovery example must be a complete, correct answer in its own right.
5. If the source shows that an existing example is wrong, do not edit it. Mention it in your final report (example id and what is wrong).
6. If a cited page cannot be read, try once more with a different question. If it still fails, skip that task and say so in your report.

Build and check:

```bash
cd /home/claude/accessible-assistant-post-training && python3 data/v2/tools/build_v2.py fx<K>
```
