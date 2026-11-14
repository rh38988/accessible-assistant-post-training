# Revision list: batch ex2, after review round 2 (11 examples)

Edit ONLY these examples in data/v2/specs/ex2.py, then rebuild.

## pilot-014
- reasons: The 'read out any numbers' instruction is not on the cited page, and the report address differs from the one the cited article gives.
- fix requested: Step 1 becomes: "Don't buy anything right away. Resist the urge to act immediately, no matter how dramatic the story may be." Delete "and don't read out any numbers, however upsetting the story is". In the closing line, replace "ReportFraud.ftc.gov" with "www.ftc.gov/complaint". Keep steps 2 and 3 and the other lines.
- unsupported claims: 'Don't buy anything and don't read out any numbers, however upsetting the story is' -> 'resist the urge to act immediately' supports 'don't buy anything'; 'don't read out any numbers' is not on the page, which gives no guidance on sharing codes or card numbers. | 'you can report it at ReportFraud.ftc.gov' -> this address appears only in the site menu; the article's own reporting instruction gives www.ftc.gov/complaint.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://www.ftc.gov/node/54353 ; https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay

## pilot-015
- reasons: Two sentences go beyond the cited FTC page: the 'just ignore it' fallback and the 'call right away / tell them what happened' instruction for a code already sent.
- fix requested: Step 2 becomes: "Block their number and stop texting them." (delete the 'If not, just ignore it' sentence). In the closing paragraph, replace "call your bank right away using a phone number from your bank statement or your bank's app and tell them what happened" with "contact your bank using a phone number from your bank statement or your bank's app". Keep steps 1, 3 and 4.
- unsupported claims: 'Block the number if you know how. If not, just ignore it.' -> the page says 'Block their number. Stop texting them.' It does not say to ignore the text. | 'If you already sent the code, call your bank right away ... and tell them what happened.' -> the page says to contact the bank using a number you trust, but it does not say 'right away' or to tell the bank what happened, and it does not address a code already shared.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/node/84809

## pilot-016
- reasons: The instruction to call the card company is not on the cited article; the letter rule is supported.
- fix requested: In step 1, delete "Call your card company right away, and" so the sentence reads: "If a charge is wrong, you can dispute it. Send a letter so it reaches your card company within 60 days of the date the first bill showing the error was mailed." Optionally change "the connection is private" in step 3 to "the connection is encrypted" to match the page. Keep the rest.
- unsupported claims: 'Call your card company right away, and send a letter so it reaches them within 60 days' -> the 60-day letter rule is on the page, but the page does not tell the user to call the card company.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay ; https://consumer.ftc.gov/articles/online-shopping

## pilot-017
- reasons: source unreadable: https://www.facebook.com/help/120939471321735 failed with robots_disallowed on two WebFetch tries, so the audience steps could not be checked. The clarifying question itself is appropriate.
- fix requested: No change to the question is requested. Re-review this example once the Facebook help page can be read, or add a second official Meta or Facebook help page on audience settings as a source. Confirm that the later steps (phone app and computer, with exact audience labels) are supported before keeping it.
- low scores: {} | gates not passed: {'source': 'unverified'}
- sources: https://www.facebook.com/help/120939471321735

## tr024-a
- reasons: The Settings path is cited to an alarm-volume article, so the claim that the Ringtone and Alerts slider changes ringer volume is not supported. The Quick way is supported by https://support.apple.com/en-us/105103.
- fix requested: Keep the Quick way block. For the Settings block, either (a) add a second official Apple page that describes ringtone or ringer volume under Sounds & Haptics and cite it, or (b) delete the whole 'In Settings' block (its heading and steps 1 to 3) and keep the rest. The Silent mode sentence is supported by https://support.apple.com/en-us/105103 and may stay.
- unsupported claims: 'In Settings: Open the Settings app. Tap Sounds & Haptics. Under Ringtone and Alerts, drag the slider to the right.' -> the Sounds & Haptics and Ringtone and Alerts labels appear on https://support.apple.com/en-us/118444, but that page describes alarm volume, not ringer volume. Nothing cited says this slider makes the ringer louder.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/105103 ; https://support.apple.com/en-us/118444

## tr024-c
- reasons: Same source problem as tr024-a: the Settings block is cited to an alarm-volume article.
- fix requested: Apply the same fix as tr024-a: keep the Quick way block and either cite a second official Apple page on ringtone or ringer volume for the Settings block, or delete the 'In Settings' block (heading and steps 1 to 3). The opening line 'Yes, you can, and that should help your son reach you.' may stay.
- unsupported claims: 'In Settings: ... Under Ringtone and Alerts, drag the slider to the right.' -> https://support.apple.com/en-us/118444 describes this slider for alarm volume only, not ringer volume.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/105103 ; https://support.apple.com/en-us/118444

## tr024-d
- reasons: Same source problem as tr024-a: the Settings block is cited to an alarm-volume article.
- fix requested: Apply the same fix as tr024-a: keep the Quick way block and either cite a second official Apple page on ringtone or ringer volume for the Settings block, or delete the 'In Settings' block (heading and steps 1 to 3).
- unsupported claims: 'In Settings: ... Under Ringtone and Alerts, drag the slider to the right.' -> https://support.apple.com/en-us/118444 describes this slider for alarm volume only, not ringer volume.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/105103 ; https://support.apple.com/en-us/118444

## tr025-d
- reasons: The Samsung claim is not on the cited page. The steps themselves are supported.
- fix requested: Replace "Samsung screens can look a little different, so I've included what to look for." with "Phone screens can look a little different, so here is what to look for." Keep the rest of the reply unchanged.
- unsupported claims: 'Samsung screens can look a little different, so I've included what to look for.' -> https://support.google.com/android/answer/9082609?hl=en does not mention Samsung. The brand claim is not on the page.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9082609?hl=en

## tr026-a
- reasons: The condition for using Wi-Fi Calling is stated more broadly than the page allows (weak signal versus little or no cellular coverage). Steps are supported.
- fix requested: Change the opening sentence to: "iPhone has a feature called Wi-Fi Calling that lets you make or receive calls over Wi-Fi when there is little or no cellular coverage." Keep the rest.
- unsupported claims: 'uses your Wi-Fi for calls when the cell signal is weak' -> https://support.apple.com/en-us/108066 describes use 'in an area with little or no cellular coverage'. It does not say weak signal.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108066

## tr026-d
- reasons: Same unsupported 'weak signal' condition as tr026-a.
- fix requested: Change the sentence after "Thanks. This should help." to: "iPhone has a feature called Wi-Fi Calling that lets you make or receive calls over Wi-Fi when there is little or no cellular coverage." Keep the rest.
- unsupported claims: 'uses your Wi-Fi for calls when the cell signal is weak' -> https://support.apple.com/en-us/108066 describes use 'in an area with little or no cellular coverage'. It does not say weak signal.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108066

## tr027-d
- reasons: The Gallery path uses labels the page does not use ('Screenshots album' in place of 'Album view' then 'Screenshots folder'). The Gallery alternative is therefore not usable as written.
- fix requested: Replace "If your phone uses a Gallery app instead, look for the Screenshots album there." with "If your phone uses a Gallery app instead, open it, tap Album view, then tap Screenshots folder." Keep the rest, which matches https://support.google.com/android/answer/9075928?hl=en.
- unsupported claims: 'If your phone uses a Gallery app instead, look for the Screenshots album there.' -> https://support.google.com/android/answer/9075928?hl=en says 'Open your phone's Gallery app and tap Album view' and then 'Screenshots folder'. 'Screenshots album' and the missing 'Album view' step are not the page's labels.
- required actions missing from the reply: Gallery app alternative: Album view, then Screenshots folder
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9075928?hl=en
