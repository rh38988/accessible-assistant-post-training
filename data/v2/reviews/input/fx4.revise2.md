# Revision list: batch fx4, after review round 2 (3 examples)

Edit ONLY these examples in data/v2/specs/fx4.py, then rebuild.

## tr050-r
- reasons: Step 2 'Get service for the battery through Apple Support, Apple's support website, to have it checked' is garbled and gives no clear starting point; the page's wording is 'To have your battery checked, get service' linking to getsupport.apple.com. Step 1 'Don't rely on the numbers shown there' is not an action.
- fix requested: Replace the two steps with one clear action: '1. To have the battery checked, go to **getsupport.apple.com** and choose the battery service option (this is the 'get service' link on Apple's battery page).' Drop the phrase 'Apple Support, Apple's support website'. Keep the opening explanation that the numbers on that screen may not be accurate. Source: https://support.apple.com/en-us/101575 (link: https://getsupport.apple.com/?caller=kbase&PRKEYS=PF9&category_id=SC0999&symptom_id=23306).
- low scores: {'actionable': 1, 'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/101575

## tr051-r
- reasons: 'group MMS' is used unexplained in the final reply and the carrier action has no 'what you will hear' cue; the reply is terse for an anxious user who just saw nothing arrive for the Android cousin.
- fix requested: Reword the final reply in plain words, e.g. 'That setting is needed to send group messages to a phone that is not an iPhone. If your iPhone does not show it, your phone company has to turn it on. 1. Call or contact your phone carrier. 2. Ask: 'Does my plan support Group MMS Messaging?' (that is the name for group picture-and-text messages to non-iPhones).' Keep it short. Source: https://support.apple.com/en-us/118236 ('If you don't see an option to turn on MMS Messaging, contact your carrier').
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/118236

## tr056-r
- reasons: Step 3 'Adjust your iTunes & App Store Purchases settings' gives no starting point (where to open it); the cited page gives no Settings path and its linked article no longer uses these labels. Order is also reversed from the page (page: restrictions first, then Spotlight).
- fix requested: Fetch Apple's current Screen Time guide for blocking/allowing app installs (e.g. https://support.apple.com/guide/iphone/block-apps-app-downloads-websites-purchases-iph3ff83f3b1/ios, section on preventing app installs) and add it as a second source; then write the exact Settings path (Settings > Screen Time > Content & Privacy Restrictions > ... > Installing Apps > Allow) only if that page shows it, one action per step, in the page's order (restrictions check first, Spotlight search as the fallback). If the path cannot be confirmed, reject this example. Remove or soften 'ask the person who manages your phone'.
- unsupported claims: "If you did not set this up, ask the person who manages your phone." -> not on the page (harmless general advice, but unsupported)
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102590
