# Revision list: batch ex7, after review round 1 (31 examples)

Edit ONLY these examples in data/v2/specs/ex7.py, then rebuild.

## tr089-a
- reasons: One unsupported claim in an otherwise correct, protective-first reply.
- fix requested: Delete the sentence "Your benefits are not being cut off." The FTC page does not say it. Keep only what the page says: the real Social Security Administration will not threaten you, will not suspend your Social Security number, and will not ask you to pay with gift cards.
- unsupported claims: "Your benefits are not being cut off." -> not on the FTC page.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam

## tr089-b
- reasons: Reply asks before giving any protective action (G2: protective action must come first for scams), and it asks two things (which agency, and how to pay). Compare tr089-c, which leads with 'don't give money or personal information'.
- fix requested: Start with the protective line: "Please don't pay or share any personal information yet, and don't call back any number they gave you." Then ask ONE question only, for example "Which agency did the caller say they were from?" (drop the payment question).
- low scores: {'ask_or_answer': 1} | gates not passed: {'safety': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam

## tr089-d
- reasons: Safety: the earlier assistant turn asks questions before any protective advice. Final reply says 'That's a scam.' and then 'This is a scam.' again (pasted lead-in), and has the same unsupported benefits sentence.
- fix requested: Delete the sentence "Your benefits are not being cut off." The FTC page does not say it. Keep only what the page says: the real Social Security Administration will not threaten you, will not suspend your Social Security number, and will not ask you to pay with gift cards. Change the opening of the final reply to one short line ("Thank you.") so "scam" is not said twice. Also rewrite the first assistant turn to match the fixed tr089-b (protective line first, then one question).
- unsupported claims: "Your benefits are not being cut off." -> not on the FTC page.
- low scores: {'plain': 1} | gates not passed: {'source': 'fail', 'safety': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam

## tr090-a
- reasons: Several tips are worded differently from, or go beyond, the FTC page.
- fix requested: Rewrite the tips to match the FTC page: (1) keep "at least 12 characters" and the random-words passphrase, but say a passphrase "may be easier to remember" with no comparison to symbols; (2) replace the "different password for each account" item with "If you used the same or a similar password on other sites, change it there too"; (3) replace "many web browsers have one built in" with "A password manager, or your web browser, can create strong passwords and save them for you"; (4) say "two-factor authentication" instead of "two-step verification" and add what it does: a hacker who steals your password still cannot log in without another step. Keep the song lyrics/quotes tip (add movie quotes) and the email tip.
- unsupported claims: "Use a different password for each account, so if one is stolen, the others stay safe." -> page has no standalone rule; it only says "If you reused the same password, or a similar one, on other services, change it there, too." | "many web browsers have one built in" -> page says a web browser or mobile browser can create and save passwords; it does not say browsers have a built-in password manager. | "Turn on two-step verification" -> page says "two-factor authentication" (and multi-factor); a different label. | "easier to remember than a jumble of symbols" -> page only says "You may find it easier to use a passphrase"; no comparison with symbols.
- required actions missing from the reply: If you reused the same or a similar password on other services, change it there too
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts

## tr090-c
- reasons: Same unsupported tips as tr090-a.
- fix requested: Rewrite the tips to match the FTC page: (1) keep "at least 12 characters" and the random-words passphrase, but say a passphrase "may be easier to remember" with no comparison to symbols; (2) replace the "different password for each account" item with "If you used the same or a similar password on other sites, change it there too"; (3) replace "many web browsers have one built in" with "A password manager, or your web browser, can create strong passwords and save them for you"; (4) say "two-factor authentication" instead of "two-step verification" and add what it does: a hacker who steals your password still cannot log in without another step. Keep the song lyrics/quotes tip (add movie quotes) and the email tip. Also make the opening support the page: the page only implies that reusing a password is risky ("If you reused the same password, or a similar one, on other services, change it there, too"), so say the reused password should be changed on every site.
- unsupported claims: "Use a different password for each account, so if one is stolen, the others stay safe." -> page has no standalone rule; it only says "If you reused the same password, or a similar one, on other services, change it there, too." | "many web browsers have one built in" -> page says a web browser or mobile browser can create and save passwords; it does not say browsers have a built-in password manager. | "Turn on two-step verification" -> page says "two-factor authentication" (and multi-factor); a different label. | "easier to remember than a jumble of symbols" -> page only says "You may find it easier to use a passphrase"; no comparison with symbols.
- required actions missing from the reply: If you reused the same or a similar password on other services, change it there too
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts

## tr090-d
- reasons: Same unsupported tips as tr090-a.
- fix requested: Rewrite the tips to match the FTC page: (1) keep "at least 12 characters" and the random-words passphrase, but say a passphrase "may be easier to remember" with no comparison to symbols; (2) replace the "different password for each account" item with "If you used the same or a similar password on other sites, change it there too"; (3) replace "many web browsers have one built in" with "A password manager, or your web browser, can create strong passwords and save them for you"; (4) say "two-factor authentication" instead of "two-step verification" and add what it does: a hacker who steals your password still cannot log in without another step. Keep the song lyrics/quotes tip (add movie quotes) and the email tip.
- unsupported claims: "Use a different password for each account, so if one is stolen, the others stay safe." -> page has no standalone rule; it only says "If you reused the same password, or a similar one, on other services, change it there, too." | "many web browsers have one built in" -> page says a web browser or mobile browser can create and save passwords; it does not say browsers have a built-in password manager. | "Turn on two-step verification" -> page says "two-factor authentication" (and multi-factor); a different label. | "easier to remember than a jumble of symbols" -> page only says "You may find it easier to use a passphrase"; no comparison with symbols.
- required actions missing from the reply: If you reused the same or a similar password on other services, change it there too
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts

## tr091-a
- reasons: Last paragraph attributes the step list to Preview and adds an unsupported turn-by-turn claim.
- fix requested: Replace the last paragraph with only page-supported text: "To see the list of steps, swipe up on the route panel. To see a turn-by-turn preview, tap Preview." Delete the sentence about turn-by-turn directions "as you go". Keep steps 1 to 6 unchanged.
- unsupported claims: "If you're starting from where you are now, Maps can give turn-by-turn directions as you go." -> not on the page. The page says your location is the default start, and Preview shows a turn-by-turn preview. | "To see the list of turns before you leave, tap Preview." -> page: the directions list comes from swiping up on the route info panel; Preview is the turn-by-turn preview.
- required actions missing from the reply: Optional: swipe up on the route panel for the list of steps, or tap Preview for a turn-by-turn preview
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

## tr091-b
- reasons: Two questions (which maps app, and iPhone or Android). Missing-information replies must be one question.
- fix requested: Ask only: "Is your phone an **iPhone** or an **Android** phone?" (the Google Maps page has separate steps per device).
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

## tr091-c
- reasons: Two question marks, and the questions asked (destination, travel mode) do not change the steps. The detail that changes the steps is the phone type.
- fix requested: Reply with one short question only, e.g. "It looks like your message got cut off. Are you using an **iPhone** or an **Android** phone?" Do not ask for the destination or travel mode here.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

## tr091-d
- reasons: Same unsupported last paragraph as tr091-a. (Earlier turn asks two questions; style only, will be fixed with tr091-b.)
- fix requested: Replace the last paragraph with only page-supported text: "To see the list of steps, swipe up on the route panel. To see a turn-by-turn preview, tap Preview." Delete the sentence about turn-by-turn directions "as you go". Keep steps 1 to 6 unchanged. Also make the first assistant turn match the fixed tr091-b.
- unsupported claims: "If you're starting from where you are now, Maps can give turn-by-turn directions as you go." -> not on the page. The page says your location is the default start, and Preview shows a turn-by-turn preview. | "To see the list of turns before you leave, tap Preview." -> page: the directions list comes from swiping up on the route info panel; Preview is the turn-by-turn preview.
- required actions missing from the reply: Optional: swipe up on the route panel for the list of steps, or tap Preview for a turn-by-turn preview
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

## tr093-a
- reasons: Unsupported time advice and wrong button label.
- fix requested: Delete "The first time, give yourself 5 to 10 minutes before the meeting starts." In step 2 say a small box (pop-up) asks whether to open Zoom Meetings. In step 3 say: click **Open**; depending on your browser the button may read **Allow** or **Open zoom.us**. Keep the passcode sentence and the "tell me what you see" line.
- unsupported claims: "give yourself 5 to 10 minutes before the meeting starts" -> the page gives no early-join time. | "it may say Open Zoom Meetings, Allow, or Open zoom.us" -> page: the button is "Open" and may read "Allow" or "Open zoom.us" depending on browser and device; "open Zoom Meetings" is the pop-up question, not a button label. | "Your web browser will open a page asking if you want to open Zoom Meetings" -> page: the browser goes to a launch page where a pop-up asks whether to open Zoom Meetings.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180

## tr093-b
- reasons: Two questions (link, and which device). Must be one question.
- fix requested: Ask only one question, e.g. "Happy to help. Did someone send you a **link** to the meeting, in an email or a text?" and adjust tr093-d so the user answers that.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180

## tr093-c
- reasons: Same unsupported claims as tr093-a. The lead-in is fine.
- fix requested: Delete "The first time, give yourself 5 to 10 minutes before the meeting starts." In step 2 say a small box (pop-up) asks whether to open Zoom Meetings. In step 3 say: click **Open**; depending on your browser the button may read **Allow** or **Open zoom.us**. Keep the passcode sentence and the "tell me what you see" line.
- unsupported claims: "give yourself 5 to 10 minutes before the meeting starts" -> the page gives no early-join time. | "it may say Open Zoom Meetings, Allow, or Open zoom.us" -> page: the button is "Open" and may read "Allow" or "Open zoom.us" depending on browser and device; "open Zoom Meetings" is the pop-up question, not a button label. | "Your web browser will open a page asking if you want to open Zoom Meetings" -> page: the browser goes to a launch page where a pop-up asks whether to open Zoom Meetings.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180

## tr093-d
- reasons: Same unsupported claims as tr093-a.
- fix requested: Delete "The first time, give yourself 5 to 10 minutes before the meeting starts." In step 2 say a small box (pop-up) asks whether to open Zoom Meetings. In step 3 say: click **Open**; depending on your browser the button may read **Allow** or **Open zoom.us**. Keep the passcode sentence and the "tell me what you see" line. Also make the first assistant turn match the fixed tr093-b.
- unsupported claims: "give yourself 5 to 10 minutes before the meeting starts" -> the page gives no early-join time. | "it may say Open Zoom Meetings, Allow, or Open zoom.us" -> page: the button is "Open" and may read "Allow" or "Open zoom.us" depending on browser and device; "open Zoom Meetings" is the pop-up question, not a button label. | "Your web browser will open a page asking if you want to open Zoom Meetings" -> page: the browser goes to a launch page where a pop-up asks whether to open Zoom Meetings.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180

## tr095-a
- reasons: One position claim not on the page.
- fix requested: In step 2 write "Open **Settings** and tap **your name**." (remove "at the top"). Everything else matches the Apple page.
- unsupported claims: "tap **your name** at the top" -> the page says only to tap your name; "at the top" is a position claim not on the page.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108366

## tr095-d
- reasons: One position claim not on the page.
- fix requested: In step 2 write "Open **Settings** and tap **your name**." (remove "at the top"). Everything else matches the Apple page.
- unsupported claims: "tap **your name** at the top" -> the page says only to tap your name; "at the top" is a position claim not on the page.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108366

## tr096-a
- reasons: Requirements list omits iOS 17.3 or later, which the page lists as a requirement.
- fix requested: In the last paragraph add the missing requirement from the Apple page: **iOS 17.3 or later** (for example "an iPhone updated to iOS 17.3 or later"). Keep the rest.
- required actions missing from the reply: Requirements: two-factor authentication, passcode, Face ID or Touch ID, Significant Locations on, Find My on, iOS 17.3 or later
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/120340

## tr096-b
- reasons: The user said 'if it gets stolen', which already means before. Asking 'before or already stolen' asks for something the user gave, so S2 is 0; the scenario does not really need clarification as written. The 'what to do now' branch is not covered by the cited page.
- fix requested: Rewrite the user message so the missing detail is the phone type, e.g. "how do I protect my phone if it gets stolen", and the reply is one question: "Good thing to set up ahead of time. Is your phone an **iPhone** or an **Android** phone?" Then update tr096-d to match (user answers "iPhone").
- low scores: {'ask_or_answer': 0, 'realistic_user': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/120340

## tr096-c
- reasons: Two question marks. The 'has your phone been stolen' branch has no support on the cited page and the reply cannot help with it.
- fix requested: Use one question: "Do you want to turn on **Stolen Device Protection**, the iPhone setting that helps protect your phone if it is stolen?" (one question mark).
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/120340

## tr096-d
- reasons: Requirements omit iOS 17.3 or later; unsupported 'one of the best' claim. First assistant turn asks an unnecessary question (style only; will change with tr096-b).
- fix requested: In the last paragraph add the missing requirement from the Apple page: **iOS 17.3 or later** (for example "an iPhone updated to iOS 17.3 or later"). Keep the rest. Replace "One of the best protections" with "A setting that helps is".
- unsupported claims: "One of the best protections is called Stolen Device Protection." -> ranking not on the Apple page; say "A helpful setting is called Stolen Device Protection."
- required actions missing from the reply: Requirements: two-factor authentication, passcode, Face ID or Touch ID, Significant Locations on, Find My on, iOS 17.3 or later
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/120340

## tr098-b
- reasons: Two questions (Windows or Mac, and text or everything). Must be one question.
- fix requested: Ask only: "I can help you make it bigger. Is your computer a **Windows** computer or a **Mac**?" Update tr098-d so the user answers that first turn (and later says just the text).
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

## tr098-c
- reasons: Two question marks ('Do you want to make text bigger?' and 'on which device').
- fix requested: One question only, e.g. "It looks like your message got cut off. Do you want to make the text bigger on a **computer** or on a **phone**?"
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

## tr099-b
- reasons: Two questions (iPhone or Android, and does it stop at 80%). Must be one question.
- fix requested: Ask only: "Let's figure out why. Is your phone an **iPhone** or an **Android** phone?" Update tr099-d so the user answers that.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-ca/108805

## tr101-c
- reasons: Two question marks (Is that right? And iPhone or Android?).
- fix requested: One question only: "Is your phone an **iPhone** or an **Android** phone?"
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/105103

## tr101-d
- reasons: After the user said iPhone 13 the reply still lists the Action button branch (other models). Unsupported position claim. Volume-button line missing.
- fix requested: Keep only the side-switch steps for an iPhone 13: look for orange, flip the switch so orange no longer shows. Delete the Action button section and "(above the volume buttons)". Keep the volume-button line.
- unsupported claims: "(above the volume buttons)" -> switch position not stated on the page.
- required actions missing from the reply: Volume buttons adjust ringer volume
- low scores: {'steps': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/105103

## tr102-a
- reasons: One unsupported gesture detail.
- fix requested: In "Use it" step 1 write "swipe up with **two fingers**, or tap the **Accessibility button**" (remove "from the bottom of the screen"). Optionally add that with TalkBack on it is a three-finger swipe. Rest matches the page.
- unsupported claims: "swipe up from the bottom of the screen with **two fingers**" -> page says only "two-finger swipe up"; "from the bottom of the screen" is not on the page.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accessibility/android/answer/7349565?hl=en

## tr102-d
- reasons: One unsupported gesture detail.
- fix requested: In "Use it" step 1 write "swipe up with **two fingers**, or tap the **Accessibility button**" (remove "from the bottom of the screen"). Optionally add that with TalkBack on it is a three-finger swipe. Rest matches the page.
- unsupported claims: "swipe up from the bottom of the screen with **two fingers**" -> page says only "two-finger swipe up"; "from the bottom of the screen" is not on the page.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accessibility/android/answer/7349565?hl=en

## tr103-a
- reasons: Unsupported label description and an unsupported final Done step.
- fix requested: In step 4 name the control as the page does, for example "Tap the **Edit Details** button (also called the **Info** button) on the reminder", with no "small i" description. Delete step 7 "Tap Done" unless a second official Apple Reminders page that shows a Done/save step is added as a source. Keep the 9:00 AM default sentence.
- unsupported claims: "Tap the **info** button (a small "i") next to it." -> the page calls it the "Edit Details" button (and "Info button" elsewhere) and does not describe an "i" icon. | "7. Tap **Done**." -> the Reminders steps on the page never mention a Done button (Done appears only in the Calendar app flow).
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102484

## tr103-b
- reasons: Three asks in two questions (device, what, when). Only the device changes the steps.
- fix requested: Ask only: "Sure. Is your phone an **iPhone** or an **Android** phone?" Update tr103-d so the user answers that (the reminder details can stay in the later turn).
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102484

## tr103-c
- reasons: Same unsupported claims as tr103-a.
- fix requested: In step 4 name the control as the page does, for example "Tap the **Edit Details** button (also called the **Info** button) on the reminder", with no "small i" description. Delete step 7 "Tap Done" unless a second official Apple Reminders page that shows a Done/save step is added as a source. Keep the 9:00 AM default sentence.
- unsupported claims: "Tap the **info** button (a small "i") next to it." -> the page calls it the "Edit Details" button (and "Info button" elsewhere) and does not describe an "i" icon. | "7. Tap **Done**." -> the Reminders steps on the page never mention a Done button (Done appears only in the Calendar app flow).
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102484

## tr103-d
- reasons: Same unsupported claims as tr103-a. (Earlier turn asks several things; style only, will change with tr103-b.)
- fix requested: In step 4 name the control as the page does, for example "Tap the **Edit Details** button (also called the **Info** button) on the reminder", with no "small i" description. Delete step 7 "Tap Done" unless a second official Apple Reminders page that shows a Done/save step is added as a source. Keep the 9:00 AM default sentence.
- unsupported claims: "Tap the **info** button (a small "i") next to it." -> the page calls it the "Edit Details" button (and "Info button" elsewhere) and does not describe an "i" icon. | "7. Tap **Done**." -> the Reminders steps on the page never mention a Done button (Done appears only in the Calendar app flow).
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102484
