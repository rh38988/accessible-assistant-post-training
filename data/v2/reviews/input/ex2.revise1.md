# Revision list: batch ex2, after review round 1 (25 examples)

Edit ONLY these examples in data/v2/specs/ex2.py, then rebuild.

## pilot-014
- reasons: Two claims not supported by the cited pages (hang up step, 'almost impossible to get back').
- fix requested: Delete step 1 ('Hang up if they call back...'), or replace it with 'Don't buy anything and don't read out any numbers, however upsetting the story is' (page: 'resist the urge to act immediately, no matter how dramatic the story may be'). Replace 'which are almost impossible to get back' with 'a way of paying that scammers like because it is hard to get your money back'. Keep the other steps. Renumber the steps.
- unsupported claims: 'Hang up if they call back. You don't need to argue.' -> the FTC page does not tell the user to hang up; it says resist acting immediately and verify at a known number. | 'gift cards, which are almost impossible to get back' -> the pages say scammers ask for payment that is hard to get money back with and list gift cards among such methods; they do not say gift cards are 'almost impossible' to get back.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://www.ftc.gov/node/54353 ; https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay

## pilot-015
- reasons: Bank phone number source ('back of your bank card') is not on the page, which names the statement or the bank's app.
- fix requested: In step 3 and the final paragraph replace 'the number on the back of your bank card or on a paper statement' / 'the number on your card' with 'a phone number from your bank statement or your bank's app'. Keep 'Don't use any number from the text.' Optionally say 'That code is only meant for you to log in to your account' instead of 'works like a key'.
- unsupported claims: 'call your bank using the number on the **back of your bank card**' (also repeated in 'using the number on your card') -> the page says to use a number from your statement or app; the back of the card is not on the page. | 'That code works like a key to your bank account.' -> page only says the code is 'only for you to log into your account'; the 'key' framing is added (minor).
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/node/84809

## pilot-016
- reasons: The sources give a complete general answer (pay by credit card; avoid sellers insisting on gift cards, wire transfers, payment apps, crypto), so the question does not change the steps. The reply asks a two-part question (what are you buying AND how are they asking you to pay) and adds a tip, which is neither one clean question nor a direct answer.
- fix requested: Either (a) rewrite as a direct answer from https://consumer.ftc.gov/articles/online-shopping: paying by credit card best protects you in case of a scam and lets you dispute a charge (written notice within 60 days of the first bill showing the error); 'https' means the connection is encrypted but does not mean the site is legitimate; do not buy from sellers who insist on gift cards, wire transfers, payment apps, or cryptocurrency; and relabel the scenario direct; or (b) keep it as missing_info but ask ONE short question with one question mark, e.g. 'How is the seller asking you to pay?', with no tip.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay ; https://consumer.ftc.gov/articles/online-shopping

## pilot-017
- reasons: source unreadable: https://www.facebook.com/help/120939471321735 returned robots_disallowed on two WebFetch tries and curl through the proxy was blocked (403). The reply itself (one clarifying question about phone vs computer) looks sound but cannot be checked against the page; whether the steps differ by device cannot be confirmed.
- fix requested: Data Lead: confirm by hand that the Facebook page gives different steps for the app and for a computer (so the question is needed), or replace the source with a readable official page (for example a Facebook Help Center mirror or a different Facebook help article on audience and privacy settings).
- low scores: {} | gates not passed: {'source': 'unverified'}
- sources: https://www.facebook.com/help/120939471321735

## tr021-a
- reasons: Three details not on the cited page (icon, slider position, sample text).
- fix requested: Delete 'Its icon is a gray gear.'; change step 4 to 'Drag the slider to the right.' (remove 'at the bottom of the screen'); delete the sentence 'The sample text changes as you drag, so you can stop when it's easy to read.' and, if a cue is wanted, say 'Stop when the text is easy to read.' Keep the Larger Text path (Settings > Accessibility > Display & Text Size > Larger Text) and the warning that very large text can make buttons harder to tap.
- unsupported claims: 'Its icon is a gray gear.' -> the Apple page does not describe the Settings icon. | 'Drag the slider at the bottom of the screen to the right.' -> page says only 'Drag the slider'; position (bottom of the screen) is not on the page. | 'The sample text changes as you drag, so you can stop when it's easy to read.' -> the page mentions no preview text.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102453

## tr021-d
- reasons: Same three unsupported details as tr021-a in the final reply.
- fix requested: Delete 'Its icon is a gray gear.'; change step 4 to 'Drag the slider to the right.' (remove 'at the bottom of the screen'); delete the sentence 'The sample text changes as you drag, so you can stop when it's easy to read.' and, if a cue is wanted, say 'Stop when the text is easy to read.' Keep the Larger Text path (Settings > Accessibility > Display & Text Size > Larger Text) and the warning that very large text can make buttons harder to tap.
- unsupported claims: 'Its icon is a gray gear.' -> the Apple page does not describe the Settings icon. | 'Drag the slider at the bottom of the screen to the right.' -> page says only 'Drag the slider'; position (bottom of the screen) is not on the page. | 'The sample text changes as you drag, so you can stop when it's easy to read.' -> the page mentions no preview text.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102453

## tr022-a
- reasons: Search bar position and 'right away' are not on the page.
- fix requested: Change step 2 to 'Search for **Font size** in Settings.' (remove 'the search bar at the top of'), e.g. 'Tap the search icon in Settings and type **Font size**' only if you keep it generic; delete 'The change happens right away.' Keep 'A few apps ignore this setting' (page: 'The font size setting doesn't apply to some apps'). Optionally add the page's Quick Settings option: swipe down from the top, tap Font Size, use Increase or drag the slider (up to 200%).
- unsupported claims: 'Tap the search bar at the top of Settings' -> the Google page says only 'Search and select Font size'; the search bar position is not on the page. | 'The change happens right away.' -> not stated on the page.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accessibility/android/answer/11183305?hl=en

## tr022-d
- reasons: Search bar position and 'right away' are not on the page.
- fix requested: Change step 2 to 'Search for **Font size** in Settings.' (remove 'the search bar at the top of'), e.g. 'Tap the search icon in Settings and type **Font size**' only if you keep it generic; delete 'The change happens right away.' Keep 'A few apps ignore this setting' (page: 'The font size setting doesn't apply to some apps'). Optionally add the page's Quick Settings option: swipe down from the top, tap Font Size, use Increase or drag the slider (up to 200%).
- unsupported claims: 'Tap the search bar at the top of Settings' -> the Google page says only 'Search and select Font size'; the search bar position is not on the page. | 'The change happens right away.' -> not stated on the page.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/accessibility/android/answer/11183305?hl=en

## tr024-a
- reasons: Button location not on the page. Note: the Sounds & Haptics > Ringtone and Alerts slider appears on the cited alarm article (118444) in the alarm-volume context; it is acceptable but a general 'Change sounds and vibrations' page would be a stronger second source.
- fix requested: Change quick-way step 2 to 'Press the **volume up** button a few times. When you are not using other apps, the buttons change the ringer volume.' (remove 'on the side of the phone').
- unsupported claims: 'Press the **volume up** button on the side of the phone' -> the Apple page does not say where the buttons are; remove 'on the side of the phone'.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/105103 ; https://support.apple.com/en-us/118444

## tr024-c
- reasons: Button location not on the page; doubled lead-in ('Here's how:' then 'There are two quick ways.').
- fix requested: Change quick-way step 2 to 'Press the **volume up** button a few times. When you are not using other apps, the buttons change the ringer volume.' (remove 'on the side of the phone'). Also drop the second lead-in: keep 'Yes, you can, and that should help your son reach you.' then go straight to 'There are two quick ways. Both take less than a minute.' with no 'Here's how:' line.
- unsupported claims: 'Press the **volume up** button on the side of the phone' -> the Apple page does not say where the buttons are; remove 'on the side of the phone'.
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/105103 ; https://support.apple.com/en-us/118444

## tr024-d
- reasons: Button location not on the page.
- fix requested: Change quick-way step 2 to 'Press the **volume up** button a few times. When you are not using other apps, the buttons change the ringer volume.' (remove 'on the side of the phone').
- unsupported claims: 'Press the **volume up** button on the side of the phone' -> the Apple page does not say where the buttons are; remove 'on the side of the phone'.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/105103 ; https://support.apple.com/en-us/118444

## tr025-a
- reasons: Button location not on the page.
- fix requested: Change step 1 to 'Press a **volume button**. A volume panel appears on the screen.' only if the panel is on the page; otherwise 'Press a **volume button**.' (remove 'either' and 'on the side of your phone'). Keep step 2 (the **More** icon, which is the Menu icon labeled More, at the right) and step 3 (**Ring Volume** slider; match the page's capital V). Keep the older-phone note but say 'On older versions of Android, tap the **down arrow** and use the **Ring** slider.'
- unsupported claims: 'Press either **volume button** on the side of your phone.' -> the Google page says 'Press a volume button'; 'on the side of your phone' is not on the page.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9082609?hl=en

## tr025-c
- reasons: The user already gave device (Android) and topic (ringer volume). The steps are the same to make the ringer louder or quieter (move the Ring Volume slider), so the louder/quieter question does not change the steps; asking first is a 0 on ask_or_answer.
- fix requested: Make this a direct answer: 'Press a volume button, tap the More icon at the right of the volume panel, then slide the Ring Volume slider right for louder or left for quieter.' as numbered steps from https://support.google.com/android/answer/9082609, with the older-Android alternative (tap the down arrow, choose Ring, adjust its slider). Relabel the scenario as direct_messy/incomplete, not missing_info. Or, if the writer prefers a missing_info example, change the user message so a needed detail is actually missing (for example 'the ringing on my phone is too quiet' with no device named).
- required actions missing from the reply: Press a volume button (critical) | Tap the Menu icon labeled More at the right of the volume panel (critical, Android 12 and up) | Slide the Ring Volume slider (critical) | Older Android: tap the Down arrow, choose Ring and adjust its slider
- low scores: {'ask_or_answer': 0} | gates not passed: {}
- sources: https://support.google.com/android/answer/9082609?hl=en

## tr025-d
- reasons: Button location not on the page.
- fix requested: Change step 1 to 'Press a **volume button**. A volume panel appears on the screen.' only if the panel is on the page; otherwise 'Press a **volume button**.' (remove 'either' and 'on the side of your phone'). Keep step 2 (the **More** icon, which is the Menu icon labeled More, at the right) and step 3 (**Ring Volume** slider; match the page's capital V). Keep the older-phone note but say 'On older versions of Android, tap the **down arrow** and use the **Ring** slider.'
- unsupported claims: 'Press either **volume button** on the side of your phone.' -> the Google page says 'Press a volume button'; 'on the side of your phone' is not on the page. | 'Samsung screens can look a little different, so I've included what to look for.' -> acceptable hedge, but the page is Google's generic Android help and says nothing about Samsung; keep it only as a general hedge.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9082609?hl=en

## tr026-a
- reasons: Missing the carrier-must-offer-it requirement; status bar claim does not match the page (Control Center).
- fix requested: Replace the last paragraph's status-bar sentence with: 'To check, open Control Center. If Wi-Fi Calling is available, you'll see **Wi-Fi** in the status bar there.' Add one plain sentence that Wi-Fi Calling only works if your phone company offers it, and change the last line to: 'If you don't see **Wi-Fi Calling** in that menu, your phone company may not offer it. Tell me what you see, and you can also ask your phone company.' (page: 'verify that your carrier offers Wi-Fi Calling and that your devices have the latest software').
- unsupported claims: 'you'll see **Wi-Fi** in the status bar at the top of the screen' -> the Apple page says 'you'll see Wi-Fi in the status bar while viewing Control Center', not on the normal top bar.
- required actions missing from the reply: Carrier must offer Wi-Fi Calling (verify with carrier) | Wi-Fi appears in the status bar when viewing Control Center
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108066

## tr026-b
- reasons: Asks two questions in one sentence (Wi-Fi at home, and iPhone or Android). Only the device changes the steps.
- fix requested: Reply with ONE short question, e.g. 'That's frustrating. Is your phone an **iPhone** or an Android phone?' Drop the Wi-Fi-at-home question (it can come up after the device is known) and keep the sentence short.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/108066

## tr026-c
- reasons: Missing carrier requirement; status bar claim does not match the page; the lead-in 'Since you already know what you're looking for, here are the exact steps:' is followed by an explanation of what Wi-Fi Calling is, which the user already said they read about (extra text).
- fix requested: Replace the last paragraph's status-bar sentence with: 'To check, open Control Center. If Wi-Fi Calling is available, you'll see **Wi-Fi** in the status bar there.' Add one plain sentence that Wi-Fi Calling only works if your phone company offers it, and change the last line to: 'If you don't see **Wi-Fi Calling** in that menu, your phone company may not offer it. Tell me what you see, and you can also ask your phone company.' (page: 'verify that your carrier offers Wi-Fi Calling and that your devices have the latest software'). Also delete the line 'Since you already know what you're looking for, here are the exact steps:' and the sentence 'iPhone has a feature called Wi-Fi Calling that uses your Wi-Fi...'; start with 'It's in Settings.' then the numbered steps. Page says it is for 'an area with little or no cellular coverage' with a Wi-Fi connection.
- unsupported claims: 'you'll see **Wi-Fi** in the status bar at the top of the screen' -> the Apple page says 'you'll see Wi-Fi in the status bar while viewing Control Center', not on the normal top bar.
- required actions missing from the reply: Carrier must offer Wi-Fi Calling (verify with carrier) | Wi-Fi appears in the status bar when viewing Control Center
- low scores: {'steps': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108066

## tr026-d
- reasons: Missing carrier requirement; status bar claim does not match the page. (Style note: the earlier assistant turn asks two questions; context only.)
- fix requested: Replace the last paragraph's status-bar sentence with: 'To check, open Control Center. If Wi-Fi Calling is available, you'll see **Wi-Fi** in the status bar there.' Add one plain sentence that Wi-Fi Calling only works if your phone company offers it, and change the last line to: 'If you don't see **Wi-Fi Calling** in that menu, your phone company may not offer it. Tell me what you see, and you can also ask your phone company.' (page: 'verify that your carrier offers Wi-Fi Calling and that your devices have the latest software'). In the follow-up the earlier turn should ask only the device question.
- unsupported claims: 'you'll see **Wi-Fi** in the status bar at the top of the screen' -> the Apple page says 'you'll see Wi-Fi in the status bar while viewing Control Center', not on the normal top bar.
- required actions missing from the reply: Carrier must offer Wi-Fi Calling (verify with carrier) | Wi-Fi appears in the status bar when viewing Control Center
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108066

## tr027-d
- reasons: Final reply stacks two lead-ins ('Thanks. On Android phones like your Motorola:' then 'Here's how to take a picture of your screen.'), which is a plain-language problem.
- fix requested: Use one lead-in only, e.g. 'Thanks. Here's how to take a picture of your screen on your Motorola. It only takes a second.' then the numbered steps; delete the line 'On Android phones like your Motorola:'. Keep the rest unchanged.
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/9075928?hl=en

## tr030-a
- reasons: Step 5 bundles typing the password with a vague unsupported 'confirm'; no cue for what the user sees when connected.
- fix requested: Change step 5 to 'If it asks for a password, type it.' (delete 'then confirm', or add the exact on-screen button only if a Google page you cite names it). Add what the user will see when it works: the network is labeled **Saved**. Optionally note that some steps work only on Android 12 and up.
- unsupported claims: '5. Type your Wi-Fi password when asked, then confirm.' -> the Google page only says 'Tap a listed network' and that password networks show a lock icon; it describes no password prompt and no 'confirm' action, so 'then confirm' is vague and unsupported.
- required actions missing from the reply: Some steps work only on Android 12 and up
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9075847?hl=en

## tr030-c
- reasons: Step 5 issue as above; opening stacks two lead-ins ('That sticker has everything you need...' then 'Here's how. Have your Wi-Fi password ready.').
- fix requested: Change step 5 to 'If it asks for a password, type it.' (delete 'then confirm', or add the exact on-screen button only if a Google page you cite names it). Add what the user will see when it works: the network is labeled **Saved**. Optionally note that some steps work only on Android 12 and up. Also use one lead-in: 'The sticker on your router has what you need: the network name HOME-4G7K and the password.' then the steps; delete 'Here's how. Have your Wi-Fi password ready.' and the reference to step numbers ('In step 4... in step 5'); put the name HOME-4G7K inside step 4 and 'the password from the sticker' inside step 5.
- unsupported claims: '5. Type your Wi-Fi password when asked, then confirm.' -> the Google page only says 'Tap a listed network' and that password networks show a lock icon; it describes no password prompt and no 'confirm' action, so 'then confirm' is vague and unsupported.
- required actions missing from the reply: Some steps work only on Android 12 and up
- low scores: {'actionable': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9075847?hl=en

## tr030-d
- reasons: Step 5 issue as above; the reply says 'Have your Wi-Fi password nearby' and then 'Here's how. Have your Wi-Fi password ready.' (pasted twice).
- fix requested: Change step 5 to 'If it asks for a password, type it.' (delete 'then confirm', or add the exact on-screen button only if a Google page you cite names it). Add what the user will see when it works: the network is labeled **Saved**. Optionally note that some steps work only on Android 12 and up. Keep only one 'have your Wi-Fi password ready' sentence. (Style note: the earlier turn is fine.)
- unsupported claims: '5. Type your Wi-Fi password when asked, then confirm.' -> the Google page only says 'Tap a listed network' and that password networks show a lock icon; it describes no password prompt and no 'confirm' action, so 'then confirm' is vague and unsupported.
- required actions missing from the reply: Some steps work only on Android 12 and up
- low scores: {'actionable': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9075847?hl=en

## tr031-b
- reasons: Asks two questions (Windows or Mac; Wi-Fi or cable) in one sentence.
- fix requested: Ask ONE short question: 'I can help. Is your computer a **Windows** computer or a **Mac**?' Leave the Wi-Fi-or-cable question for later, since Wi-Fi can be assumed from the task.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows

## tr031-c
- reasons: Asks two questions ('What won't your laptop connect to...?' and 'is it a Windows laptop or a Mac?').
- fix requested: Ask ONE short question: 'It looks like your message got cut off. What won't your laptop connect to: the **Wi-Fi**, a **printer**, or something else?' Drop the Windows-or-Mac question.
- low scores: {'ask_or_answer': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows

## tr031-d
- reasons: Taskbar position is not on the page. The 'Refresh network list' tip is present but without 'lower right' (fine). (Style note: earlier turn asks two questions; context only.)
- fix requested: In step 1 delete 'at the bottom right of the screen' so it reads 'On the taskbar, click the **network, sound, or battery icons**.' Keep 'in the lower right of the panel' for **Refresh network list**, which the page does say ('in the lower right').
- unsupported claims: 'On the taskbar at the bottom right of the screen' -> the Microsoft page says only 'Select the Network, Sound, or Battery icons on the taskbar'; it does not say bottom right.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows
