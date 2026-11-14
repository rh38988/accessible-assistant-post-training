# Revision list: batch fx2, after review round 1 (9 examples)

Edit ONLY these examples in data/v2/specs/fx2.py, then rebuild.

## tr016-e
- reasons: User said they cannot use a credit card, but step 3 still leads with 'Paying by credit card is safest', which pushes the one option the user ruled out. The opening 'Please be careful' is soft for a seller who says a payment app is the only way; the page says such a seller is probably a scammer and to never send money that way. The reply does not use the 'only way' wording or the ReportFraud report step.
- fix requested: Start with 'Please don't pay this seller with Zelle.' Say that a seller who says you can only pay with a payment app is probably a scammer, and that the tickets going fast is the kind of pressure scammers use (keep this general, no new facts). Keep step 1 (never send money to anyone who says you can only pay one specific way, whatever reason they give) and step 2 (search the seller's name with review, scam, complaint). Replace step 3 with: 'The FTC suggests a credit card when possible because it lets you dispute charges. Since you can't use one, the safe choice is to skip a seller who insists on a payment app.' Add: 'You can report the seller at ReportFraud.ftc.gov.' Source: https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay. Keep the ftc.gov/scams line if wanted (the page names ftc.gov/scams).
- required actions missing from the reply: Report at ReportFraud.ftc.gov
- low scores: {'steps': 1, 'constraints': 1} | gates not passed: {}
- sources: https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay

## tr024-e
- reasons: Only issue is the button location, which the page does not state. Everything else matches the page (media vs ringer volume behavior, Silent mode vibrate).
- fix requested: In step 2 change to 'Press the **volume up** button a few times.' (drop 'on the side of the phone'). Keep everything else. Source: https://support.apple.com/en-us/105103.
- unsupported claims: 'Press the **volume up** button on the side of the phone' -> the Apple page does not say where the volume buttons are; remove the location.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/105103

## tr024-r
- reasons: The switch location ('small', 'above the volume buttons') is not on the page. The user already said they see orange on the side of the phone, so the location can be tied to that instead.
- fix requested: Step 1 should read: 'Find the **Ring/Silent switch**, where you see the orange.' Drop 'small' and 'above the volume buttons'. Keep steps 2 and 3 and the Action button paragraph. Do not add a press-and-hold instruction for the Action button; the page does not give one. Source: https://support.apple.com/en-us/105103.
- unsupported claims: 'Find the small **Ring/Silent switch** above the volume buttons.' -> the page does not say where the switch is or that it is small; the page text and image alt text give no location.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/105103

## tr025-e
- reasons: Two small unsupported details: the arrow position wording and the slide direction. The user described a slider plus a small arrow, so the reply may refer to the arrow they already see.
- fix requested: Step 2: 'At the right, tap the **Down arrow**.' Step 4: 'Slide the **Ring** level to where you want it.' (no direction). Keep the closing line about Media, Ring, and Alarm. Source: https://support.google.com/android/answer/9082609?hl=en.
- unsupported claims: 'Tap the **Down arrow** that appears next to the slider.' -> the page says only 'At the right, tap the Down arrow'; it does not say next to the slider. | 'Slide it to the right to make the ring louder.' -> the page gives no slide direction for the older-version steps.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9082609?hl=en

## tr025-r
- reasons: Final reply is right about the Down arrow and Ring, but adds a slide direction that the page does not state. Step 3 'Choose Ring' and step 4 are also described by the page only as choosing the volume type.
- fix requested: Step 4: 'Slide the **Ring** level to where you want it.' (remove 'to the right to make it louder'). Optionally add 'At the right' to step 2 ('At the right, tap the **Down arrow**.'), matching the page. Source: https://support.google.com/android/answer/9082609?hl=en.
- unsupported claims: 'Slide it to the right to make it louder.' -> the page gives no slide direction for the older-version steps.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9082609?hl=en

## tr026-r
- reasons: Order is wrong against the page and step 4 packs three actions into one. The check that Wi-Fi Calling is on in Settings > Cellular (the page's first troubleshooting step) and the wait between steps are missing.
- fix requested: Rewrite the final reply as: 'Let's try these in order.' 1. Check that your carrier offers Wi-Fi Calling and that your iPhone software is up to date. 2. Open **Settings**, tap **Cellular**, tap **Wi-Fi Calling**, and make sure **Wi-Fi Calling on This iPhone** is on. 3. Restart your iPhone. 4. Connect to a different Wi-Fi network, because some networks don't work with Wi-Fi Calling. 5. Turn Wi-Fi Calling off, then on again. Then: 'Wait about two minutes between steps. If it still won't turn on, contact your carrier.' Keep each step to one action. Source: https://support.apple.com/en-us/108066 (page also lists General > Transfer or Reset iPhone > Reset > Reset Network Settings as a last step; leave it out for simplicity or add it as step 6).
- unsupported claims: '3. If it still won't turn on, contact your carrier. 4. If your carrier can't fix it, restart your iPhone, try a different Wi-Fi network, and then turn Wi-Fi Calling off and on again.' -> the page lists restart, different Wi-Fi network, and off/on as the troubleshooting sequence, and says to contact the carrier if it still can't be turned on afterward. The reply puts the carrier before the restart and invents an 'if your carrier can't fix it' condition.
- required actions missing from the reply: Open Settings > Cellular, select the line if multiple SIMs, tap Wi-Fi Calling and make sure it is on
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/108066

## tr028-r
- reasons: The user asked how to find the picture, but step 1 says only 'Look in your Screenshots folder' with no way to open that folder. The cited Snipping Tool page does not give the path; another Microsoft page does.
- fix requested: Replace step 1 with: 'Open **File Explorer** from the taskbar.' Add step 2: 'On the left side, select the **Pictures** folder, then select **Screenshots**.' Keep the Save as step (select **Save as** in Snipping Tool, choose a location and a name, then select **Save**) as step 3 and the See More > Settings line. Add a second source: https://support.microsoft.com/en-us/windows/experience/keyboard-shortcut-for-print-screen (says: open File Explorer from the taskbar, select the Pictures folder, then Screenshots).
- required actions missing from the reply: Open the Screenshots folder (needs a starting point such as File Explorer > Pictures > Screenshots) (critical)
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots

## tr030-e
- reasons: The user says the son gave him the name and the password, but step 5 says only 'Enter the security details if asked', which does not tell him the password goes there; it also makes the step sound optional. The page says to provide the security details with the name.
- fix requested: Change step 5 to: 'Enter the security details your son gave you, including the password.' Keep all other steps and the closing Saved line. Source: https://support.google.com/android/answer/9075847?hl=en.
- low scores: {'constraints': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/9075847?hl=en

## tr030-r
- reasons: For a network that is not listed the page requires choosing Hidden Network = Yes under Advanced options (critical), and entering security details (the password). The final reply leaves both out, so the steps would not connect to a hidden network. It also starts from 'Add network' without the path and adds an unsupported 'wait a few seconds' step.
- fix requested: Rewrite the final reply: 'Her network may be hidden. Ask her for the network name and the password.' 1. Open **Settings**, tap **Network & internet**, then **Internet**. 2. Scroll to the bottom of the list and tap **Add network**. 3. Type the network name, then enter the security details (the password). 4. Tap **Advanced options**, and under **Hidden Network** select **Yes**. 5. Tap **Save**. Remove 'Wait a few seconds for the list to reload.' Source: https://support.google.com/android/answer/9075847?hl=en.
- unsupported claims: 'Wait a few seconds for the list to reload.' -> not on the page.
- required actions missing from the reply: Open Settings; tap Network & internet, then Internet | Tap Advanced options; under Hidden Network select Yes (critical)
- low scores: {'steps': 0, 'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/android/answer/9075847?hl=en
