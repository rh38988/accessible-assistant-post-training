TASKS = [
    {
        "task_id": "TR-007",
        "task_type": "wifi_connect",
        "task": "Connect to a Wi-Fi network",
        "platform": "iPhone",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: Connect to Wi-Fi on your iPhone or iPad", "url": "https://support.apple.com/en-au/111107"},
        "source_notes": """Steps: 1. In Settings, tap Wi-Fi, then turn on Wi-Fi. The device searches for networks automatically. 2. Tap the name of the network you want. You might first be asked for the network's password or to agree to terms and conditions. If you don't know the password, contact your network administrator. 3. Look for a blue tick (checkmark) next to the network name and the Wi-Fi icon in the top corner of the screen: this means you connected successfully. 4. Optional: for a more reliable connection, scroll down and turn on Connectivity Assist to use cellular data alongside Wi-Fi.
Not covered: hidden networks, login pages, Control Center, a Join button, the color of the switch, what the icon looks like, how to find the gear icon. The page links to a separate troubleshooting article without giving steps.
NOTE: pilot-007 mentions a Join button, a green switch and a fan-shaped icon, which this page does not state.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "How do I connect my iPhone to the wifi at my house? I know the password.",
                 """Here is how to connect your iPhone to your home Wi-Fi.

1. Open **Settings**.
2. Tap **Wi-Fi**.
3. Turn on **Wi-Fi** if it is off. Your iPhone will look for networks by itself.
4. Tap the name of your home network.
5. Type the password if it asks for it.

When it worked, you will see a blue checkmark next to the network name and the Wi-Fi symbol at the top corner of the screen.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my son said to get on the wifi at his place. how do i do that on my phone",
                 """I can help with that. Is your phone an **iPhone** or an **Android** phone?""",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "my son said to get on the wifi at his place. how do i do that on my phone",
                 """I can help with that. Is your phone an **iPhone** or an **Android** phone?""",
                 "iPhone",
                 """Thank you. Here is how to join your son's Wi-Fi on your iPhone. Have the password handy.

1. Open **Settings**.
2. Tap **Wi-Fi**.
3. Turn on **Wi-Fi** if it is off.
4. Tap the name of your son's network in the list.
5. Type the password if it asks for it. It may also ask you to agree to terms and conditions.

When you are connected, you will see a blue checkmark next to the network name and the Wi-Fi symbol at the top corner of the screen.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I'm at the community center with my iPhone and they have free wifi, but nobody gave me a password and I don't want to go bother the front desk if there's another way around it. Can you just connect me?",
                 """I can show you the steps, but the network may ask for a password or for you to agree to terms and conditions.

1. Open **Settings**.
2. Tap **Wi-Fi**.
3. Turn on **Wi-Fi** if it is off.
4. Tap the name of the community center network.
5. If it asks you to agree to terms and conditions, agree to them.

If it asks for a password, I can't get around that. You will need to ask the network administrator for it. Once you are connected, you will see a blue checkmark next to the network name.""",
             ]},
        ],
    },
    {
        "task_id": "TR-008",
        "task_type": "display_scale",
        "task": "Make everything on screen bigger",
        "platform": "Windows 11",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Make text and apps bigger", "url": "https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64"},
        "source_notes": """Windows 11, make text bigger: 1. Open Accessibility settings by pressing Windows logo key+U, or go to Start > Settings > Accessibility. 2. Select "Text size". 3. Drag the "Text size" slider to the right to enlarge the sample text. 4. Select "Apply". Windows scales up all text. This affects title bars, menus, and icon labels.
Make images and apps bigger (Scale): 1. Open Settings by pressing Windows logo key+I, or go to Start > Settings. 2. Select "Display". 3. Under "Scale & layout", expand the "Scale" menu and choose the option you want. Scale enlarges everything on screen, including images and apps.
Notes: most changes take effect immediately. Some apps may require you to sign out and back in.
Not covered: Windows 10 steps, Magnifier, browser zoom, specific percentages like 125% or 150%, a way to change it back.
NOTE: pilot-008 names 125% and 150% and says you can change it back; the page does not list them.""",
        "examples": [
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "Windows 11",
             "messages": [
                 "My Windows 11 laptop is hard for me to read, can you make it bigger?",
                 """I can help with that. Do you want just the **words** bigger, or **everything** on the screen, including pictures and programs?""",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "My Windows 11 laptop is hard for me to read, can you make it bigger?",
                 """I can help with that. Do you want just the **words** bigger, or **everything** on the screen, including pictures and programs?""",
                 "just the words",
                 """Here is how to make just the words bigger on Windows 11.

1. Click **Start**, then click **Settings**.
2. Click **Accessibility**.
3. Click **Text size**.
4. Drag the **Text size** slider to the right. The sample text gets bigger.
5. Click **Apply**.

Windows will make the text bigger on title bars, menus, and icon labels.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "My eyes aren't what they used to be. I'm on a Windows 11 computer. The pictures and the windows are fine, it's the writing under the little icons and the menus at the top that I can barely read. I don't want to change the whole screen, only the writing. What do I do?",
                 """You can make only the writing bigger, and leave the pictures and windows as they are.

1. Press the **Windows logo key** and the **U** key together. This opens Accessibility settings.
2. Click **Text size**.
3. Drag the **Text size** slider to the right until the sample text looks easy to read.
4. Click **Apply**.

Windows will make the text bigger on title bars, menus, and icon labels.

If the Windows logo key and U do not work, click **Start**, click **Settings**, then click **Accessibility**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "Everything on my Windows 11 screen is too small, the pictures, the programs, all of it. I'd like the fastest way, I heard there is a key I can press so I don't have to click around the Start menu. Is there?",
                 """Yes. A key shortcut opens Settings directly.

1. Press the **Windows logo key** and the **I** key together. Settings opens.
2. Click **Display**.
3. Under **Scale & layout**, click the **Scale** menu.
4. Choose a bigger option from the list.

Scale makes everything on the screen bigger, including pictures and programs. Most changes show up right away.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "Please help me make everything bigger on my Windows 11 laptop screen.",
                 """Here is how to make everything on the screen bigger.

1. Click **Start**, then click **Settings**.
2. Click **Display**.
3. Under **Scale & layout**, click the **Scale** menu.
4. Choose a bigger option.

Most changes show up right away.""",
                 "Most of it got bigger but one program still looks tiny.",
                 """Some programs only show the change after you sign out and sign back in.

1. Save your work in your programs.
2. Sign out of Windows.
3. Sign back in and open the program again.""",
             ]},
        ],
    },
    {
        "task_id": "TR-009",
        "task_type": "internet_not_working",
        "task": "Internet not working (message cut off)",
        "platform": "unknown",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: If you can't connect to Wi-Fi on your iPhone or iPad", "url": "https://support.apple.com/en-euro/111786"},
        "source_notes": """Check Wi-Fi settings: 1. Open Settings and tap Wi-Fi, make sure Wi-Fi is turned on. 2. To join a network, tap the network name. 3. Look for a blue checkmark to confirm you're connected. 4. If you still can't connect, go back to Settings and make sure Airplane Mode is off. 5. Tap Wi-Fi again and make sure Connectivity Assist is off. If the Wi-Fi setting is dimmed (grayed out), restart your device. 6. If you still see "No Internet Connection", there may be another issue; check your router and network settings.
VPN and security software (if installed): uninstall the software, restart your device, test the Wi-Fi connection. If uninstalling fixes the issue but you must keep the software, contact your VPN manager or security software provider.
Only one network: if your network doesn't appear, it may be hidden by technology that blocks unauthorized devices or may not meet Apple's recommendations. If you don't manage your network and can't change its configuration, contact your internet service provider (ISP).
Verify the router: check whether other devices can connect (if they can, the router and network are working). Update router firmware and confirm it supports your Apple product (contact the router's manufacturer for help). Make sure the router is on and within range; if it supports separate frequencies, try 5 GHz instead of 2.4 GHz. Unplug the router and cable modem, then plug them back in to restart them.
Reset network settings (only if other solutions fail): removes all network settings, including home, work and school configurations; if a school or business manages your network, consult IT first. Steps: Settings, General, Transfer or Reset [device], Reset, Reset Network Settings. This resets Wi-Fi networks and passwords, cellular settings, VPN and APN settings. If the device connects to Wi-Fi but still has no internet, contact your ISP.
More help: if connected to Wi-Fi but can't get online, try the same network on other devices. If other devices can't get online either, there may be a service outage; contact your ISP. Try a different location. If your device can't connect to any Wi-Fi network, contact Apple.
Not covered: a restart method, the exact Airplane Mode screen.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iOS",
             "messages": [
                 "My iPhone won't get on the internet at home. The wifi at home is the only thing I use. What should I check?",
                 """Let's check a few things on your iPhone. Stop when it works.

1. Open **Settings**, then tap **Wi-Fi**. Make sure **Wi-Fi** is turned on.
2. Tap the name of your home network. Look for a blue checkmark next to it.
3. If it still does not work, go back to **Settings** and make sure **Airplane Mode** is off.
4. Tap **Wi-Fi** again and make sure **Connectivity Assist** is off.

If you still see **No Internet Connection**, the problem may be with your router. Check your router and network settings.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iOS",
             "messages": [
                 "Last week my grandson put a VPN app on my iPhone so I could watch shows from home. Ever since then my phone says it's connected to the wifi but nothing loads. The wifi worked fine before that and my other devices are fine too. What do I do?",
                 """The VPN app may be getting in the way. Try this.

1. Uninstall the VPN app.
2. Restart your iPhone.
3. Test your Wi-Fi connection again.

If that fixes it, you know the app was the cause. If you need to keep the app, contact whoever manages your VPN or the company that makes the app.""",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iOS",
             "messages": [
                 "the internet on my",
                 """It looks like your message got cut off, but I'd be glad to help with your internet.

**Which device is having trouble** (for example your phone, computer, or TV), and **what happens when you try to go online?**""",
                 "my iPhone, it won't connect to the wifi at home",
                 """Thank you. Let's check your iPhone. Stop when it connects.

1. Open **Settings**, then tap **Wi-Fi**. Make sure **Wi-Fi** is turned on.
2. Tap the name of your home network. Look for a blue checkmark.
3. If it still won't connect, go back to **Settings** and make sure **Airplane Mode** is off.
4. Tap **Wi-Fi** again and make sure **Connectivity Assist** is off.

If you still see **No Internet Connection**, check your router and network settings.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iOS",
             "messages": [
                 "My iPhone says it's on the wifi but I can't get any web pages. The password to my wifi is written down somewhere I can't find, so please don't have me do anything that would make me forget the wifi and type the password again. What can I do?",
                 """You can try these without losing your saved Wi-Fi password. Do not use **Reset Network Settings**, because it removes your saved Wi-Fi networks and passwords.

1. See if other devices, like a tablet or another phone, can get online on the same network. If they can, the router is working.
2. Make sure the router is on and close to you.
3. Unplug the router and the cable modem, then plug them back in.
4. If other devices cannot get online either, there may be an outage. Contact your internet service provider.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iOS",
             "messages": [
                 "My iPhone will not connect to my home wifi. Please tell me what to try.",
                 """Let's check a few things on your iPhone.

1. Open **Settings**, then tap **Wi-Fi**. Make sure **Wi-Fi** is turned on.
2. Tap your home network name. Look for a blue checkmark.
3. If it still does not work, go back to **Settings** and make sure **Airplane Mode** is off.
4. Tap **Wi-Fi** again and make sure **Connectivity Assist** is off.""",
                 "The wifi setting is gray and I can't tap it.",
                 """When the Wi-Fi setting is grayed out, the fix is to restart your iPhone.

1. Restart your iPhone.
2. Open **Settings** and tap **Wi-Fi** again.
3. Tap your home network name and look for a blue checkmark.

If it still will not connect to any Wi-Fi network, contact Apple.""",
             ]},
        ],
    },
    {
        "task_id": "TR-010",
        "task_type": "account_password_reset",
        "task": "Reset forgotten Apple Account password",
        "platform": "iPhone",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "Apple Support: Change your Apple Account password", "url": "https://support.apple.com/en-mz/101567"},
        "source_notes": """iPhone, iPad, Apple Watch, Apple Vision Pro: 1. Open Settings and tap your name. 2. Tap Sign-In & Security. 3. Tap Change Password. 4. Follow the onscreen instructions. 5. If other devices are signed in, choose Remove Other Devices to require signing in again on them, or Keep All Devices Signed In.
Mac: 1. Choose the Apple menu, then System Settings. 2. Click your name, then Sign-In & Security. 3. Click Change Password. 4. Enter the password used to unlock your Mac, then follow the onscreen instructions.
Web: 1. Go to account.apple.com and sign in. 2. Go to Sign-In and Security and choose Password. The site redirects you to a trusted device when possible. You might only be able to change the password on the web if you have no trusted device.
Child's account: Settings, Family, choose the child, Change [child's Name] Password; if Screen Time is on you may first need Personal Information.
Tips: the easiest and most secure method is a trusted device already signed in with two-factor authentication. You might have to wait one hour before changing the password because of Stolen Device Protection.
Forgotten password: the page only links to a separate article on regaining access (not included). No recovery key or account recovery steps are given here. So examples cover CHANGING the password only.
NOTE: pilot-010 says to use the iPhone unlock passcode, to type the new password twice, and to write it down; the page does not say these things.""",
        "examples": [
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I need to change my Apple ID password",
                 """I can help with that. Which device are you using: an **iPhone or iPad**, a **Mac**, or a **web browser** on a computer?""",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPad",
             "messages": [
                 "I need to change my Apple ID password",
                 """I can help with that. Which device are you using: an **iPhone or iPad**, a **Mac**, or a **web browser** on a computer?""",
                 "my iPad",
                 """Here is how to change your Apple Account password on your iPad.

1. Open **Settings**.
2. Tap **your name** at the top.
3. Tap **Sign-In & Security**.
4. Tap **Change Password**.
5. Follow the instructions on the screen.
6. If other devices are signed in, choose **Remove Other Devices** or **Keep All Devices Signed In**.

If it asks you to wait about an hour, that is a security feature called Stolen Device Protection.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "web",
             "messages": [
                 "My nephew told me I should change my Apple ID password every so often. I'm at my computer at the library and I only have the internet browser, no Apple stuff on this machine. Is there a way to do it on a website?",
                 """Yes, you can do it on the Apple website.

1. Go to **account.apple.com** and sign in.
2. Go to **Sign-In and Security**.
3. Choose **Password**.

If you have an Apple device you trust, the website may send you to that device to finish. That is normal. The website may only let you change the password itself if you have no trusted device.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iOS",
             "messages": [
                 "I want to change my Apple Account password on my iPhone, but my wife uses the iPad that is signed in with my account too and I don't want her kicked out of it while I change it. Can I do that?",
                 """Yes. You can choose to keep your other devices signed in.

1. Open **Settings** and tap **your name** at the top.
2. Tap **Sign-In & Security**.
3. Tap **Change Password**.
4. Follow the instructions on the screen.
5. When it asks about other signed in devices, choose **Keep All Devices Signed In**.

Do not choose **Remove Other Devices**, because that makes the iPad sign in again.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iOS",
             "messages": [
                 "Please walk me through changing my Apple Account password on my iPhone.",
                 """Here is how to change it on your iPhone.

1. Open **Settings** and tap **your name**.
2. Tap **Sign-In & Security**.
3. Tap **Change Password**.
4. Follow the instructions on the screen.
5. If other devices are signed in, choose **Remove Other Devices** or **Keep All Devices Signed In**.""",
                 "It says I have to wait an hour before I can change it. Is something wrong?",
                 """Nothing is wrong. You might have to wait one hour before changing your password because of a security feature called Stolen Device Protection.

1. Wait one hour.
2. Then open **Settings**, tap **your name**, tap **Sign-In & Security**, and tap **Change Password** again.""",
             ]},
        ],
    },
    {
        "task_id": "TR-011",
        "task_type": "software_update",
        "task": "Install a software update",
        "platform": "iPhone",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: Update your iPhone or iPad", "url": "https://support.apple.com/en-ie/118575"},
        "source_notes": """Manual update wirelessly: 1. Back up your device using iCloud or your computer. 2. Plug the device into power and connect to Wi-Fi. 3. Open Settings, tap General, then tap Software Update. This shows your installed iOS version and whether an update is available. 4. If an update is available, tap Download and Install and follow the onscreen instructions.
Space message: tap Continue to let the system temporarily remove apps (they are reinstalled automatically afterward), or tap Cancel to delete content manually and free up space.
If you can't see the update: use a computer instead (separate guides for Mac and Windows PC).
Automatic updates (optional): Settings, General, Software Update, Automatic Updates. Turn on Automatically Install to download and install updates overnight while charging on Wi-Fi; you're notified before installation. Or turn on Automatically Download to download in the background so you can install later (this option appears only when Automatically Install is off).
Troubleshooting: an alert while updating wirelessly links to a separate guide. Some updates aren't available wirelessly. VPN or proxy connections may stop the device reaching update servers.
Not covered: Install Now, Later, Remind me later, Tonight, passcode entry, how long it takes, the device restarting, how to back up.
NOTE: pilot-011 mentions an Update Now button, a passcode prompt, and the phone turning off and on; the page does not say these.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iOS",
             "messages": [
                 "My iPhone says iOS has something new to install. What do I press to get it on there?",
                 """Here is how to update your iPhone.

1. Back up your iPhone using iCloud or your computer.
2. Plug your iPhone into a power source.
3. Connect your iPhone to Wi-Fi.
4. Open **Settings**.
5. Tap **General**.
6. Tap **Software Update**. It shows whether an update is available.
7. Tap **Download and Install**.
8. Follow the instructions on the screen.

If you see a message about space, tap **Continue** to let your iPhone temporarily remove some apps. They are put back by themselves afterward.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my phone says there is a new update. how do i put it on",
                 """I can help with that. Is your phone an **iPhone** or an **Android** phone?""",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iOS",
             "messages": [
                 "my phone says there is a new update. how do i put it on",
                 """I can help with that. Is your phone an **iPhone** or an **Android** phone?""",
                 "iphone",
                 """Here is how to put the update on your iPhone.

1. Back up your iPhone using iCloud or your computer.
2. Plug your iPhone into a power source and connect it to Wi-Fi.
3. Open **Settings**.
4. Tap **General**.
5. Tap **Software Update**.
6. Tap **Download and Install**.
7. Follow the instructions on the screen.

If you do not see the update on your phone, you can update using a computer instead.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iOS",
             "messages": [
                 "I always forget to update my iPhone and I don't want to sit and watch it while it updates. I'd like it to just happen at night while I'm asleep and the phone is on the charger. Can it?",
                 """Yes, you can turn on automatic updates.

1. Open **Settings**.
2. Tap **General**.
3. Tap **Software Update**.
4. Tap **Automatic Updates**.
5. Turn on **Automatically Install**.

Your iPhone will then download and install updates overnight while it is charging and on Wi-Fi. It will notify you before it installs.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iOS",
             "messages": [
                 "Show me how to install the newest update on my iPhone please.",
                 """Here is how to update your iPhone.

1. Back up your iPhone using iCloud or your computer.
2. Plug it into a power source and connect to Wi-Fi.
3. Open **Settings**, tap **General**, then tap **Software Update**.
4. Tap **Download and Install**.
5. Follow the instructions on the screen.""",
                 "It says there isn't enough space. Now what?",
                 """You have two choices.

1. Tap **Continue** to let your iPhone temporarily remove some apps. They are put back by themselves after the update.
2. Or tap **Cancel** and delete some things yourself to free up space.""",
             ]},
        ],
    },
    {
        "task_id": "TR-012",
        "task_type": "email_attach",
        "task": "Attach a photo to an email",
        "platform": "Gmail (computer)",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Gmail Help: Send attachments with your Gmail message", "url": "https://support.google.com/mail/answer/6584"},
        "source_notes": """Computer: 1. Go to Gmail in your browser. 2. Click Compose. 3. At the bottom of the window, click the icon labeled Attach. 4. Choose the files you want to upload. 5. Click Open.
Drag and drop: you can add an image by dragging it directly into the compose window (a tip, not a full procedure). No separate photo-insert steps.
Size limits: personal Gmail accounts 25 MB; work and school accounts, your Google Workspace administrator sets limits. Over the limit: Gmail removes the attachment and adds it to the email as a Google Drive link. For large files such as videos, the page recommends Google Drive.
Remove an attachment: click Close to the right of the attachment name.
Not covered: mobile steps, a Send step, the paperclip picture, a Pictures folder, what the attachment looks like.
NOTE: pilot-012 says paperclip icon, Pictures folder and Send; the page says the icon is labeled Attach.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "How do I put a picture in an email in Gmail on my computer?",
                 """Here is how to add a picture to your email in Gmail on a computer.

1. Go to Gmail in your browser.
2. Click **Compose**.
3. At the bottom of the email window, click **Attach**.
4. Choose the picture you want to send.
5. Click **Open**.

If the picture is too big for a personal Gmail account (over 25 MB), Gmail removes it and puts it in the email as a Google Drive link instead.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "want to email my grandson a snapshot, where do I start",
                 """I can help with that. Are you using **Gmail** on a computer, or a different email program?""",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "want to email my grandson a snapshot, where do I start",
                 """I can help with that. Are you using **Gmail** on a computer, or a different email program?""",
                 "gmail on my computer",
                 """Here is how to send a picture in Gmail on your computer.

1. Go to Gmail in your browser.
2. Click **Compose**.
3. At the bottom of the email window, click **Attach**.
4. Choose the picture you want to send.
5. Click **Open**.

If the picture is very large, Gmail may add it to the email as a Google Drive link instead of attaching it.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "I'm writing an email in Gmail on my computer and my picture is already showing in a folder on the screen next to it. The little buttons at the bottom are hard for me to hit with my shaky hand. Can I just pull the picture over into the email instead of using the button?",
                 """Yes, you can add the picture by dragging it.

1. Click the picture in the folder window and hold the mouse button down.
2. Drag it into your email window.
3. Let go of the mouse button.

If dragging is hard, the other way is the **Attach** button at the bottom of the email window.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "Show me how to attach a photo in Gmail on my computer please.",
                 """Here is how to attach a photo in Gmail on your computer.

1. Go to Gmail in your browser.
2. Click **Compose**.
3. At the bottom of the email window, click **Attach**.
4. Choose the photo you want.
5. Click **Open**.""",
                 "I picked the wrong photo and it's in the email now. How do I take it out?",
                 """You can remove it easily.

1. Find the photo's name in your email.
2. Click **Close** to the right of the photo's name.

Then use **Attach** again to add the right photo.""",
             ]},
        ],
    },
    {
        "task_id": "TR-013",
        "task_type": "backup_photos",
        "task": "Back up photos",
        "platform": "iPhone (iCloud Photos)",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple iCloud User Guide: Set up and use iCloud Photos", "url": "https://support.apple.com/guide/icloud/mm7e90c1ba48"},
        "source_notes": """Prerequisite: sign in to the same Apple Account on each device. If a device isn't signed in, or iCloud Photos is off, you can't access your photos there.
iPhone or iPad: 1. Go to Settings > your name > iCloud. 2. Tap Photos, then turn on "Sync this [device]". What happens: photos and videos in the Photos app are added to iCloud; photos already in iCloud Photos become available on the device. View: open Photos and tap Library. Check progress: tap Collections, then tap your profile in the top right corner; status appears below your name.
Mac: in the Photos app choose Photos > Settings, click iCloud, select iCloud Photos. View: click Library in the sidebar. Check progress: scroll to bottom.
Windows: iCloud for Windows; click arrow right of iCloud Photos, turn on iCloud Photos, click Done.
iCloud.com: go to icloud.com/photos and sign in with your Apple Account.
Troubleshooting: confirm the same Apple Account on every device; confirm iCloud Photos is on for that device; for sync problems see "If your iCloud Photos aren't syncing to your device".
Not covered: Wi-Fi vs cellular upload, storage amounts, Optimize iPhone Storage, what happens when storage is full, charging.
NOTE: pilot-013 says keep connected to Wi-Fi and charging and mentions a storage-full message; the page does not say these.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iOS",
             "messages": [
                 "I have an iPhone. How do I turn on iCloud Photos so my pictures are saved online?",
                 """Here is how to turn on iCloud Photos on your iPhone.

1. Open **Settings**.
2. Tap **your name** at the top.
3. Tap **iCloud**.
4. Tap **Photos**.
5. Turn on **Sync this iPhone**.

Your photos and videos are then added to iCloud. To see them, open the **Photos** app and tap **Library**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my phone has thousands of pictures of the kids on it and I'm scared I'll lose them. can you help me save them somewhere",
                 """I can help with that. Is your phone an **iPhone** or an **Android** phone?""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "My husband handles the computer stuff but he's traveling. We have a Mac and all of our family pictures are in the Photos app on it. I want them kept safe in iCloud in case the computer breaks. I'm signed in with my Apple Account already. What do I click?",
                 """Here is how to keep your Mac's photos in iCloud.

1. Open the **Photos** app.
2. In the menu at the top of the screen, click **Photos**, then click **Settings**.
3. Click **iCloud**.
4. Select **iCloud Photos**.

The photos and videos in Photos are then added to iCloud. To check on progress, scroll to the bottom of the Photos screen.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iOS",
             "messages": [
                 "I want my iPhone pictures saved to iCloud, and I also want to look at them on my old laptop. But I don't want to install anything on the laptop, it's slow already. Is there a way?",
                 """Yes. You can see them in a web browser, with nothing to install.

1. On your iPhone, open **Settings** and tap **your name**.
2. Tap **iCloud**, then tap **Photos**.
3. Turn on **Sync this iPhone**.
4. On your laptop, open a web browser and go to **icloud.com/photos**.
5. Sign in with your Apple Account.

Use the same Apple Account on both.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iOS",
             "messages": [
                 "Please show me how to save my iPhone photos to iCloud.",
                 """Here is how to save your iPhone photos to iCloud.

1. Open **Settings** and tap **your name** at the top.
2. Tap **iCloud**.
3. Tap **Photos**.
4. Turn on **Sync this iPhone**.""",
                 "I turned it on but I can't tell if anything is happening. How do I check?",
                 """You can check the progress in the Photos app.

1. Open the **Photos** app.
2. Tap **Collections**.
3. Tap your **profile picture** in the top right corner.
4. Look below your name for the status.

If it still doesn't seem right, make sure you are signed in to the same Apple Account and that iCloud Photos is turned on.""",
             ]},
        ],
    },
]
