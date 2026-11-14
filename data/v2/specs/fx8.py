"""New examples e and r for tasks in ex8 (batch fx8)."""

IPH_FACE_RESTART = """1. Press and quickly release the **volume up** button.
2. Press and quickly release the **volume down** button.
3. Press and **hold** the **side button** until you see the **Apple logo**. This might take longer than 10 seconds, so keep holding."""

TASKS = [
    {
        "task_id": 'TR-104', "task_type": 'bookmark_site', "task": 'Bookmark a website',
        "platform": 'Chrome (computer)', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Google Chrome Help: Create, find and edit bookmarks in Chrome, computer', "url": 'https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop'},
        "source_notes": """Add a bookmark: 1 Open Chrome on your computer. 2 Go to the site. 3 Click the Bookmark icon to the right of the address bar (label "Bookmark this page").
Show the bookmarks bar: click More at top right, then Bookmarks and lists, then Show bookmarks bar.
Find a bookmark: Bookmarks bar (if turned on, click the bookmark there). Address bar: type @bookmarks and press Tab or Space; you can also click Search bookmarks in the suggestions; enter keywords and select the bookmark from the list. Menu: More, Bookmarks and lists, Bookmark Manager, select the bookmark. Navigation panel: More, Bookmarks and lists, Show all bookmarks.
Edit/delete/folders/sort exist. Deleted bookmarks can't be recovered. Page has no troubleshooting and no keyboard shortcuts.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "I have a lot of bookmarks in Chrome on my computer and I really don't want a bar taking up room across my screen. Last week I saved a recipe site and I just want to find it again by typing a word. Is that possible?",
                 """Yes, you can search your bookmarks from the address bar. It takes a few seconds.

1. Open **Chrome** on your computer.
2. Click the address bar at the top.
3. Type **@bookmarks**, then press **Tab** or **Space**.
4. Type a word from the site's name, like "recipe".
5. Click the bookmark in the list that appears.

You can also click **Search bookmarks** in the suggestions instead of typing @bookmarks.

If you would rather look through all of them, click **More** at the top right, then **Bookmarks and lists**, then **Bookmark Manager**, and click the bookmark there.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chrome (computer)",
             "messages": [
                 "I keep losing pages I like. How do I save a website in Chrome on my computer?",
                 """Here's how to save a page. It takes a few seconds.

1. Go to the website you want to save.
2. Click the **bookmark icon** to the right of the address bar.

To find it later, look under the address bar. If the **bookmarks bar** is turned on, click the bookmark there.""",
                 "I saved one but I don't see any bar under the address bar.",
                 """The bar may just be turned off. Let's turn it on.

1. Click **More** at the top right of Chrome.
2. Click **Bookmarks and lists**.
3. Click **Show bookmarks bar**.

Your bookmark should now show in the bar. Click it to open the site.

You can also click **More**, then **Bookmarks and lists**, then **Bookmark Manager** to see all your bookmarks.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-105', "task_type": 'unsubscribe_email', "task": 'Unsubscribe from emails',
        "platform": 'Gmail', "category": 'communication', "sensitive": False,
        "source": {"title": 'Gmail Help: Unsubscribe from an email (computer)', "url": 'https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop'},
        "source_notes": """Steps: 1 In your browser open Gmail at mail.google.com. 2 Open an email from the sender. 3 Click Unsubscribe next to the sender's name. 4 In the pop-up, click Unsubscribe or Go to website.
Manage subscriptions: click More on the left, then Manage subscriptions (to find a sender's active subscriptions).
Go to website: some senders require you to unsubscribe on their website; the email shows Go to website instead of an unsubscribe option.
After unsubscribing, emails may keep arriving for a few days.
Troubleshooting: unsubscribing from one email may only remove you from a single mailing list; check Manage subscriptions for the sender's other lists. You may see a list ID instead of the sender's name.
If no Unsubscribe option: page gives no steps, only links to Report spam and Block articles.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Gmail",
             "messages": [
                 "I only use Gmail on my laptop and I don't want to visit any other websites or sign up for anything new. Can I stop a store's emails just from inside Gmail?",
                 """You can try it right inside Gmail. It takes a few seconds.

1. Go to **mail.google.com**.
2. Open an email from that store.
3. Click **Unsubscribe** next to the sender's name.
4. In the box that pops up, click **Unsubscribe**.

Some senders require you to unsubscribe on their own website. For those, you will see **Go to website** instead, and Gmail can't finish it for you inside the email.

After you unsubscribe, emails may keep arriving for a few days.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Gmail",
             "messages": [
                 "Gmail on my computer. How do I stop the emails from a clothing store?",
                 """Gmail can do it in a few clicks.

1. Go to **mail.google.com**.
2. Open an email from the store.
3. Click **Unsubscribe** next to the sender's name.
4. In the box that pops up, click **Unsubscribe**.

If you see **Go to website** instead, that sender needs you to unsubscribe on their own site. Emails may keep arriving for a few days.""",
                 "I did that last week and the store still sends me emails.",
                 """That can happen. Unsubscribing from one email may only remove you from one of the sender's mailing lists, so the store may have other lists.

1. Go to **mail.google.com**.
2. On the left, click **More**.
3. Click **Manage subscriptions**.
4. Check it for the store's other lists.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-106', "task_type": 'recover_deleted_email', "task": 'Get back a deleted email',
        "platform": 'Gmail', "category": 'communication', "sensitive": False,
        "source": {"title": 'Gmail Help: Delete or recover deleted Gmail messages (computer)', "url": 'https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop'},
        "source_notes": """Recover: 1 Go to Gmail (mail.google.com) on your computer. Act within 30 days; deleted messages stay in Trash for up to 30 days, then are permanently removed. 2 On the left click More, then Trash. 3 Check the box on the left of each message. 4 At the top click Move to. 5 In the Move to menu choose where to send them, such as your inbox.
Empty Trash: Delete forever (selected) or Empty Trash now; cannot be undone.
Notes: Deleted drafts can't be recovered from Trash. After 30 days messages are permanently deleted and can't be recovered. Page does not cover Spam, All Mail, archived messages, work/school accounts, admin recovery.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Gmail",
             "messages": [
                 "I was writing a long email in Gmail on my computer. It was a draft, I never sent it, and I think I deleted it by mistake. I'd really like it back in my inbox, please.",
                 """I'm sorry, but a deleted draft can't be recovered from Trash, so I can't offer a way to bring it back.

If you also deleted other emails (not drafts) in the last 30 days, you can get those back.

1. Go to **mail.google.com**.
2. On the left, click **More**, then click **Trash**.
3. Check the box next to the email.
4. At the top, click **Move to**.
5. Choose **Inbox**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Gmail",
             "messages": [
                 "I deleted an email in Gmail on my computer last week by accident. How do I get it back?",
                 """Deleted emails stay in **Trash** for up to 30 days, so it may still be there.

1. Go to **mail.google.com**.
2. On the left, click **More**, then click **Trash**.
3. Check the box next to the email.
4. At the top, click **Move to**.
5. Choose **Inbox**.""",
                 "I opened Trash but the email isn't there.",
                 """I'm sorry. Check that you are looking in the right place: on the left, click **More**, then **Trash**.

If it still isn't there, it may have been removed for good. Emails are permanently deleted after 30 days, and **Delete forever** or **Empty Trash now** can't be undone. Deleted drafts also can't be recovered from Trash. Once an email is permanently deleted, it can't be recovered.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-107', "task_type": 'mark_spam_email', "task": 'Mark an email as spam',
        "platform": 'Gmail', "category": 'communication', "sensitive": True,
        "source": {"title": 'Gmail Help: Report spam in Gmail (computer)', "url": 'https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer'},
        "source_notes": """Report spam: 1 On your computer open Gmail. 2 Select one or more emails. 3 At the top click the Report spam icon.
Unmark spam: 1 Open Gmail. 2 In the main menu on the left click More, then Spam. 3 Check the box next to the email. 4 At the top click Not spam.
Delete spam: More, Spam, then Delete all spam messages now, or select emails and Delete forever.
Notes: reporting or moving an email to Spam sends Google a copy, which it may analyze. Phishing: if not sure an email is from a trusted sender, report it as phishing with a form; don't reply or open links first. Page gives no block steps and no filter steps. Page does not say how long spam is kept.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Gmail",
             "messages": [
                 "I have about ten junk emails sitting in my Gmail inbox on my computer and I really don't want to click on each one and report it separately. Can I report them all together?",
                 """Yes, you can select several emails and report them at the same time.

1. Open **Gmail** in your web browser.
2. Check the box next to each junk email.
3. At the top, click the **Report spam** icon.

Reporting sends Google a copy of the emails, which it may analyze.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Gmail",
             "messages": [
                 "Gmail on my computer: what do I click to report an email as spam?",
                 """Here's how. It takes a few seconds.

1. Open **Gmail** in your web browser.
2. Check the box next to the email.
3. At the top, click the **Report spam** icon.

Reporting sends Google a copy of the email, which it may analyze.""",
                 "Oh no, I just did that to an email from my daughter by mistake.",
                 """That's easy to undo.

1. In **Gmail**, on the left, click **More**, then click **Spam**.
2. Check the box next to the email from your daughter.
3. At the top, click **Not spam**.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-108', "task_type": 'rotation_lock', "task": 'Stop the screen from turning sideways',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Rotate the screen on your iPhone or iPod touch', "url": 'https://support.apple.com/en-us/118226'},
        "source_notes": """Rotate page (118226): iPhone without a Home button: 1 Swipe down from the top-right corner of the screen to open Control Center. 2 Tap the Portrait Orientation Lock button to make sure it's off. 3 Close Control Center. 4 Turn the iPhone sideways. The page does not say in words how to turn the lock on (implied: same button) and does not describe the icon. Some apps don't support rotation, so the screen may not rotate even if the lock is off. If you don't see the Portrait Orientation Lock button, there is a link about accessing more controls in Control Center.
Control Center page (105001, also cited): iPhone with Face ID: swipe down from the upper-right corner. iPhone with a Home button: swipe up from the bottom edge of the screen.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I have an older iPhone 8 with the round Home button. I read in bed and want the page to stay upright, but later I'll want it to turn sideways again for photos. Can I do both?",
                 """Yes, you can lock it now and turn the lock off later. This takes a few seconds.

1. Swipe up from the bottom edge of the screen to open **Control Center**.
2. Tap the **Portrait Orientation Lock** button.
3. Close Control Center.

When you want the screen to turn sideways again:

1. Open **Control Center** again.
2. Tap the **Portrait Orientation Lock** button to make sure it's off.
3. Close Control Center.
4. Turn the iPhone sideways.

Some apps don't support turning sideways, so the screen may stay upright in those even with the lock off.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "iPhone 13 here. The screen keeps flipping sideways while I read. Help?",
                 """You can lock the screen so it stays upright.

1. **Swipe down from the top-right corner** of the screen to open **Control Center**.
2. Tap the **Portrait Orientation Lock** button.
3. Close Control Center.""",
                 "I swiped down from the top but I can't find any button.",
                 """Control Center opens from the corner, not the middle of the top edge.

1. Put your finger on the **top-right corner** of the screen.
2. Swipe down from there to open **Control Center**.
3. Tap the **Portrait Orientation Lock** button.
4. Close Control Center.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-109', "task_type": 'rotation_lock', "task": 'Stop the screen from turning sideways',
        "platform": 'Android', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Android Accessibility Help: How to make your screen rotate all by itself', "url": 'https://support.google.com/accessibility/android/answer/6006961?hl=en'},
        "source_notes": """Page intro: "Your phone screen can turn by itself." Steps: 1 Open your device's Settings app. 2 Tap Display & touch. 3 To turn the Auto-rotate screen on or off, select Auto-rotate screen.
Note: "If you use TalkBack, you must turn off auto-rotate, because rotating the screen can interrupt spoken feedback."
Page has no other troubleshooting, no Quick Settings route, no per-phone differences. "Get more help": "For more Accessibility help, contact the Disability Support team."
""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "I use TalkBack on my Android phone because my eyesight is poor. When I turn the phone in my hand the screen turns too and it interrupts the voice. How do I stop the screen rotating?",
                 """Turning off auto-rotate is the right fix. If you use TalkBack, auto-rotate must be off, because turning the screen can interrupt the spoken voice.

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Select **Auto-rotate screen** to turn it off.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My Android screen won't stop turning when I tilt the phone. How do I turn that off?",
                 """You can turn off auto-rotate. It takes a few seconds.

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Select **Auto-rotate screen** to turn it off.""",
                 "I opened Settings but there is no Display & touch on my phone.",
                 """I'm sorry about that. The steps I have use **Display & touch**, and I can't confirm another place for this setting on your phone.

For more accessibility help, you can contact the Disability Support team.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-110', "task_type": 'force_restart', "task": 'Restart a frozen iPhone',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": 'Apple Support: Restart an unresponsive iPhone', "url": 'https://support.apple.com/en-us/116940'},
        "source_notes": """Face ID models: 1 Press and quickly release volume up. 2 Press and quickly release volume down. 3 Press and hold the side button until you see the Apple logo (might take longer than 10 seconds).
iPhone 7 and 7 Plus: press and hold both the side button and the volume down button at the same time until you see the Apple logo (might take longer than 10 seconds).
iPhone 6s and earlier: press and hold both the Home button and the side or top button until the Apple logo (around 10 seconds).
If it doesn't work: "If your iPhone doesn't turn on, charge your iPhone for one hour and then try again." If it shows a low-battery icon: check iPhone hardware then charge for 30 minutes or until it starts. "If your iPhone still won't turn on, you might need service."
""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "I have arthritis in my hands and I can't press two buttons at once. My iPhone has Face ID, it's frozen and the screen won't respond at all. Is there a way to restart it?",
                 f"""Yes. For an iPhone with Face ID, you press one button at a time. No step needs two buttons together.

{IPH_FACE_RESTART}

If it still doesn't turn on, charge it for one hour and try again. If it still won't turn on after that, it might need service.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone 7 froze and won't respond to anything. How do I restart it?",
                 """For an iPhone 7, you force restart it with two buttons.

1. Press and hold the **side button** and the **volume down** button at the same time.
2. Keep holding both until you see the **Apple logo**. This might take longer than 10 seconds.""",
                 "I held both for a long time and the screen is still black.",
                 """Let's try charging it first.

1. Charge the iPhone for one hour.
2. Then try again: hold the **side button** and **volume down** together until you see the **Apple logo**.

If it still won't turn on, it might need service.""",
             ]},
        ],
    },
    {
        "task_id": 'TR-111', "task_type": 'phone_not_charging', "task": 'Phone is not charging',
        "platform": 'iPhone', "category": 'technical_support', "sensitive": False,
        "source": {"title": "Apple Support: If your iPhone or iPod touch won't charge", "url": 'https://support.apple.com/en-ca/108805'},
        "source_notes": """If your device won't charge: 1 Plug into a computer, power accessory, or wall outlet. 2 Restart the iPhone (no how given). 3 Check cable and USB adapter for damage; don't use damaged accessories. 4 Use a wall outlet; make sure cable, adapter and outlet connect firmly, or try a different outlet. 5 Remove debris from the charging port on the bottom, then firmly plug in the cable. 6 Let it charge for half an hour. 7 If it still won't power on or shows a battery icon, force restart: iPhone 8 or later: quickly press and release volume up, then volume down, then press and hold side button until Apple logo. iPhone 7: hold side and volume down until Apple logo. iPhone 6s or earlier: side/top and Home. 8 Charge another half hour.
Stopped at 80 percent: Optimized Battery Charging (iOS 13+); warm battery may limit charging above 80 until it cools (move iPhone and charger somewhere cooler); iPhone 15 and later may have a Charge Limit (change the charging limit; no path given).
Alert says accessory not supported or certified: 1 Connect directly to the charger, with no adapters or other equipment in between. 2 Remove debris from the charging port. 3 Restart the iPhone. 4 Try a different USB cable or charger. 5 Make sure you have the latest iOS.
If still won't power on or charge: you might need service.""",
        "examples": [
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "My iPhone 12 only shows a little picture of a battery and won't charge. I have just the one cable and charger, so I can't borrow another one. What can I do with only what I have?",
                 f"""You can try these with your own cable and charger. This takes about an hour, mostly waiting.

1. Check the cable and the adapter for damage. If either is damaged, don't use it.
2. Plug into a wall outlet. Make sure the cable, the adapter, and the outlet connect firmly, or try a different outlet.
3. Look at the charging port on the bottom of the phone and remove any debris. Then plug the cable in firmly.
4. Let it charge for half an hour.
If it still won't turn on or still shows the battery picture, force restart it:
5. Press and quickly release the **volume up** button.
6. Press and quickly release the **volume down** button.
7. Press and **hold** the **side button** until you see the **Apple logo**.
8. Let it charge for another half hour.

If it still won't charge, it might need service.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPhone",
             "messages": [
                 "iPhone 11 isn't charging when I plug it in. What can I check?",
                 """Let's go through some checks. This takes about an hour, mostly waiting.

1. Check the cable and the adapter for damage. Don't use damaged ones.
2. Plug into a wall outlet. Make sure everything connects firmly, or try a different outlet.
3. Remove any debris from the charging port on the bottom of the phone, then plug the cable in firmly.
4. Let it charge for half an hour.
If it still won't turn on or shows a battery picture, force restart it:
5. Press and quickly release **volume up**.
6. Press and quickly release **volume down**.
7. Press and **hold** the **side button** until you see the **Apple logo**.
8. Let it charge for another half hour.""",
                 "Now it shows a message that the accessory is not supported or certified.",
                 """Try these.

1. Plug the iPhone straight into the charger, with no adapters or other equipment in between.
2. Remove any debris from the charging port on the bottom of the phone.
3. Restart the iPhone.
4. Try a different USB cable or charger.

Also make sure your iPhone has the latest version of iOS. If it still won't charge, it might need service.""",
             ]},
        ],
    },
]
