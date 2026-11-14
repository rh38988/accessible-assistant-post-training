# Review input: batch ny4a, round 1 (42 examples)

## tr160-a
- scenario: direct | style: plain | specification: fully_specified | platform: Samsung Galaxy
- task: Take a screenshot (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002500/

**USER:**
How do I take a screenshot on my Samsung Galaxy phone?

**ASSISTANT:**
You can capture your screen with two buttons. Here is how.

1. Go to the screen you want to capture.
2. Press and hold the **Power** (side) button and the **Volume Down** button at the same time.
3. Let go after a moment.

The screen flashes to show the picture was taken.

If nothing happens, check where the buttons are on your model, since their position can differ.

## tr160-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Samsung Galaxy
- task: Take a screenshot (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002500/

**USER:**
My daughter sent me a long recipe on a website and I want to keep the whole thing as one picture, not a bunch of little pieces. I have a Samsung Galaxy phone. The recipe goes way past the bottom of the screen. Is there a way to get all of it?

**ASSISTANT:**
Yes, there is a way to capture a long page as one picture.

1. Open the recipe on your screen.
2. Press and hold the **Power** (side) button and the **Volume Down** button together, then let go. The screen flashes.
3. Tap the **Scroll capture** icon. It looks like two arrows pointing down.

Long content is then captured as one image.

## tr160-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Take a screenshot (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002500/

**USER:**
I need to save what is on my screen as a picture. How do I do that?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

## tr160-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Take a screenshot (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002500/

**USER:**
I need to save what is on my screen as a picture. How do I do that?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

**USER:**
It's a Samsung Galaxy.

**ASSISTANT:**
Thank you. On a Samsung Galaxy it takes two buttons.

1. Go to the screen you want to capture.
2. Press and hold the **Power** (side) button and the **Volume Down** button at the same time.
3. Let go after a moment.

The screen flashes to show the picture was taken.

## tr160-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Take a screenshot (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002500/

**USER:**
I have a Samsung Galaxy and my hands have arthritis, so pressing two buttons at once is really hard for me. Is there another way to take a screenshot that does not use the buttons?

**ASSISTANT:**
Yes. You can turn on a swipe that captures the screen with the side of your hand.

1. Swipe down from the top right corner with two fingers to open the **Quick panel**.
2. Tap **Settings**, the gear icon.
3. Swipe to **Advanced features** and tap it.
4. Tap **Palm swipe to capture** and turn its switch on.

After that, swipe the edge of your hand across the screen to take a screenshot.

You can also say "Hey Google, take a screenshot" or "Hey Bixby, take a screenshot".

## tr160-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Samsung Galaxy
- task: Take a screenshot (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002500/

**USER:**
Samsung Galaxy here. How can I take a picture of what is on my screen?

**ASSISTANT:**
You can do that with two buttons.

1. Go to the screen you want to capture.
2. Press and hold the **Power** (side) button and the **Volume Down** button at the same time.
3. Let go after a moment.

The screen flashes to show the picture was taken.

**USER:**
The screen flashed, but now I can't find the picture anywhere.

**ASSISTANT:**
Good, that means it worked. You can find it in either of these places.

1. Open **Gallery**, tap the **Albums** tab, then tap the **Screenshots** folder.
2. Or open **My Files** and tap **Images**.

## tr161-a
- scenario: direct | style: plain | specification: fully_specified | platform: Samsung Galaxy
- task: Update the phone's software (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002027/

**USER:**
How do I update the software on my Samsung Galaxy phone?

**ASSISTANT:**
You can do it right on the phone. Here is how.

1. Swipe down with two fingers from the top right corner of the screen.
2. Tap the **Settings** icon.
3. Swipe to **Software update** and tap it. On some phones it is called **System updates**.
4. Tap **Download and install**. On some phones you may need to tap **Download now**.
5. When the download finishes, follow the instructions on the screen to install it.

If the name is different on your phone, look for **System updates** instead.

## tr161-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Samsung Galaxy
- task: Update the phone's software (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002027/

**USER:**
My grandson keeps telling me my Samsung Galaxy is out of date and that I need to get the latest software. I have a laptop here that I use for email, and I would rather do it with the laptop and the cable that came in the box if that works. What should I do?

**ASSISTANT:**
Yes, you can update with a computer by using a program called Smart Switch.

1. Plug your Galaxy into the computer with the USB cable from the box. Some computers need a USB adapter.
2. Open **Smart Switch** on the computer and let it find your phone.
3. If an update is available, click **Update** and follow the prompts.

Keep the cable plugged in and do not use the phone until it finishes. The phone will restart by itself.

## tr161-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Update the phone's software (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002027/

**USER:**
My phone keeps saying it needs an update. How do I do it?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

## tr161-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Update the phone's software (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002027/

**USER:**
My phone keeps saying it needs an update. How do I do it?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

**USER:**
Samsung Galaxy

**ASSISTANT:**
Thanks. You can update it right on the phone.

1. Swipe down with two fingers from the top right corner of the screen.
2. Tap the **Settings** icon.
3. Swipe to **Software update** and tap it. On some phones it is called **System updates**.
4. Tap **Download and install**. On some phones you may need to tap **Download now**.
5. When the download finishes, follow the instructions on the screen to install it.

## tr161-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Update the phone's software (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002027/

**USER:**
I have a Samsung Galaxy and I don't own a computer, so I can't plug it into anything. Before I update, I would also like to know what the update changes. Can I see that on the phone?

**ASSISTANT:**
Yes, you can see that on the phone, and you do not need a computer.

To see what the update includes:
1. Swipe down with two fingers from the top right corner, then tap the **Settings** icon.
2. Swipe to **Software update** (or **System updates**) and tap it.
3. Tap **Last update**, then tap **All changes**.

To update on the phone:
1. Go back to **Software update** (or **System updates**).
2. Tap **Download and install**. On some phones you may need to tap **Download now**.
3. When it finishes downloading, follow the instructions on the screen.

Note that you cannot use the phone while it installs, and that includes emergency calls.

## tr161-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Samsung Galaxy
- task: Update the phone's software (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002027/

**USER:**
Please walk me through updating my Samsung Galaxy phone's software.

**ASSISTANT:**
Here is how to update it on the phone.

1. Swipe down with two fingers from the top right corner of the screen.
2. Tap the **Settings** icon.
3. Swipe to **Software update** and tap it. On some phones it is called **System updates**.
4. Tap **Download and install**. On some phones you may need to tap **Download now**.
5. When the download finishes, follow the instructions on the screen to install it.

**USER:**
I looked all through Settings and there is no Software update. Where did it go?

**ASSISTANT:**
On some phones it has a different name. Try this.

1. In **Settings**, swipe down the list and look for **System updates**.
2. Tap it, then tap **Download and install**, **Check for system updates**, or **Check for software updates**. Which one you see depends on your phone company.
3. If an update is found and you see **Download now**, tap it.

## tr162-a
- scenario: direct | style: plain | specification: fully_specified | platform: Samsung Galaxy
- task: Connect to a Wi-Fi network (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/ca/support/mobile-devices/connect-your-samsung-galaxy-to-the-internet/

**USER:**
How do I connect my Samsung Galaxy phone to my home Wi-Fi?

**ASSISTANT:**
Here is how to join a Wi-Fi network.

1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. If Wi-Fi is off, tap the switch to turn it on. The networks nearby will appear in a list.
4. Tap the name of your network.
5. Type the password, then tap **Connect**.

When it works, your network name shows under **Current network** with the word **Connected** under it.

## tr162-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Samsung Galaxy
- task: Connect to a Wi-Fi network (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/ca/support/mobile-devices/connect-your-samsung-galaxy-to-the-internet/

**USER:**
I am visiting my sister for the week and she gave me her Wi-Fi name and password on a piece of paper. I have a Samsung Galaxy and I think the Wi-Fi on my phone is switched off because I turned it off on the plane. I don't want to mess anything up. What do I tap?

**ASSISTANT:**
You will not mess anything up. Follow these steps.

1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. Tap the switch to turn Wi-Fi on. The networks nearby will appear in a list.
4. Tap the name your sister wrote down.
5. Type the password from the paper, then tap **Connect**.

When it works, her network name shows under **Current network** with **Connected** under it.

## tr162-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Connect to a Wi-Fi network (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/ca/support/mobile-devices/connect-your-samsung-galaxy-to-the-internet/

**USER:**
My phone says I have no internet at home. How do I get it onto my Wi-Fi?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

## tr162-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Connect to a Wi-Fi network (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/ca/support/mobile-devices/connect-your-samsung-galaxy-to-the-internet/

**USER:**
My phone says I have no internet at home. How do I get it onto my Wi-Fi?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

**USER:**
its a samsung galaxy

**ASSISTANT:**
Thanks. Here is how to join your Wi-Fi.

1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. If Wi-Fi is off, tap the switch to turn it on.
4. Tap the name of your home network in the list.
5. Type the password, then tap **Connect**.

When it works, the network name shows under **Current network** with **Connected** under it.

## tr162-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Connect to a Wi-Fi network (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/ca/support/mobile-devices/connect-your-samsung-galaxy-to-the-internet/

**USER:**
I just got a new internet router and my Samsung Galaxy needs to join it. The problem is I never wrote down the password and I have no idea what it is. Where would I find it, and what do I tap on the phone?

**ASSISTANT:**
The password is often printed on a sticker on the router, so look there first.

Then on your phone:
1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. If Wi-Fi is off, tap the switch to turn it on.
4. Tap the name of your router's network.
5. Type the password from the sticker, then tap **Connect**.

When it works, the network name shows under **Current network** with **Connected** under it.

## tr162-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Samsung Galaxy
- task: Connect to a Wi-Fi network (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/ca/support/mobile-devices/connect-your-samsung-galaxy-to-the-internet/

**USER:**
Samsung Galaxy phone. Please tell me how to connect to Wi-Fi.

**ASSISTANT:**
Here is how to join a Wi-Fi network.

1. Open **Settings** and tap **Connections**.
2. Tap **Wi-Fi**.
3. If Wi-Fi is off, tap the switch to turn it on.
4. Tap the name of your network in the list.
5. Type the password, then tap **Connect**.

When it works, the network name shows under **Current network** with **Connected** under it.

**USER:**
I did all that but it will not connect. I think I might have typed the password wrong.

**ASSISTANT:**
A mistyped password is the most common reason. Try this.

1. Tap the network name again.
2. In the password box, tap the eye icon to see what you typed.
3. Fix any mistakes, then tap **Connect**.

If it still fails, go to **Settings**, **Connections**, then turn Wi-Fi off, wait a few seconds, and turn it back on.

## tr163-a
- scenario: direct | style: plain | specification: fully_specified | platform: Samsung Galaxy
- task: Block a phone number (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002869/

**USER:**
Someone keeps calling me from a number I don't know. How do I block it on my Samsung Galaxy phone?

**ASSISTANT:**
You can block it from your list of recent calls.

1. Open the **Phone** app and tap the **Recents** tab.
2. Tap the number that keeps calling.
3. Tap **Menu**. It looks like three lines with three dots.
4. Tap **Block**.
5. Tap **Block** again to confirm.

## tr163-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Samsung Galaxy
- task: Block a phone number (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002869/

**USER:**
I have a Samsung Galaxy. A salesman is saved in my contacts from a while back, and now he calls me every single day about insurance. I don't want to delete him because I might forget, but I never want to hear from him again. Can I just block him from the contacts?

**ASSISTANT:**
Yes. A blocked contact stays in your list but cannot reach you.

1. Open the **Contacts** app.
2. Tap his name.
3. Tap **More**.
4. Tap **Block contact**.
5. Tap **Block** to confirm.

## tr163-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Block a phone number (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002869/

**USER:**
There is a number I want to stop hearing from. How do I block it?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

## tr163-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Block a phone number (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002869/

**USER:**
There is a number I want to stop hearing from. How do I block it?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

**USER:**
Samsung Galaxy

**ASSISTANT:**
Thanks. If the number called you recently, you can block it from your recent calls.

1. Open the **Phone** app and tap the **Recents** tab.
2. Tap the number.
3. Tap **Menu**. It looks like three lines with three dots.
4. Tap **Block**.
5. Tap **Block** again to confirm.

## tr163-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Block a phone number (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002869/

**USER:**
My Samsung Galaxy gets text messages from a number that keeps sending me ads. It never calls, it only texts, so it is not in my call list. How do I block it from the text messages?

**ASSISTANT:**
You can block it right from the conversation.

1. Open the **Samsung Messages** app.
2. Touch and hold the conversation from that number.
3. Tap **More**.
4. Tap **Block**.
5. Tap **Block** again to confirm.

## tr163-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Samsung Galaxy
- task: Block a phone number (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002869/

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

## tr164-a
- scenario: direct | style: plain | specification: fully_specified | platform: Samsung Galaxy
- task: Turn the flashlight on and off (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10003351/

**USER:**
How do I turn on the flashlight on my Samsung Galaxy phone?

**ASSISTANT:**
It is quick to do from the top of the screen.

1. Swipe down from the top right of the screen to open the **Quick settings** panel.
2. Tap the **Flashlight** icon. The light comes on.
3. To turn it off, tap the **Flashlight** icon again.

The icon looks highlighted while the light is on.

## tr164-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Samsung Galaxy
- task: Turn the flashlight on and off (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10003351/

**USER:**
I use the flashlight on my Samsung Galaxy to walk to the mailbox at night, but it is so bright that it blinds me and I can't see the path. Is there a way to make the light dimmer? I only know how to turn it on and off.

**ASSISTANT:**
Yes, you can set how bright it is.

1. Swipe down from the top right of the screen to open the **Quick settings** panel.
2. Press and hold the **Flashlight** icon.
3. Tap the switch to turn the light on.
4. Drag the slider to make the light brighter or dimmer.

If the slider looks grayed out, turn the light on with the switch first.

## tr164-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn the flashlight on and off (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10003351/

**USER:**
I need some light to look under the bed. How can I make the phone light up?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

## tr164-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Turn the flashlight on and off (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10003351/

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

## tr164-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Turn the flashlight on and off (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10003351/

**USER:**
The power went out and it is pitch dark in my house. I have a Samsung Galaxy and I can barely see the screen, so I don't want to go hunting through apps or settings. What is the fastest way to get the light on, and then off again later?

**ASSISTANT:**
The fastest way is one swipe and one tap.

1. Swipe down from the top right of the screen to open the **Quick settings** panel.
2. Tap the **Flashlight** icon. The light comes on.

Later, to turn it off, open the same panel and tap the **Flashlight** icon again.

## tr164-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Samsung Galaxy
- task: Turn the flashlight on and off (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10003351/

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

## tr165-a
- scenario: direct | style: plain | specification: fully_specified | platform: Samsung Galaxy
- task: Turn on Easy mode for bigger icons and a simpler screen (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/ae/support/mobile-devices/using-easy-mode-on-my-samsung-phone

**USER:**
How do I make the icons and writing bigger on my Samsung Galaxy phone? I heard there is an Easy mode.

**ASSISTANT:**
Yes, Easy Mode makes the icons and text larger. Here is how to turn it on.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Easy Mode**.
4. Turn on the switch.

Your screen will change to larger icons and text.

## tr165-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Samsung Galaxy
- task: Turn on Easy mode for bigger icons and a simpler screen (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/ae/support/mobile-devices/using-easy-mode-on-my-samsung-phone

**USER:**
My eyesight is not what it used to be and I keep tapping the wrong things on my Samsung Galaxy phone because everything is so small and crowded. My son said there is some kind of simple setting that spreads everything out and makes it bigger. Where do I find it?

**ASSISTANT:**
Your son means Easy Mode. It makes icons and text larger and spaces things out.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Easy Mode**.
4. Turn on the switch.

If the change does not show up, restart the phone and try again.

## tr165-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on Easy mode for bigger icons and a simpler screen (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/ae/support/mobile-devices/using-easy-mode-on-my-samsung-phone

**USER:**
Everything on my phone is too small. Is there a simple mode with bigger icons?

**ASSISTANT:**
I can help with that. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

## tr165-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Turn on Easy mode for bigger icons and a simpler screen (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/ae/support/mobile-devices/using-easy-mode-on-my-samsung-phone

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

## tr165-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Turn on Easy mode for bigger icons and a simpler screen (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/ae/support/mobile-devices/using-easy-mode-on-my-samsung-phone

**USER:**
I turned on Easy Mode on my Samsung Galaxy last week, but now I want my old screen back. I do not want to reset the whole phone or lose anything. Can I just switch Easy Mode off?

**ASSISTANT:**
Yes. You only need to turn that one setting off.

1. Open the **Settings** app.
2. Tap **Display**.
3. Tap **Easy Mode**.
4. Turn the switch off.

## tr165-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Samsung Galaxy
- task: Turn on Easy mode for bigger icons and a simpler screen (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/ae/support/mobile-devices/using-easy-mode-on-my-samsung-phone

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

## tr166-a
- scenario: direct | style: plain | specification: fully_specified | platform: Samsung Galaxy
- task: Find a lost phone (Samsung Galaxy) | sensitive: True | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS00080182

**USER:**
I can't find my Samsung Galaxy phone anywhere. How can I find it?

**ASSISTANT:**
You can look for it from a computer or another phone.

1. In a web browser, go to the **SmartThings Find** website or the **Samsung Find** website.
2. Sign in with your Samsung account.
3. Choose your phone from the list on the left.
4. Look at the map to see where it is.

Your phone needs to be turned on and connected to a network for this to work.

## tr166-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Samsung Galaxy
- task: Find a lost phone (Samsung Galaxy) | sensitive: True | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS00080182

**USER:**
I was in the kitchen and then the garden and now my Samsung Galaxy phone has disappeared. I am fairly sure it is somewhere in the house but I can't hear it because it is on silent. My husband has a laptop. Can we make it ring?

**ASSISTANT:**
Yes, a ring works even when the phone is on silent.

1. On the laptop, open a web browser and go to the **SmartThings Find** website or the **Samsung Find** website.
2. Sign in with your Samsung account.
3. Choose your phone from the list on the left.
4. Select **Ring**, then select **Start**.

It rings for one minute, even on Mute or Vibrate. To stop it, select **Stop** on the website, or swipe **Dismiss** on the phone.

## tr166-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Find a lost phone (Samsung Galaxy) | sensitive: True | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS00080182

**USER:**
I lost my phone and I'm worried. Can you help me find it?

**ASSISTANT:**
I'm sorry, let's find it. Is your phone a **Samsung Galaxy**, an **iPhone**, or another kind of phone?

## tr166-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Find a lost phone (Samsung Galaxy) | sensitive: True | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS00080182

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

## tr166-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Find a lost phone (Samsung Galaxy) | sensitive: True | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS00080182

**USER:**
My Samsung Galaxy phone is lost somewhere in the house. I don't have a computer or a second phone, but I am wearing my Galaxy watch. Can I use the watch to find the phone?

**ASSISTANT:**
Yes, you can make the phone ring from the watch.

1. Press the **Home** button on the watch.
2. Open **Samsung Find**.
3. Select your phone.
4. Tap the **Ring** icon.

The watch must be connected to the phone by Bluetooth, Wi-Fi, or LTE. If the watch cannot find the phone, you would need to use the Samsung Find or SmartThings Find website instead.

## tr166-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Samsung Galaxy
- task: Find a lost phone (Samsung Galaxy) | sensitive: True | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS00080182

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
