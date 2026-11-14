"""Existing English drafts, group 2. Exported by export_spec.py; ids and provenance preserved."""
TASKS = [
    {
        "task_id": 'TR-014', "task_type": 'family_emergency_scam', "task": 'Caller claims to be grandchild needing gift cards',
        "platform": 'any', "category": 'online_services', "sensitive": True,
        "source": {"title": 'FTC: Talking Turkey (family emergency scams)', "url": 'https://www.ftc.gov/node/54353'},
        "examples": [
            {
                "existing": True, "id": 'pilot-014', "suffix": 'p', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC: Talking Turkey (family emergency scams)', 'url': 'https://www.ftc.gov/node/54353', 'accessed': '2026-10-24'}, {'title': 'FTC Consumer Alert: A way to spot scams: how someone asks you to pay', 'url': 'https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay', 'accessed': '2026-10-24'}],
                "messages": [
                    'My grandson just called crying. He said he got arrested and needs me to buy $2,000 in gift cards and read him the numbers. He said not to tell his mom. What should I do?',
                    """I'm sorry, that must have been frightening. Please **don't buy the gift cards yet**. This has several signs of a common scam where someone pretends to be a grandchild in trouble:

- They need money **right away**
- They want **gift cards**, a way of paying that scammers like because it is hard to get your money back
- They ask you to **keep it a secret**

Here's what to do:

1. Don't buy anything right away. Resist the urge to act immediately, no matter how dramatic the story may be.
2. Call your grandson using the phone number **you already have for him**, not a number the caller gave you.
3. Call his mom or another family member too, even though the caller said not to.

If it really was him, your family can help sort it out. If it was a scammer, you can report it at **www.ftc.gov/complaint**.

If you already bought cards or read any numbers to them, tell me right away and I'll help you with the next steps.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-015', "task_type": 'verification_code_scam', "task": 'Stranger asks for a verification code',
        "platform": 'any', "category": 'online_services', "sensitive": True,
        "source": {"title": 'FTC Consumer Advice: Verification code scams', "url": 'https://consumer.ftc.gov/node/84809'},
        "examples": [
            {
                "existing": True, "id": 'pilot-015', "suffix": 'p', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: Verification code scams', 'url': 'https://consumer.ftc.gov/node/84809', 'accessed': '2026-10-24'}],
                "messages": [
                    "Someone texted me saying they sent me a code by mistake and asked me to send it back. It's a 6-digit number from my bank. Should I just send it to them?",
                    """**No, please don't send it.** That code is only meant for you to log in to your account. Anyone who asks you for it is trying to get into your account, even if their message sounds friendly.

Here's what to do:

1. Don't reply to the text.
2. Block their number and stop texting them.
3. If you're worried about your account, call your bank using a phone number from your bank statement or your bank's app. Don't use any number from the text.
4. You can report the text at **ReportFraud.ftc.gov**.

If you already sent the code, contact your bank using a phone number from your bank statement or your bank's app.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-016', "task_type": 'online_payment_safety', "task": 'Is it safe to pay online?',
        "platform": 'any', "category": 'online_services', "sensitive": True,
        "source": {"title": 'FTC Consumer Alert: A way to spot scams: how someone asks you to pay', "url": 'https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay'},
        "examples": [
            {
                "existing": True, "id": 'pilot-016', "suffix": 'p', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Alert: A way to spot scams: how someone asks you to pay', 'url': 'https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay', 'accessed': '2026-10-24'}, {'title': 'FTC Consumer Advice: Online Shopping', 'url': 'https://consumer.ftc.gov/articles/online-shopping', 'accessed': '2026-10-24'}],
                "messages": [
                    'is it safe to pay for something online?',
                    """Yes, it can be safe if you pay the right way. Paying by **credit card** is best, because it protects you and your money if it turns out to be a scam or if something else goes wrong.

1. Pay by credit card when you can. If a charge is wrong, you can dispute it. Call your card company right away, and send a letter so it reaches them within 60 days of the date the first bill showing the error was mailed.
2. Don't buy from a seller who insists you can only pay with **gift cards, wire transfers, payment apps, or cryptocurrency**. Scammers like those ways of paying because it is hard to get your money back.
3. Look for **https** at the start of the website address. The "s" only means the connection is encrypted. Scammers can use it too, so it doesn't prove the seller is honest.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-017', "task_type": 'social_media_privacy', "task": 'Stop strangers seeing Facebook posts',
        "platform": 'Facebook', "category": 'communication', "sensitive": True,
        "source": {"title": 'Facebook Help Center: Choose who can see your post on Facebook', "url": 'https://www.facebook.com/help/120939471321735'},
        "examples": [
            {
                "existing": True, "id": 'pilot-017', "suffix": 'p', "scenario": 'missing_info',
                "style": 'plain', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Facebook Help Center: Choose who can see your post on Facebook', 'url': 'https://www.facebook.com/help/120939471321735', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I stop strangers from seeing my facebook posts',
                    """That's a smart thing to set up. The buttons are in different places depending on how you use Facebook.

**Do you use Facebook on a phone (the Facebook app) or on a computer?**""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-021', "task_type": 'text_size', "task": 'Make text bigger',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Change the font size on your iPhone, iPad, and iPod touch', "url": 'https://support.apple.com/en-us/102453'},
        "examples": [
            {
                "existing": True, "id": 'tr021-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Change the font size on your iPhone, iPad, and iPod touch', 'url': 'https://support.apple.com/en-us/102453', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I make the text bigger on my iPhone? Everything is too small to read.',
                    """You can make the text bigger in Settings. It takes about a minute, and you can change it back anytime.

1. Open the **Settings** app.
2. Tap **Display & Brightness**.
3. Tap **Text Size**.
4. Drag the slider to the right. Stop when the text is easy to read.

If you need it even bigger, go to **Settings**, then **Accessibility**, then **Display & Text Size**, then **Larger Text**, and drag that slider. Very large text can make some buttons harder to tap, so slide it back a little if that happens.""",
                ],
            },
            {
                "existing": True, "id": 'tr021-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Change the font size on your iPhone, iPad, and iPod touch', 'url': 'https://support.apple.com/en-us/102453', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I make the letters bigger on my phone',
                    'I can help with that. Is your phone an **iPhone**, or another kind of phone like a Samsung or Google Pixel?',
                ],
            },
            {
                "existing": True, "id": 'tr021-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Change the font size on your iPhone, iPad, and iPod touch', 'url': 'https://support.apple.com/en-us/102453', 'accessed': '2026-10-24'}],
                "messages": [
                    'the words on my iphone are too',
                    'It looks like your message got cut off. Do you mean the words are too **small** to read? If so, I can show you how to make them bigger.',
                ],
            },
            {
                "existing": True, "id": 'tr021-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Change the font size on your iPhone, iPad, and iPod touch', 'url': 'https://support.apple.com/en-us/102453', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I make the letters bigger on my phone',
                    'I can help with that. Is your phone an **iPhone**, or another kind of phone like a Samsung or Google Pixel?',
                    "It's an iPhone.",
                    """Great, thanks.

You can make the text bigger in Settings. It takes about a minute, and you can change it back anytime.

1. Open the **Settings** app.
2. Tap **Display & Brightness**.
3. Tap **Text Size**.
4. Drag the slider to the right. Stop when the text is easy to read.

If you need it even bigger, go to **Settings**, then **Accessibility**, then **Display & Text Size**, then **Larger Text**, and drag that slider. Very large text can make some buttons harder to tap, so slide it back a little if that happens.""",
                ],
            },
            {
                "existing": True, "id": 'tr021-r', "suffix": 'r', "scenario": 'failure_recovery',
                "style": 'failure_recovery', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": True, "inspired_by": 'original',
                "sources": [{'title': 'Apple Support: Change the font size on your iPhone, iPad, and iPod touch', 'url': 'https://support.apple.com/en-us/102453', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I make the text bigger on my iPhone? Everything is too small to read.',
                    """You can make the text bigger in Settings. It takes about a minute, and you can change it back anytime.

1. Open the **Settings** app. Its icon is a gray gear.
2. Tap **Display & Brightness**.
3. Tap **Text Size**.
4. Drag the slider at the bottom of the screen to the right.

The sample text changes as you drag, so you can stop when it's easy to read.

If you need it even bigger, go to **Settings**, then **Accessibility**, then **Display & Text Size**, then **Larger Text**, and drag that slider. Very large text can make some buttons harder to tap, so slide it back a little if that happens.""",
                    'I made it really big and now some of the buttons are cut off and hard to tap.',
                    """That can happen when the text is set very large. Let's make it a little smaller so the buttons fit again.

1. Open **Settings**.
2. Tap **Display & Brightness**.
3. Tap **Text Size**.
4. Drag the slider **one step to the left**.
5. Go back to the app and check the buttons.

If you made the text bigger with **Larger Text** instead, the slider is in **Settings**, then **Accessibility**, then **Display & Text Size**, then **Larger Text**.

Repeat until the buttons fit on the screen and the text is still easy for you to read.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-022', "task_type": 'text_size', "task": 'Make text bigger',
        "platform": 'Android (Pixel)', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Accessibility Help: Change text & display settings', "url": 'https://support.google.com/accessibility/android/answer/11183305?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr022-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android (Pixel)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: Change text & display settings', 'url': 'https://support.google.com/accessibility/android/answer/11183305?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'I have a Google Pixel phone. How can I make the writing on the screen larger?',
                    """You can make the writing larger in Settings. It takes about a minute.

1. Open the **Settings** app.
2. Search for **Font size** in Settings.
3. Tap **Font size**.
4. Move the slider toward the larger end until the text is easy to read.

A few apps ignore this setting, so text in those apps may stay the same size.

If you can't find **Font size**, tell me what you see after searching and I'll help you find it.""",
                ],
            },
            {
                "existing": True, "id": 'tr022-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: Change text & display settings', 'url': 'https://support.google.com/accessibility/android/answer/11183305?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'my phone screen writing is too small',
                    'I can help you make it bigger. What kind of phone do you have, an **iPhone** or an Android phone like a Samsung or Google Pixel?',
                ],
            },
            {
                "existing": True, "id": 'tr022-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'Android (Pixel)',
                "author": 'claude-draft, edited by Ryan Hsieh', "reviewed": True, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Accessibility Help: Change text & display settings', 'url': 'https://support.google.com/accessibility/android/answer/11183305?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "My daughter gave me her old Google Pixel when she got a new phone. It works fine but I can't read anything without my glasses and I always forget where I put them. Is there a way to make the letters on the screen bigger?",
                    """Yes. You can make the writing larger in Settings. It takes about a minute.

1. Open the **Settings** app.
2. Tap the search bar at the top of Settings.
3. Type **Font size**.
4. Tap **Font size** in the results.
5. Move the slider toward the larger end until the text is easy to read.

The change happens right away. A few apps ignore this setting, so text in those apps may stay the same size.

If you can't find **Font size**, tell me what you see after searching and I'll help you find it.""",
                ],
            },
            {
                "existing": True, "id": 'tr022-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android (Pixel)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: Change text & display settings', 'url': 'https://support.google.com/accessibility/android/answer/11183305?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'my phone screen writing is too small',
                    'I can help you make it bigger. What kind of phone do you have, an **iPhone** or an Android phone like a Samsung or Google Pixel?',
                    'Google Pixel 8',
                    """Thanks.

You can make the writing larger in Settings. It takes about a minute.

1. Open the **Settings** app.
2. Search for **Font size** in Settings.
3. Tap **Font size**.
4. Move the slider toward the larger end until the text is easy to read.

A few apps ignore this setting, so text in those apps may stay the same size.

If you can't find **Font size**, tell me what you see after searching and I'll help you find it.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-024', "task_type": 'ring_volume', "task": 'Turn up ringer volume',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Use the volume buttons, side button, and other controls on your iPhone', "url": 'https://support.apple.com/en-us/105103'},
        "examples": [
            {
                "existing": True, "id": 'tr024-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use the volume buttons, side button, and other controls on your iPhone', 'url': 'https://support.apple.com/en-us/105103', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I make my iPhone ring louder when someone calls?',
                    """Here is a quick way to do it. It takes less than a minute.

1. Go to your Home Screen so you're not inside an app.
2. Press the **volume up** button a few times. When you are not using other apps, the buttons change the ringer volume.

If your phone still only vibrates, it may be in Silent mode. Tell me and I'll show you how to check.""",
                ],
            },
            {
                "existing": True, "id": 'tr024-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use the volume buttons, side button, and other controls on your iPhone', 'url': 'https://support.apple.com/en-us/105103', 'accessed': '2026-10-24'}, {'title': 'Apple Support: How to set and change alarms on your iPhone', 'url': 'https://support.apple.com/en-us/118444', 'accessed': '2026-10-24'}],
                "messages": [
                    'My phone is too quiet when it rings.',
                    "Let's fix that so you don't miss calls. Is your phone an **iPhone**, or another kind of phone like a Samsung or Google Pixel?",
                ],
            },
            {
                "existing": True, "id": 'tr024-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Use the volume buttons, side button, and other controls on your iPhone', 'url': 'https://support.apple.com/en-us/105103', 'accessed': '2026-10-24'}],
                "messages": [
                    "I keep missing calls from my son because I don't hear my iPhone ring when I'm in the kitchen cooking. He gets worried. Can I make the ringing louder?",
                    """Yes, you can, and that should help your son reach you.

Here is a quick way to do it. It takes less than a minute.

1. Go to your Home Screen so you're not inside an app.
2. Press the **volume up** button a few times. When you are not using other apps, the buttons change the ringer volume.

If your phone still only vibrates, it may be in Silent mode. Tell me and I'll show you how to check.""",
                ],
            },
            {
                "existing": True, "id": 'tr024-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use the volume buttons, side button, and other controls on your iPhone', 'url': 'https://support.apple.com/en-us/105103', 'accessed': '2026-10-24'}],
                "messages": [
                    'My phone is too quiet when it rings.',
                    "Let's fix that so you don't miss calls. Is your phone an **iPhone**, or another kind of phone like a Samsung or Google Pixel?",
                    'iPhone 13',
                    """Thanks. Here's how on your iPhone. It takes less than a minute.

1. Go to your Home Screen so you're not inside an app.
2. Press the **volume up** button a few times. When you are not using other apps, the buttons change the ringer volume.

If your phone still only vibrates, it may be in Silent mode. Tell me and I'll show you how to check.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-025', "task_type": 'ring_volume', "task": 'Turn up ring volume',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Change volume, sound & vibrate settings', "url": 'https://support.google.com/android/answer/9082609?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr025-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Change volume, sound & vibrate settings', 'url': 'https://support.google.com/android/answer/9082609?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I turn up the ringer on my Android phone?',
                    """You can do this with the volume buttons. It takes a few seconds.

1. Press a **volume button**.
2. At the right, tap the **Menu** icon, also called **More**.
3. Drag the **Ring Volume** slider to the right.

Some of these steps work only on Android 12 and up. On older versions of Android, tap the **down arrow** at the right and use the **Ring** slider.

If neither of these matches what you see, tell me and I'll help you find it.""",
                ],
            },
            {
                "existing": True, "id": 'tr025-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Change volume, sound & vibrate settings', 'url': 'https://support.google.com/android/answer/9082609?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I make the ringing louder',
                    'Happy to help. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?',
                ],
            },
            {
                "existing": True, "id": 'tr025-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'incomplete', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Help: Change volume, sound & vibrate settings', 'url': 'https://support.google.com/android/answer/9082609?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'ringer volume on my android',
                    """Here's how to change the ringer volume on your Android phone.

1. Press a **volume button**.
2. At the right, tap the **Menu** icon, also called **More**.
3. Slide the **Ring Volume** slider to the right for louder, or to the left for quieter.

Some of these steps work only on Android 12 and up. On older versions of Android, tap the **down arrow** at the right, choose **Ring**, and slide it the same way.""",
                ],
            },
            {
                "existing": True, "id": 'tr025-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Change volume, sound & vibrate settings', 'url': 'https://support.google.com/android/answer/9082609?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I make the ringing louder',
                    'Happy to help. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?',
                    "android, it's a samsung",
                    """Thanks. Phone screens can look a little different, so here is what to look for.

You can do this with the volume buttons. It takes a few seconds.

1. Press a **volume button**.
2. At the right, tap the **Menu** icon, also called **More**.
3. Drag the **Ring Volume** slider to the right.

Some of these steps work only on Android 12 and up. On older versions of Android, tap the **down arrow** at the right and use the **Ring** slider.

If neither of these matches what you see, tell me and I'll help you find it.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-026', "task_type": 'wifi_calling', "task": 'Turn on Wi-Fi Calling',
        "platform": 'iPhone', "category": 'communication', "sensitive": False,
        "source": {"title": 'Apple Support: Make a call with Wi-Fi Calling', "url": 'https://support.apple.com/en-us/108066'},
        "examples": [
            {
                "existing": True, "id": 'tr026-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Make a call with Wi-Fi Calling', 'url': 'https://support.apple.com/en-us/108066', 'accessed': '2026-10-24'}],
                "messages": [
                    'My iPhone has no signal in my basement apartment but I have Wi-Fi. Can I make calls using the Wi-Fi?',
                    """iPhone has a feature called **Wi-Fi Calling** that lets you make calls over Wi-Fi when there is little or no cellular coverage. Turning it on takes about a minute.

1. Open the **Settings** app.
2. Tap **Cellular**.
3. Tap **Wi-Fi Calling**.
4. Turn on **Wi-Fi Calling on This iPhone**.
5. Tap **Enable** when asked.

Your iPhone may ask you to enter or confirm your address. This address is used for emergency services, so please enter it carefully.

Wi-Fi Calling only works if your phone company offers it. To see that it's working, open Control Center. If Wi-Fi Calling is available, you'll see **Wi-Fi** in the status bar there. Then you make calls the same way you always do.

If you don't see **Wi-Fi Calling** in that menu, your phone company may not offer it. Tell me what you see, and you can also ask your phone company.""",
                ],
            },
            {
                "existing": True, "id": 'tr026-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Make a call with Wi-Fi Calling', 'url': 'https://support.apple.com/en-us/108066', 'accessed': '2026-10-24'}],
                "messages": [
                    'calls keep dropping in my house, what can I do',
                    "That's frustrating. Is your phone an **iPhone** or an Android phone?",
                ],
            },
            {
                "existing": True, "id": 'tr026-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'over_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Make a call with Wi-Fi Calling', 'url': 'https://support.apple.com/en-us/108066', 'accessed': '2026-10-24'}],
                "messages": [
                    'I have an iPhone 15 on Verizon, iOS 18. Cell signal inside my house is one bar but Wi-Fi is strong. I read about Wi-Fi Calling. Where is the setting?',
                    """It's in Settings.

1. Open the **Settings** app.
2. Tap **Cellular**.
3. Tap **Wi-Fi Calling**.
4. Turn on **Wi-Fi Calling on This iPhone**.
5. Tap **Enable** when asked.

Your iPhone may ask you to enter or confirm your address. This address is used for emergency services, so please enter it carefully.

Wi-Fi Calling only works if your phone company offers it. To see that it's working, open Control Center. If Wi-Fi Calling is available, you'll see **Wi-Fi** in the status bar there. Then you make calls the same way you always do.

If you don't see **Wi-Fi Calling** in that menu, your phone company may not offer it. Tell me what you see, and you can also ask your phone company.""",
                ],
            },
            {
                "existing": True, "id": 'tr026-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Make a call with Wi-Fi Calling', 'url': 'https://support.apple.com/en-us/108066', 'accessed': '2026-10-24'}],
                "messages": [
                    'calls keep dropping in my house, what can I do',
                    "That's frustrating. Is your phone an **iPhone** or an Android phone?",
                    "It's an iPhone 12.",
                    """Thanks. This should help.

iPhone has a feature called **Wi-Fi Calling** that lets you make calls over Wi-Fi when there is little or no cellular coverage. Turning it on takes about a minute.

1. Open the **Settings** app.
2. Tap **Cellular**.
3. Tap **Wi-Fi Calling**.
4. Turn on **Wi-Fi Calling on This iPhone**.
5. Tap **Enable** when asked.

Your iPhone may ask you to enter or confirm your address. This address is used for emergency services, so please enter it carefully.

Wi-Fi Calling only works if your phone company offers it. To see that it's working, open Control Center. If Wi-Fi Calling is available, you'll see **Wi-Fi** in the status bar there. Then you make calls the same way you always do.

If you don't see **Wi-Fi Calling** in that menu, your phone company may not offer it. Tell me what you see, and you can also ask your phone company.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-027', "task_type": 'screenshot', "task": 'Take a screenshot',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Take a screenshot or record your screen', "url": 'https://support.google.com/android/answer/9075928?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr027-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Take a screenshot or record your screen', 'url': 'https://support.google.com/android/answer/9075928?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I take a screenshot on my Android phone?',
                    """Here's how to take a picture of your screen. It only takes a second.

1. Get the screen showing what you want to capture.
2. Press the **Power** button and the **Volume Down** button **at the same time**, then let go.

You'll see a small preview of the screenshot in the bottom-left corner.

**To find it later:** open the **Photos** app, tap **Collections** at the bottom, then **On this device**, then **Screenshots**. If your phone uses a **Gallery** app instead, look for the **Screenshots** album there.

If pressing both buttons doesn't work, hold the **Power** button for a few seconds and tap **Screenshot**.""",
                ],
            },
            {
                "existing": True, "id": 'tr027-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Take a screenshot or record your screen', 'url': 'https://support.google.com/android/answer/9075928?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do i take a screenshot',
                    'Sure. The buttons are different depending on the phone. Is yours an **iPhone** or an **Android** phone, like Samsung or Google Pixel?',
                ],
            },
            {
                "existing": True, "id": 'tr027-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": True, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Help: Take a screenshot or record your screen', 'url': 'https://support.google.com/android/answer/9075928?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "My grandson is helping me with my phone over the phone and he keeps saying send me a screenshot so he can see what I see. I don't know what that is or how to do it.",
                    """A screenshot is a picture of exactly what's on your screen, so your grandson can see it too. The buttons to take one depend on your phone.

**Is your phone an iPhone or an Android phone** (like Samsung or Google Pixel)? If you're not sure, an iPhone has an apple logo on the back.""",
                ],
            },
            {
                "existing": True, "id": 'tr027-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Take a screenshot or record your screen', 'url': 'https://support.google.com/android/answer/9075928?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do i take a screenshot',
                    'Sure. The buttons are different depending on the phone. Is yours an **iPhone** or an **Android** phone, like Samsung or Google Pixel?',
                    'Android. Motorola.',
                    """Thanks. Here's how to take a picture of your screen on your Motorola. It only takes a second.

1. Get the screen showing what you want to capture.
2. Press the **Power** button and the **Volume Down** button **at the same time**, then let go.

You'll see a small preview of the screenshot in the bottom-left corner.

**To find it later:** open the **Photos** app, tap **Collections** at the bottom, then **On this device**, then **Screenshots**. If your phone uses a **Gallery** app instead, open it, tap **Album view**, then tap **Screenshots folder**.

If pressing both buttons doesn't work, hold the **Power** button for a few seconds and tap **Screenshot**.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-028', "task_type": 'screenshot', "task": 'Take a screenshot',
        "platform": 'Windows 11', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Microsoft Support: Use Snipping Tool to capture screenshots', "url": 'https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots'},
        "examples": [
            {
                "existing": True, "id": 'tr028-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Use Snipping Tool to capture screenshots', 'url': 'https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I take a screenshot on my Windows 11 laptop?',
                    """The quickest way uses three keys at once. It takes a few seconds.

1. Press and hold the **Windows logo key** and the **Shift** key, then press **S**.
2. The screen dims and shows a few capture choices.
3. Choose the shape you want: a rectangle, a window, or the full screen.
4. If you chose rectangle, click and drag over the part of the screen you want.

Your screenshot is saved automatically in your **Screenshots** folder.

**Another option:** press the **Print Screen** key (often labeled **PrtSc**). This copies the whole screen, but it isn't saved as a file until you paste it somewhere, like an email.""",
                ],
            },
            {
                "existing": True, "id": 'tr028-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Use Snipping Tool to capture screenshots', 'url': 'https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I take a picture of my computer screen',
                    "Happy to help. Is your computer a **Windows** computer or a **Mac**? If you're not sure, a Windows keyboard usually has a key with the Windows logo near the bottom left.",
                ],
            },
            {
                "existing": True, "id": 'tr028-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'incomplete', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Use Snipping Tool to capture screenshots', 'url': 'https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots', 'accessed': '2026-10-24'}],
                "messages": [
                    'screenshot on windows',
                    """Here's how to take a screenshot on Windows 11:

The quickest way uses three keys at once. It takes a few seconds.

1. Press and hold the **Windows logo key** and the **Shift** key, then press **S**.
2. The screen dims and shows a few capture choices.
3. Choose the shape you want: a rectangle, a window, or the full screen.
4. If you chose rectangle, click and drag over the part of the screen you want.

Your screenshot is saved automatically in your **Screenshots** folder.

**Another option:** press the **Print Screen** key (often labeled **PrtSc**). This copies the whole screen, but it isn't saved as a file until you paste it somewhere, like an email.""",
                ],
            },
            {
                "existing": True, "id": 'tr028-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Use Snipping Tool to capture screenshots', 'url': 'https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I take a picture of my computer screen',
                    "Happy to help. Is your computer a **Windows** computer or a **Mac**? If you're not sure, a Windows keyboard usually has a key with the Windows logo near the bottom left.",
                    'Windows 11',
                    """Great, here's the easiest way on Windows 11.

The quickest way uses three keys at once. It takes a few seconds.

1. Press and hold the **Windows logo key** and the **Shift** key, then press **S**.
2. The screen dims and shows a few capture choices.
3. Choose the shape you want: a rectangle, a window, or the full screen.
4. If you chose rectangle, click and drag over the part of the screen you want.

Your screenshot is saved automatically in your **Screenshots** folder.

**Another option:** press the **Print Screen** key (often labeled **PrtSc**). This copies the whole screen, but it isn't saved as a file until you paste it somewhere, like an email.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-030', "task_type": 'wifi_connect', "task": 'Connect to a Wi-Fi network',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Connect to Wi-Fi networks on your Android device', "url": 'https://support.google.com/android/answer/9075847?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr030-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Connect to Wi-Fi networks on your Android device', 'url': 'https://support.google.com/android/answer/9075847?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I connect my Android phone to my Wi-Fi at home?',
                    """Here's how. Have your Wi-Fi password ready. It takes about two minutes.

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **Internet**.
4. Tap the name of your home network in the list. A lock icon means it needs a password.
5. If it asks for a password, type it.

When you're connected, the network is labeled **Saved**.

Some of these steps work only on Android 12 and up. Menu names can be a little different on some phones. If you don't see **Network & internet**, tell me what you see in Settings.""",
                ],
            },
            {
                "existing": True, "id": 'tr030-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Connect to Wi-Fi networks on your Android device', 'url': 'https://support.google.com/android/answer/9075847?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I get my phone on the wifi',
                    'I can walk you through it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?',
                ],
            },
            {
                "existing": True, "id": 'tr030-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'over_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Help: Connect to Wi-Fi networks on your Android device', 'url': 'https://support.google.com/android/answer/9075847?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "I have a Google Pixel 7 with Android 15. My new internet company's router has a sticker on the bottom with the network name HOME-4G7K and a password. How do I connect the phone to it?",
                    """The sticker on your router has what you need: the network name **HOME-4G7K** and the password.

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **Internet**.
4. Tap **HOME-4G7K** in the list. A lock icon means it needs a password.
5. If it asks for a password, type the password from the sticker.

When you're connected, the network is labeled **Saved**.

Some of these steps work only on Android 12 and up. Menu names can be a little different on some phones. If you don't see **Network & internet**, tell me what you see in Settings.""",
                ],
            },
            {
                "existing": True, "id": 'tr030-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Connect to Wi-Fi networks on your Android device', 'url': 'https://support.google.com/android/answer/9075847?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I get my phone on the wifi',
                    'I can walk you through it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?',
                    'Android',
                    """Thanks. Have your Wi-Fi password ready. It takes about two minutes.

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **Internet**.
4. Tap the name of your home network in the list. A lock icon means it needs a password.
5. If it asks for a password, type it.

When you're connected, the network is labeled **Saved**.

Some of these steps work only on Android 12 and up. Menu names can be a little different on some phones. If you don't see **Network & internet**, tell me what you see in Settings.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-031', "task_type": 'wifi_connect', "task": 'Connect to a Wi-Fi network',
        "platform": 'Windows 11', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Microsoft Support: Connect to a Wi-Fi network in Windows', "url": 'https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows'},
        "examples": [
            {
                "existing": True, "id": 'tr031-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft, edited by Ryan Hsieh', "reviewed": True, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Connect to a Wi-Fi network in Windows', 'url': 'https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I connect my Windows 11 laptop to Wi-Fi?',
                    """Here's how. Have your Wi-Fi password ready. This takes about two minutes.

1. On the taskbar at the bottom right of the screen, click the **network, sound, or battery icons**. A small panel opens.
2. Next to the Wi-Fi button, click the **arrow** for **Manage Wi-Fi connections**.
3. Click the name of your network.
4. Click **Connect**.
5. Type your Wi-Fi password.
6. Click **Next**.

When it's done, try opening a website to check that it works.

If you don't see your network in the list, click **Refresh network list** in the lower right of the panel and look again.""",
                ],
            },
            {
                "existing": True, "id": 'tr031-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Connect to a Wi-Fi network in Windows', 'url': 'https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do i connect my computer to the internet',
                    'I can help. Is your computer a **Windows** computer or a **Mac**?',
                ],
            },
            {
                "existing": True, "id": 'tr031-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Connect to a Wi-Fi network in Windows', 'url': 'https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows', 'accessed': '2026-10-24'}],
                "messages": [
                    'laptop wont connect to',
                    "It looks like your message got cut off. What won't your laptop connect to: the **Wi-Fi**, a **printer**, or something else?",
                ],
            },
            {
                "existing": True, "id": 'tr031-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Connect to a Wi-Fi network in Windows', 'url': 'https://support.microsoft.com/en-us/windows/experience/connectivity-networking/connect-to-a-wi-fi-network-in-windows', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do i connect my computer to the internet',
                    'I can help. Is your computer a **Windows** computer or a **Mac**?',
                    'Windows 11',
                    """Thanks. Have your Wi-Fi password ready. This takes about two minutes.

1. On the taskbar, click the **network, sound, or battery icons**. A small panel opens.
2. Next to the Wi-Fi button, click the **arrow** for **Manage Wi-Fi connections**.
3. Click the name of your network.
4. Click **Connect**.
5. Type your Wi-Fi password and click **Next**.

When it's done, try opening a website to check that it works.

If you don't see your network in the list, click **Refresh network list** in the lower right of the panel and look again.""",
                ],
            },
        ],
    },
]
