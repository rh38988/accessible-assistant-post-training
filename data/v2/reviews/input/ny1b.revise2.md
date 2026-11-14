# Revision list: batch ny1b, after review round 2 (5 examples)

Edit ONLY these examples in data/v2/specs/ny1b.py, then rebuild.

## tr128-e
- reasons: Source gate fails: the reply says the speaker's online instructions give the PIN. The Apple page (HT204091) does not say where the PIN is found; it only tells the user to consult the accessory's manual or online instructions for help.
- fix requested: Opening lines: replace 'You do not need the paper manual. The speaker's online instructions also give the code.' with 'Apple's support page does not say where the PIN or passcode is. If you need help, check the speaker's manual or its online instructions.' Step 1: replace 'Look up your speaker's online instructions, and find the PIN or passcode.' with 'Look for the PIN or passcode. If you need help, check the speaker's manual or its online instructions.' Last paragraph: replace 'check the online instructions again for the right one' with 'check the speaker's manual or its online instructions again'. Keep steps 2 and the Settings > Bluetooth > My Devices path unchanged. Source: https://support.apple.com/en-us/HT204091
- unsupported claims: 'The speaker's online instructions also give the code.' -> the Apple page only says 'You might need to enter your PIN or passcode' and, for help, 'consult the accessory's manual or online instructions again'. It does not say the code is printed in the manual or online instructions. | 'Look up your speaker's online instructions, and find the PIN or passcode.' -> same unsupported location of the code, repeated in step 1.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/HT204091

## tr130-r
- reasons: Step coverage: the reply does not give the page's alternative for an account where the option is not shown at all (account.apple.com, Upgrade Account Security). The rest is supported and correct. Minor: 'To check:' implies that the Sign-In & Security screen shows whether two-factor authentication is on, which the page does not say.
- fix requested: After 'If your account was created with two-factor authentication, Apple says this extra protection can't be removed.', add: 'If you still do not see the option at all, go to account.apple.com in a web browser, sign in, tap Upgrade Account Security, and follow the onscreen instructions.' Change 'To check:' to 'If you want to look again:'. Source: https://support.apple.com/en-us/102660
- required actions missing from the reply: If the option is not shown at all, use the alternative: sign in at account.apple.com, tap Upgrade Account Security, and follow the onscreen instructions (not critical; the only alternative the page gives)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102660

## tr133-a
- reasons: Actionable: the source says the Delete button is 'shown as an icon, with no text label', but the reply tells the user to tap the Delete button without saying it has no written word, so the user will look for a word that is not there. The rest is supported.
- fix requested: In step 3, replace 'Tap the **Delete** button.' with 'Tap the Delete button. It is an icon with no word on it.' Keep the other steps. Source: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios

## tr133-c
- reasons: Actionable: the source says the Delete button is 'shown as an icon, with no text label', but the reply says 'Tap the Delete button' with no cue, so the user will look for a word that is not there. Everything else is supported.
- fix requested: In report step 3, replace 'Tap the **Delete** button.' with 'Tap the Delete button. It is an icon with no word on it.' Keep the other steps. Source: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios

## tr133-d
- reasons: Actionable: same missing cue as tr133-a and tr133-c for the Delete button. Also, the opened-message path says 'tap Report Spam at the bottom' without the source's condition that this link appears on messages from unknown senders, and 'report first and block them afterwards' states an order the page does not give (it says only that reporting does not stop the sender).
- fix requested: In step 3, replace 'Tap the **Delete** button.' with 'Tap the Delete button. It is an icon with no word on it.' In the opened-message line, add 'This link appears on messages from unknown senders.' Replace 'so report first and block them afterwards.' with 'so you also need to block them.' Source: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios
