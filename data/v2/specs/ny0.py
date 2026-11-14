TASKS = [
    {
        "task_id": "TR-117",
        "task_type": "screenshot",
        "task": "Take a screenshot",
        "platform": "Mac",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: How to take a screenshot on your Mac", "url": "https://support.apple.com/en-us/102646"},
        "source_notes": """Whole screen: press and release Shift-Command-3. If a thumbnail appears in the corner, click it to edit the screenshot. Otherwise the screenshot saves to the desktop.
Portion: press and release Shift-Command-4, pointer becomes a crosshair. Click and hold the mouse or trackpad button, drag to select the area, release the button to capture. Esc cancels. Hold Space bar while dragging to move the selection without resizing. Then handle thumbnail or saved file as above.
Window or menu: open the window or menu, press Shift-Command-4, then press and release Space bar; pointer becomes a camera icon. Esc cancels. Click the window or menu to capture. Hold Option while clicking to exclude the window shadow.
Screenshot app (macOS Mojave 10.14 or later): press Shift-Command-5 or open Applications > Utilities > Screenshot. Options menu: set a timer, choose a save location, show or hide the floating thumbnail, show or hide mouse pointer.
Where it goes: default saved to desktop named "Screen Shot [date] at [time]". Drag the corner thumbnail to a folder or app before it saves. To copy to the Clipboard instead of saving a file, Control-click the thumbnail and choose Save to Clipboard, or add Control to the combo, e.g. Control-Shift-Command-3.
Thumbnail stays on screen if you hover over it. Some apps (e.g. Apple TV app) may block screenshots of their windows.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "How do I take a picture of my whole screen on my Mac?",
                 """You can do this with three keys on the keyboard.

1. Press and release **Shift-Command-3** all together.
2. If a small picture appears in the corner of the screen, click it if you want to edit the screenshot.

If no small picture appears, the screenshot was saved on your desktop.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "My daughter set up this MacBook for me and my doctor's office sent me a long message in my email. I only want to save the small part with my appointment time, not the whole screen, because the rest has other stuff on it. How would I take a screenshot of just that part on my Mac?",
                 """You can pick just the part you want.

1. Press and release **Shift-Command-4**. The pointer turns into a crosshair.
2. Click and hold the mouse or trackpad button.
3. Drag to cover the part with your appointment time.
4. Let go of the button to take the screenshot.

The picture is saved on your desktop unless a small picture appears in the corner, which you can click to edit it.

If you change your mind, press **Esc** before you let go and nothing is saved.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "how do i take a picture of what is on my screen",
                 "I can help with that. Is your computer a **Mac** or a **Windows** PC?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "how do i take a picture of what is on my screen",
                 "I can help with that. Is your computer a **Mac** or a **Windows** PC?",
                 "its a mac",
                 """Thanks. On a Mac, three keys take a picture of the whole screen.

1. Press and release **Shift-Command-3** all together.
2. If a small picture appears in the corner of the screen, you can click it to edit the screenshot.

If no small picture appears, the screenshot was saved on your desktop.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "I'm on a Mac and I want to screenshot my whole screen and paste it into an email to my son. I don't want a file left sitting on my desktop, I have too many already. Is there a way to skip that?",
                 """Yes, you can copy the screenshot instead of saving it as a file.

1. Press and release **Control-Shift-Command-3** all together.

Adding the **Control** key sends the screenshot to the Clipboard instead of saving a file on your desktop.

If a small picture appears in the corner, you can also Control-click it and choose **Save to Clipboard**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "How do I screenshot my entire screen on my Mac?",
                 """Here is how.

1. Press and release **Shift-Command-3** all together.
2. If a small picture appears in the corner, click it to edit the screenshot.

If it does not appear, the screenshot was saved on your desktop.""",
                 "I pressed those keys but no little picture showed up. Where did it go?",
                 """That is fine. Your screenshot was saved on your desktop.

1. Look on your desktop for a file named **Screen Shot**, followed by the date and time.
2. If you want to see the small picture next time, press **Shift-Command-5**, open the **Options** menu, and choose to show the floating thumbnail.""",
             ]},
        ],
    },
    {
        "task_id": "TR-118",
        "task_type": "backup_phone",
        "task": "Back up the phone",
        "platform": "Android",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Android Help: Back up or restore data on your Android device", "url": "https://support.google.com/android/answer/2819582?hl=en"},
        "source_notes": """Automatically back up: 1 Open device Settings app. 2 Go to Google services, then All services. Choose data to back up: Photos & videos, Device data, or both. 3 Turn Backup on (switch is called Backup; Backup by Google One appears only in the turn-off section). "On" appears below the selected data types once the data is saved; allow up to 24 hours for a Google One backup.
Manually back up: 1 Open Settings. 2 Tap Google, then All services. 3 Under "Backup and restore" tap Backup, then Back up now.
Switch account: Google > All services > Backup > Account storage, tap the account you want (PIN, pattern, or password if asked).
Conditions: not usable on a work-profile device, work-only device, or company-owned device. Some steps Android 9 and up. Restoring a backup from a higher Android version onto a lower one is not possible. Use a PIN, pattern, or password lock, not swipe or Smart Lock. Free storage up to 15 GB, more with Google One.
Included always: apps and app data, call history, contacts, device settings, SMS and MMS. Through specific apps: RCS (Google Messages), phone call settings and blocked numbers (Phone by Google), photos and videos (Google Photos).
Troubleshooting: "On" doesn't appear: allow up to 24 hours. Turn off: Settings > Google > All services > Backup, turn off Backup by Google One. No Wi-Fi or charging requirement mentioned. Samsung or Pixel differences not covered.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "How can I make my Android phone save a copy of everything automatically?",
                 """You can turn on automatic backup in Settings.

1. Open the **Settings** app on your phone.
2. Tap **Google services**, then tap **All services**.
3. Choose what to save: **Photos & videos**, **Device data**, or both.
4. Turn **Backup** on.

When your data is saved, the word **On** shows under what you chose.

If **On** does not show up, wait. A backup can take up to 24 hours.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My son told me I should save everything on my phone before I go to the store to get a new one next week. I have a Samsung Android phone and I never changed anything in the settings. I want to do a backup right now, today, so I know it is done. What do I press?",
                 """You can start a backup yourself right now.

1. Open the **Settings** app.
2. Tap **Google**, then tap **All services**.
3. Under **Backup and restore**, tap **Backup**.
4. Tap **Back up now**.

This saves your apps, contacts, call history, settings, and text messages. Photos and videos are saved through Google Photos.

If you cannot find **Backup**, your phone may be a work phone, and backup does not work on those.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I want to back up my phone so I don't lose my stuff",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I want to back up my phone so I don't lose my stuff",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "android",
                 """You can back it up right now.

1. Open the **Settings** app.
2. Tap **Google**, then tap **All services**.
3. Under **Backup and restore**, tap **Backup**.
4. Tap **Back up now**.

If you do not see **Backup**, your phone may be a work phone, and backup does not work on those.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I have an Android phone and I only care about my photos and videos of the grandkids. I don't need apps or contacts backed up, I just don't want to lose the pictures. Can I back up only those?",
                 """Yes, you can choose only photos and videos.

1. Open the **Settings** app.
2. Tap **Google services**, then tap **All services**.
3. Choose **Photos & videos** only. Leave **Device data** unselected.
4. Turn **Backup** on.

When your photos and videos are saved, the word **On** shows below **Photos & videos**.

If **On** does not show, wait. It can take up to 24 hours.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "Please help me turn on backup on my Android phone so it saves my contacts and settings.",
                 """Here is how to turn it on.

1. Open the **Settings** app.
2. Tap **Google services**, then tap **All services**.
3. Choose **Device data**.
4. Turn **Backup** on.

When your data is saved, the word **On** shows below it.""",
                 "I did all that this morning but I don't see the word On under it. Did it work?",
                 """It may just need more time. A backup can take up to 24 hours.

1. Wait and look again later today or tomorrow.
2. Check that you turned **Backup** on and that **Device data** is chosen.

The word **On** will appear below it once your data is saved.""",
             ]},
        ],
    },
    {
        "task_id": "TR-119",
        "task_type": "install_app",
        "task": "Install an app from the Microsoft Store",
        "platform": "Windows 11",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Get apps from Microsoft Store on your Windows PC", "url": "https://support.microsoft.com/en-us/help/4479732/get-apps-from-microsoft-store-on-windows-10-pc"},
        "source_notes": """Also read: support.microsoft.com/en-us/help/4027119 (same steps), /help/4000641 (Find and install your Microsoft downloads), and "I can't find or install an app from Microsoft Store" (support.microsoft.com/en-us/accounts-billing/i-can-t-find-or-install-an-app-from-microsoft-store). Page 4479732 says it applies to Windows 11.
Steps: 1 Select Start, then Microsoft Store (or select the Microsoft Store icon on the taskbar). 2 In Microsoft Store choose Apps or Gaming. 3 To see more in a category select Show all. To install something already acquired: open Microsoft Store from taskbar icon, select More info by your account picture, then select My Library. An app or game with a Download icon next to it hasn't been downloaded yet. Select the Download icon to download and install it. Many apps and games are free. Installed apps follow you to any device and update automatically. Past purchases: Order history shows apps not yet installed.
GAP: these pages do NOT describe a search step or a Get/Install button on an app page for new apps (the reset article only says to open the Store and search for your app). Examples therefore stick to browsing Apps/Gaming/Show all and the My Library Download icon.
Troubleshooting (can't find or install): app may be unavailable in your region, hidden by Microsoft Family settings, removed, or incompatible with the device. If Windows updates were recently installed, restart the PC before installing Store apps. Sign in to the app with your Microsoft account. Reset the Store: press Windows logo key + R, enter wsreset.exe, select OK. A blank command prompt window opens, closes after about ten seconds, and the Store opens automatically. Run the troubleshooter for Windows apps for problems with a free game.""",
        "examples": [
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "My nephew put a new Windows 11 laptop on my desk and said I could pick up a few games from the Microsoft Store. I have the Store icon down on the bottom bar of the screen, I think. How would I look at the games the store has?",
                 """You can start from that icon.

1. Select the **Microsoft Store** icon on the taskbar, the bar at the bottom of the screen.
2. In the Store, choose **Gaming**.
3. To see more games, select **Show all**.

Many games are free to download and play. Games you install update automatically.

If you do not see the icon, select **Start**, then select **Microsoft Store**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my grandson said i can get a weather app for my computer from the store. how",
                 "I can help with that. Is your computer a **Windows** PC or a **Mac**?",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "I got an app from the Microsoft Store last year on my old computer and now I have a new Windows 11 PC. I don't want to buy it again. How do I put it on this one?",
                 """You can install it again from your Library, with no new purchase.

1. Select the **Microsoft Store** icon on the taskbar.
2. Select **More info** next to your account picture.
3. Select **My Library**.
4. Find your app. If it has a **Download** icon next to it, it has not been downloaded on this PC yet.
5. Select the **Download** icon.

Make sure you are signed in with the same Microsoft account you used before.

If you do not see the app, look in **Order history** for apps you have not installed.""",
             ]},
        ],
    },
    {
        "task_id": "TR-120",
        "task_type": "crypto_investment_scam",
        "task": "Someone urges the user to invest or pay with cryptocurrency",
        "platform": "any",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "FTC Consumer Advice: What To Know About Cryptocurrency and Scams", "url": "https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams"},
        "source_notes": """How scammers use crypto: Investment scams (often met on social media or dating apps; promise easy profits, steer you to buy crypto and send it to their "investment account"; site looks real but is fake; you may be unable to withdraw). Impersonation scams (pose as well-known companies, government agencies, utilities, law enforcement; claim fraud or legal problem; tell you to buy crypto). Fake job scams (crypto fee, or move money from a fake check; you owe the bank). Fake coins or tokens. Blackmail (threaten to release material unless you pay in crypto).
Warning signs: anyone demanding payment in cryptocurrency ("Only scammers demand payment in cryptocurrency"); guaranteed profits or big quick returns ("Nobody can make those guarantees"); unexpected contact from a business, agency or "investment manager"; a love interest who offers investment advice or asks for money; pressure to click links from unexpected messages or to pay someone who contacted you first; vague explanations of how an investment works.
Avoid: don't click links in unexpected texts, emails or social media messages, even if they look like from a known company. Don't pay anyone who contacts you unexpectedly and demands crypto. Before investing search the company or person's name plus the crypto name with words like review, scam, complaint.
If already paid: crypto payments are typically not reversible; you can usually only get money back if the recipient sends it back. Crypto isn't protected like credit card payments. Report to the agencies below and contact the exchange you used to send the money. Blackmail: report to the FBI immediately. No step-by-step recovery given.
Where to report: FTC ReportFraud.ftc.gov; CFTC CFTC.gov/complaint; SEC sec.gov/tcr; Internet Crime Complaint Center ic3.gov/Home/FileComplaint; the crypto exchange company you used; FBI fbi.gov/contact-us (blackmail or extortion).""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "any",
             "messages": [
                 "A man I met online says he is an investment manager and wants me to buy cryptocurrency and send it to his site. He says I will make a lot of money. Is this real?",
                 """Please do not buy or send any cryptocurrency. This is very likely a scam.

Scammers promise easy profits and steer people to send crypto to a fake investment account. The site can look real, but you may never be able to take your money out.

1. Do not click any more links from him or pay him.
2. Search his name and the crypto name with words like **review**, **scam**, or **complaint**.
3. Report him at **ReportFraud.ftc.gov**.

Nobody can truly guarantee profits.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "any",
             "messages": [
                 "I got a text yesterday saying it was from the power company. It said my account has a legal problem and I have to buy cryptocurrency and send it today or they will shut off my power. I am a widow and I live alone and I am scared. I have not done anything yet. What should I do?",
                 """Do not pay, and do not click the link in that text. Only scammers demand payment in cryptocurrency.

Scammers pretend to be utilities or government offices, claim there is a problem, and tell you to buy crypto to fix it. You have done nothing wrong.

1. Do not click any links in the text, even if it looks like it is from a company you know.
2. Do not send any money to the person who contacted you.
3. Report the text at **ReportFraud.ftc.gov**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "any",
             "messages": [
                 "A woman on a dating app has been teaching me to invest in crypto. Her website shows my money has doubled. She says I must add more by tonight or I lose my profits, but when I tried to take some out it would not let me. What do I do?",
                 """Do not add any more money. This looks like an investment scam.

The site can look real but be fake, and scammers often make it hard to withdraw. A love interest who gives investment advice is a warning sign, and so is pressure to pay someone who contacted you first.

1. Stop sending money and stop clicking her links.
2. Report it at **ReportFraud.ftc.gov**.
3. You can also report it at **sec.gov/tcr** and **CFTC.gov/complaint**.
4. If you sent crypto already, contact the exchange you used.""",
             ]},
            {"suffix": "r", "scenario": "already_acted", "style": "failure_recovery", "specification": "fully_specified", "platform": "any",
             "messages": [
                 "I already sent a lot of cryptocurrency to a person I met on social media for an investment. Now they want more money to let me withdraw. Can I get my money back?",
                 """Do not send anything more. I am sorry this happened. It is not your fault.

Crypto payments are usually not reversible. You can generally only get the money back if the person who received it sends it back, so please act quickly on these steps.

1. Contact the crypto exchange you used to send the money.
2. Report it at **ReportFraud.ftc.gov**.
3. Also report it at **CFTC.gov/complaint**, **sec.gov/tcr**, and **ic3.gov/Home/FileComplaint**.""",
             ]},
            {"suffix": "f", "scenario": "helper", "style": "plain", "specification": "fully_specified", "platform": "any",
             "messages": [
                 "My mother says someone who emailed her out of the blue is going to help her invest in a new coin. She wants to buy cryptocurrency and send it to him. How can I help her?",
                 """Ask her not to send anything to him. This has the signs of a scam.

Unexpected contact from an "investment manager" is a warning sign. So is pressure to pay someone who contacted her first.

1. Ask her not to click links in that email or pay him.
2. Together, search his name and the coin name with words like **review**, **scam**, or **complaint**.
3. Report the email at **ReportFraud.ftc.gov**.
4. If she already sent crypto, contact the exchange she used.""",
             ]},
            {"suffix": "g", "scenario": "prevention", "style": "plain", "specification": "fully_specified", "platform": "any",
             "messages": [
                 "How can I tell if a crypto investment offer is a scam, and where do I report one?",
                 """Never pay anyone who contacts you out of the blue and asks for crypto. Only scammers demand payment in cryptocurrency.

Warning signs:
1. Guaranteed profits or big, quick returns.
2. Unexpected contact from a company, agency, or "investment manager".
3. A love interest who gives investment advice or asks for money.
4. Vague explanations of how the investment works.

Do not click links in unexpected texts, emails, or social media messages. Before investing, search the name and the crypto name with words like **review**, **scam**, or **complaint**.

To report, go to **ReportFraud.ftc.gov**.""",
             ]},
        ],
    },
]
