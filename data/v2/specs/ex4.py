"""Existing English drafts, group 4. Exported by export_spec.py; ids and provenance preserved."""
TASKS = [
    {
        "task_id": 'TR-048', "task_type": 'silence_unknown_callers', "task": 'Silence calls from unknown numbers',
        "platform": 'iPhone', "category": 'communication', "sensitive": False,
        "source": {"title": 'Apple Support: Manage unknown callers on iPhone', "url": 'https://support.apple.com/en-us/111106'},
        "examples": [
            {
                "existing": True, "id": 'tr048-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Manage unknown callers on iPhone', 'url': 'https://support.apple.com/en-us/111106', 'accessed': '2026-10-24'}],
                "messages": [
                    "I get a lot of spam calls from numbers I don't know. Can I make my iPhone only ring for people in my contacts?",
                    """iPhone can silence calls from numbers that aren't in your contacts and send them to voicemail. It takes about a minute.

1. Open the **Settings** app.
2. Tap **Apps**, then **Phone**.
3. Scroll to **Screen Unknown Callers** and tap it.
4. Choose **Silence**.

Calls from people in your contacts will still ring normally. Unknown callers go to voicemail, so check your voicemail now and then in case a doctor's office or pharmacy calls from a new number.

Tip: save important numbers, like your doctor and pharmacy, to your contacts so they always ring through.""",
                ],
            },
            {
                "existing": True, "id": 'tr048-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Manage unknown callers on iPhone', 'url': 'https://support.apple.com/en-us/111106', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I stop spam calls?',
                    'There are a few ways to cut down on them. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr048-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Manage unknown callers on iPhone', 'url': 'https://support.apple.com/en-us/111106', 'accessed': '2026-10-24'}],
                "messages": [
                    "Every day I get calls about my car warranty and I don't even have a car anymore. It's driving me crazy.",
                    """Those calls are so annoying. There are phone settings that can quiet calls from numbers you don't know.

**Is your phone an iPhone or an Android phone?**""",
                ],
            },
            {
                "existing": True, "id": 'tr048-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Manage unknown callers on iPhone', 'url': 'https://support.apple.com/en-us/111106', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I stop spam calls?',
                    'There are a few ways to cut down on them. Is your phone an **iPhone** or an **Android** phone?',
                    'iPhone',
                    """Thanks. One helpful option on iPhone is to silence calls from numbers you don't know.

iPhone can silence calls from numbers that aren't in your contacts and send them to voicemail. It takes about a minute.

1. Open the **Settings** app.
2. Tap **Apps**, then **Phone**.
3. Scroll to **Screen Unknown Callers** and tap it.
4. Choose **Silence**.

Calls from people in your contacts will still ring normally. Unknown callers go to voicemail, so check your voicemail now and then in case a doctor's office or pharmacy calls from a new number.

Tip: save important numbers, like your doctor and pharmacy, to your contacts so they always ring through.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-049', "task_type": 'spam_call_filter', "task": 'Filter spam calls',
        "platform": 'Android (Pixel)', "category": 'communication', "sensitive": False,
        "source": {"title": 'Phone app Help: Use caller ID & spam protection', "url": 'https://support.google.com/phoneapp/answer/3459196?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr049-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android (Pixel)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Phone app Help: Use caller ID & spam protection', 'url': 'https://support.google.com/phoneapp/answer/3459196?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'Can my Google Pixel phone filter out spam calls automatically?',
                    """The Phone app on your Pixel can filter spam calls. It takes about a minute to turn on.

1. Open the **Phone** app.
2. Tap the **More options** menu (three dots).
3. Tap **Settings**.
4. Tap **Caller ID and spam**.
5. Make sure **See caller ID & spam** is on.
6. Turn on **Filter spam calls**.

Filtered calls won't ring or notify you, but they still appear in your call history.

If you don't see **Filter spam calls**, your phone may use **Call Screen** instead, where spam blocking is one of the options. Tell me and I'll walk you through it.""",
                ],
            },
            {
                "existing": True, "id": 'tr049-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Phone app Help: Use caller ID & spam protection', 'url': 'https://support.google.com/phoneapp/answer/3459196?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'too many robocalls, can my phone block them?',
                    "Many phones can filter them. Is yours an **iPhone** or an **Android** phone? If it's Android, which brand?",
                ],
            },
            {
                "existing": True, "id": 'tr049-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'over_specified', "specification": 'fully_specified', "platform": 'Android (Pixel)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Phone app Help: Use caller ID & spam protection', 'url': 'https://support.google.com/phoneapp/answer/3459196?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "Pixel 8, using the default Google Phone app. Caller ID shows 'Suspected spam' but they still ring. How do I make those not ring at all?",
                    """Since your phone already labels them, you just need to turn on filtering:

The Phone app on your Pixel can filter spam calls. It takes about a minute to turn on.

1. Open the **Phone** app.
2. Tap the **More options** menu (three dots).
3. Tap **Settings**.
4. Tap **Caller ID and spam**.
5. Make sure **See caller ID & spam** is on.
6. Turn on **Filter spam calls**.

Filtered calls won't ring or notify you, but they still appear in your call history.

If you don't see **Filter spam calls**, your phone may use **Call Screen** instead, where spam blocking is one of the options. Tell me and I'll walk you through it.""",
                ],
            },
            {
                "existing": True, "id": 'tr049-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android (Pixel)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Phone app Help: Use caller ID & spam protection', 'url': 'https://support.google.com/phoneapp/answer/3459196?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'too many robocalls, can my phone block them?',
                    "Many phones can filter them. Is yours an **iPhone** or an **Android** phone? If it's Android, which brand?",
                    'Google Pixel 7a',
                    """Thanks. The Pixel has a built-in spam filter.

The Phone app on your Pixel can filter spam calls. It takes about a minute to turn on.

1. Open the **Phone** app.
2. Tap the **More options** menu (three dots).
3. Tap **Settings**.
4. Tap **Caller ID and spam**.
5. Make sure **See caller ID & spam** is on.
6. Turn on **Filter spam calls**.

Filtered calls won't ring or notify you, but they still appear in your call history.

If you don't see **Filter spam calls**, your phone may use **Call Screen** instead, where spam blocking is one of the options. Tell me and I'll walk you through it.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-050', "task_type": 'battery_health', "task": 'Check battery health',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: iPhone battery and performance', "url": 'https://support.apple.com/en-us/101575'},
        "examples": [
            {
                "existing": True, "id": 'tr050-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: iPhone battery and performance', 'url': 'https://support.apple.com/en-us/101575', 'accessed': '2026-10-24'}],
                "messages": [
                    'My iPhone battery seems to die quickly. How do I check the battery health?',
                    """You can check it in Settings. It takes a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Health**. On some versions the name is slightly different.
4. Look at **Maximum Capacity**. This compares your battery now to when it was new. A lower number means it won't last as long between charges.

If you see a message that your battery's health is **significantly degraded**, it isn't a safety problem, but a new battery would help it last longer. Apple offers battery service, and it may be covered if your phone is still under warranty.""",
                ],
            },
            {
                "existing": True, "id": 'tr050-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: iPhone battery and performance', 'url': 'https://support.apple.com/en-us/101575', 'accessed': '2026-10-24'}],
                "messages": [
                    'my battery dies so fast',
                    "That's annoying. I can help you check what's going on. Is your phone an **iPhone** or an **Android** phone, and about how old is it?",
                ],
            },
            {
                "existing": True, "id": 'tr050-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: iPhone battery and performance', 'url': 'https://support.apple.com/en-us/101575', 'accessed': '2026-10-24'}],
                "messages": [
                    'battery health',
                    "Sure. Do you want to **check your battery's health**? If so, is your phone an iPhone or an Android phone?",
                ],
            },
            {
                "existing": True, "id": 'tr050-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: iPhone battery and performance', 'url': 'https://support.apple.com/en-us/101575', 'accessed': '2026-10-24'}],
                "messages": [
                    'my battery dies so fast',
                    "That's annoying. I can help you check what's going on. Is your phone an **iPhone** or an **Android** phone, and about how old is it?",
                    'iPhone, about 4 years old',
                    """Thanks. At four years old, the battery may be worn. Let's check:

You can check it in Settings. It takes a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Health**. On some versions the name is slightly different.
4. Look at **Maximum Capacity**. This compares your battery now to when it was new. A lower number means it won't last as long between charges.

If you see a message that your battery's health is **significantly degraded**, it isn't a safety problem, but a new battery would help it last longer. Apple offers battery service, and it may be covered if your phone is still under warranty.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-051', "task_type": 'group_text', "task": 'Start a group text',
        "platform": 'iPhone', "category": 'communication', "sensitive": False,
        "source": {"title": 'Apple Support: Send a group text message on your iPhone or iPad', "url": 'https://support.apple.com/en-us/118236'},
        "examples": [
            {
                "existing": True, "id": 'tr051-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Send a group text message on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/118236', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I send one text message to my three kids at the same time on my iPhone?',
                    """You can start a group text. It takes about a minute.

1. Open the **Messages** app.
2. Tap the **Compose** button (a square with a pencil) at the top.
3. Type the name of your first child and choose them. Do the same for the other two. You can also tap the **plus** button to pick them from your contacts.
4. Type your message.
5. Tap the **Send** button (the up arrow).

All three will get the message, and when anyone replies, everyone in the group sees it.

If one of your kids has an Android phone and the message won't send, go to **Settings**, then **Messages**, and make sure **MMS Messaging** is turned on.""",
                ],
            },
            {
                "existing": True, "id": 'tr051-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft, edited by Ryan Hsieh', "reviewed": True, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Send a group text message on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/118236', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I text all my kids at once',
                    "You can send a group text. Is your phone an **iPhone** or an **Android** phone? If you're not sure, an iPhone has an apple logo on the back.",
                ],
            },
            {
                "existing": True, "id": 'tr051-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Send a group text message on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/118236', 'accessed': '2026-10-24'}],
                "messages": [
                    'I want to tell my three children about our Thanksgiving plans but typing the same message three times is a pain and I always forget someone. I have an iPhone.',
                    """A group text will send it to all three at once, so no one gets left out. Here's how:

You can start a group text. It takes about a minute.

1. Open the **Messages** app.
2. Tap the **Compose** button (a square with a pencil) at the top.
3. Type the name of your first child and choose them. Do the same for the other two. You can also tap the **plus** button to pick them from your contacts.
4. Type your message.
5. Tap the **Send** button (the up arrow).

All three will get the message, and when anyone replies, everyone in the group sees it.

If one of your kids has an Android phone and the message won't send, go to **Settings**, then **Messages**, and make sure **MMS Messaging** is turned on.""",
                ],
            },
            {
                "existing": True, "id": 'tr051-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Send a group text message on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/118236', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I text all my kids at once',
                    'You can send a group text. Is your phone an **iPhone** or an **Android** phone?',
                    'iPhone',
                    """Thanks, here's how on your iPhone.

You can start a group text. It takes about a minute.

1. Open the **Messages** app.
2. Tap the **Compose** button (a square with a pencil) at the top.
3. Type the name of your first child and choose them. Do the same for the other two. You can also tap the **plus** button to pick them from your contacts.
4. Type your message.
5. Tap the **Send** button (the up arrow).

All three will get the message, and when anyone replies, everyone in the group sees it.

If one of your kids has an Android phone and the message won't send, go to **Settings**, then **Messages**, and make sure **MMS Messaging** is turned on.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-052', "task_type": 'browser_zoom', "task": 'Make every web page bigger by default',
        "platform": 'Chrome (computer)', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Google Chrome Help: Change text, image & video sizes (zoom), computer', "url": 'https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop'},
        "examples": [
            {
                "existing": True, "id": 'tr052-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Chrome (computer)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Chrome Help: Change text, image & video sizes (zoom), computer', 'url': 'https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    "Is there a way to make every website bigger in Chrome on my computer, so I don't have to zoom in each time?",
                    """You can change Chrome's default zoom so every website opens bigger. It takes about a minute.

1. Click the **More** menu (three dots) at the top right of Chrome.
2. Click **Settings**.
3. Click **Appearance**.
4. Find **Page zoom** and choose a bigger number, like **125%** or **150%**.

Every website will now open at that size.

To zoom in on just one page, hold the **Ctrl** key and press **+** (on a Mac, use the **Command** key instead).""",
                ],
            },
            {
                "existing": True, "id": 'tr052-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Chrome Help: Change text, image & video sizes (zoom), computer', 'url': 'https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'websites are too small on my computer',
                    "I can help you make them bigger. Which web browser do you use, for example **Chrome**, **Edge**, or **Safari**? If you're not sure, tell me what the icon you click looks like.",
                ],
            },
            {
                "existing": True, "id": 'tr052-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Chrome Help: Change text, image & video sizes (zoom), computer', 'url': 'https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'make websites bigger',
                    'Sure. Do you want to make **one website** bigger right now, or make **every website** bigger from now on? And which browser do you use, such as Chrome or Safari?',
                ],
            },
            {
                "existing": True, "id": 'tr052-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Chrome (computer)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Chrome Help: Change text, image & video sizes (zoom), computer', 'url': 'https://support.google.com/chrome/answer/96810?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'websites are too small on my computer',
                    "I can help you make them bigger. Which web browser do you use, for example **Chrome**, **Edge**, or **Safari**? If you're not sure, tell me what the icon you click looks like.",
                    'Chrome',
                    """Thanks. Chrome lets you set a bigger size for every website.

You can change Chrome's default zoom so every website opens bigger. It takes about a minute.

1. Click the **More** menu (three dots) at the top right of Chrome.
2. Click **Settings**.
3. Click **Appearance**.
4. Find **Page zoom** and choose a bigger number, like **125%** or **150%**.

Every website will now open at that size.

To zoom in on just one page, hold the **Ctrl** key and press **+** (on a Mac, use the **Command** key instead).""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-054', "task_type": 'share_location', "task": 'Share location with family',
        "platform": 'iPhone (Find My)', "category": 'communication', "sensitive": True,
        "source": {"title": 'Apple Support: Share your location with iPhone', "url": 'https://support.apple.com/en-us/105104'},
        "examples": [
            {
                "existing": True, "id": 'tr054-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone (Find My)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Apple Support: Share your location with iPhone', 'url': 'https://support.apple.com/en-us/105104', 'accessed': '2026-10-24'}],
                "messages": [
                    'How can I share my location with my daughter on my iPhone so she knows I got home safe?',
                    """You can do this in the **Find My** app. It takes about two minutes. You and your daughter both need iPhones with a recent software update.

1. Open the **Find My** app.
2. Tap **Me** at the bottom, and make sure **Share My Location** is turned on.
3. Tap **People** at the bottom.
4. Tap the **Add** button (a plus sign), then tap **Share My Location**.
5. Choose your daughter.
6. Choose how long to share, such as **one hour**, **until the end of the day**, or **indefinitely**. Some versions also let you pick a custom time.

Your daughter can then see where you are in her Find My app.

Only share your location with people you trust.""",
                ],
            },
            {
                "existing": True, "id": 'tr054-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Apple Support: Share your location with iPhone', 'url': 'https://support.apple.com/en-us/105104', 'accessed': '2026-10-24'}],
                "messages": [
                    'how can my daughter see where I am',
                    "That's a nice way to give her peace of mind. Is your phone an **iPhone** or an **Android** phone? And does your daughter have an iPhone or Android?",
                ],
            },
            {
                "existing": True, "id": 'tr054-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Share your location with iPhone', 'url': 'https://support.apple.com/en-us/105104', 'accessed': '2026-10-24'}],
                "messages": [
                    'share location',
                    'Sure. **Who would you like to share your location with**, and is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr054-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone (Find My)',
                "author": 'claude-draft, edited by Ryan Hsieh', "reviewed": True, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Apple Support: Share your location with iPhone', 'url': 'https://support.apple.com/en-us/105104', 'accessed': '2026-10-24'}],
                "messages": [
                    'how can my daughter see where I am',
                    "That's a nice way to give her peace of mind. Is your phone an **iPhone** or an **Android** phone? And does your daughter have an iPhone or Android?",
                    'We both have iPhones',
                    """Great. Since you both have iPhones, you can do this in the **Find My** app. It takes about two minutes. You and your daughter both need iPhones with a recent software update.

1. Open the **Find My** app.
2. Tap **Me** at the bottom, and make sure **Share My Location** is turned on.
3. Tap **People** at the bottom.
4. Tap the **Add** button (a plus sign), then tap **Share My Location**.
5. Type your daughter's name and tap it when it appears.
6. Tap **Send**.
7. Choose how long to share, such as **one hour**, **until the end of the day**, or **indefinitely**. Some versions also let you pick a custom time.

Your daughter can then see where you are in her Find My app.

Only share your location with people you trust.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-055', "task_type": 'share_location', "task": 'Share location with family',
        "platform": 'Android (Google Maps)', "category": 'communication', "sensitive": True,
        "source": {"title": 'Google Maps Help: Share your real-time location with others (Android)', "url": 'https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid'},
        "examples": [
            {
                "existing": True, "id": 'tr055-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android (Google Maps)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Google Maps Help: Share your real-time location with others (Android)', 'url': 'https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I share my location with my son using Google Maps on my Android phone?',
                    """Here's how. It takes about two minutes. Your son needs a Gmail address, saved in your contacts.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial** at the top.
3. Tap **Location sharing**.
4. Tap **New share**.
5. Choose how long to share your location.
6. Choose your son. If Maps asks to see your contacts, allow it.
7. Tap **Share**.

Your son can then see where you are in Google Maps.

If he doesn't use Gmail, you can share a **link** instead, which works for up to 24 hours. Only share your location with people you trust.""",
                ],
            },
            {
                "existing": True, "id": 'tr055-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Google Maps Help: Share your real-time location with others (Android)', 'url': 'https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'I want my son to be able to see where I am when I drive',
                    "That's a good safety idea. Is your phone an **iPhone** or an **Android** phone? And does your son use Gmail?",
                ],
            },
            {
                "existing": True, "id": 'tr055-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'Android (Google Maps)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Maps Help: Share your real-time location with others (Android)', 'url': 'https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    "I drive to my sister's house two hours away every weekend and my son always wants me to text him when I get there but I forget. He said there's a way in Google Maps so he can just see. I have an Android.",
                    """Yes, then he won't have to wait for your text. Here's how:

Here's how. It takes about two minutes. Your son needs a Gmail address, saved in your contacts.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial** at the top.
3. Tap **Location sharing**.
4. Tap **New share**.
5. Choose how long to share your location.
6. Choose your son. If Maps asks to see your contacts, allow it.
7. Tap **Share**.

Your son can then see where you are in Google Maps.

If he doesn't use Gmail, you can share a **link** instead, which works for up to 24 hours. Only share your location with people you trust.""",
                ],
            },
            {
                "existing": True, "id": 'tr055-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android (Google Maps)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Google Maps Help: Share your real-time location with others (Android)', 'url': 'https://support.google.com/maps/answer/15437054?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'I want my son to be able to see where I am when I drive',
                    "That's a good safety idea. Is your phone an **iPhone** or an **Android** phone? And does your son use Gmail?",
                    'Android, and yes he uses Gmail',
                    """Great. Google Maps can do this.

Here's how. It takes about two minutes. Your son needs a Gmail address, saved in your contacts.

1. Open **Google Maps** and make sure you're signed in.
2. Tap your **profile picture or initial** at the top.
3. Tap **Location sharing**.
4. Tap **New share**.
5. Choose how long to share your location.
6. Choose your son. If Maps asks to see your contacts, allow it.
7. Tap **Share**.

Your son can then see where you are in Google Maps.

If he doesn't use Gmail, you can share a **link** instead, which works for up to 24 hours. Only share your location with people you trust.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-056', "task_type": 'install_app', "task": 'Install an app',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Download apps on your iPhone or iPad', "url": 'https://support.apple.com/en-us/102590'},
        "examples": [
            {
                "existing": True, "id": 'tr056-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Download apps on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/102590', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I download the WhatsApp app on my iPhone?',
                    """You can get it from the **App Store**. It takes a couple of minutes.

1. Open the **App Store** app.
2. Tap **Search** at the bottom.
3. Type **WhatsApp** and tap the search button.
4. Find the right app and tap **Get** next to it.
5. To confirm, double-click the **side button**. If your iPhone has Face ID, look at the screen. If it has Touch ID, rest your finger on the Home button. You may also be asked for your Apple Account password.

When the download finishes, the button changes to **Open** and the app appears on your Home Screen.

Tip: check the app's name and maker before tapping **Get**, so you get the real app and not a lookalike.""",
                ],
            },
            {
                "existing": True, "id": 'tr056-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Download apps on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/102590', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I download an app',
                    'I can walk you through it. Is your phone an **iPhone** or an **Android** phone? And which app would you like to get?',
                ],
            },
            {
                "existing": True, "id": 'tr056-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Download apps on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/102590', 'accessed': '2026-10-24'}],
                "messages": [
                    'app store download',
                    'Sure, I can help you download an app from the App Store. **Which app would you like to get?**',
                ],
            },
            {
                "existing": True, "id": 'tr056-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Download apps on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/102590', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I download an app',
                    'I can walk you through it. Is your phone an **iPhone** or an **Android** phone? And which app would you like to get?',
                    'iPhone, I want WhatsApp',
                    """Great, here's how to get WhatsApp.

You can get it from the **App Store**. It takes a couple of minutes.

1. Open the **App Store** app.
2. Tap **Search** at the bottom.
3. Type **WhatsApp** and tap the search button.
4. Find the right app and tap **Get** next to it.
5. To confirm, double-click the **side button**. If your iPhone has Face ID, look at the screen. If it has Touch ID, rest your finger on the Home button. You may also be asked for your Apple Account password.

When the download finishes, the button changes to **Open** and the app appears on your Home Screen.

Tip: check the app's name and maker before tapping **Get**, so you get the real app and not a lookalike.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-057', "task_type": 'install_app', "task": 'Install an app',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Download apps to your Android device', "url": 'https://support.google.com/android/answer/9457058?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr057-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Download apps to your Android device', 'url': 'https://support.google.com/android/answer/9457058?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "How do I install an app on my Android phone? My doctor's office wants me to download their app.",
                    """You can get it from the **Play Store**. It takes a couple of minutes.

1. Open the **Play Store** app.
2. Tap the search bar and type the app's name.
3. Tap the app in the results. Check that the name and maker are what you expected. The star rating and number of downloads are shown under the title.
4. Tap **Install**. (If you see a price instead, it's a paid app.)
5. When it's finished, open the app from the Play Store or find it with your other apps.

It's safest to get apps from the Play Store, because Google checks them for harmful software. Avoid installing apps from links in texts or emails.""",
                ],
            },
            {
                "existing": True, "id": 'tr057-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Download apps to your Android device', 'url': 'https://support.google.com/android/answer/9457058?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I get an app on my phone',
                    'I can help. Is your phone an **iPhone** or an **Android** phone? And which app are you looking for?',
                ],
            },
            {
                "existing": True, "id": 'tr057-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Help: Download apps to your Android device', 'url': 'https://support.google.com/android/answer/9457058?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "My neighbor told me there's an app that shows when the bus is coming, and I'd like to try it. I've never downloaded an app myself. My phone is a Samsung Galaxy.",
                    """That sounds handy. Ask your neighbor for the app's exact name, then follow these steps:

You can get it from the **Play Store**. It takes a couple of minutes.

1. Open the **Play Store** app.
2. Tap the search bar and type the app's name.
3. Tap the app in the results. Check that the name and maker are what you expected. The star rating and number of downloads are shown under the title.
4. Tap **Install**. (If you see a price instead, it's a paid app.)
5. When it's finished, open the app from the Play Store or find it with your other apps.

It's safest to get apps from the Play Store, because Google checks them for harmful software. Avoid installing apps from links in texts or emails.""",
                ],
            },
            {
                "existing": True, "id": 'tr057-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Download apps to your Android device', 'url': 'https://support.google.com/android/answer/9457058?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I get an app on my phone',
                    'I can help. Is your phone an **iPhone** or an **Android** phone? And which app are you looking for?',
                    "Android. It's the app for my doctor's office.",
                    """Thanks. If you don't have the app's exact name, ask the office for it. Then:

You can get it from the **Play Store**. It takes a couple of minutes.

1. Open the **Play Store** app.
2. Tap the search bar and type the app's name.
3. Tap the app in the results. Check that the name and maker are what you expected. The star rating and number of downloads are shown under the title.
4. Tap **Install**. (If you see a price instead, it's a paid app.)
5. When it's finished, open the app from the Play Store or find it with your other apps.

It's safest to get apps from the Play Store, because Google checks them for harmful software. Avoid installing apps from links in texts or emails.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-058', "task_type": 'delete_app', "task": 'Delete an app',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Delete apps on your iPhone or iPad', "url": 'https://support.apple.com/en-us/101550'},
        "examples": [
            {
                "existing": True, "id": 'tr058-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Delete apps on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/101550', 'accessed': '2026-10-24'}, {'title': 'Apple Support: How to check the storage on your iPhone and iPad', 'url': 'https://support.apple.com/en-us/108429', 'accessed': '2026-10-24'}],
                "messages": [
                    "How do I delete an app I don't use anymore from my iPhone?",
                    """Here's how. It takes a few seconds.

1. Find the app on your Home Screen.
2. **Press and hold** the app's icon until a menu appears.
3. Tap **Remove App**.
4. Tap **Delete App**.
5. Tap **Delete** to confirm.

If the icons start to jiggle instead of showing a menu:
1. Tap the **minus** sign in the app's upper-left corner.
2. Tap **Delete App**.
3. Tap **Delete**.
4. Tap **Done** at the top of the screen.

Deleting an app also removes its data from your phone. If you might want it later, you can download it again from the App Store.

Deleting an app does **not** cancel any paid subscriptions inside it. If you pay for the app every month, cancel the subscription first.""",
                ],
            },
            {
                "existing": True, "id": 'tr058-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Delete apps on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/101550', 'accessed': '2026-10-24'}, {'title': 'Apple Support: How to check the storage on your iPhone and iPad', 'url': 'https://support.apple.com/en-us/108429', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I get rid of an app',
                    'Sure. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr058-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Delete apps on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/101550', 'accessed': '2026-10-24'}, {'title': 'Apple Support: How to check the storage on your iPhone and iPad', 'url': 'https://support.apple.com/en-us/108429', 'accessed': '2026-10-24'}],
                "messages": [
                    'delete app',
                    'Sure, I can help you delete an app. Is it on an **iPhone**, an **Android** phone, or a **computer**?',
                ],
            },
            {
                "existing": True, "id": 'tr058-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": True, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Delete apps on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/101550', 'accessed': '2026-10-24'}, {'title': 'Apple Support: How to check the storage on your iPhone and iPad', 'url': 'https://support.apple.com/en-us/108429', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I get rid of an app',
                    'Sure. Is your phone an **iPhone** or an **Android** phone?',
                    'iphone',
                    """Thanks.

Here's how. It takes a few seconds.

1. Find the app on your Home Screen.
2. **Press and hold** the app's icon until a menu appears.
3. Tap **Remove App**.
4. Tap **Delete App**.
5. Tap **Delete** to confirm.

If the icons start to jiggle instead of showing a menu:
1. Tap the **minus** sign in the app's upper-left corner.
2. Tap **Delete App**.
3. Tap **Delete**.
4. Tap **Done** at the top of the screen.

Deleting an app also removes its data from your phone. If you might want it later, you can download it again from the App Store.

Deleting an app does **not** cancel any paid subscriptions inside it. If you pay for the app every month, cancel the subscription first.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-059', "task_type": 'delete_app', "task": 'Delete an app',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Google Play Help: Delete apps on your Android device', "url": 'https://support.google.com/googleplay/answer/13627402?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr059-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Google Play Help: Delete apps on your Android device', 'url': 'https://support.google.com/googleplay/answer/13627402?hl=en', 'accessed': '2026-10-24'}, {'title': 'Android Help: Free up storage on your Android device', 'url': 'https://support.google.com/android/answer/7431795?hl=en', 'accessed': '2026-10-24'}, {'title': 'Google Play Help: Disable apps that came with your Android device', 'url': 'https://support.google.com/googleplay/answer/13627571?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I uninstall an app on my Android phone?',
                    """You can remove it through the Play Store. It takes about a minute.

1. Open the **Play Store** app.
2. Tap your **profile icon** at the top right.
3. Tap **Manage apps & device**.
4. Tap **Manage**.
5. Tap the app you want to remove.
6. Tap **Uninstall**.

If you change your mind later, you can reinstall it from the Play Store without paying again.""",
                ],
            },
            {
                "existing": True, "id": 'tr059-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Google Play Help: Delete apps on your Android device', 'url': 'https://support.google.com/googleplay/answer/13627402?hl=en', 'accessed': '2026-10-24'}, {'title': 'Android Help: Free up storage on your Android device', 'url': 'https://support.google.com/android/answer/7431795?hl=en', 'accessed': '2026-10-24'}, {'title': 'Google Play Help: Disable apps that came with your Android device', 'url': 'https://support.google.com/googleplay/answer/13627571?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'my phone has apps I never use, can I get rid of them',
                    'Yes, you can remove them. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr059-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Play Help: Delete apps on your Android device', 'url': 'https://support.google.com/googleplay/answer/13627402?hl=en', 'accessed': '2026-10-24'}, {'title': 'Android Help: Free up storage on your Android device', 'url': 'https://support.google.com/android/answer/7431795?hl=en', 'accessed': '2026-10-24'}, {'title': 'Google Play Help: Disable apps that came with your Android device', 'url': 'https://support.google.com/googleplay/answer/13627571?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "When I bought my Android phone the store guy put a bunch of games and things on it that I'll never use, and they keep sending me notifications. How do I take them off?",
                    """You can remove most of them. Some apps that came built into the phone can only be turned off, not deleted, but most apps can be removed like this:

You can remove it through the Play Store. It takes about a minute.

1. Open the **Play Store** app.
2. Tap your **profile icon** at the top right.
3. Tap **Manage apps & device**.
4. Tap **Manage**.
5. Tap the app you want to remove.
6. Tap **Uninstall**.

If you change your mind later, you can reinstall it from the Play Store without paying again.""",
                ],
            },
            {
                "existing": True, "id": 'tr059-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Google Play Help: Delete apps on your Android device', 'url': 'https://support.google.com/googleplay/answer/13627402?hl=en', 'accessed': '2026-10-24'}, {'title': 'Android Help: Free up storage on your Android device', 'url': 'https://support.google.com/android/answer/7431795?hl=en', 'accessed': '2026-10-24'}, {'title': 'Google Play Help: Disable apps that came with your Android device', 'url': 'https://support.google.com/googleplay/answer/13627571?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'my phone has apps I never use, can I get rid of them',
                    'Yes, you can remove them. Is your phone an **iPhone** or an **Android** phone?',
                    'Android',
                    """Thanks. Here's one way that works on most Android phones.

You can remove it through the Play Store. It takes about a minute.

1. Open the **Play Store** app.
2. Tap your **profile icon** at the top right.
3. Tap **Manage apps & device**.
4. Tap **Manage**.
5. Tap the app you want to remove.
6. Tap **Uninstall**.

If you change your mind later, you can reinstall it from the Play Store without paying again.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-060', "task_type": 'delete_app', "task": 'Uninstall a program',
        "platform": 'Windows 11', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Microsoft Support: Uninstall or remove apps and programs in Windows', "url": 'https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98'},
        "examples": [
            {
                "existing": True, "id": 'tr060-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Uninstall or remove apps and programs in Windows', 'url': 'https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I uninstall a program from my Windows 11 computer?',
                    """Here's how. It takes a minute or two.

1. Click the **Start** button, then click **Settings**.
2. Click **Apps**.
3. Click **Installed apps**.
4. Find the program in the list.
5. Click the **three dots** next to it, then click **Uninstall**.
6. Confirm, and follow any instructions that appear.

**Another way:** click **Start**, then **All apps**, right-click the program, and choose **Uninstall**.""",
                ],
            },
            {
                "existing": True, "id": 'tr060-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Uninstall or remove apps and programs in Windows', 'url': 'https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I remove a program from my computer',
                    'I can help. Is your computer a **Windows** computer or a **Mac**?',
                ],
            },
            {
                "existing": True, "id": 'tr060-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'over_specified', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Uninstall or remove apps and programs in Windows', 'url': 'https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98', 'accessed': '2026-10-24'}],
                "messages": [
                    "Windows 11 Home, HP laptop. There's an old program called PhotoEasy that came preinstalled. I want it gone. Settings or Control Panel?",
                    """Settings is the easiest place on Windows 11. If PhotoEasy doesn't appear there, open **Control Panel** and use **Programs and Features** instead.

Here's how. It takes a minute or two.

1. Click the **Start** button, then click **Settings**.
2. Click **Apps**.
3. Click **Installed apps**.
4. Find the program in the list.
5. Click the **three dots** next to it, then click **Uninstall**.
6. Confirm, and follow any instructions that appear.

**Another way:** click **Start**, then **All apps**, right-click the program, and choose **Uninstall**.""",
                ],
            },
            {
                "existing": True, "id": 'tr060-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Uninstall or remove apps and programs in Windows', 'url': 'https://support.microsoft.com/en-us/windows/uninstall-or-remove-apps-and-programs-in-windows-4b55f974-2cc6-2d2b-d092-5905080eaf98', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I remove a program from my computer',
                    'I can help. Is your computer a **Windows** computer or a **Mac**?',
                    'Windows 11',
                    """Thanks.

Here's how. It takes a minute or two.

1. Click the **Start** button, then click **Settings**.
2. Click **Apps**.
3. Click **Installed apps**.
4. Find the program in the list.
5. Click the **three dots** next to it, then click **Uninstall**.
6. Confirm, and follow any instructions that appear.

**Another way:** click **Start**, then **All apps**, right-click the program, and choose **Uninstall**.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-061', "task_type": 'free_storage', "task": 'Free up storage space',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: How to check the storage on your iPhone and iPad', "url": 'https://support.apple.com/en-us/108429'},
        "examples": [
            {
                "existing": True, "id": 'tr061-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to check the storage on your iPhone and iPad', 'url': 'https://support.apple.com/en-us/108429', 'accessed': '2026-10-24'}],
                "messages": [
                    'My iPhone says storage is almost full. How do I free up space?',
                    """Let's see what's using the space first. This takes a few minutes.

1. Open the **Settings** app.
2. Tap **General**.
3. Tap **iPhone Storage**.
4. At the top, look at the **recommendations**. Tap one to see what it would remove, or tap **Show All** to see more.
5. Below that is a list of your apps. Tap an app to see your choices:
   - **Offload App** removes the app but keeps your documents and data, so nothing is lost if you reinstall it.
   - **Delete App** removes the app and its data.

Offloading apps you rarely use is a safe place to start.""",
                ],
            },
            {
                "existing": True, "id": 'tr061-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to check the storage on your iPhone and iPad', 'url': 'https://support.apple.com/en-us/108429', 'accessed': '2026-10-24'}],
                "messages": [
                    "my phone says it's full",
                    'I can help you free up some space. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr061-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: How to check the storage on your iPhone and iPad', 'url': 'https://support.apple.com/en-us/108429', 'accessed': '2026-10-24'}],
                "messages": [
                    "I wanted to take pictures at my grandson's graduation but my phone said not enough storage. I don't understand, I don't have that many things on it.",
                    """That's frustrating, especially at a big moment. Photos, videos, and apps can fill up space faster than you'd expect.

**Is your phone an iPhone or an Android phone?** Then I'll show you how to see what's using the space.""",
                ],
            },
            {
                "existing": True, "id": 'tr061-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to check the storage on your iPhone and iPad', 'url': 'https://support.apple.com/en-us/108429', 'accessed': '2026-10-24'}],
                "messages": [
                    "my phone says it's full",
                    'I can help you free up some space. Is your phone an **iPhone** or an **Android** phone?',
                    'iPhone 11',
                    """Thanks.

Let's see what's using the space first. This takes a few minutes.

1. Open the **Settings** app.
2. Tap **General**.
3. Tap **iPhone Storage**.
4. At the top, look at the **recommendations**. Tap one to see what it would remove, or tap **Show All** to see more.
5. Below that is a list of your apps. Tap an app to see your choices:
   - **Offload App** removes the app but keeps your documents and data, so nothing is lost if you reinstall it.
   - **Delete App** removes the app and its data.

Offloading apps you rarely use is a safe place to start.""",
                ],
            },
        ],
    },
]
