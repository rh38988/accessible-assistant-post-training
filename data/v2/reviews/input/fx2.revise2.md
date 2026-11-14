# Revision list: batch fx2, after review round 2 (4 examples)

Edit ONLY these examples in data/v2/specs/fx2.py, then rebuild.

## tr016-e
- reasons: One sentence is not on the cited page (urgency or pressure claim). Everything else is supported and the protective action comes first.
- fix requested: Delete the sentence 'Tickets going fast is the kind of pressure scammers use.' Optionally keep the opening as: 'A seller who says you can only pay with a payment app is probably a scammer.' (the page says anyone who says you can only pay in one of these ways is probably a scammer). Do not add other claims about urgency.
- unsupported claims: 'Tickets going fast is the kind of pressure scammers use.' -> the FTC page says nothing about pressure or urgency tactics; its only time-related advice is 'Don't delay if you paid a scammer.'
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay

## tr024-r
- reasons: The user already described an orange mark on the side, so the switch applies. The last paragraph ('If you have an iPhone 15 Pro or a newer model, there is no switch. The Action button toggles Silent mode...') is about other models and gives no way to use the Action button (the page gives no gesture). It adds clutter for a low-confidence user. The page also never says outright that newer models 'have no switch'. The favorites line is not needed for this fix.
- fix requested: Delete the final paragraph about iPhone 15 Pro, newer models and favorite contacts. Keep steps 1 to 3 and the first sentence about orange meaning Silent mode.
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/105103

## tr026-r
- reasons: The page's last troubleshooting step (Reset Network Settings) is missing. Step 1 bundles two separate checks (carrier support and software update) with no way to do either.
- fix requested: Split step 1 into: 'Make sure your carrier offers Wi-Fi Calling (the carrier can confirm).' and 'Make sure your iPhone has the latest software.' Add a step after 'turn off, then on': 'Open Settings, tap General, tap Transfer or Reset iPhone, tap Reset, then tap Reset Network Settings.' (Do not add warnings about what it erases; the page gives none. Optionally say it is the last thing to try.) Keep the two-minute wait and the carrier line.
- required actions missing from the reply: Settings > General > Transfer or Reset iPhone > Reset > Reset Network Settings
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/108066

## tr030-r
- reasons: The page says to wait for the list to refresh first if the network should be in range. The reply goes straight to Add network when the user says her network is not listed.
- fix requested: Before the current step 1, add a step: 'Wait a few seconds for the list of networks to refresh. If her network still is not listed, it may be hidden.' Then continue with the existing steps (Add network, name and password, Hidden Network, Save). Keep 'Ask her for the network name and the password.'
- required actions missing from the reply: If the network should be nearby, wait for the list to refresh
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/9075847?hl=en
