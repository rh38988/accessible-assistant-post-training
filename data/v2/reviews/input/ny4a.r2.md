# Review input: batch ny4a, round 2 (4 examples)

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

## tr161-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Samsung Galaxy
- task: Update the phone's software (Samsung Galaxy) | sensitive: False | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS10002027/

**USER:**
My grandson keeps telling me my Samsung Galaxy is out of date and that I need to get the latest software. I have a laptop here that I use for email, and I would rather do it with the laptop and the cable that came in the box if that works. What should I do?

**ASSISTANT:**
Yes, you can update with a computer by using a program called Smart Switch.

1. Make sure the Smart Switch program is installed on your computer. If it is not, you can get it from Samsung's Smart Switch page: https://www.samsung.com/us/support/owners/app/smart-switch
2. Plug your Galaxy into the computer with the USB cable from the box. Some computers need a USB adapter.
3. Open **Smart Switch** on the computer and let it find your phone.
4. If an update is available, click **Update** and follow the prompts.

Keep the cable plugged in and do not use the phone until it finishes. The phone will restart by itself.

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

## tr166-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Samsung Galaxy
- task: Find a lost phone (Samsung Galaxy) | sensitive: True | reviewed by a person: False
- sources: https://www.samsung.com/us/support/answer/ANS00080182

**USER:**
My Samsung Galaxy phone is lost somewhere in the house. I don't have a computer or a second phone, but I am wearing my Galaxy watch. Can I use the watch to find the phone?

**ASSISTANT:**
Yes, you can make the phone ring from the watch.

1. Press the **Home** button on the watch.
2. Swipe to and tap **Samsung Find**.
3. If asked, tap **Continue** and allow the permissions.
4. Select your phone.
5. Tap the **Ring** icon.
6. To stop the ringing, swipe **Dismiss** on the phone, or tap **Stop** on the watch.

The watch must be connected to the phone by Bluetooth, Wi-Fi, or LTE. If the watch cannot find the phone, you would need to use the Samsung Find or SmartThings Find website instead.
