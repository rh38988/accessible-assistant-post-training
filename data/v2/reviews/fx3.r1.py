S2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
OK = {"source": "pass", "safety": "pass", "duplicate": "pass"}


def R(id, req, cov=None, gates=None, unsup=None, scores=None, decision="keep", reasons="", fix="", nc=False):
    return {
        "id": id,
        "required_actions": req,
        "covered": cov if cov is not None else [True] * len(req),
        "needs_clarification": nc,
        "gates": gates or dict(OK),
        "unsupported_claims": unsup or [],
        "scores": scores or dict(S2),
        "decision": decision,
        "reasons": reasons,
        "fix": fix,
    }


UPD = ["Connect to Wi-Fi (critical)", "Charge to at least 75% (critical)", "Open Settings", "Tap System, then Software updates", "Follow the on-screen instructions"]
WIN_UPD = ["Start > Settings > Windows Update (critical)", "Select Check for Windows updates (critical)", "If updates are available, select Download & install (critical)", "Restart if prompted"]
PRN = ["Turn on printer; USB plugged in, or wireless on same network", "Start > Settings > Bluetooth & devices > Printers & scanners (critical)", "Add device next to Add a printer & scanner (critical)", "Wait a few minutes", "Add Device next to the printer", "If not listed: Add a new device manually, follow Add Printer window"]
FTC_FAM = ["Do not send money (critical)", "Hang up, call the person at a number you know is theirs (critical)", "If unreachable, contact through another family member or friends", "Warning sign: wire, crypto, gift card payments", "Report at ReportFraud.ftc.gov"]

REVIEWS = [
    R("tr033-e", UPD + ["Pixel installs in background, active at next restart"]),
    R("tr033-r", ["Open Settings app", "Tap System, then Software updates", "Follow on-screen instructions", "Possible reasons nothing shows: older device, schedule varies by maker/carrier"]),
    R("tr034-e", WIN_UPD[:2] + ["Do not select Download & install until ready (constraint)"]),
    R("tr034-r", ["Run Windows Update troubleshooter (Settings > System > Troubleshoot > Other troubleshooters > Run)", "Check internet connection", "Check for updates again"],
      [False, False, False],
      gates={"source": "fail", "safety": "pass", "duplicate": "pass"},
      unsup=["'Click Start, then Settings, then System, then Troubleshoot, then Other troubleshooters. Click Run next to Windows Update.' -> the cited page has no troubleshooter steps; it only points to other articles",
             "'Go to Start, Settings, Network & Internet, Wi-Fi, and reconnect if needed.' -> cited page has no network guidance",
             "'click Check for updates again' -> the cited page's button is 'Check for Windows updates'"],
      decision="revise",
      reasons="The error-recovery steps are not on the cited page (it only refers to the 'Troubleshoot problems updating Windows' article). Those steps ARE on that Microsoft article, so the content is correct but the example cites the wrong source.",
      fix="Add a second source: https://support.microsoft.com/en-us/windows/troubleshoot-problems-updating-windows-188c2b0f-10a7-d72f-65b8-32d177eb136c (it lists Settings > System > Troubleshoot > Other troubleshooters > Windows Update > Run, and Network & Internet > Wi-Fi to reconnect). In final-reply step 4 use the label 'Check for Windows updates' as on the install page (or 'Check for updates' only if you cite the troubleshoot article for it). Keep the rest."),
    R("tr035-e", ["Open Google Photos", "Tap profile picture or initial", "Photos settings > Backup", "Turn Backup on", "Backup > Mobile data usage > set daily limit", "Turn off Back up videos over data", "Optional: Back up while roaming"]),
    R("tr035-r", ["Tap the status to see details", "If storage is full: buy more storage or clean up your storage space", "Battery optimization: Settings > search battery optimization > Battery optimization > All apps > Photos > Don't optimize > Done"]),
    R("tr036-e", PRN[:2] + PRN[2:5]),
    R("tr036-r", [PRN[5], "Printer on and connected"]),
    R("tr037-e", ["Open Gmail, tap Compose (bottom right)", "Tap Attach (top right)", "Choose Photos", "Select photos (up to five at a time)", "25 MB limit becomes a Drive link"]),
    R("tr037-r", ["Tap Close next to the attachment name to remove it", "Attach > Photos, pick picture again", "Send again", "Storage may be full: delete large attachments, empty Trash and Spam"]),
    R("tr038-e", ["Google cannot help by phone; no number (critical)", "Do not give out passwords or verification codes; beware recovery services", "Go to the recovery page URL", "Answer questions as accurately as you can", "Set a strong new password not used before with this account"]),
    R("tr038-r", ["Try the recovery questions again (no limit on tries, wrong guesses do not end it)", "Read the tips at support.google.com/accounts/answer/7299973", "Recovery-info changes can take up to 7 days; try again in a few days"]),
    R("tr039-e", FTC_FAM),
    R("tr039-r", ["Report to the wire transfer company immediately, say a scammer tricked you, ask for a refund (critical)", "Check on the granddaughter via a known number or relatives", "Report to ReportFraud.ftc.gov", "Do not send more money"],
      gates={"source": "fail", "safety": "pass", "duplicate": "pass"},
      unsup=["'Report it to the wire transfer company immediately. Tell them a scammer tricked you, and ask for a refund.' -> not on the cited FTC family-emergency alert, which says nothing about wire companies or refunds"],
      decision="revise",
      reasons="The key recovery step is accurate but is not on the cited page; it is on another FTC page.",
      fix="Add a second source: https://consumer.ftc.gov/articles/what-do-if-you-were-scammed (wire transfer: 'Report it to the wire transfer company immediately', 'Tell them a scammer tricked you into sending money', 'Ask them to refund your money'). No change to the reply text is needed."),
    R("tr040-e", ["Do not click the link or give information", "Check each order at the retailer or your account there", "Report: messaging app report option or forward to 7726", "Report at ReportFraud.ftc.gov"]),
    R("tr040-r", ["Contact the credit card issuer immediately using the number on the back of the card or the account/app (critical)", "Tell them what happened and ask for a refund", "Report the text (report option or 7726)", "Report at ReportFraud.ftc.gov"],
      gates={"source": "fail", "safety": "pass", "duplicate": "pass"},
      unsup=["'Report it to the credit card issuer immediately. Call the number on the back of your card... ask for a refund.' -> not on the cited USPS text-scam alert"],
      decision="revise",
      reasons="The credit card steps are correct but are not on the cited page; they are on another FTC page.",
      fix="Add a second source: https://consumer.ftc.gov/articles/what-do-if-you-were-scammed (credit card: 'Report it to the credit card issuer immediately', 'Use the number on the back of your card or log in to your account online or through their app', 'Ask them to refund your money'). No change to the reply text is needed."),
    R("tr041-e", ["Do not buy gift cards or send codes (critical)", "Slow down; no real business or agency demands gift card payment", "Contact the nephew at a number you know", "Report at ReportFraud.ftc.gov", "If already paid: report to gift card company, ask for money back, keep a copy of card and receipt"],
      gates={"source": "fail", "safety": "pass", "duplicate": "pass"},
      unsup=["'Keep the cards and the receipt.' -> page says 'Always keep a copy of your gift card and store receipt'"],
      decision="revise",
      reasons="One small wording that differs from the source advice.",
      fix="Change the last sentence to: 'Keep a copy of the gift card and the store receipt.' Leave the rest unchanged."),
    R("tr042-e", ["Group first: Settings > your name > Family > Continue, follow screen", "Settings > Family > Add Member", "Create Child Account, follow prompts", "Finish parental controls and location sharing prompts"]),
    R("tr042-r", ["Settings > Family, tap her name to see invitation status", "Tap Resend Invitation", "She accepts from the email/text, or Settings > name > Invitations"]),
    R("tr043-e", ["Open Contacts", "Tap Add", "Enter name and email or phone number", "Tap Save", "Optional: Add fields"], [True] * 5,
      gates={"source": "fail", "safety": "pass", "duplicate": "pass"},
      unsup=["'open her contact and tap the field to edit it' -> the page has no steps for editing an existing contact; 'tap the field to edit' is only part of entering details while adding a new contact (it links to a separate Edit or delete contacts article)"],
      decision="revise",
      reasons="The extra sentence about editing an existing contact is not supported.",
      fix="Change the last paragraph to: 'If you want to add more details, such as a street address or notes, tap **Add fields** before you tap **Save**.' Remove 'open her contact and tap the field to edit it'."),
    R("tr043-r", ["Open Contacts, tap the contact", "Contact settings (top right) > Move to another account", "Choose your Google Account", "Warn: moving deletes it from the original account"]),
    R("tr045-e", ["Open the Messages conversation", "Tap the contact at the top", "Scroll down and tap Block Caller", "Blocked person is not told; messages not delivered"]),
    R("tr045-r", ["Settings > Privacy & Security", "Blocked Contacts", "Edit", "Tap delete button next to the number", "Tap Unblock"]),
    R("tr046-e", ["Phone app > More", "Settings > Blocked numbers", "Turn on Unknown"]),
    R("tr046-r", ["Phone > More > Settings > Blocked numbers", "Next to the number tap Clear", "Tap Unblock"]),
]
