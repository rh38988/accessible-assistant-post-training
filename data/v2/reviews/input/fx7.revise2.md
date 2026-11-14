# Revision list: batch fx7, after review round 2 (4 examples)

Edit ONLY these examples in data/v2/specs/fx7.py, then rebuild.

## tr091-e
- reasons: Step 6 says 'Add the pharmacy as a stop' but never says how to find and select it. The page only says to search for places along the route and does not name an 'Add stop' button. Every other claim matches the page.
- fix requested: Replace step 6 with: 'Search for the pharmacy by name and tap it to add it as a stop. You can add up to 9 stops, including the final destination.' Do not name an 'Add stop' button, because the page does not use that label. Keep the rest of the reply unchanged.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

## tr099-e
- reasons: The opening sentence promises a one-day effect and no settings change. The source gives neither. The three steps match the page.
- fix requested: Replace the opening sentence with: 'You can have your iPhone charged fully sooner from the Lock Screen.' Delete 'just for today' and 'without changing any settings'. Keep steps 1 to 3 and the final line unchanged.
- unsupported claims: 'You can charge it fully just for today, without changing any settings.' -> the page says the Charge Now option gets the iPhone fully charged sooner; it does not say the option lasts one day or that it leaves settings unchanged
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-ca/108805 ; https://support.apple.com/en-ca/108055

## tr099-r
- reasons: The last paragraph limits Charge Now to one day, which the source does not say. The iPhone 15 path, the 80 to 100 percent range in 5 percent steps, and the note that optimization can still delay charging past 80 percent at 100 percent all match the page.
- fix requested: In the last paragraph, delete 'For just one day,' and change the sentence to: 'You can also touch and hold the Optimized Battery Charging notification on your Lock Screen and tap Charge Now to get your iPhone fully charged sooner.' Keep the rest of the reply unchanged.
- unsupported claims: 'For just one day, you can also touch and hold the Optimized Battery Charging notification on your Lock Screen and tap Charge Now.' -> the page gives Charge Now as a way to get the iPhone fully charged sooner; it does not say the option applies for one day
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-ca/108805 ; https://support.apple.com/en-ca/108055

## tr103-r
- reasons: The Siri paragraph states a requirement the page does not give. It is also not needed for this user, who built the reminder with the Location button and never mentioned Siri. Step 2 also skips the tap on Location Services, which the page describes.
- fix requested: Delete the paragraph that starts 'If you set the reminder by asking Siri'. In step 2, change 'Turn on Location Services.' to 'Tap Location Services, then turn it on.' Keep the rest of the reply unchanged.
- unsupported claims: 'your address must be on My Card' -> the page says adding home and work addresses to your Contacts card lets Siri help set location reminders; it does not say the address must be there
- low scores: {'actionable': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102484
