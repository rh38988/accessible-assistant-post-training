# Review input: batch ex2, round 3 (11 examples)

## pilot-014
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Caller claims to be grandchild needing gift cards (any) | sensitive: True | reviewed by a person: False
- sources: https://www.ftc.gov/node/54353 ; https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay

**USER:**
My grandson just called crying. He said he got arrested and needs me to buy $2,000 in gift cards and read him the numbers. He said not to tell his mom. What should I do?

**ASSISTANT:**
I'm sorry, that must have been frightening. Please **don't buy the gift cards yet**. This has several signs of a common scam where someone pretends to be a grandchild in trouble:

- They need money **right away**
- They want **gift cards**, a way of paying that scammers like because it is hard to get your money back
- They ask you to **keep it a secret**

Here's what to do:

1. Don't buy anything right away. Resist the urge to act immediately, no matter how dramatic the story may be.
2. Call your grandson using the phone number **you already have for him**, not a number the caller gave you.
3. Call his mom or another family member too, even though the caller said not to.

If it really was him, your family can help sort it out. If it was a scammer, you can report it at **www.ftc.gov/complaint**.

If you already bought cards or read any numbers to them, tell me right away and I'll help you with the next steps.

## pilot-015
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Stranger asks for a verification code (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/node/84809

**USER:**
Someone texted me saying they sent me a code by mistake and asked me to send it back. It's a 6-digit number from my bank. Should I just send it to them?

**ASSISTANT:**
**No, please don't send it.** That code is only meant for you to log in to your account. Anyone who asks you for it is trying to get into your account, even if their message sounds friendly.

Here's what to do:

1. Don't reply to the text.
2. Block their number and stop texting them.
3. If you're worried about your account, call your bank using a phone number from your bank statement or your bank's app. Don't use any number from the text.
4. You can report the text at **ReportFraud.ftc.gov**.

If you already sent the code, contact your bank using a phone number from your bank statement or your bank's app.

## pilot-016
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Is it safe to pay online? (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/consumer-alerts/2026/07/way-spot-scams-how-someone-asks-you-pay ; https://consumer.ftc.gov/articles/online-shopping

**USER:**
is it safe to pay for something online?

**ASSISTANT:**
Yes, it can be safe if you pay the right way. Paying by **credit card** is best, because it protects you and your money if it turns out to be a scam or if something else goes wrong.

1. Pay by credit card when you can. If a charge is wrong, you can dispute it. Call your card company right away, and send a letter so it reaches them within 60 days of the date the first bill showing the error was mailed.
2. Don't buy from a seller who insists you can only pay with **gift cards, wire transfers, payment apps, or cryptocurrency**. Scammers like those ways of paying because it is hard to get your money back.
3. Look for **https** at the start of the website address. The "s" only means the connection is encrypted. Scammers can use it too, so it doesn't prove the seller is honest.

## pilot-017
- scenario: missing_info | style: plain | specification: underspecified | platform: unknown
- task: Stop strangers seeing Facebook posts (Facebook) | sensitive: True | reviewed by a person: False
- sources: https://www.facebook.com/help/120939471321735

**USER:**
how do I stop strangers from seeing my facebook posts

**ASSISTANT:**
That's a smart thing to set up. The buttons are in different places depending on how you use Facebook.

**Do you use Facebook on a phone (the Facebook app) or on a computer?**

## tr024-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Turn up ringer volume (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105103

**USER:**
How do I make my iPhone ring louder when someone calls?

**ASSISTANT:**
Here is a quick way to do it. It takes less than a minute.

1. Go to your Home Screen so you're not inside an app.
2. Press the **volume up** button a few times. When you are not using other apps, the buttons change the ringer volume.

If your phone still only vibrates, it may be in Silent mode. Tell me and I'll show you how to check.

## tr024-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Turn up ringer volume (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105103

**USER:**
I keep missing calls from my son because I don't hear my iPhone ring when I'm in the kitchen cooking. He gets worried. Can I make the ringing louder?

**ASSISTANT:**
Yes, you can, and that should help your son reach you.

Here is a quick way to do it. It takes less than a minute.

1. Go to your Home Screen so you're not inside an app.
2. Press the **volume up** button a few times. When you are not using other apps, the buttons change the ringer volume.

If your phone still only vibrates, it may be in Silent mode. Tell me and I'll show you how to check.

## tr024-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Turn up ringer volume (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/105103

**USER:**
My phone is too quiet when it rings.

**ASSISTANT:**
Let's fix that so you don't miss calls. Is your phone an **iPhone**, or another kind of phone like a Samsung or Google Pixel?

**USER:**
iPhone 13

**ASSISTANT:**
Thanks. Here's how on your iPhone. It takes less than a minute.

1. Go to your Home Screen so you're not inside an app.
2. Press the **volume up** button a few times. When you are not using other apps, the buttons change the ringer volume.

If your phone still only vibrates, it may be in Silent mode. Tell me and I'll show you how to check.

## tr025-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Turn up ring volume (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9082609?hl=en

**USER:**
how do I make the ringing louder

**ASSISTANT:**
Happy to help. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?

**USER:**
android, it's a samsung

**ASSISTANT:**
Thanks. Phone screens can look a little different, so here is what to look for.

You can do this with the volume buttons. It takes a few seconds.

1. Press a **volume button**.
2. At the right, tap the **Menu** icon, also called **More**.
3. Drag the **Ring Volume** slider to the right.

Some of these steps work only on Android 12 and up. On older versions of Android, tap the **down arrow** at the right and use the **Ring** slider.

If neither of these matches what you see, tell me and I'll help you find it.

## tr026-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Turn on Wi-Fi Calling (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108066

**USER:**
My iPhone has no signal in my basement apartment but I have Wi-Fi. Can I make calls using the Wi-Fi?

**ASSISTANT:**
iPhone has a feature called **Wi-Fi Calling** that lets you make calls over Wi-Fi when there is little or no cellular coverage. Turning it on takes about a minute.

1. Open the **Settings** app.
2. Tap **Cellular**.
3. Tap **Wi-Fi Calling**.
4. Turn on **Wi-Fi Calling on This iPhone**.
5. Tap **Enable** when asked.

Your iPhone may ask you to enter or confirm your address. This address is used for emergency services, so please enter it carefully.

Wi-Fi Calling only works if your phone company offers it. To see that it's working, open Control Center. If Wi-Fi Calling is available, you'll see **Wi-Fi** in the status bar there. Then you make calls the same way you always do.

If you don't see **Wi-Fi Calling** in that menu, your phone company may not offer it. Tell me what you see, and you can also ask your phone company.

## tr026-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Turn on Wi-Fi Calling (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/108066

**USER:**
calls keep dropping in my house, what can I do

**ASSISTANT:**
That's frustrating. Is your phone an **iPhone** or an Android phone?

**USER:**
It's an iPhone 12.

**ASSISTANT:**
Thanks. This should help.

iPhone has a feature called **Wi-Fi Calling** that lets you make calls over Wi-Fi when there is little or no cellular coverage. Turning it on takes about a minute.

1. Open the **Settings** app.
2. Tap **Cellular**.
3. Tap **Wi-Fi Calling**.
4. Turn on **Wi-Fi Calling on This iPhone**.
5. Tap **Enable** when asked.

Your iPhone may ask you to enter or confirm your address. This address is used for emergency services, so please enter it carefully.

Wi-Fi Calling only works if your phone company offers it. To see that it's working, open Control Center. If Wi-Fi Calling is available, you'll see **Wi-Fi** in the status bar there. Then you make calls the same way you always do.

If you don't see **Wi-Fi Calling** in that menu, your phone company may not offer it. Tell me what you see, and you can also ask your phone company.

## tr027-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Take a screenshot (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9075928?hl=en

**USER:**
how do i take a screenshot

**ASSISTANT:**
Sure. The buttons are different depending on the phone. Is yours an **iPhone** or an **Android** phone, like Samsung or Google Pixel?

**USER:**
Android. Motorola.

**ASSISTANT:**
Thanks. Here's how to take a picture of your screen on your Motorola. It only takes a second.

1. Get the screen showing what you want to capture.
2. Press the **Power** button and the **Volume Down** button **at the same time**, then let go.

You'll see a small preview of the screenshot in the bottom-left corner.

**To find it later:** open the **Photos** app, tap **Collections** at the bottom, then **On this device**, then **Screenshots**. If your phone uses a **Gallery** app instead, open it, tap **Album view**, then tap **Screenshots folder**.

If pressing both buttons doesn't work, hold the **Power** button for a few seconds and tap **Screenshot**.
