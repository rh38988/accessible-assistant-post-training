# Rule scan input, part 11 (50 examples)

## tr123-r
- task: Connect to a Wi-Fi network | platform: Mac | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Connect your Mac to the internet using Wi-Fi <https://support.apple.com/guide/mac-help/mchlp1180>

**USER:**
How do I join my home Wi-Fi on my Mac?

**ASSISTANT:**
Here is how to join your Wi-Fi on your Mac. Have the password ready.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen.
2. Click the name of your network.
3. If it asks for a password, type it and click **Join**.

**USER:**
I clicked the Wi-Fi icon but my network is not in the list.

**ASSISTANT:**
Try this.

1. Click the **Wi-Fi status menu** in the menu bar again.
2. Click **Other Networks**. This shows the nearby networks.
3. Click your network's name.
4. If it asks for a password, type it and click **Join**.

---

## tr124-a
- task: Delete (uninstall) an app | platform: Mac | scenario: direct | sensitive: False
- sources: Apple Support: Uninstall apps on your Mac <https://support.apple.com/en-us/102610>

**USER:**
How do I delete a game I downloaded from the internet on my Mac? I do not play it anymore.

**ASSISTANT:**
Here is how to remove it.

1. If the game is open, quit it first.
2. Open a **Finder** window and click **Applications** in the sidebar.
3. Find the game. If it came with an app called **Uninstall** or **Uninstaller**, open that and follow it. That also removes the extra files it left behind.
4. If there is no uninstaller, drag the game to the **Trash**.
5. If asked, type your administrator name and password. This is usually what you use to log in.
6. In the menu bar, choose **Finder**, then **Empty Trash**. This deletes it for good and frees up space.

---

## tr124-b
- task: Delete (uninstall) an app | platform: Mac | scenario: missing_info | sensitive: False
- sources: Apple Support: Uninstall apps on your Mac <https://support.apple.com/en-us/102610>

**USER:**
i want to delete an app i dont use

**ASSISTANT:**
I can help with that. Is the app on an **iPhone**, an **iPad**, or a **Mac**?

---

## tr124-c
- task: Delete (uninstall) an app | platform: Mac | scenario: direct_messy | sensitive: False
- sources: Apple Support: Uninstall apps on your Mac <https://support.apple.com/en-us/102610>

**USER:**
My MacBook has so many programs on it that I never use and I think it is making things slow. I know the name of one of them, a photo editing app that a friend told me to install. I do not see it on my Dock. I can search for it with the magnifying glass though. How can I get rid of it?

**ASSISTANT:**
You can use that search to find it.

1. If the app is open, quit it first.
2. Use the search (**Spotlight**) to find the app. Hold the **Command** key and double-click the app in the results. This shows it in **Finder**.
3. Look for an app named **Uninstall** or **Uninstaller**, possibly in the same folder. If you find one, open it and follow it.
4. If there is none, drag the app to the **Trash**, or select it and choose **File**, then **Move to Trash**.
5. If asked, type your administrator name and password.
6. Choose **Finder**, then **Empty Trash**.

---

## tr124-d
- task: Delete (uninstall) an app | platform: Mac | scenario: followup | sensitive: False
- sources: Apple Support: Uninstall apps on your Mac <https://support.apple.com/en-us/102610>

**USER:**
i want to delete an app i dont use

**ASSISTANT:**
I can help with that. Is the app on an **iPhone**, an **iPad**, or a **Mac**?

**USER:**
mac

**ASSISTANT:**
Thank you. Here is how to delete an app on your Mac.

1. If the app is open, quit it first.
2. Open a **Finder** window and click **Applications** in the sidebar.
3. Find the app. If it has an **Uninstall** or **Uninstaller** app next to it, use that instead and follow it.
4. Otherwise, drag the app to the **Trash**.
5. If asked, type your administrator name and password.
6. In the menu bar, choose **Finder**, then **Empty Trash**.

---

## tr124-e
- task: Delete (uninstall) an app | platform: Mac | scenario: constraint | sensitive: False
- sources: Apple Support: Uninstall apps on your Mac <https://support.apple.com/en-us/102610>

**USER:**
I want to delete a writing program from my Mac because I stopped using it, but I have a lot of old letters I wrote in it and I do NOT want to lose those. Will deleting it get rid of my letters too? And what do I do?

**ASSISTANT:**
No, deleting the app does not delete the letters or files you made with it. You might need an app to open them later, though.

1. If the writing program is open, quit it first.
2. Open a **Finder** window and click **Applications** in the sidebar.
3. Find the program and look for an **Uninstall** or **Uninstaller** app. If there is one, use it.
4. If there is none, drag the program to the **Trash**.
5. If asked, type your administrator name and password.
6. Choose **Finder**, then **Empty Trash**.

Deleting an app also does not cancel any subscription you bought through it.

---

## tr124-r
- task: Delete (uninstall) an app | platform: Mac | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Uninstall apps on your Mac <https://support.apple.com/en-us/102610>; Apple Support: Start up your Mac in safe mode <https://support.apple.com/en-us/116946>

**USER:**
How do I delete an app from my Mac?

**ASSISTANT:**
Here is how to delete an app on your Mac.

1. If the app is open, quit it first.
2. Open a **Finder** window and click **Applications** in the sidebar.
3. Find the app. If it has an **Uninstall** or **Uninstaller** app, use that.
4. Otherwise, drag the app to the **Trash**.
5. If asked, type your administrator name and password.
6. Choose **Finder**, then **Empty Trash**.

**USER:**
My Mac says the app is in use and will not let me delete it.

**ASSISTANT:**
Try this.

1. Make sure the app is not open. Quit it.
2. Try to delete it again.
3. If it still will not delete, restart your Mac and try again.

If that does not work, Apple has a guide called start up in Safe Mode: https://support.apple.com/en-us/116946.

---

## tr125-c
- task: Free up storage space | platform: Mac | scenario: direct_messy | sensitive: False
- sources: Apple Support: Free up storage space on your Mac <https://support.apple.com/en-us/102624>

**USER:**
I have an old iMac that my husband bought years ago and it is not on the newest macOS, definitely older than Ventura. It keeps saying the disk is nearly full and I cannot save my family pictures anymore. I would like to see what is taking up all the room and then clear some of it. Where do I begin?

**ASSISTANT:**
Start by looking at what is using the space.

1. Click the **Apple** menu and choose **About This Mac**.
2. Click **Storage**. It shows your space by category.
3. Next to a category, click **More Info** if you see it. It gives you ways to manage that category.
4. Delete things you do not need, such as files in your **Downloads** folder or apps you no longer use.
5. Empty the **Trash**. Space from trashed files is not freed until you do.

The Storage screen updates as you free up space.

---

## tr125-d
- task: Free up storage space | platform: Mac | scenario: followup | sensitive: False
- sources: Apple Support: Free up storage space on your Mac <https://support.apple.com/en-us/102624>

**USER:**
it says my storage is full. how do i clear some space

**ASSISTANT:**
I can help with that. Is the full storage on an **iPhone**, an **iPad**, or a **Mac**?

**USER:**
the mac

**ASSISTANT:**
Thank you. Here are some good ways to free up space on your Mac.

1. Click the **Apple** menu, choose **System Settings**, click **General**, then click **Storage**. This shows what is using your space.
2. Open your **Downloads** folder from the Dock and delete what you do not need.
3. Delete apps you no longer use.
4. Empty the **Trash**. Space from trashed files is not freed until you do.

---

## tr125-r
- task: Free up storage space | platform: Mac | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Free up storage space on your Mac <https://support.apple.com/en-us/102624>

**USER:**
How do I see what is using up the storage on my Mac?

**ASSISTANT:**
Here is how to see it.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Storage**. It shows your space by category.
4. Next to a category, click **More Info** if you see it for ways to manage it.

**USER:**
I do not see Storage under General. My Mac is very old.

**ASSISTANT:**
On an older version of macOS, it is in a different place.

1. Click the **Apple** menu.
2. Choose **About This Mac**.
3. Click **Storage**.

---

## tr126-a
- task: Turn on Low Power Mode | platform: Mac laptop | scenario: direct | sensitive: False
- sources: Apple Support: About Power Modes on your Mac <https://support.apple.com/101613>

**USER:**
How do I turn on Low Power Mode on my MacBook to make the battery last longer?

**ASSISTANT:**
Here is how to turn it on.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **Battery**.
3. Under **Energy Mode**, open the **On battery** pop-up menu.
4. Choose **Low Power Mode**.

To use it while plugged in too, do the same in the **On power adapter** pop-up menu.

To check, click the battery icon in the menu bar. It shows whether a power mode is on.

---

## tr126-b
- task: Turn on Low Power Mode | platform: Mac laptop | scenario: missing_info | sensitive: False
- sources: Apple Support: About Power Modes on your Mac <https://support.apple.com/101613>

**USER:**
how do i turn on battery saver

**ASSISTANT:**
I can help with that. Is the device an **iPhone**, an **iPad**, or a **Mac laptop**?

---

## tr126-c
- task: Turn on Low Power Mode | platform: Mac laptop | scenario: direct_messy | sensitive: False
- sources: Apple Support: About Power Modes on your Mac <https://support.apple.com/101613>

**USER:**
I have an older MacBook Pro running Monterey, and I take it on the train every day and the battery drains before I get home. My daughter said there is a battery saving setting called Low Power or something. On my Mac the settings app is called System Preferences. How do I turn it on?

**ASSISTANT:**
Yes, on Monterey it is in System Preferences.

1. Click the **Apple** menu and choose **System Preferences**.
2. Click **Battery**.
3. In the sidebar, click **Battery**. If you also want it while plugged in, click **Power Adapter** instead.
4. From the **Energy Mode** pop-up menu, choose **Low Power**.

To check, click the battery icon in the menu bar. It shows whether a power mode is on.

---

## tr126-d
- task: Turn on Low Power Mode | platform: Mac laptop | scenario: followup | sensitive: False
- sources: Apple Support: About Power Modes on your Mac <https://support.apple.com/101613>

**USER:**
how do i turn on battery saver

**ASSISTANT:**
I can help with that. Is the device an **iPhone**, an **iPad**, or a **Mac laptop**?

**USER:**
mac laptop

**ASSISTANT:**
Thank you. On a Mac laptop it is called Low Power Mode.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **Battery**.
3. Under **Energy Mode**, open the **On battery** pop-up menu.
4. Choose **Low Power Mode**.

If your Apple menu says System Preferences instead of System Settings, tell me and I will give you the steps for that.

---

## tr126-e
- task: Turn on Low Power Mode | platform: Mac laptop | scenario: constraint | sensitive: False
- sources: Apple Support: About Power Modes on your Mac <https://support.apple.com/101613>

**USER:**
I only want Low Power Mode on my MacBook when it is plugged into the charger at my desk, because I do not want my Mac to feel slower when I am using the battery. It is on a recent macOS with System Settings. How do I set it just for when it is plugged in?

**ASSISTANT:**
You can set it for the charger only.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **Battery**.
3. Under **Energy Mode**, open the **On power adapter** pop-up menu.
4. Choose **Low Power Mode**.

Leave the **On battery** menu as it is, since your Mac can use a different energy mode for each.

---

## tr127-a
- task: Back up the Mac with Time Machine | platform: Mac | scenario: direct | sensitive: False
- sources: Apple Support: Back up your Mac with Time Machine <https://support.apple.com/en-us/104984>

**USER:**
How do I set up Time Machine to back up my Mac? I just bought an external hard drive.

**ASSISTANT:**
Here is how to set it up. Use a drive that is at least twice the size of your Mac's storage, and only for Time Machine.

1. Plug the external drive into your Mac.
2. Click the **Apple** menu and choose **System Settings**.
3. Click **General** in the sidebar, then click **Time Machine** on the right.
4. Click **Add Backup Disk**.
5. Select your drive, then click **Set Up Disk**.

If your Mac asks whether to erase the drive, erasing wipes everything on it. Erase only if you do not need anything on it, or choose a different backup disk instead. After setup, it starts backing up right away.

---

## tr127-b
- task: Back up the Mac with Time Machine | platform: Mac | scenario: missing_info | sensitive: False
- sources: Apple Support: Back up your Mac with Time Machine <https://support.apple.com/en-us/104984>

**USER:**
my grandson says i should make a copy of everything on my computer in case it breaks. how

**ASSISTANT:**
I can help with that. Is your computer a **Mac** or a **Windows** computer?

---

## tr127-c
- task: Back up the Mac with Time Machine | platform: Mac | scenario: direct_messy | sensitive: False
- sources: Apple Support: Back up your Mac with Time Machine <https://support.apple.com/en-us/104984>

**USER:**
My son set up Time Machine on my iMac a while ago, and the backup drive is plugged in. I do not want to wait for the next automatic backup because I am about to install some new things and I want a fresh backup first. I do not need to set anything up again. How do I start a backup right now?

**ASSISTANT:**
You can start one right now from the menu bar.

1. Click the **Time Machine** menu in the menu bar at the top of the screen.
2. Choose **Back Up Now**.

You can use the same menu to see the progress, or to stop or skip a backup. It also shows the date and time of your latest backup. You can keep using your Mac while it backs up.

---

## tr127-d
- task: Back up the Mac with Time Machine | platform: Mac | scenario: followup | sensitive: False
- sources: Apple Support: Back up your Mac with Time Machine <https://support.apple.com/en-us/104984>

**USER:**
my grandson says i should make a copy of everything on my computer in case it breaks. how

**ASSISTANT:**
I can help with that. Is your computer a **Mac** or a **Windows** computer?

**USER:**
its a mac

**ASSISTANT:**
Thank you. On a Mac you use Time Machine with an external drive. Use a drive at least twice the size of your Mac's storage, only for backups.

1. Plug the external drive into your Mac.
2. Click the **Apple** menu and choose **System Settings**.
3. Click **General** in the sidebar, then click **Time Machine** on the right.
4. Click **Add Backup Disk**.
5. Select your drive, then click **Set Up Disk**.

If your Mac asks whether to erase the drive, erasing wipes everything on it. Erase only if you do not need anything on it, or choose a different backup disk instead.

After setup, your Mac starts backing up right away.

---

## tr127-e
- task: Back up the Mac with Time Machine | platform: Mac | scenario: constraint | sensitive: False
- sources: Apple Support: Back up your Mac with Time Machine <https://support.apple.com/en-us/104984>

**USER:**
I keep tax records and bank papers on my MacBook, so I want my Time Machine backup to be protected with a password in case someone takes the backup drive. I have the drive plugged in already. How do I set up Time Machine so the backup needs a password?

**ASSISTANT:**
You can turn on encryption when you set up the backup.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **General** in the sidebar, then click **Time Machine** on the right.
3. Click **Add Backup Disk**.
4. Select your drive, then click **Set Up Disk**.
5. During setup, turn on **Encrypt Backup**, then create a backup password.

If your Mac asks whether to erase the drive, erasing wipes everything on it. Erase only if you do not need anything on it, or choose a different backup disk instead.

Keep that password safe. You will need it to restore your files later. After setup, your Mac starts backing up right away.

---

## tr127-r
- task: Back up the Mac with Time Machine | platform: Mac | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Back up your Mac with Time Machine <https://support.apple.com/en-us/104984>

**USER:**
How do I set up Time Machine on my Mac? I have a USB drive plugged in.

**ASSISTANT:**
Here is how to set it up. Use a drive at least twice the size of your Mac's storage, and only for Time Machine.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **General** in the sidebar, then click **Time Machine** on the right.
3. Click **Add Backup Disk**.
4. Select your USB drive, then click **Set Up Disk**.

**USER:**
It is asking if I want to erase the drive but I have family photos on that drive!

**ASSISTANT:**
Do not erase it, then. Your Mac lets you pick a different drive instead.

1. Do not agree to erase the drive.
2. Choose a different backup disk or volume when it asks.
3. Use a drive that you only use for Time Machine backups.

---

## tr128-a
- task: Pair a Bluetooth accessory such as headphones or a speaker | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Pair a third-party Bluetooth accessory with your iPhone or iPad <https://support.apple.com/en-us/HT204091>

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

---

## tr128-b
- task: Pair a Bluetooth accessory such as headphones or a speaker | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Pair a third-party Bluetooth accessory with your iPhone or iPad <https://support.apple.com/en-us/HT204091>

**USER:**
my new earbuds wont hook up to my phone, what do i do

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr128-c
- task: Pair a Bluetooth accessory such as headphones or a speaker | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Pair a third-party Bluetooth accessory with your iPhone or iPad <https://support.apple.com/en-us/HT204091>

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

---

## tr128-d
- task: Pair a Bluetooth accessory such as headphones or a speaker | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Pair a third-party Bluetooth accessory with your iPhone or iPad <https://support.apple.com/en-us/HT204091>

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

---

## tr128-r
- task: Pair a Bluetooth accessory such as headphones or a speaker | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Pair a third-party Bluetooth accessory with your iPhone or iPad <https://support.apple.com/en-us/HT204091>; Apple Support: If you can't pair a Bluetooth accessory with your iPhone or iPad <https://support.apple.com/en-us/111804>

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

---

## tr129-a
- task: Connect a Bluetooth device | platform: Mac | scenario: direct | sensitive: False
- sources: Apple Support: Connect a Bluetooth device with your Mac <https://support.apple.com/en-us/guide/mac-help/blth1004/mac>

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

---

## tr129-b
- task: Connect a Bluetooth device | platform: Mac | scenario: missing_info | sensitive: False
- sources: Apple Support: Connect a Bluetooth device with your Mac <https://support.apple.com/en-us/guide/mac-help/blth1004/mac>

**USER:**
My computer will not find my wireless mouse. How do I hook it up?

**ASSISTANT:**
I can help with that. Is your computer a **Mac** or a **Windows** PC?

---

## tr129-c
- task: Connect a Bluetooth device | platform: Mac | scenario: direct_messy | sensitive: False
- sources: Apple Support: Connect a Bluetooth device with your Mac <https://support.apple.com/en-us/guide/mac-help/blth1004/mac>

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

---

## tr129-d
- task: Connect a Bluetooth device | platform: Mac | scenario: followup | sensitive: False
- sources: Apple Support: Connect a Bluetooth device with your Mac <https://support.apple.com/en-us/guide/mac-help/blth1004/mac>

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

---

## tr129-r
- task: Connect a Bluetooth device | platform: Mac | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Connect a Bluetooth device with your Mac <https://support.apple.com/en-us/guide/mac-help/blth1004/mac>

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

---

## tr130-a
- task: Turn on two-factor authentication for the Apple Account | platform: iPhone | scenario: direct | sensitive: True
- sources: Apple Support: Two-factor authentication for Apple Account <https://support.apple.com/en-us/102660>

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

---

## tr130-c
- task: Turn on two-factor authentication for the Apple Account | platform: iPhone | scenario: direct_messy | sensitive: True
- sources: Apple Support: Two-factor authentication for Apple Account <https://support.apple.com/en-us/102660>

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

---

## tr130-e
- task: Turn on two-factor authentication for the Apple Account | platform: iPhone | scenario: constraint | sensitive: True
- sources: Apple Support: Two-factor authentication for Apple Account <https://support.apple.com/en-us/102660>

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

---

## tr131-a
- task: Find saved passwords in the Passwords app and keep them in sync with iCloud Keychain | platform: iPhone | scenario: direct | sensitive: True
- sources: Apple Support: Find saved passwords and passkeys on your iPhone <https://support.apple.com/en-us/104955>

**USER:**
Where can I see my saved passwords on my iPhone? It has the newest iOS.

**ASSISTANT:**
Your saved passwords are in the Passwords app.

1. Open the **Passwords** app.
2. Unlock it with Face ID, Touch ID, or your passcode.
3. Tap **All**, or choose another category.
4. Tap the website or app you want. Your password appears.

---

## tr131-b
- task: Find saved passwords in the Passwords app and keep them in sync with iCloud Keychain | platform: iPhone | scenario: missing_info | sensitive: True
- sources: Apple Support: Find saved passwords and passkeys on your iPhone <https://support.apple.com/en-us/104955>

**USER:**
where does my phone keep the passwords it saved for me

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr131-c
- task: Find saved passwords in the Passwords app and keep them in sync with iCloud Keychain | platform: iPhone | scenario: direct_messy | sensitive: True
- sources: Apple Support: Find saved passwords and passkeys on your iPhone <https://support.apple.com/en-us/104955>

**USER:**
I have an old iPhone that is on iOS 17 and I forgot my password for my bank's website but I know my phone saved it at some point. I do not see any Passwords app on it. How do I look it up?

**ASSISTANT:**
On iOS 17, your passwords are in Settings.

1. Open **Settings**.
2. Scroll down and tap **Passwords**.
3. Unlock it with Face ID, Touch ID, or your passcode.
4. Tap the website or app you want. Your password appears.

If you cannot find it, check that you are looking at the main **Passwords** list. Then look in **Recently Deleted**.

---

## tr131-d
- task: Find saved passwords in the Passwords app and keep them in sync with iCloud Keychain | platform: iPhone | scenario: followup | sensitive: True
- sources: Apple Support: Find saved passwords and passkeys on your iPhone <https://support.apple.com/en-us/104955>

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

---

## tr132-a
- task: iPad is frozen or will not respond | platform: iPad | scenario: direct | sensitive: False
- sources: Apple Support: If your iPad is frozen, doesn't turn on, or doesn't respond <https://support.apple.com/kb/HT212017>

**USER:**
My iPad has no Home button and the screen is frozen. Nothing happens when I touch it. What should I do?

**ASSISTANT:**
You can force it to restart.

1. Press and quickly let go of the volume button closest to the top button.
2. Press and quickly let go of the volume button farthest from the top button.
3. Press and hold the top button until the Apple logo appears.

If the iPad still will not turn on, charge it. Charging can take up to an hour.

---

## tr132-b
- task: iPad is frozen or will not respond | platform: iPad | scenario: missing_info | sensitive: False
- sources: Apple Support: If your iPad is frozen, doesn't turn on, or doesn't respond <https://support.apple.com/kb/HT212017>

**USER:**
my ipad is frozen and wont do anything

**ASSISTANT:**
I can help with that. Does your iPad have a **Home button**, or **no Home button**?

---

## tr132-c
- task: iPad is frozen or will not respond | platform: iPad | scenario: direct_messy | sensitive: False
- sources: Apple Support: If your iPad is frozen, doesn't turn on, or doesn't respond <https://support.apple.com/kb/HT212017>

**USER:**
My iPad is the older kind with the round Home button under the screen. I was reading and it just stopped. The screen is on but nothing moves and it will not respond to anything. I tried holding the top button and it did not do anything. Help please.

**ASSISTANT:**
You can force it to restart. On an iPad with a Home button, use two buttons together.

1. Press and hold the **Home button** and the **top button** at the same time.
2. Keep holding both until the Apple logo appears.

If the iPad still will not turn on, charge it. Charging can take up to an hour.

---

## tr132-d
- task: iPad is frozen or will not respond | platform: iPad | scenario: followup | sensitive: False
- sources: Apple Support: If your iPad is frozen, doesn't turn on, or doesn't respond <https://support.apple.com/kb/HT212017>

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

---

## tr132-e
- task: iPad is frozen or will not respond | platform: iPad | scenario: constraint | sensitive: False
- sources: Apple Support: If your iPad is frozen, doesn't turn on, or doesn't respond <https://support.apple.com/kb/HT212017>

**USER:**
My iPad has no Home button and it is frozen. I have arthritis in my hands, so I cannot hold two buttons down at the same time. Is there a way to restart it without that?

**ASSISTANT:**
Yes. On an iPad with no Home button, you press the buttons one at a time.

1. Press and quickly let go of the volume button closest to the top button.
2. Press and quickly let go of the volume button farthest from the top button.
3. Press and hold the top button until the Apple logo appears.

You only hold one button, the top button, at the end.

---

## tr132-r
- task: iPad is frozen or will not respond | platform: iPad | scenario: failure_recovery | sensitive: False
- sources: Apple Support: If your iPad is frozen, doesn't turn on, or doesn't respond <https://support.apple.com/kb/HT212017>

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

---

## tr133-b
- task: Report and block junk text messages | platform: iPhone | scenario: missing_info | sensitive: True
- sources: Apple iPhone User Guide: Report spam and block senders in Messages <https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios>

**USER:**
how do i report and block junk texts

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr133-r
- task: Report and block junk text messages | platform: iPhone | scenario: failure_recovery | sensitive: True
- sources: Apple iPhone User Guide: Report spam and block senders in Messages <https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios>

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

---

## tr134-a
- task: Cannot send or receive email in the Mail app | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: If you can't receive email on your iPhone or iPad (send steps from Apple Support: If you can't send email on your iPhone or iPad, support.apple.com/en-us/102556) <https://support.apple.com/en-us/102578>

**USER:**
The Mail app on my iPhone will not send or get any email. What should I do?

**ASSISTANT:**
Try these first, in order, and stop when your email works.

1. Make sure your iPhone is connected to the internet.
2. Check your email provider's status page, or contact them, to see if there is an outage.
3. In a web browser, sign in to your provider's website to confirm your email address and password.
4. Ask your provider if two-step verification is turned on. You may need a special password from them to use email on your iPhone.
5. Open **Settings**, then tap **Apps**.
6. Tap **Mail**, then tap **Mail Accounts**.
7. Tap **Fetch New Data**, then choose **Automatically**, **Manually**, or a schedule.

Last resort, only if nothing above works: removing the account can delete emails already saved on your phone. So first, on a computer, sign in to your provider's website and make sure all your email is there or saved somewhere other than the phone. Then:

1. Open **Settings**, tap **Apps**, then tap **Mail**.
2. Tap **Mail Accounts**, tap your account, then tap **Delete Account**.
3. Add the account again.

If that does not help, contact your email provider.

---

## tr134-b
- task: Cannot send or receive email in the Mail app | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: If you can't receive email on your iPhone or iPad (send steps from Apple Support: If you can't send email on your iPhone or iPad, support.apple.com/en-us/102556) <https://support.apple.com/en-us/102578>

**USER:**
my email is not working, can you help me

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr134-d
- task: Cannot send or receive email in the Mail app | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: If you can't receive email on your iPhone or iPad (send steps from Apple Support: If you can't send email on your iPhone or iPad, support.apple.com/en-us/102556) <https://support.apple.com/en-us/102578>

**USER:**
my email is not working, can you help me

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone. Nothing new is coming in.

**ASSISTANT:**
Let's check these in order.

1. Make sure your iPhone is connected to the internet.
2. Check your email provider's status page, or contact them, to see if there is an outage.
3. In a web browser, sign in to your provider's website to confirm your email address and password.
4. Ask your provider whether two-step verification or another security feature is turned on. If it is, you may need a special password from them to use email on your iPhone.
5. Open **Settings**, then tap **Apps**.
6. Tap **Mail**, then tap **Mail Accounts**.
7. Tap **Fetch New Data**.
8. Tap **Automatically** (or **Manually**, or pick a schedule).

With **Automatically**, the iPhone fetches new mail in the background only when it is charging and on Wi-Fi.

If it still does not work, contact your email provider or system administrator.

---

## tr134-e
- task: Cannot send or receive email in the Mail app | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: If you can't receive email on your iPhone or iPad (send steps from Apple Support: If you can't send email on your iPhone or iPad, support.apple.com/en-us/102556) <https://support.apple.com/en-us/102578>

**USER:**
On my iPhone, the Mail app gets nothing new and my sent emails fail. I have years of old emails stored on this phone and I do not want to delete my account and lose them. What can I check instead?

**ASSISTANT:**
You can check these without deleting anything. Try them in order.

1. Make sure your iPhone is connected to the internet.
2. Check your email provider's status page, or contact them, to see if there is an outage.
3. Open **Settings**, then tap **Apps**. Tap **Mail**, then **Mail Accounts**, then **Fetch New Data**. Choose **Automatically**, **Manually**, or a schedule.
4. In a web browser, sign in to your provider's website to confirm your email address and password.
5. Ask your provider if two-step verification or other security features are on. You may need a special password from them to use email on your iPhone.
6. Ask your provider to confirm that your account settings are correct.
7. If none of these work, contact your email provider.

Removing the account is not on this list. It can delete emails already downloaded to the phone, so do not remove it unless you have first confirmed on your provider's website that all your email is saved somewhere else.

---
