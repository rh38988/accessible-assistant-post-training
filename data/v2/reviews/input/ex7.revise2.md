# Revision list: batch ex7, after review round 2 (10 examples)

Edit ONLY these examples in data/v2/specs/ex7.py, then rebuild.

## tr090-a
- reasons: Breach-only advice about reused passwords is given as an unconditional tip, so the page's real condition is lost.
- fix requested: Rewrite tip 2 with its breach condition, for example: "If a company tells you it lost your password in a data breach, change it right away. If you used the same or a similar password on other sites, change it there too." Do not present it as a rule for everyone. Optionally add the page's own note that text or email codes are the weakest form of two-factor and that an authenticator app or security key is better if the user has the option. The page does not say "use a different password for every account", so do not add that.
- unsupported claims: "If you used the same or a similar password on other sites, change it there too." -> the page says this only after a company reports a data breach ("If a company or website tells you it lost your password in a data breach, change your password right away... If you reused the same password, or a similar one, on other services, change it there, too"). Listed as a general tip for making a strong password it drops that condition and changes the meaning.
- required actions missing from the reply: After a breach, change the password and any reused or similar password on other services
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts

## tr090-c
- reasons: Unsupported advice added to the opening and breach-only tip stripped of its condition.
- fix requested: Replace the opening with something the page supports, for example: "Short passwords built from familiar things are easier for a hacking program to guess. A long passphrase of random words is stronger and can still be easy to remember." Delete "Since you use the same password everywhere, you should change it on every site." and "Your grandson has a good point." Then apply this fix to tip 2: Rewrite tip 2 with its breach condition, for example: "If a company tells you it lost your password in a data breach, change it right away. If you used the same or a similar password on other sites, change it there too." Do not present it as a rule for everyone. Optionally add the page's own note that text or email codes are the weakest form of two-factor and that an authenticator app or security key is better if the user has the option. The page does not say "use a different password for every account", so do not add that.
- unsupported claims: "Since you use the same password everywhere, you should change it on every site." -> the page only says to change reused passwords after a data breach; it never tells readers to change all reused passwords now. | "Your grandson has a good point." -> the page does not say that a pet name plus birthday is unsafe; it says to avoid common phrases and to use long random-word passphrases. | "If you used the same or a similar password on other sites, change it there too." -> the page says this only after a company reports a data breach ("If a company or website tells you it lost your password in a data breach, change your password right away... If you reused the same password, or a similar one, on other services, change it there, too"). Listed as a general tip for making a strong password it drops that condition and changes the meaning.
- required actions missing from the reply: After a breach, change the password and any reused or similar password on other services
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts

## tr090-d
- reasons: Same breach-condition problem in tip 2 of the final reply.
- fix requested: Rewrite tip 2 with its breach condition, for example: "If a company tells you it lost your password in a data breach, change it right away. If you used the same or a similar password on other sites, change it there too." Do not present it as a rule for everyone. Optionally add the page's own note that text or email codes are the weakest form of two-factor and that an authenticator app or security key is better if the user has the option. The page does not say "use a different password for every account", so do not add that.
- unsupported claims: "If you used the same or a similar password on other sites, change it there too." -> the page says this only after a company reports a data breach ("If a company or website tells you it lost your password in a data breach, change your password right away... If you reused the same password, or a similar one, on other services, change it there, too"). Listed as a general tip for making a strong password it drops that condition and changes the meaning.
- required actions missing from the reply: After a breach, change the password and any reused or similar password on other services
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts

## tr091-a
- reasons: Two UI details are not on the cited page.
- fix requested: Replace steps 2 and 3 with one step that matches the page: "Search for your destination, or tap it on the map." Remove "Tap the search bar" and "Tap the correct result." Renumber the rest. Keep Directions (bottom left), the modes, blue/gray routes, swipe up for the list and Preview as they are.
- unsupported claims: "Tap the search bar and type the address or name of the place." -> the page says only "Search for your destination or tap it on the map"; it never mentions a search bar. | "Tap the correct result." -> no such step on the page; it goes straight from choosing the destination to tapping Directions.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

## tr091-d
- reasons: Two UI details are not on the cited page.
- fix requested: Replace steps 2 and 3 with one step that matches the page: "Search for your destination, or tap it on the map." Remove "Tap the search bar" and "Tap the correct result." Renumber the rest. Keep Directions (bottom left), the modes, blue/gray routes, swipe up for the list and Preview as they are.
- unsupported claims: "Tap the search bar and type the address or name of the place." -> the page says only "Search for your destination or tap it on the map"; it never mentions a search bar. | "Tap the correct result." -> no such step on the page; it goes straight from choosing the destination to tapping Directions.
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

## tr102-a
- reasons: Unexplained jargon for an older user: "If TalkBack is on, use a three-finger swipe up instead." TalkBack is never explained.
- fix requested: Explain or drop the TalkBack clause. For example: "If your phone already reads aloud everything you touch (this is called TalkBack), swipe up with three fingers instead." Also say in plain words what the Accessibility button is only if you can support it from the page (the page names it but does not describe its look or place, so keep it as just "the Accessibility button"). Keep every other step as is.
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.google.com/accessibility/android/answer/7349565?hl=en

## tr102-d
- reasons: Unexplained jargon in the final reply: "If TalkBack is on, use a three-finger swipe up instead."
- fix requested: Explain or drop the TalkBack clause. For example: "If your phone already reads aloud everything you touch (this is called TalkBack), swipe up with three fingers instead." Also say in plain words what the Accessibility button is only if you can support it from the page (the page names it but does not describe its look or place, so keep it as just "the Accessibility button"). Keep every other step as is.
- low scores: {'plain': 1} | gates not passed: {}
- sources: https://support.google.com/accessibility/android/answer/7349565?hl=en

## tr103-a
- reasons: Step 5 bundles three actions (tap Custom, pick date, set time).
- fix requested: Split step 5 into separate steps, each with one action: "Tap Custom." then "Choose tomorrow's date." then "Set the time to 10:00 AM." The page gives no Done/Add step for Reminders, so do not invent one. Keep the 9:00 AM default note.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102484

## tr103-c
- reasons: Step 5 bundles three actions (tap Custom, pick date, set time).
- fix requested: Split step 5 into separate steps, each with one action: "Tap Custom." then "Choose tomorrow's date." then "Set the time to 10:00 AM." The page gives no Done/Add step for Reminders, so do not invent one. Keep the 9:00 AM default note.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102484

## tr103-d
- reasons: Step 5 bundles three actions (tap Custom, pick date, set time).
- fix requested: Split step 5 into separate steps, each with one action: "Tap Custom." then "Choose tomorrow's date." then "Set the time to 10:00 AM." The page gives no Done/Add step for Reminders, so do not invent one. Keep the 9:00 AM default note.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/en-us/102484
