Q_OS = "I can help with that. Is your computer a **Windows PC** or a **Mac**?"

TASKS = [
    {
        "task_id": "TR-173",
        "task_type": "free_storage",
        "task": "Free up drive space",
        "platform": "Windows 11",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Free up drive space in Windows", "url": "https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32"},
        "source_notes": """Check space: File Explorer on taskbar, This PC, free space under Devices and drives.
Cleanup recommendations: Start > Settings > System > Storage > Cleanup recommendations. Categories: Temporary files, Large or unused files, Files synced to the cloud, Unused apps. Select the items to remove; Windows shows how much space each will save. Select the Clean up button for each section. If upgraded Windows fewer than 10 days ago, previous version appears as a system file you can delete; deleting it removes the Windows.old folder, which allows rollback; cannot be undone.
Delete or move personal files: open File Explorer, select a folder under This PC (Videos, Music, Pictures, Downloads often hold largest files). Select View > Details. Right-click open area (or press and hold), Sort by > Size to list largest first. Delete unneeded files or move to external storage. Empty the Recycle Bin to fully remove deleted files.
Move files you keep but rarely use: connect USB drive or SD card; in File Explorer select files, select Cut on the ribbon; go to external device, select Paste. Files on external storage work only while drive connected.
Save new files elsewhere: Start > Settings > System > Storage > Advanced storage settings > Where new content is saved; pick a drive per content type.
Storage Sense: no setup steps on this page.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "My Windows 11 laptop says the drive is almost full. How can I clear some space?",
                 """Windows has a cleanup tool that shows what you can safely remove. Here is how to use it:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Storage**.
3. Select **Cleanup recommendations**.
4. Look at the groups: **Temporary files**, **Large or unused files**, **Files synced to the cloud**, and **Unused apps**. Tick the items you want to remove. Windows shows how much space each one will save.
5. Select the **Clean up** button in each section.

If you want to see how much room you have, open **File Explorer**, select **This PC**, and look under **Devices and drives**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "So my grandson helped me update my Windows 11 computer last week and ever since then I keep getting told there is not enough storage. I think the old version of Windows might still be sitting there taking up room. Can you show me how to get rid of it? I do not need to go back.",
                 """Yes, the older version of Windows can be removed from the same cleanup screen:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Storage**.
3. Select **Cleanup recommendations**.
4. Find the previous version of Windows in the list. After a recent upgrade it shows up as a system file you can delete. Tick it.
5. Select the **Clean up** button.

Please note that this removes the Windows.old folder, so you will not be able to go back to the older version. It cannot be undone.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my computer keeps saying i am out of space what do i do",
                 Q_OS,
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "my computer keeps saying i am out of space what do i do",
                 Q_OS,
                 "Windows PC, it has Windows 11",
                 """Thanks. On Windows 11 you can use the cleanup tool:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Storage**.
3. Select **Cleanup recommendations**.
4. Tick the items you want to remove from **Temporary files**, **Large or unused files**, **Files synced to the cloud**, or **Unused apps**. Windows shows how much space each will save.
5. Select the **Clean up** button in each section.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "I have a Windows 11 PC full of old family photos and videos in the Pictures and Videos folders. I do not want to delete any of them, but I need room. I have a USB drive here. Can I move them instead?",
                 """Yes, you can move them to the USB drive instead of deleting them:

1. Plug the USB drive into the computer.
2. Open **File Explorer** from the taskbar.
3. Open the folder with your photos or videos and select the files you want to move.
4. Select **Cut** on the ribbon at the top.
5. Open the USB drive in **File Explorer**.
6. Select **Paste**.

You can still use the files when the drive is connected, but they will not take up space on your computer.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "How do I free up space on my Windows 11 computer?",
                 """You can use the cleanup tool in Settings:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Storage**.
3. Select **Cleanup recommendations**.
4. Tick the items you want to remove. Windows shows how much space each will save.
5. Select the **Clean up** button in each section.""",
                 "I did that but there is still not much room left. Is there anything else?",
                 """Yes, your own big files may be taking the space:

1. Open **File Explorer** and select a folder such as **Downloads**, **Videos**, **Music**, or **Pictures**. These often hold the largest files.
2. Select **View**, then **Details**.
3. Right-click an empty spot, choose **Sort by**, then **Size**. The biggest files come first.
4. Delete the ones you do not need.
5. Empty the **Recycle Bin**, because deleted files still take up room until you do.""",
             ]},
        ],
    },
    {
        "task_id": "TR-174",
        "task_type": "battery_saver",
        "task": "Turn on battery saver (energy saver)",
        "platform": "Windows 11 laptop",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Battery saving tips (Windows 11 Energy saver)", "url": "https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99"},
        "source_notes": """Windows 11 calls it Energy saver.
Settings route: Select Start, then Settings. System, then Power & battery. Expand Energy saver. Next to "Turn energy saver on when battery level is at", choose the battery percentage. Set "Always use energy saver" to On (stays on until you next plug in the PC).
Quick setting: select the battery icon in the notification area, then select the Energy saver quick setting.
Optional lower brightness: Settings > System > Display > Brightness; if they appear, clear "Change brightness automatically when lighting changes" and "Help improve battery by optimizing the content shown and brightness"; use slider. Check boxes only on some PCs.
Troubleshooting if Energy saver still not turning on: restart the PC; then run Power troubleshooter: Settings > System > Troubleshoot > Other troubleshooters, select Run next to Power. Power mode options depend on hardware and manufacturer.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Windows 11 laptop",
             "messages": [
                 "How do I turn on battery saver on my Windows 11 laptop? The battery runs out too fast.",
                 """On Windows 11 this is called Energy saver. Here is the quickest way:

1. Select the **battery icon** in the notification area, near the clock.
2. Select the **Energy saver** quick setting.

That turns Energy saver on.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11 laptop",
             "messages": [
                 "I travel a lot and my Windows 11 laptop is never near a plug. I forget to turn the power saving thing on every time. Is there a way to make the laptop do it by itself when the battery gets low?",
                 """Yes, you can set it to turn on by itself:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Power & battery**.
3. Expand **Energy saver**.
4. Next to **Turn energy saver on when battery level is at**, choose the battery percentage you want.

Once the battery drops to that level, Energy saver turns on.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "battery saver how",
                 "I can help with that. Is it a **Windows laptop**, a **Mac laptop**, or a **phone**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Windows 11 laptop",
             "messages": [
                 "battery saver how",
                 "I can help with that. Is it a **Windows laptop**, a **Mac laptop**, or a **phone**?",
                 "windows laptop, windows 11",
                 """On Windows 11 it is called Energy saver:

1. Select the **battery icon** in the notification area, near the clock.
2. Select the **Energy saver** quick setting.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11 laptop",
             "messages": [
                 "I am on a long train ride with my Windows 11 laptop and there are no outlets. I want Energy saver on right now and I want it to stay on until I plug in again. I do not want to pick a battery percentage. What do I do?",
                 """You can turn it on now and leave it on:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Power & battery**.
3. Expand **Energy saver**.
4. Set **Always use energy saver** to **On**.

It stays on until you next plug in the laptop.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11 laptop",
             "messages": [
                 "Please show me how to turn on Energy saver on my Windows 11 laptop.",
                 """Here is the quick way:

1. Select the **battery icon** in the notification area, near the clock.
2. Select the **Energy saver** quick setting.""",
                 "I did that but Energy saver still does not turn on.",
                 """Let us try the Settings route instead:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Power & battery**.
3. Expand **Energy saver**.
4. Set **Always use energy saver** to **On**.

If that does not help, restart the laptop. Then go to **Settings**, **System**, **Troubleshoot**, **Other troubleshooters**, and next to **Power** select **Run**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-175",
        "task_type": "bluetooth_pair",
        "task": "Pair a Bluetooth device",
        "platform": "Windows 11",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Pair a Bluetooth device in Windows", "url": "https://support.microsoft.com/en-US/windows/pair-a-bluetooth-device-in-windows-2be7b51f-6ae9-b757-a3b9-95ee40c3e242"},
        "source_notes": """Turn on Bluetooth: Start > Settings > Bluetooth & devices, or select the Network, Sound, or Battery icon near the clock and select the Bluetooth quick setting tile. In Bluetooth & devices make sure the Bluetooth switch is On.
General device (keyboard, mouse, headphones, phone): 1 Make the device discoverable (depends on device, check manual or maker's site). 2 Select the Network, Sound, or Battery icon on taskbar. 3 Select the chevron next to the Bluetooth quick setting labeled "Manage Bluetooth devices". 4 Under "New devices" select your device; if you do not see it, scroll through "Your devices". 5 Follow any extra prompts, then select Done.
Printer or scanner: make discoverable; Start > Settings > Bluetooth & devices > Printers & scanners; next to "Add a printer or scanner" select Add device; wait while Windows searches (can take a few minutes); select Add device next to the printer or scanner you want.
Swift Pair: turn on compatible device and make discoverable; first time select Yes when asked to allow; when notification about new device appears, select Connect.
Troubleshooting: device not listed: set "Bluetooth devices discovery" to "Advanced". Device not supported: check PC has Bluetooth; if not, a USB Bluetooth adapter can add it.
What user sees: Bluetooth tile highlighted when on; shows Connected, Not connected, or device name. After pairing, devices reconnect automatically when Bluetooth is on and in range.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "I just got wireless headphones and want to hook them up to my Windows 11 PC through Bluetooth. Where do I start?",
                 """Here is how to pair them:

1. Make sure Bluetooth is turned on. Select the **Network**, **Sound**, or **Battery** icon near the clock and check that the **Bluetooth** tile is on.
2. Put the headphones in pairing mode so the computer can find them. The way to do this depends on the headphones, so check their manual.
3. Select the **Network**, **Sound**, or **Battery** icon on the taskbar again.
4. Select the small arrow next to the Bluetooth quick setting, labeled **Manage Bluetooth devices**.
5. Under **New devices**, select your headphones.
6. Follow any extra prompts, then select **Done**.

After this, they reconnect by themselves whenever Bluetooth is on and they are in range.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "My daughter bought me a little Bluetooth printer for my Windows 11 computer so I can stop using that long cable. It is turned on and the light is blinking. I have never done this before and I do not want to mess up my settings. How do I connect it?",
                 """Here is how to add it:

1. Make sure the printer is discoverable. Your printer's manual shows how.
2. Select **Start**, then **Settings**.
3. Select **Bluetooth & devices**, and check that the **Bluetooth** switch is **On**.
4. Select **Printers & scanners**.
5. Next to **Add a printer or scanner**, select **Add device**.
6. Wait while Windows searches. This can take a few minutes.
7. When your printer appears, select **Add device** next to it.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I need to pair my bluetooth speaker with my computer",
                 Q_OS,
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "I need to pair my bluetooth speaker with my computer",
                 Q_OS,
                 "its a windows 11 pc",
                 """Here is how to pair the speaker:

1. Make sure Bluetooth is turned on. Select the **Network**, **Sound**, or **Battery** icon near the clock and check that the **Bluetooth** tile is on.
2. Put the speaker in pairing mode. Check its manual for how.
3. Select the **Network**, **Sound**, or **Battery** icon on the taskbar again.
4. Select the small arrow next to the Bluetooth quick setting, labeled **Manage Bluetooth devices**.
5. Under **New devices**, select your speaker.
6. Follow any extra prompts, then select **Done**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "I would like to connect my Bluetooth mouse to my Windows 11 laptop but I do not want to go digging through the Settings app, it confuses me. Is there a quicker way from the bottom of the screen?",
                 """Yes, you can do it from the taskbar:

1. Select the **Network**, **Sound**, or **Battery** icon on the taskbar, near the clock, and make sure the **Bluetooth** tile is on.
2. Put the mouse in pairing mode. Check its manual for how.
3. Select the **Network**, **Sound**, or **Battery** icon again.
4. Select the small arrow next to the Bluetooth quick setting, labeled **Manage Bluetooth devices**.
5. Under **New devices**, select your mouse. If you do not see it, look through **Your devices**.
6. Follow any extra prompts, then select **Done**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "Show me how to pair my Bluetooth keyboard with my Windows 11 computer.",
                 """Here is how to pair it:

1. Put the keyboard in pairing mode. Check its manual for how.
2. Select the **Network**, **Sound**, or **Battery** icon on the taskbar.
3. Select the small arrow next to the Bluetooth quick setting, labeled **Manage Bluetooth devices**.
4. Under **New devices**, select your keyboard.
5. Follow any extra prompts, then select **Done**.""",
                 "My keyboard is not showing up in that list.",
                 """Try these:

1. Put the keyboard in pairing mode again, using its manual.
2. Look through **Your devices** in the same list, as well as **New devices**.
3. Check that Bluetooth is on. Select **Start**, then **Settings**, then **Bluetooth & devices**, and make sure the **Bluetooth** switch is **On**.
4. Select **Devices**. Under **Device settings**, set **Bluetooth devices discovery** to **Advanced**.

If it still does not show, make sure your computer has Bluetooth. If it does not, a USB Bluetooth adapter can add it.""",
             ]},
        ],
    },
    {
        "task_id": "TR-176",
        "task_type": "app_notifications_off",
        "task": "Turn off notifications from an app",
        "platform": "Windows 11",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Notifications and Do Not Disturb in Windows", "url": "https://support.microsoft.com/en-us/windows/notifications-and-do-not-disturb-in-windows-feeca47f-0baf-5680-16f0-8801db1a8466"},
        "source_notes": """Windows 11: Start > Settings > System > Notifications. Under "Notifications from apps and other senders", select the app. Switch off "Turn notifications on or off" to stop alerts from that app. To keep some alerts, instead turn off "Show notification banners", "Show notifications in notification center", or "Play a sound". Alternative: in the notification center select the more button on a notification and choose "Turn off all notifications". Page has no troubleshooting and does not describe what the screen shows afterward.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "How do I stop one app from sending me notifications on Windows 11?",
                 """You can turn off alerts for one app in Settings:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Notifications**.
3. Under **Notifications from apps and other senders**, select the app you want to quiet.
4. Switch off **Turn notifications on or off**.

That stops alerts from that app.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "Every few minutes a little box pops up in the corner of my Windows 11 screen from the Solitaire game telling me to come back and play. It drives me crazy when I am writing emails. I do not want to uninstall it, I just want it to leave me alone.",
                 """You can silence it without removing the game:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Notifications**.
3. Under **Notifications from apps and other senders**, select the game.
4. Switch off **Turn notifications on or off**.

The game stays installed, and it stops sending you alerts.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "these popups from one program on my computer keep bothering me, can they be turned off",
                 Q_OS,
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "these popups from one program on my computer keep bothering me, can they be turned off",
                 Q_OS,
                 "Windows 11 PC",
                 """Yes. Here is how to turn off alerts for that program:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Notifications**.
3. Under **Notifications from apps and other senders**, select the program that bothers you.
4. Switch off **Turn notifications on or off**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "On my Windows 11 computer my Mail app makes a loud ding for every message. I still want to see the messages, I just do not want the sound. How do I turn off only the sound?",
                 """You can keep the alerts and turn off just the sound:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Notifications**.
3. Under **Notifications from apps and other senders**, select **Mail**.
4. Switch off **Play a sound**.

Leave **Turn notifications on or off** switched on, so the messages still show up.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "Please help me make my Mail app stop sending me notifications on Windows 11.",
                 """Here is how to turn them off:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Notifications**.
3. Under **Notifications from apps and other senders**, select **Mail**.
4. Switch off **Turn notifications on or off**.""",
                 "Now I am worried I will miss important emails. I only wanted the pop-up boxes and the sound gone.",
                 """You can turn the alerts back on and then quiet only those parts:

1. Go back to **Settings**, **System**, **Notifications**, and select **Mail**.
2. Switch **Turn notifications on or off** back on.
3. Switch off **Show notification banners**. This stops the pop-up boxes.
4. Switch off **Play a sound**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-177",
        "task_type": "magnifier",
        "task": "Use Magnifier to make things on screen bigger (keyboard shortcuts)",
        "platform": "Windows 11",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: How to quickly change the zoom level for Magnifier (and Keyboard shortcuts for Magnifier)", "url": "https://support.microsoft.com/en-US/accessibility/windows/magnifier/how-to-quickly-change-the-zoom-level-for-magnifier"},
        "source_notes": """Turn on Magnifier: Windows key + Plus sign (+). Zoom in: Windows key + Plus sign (+) again. Zoom out: Windows key + Minus sign (-). Zoom with mouse: Ctrl + Alt + mouse wheel (direction not stated). Turn off Magnifier: Windows key + Esc. "The greater the Magnifier zoom level, the larger something appears on your screen."
Keyboard shortcuts page (support.microsoft.com/en-us/accessibility/windows/magnifier/keyboard-shortcuts-for-magnifier): Full screen view Ctrl+Alt+F; Lens view Ctrl+Alt+L; Docked view Ctrl+Alt+D; cycle views Ctrl+Alt+M; Invert colors Ctrl+Alt+I; Open Magnifier settings Windows key+Ctrl+M.
Neither page has troubleshooting or on-screen toolbar steps.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "The words on my Windows 11 computer are too small to read. Can I make them bigger with Magnifier?",
                 """Yes. Use the keyboard:

1. Press the **Windows key + Plus sign (+)**. This turns Magnifier on.
2. Press **Windows key + Plus sign (+)** again to zoom in more. Each press makes things on the screen larger.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "My eyes are not what they used to be and I am trying to read a recipe online on my Windows 11 computer. I would like to make the screen bigger for a bit and then get it back to normal after, because it is hard to do my other things when everything is huge. How do I do all of that?",
                 """You can do all of it with the keyboard:

1. Press the **Windows key + Plus sign (+)** to turn Magnifier on.
2. Press **Windows key + Plus sign (+)** again to make things larger.
3. If it gets too big, press the **Windows key + Minus sign (-)** to make things smaller.
4. When you are done reading, press the **Windows key + Esc** to turn Magnifier off.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "how do i make everything on the screen bigger so i can see it",
                 Q_OS,
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "how do i make everything on the screen bigger so i can see it",
                 Q_OS,
                 "windows 11",
                 """On Windows 11 you can use Magnifier:

1. Press the **Windows key + Plus sign (+)** to turn Magnifier on.
2. Press **Windows key + Plus sign (+)** again to zoom in more.
3. To make things smaller again, press the **Windows key + Minus sign (-)**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "I use Magnifier on my Windows 11 PC, but I do not want the whole screen to get big, I only want a part of it magnified like a lens. Is that possible, and how do I switch to it?",
                 """Yes, Magnifier has a Lens view:

1. If Magnifier is not on yet, press the **Windows key + Plus sign (+)**.
2. Press **Ctrl + Alt + L**. This switches to Lens view.

To go back to the whole screen, press **Ctrl + Alt + F**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "How do I turn on Magnifier on my Windows 11 computer?",
                 """Use the keyboard:

1. Press the **Windows key + Plus sign (+)**. This turns Magnifier on.
2. Press **Windows key + Plus sign (+)** again to zoom in more.""",
                 "Now everything is way too big and I cannot read anything. Help!",
                 """Do not worry. You can fix it two ways:

1. To make things a bit smaller, press the **Windows key + Minus sign (-)**. Press it again if it is still too big.
2. To turn Magnifier off completely, press the **Windows key + Esc**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-178",
        "task_type": "live_captions",
        "task": "Turn on live captions",
        "platform": "Windows 11",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Use live captions to better understand audio", "url": "https://support.microsoft.com/windows/use-live-captions-to-better-understand-audio-b52da59c-14b8-4031-aeeb-f6a47e6055df"},
        "source_notes": """Turn on (any one method): 1 Select battery, network, or volume icon on taskbar to open quick settings, then turn on Live captions. 2 In quick settings Accessibility flyout, turn on Live captions toggle. 3 Press Windows key + Ctrl + L. 4 Start > All apps > Accessibility > Live captions. 5 Settings > Accessibility > Captions, turn on Live captions toggle.
First time: asks for consent to process voice data on your device; prompts to download language files for on-device speech recognition; if your language is not available, can choose another during setup.
Position: Settings button in live captions window > Position > Above screen, Below screen, or Overlaid on screen.
Include microphone: Settings button > Preferences > Include microphone audio (off by default each start).
Captions only appear for audio sent to default output device (Settings > System > Sound). Troubleshooting: headset audio not captioned: check default sound output device in Settings > System > Sound. Delayed or missing captions: close unused apps. Article does not give separate turn-off steps.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "Is there a way to see words on screen for videos I watch on my Windows 11 computer? I have trouble hearing.",
                 """Yes, Windows 11 has live captions. The quickest way is the keyboard:

1. Press **Windows key + Ctrl + L**.
2. The first time, Windows asks for your consent to process voice on your device. Follow the prompts.
3. If asked, let it download the language files it needs.

Captions then appear for speech in what your computer plays.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "My husband and I watch our church service online on our Windows 11 computer and he cannot make out what the pastor says. I do not like using key combinations because I always press the wrong ones. Can you walk me through turning on captions using the Settings app?",
                 """Yes, here is the way through Settings:

1. Select **Start**, then **Settings**.
2. Select **Accessibility**, then **Captions**.
3. Turn on the **Live captions** toggle.
4. The first time, follow the prompts. Windows asks for your consent to process voice on your device and may download language files.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "can i get subtitles to show up for everything that plays on my computer",
                 Q_OS,
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "can i get subtitles to show up for everything that plays on my computer",
                 Q_OS,
                 "windows 11",
                 """Yes, Windows 11 has live captions:

1. Press **Windows key + Ctrl + L**.
2. The first time, follow the prompts. Windows asks for your consent to process voice on your device and may download language files.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "I want live captions on my Windows 11 PC, but I can only use the mouse right now, my keyboard is not working. Can I turn them on from the taskbar?",
                 """Yes, you can do it with the mouse only:

1. Select the **battery**, **network**, or **volume** icon on the taskbar, near the clock. This opens quick settings.
2. Turn on **Live captions**.

The first time, follow the prompts. Windows asks for your consent to process voice on your device and may download language files.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "How do I turn on live captions in Windows 11?",
                 """Use the keyboard:

1. Press **Windows key + Ctrl + L**.
2. The first time, follow the prompts. Windows asks for your consent to process voice on your device and may download language files.""",
                 "The captions window opened but nothing shows up when I play a video with my headset on.",
                 """Captions only show sound that goes to your default sound output. Let us check it:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Sound**.
3. Check which output device is chosen as your default. If it is not the headset you are using, change the default output device to your headset.
4. Play the video again and check that captions show.""",
             ]},
        ],
    },
    {
        "task_id": "TR-179",
        "task_type": "brightness",
        "task": "Make the screen brighter or dimmer",
        "platform": "Windows 11",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Change display brightness and color in Windows", "url": "https://support.microsoft.com/en-us/help/4026946"},
        "source_notes": """Quick settings: select the Network icon on the right side of the taskbar; move the Brightness slider.
Settings: Start > Settings > System > Display; use the Brightness slider.
Automatic based on lighting: Start > Settings > System > Display, select Brightness, turn on the toggle for brightness automatically when lighting changes (label seen on another Microsoft page: "Change brightness automatically when lighting changes"). Works only on some PCs. You can still fine-tune with the slider.
Desktop PCs with an external monitor: might not see the Brightness slider; use the buttons on the external monitor.
Page does not describe brightness keyboard keys.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "The screen on my Windows 11 laptop is too bright. How do I make it dimmer?",
                 """You can change it from the taskbar:

1. Select the **Network** icon on the right side of the taskbar.
2. Move the **Brightness** slider to the left to dim the screen, or to the right to make it brighter.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "I read a lot in the evenings on my Windows 11 laptop and the screen hurts my eyes. My son once showed me a slider but I forget where it was. Could you tell me how to find it in Settings so I can write it down?",
                 """Here is the way through Settings:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Display**.
3. Use the **Brightness** slider. Move it left to make the screen dimmer.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my screen is too dark how do i fix it",
                 Q_OS,
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "my screen is too dark how do i fix it",
                 Q_OS,
                 "its windows 11",
                 """You can make it brighter from the taskbar:

1. Select the **Network** icon on the right side of the taskbar.
2. Move the **Brightness** slider to the right.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "My Windows 11 laptop is by a window and the light in the room changes all day. I am tired of moving the brightness by hand. Can the laptop change it by itself when the room gets lighter or darker?",
                 """It can on some PCs. Here is how to try:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Display**.
3. Select **Brightness**.
4. Turn on the toggle that changes brightness automatically when lighting changes.

This works only on some PCs. You can still fine-tune the level with the **Brightness** slider.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Windows 11",
             "messages": [
                 "How do I change the brightness on my Windows 11 computer?",
                 """You can use the taskbar:

1. Select the **Network** icon on the right side of the taskbar.
2. Move the **Brightness** slider to the level you like.""",
                 "I do not see any Brightness slider there. I have a desktop with a separate monitor.",
                 """That is normal for a desktop with a separate monitor, because the slider may not appear. Use the buttons on the monitor itself to change its brightness.""",
             ]},
        ],
    },
]
