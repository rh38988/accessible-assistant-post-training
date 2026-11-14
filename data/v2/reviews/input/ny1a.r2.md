# Review input: batch ny1a, round 2 (14 examples)

## tr121-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPad
- task: Take a screenshot (iPad) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/102500

**USER:**
I want to save a picture of what is on my iPad screen to show my daughter. How?

**ASSISTANT:**
I can help with that. Does your iPad have a round **Home button** at the bottom, or **no Home button**?

**USER:**
No button, the bottom is all smooth

**ASSISTANT:**
Thank you. Here is how to do it on an iPad with no Home button.

1. Press the top button and either volume button at the same time.
2. Quickly let go of both buttons.
3. A small picture of the screenshot shows in the lower-left corner for a moment. Tap it to open the screenshot, or swipe it left to dismiss it.

To find it later, open **Photos**, tap **Collections**, swipe up, tap **Media Types**, then tap **Screenshots**.

## tr121-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPad
- task: Take a screenshot (iPad) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/102500

**USER:**
My hands are stiff from arthritis and I just cannot press two buttons at the same time on my iPad. I do have an Apple Pencil that came with it. Is there another way to take a screenshot using the Pencil?

**ASSISTANT:**
Yes, if your iPad works with the Apple Pencil, you can use it instead of the buttons.

1. Swipe your Apple Pencil from a bottom corner of the screen. Either the left or the right corner works.
2. A small picture of the screenshot shows in the lower-left corner for a moment. Tap it to open the screenshot, or swipe it left to dismiss it.

Here is where to look for it afterward. Open **Photos**, tap **Collections**, swipe up, tap **Media Types**, then tap **Screenshots**.

## tr122-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Mac
- task: Update the Mac's software (macOS) (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108382

**USER:**
it says i need to update my apple thing. what do i do

**ASSISTANT:**
I can help with that. Which device is it: a **Mac**, an **iPhone**, or an **iPad**?

**USER:**
its my mac

**ASSISTANT:**
Thank you. Here is how to update your Mac. Before you install anything, it is a good idea to back up your Mac.

1. Click the **Apple** menu at the top left of the screen and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Software Update** on the right. Your Mac checks for updates by itself.
4. If an update is shown, click the button to update, upgrade, or restart now.
5. If asked, type your administrator password. This is the password you use to log in to your Mac.
6. Let it finish. Do not let the Mac go to sleep or close its lid.

## tr123-a
- scenario: direct | style: plain | specification: fully_specified | platform: Mac
- task: Connect to a Wi-Fi network (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/guide/mac-help/mchlp1180

**USER:**
How do I connect my MacBook to the Wi-Fi at my house?

**ASSISTANT:**
Here is how to join a Wi-Fi network on your Mac. Make sure Wi-Fi is turned on and have the Wi-Fi password ready.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen. It is the Wi-Fi icon.
2. Click the name of your network in the list.
3. If it asks for a password, type it and click **Join**.

If you do not see your network in the list, click **Other Networks** to show the nearby networks.

## tr123-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Mac
- task: Connect to a Wi-Fi network (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/guide/mac-help/mchlp1180

**USER:**
My son set up a new router for me and he told me the network is hidden so my neighbors cannot see it. He wrote the network name and the password on a sticky note. Now my iMac will not find it anywhere in the list. How do I connect my iMac to a hidden network?

**ASSISTANT:**
For a hidden network, you type the name yourself. Make sure Wi-Fi is turned on, and have the network name, security type, and password from the sticky note ready.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen.
2. Click **Other Networks**.
3. Click **Other** at the bottom of the list.
4. In the **Network Name** box, type the network name from your sticky note.
5. Click the **Security** pop-up menu and choose the security type your network uses.
6. Fill in any other boxes that appear, such as a user name and the password, then click **Join**.

## tr123-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Mac
- task: Connect to a Wi-Fi network (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/guide/mac-help/mchlp1180

**USER:**
my laptop is not on the internet, how do i get it on the wifi

**ASSISTANT:**
I can help with that. Is your laptop a **Mac** (MacBook) or a **Windows** laptop?

**USER:**
macbook

**ASSISTANT:**
Thank you. Here is how to join a Wi-Fi network on your MacBook. Make sure Wi-Fi is turned on and have the Wi-Fi password ready.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen. It is the Wi-Fi icon.
2. Click the name of your network in the list.
3. If it asks for a password, type it and click **Join**.

If you do not see your network, click **Other Networks** to show the nearby networks.

## tr123-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Mac
- task: Connect to a Wi-Fi network (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/guide/mac-help/mchlp1180

**USER:**
I am at the library with my MacBook and I do not want to dig around in settings, I get lost in there. Just tell me the quickest way to connect to the library Wi-Fi from the top of the screen.

**ASSISTANT:**
You can do it from the top of the screen, no settings needed. Make sure Wi-Fi is turned on.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen. It is the Wi-Fi icon.
2. Click the library network in the list.
3. If it asks for a password, type it and click **Join**.

If you do not see the library network, click **Other Networks** to show the nearby networks.

## tr124-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Mac
- task: Delete (uninstall) an app (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102610 ; https://support.apple.com/en-us/116946

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

## tr125-a
- scenario: direct | style: plain | specification: fully_specified | platform: Mac
- task: Free up storage space (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102624

**USER:**
My MacBook is almost full. How can I free up some space?

**ASSISTANT:**
Here are some good ways to free up space.

1. Click the **Apple** menu, choose **System Settings**, click **General**, then click **Storage**. This shows what is using your space.
2. Open your **Downloads** folder from the Dock and delete what you do not need.
3. Delete apps you no longer use.
4. Empty the **Trash**. Space from trashed files is not freed until you do.

The Storage screen updates as you free up space.

## tr125-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Mac
- task: Free up storage space (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102624 ; https://support.apple.com/en-us/108345

**USER:**
My Mac is full because of my grandchildren's photos and videos, and I refuse to delete any of them. I have a spare external hard drive in my drawer though. What can I do to free up space without throwing away a single photo?

**ASSISTANT:**
You can move them to the external drive instead of deleting them. Photos and videos are some of the best things to move.

1. Plug your external drive into your Mac.
2. Move your Photos library to the external drive by following Apple's guide Move your Photos library to save space on your Mac: https://support.apple.com/en-us/108345.
3. Click the **Apple** menu, choose **System Settings**, click **General**, then click **Storage** to check how much space you now have.

## tr126-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Mac laptop
- task: Turn on Low Power Mode (Mac laptop) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/101613

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

## tr127-a
- scenario: direct | style: plain | specification: fully_specified | platform: Mac
- task: Back up the Mac with Time Machine (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/104984

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

## tr127-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Mac
- task: Back up the Mac with Time Machine (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/104984

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

## tr127-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Mac
- task: Back up the Mac with Time Machine (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/104984

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
