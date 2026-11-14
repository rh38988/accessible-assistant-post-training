# Revision list: batch ny1b, after review round 1 (14 examples)

Edit ONLY these examples in data/v2/specs/ny1b.py, then rebuild.

## tr128-e
- reasons: The user is already at the PIN prompt, but the reply restarts from Settings > Bluetooth > My Devices (steps 2-4), which are redundant and may make the user leave the prompt. Steps 2-4 are extra text.
- fix requested: Rewrite so the reply starts from the user's current screen: (1) Look up the speaker's PIN or passcode in its online instructions (the maker's website or search the speaker's model name with 'manual'); (2) go back to the pairing prompt on the iPhone and enter the PIN or passcode. Remove the Settings/Bluetooth/My Devices steps. Keep the line that the code is in the manual or online instructions (page: 'check the accessory's manual or online instructions'). If the prompt has closed: Settings, Bluetooth, tap the speaker's name under My Devices, enter the code.
- low scores: {'actionable': 1, 'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/HT204091

## tr128-r
- reasons: Charge requirement is not on the cited page. It is supported on a different official Apple page.
- fix requested: Add https://support.apple.com/en-us/111804 as a second source (it says: make sure the accessory is on and fully charged or plugged in; keep it near the iPhone; restart the accessory by turning it off and on; put it in discovery mode). Keep the reply as is otherwise. Optionally say 'Keep the headphones close to your iPhone.'
- unsupported claims: 'Make sure the headphones are turned on and charged.' -> 'charged' is not on the cited page HT204091 (page only says to check manual/online instructions for making it discoverable).
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/HT204091

## tr129-a
- reasons: Unsupported position claim.
- fix requested: Change step 2 to 'Click the **Apple menu**, then choose **System Settings**.' (remove 'at the top left of the screen').
- unsupported claims: 'Click the Apple menu at the top left of the screen' -> page gives no screen position for the Apple menu.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/guide/mac-help/blth1004/mac

## tr129-c
- reasons: Unsupported scroll claim for Sound.
- fix requested: Step 6: 'Back in the sidebar, click **Sound**.' Remove 'You may need to scroll down.' from step 6. Keep the rest.
- unsupported claims: 'Back in the sidebar, click **Sound**. You may need to scroll down.' -> the page only says scrolling may be needed for Bluetooth, not Sound.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/guide/mac-help/blth1004/mac

## tr129-d
- reasons: Magic Mouse note is paraphrased beyond the page and drops the power-switch check; 'pairs by itself' is unsupported.
- fix requested: Replace the last paragraph with: 'If your mouse is an Apple Magic Mouse, you can use a cable instead: plug it into your Mac's USB-C port (you may need an adapter), turn the mouse on and check that its power switch shows green. When a notification appears, you can unplug the cable and use the mouse wirelessly.' Remove 'It pairs by itself'.
- unsupported claims: 'It pairs by itself' -> page does not say this; it says to connect with the cable, turn the device on, check that the power switch is green, and unplug when you get a notification.
- required actions missing from the reply: Apple Magic Mouse alternative: connect with cable to USB-C port, turn on, check power switch is green, unplug when notified
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/guide/mac-help/blth1004/mac

## tr130-a
- reasons: Unsupported claim about the missing option and 'Most accounts'.
- fix requested: Replace the last line with 'Many accounts already have two-factor authentication turned on, so you may not need to do this.' (the wording the page supports).
- unsupported claims: 'If you do not see that option, your account may already use it. Most accounts do.' -> page says 'Many accounts already have two-factor authentication'; it says nothing about the option being hidden, and 'Most' is not supported.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102660

## tr130-d
- reasons: 'Most' is stronger than the page.
- fix requested: Change last line to 'Many accounts already have two-factor authentication turned on, so you may not need to do this.'
- unsupported claims: 'Most accounts already use two-factor authentication' -> page says 'Many accounts already have it'.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102660

## tr130-r
- reasons: The cited page gives no troubleshooting for the missing option; the reply states an unsupported cause and 'Most'.
- fix requested: Rewrite the final reply to hedge only what the page says: 'Many accounts already have two-factor authentication turned on, so you may not need to turn it on. To check, go to Settings, tap your name, tap Sign-In & Security. If your account was created with two-factor authentication, Apple says this extra protection can't be removed.' Do not say the option 'may not appear' or 'most accounts'.
- unsupported claims: 'That is likely because you do not need it. Most accounts already use two-factor authentication, so the option may not appear.' -> page does not say the option may not appear; 'Most' not supported. | 'If your account was created with two-factor authentication, it is already on' -> page says it cannot be turned off/removed; 'already on' is a mild inference.
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102660

## tr131-a
- reasons: The user said they have the newest iOS, but the reply adds an iOS 17 or earlier line that is not needed.
- fix requested: Delete the last paragraph ('If your iPhone is on iOS 17 or earlier ...'). Keep steps 1-4.
- low scores: {'constraints': 1, 'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/104955

## tr131-e
- reasons: Wrong labels for the sync steps and an unsupported approval claim. The cited page HT/104955 only says to make sure iCloud Keychain is on, with no path.
- fix requested: Add https://support.apple.com/en-us/109016 as second source. Steps: 1. Open Settings. 2. Tap your name. 3. Tap iCloud. 4. Under 'Saved to iCloud', tap Passwords (on iOS 17 or earlier, tap Passwords and Keychain). 5. Turn on 'Sync this iPhone' (you may need your passcode or Apple Account password). Add: do the same on the iPad. Remove the approval sentence. The 109016 page says two-factor authentication must be on for the Apple Account.
- unsupported claims: 'Tap **Passwords and Keychain**.' -> on current iOS the label is 'Passwords' under 'Saved to iCloud'; 'Passwords and Keychain' is iOS 17 or earlier (https://support.apple.com/en-us/109016). | 'Turn on **iCloud Keychain**.' -> the switch is 'Sync this iPhone' per 109016, not 'iCloud Keychain'. | 'you may need to approve it first, using iCloud Keychain or the passcode of your old device' -> not on either page for iPhone.
- required actions missing from the reply: Under Saved to iCloud choose Passwords (iOS 17 or earlier: Passwords and Keychain) | Turn on Sync this iPhone
- low scores: {'steps': 0, 'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/104955

## tr131-r
- reasons: Sync path and labels are wrong for iOS 18.
- fix requested: Add https://support.apple.com/en-us/109016 as second source. Change step 3 to: 'If you use more than one Apple device, open **Settings**, tap your name, tap **iCloud**, and under **Saved to iCloud** tap **Passwords**. Make sure **Sync this iPhone** is on.' Keep the Deleted check and the Shared Group iOS 17 line.
- unsupported claims: 'open **Settings**, tap your name, tap **iCloud**, tap **Passwords and Keychain**, and make sure **iCloud Keychain** is on' -> labels not on the cited page; on current iOS (user said iOS 18) the path is iCloud > Passwords > 'Sync this iPhone' per https://support.apple.com/en-us/109016.
- required actions missing from the reply: Make sure iCloud Keychain/passwords sync is on
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/104955

## tr133-a
- reasons: Unsupported icon description.
- fix requested: Change step 3 to 'Tap the **Delete** button.' Remove 'the trash can icon'.
- unsupported claims: 'the **Delete** button, the trash can icon' -> page only says 'the Delete button'; no trash can icon is described.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios

## tr133-c
- reasons: Block-first order conflicts with the user's 'have not opened' constraint; trash can icon unsupported.
- fix requested: Put the report steps first (Messages list, swipe left on the message, tap the Delete button, tap Delete and Report Spam), then 'Now block them' with the Block Contact steps. Remove 'the trash can icon'. Keep the line that reporting alone will not stop the sender.
- unsupported claims: 'the **Delete** button, the trash can icon' -> not on page. | Order: block first by 'Open the conversation with the sender', then 'swipe left on the message' -> the user said they have not opened the latest message; opening the conversation opens it, and the page uses a different path (Report Spam link) for opened messages.
- low scores: {'constraints': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios

## tr133-d
- reasons: Whether the text was opened changes the report steps and the reply does not address it; trash can icon unsupported; block-first order.
- fix requested: Report first, then block. Give the unopened path (swipe left, tap the Delete button, tap Delete and Report Spam) and one line for an opened message: 'If you already opened it, open the message, tap Report Spam at the bottom, then tap Delete and Report Spam.' Then the Block Contact steps. Remove 'the trash can icon'. Change the lead-in to say reporting does not stop the sender, so block them afterwards.
- unsupported claims: 'the **Delete** button, the trash can icon' -> not on page. | Reply assumes the message is unopened (swipe-left path); the page has a different path for opened messages (open it, tap Report Spam link, tap Delete and Report Spam), and blocking first opens the conversation.
- low scores: {'steps': 1, 'ask_or_answer': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios
