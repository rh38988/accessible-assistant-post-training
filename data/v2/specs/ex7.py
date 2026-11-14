"""Existing English drafts, group 7. Exported by export_spec.py; ids and provenance preserved."""
TASKS = [
    {
        "task_id": 'TR-089', "task_type": 'government_impersonation', "task": 'Caller claims to be from Social Security',
        "platform": 'phone', "category": 'online_services', "sensitive": True,
        "source": {"title": 'FTC Consumer Advice: How To Avoid a Government Impersonation Scam', "url": 'https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam'},
        "examples": [
            {
                "existing": True, "id": 'tr089-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'phone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: How To Avoid a Government Impersonation Scam', 'url': 'https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam', 'accessed': '2026-10-24'}],
                "messages": [
                    "A caller said he's from Social Security and my number has been suspended because of a crime. He wants me to buy gift cards to fix it. What should I do?",
                    """Please **hang up and don't pay anything**. This is a scam. The real Social Security Administration **won't threaten you, won't suspend your Social Security number, and won't ask you to pay with gift cards**.

**What to do:**
1. **Hang up.** Don't share any personal or bank information.
2. Don't trust caller ID. Scammers can make it show a government name or number.
3. If you're worried, **call Social Security yourself** using the phone number on its official website, not a number the caller gave you.
4. **Report the call** to the Social Security Administration's Office of the Inspector General and to the FTC at **ReportFraud.ftc.gov**.

If you already shared your Social Security number or bank details, go to **IdentityTheft.gov** for next steps, and tell me so I can help.""",
                ],
            },
            {
                "existing": True, "id": 'tr089-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: How To Avoid a Government Impersonation Scam', 'url': 'https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam', 'accessed': '2026-10-24'}],
                "messages": [
                    'Got a call from the government saying I owe money. Is that real?',
                    "Please don't pay or share any personal information yet, and don't call back any number they gave you. **Which agency did the caller say they were from?**",
                ],
            },
            {
                "existing": True, "id": 'tr089-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft, edited by Ryan Hsieh', "reviewed": True, "inspired_by": 'OATS',
                "sources": [{'title': 'FTC Consumer Advice: How To Avoid a Government Impersonation Scam', 'url': 'https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam', 'accessed': '2026-10-24'}],
                "messages": [
                    'social security called me',
                    """Okay, let's make sure it was really them. Until we know, please don't give them any money or personal information.

**Did the caller ask you for money or personal information?**""",
                ],
            },
            {
                "existing": True, "id": 'tr089-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'phone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: How To Avoid a Government Impersonation Scam', 'url': 'https://consumer.ftc.gov/articles/how-avoid-government-impersonation-scam', 'accessed': '2026-10-24'}],
                "messages": [
                    'Got a call from the government saying I owe money. Is that real?',
                    "Please don't pay or share any personal information yet, and don't call back any number they gave you. **Which agency did the caller say they were from?**",
                    'Social Security. They said I need to buy gift cards or my number will be suspended.',
                    """Thank you.

Please **hang up and don't pay anything**. This is a scam. The real Social Security Administration **won't threaten you, won't suspend your Social Security number, and won't ask you to pay with gift cards**.

**What to do:**
1. **Hang up.** Don't share any personal or bank information.
2. Don't trust caller ID. Scammers can make it show a government name or number.
3. If you're worried, **call Social Security yourself** using the phone number on its official website, not a number the caller gave you.
4. **Report the call** to the Social Security Administration's Office of the Inspector General and to the FTC at **ReportFraud.ftc.gov**.

If you already shared your Social Security number or bank details, go to **IdentityTheft.gov** for next steps, and tell me so I can help.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-090', "task_type": 'strong_passwords', "task": 'Make a strong password',
        "platform": 'any', "category": 'online_services', "sensitive": True,
        "source": {"title": 'FTC Consumer Advice: Creating Strong Passwords and Other Ways To Protect Your Accounts', "url": 'https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts'},
        "examples": [
            {
                "existing": True, "id": 'tr090-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: Creating Strong Passwords and Other Ways To Protect Your Accounts', 'url': 'https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I make a strong password that I can actually remember?',
                    """You may find it easier to use a **passphrase**: a series of random words separated by spaces. It may be easier to remember.

**Tips for a strong password:**
1. **Make it long**, at least 12 characters. Make sure the words in a passphrase are random.
2. **If a company tells you it lost your password in a data breach, change it right away.** If you used the same or a similar password on other sites, change it there too.
3. **Avoid common phrases, song lyrics, or movie quotes**, because hacking programs can guess them.
4. **A password manager, or your web browser,** can create strong passwords and save them for you.
5. **Turn on two-factor authentication** where you can. Then a hacker who steals your password still can't log in without another step. Text or email codes are the least secure type, so an authenticator app or security key is better if you can use one.

Protect your **email** account with a strong password, because a hacker who takes it over can get password reset links for your other accounts.""",
                ],
            },
            {
                "existing": True, "id": 'tr090-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: Creating Strong Passwords and Other Ways To Protect Your Accounts', 'url': 'https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts', 'accessed': '2026-10-24'}],
                "messages": [
                    'Can you help me with my passwords?',
                    'Of course. What would you like help with: **making a strong new password**, **keeping track of the ones you have**, or **resetting one you forgot**?',
                ],
            },
            {
                "existing": True, "id": 'tr090-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'FTC Consumer Advice: Creating Strong Passwords and Other Ways To Protect Your Accounts', 'url': 'https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts', 'accessed': '2026-10-24'}],
                "messages": [
                    "I use my dog's name and my birthday for everything because that's the only way I remember. My grandson says that's not safe. What should I do instead?",
                    """A long passphrase of random words can be strong and still easy to remember. Here are some tips for choosing a new one.

You may find it easier to use a **passphrase**: a series of random words separated by spaces. It may be easier to remember.

**Tips for a strong password:**
1. **Make it long**, at least 12 characters. Make sure the words in a passphrase are random.
2. **If a company tells you it lost your password in a data breach, change it right away.** If you used the same or a similar password on other sites, change it there too.
3. **Avoid common phrases, song lyrics, or movie quotes**, because hacking programs can guess them.
4. **A password manager, or your web browser,** can create strong passwords and save them for you.
5. **Turn on two-factor authentication** where you can. Then a hacker who steals your password still can't log in without another step. Text or email codes are the least secure type, so an authenticator app or security key is better if you can use one.

Protect your **email** account with a strong password, because a hacker who takes it over can get password reset links for your other accounts.""",
                ],
            },
            {
                "existing": True, "id": 'tr090-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: Creating Strong Passwords and Other Ways To Protect Your Accounts', 'url': 'https://consumer.ftc.gov/articles/creating-strong-passwords-and-other-ways-protect-your-accounts', 'accessed': '2026-10-24'}],
                "messages": [
                    'Can you help me with my passwords?',
                    'Of course. What would you like help with: **making a strong new password**, **keeping track of the ones you have**, or **resetting one you forgot**?',
                    'Making a strong new one that I can remember.',
                    """Sure.

You may find it easier to use a **passphrase**: a series of random words separated by spaces. It may be easier to remember.

**Tips for a strong password:**
1. **Make it long**, at least 12 characters. Make sure the words in a passphrase are random.
2. **If a company tells you it lost your password in a data breach, change it right away.** If you used the same or a similar password on other sites, change it there too.
3. **Avoid common phrases, song lyrics, or movie quotes**, because hacking programs can guess them.
4. **A password manager, or your web browser,** can create strong passwords and save them for you.
5. **Turn on two-factor authentication** where you can. Then a hacker who steals your password still can't log in without another step. Text or email codes are the least secure type, so an authenticator app or security key is better if you can use one.

Protect your **email** account with a strong password, because a hacker who takes it over can get password reset links for your other accounts.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-091', "task_type": 'maps_directions', "task": 'Get directions',
        "platform": 'Google Maps (phone)', "category": 'online_services', "sensitive": False,
        "source": {"title": 'Google Maps Help: Get directions & show routes (Android)', "url": 'https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid'},
        "examples": [
            {
                "existing": True, "id": 'tr091-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Google Maps (phone)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Google Maps Help: Get directions & show routes (Android)', 'url': 'https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    "How do I get directions to my doctor's office in Google Maps on my Android phone?",
                    """Here's how. It takes about a minute.

1. Open the **Google Maps** app.
2. Search for your destination, or tap it on the map.
3. Tap **Directions** at the bottom left.
4. Choose how you're traveling: **driving**, **transit**, or **walking**.
5. Pick a route. The best route is shown in **blue**, and other options are gray.

To see the list of steps, swipe up on the route panel. To see a turn-by-turn preview, tap **Preview**.""",
                ],
            },
            {
                "existing": True, "id": 'tr091-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Google Maps Help: Get directions & show routes (Android)', 'url': 'https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I find my way to a new place',
                    'I can help. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr091-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Maps Help: Get directions & show routes (Android)', 'url': 'https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'directions to',
                    'It looks like your message got cut off. Are you using an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr091-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Google Maps (phone)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Google Maps Help: Get directions & show routes (Android)', 'url': 'https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I find my way to a new place',
                    'I can help. Is your phone an **iPhone** or an **Android** phone?',
                    'Android, and I use Google Maps',
                    """Great.

Here's how. It takes about a minute.

1. Open the **Google Maps** app.
2. Search for your destination, or tap it on the map.
3. Tap **Directions** at the bottom left.
4. Choose how you're traveling: **driving**, **transit**, or **walking**.
5. Pick a route. The best route is shown in **blue**, and other options are gray.

To see the list of steps, swipe up on the route panel. To see a turn-by-turn preview, tap **Preview**.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-093', "task_type": 'join_video_meeting', "task": 'Join a Zoom meeting from a link',
        "platform": 'Zoom', "category": 'communication', "sensitive": False,
        "source": {"title": 'Zoom Support: Joining a meeting with the invite link', "url": 'https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180'},
        "examples": [
            {
                "existing": True, "id": 'tr093-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Zoom',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Zoom Support: Joining a meeting with the invite link', 'url': 'https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180', 'accessed': '2026-10-24'}],
                "messages": [
                    'My book club meets on Zoom now and they emailed me a link. How do I join from my computer?',
                    """Joining with a link is pretty simple.

1. Open the email and **click the Zoom link**.
2. Your web browser opens a page, and a small box (pop-up) asks whether you want to open **Zoom Meetings**.
3. Click **Open**. Depending on your browser, the button may read **Allow** or **Open zoom.us**.
4. The Zoom app will open and take you into the meeting.

If the link already includes the passcode, you won't need to type one.

If Zoom doesn't open, or you don't have the Zoom app yet, tell me what you see on the screen and I'll help.""",
                ],
            },
            {
                "existing": True, "id": 'tr093-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Zoom Support: Joining a meeting with the invite link', 'url': 'https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I get on a zoom call',
                    'Happy to help. Did someone send you a **link** to the meeting, in an email or a text?',
                ],
            },
            {
                "existing": True, "id": 'tr093-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'Zoom',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Zoom Support: Joining a meeting with the invite link', 'url': 'https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180', 'accessed': '2026-10-24'}],
                "messages": [
                    "Since my knees got bad I can't drive to my book club anymore, so the ladies started doing it on Zoom. My friend emailed me the link for Thursday but I've never done a Zoom before and I'm nervous I'll mess it up.",
                    """You won't mess it up, and it's lovely that your book club found a way to keep you in. Here's what to do on Thursday:

Joining with a link is pretty simple.

1. Open the email and **click the Zoom link**.
2. Your web browser opens a page, and a small box (pop-up) asks whether you want to open **Zoom Meetings**.
3. Click **Open**. Depending on your browser, the button may read **Allow** or **Open zoom.us**.
4. The Zoom app will open and take you into the meeting.

If the link already includes the passcode, you won't need to type one.

If Zoom doesn't open, or you don't have the Zoom app yet, tell me what you see on the screen and I'll help.""",
                ],
            },
            {
                "existing": True, "id": 'tr093-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Zoom',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Zoom Support: Joining a meeting with the invite link', 'url': 'https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I get on a zoom call',
                    'Happy to help. Did someone send you a **link** to the meeting, in an email or a text?',
                    "Yes, I have a link in my email.",
                    """Great, having the link makes it easy.

Joining with a link is pretty simple.

1. Open the email and **click the Zoom link**.
2. Your web browser opens a page, and a small box (pop-up) asks whether you want to open **Zoom Meetings**.
3. Click **Open**. Depending on your browser, the button may read **Allow** or **Open zoom.us**.
4. The Zoom app will open and take you into the meeting.

If the link already includes the passcode, you won't need to type one.

If Zoom doesn't open, or you don't have the Zoom app yet, tell me what you see on the screen and I'll help.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-094', "task_type": 'video_captions', "task": 'Turn on captions',
        "platform": 'YouTube', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'YouTube Help: Manage caption settings (Android)', "url": 'https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid'},
        "examples": [
            {
                "existing": True, "id": 'tr094-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'YouTube',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'YouTube Help: Manage caption settings (Android)', 'url': 'https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    "How do I turn on captions for a YouTube video on my phone? I can't hear it well.",
                    """Here's how. It takes a few seconds.

1. Start the video in the **YouTube** app.
2. Tap the video once so the controls appear.
3. Tap the **CC** button (closed captions) to turn captions on.
4. Tap it again if you want to turn them off.

If you don't see a **CC** button, that video doesn't have captions available.""",
                ],
            },
            {
                "existing": True, "id": 'tr094-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'YouTube Help: Manage caption settings (Android)', 'url': 'https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'can I see the words on videos',
                    'Yes, you can turn on captions. Where are you watching: **YouTube**, another app, or on **TV**?',
                ],
            },
            {
                "existing": True, "id": 'tr094-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'YouTube Help: Manage caption settings (Android)', 'url': 'https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'captions',
                    'Sure. Where would you like to turn on captions: **YouTube**, a **video call**, your **phone** in general, or somewhere else?',
                ],
            },
            {
                "existing": True, "id": 'tr094-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'YouTube',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'YouTube Help: Manage caption settings (Android)', 'url': 'https://support.google.com/youtube/answer/100078?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'can I see the words on videos',
                    'Yes, you can turn on captions. Where are you watching: **YouTube**, another app, or on **TV**?',
                    'YouTube on my phone',
                    """Great.

Here's how. It takes a few seconds.

1. Start the video in the **YouTube** app.
2. Tap the video once so the controls appear.
3. Tap the **CC** button (closed captions) to turn captions on.
4. Tap it again if you want to turn them off.

If you don't see a **CC** button, that video doesn't have captions available.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-095', "task_type": 'backup_phone', "task": 'Back up the whole phone',
        "platform": 'iPhone (iCloud Backup)', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: How to back up your iPhone or iPad with iCloud', "url": 'https://support.apple.com/en-us/108366'},
        "examples": [
            {
                "existing": True, "id": 'tr095-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone (iCloud Backup)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to back up your iPhone or iPad with iCloud', 'url': 'https://support.apple.com/en-us/108366', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I back up my whole iPhone to iCloud before I get a new phone?',
                    """Here's how to make a full backup. Do this on Wi-Fi. The first backup can take a while.

1. Connect your iPhone to **Wi-Fi**.
2. Open **Settings** and tap **your name**.
3. Tap **iCloud**.
4. Tap **iCloud Backup**.
5. Make sure **Back Up This iPhone** is turned on.
6. Tap **Back Up Now**.
7. Stay connected to Wi-Fi until it finishes.

When it's done, you'll see the date and time of the last backup under **Back Up Now**.

If you see a message about not enough iCloud storage, you'll need more storage before the backup can finish. Tell me and we'll look at your options.""",
                ],
            },
            {
                "existing": True, "id": 'tr095-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to back up your iPhone or iPad with iCloud', 'url': 'https://support.apple.com/en-us/108366', 'accessed': '2026-10-24'}],
                "messages": [
                    "how do I make sure I don't lose anything on my phone",
                    'A backup will protect your things. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr095-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: How to back up your iPhone or iPad with iCloud', 'url': 'https://support.apple.com/en-us/108366', 'accessed': '2026-10-24'}],
                "messages": [
                    "My phone is getting old and my son is going to help me switch to a new one next month. I'm scared I'll lose my pictures and messages from my late husband.",
                    """Those are precious, and it's wise to protect them before switching. A backup saves a copy of everything.

**Is your phone an iPhone or an Android phone?** Then I'll walk you through backing it up.""",
                ],
            },
            {
                "existing": True, "id": 'tr095-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone (iCloud Backup)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to back up your iPhone or iPad with iCloud', 'url': 'https://support.apple.com/en-us/108366', 'accessed': '2026-10-24'}],
                "messages": [
                    "how do I make sure I don't lose anything on my phone",
                    'A backup will protect your things. Is your phone an **iPhone** or an **Android** phone?',
                    'iPhone',
                    """Thanks. An iCloud backup saves a copy of your iPhone.

Here's how to make a full backup. Do this on Wi-Fi. The first backup can take a while.

1. Connect your iPhone to **Wi-Fi**.
2. Open **Settings** and tap **your name**.
3. Tap **iCloud**.
4. Tap **iCloud Backup**.
5. Make sure **Back Up This iPhone** is turned on.
6. Tap **Back Up Now**.
7. Stay connected to Wi-Fi until it finishes.

When it's done, you'll see the date and time of the last backup under **Back Up Now**.

If you see a message about not enough iCloud storage, you'll need more storage before the backup can finish. Tell me and we'll look at your options.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-096', "task_type": 'stolen_device_protection', "task": 'Turn on Stolen Device Protection',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": True,
        "source": {"title": 'Apple Support: About Stolen Device Protection for iPhone', "url": 'https://support.apple.com/en-us/120340'},
        "examples": [
            {
                "existing": True, "id": 'tr096-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Apple Support: About Stolen Device Protection for iPhone', 'url': 'https://support.apple.com/en-us/120340', 'accessed': '2026-10-24'}],
                "messages": [
                    'What is Stolen Device Protection on iPhone and how do I turn it on?',
                    """Stolen Device Protection adds extra security if someone steals your iPhone **and** knows your passcode. When your phone is away from familiar places like home or work, it requires **Face ID or Touch ID** for things like using saved passwords, and it adds a **one-hour wait** before important changes, like changing your Apple Account password.

**To turn it on:**
1. Open **Settings**.
2. Tap **Face ID & Passcode** (or **Touch ID & Passcode**).
3. Enter your passcode.
4. Tap **Stolen Device Protection** and turn it on.

It may already be on, so check first.

It needs a few things to work: an iPhone updated to **iOS 17.3 or later**, a passcode, Face ID or Touch ID, two-factor authentication on your Apple Account, **Find My** turned on, and **Significant Locations** turned on in Location Services.""",
                ],
            },
            {
                "existing": True, "id": 'tr096-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Apple Support: About Stolen Device Protection for iPhone', 'url': 'https://support.apple.com/en-us/120340', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I protect my phone if it gets stolen',
                    "Good thing to set up ahead of time. Is your phone an **iPhone** or an **Android** phone?",
                ],
            },
            {
                "existing": True, "id": 'tr096-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: About Stolen Device Protection for iPhone', 'url': 'https://support.apple.com/en-us/120340', 'accessed': '2026-10-24'}],
                "messages": [
                    'stolen device',
                    "Do you want to turn on **Stolen Device Protection**, the iPhone setting that helps protect your phone if it is stolen?",
                ],
            },
            {
                "existing": True, "id": 'tr096-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'Apple Support: About Stolen Device Protection for iPhone', 'url': 'https://support.apple.com/en-us/120340', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I protect my phone if it gets stolen',
                    "Good thing to set up ahead of time. Is your phone an **iPhone** or an **Android** phone?",
                    'iPhone',
                    """Great. A helpful setting is called Stolen Device Protection.

Stolen Device Protection adds extra security if someone steals your iPhone **and** knows your passcode. When your phone is away from familiar places like home or work, it requires **Face ID or Touch ID** for things like using saved passwords, and it adds a **one-hour wait** before important changes, like changing your Apple Account password.

**To turn it on:**
1. Open **Settings**.
2. Tap **Face ID & Passcode** (or **Touch ID & Passcode**).
3. Enter your passcode.
4. Tap **Stolen Device Protection** and turn it on.

It may already be on, so check first.

It needs a few things to work: an iPhone updated to **iOS 17.3 or later**, a passcode, Face ID or Touch ID, two-factor authentication on your Apple Account, **Find My** turned on, and **Significant Locations** turned on in Location Services.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-097', "task_type": 'live_captions', "task": 'Turn on live captions',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Accessibility Help: Live Caption', "url": 'https://support.google.com/accessibility/android/answer/9350862?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr097-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: Live Caption', 'url': 'https://support.google.com/accessibility/android/answer/9350862?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I turn on Live Caption on my Android phone so I can read what people say in videos?',
                    """**Live Caption** shows captions for videos and calls on your phone. It takes about a minute to turn on.

**Quick way:**
1. Press a **volume button** on the side of your phone.
2. Under the volume controls, tap **More**.
3. Tap **Live Caption**, then **Done**.

**In Settings:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Live Caption** and turn it on.

Connect to Wi-Fi the first time you use it, so your phone can download what it needs.

If you can't find **Live Caption**, search for it in Settings.""",
                ],
            },
            {
                "existing": True, "id": 'tr097-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: Live Caption', 'url': 'https://support.google.com/accessibility/android/answer/9350862?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "I can't hear people on videos well, can my phone show the words?",
                    "Yes, many phones can show captions for what's being said. Is your phone an **iPhone** or an **Android** phone?",
                ],
            },
            {
                "existing": True, "id": 'tr097-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Accessibility Help: Live Caption', 'url': 'https://support.google.com/accessibility/android/answer/9350862?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "My hearing isn't what it used to be and my grandkids send me videos all the time. I just nod along but I can't make out what they're saying.",
                    """Your phone may be able to show captions for those videos so you can read along.

**Is your phone an iPhone or an Android phone?**""",
                ],
            },
            {
                "existing": True, "id": 'tr097-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: Live Caption', 'url': 'https://support.google.com/accessibility/android/answer/9350862?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "I can't hear people on videos well, can my phone show the words?",
                    "Yes, many phones can show captions for what's being said. Is your phone an **iPhone** or an **Android** phone?",
                    'Android, a Pixel',
                    """Thanks. On Android, this is called Live Caption.

**Live Caption** shows captions for videos and calls on your phone. It takes about a minute to turn on.

**Quick way:**
1. Press a **volume button** on the side of your phone.
2. Under the volume controls, tap **More**.
3. Tap **Live Caption**, then **Done**.

**In Settings:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Live Caption** and turn it on.

Connect to Wi-Fi the first time you use it, so your phone can download what it needs.

If you can't find **Live Caption**, search for it in Settings.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-098', "task_type": 'text_size', "task": 'Make text bigger',
        "platform": 'Windows 11', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Microsoft Support: Make text and apps bigger', "url": 'https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64'},
        "examples": [
            {
                "existing": True, "id": 'tr098-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Make text and apps bigger', 'url': 'https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I make just the text bigger on my Windows 11 computer?',
                    """You can make the text bigger without changing anything else. It takes about a minute.

1. Click the **Start** button, then **Settings**.
2. Click **Accessibility**.
3. Click **Text size**.
4. Drag the slider to the right until the sample text is easy to read.
5. Click **Apply**.

Windows will make the text bigger everywhere.

Tip: you can also open Accessibility settings by holding the **Windows logo key** and pressing **U**.

If you want everything bigger, including pictures and buttons, there's a separate **Scale** setting under **Display**. Tell me if you'd like that instead.""",
                ],
            },
            {
                "existing": True, "id": 'tr098-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Make text and apps bigger', 'url': 'https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64', 'accessed': '2026-10-24'}],
                "messages": [
                    'the writing on my computer is too small',
                    'I can help you make it bigger. Is your computer a **Windows** computer or a **Mac**?',
                ],
            },
            {
                "existing": True, "id": 'tr098-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Make text and apps bigger', 'url': 'https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64', 'accessed': '2026-10-24'}],
                "messages": [
                    'make text',
                    'It looks like your message got cut off. Do you want to make the text bigger on a **computer** or on a **phone**?',
                ],
            },
            {
                "existing": True, "id": 'tr098-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Make text and apps bigger', 'url': 'https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64', 'accessed': '2026-10-24'}],
                "messages": [
                    'the writing on my computer is too small',
                    'I can help you make it bigger. Is your computer a **Windows** computer or a **Mac**?',
                    'Windows 11, just the text',
                    """Got it.

You can make the text bigger without changing anything else. It takes about a minute.

1. Click the **Start** button, then **Settings**.
2. Click **Accessibility**.
3. Click **Text size**.
4. Drag the slider to the right until the sample text is easy to read.
5. Click **Apply**.

Windows will make the text bigger everywhere.

Tip: you can also open Accessibility settings by holding the **Windows logo key** and pressing **U**.

If you want everything bigger, including pictures and buttons, there's a separate **Scale** setting under **Display**. Tell me if you'd like that instead.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-099', "task_type": 'phone_not_charging', "task": 'iPhone stops charging at 80%',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": "Apple Support: If your iPhone or iPod touch won't charge", "url": 'https://support.apple.com/en-ca/108805'},
        "examples": [
            {
                "existing": True, "id": 'tr099-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': "Apple Support: If your iPhone or iPod touch won't charge", 'url': 'https://support.apple.com/en-ca/108805', 'accessed': '2026-10-24'}],
                "messages": [
                    'Why does my iPhone stop charging at 80% overnight? Is something wrong with it?',
                    """Most likely nothing is wrong. This is usually a feature called **Optimized Battery Charging**. It holds the battery at 80% during long charges, like overnight, to slow down battery wear. Your iPhone then finishes charging around the time you usually unplug it.

A couple of other things can also stop charging at 80%:
- **Heat:** if your iPhone gets too warm, it may pause charging above 80%. Moving it to a cooler spot helps.
- **Charge limit:** on iPhone 15 and newer, a charge limit setting may be turned on. You can change it if you want a full charge.

If you need a full charge right away, tell me and I'll walk you through it.""",
                ],
            },
            {
                "existing": True, "id": 'tr099-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': "Apple Support: If your iPhone or iPod touch won't charge", 'url': 'https://support.apple.com/en-ca/108805', 'accessed': '2026-10-24'}],
                "messages": [
                    "my phone won't charge all the way",
                    "Let's figure out why. Is your phone an **iPhone** or an **Android** phone?",
                ],
            },
            {
                "existing": True, "id": 'tr099-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': "Apple Support: If your iPhone or iPod touch won't charge", 'url': 'https://support.apple.com/en-ca/108805', 'accessed': '2026-10-24'}],
                "messages": [
                    'I plug in my iPhone every night before bed and when I wake up it says 80% and charging is on hold or something. I thought my charger was broken so I bought a new one but it does the same thing.',
                    """Your charger is probably fine.

Most likely nothing is wrong. This is usually a feature called **Optimized Battery Charging**. It holds the battery at 80% during long charges, like overnight, to slow down battery wear. Your iPhone then finishes charging around the time you usually unplug it.

A couple of other things can also stop charging at 80%:
- **Heat:** if your iPhone gets too warm, it may pause charging above 80%. Moving it to a cooler spot helps.
- **Charge limit:** on iPhone 15 and newer, a charge limit setting may be turned on. You can change it if you want a full charge.

If you need a full charge right away, tell me and I'll walk you through it.""",
                ],
            },
            {
                "existing": True, "id": 'tr099-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': "Apple Support: If your iPhone or iPod touch won't charge", 'url': 'https://support.apple.com/en-ca/108805', 'accessed': '2026-10-24'}],
                "messages": [
                    "my phone won't charge all the way",
                    "Let's figure out why. Is your phone an **iPhone** or an **Android** phone?",
                    'iPhone, it always stops at 80%',
                    """Thanks, that detail helps.

Most likely nothing is wrong. This is usually a feature called **Optimized Battery Charging**. It holds the battery at 80% during long charges, like overnight, to slow down battery wear. Your iPhone then finishes charging around the time you usually unplug it.

A couple of other things can also stop charging at 80%:
- **Heat:** if your iPhone gets too warm, it may pause charging above 80%. Moving it to a cooler spot helps.
- **Charge limit:** on iPhone 15 and newer, a charge limit setting may be turned on. You can change it if you want a full charge.

If you need a full charge right away, tell me and I'll walk you through it.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-101', "task_type": 'ring_volume', "task": 'Phone only vibrates, does not ring',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Use the volume buttons, side button, and other controls on your iPhone', "url": 'https://support.apple.com/en-us/105103'},
        "examples": [
            {
                "existing": True, "id": 'tr101-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft, edited by Ryan Hsieh', "reviewed": True, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use the volume buttons, side button, and other controls on your iPhone', 'url': 'https://support.apple.com/en-us/105103', 'accessed': '2026-10-24'}],
                "messages": [
                    "My iPhone only vibrates when someone calls. It doesn't ring. How do I fix that?",
                    """Your iPhone is probably in **Silent mode**. Here's how to check.

**If your iPhone has a small switch on the side** (above the volume buttons):
1. Look at the switch. If you see **orange**, Silent mode is on.
2. Flip the switch so the orange no longer shows.

**If your iPhone has an Action button instead** (iPhone 15 Pro and newer):
1. **Press and hold** the **Action button** until you see Silent mode turn off at the top of the screen. By default, this button turns Silent mode on and off. If it's been set to do something else, tell me and we'll check another way.

Once Silent mode is off, your phone will ring again. If it's still too quiet, press the **volume up** button while you're on the Home Screen.""",
                ],
            },
            {
                "existing": True, "id": 'tr101-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use the volume buttons, side button, and other controls on your iPhone', 'url': 'https://support.apple.com/en-us/105103', 'accessed': '2026-10-24'}],
                "messages": [
                    "my phone isn't ringing, only buzzing",
                    'That usually means a silent setting is on. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr101-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Use the volume buttons, side button, and other controls on your iPhone', 'url': 'https://support.apple.com/en-us/105103', 'accessed': '2026-10-24'}],
                "messages": [
                    'phone wont ring just',
                    'It sounds like your phone only vibrates when someone calls. Is it an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr101-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use the volume buttons, side button, and other controls on your iPhone', 'url': 'https://support.apple.com/en-us/105103', 'accessed': '2026-10-24'}],
                "messages": [
                    "my phone isn't ringing, only buzzing",
                    'That usually means a silent setting is on. Is your phone an **iPhone** or an **Android** phone?',
                    'iPhone 13',
                    """Thanks.

Your iPhone is probably in **Silent mode**. Here's how to check.

1. Look at the switch on the side of your iPhone. If you see **orange**, Silent mode is on.
2. Flip the switch so the orange no longer shows.

Once Silent mode is off, your phone will ring again. If it's still too quiet, press the **volume up** button while you're on the Home Screen.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-102', "task_type": 'read_aloud', "task": 'Have the phone read the screen aloud',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Accessibility Help: Use Select to Speak', "url": 'https://support.google.com/accessibility/android/answer/7349565?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr102-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: Use Select to Speak', 'url': 'https://support.google.com/accessibility/android/answer/7349565?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'Can my Android phone read the words on the screen out loud to me?',
                    """Yes, with a feature called **Select to Speak**. Setting it up takes a couple of minutes.

**Turn it on:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Select to Speak**.
4. Turn on the **Select to Speak shortcut**.

If you don't see **Select to Speak**, update the **Android Accessibility Suite** app in the Play Store.

**Use it:**
1. Start it with the shortcut: swipe up with **two fingers**, or tap the **Accessibility button**.
2. Tap any text you want to hear.
3. To hear everything on the screen, tap **Play**.""",
                ],
            },
            {
                "existing": True, "id": 'tr102-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: Use Select to Speak', 'url': 'https://support.google.com/accessibility/android/answer/7349565?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'is there a way to have my phone read things to me',
                    'Most phones can. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr102-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Accessibility Help: Use Select to Speak', 'url': 'https://support.google.com/accessibility/android/answer/7349565?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "Reading long emails on my phone tires out my eyes. I'd love it if the phone could just read them to me like an audiobook.",
                    """Many phones can read text out loud.

**Is your phone an iPhone or an Android phone?** I'll show you how to turn it on.""",
                ],
            },
            {
                "existing": True, "id": 'tr102-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: Use Select to Speak', 'url': 'https://support.google.com/accessibility/android/answer/7349565?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'is there a way to have my phone read things to me',
                    'Most phones can. Is your phone an **iPhone** or an **Android** phone?',
                    'Android',
                    """Thanks.

Yes, with a feature called **Select to Speak**. Setting it up takes a couple of minutes.

**Turn it on:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Select to Speak**.
4. Turn on the **Select to Speak shortcut**.

If you don't see **Select to Speak**, update the **Android Accessibility Suite** app in the Play Store.

**Use it:**
1. Start it with the shortcut: swipe up with **two fingers**, or tap the **Accessibility button**.
2. Tap any text you want to hear.
3. To hear everything on the screen, tap **Play**.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-103', "task_type": 'reminders', "task": 'Set a reminder',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Use Reminders on your iPhone, iPad, or iPod touch', "url": 'https://support.apple.com/en-us/102484'},
        "examples": [
            {
                "existing": True, "id": 'tr103-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use Reminders on your iPhone, iPad, or iPod touch', 'url': 'https://support.apple.com/en-us/102484', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I set a reminder on my iPhone to call the pharmacy tomorrow at 10 AM?',
                    """You can use the **Reminders** app. It takes about a minute.

1. Open the **Reminders** app.
2. Tap **New Reminder**.
3. Type what you want to remember, like **Call the pharmacy**.
4. Tap the **Date and Time** button.
5. To set your own day and time, tap **Custom**.
6. Choose tomorrow's date.
7. Set the time to **10:00 AM**.

Your iPhone will show a reminder at that time.

If you set a date without a time, the reminder comes at 9:00 AM by default.""",
                ],
            },
            {
                "existing": True, "id": 'tr103-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use Reminders on your iPhone, iPad, or iPod touch', 'url': 'https://support.apple.com/en-us/102484', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I get my phone to remind me to do something',
                    'Sure. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr103-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Use Reminders on your iPhone, iPad, or iPod touch', 'url': 'https://support.apple.com/en-us/102484', 'accessed': '2026-10-24'}],
                "messages": [
                    'I keep forgetting to call in my prescription refill and then I run out. Tomorrow at 10 is when they open. Can my iPhone remind me?',
                    """Yes, a reminder will help with that. Here's how to set it for tomorrow at 10:

You can use the **Reminders** app. It takes about a minute.

1. Open the **Reminders** app.
2. Tap **New Reminder**.
3. Type what you want to remember, like **Call the pharmacy**.
4. Tap the **Date and Time** button.
5. To set your own day and time, tap **Custom**.
6. Choose tomorrow's date.
7. Set the time to **10:00 AM**.

Your iPhone will show a reminder at that time.

If you set a date without a time, the reminder comes at 9:00 AM by default.""",
                ],
            },
            {
                "existing": True, "id": 'tr103-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Use Reminders on your iPhone, iPad, or iPod touch', 'url': 'https://support.apple.com/en-us/102484', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I get my phone to remind me to do something',
                    'Sure. Is your phone an **iPhone** or an **Android** phone?',
                    'iPhone. Call the pharmacy tomorrow at 10.',
                    """Got it.

You can use the **Reminders** app. It takes about a minute.

1. Open the **Reminders** app.
2. Tap **New Reminder**.
3. Type what you want to remember, like **Call the pharmacy**.
4. Tap the **Date and Time** button.
5. To set your own day and time, tap **Custom**.
6. Choose tomorrow's date.
7. Set the time to **10:00 AM**.

Your iPhone will show a reminder at that time.

If you set a date without a time, the reminder comes at 9:00 AM by default.""",
                ],
            },
        ],
    },
]
