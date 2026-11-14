# Review input: batch ny3b, round 2 (3 examples)

## tr154-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Pair a Bluetooth accessory (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9417604

**USER:**
I want to connect a Bluetooth keyboard to my Android phone so typing is easier on my eyes. I don't want to go hunting through lots of menus, my eyes get tired. Is there a quick way to start from the top of the screen?

**ASSISTANT:**
Yes, you can start right from the top of the screen:

1. Drag down from the top of the screen.
2. Touch and hold the **Bluetooth** icon.
3. Tap **Pair new device**.
4. Tap the name of your keyboard.
5. Follow the on-screen prompts.

When it works, the keyboard shows as **Connected**.

Bluetooth is off while Airplane mode is on, so turn Airplane mode off before you pair.

## tr158-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Turn on theft protection (Android) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/android/answer/15146908

**USER:**
I don't want to count on my phone guessing that it was grabbed. I want to be able to lock it myself from my laptop if it goes missing. My Android phone has a screen lock, a working SIM, and Find Hub is on. What do I set up?

**ASSISTANT:**
You want **Remote Lock**. Here is how to turn it on:

1. Open the **Settings** app.
2. Tap **Google**.
3. Tap **All services**.
4. Under **Personal & device safety**, tap **Theft protection**.
5. Tap **Remote Lock**.
6. Turn on **Remote lock**.

If it says your number isn't verified, tap **Verify number**, then turn on **Automatically verify phone numbers**.

To lock the phone later, use your laptop:

1. Go to android.com/lock.
2. Enter your phone number.
3. Complete the security check (reCaptcha) that appears.
4. Request the lock.

The phone screen locks shortly after.

## tr159-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Make calls over Wi-Fi (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/phoneapp/answer/2811843

**USER:**
I'm staying at my daughter's house for a while and I don't have a mobile service plan on my Android phone right now, just her Wi-Fi. Is there any way to still make phone calls with it?

**ASSISTANT:**
It may work. Some carriers let you use Wi-Fi calling without a mobile service plan. Here is how to check:

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **SIMs**.
4. Tap **Carrier SIM**.
5. Tap **Wi-Fi calling**.
6. Turn on **Wi-Fi calling**.

Then make calls as you normally would while you are connected to her Wi-Fi.

If you don't see **Wi-Fi calling**, your carrier doesn't support it. Whether this works without a plan depends on your carrier, so ask your carrier to confirm.
