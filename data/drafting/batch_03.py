SPECS = [
    {
        "id": "TR-057", "src": ["and_install_app"], "inspired": "ElderBench",
        "full": "How do I install an app on my Android phone? My doctor's office wants me to download their app.",
        "steps": """You can get it from the **Play Store**. It takes a couple of minutes.

1. Open the **Play Store** app.
2. Tap the search bar and type the app's name.
3. Tap the app in the results. Check that the name and maker are what you expected. The star rating and number of downloads are shown under the title.
4. Tap **Install**. (If you see a price instead, it's a paid app.)
5. When it's finished, open the app from the Play Store or find it with your other apps.

It's safest to get apps from the Play Store, because Google checks them for harmful software. Avoid installing apps from links in texts or emails.""",
        "under": "how do I get an app on my phone",
        "clarify": "I can help. Is your phone an **iPhone** or an **Android** phone? And which app are you looking for?",
        "answer": "Android. It's the app for my doctor's office.",
        "d_open": "Thanks. If you don't have the app's exact name, ask the office for it. Then:",
        "style": "verbose", "styled_full": True,
        "styled": "My neighbor told me there's an app that shows when the bus is coming, and I'd like to try it. I've never downloaded an app myself. My phone is a Samsung Galaxy.",
        "styled_open": "That sounds handy. Ask your neighbor for the app's exact name, then follow these steps:",
    },
    {
        "id": "TR-058", "src": ["ios_delete_app", "ios_storage"], "inspired": "ElderBench",
        "full": "How do I delete an app I don't use anymore from my iPhone?",
        "steps": """Here's how. It takes a few seconds.

1. Find the app on your Home Screen.
2. **Press and hold** the app's icon until a menu appears.
3. Tap **Remove App**.
4. Tap **Delete App**.
5. Tap **Delete** to confirm.

If the icons start to jiggle instead of showing a menu, tap the **minus** sign on the app's corner, tap **Delete**, then tap **Done**.

Deleting an app also removes its data from your phone. If you might want it later, you can download it again from the App Store.""",
        "under": "how do I get rid of an app",
        "clarify": "Sure. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "iphone",
        "d_open": "Thanks.",
        "style": "incomplete", "styled_full": False,
        "styled": "delete app",
        "styled_reply": "Sure, I can help you delete an app. Is it on an **iPhone**, an **Android** phone, or a **computer**?",
    },
    {
        "id": "TR-059", "src": ["play_delete_app", "and_storage"], "inspired": "ElderBench",
        "full": "How do I uninstall an app on my Android phone?",
        "steps": """You can remove it through the Play Store. It takes about a minute.

1. Open the **Play Store** app.
2. Tap your **profile icon** at the top right.
3. Tap **Manage apps & device**.
4. Tap **Manage**.
5. Tap the app you want to remove.
6. Tap **Uninstall**.

If you change your mind later, you can reinstall it from the Play Store without paying again.""",
        "under": "my phone has apps I never use, can I get rid of them",
        "clarify": "Yes, you can remove them. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "Android",
        "d_open": "Thanks. Here's one way that works on most Android phones.",
        "style": "verbose", "styled_full": True,
        "styled": "When I bought my Android phone the store guy put a bunch of games and things on it that I'll never use, and they keep sending me notifications. How do I take them off?",
        "styled_open": "You can remove most of them. Some apps that came built into the phone can only be turned off, not deleted, but most apps can be removed like this:",
    },
    {
        "id": "TR-060", "src": ["win_uninstall"], "inspired": "OATS",
        "full": "How do I uninstall a program from my Windows 11 computer?",
        "steps": """Here's how. It takes a minute or two.

1. Click the **Start** button, then click **Settings**.
2. Click **Apps**.
3. Click **Installed apps**.
4. Find the program in the list.
5. Click the **three dots** next to it, then click **Uninstall**.
6. Confirm, and follow any instructions that appear.

**Another way:** click **Start**, then **All apps**, right-click the program, and choose **Uninstall**.""",
        "under": "how do I remove a program from my computer",
        "clarify": "I can help. Is your computer a **Windows** computer or a **Mac**?",
        "answer": "Windows 11",
        "d_open": "Thanks.",
        "style": "over_specified", "styled_full": True,
        "styled": "Windows 11 Home, HP laptop. There's an old program called PhotoEasy that came preinstalled. I want it gone. Settings or Control Panel?",
        "styled_open": "Settings is the easiest place on Windows 11. If PhotoEasy doesn't appear there, open **Control Panel** and use **Programs and Features** instead.",
    },
    {
        "id": "TR-061", "src": ["ios_storage"], "inspired": "ElderBench",
        "full": "My iPhone says storage is almost full. How do I free up space?",
        "steps": """Let's see what's using the space first. This takes a few minutes.

1. Open the **Settings** app.
2. Tap **General**.
3. Tap **iPhone Storage**.
4. At the top, look at the **recommendations**. Tap one to see what it would remove, or tap **Show All** to see more.
5. Below that is a list of your apps. Tap an app to see your choices:
   - **Offload App** removes the app but keeps your documents and data, so nothing is lost if you reinstall it.
   - **Delete App** removes the app and its data.

Offloading apps you rarely use is a safe place to start.""",
        "under": "my phone says it's full",
        "clarify": "I can help you free up some space. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "iPhone 11",
        "d_open": "Thanks.",
        "style": "verbose", "styled_full": False,
        "styled": "I wanted to take pictures at my grandson's graduation but my phone said not enough storage. I don't understand, I don't have that many things on it.",
        "styled_reply": "That's frustrating, especially at a big moment. Photos, videos, and apps can fill up space faster than you'd expect.\n\n**Is your phone an iPhone or an Android phone?** Then I'll show you how to see what's using the space.",
    },
    {
        "id": "TR-062", "src": ["and_storage"], "inspired": "ElderBench",
        "full": "How do I free up storage space on my Android phone?",
        "steps": """Here's how to see what's using space and clear some out. It takes a few minutes.

1. Open the **Settings** app.
2. Tap **Storage**. You'll see which kinds of files use the most space.
3. Tap **Free up space**.
4. Choose a category, then tap **Select files**.
5. Select the files you don't need.
6. Tap **Move files to Trash**.

**Other ways to save space:**
- If your photos are backed up in **Google Photos**, you can delete the copies on your phone. The backed-up copies stay safe in the app.
- Uninstall apps you don't use. You can reinstall them later without paying again.

Menu names vary between phones, and some of these steps need a newer version of Android. Tell me what you see if something doesn't match.""",
        "under": "phone says storage full",
        "clarify": "I can help you clear some space. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "Android, Samsung",
        "d_open": "Thanks. Samsung menus can look a little different, so tell me if something doesn't match.",
        "style": "incomplete", "styled_full": False,
        "styled": "how do i clear",
        "styled_reply": "It looks like your message got cut off. What would you like to clear: **storage space** on your phone, your **notifications**, or something else?",
    },
    {
        "id": "TR-063", "src": ["ios_flashlight"], "inspired": "ElderBench",
        "full": "How do I turn on the flashlight on my iPhone?",
        "steps": """There are a few quick ways.

**From Control Center:**
1. If your iPhone has Face ID (no Home button), **swipe down from the top-right corner** of the screen. If it has a Home button, **swipe up from the bottom edge**.
2. Tap the **Flashlight** button.
3. Tap it again to turn it off.

**From the Lock Screen:** press and hold the **Flashlight** button in the bottom-left corner.

**With Siri:** say "Hey Siri, turn on my flashlight." """,
        "under": "how do I turn on the light on my phone",
        "clarify": "Do you mean the **flashlight**? Sure. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "Yes the flashlight. iPhone.",
        "d_open": "Got it.",
        "style": "verbose", "styled_full": False,
        "styled": "I was trying to find my keys in my purse last night and my husband said use your phone light but I couldn't figure out how.",
        "styled_reply": "Your phone has a flashlight, and it's handy for things like that.\n\n**Is your phone an iPhone or an Android phone?** Then I'll show you the quickest way.",
    },
    {
        "id": "TR-064", "src": ["and_quick_settings"], "inspired": "ElderBench",
        "full": "How do I turn on the flashlight on my Android phone?",
        "steps": """Here's the quickest way.

1. **Swipe down** from the top of the screen. You'll see a few quick settings. Swipe down again to see all of them.
2. Tap **Flashlight**. A dimmed icon means it's off.
3. Tap it again to turn it off.

**If you don't see Flashlight:**
1. Swipe down twice from the top of the screen.
2. Tap the **edit** icon (a pencil).
3. Scroll down, find **Flashlight**, and tap **Add**.
4. Drag it to where you want it.""",
        "under": "where is the flashlight",
        "clarify": "I can show you. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "Android",
        "d_open": "Thanks.",
        "style": "over_specified", "styled_full": True,
        "styled": "Samsung A15. I know it's somewhere in the pull-down menu but I only see Wi-Fi, Bluetooth, and a few others.",
        "styled_open": "You're in the right place. Swipe down a second time to see more, and if it's still not there, you can add it:",
    },
    {
        "id": "TR-065", "src": ["line_security", "tw_line_borrow"], "inspired": "GrandGuard",
        "full": "聽說很多人的LINE被盜用，我要怎麼保護我的LINE帳號？",
        "steps": """做幾個設定，就能讓帳號安全很多。

1. **設定一組好密碼**：不要用生日、電話這種容易被猜到的密碼，也不要跟其他網站用一樣的密碼。
   修改密碼的位置：**主頁** → **設定**（齒輪圖示）→ **我的帳號** → **密碼**。
2. **開啟雙重認證**：在**我的帳號**裡，開啟**網頁登入雙重認證**。
3. **保護綁定的電子信箱**：如果 LINE 綁的是 Gmail 等信箱，那個信箱的密碼也要設得安全。
4. **驗證碼絕對不要給別人**：LINE 不會請別人幫您代收簡訊驗證碼。如果有人（就算是朋友）傳訊息要您的驗證碼，一定是詐騙。

如果發現帳號怪怪的，例如出現您沒傳過的訊息，請先馬上**改密碼**，再告訴我，我幫您一步一步處理。""",
        "under": "LINE要怎麼設定比較安全",
        "clarify": "可以的！請問您是想**防止帳號被別人盜用**，還是想**避免陌生人加您好友或傳訊息**？",
        "answer": "防止被盜用",
        "d_open": "好的，防止被盜用可以這樣做：",
        "style": "verbose", "styled_full": True,
        "styled": "我朋友的LINE上個月被盜了，盜他帳號的人還傳訊息跟大家借錢，我好怕我的也被盜，我年紀大了這些設定都不太懂。",
        "styled_open": "您朋友遇到的事真的很常見。不用擔心，我們一步一步來設定：",
    },
    {
        "id": "TR-066", "src": ["ios_alarm"], "inspired": "ElderBench",
        "full": "How do I set an alarm on my iPhone for 6:30 in the morning?",
        "steps": """Here's how. It takes about a minute.

1. Open the **Clock** app.
2. Tap **Alarms** at the bottom.
3. Tap the **plus (+)** button.
4. Set the time to **6:30 AM**.
5. If you want it every day, tap **Repeat** and choose the days.
6. Tap **Save** (on some versions, **Done**).

The alarm will ring even if your phone is on Silent or Do Not Disturb.

If the alarm is too quiet, go to **Settings**, then **Sounds & Haptics**, and drag the **Ringtone and Alerts** slider to the right. If it only vibrates, check that the alarm's **Sound** isn't set to **None**.""",
        "under": "how do I set an alarm to wake me up",
        "clarify": "Sure. Is your phone an **iPhone** or an **Android** phone, and what time would you like to wake up?",
        "answer": "iPhone, 6:30 in the morning",
        "d_open": "Got it. Here's how to set it for 6:30.",
        "style": "verbose", "styled_full": True,
        "styled": "I have a doctor's appointment early tomorrow and I'm worried I'll oversleep. I usually wake up on my own but I can't risk it. I need to be up at 6:30. I have an iPhone.",
        "styled_open": "Good idea to set one. Here's how to make sure you're up at 6:30:",
    },
    {
        "id": "TR-067", "src": ["and_alarm"], "inspired": "ElderBench",
        "full": "How do I set an alarm on my Android phone?",
        "steps": """Here's how, using the **Clock** app. It takes about a minute.

1. Open the **Clock** app.
2. Tap **Alarm**.
3. Tap **Add**.
4. Set the time. On a round clock face, drag the hand to the hour, then to the minutes. Choose **AM** or **PM**.
5. Tap **OK**.

Make sure your alarm volume isn't too low. Below about 30%, you might not hear it.

If you set more than one alarm, leave at least 5 minutes between them.""",
        "under": "need an alarm for tomorrow",
        "clarify": "I can help you set one. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "Android",
        "d_open": "Thanks.",
        "style": "incomplete", "styled_full": False,
        "styled": "alarm for 7",
        "styled_reply": "Sure. Do you mean **7 in the morning** or **7 in the evening**? And is your phone an iPhone or an Android phone?",
    },
    {
        "id": "TR-068", "src": ["ios_hearing"], "inspired": "ElderBench",
        "full": "I just got new hearing aids that work with iPhone. How do I connect them?",
        "steps": """Here's how to pair them. It takes a few minutes.

1. Make sure your iPhone has the latest software update.
2. Put your hearing aids in **pairing mode**. Depending on the model, you might open and close the battery doors, turn them off and on, or take them out of the charger. Your hearing aid instructions will say which.
3. On your iPhone, open **Settings**.
4. Tap **Accessibility**.
5. Tap **Hearing Devices**.
6. Tap **Pair MFi Hearing Device** if you see it, or tap your hearing aids' name when it appears. Then tap **Pair**.

If you don't see them, put them back in pairing mode and try again. Your audiologist can also help.""",
        "under": "how do I connect my hearing aids to my phone",
        "clarify": "I can help you pair them. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "iPhone",
        "d_open": "Thanks.",
        "style": "verbose", "styled_full": True,
        "styled": "My audiologist set up my new hearing aids in the office but she said I could connect them to my iPhone so phone calls go straight into my ears. I forgot to ask her how.",
        "styled_open": "That's a great feature. Here's how to connect them:",
    },
    {
        "id": "TR-069", "src": ["and_bluetooth"], "inspired": "ElderBench",
        "full": "How do I connect my new Bluetooth headphones to my Android phone?",
        "steps": """Here's how. It takes a couple of minutes.

1. Put your headphones in **pairing mode**. Each brand does this differently, so check the instructions that came with them.
2. On your phone, **swipe down** from the top of the screen.
3. **Press and hold** the **Bluetooth** icon.
4. Tap **Pair new device**.
5. Tap the name of your headphones when it appears.
6. Follow any instructions on the screen.

If your headphones don't appear, check under **Available devices**, or tap **More** and then **Refresh**.

If you're asked for a code and don't have one, try **0000** or **1234**.""",
        "under": "how do I connect my earbuds",
        "clarify": "Sure. What are you connecting them to: an **iPhone**, an **Android** phone, or a **computer**?",
        "answer": "My Android phone",
        "d_open": "Thanks.",
        "style": "incomplete", "styled_full": False,
        "styled": "bluetooth wont",
        "styled_reply": "It looks like your message got cut off. What won't connect over Bluetooth: **headphones**, a **speaker**, a **car**, or something else? And is your phone an iPhone or an Android phone?",
    },
    {
        "id": "TR-070", "src": ["ios_low_power"], "inspired": "ElderBench",
        "full": "How do I turn on Low Power Mode on my iPhone? I'm going out and my battery is low.",
        "steps": """Here's how. It takes a few seconds.

**Quickest way:** swipe down from the top-right corner to open **Control Center**, then tap the **battery** icon.

**In Settings:**
1. Open **Settings**.
2. Tap **Battery**.
3. On iPhone 15 and newer, tap **Power Mode**, then **Low Power Mode**. On older iPhones, turn on **Low Power Mode**.

You'll know it's on when the battery icon at the top of the screen turns **yellow**.

Low Power Mode dims the screen a little and pauses some background activity, like checking for new email. It turns off by itself once you charge above 80%.""",
        "under": "how do I make my battery last longer today",
        "clarify": "There's a battery-saving mode that can help. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "iPhone 14",
        "d_open": "Thanks. On your iPhone, it's called Low Power Mode.",
        "style": "verbose", "styled_full": False,
        "styled": "We're going to a wedding tomorrow and it'll be a long day. My phone usually dies by dinner and I want to take pictures all night.",
        "styled_reply": "A battery-saving mode can help it last longer.\n\n**Is your phone an iPhone or an Android phone?** I'll show you how to turn it on.",
    },
    {
        "id": "TR-071", "src": ["and_battery"], "inspired": "ElderBench",
        "full": "How do I turn on Battery Saver on my Android phone?",
        "steps": """Here's how. It takes less than a minute.

1. Open the **Settings** app.
2. Tap **Battery**.
3. Tap **Battery Saver** and turn it on.

You can also set it to turn on by itself on a schedule.

Battery Saver switches the screen to a dark theme and limits what apps do in the background, so your battery lasts longer.

Some phones call this something like **low power mode**. If you don't see **Battery Saver**, tell me what you see under **Battery**.""",
        "under": "my phone battery won't last the day, can I make it last longer?",
        "clarify": "Yes, a battery-saving mode can help. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "Android",
        "d_open": "Thanks.",
        "style": "over_specified", "styled_full": True,
        "styled": "Galaxy S23, battery at 40%, I need it until 10pm tonight. I'd like to turn on whatever the power saving setting is.",
        "styled_open": "Here's how to turn it on. Menu names on Samsung phones can differ a little:",
    },
    {
        "id": "TR-072", "src": ["ios_app_updates"], "inspired": "ElderBench",
        "full": "How do I update the apps on my iPhone?",
        "steps": """Here's how to update them all at once. It takes a few minutes.

1. Open the **App Store**.
2. Tap your **profile picture** (or the account icon) at the top of the screen.
3. Tap **App Updates**.
4. Tap **Update All**, or tap **Update** next to just one app.

**To have apps update by themselves:**
1. Open **Settings**.
2. Tap **Apps**, then **App Store**.
3. Turn on **App Updates**.""",
        "under": "my banking app says I need to update it",
        "clarify": "Updating the app is usually quick. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "iPhone",
        "d_open": "Thanks. Open the App Store from your Home Screen, not from a link in a message, then:",
        "style": "incomplete", "styled_full": False,
        "styled": "update apps on",
        "styled_reply": "It looks like your message got cut off. Which device do you want to update apps on: an **iPhone**, an **Android** phone, or a **computer**?",
    },
    {
        "id": "TR-073", "src": ["and_magnification"], "inspired": "ElderBench",
        "full": "Is there a way to zoom in on my Android phone's screen to read small things?",
        "steps": """Android has a **Magnification** feature. Setting it up takes a couple of minutes.

**Turn it on:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Magnification**.
4. Turn on the **Magnification shortcut**. You can choose how to start it: the **Accessibility button** on the screen, **pressing both volume keys**, or **triple-tapping** the screen.

**Use it:**
1. Start magnification with your shortcut.
2. **Pinch** with two fingers to zoom in or out.
3. **Drag with two fingers** to move around.
4. Use the shortcut again to stop.

It can zoom up to 8 times.""",
        "under": "can I zoom in on my phone screen",
        "clarify": "Yes, most phones can. Is yours an **iPhone** or an **Android** phone?",
        "answer": "Android",
        "d_open": "Thanks.",
        "style": "verbose", "styled_full": True,
        "styled": "The print on my medicine reminder app is so tiny, and making the text bigger messes up how the app looks. My Android phone is a Pixel.",
        "styled_open": "Magnification is a good fit for that: it zooms in only when you need it and doesn't change how the app looks the rest of the time.",
    },
    {
        "id": "TR-074", "src": ["ios_find_my"], "inspired": "GrandGuard",
        "full": "I can't find my iPhone. I think I left it at a restaurant. How do I find it?",
        "steps": """Let's try to find it. You'll need another device or a computer.

**Option 1: another Apple device**
1. Open the **Find My** app and tap **Devices**.
2. Select your iPhone to see it on a map.
(A family member's iPhone also works if you're in the same Family Sharing group.)

**Option 2: a computer**
1. Go to **icloud.com/find** and sign in with your Apple Account.
2. Select your iPhone under **All Devices**.

From there you can **play a sound** to help find it nearby, or turn on **Lost Mode**. Lost Mode locks your phone and shows a message with a number where you can be reached.

Stay safe: Apple will never contact you to say your iPhone has been found. Don't share your passcode or any codes with anyone who calls or texts about your phone.""",
        "under": "I lost my phone",
        "clarify": "I'm sorry, that's stressful. Let's try to find it. Is your phone an **iPhone** or an **Android** phone? And do you have another device or a computer you can use right now?",
        "answer": "iPhone. I'm on my laptop now.",
        "d_open": "Good, your laptop will work.",
        "style": "verbose", "styled_full": True,
        "styled": "I left the grocery store and when I got home my iPhone wasn't in my bag. My husband has an iPhone too. I'm panicking a little.",
        "styled_open": "Take a breath. There's a good chance you can find it, and your husband's iPhone may help if you're both in the same Family Sharing group.",
    },
    {
        "id": "TR-075", "src": ["and_find_hub"], "inspired": "GrandGuard",
        "full": "I lost my Android phone. How can I find it?",
        "steps": """You can look for it with **Find Hub** from another device. It works if your phone is on and connected to the internet.

1. On another Android phone, open the **Find Hub** app. On a computer, go to **google.com/android/find**.
2. Sign in with your Google Account.
3. Select your lost phone. You'll see where it is on a map.

Then choose what to do:
- **Play sound:** your phone rings loudly for 5 minutes, even if it's on silent.
- **Mark as lost:** locks your phone and lets you show a message and a contact number on the screen.
- **Factory reset:** erases everything on the phone. Only do this if you can't get it back, because afterward you can't find it with Find Hub.""",
        "under": "can't find my phone anywhere",
        "clarify": "Let's try to find it. Is it an **iPhone** or an **Android** phone? And do you have a computer or another phone you can use right now?",
        "answer": "Android. I can use my husband's phone.",
        "d_open": "Good, your husband's phone will work.",
        "style": "incomplete", "styled_full": False,
        "styled": "lost phone help",
        "styled_reply": "I'm sorry, let's try to find it. **Is it an iPhone or an Android phone**, and is there a computer or another phone you can use right now?",
    },
    {
        "id": "TR-076", "src": ["ios_qr"], "inspired": "ElderBench",
        "full": "How do I scan a QR code with my iPhone? The restaurant menu is a QR code.",
        "steps": """Your iPhone camera can read QR codes. It takes a few seconds.

1. Open the **Camera** app.
2. Point the camera at the QR code so it shows on the screen.
3. Tap the **link** that appears on the screen.

The restaurant's menu will open.

You can also open **Control Center** and tap **Scan Code**.

Only open QR codes you trust, like ones printed on the restaurant's own menu or table.""",
        "under": "how do i scan a QR code",
        "clarify": "Sure. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "iPhone",
        "d_open": "Thanks.",
        "style": "verbose", "styled_full": True,
        "styled": "We went to lunch and there were no paper menus, just a little black and white square on the table. My friend scanned it with her phone but I didn't know how. I have an iPhone 12.",
        "styled_open": "That square is a QR code, and your iPhone can read it with the camera. Next time, try this:",
    },
]
