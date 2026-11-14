# Review input: batch ny1a, round 1 (42 examples)

## tr121-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPad
- task: Take a screenshot (iPad) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/102500

**USER:**
How do I take a screenshot on my iPad? It is the newer kind with no round Home button.

**ASSISTANT:**
Here is how to take a screenshot on an iPad that has no Home button.

1. Press the top button and either volume button at the same time.
2. Quickly let go of both buttons.
3. A small picture of the screenshot shows in the lower-left corner for a moment. Tap it to open the screenshot, or swipe it left to dismiss it.

To find it later, open **Photos**, tap **Collections**, swipe up, tap **Media Types**, then tap **Screenshots**.

## tr121-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPad
- task: Take a screenshot (iPad) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/102500

**USER:**
My neighbor sent me a recipe on my iPad and I want to keep a picture of it so I can look at it in the kitchen. My iPad is the older one with the round Home button at the bottom of the screen. My grandson told me about taking a screenshot but I forgot how. What do I press?

**ASSISTANT:**
Your iPad has a Home button, so here is how to do it.

1. Open the recipe so it is on the screen.
2. Press the top button and the Home button at the same time.
3. Quickly let go of both buttons.
4. A small picture of the screenshot shows in the lower-left corner for a moment. Tap it to open the screenshot, or swipe it left to dismiss it.

To find it later, open **Photos**, tap **Collections**, swipe up, tap **Media Types**, then tap **Screenshots**.

## tr121-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: iPad
- task: Take a screenshot (iPad) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/102500

**USER:**
I want to save a picture of what is on my iPad screen to show my daughter. How?

**ASSISTANT:**
I can help with that. Does your iPad have a round **Home button** at the bottom, or **no Home button**?

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

You will find the saved picture in **Photos**, under **Collections**, then **Media Types**, then **Screenshots**.

## tr121-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPad
- task: Take a screenshot (iPad) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/102500

**USER:**
My hands are stiff from arthritis and I just cannot press two buttons at the same time on my iPad. I do have an Apple Pencil that came with it. Is there another way to take a screenshot using the Pencil?

**ASSISTANT:**
Yes, if your iPad works with the Apple Pencil, you can use it instead of the buttons.

1. Hold your Apple Pencil.
2. Swipe it from a bottom corner of the screen. Either the left or the right corner works.

The screenshot is saved for you. To find it, open **Photos**, tap **Collections**, swipe up, tap **Media Types**, then tap **Screenshots**.

## tr121-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPad
- task: Take a screenshot (iPad) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/102500

**USER:**
How do I take a screenshot on my iPad with a Home button?

**ASSISTANT:**
Here is how to take a screenshot on an iPad with a Home button.

1. Press the top button and the Home button at the same time.
2. Quickly let go of both buttons.
3. A small picture of the screenshot shows in the lower-left corner for a moment. Tap it to open the screenshot, or swipe it left to dismiss it.

If you do not tap the picture right away, it goes away on its own.

**USER:**
I did it but I was too slow and the little picture went away. Did I lose it?

**ASSISTANT:**
It is not lost, the little picture just goes away by itself. Here is where to find your screenshot.

1. Open **Photos**.
2. Tap **Collections**.
3. Swipe up, then tap **Media Types**.
4. Tap **Screenshots**.

## tr122-a
- scenario: direct | style: plain | specification: fully_specified | platform: Mac
- task: Update the Mac's software (macOS) (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108382

**USER:**
How do I update the software on my MacBook?

**ASSISTANT:**
Here is how to update your Mac.

1. Click the **Apple** menu at the top left of the screen and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Software Update** on the right. Your Mac checks for updates by itself.
4. If an update is shown, click the button to update, upgrade, or restart now.
5. If asked, type your administrator password. This is the password you use to log in to your Mac.
6. Let it finish. Do not let the Mac go to sleep or close its lid. It may restart a few times and show a progress bar or a blank screen.

It is a good idea to back up your Mac before you install new software.

## tr122-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Mac
- task: Update the Mac's software (macOS) (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108382

**USER:**
Hello, my iMac keeps telling me something about software but I never know what to do and I do not want to break anything. My nephew set it up for me last year. I would like to update the macOS on it. Is there a quick way to get to the update screen using search instead of clicking through lots of menus?

**ASSISTANT:**
Yes, you can use search to get there.

1. Click the **Spotlight** or **Siri** icon in the menu bar at the top of the screen.
2. Type **Software Update** and open it from the results.
3. Your Mac checks for updates by itself. If one is shown, click the button to update, upgrade, or restart now.
4. If asked, type your administrator password. This is the password you use to log in to your Mac.
5. Let it finish. Do not let the Mac go to sleep. It may restart a few times and show a progress bar or a blank screen.

Before installing, it is wise to back up your Mac.

## tr122-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Update the Mac's software (macOS) (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108382

**USER:**
it says i need to update my apple thing. what do i do

**ASSISTANT:**
I can help with that. Which device is it: a **Mac**, an **iPhone**, or an **iPad**?

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
Thank you. Here is how to update your Mac.

1. Click the **Apple** menu at the top left of the screen and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Software Update** on the right. Your Mac checks for updates by itself.
4. If an update is shown, click the button to update, upgrade, or restart now.
5. If asked, type your administrator password. This is the password you use to log in to your Mac.
6. Let it finish. Do not let the Mac go to sleep or close its lid.

## tr122-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Mac
- task: Update the Mac's software (macOS) (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108382

**USER:**
I am not ready to install anything on my Mac today because I am in the middle of tax paperwork. I only want to look and see whether an update is waiting for me, without actually installing it. How do I look?

**ASSISTANT:**
You can look without installing anything.

1. Click the **Apple** menu at the top left of the screen and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Software Update** on the right. Your Mac checks for updates by itself.
4. Read what it shows. If an update is waiting, you will see a button to update, upgrade, or restart now. Do not click it, and nothing will install.
5. If it says your Mac is up to date, there is nothing waiting.

## tr122-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Mac
- task: Update the Mac's software (macOS) (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108382

**USER:**
How do I check for a macOS update on my Mac?

**ASSISTANT:**
Here is how to check for an update on your Mac.

1. Click the **Apple** menu at the top left of the screen and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Software Update** on the right. Your Mac checks for updates by itself.
4. If an update is shown, click the button to update, upgrade, or restart now.
5. If asked, type your administrator password.
6. Let it finish and do not close the lid.

**USER:**
It just says my Mac is up to date, but my friend has a newer version on hers. Is it wrong?

**ASSISTANT:**
It may not be wrong. Here is what to try.

1. Click **Check for Updates** to look again. You can also press Command-R, or close and reopen **Software Update**.
2. If it still says up to date, that may be because Software Update only shows updates that work with your Mac model. A newer version that does not work with your Mac will not be offered.

## tr123-a
- scenario: direct | style: plain | specification: fully_specified | platform: Mac
- task: Connect to a Wi-Fi network (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/guide/mac-help/mchlp1180

**USER:**
How do I connect my MacBook to the Wi-Fi at my house?

**ASSISTANT:**
Here is how to join a Wi-Fi network on your Mac. Have the Wi-Fi password ready.

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
For a hidden network, you type the name yourself.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen.
2. Click **Other Networks**.
3. Click **Other** at the bottom of the list.
4. In the **Network Name** box, type the network name from your sticky note.
5. Click the **Security** pop-up menu and choose the security type your network uses.
6. Fill in any other boxes that appear, such as a user name and the password, then click **Join**.

## tr123-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Connect to a Wi-Fi network (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/guide/mac-help/mchlp1180

**USER:**
my laptop is not on the internet, how do i get it on the wifi

**ASSISTANT:**
I can help with that. Is your laptop a **Mac** (MacBook) or a **Windows** laptop?

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
Thank you. Here is how to join a Wi-Fi network on your MacBook. Have the Wi-Fi password ready.

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
You can do it from the top of the screen, no settings needed.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen. It is the Wi-Fi icon.
2. Click the library network in the list.
3. If it asks for a password, type it and click **Join**. If it shows terms and conditions, accept them.

If you do not see the library network, click **Other Networks** to show the nearby networks.

## tr123-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Mac
- task: Connect to a Wi-Fi network (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/guide/mac-help/mchlp1180

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

## tr124-a
- scenario: direct | style: plain | specification: fully_specified | platform: Mac
- task: Delete (uninstall) an app (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102610

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

## tr124-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Mac
- task: Delete (uninstall) an app (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102610

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

## tr124-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Delete (uninstall) an app (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102610

**USER:**
i want to delete an app i dont use

**ASSISTANT:**
I can help with that. Is the app on an **iPhone**, an **iPad**, or a **Mac**?

## tr124-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Mac
- task: Delete (uninstall) an app (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102610

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

## tr124-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Mac
- task: Delete (uninstall) an app (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102610

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

## tr124-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Mac
- task: Delete (uninstall) an app (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102610

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
3. If it still will not delete, restart your Mac, or start it up in Safe Mode, then try again.

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
4. Delete old iPhone or iPad backups, if your Mac stores any.
5. Empty the **Trash**. Space from trashed files is not freed until you do.

The Storage screen updates as you free up space.

## tr125-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Mac
- task: Free up storage space (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102624

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

## tr125-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Free up storage space (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102624

**USER:**
it says my storage is full. how do i clear some space

**ASSISTANT:**
I can help with that. Is the full storage on an **iPhone**, an **iPad**, or a **Mac**?

## tr125-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Mac
- task: Free up storage space (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102624

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

## tr125-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Mac
- task: Free up storage space (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102624

**USER:**
My Mac is full because of my grandchildren's photos and videos, and I refuse to delete any of them. I have a spare external hard drive in my drawer though. What can I do to free up space without throwing away a single photo?

**ASSISTANT:**
You can move them to the external drive instead of deleting them. Photos and videos are some of the best things to move.

1. Plug your external drive into your Mac.
2. Move the photos and videos you want to keep onto the drive.
3. Click the **Apple** menu, choose **System Settings**, click **General**, then click **Storage** to check how much space you now have.

Apple has a separate guide for moving a Photos library, so check that guide before you move yours.

## tr125-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Mac
- task: Free up storage space (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102624

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

## tr126-a
- scenario: direct | style: plain | specification: fully_specified | platform: Mac laptop
- task: Turn on Low Power Mode (Mac laptop) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/101613

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

## tr126-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Mac laptop
- task: Turn on Low Power Mode (Mac laptop) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/101613

**USER:**
I have an older MacBook Pro running Monterey, and I take it on the train every day and the battery drains before I get home. My daughter said there is a battery saving setting called Low Power or something. On my Mac the settings app is called System Preferences. How do I turn it on?

**ASSISTANT:**
Yes, on Monterey it is in System Preferences.

1. Click the **Apple** menu and choose **System Preferences**.
2. Click **Battery**.
3. In the sidebar, click **Battery**. If you also want it while plugged in, click **Power Adapter** instead.
4. From the **Energy Mode** pop-up menu, choose **Low Power**.

To check, click the battery icon in the menu bar. It shows whether a power mode is on.

## tr126-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on Low Power Mode (Mac laptop) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/101613

**USER:**
how do i turn on battery saver

**ASSISTANT:**
I can help with that. Is the device an **iPhone**, an **iPad**, or a **Mac laptop**?

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

If your Mac says System Preferences instead of System Settings, choose that.

## tr126-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Mac laptop
- task: Turn on Low Power Mode (Mac laptop) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/101613

**USER:**
I only want Low Power Mode on my MacBook when it is plugged into the charger at my desk, because I do not want my Mac to feel slower when I am using the battery. It is on a recent macOS with System Settings. How do I set it just for when it is plugged in?

**ASSISTANT:**
You can set it for the charger only.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **Battery**.
3. Under **Energy Mode**, open the **On power adapter** pop-up menu.
4. Choose **Low Power Mode**.

Leave the **On battery** menu as it is, since your Mac can use a different energy mode for each.

## tr126-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Mac laptop
- task: Turn on Low Power Mode (Mac laptop) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/101613

**USER:**
How do I turn on Low Power Mode on my MacBook?

**ASSISTANT:**
Here is how to turn it on.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **Battery**.
3. Under **Energy Mode**, open the **On battery** pop-up menu.
4. Choose **Low Power Mode**.

**USER:**
My Apple menu does not say System Settings. It says System Preferences.

**ASSISTANT:**
That means you have an older macOS. Use these steps.

1. Click the **Apple** menu and choose **System Preferences**.
2. Click **Battery**.
3. In the sidebar, click **Battery**, or **Power Adapter** if you want it while plugged in.
4. From the **Energy Mode** pop-up menu, choose **Low Power**.

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

Your Mac may ask whether to erase the drive. After setup, it starts backing up right away.

## tr127-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Mac
- task: Back up the Mac with Time Machine (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/104984

**USER:**
My son set up Time Machine on my iMac a while ago, and the backup drive is plugged in. I do not want to wait for the next automatic backup because I am about to install some new things and I want a fresh backup first. I do not need to set anything up again. How do I start a backup right now?

**ASSISTANT:**
You can start one right now from the menu bar.

1. Click the **Time Machine** menu in the menu bar at the top of the screen.
2. Choose **Back Up Now**.

You can use the same menu to see the progress, or to stop or skip a backup. It also shows the date and time of your latest backup. You can keep using your Mac while it backs up.

## tr127-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Back up the Mac with Time Machine (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/104984

**USER:**
my grandson says i should make a copy of everything on my computer in case it breaks. how

**ASSISTANT:**
I can help with that. Is your computer a **Mac** or a **Windows** computer?

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

Keep that password safe. You will need it to restore your files later. After setup, your Mac starts backing up right away.

## tr127-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Mac
- task: Back up the Mac with Time Machine (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/104984

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
