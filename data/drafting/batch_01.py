SPECS = [
    {
        "id": "TR-021", "src": ["ios_text_size"], "inspired": "ElderBench",
        "full": "How do I make the text bigger on my iPhone? Everything is too small to read.",
        "steps": """You can make the text bigger in Settings. It takes about a minute, and you can change it back anytime.

1. Open the **Settings** app. Its icon is a gray gear.
2. Tap **Display & Brightness**.
3. Tap **Text Size**.
4. Drag the slider at the bottom of the screen to the right.

The sample text changes as you drag, so you can stop when it's easy to read.

If you need it even bigger, go to **Settings**, then **Accessibility**, then **Display & Text Size**, then **Larger Text**, and drag that slider. Very large text can make some buttons harder to tap, so slide it back a little if that happens.""",
        "under": "how do I make the letters bigger on my phone",
        "clarify": "I can help with that. Is your phone an **iPhone**, or another kind of phone like a Samsung or Google Pixel?",
        "answer": "It's an iPhone.",
        "d_open": "Great, thanks.",
        "style": "incomplete", "styled_full": False,
        "styled": "the words on my iphone are too",
        "styled_reply": "It looks like your message got cut off. Do you mean the words are too **small** to read? If so, I can show you how to make them bigger.",
    },
    {
        "id": "TR-022", "src": ["and_text_size"], "inspired": "ElderBench",
        "full": "I have a Google Pixel phone. How can I make the writing on the screen larger?",
        "steps": """You can make the writing larger in Settings. It takes about a minute.

1. Open the **Settings** app.
2. Tap the search bar at the top of Settings and type **Font size**.
3. Tap **Font size** in the results.
4. Move the slider toward the larger end until the text is easy to read.

The change happens right away. A few apps ignore this setting, so text in those apps may stay the same size.

If you can't find **Font size**, tell me what you see after searching and I'll help you find it.""",
        "under": "my phone screen writing is too small",
        "clarify": "I can help you make it bigger. What kind of phone do you have, an **iPhone** or an Android phone like a Samsung or Google Pixel?",
        "answer": "Google Pixel 8",
        "d_open": "Thanks.",
        "style": "verbose", "styled_full": True,
        "styled": "My daughter gave me her old Google Pixel when she got a new phone. It works fine but I can't read anything without my glasses and I always forget where I put them. Is there a way to make the letters on the screen bigger?",
        "styled_open": "Yes, there is, and it should mean reaching for your glasses less often. Here's how:",
    },
    {
        "id": "TR-023", "src": ["line_font"], "inspired": "ElderBench",
        "full": "LINE聊天室的字好小，我要怎麼把字變大？",
        "steps": """可以的，在 LINE 的設定裡就能把字放大，大約一分鐘。

1. 打開 **LINE**，回到**主頁**。
2. 點**齒輪圖示**，進入設定。
3. 點**聊天**。
4. 點**字體大小**。
5. 選**大**或**特大**。

回到聊天室，就會看到字變大了。如果您用的是 iPhone，也可以開啟「**按照iPhone設定**」，讓 LINE 跟著手機的字體大小。

如果找不到**字體大小**，請告訴我您在設定畫面看到什麼，我再帶您找。""",
        "under": "手機上的字太小了怎麼辦",
        "clarify": "我可以幫您把字變大。請問是**哪裡的字**太小呢？是整支手機的字，還是 LINE 聊天室裡的字？",
        "answer": "是LINE裡面的字",
        "d_open": "了解，謝謝您。",
        "style": "incomplete", "styled_full": False,
        "styled": "LINE的字可以",
        "styled_reply": "您的訊息好像沒打完。您是想問 LINE 的字可以**放大**嗎？如果是的話，我可以一步一步教您。",
    },
    {
        "id": "TR-024", "src": ["ios_buttons", "ios_alarm"], "inspired": "ElderBench",
        "full": "How do I make my iPhone ring louder when someone calls?",
        "steps": """There are two quick ways. Both take less than a minute.

**Quick way:**
1. Go to your Home Screen so you're not inside an app.
2. Press the **volume up** button on the side of the phone a few times. When no other app is in use, these buttons change the ringer volume.

**In Settings:**
1. Open the **Settings** app.
2. Tap **Sounds & Haptics**.
3. Under **Ringtone and Alerts**, drag the slider to the right.

If your phone still only vibrates, it may be in Silent mode. Tell me and I'll show you how to check.""",
        "under": "My phone is too quiet when it rings.",
        "clarify": "Let's fix that so you don't miss calls. Is your phone an **iPhone**, or another kind of phone like a Samsung or Google Pixel?",
        "answer": "iPhone 13",
        "d_open": "Thanks. Here's how on your iPhone.",
        "style": "verbose", "styled_full": True,
        "styled": "I keep missing calls from my son because I don't hear my iPhone ring when I'm in the kitchen cooking. He gets worried. Can I make the ringing louder?",
        "styled_open": "Yes, you can, and that should help your son reach you. Here's how:",
    },
    {
        "id": "TR-025", "src": ["and_volume"], "inspired": "ElderBench",
        "full": "How do I turn up the ringer on my Android phone?",
        "steps": """You can do this with the volume buttons. It takes a few seconds.

1. Press either **volume button** on the side of your phone. A volume panel appears on the screen.
2. Tap the **More** icon on the right side of the volume panel.
3. Find the **Ring volume** slider and drag it to the right.

On some phones the panel looks different. If you see a small **down arrow** instead, tap it and turn up **Ring**.

If neither of these matches what you see, tell me and I'll help you find it.""",
        "under": "how do I make the ringing louder",
        "clarify": "Happy to help. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?",
        "answer": "android, it's a samsung",
        "d_open": "Thanks. Samsung screens can look a little different, so I've included what to look for.",
        "style": "incomplete", "styled_full": False,
        "styled": "ringer volume on my android",
        "styled_reply": "Sure. Do you want to make the ringer **louder** or **quieter**? I can show you either way.",
    },
    {
        "id": "TR-026", "src": ["ios_wifi_calling"], "inspired": "OATS",
        "full": "My iPhone has no signal in my basement apartment but I have Wi-Fi. Can I make calls using the Wi-Fi?",
        "steps": """iPhone has a feature called **Wi-Fi Calling** that uses your Wi-Fi for calls when the cell signal is weak. Turning it on takes about a minute.

1. Open the **Settings** app.
2. Tap **Cellular**.
3. Tap **Wi-Fi Calling**.
4. Turn on **Wi-Fi Calling on This iPhone**.
5. Tap **Enable** when asked.

Your iPhone may ask you to enter or confirm your address. This address is used for emergency services, so please enter it carefully.

When it's working, you'll see **Wi-Fi** in the status bar at the top of the screen. Then you make calls the same way you always do.

If you don't see **Wi-Fi Calling** in that menu, tell me what you see and I'll help.""",
        "under": "calls keep dropping in my house, what can I do",
        "clarify": "That's frustrating. One option is to make calls over your home Wi-Fi instead. Do you have **Wi-Fi at home**, and is your phone an **iPhone** or an Android phone?",
        "answer": "Yes I have Wi-Fi. It's an iPhone 12.",
        "d_open": "Thanks. Since you have Wi-Fi, this should help.",
        "style": "over_specified", "styled_full": True,
        "styled": "I have an iPhone 15 on Verizon, iOS 18. Cell signal inside my house is one bar but Wi-Fi is strong. I read about Wi-Fi Calling. Where is the setting?",
        "styled_open": "Since you already know what you're looking for, here are the exact steps:",
    },
    {
        "id": "TR-027", "src": ["and_screenshot"], "inspired": "ElderBench",
        "full": "How do I take a screenshot on my Android phone?",
        "steps": """Here's how to take a picture of your screen. It only takes a second.

1. Get the screen showing what you want to capture.
2. Press the **Power** button and the **Volume Down** button **at the same time**, then let go.

You'll see a small preview of the screenshot in the bottom-left corner.

**To find it later:** open the **Photos** app, tap **Collections** at the bottom, then **On this device**, then **Screenshots**. If your phone uses a **Gallery** app instead, look for the **Screenshots** album there.

If pressing both buttons doesn't work, hold the **Power** button for a few seconds and tap **Screenshot**.""",
        "under": "how do i take a screenshot",
        "clarify": "Sure. The buttons are different depending on the phone. Is yours an **iPhone** or an **Android** phone, like Samsung or Google Pixel?",
        "answer": "Android. Motorola.",
        "d_open": "Thanks. On Android phones like your Motorola:",
        "style": "verbose", "styled_full": False,
        "styled": "My grandson is helping me with my phone over the phone and he keeps saying send me a screenshot so he can see what I see. I don't know what that is or how to do it.",
        "styled_reply": "A screenshot is a picture of exactly what's on your screen, so your grandson can see it too. The buttons to take one depend on your phone.\n\n**Is your phone an iPhone or an Android phone** (like Samsung or Google Pixel)? If you're not sure, an iPhone has an apple logo on the back.",
    },
    {
        "id": "TR-028", "src": ["win_screenshot"], "inspired": "OATS",
        "full": "How do I take a screenshot on my Windows 11 laptop?",
        "steps": """The quickest way uses three keys at once. It takes a few seconds.

1. Press and hold the **Windows logo key** and the **Shift** key, then press **S**.
2. The screen dims and shows a few capture choices.
3. Choose the shape you want: a rectangle, a window, or the full screen.
4. If you chose rectangle, click and drag over the part of the screen you want.

Your screenshot is saved automatically in your **Screenshots** folder.

**Another option:** press the **Print Screen** key (often labeled **PrtSc**). This copies the whole screen, but it isn't saved as a file until you paste it somewhere, like an email.""",
        "under": "how do I take a picture of my computer screen",
        "clarify": "Happy to help. Is your computer a **Windows** computer or a **Mac**? If you're not sure, a Windows keyboard usually has a key with the Windows logo near the bottom left.",
        "answer": "Windows 11",
        "d_open": "Great, here's the easiest way on Windows 11.",
        "style": "incomplete", "styled_full": True,
        "styled": "screenshot on windows",
        "styled_open": "Here's how to take a screenshot on Windows 11:",
    },
    {
        "id": "TR-029", "src": ["line_friend"], "inspired": "ElderBench",
        "full": "孫子就在我旁邊，他說用掃QR code加LINE，要怎麼掃？",
        "steps": """好的，他在旁邊的話，掃行動條碼最快，大約一分鐘。

1. 打開 **LINE**，進入**聊天**頁面。
2. 點畫面上方的 **「+」**。
3. 選擇掃描**行動條碼**，手機的相機會打開。
4. 請孫子打開他的 LINE 行動條碼，您把相機對準他的條碼。
5. 畫面出現他的名字後，點**加入好友**。

加好友成功後，他就會出現在您的好友名單裡，可以開始聊天了。

如果找不到掃描的選項，請告訴我您點了「+」之後看到什麼，我再幫您。""",
        "under": "要怎麼加別人的LINE好友？",
        "clarify": "可以的！加好友有幾種方法，要看對方現在在不在您旁邊。**請問對方現在在您身邊嗎？**",
        "answer": "在，我孫子就坐在我旁邊",
        "d_open": "太好了，那用掃描最簡單。",
        "style": "verbose", "styled_full": True,
        "styled": "我女兒說我孫子現在也有手機了，叫我加他的LINE。他今天剛好來我家吃飯，就坐在我旁邊，他說掃一下就好，可是我不知道要掃哪裡。",
        "styled_open": "他在旁邊正好，掃一下就能加。我們一起來：",
    },
    {
        "id": "TR-030", "src": ["and_wifi"], "inspired": "ElderBench",
        "full": "How do I connect my Android phone to my Wi-Fi at home?",
        "steps": """Here's how. Have your Wi-Fi password ready. It takes about two minutes.

1. Open the **Settings** app.
2. Tap **Network & internet**.
3. Tap **Internet**.
4. Tap the name of your home network in the list. A lock icon means it needs a password.
5. Type your Wi-Fi password when asked, then confirm.

Once you're connected, your phone remembers the network and connects by itself whenever you're home with Wi-Fi turned on.

Menu names can be a little different on some phones. If you don't see **Network & internet**, tell me what you see in Settings.""",
        "under": "how do I get my phone on the wifi",
        "clarify": "I can walk you through it. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?",
        "answer": "Android",
        "d_open": "Thanks. Have your Wi-Fi password nearby.",
        "style": "over_specified", "styled_full": True,
        "styled": "I have a Google Pixel 7 with Android 15. My new internet company's router has a sticker on the bottom with the network name HOME-4G7K and a password. How do I connect the phone to it?",
        "styled_open": "That sticker has everything you need. In step 4, look for **HOME-4G7K**, and use the password from the sticker in step 5.",
    },
    {
        "id": "TR-031", "src": ["win_wifi"], "inspired": "OATS",
        "full": "How do I connect my Windows 11 laptop to Wi-Fi?",
        "steps": """Here's how. Have your Wi-Fi password ready. This takes about two minutes.

1. On the taskbar at the bottom right of the screen, click the **network, sound, or battery icons**. A small panel opens.
2. Next to the Wi-Fi button, click the **arrow** for **Manage Wi-Fi connections**.
3. Click the name of your network.
4. Click **Connect**.
5. Type your Wi-Fi password and click **Next**.

When it's done, try opening a website to check that it works.

If you don't see your network in the list, click **Refresh network list** and look again.""",
        "under": "how do i connect my computer to the internet",
        "clarify": "I can help. Is your computer a **Windows** computer or a **Mac**, and are you connecting with **Wi-Fi** or a cable?",
        "answer": "Windows 11, Wi-Fi",
        "d_open": "Thanks, here's how on Windows 11.",
        "style": "incomplete", "styled_full": False,
        "styled": "laptop wont connect to",
        "styled_reply": "It looks like your message got cut off. What won't your laptop connect to: the **Wi-Fi**, a **printer**, or something else? And is it a Windows laptop or a Mac?",
    },
    {
        "id": "TR-032", "src": ["line_notify"], "inspired": "ElderBench",
        "full": "有一個LINE群組一直跳通知，好吵，要怎麼只關掉這個群組的通知？",
        "steps": """可以只關掉這個群組，其他人的訊息還是會照常提醒您。大約十秒鐘。

1. 打開那個群組的聊天室。
2. 點聊天室上方的**選單圖示**（三條橫線）。
3. 點**關閉提醒**。

關掉之後，同一個位置會變成**開啟提醒**，想恢復時再點一次就好。

提醒您：如果群組裡有人在訊息中**標註**您，還是可能會收到提醒。""",
        "under": "LINE一直響好吵",
        "clarify": "了解，一直響真的很困擾。請問您是想**只關掉某一個聊天室或群組**的提醒，還是想**暫時關掉 LINE 全部的提醒**？",
        "answer": "只要關掉家族群組就好",
        "d_open": "好的，只關掉家族群組的話：",
        "style": "verbose", "styled_full": True,
        "styled": "我們社區的LINE群組每天早上都有人傳早安圖，一傳就好幾十則，我手機一直叮咚叮咚，但我又不想退出群組，怕錯過重要的公告。",
        "styled_open": "不用退出群組，只要關掉這個群組的提醒就好，公告還是看得到。做法如下：",
    },
    {
        "id": "TR-033", "src": ["and_update"], "inspired": "ElderBench",
        "full": "How do I update the software on my Android phone?",
        "steps": """Here's how to check for an update. Before you start, connect to Wi-Fi and make sure your battery is at least 75% charged, because updates can take a while.

1. Open the **Settings** app.
2. Tap **System**.
3. Tap **Software updates**. On some phones this is called **System update** or is in a different spot.
4. Follow the instructions on the screen to download and install the update.

Your phone may restart during the update. On Google Pixel phones, the update installs in the background and finishes when you restart.

If it says there isn't enough space, tell me and I'll help you free some up first.""",
        "under": "my phone says there's an update, should I do it?",
        "clarify": "Updates are usually a good idea because they fix problems and help keep your phone secure. So I can show you the right steps: is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?",
        "answer": "Android",
        "d_open": "Thanks. If you still see the update notification, you can tap it. Otherwise, follow these steps.",
        "style": "verbose", "styled_full": False,
        "styled": "My phone keeps showing a message about an update. Last time I updated something on my old phone all my contacts disappeared and I don't want that to happen again.",
        "styled_reply": "That sounds stressful, and it makes sense to be careful. I can walk you through doing it the safe way.\n\nFirst, **is your phone an iPhone or an Android phone** (like Samsung or Google Pixel)?",
    },
    {
        "id": "TR-034", "src": ["win_update"], "inspired": "OATS",
        "full": "How do I install Windows updates on my Windows 11 computer?",
        "steps": """Here's how to check for updates and install them. It can take a while, so do it when you won't need the computer for a bit.

1. Click the **Start** button (the Windows logo).
2. Click **Settings**.
3. Click **Windows Update**.
4. Click **Check for updates**.
5. If updates are found, click **Download & install**.

If Windows asks you to restart, save anything you're working on first, then restart to finish the update.

If you see an error message, write it down or take a picture of it, and tell me what it says.""",
        "under": "my computer keeps saying it needs to update",
        "clarify": "Updates help keep your computer working well and safe. Is your computer a **Windows** computer or a **Mac**?",
        "answer": "Windows 11",
        "d_open": "Thanks. Here's how to install the updates.",
        "style": "over_specified", "styled_full": True,
        "styled": "Dell Inspiron, Windows 11 Home. The little icon by the clock says updates are available. I'm comfortable with Settings, just tell me where to go.",
        "styled_open": "Sure, here's the path:",
    },
    {
        "id": "TR-035", "src": ["gphotos_backup"], "inspired": "ElderBench",
        "full": "How do I back up my photos on my Android phone so I don't lose them?",
        "steps": """You can use the **Google Photos** app to save copies of your photos to your Google Account. It takes a couple of minutes to turn on.

1. Open the **Google Photos** app.
2. Sign in to your Google Account if it asks.
3. Tap your **profile picture or initial** at the top right.
4. Tap **Photos settings**.
5. Tap **Backup**.
6. Turn **Backup** on.

Your photos will start saving to your Google Account. This can take a while if you have many photos.

Your Google storage is shared with Gmail and Google Drive, and backup stops if it fills up. Tell me if you see a storage message and we'll look at the options.""",
        "under": "how can I save my pictures so I don't lose them if I lose my phone",
        "clarify": "That's a smart thing to set up. Is your phone an **iPhone** or an **Android** phone (like Samsung or Google Pixel)?",
        "answer": "android",
        "d_open": "Great. On Android, Google Photos can do this for you.",
        "style": "verbose", "styled_full": True,
        "styled": "I dropped my old phone in the lake last summer and lost all the pictures of my granddaughter's first year. I have a new Android phone now and I don't want that to happen again.",
        "styled_open": "I'm sorry about those pictures. Let's make sure your new ones are kept safe. Google Photos can save a copy online:",
    },
    {
        "id": "TR-036", "src": ["win_printer"], "inspired": "OATS",
        "full": "I just bought a new printer. How do I add it to my Windows 11 computer?",
        "steps": """Here's how to add your new printer. It takes about five minutes.

**First:** turn the printer on. If it uses a cable, plug it into the computer. If it's wireless, make sure it's on the same Wi-Fi network as your computer.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Printers & scanners**.
4. Next to **Add a printer & scanner**, click **Add device**.
5. Wait a few minutes while the computer searches.
6. When your printer appears, click **Add device** next to it.

Some printers install by themselves after step 4.

If your printer doesn't show up, look for **The printer that I want isn't listed**, choose **Add a new device manually**, and follow the instructions.""",
        "under": "how do I set up my new printer",
        "clarify": "Congratulations on the new printer. What will you print from: a **Windows computer**, a **Mac**, or a **phone**?",
        "answer": "My Windows 11 laptop",
        "d_open": "Great, here's how to add it to your Windows 11 laptop.",
        "style": "incomplete", "styled_full": False,
        "styled": "new printer wont",
        "styled_reply": "It sounds like your message got cut off. What won't the new printer do: **turn on**, **connect**, or **print**? And what are you printing from, a computer or a phone?",
    },
]
