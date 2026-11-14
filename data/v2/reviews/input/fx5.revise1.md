# Revision list: batch fx5, after review round 1 (8 examples)

Edit ONLY these examples in data/v2/specs/fx5.py, then rebuild.

## tr062-r
- reasons: The explanation misdescribes the user's situation and Browse has no stated location/cue.
- fix requested: Replace 'That happens when a category is not listed the usual way. Try this instead:' with 'Your phone may show it a little differently. Try this instead:'. Keep the three steps, but change step 1 to 'On the **Free up space** screen, tap **Browse**.' only if you can keep it to what the page says; otherwise write 'Look for **Browse** and tap it.' Add one closing line: 'Menu names can differ a little between phones, and some steps need Android 14 or newer.'
- unsupported claims: 'That happens when a category is not listed the usual way.' -> the user said they DID find the category; the page only says 'If the category isn't listed, tap Browse', so the explanation does not match the user's report and the page never says where Browse appears
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/7431795?hl=en

## tr063-r
- reasons: User message contradicts itself (iPhone 11 vs round Home button); step 3 uses a label the page does not give.
- fix requested: In the user's first message, change 'iPhone 11 here, the one with the round button at the bottom.' to 'iPhone SE here, the one with the round button at the bottom.' (a Home button model) and keep the swipe-up reply. In the final reply replace step 3 'Add **Flashlight**.' with 'In the list of controls, tap **Flashlight**.'
- unsupported claims: '3. Add **Flashlight**.' -> the page says 'tap Flashlight in the list of available controls'; 'Add' is not a label on the page | User message 'iPhone 11 here, the one with the round button at the bottom' -> the iPhone 11 has no Home button (Face ID), so the stated model contradicts the swipe-up steps
- low scores: {'actionable': 1, 'realistic_user': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/105001

## tr068-e
- reasons: Page says to bring the hearing devices near the iPhone before pairing; the reply omits it (non-critical).
- fix requested: After step 2 ('Take both hearing aids **out of the charger**.') add the sentence 'Keep them close to your iPhone.' inside step 2, or as a new step before opening Settings. Do not add anything else.
- required actions missing from the reply: Check compatibility with the MFi list | Bring the hearing aids near the iPhone
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/108780

## tr071-e
- reasons: Overpromises an evening timetable and presents 'Schedule' as an on-screen label; the page gives no schedule options.
- fix requested: Replace the opening line with 'Yes, Battery Saver lets you choose a schedule, or have it turn off automatically.' Replace step 4 with 'Look for the option to set a schedule or to turn it off automatically, and choose what fits you.' (no bold label). Add the hedge 'The choices can look a little different on some phones.' Keep the last paragraph about dark theme and slower apps.
- unsupported claims: 'Yes, Battery Saver has a schedule.' / 'Choose a **Schedule** for when it should run.' -> the page says only 'Choose a schedule for battery saver mode or automatically turn it off'; it does not say you can set evening hours or a timetable, and 'Schedule' is not given as a label
- low scores: {'constraints': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/7664692?hl=en

## tr073-e
- reasons: Step 4 bundles two actions with an unsupported 'if you are asked'; step 5 gives no cue for where the button is.
- fix requested: Split step 4 into: '4. Turn on **Magnification shortcut**.' and '5. Tap **Magnification shortcut** and choose **Accessibility button**.' Then '6. Tap the **Accessibility** icon at the bottom of the screen. Its exact spot depends on how your phone is set up.' Then '7. Drag with two fingers ... pinch ...'. Delete 'if you are asked how to start it'.
- unsupported claims: 'pick **Accessibility button** if you are asked how to start it' -> the page says to tap Magnification shortcut to pick a trigger; it never says you are asked | '5. Tap the **Accessibility button**.' -> the page calls it the Accessibility icon at the bottom of the screen (position depends on navigation setup); no cue where it is
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/accessibility/android/answer/6006949?hl=en

## tr073-r
- reasons: After switching shortcuts the reply never says how to start magnification with the new one.
- fix requested: After step 3 add a short line: 'With **Accessibility button**, tap the Accessibility icon at the bottom of the screen. With **Hold volume keys**, hold both volume buttons together.' Keep the rest.
- required actions missing from the reply: How to start the new shortcut (tap the Accessibility icon, or hold both volume buttons)
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/accessibility/android/answer/6006949?hl=en

## tr074-r
- reasons: Signing in to the wife's iPad app is unsupported and could mix accounts; icloud.com/find is the page-supported route on someone else's device.
- fix requested: Rewrite the first assistant turn to: 'Use the web browser on her iPad.' 1. Go to **icloud.com/find**. 2. Sign in with your Apple Account. 3. Open **All Devices** and tap your iPhone. 4. Choose to **mark it as lost**. (Mention you can also play a sound.) In the final reply, give the same icloud.com/find route for Lost Mode (page gives no button labels, so describe 'mark it as lost' in words) and drop 'scroll to the **Lost** section'. Alternatively, ask first whether her iPad is in your Family Sharing group, then use Find My > Devices > your iPhone > More > scroll to Lost iPhone > Lost Mode > Activate only if yes. Keep the offline explanation.
- unsupported claims: 'Open the **Find My** app and sign in with your Apple Account.' (on the wife's iPad) -> the page covers only your own signed-in trusted device, Family Sharing members' devices, and icloud.com/find; it does not describe signing in to Find My on someone else's iPad | 'scroll to the **Lost** section' -> the page says 'Lost [Device]' (e.g. Lost iPhone)
- required actions missing from the reply: Use Find My / Lost Mode from a device that supports it (own trusted Apple device, Family Sharing, or icloud.com/find) (critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/101593

## tr075-r
- reasons: Accuracy figure understated and contradicts the page (roughly 20 meters).
- fix requested: Replace the first sentence with 'The location can be off by roughly 20 meters, and it is less reliable indoors.' Keep the three steps.
- unsupported claims: 'The location can be off by a few meters, especially indoors.' -> the page says GPS is accurate to roughly 20 meters and can be unreliable indoors or underground
- required actions missing from the reply: Location accuracy: GPS roughly 20 meters, unreliable indoors
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.google.com/accounts/answer/6160491?hl=en
