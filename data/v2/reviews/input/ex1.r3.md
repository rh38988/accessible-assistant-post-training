# Review input: batch ex1, round 3 (6 examples)

## pilot-003
- scenario: direct | style: plain | specification: fully_specified | platform: Android (Google Messages)
- task: Send a photo by text message (Android (Google Messages)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/messages/answer/6159880?hl=en

**USER:**
I have an Android phone and use the Messages app. How do I text a picture of my garden to my sister?

**ASSISTANT:**
Here's how to send a picture in the Messages app. It takes less than a minute.

1. Open the **Messages** app.
2. Tap your conversation with your sister. If you haven't texted her before, start a new conversation with her.
3. Tap **Gallery**.
4. Tap the picture of your garden.
5. Tap **Send**.

If you don't see **Gallery**, tell me what you see on the screen and I'll guide you from there.

## pilot-007
- scenario: direct_messy | style: over_specified | specification: fully_specified | platform: iOS
- task: Connect to a Wi-Fi network (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-au/111107 ; https://support.apple.com/en-euro/111786

**USER:**
I'm staying at my daughter's house this weekend. She wrote the Wi-Fi name and password on a card for me. The network is called SmithHome. I have an iPhone 13 with the latest update. How do I get my phone on her internet?

**ASSISTANT:**
Here's how to connect your iPhone to SmithHome. Keep the card with the password nearby. This takes about two minutes.

1. Open the **Settings** app.
2. Tap **Wi-Fi**.
3. Make sure Wi-Fi is turned on.
4. Tap **SmithHome** in the list.
5. Type the password from the card if it asks.

When you're connected, you'll see a blue tick next to **SmithHome**, and the Wi-Fi icon at the top corner of the screen.

If you don't see SmithHome in the list, move closer to the internet box in her home and check again.

## pilot-008
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Make everything on screen bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

**USER:**
Everything on my laptop screen is too small. It has Windows 11. How do I make it all bigger?

**ASSISTANT:**
You can make everything on the screen bigger in Settings. It takes about two minutes, and you can change it back anytime.

1. Click the **Start** button.
2. Click **Settings**.
3. Click **Display**.
4. Under **Scale & layout**, open the **Scale** dropdown.
5. Choose a bigger percentage.

The screen will change size right away. Try a number, and if things are still too small, pick a bigger one.

If only the **words** are too small, there's another setting just for text. Tell me and I'll walk you through it. Some programs may look right only after you sign out and back in.

## pilot-010
- scenario: direct | style: plain | specification: fully_specified | platform: iOS
- task: Reset forgotten Apple Account password (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-mz/101567 ; https://support.apple.com/en-us/ht201487 ; https://support.apple.com/en-us/102568

**USER:**
I forgot my Apple ID password. I can still open my iPhone with my passcode. How do I make a new password?

**ASSISTANT:**
Good news: you can make a new password right on your iPhone if it is already signed in to your Apple Account with two-factor authentication. (Apple calls this your Apple Account.)

1. Open the **Settings** app.
2. Tap **your name**.
3. Tap **Sign-In & Security**.
4. Tap **Change Password**.
5. Follow the instructions on the screen to set your new password.
6. If it asks, choose **Remove Other Devices** (other devices must sign in again) or **Keep All Devices Signed In**.

You may have to wait one hour before you can change it.

Never give it to anyone who calls or texts you offering help with your account.

If **Change Password** doesn't appear, tell me what you see and I'll help with another way.

## pilot-012
- scenario: direct_messy | style: over_specified | specification: fully_specified | platform: Windows 11 (Gmail in Chrome)
- task: Attach a photo to an email (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/6584

**USER:**
I have a Dell computer with Windows 11 and I use Google Chrome to read my Gmail. I have a photo saved in my Pictures folder called birthday.jpg that I want to email to my son. I already know how to write the email, I just don't know how to add the photo.

**ASSISTANT:**
Since you already know how to write the email, here's just the part for adding the photo:

1. At the bottom of the message window, click the **Attach** icon.
2. Select the photo **birthday.jpg**. It is in your Pictures folder.
3. Click **Open**.

You'll see the file appear in your email. In a personal Gmail account, if the attachments are bigger than 25 MB in total, Gmail adds a Google Drive link to the email instead of the file.

## pilot-013
- scenario: followup | style: under_specified | specification: fully_specified | platform: iOS
- task: Back up photos (iPhone (iCloud Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/guide/icloud/mm7e90c1ba48

**USER:**
how do I back up my photos so I don't lose them?

**ASSISTANT:**
Happy to help you keep your photos safe. Are you using an **iPhone**, or a different kind of phone?

**USER:**
iPhone

**ASSISTANT:**
Great. Your iPhone can save your photos to iCloud, Apple's online storage, so they're safe even if the phone is lost or broken.

1. Open the **Settings** app.
2. Tap **your name**.
3. Tap **iCloud**.
4. Tap **Photos**.
5. Turn on the switch next to **Sync this iPhone**.

Your photos will start saving to iCloud on their own. To see your photos in iCloud, open the **Photos** app and tap **Library**.
