TASKS = [
    {
        "task_id": "TR-128",
        "task_type": "bluetooth_pair",
        "task": "Pair a Bluetooth accessory such as headphones or a speaker",
        "platform": "iPhone",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: Pair a third-party Bluetooth accessory with your iPhone or iPad", "url": "https://support.apple.com/en-us/HT204091"},
        "source_notes": """Steps: 1. Go to Settings, tap Bluetooth, and turn on Bluetooth. 2. Under My Devices, look for the accessory you want to pair. 3. Tap the name of your accessory when it appears. You might need to enter your PIN or passcode (check the accessory's manual or online instructions for the code). 4. Repeat these steps to pair multiple accessories.
Condition: if the accessory is not listed, put it in discoverable (pairing) mode; the accessory's manual or online instructions explain how. Also confirm it is powered on and charged.
Troubleshooting: PIN or passcode rejected or unknown: use the code in the accessory's manual or online instructions. Pairing still fails: Apple has a separate article with more fixes (not given here). Remove an accessory: Settings > Bluetooth, tap the More Info button next to the device, tap Forget this Device (it can be paired again later).
The page does not describe a confirmation screen.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I just bought wireless headphones. How do I connect them to my iPhone?",
                 """Here is how to pair them with your iPhone.

1. Turn your headphones on and put them in pairing mode. The headphone manual explains how.
2. On your iPhone, open **Settings**.
3. Tap **Bluetooth**, and make sure Bluetooth is turned on.
4. Under **My Devices**, look for your headphones.
5. Tap the name of your headphones when it appears.

If it asks for a PIN or passcode, the code is in the headphone manual or in the maker's online instructions.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My grandson gave me a little Bluetooth speaker for my birthday and I want to play my music from my iPhone on it. It is in the box on the kitchen table and it has a light that blinks. I have never connected anything to my phone before. What do I do?",
                 """Happy birthday! Connecting a speaker takes only a few taps.

1. Turn the speaker on and put it in pairing mode. The speaker's manual or online instructions show how.
2. On your iPhone, open **Settings**.
3. Tap **Bluetooth**, and turn Bluetooth on if it is off.
4. Under **My Devices**, look for your speaker.
5. Tap the speaker's name when it appears.

If it asks for a PIN or passcode, check the speaker's manual or online instructions for the code.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my new earbuds wont hook up to my phone, what do i do",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "my new earbuds wont hook up to my phone, what do i do",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "iPhone",
                 """Here is how to pair your earbuds with your iPhone.

1. Turn your earbuds on and put them in pairing mode. Their manual explains how.
2. Open **Settings** on your iPhone.
3. Tap **Bluetooth**, and make sure Bluetooth is on.
4. Under **My Devices**, look for your earbuds.
5. Tap their name when it appears.

If it asks for a PIN or passcode, check the earbuds' manual or online instructions for the code.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I am trying to connect a Bluetooth speaker to my iPhone and it is asking me for a PIN. I threw away the paper manual a long time ago and I have no idea what the number is. Where can I find it?",
                 """The speaker may ask for a PIN or passcode, and you can enter it at the pairing prompt.

1. Look for the PIN or passcode. If you need help, check the speaker's manual or its online instructions.
2. Go back to the pairing prompt on your iPhone and enter the PIN or passcode.

If the prompt has closed, open **Settings**, tap **Bluetooth**, tap your speaker's name under **My Devices**, and enter the code.

If the code does not work, check the speaker's manual or its online instructions again.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "sources": [{"title": 'Apple Support: Pair a third-party Bluetooth accessory with your iPhone or iPad', "url": 'https://support.apple.com/en-us/HT204091', "accessed": "2026-11-13"},
                         {"title": "Apple Support: If you can't pair a Bluetooth accessory with your iPhone or iPad", "url": 'https://support.apple.com/en-us/111804', "accessed": "2026-11-13"}],
             "messages": [
                 "Could you tell me the way to pair some Bluetooth headphones with an iPhone?",
                 """Here is how to pair them.

1. Turn your headphones on and put them in pairing mode.
2. On your iPhone, open **Settings**.
3. Tap **Bluetooth**, and make sure Bluetooth is on.
4. Under **My Devices**, look for your headphones.
5. Tap their name when it appears.

If it asks for a PIN or passcode, check the headphone manual for the code.""",
                 "I did all that but my headphones are not showing up in the list under My Devices.",
                 """That usually means the headphones are not ready to be found yet. Try this.

1. Make sure the headphones are turned on and charged, and keep them close to your iPhone.
2. Put them in discoverable (pairing) mode again. The headphone manual or online instructions explain how.
3. Go back to **Settings**, then **Bluetooth**, and look under **My Devices** again.
4. Tap their name when it appears.""",
             ]},
        ],
    },
    {
        "task_id": "TR-129",
        "task_type": "bluetooth_pair",
        "task": "Connect a Bluetooth device",
        "platform": "Mac",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: Connect a Bluetooth device with your Mac", "url": "https://support.apple.com/en-us/guide/mac-help/blth1004/mac"},
        "source_notes": """Connect: 1. Turn on the device and make it discoverable (the device's own documentation explains how). 2. Click the Apple menu, choose System Settings. Select Bluetooth in the sidebar (you may need to scroll down to find it). 3. Point at your device in the list and click Connect. If a prompt appears, click Accept, or type the displayed numbers and press Enter.
You can also click the Bluetooth status icon in Control Center and select the device.
Set a Bluetooth audio device as output or input: 1. Apple menu, System Settings, then select Sound in the sidebar (may need to scroll down). 2. Click Output for headphones or speakers, or Input for a headset microphone. 3. Select your device from the list.
Disconnect: open Bluetooth in System Settings, point at the device, click Disconnect. To stop a device reconnecting automatically, Control-click its name and click Forget (must set up again later).
Apple keyboard, mouse, trackpad first time: connect by cable to a USB-C port (some Macs need an adapter), turn the device on (power switch shows green); a notification appears when you can unplug and use it wirelessly. Magic Mouse must be unplugged to work; Magic Keyboard or Trackpad can stay plugged in. Magic devices pair automatically over Bluetooth when connected by cable.
Troubleshooting: if the device does not appear in the list, make sure it is on and discoverable. The page lists macOS versions but notes no differing steps.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "How do I connect my Bluetooth headphones to my Mac?",
                 """Here is how to connect them to your Mac.

1. Turn your headphones on and make them discoverable. The headphone manual explains how.
2. Click the **Apple menu**, then choose **System Settings**.
3. In the sidebar, click **Bluetooth**. You may need to scroll down to find it.
4. Point at your headphones in the list and click **Connect**.
5. If a prompt appears, click **Accept**, or type the numbers it shows and press Enter.

If your headphones are not in the list, check that they are on and discoverable.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "I have a MacBook and a new Bluetooth speaker. I want to connect it and then actually hear my music coming out of the speaker instead of the laptop. I connected it once but the sound still comes out of the laptop. Can you walk me through the whole thing?",
                 """Yes. First connect the speaker, then tell your Mac to play sound through it.

1. Turn the speaker on and make it discoverable. Its manual explains how.
2. Click the **Apple menu**, then choose **System Settings**.
3. Click **Bluetooth** in the sidebar. You may need to scroll down.
4. Point at your speaker in the list and click **Connect**.
5. If a prompt appears, click **Accept**, or type the numbers shown and press Enter.
6. Back in the sidebar, click **Sound**. You may need to scroll down.
7. Click **Output**.
8. Select your speaker from the list.

Now your music should play through the speaker.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "My computer will not find my wireless mouse. How do I hook it up?",
                 "I can help with that. Is your computer a **Mac** or a **Windows** PC?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "My computer will not find my wireless mouse. How do I hook it up?",
                 "I can help with that. Is your computer a **Mac** or a **Windows** PC?",
                 "Mac",
                 """Here is how to connect a Bluetooth mouse to your Mac.

1. Turn the mouse on and make it discoverable. Its manual explains how.
2. Click the **Apple menu**, then choose **System Settings**.
3. Click **Bluetooth** in the sidebar. You may need to scroll down.
4. Point at your mouse in the list and click **Connect**.
5. If a prompt appears, click **Accept**, or type the numbers it shows and press Enter.

If your mouse is an Apple Magic Mouse, you can use a cable instead: plug it into your Mac's USB-C port (you may need an adapter), turn the mouse on and check that its power switch shows green. When a notification appears, you can unplug the cable and use the mouse wirelessly.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "My Bluetooth headphones are already set up on my Mac, they just are not connected right now. I do not want to dig through System Settings every time. Is there a quicker way to connect them?",
                 """Yes, there is a quicker way.

1. Make sure your headphones are on.
2. Click the **Bluetooth** status icon in Control Center.
3. Select your headphones from the list.

If you ever want the longer way, open the **Apple menu**, choose **System Settings**, click **Bluetooth**, point at the headphones, and click **Connect**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "Need to get my Bluetooth speaker working with my Mac, steps please",
                 """Here is how to connect it.

1. Turn the speaker on and make it discoverable.
2. Click the **Apple menu**, then choose **System Settings**.
3. Click **Bluetooth** in the sidebar. You may need to scroll down.
4. Point at the speaker in the list and click **Connect**.
5. If a prompt appears, click **Accept**, or type the numbers shown and press Enter.""",
                 "I opened System Settings but I cannot find Bluetooth anywhere in the sidebar.",
                 """It may just be lower down the list. Try this.

1. In the System Settings sidebar, scroll down.
2. Click **Bluetooth** when you see it.
3. Point at your speaker in the list and click **Connect**.

If the speaker is not listed, check that it is on and discoverable.""",
             ]},
        ],
    },
    {
        "task_id": "TR-130",
        "task_type": "two_step_verification",
        "task": "Turn on two-factor authentication for the Apple Account",
        "platform": "iPhone",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "Apple Support: Two-factor authentication for Apple Account", "url": "https://support.apple.com/en-us/102660"},
        "source_notes": """Turn on on iPhone: 1. Open Settings. 2. Tap your name, then tap Sign-In & Security. 3. Tap Turn on two-factor authentication and follow the onscreen instructions.
Notes: Most accounts already use two-factor authentication, so you may not need to do this. If your Apple Account was created with two-factor authentication, "this extra protection can't be removed." If you recently turned it on, you can lower your account security within two weeks of enrollment. Verification codes are shown on trusted devices or sent to a trusted phone number. The page does not describe the specific onscreen screens; it only says to follow the onscreen instructions.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "How do I turn on two-factor authentication for my Apple Account on my iPhone?",
                 """Here is how to turn it on.

1. Open **Settings** on your iPhone.
2. Tap your name at the top.
3. Tap **Sign-In & Security**.
4. Tap **Turn on two-factor authentication**.
5. Follow the instructions on the screen.

Most accounts already use two-factor authentication, so you may not need to do this.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My son told me I should make my Apple ID safer by adding some extra code step when I sign in. I have an iPhone and I am not good with settings. I do not want to break anything. Can you tell me what to tap?",
                 """That extra step is called two-factor authentication. Here is what to tap.

1. Open **Settings**.
2. Tap your name at the top.
3. Tap **Sign-In & Security**.
4. Tap **Turn on two-factor authentication**.
5. Follow the instructions on the screen.

Many accounts already have it turned on, so you may not need to do this.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "i want to turn on the extra security thing for my apple account",
                 "I can help with that. Are you using an **iPhone**, an **iPad**, or a **Mac**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "i want to turn on the extra security thing for my apple account",
                 "I can help with that. Are you using an **iPhone**, an **iPad**, or a **Mac**?",
                 "iphone",
                 """Here is how to do it on your iPhone.

1. Open **Settings**.
2. Tap your name at the top.
3. Tap **Sign-In & Security**.
4. Tap **Turn on two-factor authentication**.
5. Follow the instructions on the screen.

Most accounts already use two-factor authentication, so you may not need to do this.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I want to turn on two-factor authentication on my iPhone, but only if I can switch it off again later if it turns out to be too much hassle. Is that possible?",
                 """Only for a short time. If you recently turned it on, you can lower your account security within two weeks of enrollment. If your account was created with two-factor authentication, Apple says this extra protection can't be removed.

If you still want to turn it on:

1. Open **Settings**.
2. Tap your name at the top.
3. Tap **Sign-In & Security**.
4. Tap **Turn on two-factor authentication**.
5. Follow the instructions on the screen.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "Please show me how to switch on two-factor authentication on my iPhone for my Apple Account",
                 """Here is how to turn it on.

1. Open **Settings**.
2. Tap your name at the top.
3. Tap **Sign-In & Security**.
4. Tap **Turn on two-factor authentication**.
5. Follow the instructions on the screen.""",
                 "I went there but I do not see Turn on two-factor authentication anywhere.",
                 """Most accounts already use two-factor authentication, so you may not need to turn it on. If you want to look again:

1. Open **Settings**.
2. Tap your name at the top.
3. Tap **Sign-In & Security**.

If your account was created with two-factor authentication, this extra protection can't be removed.

If you still do not see the option at all, go to account.apple.com, sign in to your Apple Account, select Upgrade Account Security, and follow the on-screen steps.""",
             ]},
        ],
    },
    {
        "task_id": "TR-131",
        "task_type": "password_manager",
        "task": "Find saved passwords in the Passwords app and keep them in sync with iCloud Keychain",
        "platform": "iPhone",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "Apple Support: Find saved passwords and passkeys on your iPhone", "url": "https://support.apple.com/en-us/104955"},
        "source_notes": """Find passwords, iOS 18 or later: 1. Open the Passwords app. 2. Authenticate with Face ID, Touch ID, or your passcode. 3. Choose a category or Shared Group, then select the website or app. Your password or passkey appears. To change a password, tap Edit, then Change Password. To delete, tap Edit, then Delete.
Find passwords, iOS 17 or earlier: 1. Open Settings, scroll down, tap Passwords. 2. Authenticate when prompted. 3. Select the website or app. (Change: Edit. Delete: Delete Password or Delete Passkey.)
Siri: say "Show my passwords" or name a site, e.g. "What is my Hulu password?"
This page does not describe a manual way to add a password. iCloud Keychain keeps passwords and passkeys updated across iPhone, iPad, Mac, or PC.
Can't find an entry: in the Passwords app choose All (iOS 17 or earlier: Settings should show Passwords at the top, not a Shared Group name). Check Deleted: in the Passwords app tap Deleted (iOS 17 or earlier: Settings > Passwords, then Recently Deleted). Make sure iCloud Keychain is on if you use multiple Apple devices. Passwords moved to a Shared Group are visible only on devices with compatible software; iPhone needs iOS 17 or later to see them.
Supplement from Apple Support 120758 (Use the Passwords app...): when creating an account on a supported website or app, iPhone suggests a unique, strong password. Turn on iCloud Keychain, if not on at setup: Settings, tap your name at the top, tap iCloud, then Passwords and Keychain, turn on iCloud Keychain. If passwords are not syncing, check iCloud Keychain is on under Settings > [your name] > iCloud > Passwords and Keychain on each device. The Passwords app requires iOS 18 or later. A new device must be approved (through iCloud Keychain or an old device's passcode) before its passwords update.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "Where can I see my saved passwords on my iPhone? It has the newest iOS.",
                 """Your saved passwords are in the Passwords app.

1. Open the **Passwords** app.
2. Unlock it with Face ID, Touch ID, or your passcode.
3. Tap **All**, or choose another category.
4. Tap the website or app you want. Your password appears.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I have an old iPhone that is on iOS 17 and I forgot my password for my bank's website but I know my phone saved it at some point. I do not see any Passwords app on it. How do I look it up?",
                 """On iOS 17, your passwords are in Settings.

1. Open **Settings**.
2. Scroll down and tap **Passwords**.
3. Unlock it with Face ID, Touch ID, or your passcode.
4. Tap the website or app you want. Your password appears.

If you cannot find it, check that you are looking at the main **Passwords** list. Then look in **Recently Deleted**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "where does my phone keep the passwords it saved for me",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "where does my phone keep the passwords it saved for me",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "iPhone",
                 """On an iPhone, saved passwords are in the Passwords app.

1. Open the **Passwords** app.
2. Unlock it with Face ID, Touch ID, or your passcode.
3. Tap **All**.
4. Tap the website or app you want. Your password appears.

If your iPhone is on iOS 17 or earlier, open **Settings**, scroll down, and tap **Passwords** instead.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "sources": [{"title": 'Apple Support: Find saved passwords and passkeys on your iPhone', "url": 'https://support.apple.com/en-us/104955', "accessed": "2026-11-13"},
                         {"title": 'Apple Support: Set up iCloud Keychain (Passwords)', "url": 'https://support.apple.com/en-us/109016', "accessed": "2026-11-13"}],
             "messages": [
                 "I have an iPhone and an iPad. My passwords show up on my iPad but not on my iPhone, and I do not want to type them all in again by hand. How do I get them onto my iPhone?",
                 """You can let them sync with iCloud Keychain. Do this on your iPhone.

1. Open **Settings**.
2. Tap your name at the top.
3. Tap **iCloud**.
4. Under **Saved to iCloud**, tap **Passwords**. On iOS 17 or earlier, tap **Passwords and Keychain**.
5. Turn on **Sync this iPhone**. You may need your passcode or Apple Account password.

Do the same on your iPad. Two-factor authentication must also be on for your Apple Account.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "sources": [{"title": 'Apple Support: Find saved passwords and passkeys on your iPhone', "url": 'https://support.apple.com/en-us/104955', "accessed": "2026-11-13"},
                         {"title": 'Apple Support: Set up iCloud Keychain (Passwords)', "url": 'https://support.apple.com/en-us/109016', "accessed": "2026-11-13"}],
             "messages": [
                 "How do I find a saved password on my iPhone? It is on iOS 18.",
                 """Here is how to find it.

1. Open the **Passwords** app.
2. Unlock it with Face ID, Touch ID, or your passcode.
3. Tap **All**, or choose another category.
4. Tap the website or app you want. Your password appears.""",
                 "I looked but the website I need is not in the list.",
                 """Try these checks.

1. In the Passwords app, tap **All**, so you are looking at everything.
2. Tap **Deleted**, in case the password was removed.
3. If you use more than one Apple device, open **Settings**, tap your name, tap **iCloud**, and under **Saved to iCloud** tap **Passwords**. Make sure **Sync this iPhone** is on.

If the password was moved to a Shared Group, your iPhone needs iOS 17 or later to see it.""",
             ]},
        ],
    },
    {
        "task_id": "TR-132",
        "task_type": "force_restart",
        "task": "iPad is frozen or will not respond",
        "platform": "iPad",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: If your iPad is frozen, doesn't turn on, or doesn't respond", "url": "https://support.apple.com/kb/HT212017"},
        "source_notes": """Force restart, iPad without a Home button: 1. Press and quickly release the volume button closest to the top button. 2. Press and quickly release the volume button farthest from the top button. 3. Press and hold the top button until the Apple logo appears.
iPad with a Home button: Press and hold both the Home button and the top button until the Apple logo appears.
Charging: if the iPad still won't turn on, check the hardware and charge it. Charging can take up to an hour.
Separate section (startup stuck on Apple logo or red/blue screen) needs a computer and recovery mode; not used here. If still not working after charging, Apple says you may need service.
No alternative to pressing buttons together is given for Home button models.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPad",
             "messages": [
                 "My iPad has no Home button and the screen is frozen. Nothing happens when I touch it. What should I do?",
                 """You can force it to restart.

1. Press and quickly let go of the volume button closest to the top button.
2. Press and quickly let go of the volume button farthest from the top button.
3. Press and hold the top button until the Apple logo appears.

If the iPad still will not turn on, charge it. Charging can take up to an hour.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPad",
             "messages": [
                 "My iPad is the older kind with the round Home button under the screen. I was reading and it just stopped. The screen is on but nothing moves and it will not respond to anything. I tried holding the top button and it did not do anything. Help please.",
                 """You can force it to restart. On an iPad with a Home button, use two buttons together.

1. Press and hold the **Home button** and the **top button** at the same time.
2. Keep holding both until the Apple logo appears.

If the iPad still will not turn on, charge it. Charging can take up to an hour.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "iPad",
             "messages": [
                 "my ipad is frozen and wont do anything",
                 "I can help with that. Does your iPad have a **Home button**, or **no Home button**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPad",
             "messages": [
                 "my ipad is frozen and wont do anything",
                 "I can help with that. Does your iPad have a **Home button**, or **no Home button**?",
                 "no home button",
                 """Here is how to force restart an iPad with no Home button.

1. Press and quickly let go of the volume button closest to the top button.
2. Press and quickly let go of the volume button farthest from the top button.
3. Press and hold the top button until the Apple logo appears.

If the iPad still will not turn on, charge it. Charging can take up to an hour.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPad",
             "messages": [
                 "My iPad has no Home button and it is frozen. I have arthritis in my hands, so I cannot hold two buttons down at the same time. Is there a way to restart it without that?",
                 """Yes. On an iPad with no Home button, you press the buttons one at a time.

1. Press and quickly let go of the volume button closest to the top button.
2. Press and quickly let go of the volume button farthest from the top button.
3. Press and hold the top button until the Apple logo appears.

You only hold one button, the top button, at the end.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPad",
             "messages": [
                 "My iPad with no Home button is frozen. How do I force restart it?",
                 """Here is how.

1. Press and quickly let go of the volume button closest to the top button.
2. Press and quickly let go of the volume button farthest from the top button.
3. Press and hold the top button until the Apple logo appears.""",
                 "I did it and held the top button but the screen stayed black. No Apple logo came up.",
                 """The iPad may be out of battery, so charge it.

1. Plug the iPad into its charger and let it charge. Charging can take up to an hour.
2. After it has charged, try the force restart steps again.

If it still does not turn on, you may need to get it serviced by Apple.""",
             ]},
        ],
    },
    {
        "task_id": "TR-133",
        "task_type": "report_spam_text",
        "task": "Report and block junk text messages",
        "platform": "iPhone",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "Apple iPhone User Guide: Report spam and block senders in Messages", "url": "https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios"},
        "source_notes": """Report spam (iMessage). Message not opened: 1. Open Messages. 2. Swipe left on the message. 3. Tap the Delete button (trash icon). 4. Tap Delete and Report Spam. Message already opened: open Messages and the message, tap the Report Spam link at the bottom of the message (appears for messages from unknown senders), then tap Delete and Report Spam. You can't report a message after you've replied to it. For iMessage, the reported message goes to Apple with the sender's information and is permanently deleted from your iPhone. For SMS, MMS or RCS, reporting depends on your carrier and country or region and shares the information with your carrier and its affiliates; if you don't see the option, contact your carrier. If you accidentally report and delete a message you can recover it.
Reporting does not stop the sender. To stop their messages, block the contact.
Block: 1. Open Messages. 2. Open the conversation with the sender and tap the person's icon at the top. 3. Tap Info, scroll down, tap Block Contact. Blocked messages aren't delivered and the sender doesn't know they are blocked. Blocking also applies to Mail, Phone, FaceTime, Calendar and other apps. You can't block a group conversation (leave the group or stop its notifications instead).
Spam folder: detected spam moves to the spam folder and does not appear in the conversation list. Spam filtering is on by default (Filter, Manage Filtering, Filter spam). Recover: tap Filter, tap Spam, open message, tap Not Spam, tap Move to Messages.
Check or unblock: Settings, Privacy & Security, Blocked Contacts. Swipe left on a number and tap Unblock, or Edit and Remove.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I got a junk text on my iPhone from a number I do not know and I have not opened it. How do I report it?",
                 """You can report it without opening it.

1. Open the **Messages** app.
2. Swipe left on the junk message.
3. Tap the Delete button. It appears as an icon, not a word.
4. Tap **Delete and Report Spam**.

Reporting does not stop the sender from texting you. To stop them, block the contact.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "Every day I get texts on my iPhone from some random number trying to sell me things and I am sick of it. I have not opened the latest one. I want to report it and also make them stop. What exactly do I tap?",
                 """Reporting alone will not stop them, so do both. First, report the message.

1. Open the **Messages** app.
2. In the **Messages** list, swipe left on the message.
3. Tap the Delete button. It appears as an icon, not a word.
4. Tap **Delete and Report Spam**.

Now block them.

1. Open the conversation with the sender and tap the person's icon at the top.
2. Tap **Info**.
3. Scroll down and tap **Block Contact**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "how do i report and block junk texts",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "how do i report and block junk texts",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "iphone",
                 """On an iPhone, reporting does not stop the sender, so you also need to block them.

1. Open the **Messages** app.
2. In the **Messages** list, swipe left on the message.
3. Tap the Delete button. It appears as an icon, not a word.
4. Tap **Delete and Report Spam**.

If you already opened it, open the message, tap **Report Spam** at the bottom (this link appears on messages from unknown senders), then tap **Delete and Report Spam**.

Now block them.

1. Open the conversation with the sender and tap the person's icon at the top.
2. Tap **Info**.
3. Scroll down and tap **Block Contact**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "A stranger texted my iPhone and I already wrote back to ask who they were. Now they keep texting. Can I still report them as spam?",
                 """No, you cannot report a message after you have replied to it. You can still block them, which stops their messages from reaching you.

1. Open the **Messages** app.
2. Open the conversation with the sender and tap the person's icon at the top.
3. Tap **Info**.
4. Scroll down and tap **Block Contact**.

The sender does not know they have been blocked.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I opened a junk text on my iPhone. How do I report it?",
                 """Here is how to report it.

1. Open the **Messages** app and open the message.
2. Tap the **Report Spam** link at the bottom of the message.
3. Tap **Delete and Report Spam**.

Reporting does not stop the sender. To stop them, block the contact.""",
                 "There is no Report Spam link at the bottom of my message.",
                 """The link only appears for messages from unknown senders, and you cannot report a message you have replied to. For SMS, MMS, or RCS messages without this option, contact your carrier.

You can still block the sender.

1. Open the **Messages** app.
2. Open the conversation and tap the person's icon at the top.
3. Tap **Info**.
4. Scroll down and tap **Block Contact**.""",
             ]},
        ],
    },
]
