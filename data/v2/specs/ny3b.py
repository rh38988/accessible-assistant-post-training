TASKS = [
    {
        "task_id": "TR-154",
        "task_type": "bluetooth_pair",
        "task": "Pair a Bluetooth accessory",
        "platform": "Android",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Android Help: Find and set up Bluetooth devices near your Android device", "url": "https://support.google.com/android/answer/9417604"},
        "source_notes": """Turn Bluetooth on: drag down from the top of the screen, tap the Bluetooth icon. Bluetooth is off in Airplane mode.
Pair (through Settings): 1 Drag down from the top of the screen. 2 Touch and hold the Bluetooth icon. 3 Tap "Pair new device". If you don't see "Pair new device": check under "Available devices", or tap the More icon, then "Refresh". 4 Tap the name of the Bluetooth accessory you want to pair. 5 Follow the on-screen prompts. If asked for a passcode and you don't have it, try the common ones "0000" or "1234" (a tip).
When phone and device are connected, the device shows as "Connected". Paired devices stay paired until you unpair them. If you see a notification to pair, Fast Pair connects automatically.
Page does NOT say to put the accessory in pairing mode or keep it close. Some steps work only on Android 15 and up; some need supporting hardware.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "How do I connect my new wireless earbuds to my Pixel phone?",
                 """Here is how to pair your earbuds with your phone:

1. Drag down from the top of the screen.
2. Touch and hold the **Bluetooth** icon.
3. Tap **Pair new device**.
4. Tap the name of your earbuds in the list.
5. Follow the on-screen prompts.

When it works, the earbuds show as **Connected**.

If you don't see **Pair new device**, look under **Available devices**, or tap the **More** icon and then **Refresh**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My daughter gave me a little Bluetooth speaker for my birthday and I have never used Bluetooth before. I have an Android phone. I got as far as seeing the speaker on my phone but now it wants some kind of passcode and I have no idea what to type. Can you walk me through the whole thing?",
                 """Happy birthday! Here is the whole thing:

1. Drag down from the top of the screen.
2. Touch and hold the **Bluetooth** icon.
3. Tap **Pair new device**.
4. Tap the name of your speaker.
5. Follow the on-screen prompts.

If it asks for a passcode and you don't have one, try **0000**. If that does not work, try **1234**.

When it works, the speaker shows as **Connected**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I just bought something that connects to my phone with Bluetooth. How do I set it up?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I just bought something that connects to my phone with Bluetooth. How do I set it up?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "It's an Android, a Pixel.",
                 """Thanks. Here is how to pair your Bluetooth device with your Pixel:

1. Drag down from the top of the screen.
2. Touch and hold the **Bluetooth** icon.
3. Tap **Pair new device**.
4. Tap the name of your device.
5. Follow the on-screen prompts.

When it works, the device shows as **Connected**.

If you don't see **Pair new device**, look under **Available devices**, or tap the **More** icon and then **Refresh**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I want to connect a Bluetooth keyboard to my Android phone so typing is easier on my eyes. I don't want to go hunting through lots of menus, my eyes get tired. Is there a quick way to start from the top of the screen?",
                 """Yes, you can start right from the top of the screen:

1. Drag down from the top of the screen.
2. Touch and hold the **Bluetooth** icon.
3. Tap **Pair new device**.
4. Tap the name of your keyboard.
5. Follow the on-screen prompts.

When it works, the keyboard shows as **Connected**.

Bluetooth is off while Airplane mode is on, so turn Airplane mode off before you pair.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "How do I pair my Bluetooth headphones with my Android phone?",
                 """Here is how to pair them:

1. Drag down from the top of the screen.
2. Touch and hold the **Bluetooth** icon.
3. Tap **Pair new device**.
4. Tap the name of your headphones.
5. Follow the on-screen prompts.

When it works, the headphones show as **Connected**.""",
                 "I touched and held the Bluetooth icon but I can't find Pair new device anywhere.",
                 """No problem. Try one of these:

1. Look under **Available devices** for your headphones.
2. Or tap the **More** icon, then tap **Refresh**.
3. When you see the name of your headphones, tap it and follow the on-screen prompts.""",
             ]},
        ],
    },
    {
        "task_id": "TR-155",
        "task_type": "brightness",
        "task": "Make the screen brighter or dimmer",
        "platform": "Android",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Pixel Phone Help: Change screen brightness", "url": "https://support.google.com/pixelphone/answer/6111557"},
        "source_notes": """Change brightness manually: 1 Open your phone's Settings app. 2 Tap "Display & touch". If you don't see the brightness setting, tap "Advanced" to see more settings. 3 Tap "Brightness level", then move the slider to set your preferred brightness.
"Adaptive brightness" adjusts brightness to the light around you; on by default; you can still change brightness manually while it is on; over time the phone learns your preferences. On Pixel 4 and later it can temporarily go above normal maximum in very bright light such as direct sunlight.
Page does not say how to turn adaptive brightness off. (Sensitive eyes setting is Pixel 10 Pro only; not used.) Page is for Pixel phones.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My Pixel phone screen is too dim. How do I make it brighter?",
                 """Here is how to make the screen brighter:

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Tap **Brightness level**.
4. Move the slider to set the brightness you like.

If you don't see the brightness setting, tap **Advanced** on the **Display & touch** screen to see more settings.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I read a lot at night before bed on my Pixel phone and the screen is so bright it hurts my eyes and keeps my husband awake. I went into Settings and Display & touch but I do not see anything about brightness on that screen, just a bunch of other things. How do I make it dimmer?",
                 """Let's get it dimmer. Since you are already in Settings:

1. On the **Display & touch** screen, tap **Advanced** to see more settings.
2. Tap **Brightness level**.
3. Move the slider toward the dimmer side.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "My phone screen is way too dark to see. Can you help?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My phone screen is way too dark to see. Can you help?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "Android. It's a Google Pixel.",
                 """Thanks. Here is how to make the screen brighter on your Pixel:

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Tap **Brightness level**.
4. Move the slider to a brighter setting.

If you don't see the brightness setting, tap **Advanced** on the **Display & touch** screen to see more settings.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I have a Pixel 8 and I only want to change the brightness myself. I don't want to touch any other settings, and I would like the screen a bit dimmer for the evening. It also seems to change by itself sometimes, why is that?",
                 """You only need one setting for this:

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Tap **Brightness level**.
4. Move the slider to make the screen dimmer.

The screen may change by itself because of **Adaptive brightness**. It is on by default and adjusts the screen to the light around you. You can still set the brightness yourself while it is on.

If you don't see the brightness setting, tap **Advanced** first.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "How can I change the screen brightness on my Pixel phone?",
                 """Here is how:

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Tap **Brightness level**.
4. Move the slider to the brightness you want.""",
                 "I'm on the Display & touch screen but there is no Brightness level there.",
                 """That can happen. Try this:

1. On the **Display & touch** screen, tap **Advanced** to see more settings.
2. Tap **Brightness level**.
3. Move the slider to the brightness you want.""",
             ]},
        ],
    },
    {
        "task_id": "TR-156",
        "task_type": "date_time",
        "task": "Fix the wrong date or time",
        "platform": "Android",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Android Help: Set time, date and time zone", "url": "https://support.google.com/android/answer/2841106"},
        "source_notes": """Open your device's Clock app. Tap More, then Settings. Then:
- Wrong time or date: tap "Change date and time", then turn on "Automatic date and time".
- Wrong time zone (automatic): tap "Change date and time". Under "Time zone", turn on "Automatic time zone".
- Wrong time zone (manual): tap "Change date and time", then tap "Time zone". If present, turn off "Set automatically". Tap "Time zone" again and select your time zone.
- Home clock: "Home time zone" to choose home zone; "Automatic home clock" shows a home clock when travelling.
Notes: automatic time zone may use device location ("Use location" setting). Only some devices support automatic time zone, so the option may be missing. Page uses the names "Automatic date and time" and "Automatic time zone"; menu names and places may differ on other phones/versions.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "The date and time on my Android phone is wrong. How do I fix it?",
                 """Here is how to fix it:

1. Open the **Clock** app.
2. Tap **More**, then tap **Settings**.
3. Tap **Change date and time**.
4. Turn on **Automatic date and time**.

If your screen looks a little different, the names can vary a bit on some phones.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "So I just flew back from visiting my sister and now my Android phone shows the wrong time, it is still on the old time zone, and I missed a doctor reminder because of it. The time is right when I look at my watch. I would like the phone to just fix the time zone on its own. What do I do?",
                 """Let's make the phone fix its own time zone:

1. Open the **Clock** app.
2. Tap **More**, then tap **Settings**.
3. Tap **Change date and time**.
4. Under **Time zone**, turn on **Automatic time zone**.

If you don't see **Automatic time zone**, your phone may not support it. Only some devices do.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "incomplete", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "the clock on my phone is wrong",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "incomplete", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "the clock on my phone is wrong",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "android",
                 """Thanks. Here is how to fix the time and date on your Android phone:

1. Open the **Clock** app.
2. Tap **More**, then tap **Settings**.
3. Tap **Change date and time**.
4. Turn on **Automatic date and time**.

Names can look a little different on some phones.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My Android phone has the wrong time zone. I don't want the phone guessing anything for me, I want to pick my own time zone from the list. I'm in the Central time zone. Please don't tell me to turn on the automatic one.",
                 """Understood. Here is how to choose it yourself:

1. Open the **Clock** app.
2. Tap **More**, then tap **Settings**.
3. Tap **Change date and time**.
4. Tap **Time zone**.
5. If you see **Set automatically**, turn it off.
6. Tap **Time zone** again.
7. Select your time zone from the list.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My Android phone shows the wrong time zone. How do I get it to fix itself?",
                 """Here is how:

1. Open the **Clock** app.
2. Tap **More**, then tap **Settings**.
3. Tap **Change date and time**.
4. Under **Time zone**, turn on **Automatic time zone**.""",
                 "There is no Automatic time zone on my phone. It's not there at all.",
                 """That can happen, because only some phones support it. You can pick the time zone yourself:

1. Tap **Time zone**.
2. If you see **Set automatically**, turn it off.
3. Tap **Time zone** again and select your time zone.""",
             ]},
        ],
    },
    {
        "task_id": "TR-157",
        "task_type": "home_screen_organize",
        "task": "Add and move apps on the Home screen",
        "platform": "Android",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Android Help: Add apps, shortcuts & widgets to your Home screens", "url": "https://support.google.com/android/answer/9450271"},
        "source_notes": """Add an app to a Home screen: 1 Swipe up from the bottom of the Home screen to open your apps. 2 Touch and drag the app; thumbnails of your Home screens appear. 3 Drag the app to the spot you want and release.
Move an app: 1 Touch and drag the app; thumbnails of Home screens appear. 2 Drag it to the new position. 3 Release. If dropped in the wrong place, just drag it again.
Remove an app from a Home screen: touch and hold the app, drag it up onto "Remove", release. "Remove" takes the app off the Home screen only; "Uninstall" removes it from the device.
Notes: some steps only work on Android 14 and up. If you move the last item off a Home screen, that Home screen is removed. Page does not cover phone brands or custom launchers.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "How do I put the Gmail app on my Android home screen so I can open it faster?",
                 """Here is how to add Gmail to your Home screen:

1. Swipe up from the bottom of the Home screen to open your apps.
2. Touch and drag the Gmail app. Thumbnails of your Home screens appear.
3. Drag the app to the spot you want.
4. Let go of it there.

If it lands in the wrong place, just drag it again.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I have an Android phone and the camera app is way down in the corner where I always miss it. My grandson showed me once how to rearrange things but I forgot. I want to take the camera icon that is already on my home screen and put it right at the bottom in the middle. How?",
                 """You can move it like this:

1. Touch and drag the camera app. Thumbnails of your Home screens appear.
2. Drag it to the spot you want.
3. Let go of it there.

If it lands in the wrong place, just drag it again.

Some of these steps only work on Android 14 and newer.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I want my favorite app on the main screen of my phone. How?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I want my favorite app on the main screen of my phone. How?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "Android",
                 """Thanks. Here is how to add an app to the Home screen on your Android phone:

1. Swipe up from the bottom of the Home screen to open your apps.
2. Touch and drag your favorite app. Thumbnails of your Home screens appear.
3. Drag the app to the spot you want.
4. Let go of it there.

If it lands in the wrong place, just drag it again.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I'm scared of deleting something by accident on my Android phone. I only want to add the weather app to my home screen and I do not want to uninstall or lose anything. Can you tell me what to do and what to stay away from?",
                 """Adding an app does not delete anything. Here is how to add the weather app:

1. Swipe up from the bottom of the Home screen to open your apps.
2. Touch and drag the weather app. Thumbnails of your Home screens appear.
3. Drag the app to the spot you want.
4. Let go of it there.

Stay away from **Remove** and **Uninstall**. They show up when you touch and hold an app and drag it up. **Remove** only takes an app off the Home screen. **Uninstall** takes it off your phone.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "How do I add the Photos app to the home screen on my Android phone?",
                 """Here is how:

1. Swipe up from the bottom of the Home screen to open your apps.
2. Touch and drag the Photos app. Thumbnails of your Home screens appear.
3. Drag the app to the spot you want.
4. Let go of it there.""",
                 "I did it but it landed in the wrong spot, not where I wanted.",
                 """That is easy to fix. Just move it again:

1. Touch and drag the app. Thumbnails of your Home screens appear.
2. Drag it to the new spot you want.
3. Let go of it there.""",
             ]},
        ],
    },
    {
        "task_id": "TR-158",
        "task_type": "stolen_device_protection",
        "task": "Turn on theft protection",
        "platform": "Android",
        "category": "technical_support",
        "sensitive": True,
        "source": {"title": "Android Help: Protect your personal data against theft", "url": "https://support.google.com/android/answer/15146908"},
        "source_notes": """Common path: open Settings, tap "Google", then "All services", then under "Personal & device safety" tap "Theft protection".
Before you start: set a screen lock first (features won't turn on without one). Some steps need Android 10 or later; Remote Lock and some protections need Android 15 or later. Not supported on Android Go devices, tablets, wearables; support varies by phone model. Some may already be on by default.
1 Theft Detection Lock: go to Theft protection, turn on "Theft Detection Lock". Screen locks automatically if the device is taken from you (grab-and-run). If setting is grayed out, the device doesn't support it. If it locks during normal use, unlock and keep using.
2 Offline Device Lock: go to Theft protection, turn on "Offline Device Lock". Screen locks after the device has been used offline for a short time. Phone must be unlocked when it loses internet.
3 Remote Lock: go to Theft protection, tap "Remote Lock", turn on "Remote lock". Requirements: screen lock, active SIM, verified phone number, Find Hub turned on, internet connection. If number not verified: tap "Verify number", then turn on "Automatically verify phone numbers". To lock remotely: go to android.com/lock, enter your phone number, complete the reCAPTCHA, request a lock. If device offline it locks once reconnected. Works twice in 24 hours. Needs Android 15 or later.
4 Identity Check: certain devices only (not covered in examples).""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I heard my Android phone can lock itself if someone grabs it out of my hand and runs. How do I turn that on?",
                 """That is the **Theft Detection Lock** setting. Here is how to turn it on:

1. Open the **Settings** app.
2. Tap **Google**.
3. Tap **All services**.
4. Under **Personal & device safety**, tap **Theft protection**.
5. Turn on **Theft Detection Lock**.

Once it is on, the screen locks automatically if the phone is taken from you.

Set a screen lock first, because the setting won't turn on without one. If it is grayed out, your phone doesn't support it.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My neighbor's phone got snatched on the bus and the thief switched off the internet right away so she could not do anything. I have an Android phone and I want mine to lock itself if that ever happens to me, even with no internet. Is there a setting for that?",
                 """Yes. It is called **Offline Device Lock**. Here is how to turn it on:

1. Open the **Settings** app.
2. Tap **Google**.
3. Tap **All services**.
4. Under **Personal & device safety**, tap **Theft protection**.
5. Turn on **Offline Device Lock**.

Once it is on, the screen locks after the phone has been used offline for a short time. Your phone must be unlocked when it loses its internet connection.

Set a screen lock first, because the setting won't turn on without one.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I want to make my phone safer in case somebody steals it. What should I turn on?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I want to make my phone safer in case somebody steals it. What should I turn on?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "Android phone",
                 """Thanks. A good setting to start with is **Theft Detection Lock**:

1. Open the **Settings** app.
2. Tap **Google**.
3. Tap **All services**.
4. Under **Personal & device safety**, tap **Theft protection**.
5. Turn on **Theft Detection Lock**.

Once it is on, the screen locks automatically if the phone is taken from you.

Set a screen lock first, because the setting won't turn on without one.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I don't want to count on my phone guessing that it was grabbed. I want to be able to lock it myself from my laptop if it goes missing. My Android phone has a screen lock, a working SIM, and Find Hub is on. What do I set up?",
                 """You want **Remote Lock**. Here is how to turn it on:

1. Open the **Settings** app.
2. Tap **Google**.
3. Tap **All services**.
4. Under **Personal & device safety**, tap **Theft protection**.
5. Tap **Remote Lock**.
6. Turn on **Remote lock**.

If it says your number isn't verified, tap **Verify number**, then turn on **Automatically verify phone numbers**.

To lock the phone later, use your laptop:

1. Go to android.com/lock.
2. Enter your phone number.
3. Complete the security check (reCaptcha) that appears.
4. Request the lock.

The phone screen locks shortly after.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "How do I turn on Theft Detection Lock on my Android phone?",
                 """Here is how:

1. Open the **Settings** app.
2. Tap **Google**.
3. Tap **All services**.
4. Under **Personal & device safety**, tap **Theft protection**.
5. Turn on **Theft Detection Lock**.""",
                 "The Theft Detection Lock switch is gray and I can't turn it on.",
                 """When it is grayed out, your phone doesn't support that setting. Support differs from phone to phone.

You can look at the same **Theft protection** screen for other protections your phone may offer, such as **Offline Device Lock**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-159",
        "task_type": "wifi_calling",
        "task": "Make calls over Wi-Fi",
        "platform": "Android",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Phone app Help: Make calls over Wi-Fi", "url": "https://support.google.com/phoneapp/answer/2811843"},
        "source_notes": """Turn on: 1 Open the device's Settings app. 2 Go to "Network & internet", then "SIMs", then "Carrier SIM", then "Wi-Fi calling". If "Wi-Fi calling" doesn't appear, your carrier doesn't support it. 3 Turn on "Wi-Fi calling". Some carriers let you use Wi-Fi calling without a mobile service plan.
Make calls: place calls as you normally would. When connected to the internet, the notification screen shows "Internet Call" or "Wi-Fi calling". Without Wi-Fi, calls use your mobile carrier if you have one.
Conditions: some steps only work on Android 6.0 and up. Wi-Fi calling may incur extra charges, check with your mobile provider. Confirm with your carrier that it is supported.
Troubleshooting: if the phone detects a Wi-Fi calling problem it turns Wi-Fi calling off until fixed; if it persists a notification says it was turned off entirely; you may need to restart the device or contact your carrier to reactivate it.
No emergency call info on the page.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My Android phone gets bad cell signal inside my house. Can I make phone calls over my Wi-Fi instead? How do I set that up?",
                 """Yes, you can. Here is how to turn on Wi-Fi calling:

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **SIMs**.
4. Tap **Carrier SIM**.
5. Tap **Wi-Fi calling**.
6. Turn on **Wi-Fi calling**.

After that, make calls the way you always do. When your phone is connected to the internet, the notification screen shows **Internet Call** or **Wi-Fi calling**.

If you don't see **Wi-Fi calling**, your carrier doesn't support it.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "We live out in the country and the signal is terrible in our basement where my husband's workshop is. Our grandson says my Android phone can call using the internet but I am worried it will cost extra money on our bill. How do I turn it on and will it cost anything?",
                 """Here is how to turn on Wi-Fi calling:

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **SIMs**.
4. Tap **Carrier SIM**.
5. Tap **Wi-Fi calling**.
6. Turn on **Wi-Fi calling**.

About cost, Wi-Fi calling may come with extra charges, so check with your mobile provider before you use it.

If you don't see **Wi-Fi calling**, your carrier doesn't support it.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I have bad signal at home. Can I call people over my Wi-Fi instead?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I have bad signal at home. Can I call people over my Wi-Fi instead?",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "It's an Android.",
                 """Yes, you can. Here is how to turn on Wi-Fi calling on your Android phone:

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **SIMs**.
4. Tap **Carrier SIM**.
5. Tap **Wi-Fi calling**.
6. Turn on **Wi-Fi calling**.

After that, make calls the way you always do.

If you don't see **Wi-Fi calling**, your carrier doesn't support it.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I'm staying at my daughter's house for a while and I don't have a mobile service plan on my Android phone right now, just her Wi-Fi. Is there any way to still make phone calls with it?",
                 """It may work. Some carriers let you use Wi-Fi calling without a mobile service plan. Here is how to check:

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **SIMs**.
4. Tap **Carrier SIM**.
5. Tap **Wi-Fi calling**.
6. Turn on **Wi-Fi calling**.

Then make calls as you normally would while you are connected to her Wi-Fi.

If you don't see **Wi-Fi calling**, your carrier doesn't support it. Whether this works without a plan depends on your carrier, so ask your carrier to confirm.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "How do I turn on Wi-Fi calling on my Android phone?",
                 """Here is how:

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **SIMs**.
4. Tap **Carrier SIM**.
5. Tap **Wi-Fi calling**.
6. Turn on **Wi-Fi calling**.""",
                 "I got to Carrier SIM but there is no Wi-Fi calling option on that screen.",
                 """If **Wi-Fi calling** doesn't appear, your carrier doesn't support it. It is best to ask your carrier to confirm.""",
             ]},
        ],
    },
]
