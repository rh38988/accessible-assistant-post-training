# Revision list: batch fx5, after review round 2 (3 examples)

Edit ONLY these examples in data/v2/specs/fx5.py, then rebuild.

## tr062-r
- reasons: The recovery step offers Browse for a missing Select files button. The source gives Browse only when the category is not listed, so the reply applies it under a condition the page does not give. The rest of the steps (select files, Move files to Trash) are supported.
- fix requested: In the final assistant reply, delete the step 'Look for **Browse** and tap it.' Do not say Browse replaces a missing Select files button. Replace it with: 'Some steps need Android 14 or newer, so check your version under Settings.' Keep the select-files and 'Move files to Trash' steps. If Browse is mentioned at all, use the page's wording only: 'If the category isn't listed, tap **Browse** instead.' Keep the closing line about menu names.
- unsupported claims: 'Look for **Browse** and tap it.' used as the fix when the category is listed but **Select files** is missing -> the page says to tap Browse 'If the category isn't listed'; the user says the category is listed, so the condition is not supported and the substitute path is not on the page.
- required actions missing from the reply: Tap Select files, or Browse only if the category isn't listed (critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/7431795?hl=en

## tr073-r
- reasons: The page says magnification stops when the shortcut is pressed again. The user's phone is slow with zoom on, and the reply moves to a new shortcut without saying how to stop the current triple-tap zoom. Otherwise the steps are supported by the page.
- fix requested: Add one new first step before 'Open Settings': 'To stop the zoom now, press your magnification shortcut again: quickly tap the screen 3 times.' Keep the rest of the reply unchanged.
- required actions missing from the reply: Stop the current zoom by pressing the magnification shortcut again (non-critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.google.com/accessibility/android/answer/6006949?hl=en

## tr074-r
- reasons: The reply names the account as 'Apple Account' for the icloud.com/find sign-in, which the source does not say. Otherwise the steps, the offline explanation, and the no-code safety point are supported. Safety gate passes: no code or password is requested, and the reply does not ask the user to pay or install anything.
- fix requested: Replace 'Sign in with your Apple Account.' with 'Sign in to icloud.com/find.' and 'Sign in with your Apple Account if you are asked.' with 'Sign in if you are asked.' Make the same change in the turn 1 step 2. Do not add the name 'Apple Account' or any other account name. Keep all other steps and the offline explanation unchanged.
- unsupported claims: 'Sign in with your Apple Account.' (turn 1, step 2) -> the page never names an Apple Account for the web sign-in; it says only 'When you sign in to icloud.com/find'. | 'Sign in with your Apple Account if you are asked.' (final reply, step 2) -> same claim; the page's only sign-in-related note is that a verification code is not needed, and 'select the Find Devices button' if one is asked for.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/101593
