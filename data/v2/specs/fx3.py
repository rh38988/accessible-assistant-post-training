"""New examples (e and r) for group 3 tasks. Batch fx3."""
TASKS = [
    {
        "task_id": "TR-033", "task_type": "software_update", "task": "Install a software update",
        "platform": "Android", "category": "technical_support", "sensitive": False,
        "source": {"title": "Android Help: Check & update your Android version", "url": "https://support.google.com/android/answer/7680439?hl=en"},
        "source_notes": """Before you start: connect to Wi-Fi and charge to at least 75%. Updates can be large and take a while.
From a notification: when an update notification appears, open it, then tap the update action.
From Settings (if you dismissed the notification or were offline): open Settings; tap System, then Software updates (update status appears here); follow the on-screen instructions.
Pixel phones and Pixel Tablet download and install updates in the background; they take effect the next time you restart. Other Android devices often restart automatically during installation; update takes effect when installation finishes.
If you don't see an update: check Software updates in Settings since the notification may have been cleared. If nothing appears, device may already be current, may have reached end of update support, or may be waiting for carrier or manufacturer to release it.
If a download fails: device retries automatically over the next few days and sends a notification; open it and tap the update action.
Not enough space: free up storage, then try again.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I have a Google Pixel and it says there's an update. I'm waiting on a call from my doctor's office and I don't want my phone restarting on me right now. How do I install it?",
                 """Good news: on a Pixel, updates download and install in the background, and the update only takes effect the next time you restart. So you can restart after your call.

Before you start, connect to Wi-Fi and make sure your battery is at least 75%.

1. Open the **Settings** app.
2. Tap **System**.
3. Tap **Software updates**. The update status shows here.
4. Follow the instructions on the screen.

When your call is done, restart the phone and the update will take effect.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "A box popped up on my Samsung Android phone saying a new Android version is ready. How do I install it from that message?",
                 """You can start it right from that message. Before you start, connect to Wi-Fi and make sure your battery is at least 75%.

1. Open the update notification.
2. Tap the update action on it.
3. Follow the instructions on the screen.

Your phone may restart on its own while the update installs.""",
                 "I swiped the message away by accident and now it's gone.",
                 """That's okay. The update is still available in Settings.

1. Open the **Settings** app.
2. Tap **System**, then **Software updates**. The update status appears here.
3. Follow the instructions on the screen.

If nothing shows up, your phone may already be up to date, it may no longer get updates, or it may be waiting for your carrier or phone maker to release the update.""",
             ]},
        ],
    },
    {
        "task_id": "TR-034", "task_type": "software_update", "task": "Install Windows updates",
        "platform": "Windows 11", "category": "technical_support", "sensitive": False,
        "source": {"title": "Microsoft Support: Install Windows Updates", "url": "https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates"},
        "source_notes": """Install page: 1. Select Start > Settings > Windows Update, then select Check for Windows updates. 2. If updates are available, select Download & install; the device downloads and installs them. 3. If prompted, restart the device to finish applying the updates.
Troubleshooting on the page: if you get an error or can't install updates, see 'Troubleshoot problems updating Windows'. Low storage warning: see 'Free up space for Windows updates'.
Extra page used for the r example (same publisher), support.microsoft.com 'Troubleshoot problems updating Windows', Windows 11, general steps in order: Run the troubleshooter manually: Start > Settings > System > Troubleshoot > Other troubleshooters, select Run next to Windows Update. Check your connection: Start > Settings > Network & Internet > Wi-Fi and confirm you're connected, reconnect if needed. Check for updates again: Start > Settings > Windows Update, select Check for updates, install any new updates.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "I'm on my Windows 11 laptop and in the middle of a big project, so I don't want to install anything just yet. I only want to see whether any updates are waiting for me.",
                 """You can look without installing anything.

1. Click the **Start** button.
2. Click **Settings**.
3. Click **Windows Update**.
4. Click **Check for Windows updates**.

If updates are available, you don't have to do anything more right now. The **Download & install** button is the one that starts the installing, so you can leave it alone until you're ready.

When you do install them, Windows may ask you to restart to finish. Save your work first.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "sources": [{'title': 'Microsoft Support: Install Windows Updates', 'url': 'https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates', 'accessed': '2026-11-13'}, {'title': 'Microsoft Support: Troubleshoot problems updating Windows', 'url': 'https://support.microsoft.com/en-us/windows/troubleshoot-problems-updating-windows-188c2b0f-10a7-d72f-65b8-32d177eb136c', 'accessed': '2026-11-13'}],
             "messages": [
                 "Can you walk me through updating my Windows 11 PC? I've never done it before.",
                 """Sure, it only takes a few clicks.

1. Click **Start**, then **Settings**.
2. Click **Windows Update**.
3. Click **Check for Windows updates**.
4. If updates are available, click **Download & install**.
5. If Windows asks you to restart, restart to finish the update.

Save your work before restarting.""",
                 "I clicked Check for Windows updates but it just shows an error.",
                 """Let's try Windows' built-in fixer.

1. Click **Start**, then **Settings**, then **System**, then **Troubleshoot**, then **Other troubleshooters**.
2. Click **Run** next to **Windows Update**.
3. Make sure you're online: go to **Start**, **Settings**, **Network & Internet**, **Wi-Fi**, and reconnect if needed.
4. Go back to **Settings**, **Windows Update**, and click **Check for Windows updates** again.

If you still get an error, write down the error code and tell me what it says.""",
             ]},
        ],
    },
    {
        "task_id": "TR-035", "task_type": "backup_photos", "task": "Back up photos",
        "platform": "Android (Google Photos)", "category": "technical_support", "sensitive": False,
        "source": {"title": "Google Photos Help: Back up photos & videos (Android)", "url": "https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid"},
        "source_notes": """Turn on backup: open Google Photos app; tap Profile picture or Initial at top right; tap Photos settings, then Backup; turn on Backup. Account storage is shared with Drive and Gmail.
Mobile data: in Backup, tap Mobile data usage. Set a daily data limit for automatic backup. Turn off 'Back up videos over data' to keep videos off mobile data. Turn 'Back up while roaming' on or off.
Check status: tap Profile picture or Initial; shows 'Backup complete' or 'Backup is off'. Library status at top reads 'Preparing backup', 'Backing up photos', 'Backup complete', or 'Backup paused'; tap it for details.
Storage: out of space, tap 'buy more storage' or 'clean up your storage space'. Single photo with too little space shows 'Not enough storage to back up'. Backup works only with enough storage.
Troubleshooting: battery optimization can interfere. Open Settings and search for 'battery optimization'; tap Battery optimization, then All apps; tap Photos, choose Don't optimize, tap Done. On some other devices touch and hold the Photos app, tap Info, under Manage battery usage select Unrestricted.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android (Google Photos)",
             "messages": [
                 "I have a Samsung phone and a small data plan. I'd like my pictures kept safe in Google Photos, but I don't want the backup eating up my data. Can I set that up with a limit?",
                 """Yes. Turn backup on first, then set limits for mobile data.

1. Open the **Google Photos** app.
2. Tap your **profile picture or initial** at the top right.
3. Tap **Photos settings**, then **Backup**.
4. Turn **Backup** on.
5. Still in **Backup**, tap **Mobile data usage**.
6. Set a **daily data limit** for automatic backup.
7. Turn off **Back up videos over data** so your videos stay off mobile data.

You can also choose whether to turn **Back up while roaming** on or off in the same place.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android (Google Photos)",
             "messages": [
                 "My daughter says I should use Google Photos to keep my pictures safe. I have a Pixel phone. What do I do?",
                 """Google Photos can save copies of your pictures to your Google Account.

1. Open the **Google Photos** app.
2. Tap your **profile picture or initial** at the top right.
3. Tap **Photos settings**, then **Backup**.
4. Turn **Backup** on.

Your pictures start saving to your account. With many photos it can take a while.""",
                 "I did that yesterday, but now the top of the app says Backup paused and nothing seems to be uploading.",
                 """Let's check two common causes.

1. Tap the status at the top of the app to see details. Backup works only if your Google storage has room. If you're out of space, tap **buy more storage** or **clean up your storage space**.
2. Your phone's battery saver can interfere. Open **Settings** and search for **battery optimization**. Tap **Battery optimization**, then **All apps**. Tap **Photos**, choose **Don't optimize**, and tap **Done**.

After that, open Google Photos again and check the status at the top.""",
             ]},
        ],
    },
    {
        "task_id": "TR-036", "task_type": "add_printer", "task": "Add a printer",
        "platform": "Windows 11", "category": "technical_support", "sensitive": False,
        "source": {"title": "Microsoft Support: Add or install a printer in Windows", "url": "https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows"},
        "source_notes": """Wired or local printer (Windows 11): plug printer into PC (for example USB) and turn it on; Windows usually installs it automatically. Open Start, go to Settings > Bluetooth & devices > Printers & scanners. Check whether the printer already appears in the installed list. If not, select Add a printer & scanner, then Add device. Wait for the list to fill, which can take a few minutes; select Add Device next to your printer.
What you may see: the printer may install after you select Add device without step 5. A Find drivers button may appear; printer should work with reduced functionality until full drivers installed. After installing, check Windows Update for updated printer drivers.
If the printer isn't listed: select Add a new device manually next to 'The printer that I want isn't listed' and follow the Add Printer window instructions (options inside not detailed).
Network or wireless printers: make sure printer is on and on the same network as the PC; for wireless, same wireless network. Then follow the same steps (open Settings > Bluetooth & devices > Printers & scanners, Add a printer & scanner, Add device, wait, Add device next to printer).""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "I have a Windows 11 PC and a new wireless printer. I don't have a USB cable and I don't want to go buy one. Can I still get them working together?",
                 """Yes, a wireless printer doesn't need a cable. First, turn the printer on and make sure it's on the same wireless network as your computer.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**, then **Printers & scanners**.
3. Next to **Add a printer & scanner**, click **Add device**.
4. Wait a few minutes while the list fills up.
5. When your printer appears, click **Add device** next to it.

Some printers install by themselves after step 3.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "I plugged my printer into my Windows 11 computer with the USB cable and turned it on. Now what?",
                 """Windows usually installs the printer by itself. Let's check.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**, then **Printers & scanners**.
3. Look for your printer in the list. If it's there, you're done.
4. If it's not, next to **Add a printer & scanner**, click **Add device**.
5. Wait a few minutes while the list fills up, then click **Add device** next to your printer.""",
                 "I waited several minutes and my printer never showed up in the list.",
                 """Let's try adding it by hand.

1. Check that the printer is turned on and plugged in to the computer.
2. On the same screen, find **The printer that I want isn't listed** and click **Add a new device manually** next to it.
3. Follow the instructions in the **Add Printer** window that opens.""",
             ]},
        ],
    },
    {
        "task_id": "TR-037", "task_type": "email_attach", "task": "Attach a photo to an email",
        "platform": "Gmail app (phone)", "category": "communication", "sensitive": False,
        "source": {"title": "Gmail Help: Send attachments with your Gmail message (Android)", "url": "https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid"},
        "source_notes": """Steps: open Gmail app; at bottom right tap Compose; at top right tap Attach; in the menu choose Photos, Camera, Files, or Drive.
Limits: personal Gmail accounts 25 MB; work/school set by administrator. Multiple photos: you can select up to five at a time.
If total attachment size exceeds the limit, Gmail removes the attachment and adds it to the email as a Google Drive link. You can send while an attachment is still uploading; upload finishes in the background.
Remove an attachment: tap Close on the right side of the attachment name.
Troubleshooting: storage full: attachments count toward Google storage; if you reach the limit you can't send or receive attachments; delete large attachments and empty trash and spam. 'Couldn't send message' error: one or more files didn't upload to Drive, possibly due to low space or slow internet; remove or re-add the attachment, then send.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Gmail app (phone)",
             "messages": [
                 "I have three photos from the picnic on my Android phone and I'd like all of them in one email in the Gmail app, not three separate emails.",
                 """You can put them all in one email.

1. Open the **Gmail** app.
2. Tap **Compose** at the bottom right.
3. Tap **Attach** at the top right.
4. Choose **Photos**.
5. Tap each photo you want. You can select up to five at a time, so all three fit.

Then add the email address and your message, and send it.

If the photos are very large (over 25 MB together on a regular Gmail account), Gmail adds them as a Google Drive link instead.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Gmail app (phone)",
             "messages": [
                 "Please show me how to put a picture into an email with the Gmail app on my Android phone. It's for my nephew's birthday.",
                 """Here's how.

1. Open the **Gmail** app.
2. Tap **Compose** at the bottom right.
3. Tap **Attach** at the top right.
4. Choose **Photos**.
5. Tap the picture you want.

Then add your nephew's email address and your message, and send it.""",
                 "I tapped send and it says Couldn't send message.",
                 """That message can appear when a picture didn't finish uploading, often because of slow internet or low space. Try this:

1. Tap **Close** on the right side of the picture's name to remove it.
2. Tap **Attach**, choose **Photos**, and pick the picture again.
3. Send the email again.

If it keeps happening, your Google storage may be full. Attachments count toward it, so deleting large attachments and emptying your trash and spam can free space.""",
             ]},
        ],
    },
    {
        "task_id": "TR-038", "task_type": "account_password_reset", "task": "Reset forgotten Google Account password",
        "platform": "Google Account", "category": "online_services", "sensitive": True,
        "source": {"title": "Google Account Help: How to recover your Google Account or Gmail", "url": "https://support.google.com/accounts/answer/7682439?hl=en"},
        "source_notes": """Forgotten password: 1. Go to the recovery page https://accounts.google.com/signin/recovery?ec=ar_hc_7682439 . 'You'll be asked some questions to confirm it's your account.' Answer as accurately as you can. 2. If you have trouble, use the tips at https://support.google.com/accounts/answer/7299973 . 3. When prompted, reset your password; choose a strong one you haven't used with this account.
If you still can't sign in: wait before retrying; after changing recovery info 'it may take up to 7 days for those changes to take effect'; try again in a few days. If recovery still fails you can create a new account.
Tips: wrong guesses don't end the recovery process, no limit on attempts.
Security: you 'can't call Google for help to sign into your account.' Google doesn't work with account or password recovery services. Don't give out passwords or verification codes.
Not covered: familiar device/location, exact button labels.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Google Account",
             "messages": [
                 "I'm not good with websites. I'd rather just phone Google and have them reset my Gmail password for me. What's their number?",
                 """Google can't help you sign in over the phone, so there's no number to call for this. Please be careful with anyone who offers to recover your account for you, because Google doesn't work with account or password recovery services. Never give out your password or any verification codes.

The way back in is Google's recovery page, which asks you some questions:

1. Go to **https://accounts.google.com/signin/recovery?ec=ar_hc_7682439**.
2. Answer the questions as accurately as you can. They confirm it's your account.
3. When prompted, reset your password. Choose a strong one you haven't used with this account.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Google Account",
             "messages": [
                 "My grandson says I need to reset my Google password. I use it for email on my tablet. How do I do that?",
                 """You can do it on Google's recovery page.

1. Go to **https://accounts.google.com/signin/recovery?ec=ar_hc_7682439**.
2. Answer the questions as accurately as you can. They confirm it's your account.
3. When prompted, reset your password. Choose a strong one you haven't used with this account.

Never share your password or any verification code with anyone, and remember that Google can't help you sign in over the phone.""",
                 "I answered the questions but it says it can't tell it's my account.",
                 """Don't worry, you can try again.

1. Go through the questions again and answer as accurately as you can. Wrong guesses don't end the process, and there's no limit on tries.
2. Read Google's tips for trouble at **https://support.google.com/accounts/answer/7299973**.
3. If you changed your recovery information recently, the change can take up to 7 days to take effect. Try again in a few days.""",
             ]},
        ],
    },
    {
        "task_id": "TR-039", "task_type": "family_emergency_scam", "task": "Call that sounds like a family member's voice asking for money",
        "platform": "any", "category": "online_services", "sensitive": True,
        "source": {"title": "FTC Consumer Alert: Scammers use AI to enhance their family emergency schemes", "url": "https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes"},
        "source_notes": """Scammer can use a voice-cloning program to imitate a loved one, may need only a short recording (can come from online posts), then calls pretending to be that person in trouble and asking for money.
Advice: 'Don't trust the voice.' Hang up and check the story yourself: call the person who supposedly contacted you and verify. Use a phone number you know is theirs. If you can't reach them, contact them through another family member or their friends.
Red flags: scammers ask you to pay in ways that make it hard to get your money back. If the caller asks you to wire money, send cryptocurrency, or buy gift cards and give the card numbers and PINs, those could be signs of a scam.
Report to the FTC at ReportFraud.ftc.gov.
The page does not cover what to do after paying. For the r example I used the FTC page https://consumer.ftc.gov/articles/what-do-if-you-were-scammed : wire transfer: 'Report it to the wire transfer company immediately'; tell them a scammer tricked you and ask for a refund. Report the scam to the FTC at reportfraud.ftc.gov.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "any",
             "messages": [
                 "My grandson called from a number I don't know, sounding scared, and said he'd been in a car accident and needs $2,000 sent through Western Union. He begged me not to tell his parents. I've tried his own phone but it goes straight to voicemail.",
                 """Please **don't send any money**. Scammers can copy a person's voice, sometimes from a short recording posted online, so a call can sound just like your grandson. Don't trust the voice.

1. **Hang up** if you haven't already.
2. **Call him again** at the number you already know is his, not the number that called you.
3. Since you can't reach him, **contact him through another family member or his friends**. That includes his parents, even though the caller asked you not to tell them.

Asking you to wire money, send cryptocurrency, or buy gift cards are warning signs, because those payments are hard to get back.

You can report the call at **ReportFraud.ftc.gov**.""",
             ]},
            {"suffix": "r", "scenario": "already_acted", "style": "failure_recovery", "specification": "fully_specified", "platform": "any",
             "sources": [{'title': 'FTC Consumer Alert: Scammers use AI to enhance their family emergency schemes', 'url': 'https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes', 'accessed': '2026-11-13'}, {'title': 'FTC Consumer Advice: What To Do if You Were Scammed', 'url': 'https://consumer.ftc.gov/articles/what-do-if-you-were-scammed', 'accessed': '2026-11-13'}],
             "messages": [
                 "A call came in that sounded just like my granddaughter saying she was in trouble. I wired $2,500 through Western Union an hour ago, and now I can't reach her and I'm afraid it was a scam.",
                 """I'm sorry, this happens to careful people. Please don't send any more money, and contact the wire transfer company right away.

1. **Report it to the wire transfer company immediately.** Tell them a scammer tricked you, and ask for a refund.
2. **Check on your granddaughter.** Call her at a number you know is hers. If you can't reach her, contact her through another family member or her friends.
3. **Report the scam to the FTC** at **ReportFraud.ftc.gov**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-040", "task_type": "package_text_scam", "task": "Text says package could not be delivered",
        "platform": "any", "category": "online_services", "sensitive": True,
        "source": {"title": "FTC Consumer Alert: Think that text message is from USPS? It could be a scam", "url": "https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam"},
        "source_notes": """Scammers want you to click the link in their message. The link leads to a look-alike of a real website where you're asked for personal or financial information; anything you pay or enter goes to the scammer.
Texts may confirm an order, say a package is out for delivery, or report a problem such as unpaid postage, a missed delivery, or a need to update shipping preferences. Each asks you to click a link.
What to do: If you think a text is about a real delivery, don't give information or click on any links. Check your phone's options to filter and block texts from unknown senders. Report on your messaging app: look for a junk or spam option; if not, forward the message to 7726.
Check a real package: go to the online retailer or account where you ordered the item and look up the shipping and tracking information. Don't use the link in the text.
Report to the FTC at ReportFraud.ftc.gov.
The page does not cover what to do after clicking or paying. For the r example I used https://consumer.ftc.gov/articles/what-do-if-you-were-scammed : credit card: 'Report it to the credit card issuer immediately'; use the number on the back of your card or log in to your account online or in the app, then ask for a refund.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "any",
             "messages": [
                 "I'm expecting about four packages this week from different places, so a text from USPS about a package problem could be real. It wants me to tap a link to confirm my delivery preferences. I don't remember which store each package came from.",
                 """Please **don't tap the link** or give any information, even with several packages on the way. The link usually goes to a look-alike of a real website that asks for personal or payment details, and anything you enter goes to the scammer.

1. **Don't click** the link or reply.
2. **Check each order where you bought it.** Open the website or account of each store you ordered from, and look up the shipping and tracking information there, not through the text.
3. **Report the text.** Use your messaging app's junk or spam option, or forward it to **7726**.
4. You can also report it at **ReportFraud.ftc.gov**.""",
             ]},
            {"suffix": "r", "scenario": "already_acted", "style": "failure_recovery", "specification": "fully_specified", "platform": "any",
             "sources": [{'title': 'FTC Consumer Alert: Think that text message is from USPS? It could be a scam', 'url': 'https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam', 'accessed': '2026-11-13'}, {'title': 'FTC Consumer Advice: What To Do if You Were Scammed', 'url': 'https://consumer.ftc.gov/articles/what-do-if-you-were-scammed', 'accessed': '2026-11-13'}],
             "messages": [
                 "I got a text from USPS about a missed delivery. I clicked the link and typed in my credit card number to pay a $1.99 fee, then got suspicious. What do I do?",
                 """I'm sorry, these texts look very real and fool many people. Contact your credit card company right away.

1. **Report it to the credit card issuer immediately.** Call the number on the back of your card, or log in to your account online or in the app.
2. Tell them what happened and **ask for a refund**.
3. **Report the text.** Use your messaging app's junk or spam option, or forward it to **7726**.
4. **Report it to the FTC** at **ReportFraud.ftc.gov**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-041", "task_type": "gift_card_scam", "task": "Someone asks to be paid with gift cards",
        "platform": "any", "category": "online_services", "sensitive": True,
        "source": {"title": "FTC Consumer Advice: Avoiding and Reporting Gift Card Scams", "url": "https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams"},
        "source_notes": """Signs: scammers say it's urgent; slow down and don't pay. May name a card brand or store, or stay on the phone while you load money; if so, hang up. Asking for the card number and PIN, or a photo of the card, is a scam sign. Common stories include a family emergency, government, tech support, prize fee, utility shutoff.
'No real business or government agency will ever tell you to buy a gift card to pay them.' Gift cards are for gifts only, never for paying bills, fees, or prizes.
If you paid or shared numbers: report to the gift card company right away, ask for money back, ask whether funds remain (Apple and Google can freeze a card that still has money); keep card and receipt or photo; report to the FTC at ReportFraud.ftc.gov.
Family or friends: scammers may use voice cloning. Contact the relative directly to check they're safe. If someone claims a relative is in trouble, reach that relative through a number you already know. If a caller pressures you to stay on the line, hang up.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "any",
             "messages": [
                 "My nephew texted me from a new number saying he's stuck at the airport and needs me to buy Google Play gift cards to pay for a rebooked flight, then text him the codes. His regular phone seems to be off, so I can't reach him to check. He says it's really urgent.",
                 """Please **don't buy the gift cards**. Scammers say it's urgent so you'll rush, so slow down and don't pay. No real business or government agency will ever tell you to buy a gift card to pay them, and gift cards are for gifts only.

1. **Don't reply** and don't send any codes or photos of cards.
2. **Reach your nephew through a number you already know is his**, not the new number that texted you. Scammers may also use voice cloning, so check with him directly. If his phone stays off, ask another family member or his friends to check on him.
3. **Report the text** at **ReportFraud.ftc.gov**.

If you've already bought cards or shared the numbers, report it to the gift card company right away and ask for your money back. Keep a copy of the gift card and your store receipt by taking a picture of each with your phone.""",
             ],
             "sources": [{'title': 'FTC Consumer Advice: Avoiding and Reporting Gift Card Scams', 'url': 'https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams', 'accessed': '2026-11-13'}, {'title': 'FTC Consumer Alert: Scammers use AI to enhance their family emergency schemes', 'url': 'https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes', 'accessed': '2026-11-13'}]},
        ],
    },
    {
        "task_id": "TR-042", "task_type": "family_sharing", "task": "Set up Family Sharing",
        "platform": "iPhone", "category": "technical_support", "sensitive": False,
        "source": {"title": "Apple Support: How to set up Family Sharing on your iPhone, iPad, or Mac", "url": "https://support.apple.com/en-us/108380"},
        "source_notes": """Set up group (organizer): open Settings, tap your name; tap Family, then tap Continue; follow onscreen instructions to set up the group and invite members. Organizer must be an adult.
Invite people: open Settings, tap Family; tap the Add Member button; tap Invite Others to add an adult or a child who already has a Child Account; if the child doesn't have one, tap Create Child Account and follow onscreen instructions; finish remaining prompts for parental controls, location sharing and similar settings. Invitations are sent by Messages or email.
Invitee accepts: respond from the email or text invitation, or open Settings, tap your name, tap Invitations, complete onscreen instructions. May need to confirm Apple Account info and opt in to features.
If invitation isn't received: open Settings, tap Family, tap the person's name to check status; tap Resend Invitation if needed.
Shared features: Apple services such as iCloud+, Apple Music, Apple TV without sharing an Apple Account; locating devices and sharing location; Screen Time and parental controls.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I have an iPhone and my 12 year old grandson doesn't have his own Apple Account yet. I'd like him in my Family Sharing, but I don't want to give him my login.",
                 """Family Sharing is made for that. You can share things like iCloud+, Apple Music, and Apple TV without sharing an Apple Account. For a child without an account, you create a Child Account.

**Set up the group (if you haven't yet):**
1. Open **Settings** and tap **your name**.
2. Tap **Family**, then tap **Continue**.
3. Follow the instructions on the screen.

**Add your grandson:**
4. Go to **Settings**, then **Family**.
5. Tap the **Add Member** button.
6. Tap **Create Child Account** and follow the instructions on the screen.
7. Finish the prompts for parental controls, location sharing, and similar settings.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I'm on an iPhone and I want to invite my wife to my Family Sharing group. I already made the group.",
                 """Here's how to invite her.

1. Open **Settings**, then tap **Family**.
2. Tap the **Add Member** button.
3. Tap **Invite Others**.
4. Finish the prompts that follow.

The invitation is sent to her by Messages or email.""",
                 "She says the invitation never came.",
                 """Let's check on it and send it again.

1. Open **Settings**, then tap **Family**.
2. Tap her name to see the invitation status.
3. Tap **Resend Invitation**.

She can accept from the email or text invitation. Or on her iPhone she can open **Settings**, tap her name, tap **Invitations**, and follow the instructions on the screen.""",
             ]},
        ],
    },
    {
        "task_id": "TR-043", "task_type": "add_contact", "task": "Add a contact",
        "platform": "Android", "category": "communication", "sensitive": False,
        "source": {"title": "Contacts Help: Add or move contacts (Android)", "url": "https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid"},
        "source_notes": """Add a contact: open Contacts app; at bottom right tap Add; enter the contact's name and an email address or phone number (more name details: Add fields; photo: Add picture, then Choose; street address, notes: tap field or Add fields); when finished tap Save.
Move a contact to a Google Account: open Contacts and tap the contact; at top right tap Contact settings, then Move to another account; choose the Google Account. Moving a contact deletes it from its original account.
Google Account contacts sync to Google Contacts and your Android devices.
Not covered: adding from a call or message, choosing account when creating, troubleshooting.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My son's teacher gave me only her email address, no phone number. I have an Android phone. Can I still make a contact for her?",
                 """Yes. A contact needs a name and either an email address or a phone number.

1. Open the **Contacts** app.
2. Tap **Add** at the bottom right.
3. Type her name.
4. Type her email address.
5. Tap **Save**.

If you want to add more details, such as a street address or notes, tap **Add fields** before you tap **Save**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I'm using an Android phone. How do I put my friend Linda's number into my Contacts?",
                 """Here's how.

1. Open the **Contacts** app.
2. Tap **Add** at the bottom right.
3. Type Linda's name.
4. Type her phone number.
5. Tap **Save**.""",
                 "I saved her, but when I signed in on my new Android phone, Linda isn't there.",
                 """Contacts saved to a Google Account sync to your Android devices, so Linda may be saved somewhere else. You can move her to your Google Account:

1. Open the **Contacts** app and tap **Linda**.
2. At the top right, tap **Contact settings**.
3. Tap **Move to another account**.
4. Choose your Google Account.

Moving a contact deletes it from its original account.""",
             ]},
        ],
    },
    {
        "task_id": "TR-045", "task_type": "block_number", "task": "Block a phone number",
        "platform": "iPhone", "category": "communication", "sensitive": False,
        "source": {"title": "Apple Support: Block phone numbers, contacts, and emails on your iPhone or iPad", "url": "https://support.apple.com/en-us/111104"},
        "source_notes": """Phone app: tap Recents; tap the phone number or contact, or tap the Info button in Classic view; scroll down and tap Block Caller.
Messages: open the conversation; tap the contact at the top; scroll down and tap Block Caller.
What happens: blocked callers can still leave a voicemail but you won't get a notification. Messages they send or receive won't be delivered. The contact isn't notified that their call or message was blocked.
View and unblock (Settings, iOS 26): open Settings and tap Privacy & Security; tap Blocked Contacts; tap Edit (or tap Unknown contacts and then Edit); tap the delete button next to the contact; tap Unblock.
Not covered: confirmation dialog wording.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "A man keeps texting me from a number I don't know on my iPhone, mostly rude stuff. He never calls, so there's nothing in my recent calls. I don't want him to know I blocked him.",
                 """You can block him right from the text conversation, and he won't be told.

1. Open the **Messages** app and open the conversation with him.
2. Tap his number or name at the top.
3. Scroll down and tap **Block Caller**.

After that, messages he sends won't be delivered to you, and he isn't notified that he was blocked.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "A telemarketer calls my iPhone every afternoon. Please show me how to block the number.",
                 """You can block it from your recent calls.

1. Open the **Phone** app.
2. Tap **Recents**.
3. Tap the phone number. If you see the **Info** button, tap that instead.
4. Scroll down and tap **Block Caller**.

After that, the caller isn't told they were blocked.""",
                 "Oh no, I think I blocked my daughter's number by mistake. How do I undo it?",
                 """No problem, you can unblock her. These steps are for the newest iPhone software, iOS 26.

1. Open **Settings** and tap **Privacy & Security**.
2. Tap **Blocked Contacts**.
3. Tap **Edit**.
4. Tap the delete button next to her number.
5. Tap **Unblock**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-046", "task_type": "block_number", "task": "Block a phone number",
        "platform": "Android", "category": "communication", "sensitive": False,
        "source": {"title": "Phone app Help: Block or unblock a phone number", "url": "https://support.google.com/phoneapp/answer/6325463?hl=en"},
        "source_notes": """Block from Call history: open your Phone app; tap More, then Call history; tap a call from the number you want to block; tap 'Block / report spam'.
Block unknown (private or unidentified) numbers: open Phone app; tap More; tap Settings, then Blocked numbers; turn on Unknown.
Unblock: open Phone app; tap More; tap Settings, then Blocked numbers; next to the number tap Clear, then Unblock.
Effects: your phone declines the blocked number's calls automatically; if visual voicemail is on, blocked callers can't leave voicemails; calls received from a number while blocked don't appear in call history.
Some steps only work on Android 6.0 and up. Not covered: blocking from Contacts, Samsung or other phone differences.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "Calls keep coming in on my Android phone that show up as Unknown with no number at all, so I can't pick one from my call history to block. Is there another way?",
                 """Yes. You can block all unknown (private or unidentified) numbers.

1. Open the **Phone** app.
2. Tap **More**.
3. Tap **Settings**, then **Blocked numbers**.
4. Turn on **Unknown**.

Your phone will then decline calls from those numbers automatically. That covers every unknown caller, not only the one bothering you.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "A telemarketer keeps ringing my Pixel phone. Show me how to block that number from my call history.",
                 """You can block it from your call history.

1. Open the **Phone** app.
2. Tap **More**, then **Call history**.
3. Tap a call from the number you want to block.
4. Tap **Block / report spam**.

After that, your phone declines that number's calls automatically.""",
                 "I think I blocked the wrong number. How do I undo it?",
                 """You can unblock it.

1. Open the **Phone** app and tap **More**.
2. Tap **Settings**, then **Blocked numbers**.
3. Next to the number, tap **Clear**.
4. Tap **Unblock**.""",
             ]},
        ],
    },
]
