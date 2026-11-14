# Review input: batch ny1b, round 1 (36 examples)

## tr128-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Pair a Bluetooth accessory such as headphones or a speaker (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/HT204091

**USER:**
I just bought wireless headphones. How do I connect them to my iPhone?

**ASSISTANT:**
Here is how to pair them with your iPhone.

1. Turn your headphones on and put them in pairing mode. The headphone manual explains how.
2. On your iPhone, open **Settings**.
3. Tap **Bluetooth**, and make sure Bluetooth is turned on.
4. Under **My Devices**, look for your headphones.
5. Tap the name of your headphones when it appears.

If it asks for a PIN or passcode, the code is in the headphone manual or in the maker's online instructions.

## tr128-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Pair a Bluetooth accessory such as headphones or a speaker (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/HT204091

**USER:**
My grandson gave me a little Bluetooth speaker for my birthday and I want to play my music from my iPhone on it. It is in the box on the kitchen table and it has a light that blinks. I have never connected anything to my phone before. What do I do?

**ASSISTANT:**
Happy birthday! Connecting a speaker takes only a few taps.

1. Turn the speaker on and put it in pairing mode. The speaker's manual or online instructions show how.
2. On your iPhone, open **Settings**.
3. Tap **Bluetooth**, and turn Bluetooth on if it is off.
4. Under **My Devices**, look for your speaker.
5. Tap the speaker's name when it appears.

If it asks for a PIN or passcode, check the speaker's manual or online instructions for the code.

## tr128-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Pair a Bluetooth accessory such as headphones or a speaker (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/HT204091

**USER:**
my new earbuds wont hook up to my phone, what do i do

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr128-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Pair a Bluetooth accessory such as headphones or a speaker (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/HT204091

**USER:**
my new earbuds wont hook up to my phone, what do i do

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Here is how to pair your earbuds with your iPhone.

1. Turn your earbuds on and put them in pairing mode. Their manual explains how.
2. Open **Settings** on your iPhone.
3. Tap **Bluetooth**, and make sure Bluetooth is on.
4. Under **My Devices**, look for your earbuds.
5. Tap their name when it appears.

If it asks for a PIN or passcode, check the earbuds' manual or online instructions for the code.

## tr128-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Pair a Bluetooth accessory such as headphones or a speaker (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/HT204091

**USER:**
I am trying to connect a Bluetooth speaker to my iPhone and it is asking me for a PIN. I threw away the paper manual a long time ago and I have no idea what the number is. Where can I find it?

**ASSISTANT:**
You do not need the paper manual. The speaker's online instructions also give the code.

1. Look up your speaker's instructions online, and find the PIN or passcode.
2. On your iPhone, open **Settings**.
3. Tap **Bluetooth**.
4. Under **My Devices**, tap your speaker's name.
5. Enter the PIN or passcode when it asks.

If the code does not work, check the online instructions again for the right one.

## tr128-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Pair a Bluetooth accessory such as headphones or a speaker (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/HT204091

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

1. Make sure the headphones are turned on and charged.
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
2. Click the **Apple menu** at the top left of the screen, then choose **System Settings**.
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

## tr129-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Connect a Bluetooth device (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/guide/mac-help/blth1004/mac

**USER:**
My computer will not find my wireless mouse. How do I hook it up?

**ASSISTANT:**
I can help with that. Is your computer a **Mac** or a **Windows** PC?

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

If your mouse is an Apple Magic Mouse, you can instead plug it into your Mac with its cable and turn it on. It pairs by itself, and a notification tells you when to unplug it.

## tr129-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Mac
- task: Connect a Bluetooth device (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/guide/mac-help/blth1004/mac

**USER:**
My Bluetooth headphones are already set up on my Mac, they just are not connected right now. I do not want to dig through System Settings every time. Is there a quicker way to connect them?

**ASSISTANT:**
Yes, there is a quicker way.

1. Make sure your headphones are on.
2. Click the **Bluetooth** status icon in Control Center.
3. Select your headphones from the list.

If you ever want the longer way, open the **Apple menu**, choose **System Settings**, click **Bluetooth**, point at the headphones, and click **Connect**.

## tr129-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Mac
- task: Connect a Bluetooth device (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/guide/mac-help/blth1004/mac

**USER:**
Need to get my Bluetooth speaker working with my Mac, steps please

**ASSISTANT:**
Here is how to connect it.

1. Turn the speaker on and make it discoverable.
2. Click the **Apple menu**, then choose **System Settings**.
3. Click **Bluetooth** in the sidebar. You may need to scroll down.
4. Point at the speaker in the list and click **Connect**.
5. If a prompt appears, click **Accept**, or type the numbers shown and press Enter.

**USER:**
I opened System Settings but I cannot find Bluetooth anywhere in the sidebar.

**ASSISTANT:**
It may just be lower down the list. Try this.

1. In the System Settings sidebar, scroll down.
2. Click **Bluetooth** when you see it.
3. Point at your speaker in the list and click **Connect**.

If the speaker is not listed, check that it is on and discoverable.

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

If you do not see that option, your account may already use it. Most accounts do.

## tr130-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Turn on two-factor authentication for the Apple Account (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/102660

**USER:**
My son told me I should make my Apple ID safer by adding some extra code step when I sign in. I have an iPhone and I am not good with settings. I do not want to break anything. Can you tell me what to tap?

**ASSISTANT:**
That extra step is called two-factor authentication. Here is what to tap.

1. Open **Settings**.
2. Tap your name at the top.
3. Tap **Sign-In & Security**.
4. Tap **Turn on two-factor authentication**.
5. Follow the instructions on the screen.

Many accounts already have it turned on, so you may not need to do this.

## tr130-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on two-factor authentication for the Apple Account (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/102660

**USER:**
i want to turn on the extra security thing for my apple account

**ASSISTANT:**
I can help with that. Are you using an **iPhone**, an **iPad**, or a **Mac**?

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

## tr130-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Turn on two-factor authentication for the Apple Account (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/102660

**USER:**
I want to turn on two-factor authentication on my iPhone, but only if I can switch it off again later if it turns out to be too much hassle. Is that possible?

**ASSISTANT:**
Only for a short time. If you recently turned it on, you can lower your account security within two weeks of enrollment. If your account was created with two-factor authentication, Apple says this extra protection can't be removed.

If you still want to turn it on:

1. Open **Settings**.
2. Tap your name at the top.
3. Tap **Sign-In & Security**.
4. Tap **Turn on two-factor authentication**.
5. Follow the instructions on the screen.

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
That is likely because you do not need it. Most accounts already use two-factor authentication, so the option may not appear.

1. Open **Settings**.
2. Tap your name at the top.
3. Tap **Sign-In & Security**.

If your account was created with two-factor authentication, it is already on, and Apple says this extra protection can't be removed.

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

If your iPhone is on iOS 17 or earlier, open **Settings**, scroll down, and tap **Passwords** instead.

## tr131-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Find saved passwords in the Passwords app and keep them in sync with iCloud Keychain (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/104955

**USER:**
I have an old iPhone that is on iOS 17 and I forgot my password for my bank's website but I know my phone saved it at some point. I do not see any Passwords app on it. How do I look it up?

**ASSISTANT:**
On iOS 17, your passwords are in Settings.

1. Open **Settings**.
2. Scroll down and tap **Passwords**.
3. Unlock it with Face ID, Touch ID, or your passcode.
4. Tap the website or app you want. Your password appears.

If you cannot find it, check that you are looking at the main **Passwords** list. Then look in **Recently Deleted**.

## tr131-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Find saved passwords in the Passwords app and keep them in sync with iCloud Keychain (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/104955

**USER:**
where does my phone keep the passwords it saved for me

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr131-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Find saved passwords in the Passwords app and keep them in sync with iCloud Keychain (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/104955

**USER:**
where does my phone keep the passwords it saved for me

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
On an iPhone, saved passwords are in the Passwords app.

1. Open the **Passwords** app.
2. Unlock it with Face ID, Touch ID, or your passcode.
3. Tap **All**.
4. Tap the website or app you want. Your password appears.

If your iPhone is on iOS 17 or earlier, open **Settings**, scroll down, and tap **Passwords** instead.

## tr131-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Find saved passwords in the Passwords app and keep them in sync with iCloud Keychain (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/104955

**USER:**
I have an iPhone and an iPad. My passwords show up on my iPad but not on my iPhone, and I do not want to type them all in again by hand. How do I get them onto my iPhone?

**ASSISTANT:**
You can let them sync with iCloud Keychain. Do this on your iPhone.

1. Open **Settings**.
2. Tap your name at the top.
3. Tap **iCloud**.
4. Tap **Passwords and Keychain**.
5. Turn on **iCloud Keychain**.

Also check that iCloud Keychain is on the same way on your iPad. If your iPhone is a newer device, you may need to approve it first, using iCloud Keychain or the passcode of your old device.

## tr131-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Find saved passwords in the Passwords app and keep them in sync with iCloud Keychain (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-us/104955

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
3. If you use more than one Apple device, open **Settings**, tap your name, tap **iCloud**, tap **Passwords and Keychain**, and make sure **iCloud Keychain** is on.

If the password was moved to a Shared Group, your iPhone needs iOS 17 or later to see it.

## tr132-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPad
- task: iPad is frozen or will not respond (iPad) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/kb/HT212017

**USER:**
My iPad has no Home button and the screen is frozen. Nothing happens when I touch it. What should I do?

**ASSISTANT:**
You can force it to restart.

1. Press and quickly let go of the volume button closest to the top button.
2. Press and quickly let go of the volume button farthest from the top button.
3. Press and hold the top button until the Apple logo appears.

If the iPad still will not turn on, charge it. Charging can take up to an hour.

## tr132-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPad
- task: iPad is frozen or will not respond (iPad) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/kb/HT212017

**USER:**
My iPad is the older kind with the round Home button under the screen. I was reading and it just stopped. The screen is on but nothing moves and it will not respond to anything. I tried holding the top button and it did not do anything. Help please.

**ASSISTANT:**
You can force it to restart. On an iPad with a Home button, use two buttons together.

1. Press and hold the **Home button** and the **top button** at the same time.
2. Keep holding both until the Apple logo appears.

If the iPad still will not turn on, charge it. Charging can take up to an hour.

## tr132-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: iPad
- task: iPad is frozen or will not respond (iPad) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/kb/HT212017

**USER:**
my ipad is frozen and wont do anything

**ASSISTANT:**
I can help with that. Does your iPad have a **Home button**, or **no Home button**?

## tr132-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPad
- task: iPad is frozen or will not respond (iPad) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/kb/HT212017

**USER:**
my ipad is frozen and wont do anything

**ASSISTANT:**
I can help with that. Does your iPad have a **Home button**, or **no Home button**?

**USER:**
no home button

**ASSISTANT:**
Here is how to force restart an iPad with no Home button.

1. Press and quickly let go of the volume button closest to the top button.
2. Press and quickly let go of the volume button farthest from the top button.
3. Press and hold the top button until the Apple logo appears.

If the iPad still will not turn on, charge it. Charging can take up to an hour.

## tr132-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPad
- task: iPad is frozen or will not respond (iPad) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/kb/HT212017

**USER:**
My iPad has no Home button and it is frozen. I have arthritis in my hands, so I cannot hold two buttons down at the same time. Is there a way to restart it without that?

**ASSISTANT:**
Yes. On an iPad with no Home button, you press the buttons one at a time.

1. Press and quickly let go of the volume button closest to the top button.
2. Press and quickly let go of the volume button farthest from the top button.
3. Press and hold the top button until the Apple logo appears.

You only hold one button, the top button, at the end.

## tr132-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPad
- task: iPad is frozen or will not respond (iPad) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/kb/HT212017

**USER:**
My iPad with no Home button is frozen. How do I force restart it?

**ASSISTANT:**
Here is how.

1. Press and quickly let go of the volume button closest to the top button.
2. Press and quickly let go of the volume button farthest from the top button.
3. Press and hold the top button until the Apple logo appears.

**USER:**
I did it and held the top button but the screen stayed black. No Apple logo came up.

**ASSISTANT:**
The iPad may be out of battery, so charge it.

1. Plug the iPad into its charger and let it charge. Charging can take up to an hour.
2. After it has charged, try the force restart steps again.

If it still does not turn on, you may need to get it serviced by Apple.

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
3. Tap the **Delete** button, the trash can icon.
4. Tap **Delete and Report Spam**.

Reporting does not stop the sender from texting you. To stop them, block the contact.

## tr133-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Report and block junk text messages (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios

**USER:**
Every day I get texts on my iPhone from some random number trying to sell me things and I am sick of it. I have not opened the latest one. I want to report it and also make them stop. What exactly do I tap?

**ASSISTANT:**
Reporting alone will not stop them, so do both. First, block the sender.

1. Open the **Messages** app.
2. Open the conversation with the sender and tap the person's icon at the top.
3. Tap **Info**.
4. Scroll down and tap **Block Contact**.

Then report the message.

1. In the **Messages** list, swipe left on the message.
2. Tap the **Delete** button, the trash can icon.
3. Tap **Delete and Report Spam**.

## tr133-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Report and block junk text messages (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios

**USER:**
how do i report and block junk texts

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

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
On an iPhone, block first so the sender cannot text you again.

1. Open the **Messages** app.
2. Open the conversation with the sender and tap the person's icon at the top.
3. Tap **Info**.
4. Scroll down and tap **Block Contact**.

Then report it.

1. In the **Messages** list, swipe left on the message.
2. Tap the **Delete** button, the trash can icon.
3. Tap **Delete and Report Spam**.

## tr133-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Report and block junk text messages (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios

**USER:**
A stranger texted my iPhone and I already wrote back to ask who they were. Now they keep texting. Can I still report them as spam?

**ASSISTANT:**
No, you cannot report a message after you have replied to it. You can still block them, which stops their messages from reaching you.

1. Open the **Messages** app.
2. Open the conversation with the sender and tap the person's icon at the top.
3. Tap **Info**.
4. Scroll down and tap **Block Contact**.

The sender does not know they have been blocked.

## tr133-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Report and block junk text messages (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios

**USER:**
I opened a junk text on my iPhone. How do I report it?

**ASSISTANT:**
Here is how to report it.

1. Open the **Messages** app and open the message.
2. Tap the **Report Spam** link at the bottom of the message.
3. Tap **Delete and Report Spam**.

Reporting does not stop the sender. To stop them, block the contact.

**USER:**
There is no Report Spam link at the bottom of my message.

**ASSISTANT:**
The link only appears for messages from unknown senders, and you cannot report a message you have replied to. For SMS, MMS, or RCS messages without this option, contact your carrier.

You can still block the sender.

1. Open the **Messages** app.
2. Open the conversation and tap the person's icon at the top.
3. Tap **Info**.
4. Scroll down and tap **Block Contact**.
