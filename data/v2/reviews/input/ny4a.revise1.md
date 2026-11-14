# Revision list: batch ny4a, after review round 1 (4 examples)

Edit ONLY these examples in data/v2/specs/ny4a.py, then rebuild.

## tr161-a
- reasons: Closing line repeats what step 3 already says, so the reply says the same thing twice; this is extra text a learner would copy.
- fix requested: Delete the last line 'If the name is different on your phone, look for **System updates** instead.' Step 3 already says 'On some phones it is called **System updates**.' Change nothing else.
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://www.samsung.com/us/support/answer/ANS10002027/

## tr161-c
- reasons: Reply never says Smart Switch must already be installed on the laptop. This user only uses the laptop for email, so step 2 'Open Smart Switch' would not work for them and they are not told what to do.
- fix requested: Add a first step before plugging in: 'Make sure the Smart Switch program is installed on your computer. If it is not, you can get it from Samsung's Smart Switch page: https://www.samsung.com/us/support/owners/app/smart-switch'. Then keep the existing steps 1-3 (renumbered) and the closing note. Keep it short.
- required actions missing from the reply: Have Smart Switch installed on the computer (page: 'a computer that has Smart Switch installed'; page links samsung.com/us/support/owners/app/smart-switch) (critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://www.samsung.com/us/support/answer/ANS10002027/

## tr164-a
- reasons: One cue is not on the cited page.
- fix requested: Delete the last line 'The icon looks highlighted while the light is on.' The page does not describe how the icon looks when on. Keep 'The light comes on.' in step 2 as the cue.
- unsupported claims: 'The icon looks highlighted while the light is on.' -> the page does not describe the icon's appearance when on
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://www.samsung.com/us/support/answer/ANS10003351/

## tr166-e
- reasons: Page's watch procedure has a Continue/allow permissions step that is missing, and the reply never says how to stop the ringing, which matters for someone who finds the phone by sound.
- fix requested: After 'Open **Samsung Find**' (say 'swipe to and tap **Samsung Find**'), add a step: 'If asked, tap **Continue** and allow the permissions.' After the Ring step add: 'To stop the ringing, swipe **Dismiss** on the phone, or tap **Stop** on the watch.' Keep the closing note about Bluetooth, Wi-Fi or LTE and the website fallback.
- required actions missing from the reply: Tap Continue and allow the permissions (critical) | Stop with Dismiss on phone or Stop on watch
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://www.samsung.com/us/support/answer/ANS00080182
