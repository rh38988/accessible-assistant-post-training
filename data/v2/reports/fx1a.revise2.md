# fx1a revise2

Fixed (8): tr001-c, tr002-d, tr004-d, tr005-a, tr005-d, tr006-c, tr006-d, tr006-r.
Builder: `python3 data/v2/tools/build_v2.py fx1a` printed OK (30 examples, longest conversation 1578 characters).

Each source page was fetched again before editing.

Cannot fix: none outright. One reviewer requirement was only partly met, see below.

Notes per example:
- tr001-c: removed "makes the letters darker and thicker" (page does not say bold makes letters darker). Added the high contrast fonts path (Settings > Accessibility > Visibility enhancements > switch next to high contrast fonts), which the page supports as adding an outline to all text.
- tr002-d: added the older-software line after step 3. The page's condition is "If you don't find Settings, go to the steps for older Android versions", so the line says "no Menu icon, or you can't find Settings under it". The reviewer's "Menu or Settings" wording matched the page.
- tr004-d: after step 3 added what the user sees (picture appears right away; iOS 26 quick tools include draw, crop, send to apps or contacts; older iOS shows a lower-left thumbnail that opens when tapped). Did not use "Done" or "Save to Photos". The page says "tap it to open" for the thumbnail, not "share", so the reply says "open" and attributes sending to iOS 26 quick tools.
- tr005-a: added step 1 (Google Workspace Status Dashboard), extension step, incognito/private window sentence, and a Chrome cache/cookies path. The Chrome path is from a second official page (support.google.com/accounts/answer/32050), added as the example-level "sources" list with the original source first. The Gmail page gives no menu path, so the Chrome steps are the only starting point.
- tr005-d: replaced the restart step (user already restarted) with clear cache and cookies. Added the extensions step. Kept update browser, different browser, and Wi-Fi off and on.
- tr006-c: added the Windows 11 Get Help first step. Reworded the blue-wireless step. Deleted step 6 ("make sure your laptop is online"), which the reviewer said is not on the page. Same-network step now uses the page's "extenders ... same network" wording. Dropped the reviewer's "tries to fix most problems" phrase, which the page does not say. Dropped "Many printers have a menu option for it" from the wireless test step (not on the page).
- tr006-d: after the wireless step added the wireless connectivity test and the same-network check. Dropped the reviewer's "from its menu if it has one" (the page does not say that).
- tr006-r: step 8 now has the Have Disk / Windows Update choice (page order: driver source first, then maker and model). Step 9 is maker and model then Next. Step 10 is the name then Next. Step 11 is Do not share then Next. Step 12 is the test page and Finish.

Required actions NOT fully covered (judgment call, flagged for the reviewer):
- tr005-a and tr005-d: the page also says to "uninstall applications one by one" in the extensions step. The replies cover extensions and the private window, but not uninstalling. The reply omits uninstalling because the user is low-confidence and tr005-e (a different example) asks not to remove programs. If the reviewer insists on this action, it can be added as one more step.

Follow-ups touched: none outside the revision list. tr001, tr002, tr004, tr005, tr006 have no missing-information example whose question needed changing.

Page contradicting the reviewer: the reviewer's tr002-d wording ("if the menu/Settings option is not there") was slightly broader than the page's "If you don't find Settings" condition. Adjusted as noted above.
