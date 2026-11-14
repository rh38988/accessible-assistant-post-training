# Revision list: batch ny3a, after review round 2 (5 examples)

Edit ONLY these examples in data/v2/specs/ny3a.py, then rebuild.

## tr148-e
- reasons: Critical 10-minute charge is missing from step 6, so the one-minute wait misstates the check. Three non-critical items missing (charging-accessory notification, 35-second reboot fallback, adapter rating). Constraint respected: no advice to buy a new charger.
- fix requested: Replace step 6 with: 'Plug the phone in and let it charge for 10 minutes. Then wait one minute. If you see a battery icon on the screen, the phone is charging.' Replace 'means the phone is off and charging' with 'means the phone is charging'. Add a new step after step 6 (or after step 7): 'If there is still no battery icon, hold the Power button for about 35 seconds to reboot. Wait about 2 minutes, then check again.' Optionally add to step 2: 'If you see a Check charging accessory message, the cable or charger may be damaged.' Source: https://support.google.com/pixelphone/answer/7167687 (steps 4, 6, 8, 10).
- unsupported claims: 'Plug it in and wait one minute.' -> the page says to charge for 10 minutes and then wait one minute; the reply drops the 10-minute charge, so the test result it describes is not what the page sets up. | 'A battery icon on the screen means the phone is off and charging.' -> the page says a battery icon means the phone is charging and that you can then restart it; 'the phone is off' is an inference, not a page statement.
- required actions missing from the reply: Plug in and charge for 10 minutes, then wait one minute and look for the battery icon (critical) | Look for a 'Check charging accessory' notification (non-critical) | If there is still no battery icon, hold the Power button for about 35 seconds to reboot, wait about 2 minutes (non-critical) | Confirm the adapter is rated 30 W or higher, or 15 W or higher for other USB PD adapters (non-critical)
- low scores: {'steps': 0} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/pixelphone/answer/7167687

## tr149-e
- reasons: Step 3 bundles two separate test rounds (four toggles) into one step. The mobile data indicator check and the move-to-better-coverage fallback from the page are missing. Router restart is correctly left out because the user said they cannot touch the router. Sources and safety are fine: the page supports every menu name and the router-owner advice.
- fix requested: Split step 3 into two steps: (a) 'Turn Wi-Fi off and mobile data on. See if things load.' (b) 'Then turn mobile data off and Wi-Fi on, and check again.' Add to step 3 or as a new step: 'Look for a data indicator (2G, 3G, 4G, or H) beside the signal bars. If none shows while Wi-Fi is on, turn Wi-Fi off and check again. If there is still no indicator, move to a spot with better coverage.' In step 5, change 'If no bars are filled' to 'If the Wi-Fi symbol is missing, or no bars are filled, you may be out of range.' Source: https://support.google.com/android/answer/2651367 (steps 2, 3, 5).
- required actions missing from the reply: Check the mobile data indicator (2G, 3G, 4G, or H) beside the signal bars; if none shows while Wi-Fi is active, turn Wi-Fi off and check again (non-critical) | If no data indicator appears, move to a spot with better coverage (non-critical)
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/2651367

## tr151-a
- reasons: The last line uses 'RCS tag' and 'MMS group chat' without saying what they mean, and the user is low-confidence. Start chat and Create group are not on 9367099 but are on 16287429, so both sources must stay cited.
- fix requested: Replace 'Contacts without the RCS tag will get a regular group text (an MMS group chat), which still works.' with: 'The RCS tag shows for a contact who has RCS chats turned on. A contact without the tag gets a regular group text, called an MMS group chat, which still works.' Sources: https://support.google.com/messages/answer/9367099 (RCS tag appears when RCS is on; a contact without the tag creates an MMS chat) and https://support.google.com/messages/answer/16287429 (Start chat, then Create group).
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.google.com/messages/answer/9367099 ; https://support.google.com/messages/answer/16287429

## tr151-c
- reasons: 'RCS chats', 'RCS tag', and 'MMS group chat' appear in the closing note without explanation, which a low-confidence user cannot act on. The iPhone answer is supported by 9367099 (iPhone contacts can show the RCS tag when RCS is on; contacts without the tag get an MMS group chat).
- fix requested: Replace the closing note with: 'The RCS tag shows for a contact who has RCS chats turned on, and iPhone contacts can have it too. A contact without the tag gets a regular group text, called an MMS group chat. That still reaches everyone in the group.' Sources: https://support.google.com/messages/answer/9367099 and https://support.google.com/messages/answer/16287429 (Start chat, then Create group).
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.google.com/messages/answer/9367099 ; https://support.google.com/messages/answer/16287429

## tr151-e
- reasons: Step 4 says 'Choose mass text as your default' but the page labels the option 'Send an SMS reply to all recipients and get individual replies (mass text)', so the user cannot match the words to the screen. The steps, the top-right profile icon, and the sources are otherwise correct, and the constraint (no replies to the whole choir) is met.
- fix requested: Replace step 4 with: 'Tap Send an SMS reply to all recipients and get individual replies (mass text) to make it your default.' Optionally add to the reply: 'This default applies to your group chats in general.' Sources: https://support.google.com/messages/answer/9077245 (exact option label and the individual-replies effect) and https://support.google.com/messages/answer/16287429 (mass text can be set as the default).
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.google.com/messages/answer/9367099 ; https://support.google.com/messages/answer/16287429 ; https://support.google.com/messages/answer/9077245
