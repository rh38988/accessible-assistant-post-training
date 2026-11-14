# Review input: batch fx4, round 2 (4 examples)

## tr050-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Check battery health (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/101575

**USER:**
My iPhone XR battery goes down fast. How can I see how healthy it is?

**ASSISTANT:**
You can check it in Settings.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Health**.
4. Look at **Maximum Capacity**. It compares your battery now to when it was new.

**USER:**
I did that, but there's no capacity number. It says Unable to verify this iPhone has a genuine Apple battery. What does that mean?

**ASSISTANT:**
That message means the iPhone could not confirm that it has a genuine Apple battery. The battery health information on that screen may not be accurate.

1. Don't rely on the numbers shown there.
2. Get service for the battery through Apple Support, Apple's support website, to have it checked.

## tr051-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Start a group text (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118236

**USER:**
How do I send one message to my brother and two cousins at once on my iPhone? One cousin has an Android.

**ASSISTANT:**
You can send a group text.

1. Open the **Messages** app.
2. Tap the **Compose** button (a square with a pencil).
3. Enter their names, or tap the **Add** button (a plus icon) to pick them from Contacts.
4. Type your message.
5. Tap the **Send** button (the up arrow).

Because one person uses Android, go to **Settings**, then **Messages**, and turn on **MMS Messaging**.

**USER:**
I went to Settings, then Messages, but there is no MMS Messaging switch. My cousin with the Android didn't get anything.

**ASSISTANT:**
When that option is missing, the next step is to check with your carrier.

1. Contact your phone carrier.
2. Ask whether group MMS is included in your plan.

## tr056-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Install an app (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102590

**USER:**
Please tell me how to get the Zoom app on my iPhone.

**ASSISTANT:**
You can get it from the **App Store**.

1. Open the **App Store** app.
2. Tap the **Search** tab and look for **Zoom**.
3. Tap **Get**.
4. Confirm by double-clicking the **side button**. Use Face ID or Touch ID, or enter your Apple Account password if asked.

**USER:**
I can't find the App Store on my phone. The icon is gone.

**ASSISTANT:**
Let's look for it.

1. Swipe down from the middle of your Home Screen and search for **App Store**.
2. If it still doesn't appear, **Content & Privacy Restrictions** may be turned on.
3. Adjust your **iTunes & App Store Purchases** settings so **Installing Apps** is set to **Allow**.
4. If you did not set this up, ask the person who manages your phone.

The App Store should reappear on your device.

## tr057-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Install an app (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/9457058?hl=en

**USER:**
How do I put a weather app on my Android phone?

**ASSISTANT:**
You can get it from the **Play Store**.

1. Open the **Play Store** app.
2. Find the weather app you want.
3. Under the title, look at the star ratings and the number of downloads.
4. Tap **Install**.

**USER:**
There's no Install button. There's a price with a dollar sign where it should be.

**ASSISTANT:**
A price means it is a paid app. Free apps show **Install**.

1. If you only want a free app, don't tap the price. Go back and look for a different weather app that shows **Install**.
2. Tapping the price is how you buy the app, so only tap it if you mean to pay for it.
