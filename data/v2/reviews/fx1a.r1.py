S2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
P = {"source": "pass", "safety": "pass", "duplicate": "pass"}

def sc(**kw):
    d = dict(S2)
    d.update(kw)
    return d

def rec(id, ra, cov, sc_, dec, gates=None, unsup=None, reasons="", fix="", nc=False):
    return {
        "id": id, "required_actions": ra, "covered": cov, "needs_clarification": nc,
        "gates": gates or dict(P), "unsupported_claims": unsup or [],
        "scores": sc_, "decision": dec, "reasons": reasons, "fix": fix,
    }

SAM = ["Open the Settings app (critical)", "Tap Display (critical)", "Tap Font size and style (critical)",
       "Adjust the options to make the font bigger or bold (critical)"]
GEAR = "'Its icon looks like a gear.' -> the Samsung page never describes the Settings icon (text or image alt text)."
GEARFIX = "Delete the sentence 'Its icon looks like a gear.' from step 1; keep 'Open the **Settings** app.'"

AND = ["Press a volume button (critical)", "Tap the Menu icon at the right of the volume bar (critical)",
       "Slide Ring Volume up (critical)", "If set to vibrate/mute: tap the Ring icon above the slider, turn off Vibrate or turn on Ring"]
MORE = "'It may say **More**.' -> the Google page says only the 'Menu' icon for the volume bar; 'More' is not given for it."
MOREFIX = "Delete 'It may say **More**.' from the Menu-icon step."

MSG = ["Open Google Messages (critical)", "Open or start a conversation (critical)", "Tap Gallery (critical)",
       "Select a photo (critical)", "Tap Send (critical)"]
PHOTOS = "'Your photos will appear.' -> the Google page does not say what appears after tapping Gallery."

IPH = ["Press the correct button pair at the same time (critical)", "Release both buttons quickly (critical)",
       "Find it in Photos > Collections > Media Types > Screenshots"]

REVIEWS = [
 rec("tr001-c", SAM, [True]*4, sc(), "revise", {"source":"fail","safety":"pass","duplicate":"pass"}, [GEAR],
     "Gear-icon description is unsupported by the cited page.", GEARFIX),
 rec("tr001-b", [], [], sc(steps="NA"), "keep", nc=True),
 rec("tr001-d", SAM, [True]*4, sc(), "revise", {"source":"fail","safety":"pass","duplicate":"pass"}, [GEAR],
     "Gear-icon description is unsupported by the cited page.", GEARFIX, nc=True),
 rec("tr001-e", SAM, [True]*4, sc(), "revise", {"source":"fail","safety":"pass","duplicate":"pass"}, [GEAR],
     "Gear-icon description is unsupported by the cited page. The Font style / download-fonts warning is supported.", GEARFIX),
 rec("tr001-r", ["Acknowledge menu names differ by model and software version", "Point to Samsung Support (Live Chat, Email, Find a Support Center) if Font size and style is missing"],
     [True, True], sc(steps=1, actionable=1), "revise", {"source":"fail","safety":"pass","duplicate":"pass"},
     [GEAR + " (first assistant turn)",
      "'Stay on the **Display** screen and look through the whole list for any choice about the font or the size of the writing. If you find one, tap it and make the font bigger there.' -> not on the page; the page has no troubleshooting steps and names no alternative item."],
     "Final reply adds an invented search-the-list step. The page gives no troubleshooting, so only the model-differences note and Samsung Support contact are supported.",
     "In the first assistant turn delete 'Its icon looks like a gear.' In the final reply delete numbered steps 1 and 2 (look through Display list). Keep: menus differ by model and software version; then give Samsung Support options as the page lists them: Live Chat, Email, and Find a Support Center (the page has no phone number, so say 'Call' only as a link on Samsung's Contact page or drop it). Ask the user to tell you what they see only if no invented steps are added.")
]

REVIEWS += [
 rec("tr002-a", AND, [True]*4, sc(), "revise", {"source":"fail","safety":"pass","duplicate":"pass"}, [MORE],
     "Unsupported 'More' label.", MOREFIX + " Optionally add: if there is no Menu icon, the phone has older software and the steps are Down arrow > Ring (page's older-version steps)."),
 rec("tr002-c", ["Press a volume button (critical)", "Tap the Down arrow at the right of the volume bar (critical)", "Slide Ring up (critical)", "Optional: Settings > Sound"],
     [True]*4, sc(), "keep"),
 rec("tr002-d", AND, [True]*4, sc(), "revise", {"source":"fail","safety":"pass","duplicate":"pass"}, [MORE + " (final reply)"],
     "Unsupported 'More' label.", MOREFIX, nc=True),
 rec("tr002-e", AND[:3], [True]*3, sc(), "revise", {"source":"fail","safety":"pass","duplicate":"pass"}, [MORE],
     "Unsupported 'More' label.", MOREFIX),
 rec("tr002-r", ["Press a volume button again (critical)", "Tap the Down arrow icon at the right (critical)", "Slide Ring up (critical)"],
     [True]*3, sc(), "revise", {"source":"fail","safety":"pass","duplicate":"pass"},
     [MORE + " (first assistant turn, repeated in the same turn's closing line context)"],
     "Earlier assistant turn contains the unsupported 'More' label. Final reply is correct and supported.",
     "In the first assistant turn delete 'It may say **More**.' Leave the final reply unchanged."),
]

REVIEWS += [
 rec("tr003-c", MSG, [True]*5, sc(), "revise", {"source":"fail","safety":"pass","duplicate":"pass"}, [PHOTOS],
     "Unsupported sentence about what appears after tapping Gallery.", "Delete 'Your photos will appear.' from step 3 (or replace with the page's wording: select a photo or take a picture)."),
 rec("tr003-b", [], [], sc(steps="NA"), "keep", nc=True),
 rec("tr003-d", MSG, [True]*5, sc(), "revise", {"source":"fail","safety":"pass","duplicate":"pass"}, [PHOTOS],
     "Unsupported sentence about what appears after tapping Gallery.", "Delete 'Your photos will appear.' from step 3.", nc=True),
 rec("tr003-e", MSG + ["Tap HD for less data (HD labeled Optimized for chat)"], [True]*6, sc(), "keep"),
 rec("tr003-r", ["Open the conversation (critical)", "Tap Gallery (critical)", "Select the photo (critical)", "Tap HD, choose HD+ (Original quality) (critical)", "Tap Send (critical)"],
     [True]*5, sc(actionable=1), "revise", {"source":"fail","safety":"pass","duplicate":"pass"},
     [PHOTOS + " (first assistant turn)"],
     "Earlier turn has an unsupported sentence; final reply step 1 bundles two actions ('Open your conversation with Carol and tap Gallery').",
     "First turn: delete 'Your photos will appear.' Final reply: split step 1 into 'Open your conversation with Carol.' and 'Tap Gallery.' and renumber."),
]

REVIEWS += [
 rec("tr004-a", IPH, [True]*3, sc(), "keep"),
 rec("tr004-c", IPH, [True]*3, sc(), "keep"),
 rec("tr004-d", IPH, [True]*3, sc(ask_or_answer=0), "revise", P, [],
     "A Home-button iPhone uses either the side button or the top button (page lists both: side+Home, top+Home). The user was asked only about the Home button, so the final reply guessed 'side button' (device-specific guess).",
     "Change the first assistant turn to one question that settles which: 'Is the button you press to wake the phone on the top edge or on the right side?' (keeping or dropping the Home-button question is fine if one question mark remains). In the final reply, use the answer: right side -> side button + Home button; top edge -> top button + Home button. Or, keep the current question and have the final reply give both pairs with a plain way to tell which applies.", nc=True),
 rec("tr004-e", IPH, [True]*3, sc(), "keep"),
 rec("tr004-r", ["Explain thumbnail on iOS 18 or earlier vs iOS 26 (critical)", "Check Photos > Collections > Media Types > Screenshots (critical)", "Retry with side + volume up if missing"],
     [True]*3, sc(), "keep"),
]

REVIEWS += [
 rec("tr005-a", ["Update browser (critical)", "Open Gmail again", "Try a different browser", "Clear cache and cookies, reopen Gmail", "Optional: extensions off, private window"],
     [True, True, True, True, False], sc(plain=1), "revise", P,
     ["'Clear your browser's cache and cookies' -> supported wording, but jargon is left unexplained for a low-confidence user."],
     "Unexplained jargon: 'cache and cookies'.",
     "Explain in plain words on first use, e.g. 'Clear your browser's saved website data (called cache and cookies), then open Gmail again.' Do not add menu paths (the page gives none)."),
 rec("tr005-c", ["Turn off extensions one at a time, reopening Gmail after each (critical)", "Optionally try a private/incognito window"],
     [True, True], sc(), "keep"),
 rec("tr005-d", ["Update browser", "Try a different browser", "Restart device", "Turn Wi-Fi off then on"],
     [True]*4, sc(ask_or_answer=1, realistic_user=1), "revise", P, [],
     "The user's problem is not receiving church-group emails; she never says Gmail will not load. The cited page is only about Gmail not loading, so the final reply assumes a problem the user did not describe, and the scenario does not match the page.",
     "Rewrite the user's first message so the problem is that the Gmail page will not open or load (not that mail stopped arriving), keeping the plain voice and the 'turned it off and on' detail. Keep the question for where she reads email and the address ending, or make it a single question. Final reply then stays as is.", nc=True),
 rec("tr005-e", ["Update browser", "Try a different browser", "Restart device", "Turn Wi-Fi off then on", "Optionally private window"],
     [True]*5, sc(), "keep"),
 rec("tr005-r", ["Restart router per manual (critical)", "Open Gmail again", "Connect to another network", "Contact ISP or Wi-Fi host if it continues"],
     [True]*4, sc(), "keep"),
]

BLUE = "'It may be a blue wireless icon or a menu option.' -> page says 'Many printers have a button that displays a blue wireless icon' for turning wireless on; 'menu option' appears on the page only for the wireless connectivity test."
BLUEFIX = "Change to: 'Look for a button on the printer that shows a blue wireless icon.'"
REVIEWS += [
 rec("tr006-a", ["Turn off, unplug printer; wait 30 seconds; plug in, turn on (critical)", "Check USB cable at both ends (critical)", "Check for error: ink, paper, cover, jam"],
     [True]*3, sc(), "keep"),
 rec("tr006-c", ["Make sure printer wireless is on (blue wireless icon button) (critical)", "Run the printer's wireless connectivity test", "Check the PC is online", "Same network as printer when extenders are used (critical)", "Power-cycle the printer: off, unplug, wait 30 seconds, plug in"],
     [True, True, True, True, False], sc(steps=1, actionable=1), "revise", {"source":"fail","safety":"pass","duplicate":"pass"},
     [BLUE],
     "Unsupported 'menu option' for turning wireless on; power-cycle step (page's first step) is missing; step 2 bundles running the test with a conditional check.",
     BLUEFIX + " Add the power cycle as step 1 (turn off, unplug, wait 30 seconds, plug in, turn on). Split step 2: 'Run the printer's built-in wireless test (many printers have a menu option for it).' and a separate 'If the test passes but it still will not print, make sure your laptop is online.'"),
 rec("tr006-d", ["Power-cycle printer (critical)", "USB cable firm at both ends", "Wireless option on", "Try printing again"],
     [True]*4, sc(), "revise", {"source":"fail","safety":"pass","duplicate":"pass"},
     ["'The green light is a good sign: it means the printer has power.' -> not on the page; a green light can mean other things.",
      BLUE],
     "Earlier assistant turn asserts what the green light means (unsupported), and final reply has the 'menu option' error.",
     "First turn: delete 'The green light is a good sign: it means the printer has power.' (e.g. say 'Let's get that boarding pass printed.'). Final reply step 5: " + BLUEFIX, nc=True),
 rec("tr006-e", ["Power-cycle printer (critical)", "USB cable firm at both ends (critical)", "Check error: ink, paper, cover, jam", "Try printing again"],
     [True]*4, sc(), "keep"),
 rec("tr006-r", ["Remove: Start > Settings > Bluetooth & devices > Printers & scanners, select printer, Remove, Yes (critical)", "Printer on and connected, Add device (critical)", "Wait for search; Add device next to printer (critical)", "If not listed, Add manually and follow the prompts"],
     [True, True, True, False], sc(steps=1), "revise", {"source":"fail","safety":"pass","duplicate":"pass"},
     [BLUE + " (first assistant turn, step 5)"],
     "Earlier turn has the 'menu option' error. Final reply stops at 'Add manually' with no way forward for a user whose printer is not listed, and does not mention the Windows 11 troubleshooter (Get Help app) that the page says to try first.",
     "First turn step 5: " + BLUEFIX + " Final reply: after 'Add manually', add the page's next step in plain words (choose 'Add a local printer or network printer with manual settings', pick the USB port, choose maker and model, print a test page) or tell the user to say what appears so you can continue. Optionally start the final reply by offering the Get Help printer troubleshooter for Windows 11 (page: aka.ms/PrinterConnection)."),
]
