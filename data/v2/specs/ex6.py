"""Existing English drafts, group 6. Exported by export_spec.py; ids and provenance preserved."""
TASKS = [
    {
        "task_id": 'TR-076', "task_type": 'scan_qr', "task": 'Scan a QR code',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Scan a QR code with your iPhone or iPad', "url": 'https://support.apple.com/en-us/102680'},
        "examples": [
            {
                "existing": True, "id": 'tr076-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Scan a QR code with your iPhone or iPad', 'url': 'https://support.apple.com/en-us/102680', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I scan a QR code with my iPhone? The restaurant menu is a QR code.',
                    """Your iPhone camera can read QR codes. It takes a few seconds.

1. Open the **Camera** app.
2. Point the camera at the QR code so it shows on the screen.
3. Tap the **link** that appears on the screen.

The restaurant's menu will open.

You can also open **Control Center** and tap **Scan Code**.

Only open QR codes you trust, like ones printed on the restaurant's own menu or table.""",
                ],
            },
            {
                "existing": True, "id": 'tr076-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Scan a QR code with your iPhone or iPad', 'url': 'https://support.apple.com/en-us/102680', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do i scan a QR code',
                    'Sure. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr076-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Scan a QR code with your iPhone or iPad', 'url': 'https://support.apple.com/en-us/102680', 'accessed': '2026-10-24'}],
                "messages": [
                    "We went to lunch and there were no paper menus, just a little black and white square on the table. My friend scanned it with her phone but I didn't know how. I have an iPhone 12.",
                    """That square is a QR code, and your iPhone can read it with the camera. Next time, try this:

Your iPhone camera can read QR codes. It takes a few seconds.

1. Open the **Camera** app.
2. Point the camera at the QR code so it shows on the screen.
3. Tap the **link** that appears on the screen.

The restaurant's menu will open.

You can also open **Control Center** and tap **Scan Code**.

Only open QR codes you trust, like ones printed on the restaurant's own menu or table.""",
                ],
            },
            {
                "existing": True, "id": 'tr076-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Scan a QR code with your iPhone or iPad', 'url': 'https://support.apple.com/en-us/102680', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do i scan a QR code',
                    'Sure. Is your phone an **iPhone** or an **Android** phone?',
                    'iPhone',
                    """Thanks.

Your iPhone camera can read QR codes. It takes a few seconds.

1. Open the **Camera** app.
2. Point the camera at the QR code so it shows on the screen.
3. Tap the **link** that appears on the screen.

The restaurant's menu will open.

You can also open **Control Center** and tap **Scan Code**.

Only open QR codes you trust, like ones printed on the restaurant's own menu or table.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-077', "task_type": 'scan_qr', "task": 'Scan a QR code',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Camera from Google Help: Scan QR codes', "url": 'https://support.google.com/camerafromgoogle/answer/12033278?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr077-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Camera from Google Help: Scan QR codes', 'url': 'https://support.google.com/camerafromgoogle/answer/12033278?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "How do I scan a QR code with my Android phone's camera?",
                    """Many Android phones can read QR codes with the camera. It takes a few seconds.

1. Open the **Camera** app.
2. Make sure it's in regular **photo** mode. QR scanning doesn't work in video or portrait mode. Some phones also have a **QR** option you can tap.
3. Point the camera at the QR code.
4. When a banner appears on the screen, tap it to open the link.

These steps are for Google's Camera app. Other phone brands work in a similar way but may look different. If nothing appears, tell me your phone's brand and I'll help.

Only open QR codes you trust. If a QR code asks you to pay or sign in, double-check that it's from the real business first.""",
                ],
            },
            {
                "existing": True, "id": 'tr077-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Camera from Google Help: Scan QR codes', 'url': 'https://support.google.com/camerafromgoogle/answer/12033278?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I read one of those square codes with my phone',
                    'Those are called **QR codes**, and most phones can read them with the camera. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr077-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Camera from Google Help: Scan QR codes', 'url': 'https://support.google.com/camerafromgoogle/answer/12033278?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'qr code wont',
                    "It looks like your message got cut off. Is the QR code **not scanning**, or is it **opening something you didn't expect**? And is your phone an iPhone or an Android phone?",
                ],
            },
            {
                "existing": True, "id": 'tr077-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Camera from Google Help: Scan QR codes', 'url': 'https://support.google.com/camerafromgoogle/answer/12033278?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I read one of those square codes with my phone',
                    'Those are called **QR codes**, and most phones can read them with the camera. Is your phone an **iPhone** or an **Android** phone?',
                    'Android, Pixel',
                    """Thanks. Your Pixel's camera can do it.

Many Android phones can read QR codes with the camera. It takes a few seconds.

1. Open the **Camera** app.
2. Make sure it's in regular **photo** mode. QR scanning doesn't work in video or portrait mode. Some phones also have a **QR** option you can tap.
3. Point the camera at the QR code.
4. When a banner appears on the screen, tap it to open the link.

These steps are for Google's Camera app. Other phone brands work in a similar way but may look different. If nothing appears, tell me your phone's brand and I'll help.

Only open QR codes you trust. If a QR code asks you to pay or sign in, double-check that it's from the real business first.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-078', "task_type": 'emergency_info', "task": 'Set up emergency medical info',
        "platform": 'iPhone (Medical ID)', "category": 'technical_support', "sensitive": True,
        "source": {"title": 'Apple Support: Set up your Medical ID in the Health app on your iPhone', "url": 'https://support.apple.com/en-us/105072'},
        "examples": [
            {
                "existing": True, "id": 'tr078-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone (Medical ID)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Apple Support: Set up your Medical ID in the Health app on your iPhone', 'url': 'https://support.apple.com/en-us/105072', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I set up Medical ID on my iPhone so paramedics can see my allergies?',
                    """Medical ID lets first responders see your important health information from the Lock Screen, without your passcode. It takes about five minutes.

1. Open the **Health** app.
2. Tap **Summary** at the bottom.
3. Tap your **profile picture** at the top.
4. Tap **Medical ID**.
5. Tap **Edit**.
6. Turn on **Show When Locked** so it can be seen from the Lock Screen.
7. Tap **Add** next to a section, like **Allergies**, and type your information.
8. Tap **Done**.

**Add emergency contacts:** in Medical ID, tap **Edit** next to **Emergency Contacts**, tap the **plus** button, choose a contact, and pick how they're related to you.

Keep in mind that anyone holding your phone can see this information, so only add what you're comfortable sharing.""",
                ],
            },
            {
                "existing": True, "id": 'tr078-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Apple Support: Set up your Medical ID in the Health app on your iPhone', 'url': 'https://support.apple.com/en-us/105072', 'accessed': '2026-10-24'}],
                "messages": [
                    'how can I put my medical information on my phone in case of emergency',
                    "That's a really good idea. Is your phone an **iPhone** or an **Android** phone?",
                ],
            },
            {
                "existing": True, "id": 'tr078-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Set up your Medical ID in the Health app on your iPhone', 'url': 'https://support.apple.com/en-us/105072', 'accessed': '2026-10-24'}],
                "messages": [
                    "I'm allergic to penicillin and my daughter said I should put it in my phone in case something happens.",
                    """Your daughter has a good idea. Phones can show emergency medical information on the lock screen so responders can see it.

**Is your phone an iPhone or an Android phone?**""",
                ],
            },
            {
                "existing": True, "id": 'tr078-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone (Medical ID)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Apple Support: Set up your Medical ID in the Health app on your iPhone', 'url': 'https://support.apple.com/en-us/105072', 'accessed': '2026-10-24'}],
                "messages": [
                    'how can I put my medical information on my phone in case of emergency',
                    "That's a really good idea. Is your phone an **iPhone** or an **Android** phone?",
                    'iPhone',
                    """Thanks. On iPhone, this is called Medical ID.

Medical ID lets first responders see your important health information from the Lock Screen, without your passcode. It takes about five minutes.

1. Open the **Health** app.
2. Tap **Summary** at the bottom.
3. Tap your **profile picture** at the top.
4. Tap **Medical ID**.
5. Tap **Edit**.
6. Turn on **Show When Locked** so it can be seen from the Lock Screen.
7. Tap **Add** next to a section, like **Allergies**, and type your information.
8. Tap **Done**.

**Add emergency contacts:** in Medical ID, tap **Edit** next to **Emergency Contacts**, tap the **plus** button, choose a contact, and pick how they're related to you.

Keep in mind that anyone holding your phone can see this information, so only add what you're comfortable sharing.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-079', "task_type": 'emergency_info', "task": 'Add emergency information',
        "platform": 'Android', "category": 'technical_support', "sensitive": True,
        "source": {"title": 'Android Help: Get help during an emergency with your Android phone', "url": 'https://support.google.com/android/answer/9319337?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr079-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Android Help: Get help during an emergency with your Android phone', 'url': 'https://support.google.com/android/answer/9319337?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I add my emergency contacts and medical info on my Android phone?',
                    """On Android, this is in the **Safety** app. It takes about five minutes.

**Medical information:**
1. Open the **Safety** app and sign in with your Google Account if asked.
2. Tap **Your info**.
3. Tap **Medical information**.
4. Tap an item, like **Allergies** or **Medications**, and type your details.

**Emergency contacts:**
1. In the Safety app, tap **Your info**, then **Emergency contacts**.
2. Tap **Add contact** and choose someone.

**Show it on the lock screen:**
- Tap **Emergency info access** and turn on **Show when locked**.

Anyone who picks up your phone can see this information, so only add what you're comfortable sharing. To view it from the lock screen, swipe up, tap **Emergency**, then **View emergency info**.""",
                ],
            },
            {
                "existing": True, "id": 'tr079-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Android Help: Get help during an emergency with your Android phone', 'url': 'https://support.google.com/android/answer/9319337?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I put an emergency contact in my phone',
                    'Good idea. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr079-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'over_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Help: Get help during an emergency with your Android phone', 'url': 'https://support.google.com/android/answer/9319337?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'Pixel 7, Android 15. I want my husband listed as my emergency contact and my blood thinner listed under medications, visible without unlocking.',
                    """Here's how to set up exactly that:

On Android, this is in the **Safety** app. It takes about five minutes.

**Medical information:**
1. Open the **Safety** app and sign in with your Google Account if asked.
2. Tap **Your info**.
3. Tap **Medical information**.
4. Tap an item, like **Allergies** or **Medications**, and type your details.

**Emergency contacts:**
1. In the Safety app, tap **Your info**, then **Emergency contacts**.
2. Tap **Add contact** and choose someone.

**Show it on the lock screen:**
- Tap **Emergency info access** and turn on **Show when locked**.

Anyone who picks up your phone can see this information, so only add what you're comfortable sharing. To view it from the lock screen, swipe up, tap **Emergency**, then **View emergency info**.""",
                ],
            },
            {
                "existing": True, "id": 'tr079-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Android Help: Get help during an emergency with your Android phone', 'url': 'https://support.google.com/android/answer/9319337?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I put an emergency contact in my phone',
                    'Good idea. Is your phone an **iPhone** or an **Android** phone?',
                    'Android',
                    """Thanks.

On Android, this is in the **Safety** app. It takes about five minutes.

**Medical information:**
1. Open the **Safety** app and sign in with your Google Account if asked.
2. Tap **Your info**.
3. Tap **Medical information**.
4. Tap an item, like **Allergies** or **Medications**, and type your details.

**Emergency contacts:**
1. In the Safety app, tap **Your info**, then **Emergency contacts**.
2. Tap **Add contact** and choose someone.

**Show it on the lock screen:**
- Tap **Emergency info access** and turn on **Show when locked**.

Anyone who picks up your phone can see this information, so only add what you're comfortable sharing. To view it from the lock screen, swipe up, tap **Emergency**, then **View emergency info**.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-080', "task_type": 'app_notifications_off', "task": 'Turn off notifications from an app',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Turn notifications on or off for a specific app on your iPhone', "url": 'https://support.apple.com/en-us/120681'},
        "examples": [
            {
                "existing": True, "id": 'tr080-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Turn notifications on or off for a specific app on your iPhone', 'url': 'https://support.apple.com/en-us/120681', 'accessed': '2026-10-24'}],
                "messages": [
                    'One of my iPhone games keeps sending me notifications. How do I turn them off?',
                    """You can turn off notifications for just that app. It takes less than a minute.

1. Open the **Settings** app.
2. Tap **Apps**.
3. Find and tap the game.
4. Tap **Notifications**.
5. Turn off **Allow Notifications**.

The game will still work. It just won't send you alerts anymore.

If you don't see **Notifications** for that app, it means the app can't send notifications.""",
                ],
            },
            {
                "existing": True, "id": 'tr080-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Turn notifications on or off for a specific app on your iPhone', 'url': 'https://support.apple.com/en-us/120681', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I stop all these pop-ups on my phone',
                    'I can help. **Which app is sending them** (for example a game, a store, or the news)? And is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr080-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Turn notifications on or off for a specific app on your iPhone', 'url': 'https://support.apple.com/en-us/120681', 'accessed': '2026-10-24'}],
                "messages": [
                    'notifications keep',
                    'It looks like your message got cut off. Are notifications **popping up too often**, or have they **stopped showing up**? And which app is it?',
                ],
            },
            {
                "existing": True, "id": 'tr080-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Turn notifications on or off for a specific app on your iPhone', 'url': 'https://support.apple.com/en-us/120681', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I stop all these pop-ups on my phone',
                    'I can help. **Which app is sending them** (for example a game, a store, or the news)? And is your phone an **iPhone** or an **Android** phone?',
                    "It's a solitaire game. iPhone.",
                    """Thanks. Here's how to turn off notifications for the solitaire game.

You can turn off notifications for just that app. It takes less than a minute.

1. Open the **Settings** app.
2. Tap **Apps**.
3. Find and tap the game.
4. Tap **Notifications**.
5. Turn off **Allow Notifications**.

The game will still work. It just won't send you alerts anymore.

If you don't see **Notifications** for that app, it means the app can't send notifications.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-081', "task_type": 'app_notifications_off', "task": 'Turn off notifications from an app',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Control notifications on Android', "url": 'https://support.google.com/android/answer/9079661?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr081-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Control notifications on Android', 'url': 'https://support.google.com/android/answer/9079661?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I stop a shopping app from sending notifications on my Android phone?',
                    """You can turn them off for just that app. It takes less than a minute.

**Option 1, from Settings:**
1. Open **Settings**.
2. Tap **Notifications**, then **App notifications**.
3. Find the shopping app. If it's not in the list, open the menu at the top and choose all apps.
4. Tap the app and turn its notifications off.

**Option 2, from a notification:**
1. When a notification from the app shows up, swipe down from the top of the screen.
2. Press and hold the notification, then tap the settings icon.
3. Turn off notifications.

Menu names can vary a little on different phones.""",
                ],
            },
            {
                "existing": True, "id": 'tr081-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Control notifications on Android', 'url': 'https://support.google.com/android/answer/9079661?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'can I make an app stop bugging me',
                    'Yes, you can turn off its notifications. Which app is it, and is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr081-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Help: Control notifications on Android', 'url': 'https://support.google.com/android/answer/9079661?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'Ever since I bought shoes online, my phone buzzes all day with sales and coupons. I just want it to stop.',
                    """That sounds tiring. You can usually turn off alerts from just that store.

**Are the alerts coming from an app on your phone, or are they emails or texts?** And is your phone an iPhone or an Android phone?""",
                ],
            },
            {
                "existing": True, "id": 'tr081-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Control notifications on Android', 'url': 'https://support.google.com/android/answer/9079661?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'can I make an app stop bugging me',
                    'Yes, you can turn off its notifications. Which app is it, and is your phone an **iPhone** or an **Android** phone?',
                    'A shopping app on my Android',
                    """Thanks.

You can turn them off for just that app. It takes less than a minute.

**Option 1, from Settings:**
1. Open **Settings**.
2. Tap **Notifications**, then **App notifications**.
3. Find the shopping app. If it's not in the list, open the menu at the top and choose all apps.
4. Tap the app and turn its notifications off.

**Option 2, from a notification:**
1. When a notification from the app shows up, swipe down from the top of the screen.
2. Press and hold the notification, then tap the settings icon.
3. Turn off notifications.

Menu names can vary a little on different phones.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-082', "task_type": 'browser_zoom', "task": 'Make a web page bigger',
        "platform": 'Chrome (computer)', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Google Chrome Help: Change text, image & video sizes (zoom), computer', "url": 'https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop'},
        "examples": [
            {
                "existing": True, "id": 'tr082-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Chrome (computer)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Chrome Help: Change text, image & video sizes (zoom), computer', 'url': 'https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I make a web page bigger in Chrome on my computer? The words are tiny.',
                    """You can zoom in on the page. It takes a few seconds.

**With the mouse:**
1. Click the **More** menu (three dots) at the top right of Chrome.
2. Next to **Zoom**, click **+** to make the page bigger. Click **-** to make it smaller.

**With the keyboard:**
- Hold **Ctrl** and press **+** to zoom in, or **-** to zoom out. (On a Mac, use **Command** instead of Ctrl.)

If you want every website bigger from now on, change the default size in **Settings**, then **Appearance**, then **Page zoom**.""",
                ],
            },
            {
                "existing": True, "id": 'tr082-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Chrome Help: Change text, image & video sizes (zoom), computer', 'url': 'https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'the words on this website are too small',
                    "I can help you make them bigger. Are you on a **computer**, **phone**, or **tablet**? And if it's a computer, which browser do you use, like Chrome?",
                ],
            },
            {
                "existing": True, "id": 'tr082-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Chrome Help: Change text, image & video sizes (zoom), computer', 'url': 'https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'chrome zoom',
                    'Sure. Do you want to make **just this page** bigger, or **every website** bigger from now on?',
                ],
            },
            {
                "existing": True, "id": 'tr082-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Chrome (computer)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Chrome Help: Change text, image & video sizes (zoom), computer', 'url': 'https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'the words on this website are too small',
                    "I can help you make them bigger. Are you on a **computer**, **phone**, or **tablet**? And if it's a computer, which browser do you use, like Chrome?",
                    'Computer, Chrome',
                    """Thanks.

You can zoom in on the page. It takes a few seconds.

**With the mouse:**
1. Click the **More** menu (three dots) at the top right of Chrome.
2. Next to **Zoom**, click **+** to make the page bigger. Click **-** to make it smaller.

**With the keyboard:**
- Hold **Ctrl** and press **+** to zoom in, or **-** to zoom out. (On a Mac, use **Command** instead of Ctrl.)

If you want every website bigger from now on, change the default size in **Settings**, then **Appearance**, then **Page zoom**.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-083', "task_type": 'find_downloads', "task": 'Find a downloaded file',
        "platform": 'Windows 11', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Microsoft Support: Find my downloads in Windows', "url": 'https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8'},
        "examples": [
            {
                "existing": True, "id": 'tr083-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Find my downloads in Windows', 'url': 'https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8', 'accessed': '2026-10-24'}],
                "messages": [
                    'I downloaded a form from a website on my Windows computer. Where did it go?',
                    """Files you download usually go to your **Downloads** folder. Here's how to find it.

1. Open **File Explorer**. Click the folder icon on the taskbar, or hold the **Windows logo key** and press **E**.
2. On the left side, click **Downloads**. You can also find it under **This PC**.
3. Look for your form. If the folder is sorted by date, your newest download will be near the top.

If you don't see it, tell me what the form is called or what website it came from, and we'll look together.""",
                ],
            },
            {
                "existing": True, "id": 'tr083-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Find my downloads in Windows', 'url': 'https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8', 'accessed': '2026-10-24'}],
                "messages": [
                    "I can't find something I downloaded",
                    "Let's find it. Did you download it on a **computer** or a **phone**? If it's a computer, is it **Windows** or a **Mac**?",
                ],
            },
            {
                "existing": True, "id": 'tr083-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Find my downloads in Windows', 'url': 'https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8', 'accessed': '2026-10-24'}],
                "messages": [
                    "My insurance company emailed me a link to download my card as a PDF and I clicked it and something happened at the bottom of the screen but then it disappeared and now I have no idea where the card is. It's a Windows computer.",
                    """It's most likely in your Downloads folder. Here's how to find it:

Files you download usually go to your **Downloads** folder. Here's how to find it.

1. Open **File Explorer**. Click the folder icon on the taskbar, or hold the **Windows logo key** and press **E**.
2. On the left side, click **Downloads**. You can also find it under **This PC**.
3. Look for your form. If the folder is sorted by date, your newest download will be near the top.

If you don't see it, tell me what the form is called or what website it came from, and we'll look together.""",
                ],
            },
            {
                "existing": True, "id": 'tr083-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Find my downloads in Windows', 'url': 'https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8', 'accessed': '2026-10-24'}],
                "messages": [
                    "I can't find something I downloaded",
                    "Let's find it. Did you download it on a **computer** or a **phone**? If it's a computer, is it **Windows** or a **Mac**?",
                    'Windows computer',
                    """Thanks.

Files you download usually go to your **Downloads** folder. Here's how to find it.

1. Open **File Explorer**. Click the folder icon on the taskbar, or hold the **Windows logo key** and press **E**.
2. On the left side, click **Downloads**. You can also find it under **This PC**.
3. Look for your form. If the folder is sorted by date, your newest download will be near the top.

If you don't see it, tell me what the form is called or what website it came from, and we'll look together.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-084', "task_type": 'mouse_pointer_size', "task": 'Make the mouse pointer bigger',
        "platform": 'Windows 11', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Microsoft Support: Make Windows easier to see', "url": 'https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see'},
        "examples": [
            {
                "existing": True, "id": 'tr084-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Make Windows easier to see', 'url': 'https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I make the mouse pointer bigger on Windows 11? I keep losing it on the screen.',
                    """You can make the pointer bigger and easier to spot. It takes about a minute.

1. Click the **Start** button, then **Settings**.
2. Click **Accessibility**.
3. Click **Mouse pointer & touch**.
4. Change the **size** to make the pointer bigger.
5. You can also change the **style** or color so it stands out more.

Try a few sizes until it's easy to find.""",
                ],
            },
            {
                "existing": True, "id": 'tr084-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Make Windows easier to see', 'url': 'https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see', 'accessed': '2026-10-24'}],
                "messages": [
                    'I keep losing the arrow on my screen',
                    "That's common, and the arrow can be made bigger. Is your computer a **Windows** computer or a **Mac**?",
                ],
            },
            {
                "existing": True, "id": 'tr084-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Make Windows easier to see', 'url': 'https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see', 'accessed': '2026-10-24'}],
                "messages": [
                    'mouse too small',
                    'I can help you make the mouse pointer bigger. Is your computer a **Windows** computer or a **Mac**?',
                ],
            },
            {
                "existing": True, "id": 'tr084-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Make Windows easier to see', 'url': 'https://support.microsoft.com/en-us/accessibility/windows/make-windows-easier-to-see', 'accessed': '2026-10-24'}],
                "messages": [
                    'I keep losing the arrow on my screen',
                    "That's common, and the arrow can be made bigger. Is your computer a **Windows** computer or a **Mac**?",
                    'Windows 11',
                    """Thanks.

You can make the pointer bigger and easier to spot. It takes about a minute.

1. Click the **Start** button, then **Settings**.
2. Click **Accessibility**.
3. Click **Mouse pointer & touch**.
4. Change the **size** to make the pointer bigger.
5. You can also change the **style** or color so it stands out more.

Try a few sizes until it's easy to find.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-085', "task_type": 'two_step_verification', "task": 'Turn on 2-Step Verification',
        "platform": 'Google Account', "category": 'online_services', "sensitive": True,
        "source": {"title": 'Google Account Help: Turn on 2-Step Verification (computer)', "url": 'https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop'},
        "examples": [
            {
                "existing": True, "id": 'tr085-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Google Account',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Google Account Help: Turn on 2-Step Verification (computer)', 'url': 'https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}, {'title': 'Google Account Help: How to recover your Google Account or Gmail', 'url': 'https://support.google.com/accounts/answer/7682439?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I turn on 2-Step Verification for my Google account on my computer?',
                    """2-Step Verification adds a second check when you sign in, so a password alone isn't enough to get into your account. Setting it up takes about five minutes.

1. Go to **myaccount.google.com** and sign in.
2. Click **Security & sign-in**.
3. Under **How you sign in to Google**, click **Turn on 2-Step Verification**.
4. Follow the steps on the screen.

After it's on, Google may ask you to confirm with your phone when you sign in on a new device.

**Never share these codes with anyone**, even if they say they're from Google.

If you use a work or school account, your administrator may control this setting.""",
                ],
            },
            {
                "existing": True, "id": 'tr085-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft, edited by Ryan Hsieh', "reviewed": True, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Google Account Help: Turn on 2-Step Verification (computer)', 'url': 'https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}, {'title': 'Google Account Help: How to recover your Google Account or Gmail', 'url': 'https://support.google.com/accounts/answer/7682439?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I make my email account more secure',
                    'Good question. Which email do you use, for example **Gmail**, **Outlook**, or **Yahoo**?',
                ],
            },
            {
                "existing": True, "id": 'tr085-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Account Help: Turn on 2-Step Verification (computer)', 'url': 'https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}, {'title': 'Google Account Help: How to recover your Google Account or Gmail', 'url': 'https://support.google.com/accounts/answer/7682439?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "My friend's email got hacked and sent everyone weird links. Her son told her to turn on two step something. I want to do that too so it doesn't happen to me.",
                    """That's a smart idea. It's called **2-Step Verification**, and most email services offer it.

**Which email do you use**, for example Gmail, Yahoo, or Outlook?""",
                ],
            },
            {
                "existing": True, "id": 'tr085-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Google Account',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Google Account Help: Turn on 2-Step Verification (computer)', 'url': 'https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}, {'title': 'Google Account Help: How to recover your Google Account or Gmail', 'url': 'https://support.google.com/accounts/answer/7682439?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I make my email account more secure',
                    'Good question. Which email do you use, for example **Gmail**? And are you on a **computer** or a **phone**?',
                    'Gmail, on my computer',
                    """Thanks. A strong next step for Gmail is turning on 2-Step Verification.

2-Step Verification adds a second check when you sign in, so a password alone isn't enough to get into your account. Setting it up takes about five minutes.

1. Go to **myaccount.google.com** and sign in.
2. Click **Security & sign-in**.
3. Under **How you sign in to Google**, click **Turn on 2-Step Verification**.
4. Follow the steps on the screen.

After it's on, Google may ask you to confirm with your phone when you sign in on a new device.

**Never share these codes with anyone**, even if they say they're from Google.

If you use a work or school account, your administrator may control this setting.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-086', "task_type": 'phishing_email', "task": 'Is this email asking me to log in real?',
        "platform": 'email', "category": 'online_services', "sensitive": True,
        "source": {"title": 'FTC Consumer Advice: How To Recognize and Avoid Phishing Scams', "url": 'https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams'},
        "examples": [
            {
                "existing": True, "id": 'tr086-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'email',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: How To Recognize and Avoid Phishing Scams', 'url': 'https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams', 'accessed': '2026-10-24'}],
                "messages": [
                    "I got an email that looks like it's from my bank saying my account is locked and I need to click a link to log in and fix it. Is it real?",
                    """Please **don't click the link**. This is a common type of scam called phishing. These emails often look real, even with the bank's logo, but the link can lead to a fake website that steals your password.

**Warning signs:**
- It says your account is **locked** or has a **problem**.
- It pushes you to **click a link** or update your information.
- It uses a **general greeting** like "Dear Customer" instead of your name.

**What to do:**
1. **Don't click** any links or open attachments in the email.
2. To check your account, call your bank using the number on the **back of your card**, or go to the bank's website by typing the address yourself.
3. Forward the email to **reportphishing@apwg.org**, and report it at **ReportFraud.ftc.gov**.
4. Delete the email.

If you already clicked and typed your password, call your bank right away and change your password.""",
                ],
            },
            {
                "existing": True, "id": 'tr086-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: How To Recognize and Avoid Phishing Scams', 'url': 'https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams', 'accessed': '2026-10-24'}],
                "messages": [
                    'I got a weird email, should I click on it?',
                    "Good thinking to check first. Please don't click anything yet. **Who does the email say it's from, and what is it asking you to do?**",
                ],
            },
            {
                "existing": True, "id": 'tr086-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'FTC Consumer Advice: How To Recognize and Avoid Phishing Scams', 'url': 'https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams', 'accessed': '2026-10-24'}],
                "messages": [
                    'is this email from',
                    "It looks like your message got cut off. **Who does the email say it's from?** And please don't click any links in it until we check.",
                ],
            },
            {
                "existing": True, "id": 'tr086-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'email',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: How To Recognize and Avoid Phishing Scams', 'url': 'https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams', 'accessed': '2026-10-24'}],
                "messages": [
                    'I got a weird email, should I click on it?',
                    "Good thinking to check first. Please don't click anything yet. **Who does the email say it's from, and what is it asking you to do?**",
                    "It says it's from my bank and my account is locked, and there's a link to log in.",
                    """Thank you. That's a very common scam pattern.

Please **don't click the link**. This is a common type of scam called phishing. These emails often look real, even with the bank's logo, but the link can lead to a fake website that steals your password.

**Warning signs:**
- It says your account is **locked** or has a **problem**.
- It pushes you to **click a link** or update your information.
- It uses a **general greeting** like "Dear Customer" instead of your name.

**What to do:**
1. **Don't click** any links or open attachments in the email.
2. To check your account, call your bank using the number on the **back of your card**, or go to the bank's website by typing the address yourself.
3. Forward the email to **reportphishing@apwg.org**, and report it at **ReportFraud.ftc.gov**.
4. Delete the email.

If you already clicked and typed your password, call your bank right away and change your password.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-087', "task_type": 'report_spam_text', "task": 'Report a spam text message',
        "platform": 'phone', "category": 'online_services', "sensitive": True,
        "source": {"title": 'FTC Consumer Advice: How to Recognize and Report Spam Text Messages', "url": 'https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages'},
        "examples": [
            {
                "existing": True, "id": 'tr087-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'phone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: How to Recognize and Report Spam Text Messages', 'url': 'https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages', 'accessed': '2026-10-24'}],
                "messages": [
                    'I keep getting spam text messages. How do I report them?',
                    """Reporting spam texts helps your phone company block similar messages. Here's how.

1. **Use your phone's report option.** Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.
2. **Or forward it to 7726.** Copy the message and send it to **7726** (it spells SPAM on the keypad). Your phone company uses these reports.
3. **Report it to the FTC** at **ReportFraud.ftc.gov** if it's a scam.

Then delete the text.

**While you're at it:**
- **Don't click links** in unexpected texts.
- **Don't reply** with any personal information.
- **Never send** passwords, account numbers, or your Social Security number by text.""",
                ],
            },
            {
                "existing": True, "id": 'tr087-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: How to Recognize and Report Spam Text Messages', 'url': 'https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages', 'accessed': '2026-10-24'}],
                "messages": [
                    'what do I do about junk texts',
                    'There are a couple of things you can do. Would you like to **report** them, **block** the sender, or both? And is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr087-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'phone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'FTC Consumer Advice: How to Recognize and Report Spam Text Messages', 'url': 'https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages', 'accessed': '2026-10-24'}],
                "messages": [
                    'Every few days I get a text saying my toll bill is overdue or my account needs verifying. I never click them but I want to do something so they stop.',
                    """Good for you for not clicking. Reporting them helps your phone company block more of these:

Reporting spam texts helps your phone company block similar messages. Here's how.

1. **Use your phone's report option.** Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.
2. **Or forward it to 7726.** Copy the message and send it to **7726** (it spells SPAM on the keypad). Your phone company uses these reports.
3. **Report it to the FTC** at **ReportFraud.ftc.gov** if it's a scam.

Then delete the text.

**While you're at it:**
- **Don't click links** in unexpected texts.
- **Don't reply** with any personal information.
- **Never send** passwords, account numbers, or your Social Security number by text.""",
                ],
            },
            {
                "existing": True, "id": 'tr087-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'phone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: How to Recognize and Report Spam Text Messages', 'url': 'https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages', 'accessed': '2026-10-24'}],
                "messages": [
                    'what do I do about junk texts',
                    'There are a couple of things you can do. Would you like to **report** them, **block** the sender, or both? And is your phone an **iPhone** or an **Android** phone?',
                    'I want to report them. Android phone.',
                    """Thanks. Reporting is a great idea.

Reporting spam texts helps your phone company block similar messages. Here's how.

1. **Use your phone's report option.** Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.
2. **Or forward it to 7726.** Copy the message and send it to **7726** (it spells SPAM on the keypad). Your phone company uses these reports.
3. **Report it to the FTC** at **ReportFraud.ftc.gov** if it's a scam.

Then delete the text.

**While you're at it:**
- **Don't click links** in unexpected texts.
- **Don't reply** with any personal information.
- **Never send** passwords, account numbers, or your Social Security number by text.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-088', "task_type": 'romance_scam', "task": 'Online friend asks for money',
        "platform": 'any', "category": 'online_services', "sensitive": True,
        "source": {"title": 'FTC Consumer Advice: What To Know About Romance Scams', "url": 'https://consumer.ftc.gov/articles/what-know-about-romance-scams'},
        "examples": [
            {
                "existing": True, "id": 'tr088-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft', "reviewed": True, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: What To Know About Romance Scams', 'url': 'https://consumer.ftc.gov/articles/what-know-about-romance-scams', 'accessed': '2026-10-24'}],
                "messages": [
                    'I met a man online three months ago. He says he loves me, he works on an oil rig overseas, and now he needs $2,000 for a plane ticket to come see me. Should I send it?',
                    """I'm glad you asked before sending anything. Please **don't send the money**. What you're describing matches a very common scam called a **romance scam**.

**Warning signs:**
- The person can't meet in person, often saying they work far away, like on an **oil rig** or in the military.
- Strong feelings grow quickly through lots of messages.
- Now there's a **need for money**, like travel costs or an emergency.

**What to do:**
1. **Don't send money or gift cards** to someone you haven't met in person.
2. **Talk to a friend or family member** you trust. People close to you can often spot things that are hard to see from the inside.
3. You can **search his photo** online to see if it appears under other names. I can show you how.
4. If it's a scam, stop contact and report it at **ReportFraud.ftc.gov** and to the website or app where you met.

If you've already sent money, contact your bank or the payment company right away and ask for a refund.""",
                ],
            },
            {
                "existing": True, "id": 'tr088-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: What To Know About Romance Scams', 'url': 'https://consumer.ftc.gov/articles/what-know-about-romance-scams', 'accessed': '2026-10-24'}],
                "messages": [
                    'my online friend needs money for an emergency, should I help?',
                    "I'm glad you asked first. A couple of questions will help me give you good advice: **Have you met this person in person?** And **how are they asking you to send the money?**",
                ],
            },
            {
                "existing": True, "id": 'tr088-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'FTC Consumer Advice: What To Know About Romance Scams', 'url': 'https://consumer.ftc.gov/articles/what-know-about-romance-scams', 'accessed': '2026-10-24'}],
                "messages": [
                    "I've been talking to someone special online and he's asking me for help. I don't know what to do.",
                    'Thank you for trusting me with this. **What kind of help is he asking for?** And have the two of you met in person?',
                ],
            },
            {
                "existing": True, "id": 'tr088-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: What To Know About Romance Scams', 'url': 'https://consumer.ftc.gov/articles/what-know-about-romance-scams', 'accessed': '2026-10-24'}],
                "messages": [
                    'my online friend needs money for an emergency, should I help?',
                    "I'm glad you asked first. A couple of questions will help me give you good advice: **Have you met this person in person?** And **how are they asking you to send the money?**",
                    "No, we've only talked online for three months. He wants me to wire $2,000 for a plane ticket.",
                    """Thank you for telling me.

I'm glad you asked before sending anything. Please **don't send the money**. What you're describing matches a very common scam called a **romance scam**.

**Warning signs:**
- The person can't meet in person, often saying they work far away, like on an **oil rig** or in the military.
- Strong feelings grow quickly through lots of messages.
- Now there's a **need for money**, like travel costs or an emergency.

**What to do:**
1. **Don't send money or gift cards** to someone you haven't met in person.
2. **Talk to a friend or family member** you trust. People close to you can often spot things that are hard to see from the inside.
3. You can **search his photo** online to see if it appears under other names. I can show you how.
4. If it's a scam, stop contact and report it at **ReportFraud.ftc.gov** and to the website or app where you met.

If you've already sent money, contact your bank or the payment company right away and ask for a refund.""",
                ],
            },
        ],
    },
]
