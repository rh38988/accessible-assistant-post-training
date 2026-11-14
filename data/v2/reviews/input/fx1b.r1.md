# Review input: batch fx1b, round 1 (34 examples)

## tr007-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Connect to a Wi-Fi network (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-au/111107

**USER:**
How do I connect my iPhone to the wifi at my house? I know the password.

**ASSISTANT:**
Here is how to connect your iPhone to your home Wi-Fi.

1. Open **Settings**.
2. Tap **Wi-Fi**.
3. Turn on **Wi-Fi** if it is off. Your iPhone will look for networks by itself.
4. Tap the name of your home network.
5. Type the password if it asks for it.

When it worked, you will see a blue checkmark next to the network name and the Wi-Fi symbol at the top corner of the screen.

## tr007-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Connect to a Wi-Fi network (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-au/111107

**USER:**
my son said to get on the wifi at his place. how do i do that on my phone

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr007-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Connect to a Wi-Fi network (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-au/111107

**USER:**
my son said to get on the wifi at his place. how do i do that on my phone

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Thank you. Here is how to join your son's Wi-Fi on your iPhone. Have the password handy.

1. Open **Settings**.
2. Tap **Wi-Fi**.
3. Turn on **Wi-Fi** if it is off.
4. Tap the name of your son's network in the list.
5. Type the password if it asks for it. It may also ask you to agree to terms and conditions.

When you are connected, you will see a blue checkmark next to the network name and the Wi-Fi symbol at the top corner of the screen.

## tr007-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Connect to a Wi-Fi network (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-au/111107

**USER:**
I'm at the community center with my iPhone and they have free wifi, but nobody gave me a password and I don't want to go bother the front desk if there's another way around it. Can you just connect me?

**ASSISTANT:**
I can show you the steps, but the network may ask for a password or for you to agree to terms and conditions.

1. Open **Settings**.
2. Tap **Wi-Fi**.
3. Turn on **Wi-Fi** if it is off.
4. Tap the name of the community center network.
5. If it asks you to agree to terms and conditions, agree to them.

If it asks for a password, I can't get around that. You will need to ask the network administrator for it. Once you are connected, you will see a blue checkmark next to the network name.

## tr008-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: Windows 11
- task: Make everything on screen bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

**USER:**
My Windows 11 laptop is hard for me to read, can you make it bigger?

**ASSISTANT:**
I can help with that. Do you want just the **words** bigger, or **everything** on the screen, including pictures and programs?

## tr008-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Make everything on screen bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

**USER:**
My Windows 11 laptop is hard for me to read, can you make it bigger?

**ASSISTANT:**
I can help with that. Do you want just the **words** bigger, or **everything** on the screen, including pictures and programs?

**USER:**
just the words

**ASSISTANT:**
Here is how to make just the words bigger on Windows 11.

1. Click **Start**, then click **Settings**.
2. Click **Accessibility**.
3. Click **Text size**.
4. Drag the **Text size** slider to the right. The sample text gets bigger.
5. Click **Apply**.

Windows will make the text bigger on title bars, menus, and icon labels.

## tr008-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Make everything on screen bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

**USER:**
My eyes aren't what they used to be. I'm on a Windows 11 computer. The pictures and the windows are fine, it's the writing under the little icons and the menus at the top that I can barely read. I don't want to change the whole screen, only the writing. What do I do?

**ASSISTANT:**
You can make only the writing bigger, and leave the pictures and windows as they are.

1. Press the **Windows logo key** and the **U** key together. This opens Accessibility settings.
2. Click **Text size**.
3. Drag the **Text size** slider to the right until the sample text looks easy to read.
4. Click **Apply**.

Windows will make the text bigger on title bars, menus, and icon labels.

If the Windows logo key and U do not work, click **Start**, click **Settings**, then click **Accessibility**.

## tr008-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Make everything on screen bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

**USER:**
Everything on my Windows 11 screen is too small, the pictures, the programs, all of it. I'd like the fastest way, I heard there is a key I can press so I don't have to click around the Start menu. Is there?

**ASSISTANT:**
Yes. A key shortcut opens Settings directly.

1. Press the **Windows logo key** and the **I** key together. Settings opens.
2. Click **Display**.
3. Under **Scale & layout**, click the **Scale** menu.
4. Choose a bigger option from the list.

Scale makes everything on the screen bigger, including pictures and programs. Most changes show up right away.

## tr008-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Make everything on screen bigger (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64

**USER:**
Please help me make everything bigger on my Windows 11 laptop screen.

**ASSISTANT:**
Here is how to make everything on the screen bigger.

1. Click **Start**, then click **Settings**.
2. Click **Display**.
3. Under **Scale & layout**, click the **Scale** menu.
4. Choose a bigger option.

Most changes show up right away.

**USER:**
Most of it got bigger but one program still looks tiny.

**ASSISTANT:**
Some programs only show the change after you sign out and sign back in.

1. Save your work in your programs.
2. Sign out of Windows.
3. Sign back in and open the program again.

## tr009-a
- scenario: direct | style: plain | specification: fully_specified | platform: iOS
- task: Internet not working (message cut off) (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-euro/111786

**USER:**
My iPhone won't get on the internet at home. The wifi at home is the only thing I use. What should I check?

**ASSISTANT:**
Let's check a few things on your iPhone. Stop when it works.

1. Open **Settings**, then tap **Wi-Fi**. Make sure **Wi-Fi** is turned on.
2. Tap the name of your home network. Look for a blue checkmark next to it.
3. If it still does not work, go back to **Settings** and make sure **Airplane Mode** is off.
4. Tap **Wi-Fi** again and make sure **Connectivity Assist** is off.

If you still see **No Internet Connection**, the problem may be with your router. Check your router and network settings.

## tr009-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iOS
- task: Internet not working (message cut off) (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-euro/111786

**USER:**
Last week my grandson put a VPN app on my iPhone so I could watch shows from home. Ever since then my phone says it's connected to the wifi but nothing loads. The wifi worked fine before that and my other devices are fine too. What do I do?

**ASSISTANT:**
The VPN app may be getting in the way. Try this.

1. Uninstall the VPN app.
2. Restart your iPhone.
3. Test your Wi-Fi connection again.

If that fixes it, you know the app was the cause. If you need to keep the app, contact whoever manages your VPN or the company that makes the app.

## tr009-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iOS
- task: Internet not working (message cut off) (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-euro/111786

**USER:**
the internet on my

**ASSISTANT:**
It looks like your message got cut off, but I'd be glad to help with your internet.

**Which device is having trouble** (for example your phone, computer, or TV), and **what happens when you try to go online?**

**USER:**
my iPhone, it won't connect to the wifi at home

**ASSISTANT:**
Thank you. Let's check your iPhone. Stop when it connects.

1. Open **Settings**, then tap **Wi-Fi**. Make sure **Wi-Fi** is turned on.
2. Tap the name of your home network. Look for a blue checkmark.
3. If it still won't connect, go back to **Settings** and make sure **Airplane Mode** is off.
4. Tap **Wi-Fi** again and make sure **Connectivity Assist** is off.

If you still see **No Internet Connection**, check your router and network settings.

## tr009-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iOS
- task: Internet not working (message cut off) (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-euro/111786

**USER:**
My iPhone says it's on the wifi but I can't get any web pages. The password to my wifi is written down somewhere I can't find, so please don't have me do anything that would make me forget the wifi and type the password again. What can I do?

**ASSISTANT:**
You can try these without losing your saved Wi-Fi password. Do not use **Reset Network Settings**, because it removes your saved Wi-Fi networks and passwords.

1. See if other devices, like a tablet or another phone, can get online on the same network. If they can, the router is working.
2. Make sure the router is on and close to you.
3. Unplug the router and the cable modem, then plug them back in.
4. If other devices cannot get online either, there may be an outage. Contact your internet service provider.

## tr009-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iOS
- task: Internet not working (message cut off) (unknown) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-euro/111786

**USER:**
My iPhone will not connect to my home wifi. Please tell me what to try.

**ASSISTANT:**
Let's check a few things on your iPhone.

1. Open **Settings**, then tap **Wi-Fi**. Make sure **Wi-Fi** is turned on.
2. Tap your home network name. Look for a blue checkmark.
3. If it still does not work, go back to **Settings** and make sure **Airplane Mode** is off.
4. Tap **Wi-Fi** again and make sure **Connectivity Assist** is off.

**USER:**
The wifi setting is gray and I can't tap it.

**ASSISTANT:**
When the Wi-Fi setting is grayed out, the fix is to restart your iPhone.

1. Restart your iPhone.
2. Open **Settings** and tap **Wi-Fi** again.
3. Tap your home network name and look for a blue checkmark.

If it still will not connect to any Wi-Fi network, contact Apple.

## tr010-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Reset forgotten Apple Account password (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-mz/101567

**USER:**
I need to change my Apple ID password

**ASSISTANT:**
I can help with that. Which device are you using: an **iPhone or iPad**, a **Mac**, or a **web browser** on a computer?

## tr010-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPad
- task: Reset forgotten Apple Account password (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-mz/101567

**USER:**
I need to change my Apple ID password

**ASSISTANT:**
I can help with that. Which device are you using: an **iPhone or iPad**, a **Mac**, or a **web browser** on a computer?

**USER:**
my iPad

**ASSISTANT:**
Here is how to change your Apple Account password on your iPad.

1. Open **Settings**.
2. Tap **your name** at the top.
3. Tap **Sign-In & Security**.
4. Tap **Change Password**.
5. Follow the instructions on the screen.
6. If other devices are signed in, choose **Remove Other Devices** or **Keep All Devices Signed In**.

If it asks you to wait about an hour, that is a security feature called Stolen Device Protection.

## tr010-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: web
- task: Reset forgotten Apple Account password (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-mz/101567

**USER:**
My nephew told me I should change my Apple ID password every so often. I'm at my computer at the library and I only have the internet browser, no Apple stuff on this machine. Is there a way to do it on a website?

**ASSISTANT:**
Yes, you can do it on the Apple website.

1. Go to **account.apple.com** and sign in.
2. Go to **Sign-In and Security**.
3. Choose **Password**.

If you have an Apple device you trust, the website may send you to that device to finish. That is normal. The website may only let you change the password itself if you have no trusted device.

## tr010-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iOS
- task: Reset forgotten Apple Account password (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-mz/101567

**USER:**
I want to change my Apple Account password on my iPhone, but my wife uses the iPad that is signed in with my account too and I don't want her kicked out of it while I change it. Can I do that?

**ASSISTANT:**
Yes. You can choose to keep your other devices signed in.

1. Open **Settings** and tap **your name** at the top.
2. Tap **Sign-In & Security**.
3. Tap **Change Password**.
4. Follow the instructions on the screen.
5. When it asks about other signed in devices, choose **Keep All Devices Signed In**.

Do not choose **Remove Other Devices**, because that makes the iPad sign in again.

## tr010-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iOS
- task: Reset forgotten Apple Account password (iPhone) | sensitive: True | reviewed by a person: False
- sources: https://support.apple.com/en-mz/101567

**USER:**
Please walk me through changing my Apple Account password on my iPhone.

**ASSISTANT:**
Here is how to change it on your iPhone.

1. Open **Settings** and tap **your name**.
2. Tap **Sign-In & Security**.
3. Tap **Change Password**.
4. Follow the instructions on the screen.
5. If other devices are signed in, choose **Remove Other Devices** or **Keep All Devices Signed In**.

**USER:**
It says I have to wait an hour before I can change it. Is something wrong?

**ASSISTANT:**
Nothing is wrong. You might have to wait one hour before changing your password because of a security feature called Stolen Device Protection.

1. Wait one hour.
2. Then open **Settings**, tap **your name**, tap **Sign-In & Security**, and tap **Change Password** again.

## tr011-a
- scenario: direct | style: plain | specification: fully_specified | platform: iOS
- task: Install a software update (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ie/118575

**USER:**
My iPhone says iOS has something new to install. What do I press to get it on there?

**ASSISTANT:**
Here is how to update your iPhone.

1. Back up your iPhone using iCloud or your computer.
2. Plug your iPhone into a power source.
3. Connect your iPhone to Wi-Fi.
4. Open **Settings**.
5. Tap **General**.
6. Tap **Software Update**. It shows whether an update is available.
7. Tap **Download and Install**.
8. Follow the instructions on the screen.

If you see a message about space, tap **Continue** to let your iPhone temporarily remove some apps. They are put back by themselves afterward.

## tr011-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Install a software update (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ie/118575

**USER:**
my phone says there is a new update. how do i put it on

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr011-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iOS
- task: Install a software update (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ie/118575

**USER:**
my phone says there is a new update. how do i put it on

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iphone

**ASSISTANT:**
Here is how to put the update on your iPhone.

1. Back up your iPhone using iCloud or your computer.
2. Plug your iPhone into a power source and connect it to Wi-Fi.
3. Open **Settings**.
4. Tap **General**.
5. Tap **Software Update**.
6. Tap **Download and Install**.
7. Follow the instructions on the screen.

If you do not see the update on your phone, you can update using a computer instead.

## tr011-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iOS
- task: Install a software update (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ie/118575

**USER:**
I always forget to update my iPhone and I don't want to sit and watch it while it updates. I'd like it to just happen at night while I'm asleep and the phone is on the charger. Can it?

**ASSISTANT:**
Yes, you can turn on automatic updates.

1. Open **Settings**.
2. Tap **General**.
3. Tap **Software Update**.
4. Tap **Automatic Updates**.
5. Turn on **Automatically Install**.

Your iPhone will then download and install updates overnight while it is charging and on Wi-Fi. It will notify you before it installs.

## tr011-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iOS
- task: Install a software update (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ie/118575

**USER:**
Show me how to install the newest update on my iPhone please.

**ASSISTANT:**
Here is how to update your iPhone.

1. Back up your iPhone using iCloud or your computer.
2. Plug it into a power source and connect to Wi-Fi.
3. Open **Settings**, tap **General**, then tap **Software Update**.
4. Tap **Download and Install**.
5. Follow the instructions on the screen.

**USER:**
It says there isn't enough space. Now what?

**ASSISTANT:**
You have two choices.

1. Tap **Continue** to let your iPhone temporarily remove some apps. They are put back by themselves after the update.
2. Or tap **Cancel** and delete some things yourself to free up space.

## tr012-a
- scenario: direct | style: plain | specification: fully_specified | platform: Gmail (computer)
- task: Attach a photo to an email (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/6584

**USER:**
How do I put a picture in an email in Gmail on my computer?

**ASSISTANT:**
Here is how to add a picture to your email in Gmail on a computer.

1. Go to Gmail in your browser.
2. Click **Compose**.
3. At the bottom of the email window, click **Attach**.
4. Choose the picture you want to send.
5. Click **Open**.

If the picture is too big for a personal Gmail account (over 25 MB), Gmail removes it and puts it in the email as a Google Drive link instead.

## tr012-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Attach a photo to an email (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/6584

**USER:**
want to email my grandson a snapshot, where do I start

**ASSISTANT:**
I can help with that. Are you using **Gmail** on a computer, or a different email program?

## tr012-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Gmail (computer)
- task: Attach a photo to an email (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/6584

**USER:**
want to email my grandson a snapshot, where do I start

**ASSISTANT:**
I can help with that. Are you using **Gmail** on a computer, or a different email program?

**USER:**
gmail on my computer

**ASSISTANT:**
Here is how to send a picture in Gmail on your computer.

1. Go to Gmail in your browser.
2. Click **Compose**.
3. At the bottom of the email window, click **Attach**.
4. Choose the picture you want to send.
5. Click **Open**.

If the picture is very large, Gmail may add it to the email as a Google Drive link instead of attaching it.

## tr012-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Gmail (computer)
- task: Attach a photo to an email (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/6584

**USER:**
I'm writing an email in Gmail on my computer and my picture is already showing in a folder on the screen next to it. The little buttons at the bottom are hard for me to hit with my shaky hand. Can I just pull the picture over into the email instead of using the button?

**ASSISTANT:**
Yes, you can add the picture by dragging it.

1. Click the picture in the folder window and hold the mouse button down.
2. Drag it into your email window.
3. Let go of the mouse button.

If dragging is hard, the other way is the **Attach** button at the bottom of the email window.

## tr012-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Gmail (computer)
- task: Attach a photo to an email (Gmail (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/6584

**USER:**
Show me how to attach a photo in Gmail on my computer please.

**ASSISTANT:**
Here is how to attach a photo in Gmail on your computer.

1. Go to Gmail in your browser.
2. Click **Compose**.
3. At the bottom of the email window, click **Attach**.
4. Choose the photo you want.
5. Click **Open**.

**USER:**
I picked the wrong photo and it's in the email now. How do I take it out?

**ASSISTANT:**
You can remove it easily.

1. Find the photo's name in your email.
2. Click **Close** to the right of the photo's name.

Then use **Attach** again to add the right photo.

## tr013-a
- scenario: direct | style: plain | specification: fully_specified | platform: iOS
- task: Back up photos (iPhone (iCloud Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/guide/icloud/mm7e90c1ba48

**USER:**
I have an iPhone. How do I turn on iCloud Photos so my pictures are saved online?

**ASSISTANT:**
Here is how to turn on iCloud Photos on your iPhone.

1. Open **Settings**.
2. Tap **your name** at the top.
3. Tap **iCloud**.
4. Tap **Photos**.
5. Turn on **Sync this iPhone**.

Your photos and videos are then added to iCloud. To see them, open the **Photos** app and tap **Library**.

## tr013-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Back up photos (iPhone (iCloud Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/guide/icloud/mm7e90c1ba48

**USER:**
my phone has thousands of pictures of the kids on it and I'm scared I'll lose them. can you help me save them somewhere

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr013-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Mac
- task: Back up photos (iPhone (iCloud Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/guide/icloud/mm7e90c1ba48

**USER:**
My husband handles the computer stuff but he's traveling. We have a Mac and all of our family pictures are in the Photos app on it. I want them kept safe in iCloud in case the computer breaks. I'm signed in with my Apple Account already. What do I click?

**ASSISTANT:**
Here is how to keep your Mac's photos in iCloud.

1. Open the **Photos** app.
2. In the menu at the top of the screen, click **Photos**, then click **Settings**.
3. Click **iCloud**.
4. Select **iCloud Photos**.

The photos and videos in Photos are then added to iCloud. To check on progress, scroll to the bottom of the Photos screen.

## tr013-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iOS
- task: Back up photos (iPhone (iCloud Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/guide/icloud/mm7e90c1ba48

**USER:**
I want my iPhone pictures saved to iCloud, and I also want to look at them on my old laptop. But I don't want to install anything on the laptop, it's slow already. Is there a way?

**ASSISTANT:**
Yes. You can see them in a web browser, with nothing to install.

1. On your iPhone, open **Settings** and tap **your name**.
2. Tap **iCloud**, then tap **Photos**.
3. Turn on **Sync this iPhone**.
4. On your laptop, open a web browser and go to **icloud.com/photos**.
5. Sign in with your Apple Account.

Use the same Apple Account on both.

## tr013-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iOS
- task: Back up photos (iPhone (iCloud Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/guide/icloud/mm7e90c1ba48

**USER:**
Please show me how to save my iPhone photos to iCloud.

**ASSISTANT:**
Here is how to save your iPhone photos to iCloud.

1. Open **Settings** and tap **your name** at the top.
2. Tap **iCloud**.
3. Tap **Photos**.
4. Turn on **Sync this iPhone**.

**USER:**
I turned it on but I can't tell if anything is happening. How do I check?

**ASSISTANT:**
You can check the progress in the Photos app.

1. Open the **Photos** app.
2. Tap **Collections**.
3. Tap your **profile picture** in the top right corner.
4. Look below your name for the status.

If it still doesn't seem right, make sure you are signed in to the same Apple Account and that iCloud Photos is turned on.
