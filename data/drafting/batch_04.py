SPECS = [
    {
        "id": "TR-077", "src": ["and_qr"], "inspired": "ElderBench",
        "full": "How do I scan a QR code with my Android phone's camera?",
        "steps": """Many Android phones can read QR codes with the camera. It takes a few seconds.

1. Open the **Camera** app.
2. Make sure it's in regular **photo** mode. QR scanning doesn't work in video or portrait mode. Some phones also have a **QR** option you can tap.
3. Point the camera at the QR code.
4. When a banner appears on the screen, tap it to open the link.

These steps are for Google's Camera app. Other phone brands work in a similar way but may look different. If nothing appears, tell me your phone's brand and I'll help.

Only open QR codes you trust. If a QR code asks you to pay or sign in, double-check that it's from the real business first.""",
        "under": "how do I read one of those square codes with my phone",
        "clarify": "Those are called **QR codes**, and most phones can read them with the camera. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "Android, Pixel",
        "d_open": "Thanks. Your Pixel's camera can do it.",
        "style": "incomplete", "styled_full": False,
        "styled": "qr code wont",
        "styled_reply": "It looks like your message got cut off. Is the QR code **not scanning**, or is it **opening something you didn't expect**? And is your phone an iPhone or an Android phone?",
    },
    {
        "id": "TR-078", "src": ["ios_medical_id"], "inspired": "GrandGuard",
        "full": "How do I set up Medical ID on my iPhone so paramedics can see my allergies?",
        "steps": """Medical ID lets first responders see your important health information from the Lock Screen, without your passcode. It takes about five minutes.

1. Open the **Health** app.
2. Tap **Summary** at the bottom.
3. Tap your **profile picture** at the top.
4. Tap **Medical ID**.
5. Tap **Edit**.
6. Turn on **Show When Locked** so it can be seen from the Lock Screen.
7. Tap **Add** next to a section, like **Allergies**, and type your information.
8. Tap **Done**.

**Add emergency contacts:** in Medical ID, tap **Edit** next to **Emergency Contacts**, tap the **plus** button, choose a contact, and pick how they're related to you.

Keep in mind that anyone holding your phone can see this information, so only add what you're comfortable sharing.""",
        "under": "how can I put my medical information on my phone in case of emergency",
        "clarify": "That's a really good idea. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "iPhone",
        "d_open": "Thanks. On iPhone, this is called Medical ID.",
        "style": "verbose", "styled_full": False,
        "styled": "I'm allergic to penicillin and my daughter said I should put it in my phone in case something happens.",
        "styled_reply": "Your daughter has a good idea. Phones can show emergency medical information on the lock screen so responders can see it.\n\n**Is your phone an iPhone or an Android phone?**",
    },
    {
        "id": "TR-079", "src": ["and_emergency"], "inspired": "GrandGuard",
        "full": "How do I add my emergency contacts and medical info on my Android phone?",
        "steps": """On Android, this is in the **Safety** app. It takes about five minutes.

**Medical information:**
1. Open the **Safety** app and sign in with your Google Account if asked.
2. Tap **Your info**.
3. Tap **Medical information**.
4. Tap an item, like **Allergies** or **Medications**, and type your details.

**Emergency contacts:**
1. In the Safety app, tap **Your info**, then **Emergency contacts**.
2. Tap **Add contact** and choose someone.

**Show it on the lock screen:**
- Tap **Emergency info access** and turn on **Show when locked**.

Anyone who picks up your phone can see this information, so only add what you're comfortable sharing. To view it from the lock screen, swipe up, tap **Emergency**, then **View emergency info**.""",
        "under": "how do I put an emergency contact in my phone",
        "clarify": "Good idea. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "Android",
        "d_open": "Thanks.",
        "style": "over_specified", "styled_full": True,
        "styled": "Pixel 7, Android 15. I want my husband listed as my emergency contact and my blood thinner listed under medications, visible without unlocking.",
        "styled_open": "Here's how to set up exactly that:",
    },
    {
        "id": "TR-080", "src": ["ios_notifications"], "inspired": "ElderBench",
        "full": "One of my iPhone games keeps sending me notifications. How do I turn them off?",
        "steps": """You can turn off notifications for just that app. It takes less than a minute.

1. Open the **Settings** app.
2. Tap **Apps**.
3. Find and tap the game.
4. Tap **Notifications**.
5. Turn off **Allow Notifications**.

The game will still work. It just won't send you alerts anymore.

If you don't see **Notifications** for that app, it means the app can't send notifications.""",
        "under": "how do I stop all these pop-ups on my phone",
        "clarify": "I can help. **Which app is sending them** (for example a game, a store, or the news)? And is your phone an **iPhone** or an **Android** phone?",
        "answer": "It's a solitaire game. iPhone.",
        "d_open": "Thanks. Here's how to turn off notifications for the solitaire game.",
        "style": "incomplete", "styled_full": False,
        "styled": "notifications keep",
        "styled_reply": "It looks like your message got cut off. Are notifications **popping up too often**, or have they **stopped showing up**? And which app is it?",
    },
    {
        "id": "TR-081", "src": ["and_notifications"], "inspired": "ElderBench",
        "full": "How do I stop a shopping app from sending notifications on my Android phone?",
        "steps": """You can turn them off for just that app. It takes less than a minute.

**Option 1, from Settings:**
1. Open **Settings**.
2. Tap **Notifications**, then **App notifications**.
3. Find the shopping app. If it's not in the list, open the menu at the top and choose all apps.
4. Tap the app and turn its notifications off.

**Option 2, from a notification:**
1. When a notification from the app shows up, swipe down from the top of the screen.
2. Press and hold the notification, then tap the settings icon.
3. Turn off notifications.

Menu names can vary a little on different phones.""",
        "under": "can I make an app stop bugging me",
        "clarify": "Yes, you can turn off its notifications. Which app is it, and is your phone an **iPhone** or an **Android** phone?",
        "answer": "A shopping app on my Android",
        "d_open": "Thanks.",
        "style": "verbose", "styled_full": False,
        "styled": "Ever since I bought shoes online, my phone buzzes all day with sales and coupons. I just want it to stop.",
        "styled_reply": "That sounds tiring. You can usually turn off alerts from just that store.\n\n**Are the alerts coming from an app on your phone, or are they emails or texts?** And is your phone an iPhone or an Android phone?",
    },
    {
        "id": "TR-082", "src": ["chrome_zoom"], "inspired": "OATS",
        "full": "How do I make a web page bigger in Chrome on my computer? The words are tiny.",
        "steps": """You can zoom in on the page. It takes a few seconds.

**With the mouse:**
1. Click the **More** menu (three dots) at the top right of Chrome.
2. Next to **Zoom**, click **+** to make the page bigger. Click **-** to make it smaller.

**With the keyboard:**
- Hold **Ctrl** and press **+** to zoom in, or **-** to zoom out. (On a Mac, use **Command** instead of Ctrl.)

If you want every website bigger from now on, change the default size in **Settings**, then **Appearance**, then **Page zoom**.""",
        "under": "the words on this website are too small",
        "clarify": "I can help you make them bigger. Are you on a **computer**, **phone**, or **tablet**? And if it's a computer, which browser do you use, like Chrome?",
        "answer": "Computer, Chrome",
        "d_open": "Thanks.",
        "style": "under_specified", "styled_full": False,
        "styled": "chrome zoom",
        "styled_reply": "Sure. Do you want to make **just this page** bigger, or **every website** bigger from now on?",
    },
    {
        "id": "TR-083", "src": ["win_downloads"], "inspired": "OATS",
        "full": "I downloaded a form from a website on my Windows computer. Where did it go?",
        "steps": """Files you download usually go to your **Downloads** folder. Here's how to find it.

1. Open **File Explorer**. Click the folder icon on the taskbar, or hold the **Windows logo key** and press **E**.
2. On the left side, click **Downloads**. You can also find it under **This PC**.
3. Look for your form. If the folder is sorted by date, your newest download will be near the top.

If you don't see it, tell me what the form is called or what website it came from, and we'll look together.""",
        "under": "I can't find something I downloaded",
        "clarify": "Let's find it. Did you download it on a **computer** or a **phone**? If it's a computer, is it **Windows** or a **Mac**?",
        "answer": "Windows computer",
        "d_open": "Thanks.",
        "style": "verbose", "styled_full": True,
        "styled": "My insurance company emailed me a link to download my card as a PDF and I clicked it and something happened at the bottom of the screen but then it disappeared and now I have no idea where the card is. It's a Windows computer.",
        "styled_open": "It's most likely in your Downloads folder. Here's how to find it:",
    },
    {
        "id": "TR-084", "src": ["win_easier_to_see"], "inspired": "OATS",
        "full": "How do I make the mouse pointer bigger on Windows 11? I keep losing it on the screen.",
        "steps": """You can make the pointer bigger and easier to spot. It takes about a minute.

1. Click the **Start** button, then **Settings**.
2. Click **Accessibility**.
3. Click **Mouse pointer & touch**.
4. Change the **size** to make the pointer bigger.
5. You can also change the **style** or color so it stands out more.

Try a few sizes until it's easy to find.""",
        "under": "I keep losing the arrow on my screen",
        "clarify": "That's common, and the arrow can be made bigger. Is your computer a **Windows** computer or a **Mac**?",
        "answer": "Windows 11",
        "d_open": "Thanks.",
        "style": "under_specified", "styled_full": False,
        "styled": "mouse too small",
        "styled_reply": "I can help you make the mouse pointer bigger. Is your computer a **Windows** computer or a **Mac**?",
    },
    {
        "id": "TR-085", "src": ["google_2sv", "google_recovery"], "inspired": "GrandGuard",
        "full": "How do I turn on 2-Step Verification for my Google account on my computer?",
        "steps": """2-Step Verification adds a second check when you sign in, so a password alone isn't enough to get into your account. Setting it up takes about five minutes.

1. Go to **myaccount.google.com** and sign in.
2. Click **Security & sign-in**.
3. Under **How you sign in to Google**, click **Turn on 2-Step Verification**.
4. Follow the steps on the screen.

After it's on, Google may ask you to confirm with your phone when you sign in on a new device.

**Never share these codes with anyone**, even if they say they're from Google.

If you use a work or school account, your administrator may control this setting.""",
        "under": "how do I make my email account more secure",
        "clarify": "Good question. Which email do you use, for example **Gmail**? And are you on a **computer** or a **phone**?",
        "answer": "Gmail, on my computer",
        "d_open": "Thanks. A strong next step for Gmail is turning on 2-Step Verification.",
        "style": "verbose", "styled_full": False,
        "styled": "My friend's email got hacked and sent everyone weird links. Her son told her to turn on two step something. I want to do that too so it doesn't happen to me.",
        "styled_reply": "That's a smart idea. It's called **2-Step Verification**, and most email services offer it.\n\n**Which email do you use**, for example Gmail, Yahoo, or Outlook?",
    },
    {
        "id": "TR-086", "src": ["ftc_phishing"], "inspired": "GrandGuard",
        "full": "I got an email that looks like it's from my bank saying my account is locked and I need to click a link to log in and fix it. Is it real?",
        "steps": """Please **don't click the link**. This is a common type of scam called phishing. These emails often look real, even with the bank's logo, but the link can lead to a fake website that steals your password.

**Warning signs:**
- It says your account is **locked** or has a **problem**.
- It pushes you to **click a link** or update your information.
- It uses a **general greeting** like "Dear Customer" instead of your name.

**What to do:**
1. **Don't click** any links or open attachments in the email.
2. To check your account, call your bank using the number on the **back of your card**, or go to the bank's website by typing the address yourself.
3. Forward the email to **reportphishing@apwg.org**, and report it at **ReportFraud.ftc.gov**.
4. Delete the email.

If you already clicked and typed your password, call your bank right away and change your password.""",
        "under": "I got a weird email, should I click on it?",
        "clarify": "Good thinking to check first. Please don't click anything yet. **Who does the email say it's from, and what is it asking you to do?**",
        "answer": "It says it's from my bank and my account is locked, and there's a link to log in.",
        "d_open": "Thank you. That's a very common scam pattern.",
        "style": "incomplete", "styled_full": False,
        "styled": "is this email from",
        "styled_reply": "It looks like your message got cut off. **Who does the email say it's from?** And please don't click any links in it until we check.",
    },
    {
        "id": "TR-087", "src": ["ftc_spam_text"], "inspired": "GrandGuard",
        "full": "I keep getting spam text messages. How do I report them?",
        "steps": """Reporting spam texts helps your phone company block similar messages. Here's how.

1. **Use your phone's report option.** Most phones have a way to mark a text as **junk** or **spam** right in the messaging app.
2. **Or forward it to 7726.** Copy the message and send it to **7726** (it spells SPAM on the keypad). Your phone company uses these reports.
3. **Report it to the FTC** at **ReportFraud.ftc.gov** if it's a scam.

Then delete the text.

**While you're at it:**
- **Don't click links** in unexpected texts.
- **Don't reply** with any personal information.
- **Never send** passwords, account numbers, or your Social Security number by text.""",
        "under": "what do I do about junk texts",
        "clarify": "There are a couple of things you can do. Would you like to **report** them, **block** the sender, or both? And is your phone an **iPhone** or an **Android** phone?",
        "answer": "I want to report them. Android phone.",
        "d_open": "Thanks. Reporting is a great idea.",
        "style": "verbose", "styled_full": True,
        "styled": "Every few days I get a text saying my toll bill is overdue or my account needs verifying. I never click them but I want to do something so they stop.",
        "styled_open": "Good for you for not clicking. Reporting them helps your phone company block more of these:",
    },
    {
        "id": "TR-088", "src": ["ftc_romance"], "inspired": "GrandGuard",
        "full": "I met a man online three months ago. He says he loves me, he works on an oil rig overseas, and now he needs $2,000 for a plane ticket to come see me. Should I send it?",
        "steps": """I'm glad you asked before sending anything. Please **don't send the money**. What you're describing matches a very common scam called a **romance scam**.

**Warning signs:**
- The person can't meet in person, often saying they work far away, like on an **oil rig** or in the military.
- Strong feelings grow quickly through lots of messages.
- Now there's a **need for money**, like travel costs or an emergency.

**What to do:**
1. **Don't send money or gift cards** to someone you haven't met in person.
2. **Talk to a friend or family member** you trust. People close to you can often spot things that are hard to see from the inside.
3. You can **search his photo** online to see if it appears under other names. I can show you how.
4. If it's a scam, stop contact and report it at **ReportFraud.ftc.gov** and to the website or app where you met.

If you've already sent money, contact your bank or the payment company right away and ask for a refund.""",
        "under": "my online friend needs money for an emergency, should I help?",
        "clarify": "I'm glad you asked first. A couple of questions will help me give you good advice: **Have you met this person in person?** And **how are they asking you to send the money?**",
        "answer": "No, we've only talked online for three months. He wants me to wire $2,000 for a plane ticket.",
        "d_open": "Thank you for telling me.",
        "style": "verbose", "styled_full": False,
        "styled": "I've been talking to someone special online and he's asking me for help. I don't know what to do.",
        "styled_reply": "Thank you for trusting me with this. **What kind of help is he asking for?** And have the two of you met in person?",
    },
    {
        "id": "TR-089", "src": ["ftc_gov_impersonation"], "inspired": "GrandGuard",
        "full": "A caller said he's from Social Security and my number has been suspended because of a crime. He wants me to buy gift cards to fix it. What should I do?",
        "steps": """Please **hang up and don't pay anything**. This is a scam. The real Social Security Administration **won't threaten you, won't suspend your Social Security number, and won't ask you to pay with gift cards**. Your benefits are not being cut off.

**What to do:**
1. **Hang up.** Don't share any personal or bank information.
2. Don't trust caller ID. Scammers can make it show a government name or number.
3. If you're worried, **call Social Security yourself** using the phone number on its official website, not a number the caller gave you.
4. **Report the call** to the Social Security Administration's Office of the Inspector General and to the FTC at **ReportFraud.ftc.gov**.

If you already shared your Social Security number or bank details, go to **IdentityTheft.gov** for next steps, and tell me so I can help.""",
        "under": "Got a call from the government saying I owe money. Is that real?",
        "clarify": "Let's check before you do anything. **Which agency did they say they were from, and how did they want you to pay?**",
        "answer": "Social Security. They said I need to buy gift cards or my number will be suspended.",
        "d_open": "Thank you. That's a scam.",
        "style": "incomplete", "styled_full": False,
        "styled": "social security called me",
        "styled_reply": "Okay, let's make sure it was really them. **What did the caller say, and did they ask you for money or personal information?**",
    },
    {
        "id": "TR-090", "src": ["ftc_passwords"], "inspired": "GrandGuard",
        "full": "How do I make a strong password that I can actually remember?",
        "steps": """A good trick is to use a **passphrase**: several random words strung together. It's long, which makes it strong, but it's easier to remember than a jumble of symbols.

**Tips for a strong password:**
1. **Make it long**, at least 12 characters. Several random words work well.
2. **Use a different password for each account**, so if one is stolen, the others stay safe.
3. **Avoid famous quotes or song lyrics**, because hacking programs can guess them.
4. **Consider a password manager.** It can create and remember strong passwords for you, and many web browsers have one built in.
5. **Turn on two-step verification** where you can, so a stolen password alone isn't enough to get in.

Your **email** password is the most important one to protect, since password reset links usually go there.""",
        "under": "Can you help me with my passwords?",
        "clarify": "Of course. What would you like help with: **making a strong new password**, **keeping track of the ones you have**, or **resetting one you forgot**?",
        "answer": "Making a strong new one that I can remember.",
        "d_open": "Sure.",
        "style": "verbose", "styled_full": True,
        "styled": "I use my dog's name and my birthday for everything because that's the only way I remember. My grandson says that's not safe. What should I do instead?",
        "styled_open": "Your grandson is right that one easy-to-guess password everywhere is risky. The good news is there are safer options that are still easy to remember.",
    },
    {
        "id": "TR-091", "src": ["maps_directions"], "inspired": "ElderBench",
        "full": "How do I get directions to my doctor's office in Google Maps on my Android phone?",
        "steps": """Here's how. It takes about a minute.

1. Open the **Google Maps** app.
2. Tap the search bar and type the address or name of the place.
3. Tap the correct result.
4. Tap **Directions** at the bottom left.
5. Choose how you're traveling: **driving**, **transit**, or **walking**.
6. Pick a route. The best route is shown in **blue**, and other options are gray.

If you're starting from where you are now, Maps can give turn-by-turn directions as you go. To see the list of turns before you leave, tap **Preview**.""",
        "under": "how do I find my way to a new place",
        "clarify": "I can help. Do you have **Google Maps** or another maps app on your phone? And is your phone an **iPhone** or an **Android** phone?",
        "answer": "Android, Google Maps",
        "d_open": "Great.",
        "style": "incomplete", "styled_full": False,
        "styled": "directions to",
        "styled_reply": "It looks like your message got cut off. **Where would you like to go?** And will you be driving, taking transit, or walking?",
    },
    {
        "id": "TR-092", "src": ["tw_invest", "tw_165"], "inspired": "GrandGuard",
        "full": "有人在LINE上加我，說可以帶我投資賺錢，我要怎麼查這個LINE ID是不是詐騙？",
        "steps": """先不要回他，也不要匯款，我們先查清楚。

**查詢的方法：**
1. 到 **165 全民防騙網**，可以查詢已知的**詐騙 LINE ID**、**假投資網站**和**詐騙電話**。
2. 也可以加入 **「165防騙宣導」LINE 官方帳號**來查詢。
3. 如果是投資，可以到**投信投顧公會網站**查詢是不是合法的投資管道。

**提醒您：**
- 聽到「**保證獲利**」或「**穩賺不賠**」，就應該當作詐騙。
- 不要加入陌生人的投資群組，也不要下載對方給的 APP。
- 查不到這個 ID，也不代表一定安全，還是要小心。

有疑問可以打 **165 反詐騙諮詢專線**。""",
        "under": "我想查一個LINE是不是詐騙",
        "clarify": "可以的。請問這個人**跟您說了什麼**，或**要您做什麼**？例如借錢、投資，還是買東西？",
        "answer": "他說可以帶我投資股票，保證賺錢",
        "d_open": "謝謝您告訴我。「保證賺錢」是很常見的詐騙說法，我們一起來查。",
        "style": "incomplete", "styled_full": False,
        "styled": "165查詢",
        "styled_reply": "好的，請問您是想**查詢**可疑的 LINE ID、網站或電話，還是想**報案**呢？",
    },
    {
        "id": "TR-093", "src": ["zoom_join_link"], "inspired": "OATS",
        "full": "My book club meets on Zoom now and they emailed me a link. How do I join from my computer?",
        "steps": """Joining with a link is pretty simple. The first time, give yourself 5 to 10 minutes before the meeting starts.

1. Open the email and **click the Zoom link**.
2. Your web browser will open a page asking if you want to **open Zoom Meetings**.
3. Click the button to open it. Depending on your computer, it may say **Open Zoom Meetings**, **Allow**, or **Open zoom.us**.
4. The Zoom app will open and take you into the meeting.

If the link already includes the passcode, you won't need to type one.

If Zoom doesn't open, or you don't have the Zoom app yet, tell me what you see on the screen and I'll help.""",
        "under": "how do I get on a zoom call",
        "clarify": "Happy to help. Do you have a **link** to the meeting, maybe in an email or text? And will you join from a **computer**, **phone**, or **tablet**?",
        "answer": "I have a link in my email. I'll use my laptop.",
        "d_open": "Great, having the link makes it easy.",
        "style": "verbose", "styled_full": True,
        "styled": "Since my knees got bad I can't drive to my book club anymore, so the ladies started doing it on Zoom. My friend emailed me the link for Thursday but I've never done a Zoom before and I'm nervous I'll mess it up.",
        "styled_open": "You won't mess it up, and it's lovely that your book club found a way to keep you in. Here's what to do on Thursday:",
    },
    {
        "id": "TR-094", "src": ["youtube_captions"], "inspired": "ElderBench",
        "full": "How do I turn on captions for a YouTube video on my phone? I can't hear it well.",
        "steps": """Here's how. It takes a few seconds.

1. Start the video in the **YouTube** app.
2. Tap the video once so the controls appear.
3. Tap the **CC** button (closed captions) to turn captions on.
4. Tap it again if you want to turn them off.

If you don't see a **CC** button, that video doesn't have captions available.""",
        "under": "can I see the words on videos",
        "clarify": "Yes, you can turn on captions. Where are you watching: **YouTube**, another app, or on **TV**?",
        "answer": "YouTube on my phone",
        "d_open": "Great.",
        "style": "incomplete", "styled_full": False,
        "styled": "captions",
        "styled_reply": "Sure. Where would you like to turn on captions: **YouTube**, a **video call**, your **phone** in general, or somewhere else?",
    },
    {
        "id": "TR-095", "src": ["ios_icloud_backup"], "inspired": "ElderBench",
        "full": "How do I back up my whole iPhone to iCloud before I get a new phone?",
        "steps": """Here's how to make a full backup. Do this on Wi-Fi. The first backup can take a while.

1. Connect your iPhone to **Wi-Fi**.
2. Open **Settings** and tap **your name** at the top.
3. Tap **iCloud**.
4. Tap **iCloud Backup**.
5. Make sure **Back Up This iPhone** is turned on.
6. Tap **Back Up Now**.
7. Stay connected to Wi-Fi until it finishes.

When it's done, you'll see the date and time of the last backup under **Back Up Now**.

If you see a message about not enough iCloud storage, you'll need more storage before the backup can finish. Tell me and we'll look at your options.""",
        "under": "how do I make sure I don't lose anything on my phone",
        "clarify": "A backup will protect your things. Is your phone an **iPhone** or an **Android** phone?",
        "answer": "iPhone",
        "d_open": "Thanks. An iCloud backup saves a copy of your iPhone.",
        "style": "verbose", "styled_full": False,
        "styled": "My phone is getting old and my son is going to help me switch to a new one next month. I'm scared I'll lose my pictures and messages from my late husband.",
        "styled_reply": "Those are precious, and it's wise to protect them before switching. A backup saves a copy of everything.\n\n**Is your phone an iPhone or an Android phone?** Then I'll walk you through backing it up.",
    },
    {
        "id": "TR-096", "src": ["ios_sdp"], "inspired": "GrandGuard",
        "full": "What is Stolen Device Protection on iPhone and how do I turn it on?",
        "steps": """Stolen Device Protection adds extra security if someone steals your iPhone **and** knows your passcode. When your phone is away from familiar places like home or work, it requires **Face ID or Touch ID** for things like using saved passwords, and it adds a **one-hour wait** before important changes, like changing your Apple Account password.

**To turn it on:**
1. Open **Settings**.
2. Tap **Face ID & Passcode** (or **Touch ID & Passcode**).
3. Enter your passcode.
4. Tap **Stolen Device Protection** and turn it on.

It may already be on, so check first.

It needs a few things to work: a passcode, Face ID or Touch ID, two-factor authentication on your Apple Account, **Find My** turned on, and **Significant Locations** turned on in Location Services.""",
        "under": "how do I protect my iPhone if it gets stolen",
        "clarify": "Good thing to set up ahead of time. Are you asking about **protecting it before** anything happens, or **what to do now** because it's already been stolen?",
        "answer": "Before, just in case",
        "d_open": "Great. One of the best protections is called Stolen Device Protection.",
        "style": "incomplete", "styled_full": False,
        "styled": "stolen device",
        "styled_reply": "Do you mean **Stolen Device Protection**, the iPhone setting that protects your phone if it's stolen? Or has your phone **been stolen**? Let me know so I can help with the right thing.",
    },
]
