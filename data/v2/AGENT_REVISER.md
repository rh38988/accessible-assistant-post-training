# Reviser agent instructions

Repository: /home/claude/accessible-assistant-post-training

1. Read `data/v2/GENERATION_SPEC_v1.md` and `data/v2/REVISER_INSTRUCTIONS_v1.md` completely and follow them exactly.
2. Your prompt names one or more batches and a number N. For each batch, the revision list is `data/v2/reviews/input/<batch>.revise<N>.md` and the file to edit is `data/v2/specs/<batch>.py`.
3. Work one source page at a time and save the spec file after each page, so finished fixes survive an interruption. If you were interrupted before, compare the spec with the revision list and continue with the examples not yet fixed.
4. Rebuild each batch until it prints OK:
   `cd /home/claude/accessible-assistant-post-training && python3 data/v2/tools/build_v2.py <batch>`
5. Do not open anything under `eval/`. Edit only the listed examples (plus a follow-up's earlier turns when needed for consistency).
6. Be economical: one or two fetches per page.

When finished, write a short report to `data/v2/reports/<batch>.revise<N>.md` (ids fixed, ids you could not fix and why, follow-ups touched, any case where the page contradicted the reviewer). Then reply with ONE line only, like: `ex8 revise1: 21 fixed, 1 cannot fix, builder OK`.
