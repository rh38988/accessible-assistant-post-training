# Review input: batch ny3a, round 2 (8 examples)

## tr148-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android (Pixel)
- task: The phone will not charge (Android (Pixel)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/pixelphone/answer/7167687

**USER:**
My Pixel won't charge. I only have the one cable and charger that came with it and I live far from any store, so I can't just go buy new ones. What can I check with what I have?

**ASSISTANT:**
You can check a lot with what you have.

1. Take off the phone case.
2. Test your adapter and cable on another device, for example a family member's phone, to see if they work.
3. Push the cable in firmly at both ends.
4. Look in the phone's charging port for dust or lint.
5. Test the wall outlet with another device, such as a lamp.
6. Plug it in and wait one minute. A battery icon on the screen means the phone is off and charging.
7. Press and hold the **Power** button for 5 to 7 seconds.

## tr149-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: The phone cannot connect to the internet (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2651367

**USER:**
My Android phone can't get online at my sister's house. I can't touch her router because she's away and it's in her locked office, and I don't know her Wi-Fi settings. What can I do from my phone only?

**ASSISTANT:**
You can do these from your phone.

1. Restart your phone.
2. Open **Settings** and tap **Network & internet** (or **Connections**).
3. Turn Wi-Fi off and mobile data on, and see if things load. Then turn mobile data off and Wi-Fi on, and check again.
4. Turn **Airplane mode** on, wait 10 seconds, then turn it off.
5. Make sure **Wi-Fi** is on, then look at the Wi-Fi symbol at the top of the screen. If no bars are filled, move closer to where the router is.

If the Wi-Fi still has problems, the person who runs that network can help.

## tr150-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android (Google Messages)
- task: Text messages will not send or arrive (Android (Google Messages)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/messages/answer/9077245

**USER:**
Google Messages on my Android phone is not working right, my texts are failing.

**ASSISTANT:**
I can help with that. Is the problem with **everyone**, with **one person**, or with **picture messages**?

**USER:**
picture messages, plain words go through

**ASSISTANT:**
For picture messages, try these.

1. Make sure you have a data connection.
2. In your phone's **Settings** app, find the **APN** settings (the settings your phone uses to send picture messages) and choose to reset them to default. The exact menu names are a little different on each phone.
3. Open **Google Messages**. At the top right, tap your **Profile picture** or **Initials**, then **Messages settings**, then **Advanced**, then **Group messaging**.
4. Tap **Send an MMS reply to all recipients (group MMS)**.

## tr151-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android (Google Messages)
- task: Send a group text (Android (Google Messages)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/messages/answer/9367099 ; https://support.google.com/messages/answer/16287429

**USER:**
How do I send one text to my three kids at the same time in Google Messages on my Android phone?

**ASSISTANT:**
You can send it as a group text.

1. Open **Google Messages**.
2. Tap **Start chat**, then tap **Create group**.
3. Pick each of your kids from your contacts.
4. Tap **Next**.
5. Write your message and send it.

Contacts without the **RCS** tag will get a regular group text (an MMS group chat), which still works.

## tr151-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android (Google Messages)
- task: Send a group text (Android (Google Messages)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/messages/answer/9367099 ; https://support.google.com/messages/answer/16287429

**USER:**
I'm planning a birthday dinner for my sister and I need to tell her husband, my brother, and two cousins the time and place all at once. One cousin has an iPhone. I use Google Messages on my Samsung Android phone. Will the iPhone cousin get it too, and how do I start the message?

**ASSISTANT:**
Yes, the iPhone cousin can be in the group. Here is how to start it.

1. Open **Google Messages**.
2. Tap **Start chat**, then tap **Create group**.
3. Pick everyone from your contacts.
4. Tap **Next**.
5. Write your message and send it.

If your group members have RCS chats turned on, iPhone contacts can show the **RCS** tag too. Contacts without the tag get an MMS group chat instead.

## tr151-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android (Google Messages)
- task: Send a group text (Android (Google Messages)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/messages/answer/9367099 ; https://support.google.com/messages/answer/16287429

**USER:**
I want to send the same message to a whole bunch of people at once on my Android phone

**ASSISTANT:**
I can help with that. Are you using the **Google Messages** app, or a different texting app?

**USER:**
Google Messages

**ASSISTANT:**
Thanks. Start a group text like this.

1. Open **Google Messages**.
2. Tap **Start chat**, then tap **Create group**.
3. Pick the people you want from your contacts.
4. Tap **Next**.
5. Write your message and send it.

## tr151-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android (Google Messages)
- task: Send a group text (Android (Google Messages)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/messages/answer/9367099 ; https://support.google.com/messages/answer/16287429 ; https://support.google.com/messages/answer/9077245

**USER:**
I'm sending a text to everyone in my choir in Google Messages on my Android phone, but I don't want their replies going to the whole choir. I just want each person's answer to come back to me separately. Can that be done?

**ASSISTANT:**
Yes, use mass text. Replies then come back to you one by one.

1. Open **Google Messages**.
2. At the top right, tap your **profile picture** or **initials**, then tap **Messages settings**, then **Advanced**.
3. Tap **Group messaging**.
4. Choose **mass text** as your default.
5. Go back to the main screen.
6. Tap **Start chat**, then **Create group**.
7. Pick your choir members, then tap **Next**.
8. Write your message and send it.

## tr151-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android (Google Messages)
- task: Send a group text (Android (Google Messages)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/messages/answer/9367099 ; https://support.google.com/messages/answer/16287429 ; https://support.google.com/messages/answer/9077245

**USER:**
How do I send a group text to my book club in Google Messages on Android?

**ASSISTANT:**
Start a group like this.

1. Open **Google Messages**.
2. Tap **Start chat**, then tap **Create group**.
3. Pick your book club members.
4. Tap **Next**.
5. Write your message and send it.

**USER:**
It sent, but when people answer, I get their replies in separate chats, not all together.

**ASSISTANT:**
Replies come back separately when the setting is mass text. To keep group replies in one conversation, change this.

1. In **Google Messages**, at the top right, tap your **profile picture** or **initials**.
2. Tap **Messages settings**, then **Advanced**, then **Group messaging**.
3. Tap **Send an MMS reply to all recipients (group MMS)**.
