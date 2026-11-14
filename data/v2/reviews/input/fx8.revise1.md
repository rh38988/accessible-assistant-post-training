# Revision list: batch fx8, after review round 1 (5 examples)

Edit ONLY these examples in data/v2/specs/fx8.py, then rebuild.

## tr104-e
- reasons: Method and the user's no-bar constraint are right and the Search bookmarks and Bookmark Manager lines are supported. Only the position 'at the top' is unsupported.
- fix requested: Step 2: change to 'Click the address bar.' Nothing else needs to change.
- unsupported claims: 'Click the address bar at the top.' -> the page never says where the address bar is
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

## tr105-r
- reasons: The final reply stops at 'Check it for the store's other lists' and never tells the user what to do next (click Unsubscribe next to the store). The cited page does not describe the Manage subscriptions screen; the linked Gmail page does.
- fix requested: Add a second source https://support.google.com/mail/answer/15621070?hl=en&co=GENIE.Platform%3DDesktop . Replace step 4 with: '4. Find the store in the list. To the right of its name, click **Unsubscribe**.' Add a last line: 'It can take a few days for the emails to stop.' Keep the explanation about other mailing lists.
- required actions missing from the reply: Click Unsubscribe to the right of the store's sender entry (critical) | Note: sender may take a few days to process
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop

## tr108-e
- reasons: The user has an iPhone 8 (Home button). The key gesture is not on the cited page. The reply is right, but needs the second source.
- fix requested: Add the second source https://support.apple.com/en-us/108330 (Home button models: swipe up from the bottom edge of any screen to open Control Center; tap the screen... close by tapping the top of the screen or pressing the Home button). No text change is needed, but optionally make 'Close Control Center' say 'Tap the top of the screen or press the Home button to close it.'
- unsupported claims: 'Swipe up from the bottom edge of the screen to open **Control Center**.' -> the cited page (118226) covers only models without a Home button and says nothing about the swipe up. It is correct per https://support.apple.com/en-us/108330 , which is not cited.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118226

## tr108-r
- reasons: Steps correct for iPhone 13; the 'not the middle' explanation needs the Control Center page as a second source.
- fix requested: Add the second source https://support.apple.com/en-us/108330 (it says swiping near the top-center may open Notification Center instead). No text change is needed.
- unsupported claims: 'Control Center opens from the corner, not the middle of the top edge.' -> the cited page says only 'swipe down from the top-right corner'. The warning about the top-center is on https://support.apple.com/en-us/108330 , not cited.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118226

## tr109-r
- reasons: Honest and supported, but 'contact the Disability Support team' leaves a low-confidence user with no way to do it. The cited page links the contact page.
- fix requested: Keep the text and add the contact page from the cited page: 'You can reach the Disability Support team here: https://support.google.com/accessibility/answer/7641084'. Optionally say 'Tell me what you see in Settings and I'll try to help.'
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/accessibility/android/answer/6006961?hl=en
