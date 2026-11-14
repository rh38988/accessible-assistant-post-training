# Review report: batch ex2, round 2

Input: data/v2/reviews/input/ex2.r2.md (25 examples, all listed in ex2.r2.todo.json).
Output: data/v2/reviews/ex2.r2.py. Checker: `check_review.py ex2 2` prints OK.

## Decision counts
- keep: 14
- revise: 11 (gate source fail: 10; gate source unverified: 1)
- reject: 0

Kept: tr021-a, tr021-d, tr022-a, tr022-d, tr025-a, tr025-c, tr026-b, tr026-c, tr030-a, tr030-c, tr030-d, tr031-b, tr031-c, tr031-d.

Revise: pilot-014, pilot-015, pilot-016, tr024-a, tr024-c, tr024-d, tr025-d, tr026-a, tr026-d, tr027-d, pilot-017 (source unreadable).

## Most common problems
1. Wording that goes beyond the cited page (6 examples): an instruction or label not on the page (pilot-014 "don't read out any numbers"; pilot-015 "just ignore it" and "call right away ... tell them what happened"; pilot-016 "call your card company right away"; tr025-d "Samsung screens"; tr027-d Gallery labels).
2. Wrong source for the claim (3 examples): tr024-a, tr024-c, tr024-d cite an Apple alarm-volume article (118444) for the ringer slider. The Quick way steps are supported by 105103.
3. Overstated condition (2 examples): tr026-a and tr026-d say Wi-Fi Calling is used "when the cell signal is weak". The page says "in an area with little or no cellular coverage".
4. Report address differs from the cited article (pilot-014): the article gives www.ftc.gov/complaint; ReportFraud.ftc.gov appears only in site navigation.

## Unreadable pages
- https://www.facebook.com/help/120939471321735: WebFetch returned robots_disallowed on two tries. pilot-017 is set to source "unverified" and decision revise. Its clarifying question is appropriate, but the later steps it promises could not be checked.
- No other page was unreadable. Several claims needed a second fetch (FTC node 54353 for ReportFraud and numbers; FTC node 84809 for "ignore" and "already sent code"; Apple 108066 for "weak signal"; Google 9075928 for Collections location and Gallery labels). All were resolved on that second fetch.

## Notes
- No review file was written outside data/v2/reviews/ex2.r2.py and this report.
- Round 1 files were not used as input for the decisions; each example was judged from its round 2 text against the source.
