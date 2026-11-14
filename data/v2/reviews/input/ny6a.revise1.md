# Revision list: batch ny6a, after review round 1 (22 examples)

Edit ONLY these examples in data/v2/specs/ny6a.py, then rebuild.

## tr187-a
- reasons: Unsupported icon description (three dots).
- fix requested: Remove "(the three dots)" everywhere in the reply and say only "tap **More**" (the page says: "To the right of the address bar, tap More, then Add to bookmarks"). Do not describe the icon.
- unsupported claims: "(the three dots)" -> the Chrome page labels the control "More" and shows an icon but never describes it as three dots
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid

## tr187-c
- reasons: Unsupported icon description (three dots).
- fix requested: Remove "(the three dots)" everywhere in the reply and say only "tap **More**" (the page says: "To the right of the address bar, tap More, then Add to bookmarks"). Do not describe the icon. The 'open it again' steps are fine; you may add 'Tap a folder' before 'Tap the bookmark' as the page lists it.
- unsupported claims: "(the three dots)" -> the Chrome page labels the control "More" and shows an icon but never describes it as three dots
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid

## tr187-d
- reasons: Unsupported icon description (three dots).
- fix requested: Remove "(the three dots)" everywhere in the reply and say only "tap **More**" (the page says: "To the right of the address bar, tap More, then Add to bookmarks"). Do not describe the icon.
- unsupported claims: "(the three dots)" -> the Chrome page labels the control "More" and shows an icon but never describes it as three dots
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid

## tr187-e
- reasons: Unsupported icon description (three dots).
- fix requested: Remove "(the three dots)" everywhere in the reply and say only "tap **More**" (the page says: "To the right of the address bar, tap More, then Add to bookmarks"). Do not describe the icon.
- unsupported claims: "(the three dots)" -> the Chrome page labels the control "More" and shows an icon but never describes it as three dots
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid

## tr187-r
- reasons: Unsupported claim about folder order; unsupported three dots description in the first assistant turn.
- fix requested: In the final reply replace "Recently opened folders show first." with "If you opened a bookmarks folder recently, you will see that same folder. To see other folders, tap **Back** at the top left." In the first assistant turn remove "(the three dots)" and say only "tap **More**".
- unsupported claims: "Recently opened folders show first." -> the page only says that if you recently opened a folder you will find the same folder; other folders are reached with Back at the top left. It does not say recently opened folders are listed first | Earlier assistant turn: "(the three dots)" -> icon never described as three dots on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid

## tr188-a
- reasons: Unsupported icon descriptions.
- fix requested: Delete the parentheticals "(the three dots menu)" and "(the plus sign)" and name the controls only by their labels: "Select **Settings and more**", then "Select **Zoom in**". Keep the keyboard tip (Ctrl and plus sign) as is.
- unsupported claims: "(the three dots menu)" -> the Edge page only says "select Settings and more" and shows an icon; it never describes it as three dots | "(the plus sign)" -> the page says "Zoom in"; it does not describe the icon as a plus sign
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/microsoft-edge/accessibility-features-in-microsoft-edge-4c696192-338e-9465-b2cd-bd9b698ad19a

## tr188-d
- reasons: Unsupported icon descriptions.
- fix requested: Delete the parentheticals "(the three dots menu)" and "(the plus sign)" and name the controls only by their labels: "Select **Settings and more**", then "Select **Zoom in**". Keep the keyboard tip (Ctrl and plus sign) as is.
- unsupported claims: "(the three dots menu)" -> the Edge page only says "select Settings and more" and shows an icon; it never describes it as three dots | "(the plus sign)" -> the page says "Zoom in"; it does not describe the icon as a plus sign
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/microsoft-edge/accessibility-features-in-microsoft-edge-4c696192-338e-9465-b2cd-bd9b698ad19a

## tr188-r
- reasons: Unsupported icon description in the final reply and in the first assistant turn.
- fix requested: In the final reply change to "select **Zoom out** until it looks right" (no "(the minus sign)"). In the first assistant turn delete "(the three dots menu)" and "(the plus sign)".
- unsupported claims: "select **Zoom out** (the minus sign)" -> the page says "Zoom out" but never describes the icon as a minus sign | Earlier assistant turn: "(the three dots menu)" and "(the plus sign)" -> not described on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.microsoft.com/en-us/microsoft-edge/accessibility-features-in-microsoft-edge-4c696192-338e-9465-b2cd-bd9b698ad19a

## tr189-d
- reasons: The reply only covers the allowed-list case. The user never said the site is in the allowed list, and the page has a second path for a site that is not listed. A user whose site is not listed is left with no steps.
- fix requested: After step 5 add: "If you do not see the site in that list, next to **Not allowed to send pop-ups or use redirects** click **Add**, type the web address of the site, then click **Add**." Keep the rest.
- required actions missing from the reply: If the site is not listed, click Add next to Not allowed to send pop-ups or use redirects, enter the address, click Add (critical)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.google.com/chrome/answer/95472

## tr189-r
- reasons: Unsupported location claim.
- fix requested: Change step 2 to "Click **View site information**." (remove "in the address bar"). Change step 3 to "Next to **Notifications**, choose **Block**."
- unsupported claims: "Click **View site information** in the address bar." -> the page does not say where View site information is
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95472

## tr190-a
- reasons: Missing the final review of file and link types; unsupported position claim.
- fix requested: Change step 6 to "Next to **Make Google Chrome your default browser**, click **Set default**." and add step 7: "Look at the list called **Set default file types or link types** to check Chrome is set for the types you need."
- unsupported claims: "At the top, click **Set default**..." -> the page says "Next to Make Google Chrome your default browser", not "at the top"
- required actions missing from the reply: Review Set default file types or link types list (non-critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop

## tr190-d
- reasons: Missing the final review of file and link types; unsupported position claim.
- fix requested: Change step 5 to "Next to **Make Google Chrome your default browser**, click **Set default**." and add step 6: "Look at the list called **Set default file types or link types** to check Chrome is set for the types you need."
- unsupported claims: "At the top, click **Set default**..." -> the page says "Next to Make Google Chrome your default browser", not "at the top"
- required actions missing from the reply: Review file/link types list (non-critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop

## tr190-e
- reasons: Missing the file and link types review; unsupported position claim. The user wants it short, so add only one short line.
- fix requested: Change step 5 to "Click **Set default** next to **Make Google Chrome your default browser**." and add a short step 6: "Check the **Set default file types or link types** list shows Chrome for the types you need." Do not add anything about downloading.
- unsupported claims: "At the top, click **Set default**." -> the page says "Next to Make Google Chrome your default browser", not "at the top"
- required actions missing from the reply: Review file/link types list (non-critical)
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop

## tr191-a
- reasons: Unsupported icon description.
- fix requested: Change step 1 to "At the top right of Chrome, click **More**." Remove "the three dots".
- unsupported claims: "(the three dots at the top right)" -> the page says "At the top right, click More" and shows an icon but never describes three dots
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95759?hl=en

## tr191-c
- reasons: Unsupported icon description.
- fix requested: Change step 1 to "At the top right of Chrome, click **More**." Remove "the three dots". Keep the rest.
- unsupported claims: "(the three dots at the top right)" -> never described as three dots on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95759?hl=en

## tr191-d
- reasons: Unsupported icon description.
- fix requested: Change step 1 to "At the top right of Chrome, click **More**." Remove "the three dots".
- unsupported claims: "(the three dots at the top right)" -> never described as three dots on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95759?hl=en

## tr191-r
- reasons: Unsupported icon description.
- fix requested: Change step 1 to "At the top right of Chrome, click **More**." Remove "the three dots". Optionally in the first assistant turn say "download tray" is the page name; "small download box" is fine.
- unsupported claims: "(the three dots at the top right)" -> never described as three dots on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95759?hl=en

## tr192-a
- reasons: Unsupported icon description.
- fix requested: Change step 1 of the second list to "At the top right of Chrome, click **More**." Remove "the three dots".
- unsupported claims: "(the three dots at the top right)" -> never described as three dots on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95606?hl=en

## tr192-c
- reasons: Unsupported icon description.
- fix requested: Change step 1 to "At the top right of Chrome, click **More**." Remove "the three dots". Keep the rest.
- unsupported claims: "(the three dots at the top right)" -> never described as three dots on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95606?hl=en

## tr192-d
- reasons: Unsupported icon description.
- fix requested: Change step 1 of the second list to "At the top right of Chrome, click **More**." Remove "the three dots".
- unsupported claims: "(the three dots at the top right)" -> never described as three dots on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95606?hl=en

## tr192-e
- reasons: Unsupported icon description.
- fix requested: Change step 1 to "At the top right of Chrome, click **More**." Remove "the three dots". Keep the rest.
- unsupported claims: "(the three dots at the top right)" -> never described as three dots on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95606?hl=en

## tr192-r
- reasons: Unsupported icon description.
- fix requested: Change step 1 to "At the top right of Chrome, click **More**." Remove "the three dots". Keep the rest.
- unsupported claims: "(the three dots at the top right)" -> never described as three dots on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chrome/answer/95606?hl=en
