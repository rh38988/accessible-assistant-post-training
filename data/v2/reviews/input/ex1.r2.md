# Review input: batch ex1, round 2 (13 examples)

## pilot-001
- scenario: direct | style: plain | specification: fully_specified | platform: Samsung Galaxy (Android)
- task: Make text bigger (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/latin_en/support/mobile-devices/how-to-adjust-the-font-size-and-style-on-your-galaxy-phone/

**USER:**
the letters on my samsung phone are so tiny i cant read my messages. how do i make them bigger

**ASSISTANT:**
You can make the letters bigger in your phone's settings. It takes about a minute, and you can change it back anytime.

1. Find the **Settings** app and tap it.
2. Tap **Display**.
3. Tap **Font size and style**.
4. Adjust the options on that screen until the letters are easy to read.

Menu names can be a little different on some Samsung models. If you don't see **Font size and style** after tapping **Display**, tell me what you see and I'll help you find it.

## pilot-002
- scenario: missing_info | style: plain | specification: underspecified | platform: unknown
- task: Turn up ring volume (device unknown) (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9082609?hl=en

**USER:**
My phone hardly makes any sound when someone calls and I keep missing calls from my doctor's office.

**ASSISTANT:**
I'm sorry you've been missing those calls. I can help make the ringing louder.

Is your phone an **iPhone**, or another kind, like a Samsung or Google Pixel?

If you're not sure, tell me the name on the phone or box.

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
3. Tap the **Gallery** icon.
4. Tap the picture of your garden.
5. Tap the **Send** icon, the paper-plane shaped button.

If you don't see a Gallery icon, your phone may use a different messaging app. Tell me what icons you see next to the typing box and I'll guide you from there.

## pilot-004
- scenario: missing_info | style: plain | specification: underspecified | platform: iOS
- task: Take a screenshot (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/102616

**USER:**
How do I take a picture of what's on my iPhone screen? My grandson wants me to send him a screenshot.

**ASSISTANT:**
Happy to help. The buttons you press depend on your iPhone model, so one quick question first:

Do you know which iPhone model you have, for example **iPhone 8** or **iPhone 13**?

## pilot-005
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Email stopped working (details unknown) (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/7074871?hl=en

**USER:**
Good morning. I hope you can help me. My husband always took care of these things. Since about Tuesday my email is not working right. I used to get messages from my church group every day and now nothing. I tried turning it off and on.

**ASSISTANT:**
Good morning. I'm glad you asked, and we can figure this out together. Turning it off and on was a good first try.

So I can give you the right steps: **what is at the end of your email address**, for example @gmail.com or @yahoo.com?

## pilot-006
- scenario: missing_info | style: verbose | specification: underspecified | platform: unknown
- task: Printer will not print (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/fix-printer-connection-and-printing-problems-in-windows-fb830bff-7702-6349-33cd-9443fe987f73

**USER:**
My printer won't print anything and I need to print my boarding pass for Thursday. It worked fine last month. The little green light is on.

**ASSISTANT:**
Let's get that boarding pass printed. I'm glad the light is on.

The next steps depend on your computer. **Are you printing from a Windows computer?**

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
6. Confirm the connection.

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

1. Click the **Start** button (the Windows logo).
2. Click **Settings**. Its icon is a gear.
3. Click **Display**.
4. Under **Scale & layout**, open the **Scale** dropdown.
5. Choose a bigger percentage.

The screen will change size right away. Try a number, and if things are still too small, pick a bigger one.

If only the **words** are too small, there's another setting just for text. Tell me and I'll walk you through it. Some programs may look right only after you sign out and back in.

## pilot-009
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Internet not working (message cut off) (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-euro/111786

**USER:**
the internet on my

**ASSISTANT:**
It looks like your message got cut off, but I'd be glad to help with your internet.

**Which device is having trouble with the internet**, for example your phone, computer, or TV?

## pilot-010
- scenario: direct | style: plain | specification: fully_specified | platform: iOS
- task: Reset forgotten Apple Account password (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-mz/101567 ; https://support.apple.com/en-us/ht201487

**USER:**
I forgot my Apple ID password. I can still open my iPhone with my passcode. How do I make a new password?

**ASSISTANT:**
Good news: because you can still open your iPhone, you can make a new password right on the phone. (Apple calls this your Apple Account.)

1. Open the **Settings** app.
2. Tap **your name**.
3. Tap **Sign-In & Security**.
4. Tap **Change Password**.
5. Follow the instructions on the screen to set your new password.
6. If it asks, choose **Remove Other Devices** (other devices must sign in again) or **Keep All Devices Signed In**.

You may have to wait one hour before you can change it.

Write the new password down and keep it somewhere safe at home. Never give it to anyone who calls or texts you offering help with your account.

If **Change Password** doesn't appear, tell me what you see and I'll help with another way.

## pilot-011
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iOS
- task: Install a software update (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ie/118575

**USER:**
My iPhone keeps showing a message about a software update and I keep pressing Later because I'm afraid I'll lose my pictures of my grandchildren. Should I do it, and how?

**ASSISTANT:**
It's wise to be careful with your pictures. Updates are generally a good idea because they fix problems and keep your phone secure, and backing up first protects your photos.

**Before you start:**
1. Back up your iPhone with iCloud. If you're not sure whether it's backed up, ask me and I'll show you how to check.
2. Plug your iPhone into its charger.
3. Make sure you're connected to Wi-Fi.

**To update:**
4. Open **Settings**.
5. Tap **General**.
6. Tap **Software Update**.
7. Tap **Download and Install** (the button may say **Update Now**).
8. Follow the instructions on the screen (it may ask for your passcode).

If it says there isn't enough space, tap **Continue** to let it remove some apps for now. They come back by themselves after the update.

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

You'll see the file appear in your email. If the photo is bigger than 25 MB, Gmail puts a Google Drive link in the email instead.

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
2. Tap **your name** at the top.
3. Tap **iCloud**.
4. Tap **Photos**.
5. Turn on the switch next to **Sync this iPhone**.

Your photos will start saving to iCloud on their own. To see your photos in iCloud, open the **Photos** app and tap **Library**.
