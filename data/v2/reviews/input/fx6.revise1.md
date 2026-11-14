# Revision list: batch fx6, after review round 1 (8 examples)

Edit ONLY these examples in data/v2/specs/fx6.py, then rebuild.

## tr076-e
- reasons: Unsupported 'newer'. Step 1 gives no way to get from a sleeping screen to the Lock Screen camera, and the user said the screen is asleep; the page does not explain how, so the reply must not imply a method.
- fix requested: Change the last paragraph to: 'On supported iPhone models you can also open the camera with the **Camera Control** button.' (remove 'Some newer'). Change the final line to 'The link or content from the code will open.' or drop it. In step 1 keep 'Open the **Camera** from the Lock Screen' but do not invent how (page gives no swipe or tap detail); optionally add the page-supported alternative that the camera can also be opened from Control Center.
- unsupported claims: 'Some newer iPhone models also have a Camera Control button' -> page only says 'on supported models'; it never says newer, and does not name models. | 'The recipe page will open.' -> page only says the content opens; the reply assumes what the code leads to.
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102680

## tr079-r
- reasons: The final reply leaves the user with a vague step (check Android version) and omits the page's actual troubleshooting cause: disabling the Safety app removes it from the app list.
- fix requested: Rewrite the final reply as: (1) 'In your list of apps it is called **Safety**. In the Play Store and in **Settings** it is called **Personal Safety**, so look for that name there.' (2) 'If you or someone else turned the app off (disabled it), it will not show in your app list.' (3) 'This app is only on some Android phones, so yours may not have it.' (4) 'On Android 12 and earlier without the app you can still sign in with your Google Account, add emergency contacts, and list medical information.' Delete the 'check your Android version' step. Do not add steps for re-enabling the app (page gives none).
- unsupported claims: 'Some phones call it something else' -> page says the same app shows as Personal Safety in the Play Store and Settings and as Safety in the app list; fine as a hedge but vague. | 'Open Settings and check your Android version.' -> no way to do this is given and the page does not say to do it; it is an unexplained extra step with no outcome.
- required actions missing from the reply: Note the app disappears from the app list if it was disabled | Note that on Android 12 and earlier without the app you can still sign in, add emergency contacts and list medical info
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/9319337?hl=en

## tr083-e
- reasons: Step 3 does not say where to type the search or what the user will see. The pinned-Downloads claim lacks the 22H2 condition. The cloud paragraph is off-topic for a user who said nothing about cloud storage and adds length and jargon ('cloud account').
- fix requested: Keep steps 1 and 2. Reword step 3 to 'In **Home**, search for the part of the name you remember, such as **W2**. Matching files on your PC will be listed.' (do not describe where the search box is; the page does not say). Replace the Downloads sentence with 'On Windows 11 version 22H2 or later, **Downloads** is pinned under **Quick access** on **Home**, so you can open it too.' Delete the cloud-account paragraph, or shorten it to 'If you keep files in the cloud (like OneDrive), sign in from **Start**, then **Settings**, then **Accounts** so they are searched too' only if kept plain.
- unsupported claims: 'You can also look in **Downloads**, which is pinned under **Quick access** on **Home**.' -> page says it is pinned by default only on Windows 11 version 22H2 or later; stated here without that condition.
- required actions missing from the reply: Downloads is pinned in Quick access only from Windows 11 version 22H2
- low scores: {'steps': 1, 'actionable': 1, 'plain': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

## tr086-e
- reasons: One unsupported claim about urgency as a known trick.
- fix requested: Change the first sentence to: 'Please don't click the link. Real companies won't email you a link to update your payment information.' Delete 'and the rush is a common trick'. Everything else can stay.
- unsupported claims: 'and the rush is a common trick' -> the page does not discuss time pressure or deadlines as a scam sign; it lists claims of account problems and links to update payment details.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

## tr086-r
- reasons: The user typed a credit card number into a fake page. The reply never tells them to call the card company, which is the main protective action for this case. It also adds an unsupported IdentityTheft.gov detail.
- fix requested: Add a first step: 'Call your credit card company right away, using the number on the back of your card, and tell them you gave your card number to a scammer. Ask them to refund any charges.' Add the second source https://consumer.ftc.gov/articles/what-do-if-you-were-scammed (section on credit card payments: 'Report it to the credit card issuer immediately. Use the number on the back of your card ... Ask them to refund your money.'). Change the IdentityTheft.gov step to 'Go to IdentityTheft.gov. It gives steps based on what information you gave away.' (remove 'for a lost credit card number'). Keep the scan step and the report step.
- unsupported claims: 'follow the steps for a lost credit card number' -> the cited page only says to go to IdentityTheft.gov for 'steps based on what was lost'; it does not name a 'lost credit card number' path.
- required actions missing from the reply: Contact the credit card issuer right away using the number on the back of the card and ask for a refund (critical; from a second FTC page)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

## tr087-e
- reasons: User says they do not use a computer. Step 2 sends them to a website (ReportFraud.ftc.gov) without any note about doing it on a phone; the page does not say it works on a phone and gives no phone number.
- fix requested: Keep step 1 (report junk or spam in the messaging app) as the main answer. Either remove step 2, or reword it to 'If you are able to open web pages on your phone, you can also report it at **ReportFraud.ftc.gov**.' Do not claim the site works on every phone. Keep the blocking-tools step and the final paragraph.
- low scores: {'constraints': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

## tr087-r
- reasons: One unsupported instruction ('don't reply').
- fix requested: Change the opening to 'You did the right thing by closing it. Please don't open that link again.' (delete 'and don't reply to the text'). Keep the rest. Note the page gives no steps for people who already clicked, so keep the reassurance limited to what it says.
- unsupported claims: 'Please don't open that link again, and don't reply to the text.' -> 'don't reply' is not on the cited page (it only says not to click links).
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages

## tr088-e
- reasons: One unsupported claim about urgency.
- fix requested: Change the sentence to: 'What you describe matches signs of a romance scam: asking to move off the site and asking for money for a visa.' (remove 'which is often framed as urgent'). Keep the rest.
- unsupported claims: 'which is often framed as urgent' -> the page does not say romance scam money requests are urgent.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams
