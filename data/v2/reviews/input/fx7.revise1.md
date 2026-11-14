# Revision list: batch fx7, after review round 1 (6 examples)

Edit ONLY these examples in data/v2/specs/fx7.py, then rebuild.

## tr091-e
- reasons: Invented icon description (three dots); step 6 is vague and the reply never makes sure the pharmacy comes before the sister's address, which is the user's stated goal.
- fix requested: In step 5 write: 'At the top right, tap **More**, then tap **Edit stops**.' Delete '(the three dots)'. Replace step 6 with a plain step 'Add the pharmacy as a stop (you can add up to 9 stops including the final destination).' Add a step before Done: 'If the pharmacy is listed after your sister's house, press and hold the **Reorder** icon next to it and drag it above.' Keep Done and the blue/gray note.
- unsupported claims: Tap **More** (the three dots) -> the page only names the control 'More' (alt text 'More'); it never says three dots | 6. Add the pharmacy as a stop. -> page gives no how-to beyond 'Add stops'; no explanation of order, although the user wants the pharmacy BEFORE the sister's house (page: press and hold the Reorder icon and drag)
- required actions missing from the reply: Reorder stops by holding the Reorder icon and dragging if needed
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

## tr093-r
- reasons: Step 1 tells a low-confidence user to 'check whether the plug-in is turned on in your browser' with no starting point or what they will see; the cited page itself links to the enabling steps.
- fix requested: Add as a second source the Zoom article the page links for enabling the launcher plug-in: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0070429 and write the concrete steps for enabling the plug-in from it (one action per step, say where to click and what they will see). Optionally, if the user still cannot get in, point to https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0060732 (additional ways to join a meeting). Keep the Safari note.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180

## tr099-e
- reasons: The cited page does not mention Charge Now; the steps are right but need the correct source. One sentence is unsupported.
- fix requested: Add https://support.apple.com/en-ca/108055 as the source for the Charge Now steps (page says: 'If you need to have your iPhone fully charged sooner, touch and hold the notification and then tap Charge Now.'). Delete the sentence 'Optimized Battery Charging stays on for other days.' Optionally add: if there is no such notification, an iPhone 15 or later may have a charge limit set under Settings > Battery > Charging.
- unsupported claims: Touch and hold the notification from Optimized Battery Charging... Tap Charge Now -> not on the cited page https://support.apple.com/en-ca/108805 (it is on https://support.apple.com/en-ca/108055) | Optimized Battery Charging stays on for other days. -> not stated on either page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-ca/108805

## tr099-r
- reasons: Final reply sends the user to set a limit below 100%, which would keep the phone stopping early, the opposite of what they want. Wear warning from the earlier turn was dropped for the iPhone 15 path.
- fix requested: Cite https://support.apple.com/en-ca/108055 as well. Rewrite the final reply for an iPhone 15: 1) Settings, tap Battery. 2) Tap Charging. 3) On the slider, if the limit is below 100%, move it to 100% so the phone can charge fully (page: you can choose a limit between 80 and 100 percent in 5 percent steps). Then explain in one plain sentence that at 100% Optimized Battery Charging may still hold at 80% on some nights, and that turning off charging optimizations can wear the battery faster. Keep the one-day option: touch and hold the Lock Screen notification and tap Charge Now. Remove the 'set it below 100% to turn it off' advice.
- unsupported claims: Choose an option on the slider for the charge limit... set it **below 100%** to turn it off. -> this contradicts the user's goal: a limit below 100% makes the iPhone stop charging at that limit; the page says to change the limit to charge past 80 percent | Charge Now / Charging menu steps -> not on cited page 108805 (they are on https://support.apple.com/en-ca/108055)
- required actions missing from the reply: Charge limit slider from 80 to 100 percent; to charge past 80 percent change the limit (critical) | Turning off optimizations can increase battery wear
- low scores: {'steps': 0, 'constraints': 1, 'actionable': 1, 'plain': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-ca/108805

## tr103-e
- reasons: Missing the Alarms permission step (Settings > Apps > Reminders > Alarms), which a heart-pill reminder depends on; iCloud Reminders prerequisite is tacked on at the end instead of before the steps; no way to check iOS version.
- fix requested: Put the requirements before the steps: 'This needs iOS 26.2 or later and iCloud Reminders turned on.' After the Urgent step add: 'Then open Settings, tap Apps, tap Reminders, and under Allow Reminders to Access turn on Alarms.' Add: 'Urgent alarms only sound on the iPhone that Find My uses as your location.' Say 'tap the reminder, then tap Info' as the page does.
- required actions missing from the reply: Allow alarms: Settings > Apps > Reminders > turn on Alarms under Allow Reminders to Access (critical) | Alarms only sound on the device Find My uses as your location
- low scores: {'steps': 0, 'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102484

## tr103-r
- reasons: The My Card tip is stated more broadly than the page supports.
- fix requested: Change the last paragraph to match the page: 'If you set the reminder by asking Siri for your home or work, your address must be on My Card: open Contacts, tap My Card, tap Edit, add the address, and tap Done.' Or remove it.
- unsupported claims: If you picked your home or work, also make sure that address is on your card. -> the page ties the My Card home/work address to Siri location reminders only; the user set it up in the Reminders app
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.apple.com/en-us/102484
