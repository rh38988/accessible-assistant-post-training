# Review report: batch ex2, round 3 (final)

Input: data/v2/reviews/input/ex2.r3.md (11 examples, all listed in ex2.r3.todo.json; rendered this run with review_io.py because it was missing).
Output: data/v2/reviews/ex2.r3.py. Checker: `check_review.py ex2 3` prints OK. JSONL written to data/v2/reviews/ex2.r3.jsonl.

## Decision counts
- keep: 9
- reject: 2 (pilot-016 for a scoring problem; pilot-017 for an unreadable source)
- revise: 0 (round 3 is final)

Kept: pilot-014, pilot-015, tr024-a, tr024-c, tr024-d, tr025-d, tr026-a, tr026-d, tr027-d.
Rejected: pilot-016, pilot-017.

## Changes from round 2
- pilot-016: the round 2 unsupported-claim finding is withdrawn. The FTC online-shopping page says "call immediately and send a letter to your credit card company", with the 60-day rule, so "Call your card company right away" is supported. The round 2 fix (delete that clause) was not applied, and the example is now rejected on actionability (step 1 bundles several separate actions).
- pilot-014, pilot-015, tr024-a/c/d, tr025-d, tr026-a/d, tr027-d: the round 2 fixes were applied and each cited claim now checks out against its page.

## Most common problems in this round
1. Multiple actions in one step (1 example): pilot-016 step 1 (pay by card, dispute, call, send letter).
2. Unverifiable source (1 example): pilot-017 (Facebook help page blocked).

## Unreadable pages
- https://www.facebook.com/help/120939471321735: robots_disallowed in round 2 (two tries) and again in round 3. Source gate set to unverified; pilot-017 rejected as instructed.

## Notes for the Data Lead (kept examples, minor, not scored down)
- tr024-a/c/d step 1 says "Go to your Home Screen". The Apple page (105103) says only "When you're not using other apps", so "Home Screen" is a reasonable reading, not a quoted label.
- tr027-d says "Here's how ... on your Motorola". The Google page is generic Android and does not mention Motorola. The steps are supported; only the device framing is not.
- tr026-a/d say "open Control Center" without saying how to open it. The Apple page does not say how either.
- pilot-015 closing line "If you already sent the code, contact your bank" goes beyond the FTC page's "if you're worried" wording; the action is the same, so it was accepted.
