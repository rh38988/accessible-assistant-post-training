TASKS = [
    {
        "task_id": 'TR-062', "task_type": 'free_storage', "task": 'Free up storage space',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Free up storage on your Android device', "url": 'https://support.google.com/android/answer/7431795?hl=en'},
        "source_notes": """Find usage: Settings > Storage > select a category.
Automatic: Settings > Storage > Free up space > Menu icon > Settings > turn on Smart Storage (clears backed-up photos and videos when storage is almost full).
Manual (photos, videos, apps not used recently): Settings > Storage > Free up space; scroll to the category; tap Select files (if the category isn't listed, tap Browse); select files to delete (can select all); tap Move files to Trash.
Google Photos: if you back up with Google Photos, delete the copies on the device; backed-up copies appear in the app when online.
Other: uninstall unused apps (reinstall later, paid apps not bought again); clear cache/data (menu names vary by phone). Some steps only work on Android 14 and up. Settings vary by phone.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My phone keeps saying storage is almost full. All my pictures are already backed up in Google Photos, and I would rather not dig through folders by hand every few weeks. Can the phone clear things out on its own?",
                 """Yes, Android has a setting for that. It clears photos and videos that are already backed up when your storage is almost full.

1. Open the **Settings** app.
2. Tap **Storage**, then tap **Free up space**.
3. Tap the **Menu** icon, then tap **Settings**.
4. Turn on **Smart Storage**.

Your backed-up pictures still show in the **Google Photos** app when you are online. Some of these steps need Android 14 or newer, and menu names can differ a little between phones.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "Android phone, it's nearly full. I want to delete the big stuff I don't need. Where do I go?",
                 """Here is how to find files to delete.

1. Open the **Settings** app.
2. Tap **Storage**, then tap **Free up space**.
3. Scroll to the category you want.
4. Tap **Select files**.
5. Select the files you don't need.
6. Tap **Move files to Trash**.""",
                 "I got to Free up space and found the category but there is no Select files button.",
                 """Your phone may show it a little differently. Try this instead:

1. Look for **Browse** and tap it.
2. Select the files you want to delete. You can also select all of them.
3. Tap **Move files to Trash**.

Menu names can differ a little between phones, and some steps need Android 14 or newer.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-063', "task_type": 'flashlight', "task": 'Turn on the flashlight',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro', "url": 'https://support.apple.com/en-us/105001'},
        "source_notes": """Siri: say "Hey Siri, turn on my flashlight." / "Hey Siri, turn off my flashlight."
Control Center: open Control Center, tap the Flashlight button; tap again to turn off. Open Control Center: swipe down from upper-right corner on iPhone with Face ID; swipe up from the bottom edge on iPhone with a Home button.
Lock Screen: press and hold the Flashlight button in the bottom-left corner.
Action button (iPhone 15 Pro and later Pro models): Settings > Action Button, swipe to the Flashlight icon, press and hold the Action button to toggle.
Brightness: press and hold Flashlight button in Control Center, drag slider.
Troubleshooting: if Flashlight button is missing from Control Center, go to Settings > Control Center and add it; or tap and hold the screen while Control Center is open to customize controls.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I'm in my dark garage carrying two bags of groceries and my iPhone is in my pocket. I can't use my hands at all right now. Is there any way to get the light on without touching it?",
                 """Yes, you can ask Siri without touching the phone.

1. Say **"Hey Siri, turn on my flashlight."**
2. When you are done, say **"Hey Siri, turn off my flashlight."**""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "iPhone SE here, the one with the round button at the bottom. How can I turn on the light on the back?",
                 """Here is the quickest way.

1. **Swipe up from the bottom edge** of the screen to open Control Center.
2. Tap the **Flashlight** button.
3. Tap it again to turn it off.""",
                 "I swiped up and the controls came up but I don't see a flashlight button anywhere.",
                 """It may just need to be added to Control Center.

1. Open **Settings**.
2. Tap **Control Center**.
3. In the list of controls, tap **Flashlight**.
4. Swipe up from the bottom again and tap the **Flashlight** button.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-064', "task_type": 'flashlight', "task": 'Turn on the flashlight',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Change settings quickly on your Android phone', "url": 'https://support.google.com/android/answer/9083864?hl=en'},
        "source_notes": """Open Quick Settings: swipe down from the top once to see the first few settings; swipe down again to see all.
Tap a setting's icon to turn it on or off. Dimmed settings are off.
Edit: swipe down twice, tap Edit, scroll down to see all available settings, tap Add on the one you want. To remove, tap Remove.
Move: tap and drag a setting to reposition it. Drag right side of icon left to show icon only; right to show the name.
The page does not name a Flashlight tile; you can check by opening Edit and scrolling. Some steps need Android 13 and up. If icons seem missing, the phone may hide them to save space; look for a dot at the top of the screen.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I use the flashlight button every night to get to the bathroom. I do have it, but I have to swipe down twice to find it and my hands are stiff. Can I move it so one swipe is enough?",
                 """Yes. The first swipe shows only the first few settings, so you can drag the flashlight up into that group.

1. **Swipe down** twice from the top of the screen.
2. Tap **Edit**.
3. Tap and **drag** the **Flashlight** button to the front of the list, among the first few.

After that, one swipe down should show it. Tap it to turn the light on, and tap it again to turn it off.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "Pixel phone. Where do I tap to turn on the torch?",
                 """Here is the quickest way.

1. **Swipe down** from the top of the screen to see a few quick settings. Swipe down again to see all of them.
2. Tap **Flashlight** to turn it on. A dimmed icon means it is off.
3. Tap it again to turn it off.""",
                 "I swiped down twice and there are lots of buttons but I don't see Flashlight.",
                 """Let's check the list of buttons you can add.

1. With the buttons showing, tap **Edit**.
2. Scroll down to see all the settings you can add.
3. If you find **Flashlight**, tap **Add**.

If it is not in that list, tell me what you see there.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-066', "task_type": 'alarm', "task": 'Set an alarm',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: How to set and change alarms on your iPhone', "url": 'https://support.apple.com/en-us/118444'},
        "source_notes": """Set: open Clock app, tap the Alarms tab, tap the Add button, set a time (optionally Repeat, Label, Sound, Snooze), tap Done.
Volume: Settings > Sounds & Haptics > under Ringtone and Alerts drag the slider; optionally turn on Change with Buttons.
Edit: Clock > Alarms > Edit (upper-left) > tap the alarm, change, tap Save.
Delete: swipe left over the alarm and tap Delete; or Edit, then the Delete button, then Delete.
Conditions: Do Not Disturb, the Ring/Silent switch, and Silent mode do not silence alarms.
Troubleshooting: if the alarm only vibrates, Clock > Alarms > Edit > tap the alarm > tap Sound > choose a sound instead of None. If headphones are connected, the alarm also plays through the iPhone's built-in speakers. With StandBy, alarm haptics are disabled, so set a sound rather than None.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone stays on silent all day and I turn on Do Not Disturb at night. I have a flight at 8 so I need to be up at 5:45 AM. Will an alarm still wake me if the phone is silent like that?",
                 """Yes. Silent mode and Do Not Disturb do not silence alarms, so you can leave both on.

1. Open the **Clock** app.
2. Tap the **Alarms** tab.
3. Tap the **Add** button.
4. Set the time to **5:45 AM**.
5. Tap **Done**.

The alarm's loudness follows the **Ringtone and Alerts** slider. To check it, open **Settings**, tap **Sounds & Haptics**, and drag the slider toward the louder end.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "Need my iPhone to wake me at 7:15 tomorrow, please walk me through it.",
                 """Here is how to set it.

1. Open the **Clock** app.
2. Tap the **Alarms** tab.
3. Tap the **Add** button.
4. Set the time to **7:15 AM**.
5. Tap **Done**.""",
                 "It went off this morning but it only buzzed. No sound at all.",
                 """The alarm's sound is probably set to **None**. Let's pick a sound.

1. Open **Clock** and tap **Alarms**.
2. Tap **Edit** in the upper-left corner, then tap your alarm.
3. Tap **Sound** and choose a sound instead of **None**.
4. Tap **Save**.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-067', "task_type": 'alarm', "task": 'Set an alarm',
        "platform": 'Android (Clock)', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Set, cancel, or snooze alarms on your Android device', "url": 'https://support.google.com/android/answer/2840926?hl=en'},
        "source_notes": """Set: open Clock app, tap Alarm, tap Add (or tap the current time of an existing alarm), set hour and minutes on the analog or digital clock, in 12-hour format choose AM or PM, tap OK.
Edit: open Clock, tap Alarm, tap the alarm block; tap "Alarm name" to name it, tap the days of the week to repeat it, or tap "Vibrate".
Delete: Clock > Alarm > tap the alarm block > tap Delete.
Turn off: Clock > Alarm > tap the On/Off switch on the alarm.
Snooze: tap Snooze to delay 10 minutes; tap Stop to stop it.
Conditions: alarms set within 5 minutes of each other may cancel one another, leave a 5-minute gap. If volume was below 30% it may be too quiet. Messages appear when an alarm may not work (Do Not Disturb silenced, Battery Saver, silent sound, vibration off, Clock notifications off).""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android (Clock)",
             "messages": [
                 "I work Monday to Friday and sleep in on weekends. I want an alarm on my Android phone for 7:00 in the morning, but it must not go off on Saturday or Sunday.",
                 """You can set the alarm and then choose which days it repeats.

1. Open the **Clock** app.
2. Tap **Alarm**.
3. Tap **Add**.
4. Set the time to **7:00** and choose **AM**.
5. Tap **OK**.
6. Tap the alarm you just made.
7. Tap the days of the week you want it to repeat, **Monday through Friday**.

Leave Saturday and Sunday untapped so it stays quiet on weekends.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android (Clock)",
             "messages": [
                 "Android here. Could you show me how to put an alarm on for 7 in the morning?",
                 """Here is how, in the **Clock** app.

1. Open the **Clock** app.
2. Tap **Alarm**.
3. Tap **Add**.
4. Set the time to **7:00** and choose **AM**.
5. Tap **OK**.""",
                 "Thanks. I added a second one at 7:03 as a backup, but this morning only one of them rang.",
                 """Alarms set within 5 minutes of each other can cancel one another. Move the backup so they are at least 5 minutes apart.

1. Open **Clock** and tap **Alarm**.
2. Tap the time of the second alarm.
3. Set it to **7:05** or later, then tap **OK**.

Or tap the second alarm and tap **Delete** to remove it.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-068', "task_type": 'hearing_bluetooth', "task": 'Pair hearing aids or Bluetooth headphones',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Use Made for iPhone hearing devices', "url": 'https://support.apple.com/en-us/108780'},
        "source_notes": """Confirm the hearing device is an MFi device and compatible. Update iOS before pairing.
Pairing mode (see device guide): battery door models: open the battery door on each device, close it when ready to pair. On/off switch: turn off then on. Rechargeable with no switch: remove the device from its charger.
iPhone: Settings > Accessibility > Hearing Devices > Pair MFi Hearing Device, follow onscreen instructions, select hearing device, tap Pair. If Pair MFi Hearing Device doesn't appear, tap the hearing device's name in Hearing Devices settings, then tap Pair when Bluetooth pairing requests appear.
Pairing a new hearing device replaces any previously paired one.
Controls: Settings > Accessibility > Hearing Devices, tap device name. Unpair: tap name, tap Forget this device.
Troubleshooting not appearing: confirm compatibility and pairing mode; restart the Apple device; if paired with another Apple device, unpair it there first; update device firmware with the manufacturer app. Dimmed: keep near, unpair and pair again. Disconnects: keep nearby, check battery, wireless interference. No audio: select hearing device as sound output, check microphone level.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My new hearing aids are the rechargeable kind. There is no battery door and no on and off switch, they just sit in a little charging case. I have an iPhone and want to connect them. How do I get them into pairing mode?",
                 """For hearing aids with no switch, pairing mode means taking them out of the charger.

1. Make sure your iPhone has the latest software update.
2. Take both hearing aids **out of the charger**. Keep them close to your iPhone.
3. On your iPhone, open **Settings**.
4. Tap **Accessibility**, then tap **Hearing Devices**.
5. Tap **Pair MFi Hearing Device** and follow the instructions on the screen.
6. Select your hearing aids, then tap **Pair**.

If you don't see **Pair MFi Hearing Device**, tap your hearing aids' name in **Hearing Devices**, then tap **Pair** when the Bluetooth requests appear.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My daughter got me hearing aids that work with iPhone. Where do I go on my iPhone to connect them?",
                 """Here is how to pair them.

1. Put your hearing aids in **pairing mode**. Your hearing aid instructions say how. It might mean opening and closing the battery doors, turning them off and on, or taking them out of the charger.
2. Open **Settings** on your iPhone.
3. Tap **Accessibility**, then tap **Hearing Devices**.
4. Tap **Pair MFi Hearing Device**.
5. Select your hearing aids, then tap **Pair**.""",
                 "I did all that and my hearing aids never show up on the screen.",
                 """Let's try a few things.

1. Put the hearing aids back in pairing mode.
2. Restart your iPhone.
3. If they were paired with another Apple device, like an iPad, unpair them there first.
4. Try **Settings**, **Accessibility**, **Hearing Devices** again.

Also check that your hearing aids are the kind made to work with iPhone.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-069', "task_type": 'hearing_bluetooth', "task": 'Pair Bluetooth headphones',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Find & set up Bluetooth devices near your Android device', "url": 'https://support.google.com/android/answer/9417604?hl=en'},
        "source_notes": """Turn Bluetooth on/off: pull down from top of screen, tap Bluetooth.
Pair: pull down from the top, touch and hold Bluetooth, tap Pair new device (if missing, check under Available devices, or tap More then Refresh), tap the name of the Bluetooth device, follow on-screen instructions; if asked for a passcode try 0000 or 1234.
Fast Pair: if you see a pairing notification, it connects automatically.
Reconnect already paired: make sure Bluetooth is on, touch and hold Bluetooth, under Saved devices select a paired, disconnected device, wait until it shows Connected.
Rename/disconnect/unpair: touch and hold Bluetooth, find device (under Media devices tap its Settings icon; if nothing under Saved devices tap See all, then Settings icon), Edit to rename, Disconnect, or Forget to unpair.
Some steps need Android 15 and up. No troubleshooting beyond the link.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My headphones connected to my Android phone fine last month, then I used them with my tablet and now they won't play on the phone. I don't want to go through the whole setup again, I just want to reconnect the ones my phone already knows.",
                 """You can reconnect them from your saved devices, with no new pairing.

1. **Pull down** from the top of the screen and make sure **Bluetooth** is on.
2. **Touch and hold** **Bluetooth**.
3. Under **Saved devices**, tap your headphones.
4. Wait until they show **Connected**.

Make sure the headphones are turned on and close to the phone.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I bought wireless earbuds for my walks. My phone is an Android. How do I get them connected?",
                 """Here is how to pair them.

1. Put the earbuds in **pairing mode**. Check the instructions that came with them.
2. **Pull down** from the top of the screen.
3. **Touch and hold** **Bluetooth**.
4. Tap **Pair new device**.
5. Tap the name of your earbuds.
6. Follow any instructions on the screen.""",
                 "I touched and held Bluetooth but I don't see Pair new device anywhere.",
                 """Try these:

1. Look under **Available devices** for your earbuds.
2. If they are not there, tap **More**, then tap **Refresh**.
3. Tap the name of your earbuds when it appears.

If you are asked for a passcode, try **0000** or **1234**.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-070', "task_type": 'battery_saver', "task": 'Turn on battery saving mode',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Use Low Power Mode to save battery life on your iPhone or iPad', "url": 'https://support.apple.com/en-us/101604'},
        "source_notes": """iPhone 15 and later: Settings > Battery > Power Mode > tap to turn Low Power Mode on or off. iPhone 14 and earlier: Settings > Battery > tap to turn Low Power Mode on or off.
Other ways: Control Center (swipe down from top-right corner, tap battery icon); Siri: say "Siri, turn on Low Power Mode" or "Hey Siri, turn off Low Power Mode". Adaptive Power, if supported and on, turns Low Power Mode on below 20%.
What you see: battery icon in status bar turns yellow.
Reduces: background app refresh and automatic downloads, email fetch, iCloud Photos sync paused, display brightness and some visual effects, Auto-Lock set to 30 seconds.
Turns off automatically when charged to 80% or higher.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My hands are covered in dough and my iPhone is on the counter, at 15 percent. I don't want to touch it or go through menus. Can I turn on the battery saving thing by talking to it?",
                 """Yes, Siri can do it.

1. Say **"Siri, turn on Low Power Mode."**
2. Look at the battery icon at the top of the screen once you can. When it turns **yellow**, Low Power Mode is on.

To turn it off later, say **"Hey Siri, turn off Low Power Mode."** It also turns off by itself once the battery charges to 80% or higher.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "iPhone 15. Walk me through turning on Low Power Mode please.",
                 """Here is how.

1. Open **Settings**.
2. Tap **Battery**.
3. Tap **Power Mode**.
4. Tap to turn **Low Power Mode** on.

The battery icon at the top of the screen turns yellow when it is on.""",
                 "It worked, but after I charged my phone the yellow battery went away and it seems to be off.",
                 """That is normal. Low Power Mode turns itself off once the battery charges to 80% or higher. To turn it back on:

1. Open **Settings** and tap **Battery**.
2. Tap **Power Mode**.
3. Tap to turn **Low Power Mode** on.

You will see the battery icon turn yellow again.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-071', "task_type": 'battery_saver', "task": 'Turn on battery saving mode',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": "Android Help: Get the most life from your Android device's battery", "url": 'https://support.google.com/android/answer/7664692?hl=en'},
        "source_notes": """Turn on: Settings app > Battery > Battery Saver. Schedule: choose a schedule for Battery Saver, or set it to turn off automatically.
What changes: Battery Saver turns on Dark theme; limits or turns off background activity, so some visual effects, features, network connections, and apps may be slower.
Some Android phones include a battery saver or low power mode; check your device manufacturer's support site.
Fix battery problems that won't go away: restart (hold power button about 30 seconds, tap Restart if it appears); check for Android updates (Settings > System > Software update); check app updates (Play Store, profile icon, Manage apps & devices, update apps under Updates available); factory reset last resort (erases all data, back up first); contact carrier or manufacturer if problem continues.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I don't want my Android phone stuck in battery saving mode all day because it slows everything down. I only need it in the evenings when I'm out. Can it switch on and off by itself on a timetable?",
                 """Yes, Battery Saver lets you choose a schedule, or have it turn off automatically.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver**.
4. Look for the option to set a schedule or to turn it off automatically, and choose what fits you.

The choices can look a little different on some phones.

While it is on, it switches the screen to a dark theme and limits background activity, so some apps may be a little slower.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "Android phone and the battery never lasts. Is there a power saving mode I can switch on?",
                 """Yes. Here is how to turn on Battery Saver.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver** and turn it on.

It limits background activity and turns on a dark theme.""",
                 "I did that days ago and the battery still drains really fast.",
                 """Let's try the usual fixes for battery trouble.

1. **Restart** the phone. Hold the power button for about 30 seconds, then tap **Restart** if it appears.
2. Check for an Android update: **Settings**, then **System**, then **Software update**.
3. Open the **Play Store**, tap your **profile icon**, tap **Manage apps & devices**, and update apps under **Updates available**.

If it still drains fast, your phone maker or carrier can help.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-072', "task_type": 'software_update', "task": 'Update apps',
        "platform": 'iPhone (App Store)', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: How to manually update apps from the App Store', "url": 'https://support.apple.com/en-us/102629'},
        "source_notes": """iPhone manual update: open App Store, tap your profile photo or the My Account button at the top of the screen, tap App Updates, tap Update beside an app or Update All.
Automatic updates on iPhone: Settings > Apps > App Store > turn App Updates on or off.
No troubleshooting section on the page (links to pages for apps that won't update).""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone (App Store)",
             "messages": [
                 "Last week my iPhone changed how my banking app looks on its own and I got lost. I don't want apps changing behind my back anymore. How do I stop them updating by themselves? I will update them when I'm ready.",
                 """You can turn off automatic updates.

1. Open **Settings**.
2. Tap **Apps**.
3. Tap **App Store**.
4. Turn off **App Updates**.

When you do want to update, open the **App Store**, tap your **profile photo** at the top of the screen, tap **App Updates**, then tap **Update** next to the app you want, or **Update All**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone (App Store)",
             "messages": [
                 "My iPhone apps are out of date. Could you take me through updating them?",
                 """Here is how to update them.

1. Open the **App Store**.
2. Tap your **profile photo** at the top of the screen.
3. Tap **App Updates**.
4. Tap **Update** next to an app, or tap **Update All**.""",
                 "I opened the App Store but I don't have a profile photo up top, just a plain icon.",
                 """At the top of the screen the button can also be called **My Account**.

1. Tap the **My Account** button.
2. Tap **App Updates**.
3. Tap **Update** next to an app, or tap **Update All**.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-073', "task_type": 'magnifier', "task": 'Zoom in on the screen',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Accessibility Help: Use magnification on your screen', "url": 'https://support.google.com/accessibility/android/answer/6006949?hl=en'},
        "source_notes": """Setup: Settings > Accessibility > Magnification > turn on Magnification shortcut. Optional: tap Magnification shortcut to choose Accessibility button, Hold volume keys, or Triple-tap screen. Use the shortcut again to stop.
Triple-tap: quickly tap the screen 3 times and hold. May slow the device; single taps take slightly longer once magnification is on.
Full screen: tap the Accessibility button, then tap anywhere except keyboard or navigation bar; use two fingers to move and pinch to zoom.
Partial screen: tap the Accessibility button; drag 2 fingers to move the magnification window and pinch to adjust zoom.
Switch modes: Settings > Accessibility > Magnification > Magnification type, choose full or partial screen.
Temporary zoom: tap Accessibility button, touch and hold anywhere except keyboard/navigation bar, drag finger to move around, lift to stop.
Some steps need Android 13 or later; Magnifier Settings panel needs Android 14 or later.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I only need a little magnifying glass over the small print, not the whole screen blown up, because then I lose my place. Can my Android phone zoom just a section of the screen?",
                 """Yes, Android has a partial screen mode that zooms a small window.

1. Open **Settings**.
2. Tap **Accessibility**, then tap **Magnification**.
3. Tap **Magnification type** and choose **partial screen**.
4. Turn on **Magnification shortcut**.
5. Tap **Magnification shortcut** and choose **Accessibility button**.
6. Tap the **Accessibility** icon at the bottom of the screen. Its exact spot depends on how your phone is set up.
7. **Drag with two fingers** to move the zoom window, and **pinch** to change how much it zooms.

Some of these steps need Android 13 or later.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "Android phone. I want to zoom in to read small print and I like the idea of triple tapping the screen. How do I set that up?",
                 """Here is how to set it up.

1. Open **Settings**.
2. Tap **Accessibility**, then tap **Magnification**.
3. Turn on **Magnification shortcut**.
4. Tap **Magnification shortcut** and choose **Triple-tap screen**.

To zoom, quickly tap the screen 3 times and hold. Use two fingers to pinch and to move around. Use the shortcut again to stop.""",
                 "It zooms, but now my phone feels slow and my taps are delayed.",
                 """The triple-tap shortcut can slow your phone, and single taps take slightly longer while zoom is on. Switch to a different shortcut:

1. Open **Settings**, then **Accessibility**, then **Magnification**.
2. Tap **Magnification shortcut**.
3. Choose **Accessibility button** or **Hold volume keys**.

With **Accessibility button**, tap the Accessibility icon at the bottom of the screen. With **Hold volume keys**, hold both volume buttons together.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-074', "task_type": 'find_lost_phone', "task": 'Find a lost phone',
        "platform": 'iPhone (Find My)', "category": 'technical_support', "sensitive": True,
        "source": {"title": 'Apple Support: How to find your lost iPhone or iPad', "url": 'https://support.apple.com/en-us/101593'},
        "source_notes": """Find My app on another trusted Apple device signed in with your Apple Account: Devices tab, select the iPhone, tap the More button, scroll to Lost [Device] and turn on Lost Mode, optionally follow prompts to show contact info, tap Activate.
iCloud.com: sign in at icloud.com/find (no verification code needed; if one is requested, select the Find Devices button). Open the device list under All Devices and choose the device. From there you can play a sound, mark it as lost, or erase it.
Family Sharing: the device can appear in Find My on a family member's device.
Lost Mode: device locked with passcode, Apple Pay cards and passes suspended, can show a phone number and message.
Conditions: Find My must have been turned on before the device was lost. Device shows as online and in Lost Mode only when on and connected to Wi-Fi or cellular. If offline, it won't show as online or in Lost Mode until it reconnects; a remote erase starts the next time it's online.
If lost permanently: AppleCare+ with Theft and Loss claim if covered; report to local law enforcement (serial number); contact wireless carrier to report loss and disable account; erase remotely only after trying everything else (can't be undone); review Apple Account, change password if changes you didn't make.
Warnings: Apple will never contact you to say your iPhone has been found. Never share passcode, passwords, verification codes. Don't remove the device from Find My even if erased.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone (Find My)",
             "messages": [
                 "I lost my iPhone at the park. I don't own any other Apple things, no iPad, no Mac. I only have an old Windows laptop at home. Can I still look for my phone?",
                 """Yes, you can use the laptop's web browser.

1. Go to **icloud.com/find**.
2. Sign in with your Apple Account.
3. Open the device list under **All Devices** and choose your iPhone.
4. From there, you can **play a sound**, **mark it as lost**, or erase it.

If you are asked for a verification code, select the **Find Devices** button instead. Marking it as lost locks it and can show a phone number and message. Only erase it as a last resort, because that cannot be undone.

Apple will never contact you to say your iPhone has been found, so do not share your passcode or codes with anyone who does.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone (Find My)",
             "messages": [
                 "My iPhone is missing since this morning. My wife has an iPad. What should I do on it?",
                 """Use the web browser on her iPad.

1. Go to **icloud.com/find**.
2. Sign in with your Apple Account.
3. Open **All Devices** and tap your iPhone.
4. Choose to mark it as lost.

You can also play a sound from here.""",
                 "It shows my phone as offline, no location at all.",
                 """That means it is off or not on Wi-Fi or cellular. Until it reconnects, it won't show as online or in Lost Mode. You can still mark it as lost now:

1. On her iPad, go to **icloud.com/find** in the web browser.
2. Sign in with your Apple Account if you are asked.
3. Open **All Devices** and tap your iPhone.
4. Choose to mark it as lost.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-075', "task_type": 'find_lost_phone', "task": 'Find a lost phone',
        "platform": 'Android', "category": 'technical_support', "sensitive": True,
        "source": {"title": 'Google Account Help: Find, secure, or erase a lost Android device', "url": 'https://support.google.com/accounts/answer/6160491?hl=en'},
        "source_notes": """Conditions: the phone has power, is connected to mobile data or Wi-Fi, is signed in to a Google Account, Find Hub is on, visible on Google Play.
Steps: open the Find Hub app on another Android phone or tablet, or go to google.com/android/find in a browser. Sign in (tap Continue as [your name] if it's your device; Sign in as guest if helping a friend). Select the device; it gets a notification. If prompted, enter lock screen PIN (Android 8 or lower or no PIN: may be asked for Google password). Check the map. Tap Get directions to navigate. Within 10 meters tap Find nearby.
Actions: Play sound (rings at full volume for 5 minutes even on silent or vibrate). Mark as lost: locks the device and displays a contact message on the lock screen; tap Mark as lost, then Next, add contact info and message, tap Mark as lost again. Factory reset (under Settings in Find Hub): permanently deletes data, may not delete SD cards, removes the device from Find Hub.
Troubleshooting: if current location can't be found, Find Hub may show last known location. GPS accurate to about 20 meters but can be off indoors or underground.
What you see: map with estimated location, radius around pin, Find nearby shape fills in as you get closer.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I think I dropped my Android phone on the bus. I really don't want to wipe it, my photos aren't all saved. I just want it locked, with my number on the screen so an honest person can call me. What do I do?",
                 """You can lock it and show your number without erasing anything.

1. On another Android phone or tablet, open the **Find Hub** app. On a computer, go to **google.com/android/find**.
2. Sign in and select your lost phone.
3. Tap **Mark as lost**, then tap **Next**.
4. Add your contact info and a message.
5. Tap **Mark as lost** again.

Skip **Factory reset**, since that permanently deletes the data. This works if your phone is on and connected to mobile data or Wi-Fi.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "Lost my Android phone somewhere in the house. I have a laptop handy. How do I find it?",
                 """Use Find Hub on your laptop.

1. Go to **google.com/android/find**.
2. Sign in with your Google Account.
3. Select your lost phone.
4. If asked, enter the lock screen PIN.
5. Look at the map to see where it is.

From there you can tap **Play sound** to ring it at full volume.""",
                 "The map shows a pin in my house but I walked there and still can't see the phone.",
                 """The location can be off by roughly 20 meters, and it is less reliable indoors. Try this:

1. Tap **Play sound**. It rings at full volume for 5 minutes, even on silent.
2. Walk toward the sound.
3. Once you are within 10 meters, tap **Find nearby**. A shape fills in as you get closer.""",
             ]},
        ],
    },
]
