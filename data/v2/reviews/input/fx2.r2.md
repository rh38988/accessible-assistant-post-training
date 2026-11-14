# Review input: batch fx2, round 2 (9 examples)

## tr016-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Is it safe to pay online? (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay

**USER:**
I don't have a credit card, only a debit card and some cash. A person selling concert tickets online says they only take a payment app like Zelle, and that tickets are going fast. Is that okay? I really can't use a credit card.

**ASSISTANT:**
**Please don't pay this seller with Zelle.** A seller who says you can only pay with a payment app is probably a scammer. Tickets going fast is the kind of pressure scammers use.

1. Don't send money to anyone who says you can only pay one specific way, whatever reason they give.
2. Search online for the seller's name with words like "review," "scam," or "complaint."
3. The FTC suggests a credit card when possible because it lets you dispute charges. Since you can't use one, the safe choice is to skip a seller who insists on a payment app.

You can report the seller at **ReportFraud.ftc.gov**. For more tips, you can visit **ftc.gov/scams**.

## tr024-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Turn up ringer volume (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105103

**USER:**
Every time I press the volume up button on my iPhone it only makes my YouTube videos louder, not the phone ringing. I'm usually watching videos when my daughter calls. I want the ringer louder, not the videos. How do I do that?

**ASSISTANT:**
That happens because the volume buttons change **media volume** while you are watching videos, listening to music, or playing games. They change the ringer volume only when you aren't using other apps.

1. Close the video app and go to your Home Screen, so no other app is in use.
2. Press the **volume up** button a few times.

Now the buttons raise the ringer volume. If your phone still only vibrates when someone calls, it may be in Silent mode. Tell me and I'll show you how to check.

## tr024-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Turn up ringer volume (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105103

**USER:**
Can you tell me how to make my iPhone ringer louder?

**ASSISTANT:**
Yes, you can use the volume buttons. It takes a few seconds.

1. Go to your Home Screen so you are not inside another app.
2. Press the **volume up** button on the side of the phone a few times.

When no other app is in use, these buttons change the ringer volume. If your phone only vibrates, it may be in Silent mode. Tell me and I'll show you how to check.

**USER:**
I did that but it still only buzzes when someone calls. I see something orange on the side of the phone.

**ASSISTANT:**
The orange means your iPhone is in **Silent mode**. In Silent mode it vibrates for calls instead of ringing.

1. Find the **Ring/Silent switch**, where you see the orange.
2. Flip it so the orange is no longer showing.
3. Press the **volume up** button a few times.

If you have an iPhone 15 Pro or a newer model, there is no switch. The **Action button** toggles Silent mode by default. Calls from your favorite contacts still ring in Silent mode.

## tr025-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Turn up ring volume (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9082609?hl=en

**USER:**
My Android phone is quite old and I can't update it. When I press the volume button I only see a little slider with a small arrow, no menu thing. How do I make the ring louder on an older phone like that?

**ASSISTANT:**
On older Android phones you use the small arrow.

1. Press a **volume button** on the side of the phone.
2. At the right, tap the **Down arrow**.
3. Find **Ring** in the list.
4. Slide the **Ring** level to where you want it.

The Down arrow is where older versions show Media, Ring, and Alarm.

## tr025-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Turn up ring volume (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9082609?hl=en

**USER:**
Please show me how to make my Android phone ring louder.

**ASSISTANT:**
You can do this with the volume buttons. It takes a few seconds.

1. Press a **volume button** on the side of the phone.
2. Tap the **Menu** icon on the right side of the volume panel.
3. Find the **Ring Volume** slider and slide it to the right.

If you don't see the **Menu** icon, tell me what you see and I'll help you find it.

**USER:**
I pressed the button but there is no menu icon. I only see a small arrow pointing down.

**ASSISTANT:**
That's normal on older Android versions. Use the arrow instead.

1. Press a **volume button** again.
2. At the right, tap the **Down arrow**.
3. Choose **Ring**.
4. Slide the **Ring** level to where you want it.

## tr026-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Turn on Wi-Fi Calling (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108066

**USER:**
I want my iPhone to use my home Wi-Fi for phone calls because the signal here is poor. How do I set that up?

**ASSISTANT:**
You can turn on **Wi-Fi Calling**. It takes about a minute.

1. Open the **Settings** app.
2. Tap **Cellular**.
3. Tap **Wi-Fi Calling**.
4. Turn on **Wi-Fi Calling on This iPhone**.
5. Tap **Enable**.

You may be asked to enter or confirm an address for emergency services. Your carrier must offer Wi-Fi Calling.

**USER:**
I tried but I can't get it to turn on.

**ASSISTANT:**
Let's try these in order.

1. Check that your carrier offers Wi-Fi Calling and that your iPhone software is up to date.
2. Open **Settings**, tap **Cellular**, tap **Wi-Fi Calling**, and make sure **Wi-Fi Calling on This iPhone** is on.
3. Restart your iPhone.
4. Connect to a different Wi-Fi network, because some networks don't work with Wi-Fi Calling.
5. Turn Wi-Fi Calling off, then on again.

Wait about two minutes between steps. If it still won't turn on, contact your carrier.

## tr028-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Take a screenshot (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots ; https://support.microsoft.com/en-us/windows/experience/keyboard-shortcut-for-print-screen

**USER:**
How can I take a picture of my whole screen on my Windows 11 computer?

**ASSISTANT:**
You can use **Snipping Tool**.

1. Select **Start**, type **snipping tool**, then select **Snipping Tool**.
2. Select **Snipping Mode**, then choose **Full screen**.
3. Select **New**.

It captures the whole screen right away.

**USER:**
OK it took the picture but I can't tell where it went. How do I find it?

**ASSISTANT:**
Snips are saved automatically in your **Screenshots** folder.

1. Open **File Explorer** from the taskbar.
2. On the left side, select the **Pictures** folder, then select **Screenshots**.
3. If you want another copy somewhere else, select **Save as** in Snipping Tool, choose a location and a name, then select **Save**.

To change where snips are saved, select **See More** in Snipping Tool, then **Settings**.

## tr030-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Connect to a Wi-Fi network (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9075847?hl=en

**USER:**
My son set up our Wi-Fi at the new apartment and hid the network, so it doesn't show up in the list on my Android phone. He told me the name and password. How do I connect to a network that isn't listed?

**ASSISTANT:**
You can add it yourself.

1. Open the **Settings** app.
2. Tap **Network & internet**, then **Internet**.
3. At the bottom of the list, tap **Add network**.
4. Type the network name your son gave you.
5. Enter the security details your son gave you, including the password.
6. Tap **Advanced options**, and under **Hidden Network** select **Yes**.
7. Tap **Save**.

Once connected, the network is labeled **Saved**, and your phone joins it automatically when you're nearby.

## tr030-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Connect to a Wi-Fi network (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9075847?hl=en

**USER:**
I'm at my sister's house with an Android phone. How do I get on her Wi-Fi?

**ASSISTANT:**
Here is how.

1. Open the **Settings** app.
2. Tap **Network & internet**, then **Internet**.
3. Tap your sister's network in the list. A lock icon means it needs a password.
4. Enter the password if asked.

When you're connected, the network shows as **Saved**.

**USER:**
I don't see her network in the list at all.

**ASSISTANT:**
Her network may be hidden. Ask her for the network name and the password.

1. Open the **Settings** app, tap **Network & internet**, then tap **Internet**.
2. Scroll to the bottom of the list and tap **Add network**.
3. Type the network name, then enter the security details (the password).
4. Tap **Advanced options**, and under **Hidden Network** select **Yes**.
5. Tap **Save**.
