# Review input: batch ny1b, round 2 (14 examples)

## tr128-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Pair a Bluetooth accessory such as headphones or a speaker (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/HT204091

**USER:**
I am trying to connect a Bluetooth speaker to my iPhone and it is asking me for a PIN. I threw away the paper manual a long time ago and I have no idea what the number is. Where can I find it?

**ASSISTANT:**
You do not need the paper manual. The speaker's online instructions also give the code.

1. Look up your speaker's online instructions, and find the PIN or passcode.
2. Go back to the pairing prompt on your iPhone and enter the PIN or passcode.

If the prompt has closed, open **Settings**, tap **Bluetooth**, tap your speaker's name under **My Devices**, and enter the code.

If the code does not work, check the online instructions again for the right one.

## tr128-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Pair a Bluetooth accessory such as headphones or a speaker (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/HT204091 ; https://support.apple.com/en-us/111804

**USER:**
Could you tell me the way to pair some Bluetooth headphones with an iPhone?

**ASSISTANT:**
Here is how to pair them.

1. Turn your headphones on and put them in pairing mode.
2. On your iPhone, open **Settings**.
3. Tap **Bluetooth**, and make sure Bluetooth is on.
4. Under **My Devices**, look for your headphones.
5. Tap their name when it appears.

If it asks for a PIN or passcode, check the headphone manual for the code.

**USER:**
I did all that but my headphones are not showing up in the list under My Devices.

**ASSISTANT:**
That usually means the headphones are not ready to be found yet. Try this.

1. Make sure the headphones are turned on and charged, and keep them close to your iPhone.
2. Put them in discoverable (pairing) mode again. The headphone manual or online instructions explain how.
3. Go back to **Settings**, then **Bluetooth**, and look under **My Devices** again.
4. Tap their name when it appears.

## tr129-a
- scenario: direct | style: plain | specification: fully_specified | platform: Mac
- task: Connect a Bluetooth device (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/guide/mac-help/blth1004/mac

**USER:**
How do I connect my Bluetooth headphones to my Mac?

**ASSISTANT:**
Here is how to connect them to your Mac.

1. Turn your headphones on and make them discoverable. The headphone manual explains how.
2. Click the **Apple menu**, then choose **System Settings**.
3. In the sidebar, click **Bluetooth**. You may need to scroll down to find it.
4. Point at your headphones in the list and click **Connect**.
5. If a prompt appears, click **Accept**, or type the numbers it shows and press Enter.

If your headphones are not in the list, check that they are on and discoverable.

## tr129-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Mac
- task: Connect a Bluetooth device (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/guide/mac-help/blth1004/mac

**USER:**
I have a MacBook and a new Bluetooth speaker. I want to connect it and then actually hear my music coming out of the speaker instead of the laptop. I connected it once but the sound still comes out of the laptop. Can you walk me through the whole thing?

**ASSISTANT:**
Yes. First connect the speaker, then tell your Mac to play sound through it.

1. Turn the speaker on and make it discoverable. Its manual explains how.
2. Click the **Apple menu**, then choose **System Settings**.
3. Click **Bluetooth** in the sidebar. You may need to scroll down.
4. Point at your speaker in the list and click **Connect**.
5. If a prompt appears, click **Accept**, or type the numbers shown and press Enter.
6. Back in the sidebar, click **Sound**. You may need to scroll down.
7. Click **Output**.
8. Select your speaker from the list.

Now your music should play through the speaker.

## tr129-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Mac
- task: Connect a Bluetooth device (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/guide/mac-help/blth1004/mac

**USER:**
My computer will not find my wireless mouse. How do I hook it up?

**ASSISTANT:**
I can help with that. Is your computer a **Mac** or a **Windows** PC?

**USER:**
Mac

**ASSISTANT:**
Here is how to connect a Bluetooth mouse to your Mac.

1. Turn the mouse on and make it discoverable. Its manual explains how.
2. Click the **Apple menu**, then choose **System Settings**.
3. Click **Bluetooth** in the sidebar. You may need to scroll down.
4. Point at your mouse in the list and click **Connect**.
5. If a prompt appears, click **Accept**, or type the numbers it shows and press Enter.

If your mouse is an Apple Magic Mouse, you can use a cable instead: plug it into your Mac's USB-C port (you may need an adapter), turn the mouse on and check that its power switch shows green. When a notification appears, you can unplug the cable and use the mouse wirelessly.

## tr130-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Turn on two-factor authentication for the Apple Account (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/102660

**USER:**
How do I turn on two-factor authentication for my Apple Account on my iPhone?

**ASSISTANT:**
Here is how to turn it on.

1. Open **Settings** on your iPhone.
2. Tap your name at the top.
3. Tap **Sign-In & Security**.
4. Tap **Turn on two-factor authentication**.
5. Follow the instructions on the screen.

Most accounts already use two-factor authentication, so you may not need to do this.

## tr130-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Turn on two-factor authentication for the Apple Account (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/102660

**USER:**
i want to turn on the extra security thing for my apple account

**ASSISTANT:**
I can help with that. Are you using an **iPhone**, an **iPad**, or a **Mac**?

**USER:**
iphone

**ASSISTANT:**
Here is how to do it on your iPhone.

1. Open **Settings**.
2. Tap your name at the top.
3. Tap **Sign-In & Security**.
4. Tap **Turn on two-factor authentication**.
5. Follow the instructions on the screen.

Most accounts already use two-factor authentication, so you may not need to do this.

## tr130-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Turn on two-factor authentication for the Apple Account (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/102660

**USER:**
Please show me how to switch on two-factor authentication on my iPhone for my Apple Account

**ASSISTANT:**
Here is how to turn it on.

1. Open **Settings**.
2. Tap your name at the top.
3. Tap **Sign-In & Security**.
4. Tap **Turn on two-factor authentication**.
5. Follow the instructions on the screen.

**USER:**
I went there but I do not see Turn on two-factor authentication anywhere.

**ASSISTANT:**
Most accounts already use two-factor authentication, so you may not need to turn it on. To check:

1. Open **Settings**.
2. Tap your name at the top.
3. Tap **Sign-In & Security**.

If your account was created with two-factor authentication, Apple says this extra protection can't be removed.

## tr131-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Find saved passwords in the Passwords app and keep them in sync with iCloud Keychain (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/104955

**USER:**
Where can I see my saved passwords on my iPhone? It has the newest iOS.

**ASSISTANT:**
Your saved passwords are in the Passwords app.

1. Open the **Passwords** app.
2. Unlock it with Face ID, Touch ID, or your passcode.
3. Tap **All**, or choose another category.
4. Tap the website or app you want. Your password appears.

## tr131-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Find saved passwords in the Passwords app and keep them in sync with iCloud Keychain (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/104955 ; https://support.apple.com/en-us/109016

**USER:**
I have an iPhone and an iPad. My passwords show up on my iPad but not on my iPhone, and I do not want to type them all in again by hand. How do I get them onto my iPhone?

**ASSISTANT:**
You can let them sync with iCloud Keychain. Do this on your iPhone.

1. Open **Settings**.
2. Tap your name at the top.
3. Tap **iCloud**.
4. Under **Saved to iCloud**, tap **Passwords**. On iOS 17 or earlier, tap **Passwords and Keychain**.
5. Turn on **Sync this iPhone**. You may need your passcode or Apple Account password.

Do the same on your iPad. Two-factor authentication must also be on for your Apple Account.

## tr131-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Find saved passwords in the Passwords app and keep them in sync with iCloud Keychain (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/104955 ; https://support.apple.com/en-us/109016

**USER:**
How do I find a saved password on my iPhone? It is on iOS 18.

**ASSISTANT:**
Here is how to find it.

1. Open the **Passwords** app.
2. Unlock it with Face ID, Touch ID, or your passcode.
3. Tap **All**, or choose another category.
4. Tap the website or app you want. Your password appears.

**USER:**
I looked but the website I need is not in the list.

**ASSISTANT:**
Try these checks.

1. In the Passwords app, tap **All**, so you are looking at everything.
2. Tap **Deleted**, in case the password was removed.
3. If you use more than one Apple device, open **Settings**, tap your name, tap **iCloud**, and under **Saved to iCloud** tap **Passwords**. Make sure **Sync this iPhone** is on.

If the password was moved to a Shared Group, your iPhone needs iOS 17 or later to see it.

## tr133-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Report and block junk text messages (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios

**USER:**
I got a junk text on my iPhone from a number I do not know and I have not opened it. How do I report it?

**ASSISTANT:**
You can report it without opening it.

1. Open the **Messages** app.
2. Swipe left on the junk message.
3. Tap the **Delete** button.
4. Tap **Delete and Report Spam**.

Reporting does not stop the sender from texting you. To stop them, block the contact.

## tr133-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Report and block junk text messages (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios

**USER:**
Every day I get texts on my iPhone from some random number trying to sell me things and I am sick of it. I have not opened the latest one. I want to report it and also make them stop. What exactly do I tap?

**ASSISTANT:**
Reporting alone will not stop them, so do both. First, report the message.

1. Open the **Messages** app.
2. In the **Messages** list, swipe left on the message.
3. Tap the **Delete** button.
4. Tap **Delete and Report Spam**.

Now block them.

1. Open the conversation with the sender and tap the person's icon at the top.
2. Tap **Info**.
3. Scroll down and tap **Block Contact**.

## tr133-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Report and block junk text messages (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios

**USER:**
how do i report and block junk texts

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iphone

**ASSISTANT:**
On an iPhone, reporting does not stop the sender, so report first and block them afterwards.

1. Open the **Messages** app.
2. In the **Messages** list, swipe left on the message.
3. Tap the **Delete** button.
4. Tap **Delete and Report Spam**.

If you already opened it, open the message, tap **Report Spam** at the bottom, then tap **Delete and Report Spam**.

Now block them.

1. Open the conversation with the sender and tap the person's icon at the top.
2. Tap **Info**.
3. Scroll down and tap **Block Contact**.
