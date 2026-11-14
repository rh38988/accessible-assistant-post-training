# Review report: batch ex1, round 3 (final re-review)

Input: data/v2/reviews/input/ex1.r3.md (6 examples, rendered from reviews/ex1.r3.todo.json).
Reviews: data/v2/reviews/ex1.r3.py (checker: OK).

Decisions: 5 keep, 1 reject, 0 revise (round 3 allows only keep or reject).

| id | decision | reason |
|---|---|---|
| pilot-003 | keep | Google Messages steps match the page (Gallery, Send). |
| pilot-007 | keep | iPhone Wi-Fi steps match the cited Apple pages. |
| pilot-008 | keep | Windows 11 Display > Scale & layout > Scale matches the page. |
| pilot-010 | keep | Change Password steps and the one-hour note match the cited Apple pages. |
| pilot-012 | keep | Gmail Attach, Open, and 25 MB / Drive link match the page. |
| pilot-013 | reject | Gate G1 fails: "start saving to iCloud on their own" and "safe even if the phone is lost or broken" are not on the cited page. |

Most common problem: unsupported protection or automatic-behavior claims in a reply that otherwise has correct steps (one example).

Unreadable pages: none. All six source pages returned usable text.

Notes for the Data Lead:
- pilot-013 is a reject because round 3 is the last allowed re-review. The fix text in the review record describes what a rewrite would need, but the example needs a human decision on whether to keep it.
- Several source pages (Apple en-au/111107, Apple en-mz/101567) cover the steps; the Apple 102568 and ht201487 pages do not cover the password-change steps. pilot-010 is kept on the strength of 101567, which does cover them.
