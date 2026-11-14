# Review report: batch fx6, round 3 (final re-review)

Decisions: 1 keep, 5 reject, 0 revise. Round 3 is the last allowed re-review, so no revise was issued.
Checker: `python3 data/v2/tools/check_review.py fx6 3` printed OK (6 reviews).

| id | decision | main reason |
|---|---|---|
| tr076-e | reject | S4 = 1: "Tap the link" gives no cue that a link appears over the code (Apple page says it does). Borderline. |
| tr079-r | keep | All gates pass; Safety / Personal Safety names, steps, and Android 12 fallback match the Google page. |
| tr083-e | reject | Source gate fail: says search covers cloud accounts with no sign-in condition (page: cloud search must be enabled via Start > Settings > Accounts). |
| tr086-e | reject | S4 = 1: step 3 bundles forwarding to reportphishing@apwg.org with reporting at ReportFraud.ftc.gov. |
| tr086-r | reject | S4 = 1 (update/scan/delete bundled; two reports bundled); S1 = 1 (computer-access branch omits change passwords and two-factor). |
| tr088-e | reject | S4 = 1: step 3 bundles reporting at ReportFraud.ftc.gov with telling the dating site. |

Most common problems:
- Bundled steps (S4) in 4 of 6 examples: two separate reporting destinations or several actions joined by "and" or "Then" in one numbered step.
- One unconditioned cloud-search claim (tr083-e).
- Incomplete conditional branch (tr086-r, password and two-factor step missing).

Source pages read: all six pages fetched once (Apple 102680; Google Personal Safety 9319337; Microsoft Find my downloads; FTC phishing; FTC what to do if scammed; FTC romance scams). All were readable. No page was unreadable.

Note: the S4 bundling rule is applied as written in the rubric ("bundles clearly separate actions"). Under a looser reading, tr076-e, tr086-e, and tr088-e would be keep. The Data Lead should confirm before these are treated as settled.
