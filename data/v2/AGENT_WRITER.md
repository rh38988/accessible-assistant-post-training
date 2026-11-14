# Writer agent instructions

You write supervised training examples (English) for a small model that gives tech help to older adults. Repository: /home/claude/accessible-assistant-post-training

1. Read `data/v2/GENERATION_SPEC_v1.md` completely and follow it exactly. If your batch name starts with `fx`, also read `data/v2/FILL_INSTRUCTIONS_v1.md`.
2. Read your assignment file (given in your prompt). It lists your batch name, your spec file path, and your tasks.
3. Work ONE TASK AT A TIME: WebFetch the official page, write `source_notes`, write that task's examples, save the spec file, then run the builder. Saving after every task matters: if you are interrupted, finished tasks survive.
4. If your spec file already exists, a previous run was interrupted. Read it, keep the tasks that are already complete, and write only the missing ones.
5. Build until it prints OK:
   `cd /home/claude/accessible-assistant-post-training && python3 data/v2/tools/build_v2.py <batch>`

Rules that matter most:
- Every step, label, number, phone number, and web address must be supported by the page you read. Never write from memory. Never bridge a gap with vague wording.
- Missing a required action from the source is the most common failure. Check each answer against your notes step by step.
- The reply must do exactly what the user asked. A missing-information reply is exactly ONE short question.
- Do not open anything under `eval/`. Do not edit any file other than your own spec file and your report.
- Be economical: fetch each page once or twice, do not re-read files you already read.

When finished, write a short report to `data/v2/reports/<batch>.gen.md`: for each task the source URL used; topics replaced by backups and why; anything you are not fully sure the page supports; for `fx` batches, any EXISTING example the source shows is wrong (id and what). Then reply with ONE line only, like: `ny1a: 7 tasks, 42 examples, builder OK`.
