# Rule scan input, part 15 (50 examples)

## tr163-e
- task: Block a phone number | platform: Samsung Galaxy | scenario: constraint | sensitive: False
- sources: Samsung US Support: Block a phone number or contact on your Galaxy phone <https://www.samsung.com/us/support/answer/ANS10002869/>

**USER:**
My Samsung Galaxy gets text messages from a number that keeps sending me ads. It never calls, it only texts, so it is not in my call list. How do I block it from the text messages?

**ASSISTANT:**
You can block it right from the conversation.

1. Open the **Samsung Messages** app.
2. Touch and hold the conversation from that number.
3. Tap **More**.
4. Tap **Block**.
5. Tap **Block** again to confirm.

---

## tr163-r
- task: Block a phone number | platform: Samsung Galaxy | scenario: failure_recovery | sensitive: False
- sources: Samsung US Support: Block a phone number or contact on your Galaxy phone <https://www.samsung.com/us/support/answer/ANS10002869/>

**USER:**
How do I block a number on my Samsung Galaxy phone?

**ASSISTANT:**
You can block a number from your recent calls.

1. Open the **Phone** app and tap the **Recents** tab.
2. Tap the number.
3. Tap **Menu**. It looks like three lines with three dots.
4. Tap **Block**.
5. Tap **Block** again to confirm.

**USER:**
The number I want to block isn't in my recent calls. I only have it written on paper.

**ASSISTANT:**
You can type the number in yourself.

1. Open the **Phone** app and tap **More options**, the three dots.
2. Tap **Settings**.
3. Tap **Block numbers**.
4. Type the number, then tap the plus sign to add it.

---

## tr164-a
- task: Turn the flashlight on and off | platform: Samsung Galaxy | scenario: direct | sensitive: False
- sources: Samsung US Support: Use the flashlight on your Galaxy phone <https://www.samsung.com/us/support/answer/ANS10003351/>

**USER:**
How do I turn on the flashlight on my Samsung Galaxy phone?

**ASSISTANT:**
It is quick to do from the top of the screen.

1. Swipe down from the top right of the screen to open the **Quick settings** panel.
2. Tap the **Flashlight** icon. The light comes on.
3. To turn it off, tap the **Flashlight** icon again.

---

## tr164-b
- task: Turn the flashlight on and off | platform: Samsung Galaxy | scenario: missing_info | sensitive: False
- sources: Samsung US Support: Use the flashlight on your Galaxy phone <https://www.samsung.com/us/support/answer/ANS10003351/>

**USER:**
I need some light to look under the bed. How can I make the phone light up?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

---

## tr164-c
- task: Turn the flashlight on and off | platform: Samsung Galaxy | scenario: direct_messy | sensitive: False
- sources: Samsung US Support: Use the flashlight on your Galaxy phone <https://www.samsung.com/us/support/answer/ANS10003351/>

**USER:**
I use the flashlight on my Samsung Galaxy to walk to the mailbox at night, but it is so bright that it blinds me and I can't see the path. Is there a way to make the light dimmer? I only know how to turn it on and off.

**ASSISTANT:**
Yes, you can set how bright it is.

1. Swipe down from the top right of the screen to open the **Quick settings** panel.
2. Press and hold the **Flashlight** icon.
3. Tap the switch to turn the light on.
4. Drag the slider to make the light brighter or dimmer.

If the slider looks grayed out, turn the light on with the switch first.

---

## tr164-d
- task: Turn the flashlight on and off | platform: Samsung Galaxy | scenario: followup | sensitive: False
- sources: Samsung US Support: Use the flashlight on your Galaxy phone <https://www.samsung.com/us/support/answer/ANS10003351/>

**USER:**
I need some light to look under the bed. How can I make the phone light up?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

**USER:**
It's a Galaxy, made by Samsung.

**ASSISTANT:**
Thanks. On your Galaxy, the flashlight is at the top of the screen.

1. Swipe down from the top right of the screen to open the **Quick settings** panel.
2. Tap the **Flashlight** icon. The light comes on.
3. To turn it off, tap the **Flashlight** icon again.

---

## tr164-e
- task: Turn the flashlight on and off | platform: Samsung Galaxy | scenario: constraint | sensitive: False
- sources: Samsung US Support: Use the flashlight on your Galaxy phone <https://www.samsung.com/us/support/answer/ANS10003351/>

**USER:**
The power went out and it is pitch dark in my house. I have a Samsung Galaxy and I can barely see the screen, so I don't want to go hunting through apps or settings. What is the fastest way to get the light on, and then off again later?

**ASSISTANT:**
The fastest way is one swipe and one tap.

1. Swipe down from the top right of the screen to open the **Quick settings** panel.
2. Tap the **Flashlight** icon. The light comes on.

Later, to turn it off, open the same panel and tap the **Flashlight** icon again.

---

## tr164-r
- task: Turn the flashlight on and off | platform: Samsung Galaxy | scenario: failure_recovery | sensitive: False
- sources: Samsung US Support: Use the flashlight on your Galaxy phone <https://www.samsung.com/us/support/answer/ANS10003351/>

**USER:**
Samsung Galaxy: how do I use the flashlight?

**ASSISTANT:**
Here is how to turn it on and off.

1. Swipe down from the top right of the screen to open the **Quick settings** panel.
2. Tap the **Flashlight** icon. The light comes on.
3. To turn it off, tap the **Flashlight** icon again.

**USER:**
I swiped down and I see a bunch of icons but none of them is a flashlight.

**ASSISTANT:**
It may be on another page of the panel.

1. Swipe left in the **Quick settings** panel to see more icons.
2. Look for the **Flashlight** icon and tap it.

---

## tr165-b
- task: Turn on Easy mode for bigger icons and a simpler screen | platform: Samsung Galaxy | scenario: missing_info | sensitive: False
- sources: Samsung Support (UAE): Using Easy Mode on my Samsung Phone <https://www.samsung.com/ae/support/mobile-devices/using-easy-mode-on-my-samsung-phone>

**USER:**
Everything on my phone is too small. Is there a simple mode with bigger icons?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

---

## tr165-c
- task: Turn on Easy mode for bigger icons and a simpler screen | platform: Samsung Galaxy | scenario: direct_messy | sensitive: False
- sources: Samsung Support (UAE): Using Easy Mode on my Samsung Phone <https://www.samsung.com/ae/support/mobile-devices/using-easy-mode-on-my-samsung-phone>

**USER:**
My eyesight is not what it used to be and I keep tapping the wrong things on my Samsung Galaxy phone because everything is so small and crowded. My son said there is some kind of simple setting that spreads everything out and makes it bigger. Where do I find it?

**ASSISTANT:**
Your son means Easy Mode. It makes icons and text larger and spaces things out.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Easy Mode**.
4. Turn on the switch.

If the change does not show up, restart the phone and try again.

---

## tr165-d
- task: Turn on Easy mode for bigger icons and a simpler screen | platform: Samsung Galaxy | scenario: followup | sensitive: False
- sources: Samsung Support (UAE): Using Easy Mode on my Samsung Phone <https://www.samsung.com/ae/support/mobile-devices/using-easy-mode-on-my-samsung-phone>

**USER:**
Everything on my phone is too small. Is there a simple mode with bigger icons?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

**USER:**
Samsung Galaxy.

**ASSISTANT:**
Thank you. Your phone has one called Easy Mode.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Easy Mode**.
4. Turn on the switch.

Your screen will change to larger icons and text.

---

## tr165-e
- task: Turn on Easy mode for bigger icons and a simpler screen | platform: Samsung Galaxy | scenario: constraint | sensitive: False
- sources: Samsung Support (UAE): Using Easy Mode on my Samsung Phone <https://www.samsung.com/ae/support/mobile-devices/using-easy-mode-on-my-samsung-phone>

**USER:**
I turned on Easy Mode on my Samsung Galaxy last week, but now I want my old screen back. I do not want to reset the whole phone or lose anything. Can I just switch Easy Mode off?

**ASSISTANT:**
Yes. You only need to turn that one setting off.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Easy Mode**.
4. Turn the switch off.

---

## tr165-r
- task: Turn on Easy mode for bigger icons and a simpler screen | platform: Samsung Galaxy | scenario: failure_recovery | sensitive: False
- sources: Samsung Support (UAE): Using Easy Mode on my Samsung Phone <https://www.samsung.com/ae/support/mobile-devices/using-easy-mode-on-my-samsung-phone>

**USER:**
Samsung Galaxy phone. How do I turn on Easy Mode?

**ASSISTANT:**
Here is how to turn it on.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Easy Mode**.
4. Turn on the switch.

Your screen will change to larger icons and text.

**USER:**
I turned the switch on but nothing looks different. The icons are still small.

**ASSISTANT:**
Try restarting the phone, then turn Easy Mode on again.

1. Restart your phone.
2. Open **Settings**, tap **Display**, then tap **Easy Mode**.
3. Check that the switch is on.

Easy Mode can fail to apply if the phone's software is out of date, if it has a glitch, or if its storage is nearly full.

---

## tr166-a
- task: Find a lost phone | platform: Samsung Galaxy | scenario: direct | sensitive: True
- sources: Samsung US Support: How to locate your lost Samsung Galaxy phone or tablet <https://www.samsung.com/us/support/answer/ANS00080182>

**USER:**
I can't find my Samsung Galaxy phone anywhere. How can I find it?

**ASSISTANT:**
You can look for it from a computer or another phone.

1. In a web browser, go to the **SmartThings Find** website or the **Samsung Find** website.
2. Sign in with your Samsung account.
3. Choose your phone from the list on the left.
4. Look at the map to see where it is.

Your phone needs to be turned on and connected to a network for this to work.

---

## tr166-c
- task: Find a lost phone | platform: Samsung Galaxy | scenario: direct_messy | sensitive: True
- sources: Samsung US Support: How to locate your lost Samsung Galaxy phone or tablet <https://www.samsung.com/us/support/answer/ANS00080182>

**USER:**
I was in the kitchen and then the garden and now my Samsung Galaxy phone has disappeared. I am fairly sure it is somewhere in the house but I can't hear it because it is on silent. My husband has a laptop. Can we make it ring?

**ASSISTANT:**
Yes, a ring works even when the phone is on silent.

1. On the laptop, open a web browser and go to the **SmartThings Find** website or the **Samsung Find** website.
2. Sign in with your Samsung account.
3. Choose your phone from the list on the left.
4. Select **Ring**, then select **Start**.

It rings for one minute, even on Mute or Vibrate. To stop it, select **Stop** on the website, or swipe **Dismiss** on the phone.

---

## tr166-d
- task: Find a lost phone | platform: Samsung Galaxy | scenario: followup | sensitive: True
- sources: Samsung US Support: How to locate your lost Samsung Galaxy phone or tablet <https://www.samsung.com/us/support/answer/ANS00080182>

**USER:**
I lost my phone and I'm worried. Can you help me find it?

**ASSISTANT:**
I'm sorry, let's find it. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

**USER:**
It is a Samsung Galaxy.

**ASSISTANT:**
Thank you. You can look for it from a computer or another phone.

1. In a web browser, go to the **SmartThings Find** website or the **Samsung Find** website.
2. Sign in with your Samsung account.
3. Choose your phone from the list on the left.
4. Look at the map to see where it is.

Your phone needs to be turned on and connected to a network for this to work.

---

## tr166-r
- task: Find a lost phone | platform: Samsung Galaxy | scenario: failure_recovery | sensitive: True
- sources: Samsung US Support: How to locate your lost Samsung Galaxy phone or tablet <https://www.samsung.com/us/support/answer/ANS00080182>

**USER:**
I left my Samsung Galaxy somewhere and can't remember where. How do I locate it?

**ASSISTANT:**
You can look for it from a computer or another phone.

1. In a web browser, go to the **SmartThings Find** website or the **Samsung Find** website.
2. Sign in with your Samsung account.
3. Choose your phone from the list on the left.
4. Look at the map to see where it is.

Your phone needs to be turned on and connected to a network for this to work.

**USER:**
I signed in and picked my phone, but the map only shows an old spot from yesterday. I think its battery died.

**ASSISTANT:**
That fits. When the phone is off or cannot be reached, the map only shows its last known location.

1. Go to that last known spot and look there.
2. If you still cannot find it, contact your phone company. They may be able to help locate the phone or suspend it.

If you think it was stolen, do not go to the spot on the map yourself. Contact the authorities.

---

## tr167-a
- task: Turn on power saving mode | platform: Samsung Galaxy | scenario: direct | sensitive: False
- sources: Samsung US Support: Get the most out of your Galaxy phone or tablet battery <https://www.samsung.com/us/support/answer/ANS10002534>

**USER:**
How do I turn on power saving mode on my Samsung Galaxy phone?

**ASSISTANT:**
Here is how to turn it on:

1. Open **Settings**.
2. Tap **Battery**.
3. Tap **Power saving**.
4. Turn on the switches next to the options you want.
5. Tap the switch at the top of the screen to turn on Power saving mode.

Your screens may look a little different depending on your phone model.

---

## tr167-c
- task: Turn on power saving mode | platform: Samsung Galaxy | scenario: direct_messy | sensitive: False
- sources: Samsung US Support: Get the most out of your Galaxy phone or tablet battery <https://www.samsung.com/us/support/answer/ANS10002534>

**USER:**
I am going on a long bus ride tomorrow and my Samsung Galaxy phone never seems to hold its charge anymore. My grandson said there is a mode that makes the battery last longer but I did not catch what he called it. Can you walk me through turning it on?

**ASSISTANT:**
Yes, it is called Power saving mode. Here is how to turn it on:

1. Open **Settings**.
2. Tap **Battery**.
3. Tap **Power saving**.
4. Turn on the switches next to the options you want.
5. Tap the switch at the top of the screen to turn on Power saving mode.

Be aware that it can make some apps and tasks slower, and background apps may not update or send notifications.

---

## tr167-d
- task: Turn on power saving mode | platform: Samsung Galaxy | scenario: followup | sensitive: False
- sources: Samsung US Support: Get the most out of your Galaxy phone or tablet battery <https://www.samsung.com/us/support/answer/ANS10002534>

**USER:**
my phone battery dies so fast, how do i turn on the battery saving thing

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

**USER:**
Samsung Galaxy

**ASSISTANT:**
Thanks. Here is how to turn on Power saving mode on your Galaxy:

1. Open **Settings**.
2. Tap **Battery**.
3. Tap **Power saving**.
4. Turn on the switches next to the options you want.
5. Tap the switch at the top of the screen to turn on Power saving mode.

Your screens may look a little different depending on your model.

---

## tr167-e
- task: Turn on power saving mode | platform: Samsung Galaxy | scenario: constraint | sensitive: False
- sources: Samsung US Support: Get the most out of your Galaxy phone or tablet battery <https://www.samsung.com/us/support/answer/ANS10002534>

**USER:**
I have a Samsung Galaxy and I want to use Power saving mode, but I do not want it to just switch everything on without me. I would like to choose which things get turned down first. How do I do that?

**ASSISTANT:**
You can choose the options before you start the mode:

1. Open **Settings**.
2. Tap **Battery**.
3. Tap **Power saving**.
4. Turn on the switches only for the options you want. Each switch is next to a setting.
5. Tap the switch at the top of the screen to turn on Power saving mode.

Once the mode is on, you cannot change those options. If you want to change them later, turn the mode off, make your changes, then turn it back on.

---

## tr167-r
- task: Turn on power saving mode | platform: Samsung Galaxy | scenario: failure_recovery | sensitive: False
- sources: Samsung US Support: Get the most out of your Galaxy phone or tablet battery <https://www.samsung.com/us/support/answer/ANS10002534>

**USER:**
Hi, I just got a Samsung Galaxy and my son says I should be using Power saving mode. Where is it?

**ASSISTANT:**
Here is how to turn it on:

1. Open **Settings**.
2. Tap **Battery**.
3. Tap **Power saving**.
4. Turn on the switches next to the options you want.
5. Tap the switch at the top of the screen to turn on Power saving mode.

**USER:**
It is on now, but I wanted to change one of the options and I can not touch them anymore.

**ASSISTANT:**
That is normal. You cannot change the settings while the mode is on. To fix it:

1. Turn off Power saving mode for a moment.
2. Change the options you want.
3. Turn Power saving mode back on.

---

## tr168-a
- task: Take a screenshot | platform: Chromebook | scenario: direct | sensitive: False
- sources: Chromebook Help: Take a screenshot or record your screen <https://support.google.com/chromebook/answer/10474268?hl=en>

**USER:**
How do I take a screenshot of the whole screen on my Chromebook? It has a Screenshot key on the keyboard.

**ASSISTANT:**
Here is how:

1. Press the **Screenshot** key on your keyboard.
2. In the menu at the bottom of the screen, select **Screenshot**.
3. Choose **Take a full screen screenshot**.

The picture is saved in your Downloads folder by default, and a copy is also placed on the clipboard.

---

## tr168-b
- task: Take a screenshot | platform: Chromebook | scenario: missing_info | sensitive: False
- sources: Chromebook Help: Take a screenshot or record your screen <https://support.google.com/chromebook/answer/10474268?hl=en>

**USER:**
i need a screenshot of something on my laptop, what do i do

**ASSISTANT:**
I can help with that. Is your laptop a **Chromebook**, a **Windows** laptop, or a **Mac**?

---

## tr168-c
- task: Take a screenshot | platform: Chromebook | scenario: direct_messy | sensitive: False
- sources: Chromebook Help: Take a screenshot or record your screen <https://support.google.com/chromebook/answer/10474268?hl=en>

**USER:**
My daughter bought me a Chromebook last year and I love it, but I cannot find any key that says screenshot. I want to save a picture of my e-ticket on the screen so I can show it to the person at the door. What should I do?

**ASSISTANT:**
If you do not have a Screenshot key, you can use the screen menu instead:

1. Select the **Settings** icon at the bottom right of the screen.
2. Select **Screen Capture**.
3. Choose **Take a full screen screenshot**.

The picture is saved in your Downloads folder by default.

---

## tr168-d
- task: Take a screenshot | platform: Chromebook | scenario: followup | sensitive: False
- sources: Chromebook Help: Take a screenshot or record your screen <https://support.google.com/chromebook/answer/10474268?hl=en>

**USER:**
i need a screenshot of something on my laptop, what do i do

**ASSISTANT:**
I can help with that. Is your laptop a **Chromebook**, a **Windows** laptop, or a **Mac**?

**USER:**
chromebook

**ASSISTANT:**
Thanks. If your Chromebook has a Screenshot key, here is how:

1. Press the **Screenshot** key.
2. In the menu at the bottom, select **Screenshot**.
3. Choose **Take a full screen screenshot**.

If you do not have a Screenshot key, select the **Settings** icon at the bottom right, then select **Screen Capture**, and choose the same option.

---

## tr168-e
- task: Take a screenshot | platform: Chromebook | scenario: constraint | sensitive: False
- sources: Chromebook Help: Take a screenshot or record your screen <https://support.google.com/chromebook/answer/10474268?hl=en>

**USER:**
I have a Chromebook with no Screenshot key at all, and I do not want the whole screen, just one part of a recipe on the page. Can you tell me how to capture only part of it?

**ASSISTANT:**
You can do that without a Screenshot key:

1. Select the **Settings** icon at the bottom right of the screen.
2. Select **Screen Capture**.
3. Choose **Take a partial screenshot**.

The picture is saved in your Downloads folder by default. While choosing the part, you can press the space bar to change which section you are capturing.

---

## tr168-r
- task: Take a screenshot | platform: Chromebook | scenario: failure_recovery | sensitive: False
- sources: Chromebook Help: Take a screenshot or record your screen <https://support.google.com/chromebook/answer/10474268?hl=en>

**USER:**
How do I take a screenshot on my Chromebook? I do have a Screenshot key.

**ASSISTANT:**
Here is how:

1. Press the **Screenshot** key.
2. In the menu at the bottom of the screen, select **Screenshot**.
3. Choose a capture type, such as **Take a full screen screenshot**.

**USER:**
I think it worked but I have no idea where the picture went.

**ASSISTANT:**
By default, screenshots are saved in your **Downloads** folder. A copy is also placed on the clipboard, so you can paste it where you need it.

If you want screenshots to go somewhere else in future:

1. Press **Shift + Ctrl + Show windows**.
2. Select **Settings**.
3. Select **Select folder** and pick the folder you want.

---

## tr169-a
- task: Connect to a Wi-Fi network | platform: Chromebook | scenario: direct | sensitive: False
- sources: Chromebook Help: Connect your Chromebook to Wi-Fi <https://support.google.com/chromebook/answer/1047420?hl=en>

**USER:**
How do I connect my Chromebook to my home Wi-Fi? It needs a password.

**ASSISTANT:**
Here is how to connect:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Network**, then **Wi-Fi**.
4. Select your network.
5. Type the password.
6. Select **Connect**.

If Wi-Fi is off, first select the time, select **Not Connected**, and turn on **Wi-Fi**. Then do the steps above.

---

## tr169-b
- task: Connect to a Wi-Fi network | platform: Chromebook | scenario: missing_info | sensitive: False
- sources: Chromebook Help: Connect your Chromebook to Wi-Fi <https://support.google.com/chromebook/answer/1047420?hl=en>

**USER:**
how do I get on the wifi

**ASSISTANT:**
I can help with that. What device do you want to connect: a **Chromebook**, a **phone**, or a different computer?

---

## tr169-d
- task: Connect to a Wi-Fi network | platform: Chromebook | scenario: followup | sensitive: False
- sources: Chromebook Help: Connect your Chromebook to Wi-Fi <https://support.google.com/chromebook/answer/1047420?hl=en>

**USER:**
how do I get on the wifi

**ASSISTANT:**
I can help with that. What device do you want to connect: a **Chromebook**, a **phone**, or a different computer?

**USER:**
my chromebook

**ASSISTANT:**
Thanks. Here is how to connect your Chromebook:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Network**, then **Wi-Fi**.
4. Select your network.
5. If it asks, type the password.
6. Select **Connect**.

If Wi-Fi is off, first select the time, select **Not Connected**, and turn on **Wi-Fi**. Then do the steps above.

---

## tr169-e
- task: Connect to a Wi-Fi network | platform: Chromebook | scenario: constraint | sensitive: False
- sources: Chromebook Help: Connect your Chromebook to Wi-Fi <https://support.google.com/chromebook/answer/1047420?hl=en>

**USER:**
My Chromebook keeps forgetting my Wi-Fi and I am tired of typing the password. I am connecting at my house right now. Is there a way to connect and have it reconnect by itself next time?

**ASSISTANT:**
Yes. First connect, then turn on automatic reconnecting:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Network**, then **Wi-Fi**.
4. Select your network.
5. Type the password.
6. Select **Connect**.
7. Select your network again in the Wi-Fi list, then turn on **Automatically connect to this network**.

If Wi-Fi is off, first select the time, select **Not Connected**, and turn on **Wi-Fi**.

---

## tr170-a
- task: Update the Chromebook | platform: Chromebook | scenario: direct | sensitive: False
- sources: Chromebook Help: Update your Chromebook's operating system <https://support.google.com/chromebook/answer/177889?hl=en>

**USER:**
How do I check for updates on my Chromebook?

**ASSISTANT:**
Make sure your Chromebook is on and connected to Wi-Fi. Then:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** gear icon.
3. At the bottom left, select **About ChromeOS**.
4. Select **Check for updates**.

If an update is found, it downloads by itself. If you do not see **Check for updates**, your Chromebook is most likely up to date.

---

## tr170-b
- task: Update the Chromebook | platform: Chromebook | scenario: missing_info | sensitive: False
- sources: Chromebook Help: Update your Chromebook's operating system <https://support.google.com/chromebook/answer/177889?hl=en>

**USER:**
how do i update my computer, it keeps telling me to

**ASSISTANT:**
I can help with that. Is your computer a **Chromebook**, a **Windows** PC, or a **Mac**?

---

## tr170-c
- task: Update the Chromebook | platform: Chromebook | scenario: direct_messy | sensitive: False
- sources: Chromebook Help: Update your Chromebook's operating system <https://support.google.com/chromebook/answer/177889?hl=en>

**USER:**
My Chromebook finished downloading something and now there is a little message near the date at the bottom right that says Update device. I am not sure whether to click it or ignore it. It is my own home Chromebook, not from work. What do I do?

**ASSISTANT:**
That message means an update is ready. To install it:

1. Select the **Update device** message at the bottom right, next to the date.
2. Select **Restart**.

Your Chromebook will restart and install the update.

---

## tr170-d
- task: Update the Chromebook | platform: Chromebook | scenario: followup | sensitive: False
- sources: Chromebook Help: Update your Chromebook's operating system <https://support.google.com/chromebook/answer/177889?hl=en>

**USER:**
how do i update my computer, it keeps telling me to

**ASSISTANT:**
I can help with that. Is your computer a **Chromebook**, a **Windows** PC, or a **Mac**?

**USER:**
its a chromebook

**ASSISTANT:**
Thanks. Connect your Chromebook to Wi-Fi first. Then:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** gear icon.
3. At the bottom left, select **About ChromeOS**.
4. Select **Check for updates**.
5. When the download finishes, select the **Update device** message at the bottom right.
6. Select **Restart**.

If you do not see **Check for updates**, your Chromebook is most likely up to date.

---

## tr170-e
- task: Update the Chromebook | platform: Chromebook | scenario: constraint | sensitive: False
- sources: Chromebook Help: Update your Chromebook's operating system <https://support.google.com/chromebook/answer/177889?hl=en>

**USER:**
I am traveling and my Chromebook is only on my phone's mobile data right now, nothing else. I want to update it but I am worried about using up my data. Can I still do it and will it warn me?

**ASSISTANT:**
Yes, it will warn you. Here is how to check for the update:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** gear icon.
3. At the bottom left, select **About ChromeOS**.
4. Select **Check for updates**.

If an update is found, you will get an alert showing how much data it needs. You can then stop or continue. It also helps to plug in the charger so the update is not interrupted.

---

## tr171-a
- task: Zoom in or magnify the screen | platform: Chromebook | scenario: direct | sensitive: False
- sources: Chromebook Help: Zoom in or magnify your Chromebook screen <https://support.google.com/chromebook/answer/6320705?hl=en>

**USER:**
How do I turn on the full screen magnifier on my Chromebook?

**ASSISTANT:**
Here is how to turn it on in Settings:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Accessibility**.
4. Under **Display**, turn on **Full screen magnifier**.

You can also choose how the screen moves and set the zoom level next to **Fullscreen zoom level**.

---

## tr171-b
- task: Zoom in or magnify the screen | platform: Chromebook | scenario: missing_info | sensitive: False
- sources: Chromebook Help: Zoom in or magnify your Chromebook screen <https://support.google.com/chromebook/answer/6320705?hl=en>

**USER:**
everything on my chromebook is too small, how do i make it bigger

**ASSISTANT:**
I can help with that. Do you want to enlarge just the **web page**, or **magnify the whole screen**?

---

## tr171-c
- task: Zoom in or magnify the screen | platform: Chromebook | scenario: direct_messy | sensitive: False
- sources: Chromebook Help: Zoom in or magnify your Chromebook screen <https://support.google.com/chromebook/answer/6320705?hl=en>

**USER:**
My eyesight is getting worse and I read with my Chromebook a lot. I do not want to enlarge the whole screen, I would rather have a strip at the top that shows things bigger while the rest stays normal. I have heard there is a docked kind of magnifier. How do I get it?

**ASSISTANT:**
Yes, the docked magnifier does that. It magnifies the top third of the screen. To turn it on:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Accessibility**.
4. Under **Display**, turn on **Docked magnifier**.
5. Set how big you want it next to **Docked zoom level**.

Move your cursor to change the area that is magnified.

---

## tr171-d
- task: Zoom in or magnify the screen | platform: Chromebook | scenario: followup | sensitive: False
- sources: Chromebook Help: Zoom in or magnify your Chromebook screen <https://support.google.com/chromebook/answer/6320705?hl=en>

**USER:**
everything on my chromebook is too small, how do i make it bigger

**ASSISTANT:**
I can help with that. Do you want to enlarge just the **web page**, or **magnify the whole screen**?

**USER:**
just the web page

**ASSISTANT:**
To make just the web page bigger:

1. Press **Ctrl** and **+** together.
2. Press it again to go bigger still.

To make the page smaller again, press **Ctrl** and **-**. To go back to normal size, press **Ctrl** and **0**.

---

## tr171-e
- task: Zoom in or magnify the screen | platform: Chromebook | scenario: constraint | sensitive: False
- sources: Chromebook Help: Zoom in or magnify your Chromebook screen <https://support.google.com/chromebook/answer/6320705?hl=en>

**USER:**
I only want the website to look bigger on my Chromebook. I do not want the bar at the bottom or the tabs to change size, and I do not want to go into any settings. Just a keyboard shortcut please.

**ASSISTANT:**
Use this shortcut, which only changes the page:

1. Press **Ctrl** and **+** together to make the page bigger.
2. Press it again for even bigger.

To make it smaller, press **Ctrl** and **-**. To reset, press **Ctrl** and **0**.

Do not use the shortcuts with **Shift** added. Those change the whole screen, including the bottom bar and tabs.

---

## tr171-r
- task: Zoom in or magnify the screen | platform: Chromebook | scenario: failure_recovery | sensitive: False
- sources: Chromebook Help: Zoom in or magnify your Chromebook screen <https://support.google.com/chromebook/answer/6320705?hl=en>

**USER:**
Is there a keyboard shortcut for the full screen magnifier on a Chromebook?

**ASSISTANT:**
Yes. Press **Ctrl + Search + m** to magnify your whole screen. If your keyboard has a Launcher key instead of a Search key, press **Ctrl + Launcher + m**.

To make it bigger or smaller, press **Ctrl + Alt** and the brightness up or down key.

**USER:**
I pressed it and nothing happened.

**ASSISTANT:**
I am not sure why that happened. You can turn the magnifier on from Settings instead:

1. Select the time at the bottom right of the screen.
2. Select **Settings**, then **Accessibility**.
3. Under **Display**, turn on **Full screen magnifier**.

---

## tr172-a
- task: Have text read aloud (Select-to-speak) | platform: Chromebook | scenario: direct | sensitive: False
- sources: Chromebook Help: Hear text read aloud <https://support.google.com/chromebook/answer/9032490?hl=en>

**USER:**
How can I make my Chromebook read the text on the screen out loud to me?

**ASSISTANT:**
You can use Select-to-speak. First turn it on:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** icon.
3. Select **Accessibility**.
4. Under **Text-to-Speech**, turn on **Select-to-speak**.

Then press and hold the **Search** key and drag the pointer over the text you want to hear. Your Chromebook reads it aloud and highlights each word as it is spoken.

---

## tr172-b
- task: Have text read aloud (Select-to-speak) | platform: Chromebook | scenario: missing_info | sensitive: False
- sources: Chromebook Help: Hear text read aloud <https://support.google.com/chromebook/answer/9032490?hl=en>

**USER:**
can my computer read the page to me out loud? my eyes are bad

**ASSISTANT:**
Yes, it can. Is your computer a **Chromebook**, a **Windows** PC, or a **Mac**?

---

## tr172-c
- task: Have text read aloud (Select-to-speak) | platform: Chromebook | scenario: direct_messy | sensitive: False
- sources: Chromebook Help: Hear text read aloud <https://support.google.com/chromebook/answer/9032490?hl=en>

**USER:**
I have a touchscreen Chromebook and reading long articles tires my eyes out. My nephew said it can read to me but I do not know how. Select-to-speak is already turned on in my settings. How do I get it to read one paragraph?

**ASSISTANT:**
Since Select-to-speak is already on, you only need to pick the text:

1. Tap a line of text, or drag your finger across the paragraph you want.
2. Your Chromebook reads it aloud and highlights each word as it is spoken.

To stop it, press **Ctrl** or the **Search** key, or select the **Stop** button.

---

## tr172-d
- task: Have text read aloud (Select-to-speak) | platform: Chromebook | scenario: followup | sensitive: False
- sources: Chromebook Help: Hear text read aloud <https://support.google.com/chromebook/answer/9032490?hl=en>

**USER:**
can my computer read the page to me out loud? my eyes are bad

**ASSISTANT:**
Yes, it can. Is your computer a **Chromebook**, a **Windows** PC, or a **Mac**?

**USER:**
Chromebook

**ASSISTANT:**
Good, your Chromebook has Select-to-speak. First turn it on:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** icon.
3. Select **Accessibility**.
4. Under **Text-to-Speech**, turn on **Select-to-speak**.

Then press and hold the **Search** key and drag the pointer over the text. Your Chromebook reads it aloud and highlights each word.

---

## tr172-e
- task: Have text read aloud (Select-to-speak) | platform: Chromebook | scenario: constraint | sensitive: False
- sources: Chromebook Help: Hear text read aloud <https://support.google.com/chromebook/answer/9032490?hl=en>

**USER:**
Select-to-speak is on in my Chromebook already. But my hand shakes and I cannot hold a key and drag the mouse at the same time. Is there another way to get it to read a paragraph?

**ASSISTANT:**
Yes, you can highlight the text first and then press one shortcut:

1. Highlight the text you want to hear.
2. Press the **Search** key and **s** together.

Your Chromebook reads it aloud and highlights each word. Or, you can select the **Select-to-Speak** icon near the time at the bottom right, then drag over the text without holding a key.

To stop, press **Ctrl** or the **Search** key, or select **Stop**.

---

## tr173-a
- task: Free up drive space | platform: Windows 11 | scenario: direct | sensitive: False
- sources: Microsoft Support: Free up drive space in Windows <https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32>

**USER:**
My Windows 11 laptop says the drive is almost full. How can I clear some space?

**ASSISTANT:**
Windows has a cleanup tool that shows what you can safely remove. Here is how to use it:

1. Select **Start**, then **Settings**.
2. Select **System**, then **Storage**.
3. Select **Cleanup recommendations**.
4. Look at the groups: **Temporary files**, **Large or unused files**, **Files synced to the cloud**, and **Unused apps**. Tick the items you want to remove. Windows shows how much space each one will save.
5. Select the **Clean up** button in each section.

If you want to see how much room you have, open **File Explorer**, select **This PC**, and look under **Devices and drives**.

---

## tr173-b
- task: Free up drive space | platform: Windows 11 | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Free up drive space in Windows <https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32>

**USER:**
my computer keeps saying i am out of space what do i do

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

---
