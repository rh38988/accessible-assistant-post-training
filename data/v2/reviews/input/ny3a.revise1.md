# Revision list: batch ny3a, after review round 1 (8 examples)

Edit ONLY these examples in data/v2/specs/ny3a.py, then rebuild.

## tr148-e
- reasons: The one-minute wait and the battery-icon cue are replaced by 'Charge for a few minutes', so the user is not told what to look for.
- fix requested: Replace step 6 with two steps: 'Plug it in and wait one minute. A battery icon on the screen means the phone is off and charging.' then 'Press and hold the **Power** button for 5 to 7 seconds.' Keep the no-new-cable constraint.
- required actions missing from the reply: Plug in and wait one minute; battery icon means off and charging
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/pixelphone/answer/7167687

## tr149-e
- reasons: Step 3 turns Wi-Fi off and mobile data on, but the reply never turns Wi-Fi back on before step 5 asks the user to check the Wi-Fi symbol. The user is trying to get online at the sister's house through Wi-Fi, so they would end with Wi-Fi off.
- fix requested: In step 3 say: 'Turn Wi-Fi off and mobile data on, and see if things load. Then turn mobile data off and Wi-Fi on, and check again.' In step 5 begin with 'Make sure **Wi-Fi** is on, then look at the Wi-Fi symbol at the top of the screen.' Keep the rest.
- required actions missing from the reply: Switch Wi-Fi off/mobile data on, then mobile data off/Wi-Fi on, test each (critical)
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/2651367

## tr150-d
- reasons: Step 2 uses the jargon 'APN settings' with no explanation and no starting point or cue; a low-confidence user cannot act on it. The page itself gives no path, so the reply should say so.
- fix requested: Reword step 2 to: 'In your phone's **Settings** app, find the **APN** settings (the settings your phone uses to send picture messages) and choose to reset them to default. The exact menu names are a little different on each phone.' Keep the other steps.
- low scores: {'actionable': 1, 'plain': 1} | gates not passed: {}
- sources: https://support.google.com/messages/answer/9077245

## tr151-a
- reasons: Reply is correct but its key labels are not on the cited page.
- fix requested: Add a second source https://support.google.com/messages/answer/16287429 (Create RCS groups), which has the labels Start chat, Create group, Next. The cited page 9367099 does not contain them.
- unsupported claims: 'Tap **Start chat**, then tap **Create group**' and 'Tap **Next**' -> not on the cited page 9367099 (it only says 'Start a new conversation'); supported by 16287429
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/messages/answer/9367099

## tr151-c
- reasons: Labels not on the cited page.
- fix requested: Add a second source https://support.google.com/messages/answer/16287429 (Create RCS groups), which has the labels Start chat, Create group, Next. The cited page 9367099 does not contain them.
- unsupported claims: 'Tap **Start chat**, then tap **Create group**' and 'Tap **Next**' -> not on the cited page 9367099; supported by 16287429
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/messages/answer/9367099

## tr151-d
- reasons: Labels not on the cited page.
- fix requested: Add a second source https://support.google.com/messages/answer/16287429 (Create RCS groups), which has the labels Start chat, Create group, Next. The cited page 9367099 does not contain them.
- unsupported claims: 'Tap **Start chat**, then tap **Create group**' and 'Tap **Next**' -> not on the cited page 9367099; supported by 16287429
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/messages/answer/9367099

## tr151-e
- reasons: Labels and the top-right position are not on the cited page; step 5 bundles go back, start chat, create group, pick members and Next in one step.
- fix requested: Add a second source https://support.google.com/messages/answer/16287429 (Create RCS groups), which has the labels Start chat, Create group, Next. The cited page 9367099 does not contain them. Also add https://support.google.com/messages/answer/9077245 for the 'top right' profile picture position. Split step 5 into separate steps: 'Go back to the main screen.', 'Tap **Start chat**, then **Create group**.', 'Pick your choir members, then tap **Next**.'
- unsupported claims: 'At the top right, tap your **profile picture** or **initials**' -> 9367099 says only 'Tap your profile photo or icon' (top right is on 9077245) | 'tap **Start chat**, then **Create group** ... tap **Next**' -> not on 9367099; supported by 16287429
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/messages/answer/9367099

## tr151-r
- reasons: Top-right position and the earlier-turn labels are not on the cited page.
- fix requested: Add a second source https://support.google.com/messages/answer/16287429 (Create RCS groups), which has the labels Start chat, Create group, Next. The cited page 9367099 does not contain them. Also add https://support.google.com/messages/answer/9077245 for the 'top right' profile picture position.
- unsupported claims: 'at the top right, tap your **profile picture** or **initials**' -> not on cited 9367099 (it is on 9077245) | Earlier turn 'Tap **Start chat**, then tap **Create group**' and '**Next**' -> not on 9367099; supported by 16287429
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/messages/answer/9367099
