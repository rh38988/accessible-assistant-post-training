# Revision list: batch fx1a, after review round 2 (8 examples)

Edit ONLY these examples in data/v2/specs/fx1a.py, then rebuild.

## tr001-c
- reasons: User asked for larger AND darker text. The only page-supported darker/stronger option (high contrast fonts) is missing, and the 'darker' claim for bold is not on the page.
- fix requested: Keep steps 1-4. Remove 'which makes the letters darker and thicker'; say only 'You can also turn on bold on that screen.' Then add a short second part for darker text: 'To make the words stand out more, open Settings, tap Accessibility, tap Visibility enhancements, and turn on the switch next to high contrast fonts. This adds an outline around all the text so it stands out from the background.' Keep the hedge about menu names.
- unsupported claims: 'You can also choose to make it bold, which makes the letters darker and thicker' -> the page does not say bold makes letters darker; the page's option for stronger text is high contrast fonts
- required actions missing from the reply: For darker text: Settings > Accessibility > Visibility enhancements > turn on high contrast fonts (adds an outline to text)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/

## tr002-d
- reasons: Final reply gives only the newer-Android path. The page says that if the menu/Settings option is not there, the older steps apply; the user is on a Pixel of unknown software version and the reply does not tell them what to do if they see only an arrow.
- fix requested: After step 3 add one line, as in tr002-a: 'If you don't see a Menu icon, your phone has older software. Tap the Down arrow at the right of the bar instead, then slide Ring.' Keep the rest.
- required actions missing from the reply: If no menu icon appears, use the older steps (Down arrow, then Ring slider)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.google.com/android/answer/9082609?hl=en

## tr004-d
- reasons: Reply never says what the user will see after pressing the buttons; the page says the screenshot appears right away (iOS 26 shows quick tools, iOS 18 or earlier shows a thumbnail in the lower-left corner). The user also wants to send it and the reply gives no pointer for that.
- fix requested: After step 3 add: 'The screenshot appears on the screen (on older iOS versions a small picture shows in the lower-left corner for a moment). You can tap it to share it.' Keep the Photos > Collections > Media Types > Screenshots line. Do not name 'Done' or 'Save to Photos' (not on the page).
- required actions missing from the reply: Screenshot appears; edit, share or save it (what the user sees)
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.apple.com/102616

## tr005-a
- reasons: Drops the page's extensions/incognito step and the status check; step 4 'Clear your browser's saved website data (called cache and cookies)' gives no starting point, so a low-confidence user cannot act on it (S4). Reply also never asks which browser is used, so the how-to cannot be specific.
- fix requested: Add as step 1: 'Check whether Gmail is down: look at the Google Workspace Status Dashboard.' Add after the different-browser step: 'Turn off any browser extensions one at a time, opening Gmail again after each one. You can also try a private (incognito) window.' For the cache step, either keep it as 'Clear your browser's cache and cookies, then open Gmail again' and add the second official Google source https://support.google.com/accounts/answer/32050 (Chrome: clear cache and cookies) with its exact menu path, or end with one short question asking which browser they use. Keep one action per step.
- required actions missing from the reply: Check whether Gmail is down (Google Workspace Status Dashboard) | Turn off extensions / uninstall computer apps one at a time, or use incognito/private window
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/mail/answer/7074871?hl=en

## tr005-d
- reasons: User said 'I tried turning it off and on' (already restarted); step 3 'Restart your computer and open Gmail again' repeats what she did. Page's clear cache and cookies and extensions steps are left out while the repeat is included.
- fix requested: Replace step 3 (restart) with 'Clear your browser's cache and cookies, then open Gmail again.' (or a one-line note that restarting was already done). Optionally add 'Turn off browser extensions one at a time, opening Gmail after each.' Keep update browser, different browser, and the Wi-Fi off and on step.
- required actions missing from the reply: Turn off extensions / uninstall computer apps one at a time, or use incognito/private window | Clear browser cache and cookies, then open Gmail again
- low scores: {'steps': 1, 'constraints': 1} | gates not passed: {}
- sources: https://support.google.com/mail/answer/7074871?hl=en

## tr006-c
- reasons: Windows 11 user, but the page's first step for Windows 11 (open the Get Help app and run the printer troubleshooter) is missing. Step 4 bundles 'look for a button' and 'use it to make sure wireless is on'; the extra 'make sure your laptop is online' (step 6) is not on the page.
- fix requested: Add a first step: 'Open the **Get Help** app and run the printer troubleshooter. It checks the printer and tries to fix most problems.' Reword step 4 to 'Make sure the printer's wireless is on. Many printers have a button with a blue wireless icon.' Delete step 6 ('make sure your laptop is online') or fold it into the same-network step. Keep the same-network step with the extender explanation.
- required actions missing from the reply: Windows 11: open Get Help app and run the printer troubleshooter
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73

## tr006-d
- reasons: Wireless branch is missing the page's printer wireless connectivity test and the check that the computer is on the same network as the printer (a likely cause after something worked last month).
- fix requested: After step 5 add: 'If it connects wirelessly, run the printer's wireless test from its menu if it has one.' and 'Make sure your computer is connected to the same Wi-Fi network as the printer.' Keep the rest. Ask nothing more.
- required actions missing from the reply: Run the printer's wireless connectivity test from its menu | Confirm PC is on same network as printer (extenders / separate SSIDs)
- low scores: {'steps': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73

## tr006-r
- reasons: Missing the final Next after 'Do not share this printer' (step 9 ends at the sharing choice, step 10 jumps to the test page) and the driver-source choice (Windows Update/Have Disk). Steps 1, 2 and 9 pack several clicks together; ten steps in one reply is long for the user.
- fix requested: Step 8: 'Choose your printer's maker and model. If asked, choose **Windows Update** so Windows finds the driver, then click **Next**.' Split step 9 into 'Type a name for the printer and click **Next**.' and 'Choose **Do not share this printer**, then click **Next**.' Keep the 'Print a test page, then Finish' step. If length exceeds the cap, drop the Add manually branch steps 5-9 into one line pointing to the same page.
- required actions missing from the reply: Install driver: Windows Update (or Have Disk), choose manufacturer and model, Next | Do not share this printer, Next (critical)
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73
