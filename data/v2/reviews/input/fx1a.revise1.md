# Revision list: batch fx1a, after review round 1 (17 examples)

Edit ONLY these examples in data/v2/specs/fx1a.py, then rebuild.

## tr001-c
- reasons: Gear-icon description is unsupported by the cited page.
- fix requested: Delete the sentence 'Its icon looks like a gear.' from step 1; keep 'Open the **Settings** app.'
- unsupported claims: 'Its icon looks like a gear.' -> the Samsung page never describes the Settings icon (text or image alt text).
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/

## tr001-d
- reasons: Gear-icon description is unsupported by the cited page.
- fix requested: Delete the sentence 'Its icon looks like a gear.' from step 1; keep 'Open the **Settings** app.'
- unsupported claims: 'Its icon looks like a gear.' -> the Samsung page never describes the Settings icon (text or image alt text).
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/

## tr001-e
- reasons: Gear-icon description is unsupported by the cited page. The Font style / download-fonts warning is supported.
- fix requested: Delete the sentence 'Its icon looks like a gear.' from step 1; keep 'Open the **Settings** app.'
- unsupported claims: 'Its icon looks like a gear.' -> the Samsung page never describes the Settings icon (text or image alt text).
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/

## tr001-r
- reasons: Final reply adds an invented search-the-list step. The page gives no troubleshooting, so only the model-differences note and Samsung Support contact are supported.
- fix requested: In the first assistant turn delete 'Its icon looks like a gear.' In the final reply delete numbered steps 1 and 2 (look through Display list). Keep: menus differ by model and software version; then give Samsung Support options as the page lists them: Live Chat, Email, and Find a Support Center (the page has no phone number, so say 'Call' only as a link on Samsung's Contact page or drop it). Ask the user to tell you what they see only if no invented steps are added.
- unsupported claims: 'Its icon looks like a gear.' -> the Samsung page never describes the Settings icon (text or image alt text). (first assistant turn) | 'Stay on the **Display** screen and look through the whole list for any choice about the font or the size of the writing. If you find one, tap it and make the font bigger there.' -> not on the page; the page has no troubleshooting steps and names no alternative item.
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/

## tr002-a
- reasons: Unsupported 'More' label.
- fix requested: Delete 'It may say **More**.' from the Menu-icon step. Optionally add: if there is no Menu icon, the phone has older software and the steps are Down arrow > Ring (page's older-version steps).
- unsupported claims: 'It may say **More**.' -> the Google page says only the 'Menu' icon for the volume bar; 'More' is not given for it.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9082609?hl=en

## tr002-d
- reasons: Unsupported 'More' label.
- fix requested: Delete 'It may say **More**.' from the Menu-icon step.
- unsupported claims: 'It may say **More**.' -> the Google page says only the 'Menu' icon for the volume bar; 'More' is not given for it. (final reply)
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9082609?hl=en

## tr002-e
- reasons: Unsupported 'More' label.
- fix requested: Delete 'It may say **More**.' from the Menu-icon step.
- unsupported claims: 'It may say **More**.' -> the Google page says only the 'Menu' icon for the volume bar; 'More' is not given for it.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9082609?hl=en

## tr002-r
- reasons: Earlier assistant turn contains the unsupported 'More' label. Final reply is correct and supported.
- fix requested: In the first assistant turn delete 'It may say **More**.' Leave the final reply unchanged.
- unsupported claims: 'It may say **More**.' -> the Google page says only the 'Menu' icon for the volume bar; 'More' is not given for it. (first assistant turn, repeated in the same turn's closing line context)
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9082609?hl=en

## tr003-c
- reasons: Unsupported sentence about what appears after tapping Gallery.
- fix requested: Delete 'Your photos will appear.' from step 3 (or replace with the page's wording: select a photo or take a picture).
- unsupported claims: 'Your photos will appear.' -> the Google page does not say what appears after tapping Gallery.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/messages/answer/6159880?hl=en

## tr003-d
- reasons: Unsupported sentence about what appears after tapping Gallery.
- fix requested: Delete 'Your photos will appear.' from step 3.
- unsupported claims: 'Your photos will appear.' -> the Google page does not say what appears after tapping Gallery.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/messages/answer/6159880?hl=en

## tr003-r
- reasons: Earlier turn has an unsupported sentence; final reply step 1 bundles two actions ('Open your conversation with Carol and tap Gallery').
- fix requested: First turn: delete 'Your photos will appear.' Final reply: split step 1 into 'Open your conversation with Carol.' and 'Tap Gallery.' and renumber.
- unsupported claims: 'Your photos will appear.' -> the Google page does not say what appears after tapping Gallery. (first assistant turn)
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/messages/answer/6159880?hl=en

## tr004-d
- reasons: A Home-button iPhone uses either the side button or the top button (page lists both: side+Home, top+Home). The user was asked only about the Home button, so the final reply guessed 'side button' (device-specific guess).
- fix requested: Change the first assistant turn to one question that settles which: 'Is the button you press to wake the phone on the top edge or on the right side?' (keeping or dropping the Home-button question is fine if one question mark remains). In the final reply, use the answer: right side -> side button + Home button; top edge -> top button + Home button. Or, keep the current question and have the final reply give both pairs with a plain way to tell which applies.
- low scores: {'ask_or_answer': 0} | gates not passed: {}
- sources: https://support.apple.com/102616

## tr005-a
- reasons: Unexplained jargon: 'cache and cookies'.
- fix requested: Explain in plain words on first use, e.g. 'Clear your browser's saved website data (called cache and cookies), then open Gmail again.' Do not add menu paths (the page gives none).
- unsupported claims: 'Clear your browser's cache and cookies' -> supported wording, but jargon is left unexplained for a low-confidence user.
- required actions missing from the reply: Optional: extensions off, private window
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.google.com/mail/answer/7074871?hl=en

## tr005-d
- reasons: The user's problem is not receiving church-group emails; she never says Gmail will not load. The cited page is only about Gmail not loading, so the final reply assumes a problem the user did not describe, and the scenario does not match the page.
- fix requested: Rewrite the user's first message so the problem is that the Gmail page will not open or load (not that mail stopped arriving), keeping the plain voice and the 'turned it off and on' detail. Keep the question for where she reads email and the address ending, or make it a single question. Final reply then stays as is.
- low scores: {'ask_or_answer': 1, 'realistic_user': 1} | gates not passed: {}
- sources: https://support.google.com/mail/answer/7074871?hl=en

## tr006-c
- reasons: Unsupported 'menu option' for turning wireless on; power-cycle step (page's first step) is missing; step 2 bundles running the test with a conditional check.
- fix requested: Change to: 'Look for a button on the printer that shows a blue wireless icon.' Add the power cycle as step 1 (turn off, unplug, wait 30 seconds, plug in, turn on). Split step 2: 'Run the printer's built-in wireless test (many printers have a menu option for it).' and a separate 'If the test passes but it still will not print, make sure your laptop is online.'
- unsupported claims: 'It may be a blue wireless icon or a menu option.' -> page says 'Many printers have a button that displays a blue wireless icon' for turning wireless on; 'menu option' appears on the page only for the wireless connectivity test.
- required actions missing from the reply: Power-cycle the printer: off, unplug, wait 30 seconds, plug in
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73

## tr006-d
- reasons: Earlier assistant turn asserts what the green light means (unsupported), and final reply has the 'menu option' error.
- fix requested: First turn: delete 'The green light is a good sign: it means the printer has power.' (e.g. say 'Let's get that boarding pass printed.'). Final reply step 5: Change to: 'Look for a button on the printer that shows a blue wireless icon.'
- unsupported claims: 'The green light is a good sign: it means the printer has power.' -> not on the page; a green light can mean other things. | 'It may be a blue wireless icon or a menu option.' -> page says 'Many printers have a button that displays a blue wireless icon' for turning wireless on; 'menu option' appears on the page only for the wireless connectivity test.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73

## tr006-r
- reasons: Earlier turn has the 'menu option' error. Final reply stops at 'Add manually' with no way forward for a user whose printer is not listed, and does not mention the Windows 11 troubleshooter (Get Help app) that the page says to try first.
- fix requested: First turn step 5: Change to: 'Look for a button on the printer that shows a blue wireless icon.' Final reply: after 'Add manually', add the page's next step in plain words (choose 'Add a local printer or network printer with manual settings', pick the USB port, choose maker and model, print a test page) or tell the user to say what appears so you can continue. Optionally start the final reply by offering the Get Help printer troubleshooter for Windows 11 (page: aka.ms/PrinterConnection).
- unsupported claims: 'It may be a blue wireless icon or a menu option.' -> page says 'Many printers have a button that displays a blue wireless icon' for turning wireless on; 'menu option' appears on the page only for the wireless connectivity test. (first assistant turn, step 5)
- required actions missing from the reply: If not listed, Add manually and follow the prompts
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73
