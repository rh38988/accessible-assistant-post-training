TASKS = [
    {
        "task_id": "TR-167",
        "task_type": "battery_saver",
        "task": "Turn on power saving mode",
        "platform": "Samsung Galaxy",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Samsung US Support: Get the most out of your Galaxy phone or tablet battery", "url": "https://www.samsung.com/us/support/answer/ANS10002534"},
        "source_notes": """Turn on Power saving mode (Galaxy phone): 1. Open Settings, tap Battery. 2. Tap Power saving. 3. Turn on the switches for the options you want (each is next to a setting or customization). 4. Tap the switch at the top of the screen to activate Power saving mode.
Conditions: screens and settings may vary by wireless provider, software version, and model.
Once enabled, options cannot be changed: "You will not be able to adjust the settings once the mode is enabled." To change settings, turn off Power saving mode temporarily, make changes, then turn it back on.
Using Power saving mode can affect app and device performance. Some tasks may take longer, background apps may not update or send notifications.
Page does not mention a Quick settings shortcut.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "How do I turn on power saving mode on my Samsung Galaxy phone?",
                 """Here is how to turn it on:

1. Open **Settings**.
2. Tap **Battery**.
3. Tap **Power saving**.
4. Turn on the switches next to the options you want.
5. Tap the switch at the top of the screen to turn on Power saving mode.

Your screens may look a little different depending on your phone model.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I am going on a long bus ride tomorrow and my Samsung Galaxy phone never seems to hold its charge anymore. My grandson said there is a mode that makes the battery last longer but I did not catch what he called it. Can you walk me through turning it on?",
                 """Yes, it is called Power saving mode. Here is how to turn it on:

1. Open **Settings**.
2. Tap **Battery**.
3. Tap **Power saving**.
4. Turn on the switches next to the options you want.
5. Tap the switch at the top of the screen to turn on Power saving mode.

Be aware that it can make some apps and tasks slower, and background apps may not update or send notifications.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my phone battery dies so fast, how do i turn on the battery saving thing",
                 "I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "my phone battery dies so fast, how do i turn on the battery saving thing",
                 "I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
                 "Samsung Galaxy",
                 """Thanks. Here is how to turn on Power saving mode on your Galaxy:

1. Open **Settings**.
2. Tap **Battery**.
3. Tap **Power saving**.
4. Turn on the switches next to the options you want.
5. Tap the switch at the top of the screen to turn on Power saving mode.

Your screens may look a little different depending on your model.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I have a Samsung Galaxy and I want to use Power saving mode, but I do not want it to just switch everything on without me. I would like to choose which things get turned down first. How do I do that?",
                 """You can choose the options before you start the mode:

1. Open **Settings**.
2. Tap **Battery**.
3. Tap **Power saving**.
4. Turn on the switches only for the options you want. Each switch is next to a setting.
5. Tap the switch at the top of the screen to turn on Power saving mode.

Once the mode is on, you cannot change those options. If you want to change them later, turn the mode off, make your changes, then turn it back on.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "Hi, I just got a Samsung Galaxy and my son says I should be using Power saving mode. Where is it?",
                 """Here is how to turn it on:

1. Open **Settings**.
2. Tap **Battery**.
3. Tap **Power saving**.
4. Turn on the switches next to the options you want.
5. Tap the switch at the top of the screen to turn on Power saving mode.""",
                 "It is on now, but I wanted to change one of the options and I can not touch them anymore.",
                 """That is normal. You cannot change the settings while the mode is on. To fix it:

1. Turn off Power saving mode for a moment.
2. Change the options you want.
3. Turn Power saving mode back on.""",
             ]},
        ],
    },
    {
        "task_id": "TR-168",
        "task_type": "screenshot",
        "task": "Take a screenshot",
        "platform": "Chromebook",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Chromebook Help: Take a screenshot or record your screen", "url": "https://support.google.com/chromebook/answer/10474268?hl=en"},
        "source_notes": """Ways to open the screenshot tool: (1) If the Chromebook has a Screenshot key, press it, then select "Screenshot" in the menu at the bottom and choose a capture type. (2) No Screenshot key: select the Settings icon at the bottom right, then select "Screen Capture", choose a capture type. (3) Press Shift + Ctrl + Show windows, then select "Screenshot" in the bottom menu, choose a capture type. (4) External keyboard without a Show windows key: Ctrl + Shift + F5, then "Screenshot", choose a capture type. (5) Select the time at the bottom of the screen, then select "Screen capture".
Capture types in bottom menu: "Take a full screen screenshot", "Take a partial screenshot", "Take a window screenshot".
Partial tips: press the space bar to change which section you are capturing; press Tab until a corner circle is highlighted, then Up/Down arrows change height, Left/Right change width.
Saved to Downloads folder by default. To change location: Shift + Ctrl + Show windows, select Settings, then "Select folder". Screenshots and recordings are also copied to the clipboard automatically.
Page does not cover stylus or tablet mode.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "How do I take a screenshot of the whole screen on my Chromebook? It has a Screenshot key on the keyboard.",
                 """Here is how:

1. Press the **Screenshot** key on your keyboard.
2. In the menu at the bottom of the screen, select **Screenshot**.
3. Choose **Take a full screen screenshot**.

The picture is saved in your Downloads folder by default, and a copy is also placed on the clipboard.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "My daughter bought me a Chromebook last year and I love it, but I cannot find any key that says screenshot. I want to save a picture of my e-ticket on the screen so I can show it to the person at the door. What should I do?",
                 """If you do not have a Screenshot key, you can use the screen menu instead:

1. Select the **Settings** icon at the bottom right of the screen.
2. Select **Screen Capture**.
3. Choose **Take a full screen screenshot**.

The picture is saved in your Downloads folder by default.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "i need a screenshot of something on my laptop, what do i do",
                 "I can help with that. Is your laptop a **Chromebook**, a **Windows** laptop, or a **Mac**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "i need a screenshot of something on my laptop, what do i do",
                 "I can help with that. Is your laptop a **Chromebook**, a **Windows** laptop, or a **Mac**?",
                 "chromebook",
                 """Thanks. If your Chromebook has a Screenshot key, here is how:

1. Press the **Screenshot** key.
2. In the menu at the bottom, select **Screenshot**.
3. Choose **Take a full screen screenshot**.

If you do not have a Screenshot key, select the **Settings** icon at the bottom right, then select **Screen Capture**, and choose the same option.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "I have a Chromebook with no Screenshot key at all, and I do not want the whole screen, just one part of a recipe on the page. Can you tell me how to capture only part of it?",
                 """You can do that without a Screenshot key:

1. Select the **Settings** icon at the bottom right of the screen.
2. Select **Screen Capture**.
3. Choose **Take a partial screenshot**.

The picture is saved in your Downloads folder by default. While choosing the part, you can press the space bar to change which section you are capturing.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "How do I take a screenshot on my Chromebook? I do have a Screenshot key.",
                 """Here is how:

1. Press the **Screenshot** key.
2. In the menu at the bottom of the screen, select **Screenshot**.
3. Choose a capture type, such as **Take a full screen screenshot**.""",
                 "I think it worked but I have no idea where the picture went.",
                 """By default, screenshots are saved in your **Downloads** folder. A copy is also placed on the clipboard, so you can paste it where you need it.

If you want screenshots to go somewhere else in future:

1. Press **Shift + Ctrl + Show windows**.
2. Select **Settings**.
3. Select **Select folder** and pick the folder you want.""",
             ]},
        ],
    },
    {
        "task_id": "TR-169",
        "task_type": "wifi_connect",
        "task": "Connect to a Wi-Fi network",
        "platform": "Chromebook",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Chromebook Help: Connect your Chromebook to Wi-Fi", "url": "https://support.google.com/chromebook/answer/1047420?hl=en"},
        "source_notes": """1. Select the time at the bottom right, then "Settings". 2. Select "Not Connected". If network name and signal strength appear, already connected. 3. Turn on "Wi-Fi" in the Wi-Fi panel. 4. The Chromebook searches automatically and lists nearby networks; select the one you want.
Open/public network: select network, then "Connect". If a sign-in page opens in the browser, complete it.
Secure network: select network, type the password, then select "Connect".
Hidden network: select "Add connection", then "Add Wi-Fi", enter network details, select "Connect". To reconnect automatically: Settings, "Network", "Wi-Fi", "Known networks", select the network, turn on "Hidden network", select "Save".
Enterprise network: needs administrator certificate; ask administrator.
When connected: network name and signal strength shown in the Wi-Fi panel.
Troubleshooting: administrator may have hidden the network so details must be entered manually. "Automatically connect to this network" to reconnect. Removing saved info: Known networks, More, "Forget". Ongoing problems: Google Help article on fixing Wi-Fi problems.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "How do I connect my Chromebook to my home Wi-Fi? It needs a password.",
                 """Here is how to connect:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Network**, then **Wi-Fi**.
4. Select your network.
5. Type the password.
6. Select **Connect**.

If Wi-Fi is off, first select the time, select **Not Connected**, and turn on **Wi-Fi**. Then do the steps above.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "I am at a coffee shop with my Chromebook and they said the Wi-Fi is open, no password needed. I have never done this before and I do not want to mess anything up. How do I get on their network?",
                 """It is simple. Here are the steps:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Network**, then **Wi-Fi**.
4. Select the coffee shop's network.
5. Select **Connect**.

Since this network has no password, your info is available to other people on it.

If Wi-Fi is off, first select the time, select **Not Connected**, and turn on **Wi-Fi**. If a sign-in page opens in your browser, finish it to complete the connection.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "how do I get on the wifi",
                 "I can help with that. What device do you want to connect: a **Chromebook**, a **phone**, or a different computer?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "how do I get on the wifi",
                 "I can help with that. What device do you want to connect: a **Chromebook**, a **phone**, or a different computer?",
                 "my chromebook",
                 """Thanks. Here is how to connect your Chromebook:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Network**, then **Wi-Fi**.
4. Select your network.
5. If it asks, type the password.
6. Select **Connect**.

If Wi-Fi is off, first select the time, select **Not Connected**, and turn on **Wi-Fi**. Then do the steps above.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "My Chromebook keeps forgetting my Wi-Fi and I am tired of typing the password. I am connecting at my house right now. Is there a way to connect and have it reconnect by itself next time?",
                 """Yes. First connect, then turn on automatic reconnecting:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Network**, then **Wi-Fi**.
4. Select your network.
5. Type the password.
6. Select **Connect**.
7. Select your network again in the Wi-Fi list, then turn on **Automatically connect to this network**.

If Wi-Fi is off, first select the time, select **Not Connected**, and turn on **Wi-Fi**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "I moved to a new apartment. Please help me get my Chromebook on the new password-protected Wi-Fi.",
                 """Here is how:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Network**, then **Wi-Fi**.
4. Select your network.
5. Type the password.
6. Select **Connect**.

If Wi-Fi is off, first select the time, select **Not Connected**, and turn on **Wi-Fi**.""",
                 "My network name is not shown because the router is set to hide its name, but I know the name and password.",
                 """You can add the network by hand:

1. Select the time at the bottom right, then select **Settings**.
2. Select **Network**.
3. Select **Add connection**, then **Add Wi-Fi**.
4. In the box that appears, type the network name and the password you already know.
5. Select **Connect**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-170",
        "task_type": "software_update",
        "task": "Update the Chromebook",
        "platform": "Chromebook",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Chromebook Help: Update your Chromebook's operating system", "url": "https://support.google.com/chromebook/answer/177889?hl=en"},
        "source_notes": """Check and install: 1. Turn on Chromebook and connect to Wi-Fi. 2. At bottom right select the time, then the Settings gear icon. 3. At bottom left select "About ChromeOS". 4. Under "Google ChromeOS" find current version. 5. Select "Check for updates". If this option is not shown, the Chromebook is likely up to date. 6. If an update is found it downloads automatically. On mobile data you get an alert showing how much data the update needs and you can stop or continue. Plug in the charger to avoid interruptions.
Finishing: when download finishes, look at bottom right next to the date for an "Update device" notification. Select "Restart". Chromebook restarts and installs. At work/school: blue = recommended, orange = required; select "Restart to update".
Troubleshooting if update does not download or device is several versions behind, in order: turn off and on; disconnect mobile data or phone connection and use Wi-Fi or Ethernet; reset (personal files kept); recover (erases everything, back up first). Work/school devices: contact administrator. Older devices can stop receiving updates: Settings > About ChromeOS > Additional details > "Update schedule".""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "How do I check for updates on my Chromebook?",
                 """Make sure your Chromebook is on and connected to Wi-Fi. Then:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** gear icon.
3. At the bottom left, select **About ChromeOS**.
4. Select **Check for updates**.

If an update is found, it downloads by itself. If you do not see **Check for updates**, your Chromebook is most likely up to date.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "My Chromebook finished downloading something and now there is a little message near the date at the bottom right that says Update device. I am not sure whether to click it or ignore it. It is my own home Chromebook, not from work. What do I do?",
                 """That message means an update is ready. To install it:

1. Select the **Update device** message at the bottom right, next to the date.
2. Select **Restart**.

Your Chromebook will restart and install the update.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "how do i update my computer, it keeps telling me to",
                 "I can help with that. Is your computer a **Chromebook**, a **Windows** PC, or a **Mac**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "how do i update my computer, it keeps telling me to",
                 "I can help with that. Is your computer a **Chromebook**, a **Windows** PC, or a **Mac**?",
                 "its a chromebook",
                 """Thanks. Connect your Chromebook to Wi-Fi first. Then:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** gear icon.
3. At the bottom left, select **About ChromeOS**.
4. Select **Check for updates**.
5. When the download finishes, select the **Update device** message at the bottom right.
6. Select **Restart**.

If you do not see **Check for updates**, your Chromebook is most likely up to date.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "I am traveling and my Chromebook is only on my phone's mobile data right now, nothing else. I want to update it but I am worried about using up my data. Can I still do it and will it warn me?",
                 """Yes, it will warn you. Here is how to check for the update:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** gear icon.
3. At the bottom left, select **About ChromeOS**.
4. Select **Check for updates**.

If an update is found, you will get an alert showing how much data it needs. You can then stop or continue. It also helps to plug in the charger so the update is not interrupted.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "How do I update my Chromebook? It is connected to Wi-Fi.",
                 """Here is how:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** gear icon.
3. At the bottom left, select **About ChromeOS**.
4. Select **Check for updates**.
5. When the download finishes, select **Restart** in the **Update device** message near the date.""",
                 "I did that but the update never seems to download, it just sits there.",
                 """Try these in order, and test after each one:

1. Turn your Chromebook off, then back on.
2. If you have trouble with your phone or mobile data connection while updating, disconnect it and connect to Wi-Fi or Ethernet instead.
3. If it still will not download, the next step is a reset. You can reset your Chromebook without deleting your personal files.
4. If that does not work, recovery is the last step. Recovery permanently erases everything on the drive, including downloads, so back up your files first if you can.""",
             ]},
        ],
    },
    {
        "task_id": "TR-171",
        "task_type": "magnifier",
        "task": "Zoom in or magnify the screen",
        "platform": "Chromebook",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Chromebook Help: Zoom in or magnify your Chromebook screen", "url": "https://support.google.com/chromebook/answer/6320705?hl=en"},
        "source_notes": """Browser page zoom (page only): Ctrl and + bigger, Ctrl and - smaller, Ctrl + 0 reset.
Whole-screen resolution (includes shelf and tabs): Ctrl + Shift and + bigger (lower resolution), Ctrl + Shift and - smaller, Ctrl + Shift + 0 reset. Touchscreen: touch and hold with 2 fingers, pinch.
Full-screen magnifier: quick toggle Ctrl + Search + m (or Ctrl + Launcher + m). Or: select the time at the bottom right (or Alt + Shift + s), select Settings, then Accessibility. Under "Display", turn on "Full screen magnifier". Choose movement mode: "Move screen continuously as mouse moves", "Move screen keeping mouse at center of screen", "Move screen when mouse touches edge of screen". Set zoom next to "Fullscreen zoom level". Move around: Ctrl + Alt + arrow keys.
Docked magnifier (top third of screen): quick toggle Ctrl + Search + d (or Ctrl + Launcher + d). Or same settings path, turn on "Docked magnifier" under "Display". Set "Docked zoom level".
Change magnification level (either): Ctrl + Alt + Brightness up/down.
Troubleshooting: Ctrl + Shift shortcuts change screen resolution, not just page; use Ctrl + +/- for page only. The magnifiers must be turned on in Accessibility settings before their shortcuts work as described.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "How do I turn on the full screen magnifier on my Chromebook?",
                 """Here is how to turn it on in Settings:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Accessibility**.
4. Under **Display**, turn on **Full screen magnifier**.

You can also choose how the screen moves and set the zoom level next to **Fullscreen zoom level**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "My eyesight is getting worse and I read with my Chromebook a lot. I do not want to enlarge the whole screen, I would rather have a strip at the top that shows things bigger while the rest stays normal. I have heard there is a docked kind of magnifier. How do I get it?",
                 """Yes, the docked magnifier does that. It magnifies the top third of the screen. To turn it on:

1. Select the time at the bottom right of the screen.
2. Select **Settings**.
3. Select **Accessibility**.
4. Under **Display**, turn on **Docked magnifier**.
5. Set how big you want it next to **Docked zoom level**.

Move your cursor to change the area that is magnified.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "Chromebook",
             "messages": [
                 "everything on my chromebook is too small, how do i make it bigger",
                 "I can help with that. Do you want to enlarge just the **web page**, or **magnify the whole screen**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "everything on my chromebook is too small, how do i make it bigger",
                 "I can help with that. Do you want to enlarge just the **web page**, or **magnify the whole screen**?",
                 "just the web page",
                 """To make just the web page bigger:

1. Press **Ctrl** and **+** together.
2. Press it again to go bigger still.

To make the page smaller again, press **Ctrl** and **-**. To go back to normal size, press **Ctrl** and **0**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "I only want the website to look bigger on my Chromebook. I do not want the bar at the bottom or the tabs to change size, and I do not want to go into any settings. Just a keyboard shortcut please.",
                 """Use this shortcut, which only changes the page:

1. Press **Ctrl** and **+** together to make the page bigger.
2. Press it again for even bigger.

To make it smaller, press **Ctrl** and **-**. To reset, press **Ctrl** and **0**.

Do not use the shortcuts with **Shift** added. Those change the whole screen, including the bottom bar and tabs.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "Is there a keyboard shortcut for the full screen magnifier on a Chromebook?",
                 """Yes. Press **Ctrl + Search + m** to magnify your whole screen. If your keyboard has a Launcher key instead of a Search key, press **Ctrl + Launcher + m**.

To make it bigger or smaller, press **Ctrl + Alt** and the brightness up or down key.""",
                 "I pressed it and nothing happened.",
                 """I am not sure why that happened. You can turn the magnifier on from Settings instead:

1. Select the time at the bottom right of the screen.
2. Select **Settings**, then **Accessibility**.
3. Under **Display**, turn on **Full screen magnifier**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-172",
        "task_type": "read_aloud",
        "task": "Have text read aloud (Select-to-speak)",
        "platform": "Chromebook",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Chromebook Help: Hear text read aloud", "url": "https://support.google.com/chromebook/answer/9032490?hl=en"},
        "source_notes": """1. Select the time at the bottom right (or Alt + Shift + s), select the Settings icon, then "Accessibility". 2. Under "Text-to-Speech", turn on "Select-to-speak". 3. Selection methods (any one): Option 1: press and hold the Search key, then drag the pointer over the text. Option 2: highlight the text, then press the Search key + "s". Option 3: select the "Select-to-Speak" icon near the time at the bottom right, then drag the pointer over the text. Touchscreen: tap a line of text or drag finger across area. 4. Chromebook reads the selection aloud and highlights each word as spoken. 5. Stop: press Ctrl or the Search key, or select the "Stop" button. Search key and Launcher key work the same.
Optional: Settings > "Accessibility" > "Text-to-Speech" > "Open select-to-speak settings"; under "Highlighting": "Highlight each word as it is spoken", "Color for word highlights", "Shade background content".
Troubleshooting: pause, play, speed, skip controls do not work: check "Enable navigation controls" under "Highlighting" in Select-to-speak settings; when off, quick controls are disabled. Voice, language, volume: separate article.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "How can I make my Chromebook read the text on the screen out loud to me?",
                 """You can use Select-to-speak. First turn it on:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** icon.
3. Select **Accessibility**.
4. Under **Text-to-Speech**, turn on **Select-to-speak**.

Then press and hold the **Search** key and drag the pointer over the text you want to hear. Your Chromebook reads it aloud and highlights each word as it is spoken.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "I have a touchscreen Chromebook and reading long articles tires my eyes out. My nephew said it can read to me but I do not know how. Select-to-speak is already turned on in my settings. How do I get it to read one paragraph?",
                 """Since Select-to-speak is already on, you only need to pick the text:

1. Tap a line of text, or drag your finger across the paragraph you want.
2. Your Chromebook reads it aloud and highlights each word as it is spoken.

To stop it, press **Ctrl** or the **Search** key, or select the **Stop** button.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "incomplete", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "can my computer read the page to me out loud? my eyes are bad",
                 "Yes, it can. Is your computer a **Chromebook**, a **Windows** PC, or a **Mac**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "can my computer read the page to me out loud? my eyes are bad",
                 "Yes, it can. Is your computer a **Chromebook**, a **Windows** PC, or a **Mac**?",
                 "Chromebook",
                 """Good, your Chromebook has Select-to-speak. First turn it on:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** icon.
3. Select **Accessibility**.
4. Under **Text-to-Speech**, turn on **Select-to-speak**.

Then press and hold the **Search** key and drag the pointer over the text. Your Chromebook reads it aloud and highlights each word.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "Select-to-speak is on in my Chromebook already. But my hand shakes and I cannot hold a key and drag the mouse at the same time. Is there another way to get it to read a paragraph?",
                 """Yes, you can highlight the text first and then press one shortcut:

1. Highlight the text you want to hear.
2. Press the **Search** key and **s** together.

Your Chromebook reads it aloud and highlights each word. Or, you can select the **Select-to-Speak** icon near the time at the bottom right, then drag over the text without holding a key.

To stop, press **Ctrl** or the **Search** key, or select **Stop**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Chromebook",
             "messages": [
                 "How do I turn on Select-to-speak on my Chromebook and use it?",
                 """Here is how:

1. Select the time at the bottom right of the screen.
2. Select the **Settings** icon.
3. Select **Accessibility**.
4. Under **Text-to-Speech**, turn on **Select-to-speak**.
5. Highlight some text, then press the **Search** key and **s** together.""",
                 "It reads, but the pause and skip buttons that pop up do not do anything.",
                 """Those quick controls can be turned off. To check:

1. Go to **Settings**, then **Accessibility**, then **Text-to-Speech**.
2. Select **Open select-to-speak settings**.
3. Under **Highlighting**, turn on **Enable navigation controls**.""",
             ]},
        ],
    },
]
