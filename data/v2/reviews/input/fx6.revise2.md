# Revision list: batch fx6, after review round 2 (6 examples)

Edit ONLY these examples in data/v2/specs/fx6.py, then rebuild.

## tr076-e
- reasons: Only unsupported text is the position phrase in step 3. The earlier 'newer models' claim is fixed. Step 1 (Camera from the Lock Screen) is supported; the page does not say how to wake a sleeping screen, so do not add a wake method.
- fix requested: Step 3 becomes: '3. Tap the **link**.' (delete 'that appears over the code'). Keep step 1 and the Control Center and Camera Control paragraph as written. Keep the last line 'The link or content from the code will open.' Do not add any way to wake the screen.
- unsupported claims: 'Tap the **link** that appears over the code.' -> page says only 'tap the link to open the content'; 'appears over the code' is a position detail the page does not give.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102680

## tr079-r
- reasons: One unsupported claim ('someone else'). All other items match the page: the name 'Personal Safety' in Play Store and Settings, disabling, the device note, and the Android 12-and-earlier wording.
- fix requested: In item 2 of the final reply, change 'If you or someone else turned the app off (disabled it), it will not show in your app list.' to 'If the app has been turned off (disabled), it will not show in your app list.' Leave the other three items unchanged.
- unsupported claims: 'If you or someone else turned the app off (disabled it)' -> page says the app can be disabled and then leaves the app list; it does not say anyone else turns it off. Remove 'or someone else'.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9319337?hl=en

## tr083-e
- reasons: Search is on the page but partial-name matching is not. Steps 1 and 2 and the Downloads note are supported.
- fix requested: Step 3 becomes: '3. In **Home**, search for the file by the name you remember.' Delete 'the part of the name you remember, such as **W2**' and the sentence 'Matching files on your PC will be listed.' Replace the last with: 'The search looks for relevant files on your PC and in your cloud accounts.' Keep the Downloads paragraph as written. Do not claim partial-name matching.
- unsupported claims: 'search for the part of the name you remember, such as **W2**' -> page says only to search from File Explorer Home to find relevant files on the PC and in the cloud; it never says partial-name matching or that W2 would match. | 'Matching files on your PC will be listed.' -> page says search finds relevant files from your PC and the cloud; it does not describe a list of matching names. Cloud results are omitted, which is incomplete rather than wrong.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8

## tr086-e
- reasons: Step 1 gives a delaying instruction the page does not support, which conflicts with the report-and-delete advice. The Monday step ignores the website option the page gives. The 'don't click' opening, the ReportFraud and reportphishing steps, and the delete step are supported.
- fix requested: Replace step 1 with: '1. Do not click anything in the email. Report it now, as in step 3.' Change step 2 to: '2. To check your streaming account, go to the company's website or app that you already know is real, or use a phone number you already know is real. You do not need to wait until Monday to use the website.' Keep the steps for forwarding, reporting, and deleting, and the final line about links and attachments. Do not say 'you don't have to do anything today'.
- unsupported claims: 'Leave the email alone for now. You don't have to do anything about it today.' -> page says to report the message and then delete it; it sets no wait and never says nothing needs doing today. Telling a user with a stated 24-hour deadline that nothing is needed today delays the protective step. | 'On Monday, if you want to check your account, contact the company' -> page says to contact the company using a phone number or website you know is real; it does not say to wait until Monday. The user can use the company's real website now (the user's only limit is phone calls).
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams

## tr086-r
- reasons: Step 3 bundles three actions and gives them a trigger the page does not support. The credit card, refund, and reporting steps are supported. IdentityTheft.gov is on the page, but the page ties it to Social Security numbers; the reply's 'based on what information you gave away' is a fair paraphrase, so it is kept as is.
- fix requested: Replace step 3 with: '3. If you think the scammer may have had access to your computer or phone, update your security software to make sure you have the latest protections. Then run a scan and delete anything it identifies as a problem.' Keep the other steps. Do not say that clicking a link triggers these steps.
- unsupported claims: 'Because you clicked a link, update your security software, run a scan, and remove anything it flags.' -> page scopes these steps to a scammer who gained access to the computer or phone ("If you gave a scammer access to your computer or phone"); it says nothing about clicking a link triggering them. Also 'remove anything it flags' is a paraphrase of 'delete anything it identifies as a problem'.
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams ; https://consumer.ftc.gov/articles/what-do-if-you-were-scammed

## tr088-e
- reasons: Step 1 is not in the source (G1). The phrase 'reverse image search' is unexplained jargon for a low-confidence user (S5). Everything else matches the page: never send money or gifts, the moving-off-platform and visa signs, talking to someone you trust, ReportFraud.ftc.gov, and telling the site.
- fix requested: Delete step 1 'Stop communicating with him right away.' and renumber the remaining steps 1 to 3. In the new step 3, change 'Do a reverse image search on his profile photo to see if it is linked to other names.' to 'Do a reverse image search on his profile photo. This is a search tool that shows where else the same photo appears online; if it appears under other names, that is a sign of a scam.' Keep the other wording.
- unsupported claims: '1. Stop communicating with him right away.' -> not on the page; the page gives signs of a romance scam and advice about money and trusted people, not a rule to stop contact. This step is added from general knowledge.
- low scores: {'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/what-know-about-romance-scams
