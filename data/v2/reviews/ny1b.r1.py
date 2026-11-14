G = {"source": "pass", "safety": "pass", "duplicate": "pass"}
S2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
SC = {"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}

def rec(id, ra, cov=None, nc=False, gates=None, uns=None, scores=None, dec="keep", reasons="", fix=""):
    return {"id": id, "required_actions": ra, "covered": cov if cov is not None else [True] * len(ra),
            "needs_clarification": nc, "gates": gates or dict(G), "unsupported_claims": uns or [],
            "scores": scores or dict(S2), "decision": dec, "reasons": reasons, "fix": fix}

def sc(**k):
    d = dict(S2); d.update(k); return d

def gs(**k):
    d = dict(G); d.update(k); return d

BT_IPHONE = ["Turn the accessory on and put it in pairing/discoverable mode, per its manual (critical)",
             "Open Settings, tap Bluetooth, make sure Bluetooth is on (critical)",
             "Under My Devices find the accessory (critical)",
             "Tap the accessory's name (critical)",
             "If prompted, enter the PIN or passcode from the manual or online instructions"]
BT_MAC = ["Turn the device on and make it discoverable (critical)",
          "Apple menu > System Settings > Bluetooth in sidebar (may need to scroll down) (critical)",
          "Hover over the device in the list and click Connect (critical)",
          "If prompted, click Accept or enter the number sequence and press Enter"]
TFA = ["Open Settings", "Tap your name", "Tap Sign-In & Security", "Turn on two-factor authentication and follow the onscreen prompts (critical)"]
PW18 = ["Open Passwords app (critical)", "Unlock with Face ID, Touch ID or passcode (critical)", "Choose a category (or All), then select the website/app (critical)"]
PW17 = ["Settings, scroll down, tap Passwords (critical)", "Authenticate with Face ID, Touch ID or passcode", "Select the website or app (critical)"]
FRNH = ["Press and release volume button closest to top button (critical)", "Press and release volume button farthest from top button (critical)", "Press and hold top button until Apple logo appears (critical)"]
SPAM_UNOPENED = ["Open Messages", "Swipe left on the message, tap the Delete button (critical)", "Tap Delete and Report Spam (critical)"]
BLOCK = ["Open the conversation and tap the person's icon at the top", "Tap Info, scroll down, tap Block Contact (critical)"]

REVIEWS = [
 rec("tr128-a", BT_IPHONE),
 rec("tr128-c", BT_IPHONE),
 rec("tr128-b", [], nc=True, scores=dict(SC)),
 rec("tr128-d", BT_IPHONE),
 rec("tr128-e", ["Find the PIN/passcode in the speaker's manual or online instructions (critical)", "Enter the PIN/passcode at the prompt (critical)"],
     uns=[], scores=sc(actionable=1, constraints=2, plain=1), dec="revise",
     reasons="The user is already at the PIN prompt, but the reply restarts from Settings > Bluetooth > My Devices (steps 2-4), which are redundant and may make the user leave the prompt. Steps 2-4 are extra text.",
     fix="Rewrite so the reply starts from the user's current screen: (1) Look up the speaker's PIN or passcode in its online instructions (the maker's website or search the speaker's model name with 'manual'); (2) go back to the pairing prompt on the iPhone and enter the PIN or passcode. Remove the Settings/Bluetooth/My Devices steps. Keep the line that the code is in the manual or online instructions (page: 'check the accessory's manual or online instructions'). If the prompt has closed: Settings, Bluetooth, tap the speaker's name under My Devices, enter the code."),
 rec("tr128-r", ["Make sure accessory is on", "Put it in discovery/pairing mode again", "Look under My Devices again in Settings > Bluetooth", "Tap the name"],
     gates=gs(source="fail"), uns=["'Make sure the headphones are turned on and charged.' -> 'charged' is not on the cited page HT204091 (page only says to check manual/online instructions for making it discoverable)."],
     scores=sc(), dec="revise", reasons="Charge requirement is not on the cited page. It is supported on a different official Apple page.",
     fix="Add https://support.apple.com/en-us/111804 as a second source (it says: make sure the accessory is on and fully charged or plugged in; keep it near the iPhone; restart the accessory by turning it off and on; put it in discovery mode). Keep the reply as is otherwise. Optionally say 'Keep the headphones close to your iPhone.'"),
 rec("tr129-a", BT_MAC, gates=gs(source="fail"),
     uns=["'Click the Apple menu at the top left of the screen' -> page gives no screen position for the Apple menu."],
     dec="revise", reasons="Unsupported position claim.", fix="Change step 2 to 'Click the **Apple menu**, then choose **System Settings**.' (remove 'at the top left of the screen')."),
 rec("tr129-c", BT_MAC + ["Open System Settings, click Sound in the sidebar", "Click Output", "Select the speaker from the list (critical)"],
     gates=gs(source="fail"), uns=["'Back in the sidebar, click **Sound**. You may need to scroll down.' -> the page only says scrolling may be needed for Bluetooth, not Sound."],
     dec="revise", reasons="Unsupported scroll claim for Sound.", fix="Step 6: 'Back in the sidebar, click **Sound**.' Remove 'You may need to scroll down.' from step 6. Keep the rest."),
 rec("tr129-b", [], nc=True, scores=dict(SC)),
 rec("tr129-d", BT_MAC + ["Apple Magic Mouse alternative: connect with cable to USB-C port, turn on, check power switch is green, unplug when notified"],
     cov=[True, True, True, True, False], gates=gs(source="fail"),
     uns=["'It pairs by itself' -> page does not say this; it says to connect with the cable, turn the device on, check that the power switch is green, and unplug when you get a notification."],
     scores=sc(steps=1), dec="revise", reasons="Magic Mouse note is paraphrased beyond the page and drops the power-switch check; 'pairs by itself' is unsupported.",
     fix="Replace the last paragraph with: 'If your mouse is an Apple Magic Mouse, you can use a cable instead: plug it into your Mac's USB-C port (you may need an adapter), turn the mouse on and check that its power switch shows green. When a notification appears, you can unplug the cable and use the mouse wirelessly.' Remove 'It pairs by itself'."),
 rec("tr129-e", ["Make sure device is on", "Click the Bluetooth status icon in Control Center (critical)", "Select the device (critical)"]),
 rec("tr129-r", ["Scroll down in the System Settings sidebar", "Click Bluetooth", "Hover over device and click Connect"]),
 rec("tr130-a", TFA, gates=gs(source="fail"),
     uns=["'If you do not see that option, your account may already use it. Most accounts do.' -> page says 'Many accounts already have two-factor authentication'; it says nothing about the option being hidden, and 'Most' is not supported."],
     dec="revise", reasons="Unsupported claim about the missing option and 'Most accounts'.",
     fix="Replace the last line with 'Many accounts already have two-factor authentication turned on, so you may not need to do this.' (the wording the page supports)."),
 rec("tr130-c", TFA),
 rec("tr130-b", [], nc=True, scores=dict(SC)),
 rec("tr130-d", TFA, gates=gs(source="fail"),
     uns=["'Most accounts already use two-factor authentication' -> page says 'Many accounts already have it'."],
     dec="revise", reasons="'Most' is stronger than the page.", fix="Change last line to 'Many accounts already have two-factor authentication turned on, so you may not need to do this.'"),
 rec("tr130-e", TFA + ["Tell the user: can lower account security only within two weeks of enrollment; cannot be removed if account was created with 2FA"]),
 rec("tr130-r", ["Explain that many accounts already have it on so the option may not be needed", "Note: if the account was created with 2FA, it cannot be removed"],
     gates=gs(source="fail"),
     uns=["'That is likely because you do not need it. Most accounts already use two-factor authentication, so the option may not appear.' -> page does not say the option may not appear; 'Most' not supported.", "'If your account was created with two-factor authentication, it is already on' -> page says it cannot be turned off/removed; 'already on' is a mild inference."],
     scores=sc(steps=1), dec="revise", reasons="The cited page gives no troubleshooting for the missing option; the reply states an unsupported cause and 'Most'.",
     fix="Rewrite the final reply to hedge only what the page says: 'Many accounts already have two-factor authentication turned on, so you may not need to turn it on. To check, go to Settings, tap your name, tap Sign-In & Security. If your account was created with two-factor authentication, Apple says this extra protection can't be removed.' Do not say the option 'may not appear' or 'most accounts'."),
 rec("tr131-a", PW18, gates=gs(), scores=sc(plain=1, constraints=1), dec="revise",
     reasons="The user said they have the newest iOS, but the reply adds an iOS 17 or earlier line that is not needed.",
     fix="Delete the last paragraph ('If your iPhone is on iOS 17 or earlier ...'). Keep steps 1-4."),
 rec("tr131-c", PW17),
 rec("tr131-b", [], nc=True, scores=dict(SC)),
 rec("tr131-d", PW18),
 rec("tr131-e", ["Settings > tap your name > iCloud", "Under Saved to iCloud choose Passwords (iOS 17 or earlier: Passwords and Keychain)", "Turn on Sync this iPhone"],
     cov=[True, False, False], gates=gs(source="fail"),
     uns=["'Tap **Passwords and Keychain**.' -> on current iOS the label is 'Passwords' under 'Saved to iCloud'; 'Passwords and Keychain' is iOS 17 or earlier (https://support.apple.com/en-us/109016).", "'Turn on **iCloud Keychain**.' -> the switch is 'Sync this iPhone' per 109016, not 'iCloud Keychain'.", "'you may need to approve it first, using iCloud Keychain or the passcode of your old device' -> not on either page for iPhone."],
     scores=sc(steps=0, actionable=1), dec="revise", reasons="Wrong labels for the sync steps and an unsupported approval claim. The cited page HT/104955 only says to make sure iCloud Keychain is on, with no path.",
     fix="Add https://support.apple.com/en-us/109016 as second source. Steps: 1. Open Settings. 2. Tap your name. 3. Tap iCloud. 4. Under 'Saved to iCloud', tap Passwords (on iOS 17 or earlier, tap Passwords and Keychain). 5. Turn on 'Sync this iPhone' (you may need your passcode or Apple Account password). Add: do the same on the iPad. Remove the approval sentence. The 109016 page says two-factor authentication must be on for the Apple Account."),
 rec("tr131-r", PW18 + ["Tap All", "Tap Deleted", "Make sure iCloud Keychain/passwords sync is on", "Shared Group needs iOS 17 or later"],
     cov=[True, True, True, True, True, False, True], gates=gs(source="fail"),
     uns=["'open **Settings**, tap your name, tap **iCloud**, tap **Passwords and Keychain**, and make sure **iCloud Keychain** is on' -> labels not on the cited page; on current iOS (user said iOS 18) the path is iCloud > Passwords > 'Sync this iPhone' per https://support.apple.com/en-us/109016."],
     scores=sc(steps=1), dec="revise", reasons="Sync path and labels are wrong for iOS 18.",
     fix="Add https://support.apple.com/en-us/109016 as second source. Change step 3 to: 'If you use more than one Apple device, open **Settings**, tap your name, tap **iCloud**, and under **Saved to iCloud** tap **Passwords**. Make sure **Sync this iPhone** is on.' Keep the Deleted check and the Shared Group iOS 17 line."),
 rec("tr132-a", FRNH + ["If it still will not turn on, charge it (up to an hour)"]),
 rec("tr132-c", ["Press and hold Home button and top button together (critical)", "Keep holding until Apple logo appears (critical)", "If still will not turn on, charge up to an hour"]),
 rec("tr132-b", [], nc=True, scores=dict(SC)),
 rec("tr132-d", FRNH + ["If it still will not turn on, charge it (up to an hour)"]),
 rec("tr132-e", FRNH),
 rec("tr132-r", ["Charge the iPad (up to an hour)", "Repeat force restart", "If still not on, get service from Apple"]),
 rec("tr133-a", SPAM_UNOPENED + ["Reporting does not stop the sender; block the contact"], gates=gs(source="fail"),
     uns=["'the **Delete** button, the trash can icon' -> page only says 'the Delete button'; no trash can icon is described."],
     dec="revise", reasons="Unsupported icon description.", fix="Change step 3 to 'Tap the **Delete** button.' Remove 'the trash can icon'."),
 rec("tr133-c", SPAM_UNOPENED + BLOCK, cov=[True, True, True, True, True], gates=gs(source="fail"),
     uns=["'the **Delete** button, the trash can icon' -> not on page.", "Order: block first by 'Open the conversation with the sender', then 'swipe left on the message' -> the user said they have not opened the latest message; opening the conversation opens it, and the page uses a different path (Report Spam link) for opened messages."],
     scores=sc(constraints=1), dec="revise", reasons="Block-first order conflicts with the user's 'have not opened' constraint; trash can icon unsupported.",
     fix="Put the report steps first (Messages list, swipe left on the message, tap the Delete button, tap Delete and Report Spam), then 'Now block them' with the Block Contact steps. Remove 'the trash can icon'. Keep the line that reporting alone will not stop the sender."),
 rec("tr133-b", [], nc=True, scores=dict(SC)),
 rec("tr133-d", ["Report: " + SPAM_UNOPENED[1], SPAM_UNOPENED[2]] + BLOCK, cov=[True, True, True, True], gates=gs(source="fail"),
     uns=["'the **Delete** button, the trash can icon' -> not on page.", "Reply assumes the message is unopened (swipe-left path); the page has a different path for opened messages (open it, tap Report Spam link, tap Delete and Report Spam), and blocking first opens the conversation."],
     scores=sc(steps=1, ask_or_answer=1), dec="revise", reasons="Whether the text was opened changes the report steps and the reply does not address it; trash can icon unsupported; block-first order.",
     fix="Report first, then block. Give the unopened path (swipe left, tap the Delete button, tap Delete and Report Spam) and one line for an opened message: 'If you already opened it, open the message, tap Report Spam at the bottom, then tap Delete and Report Spam.' Then the Block Contact steps. Remove 'the trash can icon'. Change the lead-in to say reporting does not stop the sender, so block them afterwards."),
 rec("tr133-e", ["Tell user cannot report after replying", "Block: conversation > person's icon > Info > Block Contact (critical)"]),
 rec("tr133-r", ["Explain Report Spam link only appears for unknown senders; cannot report after replying", "For SMS/MMS/RCS without option, contact carrier", "Block the sender: person's icon, Info, Block Contact"]),
]
