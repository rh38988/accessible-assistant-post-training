# Revision list: batch ny4b, after review round 1 (7 examples)

Edit ONLY these examples in data/v2/specs/ny4b.py, then rebuild.

## tr169-a
- reasons: Navigation path mixes two sections of the page; unsupported 'Wi-Fi panel' claim.
- fix requested: Page path is: select the time at the bottom right, then Settings, then Network on the left, then pick the network, (type password), Connect. 'Not Connected' belongs to the separate 'Turn on Wi-Fi' steps and is selected right after selecting the time, not after Settings. Rewrite the path as: 1 Select the time at the bottom right. 2 Select Settings. 3 On the left, select Network. Then select the network, type the password, select Connect. If Wi-Fi is off: select the time, select Not Connected, turn on Wi-Fi. Remove 'your network name and signal strength show in the Wi-Fi panel' (the page only says that seeing the network name and signal strength after selecting Not Connected means you are already connected; it names no 'Wi-Fi panel').
- unsupported claims: 'Select **Not Connected**' as step 3 after Settings -> page selects Not Connected right after the time (Turn on Wi-Fi steps); the connect steps go Settings > Network | 'your network name and signal strength show in the Wi-Fi panel' -> page names no Wi-Fi panel and says this only means you are already connected
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

## tr169-c
- reasons: Same path error. Sign-in page tip is supported.
- fix requested: Page path is: select the time at the bottom right, then Settings, then Network on the left, then pick the network, (type password), Connect. 'Not Connected' belongs to the separate 'Turn on Wi-Fi' steps and is selected right after selecting the time, not after Settings. Rewrite the path as: 1 Select the time at the bottom right. 2 Select Settings. 3 On the left, select Network. Then select the network, type the password, select Connect. If Wi-Fi is off: select the time, select Not Connected, turn on Wi-Fi. Remove 'your network name and signal strength show in the Wi-Fi panel' (the page only says that seeing the network name and signal strength after selecting Not Connected means you are already connected; it names no 'Wi-Fi panel'). For this open network, skip the password step and keep the sign-in page tip.
- unsupported claims: 'Select **Not Connected**' after Settings -> see path; page goes Settings > Network
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

## tr169-d
- reasons: Same path error and 'Wi-Fi panel' claim in the final reply.
- fix requested: Page path is: select the time at the bottom right, then Settings, then Network on the left, then pick the network, (type password), Connect. 'Not Connected' belongs to the separate 'Turn on Wi-Fi' steps and is selected right after selecting the time, not after Settings. Rewrite the path as: 1 Select the time at the bottom right. 2 Select Settings. 3 On the left, select Network. Then select the network, type the password, select Connect. If Wi-Fi is off: select the time, select Not Connected, turn on Wi-Fi. Remove 'your network name and signal strength show in the Wi-Fi panel' (the page only says that seeing the network name and signal strength after selecting Not Connected means you are already connected; it names no 'Wi-Fi panel').
- unsupported claims: 'Select **Not Connected**' after Settings -> wrong path | 'in the Wi-Fi panel' -> not on the page
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

## tr169-e
- reasons: Wrong Not Connected path; step 3 bundles three actions; step 4 vague about where the option is.
- fix requested: Page path is: select the time at the bottom right, then Settings, then Network on the left, then pick the network, (type password), Connect. 'Not Connected' belongs to the separate 'Turn on Wi-Fi' steps and is selected right after selecting the time, not after Settings. Rewrite the path as: 1 Select the time at the bottom right. 2 Select Settings. 3 On the left, select Network. Then select the network, type the password, select Connect. If Wi-Fi is off: select the time, select Not Connected, turn on Wi-Fi. Remove 'your network name and signal strength show in the Wi-Fi panel' (the page only says that seeing the network name and signal strength after selecting Not Connected means you are already connected; it names no 'Wi-Fi panel'). Then split step 3 into separate steps (select your network; type the password; select Connect) and make the next step: 'Select your network again in the Wi-Fi list, then turn on Automatically connect to this network.'
- unsupported claims: 'Select **Not Connected**, and turn on **Wi-Fi** if it is off' after Settings -> wrong path | 'Go back to your network's settings' -> page says open Wi-Fi, select your network, then turn on the option
- low scores: {'actionable': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

## tr169-r
- reasons: The failure cause is an unsupported inference and the first assistant turn has the wrong Wi-Fi path; the page gives no troubleshooting for a missing network.
- fix requested: Fix the first assistant turn path as in tr169-a. Change the user's second message to a story the page supports, e.g. 'My network name is not shown because the router is set to hide its name, but I know the name and password.' Then reply: 1 Select the time at the bottom right, then Settings. 2 Select Network on the left. 3 Select Add connection, then Add Wi-Fi. 4 Enter the network information in the box that appears. 5 Select Connect. Drop 'The network may be hidden' as a guess.
- unsupported claims: 'The network may be hidden.' -> page does not say a missing network means it is hidden; it only says administrators may hide networks | 'ask the person who set up the network' -> not on the page (harmless but unsourced) | Earlier turn: 'Select **Not Connected**' after Settings -> wrong path
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

## tr170-r
- reasons: Step 3 is not an action ('the next options are a reset or a recovery') and omits that the page's reset keeps personal files; the user is already on Wi-Fi so step 2 is mostly irrelevant.
- fix requested: Make step 3 concrete and sourced: 'If it still will not download, the next step is a reset. A reset does not delete your personal files. If that does not work, recovery is the last step; recovery permanently erases everything on the drive, including downloads, so back up your files first if you can.' Keep step 1 (turn off, then on). Reword step 2 as 'If you ever use your phone's connection, switch to Wi-Fi or Ethernet'. Keep 'test after each one'. If the page links reset/recovery articles, add the reset one as a second source for the how-to.
- required actions missing from the reply: Reset the Chromebook without deleting personal files
- low scores: {'steps': 1, 'actionable': 1} | gates not passed: {}
- sources: https://support.google.com/chromebook/answer/177889?hl=en

## tr171-r
- reasons: The explanation for why the shortcut did nothing is invented and may be false; page has no troubleshooting for this.
- fix requested: Remove the claimed cause. First turn: say 'Press Ctrl + Search + m to magnify your whole screen' (Launcher variant ok) without 'on or off'. Change the failure story to one the page supports, e.g. user: 'I used Ctrl + Shift + plus and now everything is just bigger and the bar at the bottom changed, I wanted a magnifier'. Reply: those keys change the whole screen size; to magnify instead, select the time at the bottom right, Settings, Accessibility, under Display turn on Full screen magnifier. Or keep the shortcut story but make the final reply: 'I cannot see a reason for that on the Google page. You can turn the magnifier on from Settings instead: ...' with the three Settings steps.
- unsupported claims: 'The shortcut only works once the magnifier is turned on in Settings.' -> page says only 'To quickly magnify your entire screen, press Ctrl + Search + m' and states no such prerequisite | Earlier turn: 'to turn it on or off' -> page does not say the shortcut toggles
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.google.com/chromebook/answer/6320705?hl=en
