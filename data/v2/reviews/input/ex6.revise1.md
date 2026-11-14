# Revision list: batch ex6, after review round 1 (37 examples)

Edit ONLY these examples in data/v2/specs/ex6.py, then rebuild.

## tr076-c
- reasons: Lead-in is pasted twice: 'Next time, try this:' followed by 'Your iPhone camera can read QR codes. It takes a few seconds.' right after 'your iPhone can read it with the camera.' Also tells the user 'The restaurant's menu will open' although it is a statement, fine; main issue is the duplicated intro.
- fix requested: Remove the pasted lead-in. Start the reply with 'That square is a QR code, and your iPhone can read it with the Camera app.' then go straight to the numbered steps. Do not repeat 'Your iPhone camera can read QR codes. It takes a few seconds.' Also change the Control Center line to 'If you don't see **Scan Code** in Control Center, touch and hold the background of Control Center, tap **Add a Control**, then tap **Scan Code**.' or drop the Control Center line.
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102680

## tr076-d
- reasons: Final reply says 'The restaurant's menu will open' and 'ones printed on the restaurant's own menu or table' but this user never mentioned a restaurant; carried over from tr076-a. Also 'Thanks.' then 'Your iPhone camera can read QR codes' is slightly repetitive.
- fix requested: Replace 'The restaurant's menu will open.' with 'The page or app that the code is for will open.' and replace the last line with 'Only open QR codes you trust, like ones printed by a business you know.' Keep the rest.
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102680

## tr077-c
- reasons: Two questions (two question marks): 'Is the QR code not scanning, or is it opening something you didn't expect? And is your phone an iPhone or an Android phone?'
- fix requested: Replace with exactly one question and no steps: 'It looks like your message got cut off. Is your phone an **iPhone** or an **Android** phone?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/camerafromgoogle/answer/12033278?hl=en

## tr077-d
- reasons: The user said Pixel. The cited page explicitly sends Pixel Camera users to a different Help Center, so the Pixel-specific steps are not from the cited source.
- fix requested: Add source https://support.google.com/pixelphone/answer/16561572?hl=en and rewrite the final reply for a Pixel: 1 Open the **Camera** app. 2 Point the lens at the code so the whole code is on the screen (no need to take a photo). 3 Wait a moment for a bubble or link to appear, then tap it. Then: 'If nothing appears, tap the **Settings** icon in Camera, tap **More settings**, and make sure **Camera scan suggestions** is on.' Optionally add: 'You can also swipe down from the top and tap **Scan QR code**.' Drop the 'Google's Camera app / other brands' paragraph and the photo/portrait/video mode lines.
- unsupported claims: 'Make sure it's in regular **photo** mode. QR scanning doesn't work in video or portrait mode. Some phones also have a **QR** option you can tap.' -> this is from the Camera from Google page, which says Pixel Camera users should use the separate Pixel help page; the Pixel page has no photo/QR mode step | 'When a banner appears on the screen, tap it' -> Pixel page says a bubble or link appears | 'These steps are for Google's Camera app... Other phone brands work in a similar way' -> user named a Pixel, so these steps are not the Pixel steps
- required actions missing from the reply: Launch Camera (critical) | If scanning is not working: tap the Settings icon, More settings, then make sure Camera scan suggestions is on | Wait for a bubble or link to appear (critical) | Alternative: swipe down for Quick Settings and tap Scan QR code
- low scores: {'steps': 1, 'constraints': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/camerafromgoogle/answer/12033278?hl=en

## tr078-a
- reasons: Emergency contacts part ends without the final Done; two small unsupported details (position of Summary, separate Edit step).
- fix requested: Change step 2 to 'Tap **Summary**.' and step 3 to 'Tap your **profile picture** in the upper corner.' Remove the standalone step 'Tap **Edit**' before Show When Locked (page order is: Medical ID, turn on Show When Locked, then tap Edit or Add beside a field such as Allergies and type, then Done). At the end of the emergency contacts paragraph add 'Then tap **Done**.' and change 'tap the **plus** button' to 'tap the **plus** button next to **Add Emergency Contact**, choose a contact, and enter how they're related to you.' Keep the privacy line.
- unsupported claims: 'Tap **Summary** at the bottom.' -> page says only 'select the Summary tab'; 'at the bottom' is not on the page | 'Tap **Edit**.' (separate step before Show When Locked) -> page does not list a separate Edit step before Show When Locked; Edit appears beside a field/Emergency Contacts
- required actions missing from the reply: Emergency contacts: Edit next to Emergency Contacts, plus button next to Add Emergency Contact, choose a contact, enter relationship, tap Done
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/105072

## tr078-d
- reasons: Same problems as tr078-a in the final reply.
- fix requested: Change step 2 to 'Tap **Summary**.' and step 3 to 'Tap your **profile picture** in the upper corner.' Remove the standalone step 'Tap **Edit**' before Show When Locked (page order is: Medical ID, turn on Show When Locked, then tap Edit or Add beside a field such as Allergies and type, then Done). At the end of the emergency contacts paragraph add 'Then tap **Done**.' and change 'tap the **plus** button' to 'tap the **plus** button next to **Add Emergency Contact**, choose a contact, and enter how they're related to you.' Keep the privacy line.
- unsupported claims: 'Tap **Summary** at the bottom.' -> page says only 'select the Summary tab'; 'at the bottom' is not on the page | 'Tap **Edit**.' (separate step before Show When Locked) -> page does not list a separate Edit step before Show When Locked; Edit appears beside a field/Emergency Contacts
- required actions missing from the reply: Emergency contacts: Edit next to Emergency Contacts, plus button next to Add Emergency Contact, choose a contact, enter relationship, tap Done
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/105072

## tr080-a
- reasons: One overstated claim, stronger than the page.
- fix requested: Change the last line to 'If you don't see **Notifications** for that app, the app may not be able to send notifications.' Leave everything else unchanged.
- unsupported claims: 'it means the app can't send notifications' -> page says only that the app 'may not be able to send notifications at all'
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/120681

## tr080-b
- reasons: Two questions in one reply ('Which app is sending them...? And is your phone an iPhone or an Android phone?'). The app name does not change the steps; only the phone type does.
- fix requested: Replace with exactly one question and no steps: 'I can help with that. Is your phone an **iPhone** or an **Android** phone?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/120681

## tr080-c
- reasons: Two questions ('popping up too often, or stopped showing up?' and 'which app is it?') and neither asks for the phone type, which is what changes the steps; the user message is too cut off to know the problem.
- fix requested: Replace with exactly one question and no steps: 'It looks like your message got cut off. Is your phone an **iPhone** or an **Android** phone?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/120681

## tr080-d
- reasons: Same overstated claim in the final reply. (Earlier assistant turn asks two questions; style only.)
- fix requested: Change the last line to 'If you don't see **Notifications** for that app, the app may not be able to send notifications.' Leave everything else unchanged.
- unsupported claims: 'it means the app can't send notifications' -> page says only that the app 'may not be able to send notifications at all'
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/120681

## tr081-a
- reasons: One unsupported position/label detail.
- fix requested: In Option 1 step 3 replace 'open the menu at the top and choose all apps' with 'open the dropdown and tap **All apps**'. Leave everything else unchanged.
- unsupported claims: 'open the menu at the top and choose all apps' -> page says 'open the dropdown and tap All apps' under 'Most recent'; 'menu at the top' is not on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9079661?hl=en

## tr081-b
- reasons: Two questions in one reply ('Which app is it, and is your phone an iPhone or an Android phone?'). The app name does not change the steps.
- fix requested: Replace with exactly one question and no steps: 'Yes, you can turn off an app's notifications. Is your phone an **iPhone** or an **Android** phone?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/9079661?hl=en

## tr081-c
- reasons: Two questions (alerts from an app vs emails or texts, and iPhone vs Android).
- fix requested: Replace with exactly one question and no steps: 'That sounds tiring. Is your phone an **iPhone** or an **Android** phone?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/9079661?hl=en

## tr081-d
- reasons: Same unsupported detail in the final reply.
- fix requested: In Option 1 step 3 replace 'open the menu at the top and choose all apps' with 'open the dropdown and tap **All apps**'. Leave everything else unchanged.
- unsupported claims: 'open the menu at the top and choose all apps' -> page says 'open the dropdown and tap All apps' under 'Most recent'; 'menu at the top' is not on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9079661?hl=en

## tr082-a
- reasons: Unsupported icon description.
- fix requested: Replace 'Click the **More** menu (three dots) at the top right of Chrome.' with 'At the top right of Chrome, click **More**.' In the last paragraph make it 'click **More**, then **Settings**, then **Appearance**, then next to **Page zoom** pick a size.' Leave everything else unchanged.
- unsupported claims: 'the **More** menu (three dots) at the top right' -> page says 'At the top right, click More' and does not describe the icon as three dots
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

## tr082-b
- reasons: Two questions (device type, then browser).
- fix requested: Replace with exactly one question and no steps: 'I can help you make them bigger. Are you on a **computer**, a **phone**, or a **tablet**?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

## tr082-c
- reasons: The question asked ('just this page or every website') does not change the steps (the reply can give both); the missing detail that does change them is whether this is Chrome on a computer or on a phone/tablet.
- fix requested: Replace with exactly one question and no steps: 'Sure. Are you using Chrome on a **computer**, a **phone**, or a **tablet**?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

## tr082-d
- reasons: Same unsupported icon description in the final reply.
- fix requested: Replace 'Click the **More** menu (three dots) at the top right of Chrome.' with 'At the top right of Chrome, click **More**.' In the last paragraph make it 'click **More**, then **Settings**, then **Appearance**, then next to **Page zoom** pick a size.' Leave everything else unchanged.
- unsupported claims: 'the **More** menu (three dots) at the top right' -> page says 'At the top right, click More' and does not describe the icon as three dots
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop

## tr083-a
- reasons: Contradicts the page on This PC; unsupported sorting claim.
- fix requested: Step 1: 'Open **File Explorer** from the taskbar, or hold the **Windows logo key** and press **E**.' Step 2: 'In the list on the left, click **Downloads** (under **Quick access**).' Delete 'You can also find it under This PC.' Replace step 3 with 'Your downloaded file should be in the list.' (no sorting claim). Optionally add: 'If you don't see **Downloads**, click **Home** on the left, click the up arrow, right-click **Downloads**, and choose **Pin to Quick access**.' Fix the closing line so it matches the user's file.
- unsupported claims: 'You can also find it under **This PC**.' -> contradicted: the page says that in Windows 11 22H2 and later the known folders no longer appear under This PC | 'If the folder is sorted by date, your newest download will be near the top.' -> page does not describe sorting | 'Click the folder icon on the taskbar' -> page says only 'select it on the taskbar'; the icon is not described
- required actions missing from the reply: If Downloads is missing: select Home, select the Up arrow, right-click Downloads, choose Pin to Quick access | Note: in Windows 11 22H2 and later, known folders no longer appear under This PC
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

## tr083-b
- reasons: Two questions ('computer or phone?' and 'Windows or a Mac?').
- fix requested: Replace with exactly one question and no steps: 'Let's find it. Is this on a **Windows computer**, a **Mac**, or a **phone**?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

## tr083-c
- reasons: Same source problems as tr083-a. Lead-in pasted twice ('It's most likely in your Downloads folder. Here's how to find it:' then 'Files you download usually go to your Downloads folder. Here's how to find it.'). Step 3 says 'your form' and the closing line says 'what the form is called' but the user is looking for an insurance card PDF.
- fix requested: Step 1: 'Open **File Explorer** from the taskbar, or hold the **Windows logo key** and press **E**.' Step 2: 'In the list on the left, click **Downloads** (under **Quick access**).' Delete 'You can also find it under This PC.' Replace step 3 with 'Your downloaded file should be in the list.' (no sorting claim). Optionally add: 'If you don't see **Downloads**, click **Home** on the left, click the up arrow, right-click **Downloads**, and choose **Pin to Quick access**.' Fix the closing line so it matches the user's file. Also delete the duplicated lead-in (keep only 'It's most likely in your **Downloads** folder. Here's how to find it.') and say 'your insurance card PDF' instead of 'your form'.
- unsupported claims: 'You can also find it under **This PC**.' -> contradicted: the page says that in Windows 11 22H2 and later the known folders no longer appear under This PC | 'If the folder is sorted by date, your newest download will be near the top.' -> page does not describe sorting | 'Click the folder icon on the taskbar' -> page says only 'select it on the taskbar'; the icon is not described
- required actions missing from the reply: If Downloads is missing: select Home, select the Up arrow, right-click Downloads, choose Pin to Quick access | Note: in Windows 11 22H2 and later, known folders no longer appear under This PC
- low scores: {'steps': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

## tr083-d
- reasons: Same source problems as tr083-a. Also 'Look for your form' but the user said only 'something I downloaded'.
- fix requested: Step 1: 'Open **File Explorer** from the taskbar, or hold the **Windows logo key** and press **E**.' Step 2: 'In the list on the left, click **Downloads** (under **Quick access**).' Delete 'You can also find it under This PC.' Replace step 3 with 'Your downloaded file should be in the list.' (no sorting claim). Optionally add: 'If you don't see **Downloads**, click **Home** on the left, click the up arrow, right-click **Downloads**, and choose **Pin to Quick access**.' Fix the closing line so it matches the user's file. Replace 'your form' with 'your file'.
- unsupported claims: 'You can also find it under **This PC**.' -> contradicted: the page says that in Windows 11 22H2 and later the known folders no longer appear under This PC | 'If the folder is sorted by date, your newest download will be near the top.' -> page does not describe sorting | 'Click the folder icon on the taskbar' -> page says only 'select it on the taskbar'; the icon is not described
- required actions missing from the reply: If Downloads is missing: select Home, select the Up arrow, right-click Downloads, choose Pin to Quick access | Note: in Windows 11 22H2 and later, known folders no longer appear under This PC
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

## tr084-a
- reasons: One unsupported option name.
- fix requested: Replace step 5 with 'You can also change the pointer's **color** so it stands out more.' (remove 'style'). Leave everything else unchanged.
- unsupported claims: 'You can also change the **style** or color' -> page says you can change the color and size of the pointer; 'style' is not named
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see

## tr084-d
- reasons: Same unsupported option name in the final reply.
- fix requested: Replace step 5 with 'You can also change the pointer's **color** so it stands out more.' (remove 'style'). Leave everything else unchanged.
- unsupported claims: 'You can also change the **style** or color' -> page says you can change the color and size of the pointer; 'style' is not named
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see

## tr085-a
- reasons: One unsupported detail and a dangling 'these codes'.
- fix requested: Replace 'After it's on, Google may ask you to confirm with your phone when you sign in on a new device.' with 'After it's on, when you sign in Google will ask for a second step as well as your password, such as tapping Yes on a prompt on your phone.' Replace 'Never share these codes with anyone, even if they say they're from Google.' with 'Never share a verification code with anyone. Google will not call you to ask for one.' Leave the work/school line.
- unsupported claims: 'Google may ask you to confirm with your phone when you sign in on a new device.' -> page says Google chooses the second step and mentions phone prompts, but nothing about 'a new device' | '**Never share these codes with anyone**' -> 'these codes' has no antecedent (no code has been mentioned); page says 'Don't share verification codes with anyone, because scammers may try to take over your account. Google won't call you to ask for a code.'
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop ; https://support.google.com/accounts/answer/7682439?hl=en

## tr085-d
- reasons: Same issues in the final reply. (Earlier turn asks two questions; style only.)
- fix requested: Replace 'After it's on, Google may ask you to confirm with your phone when you sign in on a new device.' with 'After it's on, when you sign in Google will ask for a second step as well as your password, such as tapping Yes on a prompt on your phone.' Replace 'Never share these codes with anyone, even if they say they're from Google.' with 'Never share a verification code with anyone. Google will not call you to ask for one.' Leave the work/school line.
- unsupported claims: 'Google may ask you to confirm with your phone when you sign in on a new device.' -> page says Google chooses the second step and mentions phone prompts, but nothing about 'a new device' | '**Never share these codes with anyone**' -> 'these codes' has no antecedent (no code has been mentioned); page says 'Don't share verification codes with anyone, because scammers may try to take over your account. Google won't call you to ask for a code.'
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop ; https://support.google.com/accounts/answer/7682439?hl=en

## tr086-a
- reasons: Three unsupported claims; the 'already clicked' advice is not what the page says.
- fix requested: Change the second sentence to 'These emails often look real, even with the bank's logo, but a link can carry malware.' Change step 2 to 'To check your account, contact your bank using a phone number or website you already know is real, not anything from the email.' Replace the last line with 'If you already clicked a link or opened an attachment, update your computer's security software, run a scan, and remove anything it finds. If you gave out personal information, go to **IdentityTheft.gov** for next steps.'
- unsupported claims: 'the link can lead to a fake website that steals your password' -> page says the link may contain malware; it does not describe a fake website that steals a password | 'call your bank using the number on the **back of your card**' -> page says use 'a phone number or website you know is real'; the card is not mentioned | 'If you already clicked and typed your password, call your bank right away and change your password.' -> page says nothing like this; for a clicked link it says update security software and run a scan, and if you gave information go to IdentityTheft.gov
- required actions missing from the reply: If you clicked a link/opened an attachment: update security software, run a scan; if you gave personal info, go to IdentityTheft.gov
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

## tr086-b
- reasons: Two questions in one ('Who does the email say it's from, and what is it asking you to do?').
- fix requested: Keep 'Good thinking to check first. Please don't click anything yet.' then ask exactly one question: '**Who does the email say it's from?**'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

## tr086-c
- reasons: Scam safety: the protective instruction comes after the question ('Who does the email say it's from? And please don't click any links...').
- fix requested: Reorder to put the protective line first: 'It looks like your message got cut off. Please don't click any links in it until we check. **Who does the email say it's from?**'
- low scores: {} | gates not passed: {'safety': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

## tr086-d
- reasons: Same unsupported claims in the final reply.
- fix requested: Change the second sentence to 'These emails often look real, even with the bank's logo, but a link can carry malware.' Change step 2 to 'To check your account, contact your bank using a phone number or website you already know is real, not anything from the email.' Replace the last line with 'If you already clicked a link or opened an attachment, update your computer's security software, run a scan, and remove anything it finds. If you gave out personal information, go to **IdentityTheft.gov** for next steps.'
- unsupported claims: 'the link can lead to a fake website that steals your password' -> page says the link may contain malware; it does not describe a fake website that steals a password | 'call your bank using the number on the **back of your card**' -> page says use 'a phone number or website you know is real'; the card is not mentioned | 'If you already clicked and typed your password, call your bank right away and change your password.' -> page says nothing like this; for a clicked link it says update security software and run a scan, and if you gave information go to IdentityTheft.gov
- required actions missing from the reply: If you clicked a link/opened an attachment: update security software, run a scan; if you gave personal info, go to IdentityTheft.gov
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

## tr087-a
- reasons: One unsupported step.
- fix requested: Delete the line 'Then delete the text.' Leave everything else unchanged.
- unsupported claims: 'Then delete the text.' -> the page does not tell you to delete the message
- required actions missing from the reply: Optional: use the phone's spam filter, the carrier's blocking tools or a call-blocking app
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

## tr087-b
- reasons: Two questions (report/block/both, and iPhone/Android).
- fix requested: Replace with exactly one question and no steps: 'There are a couple of things you can do about junk texts. Is your phone an **iPhone** or an **Android** phone?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

## tr087-c
- reasons: Lead-in repeated: 'Reporting them helps your phone company block more of these:' then 'Reporting spam texts helps your phone company block similar messages. Here's how.' Also the unsupported 'Then delete the text.'
- fix requested: Delete the line 'Then delete the text.' Leave everything else unchanged. Also delete the second lead-in sentence ('Reporting spam texts helps ... Here's how.') and keep only 'Good for you for not clicking. Reporting them helps your wireless provider block more of these. Here's how:'
- unsupported claims: 'Then delete the text.' -> the page does not tell you to delete the message
- required actions missing from the reply: Optional: use the phone's spam filter, the carrier's blocking tools or a call-blocking app
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

## tr087-d
- reasons: Unsupported 'Then delete the text.' in the final reply.
- fix requested: Delete the line 'Then delete the text.' Leave everything else unchanged.
- unsupported claims: 'Then delete the text.' -> the page does not tell you to delete the message
- required actions missing from the reply: Optional: use the phone's spam filter, the carrier's blocking tools or a call-blocking app
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

## tr088-b
- reasons: Two questions, and no protective advice before asking; a money request to an online friend is a scam-risk topic.
- fix requested: Reply with the protective line first and one question: 'I'm glad you asked first. Please don't send any money or gift cards yet. **Have you met this person in person?**'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams

## tr088-c
- reasons: Two questions ('What kind of help is he asking for? And have the two of you met in person?') with no protective line first.
- fix requested: Reply: 'Thank you for trusting me with this. Please don't send money or gift cards to someone you haven't met in person. **What kind of help is he asking for?**'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams

## tr088-d
- reasons: Same unsupported claim and conditional stop-contact step in the final reply. (Earlier turn asks two questions; style only.)
- fix requested: Replace that warning sign with 'After lots of friendly messages, they ask for money for emergencies, travel, or fees.' Change step 4 to 'Stop talking to him, then report it at **ReportFraud.ftc.gov** and to the website or app where you met.' (the page says stop communicating right away, not only if it is a scam). Leave the rest.
- unsupported claims: 'Strong feelings grow quickly through lots of messages.' -> page says trust is built through frequent chats and then they ask for money; nothing about feelings growing quickly
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams
