# Revision list: batch ny6b, after review round 1 (7 examples)

Edit ONLY these examples in data/v2/specs/ny6b.py, then rebuild.

## tr193-e
- reasons: Step 3 'choose the option that lets sites ask for notifications' gives no on-screen label, so the user cannot tell which option to pick.
- fix requested: Rewrite step 3 to use the page's wording: 'Select **Allow quieter notification prompts**, then choose the option that allows sites to ask to send notifications.' Keep step 4 (**Use quieter messaging**) and the closing bell-icon sentence.
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/chrome/answer/3220216

## tr193-r
- reasons: Final reply only handles the case where the site is already in the Allowed list; a site that is not listed leaves the user stuck. Page gives the alternative.
- fix requested: Add a line after step 3: 'If you do not see the site in that list, select **Add** next to **Not allowed to send pop-ups or use redirects**, type the site's web address, then select **Add**.' Also say step 3 starts after the user selects More to the right of the site's name.
- required actions missing from the reply: If the site is not listed, select Add next to Not allowed to send pop-ups or use redirects, enter the address, select Add
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.google.com/chrome/answer/3220216

## tr194-c
- reasons: Step 4 bundles adding the language and choosing it in one step, and step 5 describes the control as a 'down arrow', which the page does not say.
- fix requested: Change step 5 to: 'Next to **Preferred caption language**, open the dropdown and choose **Spanish**.' Optionally split step 4 into 'Next to **Manage languages**, select **Add languages**' and 'Choose **Spanish**. Chrome downloads the language pack by itself.'
- unsupported claims: 'open the down arrow and choose Spanish' -> page says 'open the dropdown'; no 'down arrow' is described
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/chrome/answer/10538231

## tr197-e
- reasons: Reply skips the page's step 'Read the consent wording, then check the box' between Delete and Move to trash. The user is careful not to lose photos, so the order matters too.
- fix requested: Replace step 6 with two steps: '6. Click **Delete** at the top right.' '7. Read the wording that appears, check the box to continue, then click **Move to trash**.' Keep Download (step 5) before Delete so copies are saved first.
- required actions missing from the reply: Read the consent wording and check the box (critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.google.com/googleone/answer/9776477

## tr197-r
- reasons: Last line points to 'Google Photos backup settings' with no location or step, and the page does not give one; the user cannot act on it.
- fix requested: Replace the last two sentences with: 'If it is still full after that, automatic backup may be filling the space again. Photos and videos waiting to be backed up are added to the free space unless automatic backup is turned off.' Do not name a settings screen; the page gives none (it only links to 'Learn more about Google Photos back ups').
- unsupported claims: 'Check your **Google Photos** backup settings.' -> page does not name Google Photos in that sentence and gives no place or steps for turning automatic backup off
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/googleone/answer/9776477

## tr198-c
- reasons: The user said they want to print the route. The reply gives walking directions only and never mentions printing, so a stated goal is dropped. The cited page does not cover printing.
- fix requested: Add a second source https://support.google.com/maps/answer/7101463 (Share, send or print directions from Google Maps, Computer). After step 3 add: '4. Pick the route you want. 5. Click the **printer** icon. 6. Choose **Print including maps** or **Print text only**. 7. Click **Print**.' Keep the Details line optional.
- required actions missing from the reply: Print: click the printer icon, choose Print including maps or Print text only, click Print (critical, user's stated goal; on a different page)
- low scores: {'steps': 0, 'constraints': 0} | gates not passed: {}
- sources: https://support.google.com/maps/answer/144339

## tr198-e
- reasons: Step 5 sends the user to look for a heading that is not on the screen.
- fix requested: Change step 5 to: 'Check the box next to **Tolls**.' Do not mention 'Avoid tolls & highways'.
- unsupported claims: 'Under **Avoid tolls & highways**, check **Tolls**.' -> page says 'Avoid tolls & highways' is only a section heading in the article, not a label on screen; the checkbox labels are Tolls and Highways
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/maps/answer/144339
