# Review input: batch ex3, round 3 (18 examples)

## tr033-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Install a software update (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7680439?hl=en

**USER:**
How do I update the software on my Android phone?

**ASSISTANT:**
Here's how to check for an update. Before you start, connect to Wi-Fi and make sure your battery is at least 75% charged, because updates can take a while.

1. Open the **Settings** app.
2. Tap **System**.
3. Tap **Software updates**. The update status appears there. Names can be a little different on some phones.
4. Follow the instructions on the screen to download and install the update.

Your phone may restart during the update. On Google Pixel phones, the update installs in the background and finishes when you restart.

If you get a 'not enough space available' notification, tell me and I'll help you free up some storage first.

## tr033-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Install a software update (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7680439?hl=en

**USER:**
my phone says there's an update, should I do it?

**ASSISTANT:**
Updates are usually a good idea because they fix problems and help keep your phone secure. So I can show you the right steps: is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

**USER:**
Android

**ASSISTANT:**
Thanks. If you still see the update notification, you can tap it, then tap its update button. Otherwise, before you start, connect to Wi-Fi and charge the battery to at least 75%, because updates can take a while.

1. Open the **Settings** app.
2. Tap **System**.
3. Tap **Software updates**. The update status appears there. Names can be a little different on some phones.
4. Follow the instructions on the screen to download and install the update.

Your phone may restart during the update. On Google Pixel phones, the update installs in the background and finishes when you restart.

If you get a 'not enough space available' notification, tell me and I'll help you free up some storage first.

## tr035-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android (Google Photos)
- task: Back up photos (Android (Google Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
How do I back up my photos on my Android phone so I don't lose them?

**ASSISTANT:**
You can use the **Google Photos** app to save copies of your photos to your Google Account. Make sure you have a good internet connection first.

1. Open the **Google Photos** app.
2. Sign in to your Google Account if it asks.
3. Tap your **profile picture or initial** at the top right.
4. Tap **Photos settings**.
5. Tap **Backup**.
6. Turn **Backup** on.

Your photos will start saving to your Google Account. At the top of your library you should see the backup status, such as **Backing up photos** and later **Backup complete**. This can take a while if you have many photos.

Your Google storage is shared with Gmail and Google Drive, and backup stops if it fills up. Tell me if you see a storage message and we'll look at the options.

## tr035-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android (Google Photos)
- task: Back up photos (Android (Google Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I dropped my old phone in the lake last summer and lost all the pictures of my granddaughter's first year. I have a new Android phone now and I don't want that to happen again.

**ASSISTANT:**
I'm sorry about those pictures. Let's make sure your new ones are kept safe. You can use the **Google Photos** app to save copies of your photos to your Google Account. Make sure you have a good internet connection first.

1. Open the **Google Photos** app.
2. Sign in to your Google Account if it asks.
3. Tap your **profile picture or initial** at the top right.
4. Tap **Photos settings**.
5. Tap **Backup**.
6. Turn **Backup** on.

Your photos will start saving to your Google Account. At the top of your library you should see the backup status, such as **Backing up photos** and later **Backup complete**. This can take a while if you have many photos.

Your Google storage is shared with Gmail and Google Drive, and backup stops if it fills up. Tell me if you see a storage message and we'll look at the options.

## tr035-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android (Google Photos)
- task: Back up photos (Android (Google Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
how can I save my pictures so I don't lose them if I lose my phone

**ASSISTANT:**
That's a smart thing to set up. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

**USER:**
android

**ASSISTANT:**
Great. On Android you can use the **Google Photos** app to save copies of your photos to your Google Account. Make sure you have a good internet connection first.

1. Open the **Google Photos** app.
2. Sign in to your Google Account if it asks.
3. Tap your **profile picture or initial** at the top right.
4. Tap **Photos settings**.
5. Tap **Backup**.
6. Turn **Backup** on.

Your photos will start saving to your Google Account. At the top of your library you should see the backup status, such as **Backing up photos** and later **Backup complete**. This can take a while if you have many photos.

Your Google storage is shared with Gmail and Google Drive, and backup stops if it fills up. Tell me if you see a storage message and we'll look at the options.

## tr036-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Add a printer (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows

**USER:**
I just bought a new printer. How do I add it to my Windows 11 computer?

**ASSISTANT:**
Here's how to add your new printer. It can take a few minutes.

**First:** turn the printer on. If it uses a cable, plug it into the computer. Some printers, especially ones with a cable, install by themselves once they are plugged in and on. If it's wireless, make sure it's on the same Wi-Fi network as your computer.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Printers & scanners**.
4. Look at the list of printers. If your printer is already there, you're finished.
5. If it isn't, click **Add a printer & scanner**, then click **Add device**.
6. Wait a few minutes while the computer searches.
7. When your printer appears, click **Add device** next to it.

If your printer doesn't show up, look for **The printer that I want isn't listed**, choose **Add a new device manually**, and follow the instructions.

## tr036-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Add a printer (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows

**USER:**
how do I set up my new printer

**ASSISTANT:**
Congratulations on the new printer. What will you print from: a **Windows computer**, a **Mac**, or a **phone**?

**USER:**
My Windows 11 laptop

**ASSISTANT:**
Great, here's how to add the printer to your Windows 11 laptop. It can take a few minutes.

**First:** turn the printer on. If it uses a cable, plug it into the computer. Some printers, especially ones with a cable, install by themselves once they are plugged in and on. If it's wireless, make sure it's on the same Wi-Fi network as your computer.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Printers & scanners**.
4. Look at the list of printers. If your printer is already there, you're finished.
5. If it isn't, click **Add a printer & scanner**, then click **Add device**.
6. Wait a few minutes while the computer searches.
7. When your printer appears, click **Add device** next to it.

If your printer doesn't show up, look for **The printer that I want isn't listed**, choose **Add a new device manually**, and follow the instructions.

## tr037-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Gmail app (phone)
- task: Attach a photo to an email (Gmail app (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
how do I send a picture in an email

**ASSISTANT:**
I can help. Which email app are you using, for example **Gmail** on your phone?

**USER:**
Gmail app on my Android phone

**ASSISTANT:**
Thanks, here's how in the Gmail app. It takes about a minute.

1. Open the **Gmail** app.
2. Tap **Compose** at the bottom right to start a new email.
3. Tap the **Attach** icon at the top right.
4. Choose where the photo is, such as **Photos**.
5. Tap the photo you want. You can pick up to five photos at once.

Then add the email address and your message as usual, and send it.

If you added the wrong photo, tap **Close** to the right of its name to remove it. If the attachments are over 25 MB on a personal Gmail account, Gmail adds them as a Google Drive link instead. Work and school accounts can have a different limit set by their administrator.

## tr041-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Someone asks to be paid with gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

**USER:**
I got an email from my pastor asking me to buy five $100 gift cards for church members and send him the numbers on the back. He said he's in a meeting and can't talk. Should I do it?

**ASSISTANT:**
Please **don't buy the gift cards**. This is a common scam. Real businesses and government agencies never ask to be paid with gift cards, and scammers often pretend to be someone you know. Once you share the numbers, report it to the gift card company right away, because some companies might give your money back.

Here's what to do:

1. **Don't reply** to the email.
2. **Call your pastor** using a phone number you already have, or call the church office, and ask if he really sent it.
3. If it's fake, you can report it at **ReportFraud.ftc.gov**.

**If you already bought cards and shared the numbers:**
- Call the **gift card company** right away and ask for your money back. Sometimes they can freeze what's left on the card.
- Keep the cards and the store receipt. The number on the card and the receipt help you report it to the company.
- The FTC's gift card scam page lists phone numbers for major gift card companies. If yours isn't listed, look on the card or search online for the company that issued it.
- Report it at **ReportFraud.ftc.gov**.

## tr041-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: Someone asks to be paid with gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

**USER:**
Our church secretary forwarded a weird email to everyone saying Pastor needs gift cards for a surprise and to text him the codes. My friend already bought some. I don't want to be rude to Pastor if it's real.

**ASSISTANT:**
You're not being rude by checking, and a real pastor would understand. Your friend should act first. They should **contact the gift card company right away**, tell them the cards were used in a scam, ask for the money back, and ask if they can freeze it. Your friend should keep the cards and the store receipt, because the number on the card and the receipt help with the report. They can also report it at **ReportFraud.ftc.gov**.

The FTC's gift card scam page lists phone numbers for major gift card companies. If your friend's isn't listed, they can look on the card or search online for the company that issued it.

For you: please **don't buy the gift cards**. This is a common scam. Real businesses and government agencies never ask to be paid with gift cards, and scammers often pretend to be someone you know.

1. **Don't reply** to the email.
2. **Call your pastor** using a phone number you already have, or call the church office, and ask if he really sent it.
3. If it's fake, you can report it at **ReportFraud.ftc.gov**.

## tr041-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: any
- task: Someone asks to be paid with gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

**USER:**
someone wants me to pay with gift cards, is that normal?

**ASSISTANT:**
**Please don't buy any gift cards yet.** Being asked to pay with gift cards is a common sign of a scam.

**Have you already bought or sent any gift cards?**

**USER:**
It's an email from my pastor. I haven't bought anything yet.

**ASSISTANT:**
Good, you haven't lost anything. Please **don't buy the gift cards**. This is a common scam. Real businesses and government agencies never ask to be paid with gift cards, and scammers often pretend to be someone you know. Once you share the numbers, report it to the gift card company right away, because some companies might give your money back.

Here's what to do:

1. **Don't reply** to the email.
2. **Call your pastor** using a phone number you already have, or call the church office, and ask if he really sent it.
3. If it's fake, you can report it at **ReportFraud.ftc.gov**.

If you ever do share card numbers, tell me right away and call the gift card company.

## tr042-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Set up Family Sharing (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108380

**USER:**
How do I set up Family Sharing on my iPhone so my daughter can be part of it?

**ASSISTANT:**
Here's how to start a family group and invite your daughter. It takes a few minutes.

**Create the group:**
1. Open **Settings** and tap **your name**.
2. Tap **Family**, then tap **Continue**.
3. Follow the instructions on the screen to set up your family group and invite members.

**To invite your daughter later, or if you skipped that:**
4. Go to **Settings**, then **Family**.
5. Tap the **Add Member** button.
6. Tap **Invite Others** and follow the steps to send her an invitation.

Once she accepts, she'll be part of your family group. If she doesn't see the invitation, go to **Settings**, then **Family**, tap her name, and choose **Resend Invitation**.

## tr042-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Set up Family Sharing (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108380

**USER:**
how do I share things with my family on my phone

**ASSISTANT:**
There are a few ways to do that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone. My daughter said to set up Family Sharing so we can share stuff.

**ASSISTANT:**
Got it. Family Sharing is a good choice for that.

Here's how to start a family group and invite your daughter. It takes a few minutes.

**Create the group:**
1. Open **Settings** and tap **your name**.
2. Tap **Family**, then tap **Continue**.
3. Follow the instructions on the screen to set up your family group and invite members.

**To invite your daughter later, or if you skipped that:**
4. Go to **Settings**, then **Family**.
5. Tap the **Add Member** button.
6. Tap **Invite Others** and follow the steps to send her an invitation.

Once she accepts, she'll be part of your family group. If she doesn't see the invitation, go to **Settings**, then **Family**, tap her name, and choose **Resend Invitation**.

## tr043-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Add a contact (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
How do I add a new contact on my Android phone? I want to save my new doctor's office number.

**ASSISTANT:**
Here's how to save the number. It takes about a minute.

1. Open the **Contacts** app.
2. Tap **Add** at the bottom right.
3. Type a name, like **Dr. Smith's Office**.
4. Type the phone number.
5. Tap **Save**.

Now you can find the number in Contacts.

If your phone uses a different contacts app and you don't see **Add**, tell me what you see.

## tr043-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Add a contact (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
how do I save a phone number

**ASSISTANT:**
Happy to help you save it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

**USER:**
Android

**ASSISTANT:**
Thanks.

Here's how to save the number. It takes about a minute.

1. Open the **Contacts** app.
2. Tap **Add** at the bottom right.
3. Type a name, like **Mom** or **Dr. Smith's Office**.
4. Type the phone number.
5. Tap **Save**.

Now you can find the number in Contacts.

If your phone uses a different contacts app and you don't see **Add**, tell me what you see.

## tr045-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Block a phone number (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111104

**USER:**
Someone keeps calling me from the same number and hanging up. How do I block it on my iPhone?

**ASSISTANT:**
You can block that number from your list of recent calls. It takes less than a minute.

1. Open the **Phone** app.
2. Tap **Recents**.
3. Tap the number you want to block. (In Classic view, tap the **Info** button instead.)
4. Scroll down and tap **Block Caller**.

The caller won't be told they're blocked. If they leave a voicemail, you won't get a notification.

## tr045-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Block a phone number (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111104

**USER:**
how do I stop a number from calling me

**ASSISTANT:**
You can block it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

**USER:**
iPhone

**ASSISTANT:**
Thanks. You can block that number from your list of recent calls. It takes less than a minute.

1. Open the **Phone** app.
2. Tap **Recents**.
3. Tap the number you want to block. (In Classic view, tap the **Info** button instead.)
4. Scroll down and tap **Block Caller**.

The caller won't be told they're blocked. If they leave a voicemail, you won't get a notification.

## tr046-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Block a phone number (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/6325463?hl=en

**USER:**
a spam number keeps calling

**ASSISTANT:**
That's annoying. I can show you how to block it. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android, Pixel 6

**ASSISTANT:**
Thanks, here's how in Google's Phone app. It takes less than a minute.

1. Open the **Phone** app.
2. Tap **More**, then choose **Call history**.
3. Tap a call from the number you want to block.
4. Tap **Block / report spam**.

Blocked callers can't ring through, and if you use visual voicemail, they can't leave voicemails either.

These steps are for Google's Phone app. If your Phone app looks different, tell me what you see.
