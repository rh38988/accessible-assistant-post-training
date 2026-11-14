# Review input: batch fx7, round 2 (6 examples)

## tr091-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Google Maps (phone)
- task: Get directions (Google Maps (phone)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I'm driving to my sister's house tomorrow with my Android phone and I use Google Maps. I have to pick up a prescription at the pharmacy on the way, so I can't just go straight there. Can Maps take me to the pharmacy first and then my sister's?

**ASSISTANT:**
Yes. You can add the pharmacy as a stop on the way.

1. Open the **Google Maps** app.
2. Search for your sister's address and tap it.
3. At the bottom left, tap **Directions**.
4. Choose **Driving**.
5. At the top right, tap **More**, then tap **Edit stops**.
6. Add the pharmacy as a stop (you can add up to 9 stops including the final destination).
7. If the pharmacy is listed after your sister's house, press and hold the **Reorder** icon next to it and drag it above.
8. Tap **Done**.

Maps will show the route with your stop in it. The best route is **blue** and other routes are gray.

## tr093-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Zoom
- task: Join a Zoom meeting from a link (Zoom) | sensitive: False | reviewed by a person: False
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065180 ; https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0060732

**USER:**
My daughter sent me a Zoom link by email for a family call tonight. I'm on my computer. What do I do to get in?

**ASSISTANT:**
Here is how.

1. Open the email and **click the Zoom link**. You can also copy the link and paste it into your web browser.
2. A pop-up will ask if you want to open **Zoom Meetings**.
3. Click **Open**. On your computer it may say **Allow** or **Open zoom.us** instead.
4. The Zoom app opens and takes you to the meeting.

If the link already includes the passcode, you can join more quickly.

**USER:**
I clicked the link and a page came up, but the Zoom app never opened. What now?

**ASSISTANT:**
That can happen when the **Zoom Launcher plug-in** in your browser is turned off, set up wrong, or failed to run.

If you can't get the app to open, you can join from your web browser instead.

1. Click the link in your email again.
2. In the pop-up that asks you to open or download the app, click **Cancel**.
3. At the bottom of the page, click **join from your browser**.
4. Click **Allow** so Zoom can use your microphone and camera.
5. Type your name, then click **Join**.

If you don't see **join from your browser**, the meeting host may need to turn that link on.

If you use Safari, it no longer supports most plug-ins, so you have to choose to launch Zoom each time you join.

## tr099-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: iPhone stops charging at 80% (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805 ; https://support.apple.com/en-ca/108055

**USER:**
My iPhone has been sitting at 80% since last night and I'm leaving for the airport in a half hour and I need it full. I don't want to go digging through settings or change anything for good. It's just for today. What can I tap?

**ASSISTANT:**
You can charge it fully just for today, without changing any settings.

1. Wake your iPhone and look at its **Lock Screen**.
2. **Touch and hold** the notification from **Optimized Battery Charging**. It says when your iPhone will be fully charged.
3. Tap **Charge Now**.

Your iPhone will keep charging past 80%.

## tr099-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: iPhone stops charging at 80% (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805 ; https://support.apple.com/en-ca/108055

**USER:**
I have an iPhone 14. I want to switch off whatever makes it wait at 80% when it's charging. Where is it?

**ASSISTANT:**
It is probably **Optimized Battery Charging**. Here is how to turn it off.

1. Open **Settings** and tap **Battery**.
2. Tap **Battery Health & Charging**.
3. Turn **Optimized Battery Charging** off.

Turning it off can make the battery wear out faster.

**USER:**
Oh wait, I just checked and it's actually an iPhone 15. I don't see Battery Health & Charging, only a Charging choice.

**ASSISTANT:**
That is right for an iPhone 15. The setting is in a different place.

1. Open **Settings** and tap **Battery**.
2. Tap **Charging**.
3. On the slider, if the limit is below 100%, move it to 100% so the phone can charge fully.

You can choose a limit between 80 and 100 percent, in 5 percent steps. Even at 100%, Optimized Battery Charging may still delay charging past 80% in some situations. Turning off charging optimizations can wear the battery out faster.

For just one day, you can also touch and hold the Optimized Battery Charging notification on your Lock Screen and tap **Charge Now**.

## tr103-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: iPhone
- task: Set a reminder (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102484

**USER:**
My iPhone is on silent almost all the time because I can't stand the noise. But I have a heart pill I must take at noon and I need the reminder to actually make a sound anyway. Can a reminder be loud even on silent? I want one for today at noon.

**ASSISTANT:**
Yes, you can mark a reminder as **Urgent**. Urgent alarms sound even when your iPhone is silenced. This needs **iOS 26.2 or later** and iCloud Reminders turned on.

1. Open the **Reminders** app.
2. Tap **+ New Reminder** and type **Take heart pill**.
3. Tap the **Date and Time** button, then tap **Custom** and choose today at **12:00 PM**.
4. Tap the reminder, then tap **Info**.
5. Turn on **Urgent** under **Date & Time**.
6. Then open **Settings**, tap **Apps**, tap **Reminders**, and under **Allow Reminders to Access** turn on **Alarms**.

Urgent alarms only sound on the iPhone that Find My uses as your location.

## tr103-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: iPhone
- task: Set a reminder (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102484

**USER:**
Can my iPhone remind me to take my pills when I leave the house? I want it to go off when I walk out the door.

**ASSISTANT:**
Yes. A location reminder can do that.

1. Open the **Reminders** app.
2. Tap **+ New Reminder** and type **Take pills**.
3. Tap the **Location** button.
4. Pick a preset or tap **Custom**.
5. Choose **leaving**, and set the area around the place.

Your iPhone reminds you when you leave that place.

**USER:**
I set it up like that but this morning it never went off when I left.

**ASSISTANT:**
Location reminders need **Location Services** turned on.

1. Open **Settings** and tap **Privacy & Security**.
2. Turn on **Location Services**.

If you set the reminder by asking Siri for your home or work, your address must be on My Card: open **Contacts**, tap **My Card**, tap **Edit**, add the address, and tap **Done**.
