TASKS = [
    {
        "task_id": "TR-199",
        "task_type": "email_attach",
        "task": "Attach a file or photo to an email",
        "platform": "Outlook.com",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Add pictures or attach files in Outlook.com on Outlook on the web", "url": "https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab"},
        "source_notes": """Attach a file from your computer: 1. Start a reply, forward, or new email. 2. Select Attach, then select Browse this computer. 3. Choose the file and select Open. To attach several files, hold CTRL (Command on a Mac) while selecting them.
You can also drag files from the computer into the message; a drop hint appears as you drag over the message.
Attach a OneDrive file as a link: start a reply, forward, or new email; select Attach, then Browse cloud locations; choose the file and select Next (hold CTRL or Command to pick several). To restrict editing on a OneDrive attachment, select More actions, then Manage access. Other cloud storage such as Box, Dropbox, or Google Drive can be added under Storage account settings.
Page gives no size limit and no specific troubleshooting.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "I'm writing an email in Outlook.com and want to attach a Word file that is saved on my computer. How?",
                 """Here is how to attach a file from your computer in Outlook.com.

1. In your new email, select **Attach**.
2. Select **Browse this computer**.
3. In the window that opens, click the file you want.
4. Select **Open**.

If you want to attach more than one file, hold the CTRL key while you click each file before you select **Open**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "ok so my granddaughter sent me her school pictures and I saved four of them on my Mac and now I'm in Outlook.com writing to my sister and I'd like to put all four pictures on the email but I don't know how to get more than one on there. I'm using a Mac. Can you help",
                 """Yes, you can attach all four at once.

1. In your email, select **Attach**.
2. Select **Browse this computer**.
3. Click the first picture.
4. Hold down the Command key, then click each of the other three pictures.
5. Select **Open**.

All four pictures are added to your email together.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "how do i put a document on my outlook.com email",
                 "I can help with that. Is the document saved on your computer, or is it in OneDrive?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "how do i put a document on my outlook.com email",
                 "I can help with that. Is the document saved on your computer, or is it in OneDrive?",
                 "it's on my computer",
                 """Thanks. Here is how to attach it.

1. Start a new email, or open a reply.
2. Select **Attach**.
3. Select **Browse this computer**.
4. Click your document.
5. Select **Open**.

If you would rather not use the menu, you can also drag the document from your computer into the message.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "My tax papers are stored in OneDrive. I'm writing an Outlook.com email on my computer. I don't want to download them to my computer first, I just want to send them from OneDrive. Is that possible?",
                 """Yes. You can attach a OneDrive file straight from your email, without downloading it.

1. In your email, select **Attach**.
2. Select **Browse cloud locations**.
3. Click the file you want.
4. Select **Next**.

The file is attached as a link. To limit what people can do with it, select **More actions**, then **Manage access**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "How do I attach a picture from my computer to an Outlook.com email?",
                 """Here is how to attach a picture from your computer.

1. In your email, select **Attach**.
2. Select **Browse this computer**.
3. Click the picture you want.
4. Select **Open**.""",
                 "that worked but I have 3 more pictures to add and when I did it again it only let me pick one at a time",
                 """You can pick several at once.

1. Select **Attach**, then **Browse this computer**.
2. Hold down the CTRL key (the Command key on a Mac).
3. While holding it, click each picture you want.
4. Select **Open**.

You can also drag the pictures from your computer into the message.""",
             ]},
        ],
    },
    {
        "task_id": "TR-200",
        "task_type": "email_not_working",
        "task": "Email is not arriving or syncing",
        "platform": "Outlook.com",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Can't send or receive email in Outlook.com", "url": "https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642"},
        "source_notes": """(Replaced the junk/block topic: the Outlook.com junk page could not be read at step level.)
Step 1 Check storage: if your Microsoft cloud storage is full you cannot send or receive email. Messages sent to you while it was full bounce back to the sender and cannot be recovered. Open the mailbox storage page to see what is using space, free some up, then continue.
Step 2 Check account: if you changed your password recently, update it. If you see a message that your account is temporarily blocked, follow the unblock guidance for Outlook.com (can happen after unusual sign-in activity). If you cannot sign in at all, use the Microsoft account sign-in helper.
Step 3 Receiving problems: Other tab: look for filters that hide messages, confirm you can see all messages. Junk Email: check the Junk Email settings and folder; for legitimate messages, right-click each one and select Mark as not junk to move it to the Inbox. Message order: if messages seem out of place, select Filter, then Sort, then Date to restore chronological order. Forwarding: check whether email forwarding is turned on. Rules: check for email rules that could block or redirect the message. Third-party mail needs modern authentication and IMAP; if IMAP or POP is active, disable both and test again. Specific missing email with no error: ask the sender to review Sender Support in Outlook.com.
Step 4 Sending problems: attachments over 25 MB will not send; bounce messages; new account has a temporary low sending limit; remove signature and resend; recipient may add you to Safe Senders; add recipients to Contacts.
Step 6 run the interactive troubleshooter (Start). Step 7 Select Help on the menu bar in Outlook.com and enter your query.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "My son says he sent me an email last night but I never got it in my Outlook.com inbox. Where could it be?",
                 """It may have landed in a place other than your inbox. Try these.

1. Look at the **Other** tab, in case a filter hid it. Make sure you can see all messages.
2. Open your **Junk Email** folder.
3. If you find his message there, right-click it and select **Mark as not junk**. This moves it to your Inbox.

If it is in neither place, check whether email forwarding is turned on, and whether you have any email rules that could redirect it.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "Hello, for about a week now no new mail has come into my Outlook.com account, not from my church group, not from my pharmacy, nothing, and this morning I saw a message at the top saying my Microsoft storage is full. My neighbor said that might be the reason. Is it?",
                 """Yes, that can be the reason. When your Microsoft cloud storage is full, you cannot send or receive email.

1. Open your mailbox storage page to see what is using the space.
2. Free up some space.
3. Check your inbox again for new mail.

Messages people sent while your storage was full bounced back to them and cannot be recovered, so you may need to ask them to send again.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "incomplete", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my emails stopped coming in",
                 "I can help with that. Which email do you use: **Outlook.com**, **Gmail**, or something else?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "my emails stopped coming in",
                 "I can help with that. Which email do you use: **Outlook.com**, **Gmail**, or something else?",
                 "outlook.com",
                 """Thanks. Try these checks for Outlook.com.

1. Open the **Junk Email** folder. If good mail is there, right-click it and select **Mark as not junk**.
2. Check whether email forwarding is turned on, since that could send your mail somewhere else.
3. Check for email rules that could block or redirect messages.
4. If your Microsoft cloud storage is full, free some space, because a full mailbox cannot receive email.

If a message from one person is still missing, ask that person to review Sender Support in Outlook.com.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "My Outlook.com isn't showing an email from my doctor's office. I'm nervous about breaking something, so I don't want to change any settings or rules. Is there anything I can just look at?",
                 """Yes, you can find it just by looking.

1. Click the **Other** tab and look through it. Make sure you can see all of your messages.
2. Open the **Junk Email** folder and look for the message.
3. If you find it in Junk Email, right-click it and select **Mark as not junk**. This only moves that one message to your Inbox.

None of these steps changes your settings or rules.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "An email from my sister is missing from my Outlook.com inbox. Where should I look?",
                 """Here is where to look.

1. Check the **Other** tab, in case a filter hid it.
2. Open the **Junk Email** folder.
3. If her message is there, right-click it and select **Mark as not junk**. This moves it to your Inbox.""",
                 "found it in junk and moved it, thank you. but now my inbox looks jumbled and the newest emails aren't at the top",
                 """You can put your messages back in date order.

1. Select **Filter**.
2. Select **Sort**.
3. Select **Date**.

Your messages should now be in chronological order.""",
             ]},
        ],
    },
    {
        "task_id": "TR-201",
        "task_type": "recover_deleted_email",
        "task": "Recover a deleted email",
        "platform": "Outlook.com",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Microsoft Support: Email is missing from your Outlook.com inbox", "url": "https://support.microsoft.com/office/c70b4a9a-caa5-4e8c-a88a-3372215af25e"},
        "source_notes": """1. Check the Deleted Items folder. If the message is there, select it, then select Restore. On the Outlook mobile apps or a mobile browser: select the message, choose the More options icon, then Move to folder, then Inbox.
2. If not in Deleted Items: above the message list, look for Recover items deleted from this folder. Select it, find your message, select it, then select Restore. Removed items are recoverable for 30 days. You cannot do this recovery on the mobile apps or a mobile browser; use a computer.
3. Check the Archive folder: archived messages do not appear in the inbox. If found, select it, then Move to, then Inbox. On mobile use More options, Move to folder, Inbox.
Limits: messages deleted from a child's account cannot be recovered. Junk Email folder messages are removed automatically after 30 days and cannot be recovered. If you do not sign in to Outlook.com for one year, Microsoft closes the mailbox and all email is deleted.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "I deleted an email in Outlook.com by mistake this morning and I need it back. I'm on my computer.",
                 """Let's look in your Deleted Items folder first.

1. Open the **Deleted Items** folder.
2. Select the message you want back.
3. Select **Restore**.

If it is not in **Deleted Items**, look above the message list for **Recover items deleted from this folder** and select it. Find your message, select it, then select **Restore**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "I cleaned out my Outlook.com a couple of weeks ago, I even emptied the Deleted Items folder like a tidy person, and now I realize I threw away the confirmation for my husband's surgery date. I am on my laptop. Is it gone forever?",
                 """It may not be gone. Removed items can be recovered for 30 days.

1. Open the **Deleted Items** folder.
2. Above the message list, select **Recover items deleted from this folder**.
3. Find your message and select it.
4. Select **Restore**.

You must use a computer for this, and you are on your laptop, so that is fine.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "i deleted an email i need to get it back",
                 "I can help with that. Are you using Outlook.com on a **computer** or on a **phone**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "i deleted an email i need to get it back",
                 "I can help with that. Are you using Outlook.com on a **computer** or on a **phone**?",
                 "computer",
                 """Thanks. Start with your Deleted Items folder.

1. Open the **Deleted Items** folder.
2. Select the message.
3. Select **Restore**.

If you cannot find it there, look above the message list for **Recover items deleted from this folder**. Select it, select your message, then select **Restore**. Removed items can be recovered for 30 days.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "I'm away from home and all I have is my phone, no computer. I deleted an important email in the Outlook.com app. Can I get it back from here?",
                 """Yes, if it is still in your Deleted Items folder.

1. Open the **Deleted Items** folder.
2. Select the message.
3. Choose the **More options** icon.
4. Select **Move to folder**, then **Inbox**.

If it is not in **Deleted Items**, the next recovery option, **Recover items deleted from this folder**, cannot be done on the phone app or a phone browser. You will need a computer for that.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Outlook.com",
             "messages": [
                 "I emptied my Deleted Items folder in Outlook.com and now need one email back. I'm on a computer.",
                 """You can try to recover it.

1. Open the **Deleted Items** folder.
2. Above the message list, select **Recover items deleted from this folder**.
3. Find your message and select it.
4. Select **Restore**.""",
                 "i looked in the Recover list and it's not there either",
                 """Check your Archive folder next. Archived messages do not show in your inbox.

1. Open the **Archive** folder.
2. Select the message if you find it.
3. Select **Move to**, then **Inbox**.

If it is not there either, it may be past the 30 days that removed items can be recovered.""",
             ]},
        ],
    },
    {
        "task_id": "TR-202",
        "task_type": "email_labels",
        "task": "Organize email with labels",
        "platform": "Gmail (computer)",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Gmail Help: Create & manage labels in Gmail", "url": "https://support.google.com/mail/answer/118708?hl=en"},
        "source_notes": """Create a label (computer): 1. Open Gmail. 2. On the left, next to Labels, click Create new label (the plus icon). 3. Type a name. 4. Optional: to put it inside another label, check Nest label under and choose the parent. 5. Click Create.
Add an email to a label: check the box next to the email, click Labels at the top, select the label. For a new email being written: Compose, then at bottom right More options, then Label.
Move an email to a different label: check the box next to the email, click Labels at the top, uncheck the current label, select the new one.
Show or hide labels in the sidebar: click Settings (gear icon) at top right, then See all settings, then the Labels tab at the top, then next to a label click Show or Hide.
Troubleshooting: missing label in the sidebar may be set to hidden, check the Labels tab. With conversation view on a label applies only to existing messages in the conversation; deleting an email removes it from all labels and the inbox. Up to 5,000 labels.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "I'd like to make a label called Taxes in Gmail so my tax emails are all together. I'm on my computer.",
                 """Here is how to make a label called Taxes.

1. Open Gmail on your computer.
2. On the left, next to **Labels**, click **Create new label**. It looks like a plus icon.
3. Type **Taxes** as the name.
4. Click **Create**.

Your new label is ready to use.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "I already have a Gmail label called Family on my computer, but now my emails from the grandkids are mixed in with everything else. I'd like a new label named Grandkids that sits inside the Family one, kind of like a folder in a folder. Is that something I can do?",
                 """Yes, you can place one label inside another.

1. On the left, next to **Labels**, click **Create new label**.
2. Type **Grandkids** as the name.
3. Check **Nest label under**.
4. Choose **Family** as the parent.
5. Click **Create**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my gmail is such a mess, how do I organize it with labels",
                 "I can help with that. Are you using Gmail on a **computer** or on a **phone**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "my gmail is such a mess, how do I organize it with labels",
                 "I can help with that. Are you using Gmail on a **computer** or on a **phone**?",
                 "on my computer",
                 """Thanks. First make a label, then put emails in it.

1. Open Gmail. On the left, next to **Labels**, click **Create new label**.
2. Type a name and click **Create**.
3. Check the box next to an email you want to file.
4. At the top, click **Labels**.
5. Select your new label.

Repeat steps 3 to 5 for any other emails.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "On Gmail on my computer I put a bunch of emails under the label Misc, but they really belong under my label Recipes. I don't want them in both places, I want them moved from Misc to Recipes. How?",
                 """You can move them from one label to the other.

1. Check the box next to each email you want to move.
2. At the top, click **Labels**.
3. Uncheck **Misc**.
4. Select **Recipes**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "How do I create a label in Gmail on my computer? I want one called Bills.",
                 """Here is how to create the label.

1. On the left, next to **Labels**, click **Create new label**.
2. Type **Bills** as the name.
3. Click **Create**.""",
                 "I did that but I can't see Bills on the left side anywhere",
                 """The label may be set to hidden. Here is how to show it.

1. At the top right, click **Settings**, the gear icon, then **See all settings**.
2. Click the **Labels** tab at the top.
3. Find **Bills** and click **Show** next to it.""",
             ]},
        ],
    },
    {
        "task_id": "TR-203",
        "task_type": "auto_reply",
        "task": "Set an out-of-office (vacation) reply",
        "platform": "Gmail (computer)",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Gmail Help: Send automatic replies from Gmail", "url": "https://support.google.com/mail/answer/25922?hl=en"},
        "source_notes": """Turn on (computer): 1. Open Gmail. 2. At the top right, click Settings, then See all settings. 3. Under the General tab, go to the Vacation responder section. 4. Select Vacation responder on. 5. Fill in the date range, subject, and message. 6. Optional: to send the reply to your contacts only, under the message, check the box. 7. At the bottom of the page, click Save Changes.
Turn off: while on, a banner shows across the top of your inbox; click End now.
Notes: reply starts at 12:00 AM on the start date and ends 11:59 PM on the end date unless ended earlier. Most people get the reply only the first time they message you; someone may get it again if they write after four days while it is still on, or if you edit the reply and they write again. Adding a subject sends it as a separate email instead of inside an existing thread. A signature appears below the reply. Emails in spam, or sent to a mailing list you subscribe to, do not get the reply.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "I'm going away next week. How do I set up an automatic out of office reply in Gmail on my computer?",
                 """Here is how to turn on your vacation reply.

1. Open Gmail on your computer.
2. At the top right, click **Settings**, then **See all settings**.
3. On the **General** tab, scroll to the **Vacation responder** section.
4. Select **Vacation responder on**.
5. Fill in the date range, subject, and message.
6. At the bottom of the page, click **Save Changes**.

The reply starts at 12:00 AM on your first date and ends at 11:59 PM on your last date.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "My knitting club emails me all the time and I'll be at my sister's for two weeks with no computer or internet. I'd like Gmail to tell people I'm away and when I'll be back. I'm on my laptop in a web browser right now. Please go slow, I'm not good at settings.",
                 """Happy to. Go one step at a time.

1. In Gmail, at the top right, click **Settings**.
2. Click **See all settings**.
3. Stay on the **General** tab and scroll down to **Vacation responder**.
4. Select **Vacation responder on**.
5. Enter the first and last day of your trip, a subject, and a message saying when you will be back.
6. At the bottom of the page, click **Save Changes**.

Most people will get your reply only the first time they write to you.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "set up an auto reply on my gmail while im on vacation",
                 "I can help with that. Are you using Gmail on a **computer** or on a **phone**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "set up an auto reply on my gmail while im on vacation",
                 "I can help with that. Are you using Gmail on a **computer** or on a **phone**?",
                 "computer",
                 """Thanks. Here are the steps on a computer.

1. Open Gmail.
2. At the top right, click **Settings**, then **See all settings**.
3. Under the **General** tab, go to **Vacation responder**.
4. Select **Vacation responder on**.
5. Fill in the date range, subject, and message.
6. At the bottom, click **Save Changes**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "I want an out of office reply in Gmail on my computer, but I only want the people in my contacts to get it. I don't want strangers or random senders to know I'm away from home. Can it do that?",
                 """Yes. There is a box for exactly that.

1. Click **Settings** at the top right, then **See all settings**.
2. On the **General** tab, go to **Vacation responder** and select **Vacation responder on**.
3. Fill in the date range, subject, and message.
4. Under the message, check the box to send the reply to your contacts only.
5. At the bottom, click **Save Changes**.

Emails in your spam folder do not get the reply either.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "How do I turn on a vacation reply in Gmail on my computer?",
                 """Here is how to turn it on.

1. At the top right, click **Settings**, then **See all settings**.
2. On the **General** tab, go to **Vacation responder**.
3. Select **Vacation responder on**.
4. Fill in the date range, subject, and message.
5. At the bottom, click **Save Changes**.""",
                 "thanks it worked. but I came home early and it's still sending the reply. how do I stop it",
                 """You can end it early.

1. Open your Gmail inbox.
2. Look at the banner across the top of the inbox.
3. Click **End now** on that banner.""",
             ]},
        ],
    },
    {
        "task_id": "TR-204",
        "task_type": "print_email",
        "task": "Print an email",
        "platform": "Gmail (computer)",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Gmail Help: Print Gmail messages", "url": "https://support.google.com/mail/answer/8255?co=GENIE.Platform%3DDesktop&hl=en"},
        "source_notes": """Print one email (computer): 1. Go to Gmail. 2. Open the email you want to print. 3. At the top right of the email, click More (three dot icon). 4. Click Print.
Print a whole conversation (an email with replies): 1. Go to Gmail. 2. Open the conversation. 3. At the top right, click Print all.
Notes: if a conversation has several emails, the single email method prints just the one you open. The page does not describe the printer window. If the sender used confidential mode, you cannot print the message text or attachments.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "How can I print one email from my Gmail? I'm on a computer.",
                 """Here is how to print one email.

1. Open Gmail on your computer.
2. Open the email you want to print.
3. At the top right of the email, click **More**. It looks like three dots.
4. Click **Print**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "My daughter and I went back and forth about the flight times for my trip, like six emails in a row all stacked together in Gmail, and I'd like a paper copy of the whole conversation to take to the airport. I'm using Gmail on my desktop computer. How do I print everything together?",
                 """You can print the whole conversation at once.

1. Open Gmail on your computer.
2. Open the conversation with your daughter.
3. At the top right, click **Print all**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "incomplete", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "print my email",
                 "I can help with that. Are you using Gmail on a **computer** or on a **phone**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "print my email",
                 "I can help with that. Are you using Gmail on a **computer** or on a **phone**?",
                 "its a computer",
                 """Thanks. Here is how to print an email on a computer.

1. Go to Gmail.
2. Open the email you want to print.
3. At the top right of the email, click **More**, the three dot icon.
4. Click **Print**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "There's a long chain of replies in Gmail but I only need the one email from my landlord with the new address, I don't want the paper full of all the other replies. I'm on my computer. How do I print just that one?",
                 """To print only that one email, use the single email option.

1. Open the email from your landlord.
2. At the top right of that email, click **More**, the three dot icon.
3. Click **Print**.

Do not use **Print all**, because that prints the whole conversation.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Gmail (computer)",
             "messages": [
                 "Walk me through printing a message from my Gmail inbox. Computer, not phone.",
                 """Here is how to print an email.

1. Open the email you want to print.
2. At the top right of the email, click **More**, the three dot icon.
3. Click **Print**.""",
                 "that works for my other emails but the one from my bank won't print, not the message and not the attachment",
                 """The sender may have sent it in confidential mode. That setting stops people from printing the message text and attachments.

So this email cannot be printed the normal way, even though your other emails can.""",
             ]},
        ],
    },
    {
        "task_id": "TR-205",
        "task_type": "add_contact",
        "task": "Add a contact",
        "platform": "Google Contacts (computer)",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Google Contacts Help: Add or move contacts", "url": "https://support.google.com/contacts/answer/1069522?hl=en"},
        "source_notes": """Add a contact on a computer: 1. Open Google Contacts at contacts.google.com. 2. At the top left, click Create contact, then choose Create a contact (or Create multiple contacts to add several at once). 3. Enter the contact's details; names, email addresses, phone numbers, and more can be saved. 4. Click Save.
Contacts are saved to your Google Account and sync with Google Contacts and all your Android devices.
Notes: if you email someone you have not added, Google Contacts saves their address automatically under Other contacts. To stop this: open Gmail on a computer, go to Settings, select I'll add contacts myself in the Create contacts for auto-complete section, and click Save changes. To review or delete these, go to Google Contacts and click Other contacts on the left. Other contacts does not appear on iPhone, iPad, or Android. No troubleshooting for a failed save.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Google Contacts (computer)",
             "messages": [
                 "How do I add a new person to my Google Contacts? I'm on a computer.",
                 """Here is how to add a contact.

1. Go to contacts.google.com.
2. At the top left, click **Create contact**.
3. Choose **Create a contact**.
4. Type in the person's details, such as their name, email address, and phone number.
5. Click **Save**.

The contact is saved to your Google Account.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Google Contacts (computer)",
             "messages": [
                 "I just met a lovely woman at my pottery class, Marjorie, and she gave me her email and her phone number on a napkin. I would like to put both of them into my Google Contacts so I don't lose them. I'm at my computer with the Contacts page open. What do I click?",
                 """Here is what to click.

1. At the top left, click **Create contact**.
2. Choose **Create a contact**.
3. Type Marjorie's name, her email address, and her phone number.
4. Click **Save**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I want to save my neighbor's number in my google contacts",
                 "I can help with that. Are you using a **computer** or a **phone**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Google Contacts (computer)",
             "messages": [
                 "I want to save my neighbor's number in my google contacts",
                 "I can help with that. Are you using a **computer** or a **phone**?",
                 "computer",
                 """Thanks. Here is how on a computer.

1. Go to contacts.google.com.
2. At the top left, click **Create contact**, then **Create a contact**.
3. Enter your neighbor's name and phone number.
4. Click **Save**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Google Contacts (computer)",
             "messages": [
                 "My new plumber only gave me his phone number, no email address. I'm on my computer and want to add him to Google Contacts. Is that okay, or do I have to have an email for him?",
                 """You do not need an email address. Contacts can hold names, phone numbers, and more.

1. Go to contacts.google.com.
2. At the top left, click **Create contact**, then **Create a contact**.
3. Type his name and phone number.
4. Click **Save**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Google Contacts (computer)",
             "messages": [
                 "How do I add my friend Linda to Google Contacts on my computer?",
                 """Here is how to add Linda.

1. Go to contacts.google.com.
2. At the top left, click **Create contact**, then **Create a contact**.
3. Type Linda's details.
4. Click **Save**.""",
                 "wait, I have emailed Linda before but I never saved her anywhere, and I don't see her in my list of contacts. is she lost?",
                 """She may not be lost. When you email someone you have not added, Google Contacts saves their address automatically under **Other contacts**.

1. Go to contacts.google.com.
2. On the left, click **Other contacts**.
3. Look for Linda there.""",
             ]},
        ],
    },
]
