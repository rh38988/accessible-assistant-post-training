# Review input: batch ny7a, round 2 (12 examples)

## tr199-a
- scenario: direct | style: plain | specification: fully_specified | platform: New Outlook for Windows
- task: Attach a file or photo to an email (New Outlook for Windows) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab ; https://support.microsoft.com/en-us/accessibility/outlook/basic-tasks-using-a-screen-reader-with-email-in-outlook?ad=us&rs=en-us&ui=en-us

**USER:**
I'm writing an email in the new Outlook app on my Windows computer and want to attach a Word file that is saved on my computer. How?

**ASSISTANT:**
Here is how to attach a file from your computer in the new Outlook app.

1. Start a new email, or open a reply or forward.
2. Select the **Insert** tab.
3. Select **Attach file**.
4. Select **Browse this computer**.
5. In the File Explorer window that opens, select the file you want.

## tr199-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: New Outlook for Windows
- task: Attach a file or photo to an email (New Outlook for Windows) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab ; https://support.microsoft.com/en-us/accessibility/outlook/basic-tasks-using-a-screen-reader-with-email-in-outlook?ad=us&rs=en-us&ui=en-us

**USER:**
ok so my granddaughter sent me her school pictures and I saved four of them on my Windows computer and now I'm in the new Outlook app writing to my sister and I'd like to put all four pictures on the email but I don't know how to get more than one on there. Can you help

**ASSISTANT:**
I could not find a way to pick several pictures at once, so add them one at a time.

1. Select the **Insert** tab.
2. Select **Attach file**, then **Browse this computer**.
3. In the File Explorer window, select the first picture.
4. Repeat steps 1 to 3 for each of the other three pictures.

## tr199-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: New Outlook for Windows
- task: Attach a file or photo to an email (New Outlook for Windows) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab ; https://support.microsoft.com/en-us/accessibility/outlook/basic-tasks-using-a-screen-reader-with-email-in-outlook?ad=us&rs=en-us&ui=en-us

**USER:**
how do i put a document on my outlook email

**ASSISTANT:**
I can help with that. Is the document saved on your computer, or is it in OneDrive?

**USER:**
it's on my computer, and I use the new Outlook app on Windows

**ASSISTANT:**
Thanks. Here is how to attach it.

1. Start a new email, or open a reply.
2. Select the **Insert** tab.
3. Select **Attach file**.
4. Select **Browse this computer**.
5. In the File Explorer window, select your document.

## tr199-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: New Outlook for Windows
- task: Attach a file or photo to an email (New Outlook for Windows) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab ; https://support.microsoft.com/en-us/accessibility/outlook/basic-tasks-using-a-screen-reader-with-email-in-outlook?ad=us&rs=en-us&ui=en-us

**USER:**
My tax papers are stored in OneDrive. I'm writing an email in the new Outlook app on my Windows computer. I don't want to download them to my computer first, I just want to send them from OneDrive. Is that possible?

**ASSISTANT:**
Yes. You can attach a OneDrive file as a link, so you do not need to download it first.

1. In your email, select the **Insert** tab.
2. Select **Attach file**.
3. Select **OneDrive**.
4. Select the file you want. A link to the file is added to your email.

If you see a warning that a person cannot view the linked file, select **Manage access** to resolve it.

## tr199-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: New Outlook for Windows
- task: Attach a file or photo to an email (New Outlook for Windows) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/office/8d7c1ea7-4e5f-44ce-bb6e-c5fcc92ba9ab ; https://support.microsoft.com/en-us/accessibility/outlook/basic-tasks-using-a-screen-reader-with-email-in-outlook?ad=us&rs=en-us&ui=en-us

**USER:**
How do I attach a picture from my computer to an email in the new Outlook app on Windows?

**ASSISTANT:**
Here is how to attach a picture from your computer.

1. Start a new email, or open a reply or forward.
2. Select the **Insert** tab.
3. Select **Attach file**.
4. Select **Browse this computer**.
5. In the File Explorer window, select the picture you want.

**USER:**
that worked but I have 3 more pictures to add and when I did it again it only let me pick one at a time

**ASSISTANT:**
The steps for attaching a file let you pick one file at a time, so repeat these steps for each picture.

1. Select the **Insert** tab.
2. Select **Attach file**, then **Browse this computer**.
3. In the File Explorer window, select the picture.

## tr200-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Outlook.com
- task: Email is not arriving or syncing (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642 ; https://support.microsoft.com/office/storage-limits-in-outlook-com-7ac99134-69e5-4619-ac0b-2d313bba5e9e

**USER:**
Hello, for about a week now no new mail has come into my Outlook.com account, not from my church group, not from my pharmacy, nothing, and this morning I saw a message at the top saying my Microsoft storage is full. My neighbor said that might be the reason. Is it?

**ASSISTANT:**
Yes, that can be the reason. When your Microsoft cloud storage is full, you cannot send or receive email.

1. Select **Settings**, then **Account**, then **Storage** to see how much space each folder uses.
2. Free up some space. On that page you can permanently delete all items in a folder, or only the items older than 3, 6, or 12 months.
3. Check your inbox again for new mail.

Messages people sent while your storage was full were returned to them, so they may need to send those messages again.

## tr200-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Outlook.com
- task: Email is not arriving or syncing (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642 ; https://support.microsoft.com/en-us/office/turn-on-or-off-automatic-forwarding-in-outlook-com-6246987c-6c8f-4144-b255-14fc07007dad ; https://support.microsoft.com/office/storage-limits-in-outlook-com-7ac99134-69e5-4619-ac0b-2d313bba5e9e

**USER:**
my emails stopped coming in

**ASSISTANT:**
I can help with that. Which email do you use: **Outlook.com**, **Gmail**, or something else?

**USER:**
outlook.com

**ASSISTANT:**
Thanks. Try these checks for Outlook.com.

1. Check the **Other** tab, and make sure no filters are keeping you from seeing all your messages.
2. Open the **Junk Email** folder. If good mail is there, right-click it and select **Mark as not junk**.
3. Select the **Settings** icon, then **Mail**, then **Forwarding**. Forwarding is on when **Enable forwarding** is checked. If it is checked, clear it and select **Save**.
4. Select **Settings**, then **Account**, then **Storage** to see how much space each folder uses. If your Microsoft cloud storage is full, free up some space, because a full mailbox cannot receive email.

If a message from one person is still missing, ask that person to review Sender Support in Outlook.com.

## tr200-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Outlook.com
- task: Email is not arriving or syncing (Outlook.com) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642

**USER:**
My Outlook.com isn't showing an email from my doctor's office. I'm nervous about breaking something, so I don't want to change any settings or rules. Is there anything I can just look at?

**ASSISTANT:**
Yes, you can find it just by looking.

1. Click the **Other** tab and look through it for the message.
2. Open the **Junk Email** folder and look for the message.
3. If you find it in Junk Email, right-click it and select **Mark as not junk**. This moves it back to your inbox.

If you notice a filter has been applied on the Other tab, tell me before you change anything.

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
2. On the left, next to **Labels**, click **Create new label**.
3. Type **Taxes** as the name.
4. Click **Create**.

Your new label is ready to use.

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

1. At the top right, click **Settings**, then **See all settings**.
2. Click the **Labels** tab at the top.
3. Find **Bills** and click **Show** next to it.

## tr205-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Google Contacts (computer)
- task: Add a contact (Google Contacts (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/contacts/answer/1069522?hl=en

**USER:**
My new plumber only gave me his phone number, no email address. I'm on my computer and want to add him to Google Contacts. Is that okay, or do I have to have an email for him?

**ASSISTANT:**
Google Contacts can save names, email addresses, phone numbers, and more. The help page I checked does not say whether an email address is required. The steps below save his name and phone number.

1. Go to contacts.google.com.
2. At the top left, click **Create contact**, then **Create a contact**.
3. Type his name and phone number.
4. Click **Save**.
