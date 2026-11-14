TASKS = [
    {
        "task_id": "TR-121",
        "task_type": "screenshot",
        "task": "Take a screenshot",
        "platform": "iPad",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: Take a screenshot on your iPad", "url": "https://support.apple.com/102500"},
        "source_notes": """No Home button: 1 Press the top button and either volume button at the same time. 2 Quickly release both. 3 A thumbnail briefly appears in the lower-left corner; tap it to open the screenshot, or swipe left to dismiss it.
Home button: 1 Press the top button and the Home button at the same time. 2 Quickly release both. 3 Same thumbnail in lower-left corner; tap to open or swipe left to dismiss.
Apple Pencil (models that support it): swipe your Apple Pencil from a bottom corner of either side of the screen.
Find screenshots: open Photos, tap Collections; swipe up, tap Media Types, tap Screenshots.
Troubleshooting: thumbnail disappears on its own after a short time, so tap it right away to open it. Page not covering: full-page screenshots, editing, deleting.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "iPad",
             "messages": [
                 "How do I take a screenshot on my iPad? It is the newer kind with no round Home button.",
                 """Here is how to take a screenshot on an iPad that has no Home button.

1. Press the top button and either volume button at the same time.
2. Quickly let go of both buttons.
3. A small picture of the screenshot shows in the lower-left corner for a moment. Tap it to open the screenshot, or swipe it left to dismiss it.

To find it later, open **Photos**, tap **Collections**, swipe up, tap **Media Types**, then tap **Screenshots**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "iPad",
             "messages": [
                 "My neighbor sent me a recipe on my iPad and I want to keep a picture of it so I can look at it in the kitchen. My iPad is the older one with the round Home button at the bottom of the screen. My grandson told me about taking a screenshot but I forgot how. What do I press?",
                 """Your iPad has a Home button, so here is how to do it.

1. Open the recipe so it is on the screen.
2. Press the top button and the Home button at the same time.
3. Quickly let go of both buttons.
4. A small picture of the screenshot shows in the lower-left corner for a moment. Tap it to open the screenshot, or swipe it left to dismiss it.

To find it later, open **Photos**, tap **Collections**, swipe up, tap **Media Types**, then tap **Screenshots**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "iPad",
             "messages": [
                 "I want to save a picture of what is on my iPad screen to show my daughter. How?",
                 "I can help with that. Does your iPad have a round **Home button** at the bottom, or **no Home button**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "iPad",
             "messages": [
                 "I want to save a picture of what is on my iPad screen to show my daughter. How?",
                 "I can help with that. Does your iPad have a round **Home button** at the bottom, or **no Home button**?",
                 "No button, the bottom is all smooth",
                 """Thank you. Here is how to do it on an iPad with no Home button.

1. Press the top button and either volume button at the same time.
2. Quickly let go of both buttons.
3. A small picture of the screenshot shows in the lower-left corner for a moment. Tap it to open the screenshot, or swipe it left to dismiss it.

To find it later, open **Photos**, tap **Collections**, swipe up, tap **Media Types**, then tap **Screenshots**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "iPad",
             "messages": [
                 "My hands are stiff from arthritis and I just cannot press two buttons at the same time on my iPad. I do have an Apple Pencil that came with it. Is there another way to take a screenshot using the Pencil?",
                 """Yes, if your iPad works with the Apple Pencil, you can use it instead of the buttons.

1. Swipe your Apple Pencil from a bottom corner of the screen. Either the left or the right corner works.
2. A small picture of the screenshot shows in the lower-left corner for a moment. Tap it to open the screenshot, or swipe it left to dismiss it.

Here is where to look for it afterward. Open **Photos**, tap **Collections**, swipe up, tap **Media Types**, then tap **Screenshots**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "iPad",
             "messages": [
                 "How do I take a screenshot on my iPad with a Home button?",
                 """Here is how to take a screenshot on an iPad with a Home button.

1. Press the top button and the Home button at the same time.
2. Quickly let go of both buttons.
3. A small picture of the screenshot shows in the lower-left corner for a moment. Tap it to open the screenshot, or swipe it left to dismiss it.

If you do not tap the picture right away, it goes away on its own.""",
                 "I did it but I was too slow and the little picture went away. Did I lose it?",
                 """It is not lost, the little picture just goes away by itself. Here is where to find your screenshot.

1. Open **Photos**.
2. Tap **Collections**.
3. Swipe up, then tap **Media Types**.
4. Tap **Screenshots**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-122",
        "task_type": "software_update",
        "task": "Update the Mac's software (macOS)",
        "platform": "Mac",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: Update macOS on Mac", "url": "https://support.apple.com/en-us/108382"},
        "source_notes": """Before: back up your Mac (page recommends before installing new software).
Steps: 1 Open Software Update: either click the Spotlight or Siri icon in the menu bar, search for Software Update and open it; or choose System Settings from the Apple menu, click General in the sidebar, then click Software Update on the right. 2 It automatically checks for updates for your Mac model. 3 If update available: click the button to update, upgrade, or restart now. If none: reports your Mac is up to date; to check again click Check for Updates, press Command-R, or close and reopen Software Update. 4 When prompted, enter your administrator password (the one you use to log in to the Mac). 5 Let installation finish: keep the Mac from sleeping and do not close its lid. Mac may restart several times and show a progress bar or blank screen.
Software Update only shows updates compatible with your Mac model; if not compatible it will not be offered and it says Mac is up to date.
Page links to guides for installation errors, Mac not fully starting, reinstalling from macOS Recovery; no details of those. Older Macs without Software Update: no steps on page.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "How do I update the software on my MacBook?",
                 """Here is how to update your Mac.

1. Click the **Apple** menu at the top left of the screen and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Software Update** on the right. Your Mac checks for updates by itself.
4. If an update is shown, click the button to update, upgrade, or restart now.
5. If asked, type your administrator password. This is the password you use to log in to your Mac.
6. Let it finish. Do not let the Mac go to sleep or close its lid. It may restart a few times and show a progress bar or a blank screen.

It is a good idea to back up your Mac before you install new software.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "Hello, my iMac keeps telling me something about software but I never know what to do and I do not want to break anything. My nephew set it up for me last year. I would like to update the macOS on it. Is there a quick way to get to the update screen using search instead of clicking through lots of menus?",
                 """Yes, you can use search to get there.

1. Click the **Spotlight** or **Siri** icon in the menu bar at the top of the screen.
2. Type **Software Update** and open it from the results.
3. Your Mac checks for updates by itself. If one is shown, click the button to update, upgrade, or restart now.
4. If asked, type your administrator password. This is the password you use to log in to your Mac.
5. Let it finish. Do not let the Mac go to sleep. It may restart a few times and show a progress bar or a blank screen.

Before installing, it is wise to back up your Mac.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "it says i need to update my apple thing. what do i do",
                 "I can help with that. Which device is it: a **Mac**, an **iPhone**, or an **iPad**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "it says i need to update my apple thing. what do i do",
                 "I can help with that. Which device is it: a **Mac**, an **iPhone**, or an **iPad**?",
                 "its my mac",
                 """Thank you. Here is how to update your Mac. Before you install anything, it is a good idea to back up your Mac.

1. Click the **Apple** menu at the top left of the screen and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Software Update** on the right. Your Mac checks for updates by itself.
4. If an update is shown, click the button to update, upgrade, or restart now.
5. If asked, type your administrator password. This is the password you use to log in to your Mac.
6. Let it finish. Do not let the Mac go to sleep or close its lid.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "I am not ready to install anything on my Mac today because I am in the middle of tax paperwork. I only want to look and see whether an update is waiting for me, without actually installing it. How do I look?",
                 """You can look without installing anything.

1. Click the **Apple** menu at the top left of the screen and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Software Update** on the right. Your Mac checks for updates by itself.
4. Read what it shows. If an update is waiting, you will see a button to update, upgrade, or restart now. Do not click it, and nothing will install.
5. If it says your Mac is up to date, there is nothing waiting.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "How do I check for a macOS update on my Mac?",
                 """Here is how to check for an update on your Mac.

1. Click the **Apple** menu at the top left of the screen and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Software Update** on the right. Your Mac checks for updates by itself.
4. If an update is shown, click the button to update, upgrade, or restart now.
5. If asked, type your administrator password.
6. Let it finish and do not close the lid.""",
                 "It just says my Mac is up to date, but my friend has a newer version on hers. Is it wrong?",
                 """It may not be wrong. Here is what to try.

1. Click **Check for Updates** to look again. You can also press Command-R, or close and reopen **Software Update**.
2. If it still says up to date, that may be because Software Update only shows updates that work with your Mac model. A newer version that does not work with your Mac will not be offered.""",
             ]},
        ],
    },
    {
        "task_id": "TR-123",
        "task_type": "wifi_connect",
        "task": "Connect to a Wi-Fi network",
        "platform": "Mac",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: Connect your Mac to the internet using Wi-Fi", "url": "https://support.apple.com/guide/mac-help/mchlp1180"},
        "source_notes": """Have the network password ready.
Join a public Wi-Fi network: 1 Click the Wi-Fi status menu in the menu bar, then choose the network. 2 If the network is not listed, click Other Networks to show nearby networks. 3 If prompted, enter the password and click Join.
Join a hidden Wi-Fi network: 1 Click the Wi-Fi status menu in the menu bar, click Other Networks, then click Other at the bottom of the list. 2 In the Network Name field, enter the network's name. 3 Click the Security pop-up menu and choose the network's security type. 4 Fill in any additional fields that appear, such as user name and password, then click Join.
Other page (support.apple.com/en-qa/101589): click the Wi-Fi icon in the menu bar, choose a network; if prompted enter password or accept terms and conditions.
No System Settings steps on the page. No steps for a missing Wi-Fi icon.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "How do I connect my MacBook to the Wi-Fi at my house?",
                 """Here is how to join a Wi-Fi network on your Mac. Make sure Wi-Fi is turned on and have the Wi-Fi password ready.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen. It is the Wi-Fi icon.
2. Click the name of your network in the list.
3. If it asks for a password, type it and click **Join**.

If you do not see your network in the list, click **Other Networks** to show the nearby networks.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "My son set up a new router for me and he told me the network is hidden so my neighbors cannot see it. He wrote the network name and the password on a sticky note. Now my iMac will not find it anywhere in the list. How do I connect my iMac to a hidden network?",
                 """For a hidden network, you type the name yourself. Make sure Wi-Fi is turned on, and have the network name, security type, and password from the sticky note ready.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen.
2. Click **Other Networks**.
3. Click **Other** at the bottom of the list.
4. In the **Network Name** box, type the network name from your sticky note.
5. Click the **Security** pop-up menu and choose the security type your network uses.
6. Fill in any other boxes that appear, such as a user name and the password, then click **Join**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my laptop is not on the internet, how do i get it on the wifi",
                 "I can help with that. Is your laptop a **Mac** (MacBook) or a **Windows** laptop?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "my laptop is not on the internet, how do i get it on the wifi",
                 "I can help with that. Is your laptop a **Mac** (MacBook) or a **Windows** laptop?",
                 "macbook",
                 """Thank you. Here is how to join a Wi-Fi network on your MacBook. Make sure Wi-Fi is turned on and have the Wi-Fi password ready.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen. It is the Wi-Fi icon.
2. Click the name of your network in the list.
3. If it asks for a password, type it and click **Join**.

If you do not see your network, click **Other Networks** to show the nearby networks.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "I am at the library with my MacBook and I do not want to dig around in settings, I get lost in there. Just tell me the quickest way to connect to the library Wi-Fi from the top of the screen.",
                 """You can do it from the top of the screen, no settings needed. Make sure Wi-Fi is turned on.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen. It is the Wi-Fi icon.
2. Click the library network in the list.
3. If it asks for a password, type it and click **Join**.

If you do not see the library network, click **Other Networks** to show the nearby networks.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "How do I join my home Wi-Fi on my Mac?",
                 """Here is how to join your Wi-Fi on your Mac. Have the password ready.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen.
2. Click the name of your network.
3. If it asks for a password, type it and click **Join**.""",
                 "I clicked the Wi-Fi icon but my network is not in the list.",
                 """Try this.

1. Click the **Wi-Fi status menu** in the menu bar again.
2. Click **Other Networks**. This shows the nearby networks.
3. Click your network's name.
4. If it asks for a password, type it and click **Join**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-124",
        "task_type": "delete_app",
        "task": "Delete (uninstall) an app",
        "platform": "Mac",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: Uninstall apps on your Mac", "url": "https://support.apple.com/en-us/102610"},
        "source_notes": """1 Quit the app if it is open. 2 Find the app in Finder: search with Spotlight, then hold Command and double-click the app in results to show it in Finder; or click Applications in the Finder sidebar, or choose Go > Applications in the menu bar. Some apps are in the Applications folder inside your home folder (Go > Home). 3 Non-Apple apps: look for an app named Uninstall or Uninstaller, maybe in the same folder; using it removes the app plus login items, extensions, other data. Some apps have an uninstall/remove/reset option in their menus or settings. 4 If no uninstaller: drag the app to the Trash, or select it and choose File > Move to Trash. 5 If prompted, enter the name and password of an administrator account (usually the one you log in with). 6 Choose Finder > Empty Trash to permanently delete; this frees the storage space.
Cannot delete: apps required by macOS (Mail, Music, Books, Notes, Podcasts, Maps, News, Stocks); apps in the System folder.
Troubleshooting: if Mac says app is in use, make sure it is not open; if it still will not delete, restart the Mac or start up in Safe Mode and try again.
Notes: deleting an app does not remove documents or files you created with it, but you may need the app to open them. Deleting an app does not cancel subscriptions bought through it.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "How do I delete a game I downloaded from the internet on my Mac? I do not play it anymore.",
                 """Here is how to remove it.

1. If the game is open, quit it first.
2. Open a **Finder** window and click **Applications** in the sidebar.
3. Find the game. If it came with an app called **Uninstall** or **Uninstaller**, open that and follow it. That also removes the extra files it left behind.
4. If there is no uninstaller, drag the game to the **Trash**.
5. If asked, type your administrator name and password. This is usually what you use to log in.
6. In the menu bar, choose **Finder**, then **Empty Trash**. This deletes it for good and frees up space.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "My MacBook has so many programs on it that I never use and I think it is making things slow. I know the name of one of them, a photo editing app that a friend told me to install. I do not see it on my Dock. I can search for it with the magnifying glass though. How can I get rid of it?",
                 """You can use that search to find it.

1. If the app is open, quit it first.
2. Use the search (**Spotlight**) to find the app. Hold the **Command** key and double-click the app in the results. This shows it in **Finder**.
3. Look for an app named **Uninstall** or **Uninstaller**, possibly in the same folder. If you find one, open it and follow it.
4. If there is none, drag the app to the **Trash**, or select it and choose **File**, then **Move to Trash**.
5. If asked, type your administrator name and password.
6. Choose **Finder**, then **Empty Trash**.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "i want to delete an app i dont use",
                 "I can help with that. Is the app on an **iPhone**, an **iPad**, or a **Mac**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "i want to delete an app i dont use",
                 "I can help with that. Is the app on an **iPhone**, an **iPad**, or a **Mac**?",
                 "mac",
                 """Thank you. Here is how to delete an app on your Mac.

1. If the app is open, quit it first.
2. Open a **Finder** window and click **Applications** in the sidebar.
3. Find the app. If it has an **Uninstall** or **Uninstaller** app next to it, use that instead and follow it.
4. Otherwise, drag the app to the **Trash**.
5. If asked, type your administrator name and password.
6. In the menu bar, choose **Finder**, then **Empty Trash**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "I want to delete a writing program from my Mac because I stopped using it, but I have a lot of old letters I wrote in it and I do NOT want to lose those. Will deleting it get rid of my letters too? And what do I do?",
                 """No, deleting the app does not delete the letters or files you made with it. You might need an app to open them later, though.

1. If the writing program is open, quit it first.
2. Open a **Finder** window and click **Applications** in the sidebar.
3. Find the program and look for an **Uninstall** or **Uninstaller** app. If there is one, use it.
4. If there is none, drag the program to the **Trash**.
5. If asked, type your administrator name and password.
6. Choose **Finder**, then **Empty Trash**.

Deleting an app also does not cancel any subscription you bought through it.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Mac",
             "sources": [{'title': 'Apple Support: Uninstall apps on your Mac', 'url': 'https://support.apple.com/en-us/102610', 'accessed': '2026-11-13'}, {'title': 'Apple Support: Start up your Mac in safe mode', 'url': 'https://support.apple.com/en-us/116946', 'accessed': '2026-11-13'}],
             "messages": [
                 "How do I delete an app from my Mac?",
                 """Here is how to delete an app on your Mac.

1. If the app is open, quit it first.
2. Open a **Finder** window and click **Applications** in the sidebar.
3. Find the app. If it has an **Uninstall** or **Uninstaller** app, use that.
4. Otherwise, drag the app to the **Trash**.
5. If asked, type your administrator name and password.
6. Choose **Finder**, then **Empty Trash**.""",
                 "My Mac says the app is in use and will not let me delete it.",
                 """Try this.

1. Make sure the app is not open. Quit it.
2. Try to delete it again.
3. If it still will not delete, restart your Mac and try again.

If that does not work, Apple has a guide called start up in Safe Mode: https://support.apple.com/en-us/116946.""",
             ]},
        ],
    },
    {
        "task_id": "TR-125",
        "task_type": "free_storage",
        "task": "Free up storage space",
        "platform": "Mac",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: Free up storage space on your Mac", "url": "https://support.apple.com/en-us/102624"},
        "source_notes": """1 Check space: macOS Ventura 13 or later: Apple menu > System Settings > General in sidebar > Storage. Earlier versions: Apple menu > About This Mac, then click Storage. Screen breaks down space by category and updates as you free space. Where a More Info button is next to a category, click it for management options (most useful for Applications, Documents, Messages, Music Creation, Podcasts, Trash, TV). System Data (or Other) = files that do not fit another category.
2 Optimize storage (optional): uses iCloud; follow Apple's guide for your macOS version (no steps on page). iCloud files count against iCloud plan.
3 Move files to another drive: if you have an external drive, move files to it; photos and videos are common candidates. Separate guides exist for moving Photos library and iMovie library (no steps on page).
4 Delete media you can re-download or stream (music, movies, podcasts).
5 Clear Downloads folder: open Downloads from the Dock, or click Downloads in Finder sidebar, or Go > Downloads in Finder menu bar; delete what you do not need.
6 Mail app: Mailbox > Erase Junk Mail, then Mailbox > Erase Deleted Items.
7 Delete old iPhone or iPad backups stored on the Mac.
8 Delete or uninstall unused apps.
9 Multi-user Macs: remove unneeded user accounts.
10 Compress files you want to keep; expand when needed.
11 Empty the Trash: space from trashed files is not freed until you empty it.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Mac",
             "sources": [{'title': 'Apple Support: Free up storage space on your Mac', 'url': 'https://support.apple.com/en-us/102624', 'accessed': '2026-11-13'}, {'title': 'Apple Support: Uninstall apps on your Mac', 'url': 'https://support.apple.com/en-us/102610', 'accessed': '2026-11-13'}],
             "messages": [
                 "My MacBook is almost full. How can I free up some space?",
                 """Here are some good ways to free up space.

1. Click the **Apple** menu, choose **System Settings**, click **General**, then click **Storage**. This shows what is using your space.
2. Open your **Downloads** folder from the Dock and delete what you do not need.
3. Open a Finder window, click **Applications** in the sidebar, then drag an app you no longer use to the **Trash**.
4. Click **Finder** in the menu bar at the top, then choose **Empty Trash**. Space from trashed files is not freed until you do.

The Storage screen updates as you free up space.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "I have an old iMac that my husband bought years ago and it is not on the newest macOS, definitely older than Ventura. It keeps saying the disk is nearly full and I cannot save my family pictures anymore. I would like to see what is taking up all the room and then clear some of it. Where do I begin?",
                 """Start by looking at what is using the space.

1. Click the **Apple** menu and choose **About This Mac**.
2. Click **Storage**. It shows your space by category.
3. Next to a category, click **More Info** if you see it. It gives you ways to manage that category.
4. Delete things you do not need, such as files in your **Downloads** folder or apps you no longer use.
5. Empty the **Trash**. Space from trashed files is not freed until you do.

The Storage screen updates as you free up space.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "it says my storage is full. how do i clear some space",
                 "I can help with that. Is the full storage on an **iPhone**, an **iPad**, or a **Mac**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "it says my storage is full. how do i clear some space",
                 "I can help with that. Is the full storage on an **iPhone**, an **iPad**, or a **Mac**?",
                 "the mac",
                 """Thank you. Here are some good ways to free up space on your Mac.

1. Click the **Apple** menu, choose **System Settings**, click **General**, then click **Storage**. This shows what is using your space.
2. Open your **Downloads** folder from the Dock and delete what you do not need.
3. Delete apps you no longer use.
4. Empty the **Trash**. Space from trashed files is not freed until you do.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Mac",
             "sources": [{'title': 'Apple Support: Free up storage space on your Mac', 'url': 'https://support.apple.com/en-us/102624', 'accessed': '2026-11-13'}, {'title': 'Apple Support: Move your Photos library to save space on your Mac', 'url': 'https://support.apple.com/en-us/108345', 'accessed': '2026-11-13'}],
             "messages": [
                 "My Mac is full because of my grandchildren's photos and videos, and I refuse to delete any of them. I have a spare external hard drive in my drawer though. What can I do to free up space without throwing away a single photo?",
                 """You can move them to the external drive instead of deleting them. Moving the Photos library keeps your photos.

1. Make sure the drive is formatted as **APFS** or **Mac OS Extended (Journaled)**. Do not use a drive that holds Time Machine backups, an SD card, or a USB flash drive.
2. Quit **Photos**.
3. Open a Finder window and open the **Pictures** folder in your home folder, where **Photos Library** is.
4. Drag **Photos Library** onto the external drive.
5. When the move finishes, double-click **Photos Library** on the drive to open it. Check that your photos are there.
6. Optional: to free space on your Mac, drag the old **Photos Library** from the Pictures folder to the **Trash**, then choose **Finder** > **Empty Trash**. Your library stays on the drive.
7. Click the **Apple** menu, choose **System Settings**, click **General**, then click **Storage** to check how much space you now have.

Keep the drive plugged in and turned on before you open Photos, or Photos will create a new empty library in your Pictures folder.

More help: https://support.apple.com/en-us/108345""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "How do I see what is using up the storage on my Mac?",
                 """Here is how to see it.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Storage**. It shows your space by category.
4. Next to a category, click **More Info** if you see it for ways to manage it.""",
                 "I do not see Storage under General. My Mac is very old.",
                 """On an older version of macOS, it is in a different place.

1. Click the **Apple** menu.
2. Choose **About This Mac**.
3. Click **Storage**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-126",
        "task_type": "battery_saver",
        "task": "Turn on Low Power Mode",
        "platform": "Mac laptop",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: About Power Modes on your Mac", "url": "https://support.apple.com/101613"},
        "source_notes": """macOS Ventura or later: 1 Apple menu > System Settings (Monterey or earlier: System Preferences). 2 Click Battery (on laptops). 3 Under Energy Mode, open the On battery pop-up menu, the On power adapter pop-up menu, or both, depending on when you want Low Power Mode on. 4 Choose Low Power Mode.
macOS Sequoia 15.1 or later: can also choose Energy Modes from Control Center (no steps given).
Monterey or earlier: Apple menu > System Preferences, click Battery; click Battery or Power Adapter in the sidebar; choose Low Power from the Energy Mode pop-up menu.
What you see: click the Battery (or lightning bolt) icon in the menu bar to see battery status menu, which shows whether a Power Mode is on.
Notes: Low Power Mode reduces energy use to extend battery life. Mac uses Automatic Mode by default. Can set different Energy Mode for battery and power adapter. Works whether or not connected to power.
Laptops listed with reduced power consumption: MacBook Air 2024 or later; MacBook Pro 2024 or later; MacBook Pro 2021 to 2023 with Max chip.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Mac laptop",
             "messages": [
                 "How do I turn on Low Power Mode on my MacBook to make the battery last longer?",
                 """Here is how to turn it on.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **Battery**.
3. Under **Energy Mode**, open the **On battery** pop-up menu.
4. Choose **Low Power Mode**.

To use it while plugged in too, do the same in the **On power adapter** pop-up menu.

To check, click the battery icon in the menu bar. It shows whether a power mode is on.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Mac laptop",
             "messages": [
                 "I have an older MacBook Pro running Monterey, and I take it on the train every day and the battery drains before I get home. My daughter said there is a battery saving setting called Low Power or something. On my Mac the settings app is called System Preferences. How do I turn it on?",
                 """Yes, on Monterey it is in System Preferences.

1. Click the **Apple** menu and choose **System Preferences**.
2. Click **Battery**.
3. In the sidebar, click **Battery**. If you also want it while plugged in, click **Power Adapter** instead.
4. From the **Energy Mode** pop-up menu, choose **Low Power**.

To check, click the battery icon in the menu bar. It shows whether a power mode is on.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "how do i turn on battery saver",
                 "I can help with that. Is the device an **iPhone**, an **iPad**, or a **Mac laptop**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Mac laptop",
             "messages": [
                 "how do i turn on battery saver",
                 "I can help with that. Is the device an **iPhone**, an **iPad**, or a **Mac laptop**?",
                 "mac laptop",
                 """Thank you. On a Mac laptop it is called Low Power Mode.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **Battery**.
3. Under **Energy Mode**, open the **On battery** pop-up menu.
4. Choose **Low Power Mode**.

If your Apple menu says System Preferences instead of System Settings, tell me and I will give you the steps for that.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Mac laptop",
             "messages": [
                 "I only want Low Power Mode on my MacBook when it is plugged into the charger at my desk, because I do not want my Mac to feel slower when I am using the battery. It is on a recent macOS with System Settings. How do I set it just for when it is plugged in?",
                 """You can set it for the charger only.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **Battery**.
3. Under **Energy Mode**, open the **On power adapter** pop-up menu.
4. Choose **Low Power Mode**.

Leave the **On battery** menu as it is, since your Mac can use a different energy mode for each.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Mac laptop",
             "messages": [
                 "How do I turn on Low Power Mode on my MacBook?",
                 """Here is how to turn it on.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **Battery**.
3. Under **Energy Mode**, open the **On battery** pop-up menu.
4. Choose **Low Power Mode**.""",
                 "My Apple menu does not say System Settings. It says System Preferences.",
                 """That means you have an older macOS. Use these steps.

1. Click the **Apple** menu and choose **System Preferences**.
2. Click **Battery**.
3. In the sidebar, click **Battery**, or **Power Adapter** if you want it while plugged in.
4. From the **Energy Mode** pop-up menu, choose **Low Power**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-127",
        "task_type": "backup_computer",
        "task": "Back up the Mac with Time Machine",
        "platform": "Mac",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Apple Support: Back up your Mac with Time Machine", "url": "https://support.apple.com/en-us/104984"},
        "source_notes": """Prepare: connect an external storage device (USB or Thunderbolt drive) to a compatible port. Use a drive with at least twice your Mac's storage capacity; use it only for Time Machine backups.
Setup (macOS Ventura 13 or later): 1 Apple menu > System Settings. 2 Click General in sidebar, then Time Machine on the right. 3 Click Add Backup Disk (or the Add button). 4 Select your connected device, click Set Up Disk. During setup: Mac may ask whether to erase the device (you can erase it or choose a different backup disk or volume); may ask whether to claim existing backups from another computer; if you turn on Encrypt Backup you create a backup password, needed later to restore files. 5 After setup the Mac immediately starts backing up.
Back up now: click the Time Machine menu in the menu bar, choose Back Up Now (or wait for next automatic backup). Same menu lets you stop or skip a backup or check progress; shows progress or date and time of latest backup.
Notes: hourly backups for past 24 hours, daily for the past month, weekly for earlier months; oldest deleted when disk fills. First backup can take longer than expected; you can keep using the Mac during it. Before disconnecting the backup disk, eject it or shut down the Mac. Restore steps not on page.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "How do I set up Time Machine to back up my Mac? I just bought an external hard drive.",
                 """Here is how to set it up. Use a drive that is at least twice the size of your Mac's storage, and only for Time Machine.

1. Plug the external drive into your Mac.
2. Click the **Apple** menu and choose **System Settings**.
3. Click **General** in the sidebar, then click **Time Machine** on the right.
4. Click **Add Backup Disk**.
5. Select your drive, then click **Set Up Disk**.

If your Mac asks whether to erase the drive, erasing wipes everything on it. Erase only if you do not need anything on it, or choose a different backup disk instead. After setup, it starts backing up right away.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "My son set up Time Machine on my iMac a while ago, and the backup drive is plugged in. I do not want to wait for the next automatic backup because I am about to install some new things and I want a fresh backup first. I do not need to set anything up again. How do I start a backup right now?",
                 """You can start one right now from the menu bar.

1. Click the **Time Machine** menu in the menu bar at the top of the screen.
2. Choose **Back Up Now**.

You can use the same menu to see the progress, or to stop or skip a backup. It also shows the date and time of your latest backup. You can keep using your Mac while it backs up.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my grandson says i should make a copy of everything on my computer in case it breaks. how",
                 "I can help with that. Is your computer a **Mac** or a **Windows** computer?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "my grandson says i should make a copy of everything on my computer in case it breaks. how",
                 "I can help with that. Is your computer a **Mac** or a **Windows** computer?",
                 "its a mac",
                 """Thank you. On a Mac you use Time Machine with an external drive. Use a drive at least twice the size of your Mac's storage, only for backups.

1. Plug the external drive into your Mac.
2. Click the **Apple** menu and choose **System Settings**.
3. Click **General** in the sidebar, then click **Time Machine** on the right.
4. Click **Add Backup Disk**.
5. Select your drive, then click **Set Up Disk**.

If your Mac asks whether to erase the drive, erasing wipes everything on it. Erase only if you do not need anything on it, or choose a different backup disk instead.

After setup, your Mac starts backing up right away.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "I keep tax records and bank papers on my MacBook, so I want my Time Machine backup to be protected with a password in case someone takes the backup drive. I have the drive plugged in already. How do I set up Time Machine so the backup needs a password?",
                 """You can turn on encryption when you set up the backup.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **General** in the sidebar, then click **Time Machine** on the right.
3. Click **Add Backup Disk**.
4. Select your drive, then click **Set Up Disk**.
5. During setup, turn on **Encrypt Backup**, then create a backup password.

If your Mac asks whether to erase the drive, erasing wipes everything on it. Erase only if you do not need anything on it, or choose a different backup disk instead.

Keep that password safe. You will need it to restore your files later. After setup, your Mac starts backing up right away.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Mac",
             "messages": [
                 "How do I set up Time Machine on my Mac? I have a USB drive plugged in.",
                 """Here is how to set it up. Use a drive at least twice the size of your Mac's storage, and only for Time Machine.

1. Click the **Apple** menu and choose **System Settings**.
2. Click **General** in the sidebar, then click **Time Machine** on the right.
3. Click **Add Backup Disk**.
4. Select your USB drive, then click **Set Up Disk**.""",
                 "It is asking if I want to erase the drive but I have family photos on that drive!",
                 """Do not erase it, then. Your Mac lets you pick a different drive instead.

1. Do not agree to erase the drive.
2. Choose a different backup disk or volume when it asks.
3. Use a drive that you only use for Time Machine backups.""",
             ]},
        ],
    },
]
