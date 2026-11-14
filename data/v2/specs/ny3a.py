TASKS = [
    {
        "task_id": "TR-147",
        "task_type": "force_restart",
        "task": "The phone is frozen or will not respond",
        "platform": "Android",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Android Help: Fix an Android device that freezes or won't respond", "url": "https://support.google.com/android/answer/7664998"},
        "source_notes": """After each step, restart your phone to see if it fixed the issue.
1. Force restart: if the phone is frozen with the screen on, hold down the power button for about 60 seconds to restart.
2. Check for Android updates: open the Settings app, select System, then Software update. Follow the on-screen steps. Menu names can vary by phone.
3. Check storage: problems can start when less than 10% of storage is free. Free up space if low.
4. Update apps: in Google Play Store tap the profile icon at top right, Manage apps & devices, update apps under Updates available.
5. Force stop apps you are not using: Settings, Apps, See all apps, pick the app, Force stop, OK.
6. Safe mode temporarily turns off all downloaded apps (steps vary by phone). 7. Remove recently downloaded apps one at a time.
8. Factory data reset is a last resort and erases all data on the phone; back up first. 9. If the problem continues, contact your carrier or device manufacturer. Custom Android versions: check with the device manufacturer.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My Android phone is frozen. The screen is on but nothing happens when I touch it. What do I do?",
                 """Let's restart it by force.

1. Press and hold the **power button** for about 60 seconds.
2. Keep holding it until the phone restarts.

If it freezes again after it restarts, check for an update. Open **Settings**, tap **System**, then tap **Software update**. Menu names can be a little different on some phones.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android (Pixel)",
             "messages": [
                 "So I was looking at pictures my grandson sent on my Google Pixel phone and then the picture just stopped moving. The screen is still lit up but I can't swipe or tap anything, not even the home button. I've been poking at it for ten minutes. My husband says to take the battery out but I don't think this phone has that. Help please.",
                 """You do not need to take anything apart. Try this instead.

1. Press and hold the **power button**.
2. Keep holding it for about 60 seconds, even if it seems like a long time.
3. Let go when the phone restarts.

This works when the phone is frozen with the screen on, like yours. If it keeps freezing later, open **Settings**, tap **System**, then **Software update**, and follow the steps on the screen.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my phone wont respond when i touch the screen",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "my phone wont respond when i touch the screen",
                 "I can help with that. Is your phone an **iPhone** or an **Android** phone?",
                 "Android",
                 """Thanks. If the screen is on but frozen, force a restart.

1. Press and hold the **power button** for about 60 seconds.
2. Keep holding until the phone restarts.

If it keeps freezing, open **Settings**, tap **System**, then **Software update**, and follow the steps on the screen.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My Android phone froze on the lock screen. I have a lot of photos of my late wife on it and I'm scared of losing them, so please do not tell me to erase or reset anything. Is there something gentle I can try first?",
                 """Yes. The first thing to try is only a restart.

1. Press and hold the **power button** for about 60 seconds.
2. Keep holding until the phone restarts.

A reset that erases everything is the very last thing to try, and only after other fixes fail. If the freezing keeps happening, try **Settings**, then **System**, then **Software update** next.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My Android phone is frozen with the screen on. How do I restart it?",
                 """Force a restart.

1. Press and hold the **power button** for about 60 seconds.
2. Keep holding until the phone restarts.

If it freezes again, open **Settings**, tap **System**, then **Software update**.""",
                 "It restarted, thank you, but it freezes again almost every day.",
                 """Let's look at what may be causing it. Restart the phone after each of these.

1. Open **Settings**, tap **System**, then **Software update**, and follow the steps on the screen.
2. Look at your storage in **Settings**. Problems can start when less than 10% of the storage is free, so free up some space if it is low.""",
             ]},
        ],
    },
    {
        "task_id": "TR-148",
        "task_type": "phone_not_charging",
        "task": "The phone will not charge",
        "platform": "Android (Pixel)",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Pixel Phone Help: Fix a Pixel phone that won't charge or turn on", "url": "https://support.google.com/pixelphone/answer/7167687"},
        "source_notes": """1. Press and hold the Power button for 5 to 7 seconds (use a Google 30 W USB-C or PPS adapter, or another USB PD adapter rated 15 W or more). If the battery is completely drained and was not turned on in a long time, you may see no charging icon, no vibration, and no display response for up to 25 minutes while plugged in. If still nothing after 25 minutes, get the phone repaired.
2. Case, charger, cable, outlet: remove the phone case so it does not block the charging plug or wireless charger. Wired: test adapter and cable on another device; make sure the cable is firmly connected to both adapter and phone; check the phone's port for dust or lint; try a different cable or adapter. Wireless: use a charger approved for your Pixel. A "Check charging accessory" notification means the cable or adapter may be damaged or unsupported. Outlet: plug charger into a wall outlet; test the outlet with another device such as a lamp. Charge: plug in, wait one minute; if you see a battery icon the phone is off and charging; to confirm charging open Settings and tap Battery. A very low battery may need several minutes before the screen turns on; keep charging at least 10 more minutes.
4. Screen: if no battery icon appears after plugging in, press and hold Power for about 35 seconds to reboot, wait about 2 minutes, then call the phone from another phone or use the Find Hub app. If it rings but screen stays blank, contact an authorized repair center.
5. Manual reset erases all data, last resort. 6. If steps fail, check replacement options and warranty.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android (Pixel)",
             "messages": [
                 "My Google Pixel phone won't charge. I plug it in and nothing seems to happen.",
                 """Let's check the usual causes.

1. Take the phone case off so it does not block the plug.
2. Make sure the cable is pushed in firmly at both ends, the adapter and the phone.
3. Look in the phone's charging port for dust or lint.
4. Try a different cable or adapter, and a different wall outlet.
5. Leave it plugged in for one minute. A battery icon on the screen means the phone is off and charging.
6. Press and hold the **Power** button for 5 to 7 seconds.

A very low battery can take several minutes before the screen turns on.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android (Pixel)",
             "messages": [
                 "My Pixel phone has been sitting in a drawer since the spring because I got a new one for work and now I want to use the old one for my mother. I plugged it in about ten minutes ago and the screen is totally black, no light, no buzzing, nothing. Is it broken? I'm not very good with this stuff.",
                 """It may not be broken. A phone that has been fully drained for a long time can show nothing at first.

1. Plug it into a working wall outlet with a firmly connected cable and adapter.
2. Press and hold the **Power** button for 5 to 7 seconds.
3. Keep it plugged in. You may see no charging icon, no vibration, and no screen response for up to 25 minutes.

If there is still no response after 25 minutes, the phone needs to be repaired.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "my phone wont charge anymore",
                 "I can help with that. Is it a **Google Pixel** phone, or another kind of phone?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android (Pixel)",
             "messages": [
                 "my phone wont charge anymore",
                 "I can help with that. Is it a **Google Pixel** phone, or another kind of phone?",
                 "its a pixel",
                 """Thanks. Try these in order.

1. Take off the phone case.
2. Make sure the cable is firmly connected to both the adapter and the phone.
3. Check the charging port for dust or lint.
4. Try a different cable or adapter, and plug it into a different wall outlet.
5. Wait one minute. A battery icon means the phone is off and charging.
6. Press and hold the **Power** button for 5 to 7 seconds.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android (Pixel)",
             "messages": [
                 "My Pixel won't charge. I only have the one cable and charger that came with it and I live far from any store, so I can't just go buy new ones. What can I check with what I have?",
                 """You can check a lot with what you have.

1. Take off the phone case.
2. Test your adapter and cable on another device, for example a family member's phone, to see if they work.
3. Push the cable in firmly at both ends.
4. Look in the phone's charging port for dust or lint.
5. Test the wall outlet with another device, such as a lamp.
6. Charge for a few minutes, then press and hold the **Power** button for 5 to 7 seconds.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android (Pixel)",
             "messages": [
                 "My Pixel phone won't charge. What should I try?",
                 """Try these in order.

1. Take off the phone case.
2. Make sure the cable is firmly connected at both ends.
3. Check the charging port for dust or lint.
4. Try a different cable, adapter, and wall outlet.
5. Wait one minute. A battery icon means the phone is off and charging.
6. Press and hold the **Power** button for 5 to 7 seconds.""",
                 "I did all that and no battery picture shows up on the screen.",
                 """Let's try one more thing.

1. Press and hold the **Power** button for about 35 seconds to reboot.
2. Wait about 2 minutes.
3. Call the phone from another phone, or use the **Find Hub** app, to see if it rings.

If it rings but the screen stays blank, contact an authorized repair center.""",
             ]},
        ],
    },
    {
        "task_id": "TR-149",
        "task_type": "internet_not_working",
        "task": "The phone cannot connect to the internet",
        "platform": "Android",
        "category": "technical_support",
        "sensitive": False,
        "source": {"title": "Android Help: Fix internet connection problems on Android devices", "url": "https://support.google.com/android/answer/2651367"},
        "source_notes": """Signs: downloads do not start or stay at 0%, Google Play stuck on Loading, web pages will not load.
1. Restart the device.
2. Switch between Wi-Fi and mobile data: Settings, Network & internet (or Connections; names vary). Turn Wi-Fi off and mobile data on and check. If nothing changes, turn mobile data off and Wi-Fi on and check.
Mobile data: 3. Settings, Network & internet or Connections, then Mobile data or Cellular data (some devices: Data usage first). Turn it on; if already on, turn off and on. Look for data indicator (2G, 3G, 4G, or H) beside signal bars at top. If no indicator while Wi-Fi is active, turn Wi-Fi off and check again. No indicator at all: may be out of coverage; move somewhere else or go outside. If it happens often contact mobile provider.
4. Airplane mode: Settings, Network & internet or Connections, Airplane mode. Turn on, wait 10 seconds, turn off. If problems continue contact mobile provider.
Wi-Fi: 5. Settings, Network & Internet or Connections, Wi-Fi. Turn Wi-Fi on. Look for the Wi-Fi indicator at top. If missing or no bars filled, may be out of range: move closer to router, confirm stronger signal, try again.
6. Restart the wireless router (home Wi-Fi): unplug, confirm lights go out, wait 30 seconds, plug back in, wait about 30 seconds for all lights to return. If persists contact internet provider or host of the Wi-Fi network.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My Android phone says it has no internet. Web pages won't load. What should I do?",
                 """Try these in order.

1. Restart your phone.
2. Open **Settings** and tap **Network & internet** (on some phones it is called **Connections**).
3. Turn Wi-Fi off and mobile data on, and see if things load. If not, turn mobile data off and Wi-Fi on, and check again.
4. Turn **Airplane mode** on, wait 10 seconds, then turn it off.
5. If you use home Wi-Fi, unplug the router, wait 30 seconds, plug it back in, and wait about 30 seconds for the lights to come back.

If problems continue, contact your mobile service provider or your internet provider.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "Hi, I'm at home and my Android phone shows the Wi-Fi at the top but nothing will open, not the weather, not my email. My daughter's tablet in the next room is fine though, or at least it was an hour ago. I've had the same Wi-Fi for years. I restarted the phone once already. What else can I try?",
                 """Here is what to try next for Wi-Fi.

1. Open **Settings** and tap **Network & Internet** (or **Connections**), then tap **Wi-Fi**.
2. Make sure **Wi-Fi** is turned on.
3. Look at the Wi-Fi symbol at the top of the screen. If it is missing or has no bars filled, you may be out of range. Move closer to the router and try again.
4. Restart the router. Unplug it and make sure the lights go out. Wait 30 seconds, plug it back in, and wait about 30 seconds for all the lights to come back.

If it still does not work, contact your internet provider.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "Android",
             "messages": [
                 "The internet on my Android phone is not working.",
                 "I can help with that. Is the problem when you are on **Wi-Fi**, on **mobile data**, or both?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "The internet on my Android phone is not working.",
                 "I can help with that. Is the problem when you are on **Wi-Fi**, on **mobile data**, or both?",
                 "mobile data, I'm out shopping",
                 """Let's check your mobile data.

1. Restart your phone.
2. Open **Settings** and tap **Network & internet** (or **Connections**), then **Mobile data** (or **Cellular data**).
3. Make sure it is on. If it is already on, turn it off and back on.
4. Look for 2G, 3G, 4G, or H next to the signal bars at the top of the screen.
5. If you see none, you may be out of coverage. Move somewhere else, or go outside, and check again.

If this happens often, contact your mobile service provider.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My Android phone can't get online at my sister's house. I can't touch her router because she's away and it's in her locked office, and I don't know her Wi-Fi settings. What can I do from my phone only?",
                 """You can do these from your phone.

1. Restart your phone.
2. Open **Settings** and tap **Network & internet** (or **Connections**).
3. Turn Wi-Fi off and mobile data on, and check if things load.
4. Turn **Airplane mode** on, wait 10 seconds, then turn it off.
5. Open the Wi-Fi settings and check the Wi-Fi symbol at the top of the screen. If no bars are filled, move closer to where the router is.

If the Wi-Fi still has problems, the person who runs that network can help.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android",
             "messages": [
                 "My Android phone is on Wi-Fi at home but web pages won't load. What do I try?",
                 """Try these in order.

1. Restart your phone.
2. Open **Settings**, tap **Network & Internet** (or **Connections**), then **Wi-Fi**, and make sure **Wi-Fi** is on.
3. Check for the Wi-Fi symbol at the top of the screen.
4. Restart the router. Unplug it, wait 30 seconds, plug it back in, and wait about 30 seconds for the lights to return.""",
                 "I turned Wi-Fi on but there's no Wi-Fi symbol at the top of my screen.",
                 """If the symbol is missing, or none of its bars are filled, you may be out of range.

1. Move closer to the router.
2. Check that the Wi-Fi symbol now shows a stronger signal.
3. Try opening a web page again.""",
             ]},
        ],
    },
    {
        "task_id": "TR-150",
        "task_type": "messages_not_sending",
        "task": "Text messages will not send or arrive",
        "platform": "Android (Google Messages)",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Google Messages Help: Fix problems sending, receiving, or connecting to messages", "url": "https://support.google.com/messages/answer/9077245"},
        "source_notes": """General: 1 Update Google Messages to the most recent version. 2 If you use a SIM card make sure it is inserted properly. 3 Fi users sign in to Project Fi app. 4 Set Google Messages as your default texting app. 5 Confirm your carrier supports SMS, MMS, or RCS. If you see "Not supported - RCS chats are not supported by your carrier," your carrier does not currently support RCS. 6 Check your plan or credit balance covers sending and receiving. 7 Check for signal. 8 If airplane mode is on, turn it off. 9 Switching from iPhone: deactivate iMessage for your number. 10 If you changed messaging apps and are not receiving, turn off RCS chats at messages.google.com/disable-chat.
Specific contacts: delete the contact and add again; check whether you blocked the contact; verify the phone number is correct; check whether you need a country code (for example +1 for US numbers).
MMS: make sure you have a data connection; in the device settings app reset APN settings to default; turn off MMS mass text: open Google Messages, top right tap Profile picture or Initials, Messages settings, Advanced, Group messaging, tap "Send an MMS reply to all recipients (group MMS)".
Other: if notification says Google Messages may not send or receive until more space is available, free up device storage.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "None of my texts are going through in Google Messages on my Android phone. What should I check?",
                 """Check these in order.

1. Update **Google Messages** to the newest version.
2. If your phone has a SIM card, make sure it is inserted properly.
3. Set **Google Messages** as your default texting app.
4. Check that your plan or credit balance covers sending and receiving texts.
5. Check that you have signal.
6. If airplane mode is on, turn it off.

Also check that your carrier supports SMS, MMS, or RCS.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "I can text everyone fine in Google Messages on my Android phone, my kids, my neighbor, everybody, except my friend Margaret. Her texts to me are fine too, but whenever I answer her it just won't go. I saved her number years ago when she lived in another state. What on earth is going on?",
                 """The trouble is probably with that one contact. Try these.

1. Delete Margaret from your contacts and add her again.
2. Check whether you blocked her.
3. Check that her phone number is correct.
4. Check whether the number needs a country code, for example +1 for US numbers.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "Android (Google Messages)",
             "messages": [
                 "Google Messages on my Android phone is not working right, my texts are failing.",
                 "I can help with that. Is the problem with **everyone**, with **one person**, or with **picture messages**?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "Google Messages on my Android phone is not working right, my texts are failing.",
                 "I can help with that. Is the problem with **everyone**, with **one person**, or with **picture messages**?",
                 "picture messages, plain words go through",
                 """For picture messages, try these.

1. Make sure you have a data connection.
2. In your phone's **Settings** app, reset your APN settings to default.
3. Open **Google Messages**. At the top right, tap your **Profile picture** or **Initials**, then **Messages settings**, then **Advanced**, then **Group messaging**.
4. Tap **Send an MMS reply to all recipients (group MMS)**.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "My texts in Google Messages won't send on my Android. Please don't tell me to take out the SIM card, I'm afraid I'll break it and I can't get to the store. What else can I check?",
                 """No problem, you can skip the SIM card. Check these instead.

1. Update **Google Messages** to the newest version.
2. Set **Google Messages** as your default texting app.
3. Check that your plan or credit balance covers sending and receiving.
4. Check that you have signal.
5. If airplane mode is on, turn it off.
6. Confirm your carrier supports SMS, MMS, or RCS.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "My texts won't send in Google Messages on my Android. What can I check?",
                 """Check these in order.

1. Update **Google Messages** to the newest version.
2. Set **Google Messages** as your default texting app.
3. Check that your plan or credit balance covers sending and receiving.
4. Check that you have signal.
5. If airplane mode is on, turn it off.
6. Confirm your carrier supports SMS, MMS, or RCS.""",
                 "Under my chat it says Not supported - RCS chats are not supported by your carrier. Is that why?",
                 """That message means your carrier does not currently support RCS chats. It does not point to something you did wrong.

1. Confirm your carrier supports SMS, MMS, or RCS.
2. Check that your plan or credit balance covers sending and receiving.
3. Check that you have signal.""",
             ]},
        ],
    },
    {
        "task_id": "TR-151",
        "task_type": "group_text",
        "task": "Send a group text",
        "platform": "Android (Google Messages)",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Google Messages Help: Explore group conversations in Google Messages", "url": "https://support.google.com/messages/answer/9367099"},
        "source_notes": """Primary page 9367099 (Explore group conversations): start a new conversation, look for contacts with the RCS tag and select the people you want. Contacts without the RCS tag create an MMS group chat instead of an RCS chat. You can name the group when you create it; only you can see the name. Write your message and send it. If group members have RCS turned on, iPhone contacts can show the RCS tag too. To check RCS, start a new conversation and look for the RCS tag.
Group messaging default: Messages settings, Advanced, Group messaging, pick mass text or group MMS. Group conversations (group MMS): send an MMS reply to all recipients. Mass text: send an SMS reply to all recipients and get individual replies. Add people: open group, More, Group details, Add people.
Supporting page 16287429 (Create RCS groups): open Messages, tap Start chat, then Create group, select contacts, tap Next. Supporting page 9077245: top right tap Profile picture or Initials, Messages settings, Advanced, Group messaging, option "Send an MMS reply to all recipients (group MMS)".""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "How do I send one text to my three kids at the same time in Google Messages on my Android phone?",
                 """You can send it as a group text.

1. Open **Google Messages**.
2. Tap **Start chat**, then tap **Create group**.
3. Pick each of your kids from your contacts.
4. Tap **Next**.
5. Write your message and send it.

Contacts without the **RCS** tag will get a regular group text (an MMS group chat), which still works.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "I'm planning a birthday dinner for my sister and I need to tell her husband, my brother, and two cousins the time and place all at once. One cousin has an iPhone. I use Google Messages on my Samsung Android phone. Will the iPhone cousin get it too, and how do I start the message?",
                 """Yes, the iPhone cousin can be in the group. Here is how to start it.

1. Open **Google Messages**.
2. Tap **Start chat**, then tap **Create group**.
3. Pick everyone from your contacts.
4. Tap **Next**.
5. Write your message and send it.

If your group members have RCS chats turned on, iPhone contacts can show the **RCS** tag too. Contacts without the tag get an MMS group chat instead.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "Android",
             "messages": [
                 "I want to send the same message to a whole bunch of people at once on my Android phone",
                 "I can help with that. Are you using the **Google Messages** app, or a different texting app?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "I want to send the same message to a whole bunch of people at once on my Android phone",
                 "I can help with that. Are you using the **Google Messages** app, or a different texting app?",
                 "Google Messages",
                 """Thanks. Start a group text like this.

1. Open **Google Messages**.
2. Tap **Start chat**, then tap **Create group**.
3. Pick the people you want from your contacts.
4. Tap **Next**.
5. Write your message and send it.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "I'm sending a text to everyone in my choir in Google Messages on my Android phone, but I don't want their replies going to the whole choir. I just want each person's answer to come back to me separately. Can that be done?",
                 """Yes, use mass text. Replies then come back to you one by one.

1. Open **Google Messages**.
2. At the top right, tap your **profile picture** or **initials**, then tap **Messages settings**, then **Advanced**.
3. Tap **Group messaging**.
4. Choose **mass text** as your default.
5. Go back, tap **Start chat**, then **Create group**, pick your choir members, and tap **Next**.
6. Write your message and send it.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "How do I send a group text to my book club in Google Messages on Android?",
                 """Start a group like this.

1. Open **Google Messages**.
2. Tap **Start chat**, then tap **Create group**.
3. Pick your book club members.
4. Tap **Next**.
5. Write your message and send it.""",
                 "It sent, but when people answer, I get their replies in separate chats, not all together.",
                 """Replies come back separately when the setting is mass text. To keep group replies in one conversation, change this.

1. In **Google Messages**, at the top right, tap your **profile picture** or **initials**.
2. Tap **Messages settings**, then **Advanced**, then **Group messaging**.
3. Tap **Send an MMS reply to all recipients (group MMS)**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-152",
        "task_type": "report_spam_text",
        "task": "Report and block spam texts",
        "platform": "Android (Google Messages)",
        "category": "online_services",
        "sensitive": True,
        "source": {"title": "Google Messages Help: Report spam and block a number in Google Messages", "url": "https://support.google.com/messages/answer/9061432"},
        "source_notes": """From the conversation list: open Google Messages, press and hold the conversation, tap Block, then Report spam, then OK.
From inside a conversation: open it, tap More options, then Details, then Block & report spam, then OK.
After you report: the sender is blocked and the conversation moves to your Spam & blocked folder. The number is reported to Google. The last 10 incoming messages from the spammer are reported (in a group conversation this may include other users' messages; you can choose whether to share them). Your country code (from SIM and IP address) is reported. Your past replies to the spammer are not sent to Google. Your name and phone number are not linked to the spammer's messages. The spammer cannot see your report and will not know about it. Your report might create a "Spam reporting" conversation that sends a copy of the spammer's number and most recent text to your mobile carrier; these conversations may automatically go to Spam & blocked.
Notes: you can report without blocking; sending reports is optional, you can block without reporting. Page has no unblock steps.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "I keep getting spam texts from the same number in Google Messages on my Android phone. How do I report and block it?",
                 """You can block that number and report it at the same time.

1. Open **Google Messages**.
2. Press and hold the conversation with that number.
3. Tap **Block**, then tap **Report spam**, then tap **OK**.

The sender is blocked, and the conversation moves to your **Spam & blocked** folder.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "A text came in this morning saying I won a gift card and need to click right away. I've got the conversation open in Google Messages on my Android phone right now. I don't want to hear from them again, and I'd like Google to know about it so they stop doing this to other people too.",
                 """Since the conversation is already open, do this.

1. Tap **More options**.
2. Tap **Details**.
3. Tap **Block & report spam**.
4. Tap **OK**.

That blocks the sender, moves the conversation to your **Spam & blocked** folder, and reports the number to Google.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "unknown",
             "messages": [
                 "how do i get rid of all these junk texts, they never stop",
                 "I can help with that. Do you read your texts in the **Google Messages** app, or a different app?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "how do i get rid of all these junk texts, they never stop",
                 "I can help with that. Do you read your texts in the **Google Messages** app, or a different app?",
                 "google messages",
                 """Thanks. You can report and block each spammer's number.

1. Open **Google Messages**.
2. Press and hold the junk conversation.
3. Tap **Block**, then tap **Report spam**, then tap **OK**.

The sender is blocked and the conversation moves to your **Spam & blocked** folder.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "I replied STOP to a spam text last week and now I'm nervous. If I report them in Google Messages on my Android, will Google see my reply, and will the spammer find out it was me?",
                 """No on both. Your past replies to the spammer are not sent to Google, and the spammer cannot see your report or know about it. Your name and phone number are not linked to their messages.

To report and block:

1. Open **Google Messages** and press and hold the conversation.
2. Tap **Block**, then tap **Report spam**, then tap **OK**.

Google does get the number and the last 10 incoming messages from the sender.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android (Google Messages)",
             "messages": [
                 "How do I report a spam text in Google Messages on my Android phone?",
                 """Do this to report and block it.

1. Open **Google Messages**.
2. Press and hold the conversation you want to report.
3. Tap **Block**, then tap **Report spam**, then tap **OK**.""",
                 "I did that, and now there's a new conversation called Spam reporting. Did I do something wrong?",
                 """No, that can happen after a report. Your report might create a **Spam reporting** conversation. It sends a copy of the spammer's number and most recent text to your mobile carrier. These conversations may automatically go to **Spam & blocked**.""",
             ]},
        ],
    },
    {
        "task_id": "TR-153",
        "task_type": "voicemail",
        "task": "Check voicemail and turn on visual voicemail",
        "platform": "Android (Phone app)",
        "category": "communication",
        "sensitive": False,
        "source": {"title": "Phone app Help: How to check your voicemail", "url": "https://support.google.com/phoneapp/answer/2811844"},
        "source_notes": """Some steps require Android 6.0 or higher. Visual voicemail is available only with listed carriers (AT&T, Cellcom, Coriolis, Google Fi, O2, Orange, T-Mobile); not all carriers or countries.
Method 1, notification: swipe down from the top of the screen, tap Voicemail.
Method 2, call your voicemail: open the Phone app, at the bottom tap Dialpad, touch and hold 1.
Method 3, visual voicemail (list): open the Phone app, top right More options, Settings, Voicemail, turn on Visual voicemail. To check messages open the Phone app and tap Voicemail at the bottom. If you cannot find it, call your voicemail instead. If you use your carrier's voicemail app, the Phone app's visual voicemail turns off. Turning off visual voicemail deletes recordings from the Phone app (carrier may keep a copy). To share: expand the voicemail, tap Send to, choose an app.
Voicemail settings: Phone app, More options, Settings, Voicemail; Advanced Settings then Setup is voice mailbox setup; Advanced Settings then Service is carrier handling; Notifications.
Page does not describe PIN or greeting setup.""",
        "examples": [
            {"suffix": "a", "scenario": "direct", "style": "plain", "specification": "fully_specified", "platform": "Android (Phone app)",
             "messages": [
                 "I got a notification that someone left me a voicemail on my Android phone. How do I listen to it?",
                 """You can open it from the notification.

1. Swipe down from the top of the screen.
2. Tap **Voicemail**.""",
             ]},
            {"suffix": "c", "scenario": "direct_messy", "style": "verbose", "specification": "fully_specified", "platform": "Android (Phone app)",
             "messages": [
                 "My doctor's office said they left a message on my phone but I never saw any notice about it, and I've swiped down and don't see anything there. I use the regular Phone app on my Android. Is there a way to call in and hear my messages myself?",
                 """Yes, you can call your voicemail from the Phone app.

1. Open the **Phone** app.
2. At the bottom, tap **Dialpad**.
3. Touch and hold the number **1**.

Your phone calls your voicemail so you can listen.""",
             ]},
            {"suffix": "b", "scenario": "missing_info", "style": "under_specified", "specification": "underspecified", "platform": "Android (Phone app)",
             "messages": [
                 "How do I hear my voicemail on my Android phone? I use the Phone app.",
                 "I can help with that. Do you want to **call in** to hear your messages, or see them as a **list** on the screen?",
             ]},
            {"suffix": "d", "scenario": "followup", "style": "under_specified", "specification": "fully_specified", "platform": "Android (Phone app)",
             "messages": [
                 "How do I hear my voicemail on my Android phone? I use the Phone app.",
                 "I can help with that. Do you want to **call in** to hear your messages, or see them as a **list** on the screen?",
                 "a list on the screen please",
                 """That is called visual voicemail. To turn it on:

1. Open the **Phone** app.
2. At the top right, tap **More options**, then **Settings**, then **Voicemail**.
3. Turn on **Visual voicemail**.

To listen, open the **Phone** app and tap **Voicemail** at the bottom. It works only with some carriers.""",
             ]},
            {"suffix": "e", "scenario": "constraint", "style": "over_specified", "specification": "fully_specified", "platform": "Android (Phone app)",
             "messages": [
                 "My son set up my Android phone and told me never to change anything in the settings. I just want to hear one voicemail right now in the Phone app, without changing any settings. Is that possible?",
                 """Yes. Two ways need no settings.

From the notification:
1. Swipe down from the top of the screen.
2. Tap **Voicemail**.

Or by calling in:
1. Open the **Phone** app.
2. At the bottom, tap **Dialpad**.
3. Touch and hold **1**.""",
             ]},
            {"suffix": "r", "scenario": "failure_recovery", "style": "failure_recovery", "specification": "fully_specified", "platform": "Android (Phone app)",
             "messages": [
                 "How do I see my voicemails as a list in the Phone app on my Android?",
                 """Turn on visual voicemail.

1. Open the **Phone** app.
2. At the top right, tap **More options**, then **Settings**, then **Voicemail**.
3. Turn on **Visual voicemail**.
4. To listen, open the **Phone** app and tap **Voicemail** at the bottom.""",
                 "I turned it on but I can't find a Voicemail button at the bottom of the Phone app.",
                 """If you can't find it, call your voicemail instead.

1. Open the **Phone** app.
2. At the bottom, tap **Dialpad**.
3. Touch and hold **1**.

Visual voicemail works only with some carriers, so it may not be available for yours.""",
             ]},
        ],
    },
]
