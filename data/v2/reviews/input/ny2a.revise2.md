# Revision list: batch ny2a, after review round 2 (9 examples)

Edit ONLY these examples in data/v2/specs/ny2a.py, then rebuild.

## tr134-d
- reasons: S1 = 1: the page's security step is missing (two-step verification or special password). The reply ends without any step to contact the provider if sign-in still fails.
- fix requested: After step 3 (or as a new step after step 3), add: 'Ask your provider whether two-step verification or another security feature is turned on. If it is, you may need a special password from them to use email on your iPhone.' At the end of the reply add: 'If it still does not work, contact your email provider or system administrator.' Keep all other steps unchanged.
- required actions missing from the reply: Ask provider about two-step verification or special password (non-critical) | Contact provider or administrator if a username or password error remains (non-critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102578

## tr134-e
- reasons: S5 = 1: the closing sentence says 'Deleting the account is the last step on the list', but the list has no deletion step (its last item is the provider account check). S1 = 1: no step to contact the provider if sign-in still fails.
- fix requested: Replace the closing sentence 'Deleting the account is the last step on the list, and it can remove emails already downloaded to the phone, so you can leave it alone for now.' with: 'Removing the account is not on this list. It can delete emails already downloaded to the phone, so do not remove it unless you have first confirmed on your provider's website that all your email is saved somewhere else.' Add to the end of the numbered list (as step 7): 'If none of these work, contact your email provider.'
- required actions missing from the reply: Contact provider or administrator if error remains (non-critical)
- low scores: {'steps': 1, 'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102578

## tr135-c
- reasons: One unsupported causal claim about the photo settings and carrier limits. S1 = 1: the page's restart step is not in the reply.
- fix requested: Delete the sentence 'Some carriers limit the size of attachments on regular text messages, and these settings help with that.' Replace it with: 'Some carriers limit the size of picture messages. Turning on Send Photo Previews or Low Quality Image Mode makes pictures you send use lower quality.' Add a step after step 4 (or before the carrier line): 'Restart your iPhone.' Keep all other text.
- unsupported claims: 'and these settings help with that' -> the page lists Send Photo Previews and Low Quality Image Mode under 'Lower-quality sending', separately from 'Carrier limits'; it does not say these settings address carrier size limits
- required actions missing from the reply: Restart the iPhone (non-critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118433

## tr135-e
- reasons: S4 = 1: 'Send as Text Message is another option' gives no starting point. The page's path is to tap the red exclamation point again, then tap Send as Text Message.
- fix requested: Replace 'If it still will not send, **Send as Text Message** is another option, but messaging rates may apply.' with: 'If it still will not send, tap the red exclamation point again, then tap **Send as Text Message**. Messaging rates may apply.' Keep the rest of the reply unchanged, including the sentence about contacting Apple Support.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/118433

## tr136-a
- reasons: S1 = 1: the carrier settings update check (Settings > General > About) from the Apple page is not in the reply.
- fix requested: After step 7 (Download and Install), add two steps: 'Connect to Wi-Fi. Open **Settings**, tap **General**, then tap **About**.' and 'If an update is available, you will see an option to update your carrier settings. Tap it.' Keep all other steps unchanged.
- required actions missing from the reply: Carrier settings update: Wi-Fi, Settings > General > About, update carrier settings if shown (non-critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/120000 ; https://support.apple.com/en-us/118575

## tr136-d
- reasons: S1 = 1: the carrier settings update check (Settings > General > About) is not in the reply.
- fix requested: After step 5 (Software Update), add two steps: 'Connect to Wi-Fi. Open **Settings**, tap **General**, then tap **About**.' and 'If an update is available, you will see an option to update your carrier settings. Tap it.' Keep all other steps unchanged.
- required actions missing from the reply: Carrier settings update: Wi-Fi, Settings > General > About, update carrier settings if shown (non-critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/120000 ; https://support.apple.com/en-us/118575

## tr136-e
- reasons: G1 fail: one unsupported claim about what Airplane Mode does to the download. Otherwise the steps match the page and respect the user's no-restart limit.
- fix requested: Delete the sentence 'This may pause your download, so you may prefer to do it after the download finishes.' Keep the rest of step 3 as written. Make no other change.
- unsupported claims: 'This may pause your download, so you may prefer to do it after the download finishes.' -> the page does not say that Airplane Mode pauses a download; this is an added claim
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/120000 ; https://support.apple.com/en-us/118575

## tr138-e
- reasons: S3 = 1: the user said not to turn the phone off. The reply still tells them it 'may be safer to turn it off', which pushes against that limit without a clear way to keep the phone on. Safety is not at risk, so the fix is to state the page's steps and the trade-off plainly.
- fix requested: Replace the reply's first two sentences ('The usual steps ... cool it. The closest option is this:') with: 'Apple's steps for this warning are to turn the iPhone off, move it to a cooler place away from direct sunlight, and let it cool down. Turning it off is the step that helps most.' Keep step 1 ('Move your iPhone to a cooler place, away from direct sunlight.') as the only step for keeping it on, and state it as: 'If you keep it on, move it to a cooler place away from direct sunlight.' Replace 'it may be safer to turn it off and let it cool, or ask the hospital for another number to call' with 'If the call is important, ask the hospital for another number to call.' Keep 'Apple says to let the iPhone cool down before using it again'.
- low scores: {'constraints': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/118431

## tr139-r
- reasons: G1 fail: the passcode-entry instruction is not on the page. S4 = 1: the manual path ends at 'Then tap Time Zone, or tap the date' without saying what to do next (the page says to enter a city in the time zone you need). The reply also calls the switch 'Set Automatically' in the manual step but 'Set Time Automatically' earlier in the thread, with no note that they are the same setting.
- fix requested: In item 1, delete 'or enter the passcode if you know it'. Keep 'Ask the person who set it up.' In item 3, change 'Then tap **Time Zone**, or tap the date.' to: 'Then tap **Time Zone** and enter a city in the time zone you need, or tap the date to change the date and time.' Add after 'if **Set Automatically** is not locked, turn it off.': '(This is the same setting as **Set Time Automatically** shown earlier.)'
- unsupported claims: 'or enter the passcode if you know it' -> the page does not say that entering a Screen Time passcode unlocks the Date & Time setting
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/101619
