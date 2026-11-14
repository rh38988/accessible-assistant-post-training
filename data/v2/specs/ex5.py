"""Existing English drafts, group 5. Exported by export_spec.py; ids and provenance preserved."""
TASKS = [
    {
        "task_id": 'TR-062', "task_type": 'free_storage', "task": 'Free up storage space',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Free up storage on your Android device', "url": 'https://support.google.com/android/answer/7431795?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr062-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Free up storage on your Android device', 'url': 'https://support.google.com/android/answer/7431795?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I free up storage space on my Android phone?',
                    """Here's how to see what's using space and clear some out. It takes a few minutes.

1. Open the **Settings** app.
2. Tap **Storage**.
3. Tap **Free up space**.
4. Scroll to a category, then tap **Select files**. If you don't see the category, tap **Browse**.
5. Select the files you don't need.
6. Tap **Move files to Trash**.

**Other ways to save space:**
- If your photos are backed up in **Google Photos**, you can delete the copies on your phone. The backed-up copies stay safe in the app.
- Uninstall apps you don't use. You can reinstall them later without paying again.

Menu names vary between phones, and some of these steps need a newer version of Android. Tell me what you see if something doesn't match.""",
                ],
            },
            {
                "existing": True, "id": 'tr062-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Free up storage on your Android device', 'url': 'https://support.google.com/android/answer/7431795?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'phone says storage full',
                    'I can help you clear some space. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr062-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Help: Free up storage on your Android device', 'url': 'https://support.google.com/android/answer/7431795?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do i clear',
                    'It looks like your message got cut off. What would you like to clear: **storage space** on your phone, your **notifications**, or something else?',
                ],
            },
            {
                "existing": True, "id": 'tr062-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Free up storage on your Android device', 'url': 'https://support.google.com/android/answer/7431795?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'phone says storage full',
                    'I can help you clear some space. Is your phone an **iPhone** or an **Android** phone?',
                    'Android, Samsung',
                    """Thanks. Here's how to see what's using space and clear some out. It takes a few minutes.

1. Open the **Settings** app.
2. Tap **Storage**.
3. Tap **Free up space**.
4. Scroll to a category, then tap **Select files**. If you don't see the category, tap **Browse**.
5. Select the files you don't need.
6. Tap **Move files to Trash**.

**Other ways to save space:**
- If your photos are backed up in **Google Photos**, you can delete the copies on your phone. The backed-up copies stay safe in the app.
- Uninstall apps you don't use. You can reinstall them later without paying again.

Menu names vary between phones, and some of these steps need a newer version of Android. Tell me what you see if something doesn't match.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-063', "task_type": 'flashlight', "task": 'Turn on the flashlight',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro', "url": 'https://support.apple.com/en-us/105001'},
        "examples": [
            {
                "existing": True, "id": 'tr063-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro', 'url': 'https://support.apple.com/en-us/105001', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I turn on the flashlight on my iPhone?',
                    'There are a few quick ways.\n\n**From Control Center:**\n1. If your iPhone has Face ID (no Home button), **swipe down from the top-right corner** of the screen. If it has a Home button, **swipe up from the bottom edge**.\n2. Tap the **Flashlight** button.\n3. Tap it again to turn it off.\n\n**From the Lock Screen:** press and hold the **Flashlight** button in the bottom-left corner.\n\n**With Siri:** say "Hey Siri, turn on my flashlight."',
                ],
            },
            {
                "existing": True, "id": 'tr063-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro', 'url': 'https://support.apple.com/en-us/105001', 'accessed': '2026-10-24'}],
                "messages": [
                    'my phone is dark and I need some light, where is it',
                    'I can help with the flashlight. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr063-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro', 'url': 'https://support.apple.com/en-us/105001', 'accessed': '2026-10-24'}],
                "messages": [
                    "I was trying to find my keys in my purse last night and my husband said use your phone light but I couldn't figure out how.",
                    """Your phone has a flashlight, and it's handy for things like that.

**Is your phone an iPhone or an Android phone?** Then I'll show you the quickest way.""",
                ],
            },
            {
                "existing": True, "id": 'tr063-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro', 'url': 'https://support.apple.com/en-us/105001', 'accessed': '2026-10-24'}],
                "messages": [
                    'my phone is dark and I need some light, where is it',
                    'I can help with the flashlight. Is your phone an **iPhone** or an **Android** phone?',
                    'iPhone',
                    'Got it.\n\nThere are a few quick ways.\n\n**From Control Center:**\n1. If your iPhone has Face ID (no Home button), **swipe down from the top-right corner** of the screen. If it has a Home button, **swipe up from the bottom edge**.\n2. Tap the **Flashlight** button.\n3. Tap it again to turn it off.\n\n**From the Lock Screen:** press and hold the **Flashlight** button in the bottom-left corner.\n\n**With Siri:** say "Hey Siri, turn on my flashlight."',
                ],
            },
        ],
    },
    {
        "task_id": 'TR-064', "task_type": 'flashlight', "task": 'Turn on the flashlight',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Change settings quickly on your Android phone', "url": 'https://support.google.com/android/answer/9083864?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr064-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Change settings quickly on your Android phone', 'url': 'https://support.google.com/android/answer/9083864?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I turn on the flashlight on my Android phone?',
                    """Here's the quickest way.

1. **Swipe down** from the top of the screen. You'll see a few quick settings. Swipe down again to see all of them.
2. Tap **Flashlight**. A dimmed icon means it's off.
3. Tap it again to turn it off.

**If you don't see Flashlight:**
1. Swipe down twice from the top of the screen.
2. Tap the **edit** icon (a pencil).
3. Scroll down, find **Flashlight**, and tap **Add**.
4. Drag it to where you want it.""",
                ],
            },
            {
                "existing": True, "id": 'tr064-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Change settings quickly on your Android phone', 'url': 'https://support.google.com/android/answer/9083864?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'where is the flashlight',
                    'I can show you. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr064-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'over_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Help: Change settings quickly on your Android phone', 'url': 'https://support.google.com/android/answer/9083864?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "Samsung A15. I know it's somewhere in the pull-down menu but I only see Wi-Fi, Bluetooth, and a few others.",
                    """You're in the right place. Swipe down a second time to see more, and if it's still not there, you can add it:

Here's the quickest way.

1. **Swipe down** from the top of the screen. You'll see a few quick settings. Swipe down again to see all of them.
2. Tap **Flashlight**. A dimmed icon means it's off.
3. Tap it again to turn it off.

**If you don't see Flashlight:**
1. Swipe down twice from the top of the screen.
2. Tap the **edit** icon (a pencil).
3. Scroll down, find **Flashlight**, and tap **Add**.
4. Drag it to where you want it.""",
                ],
            },
            {
                "existing": True, "id": 'tr064-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Change settings quickly on your Android phone', 'url': 'https://support.google.com/android/answer/9083864?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'where is the flashlight',
                    'I can show you. Is your phone an **iPhone** or an **Android** phone?',
                    'Android',
                    """Thanks.

Here's the quickest way.

1. **Swipe down** from the top of the screen. You'll see a few quick settings. Swipe down again to see all of them.
2. Tap **Flashlight**. A dimmed icon means it's off.
3. Tap it again to turn it off.

**If you don't see Flashlight:**
1. Swipe down twice from the top of the screen.
2. Tap the **edit** icon (a pencil).
3. Scroll down, find **Flashlight**, and tap **Add**.
4. Drag it to where you want it.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-066', "task_type": 'alarm', "task": 'Set an alarm',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: How to set and change alarms on your iPhone', "url": 'https://support.apple.com/en-us/118444'},
        "examples": [
            {
                "existing": True, "id": 'tr066-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to set and change alarms on your iPhone', 'url': 'https://support.apple.com/en-us/118444', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I set an alarm on my iPhone for 6:30 in the morning?',
                    """Here's how. It takes about a minute.

1. Open the **Clock** app, then tap the **Alarms** tab.
2. Tap the **Add** button.
3. Set the time to **6:30 AM**.
4. Only if you want it to repeat, tap **Repeat** and choose the days.
5. Tap **Done**.

The alarm will ring even if your phone is on Silent or Do Not Disturb.

If the alarm is too quiet, go to **Settings**, then **Sounds & Haptics**, and drag the **Ringtone and Alerts** slider to the right. If it only vibrates, check that the alarm's **Sound** isn't set to **None**.""",
                ],
            },
            {
                "existing": True, "id": 'tr066-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to set and change alarms on your iPhone', 'url': 'https://support.apple.com/en-us/118444', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I set an alarm to wake me up',
                    'Sure. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr066-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: How to set and change alarms on your iPhone', 'url': 'https://support.apple.com/en-us/118444', 'accessed': '2026-10-24'}],
                "messages": [
                    "I have a doctor's appointment early tomorrow and I'm worried I'll oversleep. I usually wake up on my own but I can't risk it. I need to be up at 6:30. I have an iPhone.",
                    """Good idea to set one. Here's how to make sure you're up at 6:30.

1. Open the **Clock** app, then tap the **Alarms** tab.
2. Tap the **Add** button.
3. Set the time to **6:30 AM**.
4. Only if you want it to repeat, tap **Repeat** and choose the days.
5. Tap **Done**.

The alarm will ring even if your phone is on Silent or Do Not Disturb.

If the alarm is too quiet, go to **Settings**, then **Sounds & Haptics**, and drag the **Ringtone and Alerts** slider to the right. If it only vibrates, check that the alarm's **Sound** isn't set to **None**.""",
                ],
            },
            {
                "existing": True, "id": 'tr066-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to set and change alarms on your iPhone', 'url': 'https://support.apple.com/en-us/118444', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I set an alarm to wake me up',
                    'Sure. Is your phone an **iPhone** or an **Android** phone?',
                    'iPhone',
                    """Thanks. Here's how to set an alarm.

1. Open the **Clock** app, then tap the **Alarms** tab.
2. Tap the **Add** button.
3. Set the time you want to wake up.
4. Only if you want it to repeat, tap **Repeat** and choose the days.
5. Tap **Done**.

The alarm will ring even if your phone is on Silent or Do Not Disturb.

If the alarm is too quiet, go to **Settings**, then **Sounds & Haptics**, and drag the **Ringtone and Alerts** slider to the right. If it only vibrates, check that the alarm's **Sound** isn't set to **None**.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-067', "task_type": 'alarm', "task": 'Set an alarm',
        "platform": 'Android (Clock)', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Set, cancel, or snooze alarms on your Android device', "url": 'https://support.google.com/android/answer/2840926?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr067-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android (Clock)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Set, cancel, or snooze alarms on your Android device', 'url': 'https://support.google.com/android/answer/2840926?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I set an alarm on my Android phone?',
                    """Here's how, using the **Clock** app. It takes about a minute.

1. Open the **Clock** app.
2. Tap **Alarm**.
3. Tap **Add**.
4. Set the time. On a round clock face, drag the hand to the hour, then to the minutes. Choose **AM** or **PM**.
5. Tap **OK**.

Make sure your alarm volume isn't too low. Below about 30%, you might not hear it.

If you set more than one alarm, leave at least 5 minutes between them.""",
                ],
            },
            {
                "existing": True, "id": 'tr067-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Set, cancel, or snooze alarms on your Android device', 'url': 'https://support.google.com/android/answer/2840926?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'need an alarm for tomorrow',
                    'I can help you set one. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr067-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Help: Set, cancel, or snooze alarms on your Android device', 'url': 'https://support.google.com/android/answer/2840926?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'alarm for 7',
                    'Sure. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr067-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android (Clock)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Set, cancel, or snooze alarms on your Android device', 'url': 'https://support.google.com/android/answer/2840926?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'need an alarm for tomorrow',
                    'I can help you set one. Is your phone an **iPhone** or an **Android** phone?',
                    'Android',
                    """Thanks.

Here's how, using the **Clock** app. It takes about a minute.

1. Open the **Clock** app.
2. Tap **Alarm**.
3. Tap **Add**.
4. Set the time. On a round clock face, drag the hand to the hour, then to the minutes. Choose **AM** or **PM**.
5. Tap **OK**.

Make sure your alarm volume isn't too low. Below about 30%, you might not hear it.

If you set more than one alarm, leave at least 5 minutes between them.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-068', "task_type": 'hearing_bluetooth', "task": 'Pair hearing aids or Bluetooth headphones',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Use Made for iPhone hearing devices', "url": 'https://support.apple.com/en-us/108780'},
        "examples": [
            {
                "existing": True, "id": 'tr068-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use Made for iPhone hearing devices', 'url': 'https://support.apple.com/en-us/108780', 'accessed': '2026-10-24'}],
                "messages": [
                    'I just got new hearing aids that work with iPhone. How do I connect them?',
                    """Here's how to pair them. It takes a few minutes.

1. Make sure your iPhone has the latest software update.
2. Put your hearing aids in **pairing mode**. Depending on the model, you might open and close the battery doors, turn them off and on, or take them out of the charger. Your hearing aid instructions will say which.
3. On your iPhone, open **Settings**.
4. Tap **Accessibility**.
5. Tap **Hearing Devices**.
6. Tap **Pair MFi Hearing Device** and follow the steps on the screen.
7. Select your hearing aids, then tap **Pair**.

If you don't see **Pair MFi Hearing Device**, tap your hearing aids' name when it appears under **Hearing Devices**, then tap **Pair**.

If they don't appear, check that they're in pairing mode, restart your iPhone, and look in your hearing aids' user guide or the maker's app.""",
                ],
            },
            {
                "existing": True, "id": 'tr068-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use Made for iPhone hearing devices', 'url': 'https://support.apple.com/en-us/108780', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I connect my hearing aids to my phone',
                    'I can help you pair them. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr068-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Use Made for iPhone hearing devices', 'url': 'https://support.apple.com/en-us/108780', 'accessed': '2026-10-24'}],
                "messages": [
                    'My audiologist set up my new hearing aids in the office but she said I could connect them to my iPhone so phone calls go straight into my ears. I forgot to ask her how.',
                    """That's a great feature. Here's how to pair them. It takes a few minutes.

1. Make sure your iPhone has the latest software update.
2. Put your hearing aids in **pairing mode**. Depending on the model, you might open and close the battery doors, turn them off and on, or take them out of the charger. Your hearing aid instructions will say which.
3. On your iPhone, open **Settings**.
4. Tap **Accessibility**.
5. Tap **Hearing Devices**.
6. Tap **Pair MFi Hearing Device** and follow the steps on the screen.
7. Select your hearing aids, then tap **Pair**.

If you don't see **Pair MFi Hearing Device**, tap your hearing aids' name when it appears under **Hearing Devices**, then tap **Pair**.

If they don't appear, check that they're in pairing mode, restart your iPhone, and look in your hearing aids' user guide or the maker's app.""",
                ],
            },
            {
                "existing": True, "id": 'tr068-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use Made for iPhone hearing devices', 'url': 'https://support.apple.com/en-us/108780', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I connect my hearing aids to my phone',
                    'I can help you pair them. Is your phone an **iPhone** or an **Android** phone?',
                    'iPhone',
                    """Thanks.

Here's how to pair them. It takes a few minutes.

1. Make sure your iPhone has the latest software update.
2. Put your hearing aids in **pairing mode**. Depending on the model, you might open and close the battery doors, turn them off and on, or take them out of the charger. Your hearing aid instructions will say which.
3. On your iPhone, open **Settings**.
4. Tap **Accessibility**.
5. Tap **Hearing Devices**.
6. Tap **Pair MFi Hearing Device** and follow the steps on the screen.
7. Select your hearing aids, then tap **Pair**.

If you don't see **Pair MFi Hearing Device**, tap your hearing aids' name when it appears under **Hearing Devices**, then tap **Pair**.

If they don't appear, check that they're in pairing mode, restart your iPhone, and look in your hearing aids' user guide or the maker's app.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-069', "task_type": 'hearing_bluetooth', "task": 'Pair Bluetooth headphones',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Find & set up Bluetooth devices near your Android device', "url": 'https://support.google.com/android/answer/9417604?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr069-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Find & set up Bluetooth devices near your Android device', 'url': 'https://support.google.com/android/answer/9417604?hl=en', 'accessed': '2026-10-24'}, {'title': 'Android Help: Fix Bluetooth problems on Android', 'url': 'https://support.google.com/android/answer/9769184?hl=en', 'accessed': '2026-11-13'}],
                "messages": [
                    'How do I connect my new Bluetooth headphones to my Android phone?',
                    """Here's how. It takes a couple of minutes.

1. Turn on your headphones and make sure they're discoverable and ready to pair. Follow the instructions that came with them.
2. On your phone, **swipe down** from the top of the screen.
3. **Press and hold** the **Bluetooth** icon.
4. Tap **Pair new device**.
5. Tap the name of your headphones when it appears.
6. Follow any instructions on the screen.

If you don't see **Pair new device**, check under **Available devices**, or tap **More**, then **Refresh**.

If you're asked for a code and don't have one, try **0000** or **1234**.""",
                ],
            },
            {
                "existing": True, "id": 'tr069-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Find & set up Bluetooth devices near your Android device', 'url': 'https://support.google.com/android/answer/9417604?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I connect my earbuds',
                    'Sure. What are you connecting them to: an **iPhone**, an **Android** phone, or a **computer**?',
                ],
            },
            {
                "existing": True, "id": 'tr069-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Help: Find & set up Bluetooth devices near your Android device', 'url': 'https://support.google.com/android/answer/9417604?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'bluetooth wont',
                    "It looks like your message got cut off. What won't connect over Bluetooth: **headphones**, a **speaker**, a **car**, or something else?",
                ],
            },
            {
                "existing": True, "id": 'tr069-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Find & set up Bluetooth devices near your Android device', 'url': 'https://support.google.com/android/answer/9417604?hl=en', 'accessed': '2026-10-24'}, {'title': 'Android Help: Fix Bluetooth problems on Android', 'url': 'https://support.google.com/android/answer/9769184?hl=en', 'accessed': '2026-11-13'}],
                "messages": [
                    'how do I connect my earbuds',
                    'Sure. What are you connecting them to: an **iPhone**, an **Android** phone, or a **computer**?',
                    'My Android phone',
                    """Thanks.

Here's how. It takes a couple of minutes.

1. Turn on your headphones and make sure they're discoverable and ready to pair. Follow the instructions that came with them.
2. On your phone, **swipe down** from the top of the screen.
3. **Press and hold** the **Bluetooth** icon.
4. Tap **Pair new device**.
5. Tap the name of your headphones when it appears.
6. Follow any instructions on the screen.

If you don't see **Pair new device**, check under **Available devices**, or tap **More**, then **Refresh**.

If you're asked for a code and don't have one, try **0000** or **1234**.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-070', "task_type": 'battery_saver', "task": 'Turn on battery saving mode',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Use Low Power Mode to save battery life on your iPhone or iPad', "url": 'https://support.apple.com/en-us/101604'},
        "examples": [
            {
                "existing": True, "id": 'tr070-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use Low Power Mode to save battery life on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/101604', 'accessed': '2026-10-24'}],
                "messages": [
                    "How do I turn on Low Power Mode on my iPhone? I'm going out and my battery is low.",
                    """Here's how. It takes a few seconds.

**Quickest way:** swipe down from the top-right corner to open **Control Center**, then tap the **battery** icon.

**In Settings:**
1. Open **Settings**.
2. Tap **Battery**.
3. On iPhone 15 and newer, tap **Power Mode**, then **Low Power Mode**. On older iPhones, turn on **Low Power Mode**.

You'll know it's on when the battery icon at the top of the screen turns **yellow**.

Low Power Mode dims the screen a little and pauses some background activity, like checking for new email. It turns off by itself once the battery is charged to 80% or higher.""",
                ],
            },
            {
                "existing": True, "id": 'tr070-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use Low Power Mode to save battery life on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/101604', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I make my battery last longer today',
                    "There's a battery-saving mode that can help. Is your phone an **iPhone** or an **Android** phone?",
                ],
            },
            {
                "existing": True, "id": 'tr070-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Use Low Power Mode to save battery life on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/101604', 'accessed': '2026-10-24'}],
                "messages": [
                    "We're going to a wedding tomorrow and it'll be a long day. My phone usually dies by dinner and I want to take pictures all night.",
                    """A battery-saving mode can help it last longer.

**Is your phone an iPhone or an Android phone?** I'll show you how to turn it on.""",
                ],
            },
            {
                "existing": True, "id": 'tr070-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use Low Power Mode to save battery life on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/101604', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I make my battery last longer today',
                    "There's a battery-saving mode that can help. Is your phone an **iPhone** or an **Android** phone?",
                    'iPhone 14',
                    """Thanks. On your iPhone, it's called Low Power Mode.

Here's how. It takes a few seconds.

**Quickest way:** swipe down from the top-right corner to open **Control Center**, then tap the **battery** icon.

**In Settings:**
1. Open **Settings**.
2. Tap **Battery**.
3. Turn on **Low Power Mode**.

You'll know it's on when the battery icon at the top of the screen turns **yellow**.

Low Power Mode dims the screen a little and pauses some background activity, like checking for new email. It turns off by itself once the battery is charged to 80% or higher.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-071', "task_type": 'battery_saver', "task": 'Turn on battery saving mode',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": "Android Help: Get the most life from your Android device's battery", "url": 'https://support.google.com/android/answer/7664692?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr071-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': "Android Help: Get the most life from your Android device's battery", 'url': 'https://support.google.com/android/answer/7664692?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I turn on Battery Saver on my Android phone?',
                    """Here's how. It takes less than a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver**, then choose a schedule for it, or choose to have it turn off automatically.

Battery Saver switches the screen to a dark theme and limits what apps do in the background, so your battery lasts longer.

Some phones call this something like **low power mode**. If you don't see **Battery Saver**, tell me what you see under **Battery**.""",
                ],
            },
            {
                "existing": True, "id": 'tr071-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': "Android Help: Get the most life from your Android device's battery", 'url': 'https://support.google.com/android/answer/7664692?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "my phone battery won't last the day, can I make it last longer?",
                    'Yes, a battery-saving mode can help. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr071-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'over_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': "Android Help: Get the most life from your Android device's battery", 'url': 'https://support.google.com/android/answer/7664692?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "Galaxy S23, battery at 40%, I need it until 10pm tonight. I'd like to turn on whatever the power saving setting is.",
                    """Here's how. Menu names on Samsung phones can differ a little, and it takes less than a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver**, then choose a schedule for it, or choose to have it turn off automatically.

Battery Saver switches the screen to a dark theme and limits what apps do in the background, so your battery lasts longer.

Some phones call this something like **low power mode**. If you don't see **Battery Saver**, tell me what you see under **Battery**.""",
                ],
            },
            {
                "existing": True, "id": 'tr071-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': "Android Help: Get the most life from your Android device's battery", 'url': 'https://support.google.com/android/answer/7664692?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "my phone battery won't last the day, can I make it last longer?",
                    'Yes, a battery-saving mode can help. Is your phone an **iPhone** or an **Android** phone?',
                    'Android',
                    """Thanks.

Here's how. It takes less than a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver**, then choose a schedule for it, or choose to have it turn off automatically.

Battery Saver switches the screen to a dark theme and limits what apps do in the background, so your battery lasts longer.

Some phones call this something like **low power mode**. If you don't see **Battery Saver**, tell me what you see under **Battery**.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-072', "task_type": 'software_update', "task": 'Update apps',
        "platform": 'iPhone (App Store)', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: How to manually update apps from the App Store', "url": 'https://support.apple.com/en-us/102629'},
        "examples": [
            {
                "existing": True, "id": 'tr072-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone (App Store)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to manually update apps from the App Store', 'url': 'https://support.apple.com/en-us/102629', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I update the apps on my iPhone?',
                    """Here's how to update them all at once. It takes a few minutes.

1. Open the **App Store**.
2. Tap your **profile picture** (or the account icon) at the top of the screen.
3. Tap **App Updates**.
4. Tap **Update All**, or tap **Update** next to just one app.

**To have apps update by themselves:**
1. Open **Settings**.
2. Tap **Apps**, then **App Store**.
3. Turn on **App Updates**.""",
                ],
            },
            {
                "existing": True, "id": 'tr072-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to manually update apps from the App Store', 'url': 'https://support.apple.com/en-us/102629', 'accessed': '2026-10-24'}],
                "messages": [
                    'my banking app says I need to update it',
                    'Updating the app is usually quick. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr072-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: How to manually update apps from the App Store', 'url': 'https://support.apple.com/en-us/102629', 'accessed': '2026-10-24'}],
                "messages": [
                    'update apps on',
                    'It looks like your message got cut off. Which device do you want to update apps on: an **iPhone**, an **Android** phone, or a **computer**?',
                ],
            },
            {
                "existing": True, "id": 'tr072-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone (App Store)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to manually update apps from the App Store', 'url': 'https://support.apple.com/en-us/102629', 'accessed': '2026-10-24'}],
                "messages": [
                    'my banking app says I need to update it',
                    'Updating the app is usually quick. Is your phone an **iPhone** or an **Android** phone?',
                    'iPhone',
                    """Thanks. Here's how to update your banking app.

1. Open the **App Store**.
2. Tap your **profile picture** (or the account icon) at the top of the screen.
3. Tap **App Updates**.
4. Tap **Update** next to your banking app. If you want to update every app, tap **Update All** instead.

**To have apps update by themselves:**
1. Open **Settings**.
2. Tap **Apps**, then **App Store**.
3. Turn on **App Updates**.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-073', "task_type": 'magnifier', "task": 'Zoom in on the screen',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Accessibility Help: Use magnification on your screen', "url": 'https://support.google.com/accessibility/android/answer/6006949?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr073-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: Use magnification on your screen', 'url': 'https://support.google.com/accessibility/android/answer/6006949?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "Is there a way to zoom in on my Android phone's screen to read small things?",
                    """Android has a **Magnification** feature. Setting it up takes a couple of minutes.

**Turn it on:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Magnification**.
4. Turn on the **Magnification shortcut**. You can choose how to start it: the **Accessibility button** on the screen, **pressing and holding both volume keys**, or **triple-tapping** the screen.

**Use it:**
1. Start magnification with your shortcut.
2. Tap anywhere on the screen, except the keyboard or the navigation bar.
3. **Pinch** with two fingers to zoom in or out.
4. **Drag with two fingers** to move around.
5. Use the shortcut again to stop.

It can zoom up to 8 times.""",
                ],
            },
            {
                "existing": True, "id": 'tr073-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: Use magnification on your screen', 'url': 'https://support.google.com/accessibility/android/answer/6006949?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'can I zoom in on my phone screen',
                    'Yes, most phones can. Is yours an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr073-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Accessibility Help: Use magnification on your screen', 'url': 'https://support.google.com/accessibility/android/answer/6006949?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'The print on my medicine reminder app is so tiny, and making the text bigger messes up how the app looks. My Android phone is a Pixel.',
                    """Magnification is a good fit for that: it zooms in only when you need it and doesn't change how the app looks the rest of the time.

Android has a **Magnification** feature. Setting it up takes a couple of minutes.

**Turn it on:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Magnification**.
4. Turn on the **Magnification shortcut**. You can choose how to start it: the **Accessibility button** on the screen, **pressing and holding both volume keys**, or **triple-tapping** the screen.

**Use it:**
1. Start magnification with your shortcut.
2. Tap anywhere on the screen, except the keyboard or the navigation bar.
3. **Pinch** with two fingers to zoom in or out.
4. **Drag with two fingers** to move around.
5. Use the shortcut again to stop.

It can zoom up to 8 times.""",
                ],
            },
            {
                "existing": True, "id": 'tr073-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: Use magnification on your screen', 'url': 'https://support.google.com/accessibility/android/answer/6006949?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'can I zoom in on my phone screen',
                    'Yes, most phones can. Is yours an **iPhone** or an **Android** phone?',
                    'Android',
                    """Thanks.

Android has a **Magnification** feature. Setting it up takes a couple of minutes.

**Turn it on:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Magnification**.
4. Turn on the **Magnification shortcut**. You can choose how to start it: the **Accessibility button** on the screen, **pressing and holding both volume keys**, or **triple-tapping** the screen.

**Use it:**
1. Start magnification with your shortcut.
2. Tap anywhere on the screen, except the keyboard or the navigation bar.
3. **Pinch** with two fingers to zoom in or out.
4. **Drag with two fingers** to move around.
5. Use the shortcut again to stop.

It can zoom up to 8 times.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-074', "task_type": 'find_lost_phone', "task": 'Find a lost phone',
        "platform": 'iPhone (Find My)', "category": 'technical_support', "sensitive": True,
        "source": {"title": 'Apple Support: How to find your lost iPhone or iPad', "url": 'https://support.apple.com/en-us/101593'},
        "examples": [
            {
                "existing": True, "id": 'tr074-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone (Find My)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Apple Support: How to find your lost iPhone or iPad', 'url': 'https://support.apple.com/en-us/101593', 'accessed': '2026-10-24'}],
                "messages": [
                    "I can't find my iPhone. I think I left it at a restaurant. How do I find it?",
                    """Let's try to find it. You'll need another device or a computer.

**Option 1: another Apple device**
1. Open the **Find My** app and tap **Devices**.
2. Select your iPhone to see it on a map.
(A family member's iPhone also works if you're in the same Family Sharing group.)
3. To protect it, tap **More**.
4. Scroll down and turn on **Lost Mode**.
5. Follow the steps on the screen to add a phone number and a message.
6. Tap **Activate**.

**Option 2: a computer**
1. Go to **icloud.com/find** and sign in with your Apple Account. If you're asked for a verification code, select **Find Devices** instead.
2. Select your iPhone under **All Devices**.
3. Choose to play a sound to help find it nearby, or mark it as lost.

Stay safe: Apple will never contact you to say your iPhone has been found. Don't share your passcode or any codes with anyone who calls or texts about your phone.""",
                ],
            },
            {
                "existing": True, "id": 'tr074-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Apple Support: How to find your lost iPhone or iPad', 'url': 'https://support.apple.com/en-us/101593', 'accessed': '2026-10-24'}],
                "messages": [
                    'I lost my phone',
                    "I'm sorry, that's stressful. Is your phone an **iPhone** or an **Android** phone?",
                ],
            },
            {
                "existing": True, "id": 'tr074-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'iPhone (Find My)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: How to find your lost iPhone or iPad', 'url': 'https://support.apple.com/en-us/101593', 'accessed': '2026-10-24'}],
                "messages": [
                    "I left the grocery store and when I got home my iPhone wasn't in my bag. My husband has an iPhone too. I'm panicking a little.",
                    """Take a breath. There's a good chance you can find it, and your husband's iPhone may help if you're both in the same Family Sharing group.

Let's try to find it. You'll need another device or a computer.

**Option 1: another Apple device**
1. Open the **Find My** app and tap **Devices**.
2. Select your iPhone to see it on a map.
(A family member's iPhone also works if you're in the same Family Sharing group.)
3. To protect it, tap **More**.
4. Scroll down and turn on **Lost Mode**.
5. Follow the steps on the screen to add a phone number and a message.
6. Tap **Activate**.

**Option 2: a computer**
1. Go to **icloud.com/find** and sign in with your Apple Account. If you're asked for a verification code, select **Find Devices** instead.
2. Select your iPhone under **All Devices**.
3. Choose to play a sound to help find it nearby, or mark it as lost.

Stay safe: Apple will never contact you to say your iPhone has been found. Don't share your passcode or any codes with anyone who calls or texts about your phone.""",
                ],
            },
            {
                "existing": True, "id": 'tr074-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone (Find My)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Apple Support: How to find your lost iPhone or iPad', 'url': 'https://support.apple.com/en-us/101593', 'accessed': '2026-10-24'}],
                "messages": [
                    'I lost my phone',
                    "I'm sorry, that's stressful. Is your phone an **iPhone** or an **Android** phone?",
                    "iPhone. I'm on my laptop now.",
                    """Good, your laptop will work. Here's how to look for your iPhone.

1. Go to **icloud.com/find** and sign in with your Apple Account. If you're asked for a verification code, select **Find Devices** instead.
2. Select your iPhone under **All Devices**.
3. Choose to play a sound to help find it nearby, or mark it as lost.

Stay safe: Apple will never contact you to say your iPhone has been found. Don't share your passcode or any codes with anyone who calls or texts about your phone.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-075', "task_type": 'find_lost_phone', "task": 'Find a lost phone',
        "platform": 'Android', "category": 'technical_support', "sensitive": True,
        "source": {"title": 'Google Account Help: Find, secure, or erase a lost Android device', "url": 'https://support.google.com/accounts/answer/6160491?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr075-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Google Account Help: Find, secure, or erase a lost Android device', 'url': 'https://support.google.com/accounts/answer/6160491?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'I lost my Android phone. How can I find it?',
                    """You can look for it with **Find Hub** from another device. It works if your phone is on and connected to the internet.

1. On another Android phone, open the **Find Hub** app. On a computer, go to **google.com/android/find**.
2. Sign in with your Google Account.
3. Select your lost phone. If asked, enter your lock screen PIN or password. You'll see where it is on a map.

Then choose what to do:
- **Play sound:** your phone rings loudly for 5 minutes, even if it's on silent.
- **Mark as lost:** tap **Mark as lost**, then **Next**. Add a message and a phone number, then tap **Mark as lost** again to confirm.
- **Factory reset:** erases everything on the phone. Only do this if you can't get it back, because afterward you can't find it with Find Hub.""",
                ],
            },
            {
                "existing": True, "id": 'tr075-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Google Account Help: Find, secure, or erase a lost Android device', 'url': 'https://support.google.com/accounts/answer/6160491?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "can't find my phone anywhere",
                    "Let's try to find it. Is it an **iPhone** or an **Android** phone?",
                ],
            },
            {
                "existing": True, "id": 'tr075-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Account Help: Find, secure, or erase a lost Android device', 'url': 'https://support.google.com/accounts/answer/6160491?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'lost phone help',
                    "I'm sorry, let's try to find it. Is it an **iPhone** or an **Android** phone?",
                ],
            },
            {
                "existing": True, "id": 'tr075-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Google Account Help: Find, secure, or erase a lost Android device', 'url': 'https://support.google.com/accounts/answer/6160491?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "can't find my phone anywhere",
                    "Let's try to find it. Is it an **iPhone** or an **Android** phone?",
                    "Android. I can use my husband's phone.",
                    """Good, your husband's phone will work.

You can look for it with **Find Hub** from another device. It works if your phone is on and connected to the internet.

1. On another Android phone, open the **Find Hub** app. If your husband's phone isn't an Android phone, open a web browser on it and go to **google.com/android/find**.
2. Sign in with your Google Account.
3. Select your lost phone. If asked, enter your lock screen PIN or password. You'll see where it is on a map.

Then choose what to do:
- **Play sound:** your phone rings loudly for 5 minutes, even if it's on silent.
- **Mark as lost:** tap **Mark as lost**, then **Next**. Add a message and a phone number, then tap **Mark as lost** again to confirm.
- **Factory reset:** erases everything on the phone. Only do this if you can't get it back, because afterward you can't find it with Find Hub.""",
                ],
            },
        ],
    },
]
