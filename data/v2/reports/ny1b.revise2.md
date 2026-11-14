# ny1b revise2 report

Ids fixed (5): tr128-e, tr130-r, tr133-a, tr133-c, tr133-d.
Ids not fixed: none.
Builder: `python3 data/v2/tools/build_v2.py ny1b` prints OK (median conversation 523 chars, longest 885).

Sources checked:
- https://support.apple.com/en-us/HT204091 (tr128-e): the page says only "You might need to enter your PIN or passcode" and to consult the accessory's manual or online instructions. It does not say where the code is printed, so the reply now says to check the speaker's manual or online instructions for help.
- https://support.apple.com/en-us/102660 (tr130-r): the page gives the account.apple.com / Upgrade Account Security alternative and the "can't be removed" sentence. It also says "Most accounts already use two-factor authentication," so that line is kept.
- https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios (tr133-a, c, d): the page describes the Delete button as appearing as an icon, says the Report Spam link appears at the bottom of messages from any unknown sender, and says reporting does not prevent the sender from sending messages. The page is long; the first fetch was truncated and the second part was read with an offset.

Changes:
- tr128-e: opening line, step 1 and last line reworded as the page supports. Step 2 and the Settings > Bluetooth > My Devices path are unchanged.
- tr130-r: "To check:" changed to "If you want to look again:". Added the account.apple.com / Upgrade Account Security alternative for when the option is not shown.
- tr133-a, c, d: step 3 now reads "Tap the Delete button. It appears as an icon, not a word." The bold label was removed because the page gives no text label.
- tr133-d: opened-message line notes the Report Spam link appears on messages from unknown senders. "so report first and block them afterwards" changed to "so you also need to block them."

Follow-ups touched: none. tr133-d is the follow-up of tr133-b, which was not changed.

Where the page or reviewer differed:
- The reviewer's requested text for tr128-e and tr130-r named Apple ("Apple's support page does not say..." and "Apple says..."). The generation spec forbids mentioning the source, so the wording now carries the same content without naming Apple.
- The reviewer's wording "an icon with no word on it" was replaced with the page's own description, "appears as an icon."
- tr130-r: the "Apple says" phrase was removed for the same reason above; the reviewer had marked the rest of that example as supported.
