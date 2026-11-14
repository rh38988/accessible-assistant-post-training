"""Existing English drafts, group 3. Exported by export_spec.py; ids and provenance preserved."""
TASKS = [
    {
        "task_id": 'TR-033', "task_type": 'software_update', "task": 'Install a software update',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Help: Check & update your Android version', "url": 'https://support.google.com/android/answer/7680439?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr033-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Check & update your Android version', 'url': 'https://support.google.com/android/answer/7680439?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I update the software on my Android phone?',
                    """Here's how to check for an update. Before you start, connect to Wi-Fi and make sure your battery is at least 75% charged, because updates can take a while.

1. Open the **Settings** app.
2. Tap **System**.
3. Tap **Software updates**. On some phones this is called **System update** or is in a different spot.
4. Follow the instructions on the screen to download and install the update.

Your phone may restart during the update. On Google Pixel phones, the update installs in the background and finishes when you restart.

If it says there isn't enough space, tell me and I'll help you free some up first.""",
                ],
            },
            {
                "existing": True, "id": 'tr033-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft, edited by Ryan Hsieh', "reviewed": True, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Check & update your Android version', 'url': 'https://support.google.com/android/answer/7680439?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "my phone says there's an update, should I do it?",
                    """Updates are usually a good idea because they fix problems and help keep your phone secure. If the message popped up on a website, don't tap it. Real updates come from your phone's Settings.

So I can show you the right steps: is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?""",
                ],
            },
            {
                "existing": True, "id": 'tr033-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'verbose', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Help: Check & update your Android version', 'url': 'https://support.google.com/android/answer/7680439?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "My phone keeps showing a message about an update. Last time I updated something on my old phone all my contacts disappeared and I don't want that to happen again.",
                    """That sounds stressful, and it makes sense to be careful. I can walk you through doing it the safe way.

First, **is your phone an iPhone or an Android phone** (like Samsung or Google Pixel)?""",
                ],
            },
            {
                "existing": True, "id": 'tr033-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Help: Check & update your Android version', 'url': 'https://support.google.com/android/answer/7680439?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "my phone says there's an update, should I do it?",
                    'Updates are usually a good idea because they fix problems and help keep your phone secure. So I can show you the right steps: is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?',
                    'Android',
                    """Thanks. If you still see the update notification, you can tap it. Otherwise, follow these steps.

Here's how to check for an update. Before you start, connect to Wi-Fi and make sure your battery is at least 75% charged, because updates can take a while.

1. Open the **Settings** app.
2. Tap **System**.
3. Tap **Software updates**. On some phones this is called **System update** or is in a different spot.
4. Follow the instructions on the screen to download and install the update.

Your phone may restart during the update. On Google Pixel phones, the update installs in the background and finishes when you restart.

If it says there isn't enough space, tell me and I'll help you free some up first.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-034', "task_type": 'software_update', "task": 'Install Windows updates',
        "platform": 'Windows 11', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Microsoft Support: Install Windows Updates', "url": 'https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates'},
        "examples": [
            {
                "existing": True, "id": 'tr034-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Install Windows Updates', 'url': 'https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I install Windows updates on my Windows 11 computer?',
                    """Here's how to check for updates and install them. It can take a while, so do it when you won't need the computer for a bit.

1. Click the **Start** button (the Windows logo).
2. Click **Settings**.
3. Click **Windows Update**.
4. Click **Check for updates**.
5. If updates are found, click **Download & install**.

If Windows asks you to restart, save anything you're working on first, then restart to finish the update.

If you see an error message, write it down or take a picture of it, and tell me what it says.""",
                ],
            },
            {
                "existing": True, "id": 'tr034-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Install Windows Updates', 'url': 'https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates', 'accessed': '2026-10-24'}],
                "messages": [
                    'my computer keeps saying it needs to update',
                    'Updates help keep your computer working well and safe. Is your computer a **Windows** computer or a **Mac**?',
                ],
            },
            {
                "existing": True, "id": 'tr034-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'over_specified', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Install Windows Updates', 'url': 'https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates', 'accessed': '2026-10-24'}],
                "messages": [
                    "Dell Inspiron, Windows 11 Home. The little icon by the clock says updates are available. I'm comfortable with Settings, just tell me where to go.",
                    """Sure, here's the path:

Here's how to check for updates and install them. It can take a while, so do it when you won't need the computer for a bit.

1. Click the **Start** button (the Windows logo).
2. Click **Settings**.
3. Click **Windows Update**.
4. Click **Check for updates**.
5. If updates are found, click **Download & install**.

If Windows asks you to restart, save anything you're working on first, then restart to finish the update.

If you see an error message, write it down or take a picture of it, and tell me what it says.""",
                ],
            },
            {
                "existing": True, "id": 'tr034-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Install Windows Updates', 'url': 'https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates', 'accessed': '2026-10-24'}],
                "messages": [
                    'my computer keeps saying it needs to update',
                    'Updates help keep your computer working well and safe. Is your computer a **Windows** computer or a **Mac**?',
                    'Windows 11',
                    """Thanks. Here's how to install the updates.

Here's how to check for updates and install them. It can take a while, so do it when you won't need the computer for a bit.

1. Click the **Start** button (the Windows logo).
2. Click **Settings**.
3. Click **Windows Update**.
4. Click **Check for updates**.
5. If updates are found, click **Download & install**.

If Windows asks you to restart, save anything you're working on first, then restart to finish the update.

If you see an error message, write it down or take a picture of it, and tell me what it says.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-035', "task_type": 'backup_photos', "task": 'Back up photos',
        "platform": 'Android (Google Photos)', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Google Photos Help: Back up photos & videos (Android)', "url": 'https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid'},
        "examples": [
            {
                "existing": True, "id": 'tr035-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android (Google Photos)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Google Photos Help: Back up photos & videos (Android)', 'url': 'https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    "How do I back up my photos on my Android phone so I don't lose them?",
                    """You can use the **Google Photos** app to save copies of your photos to your Google Account. It takes a couple of minutes to turn on.

1. Open the **Google Photos** app.
2. Sign in to your Google Account if it asks.
3. Tap your **profile picture or initial** at the top right.
4. Tap **Photos settings**.
5. Tap **Backup**.
6. Turn **Backup** on.

Your photos will start saving to your Google Account. This can take a while if you have many photos.

Your Google storage is shared with Gmail and Google Drive, and backup stops if it fills up. Tell me if you see a storage message and we'll look at the options.""",
                ],
            },
            {
                "existing": True, "id": 'tr035-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Google Photos Help: Back up photos & videos (Android)', 'url': 'https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    "how can I save my pictures so I don't lose them if I lose my phone",
                    "That's a smart thing to set up. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?",
                ],
            },
            {
                "existing": True, "id": 'tr035-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'Android (Google Photos)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Photos Help: Back up photos & videos (Android)', 'url': 'https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    "I dropped my old phone in the lake last summer and lost all the pictures of my granddaughter's first year. I have a new Android phone now and I don't want that to happen again.",
                    """I'm sorry about those pictures. Let's make sure your new ones are kept safe. Google Photos can save a copy online:

You can use the **Google Photos** app to save copies of your photos to your Google Account. It takes a couple of minutes to turn on.

1. Open the **Google Photos** app.
2. Sign in to your Google Account if it asks.
3. Tap your **profile picture or initial** at the top right.
4. Tap **Photos settings**.
5. Tap **Backup**.
6. Turn **Backup** on.

Your photos will start saving to your Google Account. This can take a while if you have many photos.

Your Google storage is shared with Gmail and Google Drive, and backup stops if it fills up. Tell me if you see a storage message and we'll look at the options.""",
                ],
            },
            {
                "existing": True, "id": 'tr035-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android (Google Photos)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Google Photos Help: Back up photos & videos (Android)', 'url': 'https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    "how can I save my pictures so I don't lose them if I lose my phone",
                    "That's a smart thing to set up. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?",
                    'android',
                    """Great. On Android, Google Photos can do this for you.

You can use the **Google Photos** app to save copies of your photos to your Google Account. It takes a couple of minutes to turn on.

1. Open the **Google Photos** app.
2. Sign in to your Google Account if it asks.
3. Tap your **profile picture or initial** at the top right.
4. Tap **Photos settings**.
5. Tap **Backup**.
6. Turn **Backup** on.

Your photos will start saving to your Google Account. This can take a while if you have many photos.

Your Google storage is shared with Gmail and Google Drive, and backup stops if it fills up. Tell me if you see a storage message and we'll look at the options.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-036', "task_type": 'add_printer', "task": 'Add a printer',
        "platform": 'Windows 11', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Microsoft Support: Add or install a printer in Windows', "url": 'https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows'},
        "examples": [
            {
                "existing": True, "id": 'tr036-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Add or install a printer in Windows', 'url': 'https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows', 'accessed': '2026-10-24'}],
                "messages": [
                    'I just bought a new printer. How do I add it to my Windows 11 computer?',
                    """Here's how to add your new printer. It takes about five minutes.

**First:** turn the printer on. If it uses a cable, plug it into the computer. If it's wireless, make sure it's on the same Wi-Fi network as your computer.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Printers & scanners**.
4. Next to **Add a printer & scanner**, click **Add device**.
5. Wait a few minutes while the computer searches.
6. When your printer appears, click **Add device** next to it.

Some printers install by themselves after step 4.

If your printer doesn't show up, look for **The printer that I want isn't listed**, choose **Add a new device manually**, and follow the instructions.""",
                ],
            },
            {
                "existing": True, "id": 'tr036-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Add or install a printer in Windows', 'url': 'https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I set up my new printer',
                    'Congratulations on the new printer. What will you print from: a **Windows computer**, a **Mac**, or a **phone**?',
                ],
            },
            {
                "existing": True, "id": 'tr036-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Add or install a printer in Windows', 'url': 'https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows', 'accessed': '2026-10-24'}],
                "messages": [
                    'new printer wont',
                    "It sounds like your message got cut off. What won't the new printer do: **turn on**, **connect**, or **print**? And what are you printing from, a computer or a phone?",
                ],
            },
            {
                "existing": True, "id": 'tr036-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Windows 11',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Microsoft Support: Add or install a printer in Windows', 'url': 'https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I set up my new printer',
                    'Congratulations on the new printer. What will you print from: a **Windows computer**, a **Mac**, or a **phone**?',
                    'My Windows 11 laptop',
                    """Great, here's how to add it to your Windows 11 laptop.

Here's how to add your new printer. It takes about five minutes.

**First:** turn the printer on. If it uses a cable, plug it into the computer. If it's wireless, make sure it's on the same Wi-Fi network as your computer.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Printers & scanners**.
4. Next to **Add a printer & scanner**, click **Add device**.
5. Wait a few minutes while the computer searches.
6. When your printer appears, click **Add device** next to it.

Some printers install by themselves after step 4.

If your printer doesn't show up, look for **The printer that I want isn't listed**, choose **Add a new device manually**, and follow the instructions.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-037', "task_type": 'email_attach', "task": 'Attach a photo to an email',
        "platform": 'Gmail app (phone)', "category": 'communication', "sensitive": False,
        "source": {"title": 'Gmail Help: Send attachments with your Gmail message (Android)', "url": 'https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid'},
        "examples": [
            {
                "existing": True, "id": 'tr037-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Gmail app (phone)',
                "author": 'claude-draft, edited by Ryan Hsieh', "reviewed": True, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Send attachments with your Gmail message (Android)', 'url': 'https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I attach a photo to an email in the Gmail app on my Android phone?',
                    """Here's how. It takes about a minute.

1. Open the **Gmail** app.
2. Tap **Compose** at the bottom right to start a new email.
3. Tap the **Attach** icon at the top right. It looks like a **paperclip**.
4. Choose where the photo is, such as **Photos**.
5. Tap the photo you want. You can pick up to five photos at once.

Then add the email address and your message as usual, and send it.

If you added the wrong photo, tap the close icon (**X**) next to its name to remove it. Files over 25 MB are added as a Google Drive link instead.""",
                ],
            },
            {
                "existing": True, "id": 'tr037-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Send attachments with your Gmail message (Android)', 'url': 'https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I send a picture in an email',
                    'I can help. Do you use email on a **phone** or a **computer**, and which email app, for example **Gmail**?',
                ],
            },
            {
                "existing": True, "id": 'tr037-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Send attachments with your Gmail message (Android)', 'url': 'https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'how to attach',
                    'Happy to help you attach something. **What would you like to attach** (a photo, a document?), and **where**: in an email, a text message, or somewhere else?',
                ],
            },
            {
                "existing": True, "id": 'tr037-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Gmail app (phone)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Send attachments with your Gmail message (Android)', 'url': 'https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I send a picture in an email',
                    'I can help. Do you use email on a **phone** or a **computer**, and which email app, for example **Gmail**?',
                    'Gmail app on my Android phone',
                    """Thanks, here's how in the Gmail app.

Here's how. It takes about a minute.

1. Open the **Gmail** app.
2. Tap **Compose** at the bottom right to start a new email.
3. Tap the **Attach** icon at the top right.
4. Choose where the photo is, such as **Photos**.
5. Tap the photo you want. You can pick up to five photos at once.

Then add the email address and your message as usual, and send it.

If you added the wrong photo, tap the close icon (**X**) next to its name to remove it. Very large files are added as a Google Drive link instead, which the person can still open.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-038', "task_type": 'account_password_reset', "task": 'Reset forgotten Google Account password',
        "platform": 'Google Account', "category": 'online_services', "sensitive": True,
        "source": {"title": 'Google Account Help: How to recover your Google Account or Gmail', "url": 'https://support.google.com/accounts/answer/7682439?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr038-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Google Account',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Account Help: How to recover your Google Account or Gmail', 'url': 'https://support.google.com/accounts/answer/7682439?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "I forgot my Gmail password and can't sign in. How do I get back into my account?",
                    """You can get back in through Google's account recovery. It usually takes a few minutes.

1. Go to Google's **account recovery** page.
2. Enter the details it asks for, starting with your Gmail address.
3. Answer the questions as best you can. If you're not sure of an answer, make your best guess. A wrong guess doesn't lock you out, and you can try again.
4. When asked, create a **new password** that you haven't used for this account before.

**Stay safe while you do this:**
- Google staff can't help you sign in over the phone, so ignore anyone who calls or messages offering to recover your account.
- Never share your password or any verification code with anyone.

If it doesn't work right away, wait a few days and try again.""",
                ],
            },
            {
                "existing": True, "id": 'tr038-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Account Help: How to recover your Google Account or Gmail', 'url': 'https://support.google.com/accounts/answer/7682439?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "I can't get into my email",
                    "That's stressful, but it can usually be fixed. **Which email do you use** (for example Gmail, which ends in @gmail.com), and **what's going wrong**, such as a forgotten password or an error message?",
                ],
            },
            {
                "existing": True, "id": 'tr038-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'Google Account',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Account Help: How to recover your Google Account or Gmail', 'url': 'https://support.google.com/accounts/answer/7682439?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "I haven't used my Gmail on the computer in ages because my phone just stays logged in, but my phone broke and now the new one is asking for the password and I have no idea what it is.",
                    """That happens a lot when a phone stays signed in for years. You can reset the password:

You can get back in through Google's account recovery. It usually takes a few minutes.

1. Go to Google's **account recovery** page.
2. Enter the details it asks for, starting with your Gmail address.
3. Answer the questions as best you can. If you're not sure of an answer, make your best guess. A wrong guess doesn't lock you out, and you can try again.
4. When asked, create a **new password** that you haven't used for this account before.

**Stay safe while you do this:**
- Google staff can't help you sign in over the phone, so ignore anyone who calls or messages offering to recover your account.
- Never share your password or any verification code with anyone.

If it doesn't work right away, wait a few days and try again.""",
                ],
            },
            {
                "existing": True, "id": 'tr038-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Google Account',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Account Help: How to recover your Google Account or Gmail', 'url': 'https://support.google.com/accounts/answer/7682439?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "I can't get into my email",
                    "That's stressful, but it can usually be fixed. **Which email do you use** (for example Gmail, which ends in @gmail.com), and **what's going wrong**, such as a forgotten password or an error message?",
                    'Gmail, I forgot the password',
                    """Thanks. You can reset it through Google's account recovery.

You can get back in through Google's account recovery. It usually takes a few minutes.

1. Go to Google's **account recovery** page.
2. Enter the details it asks for, starting with your Gmail address.
3. Answer the questions as best you can. If you're not sure of an answer, make your best guess. A wrong guess doesn't lock you out, and you can try again.
4. When asked, create a **new password** that you haven't used for this account before.

**Stay safe while you do this:**
- Google staff can't help you sign in over the phone, so ignore anyone who calls or messages offering to recover your account.
- Never share your password or any verification code with anyone.

If it doesn't work right away, wait a few days and try again.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-039', "task_type": 'family_emergency_scam', "task": "Call that sounds like a family member's voice asking for money",
        "platform": 'any', "category": 'online_services', "sensitive": True,
        "source": {"title": 'FTC Consumer Alert: Scammers use AI to enhance their family emergency schemes', "url": 'https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes'},
        "examples": [
            {
                "existing": True, "id": 'tr039-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Alert: Scammers use AI to enhance their family emergency schemes', 'url': 'https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes', 'accessed': '2026-10-24'}],
                "messages": [
                    "My granddaughter called crying and said she's in jail and needs bail money wired right now. It really sounded like her. Is this real?",
                    """Please **don't send any money yet**. Scammers can now copy a person's voice from a short recording, like a video posted online, so a call can sound exactly like someone you love.

Here's what to do:

1. **Hang up.** You don't need to argue or explain.
2. **Call your granddaughter** at the phone number you already have for her, not a number from the call.
3. If you can't reach her, **call another family member** or one of her friends to check.

**Warning signs of this scam:** an urgent emergency, pressure to act fast, and a request to **wire money, send cryptocurrency, or buy gift cards**. Those payments are very hard to get back.

If it turns out to be a scam, you can report it at **ReportFraud.ftc.gov**. If you already sent money, tell me right away and we'll work out the next steps.""",
                ],
            },
            {
                "existing": True, "id": 'tr039-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Alert: Scammers use AI to enhance their family emergency schemes', 'url': 'https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes', 'accessed': '2026-10-24'}],
                "messages": [
                    'Someone called and said my granddaughter needs money, what should I do?',
                    "I'm glad you asked before doing anything. To help you check: **what exactly did they ask you to do, and how did they want the money sent?** For example, did they ask for a wire transfer or gift cards?",
                ],
            },
            {
                "existing": True, "id": 'tr039-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'FTC Consumer Alert: Scammers use AI to enhance their family emergency schemes', 'url': 'https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes', 'accessed': '2026-10-24'}],
                "messages": [
                    'Got a strange call last night. Not sure what to make of it.',
                    "I'm happy to help you figure it out. **What did the caller say, and did they ask you for money or personal information?**",
                ],
            },
            {
                "existing": True, "id": 'tr039-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Alert: Scammers use AI to enhance their family emergency schemes', 'url': 'https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes', 'accessed': '2026-10-24'}],
                "messages": [
                    'Someone called and said my granddaughter needs money, what should I do?',
                    "I'm glad you asked before doing anything. To help you check: **what exactly did they ask you to do, and how did they want the money sent?** For example, did they ask for a wire transfer or gift cards?",
                    'They wanted me to wire $3,000. The voice sounded just like her.',
                    """Thank you for telling me. A request to wire money in an emergency is a common warning sign, even when the voice sounds right.

Please **don't send any money yet**. Scammers can now copy a person's voice from a short recording, like a video posted online, so a call can sound exactly like someone you love.

Here's what to do:

1. **Hang up.** You don't need to argue or explain.
2. **Call your granddaughter** at the phone number you already have for her, not a number from the call.
3. If you can't reach her, **call another family member** or one of her friends to check.

**Warning signs of this scam:** an urgent emergency, pressure to act fast, and a request to **wire money, send cryptocurrency, or buy gift cards**. Those payments are very hard to get back.

If it turns out to be a scam, you can report it at **ReportFraud.ftc.gov**. If you already sent money, tell me right away and we'll work out the next steps.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-040', "task_type": 'package_text_scam', "task": 'Text says package could not be delivered',
        "platform": 'any', "category": 'online_services', "sensitive": True,
        "source": {"title": 'FTC Consumer Alert: Think that text message is from USPS? It could be a scam', "url": 'https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam'},
        "examples": [
            {
                "existing": True, "id": 'tr040-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Alert: Think that text message is from USPS? It could be a scam', 'url': 'https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam', 'accessed': '2026-10-24'}],
                "messages": [
                    "I got a text saying USPS couldn't deliver my package and I need to click a link to update my address. I am expecting a package. Should I click it?",
                    """Please **don't click the link**. Texts like this are a common scam, even when you really are expecting a package. The link usually leads to a fake website that looks real and asks for your personal or card information.

Instead:

1. **Don't click** the link or reply.
2. Check on your package using the website or app of the **store where you bought it**. Go there directly, not through the text.
3. **Report the text.** Use your phone's **junk** or **spam** reporting option if you see one, or forward the text to **7726**.
4. Then delete it.

If you already clicked and typed in your card number, call your bank right away using the number on the back of your card.""",
                ],
            },
            {
                "existing": True, "id": 'tr040-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Alert: Think that text message is from USPS? It could be a scam', 'url': 'https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam', 'accessed': '2026-10-24'}],
                "messages": [
                    'I got a text about a package, is it real?',
                    "Let's check it together. **What does the text ask you to do?** For example, does it have a link to click, or ask you to pay a fee or update your address?",
                ],
            },
            {
                "existing": True, "id": 'tr040-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'FTC Consumer Alert: Think that text message is from USPS? It could be a scam', 'url': 'https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam', 'accessed': '2026-10-24'}],
                "messages": [
                    'usps text link',
                    "Do you mean you got a text that looks like it's from **USPS** with a link in it? If so, please don't click the link yet. **What does the text ask you to do?**",
                ],
            },
            {
                "existing": True, "id": 'tr040-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft, edited by Ryan Hsieh', "reviewed": True, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Alert: Think that text message is from USPS? It could be a scam', 'url': 'https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam', 'accessed': '2026-10-24'}],
                "messages": [
                    'I got a text about a package, is it real?',
                    "Let's check it together. **What does the text ask you to do?** For example, does it have a link to click, or ask you to pay a fee or update your address?",
                    'It has a link and says I need to pay $1.99 for redelivery.',
                    """Thanks. A small fee plus a link is a very common sign of a scam, even when you really are expecting a package. Please **don't click the link**. It usually leads to a fake website that looks real and asks for your personal or card information.

Instead:

1. **Don't click** the link or reply.
2. Check on your package using the website or app of the **store where you bought it**. Go there directly, not through the text.
3. **Report the text.** Use your phone's **junk** or **spam** reporting option if you see one, or forward the text to **7726**. You can also report it at **ReportFraud.ftc.gov**.
4. Then delete it.

If you already clicked and typed in your card number, call your bank right away using the number on the back of your card.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-041', "task_type": 'gift_card_scam', "task": 'Someone asks to be paid with gift cards',
        "platform": 'any', "category": 'online_services', "sensitive": True,
        "source": {"title": 'FTC Consumer Advice: Avoiding and Reporting Gift Card Scams', "url": 'https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams'},
        "examples": [
            {
                "existing": True, "id": 'tr041-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: Avoiding and Reporting Gift Card Scams', 'url': 'https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams', 'accessed': '2026-10-24'}],
                "messages": [
                    "I got an email from my pastor asking me to buy five $100 gift cards for church members and send him the numbers on the back. He said he's in a meeting and can't talk. Should I do it?",
                    """Please **don't buy the gift cards**. This is a common scam. Real businesses, government agencies, and people you know don't ask to be paid with gift card numbers, and once you share the numbers, the money is very hard to get back.

Here's what to do:

1. **Don't reply** to the email.
2. **Call your pastor** using a phone number you already have, or call the church office, and ask if he really sent it.
3. If it's fake, you can report it at **ReportFraud.ftc.gov**.

**If you already bought cards and shared the numbers:**
- Call the **gift card company** right away and ask for your money back. Sometimes they can freeze what's left on the card.
- Keep the cards and the store receipt.
- Report it at **ReportFraud.ftc.gov**.""",
                ],
            },
            {
                "existing": True, "id": 'tr041-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: Avoiding and Reporting Gift Card Scams', 'url': 'https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams', 'accessed': '2026-10-24'}],
                "messages": [
                    'someone wants me to pay with gift cards, is that normal?',
                    """**Please don't buy any gift cards yet.** Being asked to pay with gift cards is a common sign of a scam.

**Who is asking, and have you already bought or sent any cards?**""",
                ],
            },
            {
                "existing": True, "id": 'tr041-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'FTC Consumer Advice: Avoiding and Reporting Gift Card Scams', 'url': 'https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams', 'accessed': '2026-10-24'}],
                "messages": [
                    "Our church secretary forwarded a weird email to everyone saying Pastor needs gift cards for a surprise and to text him the codes. My friend already bought some. I don't want to be rude to Pastor if it's real.",
                    """You're not being rude by checking, and a real pastor would understand. The steps for your friend are at the end.

Please **don't buy the gift cards**. This is a common scam. Real businesses, government agencies, and people you know don't ask to be paid with gift card numbers, and once you share the numbers, the money is very hard to get back.

Here's what to do:

1. **Don't reply** to the email.
2. **Call your pastor** using a phone number you already have, or call the church office, and ask if he really sent it.
3. If it's fake, you can report it at **ReportFraud.ftc.gov**.

**If you already bought cards and shared the numbers:**
- Call the **gift card company** right away and ask for your money back. Sometimes they can freeze what's left on the card.
- Keep the cards and the store receipt.
- Report it at **ReportFraud.ftc.gov**.""",
                ],
            },
            {
                "existing": True, "id": 'tr041-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'GrandGuard',
                "sources": [{'title': 'FTC Consumer Advice: Avoiding and Reporting Gift Card Scams', 'url': 'https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams', 'accessed': '2026-10-24'}],
                "messages": [
                    'someone wants me to pay with gift cards, is that normal?',
                    """**Please don't buy any gift cards yet.** Being asked to pay with gift cards is a common sign of a scam.

**Who is asking, and have you already bought or sent any cards?**""",
                    "It's an email from my pastor. I haven't bought anything yet.",
                    """Good, you haven't lost anything. Here's what to do:

Please **don't buy the gift cards**. This is a common scam. Real businesses, government agencies, and people you know don't ask to be paid with gift card numbers, and once you share the numbers, the money is very hard to get back.

Here's what to do:

1. **Don't reply** to the email.
2. **Call your pastor** using a phone number you already have, or call the church office, and ask if he really sent it.
3. If it's fake, you can report it at **ReportFraud.ftc.gov**.

**If you already bought cards and shared the numbers:**
- Call the **gift card company** right away and ask for your money back. Sometimes they can freeze what's left on the card.
- Keep the cards and the store receipt.
- Report it at **ReportFraud.ftc.gov**.""",
                ],
            },
            {
                "existing": True, "id": 'tr041-r', "suffix": 'r', "scenario": 'failure_recovery',
                "style": 'failure_recovery', "specification": 'fully_specified', "platform": 'any',
                "author": 'claude-draft, edited by Ryan Hsieh', "reviewed": True, "inspired_by": 'original',
                "sources": [{'title': 'FTC Consumer Advice: Avoiding and Reporting Gift Card Scams', 'url': 'https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams', 'accessed': '2026-10-24'}],
                "messages": [
                    "I got an email from my pastor asking me to buy five $100 gift cards for church members and send him the numbers on the back. He said he's in a meeting and can't talk. Should I do it?",
                    """Please **don't buy the gift cards**. This is a common scam. Real businesses, government agencies, and people you know don't ask to be paid with gift card numbers, and once you share the numbers, the money is very hard to get back.

Here's what to do:

1. **Don't reply** to the email.
2. **Call your pastor** using a phone number you already have, or call the church office, and ask if he really sent it.
3. If it's fake, you can report it at **ReportFraud.ftc.gov**.

**If you already bought cards and shared the numbers:**
- Call the **gift card company** right away and ask for your money back. Sometimes they can freeze what's left on the card.
- Keep the cards and the store receipt.
- Report it at **ReportFraud.ftc.gov**.""",
                    'Oh no. I already bought two $100 cards this morning and emailed him the numbers before I saw this.',
                    """I'm sorry this happened. This scam fools a lot of careful people. Acting quickly gives you the best chance of getting money back.

1. **Contact the gift card company right away.** Tell them the cards were used in a scam and ask for your money back. Sometimes they can freeze money that hasn't been spent yet. The FTC's gift card scam page lists contact information for major gift card companies.
2. **Keep the cards and the store receipt**, and take a photo of both. You'll need them when you report it.
3. **Report the scam** at **ReportFraud.ftc.gov**.
4. **Don't reply** to the email, and don't buy more cards, even if you're asked again.
5. **Tell your church office**, so they can warn other members, and let your pastor know his email may have been hacked.

Do you have the cards and the receipt with you? If so, we can look at step 1 together.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-042', "task_type": 'family_sharing', "task": 'Set up Family Sharing',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: How to set up Family Sharing on your iPhone, iPad, or Mac', "url": 'https://support.apple.com/en-us/108380'},
        "examples": [
            {
                "existing": True, "id": 'tr042-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to set up Family Sharing on your iPhone, iPad, or Mac', 'url': 'https://support.apple.com/en-us/108380', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I set up Family Sharing on my iPhone so my daughter can be part of it?',
                    """Here's how to start a family group and invite your daughter. It takes a few minutes.

**Create the group:**
1. Open **Settings** and tap **your name** at the top.
2. Tap **Family**.
3. Follow the instructions on the screen to set up your family group.

**Invite your daughter:**
4. Go to **Settings**, then **Family**.
5. Tap the **add member** button (it has a plus sign).
6. Tap **Invite Others** and follow the steps to send her an invitation.

Once she accepts, she'll be part of your family group. If she doesn't see the invitation, go to **Settings**, then **Family**, tap her name, and choose **Resend Invitation**.""",
                ],
            },
            {
                "existing": True, "id": 'tr042-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to set up Family Sharing on your iPhone, iPad, or Mac', 'url': 'https://support.apple.com/en-us/108380', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I share things with my family on my phone',
                    'There are a few ways to do that. **What would you like to share** (for example photos, your location, or app purchases), and is your phone an **iPhone** or an Android phone?',
                ],
            },
            {
                "existing": True, "id": 'tr042-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: How to set up Family Sharing on your iPhone, iPad, or Mac', 'url': 'https://support.apple.com/en-us/108380', 'accessed': '2026-10-24'}],
                "messages": [
                    'family sharing',
                    'Sure, I can help with Family Sharing. Do you want to **set up a new family group**, **invite someone** to a group you already have, or **accept an invitation** someone sent you?',
                ],
            },
            {
                "existing": True, "id": 'tr042-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: How to set up Family Sharing on your iPhone, iPad, or Mac', 'url': 'https://support.apple.com/en-us/108380', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I share things with my family on my phone',
                    'There are a few ways to do that. **What would you like to share** (for example photos, your location, or app purchases), and is your phone an **iPhone** or an Android phone?',
                    'iPhone. My daughter said to set up Family Sharing so we can share stuff.',
                    """Got it. Family Sharing is a good choice for that.

Here's how to start a family group and invite your daughter. It takes a few minutes.

**Create the group:**
1. Open **Settings** and tap **your name** at the top.
2. Tap **Family**.
3. Follow the instructions on the screen to set up your family group.

**Invite your daughter:**
4. Go to **Settings**, then **Family**.
5. Tap the **add member** button (it has a plus sign).
6. Tap **Invite Others** and follow the steps to send her an invitation.

Once she accepts, she'll be part of your family group. If she doesn't see the invitation, go to **Settings**, then **Family**, tap her name, and choose **Resend Invitation**.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-043', "task_type": 'add_contact', "task": 'Add a contact',
        "platform": 'Android', "category": 'communication', "sensitive": False,
        "source": {"title": 'Contacts Help: Add or move contacts (Android)', "url": 'https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid'},
        "examples": [
            {
                "existing": True, "id": 'tr043-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Contacts Help: Add or move contacts (Android)', 'url': 'https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    "How do I add a new contact on my Android phone? I want to save my new doctor's office number.",
                    """Here's how to save the number. It takes about a minute.

1. Open the **Contacts** app.
2. Tap the **Add** icon at the bottom right.
3. Type a name, like **Dr. Smith's Office**.
4. Type the phone number.
5. Tap **Save**.

Now the name will show up when the office calls you, and you can find the number in Contacts.

If your phone uses a different contacts app and you don't see an **Add** icon, tell me what you see.""",
                ],
            },
            {
                "existing": True, "id": 'tr043-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Contacts Help: Add or move contacts (Android)', 'url': 'https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I save a phone number',
                    'Happy to help you save it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?',
                ],
            },
            {
                "existing": True, "id": 'tr043-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Contacts Help: Add or move contacts (Android)', 'url': 'https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'save number to my contacts on',
                    'It looks like your message got cut off. Which phone are you using, an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr043-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Contacts Help: Add or move contacts (Android)', 'url': 'https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I save a phone number',
                    'Happy to help you save it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?',
                    'Android',
                    """Thanks.

Here's how to save the number. It takes about a minute.

1. Open the **Contacts** app.
2. Tap the **Add** icon at the bottom right.
3. Type a name, like **Dr. Smith's Office**.
4. Type the phone number.
5. Tap **Save**.

Now the name will show up when the office calls you, and you can find the number in Contacts.

If your phone uses a different contacts app and you don't see an **Add** icon, tell me what you see.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-045', "task_type": 'block_number', "task": 'Block a phone number',
        "platform": 'iPhone', "category": 'communication', "sensitive": False,
        "source": {"title": 'Apple Support: Block phone numbers, contacts, and emails on your iPhone or iPad', "url": 'https://support.apple.com/en-us/111104'},
        "examples": [
            {
                "existing": True, "id": 'tr045-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Block phone numbers, contacts, and emails on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/111104', 'accessed': '2026-10-24'}],
                "messages": [
                    'Someone keeps calling me from the same number and hanging up. How do I block it on my iPhone?',
                    """You can block that number from your list of recent calls. It takes less than a minute.

1. Open the **Phone** app.
2. Tap **Recents**.
3. Find the number and tap it. (If you see a small **"i"** in a circle next to the number, tap that instead.)
4. Scroll down and tap **Block Caller**.
5. Confirm if asked.

After that, calls from that number won't ring your phone, and the caller won't be told they're blocked. If they leave a voicemail, it's saved, but you won't get a notification.""",
                ],
            },
            {
                "existing": True, "id": 'tr045-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Block phone numbers, contacts, and emails on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/111104', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I stop a number from calling me',
                    'You can block it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?',
                ],
            },
            {
                "existing": True, "id": 'tr045-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft, edited by Ryan Hsieh', "reviewed": True, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Block phone numbers, contacts, and emails on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/111104', 'accessed': '2026-10-24'}],
                "messages": [
                    "There's a number from out of state that calls me three or four times a day. When I answer nobody's there. My neighbor said I should block it but I don't know how. I have an iPhone 11.",
                    """Your neighbor is right: blocking it will stop those calls from ringing. You can do it from your list of recent calls in less than a minute.

1. Open the **Phone** app.
2. Tap **Recents**.
3. Find the number and tap it. (If you see a small **"i"** in a circle next to the number, tap that instead.)
4. Scroll down and tap **Block Caller**.
5. If a message asks you to confirm, tap **Block Contact**.

After that, calls from that number won't ring your phone, and the caller won't be told they're blocked. If they leave a voicemail, it's saved, but you won't get a notification.""",
                ],
            },
            {
                "existing": True, "id": 'tr045-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Block phone numbers, contacts, and emails on your iPhone or iPad', 'url': 'https://support.apple.com/en-us/111104', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I stop a number from calling me',
                    'You can block it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?',
                    'iPhone',
                    """Thanks. Here's how to block it on your iPhone.

You can block that number from your list of recent calls. It takes less than a minute.

1. Open the **Phone** app.
2. Tap **Recents**.
3. Find the number and tap it. (If you see a small **"i"** in a circle next to the number, tap that instead.)
4. Scroll down and tap **Block Caller**.
5. Confirm if asked.

After that, calls from that number won't ring your phone, and the caller won't be told they're blocked. If they leave a voicemail, it's saved, but you won't get a notification.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-046', "task_type": 'block_number', "task": 'Block a phone number',
        "platform": 'Android', "category": 'communication', "sensitive": False,
        "source": {"title": 'Phone app Help: Block or unblock a phone number', "url": 'https://support.google.com/phoneapp/answer/6325463?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr046-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Phone app Help: Block or unblock a phone number', 'url': 'https://support.google.com/phoneapp/answer/6325463?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    "How do I block a phone number on my Android phone? It's a spam caller.",
                    """You can block it from your call history in the **Phone** app. It takes less than a minute.

1. Open the **Phone** app.
2. Tap the **More** menu (three dots) and choose **Call history**.
3. Tap a call from the number you want to block.
4. Tap **Block / report spam**.
5. Confirm if asked.

Blocked callers can't ring through, and if you use visual voicemail, they can't leave voicemails either.

These steps are for Google's Phone app. If your Phone app looks different, tell me what you see.""",
                ],
            },
            {
                "existing": True, "id": 'tr046-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Phone app Help: Block or unblock a phone number', 'url': 'https://support.google.com/phoneapp/answer/6325463?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'a spam number keeps calling',
                    "That's annoying. I can show you how to block it. Is your phone an **iPhone** or an **Android** phone?",
                ],
            },
            {
                "existing": True, "id": 'tr046-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Phone app Help: Block or unblock a phone number', 'url': 'https://support.google.com/phoneapp/answer/6325463?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'block this number',
                    "Sure, I can help you block it. Is it a number that's been **calling** you or **texting** you? And is your phone an iPhone or an Android phone?",
                ],
            },
            {
                "existing": True, "id": 'tr046-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Phone app Help: Block or unblock a phone number', 'url': 'https://support.google.com/phoneapp/answer/6325463?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'a spam number keeps calling',
                    "That's annoying. I can show you how to block it. Is your phone an **iPhone** or an **Android** phone?",
                    'Android, Pixel 6',
                    """Thanks, here's how on your Pixel.

You can block it from your call history in the **Phone** app. It takes less than a minute.

1. Open the **Phone** app.
2. Tap the **More** menu (three dots) and choose **Call history**.
3. Tap a call from the number you want to block.
4. Tap **Block / report spam**.
5. Confirm if asked.

Blocked callers can't ring through, and if you use visual voicemail, they can't leave voicemails either.

These steps are for Google's Phone app. If your Phone app looks different, tell me what you see.""",
                ],
            },
        ],
    },
]
