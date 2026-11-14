# Review input: batch ny7a, round 1 (42 examples)

## tr199-a
- scenario: direct | style: plain | specification: fully_specified | platform: Outlook.com
- task: Attach a file or photo to an email (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab

**USER:**
I'm writing an email in Outlook.com and want to attach a Word file that is saved on my computer. How?

**ASSISTANT:**
Here is how to attach a file from your computer in Outlook.com.

1. In your new email, select **Attach**.
2. Select **Browse this computer**.
3. In the window that opens, click the file you want.
4. Select **Open**.

If you want to attach more than one file, hold the CTRL key while you click each file before you select **Open**.

## tr199-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Outlook.com
- task: Attach a file or photo to an email (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab

**USER:**
ok so my granddaughter sent me her school pictures and I saved four of them on my Mac and now I'm in Outlook.com writing to my sister and I'd like to put all four pictures on the email but I don't know how to get more than one on there. I'm using a Mac. Can you help

**ASSISTANT:**
Yes, you can attach all four at once.

1. In your email, select **Attach**.
2. Select **Browse this computer**.
3. Click the first picture.
4. Hold down the Command key, then click each of the other three pictures.
5. Select **Open**.

All four pictures are added to your email together.

## tr199-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Attach a file or photo to an email (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab

**USER:**
how do i put a document on my outlook.com email

**ASSISTANT:**
I can help with that. Is the document saved on your computer, or is it in OneDrive?

## tr199-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Outlook.com
- task: Attach a file or photo to an email (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab

**USER:**
how do i put a document on my outlook.com email

**ASSISTANT:**
I can help with that. Is the document saved on your computer, or is it in OneDrive?

**USER:**
it's on my computer

**ASSISTANT:**
Thanks. Here is how to attach it.

1. Start a new email, or open a reply.
2. Select **Attach**.
3. Select **Browse this computer**.
4. Click your document.
5. Select **Open**.

If you would rather not use the menu, you can also drag the document from your computer into the message.

## tr199-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Outlook.com
- task: Attach a file or photo to an email (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab

**USER:**
My tax papers are stored in OneDrive. I'm writing an Outlook.com email on my computer. I don't want to download them to my computer first, I just want to send them from OneDrive. Is that possible?

**ASSISTANT:**
Yes. You can attach a OneDrive file straight from your email, without downloading it.

1. In your email, select **Attach**.
2. Select **Browse cloud locations**.
3. Click the file you want.
4. Select **Next**.

The file is attached as a link. To limit what people can do with it, select **More actions**, then **Manage access**.

## tr199-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Outlook.com
- task: Attach a file or photo to an email (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab

**USER:**
How do I attach a picture from my computer to an Outlook.com email?

**ASSISTANT:**
Here is how to attach a picture from your computer.

1. In your email, select **Attach**.
2. Select **Browse this computer**.
3. Click the picture you want.
4. Select **Open**.

**USER:**
that worked but I have 3 more pictures to add and when I did it again it only let me pick one at a time

**ASSISTANT:**
You can pick several at once.

1. Select **Attach**, then **Browse this computer**.
2. Hold down the CTRL key (the Command key on a Mac).
3. While holding it, click each picture you want.
4. Select **Open**.

You can also drag the pictures from your computer into the message.

## tr200-a
- scenario: direct | style: plain | specification: fully_specified | platform: Outlook.com
- task: Email is not arriving or syncing (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642

**USER:**
My son says he sent me an email last night but I never got it in my Outlook.com inbox. Where could it be?

**ASSISTANT:**
It may have landed in a place other than your inbox. Try these.

1. Look at the **Other** tab, in case a filter hid it. Make sure you can see all messages.
2. Open your **Junk Email** folder.
3. If you find his message there, right-click it and select **Mark as not junk**. This moves it to your Inbox.

If it is in neither place, check whether email forwarding is turned on, and whether you have any email rules that could redirect it.

## tr200-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Outlook.com
- task: Email is not arriving or syncing (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642

**USER:**
Hello, for about a week now no new mail has come into my Outlook.com account, not from my church group, not from my pharmacy, nothing, and this morning I saw a message at the top saying my Microsoft storage is full. My neighbor said that might be the reason. Is it?

**ASSISTANT:**
Yes, that can be the reason. When your Microsoft cloud storage is full, you cannot send or receive email.

1. Open your mailbox storage page to see what is using the space.
2. Free up some space.
3. Check your inbox again for new mail.

Messages people sent while your storage was full bounced back to them and cannot be recovered, so you may need to ask them to send again.

## tr200-b
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Email is not arriving or syncing (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642

**USER:**
my emails stopped coming in

**ASSISTANT:**
I can help with that. Which email do you use: **Outlook.com**, **Gmail**, or something else?

## tr200-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Outlook.com
- task: Email is not arriving or syncing (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642

**USER:**
my emails stopped coming in

**ASSISTANT:**
I can help with that. Which email do you use: **Outlook.com**, **Gmail**, or something else?

**USER:**
outlook.com

**ASSISTANT:**
Thanks. Try these checks for Outlook.com.

1. Open the **Junk Email** folder. If good mail is there, right-click it and select **Mark as not junk**.
2. Check whether email forwarding is turned on, since that could send your mail somewhere else.
3. Check for email rules that could block or redirect messages.
4. If your Microsoft cloud storage is full, free some space, because a full mailbox cannot receive email.

If a message from one person is still missing, ask that person to review Sender Support in Outlook.com.

## tr200-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Outlook.com
- task: Email is not arriving or syncing (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642

**USER:**
My Outlook.com isn't showing an email from my doctor's office. I'm nervous about breaking something, so I don't want to change any settings or rules. Is there anything I can just look at?

**ASSISTANT:**
Yes, you can find it just by looking.

1. Click the **Other** tab and look through it. Make sure you can see all of your messages.
2. Open the **Junk Email** folder and look for the message.
3. If you find it in Junk Email, right-click it and select **Mark as not junk**. This only moves that one message to your Inbox.

None of these steps changes your settings or rules.

## tr200-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Outlook.com
- task: Email is not arriving or syncing (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642

**USER:**
An email from my sister is missing from my Outlook.com inbox. Where should I look?

**ASSISTANT:**
Here is where to look.

1. Check the **Other** tab, in case a filter hid it.
2. Open the **Junk Email** folder.
3. If her message is there, right-click it and select **Mark as not junk**. This moves it to your Inbox.

**USER:**
found it in junk and moved it, thank you. but now my inbox looks jumbled and the newest emails aren't at the top

**ASSISTANT:**
You can put your messages back in date order.

1. Select **Filter**.
2. Select **Sort**.
3. Select **Date**.

Your messages should now be in chronological order.

## tr201-a
- scenario: direct | style: plain | specification: fully_specified | platform: Outlook.com
- task: Recover a deleted email (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/c70b4a9a-caa5-4e8c-a88a-3372215af25e

**USER:**
I deleted an email in Outlook.com by mistake this morning and I need it back. I'm on my computer.

**ASSISTANT:**
Let's look in your Deleted Items folder first.

1. Open the **Deleted Items** folder.
2. Select the message you want back.
3. Select **Restore**.

If it is not in **Deleted Items**, look above the message list for **Recover items deleted from this folder** and select it. Find your message, select it, then select **Restore**.

## tr201-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Outlook.com
- task: Recover a deleted email (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/c70b4a9a-caa5-4e8c-a88a-3372215af25e

**USER:**
I cleaned out my Outlook.com a couple of weeks ago, I even emptied the Deleted Items folder like a tidy person, and now I realize I threw away the confirmation for my husband's surgery date. I am on my laptop. Is it gone forever?

**ASSISTANT:**
It may not be gone. Removed items can be recovered for 30 days.

1. Open the **Deleted Items** folder.
2. Above the message list, select **Recover items deleted from this folder**.
3. Find your message and select it.
4. Select **Restore**.

You must use a computer for this, and you are on your laptop, so that is fine.

## tr201-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Recover a deleted email (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/c70b4a9a-caa5-4e8c-a88a-3372215af25e

**USER:**
i deleted an email i need to get it back

**ASSISTANT:**
I can help with that. Are you using Outlook.com on a **computer** or on a **phone**?

## tr201-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Outlook.com
- task: Recover a deleted email (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/c70b4a9a-caa5-4e8c-a88a-3372215af25e

**USER:**
i deleted an email i need to get it back

**ASSISTANT:**
I can help with that. Are you using Outlook.com on a **computer** or on a **phone**?

**USER:**
computer

**ASSISTANT:**
Thanks. Start with your Deleted Items folder.

1. Open the **Deleted Items** folder.
2. Select the message.
3. Select **Restore**.

If you cannot find it there, look above the message list for **Recover items deleted from this folder**. Select it, select your message, then select **Restore**. Removed items can be recovered for 30 days.

## tr201-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Outlook.com
- task: Recover a deleted email (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/c70b4a9a-caa5-4e8c-a88a-3372215af25e

**USER:**
I'm away from home and all I have is my phone, no computer. I deleted an important email in the Outlook.com app. Can I get it back from here?

**ASSISTANT:**
Yes, if it is still in your Deleted Items folder.

1. Open the **Deleted Items** folder.
2. Select the message.
3. Choose the **More options** icon.
4. Select **Move to folder**, then **Inbox**.

If it is not in **Deleted Items**, the next recovery option, **Recover items deleted from this folder**, cannot be done on the phone app or a phone browser. You will need a computer for that.

## tr201-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Outlook.com
- task: Recover a deleted email (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/c70b4a9a-caa5-4e8c-a88a-3372215af25e

**USER:**
I emptied my Deleted Items folder in Outlook.com and now need one email back. I'm on a computer.

**ASSISTANT:**
You can try to recover it.

1. Open the **Deleted Items** folder.
2. Above the message list, select **Recover items deleted from this folder**.
3. Find your message and select it.
4. Select **Restore**.

**USER:**
i looked in the Recover list and it's not there either

**ASSISTANT:**
Check your Archive folder next. Archived messages do not show in your inbox.

1. Open the **Archive** folder.
2. Select the message if you find it.
3. Select **Move to**, then **Inbox**.

If it is not there either, it may be past the 30 days that removed items can be recovered.

## tr202-a
- scenario: direct | style: plain | specification: fully_specified | platform: Gmail (computer)
- task: Organize email with labels (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/118708?hl=en

**USER:**
I'd like to make a label called Taxes in Gmail so my tax emails are all together. I'm on my computer.

**ASSISTANT:**
Here is how to make a label called Taxes.

1. Open Gmail on your computer.
2. On the left, next to **Labels**, click **Create new label**. It looks like a plus icon.
3. Type **Taxes** as the name.
4. Click **Create**.

Your new label is ready to use.

## tr202-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Gmail (computer)
- task: Organize email with labels (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/118708?hl=en

**USER:**
I already have a Gmail label called Family on my computer, but now my emails from the grandkids are mixed in with everything else. I'd like a new label named Grandkids that sits inside the Family one, kind of like a folder in a folder. Is that something I can do?

**ASSISTANT:**
Yes, you can place one label inside another.

1. On the left, next to **Labels**, click **Create new label**.
2. Type **Grandkids** as the name.
3. Check **Nest label under**.
4. Choose **Family** as the parent.
5. Click **Create**.

## tr202-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Organize email with labels (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/118708?hl=en

**USER:**
my gmail is such a mess, how do I organize it with labels

**ASSISTANT:**
I can help with that. Are you using Gmail on a **computer** or on a **phone**?

## tr202-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Gmail (computer)
- task: Organize email with labels (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/118708?hl=en

**USER:**
my gmail is such a mess, how do I organize it with labels

**ASSISTANT:**
I can help with that. Are you using Gmail on a **computer** or on a **phone**?

**USER:**
on my computer

**ASSISTANT:**
Thanks. First make a label, then put emails in it.

1. Open Gmail. On the left, next to **Labels**, click **Create new label**.
2. Type a name and click **Create**.
3. Check the box next to an email you want to file.
4. At the top, click **Labels**.
5. Select your new label.

Repeat steps 3 to 5 for any other emails.

## tr202-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Gmail (computer)
- task: Organize email with labels (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/118708?hl=en

**USER:**
On Gmail on my computer I put a bunch of emails under the label Misc, but they really belong under my label Recipes. I don't want them in both places, I want them moved from Misc to Recipes. How?

**ASSISTANT:**
You can move them from one label to the other.

1. Check the box next to each email you want to move.
2. At the top, click **Labels**.
3. Uncheck **Misc**.
4. Select **Recipes**.

## tr202-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Gmail (computer)
- task: Organize email with labels (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/118708?hl=en

**USER:**
How do I create a label in Gmail on my computer? I want one called Bills.

**ASSISTANT:**
Here is how to create the label.

1. On the left, next to **Labels**, click **Create new label**.
2. Type **Bills** as the name.
3. Click **Create**.

**USER:**
I did that but I can't see Bills on the left side anywhere

**ASSISTANT:**
The label may be set to hidden. Here is how to show it.

1. At the top right, click **Settings**, the gear icon, then **See all settings**.
2. Click the **Labels** tab at the top.
3. Find **Bills** and click **Show** next to it.

## tr203-a
- scenario: direct | style: plain | specification: fully_specified | platform: Gmail (computer)
- task: Set an out-of-office (vacation) reply (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/25922?hl=en

**USER:**
I'm going away next week. How do I set up an automatic out of office reply in Gmail on my computer?

**ASSISTANT:**
Here is how to turn on your vacation reply.

1. Open Gmail on your computer.
2. At the top right, click **Settings**, then **See all settings**.
3. On the **General** tab, scroll to the **Vacation responder** section.
4. Select **Vacation responder on**.
5. Fill in the date range, subject, and message.
6. At the bottom of the page, click **Save Changes**.

The reply starts at 12:00 AM on your first date and ends at 11:59 PM on your last date.

## tr203-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Gmail (computer)
- task: Set an out-of-office (vacation) reply (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/25922?hl=en

**USER:**
My knitting club emails me all the time and I'll be at my sister's for two weeks with no computer or internet. I'd like Gmail to tell people I'm away and when I'll be back. I'm on my laptop in a web browser right now. Please go slow, I'm not good at settings.

**ASSISTANT:**
Happy to. Go one step at a time.

1. In Gmail, at the top right, click **Settings**.
2. Click **See all settings**.
3. Stay on the **General** tab and scroll down to **Vacation responder**.
4. Select **Vacation responder on**.
5. Enter the first and last day of your trip, a subject, and a message saying when you will be back.
6. At the bottom of the page, click **Save Changes**.

Most people will get your reply only the first time they write to you.

## tr203-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Set an out-of-office (vacation) reply (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/25922?hl=en

**USER:**
set up an auto reply on my gmail while im on vacation

**ASSISTANT:**
I can help with that. Are you using Gmail on a **computer** or on a **phone**?

## tr203-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Gmail (computer)
- task: Set an out-of-office (vacation) reply (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/25922?hl=en

**USER:**
set up an auto reply on my gmail while im on vacation

**ASSISTANT:**
I can help with that. Are you using Gmail on a **computer** or on a **phone**?

**USER:**
computer

**ASSISTANT:**
Thanks. Here are the steps on a computer.

1. Open Gmail.
2. At the top right, click **Settings**, then **See all settings**.
3. Under the **General** tab, go to **Vacation responder**.
4. Select **Vacation responder on**.
5. Fill in the date range, subject, and message.
6. At the bottom, click **Save Changes**.

## tr203-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Gmail (computer)
- task: Set an out-of-office (vacation) reply (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/25922?hl=en

**USER:**
I want an out of office reply in Gmail on my computer, but I only want the people in my contacts to get it. I don't want strangers or random senders to know I'm away from home. Can it do that?

**ASSISTANT:**
Yes. There is a box for exactly that.

1. Click **Settings** at the top right, then **See all settings**.
2. On the **General** tab, go to **Vacation responder** and select **Vacation responder on**.
3. Fill in the date range, subject, and message.
4. Under the message, check the box to send the reply to your contacts only.
5. At the bottom, click **Save Changes**.

Emails in your spam folder do not get the reply either.

## tr203-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Gmail (computer)
- task: Set an out-of-office (vacation) reply (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/25922?hl=en

**USER:**
How do I turn on a vacation reply in Gmail on my computer?

**ASSISTANT:**
Here is how to turn it on.

1. At the top right, click **Settings**, then **See all settings**.
2. On the **General** tab, go to **Vacation responder**.
3. Select **Vacation responder on**.
4. Fill in the date range, subject, and message.
5. At the bottom, click **Save Changes**.

**USER:**
thanks it worked. but I came home early and it's still sending the reply. how do I stop it

**ASSISTANT:**
You can end it early.

1. Open your Gmail inbox.
2. Look at the banner across the top of the inbox.
3. Click **End now** on that banner.

## tr204-a
- scenario: direct | style: plain | specification: fully_specified | platform: Gmail (computer)
- task: Print an email (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/8255?co=GENIE.Platform%3DDesktop&hl=en

**USER:**
How can I print one email from my Gmail? I'm on a computer.

**ASSISTANT:**
Here is how to print one email.

1. Open Gmail on your computer.
2. Open the email you want to print.
3. At the top right of the email, click **More**. It looks like three dots.
4. Click **Print**.

## tr204-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Gmail (computer)
- task: Print an email (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/8255?co=GENIE.Platform%3DDesktop&hl=en

**USER:**
My daughter and I went back and forth about the flight times for my trip, like six emails in a row all stacked together in Gmail, and I'd like a paper copy of the whole conversation to take to the airport. I'm using Gmail on my desktop computer. How do I print everything together?

**ASSISTANT:**
You can print the whole conversation at once.

1. Open Gmail on your computer.
2. Open the conversation with your daughter.
3. At the top right, click **Print all**.

## tr204-b
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Print an email (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/8255?co=GENIE.Platform%3DDesktop&hl=en

**USER:**
print my email

**ASSISTANT:**
I can help with that. Are you using Gmail on a **computer** or on a **phone**?

## tr204-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Gmail (computer)
- task: Print an email (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/8255?co=GENIE.Platform%3DDesktop&hl=en

**USER:**
print my email

**ASSISTANT:**
I can help with that. Are you using Gmail on a **computer** or on a **phone**?

**USER:**
its a computer

**ASSISTANT:**
Thanks. Here is how to print an email on a computer.

1. Go to Gmail.
2. Open the email you want to print.
3. At the top right of the email, click **More**, the three dot icon.
4. Click **Print**.

## tr204-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Gmail (computer)
- task: Print an email (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/8255?co=GENIE.Platform%3DDesktop&hl=en

**USER:**
There's a long chain of replies in Gmail but I only need the one email from my landlord with the new address, I don't want the paper full of all the other replies. I'm on my computer. How do I print just that one?

**ASSISTANT:**
To print only that one email, use the single email option.

1. Open the email from your landlord.
2. At the top right of that email, click **More**, the three dot icon.
3. Click **Print**.

Do not use **Print all**, because that prints the whole conversation.

## tr204-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Gmail (computer)
- task: Print an email (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/8255?co=GENIE.Platform%3DDesktop&hl=en

**USER:**
Walk me through printing a message from my Gmail inbox. Computer, not phone.

**ASSISTANT:**
Here is how to print an email.

1. Open the email you want to print.
2. At the top right of the email, click **More**, the three dot icon.
3. Click **Print**.

**USER:**
that works for my other emails but the one from my bank won't print, not the message and not the attachment

**ASSISTANT:**
The sender may have sent it in confidential mode. That setting stops people from printing the message text and attachments.

So this email cannot be printed the normal way, even though your other emails can.

## tr205-a
- scenario: direct | style: plain | specification: fully_specified | platform: Google Contacts (computer)
- task: Add a contact (Google Contacts (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/contacts/answer/1069522?hl=en

**USER:**
How do I add a new person to my Google Contacts? I'm on a computer.

**ASSISTANT:**
Here is how to add a contact.

1. Go to contacts.google.com.
2. At the top left, click **Create contact**.
3. Choose **Create a contact**.
4. Type in the person's details, such as their name, email address, and phone number.
5. Click **Save**.

The contact is saved to your Google Account.

## tr205-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Google Contacts (computer)
- task: Add a contact (Google Contacts (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/contacts/answer/1069522?hl=en

**USER:**
I just met a lovely woman at my pottery class, Marjorie, and she gave me her email and her phone number on a napkin. I would like to put both of them into my Google Contacts so I don't lose them. I'm at my computer with the Contacts page open. What do I click?

**ASSISTANT:**
Here is what to click.

1. At the top left, click **Create contact**.
2. Choose **Create a contact**.
3. Type Marjorie's name, her email address, and her phone number.
4. Click **Save**.

## tr205-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Add a contact (Google Contacts (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/contacts/answer/1069522?hl=en

**USER:**
I want to save my neighbor's number in my google contacts

**ASSISTANT:**
I can help with that. Are you using a **computer** or a **phone**?

## tr205-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Google Contacts (computer)
- task: Add a contact (Google Contacts (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/contacts/answer/1069522?hl=en

**USER:**
I want to save my neighbor's number in my google contacts

**ASSISTANT:**
I can help with that. Are you using a **computer** or a **phone**?

**USER:**
computer

**ASSISTANT:**
Thanks. Here is how on a computer.

1. Go to contacts.google.com.
2. At the top left, click **Create contact**, then **Create a contact**.
3. Enter your neighbor's name and phone number.
4. Click **Save**.

## tr205-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Google Contacts (computer)
- task: Add a contact (Google Contacts (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/contacts/answer/1069522?hl=en

**USER:**
My new plumber only gave me his phone number, no email address. I'm on my computer and want to add him to Google Contacts. Is that okay, or do I have to have an email for him?

**ASSISTANT:**
You do not need an email address. Contacts can hold names, phone numbers, and more.

1. Go to contacts.google.com.
2. At the top left, click **Create contact**, then **Create a contact**.
3. Type his name and phone number.
4. Click **Save**.

## tr205-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Google Contacts (computer)
- task: Add a contact (Google Contacts (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/contacts/answer/1069522?hl=en

**USER:**
How do I add my friend Linda to Google Contacts on my computer?

**ASSISTANT:**
Here is how to add Linda.

1. Go to contacts.google.com.
2. At the top left, click **Create contact**, then **Create a contact**.
3. Type Linda's details.
4. Click **Save**.

**USER:**
wait, I have emailed Linda before but I never saved her anywhere, and I don't see her in my list of contacts. is she lost?

**ASSISTANT:**
She may not be lost. When you email someone you have not added, Google Contacts saves their address automatically under **Other contacts**.

1. Go to contacts.google.com.
2. On the left, click **Other contacts**.
3. Look for Linda there.
