"""Existing English drafts, group 8. Exported by export_spec.py; ids and provenance preserved."""
TASKS = [
    {
        "task_id": 'TR-104', "task_type": 'bookmark_site', "task": 'Bookmark a website',
        "platform": 'Chrome (computer)', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Google Chrome Help: Create, find and edit bookmarks in Chrome, computer', "url": 'https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop'},
        "examples": [
            {
                "existing": True, "id": 'tr104-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Chrome (computer)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Chrome Help: Create, find and edit bookmarks in Chrome, computer', 'url': 'https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I bookmark a website in Chrome on my computer so I can find it again?',
                    """Here's how to save it. It takes a few seconds.

1. Go to the website you want to save.
2. Click the **bookmark icon** to the right of the address bar at the top.

**To find it later:**
- If the **bookmarks bar** is showing, click the bookmark there. To show the bar, click **More** at the top right, then **Bookmarks and lists**, then **Show bookmarks bar**.
- Or click **More**, then **Bookmarks and lists**, then **Bookmark Manager** to see all your bookmarks.""",
                ],
            },
            {
                "existing": True, "id": 'tr104-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Chrome Help: Create, find and edit bookmarks in Chrome, computer', 'url': 'https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I save a website so I can find it later',
                    'You can bookmark it. Which browser are you using, like **Chrome**, **Safari**, or **Edge**, and is it on a **computer** or a **phone**?',
                ],
            },
            {
                "existing": True, "id": 'tr104-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Chrome Help: Create, find and edit bookmarks in Chrome, computer', 'url': 'https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'save this website',
                    'Sure. Which browser are you using, like **Chrome**, **Safari**, or **Edge**, and is it on a **computer** or a **phone**?',
                ],
            },
            {
                "existing": True, "id": 'tr104-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Chrome (computer)',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Google Chrome Help: Create, find and edit bookmarks in Chrome, computer', 'url': 'https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I save a website so I can find it later',
                    'You can bookmark it. Which browser are you using, like **Chrome**, **Safari**, or **Edge**, and is it on a **computer** or a **phone**?',
                    'Chrome on my computer',
                    """Thanks.

Here's how to save it. It takes a few seconds.

1. Go to the website you want to save.
2. Click the **bookmark icon** to the right of the address bar at the top.

**To find it later:**
- If the **bookmarks bar** is showing, click the bookmark there. To show the bar, click **More** at the top right, then **Bookmarks and lists**, then **Show bookmarks bar**.
- Or click **More**, then **Bookmarks and lists**, then **Bookmark Manager** to see all your bookmarks.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-105', "task_type": 'unsubscribe_email', "task": 'Unsubscribe from emails',
        "platform": 'Gmail', "category": 'communication', "sensitive": False,
        "source": {"title": 'Gmail Help: Unsubscribe from an email (computer)', "url": 'https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop'},
        "examples": [
            {
                "existing": True, "id": 'tr105-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Gmail',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Unsubscribe from an email (computer)', 'url': 'https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}, {'title': 'Gmail Help: Mark or unmark spam in Gmail (computer)', 'url': 'https://support.google.com/mail/answer/1366858', 'accessed': '2026-11-13'}],
                "messages": [
                    'I get too many newsletter emails in Gmail. How do I unsubscribe on my computer?',
                    """Gmail can unsubscribe you in a couple of clicks. It takes a few seconds per sender.

1. Go to **mail.google.com**.
2. Open an email from the sender.
3. Click **Unsubscribe** next to the sender's name at the top.
4. Click **Unsubscribe** again in the box that pops up.

If you see **Go to website** instead, that sender needs you to unsubscribe on their own site.

To see all your subscriptions at once, click **More** on the left side, then **Manage subscriptions**.

If you're not sure an email is from a sender you trust, don't reply or open any links in it. It can take a few days for the emails to stop.""",
                ],
            },
            {
                "existing": True, "id": 'tr105-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Unsubscribe from an email (computer)', 'url': 'https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I stop getting so many emails',
                    'There are a few ways. Which email do you use, like **Gmail**, and are the emails from **stores or newsletters** you signed up for, or from **strangers**?',
                ],
            },
            {
                "existing": True, "id": 'tr105-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'Gmail',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Unsubscribe from an email (computer)', 'url': 'https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}, {'title': 'Gmail Help: Mark or unmark spam in Gmail (computer)', 'url': 'https://support.google.com/mail/answer/1366858', 'accessed': '2026-11-13'}],
                "messages": [
                    "Every store I've ever bought anything from sends me emails every single day. My inbox has 4,000 unread messages and I can't find the important ones from my family. I use Gmail on my computer.",
                    """That's a lot of clutter. Unsubscribing stops new ones from piling up, and Gmail can do it in a couple of clicks per sender.

1. Go to **mail.google.com**.
2. Open an email from the sender.
3. Click **Unsubscribe** next to the sender's name at the top.
4. Click **Unsubscribe** again in the box that pops up.

If you see **Go to website** instead, that sender needs you to unsubscribe on their own site.

To see all your subscriptions at once, click **More** on the left side, then **Manage subscriptions**.

If you're not sure an email is from a sender you trust, don't reply or open any links in it. It can take a few days for the emails to stop.""",
                ],
            },
            {
                "existing": True, "id": 'tr105-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Gmail',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Unsubscribe from an email (computer)', 'url': 'https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}, {'title': 'Gmail Help: Mark or unmark spam in Gmail (computer)', 'url': 'https://support.google.com/mail/answer/1366858', 'accessed': '2026-11-13'}],
                "messages": [
                    'how do I stop getting so many emails',
                    'There are a few ways. Which email do you use, like **Gmail**, and are the emails from **stores or newsletters** you signed up for, or from **strangers**?',
                    'Newsletters from stores. Gmail.',
                    """Thanks. For store newsletters, unsubscribing is the way to go.

Gmail can unsubscribe you in a couple of clicks. It takes a few seconds per sender.

1. Go to **mail.google.com**.
2. Open an email from the sender.
3. Click **Unsubscribe** next to the sender's name at the top.
4. Click **Unsubscribe** again in the box that pops up.

If you see **Go to website** instead, that sender needs you to unsubscribe on their own site.

To see all your subscriptions at once, click **More** on the left side, then **Manage subscriptions**.

If you're not sure an email is from a sender you trust, don't reply or open any links in it. It can take a few days for the emails to stop.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-106', "task_type": 'recover_deleted_email', "task": 'Get back a deleted email',
        "platform": 'Gmail', "category": 'communication', "sensitive": False,
        "source": {"title": 'Gmail Help: Delete or recover deleted Gmail messages (computer)', "url": 'https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop'},
        "examples": [
            {
                "existing": True, "id": 'tr106-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Gmail',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Delete or recover deleted Gmail messages (computer)', 'url': 'https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    "I accidentally deleted an important email in Gmail. How do I get it back? I'm on my computer.",
                    """If it was deleted in the last 30 days, it should be in your **Trash**. Here's how to get it back.

1. Open **Gmail** in your web browser.
2. On the left side, click **More**, then click **Trash**.
3. Find the email and check the box next to it.
4. At the top, click **Move to**.
5. Choose **Inbox**.

The email will be back in your inbox.

Emails stay in Trash for up to 30 days. After that, they're deleted for good and can't be recovered.""",
                ],
            },
            {
                "existing": True, "id": 'tr106-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Delete or recover deleted Gmail messages (computer)', 'url': 'https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'I deleted something by accident',
                    "Don't worry, it can often be recovered. What did you delete, like an email, a photo, or a file, and on which device or app?",
                ],
            },
            {
                "existing": True, "id": 'tr106-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Delete or recover deleted Gmail messages (computer)', 'url': 'https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'deleted email from my',
                    'It looks like your message got cut off. Which email do you use, like **Gmail**, and are you on a **computer** or a **phone**?',
                ],
            },
            {
                "existing": True, "id": 'tr106-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Gmail',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Delete or recover deleted Gmail messages (computer)', 'url': 'https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop', 'accessed': '2026-10-24'}],
                "messages": [
                    'I deleted something by accident',
                    "Don't worry, it can often be recovered. What did you delete, like an email, a photo, or a file, and on which device or app?",
                    'An email in Gmail, on my computer',
                    """Good news: Gmail keeps deleted emails for a while.

If it was deleted in the last 30 days, it should be in your **Trash**. Here's how to get it back.

1. Open **Gmail** in your web browser.
2. On the left side, click **More**, then click **Trash**.
3. Find the email and check the box next to it.
4. At the top, click **Move to**.
5. Choose **Inbox**.

The email will be back in your inbox.

Emails stay in Trash for up to 30 days. After that, they're deleted for good and can't be recovered.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-107', "task_type": 'mark_spam_email', "task": 'Mark an email as spam',
        "platform": 'Gmail', "category": 'communication', "sensitive": True,
        "source": {"title": 'Gmail Help: Report spam in Gmail (computer)', "url": 'https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer'},
        "examples": [
            {
                "existing": True, "id": 'tr107-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Gmail',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Report spam in Gmail (computer)', 'url': 'https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I mark an email as spam in Gmail on my computer?',
                    """Here's how. It takes a few seconds.

1. Open **Gmail** in your web browser.
2. Check the box next to the email.
3. Click the **Report spam** icon at the top.

The email moves to your **Spam** folder, and Google gets a copy, which helps it spot similar spam.

A couple of notes:
- If it's from a store or newsletter you signed up for, **Unsubscribe** is usually better.
- If the email is trying to **trick you into giving a password or account number**, that's phishing. Don't click any links or reply.""",
                ],
            },
            {
                "existing": True, "id": 'tr107-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Report spam in Gmail (computer)', 'url': 'https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I get rid of junk email',
                    'I can help. Which email do you use, like **Gmail**, and are you on a **computer** or a **phone**?',
                ],
            },
            {
                "existing": True, "id": 'tr107-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Report spam in Gmail (computer)', 'url': 'https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer', 'accessed': '2026-10-24'}],
                "messages": [
                    'spam',
                    'Sure. Do you mean **spam emails**, **spam texts**, or **spam calls**? I can help with any of them.',
                ],
            },
            {
                "existing": True, "id": 'tr107-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Gmail',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Gmail Help: Report spam in Gmail (computer)', 'url': 'https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer', 'accessed': '2026-10-24'}],
                "messages": [
                    'how do I get rid of junk email',
                    'I can help. Which email do you use, like **Gmail**, and are you on a **computer** or a **phone**?',
                    'Gmail on my computer',
                    """Thanks.

Here's how. It takes a few seconds.

1. Open **Gmail** in your web browser.
2. Check the box next to the email.
3. Click the **Report spam** icon at the top.

The email moves to your **Spam** folder, and Google gets a copy, which helps it spot similar spam.

A couple of notes:
- If it's from a store or newsletter you signed up for, **Unsubscribe** is usually better.
- If the email is trying to **trick you into giving a password or account number**, that's phishing. Don't click any links or reply.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-108', "task_type": 'rotation_lock', "task": 'Stop the screen from turning sideways',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Rotate the screen on your iPhone or iPod touch', "url": 'https://support.apple.com/en-us/118226'},
        "examples": [
            {
                "existing": True, "id": 'tr108-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Rotate the screen on your iPhone or iPod touch', 'url': 'https://support.apple.com/en-us/118226', 'accessed': '2026-10-24'}, {'title': 'Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro', 'url': 'https://support.apple.com/en-us/105001', 'accessed': '2026-10-24'}],
                "messages": [
                    "My iPhone screen keeps turning sideways when I'm reading in bed. How do I make it stay upright?",
                    """You can lock the screen so it stays upright. It takes a few seconds.

1. Open **Control Center**: on an iPhone with Face ID, **swipe down from the top-right corner**. On an iPhone with a Home button, **swipe up from the bottom edge**.
2. Tap the **Portrait Orientation Lock** button.
3. Close Control Center.

Now the screen will stay upright even when you tilt the phone.

To let it turn sideways again, for example to watch a video, tap the same button.""",
                ],
            },
            {
                "existing": True, "id": 'tr108-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Rotate the screen on your iPhone or iPod touch', 'url': 'https://support.apple.com/en-us/118226', 'accessed': '2026-10-24'}, {'title': 'Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro', 'url': 'https://support.apple.com/en-us/105001', 'accessed': '2026-10-24'}],
                "messages": [
                    'my screen keeps flipping when I lie down',
                    'You can lock the screen so it stays upright. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr108-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Rotate the screen on your iPhone or iPod touch', 'url': 'https://support.apple.com/en-us/118226', 'accessed': '2026-10-24'}, {'title': 'Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro', 'url': 'https://support.apple.com/en-us/105001', 'accessed': '2026-10-24'}],
                "messages": [
                    'I like to read the news on my iPhone lying on my side in bed, but the screen keeps flipping sideways and it drives me nuts.',
                    """That sounds annoying. You can lock the screen so it stays upright. It takes a few seconds.

1. Open **Control Center**: on an iPhone with Face ID, **swipe down from the top-right corner**. On an iPhone with a Home button, **swipe up from the bottom edge**.
2. Tap the **Portrait Orientation Lock** button.
3. Close Control Center.

Now the screen will stay upright even when you tilt the phone.

To let it turn sideways again, for example to watch a video, tap the same button.""",
                ],
            },
            {
                "existing": True, "id": 'tr108-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Rotate the screen on your iPhone or iPod touch', 'url': 'https://support.apple.com/en-us/118226', 'accessed': '2026-10-24'}, {'title': 'Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro', 'url': 'https://support.apple.com/en-us/105001', 'accessed': '2026-10-24'}],
                "messages": [
                    'my screen keeps flipping when I lie down',
                    'You can lock the screen so it stays upright. Is your phone an **iPhone** or an **Android** phone?',
                    'iPhone',
                    """Thanks.

You can lock the screen so it stays upright. It takes a few seconds.

1. Open **Control Center**: on an iPhone with Face ID, **swipe down from the top-right corner**. On an iPhone with a Home button, **swipe up from the bottom edge**.
2. Tap the **Portrait Orientation Lock** button.
3. Close Control Center.

Now the screen will stay upright even when you tilt the phone.

To let it turn sideways again, for example to watch a video, tap the same button.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-109', "task_type": 'rotation_lock', "task": 'Stop the screen from turning sideways',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Accessibility Help: How to make your screen rotate all by itself', "url": 'https://support.google.com/accessibility/android/answer/6006961?hl=en'},
        "examples": [
            {
                "existing": True, "id": 'tr109-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: How to make your screen rotate all by itself', 'url': 'https://support.google.com/accessibility/android/answer/6006961?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'How do I stop my Android phone screen from turning sideways?',
                    """You can turn off auto-rotate. It takes a few seconds.

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Tap **Auto-rotate screen** to turn it off.

Now the screen will stay the way it is, even when you tilt the phone.

To let it turn again, for example when watching a video, turn **Auto-rotate screen** back on.

Menu names can be a little different on some phones. If you don't see **Display & touch**, tell me what you see in Settings.""",
                ],
            },
            {
                "existing": True, "id": 'tr109-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: How to make your screen rotate all by itself', 'url': 'https://support.google.com/accessibility/android/answer/6006961?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'screen keeps turning',
                    'You can stop it from rotating. Is your phone an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr109-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Android Accessibility Help: How to make your screen rotate all by itself', 'url': 'https://support.google.com/accessibility/android/answer/6006961?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'rotate screen',
                    "Sure. Is it an **iPhone** or an **Android** phone, and do you want the screen to **stop turning sideways**, or to **turn sideways** when it won't?",
                ],
            },
            {
                "existing": True, "id": 'tr109-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'Android',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Android Accessibility Help: How to make your screen rotate all by itself', 'url': 'https://support.google.com/accessibility/android/answer/6006961?hl=en', 'accessed': '2026-10-24'}],
                "messages": [
                    'screen keeps turning',
                    'You can stop it from rotating. Is your phone an **iPhone** or an **Android** phone?',
                    'Android',
                    """Thanks.

You can turn off auto-rotate. It takes a few seconds.

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Tap **Auto-rotate screen** to turn it off.

Now the screen will stay the way it is, even when you tilt the phone.

To let it turn again, for example when watching a video, turn **Auto-rotate screen** back on.

Menu names can be a little different on some phones. If you don't see **Display & touch**, tell me what you see in Settings.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-110', "task_type": 'force_restart', "task": 'Restart a frozen iPhone',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Restart an unresponsive iPhone', "url": 'https://support.apple.com/en-us/116940'},
        "examples": [
            {
                "existing": True, "id": 'tr110-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Restart an unresponsive iPhone', 'url': 'https://support.apple.com/en-us/116940', 'accessed': '2026-10-24'}],
                "messages": [
                    "My iPhone is frozen and won't respond when I touch it. What do I do?",
                    """You can **force restart** it. The steps depend on your model.

**iPhone with Face ID (no Home button):**
1. Press and quickly release the **volume up** button.
2. Press and quickly release the **volume down** button.
3. Press and **hold** the **side button** until you see the **Apple logo**. This can take more than 10 seconds, so keep holding.

**iPhone 7:** press and hold the **side button** and **volume down** together until you see the Apple logo.

**iPhone 6s or older (with a Home button):** press and hold the **Home button** and the **side or top button** together for about 10 seconds, until you see the Apple logo.

If it still won't turn on, charge it for an hour and try again.""",
                ],
            },
            {
                "existing": True, "id": 'tr110-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Restart an unresponsive iPhone', 'url': 'https://support.apple.com/en-us/116940', 'accessed': '2026-10-24'}],
                "messages": [
                    "my phone is stuck and won't do anything",
                    "Let's get it working again. Is it an **iPhone** or an **Android** phone, and if it's an iPhone, does it have a round **Home button** below the screen?",
                ],
            },
            {
                "existing": True, "id": 'tr110-c', "suffix": 'c', "scenario": 'direct_messy',
                "style": 'verbose', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': 'Apple Support: Restart an unresponsive iPhone', 'url': 'https://support.apple.com/en-us/116940', 'accessed': '2026-10-24'}, {'title': "Apple Support: If your iPhone or iPod touch won't charge", 'url': 'https://support.apple.com/en-ca/108805', 'accessed': '2026-11-13'}],
                "messages": [
                    "I was in the middle of a FaceTime with my grandson and the screen froze on his face. Nothing I press does anything and I can't even turn it off. It's an iPhone 14.",
                    """That's frustrating. You can **force restart** it. On an iPhone 14, do this:

1. Press and quickly release the **volume up** button.
2. Press and quickly release the **volume down** button.
3. Press and **hold** the **side button** until you see the **Apple logo**. This can take more than 10 seconds, so keep holding.

If it still won't turn on, charge it for an hour and try again.""",
                ],
            },
            {
                "existing": True, "id": 'tr110-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': 'Apple Support: Restart an unresponsive iPhone', 'url': 'https://support.apple.com/en-us/116940', 'accessed': '2026-10-24'}],
                "messages": [
                    "my phone is stuck and won't do anything",
                    "Let's get it working again. Is it an **iPhone** or an **Android** phone, and if it's an iPhone, does it have a round **Home button** below the screen?",
                    'iPhone 12, no home button',
                    """Thanks. Since your iPhone has no Home button, **force restart** it like this:

1. Press and quickly release the **volume up** button.
2. Press and quickly release the **volume down** button.
3. Press and **hold** the **side button** until you see the **Apple logo**. This can take more than 10 seconds, so keep holding.

If it still won't turn on, charge it for an hour and try again.""",
                ],
            },
        ],
    },
    {
        "task_id": 'TR-111', "task_type": 'phone_not_charging', "task": 'Phone is not charging',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": "Apple Support: If your iPhone or iPod touch won't charge", "url": 'https://support.apple.com/en-ca/108805'},
        "examples": [
            {
                "existing": True, "id": 'tr111-a', "suffix": 'a', "scenario": 'direct',
                "style": 'plain', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': "Apple Support: If your iPhone or iPod touch won't charge", 'url': 'https://support.apple.com/en-ca/108805', 'accessed': '2026-10-24'}],
                "messages": [
                    "My iPhone won't charge when I plug it in. What should I try?",
                    """Let's go through a few checks. This can take up to an hour, mostly waiting.

1. **Restart your iPhone.**
2. **Check the cable and adapter** for damage, like breakage or bent prongs. Don't use a damaged one.
3. **Plug into a wall outlet** and make sure the cable, adapter, and outlet are firmly connected, or try a different outlet.
4. **Look in the charging port** on the bottom of the phone. If there's lint or dirt, carefully clear it out, then plug in firmly again.
5. **Leave it charging for half an hour.**
6. If it still won't turn on or only shows a battery picture, **force restart** it. On an iPhone 8 or later:
   - Press and quickly release **volume up**.
   - Press and quickly release **volume down**.
   - Press and hold the **side button** until you see the **Apple logo**.
   On an older iPhone, tell me the model and I'll give you those steps.
7. **Charge it for another half hour.**

If none of this works, it may need service from Apple.

**If it stops at 80%:** that's usually a battery-saving feature, not a problem.""",
                ],
            },
            {
                "existing": True, "id": 'tr111-b', "suffix": 'b', "scenario": 'missing_info',
                "style": 'under_specified', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': "Apple Support: If your iPhone or iPod touch won't charge", 'url': 'https://support.apple.com/en-ca/108805', 'accessed': '2026-10-24'}],
                "messages": [
                    "my phone won't charge",
                    "Let's figure it out. Is your phone an **iPhone** or an **Android** phone, and does it **not charge at all** or **stop partway**?",
                ],
            },
            {
                "existing": True, "id": 'tr111-c', "suffix": 'c', "scenario": 'missing_info',
                "style": 'incomplete', "specification": 'underspecified', "platform": 'unknown',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'OATS',
                "sources": [{'title': "Apple Support: If your iPhone or iPod touch won't charge", 'url': 'https://support.apple.com/en-ca/108805', 'accessed': '2026-10-24'}],
                "messages": [
                    'charger not',
                    'It looks like your message got cut off. Is your phone **not charging**, and is it an **iPhone** or an **Android** phone?',
                ],
            },
            {
                "existing": True, "id": 'tr111-d', "suffix": 'd', "scenario": 'followup',
                "style": 'under_specified', "specification": 'fully_specified', "platform": 'iPhone',
                "author": 'claude-draft', "reviewed": False, "inspired_by": 'ElderBench',
                "sources": [{'title': "Apple Support: If your iPhone or iPod touch won't charge", 'url': 'https://support.apple.com/en-ca/108805', 'accessed': '2026-10-24'}],
                "messages": [
                    "my phone won't charge",
                    "Let's figure it out. Is your phone an **iPhone** or an **Android** phone, and does it **not charge at all** or **stop partway**?",
                    "iPhone, it doesn't charge at all",
                    """Thanks. Let's go through a few checks. This can take up to an hour, mostly waiting.

1. **Restart your iPhone.**
2. **Check the cable and adapter** for damage, like breakage or bent prongs. Don't use a damaged one.
3. **Plug into a wall outlet** and make sure the cable, adapter, and outlet are firmly connected, or try a different outlet.
4. **Look in the charging port** on the bottom of the phone. If there's lint or dirt, carefully clear it out, then plug in firmly again.
5. **Leave it charging for half an hour.**
6. If it still won't turn on or only shows a battery picture, **force restart** it. On an iPhone 8 or later:
   - Press and quickly release **volume up**.
   - Press and quickly release **volume down**.
   - Press and hold the **side button** until you see the **Apple logo**.
   On an older iPhone, tell me the model and I'll give you those steps.
7. **Charge it for another half hour.**

If none of this works, it may need service from Apple.""",
                ],
            },
        ],
    },
]
