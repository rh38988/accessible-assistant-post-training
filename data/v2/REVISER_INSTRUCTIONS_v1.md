# Reviser instructions v1

An independent reviewer checked a batch of training examples against their official sources and marked some as `revise`. Your job is to fix exactly those examples.

Read `data/v2/GENERATION_SPEC_v1.md` first: the fixed examples must follow it.

## Steps

1. Open the revision list you were given (`data/v2/reviews/input/<batch>.revise<N>.md`). For each example it lists the reasons, the requested fix, unsupported claims, and missing required actions.
2. For each listed example, WebFetch the cited source page yourself and confirm what the page really says before changing anything. Apply the fix using only what the page supports. If the reviewer's requested fix is itself not supported by the page, follow the page and say so in your report.
3. Edit ONLY the listed examples in `data/v2/specs/<batch>.py`. Change the message text (and `platform` or `style` if the fix requires it). Do not change ids, suffixes, authors, or any other example.
4. Keep the pairs consistent: if you change the clarifying question of a missing-information example, make the same change in the second message of its follow-up example in the same task (same opening message), and make sure the user's answer in the follow-up still makes sense. If that follow-up is not on your list, you may still edit its second and third messages for this purpose only, and list it in your report.
5. A missing-information reply must be exactly ONE short question. If two details seem needed, ask for the one that changes the steps the most (usually the device or the app).
6. Remove details the reviewer marked unsupported (for example an icon description or a position that the page does not give) instead of rewording them. Remove pasted double lead-ins and steps for models the user does not have.
7. If the reviewer names a second official page that supports part of the reply, read that page yourself, and if it does, add it to that example: give the example a `"sources"` list with both pages, each as `{"title": ..., "url": ..., "accessed": "2026-11-13"}` (keep the original source first, with its original `accessed` date if it has one).
8. If an example cannot be fixed from the source (the page does not cover it), leave it unchanged and list it in your report as "cannot fix".
9. Rebuild until it prints OK:

```bash
cd /home/claude/accessible-assistant-post-training && python3 data/v2/tools/build_v2.py <batch>
```

For existing drafts the builder shows some style problems as warnings only. For the examples on your list, fix those warnings too.

## Report

Reply with: ids fixed, ids you could not fix (and why), any follow-up examples you touched for consistency, and any case where the page contradicted the reviewer.
