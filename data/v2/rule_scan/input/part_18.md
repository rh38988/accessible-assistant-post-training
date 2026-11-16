# Rule scan input, part 18 (50 examples)

## tr198-r
- task: Get directions on a computer | platform: Google Maps (computer) | scenario: failure_recovery | sensitive: False
- sources: Google Maps Help: Get directions and show routes <https://support.google.com/maps/answer/144339>

**USER:**
I'd like bus directions to the farmers market on Google Maps on my computer.

**ASSISTANT:**
Here is how to get bus directions:

1. Open Google Maps in your browser, then click **Directions**.
2. Enter your starting point and the farmers market as the destination.
3. Choose **Transit**.

**USER:**
I don't see any bus or transit option for my town.

**ASSISTANT:**
Transit only shows where your city's transit agency has added its route information to Google Maps. Your agency may not have added it yet. You can still choose **Driving** or **Walking** from the same screen to get directions.

---

## tr200-a
- task: Email is not arriving or syncing | platform: Outlook.com | scenario: direct | sensitive: False
- sources: Microsoft Support: Can't send or receive email in Outlook.com <https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642>

**USER:**
My son says he sent me an email last night but I never got it in my Outlook.com inbox. Where could it be?

**ASSISTANT:**
It may have landed in a place other than your inbox. Try these.

1. Look at the **Other** tab, in case a filter hid it. Make sure you can see all messages.
2. Open your **Junk Email** folder.
3. If you find his message there, right-click it and select **Mark as not junk**. This moves it to your Inbox.

If it is in neither place, check whether email forwarding is turned on, and whether you have any email rules that could redirect it.

---

## tr200-b
- task: Email is not arriving or syncing | platform: Outlook.com | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Can't send or receive email in Outlook.com <https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642>

**USER:**
my emails stopped coming in

**ASSISTANT:**
I can help with that. Which email do you use: **Outlook.com**, **Gmail**, or something else?

---

## tr200-r
- task: Email is not arriving or syncing | platform: Outlook.com | scenario: failure_recovery | sensitive: False
- sources: Microsoft Support: Can't send or receive email in Outlook.com <https://support.microsoft.com/en-us/office/can-t-send-or-receive-email-in-outlook-com-d39e3341-8d79-4bf1-b3c7-ded602233642>

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

---

## tr201-a
- task: Recover a deleted email | platform: Outlook.com | scenario: direct | sensitive: False
- sources: Microsoft Support: Email is missing from your Outlook.com inbox <https://support.microsoft.com/office/c70b4a9a-caa5-4e8c-a88a-3372215af25e>

**USER:**
I deleted an email in Outlook.com by mistake this morning and I need it back. I'm on my computer.

**ASSISTANT:**
Let's look in your Deleted Items folder first.

1. Open the **Deleted Items** folder.
2. Select the message you want back.
3. Select **Restore**.

If it is not in **Deleted Items**, look above the message list for **Recover items deleted from this folder** and select it. Find your message, select it, then select **Restore**.

---

## tr201-b
- task: Recover a deleted email | platform: Outlook.com | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Email is missing from your Outlook.com inbox <https://support.microsoft.com/office/c70b4a9a-caa5-4e8c-a88a-3372215af25e>

**USER:**
i deleted an email i need to get it back

**ASSISTANT:**
I can help with that. Are you using Outlook.com on a **computer** or on a **phone**?

---

## tr201-c
- task: Recover a deleted email | platform: Outlook.com | scenario: direct_messy | sensitive: False
- sources: Microsoft Support: Email is missing from your Outlook.com inbox <https://support.microsoft.com/office/c70b4a9a-caa5-4e8c-a88a-3372215af25e>

**USER:**
I cleaned out my Outlook.com a couple of weeks ago, I even emptied the Deleted Items folder like a tidy person, and now I realize I threw away the confirmation for my husband's surgery date. I am on my laptop. Is it gone forever?

**ASSISTANT:**
It may not be gone. Removed items can be recovered for 30 days.

1. Open the **Deleted Items** folder.
2. Above the message list, select **Recover items deleted from this folder**.
3. Find your message and select it.
4. Select **Restore**.

You must use a computer for this, and you are on your laptop, so that is fine.

---

## tr201-d
- task: Recover a deleted email | platform: Outlook.com | scenario: followup | sensitive: False
- sources: Microsoft Support: Email is missing from your Outlook.com inbox <https://support.microsoft.com/office/c70b4a9a-caa5-4e8c-a88a-3372215af25e>

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

---

## tr201-e
- task: Recover a deleted email | platform: Outlook.com | scenario: constraint | sensitive: False
- sources: Microsoft Support: Email is missing from your Outlook.com inbox <https://support.microsoft.com/office/c70b4a9a-caa5-4e8c-a88a-3372215af25e>

**USER:**
I'm away from home and all I have is my phone, no computer. I deleted an important email in the Outlook.com app. Can I get it back from here?

**ASSISTANT:**
Yes, if it is still in your Deleted Items folder.

1. Open the **Deleted Items** folder.
2. Select the message.
3. Choose the **More options** icon.
4. Select **Move to folder**, then **Inbox**.

If it is not in **Deleted Items**, the next recovery option, **Recover items deleted from this folder**, cannot be done on the phone app or a phone browser. You will need a computer for that.

---

## tr202-a
- task: Organize email with labels | platform: Gmail (computer) | scenario: direct | sensitive: False
- sources: Gmail Help: Create & manage labels in Gmail <https://support.google.com/mail/answer/118708?hl=en>

**USER:**
I'd like to make a label called Taxes in Gmail so my tax emails are all together. I'm on my computer.

**ASSISTANT:**
Here is how to make a label called Taxes.

1. Open Gmail on your computer.
2. On the left, next to **Labels**, click **Create new label**.
3. Type **Taxes** as the name.
4. Click **Create**.

Your new label is ready to use.

---

## tr202-b
- task: Organize email with labels | platform: Gmail (computer) | scenario: missing_info | sensitive: False
- sources: Gmail Help: Create & manage labels in Gmail <https://support.google.com/mail/answer/118708?hl=en>

**USER:**
my gmail is such a mess, how do I organize it with labels

**ASSISTANT:**
I can help with that. Are you using Gmail on a **computer** or on a **phone**?

---

## tr202-c
- task: Organize email with labels | platform: Gmail (computer) | scenario: direct_messy | sensitive: False
- sources: Gmail Help: Create & manage labels in Gmail <https://support.google.com/mail/answer/118708?hl=en>

**USER:**
I already have a Gmail label called Family on my computer, but now my emails from the grandkids are mixed in with everything else. I'd like a new label named Grandkids that sits inside the Family one, kind of like a folder in a folder. Is that something I can do?

**ASSISTANT:**
Yes, you can place one label inside another.

1. On the left, next to **Labels**, click **Create new label**.
2. Type **Grandkids** as the name.
3. Check **Nest label under**.
4. Choose **Family** as the parent.
5. Click **Create**.

---

## tr202-d
- task: Organize email with labels | platform: Gmail (computer) | scenario: followup | sensitive: False
- sources: Gmail Help: Create & manage labels in Gmail <https://support.google.com/mail/answer/118708?hl=en>

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

---

## tr202-e
- task: Organize email with labels | platform: Gmail (computer) | scenario: constraint | sensitive: False
- sources: Gmail Help: Create & manage labels in Gmail <https://support.google.com/mail/answer/118708?hl=en>

**USER:**
On Gmail on my computer I put a bunch of emails under the label Misc, but they really belong under my label Recipes. I don't want them in both places, I want them moved from Misc to Recipes. How?

**ASSISTANT:**
You can move them from one label to the other.

1. Check the box next to each email you want to move.
2. At the top, click **Labels**.
3. Uncheck **Misc**.
4. Select **Recipes**.

---

## tr202-r
- task: Organize email with labels | platform: Gmail (computer) | scenario: failure_recovery | sensitive: False
- sources: Gmail Help: Create & manage labels in Gmail <https://support.google.com/mail/answer/118708?hl=en>

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

---

## tr203-a
- task: Set an out-of-office (vacation) reply | platform: Gmail (computer) | scenario: direct | sensitive: False
- sources: Gmail Help: Send automatic replies from Gmail <https://support.google.com/mail/answer/25922?hl=en>

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

---

## tr203-b
- task: Set an out-of-office (vacation) reply | platform: Gmail (computer) | scenario: missing_info | sensitive: False
- sources: Gmail Help: Send automatic replies from Gmail <https://support.google.com/mail/answer/25922?hl=en>

**USER:**
set up an auto reply on my gmail while im on vacation

**ASSISTANT:**
I can help with that. Are you using Gmail on a **computer** or on a **phone**?

---

## tr203-c
- task: Set an out-of-office (vacation) reply | platform: Gmail (computer) | scenario: direct_messy | sensitive: False
- sources: Gmail Help: Send automatic replies from Gmail <https://support.google.com/mail/answer/25922?hl=en>

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

---

## tr203-d
- task: Set an out-of-office (vacation) reply | platform: Gmail (computer) | scenario: followup | sensitive: False
- sources: Gmail Help: Send automatic replies from Gmail <https://support.google.com/mail/answer/25922?hl=en>

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

---

## tr203-e
- task: Set an out-of-office (vacation) reply | platform: Gmail (computer) | scenario: constraint | sensitive: False
- sources: Gmail Help: Send automatic replies from Gmail <https://support.google.com/mail/answer/25922?hl=en>

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

---

## tr203-r
- task: Set an out-of-office (vacation) reply | platform: Gmail (computer) | scenario: failure_recovery | sensitive: False
- sources: Gmail Help: Send automatic replies from Gmail <https://support.google.com/mail/answer/25922?hl=en>

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

---

## tr204-a
- task: Print an email | platform: Gmail (computer) | scenario: direct | sensitive: False
- sources: Gmail Help: Print Gmail messages <https://support.google.com/mail/answer/8255?co=GENIE.Platform%3DDesktop&hl=en>

**USER:**
How can I print one email from my Gmail? I'm on a computer.

**ASSISTANT:**
Here is how to print one email.

1. Open Gmail on your computer.
2. Open the email you want to print.
3. At the top right of the email, click **More**. It looks like three dots.
4. Click **Print**.

---

## tr204-b
- task: Print an email | platform: Gmail (computer) | scenario: missing_info | sensitive: False
- sources: Gmail Help: Print Gmail messages <https://support.google.com/mail/answer/8255?co=GENIE.Platform%3DDesktop&hl=en>

**USER:**
print my email

**ASSISTANT:**
I can help with that. Are you using Gmail on a **computer** or on a **phone**?

---

## tr204-c
- task: Print an email | platform: Gmail (computer) | scenario: direct_messy | sensitive: False
- sources: Gmail Help: Print Gmail messages <https://support.google.com/mail/answer/8255?co=GENIE.Platform%3DDesktop&hl=en>

**USER:**
My daughter and I went back and forth about the flight times for my trip, like six emails in a row all stacked together in Gmail, and I'd like a paper copy of the whole conversation to take to the airport. I'm using Gmail on my desktop computer. How do I print everything together?

**ASSISTANT:**
You can print the whole conversation at once.

1. Open Gmail on your computer.
2. Open the conversation with your daughter.
3. At the top right, click **Print all**.

---

## tr204-d
- task: Print an email | platform: Gmail (computer) | scenario: followup | sensitive: False
- sources: Gmail Help: Print Gmail messages <https://support.google.com/mail/answer/8255?co=GENIE.Platform%3DDesktop&hl=en>

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

---

## tr204-e
- task: Print an email | platform: Gmail (computer) | scenario: constraint | sensitive: False
- sources: Gmail Help: Print Gmail messages <https://support.google.com/mail/answer/8255?co=GENIE.Platform%3DDesktop&hl=en>

**USER:**
There's a long chain of replies in Gmail but I only need the one email from my landlord with the new address, I don't want the paper full of all the other replies. I'm on my computer. How do I print just that one?

**ASSISTANT:**
To print only that one email, use the single email option.

1. Open the email from your landlord.
2. At the top right of that email, click **More**, the three dot icon.
3. Click **Print**.

Do not use **Print all**, because that prints the whole conversation.

---

## tr204-r
- task: Print an email | platform: Gmail (computer) | scenario: failure_recovery | sensitive: False
- sources: Gmail Help: Print Gmail messages <https://support.google.com/mail/answer/8255?co=GENIE.Platform%3DDesktop&hl=en>

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

---

## tr205-a
- task: Add a contact | platform: Google Contacts (computer) | scenario: direct | sensitive: False
- sources: Google Contacts Help: Add or move contacts <https://support.google.com/contacts/answer/1069522?hl=en>

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

---

## tr205-b
- task: Add a contact | platform: Google Contacts (computer) | scenario: missing_info | sensitive: False
- sources: Google Contacts Help: Add or move contacts <https://support.google.com/contacts/answer/1069522?hl=en>

**USER:**
I want to save my neighbor's number in my google contacts

**ASSISTANT:**
I can help with that. Are you using a **computer** or a **phone**?

---

## tr205-c
- task: Add a contact | platform: Google Contacts (computer) | scenario: direct_messy | sensitive: False
- sources: Google Contacts Help: Add or move contacts <https://support.google.com/contacts/answer/1069522?hl=en>

**USER:**
I just met a lovely woman at my pottery class, Marjorie, and she gave me her email and her phone number on a napkin. I would like to put both of them into my Google Contacts so I don't lose them. I'm at my computer with the Contacts page open. What do I click?

**ASSISTANT:**
Here is what to click.

1. At the top left, click **Create contact**.
2. Choose **Create a contact**.
3. Type Marjorie's name, her email address, and her phone number.
4. Click **Save**.

---

## tr205-d
- task: Add a contact | platform: Google Contacts (computer) | scenario: followup | sensitive: False
- sources: Google Contacts Help: Add or move contacts <https://support.google.com/contacts/answer/1069522?hl=en>

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

---

## tr206-a
- task: Turn on captions in a meeting | platform: Zoom | scenario: direct | sensitive: False
- sources: Zoom Support: Viewing captions in a meeting or webinar <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762>

**USER:**
I'm in a Zoom meeting on my laptop and I'd like to see captions of what people are saying. How do I turn them on?

**ASSISTANT:**
Here is how to show captions in the Zoom app on your computer.

1. In the bar of buttons at the bottom of the meeting, click the **Show captions** icon.
2. If you do not see it, click **More** in that bar, then click **Show captions**.

The words people say will appear above the meeting buttons, with each speaker's name in front.

If you cannot turn captions on, the host may have restricted them. Click **More**, then **Request captions**, then click **Send**. The host or a co-host has to approve your request before captions appear.

---

## tr206-b
- task: Turn on captions in a meeting | platform: Zoom | scenario: missing_info | sensitive: False
- sources: Zoom Support: Viewing captions in a meeting or webinar <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762>

**USER:**
I can't hear everyone well in my Zoom call. Can I get the words to show up?

**ASSISTANT:**
Yes, Zoom can show captions. Are you using Zoom on a **computer** or on a **phone**?

---

## tr206-c
- task: Turn on captions in a meeting | platform: Zoom | scenario: direct_messy | sensitive: False
- sources: Zoom Support: Viewing captions in a meeting or webinar <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762>

**USER:**
My granddaughter set up Zoom on my Android phone so I can join my church group. I'm hard of hearing and some people talk quietly, so I'm hoping to read what they say on the screen. I'm already in the meeting right now. Where do I find the captions?

**ASSISTANT:**
You can show captions in the Zoom app on your phone like this.

1. Tap **More** in the buttons along the bottom of the meeting screen.
2. Tap **Show CC**.

The words people say will appear above the meeting buttons.

If you do not see **Show CC**, the host may have limited captions. Tap **More**, then **Request captions**, then **Send**. The host or a co-host has to approve your request.

---

## tr206-d
- task: Turn on captions in a meeting | platform: Zoom | scenario: followup | sensitive: False
- sources: Zoom Support: Viewing captions in a meeting or webinar <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762>

**USER:**
I can't hear everyone well in my Zoom call. Can I get the words to show up?

**ASSISTANT:**
Yes, Zoom can show captions. Are you using Zoom on a **computer** or on a **phone**?

**USER:**
a phone

**ASSISTANT:**
Here is how to show captions in Zoom on your phone.

1. Tap **More** in the buttons along the bottom of the meeting screen.
2. Tap **Show CC**.

The words people say will appear above the meeting buttons.

If you do not see **Show CC**, tap **More**, then **Request captions**, then **Send**. The host has to approve it.

---

## tr206-e
- task: Turn on captions in a meeting | platform: Zoom | scenario: constraint | sensitive: False
- sources: Zoom Support: Viewing captions in a meeting or webinar <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762>

**USER:**
I'm on Zoom on my Windows computer. I want captions, but the letters are tiny and my eyes are bad. I only want to make the letters bigger for me, not change anything for the other people in the meeting. Can that be done?

**ASSISTANT:**
Yes. These changes only affect your own screen.

1. Click the **Show captions** icon in the buttons at the bottom of the meeting. If you do not see it, click **More**, then **Show captions**.
2. Move your mouse over the captions and click the gear icon.
3. Click **Caption settings**. A panel called **Accessibility** opens on the right.
4. Drag the **Font size** slider to make the letters bigger.

If nothing happens when you click **Show captions**, the host may have restricted them. Click **More**, then **Request captions**, then **Send**. The host or a co-host has to approve your request.

---

## tr206-r
- task: Turn on captions in a meeting | platform: Zoom | scenario: failure_recovery | sensitive: False
- sources: Zoom Support: Viewing captions in a meeting or webinar <https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762>

**USER:**
How do I turn on captions in Zoom on my Mac? I'm in a meeting now.

**ASSISTANT:**
Here is how to show captions in Zoom on your Mac.

1. Click the **Show captions** icon in the buttons at the bottom of the meeting.
2. If you do not see it, click **More**, then **Show captions**.

The words people say will appear above the meeting buttons.

**USER:**
I clicked on it but no captions came up.

**ASSISTANT:**
The host may have limited captions. You can ask for them.

1. Click **More** in the bottom buttons.
2. Click **Request captions**.
3. Click **Send**.

The host or a co-host has to approve your request before captions appear.

If you do not see **Request captions** under **More**, the host may have turned captions off, so ask the host to turn them on.

---

## tr212-c
- task: Someone sends a check and asks the user to send part of the money back | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC Consumer Advice: Fake check scams <https://consumer.ftc.gov/fakechecks>

**USER:**
I got an email saying I was picked to be a mystery shopper for a money transfer store. They mailed me a big check and told me to deposit it, keep a little for myself, and wire the rest to a man they named. I went to the bank and the teller said the money is already showing in my account. I really need the extra money right now. Should I wire it?

**ASSISTANT:**
No, please do not wire any of it. Wiring money from a check to someone who asks is a classic fake check scam.

1. Never use money from a check to wire money to anyone who asks.
2. Do not rely on money from a check unless you know and trust the person who sent it.
3. Report it to the Federal Trade Commission at reportfraud.ftc.gov.

Banks must make deposited funds available quickly, so seeing the money in your account does not mean the check is good. If it turns out to be fake, you may have to repay the bank.

---

## tr212-e
- task: Someone sends a check and asks the user to send part of the money back | platform: any | scenario: constraint | sensitive: True
- sources: FTC Consumer Advice: Fake check scams <https://consumer.ftc.gov/fakechecks>

**USER:**
The check I deposited cleared and the bank website shows the full amount as available, so it must be real. The sender keeps texting that I need to send back the extra today, and that I shouldn't bother anyone at the bank about it. Can I just send it?

**ASSISTANT:**
No, please do not send it. Money showing as available does not make the check good.

1. Banks must make deposited funds available quickly by law, even when the check is fake.
2. It can take weeks for a bank to find the fraud, and then you may have to repay the bank.
3. Do not send any of the money back, no matter how urgent the texts sound.
4. Report it to the Federal Trade Commission at reportfraud.ftc.gov.

Even if you see the funds in your account, that does not mean the check is good.

---

## tr212-f
- task: Someone sends a check and asks the user to send part of the money back | platform: any | scenario: helper | sensitive: True
- sources: FTC Consumer Advice: Fake check scams <https://consumer.ftc.gov/fakechecks>

**USER:**
My grandfather got a check in the mail from a company that wants to put an ad wrap on his car. They told him to deposit it and then pay the installers out of it. He is excited. What should I tell him?

**ASSISTANT:**
Tell him not to pay anyone from that check. This is a known fake check scam called car wrap decals.

1. Ask him not to deposit and spend money, or send any to the installers.
2. Explain that fake checks often look real, even to bank workers.
3. Remind him that a bank can find the fraud weeks later, and then he may have to repay it.
4. Help him report it to the Federal Trade Commission at reportfraud.ftc.gov.

If he already sent money, tell me how and I can help with the next step.

---

## tr212-g
- task: Someone sends a check and asks the user to send part of the money back | platform: any | scenario: prevention | sensitive: True
- sources: FTC Consumer Advice: Fake check scams <https://consumer.ftc.gov/fakechecks>

**USER:**
How can I spot a fake check scam before I fall for one, and where do I report it?

**ASSISTANT:**
Here are the warning signs and the rules to follow.

1. Be wary if you are asked to wire money, buy gift cards, or buy cryptocurrency. Gift cards are for gifts, not payments.
2. Be wary if a check is for more than the selling price, or you are asked to pay fees to get a prize.
3. Never use money from a check to buy gift cards or money orders, buy cryptocurrency, or wire money.
4. Do not rely on money from a check unless you know and trust the person.

To report one, go to the Federal Trade Commission at reportfraud.ftc.gov, the U.S. Postal Inspection Service at uspis.gov/report, or your state Attorney General.

---

## tr212-r
- task: Someone sends a check and asks the user to send part of the money back | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Advice: Fake check scams <https://consumer.ftc.gov/fakechecks>

**USER:**
A man mailed me a check and said to deposit it and buy gift cards with the money for his company. I already bought the cards and sent him the numbers on the back. Now my bank says the check was fake. What do I do?

**ASSISTANT:**
I am sorry, this happens to many people. Act quickly on the gift cards.

1. Contact the company that issued each gift card right away.
2. Tell them the card was used in a scam and ask for a refund.
3. Tell the store where you bought the cards.
4. Report it to the Federal Trade Commission at reportfraud.ftc.gov.

Because the check was fake, you may have to repay the bank.

---

## tr213-a
- task: A contractor at the door pushes for a quick repair deal and upfront payment | platform: any | scenario: direct | sensitive: True
- sources: FTC Consumer Advice: How to avoid a home improvement scam <https://consumer.ftc.gov/how-avoid-home-improvement-scam>

**USER:**
A man knocked on my door and said he was in the area and noticed my roof needs work. He wants to start today and says the price is good only right now. Should I say yes?

**ASSISTANT:**
Please do not agree today. Being "in the area" and pushing you to decide right now are both signs of a home improvement scam.

1. Tell him you will think about it, and do not pay anything.
2. Hire only a licensed and insured contractor. Confirm the license with your state or county, and ask for proof of insurance.
3. Ask people you know and trust for recommendations.
4. Get more than one written estimate before you choose.

A real contractor can wait for you to check.

---

## tr213-c
- task: A contractor at the door pushes for a quick repair deal and upfront payment | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC Consumer Advice: How to avoid a home improvement scam <https://consumer.ftc.gov/how-avoid-home-improvement-scam>

**USER:**
Two men came by saying they had leftover paving materials from a job down the street and could do my driveway cheap. They want all the money up front, in cash, and they said I should go get the building permit from the city myself. My husband is at work so I can't ask him. It sounds like a good deal but something feels off.

**ASSISTANT:**
Your feeling is right. Please do not pay them anything today.

1. Do not pay the full cost up front. Never make the final payment until the work is finished and you are satisfied.
2. Be careful of anyone who accepts only cash, or who asks you to get the building permits yourself.
3. Leftover materials from a previous job is another sign of this scam.
4. Wait and talk it over with your husband. A real contractor will give you a written estimate you can compare with others.

If they keep pressuring you, that is another warning sign.

---

## tr213-e
- task: A contractor at the door pushes for a quick repair deal and upfront payment | platform: any | scenario: constraint | sensitive: True
- sources: FTC Consumer Advice: How to avoid a home improvement scam <https://consumer.ftc.gov/how-avoid-home-improvement-scam>

**USER:**
The contractor at my door says the repair price is only good if I sign today, and he offered to set me up with a lender he knows so I don't have to pay now. I don't have the savings. He's standing on my porch waiting. What do I do?

**ASSISTANT:**
Do not sign anything today. Pushing for an immediate decision and offering a lender he knows are both signs of a scam.

1. Tell him you will not sign today, and close the door.
2. Do not sign anything you have not read, do not understand, or that has blank spaces.
3. If you need a loan, shop around and compare loan terms before accepting financing from a contractor.
4. Make sure you can afford the payments.
5. Do not let anyone pressure you into signing.

Never transfer your deed to anyone without first talking to an attorney or someone you trust.

---

## tr213-f
- task: A contractor at the door pushes for a quick repair deal and upfront payment | platform: any | scenario: helper | sensitive: True
- sources: FTC Consumer Advice: How to avoid a home improvement scam <https://consumer.ftc.gov/how-avoid-home-improvement-scam>

**USER:**
My elderly neighbor says a contractor keeps coming to her door pushing to fix her gutters, and wants half the money first. I want to help her without scaring her. What should I tell her?

**ASSISTANT:**
Here is what to share with her, kindly and simply.

1. She does not have to decide right away. Pressure for an immediate decision is a sign of a scam.
2. Do not pay the full cost up front, and never make the final payment until the work is finished and she is satisfied. Some states limit how much a contractor can ask for as a down payment, so check the rules with your state or local consumer agency before she pays any deposit.
3. Use only a licensed and insured contractor. Help her confirm the license with the state or county, and ask for proof of insurance.
4. Get recommendations from people she knows and trusts, and more than one written estimate.

If something goes wrong, her state attorney general or local consumer protection office can help.

---

## tr213-g
- task: A contractor at the door pushes for a quick repair deal and upfront payment | platform: any | scenario: prevention | sensitive: True
- sources: FTC Consumer Advice: How to avoid a home improvement scam <https://consumer.ftc.gov/how-avoid-home-improvement-scam>

**USER:**
How do I make sure a contractor is honest before I hire anyone to work on my house?

**ASSISTANT:**
Take these steps before you agree to anything.

1. Use only licensed and insured contractors. Confirm the license with your state or county and ask for proof of insurance.
2. Ask people you know and trust for recommendations.
3. Check with your local Home Builders Association and consumer protection officials for complaints. Search the company name with "scam," "review," or "complaint."
4. Get several written estimates. Do not automatically pick the lowest one.
5. Read the contract carefully. It should show the contractor's name, address, phone, license number, start and finish dates, and a written statement of your right to cancel. Write in any spoken promises and fill in all blank spaces.

Do not pay everything up front.

---

## tr214-a
- task: A caller demands payment for a debt the user does not recognize | platform: any | scenario: direct | sensitive: True
- sources: FTC Consumer Advice: Debt collection FAQs <https://www.consumer.ftc.gov/articles/debt-collection-faqs>

**USER:**
Someone called and said I owe money on an old account and have to pay today. I have never heard of this debt. What should I do?

**ASSISTANT:**
Do not pay and do not share any personal or financial information on that call. First get proof that the debt is real.

1. Ask the caller to send you a written validation notice. The collector must provide it when it first contacts you or within five days after.
2. When it arrives, check the collector's name and address, the original creditor, and the amount owed.
3. If you do not owe it, send a dispute letter within 30 days. Say you do not owe the money and ask for verification of the debt.
4. Send the letter by certified mail with a return receipt, and keep a copy.

Once the collector gets your dispute, it must stop trying to collect until it sends written verification.

---

## tr214-c
- task: A caller demands payment for a debt the user does not recognize | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC Consumer Advice: Debt collection FAQs <https://www.consumer.ftc.gov/articles/debt-collection-faqs>

**USER:**
A man keeps calling me at 7 in the morning and again at night, six times this week, about some credit card I don't have. He says if I don't pay he will have me arrested. I'm scared. I don't know whose debt this is and I don't want to just pay to make it stop. What are my rights?

**ASSISTANT:**
A collector is not allowed to treat you this way, and you can dispute a debt you do not recognize.

1. Collectors cannot threaten arrest or legal action they will not take, and cannot call before 8 a.m. or after 9 p.m. unless you agree.
2. They also cannot harass you or call more than seven times in seven days.
3. Do not share personal or financial information until you get validation information in writing.
4. Send a letter within 30 days of getting it saying you do not owe the money, by certified mail with a return receipt.
5. If you want the calls to stop, mail the collector a letter asking it to stop contacting you. Keep a copy and send it by certified mail with a return receipt.
6. Report the calls to the FTC at reportfraud.ftc.gov or the CFPB at cfpb.gov/complaint.

---

## tr214-e
- task: A caller demands payment for a debt the user does not recognize | platform: any | scenario: constraint | sensitive: True
- sources: FTC Consumer Advice: Debt collection FAQs <https://www.consumer.ftc.gov/articles/debt-collection-faqs>

**USER:**
A caller says they are suing me today unless I give my debit card number right now to settle a debt. I don't recognize it and I can't reach anyone I trust to ask. He says it's my last chance. Should I give the number?

**ASSISTANT:**
No. Do not give your card number or any other information, and end the call.

1. Collectors cannot threaten legal action they will not take, or lie about the amount you owe.
2. Do not share personal or financial information until you have validation information in writing.
3. Ask for the written validation notice, which must arrive when they first contact you or within five days after.
4. Within 30 days of getting it, send a letter by certified mail with a return receipt. Say you do not owe the money and ask for verification of the debt.

Keep a copy of everything.

---
