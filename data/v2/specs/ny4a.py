TASKS = [
    {
        "task_id": "TR-160",
        "task_type": "screenshot",
        "task": "Take a screenshot",
        "platform": "Samsung Galaxy",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Samsung US Support: How to take a screenshot on a Samsung phone or tablet", "url": "https://www.samsung.com/us/support/answer/ANS10002500/"},
        "source_notes": """Ways to screenshot on a Galaxy phone.
1. Button combination: press and hold the Power/Side and Volume Down buttons at the same time, then release after a brief moment. The screen flashes to confirm. Button placement can vary by model.
2. Palm swipe (must be turned on first): swipe down from the top right corner with two fingers to open the Quick panel. Tap Settings (gear icon), swipe to and tap Advanced features. Tap Palm swipe to capture and turn on its switch. Then swipe the edge of your hand across the screen to capture. (No confirmation described.)
3. Voice: say "Hey Bixby, take a screenshot" or "Hey Google, take a screenshot".
4. S Pen: Air command, Screen write (only S Pen devices).
5. Tasks Edge panel: Take screenshot shortcut.
6. Full page (Scroll capture): take a standard screenshot first, then tap the Scroll capture icon (two downward arrows). Lengthy content is captured as one image.
Where saved: open Gallery, tap the Albums tab, tap the Screenshots folder. Or My Files, then tap Images. To share: select it, tap the Share icon at the bottom, choose a method.
Editing after capture: tap the Draw icon (pencil) at the bottom to draw on or crop.
Notes: some apps or screens block screenshots for privacy or security reasons. Settings availability may differ by carrier, software version, or model.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "How do I take a screenshot on my Samsung Galaxy phone?",
                 """You can capture your screen with two buttons. Here is how.

1. Go to the screen you want to capture.
2. Press and hold the **Power** (side) button and the **Volume Down** button at the same time.
3. Let go after a moment.

The screen flashes to show the picture was taken.

If nothing happens, check where the buttons are on your model, since their position can differ.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "My daughter sent me a long recipe on a website and I want to keep the whole thing as one picture, not a bunch of little pieces. I have a Samsung Galaxy phone. The recipe goes way past the bottom of the screen. Is there a way to get all of it?",
                 """Yes, there is a way to capture a long page as one picture.

1. Open the recipe on your screen.
2. Press and hold the **Power** (side) button and the **Volume Down** button together, then let go. The screen flashes.
3. Tap the **Scroll capture** icon. It looks like two arrows pointing down.

Long content is then captured as one image.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I need to save what is on my screen as a picture. How do I do that?",
                 "I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I need to save what is on my screen as a picture. How do I do that?",
                 "I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
                 "It's a Samsung Galaxy.",
                 """Thank you. On a Samsung Galaxy it takes two buttons.

1. Go to the screen you want to capture.
2. Press and hold the **Power** (side) button and the **Volume Down** button at the same time.
3. Let go after a moment.

The screen flashes to show the picture was taken.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I have a Samsung Galaxy and my hands have arthritis, so pressing two buttons at once is really hard for me. Is there another way to take a screenshot that does not use the buttons?",
                 """Yes. You can turn on a swipe that captures the screen with the side of your hand.

1. Swipe down from the top right corner with two fingers to open the **Quick panel**.
2. Tap **Settings**, the gear icon.
3. Swipe to **Advanced features** and tap it.
4. Tap **Palm swipe to capture** and turn its switch on.

After that, swipe the edge of your hand across the screen to take a screenshot.

You can also say "Hey Google, take a screenshot" or "Hey Bixby, take a screenshot".""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "Samsung Galaxy here. How can I take a picture of what is on my screen?",
                 """You can do that with two buttons.

1. Go to the screen you want to capture.
2. Press and hold the **Power** (side) button and the **Volume Down** button at the same time.
3. Let go after a moment.

The screen flashes to show the picture was taken.""",
                 "The screen flashed, but now I can't find the picture anywhere.",
                 """Good, that means it worked. You can find it in either of these places.

1. Open **Gallery**, tap the **Albums** tab, then tap the **Screenshots** folder.
2. Or open **My Files** and tap **Images**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-161",
        "task_type": "software_update",
        "task": "Update the phone's software",
        "platform": "Samsung Galaxy",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Samsung US Support: How to update your Galaxy phone or tablet", "url": "https://www.samsung.com/us/support/answer/ANS10002027/"},
        "source_notes": """Method 1, on the phone: (1) Swipe down with two fingers from the top-right corner, tap the Settings icon. (2) Swipe to and tap Software update or System updates (name varies by model). (3) Tap Download and install, Check for system updates, or Check for software updates, depending on carrier. If an update is available it should start downloading; on some devices tap Download now. (4) When the download finishes, follow the on-screen instructions to install it.
Current version: Settings, About phone, Software information.
Method 2, Smart Switch on a Windows PC or Mac: connect Galaxy with the USB cable, open Smart Switch, let it detect the device, if an update is available select Update and follow the prompts. Keep the cable connected and do not use the device until it finishes. The device will reboot.
What is in the update: Settings, Software update (or System updates), tap Last update, then All changes.
Conditions: some carriers require Wi-Fi to check for and install updates. When Auto download over Wi-Fi is on, the phone updates automatically on Wi-Fi; when off you must update manually. During the update the device cannot be used, files are inaccessible, calls (including emergency calls) are not possible. Depending on version you may need to repeat the process more than once.
Troubleshooting: if the network drops mid-update the update may fail; reconnect and try again. Page does not address battery or storage.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "How do I update the software on my Samsung Galaxy phone?",
                 """You can do it right on the phone. Here is how.

1. Swipe down with two fingers from the top right corner of the screen.
2. Tap the **Settings** icon.
3. Swipe to **Software update** and tap it. On some phones it is called **System updates**.
4. Tap **Download and install**. On some phones you may need to tap **Download now**.
5. When the download finishes, follow the instructions on the screen to install it.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "My grandson keeps telling me my Samsung Galaxy is out of date and that I need to get the latest software. I have a laptop here that I use for email, and I would rather do it with the laptop and the cable that came in the box if that works. What should I do?",
                 """Yes, you can update with a computer by using a program called Smart Switch.

1. Make sure the Smart Switch program is installed on your computer. If it is not, you can get it from Samsung's Smart Switch page: https://www.samsung.com/us/support/owners/app/smart-switch
2. Plug your Galaxy into the computer with the USB cable from the box. Some computers need a USB adapter.
3. Open **Smart Switch** on the computer and let it find your phone.
4. If an update is available, click **Update** and follow the prompts.

Keep the cable plugged in and do not use the phone until it finishes. The phone will restart by itself.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "My phone keeps saying it needs an update. How do I do it?",
                 "I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "My phone keeps saying it needs an update. How do I do it?",
                 "I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
                 "Samsung Galaxy",
                 """Thanks. You can update it right on the phone.

1. Swipe down with two fingers from the top right corner of the screen.
2. Tap the **Settings** icon.
3. Swipe to **Software update** and tap it. On some phones it is called **System updates**.
4. Tap **Download and install**. On some phones you may need to tap **Download now**.
5. When the download finishes, follow the instructions on the screen to install it.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I have a Samsung Galaxy and I don't own a computer, so I can't plug it into anything. Before I update, I would also like to know what the update changes. Can I see that on the phone?",
                 """Yes, you can see that on the phone, and you do not need a computer.

To see what the update includes:
1. Swipe down with two fingers from the top right corner, then tap the **Settings** icon.
2. Swipe to **Software update** (or **System updates**) and tap it.
3. Tap **Last update**, then tap **All changes**.

To update on the phone:
1. Go back to **Software update** (or **System updates**).
2. Tap **Download and install**. On some phones you may need to tap **Download now**.
3. When it finishes downloading, follow the instructions on the screen.

Note that you cannot use the phone while it installs, and that includes emergency calls.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "Please walk me through updating my Samsung Galaxy phone's software.",
                 """Here is how to update it on the phone.

1. Swipe down with two fingers from the top right corner of the screen.
2. Tap the **Settings** icon.
3. Swipe to **Software update** and tap it. On some phones it is called **System updates**.
4. Tap **Download and install**. On some phones you may need to tap **Download now**.
5. When the download finishes, follow the instructions on the screen to install it.""",
                 "I looked all through Settings and there is no Software update. Where did it go?",
                 """On some phones it has a different name. Try this.

1. In **Settings**, swipe down the list and look for **System updates**.
2. Tap it, then tap **Download and install**, **Check for system updates**, or **Check for software updates**. Which one you see depends on your phone company.
3. If an update is found and you see **Download now**, tap it.""",
             ]},
        ],
    },
    {
        "task_id": "TR-162",
        "task_type": "wifi_connect",
        "task": "Connect to a Wi-Fi network",
        "platform": "Samsung Galaxy",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Samsung Canada Support: Connect your Samsung Galaxy to the Internet", "url": "https://www.samsung.com/ca/support/mobile-devices/connect-your-samsung-galaxy-to-the-internet/"},
        "source_notes": """(The Samsung US pages read gave only Wi-Fi turn-on and troubleshooting, not the full connect steps, so this official Samsung page was used.)
Steps: (1) Open Settings and tap Connections. (2) Tap Wi-Fi. (3) If Wi-Fi is off, tap the toggle to turn it on. Available networks appear in the list. (4) Tap the name of the network you want. (5) If the network is password-protected, enter the password and tap Connect. (6) When it succeeds, the network name appears under "Current network" with "Connected" beneath it.
Troubleshooting: mistyped passwords are the most common cause of failure; use the eye icon in the password field to check what you entered. A home router password is often printed on a sticker on the router. Weak signal: move closer to the access point. Public Wi-Fi: some networks have no password but send you to a sign-in page. Soft reset: turn Wi-Fi off in Connections, wait a few seconds, turn it back on; restarting the router can also help. Forget and rejoin can clear errors (US page: Settings, Connections, Wi-Fi, press and hold the network, tap Forget network). Full reset: Settings, General management, Reset, Reset Wi-Fi and Bluetooth settings, Reset settings (no confirmation, you must reconnect Wi-Fi and Bluetooth devices, personal data not affected).""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "How do I connect my Samsung Galaxy phone to my home Wi-Fi?",
                 """Here is how to join a Wi-Fi network.

1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. If Wi-Fi is off, tap the switch to turn it on. The networks nearby will appear in a list.
4. Tap the name of your network.
5. Type the password, then tap **Connect**.

When it works, your network name shows under **Current network** with the word **Connected** under it.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I am visiting my sister for the week and she gave me her Wi-Fi name and password on a piece of paper. I have a Samsung Galaxy and I think the Wi-Fi on my phone is switched off because I turned it off on the plane. I don't want to mess anything up. What do I tap?",
                 """You will not mess anything up. Follow these steps.

1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. Tap the switch to turn Wi-Fi on. The networks nearby will appear in a list.
4. Tap the name your sister wrote down.
5. Type the password from the paper, then tap **Connect**.

When it works, her network name shows under **Current network** with **Connected** under it.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "My phone says I have no internet at home. How do I get it onto my Wi-Fi?",
                 "I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "My phone says I have no internet at home. How do I get it onto my Wi-Fi?",
                 "I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
                 "its a samsung galaxy",
                 """Thanks. Here is how to join your Wi-Fi.

1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. If Wi-Fi is off, tap the switch to turn it on.
4. Tap the name of your home network in the list.
5. Type the password, then tap **Connect**.

When it works, the network name shows under **Current network** with **Connected** under it.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I just got a new internet router and my Samsung Galaxy needs to join it. The problem is I never wrote down the password and I have no idea what it is. Where would I find it, and what do I tap on the phone?",
                 """The password is often printed on a sticker on the router, so look there first.

Then on your phone:
1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. If Wi-Fi is off, tap the switch to turn it on.
4. Tap the name of your router's network.
5. Type the password from the sticker, then tap **Connect**.

When it works, the network name shows under **Current network** with **Connected** under it.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "Samsung Galaxy phone. Please tell me how to connect to Wi-Fi.",
                 """Here is how to join a Wi-Fi network.

1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. If Wi-Fi is off, tap the switch to turn it on.
4. Tap the name of your network in the list.
5. Type the password, then tap **Connect**.

When it works, the network name shows under **Current network** with **Connected** under it.""",
                 "I did all that but it will not connect. I think I might have typed the password wrong.",
                 """A mistyped password is the most common reason. Try this.

1. Tap the network name again.
2. In the password box, tap the eye icon to see what you typed.
3. Fix any mistakes, then tap **Connect**.

If it still fails, go to **Settings**, **Connections**, then turn Wi-Fi off, wait a few seconds, and turn it back on.""",
             ]},
        ],
    },
    {
        "task_id": "TR-163",
        "task_type": "block_number",
        "task": "Block a phone number",
        "platform": "Samsung Galaxy",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Samsung US Support: Block a phone number or contact on your Galaxy phone", "url": "https://www.samsung.com/us/support/answer/ANS10002869/"},
        "source_notes": """Requires Android 9.0 or later; availability varies by carrier, version, and model.
Block a saved contact (Contacts app): open Contacts, tap the contact, tap More, tap Block contact, tap Block to confirm.
Block from Recents (Phone app): open Phone, select the Recents tab, select the number, tap Menu (three horizontal lines with three dots), tap Block, tap Block to confirm.
Block by entering a number (Phone app): open Phone, tap More options (three vertical dots), tap Settings, tap Block numbers, type the number, tap Add (plus sign). Can also tap Recents or Contacts, select a number, tap Done.
Block from a message (Samsung Messages): open Samsung Messages, select the conversation, touch and hold the conversation, tap More, tap Block, tap Block again to confirm.
Block by entering a number in Messages: Samsung Messages, Contacts tab, More options, Settings, Block numbers and spam, Block numbers, enter number, tap Add (plus sign).
Unblock: Contacts, select contact, More, Unblock contact. Or Phone, More options, Settings, Block numbers, tap the red Minus icon next to the number.
Blocked contacts stay in your Contacts list but can't reach you. Page does not say what blocked callers hear. To stop voicemails from specific callers, contact your carrier.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "Someone keeps calling me from a number I don't know. How do I block it on my Samsung Galaxy phone?",
                 """You can block it from your list of recent calls.

1. Open the **Phone** app and tap the **Recents** tab.
2. Tap the number that keeps calling.
3. Tap **Menu**. It looks like three lines with three dots.
4. Tap **Block**.
5. Tap **Block** again to confirm.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I have a Samsung Galaxy. A salesman is saved in my contacts from a while back, and now he calls me every single day about insurance. I don't want to delete him because I might forget, but I never want to hear from him again. Can I just block him from the contacts?",
                 """Yes. A blocked contact stays in your list but cannot reach you.

1. Open the **Contacts** app.
2. Tap his name.
3. Tap **More**.
4. Tap **Block contact**.
5. Tap **Block** to confirm.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "There is a number I want to stop hearing from. How do I block it?",
                 "I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "There is a number I want to stop hearing from. How do I block it?",
                 "I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
                 "Samsung Galaxy",
                 """Thanks. If the number called you recently, you can block it from your recent calls.

1. Open the **Phone** app and tap the **Recents** tab.
2. Tap the number.
3. Tap **Menu**. It looks like three lines with three dots.
4. Tap **Block**.
5. Tap **Block** again to confirm.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "My Samsung Galaxy gets text messages from a number that keeps sending me ads. It never calls, it only texts, so it is not in my call list. How do I block it from the text messages?",
                 """You can block it right from the conversation.

1. Open the **Samsung Messages** app.
2. Touch and hold the conversation from that number.
3. Tap **More**.
4. Tap **Block**.
5. Tap **Block** again to confirm.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "How do I block a number on my Samsung Galaxy phone?",
                 """You can block a number from your recent calls.

1. Open the **Phone** app and tap the **Recents** tab.
2. Tap the number.
3. Tap **Menu**. It looks like three lines with three dots.
4. Tap **Block**.
5. Tap **Block** again to confirm.""",
                 "The number I want to block isn't in my recent calls. I only have it written on paper.",
                 """You can type the number in yourself.

1. Open the **Phone** app and tap **More options**, the three dots.
2. Tap **Settings**.
3. Tap **Block numbers**.
4. Type the number, then tap the plus sign to add it.""",
             ]},
        ],
    },
    {
        "task_id": "TR-164",
        "task_type": "flashlight",
        "task": "Turn the flashlight on and off",
        "platform": "Samsung Galaxy",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Samsung US Support: Use the flashlight on your Galaxy phone", "url": "https://www.samsung.com/us/support/answer/ANS10003351/"},
        "source_notes": """Method 1, Quick settings panel (most Galaxy phones): swipe down from the top right of the screen to open the Quick settings panel. Tap the Flashlight icon to turn the light on. Tap the Flashlight icon again to turn it off. The icon looks highlighted/active while the light is on. The light uses the phone's camera LED. If you can't find the icon, depending on setup, swipe left in the panel to reveal it. You can rearrange the order or add icons (separate guide, no steps given here).
Method 2: physical XCover or Top key, XCover6 Pro only, must be programmed first in the Advanced features menu.
Brightness: swipe down from top right to open Quick settings panel, tap and hold the Flashlight icon, tap the switch to turn the light on, drag the slider to set brightness. A brightness slider and on/off switch appear. If the slider is grayed out, turn the flashlight on first using the switch.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "How do I turn on the flashlight on my Samsung Galaxy phone?",
                 """It is quick to do from the top of the screen.

1. Swipe down from the top right of the screen to open the **Quick settings** panel.
2. Tap the **Flashlight** icon. The light comes on.
3. To turn it off, tap the **Flashlight** icon again.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I use the flashlight on my Samsung Galaxy to walk to the mailbox at night, but it is so bright that it blinds me and I can't see the path. Is there a way to make the light dimmer? I only know how to turn it on and off.",
                 """Yes, you can set how bright it is.

1. Swipe down from the top right of the screen to open the **Quick settings** panel.
2. Press and hold the **Flashlight** icon.
3. Tap the switch to turn the light on.
4. Drag the slider to make the light brighter or dimmer.

If the slider looks grayed out, turn the light on with the switch first.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I need some light to look under the bed. How can I make the phone light up?",
                 "I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I need some light to look under the bed. How can I make the phone light up?",
                 "I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
                 "It's a Galaxy, made by Samsung.",
                 """Thanks. On your Galaxy, the flashlight is at the top of the screen.

1. Swipe down from the top right of the screen to open the **Quick settings** panel.
2. Tap the **Flashlight** icon. The light comes on.
3. To turn it off, tap the **Flashlight** icon again.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "The power went out and it is pitch dark in my house. I have a Samsung Galaxy and I can barely see the screen, so I don't want to go hunting through apps or settings. What is the fastest way to get the light on, and then off again later?",
                 """The fastest way is one swipe and one tap.

1. Swipe down from the top right of the screen to open the **Quick settings** panel.
2. Tap the **Flashlight** icon. The light comes on.

Later, to turn it off, open the same panel and tap the **Flashlight** icon again.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "Samsung Galaxy: how do I use the flashlight?",
                 """Here is how to turn it on and off.

1. Swipe down from the top right of the screen to open the **Quick settings** panel.
2. Tap the **Flashlight** icon. The light comes on.
3. To turn it off, tap the **Flashlight** icon again.""",
                 "I swiped down and I see a bunch of icons but none of them is a flashlight.",
                 """It may be on another page of the panel.

1. Swipe left in the **Quick settings** panel to see more icons.
2. Look for the **Flashlight** icon and tap it.""",
             ]},
        ],
    },
    {
        "task_id": "TR-165",
        "task_type": "easy_mode",
        "task": "Turn on Easy mode for bigger icons and a simpler screen",
        "platform": "Samsung Galaxy",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Samsung Support (UAE): Using Easy Mode on my Samsung Phone", "url": "https://www.samsung.com/ae/support/mobile-devices/using-easy-mode-on-my-samsung-phone"},
        "source_notes": """(No Samsung US page was found for Easy mode; this is an official Samsung page.)
Turn on: open the Settings app, tap Display, select Easy Mode, turn on the switch.
What changes: the page says once Easy Mode is active, "your screen layout will adjust with larger icons and fonts", with enlarged spacing for easier navigation. No other specific layout changes listed.
Turn off: Settings, Display, Easy Mode, turn off the switch.
Conditions: device must support Easy Mode (page lists Galaxy S24, S25, S26, Z Fold, Z Flip, and A series). Keep device on latest software for best performance. If the changes don't apply, restart the device and try again. Outdated firmware, software glitches, or low storage can prevent Easy Mode from working correctly.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "How do I make the icons and writing bigger on my Samsung Galaxy phone? I heard there is an Easy mode.",
                 """Yes, Easy Mode makes the icons and text larger. Here is how to turn it on.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Easy Mode**.
4. Turn on the switch.

Your screen will change to larger icons and text.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "My eyesight is not what it used to be and I keep tapping the wrong things on my Samsung Galaxy phone because everything is so small and crowded. My son said there is some kind of simple setting that spreads everything out and makes it bigger. Where do I find it?",
                 """Your son means Easy Mode. It makes icons and text larger and spaces things out.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Easy Mode**.
4. Turn on the switch.

If the change does not show up, restart the phone and try again.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "Everything on my phone is too small. Is there a simple mode with bigger icons?",
                 "I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "Everything on my phone is too small. Is there a simple mode with bigger icons?",
                 "I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
                 "Samsung Galaxy.",
                 """Thank you. Your phone has one called Easy Mode.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Easy Mode**.
4. Turn on the switch.

Your screen will change to larger icons and text.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I turned on Easy Mode on my Samsung Galaxy last week, but now I want my old screen back. I do not want to reset the whole phone or lose anything. Can I just switch Easy Mode off?",
                 """Yes. You only need to turn that one setting off.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Easy Mode**.
4. Turn the switch off.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "Samsung Galaxy phone. How do I turn on Easy Mode?",
                 """Here is how to turn it on.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Easy Mode**.
4. Turn on the switch.

Your screen will change to larger icons and text.""",
                 "I turned the switch on but nothing looks different. The icons are still small.",
                 """Try restarting the phone, then turn Easy Mode on again.

1. Restart your phone.
2. Open **Settings**, tap **Display**, then tap **Easy Mode**.
3. Check that the switch is on.

Easy Mode can fail to apply if the phone's software is out of date, if it has a glitch, or if its storage is nearly full.""",
             ]},
        ],
    },
    {
        "task_id": "TR-166",
        "task_type": "find_lost_phone",
        "task": "Find a lost phone",
        "platform": "Samsung Galaxy",
        "category": "technical_support",
        "sensitive": True,
        "source": {"title": "Samsung US Support: How to locate your lost Samsung Galaxy phone or tablet", "url": "https://www.samsung.com/us/support/answer/ANS00080182"},
        "source_notes": """Requirements (set up before the phone is lost): phone must be on (if powered off only the last known location is available); needs a stable network connection; a Samsung account must be added to the device; in Settings, Security and privacy, Lost device protection, turn on Allow this phone (or tablet) to be found, Send last location, and Offline finding.
Steps: (1) In a web browser, go to the SmartThings Find website or the Samsung Find website and sign in with your Samsung account (can also use these from a Galaxy phone). (2) Select your device from the list on the left to see its location on the map. (3) Options if unsure where it is: Ring: select your device, Ring, Start; it rings for one minute even on Mute or Vibrate; stop by swiping Dismiss on the device or selecting Stop on the website. Lock: select device, Lock, Next, create a PIN and enter it twice, optionally add emergency contact and lock screen message, select Lock. Track location: select device, Track location, Start (updates every 15 minutes; Stop then Agree to stop). Erase data: select device, Erase data, may need to sign in again, read info, select Erase; back up first if you can.
(4) With a Galaxy watch: press the Home button on the watch, open Samsung Find, select your device, tap the Ring icon. Watch must be connected to the phone via Bluetooth, Wi-Fi, or LTE. If the watch can't locate the phone, use the website instead.
Troubleshooting: if device is off or can't be found, only the last known location shows; if you still can't locate it, contact your carrier, which may be able to help locate or suspend the device. Stolen device: don't go to the location on the map yourself, contact the authorities.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I can't find my Samsung Galaxy phone anywhere. How can I find it?",
                 """You can look for it from a computer or another phone.

1. In a web browser, go to the **SmartThings Find** website or the **Samsung Find** website.
2. Sign in with your Samsung account.
3. Choose your phone from the list on the left.
4. Look at the map to see where it is.

Your phone needs to be turned on and connected to a network for this to work.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I was in the kitchen and then the garden and now my Samsung Galaxy phone has disappeared. I am fairly sure it is somewhere in the house but I can't hear it because it is on silent. My husband has a laptop. Can we make it ring?",
                 """Yes, a ring works even when the phone is on silent.

1. On the laptop, open a web browser and go to the **SmartThings Find** website or the **Samsung Find** website.
2. Sign in with your Samsung account.
3. Choose your phone from the list on the left.
4. Select **Ring**, then select **Start**.

It rings for one minute, even on Mute or Vibrate. To stop it, select **Stop** on the website, or swipe **Dismiss** on the phone.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "I lost my phone and I'm worried. Can you help me find it?",
                 "I'm sorry, let's find it. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I lost my phone and I'm worried. Can you help me find it?",
                 "I'm sorry, let's find it. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?",
                 "It is a Samsung Galaxy.",
                 """Thank you. You can look for it from a computer or another phone.

1. In a web browser, go to the **SmartThings Find** website or the **Samsung Find** website.
2. Sign in with your Samsung account.
3. Choose your phone from the list on the left.
4. Look at the map to see where it is.

Your phone needs to be turned on and connected to a network for this to work.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "My Samsung Galaxy phone is lost somewhere in the house. I don't have a computer or a second phone, but I am wearing my Galaxy watch. Can I use the watch to find the phone?",
                 """Yes, you can make the phone ring from the watch.

1. Press the **Home** button on the watch.
2. Swipe to and tap **Samsung Find**.
3. If asked, tap **Continue** and allow the permissions.
4. Select your phone.
5. Tap the **Ring** icon.
6. To stop the ringing, swipe **Dismiss** on the phone, or tap **Stop** on the watch.

The watch must be connected to the phone by Bluetooth, Wi-Fi, or LTE. The phone must be turned on and have a network connection. If the watch cannot find the phone, you would need to use the Samsung Find or SmartThings Find website instead.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Samsung Galaxy",
             "messages": [
                 "I left my Samsung Galaxy somewhere and can't remember where. How do I locate it?",
                 """You can look for it from a computer or another phone.

1. In a web browser, go to the **SmartThings Find** website or the **Samsung Find** website.
2. Sign in with your Samsung account.
3. Choose your phone from the list on the left.
4. Look at the map to see where it is.

Your phone needs to be turned on and connected to a network for this to work.""",
                 "I signed in and picked my phone, but the map only shows an old spot from yesterday. I think its battery died.",
                 """That fits. When the phone is off or cannot be reached, the map only shows its last known location.

1. Go to that last known spot and look there.
2. If you still cannot find it, contact your phone company. They may be able to help locate the phone or suspend it.

If you think it was stolen, do not go to the spot on the map yourself. Contact the authorities.""",
             ]},
        ],
    },
]
