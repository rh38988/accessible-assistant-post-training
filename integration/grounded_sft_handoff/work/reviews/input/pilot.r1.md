# Review input: pilot, round 1 (19 candidates)

## gsft-battery_saver-01
- candidate_id: gsft-battery_saver-01-v1
- conversation_sha256: 48a438f10a26de935a988c11cfd2c45a7b7af454672abb669d398e289dfcfe86
- task_group: battery_saver | behavior: direct | tags: conditional, distractor
- route: answer
- decision basis (writer's): The user names an iPhone 15 Pro, which falls under the iPhone 15 and later steps. The iPhone 14 and earlier steps are the inapplicable distractor. The 80% auto-off condition and the yellow battery icon come from the same section and are kept as conditions.

Conversation (the model sees only the user turns, joined):
> **user:** I have an iPhone 15 Pro and my battery is gone by lunchtime every day. How do I turn on Low Power Mode? I'm not very techy so simple steps please.

Passages the model sees (in this order):
- [battery-saver-iphone15-settings] platform: iPhone | app: Settings
  > On iPhone 15 and later: 1. Open Settings. 2. Tap Battery. 3. Tap Power Mode. 4. Tap to turn Low Power Mode on or off.
- [battery-saver-iphone-80pct] platform: iPhone | app: Status bar
  > On iPhone: When you charge the device to 80% or higher, Low Power Mode turns off. When Low Power Mode is active, the battery icon in the status bar turns yellow.
- [battery-saver-iphone14-settings] platform: iPhone | app: Settings
  > On iPhone 14 and earlier: 1. Open Settings. 2. Tap Battery. 3. Tap to turn Low Power Mode on or off.

Source references to check:
- battery-saver-iphone15-settings: Apple, "Use Low Power Mode to save battery life on your iPhone or iPad - Apple Support" <https://support.apple.com/en-us/101604> | section: Turn Low Power Mode on or off | applicability: iPhone 15 and later | excerpt: "Tap to turn Low Power Mode on or off."
- battery-saver-iphone-80pct: Apple, "Use Low Power Mode to save battery life on your iPhone or iPad - Apple Support" <https://support.apple.com/en-us/101604> | section: Turn Low Power Mode on or off | applicability: iPhone; the page gives these as conditions of Low Power Mode | excerpt: "When you charge the device to 80% or higher, Low Power Mode turns off. When Low Power Mode is active, the battery icon in the status bar turns yellow."
- battery-saver-iphone14-settings: Apple, "Use Low Power Mode to save battery life on your iPhone or iPad - Apple Support" <https://support.apple.com/en-us/101604> | section: Turn Low Power Mode on or off | applicability: iPhone 14 and earlier | excerpt: "Tap to turn Low Power Mode on or off."

TARGET (read only after step 2)

> Here is how to turn on Low Power Mode on your iPhone 15 Pro:
> 1. Open **Settings**.
> 2. Tap **Battery**.
> 3. Tap **Power Mode**.
> 4. Tap to turn **Low Power Mode** on or off.
> 
> Low Power Mode turns off when you charge your iPhone to 80% or higher. While it is on, the battery icon in the status bar turns yellow.

---

## gsft-battery_saver-02
- candidate_id: gsft-battery_saver-02-v1
- conversation_sha256: c8aa8c284ea3d60cfbb4767bbcbb216ca73504c06869ae88a301265cacd94b07
- task_group: battery_saver | behavior: direct | tags: conditional, distractor
- route: answer
- decision basis (writer's): The user names a Windows 11 laptop and asks for automatic turn-on at a low battery level. The Windows 11 battery-level steps apply and the Mac steps are the inapplicable distractor. The page's condition that energy saver turns on whenever the battery falls below the chosen level is kept.

Conversation (the model sees only the user turns, joined):
> **user:** My Windows 11 laptop seems to die really fast since I got a new work bag and started using it on the train. I don't want to keep checking the battery myself. Is there a way to have energy saver come on by itself when the battery gets low? I'd like it to happen without me doing anything each day.

Passages the model sees (in this order):
- [battery-saver-win11-batterylevel] platform: Windows 11 laptop | app: Settings
  > On Windows 11: If you want Energy saver to turn on whenever the battery falls below a certain level, follow these steps. 1. Select Start, then Settings, then System, then Power & battery. 2. Select Energy saver to expand the options. 3. Next to Turn energy saver on when battery level is at, select the battery level you'd like.
- [battery-saver-mac-energymode] platform: Mac | app: System Settings
  > On Mac laptop (macOS Ventura or later): 1. From the Apple menu, choose System Settings, then click Battery. 2. Under Energy Mode, choose Low Power Mode, Automatic, or High Power Mode from the 'On battery' or the 'On power adapter' pop-up menu. Power Modes can be used whether your Mac is connected to power or not.

Source references to check:
- battery-saver-win11-batterylevel: Microsoft, "Battery saving tips for Windows | Microsoft Support" <https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99> | section: Use energy saver | applicability: Windows 11 (the page's Applies To line names Windows 11 and Windows 10) | excerpt: "If you want energy saver to turn on whenever the battery falls below a certain level"
- battery-saver-mac-energymode: Apple, "About Power Modes on your Mac - Apple Support" <https://support.apple.com/101613> | section: Select a Power Mode | applicability: Mac laptop with macOS Ventura or later for these steps | excerpt: "Power Modes can be used whether your Mac is connected to power or not."

TARGET (read only after step 2)

> Here is how to have Energy saver turn on by itself on your Windows 11 laptop:
> 1. Select **Start**, then **Settings**, then **System**, then **Power & battery**.
> 2. Select **Energy saver** to expand the options.
> 3. Next to **Turn energy saver on when battery level is at**, select the battery level you'd like.
> 
> Energy saver then turns on whenever the battery falls below the level you picked.

---

## gsft-battery_saver-03
- candidate_id: gsft-battery_saver-03-v1
- conversation_sha256: 3899b7cf8cd745ec068254882283bfc0e914fcec6797c22dfdabc3e25972b018
- task_group: battery_saver | behavior: clarify | tags: conditional
- route: clarify | routed question: Is your laptop a Mac or a Windows computer?
- decision basis (writer's): The user does not name the device. The Mac steps (System Settings, Battery, Energy Mode) and the Windows 11 steps (Settings, System, Power & battery, Energy saver) differ, so one question is needed before answering.

Conversation (the model sees only the user turns, joined):
> **user:** My laptop battery is dying way too fast. How do I make it last longer?

Passages the model sees: none (clarify route)

Source references to check:
- battery-saver-mac-energymode: Apple, "About Power Modes on your Mac - Apple Support" <https://support.apple.com/101613> | section: Select a Power Mode | applicability: Mac laptop with macOS Ventura or later for these steps | excerpt: "Power Modes can be used whether your Mac is connected to power or not."
- battery-saver-win11-batterylevel: Microsoft, "Battery saving tips for Windows | Microsoft Support" <https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99> | section: Use energy saver | applicability: Windows 11 (the page's Applies To line names Windows 11 and Windows 10) | excerpt: "If you want energy saver to turn on whenever the battery falls below a certain level"

TARGET (read only after step 2)

> Is your laptop a Mac or a Windows computer?

---

## gsft-battery_saver-04
- candidate_id: gsft-battery_saver-04-v1
- conversation_sha256: 1710d222c890013649263743c2125b791f6a2b89a9df2c1aea847ac424253c3c
- task_group: battery_saver | behavior: clarify | tags: none
- route: clarify | routed question: Is your phone an iPhone or an Android phone?
- decision basis (writer's): The user does not name the phone. The iPhone steps (Settings, Battery, Power Mode or the Low Power Mode toggle) and the Android steps (Settings, Battery, Battery Saver) differ, so the device must be known first.

Conversation (the model sees only the user turns, joined):
> **user:** my phone battery is at 15% by noon every day. how do i turn on the saving mode thing

Passages the model sees: none (clarify route)

Source references to check:
- battery-saver-iphone15-settings: Apple, "Use Low Power Mode to save battery life on your iPhone or iPad - Apple Support" <https://support.apple.com/en-us/101604> | section: Turn Low Power Mode on or off | applicability: iPhone 15 and later | excerpt: "Tap to turn Low Power Mode on or off."
- battery-saver-android-manual: Google, "Get the most life from your Android device's battery" <https://support.google.com/android/answer/7664692?hl=en> | section: Stretch a low battery > Turn on battery saver mode manually | applicability: Android; the page says some of these steps work only on Android 13 and up, without saying which ones | excerpt: "Some of these steps work only on Android 13 and up."

TARGET (read only after step 2)

> Is your phone an iPhone or an Android phone?

---

## gsft-battery_saver-05
- candidate_id: gsft-battery_saver-05-v1
- conversation_sha256: d2bba8764117493a048c551a7bf6d39e519446e535d69cbc12e6a7cceacb73ad
- task_group: battery_saver | behavior: clarify | tags: none
- route: clarify | routed question: Is your phone a Samsung Galaxy, or another brand of Android phone?
- decision basis (writer's): The user does not name the phone. The Samsung Galaxy steps (Settings, Battery, Power saving) and the generic Android steps (Settings, Battery, Battery Saver) differ, so the brand must be known first.

Conversation (the model sees only the user turns, joined):
> **user:** My phone keeps running out of charge before the day ends. Is there a power saving setting I can use?

Passages the model sees: none (clarify route)

Source references to check:
- battery-saver-samsung-power-saving: Samsung, "Get the most out of your Galaxy phone or tablet battery" <https://www.samsung.com/us/support/answer/ANS10002534> | section: Power saving mode | applicability: Samsung Galaxy phone or tablet; the page says available screens and settings may vary by wireless service provider, software version, and model | excerpt: "apps running in the background may not receive updates or send you notifications when Power saving mode is enabled."
- battery-saver-android-manual: Google, "Get the most life from your Android device's battery" <https://support.google.com/android/answer/7664692?hl=en> | section: Stretch a low battery > Turn on battery saver mode manually | applicability: Android; the page says some of these steps work only on Android 13 and up, without saying which ones | excerpt: "Some of these steps work only on Android 13 and up."

TARGET (read only after step 2)

> Is your phone a Samsung Galaxy, or another brand of Android phone?

---

## gsft-battery_saver-06
- candidate_id: gsft-battery_saver-06-v1
- conversation_sha256: 3a35f5a62973de1b5c7ddd8451b85c447a6cf4cb14693ebccbcbe07a348cc648
- task_group: battery_saver | behavior: constraint | tags: conditional, distractor
- route: answer
- decision basis (writer's): The user names a Samsung Galaxy phone, so the Samsung steps apply and the generic Android steps are the inapplicable distractor. The user's no-missed-notifications limit is respected by stating the page's note that background apps may not send notifications. The page's note that settings cannot be changed once the mode is on is kept as a condition.

Conversation (the model sees only the user turns, joined):
> **user:** I have a Samsung Galaxy phone. My son is supposed to text me about a ride home tonight and I really can't miss any notifications. Can I still turn on power saving? How do I do it?

Passages the model sees (in this order):
- [battery-saver-samsung-power-saving] platform: Samsung Galaxy | app: Settings
  > On Samsung Galaxy: 1. Open Settings, then tap Battery. 2. Tap Power saving. 3. Tap the switches next to your desired settings or customizations. 4. Tap the switch at the top of the screen to activate Power saving mode. You will not be able to adjust the settings once the mode is enabled. Apps running in the background may not receive updates or send you notifications when Power saving mode is enabled.
- [battery-saver-android-manual] platform: Android | app: Settings
  > On Android (some of these steps work only on Android 13 and up): 1. Open the Settings app. 2. Tap Battery, then Battery Saver. 3. Choose a schedule for battery saver mode or automatically turn it off.

Source references to check:
- battery-saver-samsung-power-saving: Samsung, "Get the most out of your Galaxy phone or tablet battery" <https://www.samsung.com/us/support/answer/ANS10002534> | section: Power saving mode | applicability: Samsung Galaxy phone or tablet; the page says available screens and settings may vary by wireless service provider, software version, and model | excerpt: "apps running in the background may not receive updates or send you notifications when Power saving mode is enabled."
- battery-saver-android-manual: Google, "Get the most life from your Android device's battery" <https://support.google.com/android/answer/7664692?hl=en> | section: Stretch a low battery > Turn on battery saver mode manually | applicability: Android; the page says some of these steps work only on Android 13 and up, without saying which ones | excerpt: "Some of these steps work only on Android 13 and up."

TARGET (read only after step 2)

> Power saving mode may stop apps running in the background from sending you notifications, so think about that before you turn it on. Here is how:
> 1. Open **Settings**, then tap **Battery**.
> 2. Tap **Power saving**.
> 3. Tap the switches next to your desired settings or customizations.
> 4. Tap the switch at the top of the screen to activate Power saving mode.
> 
> You will not be able to adjust the settings once the mode is enabled.

---

## gsft-battery_saver-07
- candidate_id: gsft-battery_saver-07-v1
- conversation_sha256: d786cd1637900cd7ac84cd2e2af7ffe161da93487f9825e2750a7e51b809a643
- task_group: battery_saver | behavior: multiturn | tags: conditional, distractor
- route: answer
- decision basis (writer's): The user says the On battery setting was chosen and that the Mac is mostly plugged in. The page names a separate On power adapter pop-up menu and says Power Modes can be used whether the Mac is connected to power or not. The Windows ref is the inapplicable distractor.

Conversation (the model sees only the user turns, joined):
> **user:** How do I save battery on my MacBook Air?
> **assistant:** On your Mac laptop: 1. From the Apple menu, choose System Settings, then click Battery. 2. Under Energy Mode, choose Low Power Mode from the On battery pop-up menu.
> **user:** I picked Low Power Mode under Energy Mode in the On battery menu. But I mostly use my MacBook Air plugged into the charger at my desk, and nothing seems different there.

Passages the model sees (in this order):
- [battery-saver-mac-energymode] platform: Mac | app: System Settings
  > On Mac laptop (macOS Ventura or later): 1. From the Apple menu, choose System Settings, then click Battery. 2. Under Energy Mode, choose Low Power Mode, Automatic, or High Power Mode from the 'On battery' or the 'On power adapter' pop-up menu. Power Modes can be used whether your Mac is connected to power or not.
- [battery-saver-win11-batterylevel] platform: Windows 11 laptop | app: Settings
  > On Windows 11: If you want Energy saver to turn on whenever the battery falls below a certain level, follow these steps. 1. Select Start, then Settings, then System, then Power & battery. 2. Select Energy saver to expand the options. 3. Next to Turn energy saver on when battery level is at, select the battery level you'd like.

Source references to check:
- battery-saver-mac-energymode: Apple, "About Power Modes on your Mac - Apple Support" <https://support.apple.com/101613> | section: Select a Power Mode | applicability: Mac laptop with macOS Ventura or later for these steps | excerpt: "Power Modes can be used whether your Mac is connected to power or not."
- battery-saver-win11-batterylevel: Microsoft, "Battery saving tips for Windows | Microsoft Support" <https://support.microsoft.com/windows/battery-saving-tips-a850d64d-ee8e-c8d2-6c75-8ffe6ea3ea99> | section: Use energy saver | applicability: Windows 11 (the page's Applies To line names Windows 11 and Windows 10) | excerpt: "If you want energy saver to turn on whenever the battery falls below a certain level"

TARGET (read only after step 2)

> Your Mac has a separate pop-up menu for when it is connected to power. Go back to **Battery** in System Settings:
> 1. Under **Energy Mode**, open the **On power adapter** pop-up menu.
> 2. Choose **Low Power Mode**, **Automatic**, or **High Power Mode**.
> 
> Power Modes can be used whether your Mac is connected to power or not.

---

## gsft-find_downloads-01
- candidate_id: gsft-find_downloads-01-v1
- conversation_sha256: e2799051156195d8e0752f383d3ee58ad3853fbb4bfc09fe0b4456116df6cc8d
- task_group: find_downloads | behavior: direct | tags: conditional, distractor
- route: answer
- decision basis (writer's): The user states Chrome on a computer, so the Chrome steps apply. The Windows 11 Quick access ref is the inapplicable distractor. The Download tray appears only after a download, which is kept as a condition.

Conversation (the model sees only the user turns, joined):
> **user:** I'm using Google Chrome on my computer. I downloaded a PDF a minute ago but I can't find where Chrome put it. How do I see my downloads?

Passages the model sees (in this order):
- [find-downloads-chrome-menu] platform: Chrome on computer | app: Chrome
  > On Chrome on a computer: 1. At the top right, click More, then Downloads. 2. To open a file, click its name. It will open in your computer's default application for the file type.
- [find-downloads-chrome-tray] platform: Chrome on computer | app: Chrome
  > On Chrome on a computer: If you download a file, or if you've recently downloaded a file, the Download tray will appear. Recently downloaded files will appear to the right of the address bar. If the Download tray isn't present to the right of the address bar, click More, then Downloads, to view all downloads.
- [find-downloads-win11-quickaccess] platform: Windows 11 | app: File Explorer
  > On Windows 11: In File Explorer, the Quick access view displays all 6 known Windows folders: Desktop, Documents, Downloads, Pictures, Music, and Videos.

Source references to check:
- find-downloads-chrome-menu: Google, "Download a file - Computer - Google Chrome Help" <https://support.google.com/chrome/answer/95759?hl=en> | section: Find a list of files you've downloaded | applicability: Google Chrome on a computer | excerpt: "At the top right, click More ... and then Downloads."
- find-downloads-chrome-tray: Google, "Download a file - Computer - Google Chrome Help" <https://support.google.com/chrome/answer/95759?hl=en> | section: Download a file (Tips) | applicability: Google Chrome on a computer; the Download tray appears only after a download | excerpt: "Recently downloaded files will appear to the right of the address bar."
- find-downloads-win11-quickaccess: Microsoft, "File Explorer in Windows | Microsoft Support" <https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8> | section: Quick access | applicability: Windows 11 and Windows 10 (the page's Applies To line) | excerpt: "This view displays all 6 known Windows folders: Desktop, Documents, Downloads, Pictures, Music, and Videos."

TARGET (read only after step 2)

> Here is how to see your downloads in Chrome on your computer:
> 1. At the top right, click **More**, then **Downloads**.
> 2. To open a file, click its name. It opens in your computer's default application for that file type.
> 
> If you just downloaded a file, the Download tray appears, and recent downloads show to the right of the address bar. If the Download tray isn't there, use **More**, then **Downloads** instead.

---

## gsft-find_downloads-02
- candidate_id: gsft-find_downloads-02-v1
- conversation_sha256: b1fbb09cd1188f0c6769e644ec5f4e7a66bb867b0a0963bd7112c90f852fcb0e
- task_group: find_downloads | behavior: direct | tags: distractor
- route: answer
- decision basis (writer's): The user states a Windows 11 laptop, so the Windows 11 File Explorer steps apply. Chrome steps are the inapplicable distractor. The page says Downloads is one of the known folders in Quick access and that files can be searched from a folder like Downloads.

Conversation (the model sees only the user turns, joined):
> **user:** I'm on my Windows 11 laptop. I saved a file from an email yesterday and now I can't find it anywhere on the computer. The email said it was an attachment I needed to keep. Where would it have gone, and how do I look for it?

Passages the model sees (in this order):
- [find-downloads-win11-taskbar] platform: Windows 11 | app: File Explorer
  > On Windows 11: 1. Select File Explorer from the taskbar. 2. To find files stored inside a folder, search from a folder like Downloads.
- [find-downloads-win11-quickaccess] platform: Windows 11 | app: File Explorer
  > On Windows 11: In File Explorer, the Quick access view displays all 6 known Windows folders: Desktop, Documents, Downloads, Pictures, Music, and Videos.
- [find-downloads-chrome-menu] platform: Chrome on computer | app: Chrome
  > On Chrome on a computer: 1. At the top right, click More, then Downloads. 2. To open a file, click its name. It will open in your computer's default application for the file type.

Source references to check:
- find-downloads-win11-taskbar: Microsoft, "Find your files and apps in Windows | Microsoft Support" <https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/find-your-files-and-apps-in-windows> | section: Find your files > Search from File Explorer | applicability: Windows 11 (the page's Applies To line names Windows 11 and Windows 10) | excerpt: "To find files stored inside a folder, search from a folder like Downloads."
- find-downloads-win11-quickaccess: Microsoft, "File Explorer in Windows | Microsoft Support" <https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8> | section: Quick access | applicability: Windows 11 and Windows 10 (the page's Applies To line) | excerpt: "This view displays all 6 known Windows folders: Desktop, Documents, Downloads, Pictures, Music, and Videos."
- find-downloads-chrome-menu: Google, "Download a file - Computer - Google Chrome Help" <https://support.google.com/chrome/answer/95759?hl=en> | section: Find a list of files you've downloaded | applicability: Google Chrome on a computer | excerpt: "At the top right, click More ... and then Downloads."

TARGET (read only after step 2)

> Look for your file in the Downloads folder on your Windows 11 laptop:
> 1. Select **File Explorer** from the taskbar.
> 2. In **Quick access**, find **Downloads**.
> 3. To find a file inside **Downloads**, search from the Downloads folder.

---

## gsft-find_downloads-03
- candidate_id: gsft-find_downloads-03-v1
- conversation_sha256: 2cfec7c48c333f07487e003191ccd80949cd8f37ae66c2f0e196fe3c71715042
- task_group: find_downloads | behavior: clarify | tags: none
- route: clarify | routed question: Are you using Google Chrome, or looking in File Explorer on Windows?
- decision basis (writer's): The user does not name the app or the device. Chrome's downloads list (More, then Downloads) and the Windows File Explorer steps (File Explorer, Quick access, Downloads) differ, so one question is needed.

Conversation (the model sees only the user turns, joined):
> **user:** I downloaded a file yesterday and now I can't find it anywhere. Help?

Passages the model sees: none (clarify route)

Source references to check:
- find-downloads-chrome-menu: Google, "Download a file - Computer - Google Chrome Help" <https://support.google.com/chrome/answer/95759?hl=en> | section: Find a list of files you've downloaded | applicability: Google Chrome on a computer | excerpt: "At the top right, click More ... and then Downloads."
- find-downloads-win11-taskbar: Microsoft, "Find your files and apps in Windows | Microsoft Support" <https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/find-your-files-and-apps-in-windows> | section: Find your files > Search from File Explorer | applicability: Windows 11 (the page's Applies To line names Windows 11 and Windows 10) | excerpt: "To find files stored inside a folder, search from a folder like Downloads."

TARGET (read only after step 2)

> Are you using Google Chrome, or looking in File Explorer on Windows?

---

## gsft-find_downloads-04
- candidate_id: gsft-find_downloads-04-v1
- conversation_sha256: da38712cd12f951dc62551c3d1a03382122df722a4b176b21a6f47cbf8eb2d92
- task_group: find_downloads | behavior: clarify | tags: none
- route: clarify | routed question: Is your computer a Windows PC or a Mac?
- decision basis (writer's): The user does not name the computer. Chrome's default download folder is a user path that differs by operating system (Windows 10 and up versus Mac), so the operating system must be known first.

Conversation (the model sees only the user turns, joined):
> **user:** Where do my downloads go? I can't find them anywhere on my computer.

Passages the model sees: none (clarify route)

Source references to check:
- find-downloads-chrome-default-windows: Google, "Download a file - Computer - Google Chrome Help" <https://support.google.com/chrome/answer/95759?hl=en> | section: Default download locations | applicability: Google Chrome on Windows 10 and up, only if the default download location was not changed | excerpt: "If you didn't change your default download location, then Google Chrome downloads files to the following locations:"
- find-downloads-chrome-default-mac: Google, "Download a file - Computer - Google Chrome Help" <https://support.google.com/chrome/answer/95759?hl=en> | section: Default download locations | applicability: Google Chrome on Mac, only if the default download location was not changed | excerpt: "If you didn't change your default download location, then Google Chrome downloads files to the following locations:"

TARGET (read only after step 2)

> Is your computer a Windows PC or a Mac?

---

## gsft-find_downloads-05
- candidate_id: gsft-find_downloads-05-v1
- conversation_sha256: f2d3babe17436e36d641c52d94185ee2c610ef4667c47709f81343708eccbfe8
- task_group: find_downloads | behavior: constraint | tags: distractor
- route: answer
- decision basis (writer's): The user states Chrome on a Windows PC and asks for only the quickest route. The reply uses the two-step Chrome menu route and no extras. The Windows 11 taskbar ref is the inapplicable distractor.

Conversation (the model sees only the user turns, joined):
> **user:** I'm in Chrome on my Windows PC and I just downloaded a recipe. I get confused with menus, so please give me only the quickest way to open my downloads. Just the fewest clicks, no extra stuff.

Passages the model sees (in this order):
- [find-downloads-chrome-menu] platform: Chrome on computer | app: Chrome
  > On Chrome on a computer: 1. At the top right, click More, then Downloads. 2. To open a file, click its name. It will open in your computer's default application for the file type.
- [find-downloads-win11-taskbar] platform: Windows 11 | app: File Explorer
  > On Windows 11: 1. Select File Explorer from the taskbar. 2. To find files stored inside a folder, search from a folder like Downloads.

Source references to check:
- find-downloads-chrome-menu: Google, "Download a file - Computer - Google Chrome Help" <https://support.google.com/chrome/answer/95759?hl=en> | section: Find a list of files you've downloaded | applicability: Google Chrome on a computer | excerpt: "At the top right, click More ... and then Downloads."
- find-downloads-win11-taskbar: Microsoft, "Find your files and apps in Windows | Microsoft Support" <https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/find-your-files-and-apps-in-windows> | section: Find your files > Search from File Explorer | applicability: Windows 11 (the page's Applies To line names Windows 11 and Windows 10) | excerpt: "To find files stored inside a folder, search from a folder like Downloads."

TARGET (read only after step 2)

> The quickest way in Chrome on your computer:
> 1. At the top right, click **More**, then **Downloads**.
> 2. Click the file's name to open it.

---

## gsft-find_downloads-06
- candidate_id: gsft-find_downloads-06-v1
- conversation_sha256: 06926fe7520632951882e25836ce9e474874139293812179dce587530db09f45
- task_group: find_downloads | behavior: multiturn | tags: conditional, distractor
- route: answer
- decision basis (writer's): The user says Downloads was unpinned from Quick access. The page's restore steps for unpinned known folders apply to this condition. The Chrome menu ref is the inapplicable distractor.

Conversation (the model sees only the user turns, joined):
> **user:** How do I find my downloads on Windows 11?
> **assistant:** On Windows 11: 1. Select File Explorer from the taskbar. 2. In Quick access, find Downloads.
> **user:** I did find Downloads under Quick access before. But I unpinned it by accident while cleaning up, and now it's gone from that list. How do I get it back?

Passages the model sees (in this order):
- [find-downloads-win11-restore] platform: Windows 11 | app: File Explorer
  > On Windows 11, if you have unpinned a folder such as Downloads from Quick access: 1. Select Start > File Explorer, or select the File Explorer icon in the taskbar. 2. Select Home in the left navigation pane. 3. Select the Up arrow from the navigation buttons available to the left of the address bar. 4. Select and hold (or right-click) on the folder you wish to restore and select Pin to Quick access from the context menu.
- [find-downloads-chrome-menu] platform: Chrome on computer | app: Chrome
  > On Chrome on a computer: 1. At the top right, click More, then Downloads. 2. To open a file, click its name. It will open in your computer's default application for the file type.

Source references to check:
- find-downloads-win11-restore: Microsoft, "File Explorer in Windows | Microsoft Support" <https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8> | section: Restore known folders if you have unpinned them | applicability: Windows 11 and Windows 10 (the page's Applies To line) | excerpt: "Select and hold (or right-click) on the folder you wish to restore and select Pin to Quick access from the context menu."
- find-downloads-chrome-menu: Google, "Download a file - Computer - Google Chrome Help" <https://support.google.com/chrome/answer/95759?hl=en> | section: Find a list of files you've downloaded | applicability: Google Chrome on a computer | excerpt: "At the top right, click More ... and then Downloads."

TARGET (read only after step 2)

> Here is how to put Downloads back in Quick access on Windows 11:
> 1. Select **Start** > **File Explorer**, or select the **File Explorer** icon in the taskbar.
> 2. Select **Home** in the left navigation pane.
> 3. Select the **Up** arrow from the navigation buttons available to the left of the address bar.
> 4. Select and hold (or right-click) **Downloads** and select **Pin to Quick access** from the context menu.

---

## gsft-gift_card_scam-01
- candidate_id: gsft-gift_card_scam-01-v1
- conversation_sha256: 74e27040dc1cf9bdb898006daf5c63f8950e7a311c7346378d1eb8c73f0809dd
- task_group: gift_card_scam | behavior: direct | tags: safety
- route: answer
- decision basis (writer's): The user describes a gift card payment request by phone, which the FTC passage addresses directly. Protective actions come first: do not pay, hang up, and do not share the numbers or a photo. The no-agency statement supports the refusal.

Conversation (the model sees only the user turns, joined):
> **user:** I'm on my phone right now. A man said he's from my bank's fraud department. He says I have to buy gift cards to protect my account and then read him the numbers on the back. Should I do it?

Passages the model sees (in this order):
- [gift-card-stop] platform: Any device | app: none
  > If someone asks you to pay with gift cards, slow down. Don't pay. It's a scam. If this happens to you, hang up. It's a scam.
- [gift-card-numbers] platform: Any device | app: none
  > Don't give them those numbers or send them a photo of the card. It's a scam.
- [gift-card-no-agency] platform: Any device | app: none
  > No real business or government agency will ever tell you to buy a gift card to pay them. Government agencies won't contact you to demand immediate payment, and they never demand payment by gift card.

Source references to check:
- gift-card-stop: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How Gift Card Scams Work | applicability: Any device; gift card payment requests | excerpt: "Slow down. Don't pay. It's a scam. If this happens to you, hang up. It's a scam."
- gift-card-numbers: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How Gift Card Scams Work | applicability: Any device; gift card payment requests | excerpt: "Don't give them those numbers or send them a photo of the card. It's a scam."
- gift-card-no-agency: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: Companies and agencies that never ask for gift card payment | applicability: Any device | excerpt: "No real business or government agency will ever tell you to buy a gift card to pay them."

TARGET (read only after step 2)

> Slow down and don't pay. It's a scam.
> 1. Hang up.
> 2. Don't give them those numbers or send them a photo of the card.
> 
> No real business or government agency will ever tell you to buy a gift card to pay them.

---

## gsft-gift_card_scam-02
- candidate_id: gsft-gift_card_scam-02-v1
- conversation_sha256: e15a568ebb54166a126959285c46fedab10a42953d3d6368f0a719b0b951d263
- task_group: gift_card_scam | behavior: direct | tags: safety
- route: answer
- decision basis (writer's): The user describes a prize-claim gift card payment. The FTC passage says to slow down and not pay, to not share card numbers or a photo, and that no honest business or agency asks for gift card payment for a prize.

Conversation (the model sees only the user turns, joined):
> **user:** I'm on my computer. I got a text saying I won a free prize, but I have to buy Apple gift cards first to cover the shipping fee. Is this real?

Passages the model sees (in this order):
- [gift-card-stop] platform: Any device | app: none
  > If someone asks you to pay with gift cards, slow down. Don't pay. It's a scam. If this happens to you, hang up. It's a scam.
- [gift-card-prize] platform: Any device | app: none
  > No honest business or agency will ever make you buy a gift card to pay them for a prize.
- [gift-card-numbers] platform: Any device | app: none
  > Don't give them those numbers or send them a photo of the card. It's a scam.

Source references to check:
- gift-card-stop: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How Gift Card Scams Work | applicability: Any device; gift card payment requests | excerpt: "Slow down. Don't pay. It's a scam. If this happens to you, hang up. It's a scam."
- gift-card-prize: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: Common Gift Card Scams (Scammers say you've won a prize) | applicability: Any device | excerpt: "No honest business or agency will ever make you buy a gift card to pay them for a prize."
- gift-card-numbers: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How Gift Card Scams Work | applicability: Any device; gift card payment requests | excerpt: "Don't give them those numbers or send them a photo of the card. It's a scam."

TARGET (read only after step 2)

> Slow down. Don't pay. It's a scam.
> 1. Don't pay with gift cards.
> 2. Don't give them those numbers or send them a photo of the card.
> 
> No honest business or agency will ever make you buy a gift card to pay them for a prize.

---

## gsft-gift_card_scam-03
- candidate_id: gsft-gift_card_scam-03-v1
- conversation_sha256: 1cc8e380c75b968c5afda191f25a793090180abd615283a8b3ed9476eee3d7f7
- task_group: gift_card_scam | behavior: constraint | tags: safety
- route: answer
- decision basis (writer's): The user is on a live call with a gift card payment demand and has a time limit. The constraint is respected by a short reply that leads with hanging up, followed by the no-numbers rule and the government-demand statement.

Conversation (the model sees only the user turns, joined):
> **user:** Someone is on the phone with me right now. They say I must buy gift cards in the next ten minutes or my benefits will stop. I can't stay on the line long and I'm scared. What do I do?

Passages the model sees (in this order):
- [gift-card-stop] platform: Any device | app: none
  > If someone asks you to pay with gift cards, slow down. Don't pay. It's a scam. If this happens to you, hang up. It's a scam.
- [gift-card-numbers] platform: Any device | app: none
  > Don't give them those numbers or send them a photo of the card. It's a scam.
- [gift-card-no-agency] platform: Any device | app: none
  > No real business or government agency will ever tell you to buy a gift card to pay them. Government agencies won't contact you to demand immediate payment, and they never demand payment by gift card.

Source references to check:
- gift-card-stop: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How Gift Card Scams Work | applicability: Any device; gift card payment requests | excerpt: "Slow down. Don't pay. It's a scam. If this happens to you, hang up. It's a scam."
- gift-card-numbers: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How Gift Card Scams Work | applicability: Any device; gift card payment requests | excerpt: "Don't give them those numbers or send them a photo of the card. It's a scam."
- gift-card-no-agency: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: Companies and agencies that never ask for gift card payment | applicability: Any device | excerpt: "No real business or government agency will ever tell you to buy a gift card to pay them."

TARGET (read only after step 2)

> Hang up now. It's a scam.
> 1. Hang up.
> 2. Don't give them those numbers or send them a photo of the card.
> 
> Government agencies won't contact you to demand immediate payment, and they never demand payment by gift card.

---

## gsft-gift_card_scam-04
- candidate_id: gsft-gift_card_scam-04-v1
- conversation_sha256: f8e505185fc921c5a67cc5549f9815507dfe1eb2eac159a895ccfb34d6783a5a
- task_group: gift_card_scam | behavior: constraint | tags: safety
- route: answer
- decision basis (writer's): The user already gave the numbers and cannot call. The passage says that if the contact information cannot be found, the scam is reported to the FTC. The FTC web address comes from the same passage's reporting section. The company step is kept as a conditional for when the contact information is found.

Conversation (the model sees only the user turns, joined):
> **user:** I already gave a scammer the numbers off a gift card. I can't make phone calls, and I only know how to use the internet. I don't have the gift card company's phone number. What should I do?

Passages the model sees (in this order):
- [gift-card-report-no-contact] platform: Any device | app: none
  > If you can't find the contact information or the card issuer doesn't want to talk to you, report it to the FTC.
- [gift-card-report-company] platform: Any device | app: none
  > If you gave a gift card to a scammer: Report the gift card scam to the gift card company right away. Ask for your money back. Tell the FTC at ReportFraud.ftc.gov.

Source references to check:
- gift-card-report-no-contact: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How To Contact Gift Card Companies | applicability: Any device; the person cannot find the company's contact information or the card issuer does not want to talk to them | excerpt: "If you can't find the contact information or the card issuer doesn't want to talk to you, report it to the FTC."
- gift-card-report-company: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: What To Do If You Gave a Gift Card to a Scammer | applicability: Any device; the person already gave a gift card to a scammer | excerpt: "Report the gift card scam to the gift card company right away."

TARGET (read only after step 2)

> Since you don't have the company's contact information, report it to the FTC at **ReportFraud.ftc.gov**.
> 1. Go to **ReportFraud.ftc.gov** and tell the FTC about the gift card scam.
> 2. If you find the gift card company's contact information, report the scam to the company right away and ask for your money back.

---

## gsft-gift_card_scam-05
- candidate_id: gsft-gift_card_scam-05-v1
- conversation_sha256: 25e46e850326310e6bf1d7872c4d1ca151b4c0d1fd6675bf29e1fe44fb4b6c15
- task_group: gift_card_scam | behavior: multiturn | tags: safety
- route: answer
- decision basis (writer's): The user already gave gift card numbers and needs the reporting steps. The passage says to report to the gift card company right away, ask for money back, and tell the FTC. The conditional about missing contact information is kept.

Conversation (the model sees only the user turns, joined):
> **user:** Someone called and said I owe back taxes and must pay with gift cards today or the police will come. Is that real?
> **assistant:** It's a scam. Government agencies won't contact you to demand immediate payment, and they never demand payment by gift card. Hang up.
> **user:** I hung up, but before that I already bought two gift cards and read the numbers to them over the phone. What do I do now?

Passages the model sees (in this order):
- [gift-card-report-company] platform: Any device | app: none
  > If you gave a gift card to a scammer: Report the gift card scam to the gift card company right away. Ask for your money back. Tell the FTC at ReportFraud.ftc.gov.
- [gift-card-report-no-contact] platform: Any device | app: none
  > If you can't find the contact information or the card issuer doesn't want to talk to you, report it to the FTC.

Source references to check:
- gift-card-report-company: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: What To Do If You Gave a Gift Card to a Scammer | applicability: Any device; the person already gave a gift card to a scammer | excerpt: "Report the gift card scam to the gift card company right away."
- gift-card-report-no-contact: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How To Contact Gift Card Companies | applicability: Any device; the person cannot find the company's contact information or the card issuer does not want to talk to them | excerpt: "If you can't find the contact information or the card issuer doesn't want to talk to you, report it to the FTC."

TARGET (read only after step 2)

> Report the gift card scam as soon as you can.
> 1. Report the gift card scam to the gift card company right away.
> 2. Ask the company for your money back.
> 3. Tell the FTC at **ReportFraud.ftc.gov**.
> 
> If you can't find the company's contact information, report it to the FTC.

---

## gsft-gift_card_scam-06
- candidate_id: gsft-gift_card_scam-06-v1
- conversation_sha256: 0c325101540a6b0c9f6ac851bab4cac940c8f2eabeaba48671300a6e20d45ed8
- task_group: gift_card_scam | behavior: multiturn | tags: safety
- route: answer
- decision basis (writer's): The user describes a repeat call demanding a photo of the card. The passage says not to give those numbers or send a photo, and that this is a scam. The no-agency statement supports the refusal.

Conversation (the model sees only the user turns, joined):
> **user:** A man on the phone says he's from my power company and will cut my electricity today unless I buy gift cards and pay him. Should I?
> **assistant:** No. Don't pay. No real business or government agency will ever tell you to buy a gift card to pay them. Hang up.
> **user:** I hung up, but he called again from a different number. Now he says if I don't send him a photo of the card, the power goes off tonight.

Passages the model sees (in this order):
- [gift-card-numbers] platform: Any device | app: none
  > Don't give them those numbers or send them a photo of the card. It's a scam.
- [gift-card-no-agency] platform: Any device | app: none
  > No real business or government agency will ever tell you to buy a gift card to pay them. Government agencies won't contact you to demand immediate payment, and they never demand payment by gift card.

Source references to check:
- gift-card-numbers: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How Gift Card Scams Work | applicability: Any device; gift card payment requests | excerpt: "Don't give them those numbers or send them a photo of the card. It's a scam."
- gift-card-no-agency: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: Companies and agencies that never ask for gift card payment | applicability: Any device | excerpt: "No real business or government agency will ever tell you to buy a gift card to pay them."

TARGET (read only after step 2)

> Don't send him a photo of the card, and don't give him those numbers. It's a scam.
> 1. Don't send a photo of the card.
> 2. Don't give him those numbers.
> 
> No real business or government agency will ever tell you to buy a gift card to pay them.

---
