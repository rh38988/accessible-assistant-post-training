# ny1b round 2 review report

Batch: ny1b (Apple support pages). Examples reviewed: 14 (tr128-e, tr128-r, tr129-a, tr129-c, tr129-d, tr130-a, tr130-d, tr130-r, tr131-a, tr131-e, tr131-r, tr133-a, tr133-c, tr133-d). Checker: OK.

## Decisions
- keep: 9 (tr128-r, tr129-a, tr129-c, tr129-d, tr130-a, tr130-d, tr131-a, tr131-e, tr131-r)
- revise: 5 (tr128-e, tr130-r, tr133-a, tr133-c, tr133-d)
- reject: 0

## Most common problems
1. Delete button cue (tr133-a, tr133-c, tr133-d): the Messages page says the Delete button is "shown as an icon, with no text label", but the replies tell the user to tap "Delete" with no cue. Actionable = 1.
2. Unsupported source claim (tr128-e): the reply says the speaker's online instructions give the PIN. The Apple page (HT204091) does not say where the PIN is; it only says to consult the accessory's manual or online instructions for help. Source gate = fail.
3. Missing alternative (tr130-r): the page's only alternative for a missing option (account.apple.com, Upgrade Account Security) is not given. Steps = 1.
4. Minor (tr133-d): the opened-message link is described without the "unknown senders" condition, and the order "report first and block them afterwards" is not stated on the page.

## Source notes
- HT204091 and 111804 (iPhone Bluetooth): readable. Pairing-mode and PIN location are not described in the page's own words; the summary of 111804 says the page calls it "discovery mode".
- guide/mac-help/blth1004 (Mac Bluetooth): readable; the Magic Mouse power-switch-green wording is on the page (cable steps).
- 102660 (two-factor): readable.
- 104955 and 109016 (Passwords / iCloud Keychain): readable. The page does not say what appears after a site is tapped; "To view a password ... select a website or app" supports the reply's "Your password appears."
- guide/iphone/report-spam (Messages): the first fetch returned only the start of the page. A second fetch with offset 100000 returned the spam section. Readable.
- No page was unreadable.

## Notes
- No file under eval/ or data/v2/specs/ was opened. Only reviews/ny1b.r2.py, reviews/ny1b.r2.jsonl and this report were written.
- Round 1 files were not read, so this round is independent.
