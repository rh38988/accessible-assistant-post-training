# Review input: batch ex3, round 1 (53 examples)

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
3. Tap **Software updates**. On some phones this is called **System update** or is in a different spot.
4. Follow the instructions on the screen to download and install the update.

Your phone may restart during the update. On Google Pixel phones, the update installs in the background and finishes when you restart.

If it says there isn't enough space, tell me and I'll help you free some up first.

## tr033-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Install a software update (Android) | sensitive: False | reviewed by a person: True
- sources: https://support.google.com/android/answer/7680439?hl=en

**USER:**
my phone says there's an update, should I do it?

**ASSISTANT:**
Updates are usually a good idea because they fix problems and help keep your phone secure. If the message popped up on a website, don't tap it. Real updates come from your phone's Settings.

So I can show you the right steps: is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

## tr033-c
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Install a software update (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7680439?hl=en

**USER:**
My phone keeps showing a message about an update. Last time I updated something on my old phone all my contacts disappeared and I don't want that to happen again.

**ASSISTANT:**
That sounds stressful, and it makes sense to be careful. I can walk you through doing it the safe way.

First, **is your phone an iPhone or an Android phone** (like Samsung or Google Pixel)?

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
Thanks. If you still see the update notification, you can tap it. Otherwise, follow these steps.

Here's how to check for an update. Before you start, connect to Wi-Fi and make sure your battery is at least 75% charged, because updates can take a while.

1. Open the **Settings** app.
2. Tap **System**.
3. Tap **Software updates**. On some phones this is called **System update** or is in a different spot.
4. Follow the instructions on the screen to download and install the update.

Your phone may restart during the update. On Google Pixel phones, the update installs in the background and finishes when you restart.

If it says there isn't enough space, tell me and I'll help you free some up first.

## tr034-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Install Windows updates (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates

**USER:**
How do I install Windows updates on my Windows 11 computer?

**ASSISTANT:**
Here's how to check for updates and install them. It can take a while, so do it when you won't need the computer for a bit.

1. Click the **Start** button (the Windows logo).
2. Click **Settings**.
3. Click **Windows Update**.
4. Click **Check for updates**.
5. If updates are found, click **Download & install**.

If Windows asks you to restart, save anything you're working on first, then restart to finish the update.

If you see an error message, write it down or take a picture of it, and tell me what it says.

## tr034-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Install Windows updates (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates

**USER:**
my computer keeps saying it needs to update

**ASSISTANT:**
Updates help keep your computer working well and safe. Is your computer a **Windows** computer or a **Mac**?

## tr034-c
- scenario: direct_messy | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Install Windows updates (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates

**USER:**
Dell Inspiron, Windows 11 Home. The little icon by the clock says updates are available. I'm comfortable with Settings, just tell me where to go.

**ASSISTANT:**
Sure, here's the path:

Here's how to check for updates and install them. It can take a while, so do it when you won't need the computer for a bit.

1. Click the **Start** button (the Windows logo).
2. Click **Settings**.
3. Click **Windows Update**.
4. Click **Check for updates**.
5. If updates are found, click **Download & install**.

If Windows asks you to restart, save anything you're working on first, then restart to finish the update.

If you see an error message, write it down or take a picture of it, and tell me what it says.

## tr034-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Install Windows updates (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates

**USER:**
my computer keeps saying it needs to update

**ASSISTANT:**
Updates help keep your computer working well and safe. Is your computer a **Windows** computer or a **Mac**?

**USER:**
Windows 11

**ASSISTANT:**
Thanks. Here's how to install the updates.

Here's how to check for updates and install them. It can take a while, so do it when you won't need the computer for a bit.

1. Click the **Start** button (the Windows logo).
2. Click **Settings**.
3. Click **Windows Update**.
4. Click **Check for updates**.
5. If updates are found, click **Download & install**.

If Windows asks you to restart, save anything you're working on first, then restart to finish the update.

If you see an error message, write it down or take a picture of it, and tell me what it says.

## tr035-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android (Google Photos)
- task: Back up photos (Android (Google Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
How do I back up my photos on my Android phone so I don't lose them?

**ASSISTANT:**
You can use the **Google Photos** app to save copies of your photos to your Google Account. It takes a couple of minutes to turn on.

1. Open the **Google Photos** app.
2. Sign in to your Google Account if it asks.
3. Tap your **profile picture or initial** at the top right.
4. Tap **Photos settings**.
5. Tap **Backup**.
6. Turn **Backup** on.

Your photos will start saving to your Google Account. This can take a while if you have many photos.

Your Google storage is shared with Gmail and Google Drive, and backup stops if it fills up. Tell me if you see a storage message and we'll look at the options.

## tr035-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Back up photos (Android (Google Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
how can I save my pictures so I don't lose them if I lose my phone

**ASSISTANT:**
That's a smart thing to set up. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

## tr035-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android (Google Photos)
- task: Back up photos (Android (Google Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I dropped my old phone in the lake last summer and lost all the pictures of my granddaughter's first year. I have a new Android phone now and I don't want that to happen again.

**ASSISTANT:**
I'm sorry about those pictures. Let's make sure your new ones are kept safe. Google Photos can save a copy online:

You can use the **Google Photos** app to save copies of your photos to your Google Account. It takes a couple of minutes to turn on.

1. Open the **Google Photos** app.
2. Sign in to your Google Account if it asks.
3. Tap your **profile picture or initial** at the top right.
4. Tap **Photos settings**.
5. Tap **Backup**.
6. Turn **Backup** on.

Your photos will start saving to your Google Account. This can take a while if you have many photos.

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
Great. On Android, Google Photos can do this for you.

You can use the **Google Photos** app to save copies of your photos to your Google Account. It takes a couple of minutes to turn on.

1. Open the **Google Photos** app.
2. Sign in to your Google Account if it asks.
3. Tap your **profile picture or initial** at the top right.
4. Tap **Photos settings**.
5. Tap **Backup**.
6. Turn **Backup** on.

Your photos will start saving to your Google Account. This can take a while if you have many photos.

Your Google storage is shared with Gmail and Google Drive, and backup stops if it fills up. Tell me if you see a storage message and we'll look at the options.

## tr036-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Add a printer (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows

**USER:**
I just bought a new printer. How do I add it to my Windows 11 computer?

**ASSISTANT:**
Here's how to add your new printer. It takes about five minutes.

**First:** turn the printer on. If it uses a cable, plug it into the computer. If it's wireless, make sure it's on the same Wi-Fi network as your computer.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Printers & scanners**.
4. Next to **Add a printer & scanner**, click **Add device**.
5. Wait a few minutes while the computer searches.
6. When your printer appears, click **Add device** next to it.

Some printers install by themselves after step 4.

If your printer doesn't show up, look for **The printer that I want isn't listed**, choose **Add a new device manually**, and follow the instructions.

## tr036-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Add a printer (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows

**USER:**
how do I set up my new printer

**ASSISTANT:**
Congratulations on the new printer. What will you print from: a **Windows computer**, a **Mac**, or a **phone**?

## tr036-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Add a printer (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows

**USER:**
new printer wont

**ASSISTANT:**
It sounds like your message got cut off. What won't the new printer do: **turn on**, **connect**, or **print**? And what are you printing from, a computer or a phone?

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
Great, here's how to add it to your Windows 11 laptop.

Here's how to add your new printer. It takes about five minutes.

**First:** turn the printer on. If it uses a cable, plug it into the computer. If it's wireless, make sure it's on the same Wi-Fi network as your computer.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Printers & scanners**.
4. Next to **Add a printer & scanner**, click **Add device**.
5. Wait a few minutes while the computer searches.
6. When your printer appears, click **Add device** next to it.

Some printers install by themselves after step 4.

If your printer doesn't show up, look for **The printer that I want isn't listed**, choose **Add a new device manually**, and follow the instructions.

## tr037-a
- scenario: direct | style: plain | specification: fully_specified | platform: Gmail app (phone)
- task: Attach a photo to an email (Gmail app (phone)) | sensitive: False | reviewed by a person: True
- sources: https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
How do I attach a photo to an email in the Gmail app on my Android phone?

**ASSISTANT:**
Here's how. It takes about a minute.

1. Open the **Gmail** app.
2. Tap **Compose** at the bottom right to start a new email.
3. Tap the **Attach** icon at the top right. It looks like a **paperclip**.
4. Choose where the photo is, such as **Photos**.
5. Tap the photo you want. You can pick up to five photos at once.

Then add the email address and your message as usual, and send it.

If you added the wrong photo, tap the close icon (**X**) next to its name to remove it. Files over 25 MB are added as a Google Drive link instead.

## tr037-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Attach a photo to an email (Gmail app (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
how do I send a picture in an email

**ASSISTANT:**
I can help. Do you use email on a **phone** or a **computer**, and which email app, for example **Gmail**?

## tr037-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Attach a photo to an email (Gmail app (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
how to attach

**ASSISTANT:**
Happy to help you attach something. **What would you like to attach** (a photo, a document?), and **where**: in an email, a text message, or somewhere else?

## tr037-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Gmail app (phone)
- task: Attach a photo to an email (Gmail app (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
how do I send a picture in an email

**ASSISTANT:**
I can help. Do you use email on a **phone** or a **computer**, and which email app, for example **Gmail**?

**USER:**
Gmail app on my Android phone

**ASSISTANT:**
Thanks, here's how in the Gmail app.

Here's how. It takes about a minute.

1. Open the **Gmail** app.
2. Tap **Compose** at the bottom right to start a new email.
3. Tap the **Attach** icon at the top right.
4. Choose where the photo is, such as **Photos**.
5. Tap the photo you want. You can pick up to five photos at once.

Then add the email address and your message as usual, and send it.

If you added the wrong photo, tap the close icon (**X**) next to its name to remove it. Very large files are added as a Google Drive link instead, which the person can still open.

## tr038-a
- scenario: direct | style: plain | specification: fully_specified | platform: Google Account
- task: Reset forgotten Google Account password (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/7682439?hl=en

**USER:**
I forgot my Gmail password and can't sign in. How do I get back into my account?

**ASSISTANT:**
You can get back in through Google's account recovery. It usually takes a few minutes.

1. Go to Google's **account recovery** page.
2. Enter the details it asks for, starting with your Gmail address.
3. Answer the questions as best you can. If you're not sure of an answer, make your best guess. A wrong guess doesn't lock you out, and you can try again.
4. When asked, create a **new password** that you haven't used for this account before.

**Stay safe while you do this:**
- Google staff can't help you sign in over the phone, so ignore anyone who calls or messages offering to recover your account.
- Never share your password or any verification code with anyone.

If it doesn't work right away, wait a few days and try again.

## tr038-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Reset forgotten Google Account password (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/7682439?hl=en

**USER:**
I can't get into my email

**ASSISTANT:**
That's stressful, but it can usually be fixed. **Which email do you use** (for example Gmail, which ends in @gmail.com), and **what's going wrong**, such as a forgotten password or an error message?

## tr038-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Google Account
- task: Reset forgotten Google Account password (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/7682439?hl=en

**USER:**
I haven't used my Gmail on the computer in ages because my phone just stays logged in, but my phone broke and now the new one is asking for the password and I have no idea what it is.

**ASSISTANT:**
That happens a lot when a phone stays signed in for years. You can reset the password:

You can get back in through Google's account recovery. It usually takes a few minutes.

1. Go to Google's **account recovery** page.
2. Enter the details it asks for, starting with your Gmail address.
3. Answer the questions as best you can. If you're not sure of an answer, make your best guess. A wrong guess doesn't lock you out, and you can try again.
4. When asked, create a **new password** that you haven't used for this account before.

**Stay safe while you do this:**
- Google staff can't help you sign in over the phone, so ignore anyone who calls or messages offering to recover your account.
- Never share your password or any verification code with anyone.

If it doesn't work right away, wait a few days and try again.

## tr038-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Google Account
- task: Reset forgotten Google Account password (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/7682439?hl=en

**USER:**
I can't get into my email

**ASSISTANT:**
That's stressful, but it can usually be fixed. **Which email do you use** (for example Gmail, which ends in @gmail.com), and **what's going wrong**, such as a forgotten password or an error message?

**USER:**
Gmail, I forgot the password

**ASSISTANT:**
Thanks. You can reset it through Google's account recovery.

You can get back in through Google's account recovery. It usually takes a few minutes.

1. Go to Google's **account recovery** page.
2. Enter the details it asks for, starting with your Gmail address.
3. Answer the questions as best you can. If you're not sure of an answer, make your best guess. A wrong guess doesn't lock you out, and you can try again.
4. When asked, create a **new password** that you haven't used for this account before.

**Stay safe while you do this:**
- Google staff can't help you sign in over the phone, so ignore anyone who calls or messages offering to recover your account.
- Never share your password or any verification code with anyone.

If it doesn't work right away, wait a few days and try again.

## tr039-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Call that sounds like a family member's voice asking for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes

**USER:**
My granddaughter called crying and said she's in jail and needs bail money wired right now. It really sounded like her. Is this real?

**ASSISTANT:**
Please **don't send any money yet**. Scammers can now copy a person's voice from a short recording, like a video posted online, so a call can sound exactly like someone you love.

Here's what to do:

1. **Hang up.** You don't need to argue or explain.
2. **Call your granddaughter** at the phone number you already have for her, not a number from the call.
3. If you can't reach her, **call another family member** or one of her friends to check.

**Warning signs of this scam:** an urgent emergency, pressure to act fast, and a request to **wire money, send cryptocurrency, or buy gift cards**. Those payments are very hard to get back.

If it turns out to be a scam, you can report it at **ReportFraud.ftc.gov**. If you already sent money, tell me right away and we'll work out the next steps.

## tr039-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Call that sounds like a family member's voice asking for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes

**USER:**
Someone called and said my granddaughter needs money, what should I do?

**ASSISTANT:**
I'm glad you asked before doing anything. To help you check: **what exactly did they ask you to do, and how did they want the money sent?** For example, did they ask for a wire transfer or gift cards?

## tr039-c
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Call that sounds like a family member's voice asking for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes

**USER:**
Got a strange call last night. Not sure what to make of it.

**ASSISTANT:**
I'm happy to help you figure it out. **What did the caller say, and did they ask you for money or personal information?**

## tr039-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: any
- task: Call that sounds like a family member's voice asking for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes

**USER:**
Someone called and said my granddaughter needs money, what should I do?

**ASSISTANT:**
I'm glad you asked before doing anything. To help you check: **what exactly did they ask you to do, and how did they want the money sent?** For example, did they ask for a wire transfer or gift cards?

**USER:**
They wanted me to wire $3,000. The voice sounded just like her.

**ASSISTANT:**
Thank you for telling me. A request to wire money in an emergency is a common warning sign, even when the voice sounds right.

Please **don't send any money yet**. Scammers can now copy a person's voice from a short recording, like a video posted online, so a call can sound exactly like someone you love.

Here's what to do:

1. **Hang up.** You don't need to argue or explain.
2. **Call your granddaughter** at the phone number you already have for her, not a number from the call.
3. If you can't reach her, **call another family member** or one of her friends to check.

**Warning signs of this scam:** an urgent emergency, pressure to act fast, and a request to **wire money, send cryptocurrency, or buy gift cards**. Those payments are very hard to get back.

If it turns out to be a scam, you can report it at **ReportFraud.ftc.gov**. If you already sent money, tell me right away and we'll work out the next steps.

## tr040-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Text says package could not be delivered (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam

**USER:**
I got a text saying USPS couldn't deliver my package and I need to click a link to update my address. I am expecting a package. Should I click it?

**ASSISTANT:**
Please **don't click the link**. Texts like this are a common scam, even when you really are expecting a package. The link usually leads to a fake website that looks real and asks for your personal or card information.

Instead:

1. **Don't click** the link or reply.
2. Check on your package using the website or app of the **store where you bought it**. Go there directly, not through the text.
3. **Report the text.** Use your phone's **junk** or **spam** reporting option if you see one, or forward the text to **7726**.
4. Then delete it.

If you already clicked and typed in your card number, call your bank right away using the number on the back of your card.

## tr040-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Text says package could not be delivered (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam

**USER:**
I got a text about a package, is it real?

**ASSISTANT:**
Let's check it together. **What does the text ask you to do?** For example, does it have a link to click, or ask you to pay a fee or update your address?

## tr040-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Text says package could not be delivered (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam

**USER:**
usps text link

**ASSISTANT:**
Do you mean you got a text that looks like it's from **USPS** with a link in it? If so, please don't click the link yet. **What does the text ask you to do?**

## tr040-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: any
- task: Text says package could not be delivered (any) | sensitive: True | reviewed by a person: True
- sources: https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam

**USER:**
I got a text about a package, is it real?

**ASSISTANT:**
Let's check it together. **What does the text ask you to do?** For example, does it have a link to click, or ask you to pay a fee or update your address?

**USER:**
It has a link and says I need to pay $1.99 for redelivery.

**ASSISTANT:**
Thanks. A small fee plus a link is a very common sign of a scam, even when you really are expecting a package. Please **don't click the link**. It usually leads to a fake website that looks real and asks for your personal or card information.

Instead:

1. **Don't click** the link or reply.
2. Check on your package using the website or app of the **store where you bought it**. Go there directly, not through the text.
3. **Report the text.** Use your phone's **junk** or **spam** reporting option if you see one, or forward the text to **7726**. You can also report it at **ReportFraud.ftc.gov**.
4. Then delete it.

If you already clicked and typed in your card number, call your bank right away using the number on the back of your card.

## tr041-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Someone asks to be paid with gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

**USER:**
I got an email from my pastor asking me to buy five $100 gift cards for church members and send him the numbers on the back. He said he's in a meeting and can't talk. Should I do it?

**ASSISTANT:**
Please **don't buy the gift cards**. This is a common scam. Real businesses, government agencies, and people you know don't ask to be paid with gift card numbers, and once you share the numbers, the money is very hard to get back.

Here's what to do:

1. **Don't reply** to the email.
2. **Call your pastor** using a phone number you already have, or call the church office, and ask if he really sent it.
3. If it's fake, you can report it at **ReportFraud.ftc.gov**.

**If you already bought cards and shared the numbers:**
- Call the **gift card company** right away and ask for your money back. Sometimes they can freeze what's left on the card.
- Keep the cards and the store receipt.
- Report it at **ReportFraud.ftc.gov**.

## tr041-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Someone asks to be paid with gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

**USER:**
someone wants me to pay with gift cards, is that normal?

**ASSISTANT:**
**Please don't buy any gift cards yet.** Being asked to pay with gift cards is a common sign of a scam.

**Who is asking, and have you already bought or sent any cards?**

## tr041-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: Someone asks to be paid with gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

**USER:**
Our church secretary forwarded a weird email to everyone saying Pastor needs gift cards for a surprise and to text him the codes. My friend already bought some. I don't want to be rude to Pastor if it's real.

**ASSISTANT:**
You're not being rude by checking, and a real pastor would understand. The steps for your friend are at the end.

Please **don't buy the gift cards**. This is a common scam. Real businesses, government agencies, and people you know don't ask to be paid with gift card numbers, and once you share the numbers, the money is very hard to get back.

Here's what to do:

1. **Don't reply** to the email.
2. **Call your pastor** using a phone number you already have, or call the church office, and ask if he really sent it.
3. If it's fake, you can report it at **ReportFraud.ftc.gov**.

**If you already bought cards and shared the numbers:**
- Call the **gift card company** right away and ask for your money back. Sometimes they can freeze what's left on the card.
- Keep the cards and the store receipt.
- Report it at **ReportFraud.ftc.gov**.

## tr041-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: any
- task: Someone asks to be paid with gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

**USER:**
someone wants me to pay with gift cards, is that normal?

**ASSISTANT:**
**Please don't buy any gift cards yet.** Being asked to pay with gift cards is a common sign of a scam.

**Who is asking, and have you already bought or sent any cards?**

**USER:**
It's an email from my pastor. I haven't bought anything yet.

**ASSISTANT:**
Good, you haven't lost anything. Here's what to do:

Please **don't buy the gift cards**. This is a common scam. Real businesses, government agencies, and people you know don't ask to be paid with gift card numbers, and once you share the numbers, the money is very hard to get back.

Here's what to do:

1. **Don't reply** to the email.
2. **Call your pastor** using a phone number you already have, or call the church office, and ask if he really sent it.
3. If it's fake, you can report it at **ReportFraud.ftc.gov**.

**If you already bought cards and shared the numbers:**
- Call the **gift card company** right away and ask for your money back. Sometimes they can freeze what's left on the card.
- Keep the cards and the store receipt.
- Report it at **ReportFraud.ftc.gov**.

## tr041-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: any
- task: Someone asks to be paid with gift cards (any) | sensitive: True | reviewed by a person: True
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

**USER:**
I got an email from my pastor asking me to buy five $100 gift cards for church members and send him the numbers on the back. He said he's in a meeting and can't talk. Should I do it?

**ASSISTANT:**
Please **don't buy the gift cards**. This is a common scam. Real businesses, government agencies, and people you know don't ask to be paid with gift card numbers, and once you share the numbers, the money is very hard to get back.

Here's what to do:

1. **Don't reply** to the email.
2. **Call your pastor** using a phone number you already have, or call the church office, and ask if he really sent it.
3. If it's fake, you can report it at **ReportFraud.ftc.gov**.

**If you already bought cards and shared the numbers:**
- Call the **gift card company** right away and ask for your money back. Sometimes they can freeze what's left on the card.
- Keep the cards and the store receipt.
- Report it at **ReportFraud.ftc.gov**.

**USER:**
Oh no. I already bought two $100 cards this morning and emailed him the numbers before I saw this.

**ASSISTANT:**
I'm sorry this happened. This scam fools a lot of careful people. Acting quickly gives you the best chance of getting money back.

1. **Contact the gift card company right away.** Tell them the cards were used in a scam and ask for your money back. Sometimes they can freeze money that hasn't been spent yet. The FTC's gift card scam page lists contact information for major gift card companies.
2. **Keep the cards and the store receipt**, and take a photo of both. You'll need them when you report it.
3. **Report the scam** at **ReportFraud.ftc.gov**.
4. **Don't reply** to the email, and don't buy more cards, even if you're asked again.
5. **Tell your church office**, so they can warn other members, and let your pastor know his email may have been hacked.

Do you have the cards and the receipt with you? If so, we can look at step 1 together.

## tr042-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Set up Family Sharing (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108380

**USER:**
How do I set up Family Sharing on my iPhone so my daughter can be part of it?

**ASSISTANT:**
Here's how to start a family group and invite your daughter. It takes a few minutes.

**Create the group:**
1. Open **Settings** and tap **your name** at the top.
2. Tap **Family**.
3. Follow the instructions on the screen to set up your family group.

**Invite your daughter:**
4. Go to **Settings**, then **Family**.
5. Tap the **add member** button (it has a plus sign).
6. Tap **Invite Others** and follow the steps to send her an invitation.

Once she accepts, she'll be part of your family group. If she doesn't see the invitation, go to **Settings**, then **Family**, tap her name, and choose **Resend Invitation**.

## tr042-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Set up Family Sharing (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108380

**USER:**
how do I share things with my family on my phone

**ASSISTANT:**
There are a few ways to do that. **What would you like to share** (for example photos, your location, or app purchases), and is your phone an **iPhone** or an Android phone?

## tr042-c
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Set up Family Sharing (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108380

**USER:**
family sharing

**ASSISTANT:**
Sure, I can help with Family Sharing. Do you want to **set up a new family group**, **invite someone** to a group you already have, or **accept an invitation** someone sent you?

## tr042-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Set up Family Sharing (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108380

**USER:**
how do I share things with my family on my phone

**ASSISTANT:**
There are a few ways to do that. **What would you like to share** (for example photos, your location, or app purchases), and is your phone an **iPhone** or an Android phone?

**USER:**
iPhone. My daughter said to set up Family Sharing so we can share stuff.

**ASSISTANT:**
Got it. Family Sharing is a good choice for that.

Here's how to start a family group and invite your daughter. It takes a few minutes.

**Create the group:**
1. Open **Settings** and tap **your name** at the top.
2. Tap **Family**.
3. Follow the instructions on the screen to set up your family group.

**Invite your daughter:**
4. Go to **Settings**, then **Family**.
5. Tap the **add member** button (it has a plus sign).
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
2. Tap the **Add** icon at the bottom right.
3. Type a name, like **Dr. Smith's Office**.
4. Type the phone number.
5. Tap **Save**.

Now the name will show up when the office calls you, and you can find the number in Contacts.

If your phone uses a different contacts app and you don't see an **Add** icon, tell me what you see.

## tr043-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Add a contact (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
how do I save a phone number

**ASSISTANT:**
Happy to help you save it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

## tr043-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Add a contact (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
save number to my contacts on

**ASSISTANT:**
It looks like your message got cut off. Which phone are you using, an **iPhone** or an **Android** phone?

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
2. Tap the **Add** icon at the bottom right.
3. Type a name, like **Dr. Smith's Office**.
4. Type the phone number.
5. Tap **Save**.

Now the name will show up when the office calls you, and you can find the number in Contacts.

If your phone uses a different contacts app and you don't see an **Add** icon, tell me what you see.

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
3. Find the number and tap it. (If you see a small **"i"** in a circle next to the number, tap that instead.)
4. Scroll down and tap **Block Caller**.
5. Confirm if asked.

After that, calls from that number won't ring your phone, and the caller won't be told they're blocked. If they leave a voicemail, it's saved, but you won't get a notification.

## tr045-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Block a phone number (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111104

**USER:**
how do I stop a number from calling me

**ASSISTANT:**
You can block it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

## tr045-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Block a phone number (iPhone) | sensitive: False | reviewed by a person: True
- sources: https://support.apple.com/en-us/111104

**USER:**
There's a number from out of state that calls me three or four times a day. When I answer nobody's there. My neighbor said I should block it but I don't know how. I have an iPhone 11.

**ASSISTANT:**
Your neighbor is right: blocking it will stop those calls from ringing. You can do it from your list of recent calls in less than a minute.

1. Open the **Phone** app.
2. Tap **Recents**.
3. Find the number and tap it. (If you see a small **"i"** in a circle next to the number, tap that instead.)
4. Scroll down and tap **Block Caller**.
5. If a message asks you to confirm, tap **Block Contact**.

After that, calls from that number won't ring your phone, and the caller won't be told they're blocked. If they leave a voicemail, it's saved, but you won't get a notification.

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
Thanks. Here's how to block it on your iPhone.

You can block that number from your list of recent calls. It takes less than a minute.

1. Open the **Phone** app.
2. Tap **Recents**.
3. Find the number and tap it. (If you see a small **"i"** in a circle next to the number, tap that instead.)
4. Scroll down and tap **Block Caller**.
5. Confirm if asked.

After that, calls from that number won't ring your phone, and the caller won't be told they're blocked. If they leave a voicemail, it's saved, but you won't get a notification.

## tr046-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Block a phone number (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/6325463?hl=en

**USER:**
How do I block a phone number on my Android phone? It's a spam caller.

**ASSISTANT:**
You can block it from your call history in the **Phone** app. It takes less than a minute.

1. Open the **Phone** app.
2. Tap the **More** menu (three dots) and choose **Call history**.
3. Tap a call from the number you want to block.
4. Tap **Block / report spam**.
5. Confirm if asked.

Blocked callers can't ring through, and if you use visual voicemail, they can't leave voicemails either.

These steps are for Google's Phone app. If your Phone app looks different, tell me what you see.

## tr046-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Block a phone number (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/6325463?hl=en

**USER:**
a spam number keeps calling

**ASSISTANT:**
That's annoying. I can show you how to block it. Is your phone an **iPhone** or an **Android** phone?

## tr046-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Block a phone number (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/6325463?hl=en

**USER:**
block this number

**ASSISTANT:**
Sure, I can help you block it. Is it a number that's been **calling** you or **texting** you? And is your phone an iPhone or an Android phone?

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
Thanks, here's how on your Pixel.

You can block it from your call history in the **Phone** app. It takes less than a minute.

1. Open the **Phone** app.
2. Tap the **More** menu (three dots) and choose **Call history**.
3. Tap a call from the number you want to block.
4. Tap **Block / report spam**.
5. Confirm if asked.

Blocked callers can't ring through, and if you use visual voicemail, they can't leave voicemails either.

These steps are for Google's Phone app. If your Phone app looks different, tell me what you see.
