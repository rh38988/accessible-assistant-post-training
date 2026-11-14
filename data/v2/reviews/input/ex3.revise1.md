# Revision list: batch ex3, after review round 1 (39 examples)

Edit ONLY these examples in data/v2/specs/ex3.py, then rebuild.

## tr033-a
- reasons: Unsupported alternative label 'System update'.
- fix requested: In step 3 delete 'or System update'. Keep only a general hedge such as 'Names can be a little different on some phones.' Optionally add the source cue that the update status appears on that screen (page: 'The update status appears there').
- unsupported claims: 'On some phones this is called **System update** or is in a different spot.' -> the page never names 'System update' as an alternative label; it only says update controls sit under System > Software updates and that schedules vary by manufacturer.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/7680439?hl=en

## tr033-d
- reasons: Unsupported label 'System update'. Final reply has a doubled lead-in ('Otherwise, follow these steps.' then 'Here's how to check for an update.').
- fix requested: Delete 'or System update' from step 3 (use a general hedge only). Remove the second lead-in 'Here's how to check for an update.' so the reply reads: 'Thanks. If you still see the update notification, you can tap it, then tap its update button. Otherwise, before you start, connect to Wi-Fi and charge the battery to at least 75%. 1. ...'. The notification tap is supported (page: open the notification and tap its update button).
- unsupported claims: 'On some phones this is called **System update** or is in a different spot.' -> 'System update' is not on the page.
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/7680439?hl=en

## tr034-a
- reasons: Wrong button label in step 4.
- fix requested: Change step 4 to 'Click **Check for Windows updates**.' Optional: for the error-message line, a second source exists, 'Troubleshoot problems updating Windows' (linked from the cited page); keep the line as a general 'tell me what it says'.
- unsupported claims: 'Click **Check for updates**.' -> the page's button is 'Check for Windows updates'.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates

## tr034-c
- reasons: Wrong button label. Doubled lead-in ('Sure, here's the path:' then 'Here's how to check...'). User said they are comfortable with Settings and only want to know where to go, but the reply keeps the beginner-style explanations.
- fix requested: Change step 4 to 'Click **Check for Windows updates**.' Use one lead-in only. Shorten for this user: 'Sure. Go to **Start**, then **Settings**, then **Windows Update**, and click **Check for Windows updates**. If it finds updates, click **Download & install**. If Windows asks you to restart, do that to finish.' (keep numbered steps only if the writer prefers; drop the Windows-logo explanation and the long lead-in).
- unsupported claims: 'Click **Check for updates**.' -> the page's button is 'Check for Windows updates'.
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates

## tr034-d
- reasons: Wrong button label. Doubled lead-in ('Thanks. Here's how to install the updates.' then 'Here's how to check for updates and install them.').
- fix requested: Change step 4 to 'Click **Check for Windows updates**.' Remove one of the two lead-in sentences, e.g. start 'Thanks. Here's how to check for updates and install them. It can take a while, so do it when you won't need the computer for a bit.'
- unsupported claims: 'Click **Check for updates**.' -> the page's button is 'Check for Windows updates'.
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates

## tr035-a
- reasons: Missing the internet/Wi-Fi requirement (non-critical); no cue for what the user will see after turning Backup on although the page gives one.
- fix requested: Add a short line before the steps: 'Use Wi-Fi if you can, because it works best.' (page: 'You need a good internet connection. Wi-Fi works best.') After step 6 add a what-you-see cue from the page: 'At the top of your library you should see the backup status, such as **Backing up photos** and later **Backup complete**.'
- required actions missing from the reply: Have a good internet connection; Wi-Fi works best (non-critical)
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid

## tr035-c
- reasons: Missing Wi-Fi/internet line; no what-you-see cue; doubled lead-in ('Google Photos can save a copy online:' then 'You can use the Google Photos app to save copies...').
- fix requested: Keep the sympathetic opening, then use only one lead-in, e.g. 'I'm sorry about those pictures. Let's make sure your new ones are kept safe. You can use the **Google Photos** app to save copies of your photos to your Google Account.' Delete the line 'Google Photos can save a copy online:'. Add a short line before the steps: 'Use Wi-Fi if you can, because it works best.' (page: 'You need a good internet connection. Wi-Fi works best.') After step 6 add a what-you-see cue from the page: 'At the top of your library you should see the backup status, such as **Backing up photos** and later **Backup complete**.'
- required actions missing from the reply: Have a good internet connection; Wi-Fi works best (non-critical)
- low scores: {'steps': 1, 'actionable': 1, 'plain': 1} | gates not passed: {}
- sources: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid

## tr035-d
- reasons: Missing Wi-Fi/internet line; no what-you-see cue; doubled lead-in ('On Android, Google Photos can do this for you.' then 'You can use the Google Photos app to save copies...').
- fix requested: Merge into one lead-in: 'Great. On Android you can use the **Google Photos** app to save copies of your photos to your Google Account.' Add a short line before the steps: 'Use Wi-Fi if you can, because it works best.' (page: 'You need a good internet connection. Wi-Fi works best.') After step 6 add a what-you-see cue from the page: 'At the top of your library you should see the backup status, such as **Backing up photos** and later **Backup complete**.'
- required actions missing from the reply: Have a good internet connection; Wi-Fi works best (non-critical)
- low scores: {'steps': 1, 'actionable': 1, 'plain': 1} | gates not passed: {}
- sources: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid

## tr036-a
- reasons: Unsupported time estimate, misplaced auto-install statement, and the 'already listed? you're finished' check is missing.
- fix requested: Replace 'It takes about five minutes.' with 'It can take a few minutes.' Add a step after opening Printers & scanners: 'Look at the list of printers. If your printer is already there, you're finished.' Move 'Some printers install by themselves' to the First section: 'Some printers, especially ones with a cable, install by themselves once they are plugged in and on. Check the list first.' Number the later steps accordingly. Optional second source for problems: 'Fix printer connection and printing problems in Windows' (linked from the cited page).
- unsupported claims: 'It takes about five minutes.' -> page gives no total time; it only says wait 'a few minutes' for the list to populate. | 'Some printers install by themselves after step 4.' -> page says a wired printer often installs automatically once connected and powered on, i.e. BEFORE opening Printers & scanners; placement after step 4 is wrong.
- required actions missing from the reply: Check whether the printer is already in the installed list; if so you are finished (non-critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows

## tr036-c
- reasons: Clarifying reply asks two questions (two question marks): what the printer won't do, and what it prints from.
- fix requested: Ask ONE question with one question mark, e.g. 'It looks like your message got cut off. What happens when you try to set up the new printer: does it not **turn on**, not **connect**, or not **print**?' Do not add the second question about computer or phone.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows

## tr036-d
- reasons: Unsupported time estimate, misplaced auto-install statement, missing 'already listed' check, and doubled lead-in ('Great, here's how to add it...' then 'Here's how to add your new printer.').
- fix requested: Replace 'It takes about five minutes.' with 'It can take a few minutes.' Add a step after opening Printers & scanners: 'Look at the list of printers. If your printer is already there, you're finished.' Move 'Some printers install by themselves' to the First section: 'Some printers, especially ones with a cable, install by themselves once they are plugged in and on. Check the list first.' Number the later steps accordingly. Optional second source for problems: 'Fix printer connection and printing problems in Windows' (linked from the cited page). Also keep only one lead-in: 'Great, here's how to add the printer to your Windows 11 laptop.'
- unsupported claims: 'It takes about five minutes.' -> page gives no total time; it only says wait 'a few minutes' for the list to populate. | 'Some printers install by themselves after step 4.' -> page says a wired printer often installs automatically once connected and powered on, i.e. BEFORE opening Printers & scanners; placement after step 4 is wrong.
- required actions missing from the reply: Check whether the printer is already in the installed list; if so you are finished (non-critical)
- low scores: {'steps': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows

## tr037-b
- reasons: The clarifying reply bundles two questions in one sentence (phone or computer, and which email app).
- fix requested: Ask one question only, e.g. 'I can help. Which email app are you using, for example **Gmail** on your phone?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid

## tr037-c
- reasons: Two questions: what to attach, and where.
- fix requested: Ask one question: 'Happy to help. **Where do you want to attach something**: in an email, in a text message, or somewhere else?' Remove the 'what would you like to attach' question.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid

## tr037-d
- reasons: Unsupported claims in the closing paragraph; doubled lead-in ('Thanks, here's how in the Gmail app.' then 'Here's how.').
- fix requested: Use one lead-in: 'Thanks, here's how in the Gmail app. It takes about a minute.' Change the last paragraph to: 'If you added the wrong photo, tap **Close** to the right of its name to remove it. If the attachments are over 25 MB, Gmail adds them as a Google Drive link instead.'
- unsupported claims: 'Very large files are added as a Google Drive link instead, which the person can still open.' -> 'which the person can still open' is not on the page, and 'the person' is odd phrasing; page says over the limit (25 MB for personal Gmail) the attachment is removed and added as a Drive link. | 'tap the close icon (**X**)' -> the page says tap 'Close'; no X described.
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid

## tr038-a
- reasons: No link to the recovery page (no starting point); unsupported 'starting with your Gmail address'.
- fix requested: Step 1: 'Go to **accounts.google.com/signin/recovery** (Google's account recovery page).' Step 2: delete 'starting with your Gmail address'; say 'Answer the questions it asks to show the account is yours. Answer as accurately as you can; if you're not sure, give your best guess. Wrong guesses don't end the process.' Last line: 'If you recently changed your recovery info, it can take up to 7 days to take effect, so try again after a few days.'
- unsupported claims: 'Go to Google's **account recovery** page.' -> gives no link or address, so a low-confidence user has no starting point; the page links to accounts.google.com/signin/recovery. | 'Enter the details it asks for, starting with your Gmail address.' -> 'starting with your Gmail address' is not on the page; it only says you will be asked questions to confirm the account is yours.
- required actions missing from the reply: Start recovery with the link 'Follow the steps to recover your Google Account or Gmail' (accounts.google.com/signin/recovery) (critical)
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accounts/answer/7682439?hl=en

## tr038-b
- reasons: Asks two things (which email, and what is going wrong).
- fix requested: Ask one question: 'That's stressful, but it can usually be fixed. **Which email do you use**, for example Gmail, which ends in @gmail.com?' Remove the 'what's going wrong' question.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/accounts/answer/7682439?hl=en

## tr038-c
- reasons: No link to the recovery page; unsupported 'starting with your Gmail address'; doubled lead-in ('You can reset the password:' then 'You can get back in through Google's account recovery.').
- fix requested: Step 1: 'Go to **accounts.google.com/signin/recovery** (Google's account recovery page).' Step 2: delete 'starting with your Gmail address'; say 'Answer the questions it asks to show the account is yours. Answer as accurately as you can; if you're not sure, give your best guess. Wrong guesses don't end the process.' Last line: 'If you recently changed your recovery info, it can take up to 7 days to take effect, so try again after a few days.' Use one lead-in only: 'That happens a lot when a phone stays signed in for years. You can get back in through Google's account recovery.'
- unsupported claims: 'Go to Google's **account recovery** page.' -> gives no link or address, so a low-confidence user has no starting point; the page links to accounts.google.com/signin/recovery. | 'Enter the details it asks for, starting with your Gmail address.' -> 'starting with your Gmail address' is not on the page; it only says you will be asked questions to confirm the account is yours.
- required actions missing from the reply: Start recovery with the link 'Follow the steps to recover your Google Account or Gmail' (accounts.google.com/signin/recovery) (critical)
- low scores: {'steps': 1, 'actionable': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accounts/answer/7682439?hl=en

## tr038-d
- reasons: No link to the recovery page; unsupported 'starting with your Gmail address'; doubled lead-in ('Thanks. You can reset it through Google's account recovery.' then 'You can get back in through Google's account recovery.').
- fix requested: Step 1: 'Go to **accounts.google.com/signin/recovery** (Google's account recovery page).' Step 2: delete 'starting with your Gmail address'; say 'Answer the questions it asks to show the account is yours. Answer as accurately as you can; if you're not sure, give your best guess. Wrong guesses don't end the process.' Last line: 'If you recently changed your recovery info, it can take up to 7 days to take effect, so try again after a few days.' Use one lead-in only: 'Thanks. You can get back in through Google's account recovery.'
- unsupported claims: 'Go to Google's **account recovery** page.' -> gives no link or address, so a low-confidence user has no starting point; the page links to accounts.google.com/signin/recovery. | 'Enter the details it asks for, starting with your Gmail address.' -> 'starting with your Gmail address' is not on the page; it only says you will be asked questions to confirm the account is yours.
- required actions missing from the reply: Start recovery with the link 'Follow the steps to recover your Google Account or Gmail' (accounts.google.com/signin/recovery) (critical)
- low scores: {'steps': 1, 'actionable': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accounts/answer/7682439?hl=en

## tr039-a
- reasons: Two claims not on the cited page ('Hang up'; urgency/pressure as warning signs).
- fix requested: Remove the 'Hang up' step and start the list with the sourced action: '1. **Don't trust the voice**, even if it sounds like her. Call your granddaughter on a phone number you know is hers, not a number from the call.' Then '2. If you can't reach her, try another family member or her friends.' In the warning-signs line keep only the payment red flag: 'Scammers ask you to pay in ways that make it hard to get your money back: wire money, cryptocurrency, or gift cards.' Remove 'an urgent emergency, pressure to act fast'. No second official source for 'hang up' was found; do not add it. Keep 'don't send any money yet' first.
- unsupported claims: '**Hang up.** You don't need to argue or explain.' -> the page never says to hang up (only 'Call the person who supposedly contacted you and verify the story'). | '**Warning signs of this scam:** an urgent emergency, pressure to act fast...' -> the page does not list urgency or pressure as warning signs; its warning sign is payment by wire, crypto, or gift card.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes

## tr039-b
- reasons: The user already said someone called asking for money for the granddaughter. Verification steps do not depend on how the money was to be sent, so no clarification is needed. The reply delays the protective action behind a question and has no 'don't send money' line (G2). It also asks two things in one sentence.
- fix requested: Lead with the protective action, as tr041-b does, then ask ONE question: 'I'm glad you asked before doing anything. **Please don't send any money yet.** Have you already sent anything, or are you still deciding?' Do not ask about the payment method and do not give steps in this reply (this keeps the missing-info shape).
- low scores: {'ask_or_answer': 0} | gates not passed: {'safety': 'fail'}
- sources: https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes

## tr039-c
- reasons: Compound clarifying question (what the caller said, and whether they asked for money or personal information). Also no light protective line while the situation is unknown.
- fix requested: Ask one question: 'I'm happy to help you figure it out. Please don't send money or share any codes or personal details until we check. **What did the caller say?**'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes

## tr039-d
- reasons: Same unsupported claims in the final reply ('Hang up'; urgency/pressure as warning signs). Earlier assistant turn asks two things (style only).
- fix requested: Remove the 'Hang up' step and start the list with the sourced action: '1. **Don't trust the voice**, even if it sounds like her. Call your granddaughter on a phone number you know is hers, not a number from the call.' Then '2. If you can't reach her, try another family member or her friends.' In the warning-signs line keep only the payment red flag: 'Scammers ask you to pay in ways that make it hard to get your money back: wire money, cryptocurrency, or gift cards.' Remove 'an urgent emergency, pressure to act fast'. No second official source for 'hang up' was found; do not add it. Keep 'don't send any money yet' first.
- unsupported claims: '**Hang up.** You don't need to argue or explain.' -> the page never says to hang up (only 'Call the person who supposedly contacted you and verify the story'). | '**Warning signs of this scam:** an urgent emergency, pressure to act fast...' -> the page does not list urgency or pressure as warning signs; its warning sign is payment by wire, crypto, or gift card.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes

## tr040-a
- reasons: Unsupported 'delete it' step and bank advice; optional ReportFraud.ftc.gov report missing.
- fix requested: Delete step 4 ('Then delete it.'). Replace the last paragraph with a non-instructional offer: 'If you already clicked the link or typed in any information, tell me and we'll look at what to do next.' (do not give bank or card steps, they are not on the page). Step 3: 'Report the text. Use your messaging app's report junk or spam option. If there isn't one, forward the text to **7726**. You can also tell the FTC at **ReportFraud.ftc.gov**.'
- unsupported claims: '4. Then delete it.' -> the page gives no advice to delete the message. | 'If you already clicked and typed in your card number, call your bank right away using the number on the back of your card.' -> the page says nothing about contacting a bank or card company; it only warns that payments and entered details go to the scammer.
- required actions missing from the reply: Optionally tell the FTC at ReportFraud.ftc.gov (non-critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam

## tr040-b
- reasons: Scam-safety reply asks a question without first giving the protective action (G2: protective action must not wait behind a question). tr040-c does include it.
- fix requested: Add a protective line before the single question: 'Let's check it together. For now, **please don't click any link or give any information** in that text. **What does the text ask you to do?**' Keep it to one question; the examples after the question are optional.
- low scores: {} | gates not passed: {'safety': 'fail'}
- sources: https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam

## tr040-c
- reasons: Two questions (two question marks): 'Do you mean ... a link in it?' and 'What does the text ask you to do?'
- fix requested: Keep the protective line and ask one question: 'If you got a text that looks like it's from USPS with a link in it, please **don't click the link** yet. **What does the text ask you to do?**'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam

## tr041-a
- reasons: Overbroad claim 'people you know don't ask'; missing 'give the card number and receipt to the company' and how to find the company's contact details.
- fix requested: Change the sentence to: 'Real businesses and government agencies never ask to be paid with gift cards, and scammers often pretend to be someone you know.' In the 'already bought' section add: 'Give the company the card number and the receipt.' and 'The FTC's gift card scam page lists phone numbers for major gift card companies. If yours isn't listed, look on the card or search online for the company that issued it.'
- unsupported claims: 'Real businesses, government agencies, and people you know don't ask to be paid with gift card numbers' -> the page says no real business or government agency will ask; it does not say people you know never do (it warns scammers pose as friends or relatives and says to contact them to check).
- required actions missing from the reply: Keep the gift card and store receipt; give the card number and receipt to the company (critical) | Contact info for gift card companies is on the FTC page; if not listed, check the card or search online for the issuer (non-critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

## tr041-b
- reasons: Protective line comes first (good), but the reply asks two questions: who is asking, and whether cards were already bought or sent.
- fix requested: Keep the first two sentences, then ask only: '**Have you already bought or sent any gift cards?**' Drop 'Who is asking'.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

## tr041-c
- reasons: The user says a friend ALREADY bought cards; the urgent protective steps (contact the gift card company right away) are placed at the very end, after the 'don't buy' steps meant for someone who has not acted (G2 order). The 'already bought' bullets are written to 'you', not the friend. Plus the overbroad 'people you know' claim and missing items.
- fix requested: Open with: 'You're not being rude by checking, and a real pastor would understand. Your friend should act first: she should **contact the gift card company right away**, tell them the cards were used in a scam, ask for the money back, and ask if they can freeze it. She should give them the card numbers and receipt, and report it at ReportFraud.ftc.gov.' Then give the 'for you' steps (don't buy, check with the pastor on a number you already have). Change the sentence to: 'Real businesses and government agencies never ask to be paid with gift cards, and scammers often pretend to be someone you know.' In the 'already bought' section add: 'Give the company the card number and the receipt.' and 'The FTC's gift card scam page lists phone numbers for major gift card companies. If yours isn't listed, look on the card or search online for the company that issued it.'
- unsupported claims: 'Real businesses, government agencies, and people you know don't ask to be paid with gift card numbers' -> the page says no real business or government agency will ask; it does not say people you know never do (it warns scammers pose as friends or relatives and says to contact them to check).
- required actions missing from the reply: Keep the gift card and store receipt; give the card number and receipt to the company (critical) | Contact info for gift card companies is on the FTC page; if not listed, check the card or search online for the issuer (non-critical)
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {'source': 'fail', 'safety': 'fail'}
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

## tr041-d
- reasons: Overbroad 'people you know' claim; 'Here's what to do:' appears twice; the user said they have bought nothing, yet the reply keeps the long 'If you already bought cards' section (extra text, ignores the user's answer); missing items.
- fix requested: Remove the first 'Here's what to do:' and the whole 'If you already bought cards and shared the numbers' section (replace with one line: 'If you ever do share card numbers, tell me right away and call the gift card company.'). Change the sentence to: 'Real businesses and government agencies never ask to be paid with gift cards, and scammers often pretend to be someone you know.' In the 'already bought' section add: 'Give the company the card number and the receipt.' and 'The FTC's gift card scam page lists phone numbers for major gift card companies. If yours isn't listed, look on the card or search online for the company that issued it.'
- unsupported claims: 'Real businesses, government agencies, and people you know don't ask to be paid with gift card numbers' -> the page says no real business or government agency will ask; it does not say people you know never do (it warns scammers pose as friends or relatives and says to contact them to check).
- required actions missing from the reply: Keep the gift card and store receipt; give the card number and receipt to the company (critical) | Contact info for gift card companies is on the FTC page; if not listed, check the card or search online for the issuer (non-critical)
- low scores: {'steps': 1, 'constraints': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

## tr042-a
- reasons: The 'Continue' tap after Family is missing, which is a required step for creating the group; plus-sign and 'at the top' claims are not on the page.
- fix requested: Step 2: 'Tap **Family**, then tap **Continue**.' Step 1: delete 'at the top'. Step 5: 'Tap the **Add Member** button.' (delete the plus-sign description). Do not repeat 'Settings, then Family' as a new first step after step 3 if the writer merges the group setup and invitation (page: the onscreen steps create the group and invite family members).
- unsupported claims: 'tap the **add member** button (it has a plus sign)' -> the page calls it the 'Add Member' button and shows an icon, but never describes a plus sign. | 'tap **your name** at the top' -> 'at the top' is not stated on the page.
- required actions missing from the reply: Tap Family, then tap Continue (critical)
- low scores: {'steps': 0} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108380

## tr042-b
- reasons: Two questions (what to share, and iPhone or Android).
- fix requested: Ask one question: 'There are a few ways to do that. Is your phone an **iPhone** or an **Android** phone?' Remove the 'what would you like to share' question.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/108380

## tr042-d
- reasons: Missing the 'Continue' tap after Family; plus-sign and 'at the top' claims not on the page. Earlier assistant turn asks two things (style only).
- fix requested: Step 2: 'Tap **Family**, then tap **Continue**.' Step 1: delete 'at the top'. Step 5: 'Tap the **Add Member** button.' (delete the plus-sign description). Do not repeat 'Settings, then Family' as a new first step after step 3 if the writer merges the group setup and invitation (page: the onscreen steps create the group and invite family members).
- unsupported claims: 'tap the **add member** button (it has a plus sign)' -> the page calls it the 'Add Member' button and shows an icon, but never describes a plus sign. | 'tap **your name** at the top' -> 'at the top' is not stated on the page.
- required actions missing from the reply: Tap Family, then tap Continue (critical)
- low scores: {'steps': 0} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108380

## tr043-a
- reasons: Unsupported claim about caller display.
- fix requested: Change the closing sentence to 'Now you can find the number in Contacts.' (delete 'the name will show up when the office calls you').
- unsupported claims: 'Now the name will show up when the office calls you' -> not on the page, which says nothing about how calls are displayed.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid

## tr043-d
- reasons: Unsupported caller-display claim, and it assumes a doctor's office although the user only asked how to save a phone number.
- fix requested: Change the closing sentence to 'Now you can find the number in Contacts.' Keep 'Dr. Smith's Office' only as an example name ('Type a name, like **Mom** or **Dr. Smith's Office**.') and remove any wording that assumes the number is an office.
- unsupported claims: 'Now the name will show up when the office calls you' -> not on the page (it says nothing about caller display); in the follow-up example the user never mentioned a doctor's office.
- low scores: {'constraints': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid

## tr045-a
- reasons: Invented confirmation step; unsupported icon look.
- fix requested: Delete step 5. In step 3 say: 'Tap the number. (In Classic view, tap the **Info** button next to it instead.)' Everything else (Recents, Block Caller, caller not told, voicemail saved with no notification) matches the page.
- unsupported claims: '5. Confirm if asked.' -> the page's Phone-app steps have no confirmation step. | 'a small **"i"** in a circle' -> the page says 'Info button' (Classic view) and does not describe its look.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/111104

## tr045-d
- reasons: Invented confirmation step; unsupported icon look; doubled lead-in ('Here's how to block it on your iPhone.' then 'You can block that number from your list of recent calls.').
- fix requested: Delete step 5. In step 3 say: 'Tap the number. (In Classic view, tap the **Info** button next to it instead.)' Everything else (Recents, Block Caller, caller not told, voicemail saved with no notification) matches the page. Use one lead-in: 'Thanks. You can block that number from your list of recent calls.'
- unsupported claims: '5. Confirm if asked.' -> the page's Phone-app steps have no confirmation step. | 'a small **"i"** in a circle' -> the page says 'Info button' (Classic view) and does not describe its look.
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/111104

## tr046-a
- reasons: Unsupported 'three dots' and invented confirmation step.
- fix requested: Step 2: 'Tap **More**, then choose **Call history**.' (delete 'three dots'). Delete step 5. Keep the line about visual voicemail and the hedge about the Phone app looking different.
- unsupported claims: 'Tap the **More** menu (three dots)' -> the page only labels the icon 'More' (alt text 'More'); 'three dots' is not stated. | '5. Confirm if asked.' -> the page gives no confirmation step after Block / report spam.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/phoneapp/answer/6325463?hl=en

## tr046-c
- reasons: Two questions (calling or texting, and iPhone or Android).
- fix requested: Ask one question: 'Sure, I can help you block it. Is your phone an **iPhone** or an **Android** phone?'
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.google.com/phoneapp/answer/6325463?hl=en

## tr046-d
- reasons: Unsupported 'three dots' and invented confirmation step.
- fix requested: Step 2: 'Tap **More**, then choose **Call history**.' (delete 'three dots'). Delete step 5. Keep the line about visual voicemail and the hedge about the Phone app looking different.
- unsupported claims: 'Tap the **More** menu (three dots)' -> the page only labels the icon 'More' (alt text 'More'); 'three dots' is not stated. | '5. Confirm if asked.' -> the page gives no confirmation step after Block / report spam.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/phoneapp/answer/6325463?hl=en
