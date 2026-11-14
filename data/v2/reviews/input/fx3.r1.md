# Review input: batch fx3, round 1 (25 examples)

## tr033-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Install a software update (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7680439?hl=en

**USER:**
I have a Google Pixel and it says there's an update. I'm waiting on a call from my doctor's office and I don't want my phone restarting on me right now. How do I install it?

**ASSISTANT:**
Good news: on a Pixel, updates download and install in the background, and the update only takes effect the next time you restart. So you can restart after your call.

Before you start, connect to Wi-Fi and make sure your battery is at least 75%.

1. Open the **Settings** app.
2. Tap **System**.
3. Tap **Software updates**. The update status shows here.
4. Follow the instructions on the screen.

When your call is done, restart the phone and the update will take effect.

## tr033-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Install a software update (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/7680439?hl=en

**USER:**
A box popped up on my Samsung Android phone saying a new Android version is ready. How do I install it from that message?

**ASSISTANT:**
You can start it right from that message. Before you start, connect to Wi-Fi and make sure your battery is at least 75%.

1. Open the update notification.
2. Tap the update action on it.
3. Follow the instructions on the screen.

Your phone may restart on its own while the update installs.

**USER:**
I swiped the message away by accident and now it's gone.

**ASSISTANT:**
That's okay. The update is still available in Settings.

1. Open the **Settings** app.
2. Tap **System**, then **Software updates**. The update status appears here.
3. Follow the instructions on the screen.

If nothing shows up, your phone may already be up to date, it may no longer get updates, or it may be waiting for your carrier or phone maker to release the update.

## tr034-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Install Windows updates (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates

**USER:**
I'm on my Windows 11 laptop and in the middle of a big project, so I don't want to install anything just yet. I only want to see whether any updates are waiting for me.

**ASSISTANT:**
You can look without installing anything.

1. Click the **Start** button.
2. Click **Settings**.
3. Click **Windows Update**.
4. Click **Check for Windows updates**.

If updates are available, you don't have to do anything more right now. The **Download & install** button is the one that starts the installing, so you can leave it alone until you're ready.

When you do install them, Windows may ask you to restart to finish. Save your work first.

## tr034-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Install Windows updates (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates

**USER:**
Can you walk me through updating my Windows 11 PC? I've never done it before.

**ASSISTANT:**
Sure, it only takes a few clicks.

1. Click **Start**, then **Settings**.
2. Click **Windows Update**.
3. Click **Check for Windows updates**.
4. If updates are available, click **Download & install**.
5. If Windows asks you to restart, restart to finish the update.

Save your work before restarting.

**USER:**
I clicked Check for Windows updates but it just shows an error.

**ASSISTANT:**
Let's try Windows' built-in fixer.

1. Click **Start**, then **Settings**, then **System**, then **Troubleshoot**, then **Other troubleshooters**.
2. Click **Run** next to **Windows Update**.
3. Make sure you're online: go to **Start**, **Settings**, **Network & Internet**, **Wi-Fi**, and reconnect if needed.
4. Go back to **Settings**, **Windows Update**, and click **Check for updates** again.

If you still get an error, write down the error code and tell me what it says.

## tr035-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android (Google Photos)
- task: Back up photos (Android (Google Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I have a Samsung phone and a small data plan. I'd like my pictures kept safe in Google Photos, but I don't want the backup eating up my data. Can I set that up with a limit?

**ASSISTANT:**
Yes. Turn backup on first, then set limits for mobile data.

1. Open the **Google Photos** app.
2. Tap your **profile picture or initial** at the top right.
3. Tap **Photos settings**, then **Backup**.
4. Turn **Backup** on.
5. Still in **Backup**, tap **Mobile data usage**.
6. Set a **daily data limit** for automatic backup.
7. Turn off **Back up videos over data** so your videos stay off mobile data.

You can also choose whether to turn **Back up while roaming** on or off in the same place.

## tr035-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android (Google Photos)
- task: Back up photos (Android (Google Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
My daughter says I should use Google Photos to keep my pictures safe. I have a Pixel phone. What do I do?

**ASSISTANT:**
Google Photos can save copies of your pictures to your Google Account.

1. Open the **Google Photos** app.
2. Tap your **profile picture or initial** at the top right.
3. Tap **Photos settings**, then **Backup**.
4. Turn **Backup** on.

Your pictures start saving to your account. With many photos it can take a while.

**USER:**
I did that yesterday, but now the top of the app says Backup paused and nothing seems to be uploading.

**ASSISTANT:**
Let's check two common causes.

1. Tap the status at the top of the app to see details. Backup works only if your Google storage has room. If you're out of space, tap **buy more storage** or **clean up your storage space**.
2. Your phone's battery saver can interfere. Open **Settings** and search for **battery optimization**. Tap **Battery optimization**, then **All apps**. Tap **Photos**, choose **Don't optimize**, and tap **Done**.

After that, open Google Photos again and check the status at the top.

## tr036-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Add a printer (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows

**USER:**
I have a Windows 11 PC and a new wireless printer. I don't have a USB cable and I don't want to go buy one. Can I still get them working together?

**ASSISTANT:**
Yes, a wireless printer doesn't need a cable. First, turn the printer on and make sure it's on the same wireless network as your computer.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**, then **Printers & scanners**.
3. Next to **Add a printer & scanner**, click **Add device**.
4. Wait a few minutes while the list fills up.
5. When your printer appears, click **Add device** next to it.

Some printers install by themselves after step 3.

## tr036-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Add a printer (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows

**USER:**
I plugged my printer into my Windows 11 computer with the USB cable and turned it on. Now what?

**ASSISTANT:**
Windows usually installs the printer by itself. Let's check.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**, then **Printers & scanners**.
3. Look for your printer in the list. If it's there, you're done.
4. If it's not, next to **Add a printer & scanner**, click **Add device**.
5. Wait a few minutes while the list fills up, then click **Add device** next to your printer.

**USER:**
I waited several minutes and my printer never showed up in the list.

**ASSISTANT:**
Let's try adding it by hand.

1. Check that the printer is turned on and plugged in to the computer.
2. On the same screen, find **The printer that I want isn't listed** and click **Add a new device manually** next to it.
3. Follow the instructions in the **Add Printer** window that opens.

## tr037-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Gmail app (phone)
- task: Attach a photo to an email (Gmail app (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I have three photos from the picnic on my Android phone and I'd like all of them in one email in the Gmail app, not three separate emails.

**ASSISTANT:**
You can put them all in one email.

1. Open the **Gmail** app.
2. Tap **Compose** at the bottom right.
3. Tap **Attach** at the top right.
4. Choose **Photos**.
5. Tap each photo you want. You can select up to five at a time, so all three fit.

Then add the email address and your message, and send it.

If the photos are very large (over 25 MB together on a regular Gmail account), Gmail adds them as a Google Drive link instead.

## tr037-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Gmail app (phone)
- task: Attach a photo to an email (Gmail app (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
Please show me how to put a picture into an email with the Gmail app on my Android phone. It's for my nephew's birthday.

**ASSISTANT:**
Here's how.

1. Open the **Gmail** app.
2. Tap **Compose** at the bottom right.
3. Tap **Attach** at the top right.
4. Choose **Photos**.
5. Tap the picture you want.

Then add your nephew's email address and your message, and send it.

**USER:**
I tapped send and it says Couldn't send message.

**ASSISTANT:**
That message can appear when a picture didn't finish uploading, often because of slow internet or low space. Try this:

1. Tap **Close** on the right side of the picture's name to remove it.
2. Tap **Attach**, choose **Photos**, and pick the picture again.
3. Send the email again.

If it keeps happening, your Google storage may be full. Attachments count toward it, so deleting large attachments and emptying your trash and spam can free space.

## tr038-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Google Account
- task: Reset forgotten Google Account password (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/7682439?hl=en

**USER:**
I'm not good with websites. I'd rather just phone Google and have them reset my Gmail password for me. What's their number?

**ASSISTANT:**
Google can't help you sign in over the phone, so there's no number to call for this. Please be careful with anyone who offers to recover your account for you, because Google doesn't work with account or password recovery services. Never give out your password or any verification codes.

The way back in is Google's recovery page, which asks you some questions:

1. Go to **https://accounts.google.com/signin/recovery?ec=ar_hc_7682439**.
2. Answer the questions as accurately as you can. They confirm it's your account.
3. When prompted, reset your password. Choose a strong one you haven't used with this account.

## tr038-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Google Account
- task: Reset forgotten Google Account password (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/7682439?hl=en

**USER:**
My grandson says I need to reset my Google password. I use it for email on my tablet. How do I do that?

**ASSISTANT:**
You can do it on Google's recovery page.

1. Go to **https://accounts.google.com/signin/recovery?ec=ar_hc_7682439**.
2. Answer the questions as accurately as you can. They confirm it's your account.
3. When prompted, reset your password. Choose a strong one you haven't used with this account.

Never share your password or any verification code with anyone, and remember that Google can't help you sign in over the phone.

**USER:**
I answered the questions but it says it can't tell it's my account.

**ASSISTANT:**
Don't worry, you can try again.

1. Go through the questions again and answer as accurately as you can. Wrong guesses don't end the process, and there's no limit on tries.
2. Read Google's tips for trouble at **https://support.google.com/accounts/answer/7299973**.
3. If you changed your recovery information recently, the change can take up to 7 days to take effect. Try again in a few days.

## tr039-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Call that sounds like a family member's voice asking for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes

**USER:**
My grandson called from a number I don't know, sounding scared, and said he'd been in a car accident and needs $2,000 sent through Western Union. He begged me not to tell his parents. I've tried his own phone but it goes straight to voicemail.

**ASSISTANT:**
Please **don't send any money**. Scammers can copy a person's voice, sometimes from a short recording posted online, so a call can sound just like your grandson. Don't trust the voice.

1. **Hang up** if you haven't already.
2. **Call him again** at the number you already know is his, not the number that called you.
3. Since you can't reach him, **contact him through another family member or his friends**. That includes his parents, even though the caller asked you not to tell them.

Asking you to wire money, send cryptocurrency, or buy gift cards are warning signs, because those payments are hard to get back.

You can report the call at **ReportFraud.ftc.gov**.

## tr039-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Call that sounds like a family member's voice asking for money (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes

**USER:**
A call came in that sounded just like my granddaughter saying she was in trouble. I wired $2,500 through Western Union an hour ago, and now I can't reach her and I'm afraid it was a scam.

**ASSISTANT:**
I'm sorry, this happens to careful people. Please don't send any more money, and contact the wire transfer company right away.

1. **Report it to the wire transfer company immediately.** Tell them a scammer tricked you, and ask for a refund.
2. **Check on your granddaughter.** Call her at a number you know is hers. If you can't reach her, contact her through another family member or her friends.
3. **Report the scam to the FTC** at **ReportFraud.ftc.gov**.

## tr040-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Text says package could not be delivered (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam

**USER:**
I'm expecting about four packages this week from different places, so a text from USPS about a package problem could be real. It wants me to tap a link to confirm my delivery preferences. I don't remember which store each package came from.

**ASSISTANT:**
Please **don't tap the link** or give any information, even with several packages on the way. The link usually goes to a look-alike of a real website that asks for personal or payment details, and anything you enter goes to the scammer.

1. **Don't click** the link or reply.
2. **Check each order where you bought it.** Open the website or account of each store you ordered from, and look up the shipping and tracking information there, not through the text.
3. **Report the text.** Use your messaging app's junk or spam option, or forward it to **7726**.
4. You can also report it at **ReportFraud.ftc.gov**.

## tr040-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Text says package could not be delivered (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam

**USER:**
I got a text from USPS about a missed delivery. I clicked the link and typed in my credit card number to pay a $1.99 fee, then got suspicious. What do I do?

**ASSISTANT:**
I'm sorry, these texts look very real and fool many people. Contact your credit card company right away.

1. **Report it to the credit card issuer immediately.** Call the number on the back of your card, or log in to your account online or in the app.
2. Tell them what happened and **ask for a refund**.
3. **Report the text.** Use your messaging app's junk or spam option, or forward it to **7726**.
4. **Report it to the FTC** at **ReportFraud.ftc.gov**.

## tr041-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Someone asks to be paid with gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams

**USER:**
My nephew texted me from a new number saying he's stuck at the airport and needs me to buy Google Play gift cards to pay for a rebooked flight, then text him the codes. His regular phone seems to be off, so I can't reach him to check. He says it's really urgent.

**ASSISTANT:**
Please **don't buy the gift cards**. Scammers say it's urgent so you'll rush, so slow down and don't pay. No real business or government agency will ever tell you to buy a gift card to pay them, and gift cards are for gifts only.

1. **Don't reply** and don't send any codes or photos of cards.
2. **Reach your nephew through a number you already know is his**, not the new number that texted you. Scammers may also use voice cloning, so check with him directly.
3. **Report the text** at **ReportFraud.ftc.gov**.

If you've already bought cards or shared the numbers, report it to the gift card company right away and ask for your money back. Keep the cards and the receipt.

## tr042-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Set up Family Sharing (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108380

**USER:**
I have an iPhone and my 12 year old grandson doesn't have his own Apple Account yet. I'd like him in my Family Sharing, but I don't want to give him my login.

**ASSISTANT:**
Family Sharing is made for that. You can share things like iCloud+, Apple Music, and Apple TV without sharing an Apple Account. For a child without an account, you create a Child Account.

**Set up the group (if you haven't yet):**
1. Open **Settings** and tap **your name**.
2. Tap **Family**, then tap **Continue**.
3. Follow the instructions on the screen.

**Add your grandson:**
4. Go to **Settings**, then **Family**.
5. Tap the **Add Member** button.
6. Tap **Create Child Account** and follow the instructions on the screen.
7. Finish the prompts for parental controls, location sharing, and similar settings.

## tr042-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Set up Family Sharing (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108380

**USER:**
I'm on an iPhone and I want to invite my wife to my Family Sharing group. I already made the group.

**ASSISTANT:**
Here's how to invite her.

1. Open **Settings**, then tap **Family**.
2. Tap the **Add Member** button.
3. Tap **Invite Others**.
4. Finish the prompts that follow.

The invitation is sent to her by Messages or email.

**USER:**
She says the invitation never came.

**ASSISTANT:**
Let's check on it and send it again.

1. Open **Settings**, then tap **Family**.
2. Tap her name to see the invitation status.
3. Tap **Resend Invitation**.

She can accept from the email or text invitation. Or on her iPhone she can open **Settings**, tap her name, tap **Invitations**, and follow the instructions on the screen.

## tr043-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Add a contact (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
My son's teacher gave me only her email address, no phone number. I have an Android phone. Can I still make a contact for her?

**ASSISTANT:**
Yes. A contact needs a name and either an email address or a phone number.

1. Open the **Contacts** app.
2. Tap **Add** at the bottom right.
3. Type her name.
4. Type her email address.
5. Tap **Save**.

If you want to add more details later, such as a street address or notes, open her contact and tap the field to edit it, or tap **Add fields**.

## tr043-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Add a contact (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I'm using an Android phone. How do I put my friend Linda's number into my Contacts?

**ASSISTANT:**
Here's how.

1. Open the **Contacts** app.
2. Tap **Add** at the bottom right.
3. Type Linda's name.
4. Type her phone number.
5. Tap **Save**.

**USER:**
I saved her, but when I signed in on my new Android phone, Linda isn't there.

**ASSISTANT:**
Contacts saved to a Google Account sync to your Android devices, so Linda may be saved somewhere else. You can move her to your Google Account:

1. Open the **Contacts** app and tap **Linda**.
2. At the top right, tap **Contact settings**.
3. Tap **Move to another account**.
4. Choose your Google Account.

Moving a contact deletes it from its original account.

## tr045-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Block a phone number (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111104

**USER:**
A man keeps texting me from a number I don't know on my iPhone, mostly rude stuff. He never calls, so there's nothing in my recent calls. I don't want him to know I blocked him.

**ASSISTANT:**
You can block him right from the text conversation, and he won't be told.

1. Open the **Messages** app and open the conversation with him.
2. Tap his number or name at the top.
3. Scroll down and tap **Block Caller**.

After that, messages he sends won't be delivered to you, and he isn't notified that he was blocked.

## tr045-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Block a phone number (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111104

**USER:**
A telemarketer calls my iPhone every afternoon. Please show me how to block the number.

**ASSISTANT:**
You can block it from your recent calls.

1. Open the **Phone** app.
2. Tap **Recents**.
3. Tap the phone number. If you see the **Info** button, tap that instead.
4. Scroll down and tap **Block Caller**.

After that, the caller isn't told they were blocked.

**USER:**
Oh no, I think I blocked my daughter's number by mistake. How do I undo it?

**ASSISTANT:**
No problem, you can unblock her. These steps are for the newest iPhone software, iOS 26.

1. Open **Settings** and tap **Privacy & Security**.
2. Tap **Blocked Contacts**.
3. Tap **Edit**.
4. Tap the delete button next to her number.
5. Tap **Unblock**.

## tr046-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Block a phone number (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/6325463?hl=en

**USER:**
Calls keep coming in on my Android phone that show up as Unknown with no number at all, so I can't pick one from my call history to block. Is there another way?

**ASSISTANT:**
Yes. You can block all unknown (private or unidentified) numbers.

1. Open the **Phone** app.
2. Tap **More**.
3. Tap **Settings**, then **Blocked numbers**.
4. Turn on **Unknown**.

Your phone will then decline calls from those numbers automatically. That covers every unknown caller, not only the one bothering you.

## tr046-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Block a phone number (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/6325463?hl=en

**USER:**
A telemarketer keeps ringing my Pixel phone. Show me how to block that number from my call history.

**ASSISTANT:**
You can block it from your call history.

1. Open the **Phone** app.
2. Tap **More**, then **Call history**.
3. Tap a call from the number you want to block.
4. Tap **Block / report spam**.

After that, your phone declines that number's calls automatically.

**USER:**
I think I blocked the wrong number. How do I undo it?

**ASSISTANT:**
You can unblock it.

1. Open the **Phone** app and tap **More**.
2. Tap **Settings**, then **Blocked numbers**.
3. Next to the number, tap **Clear**.
4. Tap **Unblock**.
