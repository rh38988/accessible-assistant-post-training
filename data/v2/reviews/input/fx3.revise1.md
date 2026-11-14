# Revision list: batch fx3, after review round 1 (5 examples)

Edit ONLY these examples in data/v2/specs/fx3.py, then rebuild.

## tr034-r
- reasons: The error-recovery steps are not on the cited page (it only refers to the 'Troubleshoot problems updating Windows' article). Those steps ARE on that Microsoft article, so the content is correct but the example cites the wrong source.
- fix requested: Add a second source: https://support.microsoft.com/en-us/windows/troubleshoot-problems-updating-windows-188c2b0f-10a7-d72f-65b8-32d177eb136c (it lists Settings > System > Troubleshoot > Other troubleshooters > Windows Update > Run, and Network & Internet > Wi-Fi to reconnect). In final-reply step 4 use the label 'Check for Windows updates' as on the install page (or 'Check for updates' only if you cite the troubleshoot article for it). Keep the rest.
- unsupported claims: 'Click Start, then Settings, then System, then Troubleshoot, then Other troubleshooters. Click Run next to Windows Update.' -> the cited page has no troubleshooter steps; it only points to other articles | 'Go to Start, Settings, Network & Internet, Wi-Fi, and reconnect if needed.' -> cited page has no network guidance | 'click Check for updates again' -> the cited page's button is 'Check for Windows updates'
- required actions missing from the reply: Run Windows Update troubleshooter (Settings > System > Troubleshoot > Other troubleshooters > Run) | Check internet connection | Check for updates again
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates

## tr039-r
- reasons: The key recovery step is accurate but is not on the cited page; it is on another FTC page.
- fix requested: Add a second source: https://consumer.ftc.gov/articles/what-do-if-you-were-scammed (wire transfer: 'Report it to the wire transfer company immediately', 'Tell them a scammer tricked you into sending money', 'Ask them to refund your money'). No change to the reply text is needed.
- unsupported claims: 'Report it to the wire transfer company immediately. Tell them a scammer tricked you, and ask for a refund.' -> not on the cited FTC family-emergency alert, which says nothing about wire companies or refunds
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes

## tr040-r
- reasons: The credit card steps are correct but are not on the cited page; they are on another FTC page.
- fix requested: Add a second source: https://consumer.ftc.gov/articles/what-do-if-you-were-scammed (credit card: 'Report it to the credit card issuer immediately', 'Use the number on the back of your card or log in to your account online or through their app', 'Ask them to refund your money'). No change to the reply text is needed.
- unsupported claims: 'Report it to the credit card issuer immediately. Call the number on the back of your card... ask for a refund.' -> not on the cited USPS text-scam alert
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam

## tr041-e
- reasons: One small wording that differs from the source advice.
- fix requested: Change the last sentence to: 'Keep a copy of the gift card and the store receipt.' Leave the rest unchanged.
- unsupported claims: 'Keep the cards and the receipt.' -> page says 'Always keep a copy of your gift card and store receipt'
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

## tr043-e
- reasons: The extra sentence about editing an existing contact is not supported.
- fix requested: Change the last paragraph to: 'If you want to add more details, such as a street address or notes, tap **Add fields** before you tap **Save**.' Remove 'open her contact and tap the field to edit it'.
- unsupported claims: 'open her contact and tap the field to edit it' -> the page has no steps for editing an existing contact; 'tap the field to edit' is only part of entering details while adding a new contact (it links to a separate Edit or delete contacts article)
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid
