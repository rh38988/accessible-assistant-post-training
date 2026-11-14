S2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
OK = {"source": "pass", "safety": "pass", "duplicate": "pass"}
BAD = {"source": "fail", "safety": "pass", "duplicate": "pass"}


def rec(id, ra, cov=None, ncl=False, gates=None, unsup=None, scores=None, dec="keep", reasons="", fix=""):
    return {
        "id": id, "required_actions": ra, "covered": cov if cov is not None else [True] * len(ra),
        "needs_clarification": ncl, "gates": gates or OK, "unsupported_claims": unsup or [],
        "scores": scores or dict(S2), "decision": dec, "reasons": reasons, "fix": fix,
    }


def ask(id, why):
    return rec(id, [], [], True, reasons="", fix="")


# ---------- Edge favorites ----------
EDGE_FAV_ADDR = ["Open Edge and go to the site (critical)", "Select the Add this page to favorites button in the address bar (critical)",
                 "Optionally rename or choose a folder", "Select Done (critical)"]
EDGE_FAV_MENU = ["Open Edge and go to the site (critical)", "Select Settings and more (critical)", "Select Favorites (critical)",
                 "Select More options (critical)", "Select Add this page to favorites (critical)"]

# ---------- Edge zoom ----------
ZOOM_UNS = ('"(the three dots menu)" -> the Edge page only says "select Settings and more" and shows an icon; it never describes it as three dots',
            '"(the plus sign)" -> the page says "Zoom in"; it does not describe the icon as a plus sign')
ZOOM_FIX = ('Delete the parentheticals "(the three dots menu)" and "(the plus sign)" and name the controls only by their labels: '
            '"Select **Settings and more**", then "Select **Zoom in**". Keep the keyboard tip (Ctrl and plus sign) as is.')

# ---------- Chrome Android ----------
DOTS_UNS = '"(the three dots)" -> the Chrome page labels the control "More" and shows an icon but never describes it as three dots'
DOTS_FIX = ('Remove "(the three dots)" everywhere in the reply and say only "tap **More**" (the page says: "To the right of the address bar, tap More, then Add to bookmarks"). '
            'Do not describe the icon.')

REVIEWS = [
    # ---- tr186 ----
    rec("tr186-a", EDGE_FAV_ADDR),
    rec("tr186-c", EDGE_FAV_MENU),
    rec("tr186-b", [], [], True, scores={"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}),
    rec("tr186-d", EDGE_FAV_ADDR),
    rec("tr186-e", EDGE_FAV_MENU),
    rec("tr186-r", EDGE_FAV_MENU),

    # ---- tr187 Chrome Android bookmark ----
    rec("tr187-a", ["Open Chrome and go to the page (critical)", "Tap More (critical)", "Tap Add to bookmarks (critical)"],
        gates=BAD, unsup=[DOTS_UNS], dec="revise", reasons="Unsupported icon description (three dots).", fix=DOTS_FIX),
    rec("tr187-c", ["Tap More next to address bar (critical)", "Tap Add to bookmarks (critical)", "Open Chrome", "At the top right tap More, then Bookmarks", "Tap the bookmark"],
        gates=BAD, unsup=[DOTS_UNS], dec="revise", reasons="Unsupported icon description (three dots).",
        fix=DOTS_FIX + " The 'open it again' steps are fine; you may add 'Tap a folder' before 'Tap the bookmark' as the page lists it."),
    rec("tr187-b", [], [], True, scores={"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}),
    rec("tr187-d", ["Open Chrome and go to the website (critical)", "Tap More (critical)", "Tap Add to bookmarks (critical)"],
        gates=BAD, unsup=[DOTS_UNS], dec="revise", reasons="Unsupported icon description (three dots).", fix=DOTS_FIX),
    rec("tr187-e", ["Tap More (to the right of the address bar) (critical)", "Tap Add to bookmarks (critical)", "Open Chrome (critical)",
                    "Swipe up on the address bar (bottom bar) (critical)", "Tap Bookmarks (critical)", "Tap a folder, tap the bookmark (critical)"],
        gates=BAD, unsup=[DOTS_UNS], dec="revise", reasons="Unsupported icon description (three dots).", fix=DOTS_FIX),
    rec("tr187-r", ["Open Chrome (critical)", "At the top right tap More, then Bookmarks (critical)", "Tap a folder (critical)", "Tap the bookmark (critical)",
                    "If address bar is at the bottom, swipe up on it and tap Bookmarks"],
        gates=BAD,
        unsup=['"Recently opened folders show first." -> the page only says that if you recently opened a folder you will find the same folder; other folders are reached with Back at the top left. It does not say recently opened folders are listed first',
               'Earlier assistant turn: "(the three dots)" -> icon never described as three dots on the page'],
        dec="revise", reasons="Unsupported claim about folder order; unsupported three dots description in the first assistant turn.",
        fix='In the final reply replace "Recently opened folders show first." with "If you opened a bookmarks folder recently, you will see that same folder. To see other folders, tap **Back** at the top left." '
            'In the first assistant turn remove "(the three dots)" and say only "tap **More**".'),

    # ---- tr188 Edge zoom ----
    rec("tr188-a", ["Select Settings and more (critical)", "Select Zoom in (critical)", "Repeat Zoom in until the size is right", "Or Ctrl and plus sign"],
        gates=BAD, unsup=list(ZOOM_UNS), dec="revise", reasons="Unsupported icon descriptions.", fix=ZOOM_FIX),
    rec("tr188-c", ["Hold Ctrl and press plus sign to zoom in (critical)", "Or Ctrl with mouse wheel up to zoom in; wheel down to zoom out"]),
    rec("tr188-b", [], [], True, scores={"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}),
    rec("tr188-d", ["Select Settings and more (critical)", "Select Zoom in (critical)", "Repeat Zoom in until the size is right"],
        gates=BAD, unsup=list(ZOOM_UNS), dec="revise", reasons="Unsupported icon descriptions.", fix=ZOOM_FIX),
    rec("tr188-e", ["Open Settings and more (critical)", "Select Settings (critical)", "Select Accessibility (critical)",
                    "Under Visibility, choose zoom level from Page zoom drop-down (critical)"]),
    rec("tr188-r", ["Press Ctrl and 0 to reset zoom to default (critical)"],
        gates=BAD,
        unsup=['"select **Zoom out** (the minus sign)" -> the page says "Zoom out" but never describes the icon as a minus sign',
               'Earlier assistant turn: "(the three dots menu)" and "(the plus sign)" -> not described on the page'],
        dec="revise", reasons="Unsupported icon description in the final reply and in the first assistant turn.",
        fix='In the final reply change to "select **Zoom out** until it looks right" (no "(the minus sign)"). In the first assistant turn delete "(the three dots menu)" and "(the plus sign)".'),

    # ---- tr189 Chrome pop-ups ----
    rec("tr189-a", ["More, then Settings (critical)", "Privacy and security (critical)", "Site Settings (critical)", "Pop-ups and redirects (critical)",
                    "Under Allowed to send pop-ups and use redirects, find the site (critical)", "Click More next to the site, then Block (critical)"]),
    rec("tr189-c", ["More, then Settings", "Privacy and security", "Site Settings", "Pop-ups and redirects",
                    "Click Add next to Not allowed to send pop-ups or use redirects (critical)", "Enter the site address (critical)", "Click Add (critical)"]),
    rec("tr189-b", [], [], True, scores={"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}),
    rec("tr189-d", ["More, then Settings", "Privacy and security, Site Settings, Pop-ups and redirects", "If the site is under Allowed to send pop-ups..., More then Block",
                    "If the site is not listed, click Add next to Not allowed to send pop-ups or use redirects, enter the address, click Add (critical)"],
        cov=[True, True, True, False], scores={"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        dec="revise", reasons="The reply only covers the allowed-list case. The user never said the site is in the allowed list, and the page has a second path for a site that is not listed. A user whose site is not listed is left with no steps.",
        fix='After step 5 add: "If you do not see the site in that list, next to **Not allowed to send pop-ups or use redirects** click **Add**, type the web address of the site, then click **Add**." Keep the rest.'),
    rec("tr189-e", ["Explain that on a work or school Chrome device the user cannot change the setting", "Ask the network administrator to change it"],
        scores=dict(S2)),
    rec("tr189-r", ["Go to the site", "Click View site information", "Next to Notifications, choose Block (critical)"],
        gates=BAD, unsup=['"Click **View site information** in the address bar." -> the page does not say where View site information is'],
        dec="revise", reasons="Unsupported location claim.", fix='Change step 2 to "Click **View site information**." (remove "in the address bar"). Change step 3 to "Next to **Notifications**, choose **Block**."'),

    # ---- tr190 default browser ----
    rec("tr190-a", ["Open Start, then Settings", "Apps, Default apps", "In search box under Set defaults for applications, enter Chrome", "Select Google Chrome",
                    "Next to Make Google Chrome your default browser, select Set default (critical)", "Review Set default file types or link types list (non-critical)"],
        cov=[True, True, True, True, True, False], gates=BAD,
        unsup=['"At the top, click **Set default**..." -> the page says "Next to Make Google Chrome your default browser", not "at the top"'],
        scores={"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        dec="revise", reasons="Missing the final review of file and link types; unsupported position claim.",
        fix='Change step 6 to "Next to **Make Google Chrome your default browser**, click **Set default**." and add step 7: "Look at the list called **Set default file types or link types** to check Chrome is set for the types you need."'),
    rec("tr190-c", ["Open Start, then Settings", "Open Default apps (System > Default apps or Apps > Default apps)", "At the bottom, under Web browser, select current browser (critical)", "In Choose an app window, select Google Chrome (critical)"]),
    rec("tr190-b", [], [], True, scores={"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}),
    rec("tr190-d", ["Open Start, then Settings", "Apps, Default apps", "In search box enter Chrome", "Select Google Chrome", "Next to Make Google Chrome your default browser, Set default (critical)", "Review file/link types list (non-critical)"],
        cov=[True, True, True, True, True, False], gates=BAD,
        unsup=['"At the top, click **Set default**..." -> the page says "Next to Make Google Chrome your default browser", not "at the top"'],
        scores={"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        dec="revise", reasons="Missing the final review of file and link types; unsupported position claim.",
        fix='Change step 5 to "Next to **Make Google Chrome your default browser**, click **Set default**." and add step 6: "Look at the list called **Set default file types or link types** to check Chrome is set for the types you need."'),
    rec("tr190-e", ["Open Start, then Settings", "Apps, Default apps", "Enter Chrome in the search box under Set defaults for applications", "Select Google Chrome",
                    "Set default next to Make Google Chrome your default browser (critical)", "Review file/link types list (non-critical)"],
        cov=[True, True, True, True, True, False], gates=BAD,
        unsup=['"At the top, click **Set default**." -> the page says "Next to Make Google Chrome your default browser", not "at the top"'],
        scores={"steps": 1, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2},
        dec="revise", reasons="Missing the file and link types review; unsupported position claim. The user wants it short, so add only one short line.",
        fix='Change step 5 to "Click **Set default** next to **Make Google Chrome your default browser**." and add a short step 6: "Check the **Set default file types or link types** list shows Chrome for the types you need." Do not add anything about downloading.'),
    rec("tr190-r", ["Review the Set default file types or link types list to confirm Chrome is set for the types needed"]),

    # ---- tr191 downloads ----
    rec("tr191-a", ["At top right click More (critical)", "Click Downloads (critical)", "Click file name to open", "Default folder is Downloads in user folder"],
        gates=BAD, unsup=['"(the three dots at the top right)" -> the page says "At the top right, click More" and shows an icon but never describes three dots'],
        dec="revise", reasons="Unsupported icon description.",
        fix='Change step 1 to "At the top right of Chrome, click **More**." Remove "the three dots".'),
    rec("tr191-c", ["State default save location: Downloads folder in the user folder on Mac", "At top right click More", "Click Downloads", "Click file name to open in default app"],
        gates=BAD, unsup=['"(the three dots at the top right)" -> never described as three dots on the page'],
        dec="revise", reasons="Unsupported icon description.",
        fix='Change step 1 to "At the top right of Chrome, click **More**." Remove "the three dots". Keep the rest.'),
    rec("tr191-b", [], [], True, scores={"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}),
    rec("tr191-d", ["At top right click More (critical)", "Click Downloads (critical)", "Click file name to open"],
        gates=BAD, unsup=['"(the three dots at the top right)" -> never described as three dots on the page'],
        dec="revise", reasons="Unsupported icon description.", fix='Change step 1 to "At the top right of Chrome, click **More**." Remove "the three dots".'),
    rec("tr191-e", ["Point to the file name in the download box at the top right (critical)", "Click Show in Folder (critical)"]),
    rec("tr191-r", ["At top right click More (critical)", "Click Downloads (critical)", "Click file name to open"],
        gates=BAD, unsup=['"(the three dots at the top right)" -> never described as three dots on the page'],
        dec="revise", reasons="Unsupported icon description.",
        fix='Change step 1 to "At the top right of Chrome, click **More**." Remove "the three dots". Optionally in the first assistant turn say "download tray" is the page name; "small download box" is fine.'),

    # ---- tr192 passwords ----
    rec("tr192-a", ["Sign in to the site, enter username and password", "Select Save when Chrome asks (critical)", "More at top right (critical)", "Passwords and autofill, then Google Password Manager (critical)",
                    "Under Passwords, select the site (critical)", "Select Show password icon (critical)"],
        gates=BAD, unsup=['"(the three dots at the top right)" -> never described as three dots on the page'],
        dec="revise", reasons="Unsupported icon description.", fix='Change step 1 of the second list to "At the top right of Chrome, click **More**." Remove "the three dots".'),
    rec("tr192-c", ["More, Passwords and autofill, Google Password Manager (critical)", "Select Add (critical)", "Enter website, username, password (critical)", "Select Save (critical)"],
        gates=BAD, unsup=['"(the three dots at the top right)" -> never described as three dots on the page'],
        dec="revise", reasons="Unsupported icon description.", fix='Change step 1 to "At the top right of Chrome, click **More**." Remove "the three dots". Keep the rest.'),
    rec("tr192-b", [], [], True, scores={"steps": "NA", "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}),
    rec("tr192-d", ["Sign in, enter username and password, Save (critical)", "More, Passwords and autofill, Google Password Manager", "Under Passwords select the site", "Select Show password icon"],
        gates=BAD, unsup=['"(the three dots at the top right)" -> never described as three dots on the page'],
        dec="revise", reasons="Unsupported icon description.", fix='Change step 1 of the second list to "At the top right of Chrome, click **More**." Remove "the three dots".'),
    rec("tr192-e", ["More, Passwords and autofill, Google Password Manager (critical)", "Select Settings (critical)", "Turn on Use Windows Hello when filling passwords (critical)", "Follow on-screen instructions to confirm (critical)"],
        gates=BAD, unsup=['"(the three dots at the top right)" -> never described as three dots on the page'],
        dec="revise", reasons="Unsupported icon description.", fix='Change step 1 to "At the top right of Chrome, click **More**." Remove "the three dots". Keep the rest.'),
    rec("tr192-r", ["More, Passwords and autofill, Google Password Manager (critical)", "Select Settings on the left (critical)", "Make sure Offer to save passwords and passkeys is on (critical)",
                    "Under Declined sites and apps, remove the site"],
        gates=BAD, unsup=['"(the three dots at the top right)" -> never described as three dots on the page'],
        dec="revise", reasons="Unsupported icon description.", fix='Change step 1 to "At the top right of Chrome, click **More**." Remove "the three dots". Keep the rest.'),
]
