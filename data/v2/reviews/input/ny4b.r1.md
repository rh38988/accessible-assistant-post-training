# Review input: batch ny4b, round 1 (36 examples)

## tr167-a
- scenario: direct | style: plain | specification: fully_specified | platform: Samsung Galaxy
- task: Turn on power saving mode (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002534

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

## tr167-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Samsung Galaxy
- task: Turn on power saving mode (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002534

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

## tr167-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on power saving mode (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002534

**USER:**
my phone battery dies so fast, how do i turn on the battery saving thing

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

## tr167-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Turn on power saving mode (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002534

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

## tr167-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Turn on power saving mode (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002534

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

## tr167-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Samsung Galaxy
- task: Turn on power saving mode (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002534

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

## tr168-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chromebook
- task: Take a screenshot (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/10474268?hl=en

**USER:**
How do I take a screenshot of the whole screen on my Chromebook? It has a Screenshot key on the keyboard.

**ASSISTANT:**
Here is how:

1. Press the **Screenshot** key on your keyboard.
2. In the menu at the bottom of the screen, select **Screenshot**.
3. Choose **Take a full screen screenshot**.

The picture is saved in your Downloads folder by default, and a copy is also placed on the clipboard.

## tr168-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Chromebook
- task: Take a screenshot (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/10474268?hl=en

**USER:**
My daughter bought me a Chromebook last year and I love it, but I cannot find any key that says screenshot. I want to save a picture of my e-ticket on the screen so I can show it to the person at the door. What should I do?

**ASSISTANT:**
If you do not have a Screenshot key, you can use the screen menu instead:

1. Select the **Settings** icon at the bottom right of the screen.
2. Select **Screen Capture**.
3. Choose **Take a full screen screenshot**.

The picture is saved in your Downloads folder by default.

## tr168-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Take a screenshot (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/10474268?hl=en

**USER:**
i need a screenshot of something on my laptop, what do i do

**ASSISTANT:**
I can help with that. Is your laptop a **Chromebook**, a **Windows** laptop, or a **Mac**?

## tr168-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chromebook
- task: Take a screenshot (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/10474268?hl=en

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

## tr168-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chromebook
- task: Take a screenshot (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/10474268?hl=en

**USER:**
I have a Chromebook with no Screenshot key at all, and I do not want the whole screen, just one part of a recipe on the page. Can you tell me how to capture only part of it?

**ASSISTANT:**
You can do that without a Screenshot key:

1. Select the **Settings** icon at the bottom right of the screen.
2. Select **Screen Capture**.
3. Choose **Take a partial screenshot**.

The picture is saved in your Downloads folder by default. While choosing the part, you can press the space bar to change which section you are capturing.

## tr168-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chromebook
- task: Take a screenshot (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/10474268?hl=en

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

## tr169-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chromebook
- task: Connect to a Wi-Fi network (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

**USER:**
How do I connect my Chromebook to my home Wi-Fi? It needs a password.

**ASSISTANT:**
Here is how to connect:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Not Connected**.
4. Turn on **Wi-Fi** if it is off.
5. Select your network from the list.
6. Type the password.
7. Select **Connect**.

When it works, your network name and signal strength show in the Wi-Fi panel.

## tr169-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Chromebook
- task: Connect to a Wi-Fi network (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

**USER:**
I am at a coffee shop with my Chromebook and they said the Wi-Fi is open, no password needed. I have never done this before and I do not want to mess anything up. How do I get on their network?

**ASSISTANT:**
It is simple. Here are the steps:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Not Connected**.
4. Turn on **Wi-Fi** if it is off.
5. Select the coffee shop's network from the list.
6. Select **Connect**.

If a sign-in page opens in your browser, finish it to complete the connection.

## tr169-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Connect to a Wi-Fi network (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

**USER:**
how do I get on the wifi

**ASSISTANT:**
I can help with that. What device do you want to connect: a **Chromebook**, a **phone**, or a different computer?

## tr169-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chromebook
- task: Connect to a Wi-Fi network (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

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
3. Select **Not Connected**.
4. Turn on **Wi-Fi** if it is off.
5. Select your network from the list.
6. If it asks, type the password.
7. Select **Connect**.

When it works, your network name and signal strength show in the Wi-Fi panel.

## tr169-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chromebook
- task: Connect to a Wi-Fi network (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

**USER:**
My Chromebook keeps forgetting my Wi-Fi and I am tired of typing the password. I am connecting at my house right now. Is there a way to connect and have it reconnect by itself next time?

**ASSISTANT:**
Yes. First connect, then turn on automatic reconnecting:

1. Select the time at the bottom right, then select **Settings**.
2. Select **Not Connected**, and turn on **Wi-Fi** if it is off.
3. Select your network, type the password, and select **Connect**.
4. Go back to your network's settings and turn on **Automatically connect to this network**.

If you have several networks around, you can also turn on **Prefer this network** for your home one.

## tr169-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chromebook
- task: Connect to a Wi-Fi network (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/1047420?hl=en

**USER:**
I moved to a new apartment. Please help me get my Chromebook on the new password-protected Wi-Fi.

**ASSISTANT:**
Here is how:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Not Connected**.
4. Turn on **Wi-Fi** if it is off.
5. Select your network from the list.
6. Type the password.
7. Select **Connect**.

**USER:**
My network name is not in the list at all. The router is right next to me.

**ASSISTANT:**
The network may be hidden. You can add it by hand:

1. In the Wi-Fi panel, select **Add connection**.
2. Select **Add Wi-Fi**.
3. Type in the network details.
4. Select **Connect**.

If you do not know the details, ask the person who set up the network.

## tr170-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chromebook
- task: Update the Chromebook (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/177889?hl=en

**USER:**
How do I check for updates on my Chromebook?

**ASSISTANT:**
Make sure your Chromebook is on and connected to Wi-Fi. Then:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** gear icon.
3. At the bottom left, select **About ChromeOS**.
4. Select **Check for updates**.

If an update is found, it downloads by itself. If you do not see **Check for updates**, your Chromebook is most likely up to date.

## tr170-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Chromebook
- task: Update the Chromebook (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/177889?hl=en

**USER:**
My Chromebook finished downloading something and now there is a little message near the date at the bottom right that says Update device. I am not sure whether to click it or ignore it. It is my own home Chromebook, not from work. What do I do?

**ASSISTANT:**
That message means an update is ready. To install it:

1. Select the **Update device** message at the bottom right, next to the date.
2. Select **Restart**.

Your Chromebook will restart and install the update.

## tr170-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Update the Chromebook (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/177889?hl=en

**USER:**
how do i update my computer, it keeps telling me to

**ASSISTANT:**
I can help with that. Is your computer a **Chromebook**, a **Windows** PC, or a **Mac**?

## tr170-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chromebook
- task: Update the Chromebook (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/177889?hl=en

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

## tr170-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chromebook
- task: Update the Chromebook (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/177889?hl=en

**USER:**
I am traveling and my Chromebook is only on my phone's mobile data right now, nothing else. I want to update it but I am worried about using up my data. Can I still do it and will it warn me?

**ASSISTANT:**
Yes, it will warn you. Here is how to check for the update:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** gear icon.
3. At the bottom left, select **About ChromeOS**.
4. Select **Check for updates**.

If an update is found, you will get an alert showing how much data it needs. You can then stop or continue. It also helps to plug in the charger so the update is not interrupted.

## tr170-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chromebook
- task: Update the Chromebook (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/177889?hl=en

**USER:**
How do I update my Chromebook? It is connected to Wi-Fi.

**ASSISTANT:**
Here is how:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** gear icon.
3. At the bottom left, select **About ChromeOS**.
4. Select **Check for updates**.
5. When the download finishes, select **Restart** in the **Update device** message near the date.

**USER:**
I did that but the update never seems to download, it just sits there.

**ASSISTANT:**
Try these in order, and test after each one:

1. Turn your Chromebook off, then back on.
2. If you are using mobile data or a phone connection, switch to Wi-Fi or Ethernet instead.
3. If it still will not download, the next options are a reset or a recovery. A recovery erases everything on the drive, so back up your files first.

## tr171-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chromebook
- task: Zoom in or magnify the screen (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/6320705?hl=en

**USER:**
How do I turn on the full screen magnifier on my Chromebook?

**ASSISTANT:**
Here is how to turn it on in Settings:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Accessibility**.
4. Under **Display**, turn on **Full screen magnifier**.

You can also choose how the screen moves and set the zoom level next to **Fullscreen zoom level**.

## tr171-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Chromebook
- task: Zoom in or magnify the screen (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/6320705?hl=en

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

## tr171-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: Chromebook
- task: Zoom in or magnify the screen (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/6320705?hl=en

**USER:**
everything on my chromebook is too small, how do i make it bigger

**ASSISTANT:**
I can help with that. Do you want to enlarge just the **web page**, or **magnify the whole screen**?

## tr171-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chromebook
- task: Zoom in or magnify the screen (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/6320705?hl=en

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

## tr171-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chromebook
- task: Zoom in or magnify the screen (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/6320705?hl=en

**USER:**
I only want the website to look bigger on my Chromebook. I do not want the bar at the bottom or the tabs to change size, and I do not want to go into any settings. Just a keyboard shortcut please.

**ASSISTANT:**
Use this shortcut, which only changes the page:

1. Press **Ctrl** and **+** together to make the page bigger.
2. Press it again for even bigger.

To make it smaller, press **Ctrl** and **-**. To reset, press **Ctrl** and **0**.

Do not use the shortcuts with **Shift** added. Those change the whole screen, including the bottom bar and tabs.

## tr171-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chromebook
- task: Zoom in or magnify the screen (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/6320705?hl=en

**USER:**
Is there a keyboard shortcut for the full screen magnifier on a Chromebook?

**ASSISTANT:**
Yes. Press **Ctrl + Search + m** to turn it on or off. If your keyboard has a Launcher key instead of a Search key, press **Ctrl + Launcher + m**.

To make it bigger or smaller, press **Ctrl + Alt** and the brightness up or down key.

**USER:**
I pressed it and nothing happened.

**ASSISTANT:**
The shortcut only works once the magnifier is turned on in Settings. Do this once:

1. Select the time at the bottom right of the screen.
2. Select **Settings**, then **Accessibility**.
3. Under **Display**, turn on **Full screen magnifier**.

After that, the shortcut should work.

## tr172-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chromebook
- task: Have text read aloud (Select-to-speak) (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/9032490?hl=en

**USER:**
How can I make my Chromebook read the text on the screen out loud to me?

**ASSISTANT:**
You can use Select-to-speak. First turn it on:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** icon.
3. Select **Accessibility**.
4. Under **Text-to-Speech**, turn on **Select-to-speak**.

Then press and hold the **Search** key and drag the pointer over the text you want to hear. Your Chromebook reads it aloud and highlights each word as it is spoken.

## tr172-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Chromebook
- task: Have text read aloud (Select-to-speak) (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/9032490?hl=en

**USER:**
I have a touchscreen Chromebook and reading long articles tires my eyes out. My nephew said it can read to me but I do not know how. Select-to-speak is already turned on in my settings. How do I get it to read one paragraph?

**ASSISTANT:**
Since Select-to-speak is already on, you only need to pick the text:

1. Tap a line of text, or drag your finger across the paragraph you want.
2. Your Chromebook reads it aloud and highlights each word as it is spoken.

To stop it, press **Ctrl** or the **Search** key, or select the **Stop** button.

## tr172-b
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Have text read aloud (Select-to-speak) (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/9032490?hl=en

**USER:**
can my computer read the page to me out loud? my eyes are bad

**ASSISTANT:**
Yes, it can. Is your computer a **Chromebook**, a **Windows** PC, or a **Mac**?

## tr172-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chromebook
- task: Have text read aloud (Select-to-speak) (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/9032490?hl=en

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

## tr172-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chromebook
- task: Have text read aloud (Select-to-speak) (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/9032490?hl=en

**USER:**
Select-to-speak is on in my Chromebook already. But my hand shakes and I cannot hold a key and drag the mouse at the same time. Is there another way to get it to read a paragraph?

**ASSISTANT:**
Yes, you can highlight the text first and then press one shortcut:

1. Highlight the text you want to hear.
2. Press the **Search** key and **s** together.

Your Chromebook reads it aloud and highlights each word. Or, you can select the **Select-to-Speak** icon near the time at the bottom right, then drag over the text without holding a key.

To stop, press **Ctrl** or the **Search** key, or select **Stop**.

## tr172-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chromebook
- task: Have text read aloud (Select-to-speak) (Chromebook) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chromebook/answer/9032490?hl=en

**USER:**
How do I turn on Select-to-speak on my Chromebook and use it?

**ASSISTANT:**
Here is how:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** icon.
3. Select **Accessibility**.
4. Under **Text-to-Speech**, turn on **Select-to-speak**.
5. Highlight some text, then press the **Search** key and **s** together.

**USER:**
It reads, but the pause and skip buttons that pop up do not do anything.

**ASSISTANT:**
Those quick controls can be turned off. To check:

1. Go to **Settings**, then **Accessibility**, then **Text-to-Speech**.
2. Select **Open select-to-speak settings**.
3. Under **Highlighting**, turn on **Enable navigation controls**.
