# Review input: batch ny2b, round 2 (7 examples)

## tr141-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Set up and listen to voicemail (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-kz/guide/iphone/check-voicemail-iph3c99490e/14.0 ; https://support.apple.com/guide/iphone/turn-on-and-activate-siri-iph83aad8922/ios

**USER:**
I have an iPhone and my fingers shake so I really struggle to tap the little buttons in the Phone app. Is there any way to find out if I have new voicemail without tapping through all the screens? I can talk to the phone fine.

**ASSISTANT:**
Yes, you can ask Siri instead of tapping. Use your voice:

1. Say "Hey Siri" to wake Siri.
2. Then say something like "Do I have any new voicemail?"
3. Or say "Play the voicemail from" and then the name of the person, for example "Play the voicemail from Eliza."

Siri will answer or play the message for you. If Siri does not answer when you say "Hey Siri", that phrase may not be turned on yet. Someone can help you open **Settings**, tap **Siri**, and tap **Turn On Siri**. If you ever want to tap instead, open the **Phone** app, tap **Voicemail**, then tap a message and tap the **Play** button.

## tr142-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Forward calls to another number (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/guide/iphone/iph7405291c4/ios

**USER:**
I'm going on a cruise next week and I will not have my iPhone with me, it is staying at home with the charger. My son said I can send calls to his number so I don't miss anything from the doctor's office. My iPhone has two SIMs in it because I travel for work. Please tell me what to do.

**ASSISTANT:**
Yes, you can forward your calls to your son's number. Set it up before you leave.

1. Open **Settings**.
2. Tap **Apps**.
3. Tap **Phone**.
4. Tap **Call Forwarding**.
5. Turn on **Call Forwarding**.
6. Because your iPhone has Dual SIM, choose a line under **SIMs**.
7. Tap **Forward To**.
8. Type in your son's number.
9. Tap **Back**.

A Call Forwarding icon shows at the top of the screen while it is on. Your phone must be in range of the cellular network when you set it up, or calls will not forward. Call forwarding works on GSM networks. If you use a CDMA network, contact your carrier.

## tr143-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Make the light flash for alerts (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/111774

**USER:**
Is there a setting to make my iPhone's flash blink when something comes in? I keep missing things.

**ASSISTANT:**
Yes, there is.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Audio/Visual**.
4. Turn on **LED Flash for Alerts**.

The light next to the camera lens blinks when you get a notification while the phone is locked.

**USER:**
I turned it on but I was holding the phone and reading it, and the light never blinked when a message came.

**ASSISTANT:**
That is expected. **LED Flash for Alerts** only works when your phone is locked.

1. Put the phone down and let the screen go dark so it is locked.
2. Wait for the next notification. The light next to the camera lens should blink.

If you are still not seeing it, go back to **Settings**, **Accessibility**, **Audio/Visual** and check that **LED Flash for Alerts** is on.

## tr144-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Find the model number of the iPhone to identify which model it is (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/106343

**USER:**
How can I find out which model my iPhone is? I'm trying to sell it.

**ASSISTANT:**
You can find the model number in Settings.

1. Open **Settings**.
2. Tap **General**.
3. Tap **About**.
4. Find **Model Number**. The part number is shown to its right.
5. Tap that part number and it changes to the model number.

Use that number when you sell the phone.

## tr144-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Find the model number of the iPhone to identify which model it is (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/106343

**USER:**
I found my old iPhone 7 in a drawer, the one my late husband used. The battery is dead and I don't have the right charger so I can't turn it on. A repair shop asked me for the model number. Is there a way to see it without turning it on?

**ASSISTANT:**
Yes. On an iPhone 7 or earlier, the model number is on the back of the phone.

1. Turn the phone over so the back faces you.
2. Look at the writing on the back and find the model number.

## tr144-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Find the model number of the iPhone to identify which model it is (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/106343

**USER:**
What model is my phone? The store wants to know.

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iphone

**ASSISTANT:**
Thank you. Here is how to find the model number on an iPhone.

1. Open **Settings**.
2. Tap **General**.
3. Tap **About**.
4. Find **Model Number**. A part number is shown to its right.
5. Tap that part number and it changes to the model number.

You can tell the store that number.

## tr144-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Find the model number of the iPhone to identify which model it is (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/106343

**USER:**
I forgot the passcode on my iPhone 8 so I can't open Settings, and I do not want to try guessing it. It has a SIM tray on the side. Can I still find the model number some other way?

**ASSISTANT:**
Yes. On an iPhone 8 or later with a SIM tray, you can look inside the SIM tray slot.

1. Remove the SIM tray from the side of the phone.
2. Hold the tray slot under bright overhead light and look inside the slot.
3. Look on the upper side of the slot, the side with the display. The model number is there.
