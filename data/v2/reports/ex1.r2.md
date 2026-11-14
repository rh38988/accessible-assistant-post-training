# Review report: batch ex1, round 2 (re-review of revised examples)

Checker: `python3 data/v2/tools/check_review.py ex1 2` printed OK (13 reviews).

## Decision counts

- keep: 7 (pilot-001, pilot-002, pilot-004, pilot-005, pilot-006, pilot-009, pilot-011)
- revise: 6 (pilot-003, pilot-007, pilot-008, pilot-010, pilot-012, pilot-013)
- reject: 0

## Most common problems

1. Unsupported control descriptions or positions (3 examples): pilot-003 ("next to the typing box"), pilot-008 ("the Windows logo" on Start, "Its icon is a gear" on Settings), pilot-013 ("at the top" for your name).
2. Steps or sentences not in the cited page (2 examples): pilot-007 step 6 "Confirm the connection." (no such action on either Apple page); pilot-010 "because you can still open your iPhone" and "Write the new password down and keep it somewhere safe at home."
3. Limit stated without its condition (1 example): pilot-012 states the 25 MB Drive-link rule for all accounts; the page applies it to personal Gmail accounts.

## Source notes

- pilot-007: the move-closer advice is supported by the router section of https://support.apple.com/en-euro/111786 ("you might be too far from the signal"), so it is not counted as unsupported.
- pilot-010: "Never give it to anyone who calls or texts you offering help with your account." is supported by https://support.apple.com/en-us/102568 ("never share your Apple Account password or verification codes with anyone"; "Apple never asks for this information to provide support"). That page is not cited yet and is added as a second source in the fix.
- pilot-011: the "(it may ask for your passcode)" hedge is kept as supported, because the page links to "If you don't know your passcode, find out what to do" in the same section. The "Update Now" button label is supported by the screenshot alt text ("update now").
- pilot-005: the cited page (https://support.google.com/mail/answer/7074871) covers Gmail not loading in a browser, not new mail missing from an inbox. The reply contains only a clarifying question, so it passes. Any later round that adds email-address or Gmail Settings steps will need another source.

## Unreadable pages

None. Every cited page was fetched; the Samsung, Android, Google Messages, Apple (102616, 111107, 111786, 101567, ht201487, 102568, 118575, iCloud photos), Microsoft (fb830bff, c3095a80) and Gmail (6584) pages all returned content.
