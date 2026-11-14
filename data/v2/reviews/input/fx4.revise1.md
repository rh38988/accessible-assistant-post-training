# Revision list: batch fx4, after review round 1 (4 examples)

Edit ONLY these examples in data/v2/specs/fx4.py, then rebuild.

## tr050-r
- reasons: Reply says only 'Get the battery checked' with no place to do it; the page says to get service through Apple's support site. 'Your phone is not broken just because of this message' is also not on the page.
- fix requested: Rewrite step 2 as one concrete action: 'Get service for the battery through Apple Support (Apple's support website)', matching the page ('To have the battery checked, get service through Apple's support site'). Optionally mention Apple's guidance page on genuine iPhone batteries. Delete the sentence 'Your phone is not broken just because of this message.' (not on the page) or replace with the page's wording that details from this battery may not be accurate.
- unsupported claims: 'Your phone is not broken just because of this message.' -> not stated on the page
- required actions missing from the reply: Get the battery checked through Apple's support site (critical)
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/101575

## tr051-r
- reasons: Last line 'Once your plan supports it, MMS Messaging can be turned on in Settings, then Messages' is an inference; the page only says to contact the provider to confirm whether group MMS is included. It also does not acknowledge the cousin who did not get the message.
- fix requested: Delete the sentence 'Once your plan supports it, **MMS Messaging** can be turned on in **Settings**, then **Messages**.' Keep the two carrier steps, matching the page: 'If you don't see an option to turn on MMS Messaging, contact your mobile provider to confirm whether group MMS is included in your plan.'
- unsupported claims: 'Once your plan supports it, MMS Messaging can be turned on in Settings, then Messages.' -> page does not say the option appears after the plan supports it
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/118236

## tr056-r
- reasons: Step 2 bundles a cause, a settings name and a setting change with no starting point on the screen, so a low-confidence user cannot find it. The cited page itself gives no Settings path.
- fix requested: Split step 2 into short steps. Keep step 1 as is. Then say: 'If it still doesn't appear, Content & Privacy Restrictions may be turned on.' Add a second source https://support.apple.com/en-us/105121 (linked from the cited page as 'Adjust your iTunes & App Store Purchases settings') and give its path with its exact labels, e.g. 'Open Settings, tap Family, tap the name of the person (that page's wording), tap Content & Privacy Restrictions, ... Apps & Websites > App Store > Installing Apps > Allowed' (use only what 105121 says). If the writer cannot verify a path for an adult's own phone, instead say 'Adjust your iTunes & App Store Purchases settings so Installing Apps is set to Allow. If you did not set this up, ask the person who manages your phone.' End with 'The App Store should reappear on your device.'
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102590

## tr057-r
- reasons: G2 caution: step 2 'If you do want this paid app, tap the price' nudges a low-confidence user toward starting a purchase with no warning that it costs money.
- fix requested: Keep step 1. Replace step 2 with: 'Tapping the price is how you buy the app, so only tap it if you mean to pay for it.' (The page says to tap Install for no-charge apps or the app's price for paid apps.) Do not suggest buying.
- low scores: {} | gates not passed: {'safety': 'fail'}
- sources: https://support.google.com/android/answer/9457058?hl=en
