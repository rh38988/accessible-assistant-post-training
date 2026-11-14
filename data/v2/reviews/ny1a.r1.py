# Reviewer file for batch ny1a, round 1.
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

NOHOME = ["Press the top button and either volume button at the same time (critical)", "Release both buttons right away (critical)",
          "Tap the thumbnail (lower-left) to open it or swipe left to dismiss", "Find it later: Photos > Collections > scroll up > Media Types > Screenshots"]
HOME = ["Press the top button and the Home button at the same time (critical)", "Release both buttons right away (critical)",
        "Tap the thumbnail (lower-left) to open it or swipe left to dismiss", "Find it later: Photos > Collections > scroll up > Media Types > Screenshots"]
FINDSHOT = ["Open Photos (critical)", "Tap Collections", "Scroll up, tap Media Types", "Tap Screenshots (critical)"]

UPD = ["Back up the Mac before installing", "Apple menu > System Settings", "Click General in sidebar", "Click Software Update on the right",
       "If an update appears, click the button to update, upgrade, or restart now (critical)", "Enter administrator password if prompted",
       "Keep Mac awake, do not close lid; may restart / progress bar / blank screen"]
WIFI = ["Make sure Wi-Fi is turned on", "Click the Wi-Fi status menu in the menu bar (critical)", "Choose the network (critical)",
        "Enter the password and click Join if prompted (critical)", "If network not listed, click Other Networks"]
DEL = ["Quit the app", "Find it in Finder (Applications in sidebar, or Spotlight + Command-double-click)", "Use Uninstall/Uninstaller app if present",
       "Otherwise drag to Trash (or File > Move to Trash) (critical)", "Enter administrator name and password if asked", "Finder > Empty Trash"]
LPM = ["Apple menu > System Settings", "Click Battery", "Under Energy Mode open On battery pop-up", "Choose Low Power Mode (critical)"]
LPM_OLD = ["Apple menu > System Preferences", "Click Battery", "In sidebar click Battery or Power Adapter", "Choose Low Power from Energy Mode pop-up (critical)"]
TM = ["Connect external drive; at least twice Mac storage; use only for Time Machine", "Apple menu > System Settings", "General > Time Machine",
      "Click Add Backup Disk (critical)", "Select the drive, click Set Up Disk (critical)",
      "If asked to erase, either erase or select a different backup disk or volume", "Backup starts automatically after setup"]

REVIEWS = [
 rec("tr121-a", NOHOME),
 rec("tr121-c", HOME),
 rec("tr121-b", [], clar=True),
 rec("tr121-d", NOHOME, [True, True, True, False],
     sc={"steps": 1}, dec="revise",
     reasons="Final reply gives the Photos path without the scroll-up step: 'under Collections, then Media Types, then Screenshots'. The page says to scroll up before Media Types, so Media Types may not be visible.",
     fix="In the last sentence use the page path: open Photos, tap Collections, swipe up, tap Media Types, then tap Screenshots (same wording as tr121-a)."),
 rec("tr121-e", ["Swipe the Apple Pencil from a bottom corner (either side) on a Pencil-compatible iPad (critical)", "Find it later: Photos > Collections > scroll up > Media Types > Screenshots"],
     unsup=["'The screenshot is saved for you.' -> the page does not say a Pencil screenshot is saved automatically (and does not mention Markup or Done)."],
     src="fail", dec="revise", reasons="Unsupported claim about automatic saving.",
     fix="Delete the sentence 'The screenshot is saved for you.' Replace with a neutral lead-in such as 'Here is where to look for it afterward.' Keep the Photos > Collections > Media Types > Screenshots path. Step 1 'Hold your Apple Pencil' can be merged into step 2."),
 rec("tr121-r", FINDSHOT),
 rec("tr122-a", UPD),
 rec("tr122-c", UPD),
 rec("tr122-b", [], clar=True),
 rec("tr122-d", UPD, [False, True, True, True, True, True, True], sc={"steps": 1}, dec="revise",
     reasons="Page step 1 is to back up the Mac before installing; the final reply omits it (tr122-a and tr122-c include it).",
     fix="Add a short line before step 1 or after the list: 'Before you install anything, it is a good idea to back up your Mac.'"),
 rec("tr122-e", ["Apple menu > System Settings", "General > Software Update", "Read the status; do not click the update button (user constraint)"]),
 rec("tr122-r", ["Click Check for Updates, press Command-R, or close and reopen Software Update", "Explain Software Update only offers updates compatible with the Mac model"]),
 rec("tr123-a", WIFI, [False, True, True, True, True], sc={"steps": 1}, dec="revise",
     reasons="Page says to make sure Wi-Fi is turned on before joining; reply only says to have the password ready.",
     fix="Change the lead-in to: 'Make sure Wi-Fi is turned on and have the Wi-Fi password ready.' (The page does not say how to turn Wi-Fi on, so add nothing more.)"),
 rec("tr123-c", ["Make sure Wi-Fi is turned on", "Wi-Fi status menu > Other Networks > Other (bottom of list) (critical)", "Type the name in Network Name",
                 "Choose the security type in Security pop-up", "Fill in other fields (user name, password), click Join (critical)"],
     [False, True, True, True, True], sc={"steps": 1}, dec="revise",
     reasons="Page lists 'make sure Wi-Fi is turned on' as a prerequisite; reply omits it.",
     fix="Add a first line: 'Make sure Wi-Fi is turned on, and have the network name, security type, and password from the sticky note ready.'"),
 rec("tr123-b", [], clar=True),
 rec("tr123-d", WIFI, [False, True, True, True, True], sc={"steps": 1}, dec="revise",
     reasons="Wi-Fi-on prerequisite missing; this user says the laptop 'is not on the internet', so it matters.",
     fix="Change lead-in to: 'Make sure Wi-Fi is turned on and have the Wi-Fi password ready.'"),
 rec("tr123-e", WIFI, [False, True, True, True, True], src="fail",
     unsup=["'If it shows terms and conditions, accept them.' -> terms and conditions are not mentioned on the cited page."],
     sc={"steps": 1}, dec="revise", reasons="Unsupported terms-and-conditions claim; Wi-Fi-on prerequisite missing.",
     fix="Delete 'If it shows terms and conditions, accept them.' Step 3 should read: 'If it asks for a password, type it and click Join.' Add 'Make sure Wi-Fi is turned on.' as a short first line."),
 rec("tr123-r", ["Click Other Networks to display nearby networks (critical)", "Click the network name", "Enter password, click Join"]),
 rec("tr124-a", DEL),
 rec("tr124-c", DEL),
 rec("tr124-b", [], clar=True),
 rec("tr124-d", DEL),
 rec("tr124-e", DEL + ["State that deleting the app does not delete documents made with it, but you may need the app to open them", "Deleting does not cancel subscriptions"]),
 rec("tr124-r", ["Make sure the app is closed (quit it)", "Try deleting again", "If still stuck, restart the Mac or start up in Safe Mode, then try again"],
     sc={"plain": 1}, dec="revise",
     reasons="Step 3 uses 'Safe Mode' with no explanation or how-to; the page links a separate Apple guide for it.",
     fix="Step 3: 'If it still will not delete, restart your Mac and try again.' Then add one line: 'If that does not work, Apple has a guide called start up in Safe Mode: https://support.apple.com/en-us/116946.' Add that URL as a second source."),
 rec("tr125-a", ["Open Storage (System Settings > General > Storage) to see what uses space", "Delete files in Downloads", "Delete or uninstall unused apps",
                 "Remove old iPhone/iPad backups", "Empty the Trash"],
     sc={"actionable": 1}, dec="revise",
     reasons="Step 4 'Delete old iPhone or iPad backups, if your Mac stores any' gives no starting point; the page gives no steps for it either.",
     fix="Remove step 4 (backups) since the cited page gives no way to do it, or add it only with a second Apple source that has the steps. Renumber the Trash step."),
 rec("tr125-c", ["Apple menu > About This Mac (older than Ventura)", "Click Storage", "Click More Info next to a category", "Delete unneeded files/apps", "Empty Trash"]),
 rec("tr125-b", [], clar=True),
 rec("tr125-d", ["Open Storage (System Settings > General > Storage)", "Delete files in Downloads", "Delete or uninstall unused apps", "Empty the Trash"]),
 rec("tr125-e", ["Move large media (Photos library) to an external drive", "Check Storage afterward", "Apple has a separate guide for moving the Photos library"],
     [True, True, True], sc={"actionable": 1}, dec="revise",
     reasons="Step 2 'Move the photos and videos you want to keep onto the drive' is not a doable step for a user whose photos live in Photos; the reply only says to 'check that guide' without naming it. The page links the guide.",
     fix="Replace step 2 with: 'Move your Photos library to the external drive by following Apple's guide Move your Photos library to save space on your Mac: https://support.apple.com/en-us/108345.' Remove 'check that guide before you move yours'. Add that URL as a second source; keep step 1 and the Storage check."),
 rec("tr125-r", ["Apple menu > About This Mac", "Click Storage"]),
 rec("tr126-a", LPM + ["Optionally set On power adapter too", "Click battery icon in menu bar to check"]),
 rec("tr126-c", LPM_OLD),
 rec("tr126-b", [], clar=True),
 rec("tr126-d", LPM, sc={"actionable": 1}, dec="revise",
     reasons="Last line 'If your Mac says System Preferences instead of System Settings, choose that.' leaves an older-macOS user stuck: on those Macs the steps differ (sidebar Battery/Power Adapter, and the option is called Low Power).",
     fix="Replace the last line with: 'If your Apple menu says System Preferences instead of System Settings, tell me and I will give you the steps for that.'"),
 rec("tr126-e", ["Apple menu > System Settings", "Click Battery", "Open On power adapter pop-up under Energy Mode", "Choose Low Power Mode", "Leave On battery unchanged"]),
 rec("tr126-r", LPM_OLD),
 rec("tr127-a", TM, [True, True, True, True, True, False, True], sc={"actionable": 1, "steps": 1}, dec="revise",
     reasons="Reply says 'Your Mac may ask whether to erase the drive' but never says what to do; page: 'Either erase it or select a different backup disk or volume.'",
     fix="Replace that sentence with: 'If your Mac asks whether to erase the drive, erasing wipes everything on it. Erase only if you do not need anything on it, or choose a different backup disk instead.'"),
 rec("tr127-c", ["Click the Time Machine menu in the menu bar (critical)", "Choose Back Up Now (critical)"]),
 rec("tr127-b", [], clar=True),
 rec("tr127-d", TM, [True, True, True, True, True, False, True], sc={"steps": 1}, dec="revise",
     reasons="Conditional erase prompt step from the page is omitted, so a user who sees it has no guidance.",
     fix="Add after step 5: 'If your Mac asks whether to erase the drive, erasing wipes everything on it. Erase only if you do not need anything on it, or choose a different backup disk instead.'"),
 rec("tr127-e", TM + ["Turn on Encrypt Backup and create a password; keep it for restoring"], [True, True, True, True, True, False, True, True],
     sc={"steps": 1}, dec="revise",
     reasons="Erase prompt guidance omitted; this user has the drive 'plugged in already' and may have used it before.",
     fix="Add after step 4: 'If your Mac asks whether to erase the drive, erasing wipes everything on it. Erase only if you do not need anything on it, or choose a different backup disk instead.'"),
 rec("tr127-r", ["Do not erase if drive has needed files", "Select a different backup disk or volume", "Use a drive only for Time Machine"]),
]
