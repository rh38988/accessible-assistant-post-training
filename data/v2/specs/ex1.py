"""Existing English drafts, group 1. Exported by export_spec.py; ids and provenance preserved."""
TASKS = [
    {
        "task_id": 'TR-001', "task_type": 'text_size', "task": 'Make text bigger',
        "platform": 'Samsung Galaxy', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Samsung Support: How to adjust the font size and style on your Galaxy phone', "url": 'https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/'},
        "examples": [
            {
                "existing": True, "id": 'pilot-001', "suffix": 'p', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Samsung Galaxy (Android)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Samsung Support: How to adjust the font size and style on your Galaxy phone', 'url': 'https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/', 'accessed': '2026-10-24'}],
                "messages": [
                    'the letters on my samsung phone are so tiny i cant read my messages. how do i make them bigger',
                    """You can make the letters bigger in your phone's settings. It takes about a minute, and you can change it back anytime.

1. Find the **Settings** app and tap it. Its icon looks like a gear.
2. Tap **Display**.
3. Tap **Font size and style**.
4. Find the font size slider and slide it to the right to make the letters bigger.

The sample words on the screen change size as you slide, so you can stop when they are easy to read. Your messages will use the bigger size too.

Menu names can be a little different on some Samsung models. If you don't see **Font size and style** after tapping **Display**, tell me what you see and I'll help you find it.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-002', "task_type": 'ring_volume', "task": 'Turn up ring volume (device unknown)',
        "platform": 'unknown', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Change volume, sound & vibrate settings', "url": 'https://support.google.com/android/answer/9082609?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'pilot-002', "suffix": 'p', "scenario": 'missing_info',
                "style": 'plain', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Change volume, sound & vibrate settings', 'url': 'https://support.google.com/android/answer/9082609?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "My phone hardly makes any sound when someone calls and I keep missing calls from my doctor's office.",
                    """I'm sorry you've been missing those calls. I can help you make the ringing louder.

First, one quick question: is your phone an **iPhone**, or another kind of phone, like a Samsung or Google Pixel?

If you're not sure, look at the back of the phone. An iPhone has an apple logo on the back.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-003', "task_type": 'send_photo_text', "task": 'Send a photo by text message',
        "platform": 'Android (Google Messages)', "category": 'communication', "sensitive": False,
        "source": {"title": 'Google Messages Help: Send photos, videos, or voice messages', "url": 'https://support.google.com/messages/answer/6159880?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'pilot-003', "suffix": 'p', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android (Google Messages)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Google Messages Help: Send photos, videos, or voice messages', 'url': 'https://support.google.com/messages/answer/6159880?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'I have an Android phone and use the Messages app. How do I text a picture of my garden to my sister?',
                    """Here's how to send a picture in the Messages app. It takes less than a minute.

1. Open the **Messages** app.
2. Tap your conversation with your sister. If you haven't texted her before, start a new conversation with her.
3. Next to the box where you type, tap the **Gallery** icon. It looks like a small picture. Your photos will appear.
4. Tap the picture of your garden.
5. Tap the **Send** button. It looks like an arrow.

You'll see the picture appear in your conversation once it's sent.

If you don't see a Gallery icon, your phone may use a different messaging app. Tell me what icons you see next to the typing box and I'll guide you from there.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-004', "task_type": 'screenshot', "task": 'Take a screenshot',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Take a screenshot on your iPhone', "url": 'https://support.apple.com/102616'},
        "examples": [
            {
                "existing": True, "id": 'pilot-004', "suffix": 'p', "scenario": 'missing_info',
                "style": 'plain', "specification": 'underspecified', "platform": 'iOS',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Take a screenshot on your iPhone', 'url': 'https://support.apple.com/102616', 'accessed': '2026-10-24'}],
                "messages": [
                    "How do I take a picture of what's on my iPhone screen? My grandson wants me to send him a screenshot.",
                    """Happy to help. The buttons you press depend on your iPhone model, so one quick question first:

Does your iPhone have a **round button below the screen** (called the Home button)? Just answer yes or no.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-005', "task_type": 'email_not_working', "task": 'Email stopped working (details unknown)',
        "platform": 'unknown', "category": 'communication', "sensitive": False,
        "source": {"title": "Gmail Help: Gmail won't load", "url": 'https://support.google.com/mail/answer/7074871?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'pilot-005', "suffix": 'p', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': "Gmail Help: Gmail won't load", 'url': 'https://support.google.com/mail/answer/7074871?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'Good morning. I hope you can help me. My husband always took care of these things. Since about Tuesday my email is not working right. I used to get messages from my church group every day and now nothing. I tried turning it off and on.',
                    """Good morning. I'm glad you asked, and we can figure this out together. Turning it off and on was a good first try.

So I can give you the right steps: **where do you usually read your email** (a computer, a phone, or a tablet), and **what comes after the @ sign in your email address**? For example, @gmail.com or @yahoo.com.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-006', "task_type": 'printer_not_printing', "task": 'Printer will not print',
        "platform": 'unknown', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Microsoft Support: Fix printer connection and printing problems in Windows', "url": 'https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73'},
        "examples": [
            {
                "existing": True, "id": 'pilot-006', "suffix": 'p', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Fix printer connection and printing problems in Windows', 'url': 'https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73', 'accessed': '2026-10-24'}],
                "messages": [
                    "My printer won't print anything and I need to print my boarding pass for Thursday. It worked fine last month. The little green light is on.",
                    """Let's get that boarding pass printed. The green light is a good sign: it means the printer has power.

The next steps depend on what you're printing from. **Are you printing from a computer or from a phone?** If it's a computer, do you know if it's a Windows computer or a Mac?""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-007', "task_type": 'wifi_connect', "task": 'Connect to a Wi-Fi network',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Connect to Wi-Fi on your iPhone or iPad', "url": 'https://support.apple.com/en-au/111107'},
        "examples": [
            {
                "existing": True, "id": 'pilot-007', "suffix": 'p', "scenario": 'direct_messy',
                "style": 'over_specified', "specification": 'fully_specified', "platform": 'iOS',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Connect to Wi-Fi on your iPhone or iPad', 'url': 'https://support.apple.com/en-au/111107', 'accessed': '2026-10-24'}, {'title': "Apple Support: If you can't connect to Wi-Fi on your iPhone or iPad", 'url': 'https://support.apple.com/en-euro/111786', 'accessed': '2026-10-24'}],
                "messages": [
                    "I'm staying at my daughter's house this weekend. She wrote the Wi-Fi name and password on a card for me. The network is called SmithHome. I have an iPhone 13 with the latest update. How do I get my phone on her internet?",
                    """Here's how to connect your iPhone to SmithHome. Keep the card with the password nearby. This takes about two minutes.

1. Open the **Settings** app. Its icon is a gray gear.
2. Tap **Wi-Fi** near the top.
3. Make sure the switch next to **Wi-Fi** is on (green).
4. Wait a moment for a list of networks to appear. Tap **SmithHome**.
5. Type the password from the card. Capital and small letters must match exactly.
6. Tap **Join**.

When you're connected, you'll see a blue checkmark next to **SmithHome**, and a Wi-Fi symbol (it looks like a fan) at the top of your screen.

If it says the password is incorrect, tap **SmithHome** again and retype it slowly. If you don't see SmithHome in the list, move closer to the internet box in her home and check again.""",
                ],
            },
            {
                "existing": True, "id": 'tr007-r', "suffix": 'r', "scenario": 'failure_recovery',
                "style": 'failure_recovery', "specification": 'fully_specified', "platform": 'iOS',
                "author": 'claude-draft, edited by Ryan Hsieh', "reviewed": True, "inspired_by": 'original',
                "sources": [{'title': 'Apple Support: Connect to Wi-Fi on your iPhone or iPad', 'url': 'https://support.apple.com/en-au/111107', 'accessed': '2026-10-24'}, {'title': "Apple Support: If you can't connect to Wi-Fi on your iPhone or iPad", 'url': 'https://support.apple.com/en-euro/111786', 'accessed': '2026-10-24'}],
                "messages": [
                    "I'm staying at my daughter's house this weekend. She wrote the Wi-Fi name and password on a card for me. The network is called SmithHome. I have an iPhone 13 with the latest update. How do I get my phone on her internet?",
                    """Here's how to connect your iPhone to SmithHome. Keep the card with the password nearby. This takes about two minutes.

1. Open the **Settings** app. Its icon is a gray gear.
2. Tap **Wi-Fi** near the top.
3. Make sure the switch next to **Wi-Fi** is on (green).
4. Wait a moment for a list of networks to appear. Tap **SmithHome**.
5. Type the password from the card. Capital and small letters must match exactly.
6. Tap **Join**.

When you're connected, you'll see a blue checkmark next to **SmithHome**, and a Wi-Fi symbol (it looks like a fan) at the top of your screen.

If it says the password is incorrect, tap **SmithHome** again and retype it slowly. If you don't see SmithHome in the list, move closer to the internet box in her home and check again.""",
                    "I don't see SmithHome in the list at all.",
                    """Let's check a few things. Try them in order, and stop as soon as **SmithHome** appears in the list.

1. **Check the exact name.** Ask your daughter to check the network name. It might be slightly different, like **SmithHome-5G**.
2. **Ask whether other phones work.** Ask your daughter whether other phones in the house can connect.
3. **Check the internet box.** Make sure the router is plugged in and its lights are on.
4. **Move closer** to the router, then look at the list again.
5. **Check Airplane Mode.** In **Settings**, make sure **Airplane Mode** is turned off.
6. **Check the Wi-Fi switch.** If it looks gray and you can't tap it, restart your iPhone.
7. **Restart the router.** Unplug the router and the modem, then plug them back in. Ask your daughter first, because this turns off the internet for everyone in the house for a few minutes.

If SmithHome still doesn't show up, tell me which network names you do see.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-008', "task_type": 'display_scale', "task": 'Make everything on screen bigger',
        "platform": 'Windows 11', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Microsoft Support: Make text and apps bigger', "url": 'https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64'},
        "examples": [
            {
                "existing": True, "id": 'pilot-008', "suffix": 'p', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Make text and apps bigger', 'url': 'https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64', 'accessed': '2026-10-24'}],
                "messages": [
                    'Everything on my laptop screen is too small. It has Windows 11. How do I make it all bigger?',
                    """You can make everything on the screen bigger in Settings. It takes about two minutes, and you can change it back anytime.

1. Click the **Start** button (the Windows logo) at the bottom of the screen.
2. Click **Settings**. Its icon is a gear.
3. Click **Display**.
4. Find **Scale & layout**. Next to **Scale**, click the box with a percentage in it, such as 100%.
5. Choose a bigger number, like 125% or 150%.

The screen will change size right away. Try a number, and if things are still too small, pick a bigger one.

If only the **words** are too small, there's another setting just for text. Tell me and I'll walk you through it. Some programs may look right only after you restart the computer.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-009', "task_type": 'internet_not_working', "task": 'Internet not working (message cut off)',
        "platform": 'unknown', "category": 'technical_support', "sensitive": False,
        "source": {"title": "Apple Support: If you can't connect to Wi-Fi on your iPhone or iPad", "url": 'https://support.apple.com/en-euro/111786'},
        "examples": [
            {
                "existing": True, "id": 'pilot-009', "suffix": 'p', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': "Apple Support: If you can't connect to Wi-Fi on your iPhone or iPad", 'url': 'https://support.apple.com/en-euro/111786', 'accessed': '2026-10-24'}],
                "messages": [
                    'the internet on my',
                    """It looks like your message got cut off, but I'd be glad to help with your internet.

**Which device is having trouble** (for example your phone, computer, or TV), and **what happens when you try to go online?**""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-010', "task_type": 'account_password_reset', "task": 'Reset forgotten Apple Account password',
        "platform": 'iPhone', "category": 'online_services', "sensitive": True,
        "source": {"title": 'Apple Support: Change your Apple Account password', "url": 'https://support.apple.com/en-mz/101567'},
        "examples": [
            {
                "existing": True, "id": 'pilot-010', "suffix": 'p', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iOS',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Change your Apple Account password', 'url': 'https://support.apple.com/en-mz/101567', 'accessed': '2026-10-24'}, {'title': 'Apple Support: If you forgot your Apple Account password', 'url': 'https://support.apple.com/en-us/ht201487', 'accessed': '2026-10-24'}],
                "messages": [
                    'I forgot my Apple ID password. I can still open my iPhone with my passcode. How do I make a new password?',
                    """Good news: because you can still open your iPhone, you can make a new password right on the phone. (Apple now calls the Apple ID an **Apple Account**.)

1. Open the **Settings** app.
2. Tap **your name** at the very top.
3. Tap **Sign-In & Security**.
4. Tap **Change Password**.
5. Follow the instructions on the screen. If it asks for a passcode, use the one you use to unlock your iPhone.
6. Type your new password twice, then confirm.

Your iPhone may ask you to wait about an hour before the change finishes. This is a security feature, not a problem.

Write the new password down and keep it somewhere safe at home. Never give it to anyone who calls or texts you offering help with your account.

If **Change Password** doesn't appear, tell me what you see and I'll help with another way.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-011', "task_type": 'software_update', "task": 'Install a software update',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Update your iPhone or iPad', "url": 'https://support.apple.com/en-ie/118575'},
        "examples": [
            {
                "existing": True, "id": 'pilot-011', "suffix": 'p', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'iOS',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Update your iPhone or iPad', 'url': 'https://support.apple.com/en-ie/118575', 'accessed': '2026-10-24'}],
                "messages": [
                    "My iPhone keeps showing a message about a software update and I keep pressing Later because I'm afraid I'll lose my pictures of my grandchildren. Should I do it, and how?",
                    """It's wise to be careful with your pictures. Updates are generally a good idea because they fix problems and keep your phone secure, and backing up first protects your photos.

**Before you start:**
1. Back up your iPhone with iCloud. If you're not sure whether it's backed up, ask me and I'll show you how to check.
2. Plug your iPhone into its charger.
3. Make sure you're connected to Wi-Fi.

**To update:**
4. Open **Settings**.
5. Tap **General**.
6. Tap **Software Update**.
7. Tap **Download and Install** (the button may say **Update Now**).
8. Enter your iPhone passcode if asked.

The update can take a while, and your iPhone will turn off and back on by itself. Start when you won't need your phone for a bit.

If it says there isn't enough space, you can let it remove some apps temporarily. They come back by themselves after the update.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-012', "task_type": 'email_attach', "task": 'Attach a photo to an email',
        "platform": 'Gmail (computer)', "category": 'communication', "sensitive": False,
        "source": {"title": 'Gmail Help: Send attachments with your Gmail message', "url": 'https://support.google.com/mail/answer/6584'},
        "examples": [
            {
                "existing": True, "id": 'pilot-012', "suffix": 'p', "scenario": 'direct_messy',
                "style": 'over_specified', "specification": 'fully_specified', "platform": 'Windows 11 (Gmail in Chrome)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Send attachments with your Gmail message', 'url': 'https://support.google.com/mail/answer/6584', 'accessed': '2026-10-24'}],
                "messages": [
                    "I have a Dell computer with Windows 11 and I use Google Chrome to read my Gmail. I have a photo saved in my Pictures folder called birthday.jpg that I want to email to my son. I already know how to write the email, I just don't know how to add the photo.",
                    """Since you already know how to write the email, here's just the part for adding the photo:

1. In your new email, look at the bottom of the message window. Click the **paperclip** icon.
2. A window opens showing your files. On the left side, click **Pictures**.
3. Click **birthday.jpg** once.
4. Click **Open**.

You'll see **birthday.jpg** appear near the bottom of your email. Wait until it finishes loading, then click **Send**.

If the photo is very large, Gmail may add it as a link instead of an attachment. That's fine: your son can still open it.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-013', "task_type": 'backup_photos', "task": 'Back up photos',
        "platform": 'iPhone (iCloud Photos)', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple iCloud User Guide: Set up and use iCloud Photos', "url": 'https://support.apple.com/guide/icloud/mm7e90c1ba48'},
        "examples": [
            {
                "existing": True, "id": 'pilot-013', "suffix": 'p', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iOS',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple iCloud User Guide: Set up and use iCloud Photos', 'url': 'https://support.apple.com/guide/icloud/mm7e90c1ba48', 'accessed': '2026-10-24'}],
                "messages": [
                    "how do I back up my photos so I don't lose them?",
                    'Happy to help you keep your photos safe. Are you using an **iPhone**, or a different kind of phone?',
                    'iPhone',
                    """Great. Your iPhone can save your photos to iCloud, Apple's online storage, so they're safe even if the phone is lost or broken.

1. Open the **Settings** app.
2. Tap **your name** at the top.
3. Tap **iCloud**.
4. Tap **Photos**.
5. Turn on the switch next to **Sync this iPhone** so it turns green.

Your photos will start saving to iCloud on their own. If you have a lot of photos, this can take a while, so it's best to leave your phone connected to Wi-Fi and charging.

If your iCloud storage fills up, your iPhone will let you know. Tell me if you see that message and we can look at your options together.""",
                ],
            },
        ],
    },
]
