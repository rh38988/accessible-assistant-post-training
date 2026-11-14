# Reviewer file for batch ny4b, round 1.
S = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}

def rec(id, acts, cov=None, clar=False, src="pass", unsup=None, sc=None, dec="keep", reasons="", fix=""):
    scores = dict(S)
    if sc:
        scores.update(sc)
    if clar:
        acts, cov = [], []
        scores["steps"] = "NA"
    if cov is None:
        cov = [True] * len(acts)
    return {
        "id": id, "required_actions": acts, "covered": cov, "needs_clarification": clar,
        "gates": {"source": src, "safety": "pass", "duplicate": "pass"},
        "unsupported_claims": unsup or [], "scores": scores,
        "decision": dec, "reasons": reasons, "fix": fix,
    }

PS = ["Open Settings, tap Battery (critical)", "Tap Power saving (critical)", "Tap the switches next to the options you want",
      "Tap the switch at the top of the screen to turn on the mode (critical)"]
PS_CHANGE = ["Turn off Power saving mode temporarily (critical)", "Change the options (critical)", "Turn Power saving mode back on (critical)"]
SS = ["Press the Screenshot key (critical)", "In the menu at the bottom, select Screenshot (critical)", "Choose a capture type, e.g. Take a full screen screenshot (critical)"]
SS_NOKEY = ["At the bottom right select Settings, then Screen Capture (critical)", "Choose Take a full screen screenshot / Take a partial screenshot (critical)"]
WIFI = ["Select the time at the bottom right, then Settings (critical)", "On the left select Network (critical)", "Turn on Wi-Fi if off (via Not Connected after selecting the time)",
        "Select the network (critical)", "Type the password if secure (critical)", "Select Connect (critical)"]
WIFI_FIX_PATH = ("Page path is: select the time at the bottom right, then Settings, then Network on the left, then pick the network, "
                 "(type password), Connect. 'Not Connected' belongs to the separate 'Turn on Wi-Fi' steps and is selected right after selecting the time, "
                 "not after Settings. Rewrite the path as: 1 Select the time at the bottom right. 2 Select Settings. 3 On the left, select Network. "
                 "Then select the network, type the password, select Connect. If Wi-Fi is off: select the time, select Not Connected, turn on Wi-Fi. "
                 "Remove 'your network name and signal strength show in the Wi-Fi panel' (the page only says that seeing the network name and signal strength after selecting Not Connected means you are already connected; it names no 'Wi-Fi panel').")
UPD = ["Make sure the Chromebook is on and on Wi-Fi", "Select the time at the bottom right, then Settings (critical)", "At bottom left select About ChromeOS (critical)", "Select Check for updates (critical)"]
UPD_FIN = ["Select the Update device notification next to the date (critical)", "Select Restart (critical)"]

R = []
R.append(rec("tr167-a", PS))
R.append(rec("tr167-c", PS))
R.append(rec("tr167-b", [], clar=True))
R.append(rec("tr167-d", PS))
R.append(rec("tr167-e", PS))
R.append(rec("tr167-r", PS_CHANGE))

R.append(rec("tr168-a", SS))
R.append(rec("tr168-c", SS_NOKEY))
R.append(rec("tr168-b", [], clar=True))
R.append(rec("tr168-d", SS))
R.append(rec("tr168-e", SS_NOKEY))
R.append(rec("tr168-r", ["Say screenshots are saved to Downloads and copied to the clipboard (critical)"]))

R.append(rec("tr169-a", WIFI, src="fail",
    unsup=["'Select **Not Connected**' as step 3 after Settings -> page selects Not Connected right after the time (Turn on Wi-Fi steps); the connect steps go Settings > Network",
           "'your network name and signal strength show in the Wi-Fi panel' -> page names no Wi-Fi panel and says this only means you are already connected"],
    dec="revise", reasons="Navigation path mixes two sections of the page; unsupported 'Wi-Fi panel' claim.", fix=WIFI_FIX_PATH))
R.append(rec("tr169-c", WIFI[:3] + WIFI[3:4] + WIFI[5:], src="fail",
    unsup=["'Select **Not Connected**' after Settings -> see path; page goes Settings > Network"],
    dec="revise", reasons="Same path error. Sign-in page tip is supported.", fix=WIFI_FIX_PATH + " For this open network, skip the password step and keep the sign-in page tip."))
R.append(rec("tr169-b", [], clar=True))
R.append(rec("tr169-d", WIFI, src="fail",
    unsup=["'Select **Not Connected**' after Settings -> wrong path", "'in the Wi-Fi panel' -> not on the page"],
    dec="revise", reasons="Same path error and 'Wi-Fi panel' claim in the final reply.", fix=WIFI_FIX_PATH))
R.append(rec("tr169-e", ["Connect to the network (time, Settings, Network, pick network, password, Connect) (critical)", "Open Wi-Fi, select your network, turn on Automatically connect to this network (critical)", "Optional: turn on Prefer this network"],
    src="fail",
    unsup=["'Select **Not Connected**, and turn on **Wi-Fi** if it is off' after Settings -> wrong path",
           "'Go back to your network's settings' -> page says open Wi-Fi, select your network, then turn on the option"],
    sc={"actionable": 1}, dec="revise",
    reasons="Wrong Not Connected path; step 3 bundles three actions; step 4 vague about where the option is.",
    fix=WIFI_FIX_PATH + " Then split step 3 into separate steps (select your network; type the password; select Connect) and make the next step: 'Select your network again in the Wi-Fi list, then turn on Automatically connect to this network.'"))
R.append(rec("tr169-r", ["Add the network by hand: Add connection, Add Wi-Fi, enter network info, Connect (critical)"],
    src="fail",
    unsup=["'The network may be hidden.' -> page does not say a missing network means it is hidden; it only says administrators may hide networks",
           "'ask the person who set up the network' -> not on the page (harmless but unsourced)",
           "Earlier turn: 'Select **Not Connected**' after Settings -> wrong path"],
    dec="revise", reasons="The failure cause is an unsupported inference and the first assistant turn has the wrong Wi-Fi path; the page gives no troubleshooting for a missing network.",
    fix="Fix the first assistant turn path as in tr169-a. Change the user's second message to a story the page supports, e.g. 'My network name is not shown because the router is set to hide its name, but I know the name and password.' Then reply: 1 Select the time at the bottom right, then Settings. 2 Select Network on the left. 3 Select Add connection, then Add Wi-Fi. 4 Enter the network information in the box that appears. 5 Select Connect. Drop 'The network may be hidden' as a guess."))

R.append(rec("tr170-a", UPD))
R.append(rec("tr170-c", UPD_FIN))
R.append(rec("tr170-b", [], clar=True))
R.append(rec("tr170-d", UPD + UPD_FIN))
R.append(rec("tr170-e", UPD + ["Mention the mobile data alert showing how much data it needs; stop or continue"]))
R.append(rec("tr170-r", ["Turn the Chromebook off and back on (critical)", "Switch from mobile data to Wi-Fi/Ethernet", "Reset the Chromebook without deleting personal files", "Recovery erases everything; back up first"],
    cov=[True, True, False, True],
    sc={"steps": 1, "actionable": 1}, dec="revise",
    reasons="Step 3 is not an action ('the next options are a reset or a recovery') and omits that the page's reset keeps personal files; the user is already on Wi-Fi so step 2 is mostly irrelevant.",
    fix="Make step 3 concrete and sourced: 'If it still will not download, the next step is a reset. A reset does not delete your personal files. If that does not work, recovery is the last step; recovery permanently erases everything on the drive, including downloads, so back up your files first if you can.' Keep step 1 (turn off, then on). Reword step 2 as 'If you ever use your phone's connection, switch to Wi-Fi or Ethernet'. Keep 'test after each one'. If the page links reset/recovery articles, add the reset one as a second source for the how-to."))

R.append(rec("tr171-a", ["Select the time, then Settings", "Select Accessibility", "Under Display turn on Full screen magnifier (critical)"]))
R.append(rec("tr171-c", ["Select the time, then Settings", "Select Accessibility", "Under Display turn on Docked magnifier (critical)", "Optionally set Docked zoom level"]))
R.append(rec("tr171-b", [], clar=True))
R.append(rec("tr171-d", ["Press Ctrl and + to zoom the page (critical)"]))
R.append(rec("tr171-e", ["Press Ctrl and + to zoom the page (critical)", "Ctrl and - smaller, Ctrl and 0 reset", "Warn that Ctrl+Shift variants change the whole screen"]))
R.append(rec("tr171-r", ["Open Settings > Accessibility > Display and turn on Full screen magnifier (critical)"],
    src="fail",
    unsup=["'The shortcut only works once the magnifier is turned on in Settings.' -> page says only 'To quickly magnify your entire screen, press Ctrl + Search + m' and states no such prerequisite",
           "Earlier turn: 'to turn it on or off' -> page does not say the shortcut toggles"],
    dec="revise", reasons="The explanation for why the shortcut did nothing is invented and may be false; page has no troubleshooting for this.",
    fix="Remove the claimed cause. First turn: say 'Press Ctrl + Search + m to magnify your whole screen' (Launcher variant ok) without 'on or off'. Change the failure story to one the page supports, e.g. user: 'I used Ctrl + Shift + plus and now everything is just bigger and the bar at the bottom changed, I wanted a magnifier'. Reply: those keys change the whole screen size; to magnify instead, select the time at the bottom right, Settings, Accessibility, under Display turn on Full screen magnifier. Or keep the shortcut story but make the final reply: 'I cannot see a reason for that on the Google page. You can turn the magnifier on from Settings instead: ...' with the three Settings steps."))

R.append(rec("tr172-a", ["Select the time, then Settings icon", "Select Accessibility", "Under Text-to-Speech turn on Select-to-speak (critical)", "Hold Search and drag over text (critical)"]))
R.append(rec("tr172-c", ["Tap a line of text or drag finger over an area (critical)", "Stop: Ctrl, Search or Stop"]))
R.append(rec("tr172-b", [], clar=True))
R.append(rec("tr172-d", ["Select the time, then Settings", "Select Accessibility", "Under Text-to-Speech turn on Select-to-speak (critical)", "Hold Search and drag over text (critical)"]))
R.append(rec("tr172-e", ["Highlight text, press Search and s together (critical)", "Or select the Select-to-Speak icon near the time and drag without a key", "Stop: Ctrl, Search or Stop"]))
R.append(rec("tr172-r", ["Open Settings > Accessibility > Text-to-Speech > Open select-to-speak settings", "Under Highlighting check Enable navigation controls"],
    cov=[True, True], src="fail",
    unsup=["'Those quick controls can be turned off.' as the cause -> the user can see the controls on screen, so they are on; the page gives no reason pause/skip would do nothing",
           "'turn on **Enable navigation controls**' -> page only describes turning it OFF to disable pause/play/skip; it never says this setting fixes unresponsive buttons"],
    dec="reject", reasons="The page has no troubleshooting for unresponsive controls; the reply invents a cause and a fix that contradicts the user's observation (controls are visibly present).",
    fix="Drop this failure scenario. Replace with a supported one, e.g. user says the pause and skip controls get in the way and asks how to remove them: Settings > Accessibility > Text-to-Speech > Open select-to-speak settings > under Highlighting turn off Enable navigation controls."))

REVIEWS = R
