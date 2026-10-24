SPECS = [
    {
        "id": "TR-097", "src": ["and_live_caption"], "inspired": "ElderBench",
        "full": "How do I turn on Live Caption on my Android phone so I can read what people say in videos?",
        "steps": """**Live Caption** shows captions for videos and calls on your phone. It takes about a minute to turn on.

**Quick way:**
1. Press a **volume button** on the side of your phone.
2. Under the volume controls, tap **More**.
3. Tap **Live Caption**, then **Done**.

**In Settings:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Live Caption** and turn it on.

Connect to Wi-Fi the first time you use it, so your phone can download what it needs.

If you can't find **Live Caption**, search for it in Settings.""",
        "under": "I can't hear people on videos well, can my phone show the words?",
        "clarify": "Yes, many phones can show captions for what's being said. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "Android, a Pixel",
        "d_open": "Thanks. On Android, this is called Live Caption.",
        "style": "verbose", "styled_full": False,
        "styled": "My hearing isn't what it used to be and my grandkids send me videos all the time. I just nod along but I can't make out what they're saying.",
        "styled_reply": "Your phone may be able to show captions for those videos so you can read along.\n\n**Is your phone an iPhone or an Android phone?**",
    },
    {
        "id": "TR-098", "src": ["win_bigger"], "inspired": "OATS",
        "full": "How do I make just the text bigger on my Windows 11 computer?",
        "steps": """You can make the text bigger without changing anything else. It takes about a minute.

1. Click the **Start** button, then **Settings**.
2. Click **Accessibility**.
3. Click **Text size**.
4. Drag the slider to the right until the sample text is easy to read.
5. Click **Apply**.

Windows will make the text bigger everywhere.

Tip: you can also open Accessibility settings by holding the **Windows logo key** and pressing **U**.

If you want everything bigger, including pictures and buttons, there's a separate **Scale** setting under **Display**. Tell me if you'd like that instead.""",
        "under": "the writing on my computer is too small",
        "clarify": "I can help you make it bigger. Is your computer a **Windows** computer or a **Mac**? And do you want **just the text** bigger, or **everything** on the screen?",
        "answer": "Windows 11, just the text",
        "d_open": "Got it.",
        "style": "incomplete", "styled_full": False,
        "styled": "make text",
        "styled_reply": "It looks like your message got cut off. Do you want to **make text bigger**? If so, on which device: a computer or a phone?",
    },
    {
        "id": "TR-099", "src": ["ios_charging"], "inspired": "ElderBench",
        "full": "Why does my iPhone stop charging at 80% overnight? Is something wrong with it?",
        "steps": """Most likely nothing is wrong. This is usually a feature called **Optimized Battery Charging**. It holds the battery at 80% during long charges, like overnight, to slow down battery wear. Your iPhone then finishes charging around the time you usually unplug it.

A couple of other things can also stop charging at 80%:
- **Heat:** if your iPhone gets too warm, it may pause charging above 80%. Moving it to a cooler spot helps.
- **Charge limit:** on iPhone 15 and newer, a charge limit setting may be turned on. You can change it if you want a full charge.

If you need a full charge right away, tell me and I'll walk you through it.""",
        "under": "my phone won't charge all the way",
        "clarify": "Let's figure out why. Is your phone an **iPhone** or an **Android** phone? And does it stop at a certain number, like **80%**?",
        "answer": "iPhone, it always stops at 80%",
        "d_open": "Thanks, that detail helps.",
        "style": "verbose", "styled_full": True,
        "styled": "I plug in my iPhone every night before bed and when I wake up it says 80% and charging is on hold or something. I thought my charger was broken so I bought a new one but it does the same thing.",
        "styled_open": "Your charger is probably fine.",
    },
    {
        "id": "TR-100", "src": ["line_voice"], "inspired": "ElderBench",
        "full": "我打字很慢，要怎麼在LINE傳語音訊息？",
        "steps": """傳語音訊息比打字快多了，我們來試試看。

1. 打開要傳訊息的**聊天室**。
2. 點聊天室下方的**麥克風圖示**。
3. 點圓形的**錄音鍵**，開始說話。
4. 說完後，點方形的**停止鍵**。
5. 想先聽聽看可以點**播放**；不想要的話點**垃圾桶**刪除。
6. 沒問題的話，點**紙飛機圖示**傳送。

第一次用的時候，手機可能會問要不要讓 LINE 使用麥克風，請點**允許**。""",
        "under": "打字好累，有沒有比較快的方法傳訊息",
        "clarify": "有的！可以傳**語音訊息**，直接用說的。請問您是用 **LINE** 傳訊息，還是用手機的簡訊？",
        "answer": "LINE",
        "d_open": "好的，LINE 傳語音很方便。",
        "style": "verbose", "styled_full": True,
        "styled": "我眼睛不好，手指也不太靈活，每次回孫女的LINE都要打好久，她說阿嬤你可以用講的，可是我不知道要按哪裡。",
        "styled_open": "用講的確實輕鬆很多，孫女也能聽到您的聲音。做法如下：",
    },
    {
        "id": "TR-101", "src": ["ios_buttons"], "inspired": "ElderBench",
        "full": "My iPhone only vibrates when someone calls. It doesn't ring. How do I fix that?",
        "steps": """Your iPhone is probably in **Silent mode**. Here's how to check.

**If your iPhone has a small switch on the side** (above the volume buttons):
1. Look at the switch. If you see **orange**, Silent mode is on.
2. Flip the switch so the orange no longer shows.

**If your iPhone has an Action button instead** (iPhone 15 Pro and newer):
1. Press the **Action button**. By default, it turns Silent mode on and off. If it's been set to do something else, tell me and we'll check another way.

Once Silent mode is off, your phone will ring again. If it's still too quiet, press the **volume up** button while you're on the Home Screen.""",
        "under": "my phone isn't ringing, only buzzing",
        "clarify": "That usually means a silent setting is on. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "iPhone 13",
        "d_open": "Thanks. On an iPhone 13, it's usually the switch on the side.",
        "style": "incomplete", "styled_full": False,
        "styled": "phone wont ring just",
        "styled_reply": "It sounds like your phone only **vibrates** or stays **silent** when someone calls. Is that right? And is it an iPhone or an Android phone?",
    },
    {
        "id": "TR-102", "src": ["and_select_to_speak"], "inspired": "ElderBench",
        "full": "Can my Android phone read the words on the screen out loud to me?",
        "steps": """Yes, with a feature called **Select to Speak**. Setting it up takes a couple of minutes.

**Turn it on:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Select to Speak**.
4. Turn on the **Select to Speak shortcut**.

If you don't see **Select to Speak**, update the **Android Accessibility Suite** app in the Play Store.

**Use it:**
1. Start it with the shortcut: swipe up from the bottom of the screen with **two fingers**, or tap the **Accessibility button**.
2. Tap any text you want to hear.
3. To hear everything on the screen, tap **Play**.""",
        "under": "is there a way to have my phone read things to me",
        "clarify": "Most phones can. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "Android",
        "d_open": "Thanks.",
        "style": "verbose", "styled_full": False,
        "styled": "Reading long emails on my phone tires out my eyes. I'd love it if the phone could just read them to me like an audiobook.",
        "styled_reply": "Many phones can read text out loud.\n\n**Is your phone an iPhone or an Android phone?** I'll show you how to turn it on.",
    },
    {
        "id": "TR-103", "src": ["ios_reminders"], "inspired": "ElderBench",
        "full": "How do I set a reminder on my iPhone to call the pharmacy tomorrow at 10 AM?",
        "steps": """You can use the **Reminders** app. It takes about a minute.

1. Open the **Reminders** app.
2. Tap **New Reminder**.
3. Type what you want to remember, like **Call the pharmacy**.
4. Tap the **info** button (a small "i") next to it.
5. Tap **Date and Time**.
6. Choose **Custom**, pick tomorrow's date, and set the time to **10:00 AM**.
7. Tap **Done**.

Your iPhone will show a reminder at that time.

If you set a date without a time, the reminder comes at 9:00 AM by default.""",
        "under": "how do I get my phone to remind me to do something",
        "clarify": "Sure. Is your phone an **iPhone** or an **Android** phone? And what would you like to be reminded about, and when?",
        "answer": "iPhone. Call the pharmacy tomorrow at 10.",
        "d_open": "Got it.",
        "style": "verbose", "styled_full": True,
        "styled": "I keep forgetting to call in my prescription refill and then I run out. Tomorrow at 10 is when they open. Can my iPhone remind me?",
        "styled_open": "Yes, a reminder will help with that. Here's how to set it for tomorrow at 10:",
    },
    {
        "id": "TR-104", "src": ["chrome_bookmarks"], "inspired": "OATS",
        "full": "How do I bookmark a website in Chrome on my computer so I can find it again?",
        "steps": """Here's how to save it. It takes a few seconds.

1. Go to the website you want to save.
2. Click the **bookmark icon** to the right of the address bar at the top.

**To find it later:**
- If you see the **bookmarks bar** under the address bar, click the bookmark there. To show the bar, click the **More** menu (three dots), then **Bookmarks and lists**, then **Show bookmarks bar**.
- Or click **More**, then **Bookmarks and lists**, then **Bookmark Manager** to see all your bookmarks.""",
        "under": "how do I save a website so I can find it later",
        "clarify": "You can bookmark it. Which browser are you using, like **Chrome**, **Safari**, or **Edge**? And is it on a **computer** or a **phone**?",
        "answer": "Chrome on my computer",
        "d_open": "Thanks.",
        "style": "incomplete", "styled_full": False,
        "styled": "save this website",
        "styled_reply": "Sure. Do you want to **bookmark** it so you can visit again later, or **save a copy** of the page? And which browser are you using?",
    },
    {
        "id": "TR-105", "src": ["gmail_unsubscribe"], "inspired": "OATS",
        "full": "I get too many newsletter emails in Gmail. How do I unsubscribe on my computer?",
        "steps": """Gmail can unsubscribe you in a couple of clicks. It takes a few seconds per sender.

1. Go to **mail.google.com** and open an email from the sender.
2. Click **Unsubscribe** next to the sender's name at the top.
3. Click **Unsubscribe** again in the box that pops up.

If you see **Go to website** instead, that sender needs you to unsubscribe on their own site.

To see all your subscriptions at once, click **More** on the left side, then **Manage subscriptions**.

Only unsubscribe from senders you recognize. If an email looks suspicious, report it as spam instead of clicking anything in it. It can take a few days for the emails to stop.""",
        "under": "how do I stop getting so many emails",
        "clarify": "There are a few ways. Are they from **companies or newsletters** you signed up for, or from **strangers or scammers**? And which email do you use, like Gmail?",
        "answer": "Newsletters from stores. Gmail.",
        "d_open": "Thanks. For store newsletters, unsubscribing is the way to go.",
        "style": "verbose", "styled_full": True,
        "styled": "Every store I've ever bought anything from sends me emails every single day. My inbox has 4,000 unread messages and I can't find the important ones from my family. I use Gmail on my computer.",
        "styled_open": "That's a lot of clutter. Unsubscribing will stop new ones from piling up:",
    },
    {
        "id": "TR-106", "src": ["gmail_trash"], "inspired": "OATS",
        "full": "I accidentally deleted an important email in Gmail. How do I get it back? I'm on my computer.",
        "steps": """If it was deleted in the last 30 days, it should be in your **Trash**. Here's how to get it back.

1. Open **Gmail** in your web browser.
2. On the left side, click **More**, then click **Trash**.
3. Find the email and check the box next to it.
4. At the top, click **Move to**.
5. Choose **Inbox**.

The email will be back in your inbox.

Emails stay in Trash for up to 30 days. After that, they're deleted for good and can't be recovered.""",
        "under": "I deleted something by accident",
        "clarify": "Don't worry, it can often be recovered. **What did you delete** (an email, a photo, a file?), and on which device or app?",
        "answer": "An email in Gmail, on my computer",
        "d_open": "Good news: Gmail keeps deleted emails for a while.",
        "style": "incomplete", "styled_full": False,
        "styled": "deleted email from my",
        "styled_reply": "It looks like your message got cut off. Which email do you use, like **Gmail**? And was it on a **computer** or a **phone**?",
    },
    {
        "id": "TR-107", "src": ["gmail_spam"], "inspired": "OATS",
        "full": "How do I mark an email as spam in Gmail on my computer?",
        "steps": """Here's how. It takes a few seconds.

1. Open **Gmail** in your web browser.
2. Check the box next to the email.
3. Click the **Report spam** icon at the top.

The email moves to your **Spam** folder, and Google gets a copy, which helps it spot similar spam.

A couple of notes:
- If it's from a store or newsletter you signed up for, **Unsubscribe** is usually better.
- If the email is trying to **trick you into giving a password or account number**, that's phishing. Don't click any links or reply.""",
        "under": "how do I get rid of junk email",
        "clarify": "I can help. Which email do you use, like **Gmail**? And are you on a **computer** or a **phone**?",
        "answer": "Gmail on my computer",
        "d_open": "Thanks.",
        "style": "under_specified", "styled_full": False,
        "styled": "spam",
        "styled_reply": "Sure. Do you mean **spam emails**, **spam texts**, or **spam calls**? I can help with any of them.",
    },
    {
        "id": "TR-108", "src": ["ios_rotate", "ios_flashlight"], "inspired": "ElderBench",
        "full": "My iPhone screen keeps turning sideways when I'm reading in bed. How do I make it stay upright?",
        "steps": """You can lock the screen so it stays upright. It takes a few seconds.

1. Open **Control Center**: on an iPhone with Face ID, **swipe down from the top-right corner**. On an iPhone with a Home button, **swipe up from the bottom edge**.
2. Tap the **Portrait Orientation Lock** button. It has a **lock** icon.
3. Close Control Center.

Now the screen will stay upright even when you tilt the phone.

To let it turn sideways again, for example to watch a video, tap the same button.""",
        "under": "my screen keeps flipping when I lie down",
        "clarify": "You can lock the screen so it stays upright. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "iPhone",
        "d_open": "Thanks.",
        "style": "verbose", "styled_full": True,
        "styled": "I like to read the news on my iPhone lying on my side in bed, but the screen keeps flipping sideways and it drives me nuts.",
        "styled_open": "You can stop that by locking the screen upright:",
    },
    {
        "id": "TR-109", "src": ["and_rotate"], "inspired": "ElderBench",
        "full": "How do I stop my Android phone screen from turning sideways?",
        "steps": """You can turn off auto-rotate. It takes a few seconds.

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Tap **Auto-rotate screen** to turn it off.

Now the screen will stay the way it is, even when you tilt the phone.

To let it turn again, for example when watching a video, turn **Auto-rotate screen** back on.

Menu names can be a little different on some phones. If you don't see **Display & touch**, tell me what you see in Settings.""",
        "under": "screen keeps turning",
        "clarify": "You can stop it from rotating. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "Android",
        "d_open": "Thanks.",
        "style": "incomplete", "styled_full": False,
        "styled": "rotate screen",
        "styled_reply": "Sure. Do you want the screen to **stop turning sideways**, or do you want it to **turn sideways** and it won't? And is it an iPhone or an Android phone?",
    },
    {
        "id": "TR-110", "src": ["ios_force_restart"], "inspired": "ElderBench",
        "full": "My iPhone is frozen and won't respond when I touch it. What do I do?",
        "steps": """You can **force restart** it. The steps depend on your model.

**iPhone with Face ID (no Home button):**
1. Press and quickly release the **volume up** button.
2. Press and quickly release the **volume down** button.
3. Press and **hold** the **side button** until you see the **Apple logo**. This can take more than 10 seconds, so keep holding.

**iPhone 7:** press and hold the **side button** and **volume down** together until you see the Apple logo.

**iPhone 6s or older (with a Home button):** press and hold the **Home button** and the **side or top button** together for about 10 seconds, until you see the Apple logo.

If it still won't turn on, charge it for an hour and try again.""",
        "under": "my phone is stuck and won't do anything",
        "clarify": "Let's get it working again. Is it an **iPhone** or an **Android** phone? If it's an iPhone, does it have a **round Home button** below the screen?",
        "answer": "iPhone 12, no home button",
        "d_open": "Thanks. For your iPhone 12, use the first set of steps.",
        "style": "verbose", "styled_full": True,
        "styled": "I was in the middle of a FaceTime with my grandson and the screen froze on his face. Nothing I press does anything and I can't even turn it off. It's an iPhone 14.",
        "styled_open": "That's frustrating. An iPhone 14 has Face ID, so use the first set of steps:",
    },
    {
        "id": "TR-111", "src": ["ios_charging"], "inspired": "ElderBench",
        "full": "My iPhone won't charge when I plug it in. What should I try?",
        "steps": """Let's go through a few checks. This can take up to an hour, mostly waiting.

1. **Plug into a wall outlet** instead of a computer or power strip.
2. **Check the cable and adapter** for damage, like breaks or bent pins. Don't use a damaged one.
3. **Make sure everything is plugged in firmly**, or try a different outlet.
4. **Look in the charging port** on the bottom of the phone. If there's lint or dirt, carefully clear it out, then plug in firmly again.
5. **Leave it charging for 30 minutes.**
6. If it still won't turn on or only shows a battery picture, **force restart** it, then charge for another 30 minutes.

If none of this works, it may need service from Apple.

**If it stops at 80%:** that's usually a battery-saving feature, not a problem.""",
        "under": "my phone won't charge",
        "clarify": "Let's figure it out. Is your phone an **iPhone** or an **Android** phone? And does it **not charge at all**, or does it **stop partway**?",
        "answer": "iPhone, it doesn't charge at all",
        "d_open": "Thanks. Let's go through some checks.",
        "style": "incomplete", "styled_full": False,
        "styled": "charger not",
        "styled_reply": "It looks like your message got cut off. Is your charger **not working**, or is your phone **not charging**? And what kind of phone do you have?",
    },
    {
        "id": "TR-112", "src": ["tw_line_borrow"], "inspired": "GrandGuard",
        "full": "我朋友在LINE上傳訊息說他急需用錢，要跟我借兩萬，請我先匯款，說之後會還。這是真的嗎？",
        "steps": """先**不要匯款**。這很可能是詐騙：詐騙集團會先盜用別人的 LINE 帳號，再假冒成朋友來借錢，或要人幫忙代買遊戲點數。

請這樣做：
1. **直接打電話給朋友本人**，用您平常打給他的電話號碼，不要用 LINE 通話，也不要用訊息裡給的號碼。
2. 問清楚是不是他本人在借錢。
3. 如果確認是詐騙，可以提醒其他朋友，他的帳號可能被盜了。

另外提醒您：
- 不管是誰，都**不要把手機收到的簡訊驗證碼**給別人。LINE 不會請別人幫忙代收驗證碼。
- 有任何疑問，可以打 **165 反詐騙諮詢專線**。

如果您已經匯款了，請馬上告訴我，我們一起處理。""",
        "under": "朋友LINE跟我借錢，我該借嗎",
        "clarify": "先別急著匯款，我們先確認一下。請問朋友是**用什麼方式**跟您借的？是 LINE 傳**文字訊息**，還是**打電話**說的？您有跟他本人**講過電話**確認嗎？",
        "answer": "是LINE傳訊息的，他說很急，我還沒打電話問他",
        "d_open": "謝謝您告訴我。很急、又只用訊息借錢，是常見的詐騙手法。",
        "style": "verbose", "styled_full": True,
        "styled": "我那個認識三十年的老同學，今天突然在LINE上跟我說他住院缺錢，要我先轉三萬給他，說他不方便講電話。我很想幫他，但覺得怪怪的。",
        "styled_open": "您覺得怪怪的是對的。說「不方便講電話」又急著要錢，是這類詐騙常見的說法。",
    },
    {
        "id": "TR-113", "src": ["tw_invest", "tw_165"], "inspired": "GrandGuard",
        "full": "網路上有人拉我進一個股票投資群組，說老師帶單保證獲利，群組裡很多人都說賺很多，我可以跟著投資嗎？",
        "steps": """請先**不要投錢**。您說的情況和**假投資詐騙**非常像。

常見的手法是這樣：
1. 先在網路上認識您，再拉您進 **LINE 投資群組**。
2. 群組裡有很多人說自己賺了很多錢，其實很多是詐騙集團安排的人。
3. 一開始讓您**小賺一點**，讓您相信。
4. 再叫您下載 APP、投入**更多錢**。
5. 等您想把錢領出來，就用各種理由拒絕，例如要先繳保證金。

**請記住：**
- 「**保證獲利**」、「**穩賺不賠**」就是詐騙。
- 不要下載對方給的投資 APP。
- 可以到 **165 全民防騙網**查詢這個 LINE ID 或網站；合法的投資管道可以到**投信投顧公會網站**查。

有疑問可以打 **165 反詐騙諮詢專線**。如果已經投了錢，請告訴我，我們一起想辦法。""",
        "under": "有人找我投資，說可以賺很多，可以相信嗎",
        "clarify": "先別急著投錢，我們一起看看。請問對方是**怎麼認識的**？是不是**網路上認識**，或拉您進 **LINE 群組**？他有說**保證賺錢**嗎？",
        "answer": "是網路上認識的，把我拉進LINE群組，說保證獲利",
        "d_open": "謝謝您告訴我，這些都是警訊。",
        "style": "incomplete", "styled_full": False,
        "styled": "投資群組",
        "styled_reply": "請問您是想問某個**投資群組可不可信**嗎？可以告訴我您是怎麼加入的、對方要您做什麼嗎？",
    },
    {
        "id": "TR-114", "src": ["tw_shopping"], "inspired": "GrandGuard",
        "full": "我在臉書上看到有人賣名牌包，價格只有專櫃的三分之一，賣家叫我加LINE私下匯款，可以買嗎？",
        "steps": """建議**不要買**，也不要匯款。這有好幾個**假網拍詐騙**的特徵：

- 價格**明顯比市價低很多**。
- 賣家要您**加 LINE 私下交易**、先匯款。

假網拍常見的結果是：付了錢卻收不到東西，或是收到很差的東西，而且私下交易出問題時很難求助。

**比較安全的做法：**
1. 選擇**信譽好的商家**，或用有**第三方支付**保障的購物平台。
2. 可以的話，**面交**驗貨再付錢。
3. 看看賣家粉絲專頁**成立多久、粉絲多不多**，太新、人太少要特別小心。

如果已經匯款，請打 **165 反詐騙諮詢專線**，或告訴我，我們一起處理。""",
        "under": "網路上買東西，賣家叫我先匯款，安全嗎",
        "clarify": "我們一起看看。請問是在**哪裡**看到的？是在購物平台上，還是臉書、LINE 這類地方？價格有沒有**特別便宜**？",
        "answer": "在臉書上看到的，比外面便宜很多，賣家要我加LINE匯款",
        "d_open": "謝謝您告訴我，這幾點都很需要小心。",
        "style": "verbose", "styled_full": False,
        "styled": "我想在網路上買東西給孫子當生日禮物，可是怕被騙。",
        "styled_reply": "先問清楚是好的。請問您是想在**哪個網站或平台**買？賣家要您**怎麼付錢**？告訴我之後，我可以幫您看看安不安全。",
    },
    {
        "id": "TR-115", "src": ["tw_gov", "tw_165_faq"], "inspired": "GrandGuard",
        "full": "有人打電話說他是警察，說我的身分被冒用涉及洗錢案，要我配合監管帳戶，而且說偵查不公開不能告訴家人。我該怎麼辦？",
        "steps": """請**馬上掛電話**，這是**假冒公務員（假檢警）詐騙**。

您聽到的幾個說法都是詐騙的關鍵字：
- 「身分**被冒用**」
- 「涉及**洗錢**」
- 「**偵查不公開**，不能告訴家人」
- 「配合**監管帳戶**」

**請記住：**
- 警察**不會在電話裡做筆錄**。
- 檢察官、警察辦案時，會用**通知書**請您到案說明，不會要您在電話中處理財產或監管帳戶。

**接下來可以這樣做：**
1. 掛掉電話，不要提供任何帳戶或個人資料。
2. 如果不放心，**自己查那個機關的官方電話**打過去確認，不要回撥對方給的號碼。
3. **告訴家人**。詐騙集團叫您保密，就是怕被家人識破。
4. 有疑問可以打 **165 反詐騙諮詢專線**。

如果已經轉帳或交出存摺、金融卡，請馬上告訴我。""",
        "under": "有人打電話說他是警察，要我配合調查",
        "clarify": "先別緊張，我們一起確認。請問對方**要您做什麼**？例如提供帳戶資料、轉帳、配合**監管帳戶**，或叫您**不要告訴家人**？",
        "answer": "他說我涉及洗錢，要我配合監管帳戶，還說不能告訴家人",
        "d_open": "謝謝您告訴我。這些都是典型的詐騙說法。",
        "style": "incomplete", "styled_full": False,
        "styled": "地檢署打來說",
        "styled_reply": "您的訊息好像沒打完。請問「地檢署」打來說了什麼？有沒有要您**轉帳**、**提供帳戶**，或**不要告訴家人**？先不要照做，我們一起確認。",
    },
    {
        "id": "TR-116", "src": ["tw_165_faq", "tw_165"], "inspired": "GrandGuard",
        "full": "我被詐騙了，要怎麼報案？可以打165嗎？",
        "steps": """很遺憾發生這種事，您願意報案是對的。可以這樣做：

**打電話：**
- 撥打 **165 反詐騙諮詢專線**。
- 用**市話**撥打免費；用**手機**撥打，中華電信門號免費，其他電信業者每分鐘新臺幣 1 元。

**網路報案：**
1. 到 **165 全民防騙網**的首頁。
2. 點**我要報案**，可以先在網路上填寫資料。
3. 之後會有專人幫您轉給方便前往的派出所，完成後續的手續。

**先準備好這些資料會比較快：** 對方的電話、LINE ID、網址、匯款紀錄或收據、對話截圖。

如果有匯款，請也**馬上聯絡您的銀行**。""",
        "under": "我好像被騙了怎麼辦",
        "clarify": "別慌，我陪您一步一步處理。請問您**已經匯款或給出個人資料**了嗎？是怎麼被騙的（電話、LINE、網路購物）？",
        "answer": "我已經匯了一萬塊，是網路買東西",
        "d_open": "謝謝您告訴我。現在最重要的是趕快報案，也要聯絡銀行。",
        "style": "verbose", "styled_full": True,
        "styled": "我前天在網路上買了一台電鍋，錢匯過去之後賣家就不見了，LINE也封鎖我，我兒子說要報案，可是我不知道要去哪裡報。",
        "styled_open": "很遺憾遇到這種事。您兒子說得對，趕快報案比較好。可以這樣做：",
    },
]
