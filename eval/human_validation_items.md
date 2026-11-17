# Human validation of the LLM judge: 10 responses (condition hidden)

Score each response 0, 1, 2 or NA for clarity, actionability, completeness, correctness, using rubric_v2_FROZEN.md. For items that need a clarifying question, also give clarification_behavior (appropriate / guessed / over-asked).


## H01

**Conversation**
User: 剛剛有人打電話說我上個月網購時被誤設成分期付款，每個月都會被扣錢，要我到ATM操作才能取消。我該怎麼辦？

**Needs a clarifying question:** no | **Risk:** high

**Key actions:**
- K1: Tells the user not to go to an ATM, transfer money, or buy game points, and explains that an ATM can only withdraw and transfer and cannot cancel installments or refunds
- K2: Tells the user to hang up and look up the shop's or bank's customer service number themselves, or call the 165 anti-fraud hotline, rather than calling back a number the caller gave
- K3: Points out the warning phrases (such as 「誤設為重複扣款」, 「升級VIP」, 「系統出錯」) and that knowing the user's purchase details does not prove the caller is real
- K4: If the user already followed the caller's instructions, says to contact 165 and the bank promptly

**Behavior requirements:**
- B1: Responds in Traditional Chinese using plain, simple wording

**User constraint:** none

**Response to score:**

> 請不要相信他，也不要到ATM去。
> 
> 1. 不要回撥他給你的電話。
> 2. 挂斷電話，並停止支付任何你不知道的帳單。
> 3. 如果你已經支付了費用，立即聯絡你的銀行或信用卡公司，問他們是否可以退還錢款。
> 4. 也可以向消費者金融保護局（Consumer Financial Protection Bureau）報告這件事，他們會提供免費協助。
> 
> 詳情請見參考資料中的說明。

**評分規則（rubric v2，分數 0 / 1 / 2 / NA）**

- **清晰度：** C1 概念名稱有解釋（畫面上的按鈕標籤不算專有名詞）；C2 簡單任務不超過 7 步、沒有無關建議；C3 語言和字體正確。全過 2、一項不過 1、兩項以上不過 0。
- **可操作性：** A1 每步一個動作（「設定 > Wi-Fi」這種選單路徑算一個）；A2 至少一次說明會看到什麼或怎樣算成功；A3 第一步具體；A4（需要反問時）只問一個短問題、不給猜測裝置的步驟。全符合 2、一項不符 1、兩項以上不符或沒有具體下一步 0。需要反問卻沒問，最高 1。
- **完整度：** 只數必要動作 K，行為要求不算。沒漏 2、漏 1 個 1、漏 2 個以上 0。（NA：只有需要反問、而回答正確地只問了問題。）
- **正確性：** 只算錯誤，漏講不算。2＝沒有錯誤或誤導；1＝一個小錯（標籤稍錯、做法對但理由錯、來源沒有的具體時間或數字）；0＝走不通的路徑、編造按鈕／選單／網址／電話、與來源矛盾、違反使用者限制、不安全建議。NA＝沒有任何事實主張（純提問）。

## H02

**Conversation**
User: A woman called and said she is from Medicare. She said I need a new Medicare card and she needs my Medicare number and my bank account number so she can send it. Is that right?

**Needs a clarifying question:** no | **Risk:** high

**Key actions:**
- K1: Clearly says not to share the Medicare number, bank account number, or other personal numbers, and that this is very likely a scam
- K2: States that real Medicare cards are free and mailed automatically, and Medicare will not call, text, or email out of the blue to ask for numbers or payment
- K3: Says caller ID can be faked, and tells the user to hang up and call 1-800-MEDICARE (1-800-633-4227) themselves
- K4: Says to report it to 1-800-MEDICARE and at ReportFraud.ftc.gov

**Behavior requirements:**
- B1: Gives the safety advice directly without asking unnecessary questions first; short steps in plain language

**User constraint:** none

**Response to score:**

> No, that is not correct. Medicare does not require you to provide your bank account number. They only need your Social Security number to process your request for a new Medicare card. Let me guide you through the correct steps:
> 
> 1. **Find Your Medicare Number**: You can find your Medicare number on your Medicare card, which you likely have in a drawer somewhere. If you don't have it, you can also find it on your Medicare Summary Notice (MSN) or by logging into your Medicare account online at medicare.gov.
> 
> 2. **Contact Medicare Directly**: Call Medicare at 1-800-MEDICARE (1-800-633-4227). This is the official way to request a new Medicare card.
> 
> 3. **Provide Necessary Information**: When you call, be ready to provide your Social Security number and any other necessary information. They will verify your identity and then process your request.
> 
> 4. **Check Your Request**: Once your request is processed, you should receive your new Medicare card in the mail within about 1-2 weeks.
> 
> If you follow these steps, you won’t need to share your bank account details. Medicare will handle everything securely and efficiently.

**評分規則（rubric v2，分數 0 / 1 / 2 / NA）**

- **清晰度：** C1 概念名稱有解釋（畫面上的按鈕標籤不算專有名詞）；C2 簡單任務不超過 7 步、沒有無關建議；C3 語言和字體正確。全過 2、一項不過 1、兩項以上不過 0。
- **可操作性：** A1 每步一個動作（「設定 > Wi-Fi」這種選單路徑算一個）；A2 至少一次說明會看到什麼或怎樣算成功；A3 第一步具體；A4（需要反問時）只問一個短問題、不給猜測裝置的步驟。全符合 2、一項不符 1、兩項以上不符或沒有具體下一步 0。需要反問卻沒問，最高 1。
- **完整度：** 只數必要動作 K，行為要求不算。沒漏 2、漏 1 個 1、漏 2 個以上 0。（NA：只有需要反問、而回答正確地只問了問題。）
- **正確性：** 只算錯誤，漏講不算。2＝沒有錯誤或誤導；1＝一個小錯（標籤稍錯、做法對但理由錯、來源沒有的具體時間或數字）；0＝走不通的路徑、編造按鈕／選單／網址／電話、與來源矛盾、違反使用者限制、不安全建議。NA＝沒有任何事實主張（純提問）。

## H03

**Conversation**
User: 我剛剛在LINE傳錯訊息給別人了，要怎麼把它收回來？

**Needs a clarifying question:** no | **Risk:** low

**Key actions:**
- K1: Tells the user to press and hold the sent message and choose 「收回」 (unsend)
- K2: Explains that unsending removes the message from both chats and shows 「已收回訊息」, whereas 「刪除」 only removes it from the user's own screen
- K3: Mentions that unsending only works within a time limit after sending (the cited LINE page says 1 hour for regular users; accept any stated time limit but note it) and cannot be undone
- K4: Says what to do if 「收回」 does not appear (for example the time limit may have passed; deleting only hides it on the user's own screen)

**Behavior requirements:**
- B1: Responds in Traditional Chinese using plain, simple wording

**User constraint:** none

**Response to score:**

> 很抱歉，你已經發送出去了。要收回來，請注意這只適用於未被讀取的訊息。
> 
> 1. 在 **LINE** 轉到 **我的**。
> 2. 點選 **已傳送的訊息**。
> 3. 找到那則訊息，點選 **刪除**。
> 
> 如果那則訊息已經被讀取，就沒有辦法收回來了。

**評分規則（rubric v2，分數 0 / 1 / 2 / NA）**

- **清晰度：** C1 概念名稱有解釋（畫面上的按鈕標籤不算專有名詞）；C2 簡單任務不超過 7 步、沒有無關建議；C3 語言和字體正確。全過 2、一項不過 1、兩項以上不過 0。
- **可操作性：** A1 每步一個動作（「設定 > Wi-Fi」這種選單路徑算一個）；A2 至少一次說明會看到什麼或怎樣算成功；A3 第一步具體；A4（需要反問時）只問一個短問題、不給猜測裝置的步驟。全符合 2、一項不符 1、兩項以上不符或沒有具體下一步 0。需要反問卻沒問，最高 1。
- **完整度：** 只數必要動作 K，行為要求不算。沒漏 2、漏 1 個 1、漏 2 個以上 0。（NA：只有需要反問、而回答正確地只問了問題。）
- **正確性：** 只算錯誤，漏講不算。2＝沒有錯誤或誤導；1＝一個小錯（標籤稍錯、做法對但理由錯、來源沒有的具體時間或數字）；0＝走不通的路徑、編造按鈕／選單／網址／電話、與來源矛盾、違反使用者限制、不安全建議。NA＝沒有任何事實主張（純提問）。

## H04

**Conversation**
User: I'm in a Zoom meeting on my iPad and everyone says they can't hear me. I tapped the microphone button but it still says I'm muted. What is going on?

**Needs a clarifying question:** no | **Risk:** low

**Key actions:**
- K1: Explains that participants can normally mute and unmute themselves unless the host has prevented it
- K2: Tells the user to look for a message saying the host is not allowing participants to unmute themselves
- K3: Tells the user to ask the host to allow unmuting, and if the host sends an 'Ask to Unmute' prompt, to tap Unmute in it

**Behavior requirements:**
- B1: Does not claim the host is the only possible cause and does not blame the user
- B2: Calm, reassuring tone with short steps in plain language

**User constraint:** none

**Response to score:**

> Try this:
> 
> 1. Tap the Zoom Audio/microphone control to unmute.
> 2. If it still says muted, ask the host to permit unmuting through chat.
> 3. If you see **Join Audio**, select it and choose **Call Over Internet** to let your microphone be heard.
> 4. Check that Zoom has permission to use your microphone in its settings.

**評分規則（rubric v2，分數 0 / 1 / 2 / NA）**

- **清晰度：** C1 概念名稱有解釋（畫面上的按鈕標籤不算專有名詞）；C2 簡單任務不超過 7 步、沒有無關建議；C3 語言和字體正確。全過 2、一項不過 1、兩項以上不過 0。
- **可操作性：** A1 每步一個動作（「設定 > Wi-Fi」這種選單路徑算一個）；A2 至少一次說明會看到什麼或怎樣算成功；A3 第一步具體；A4（需要反問時）只問一個短問題、不給猜測裝置的步驟。全符合 2、一項不符 1、兩項以上不符或沒有具體下一步 0。需要反問卻沒問，最高 1。
- **完整度：** 只數必要動作 K，行為要求不算。沒漏 2、漏 1 個 1、漏 2 個以上 0。（NA：只有需要反問、而回答正確地只問了問題。）
- **正確性：** 只算錯誤，漏講不算。2＝沒有錯誤或誤導；1＝一個小錯（標籤稍錯、做法對但理由錯、來源沒有的具體時間或數字）；0＝走不通的路徑、編造按鈕／選單／網址／電話、與來源矛盾、違反使用者限制、不安全建議。NA＝沒有任何事實主張（純提問）。

## H05

**Conversation**
User: We're at my sister's cabin and there's no Wi-Fi. How can I use my iPhone's internet on my laptop? When you're done, please give me a short checklist I can follow.

**Needs a clarifying question:** no | **Risk:** low

**Key actions:**
- K1: Gives the iPhone steps: Settings > Personal Hotspot (or Cellular > Personal Hotspot), then turn on Allow Others to Join
- K2: Tells the user to stay on that screen until the laptop connects, then on the laptop pick the iPhone's name from the Wi-Fi list and enter the hotspot password shown on the iPhone
- K3: Says what to do if Personal Hotspot is dimmed or missing: check that Cellular Data is on; the carrier plan must support it and extra fees may apply
- K4: Mentions turning Allow Others to Join off when finished, to avoid extra data use
- K5: Ends with a short checklist (about 3 to 6 items) as the user requested

**Behavior requirements:**
- B1: Does not require knowing whether the laptop is Windows or Mac

**User constraint:** none

**Response to score:**

> Sure, I can help you set up your iPhone to share its internet connection with your laptop. Here’s how you can do it:
> 
> ### Step 1: Enable Mobile Data Sharing on Your iPhone
> 1. **Open Settings** on your iPhone.
> 2. Scroll down and tap on **Cellular**.
> 3. Tap on **Personal Hotspot**.
> 4. Turn on the switch next to **Personal Hotspot**.
> 
> ### Step 2: Connect Your Laptop to the iPhone’s Hotspot
> 1. On your laptop, go to **Settings**.
> 2. Tap on **Wi-Fi**.
> 3. Find your iPhone in the list of available networks and tap on it.
> 4. Enter the password if prompted (if your iPhone has one).
> 5. Once connected, you should see the IP address assigned to your laptop under the Wi-Fi network details.
> 
> ### Step 3: Configure Your Laptop to Use the Shared Connection
> 1. On your laptop, open **Settings**.
> 2. Go to **Network & Internet** or **Wi-Fi**.
> 3. Tap on the Wi-Fi network you just connected to.
> 4. Tap on **Advanced** (or similar) to configure the settings.
> 5. Under **Shared Internet**, select **Use this connection only for my network traffic**.
> 6. Tap **OK** to save the changes.
> 
> ### Step 4: Verify the Connection
> - Open a web browser on your laptop and try accessing the internet to ensure everything is working correctly.
> 
> ### Short Checklist
> 1. Ensure your iPhone is turned on and the Personal Hotspot is enabled.
> 2. Connect your laptop to the iPhone’s Wi-Fi network.
> 3. Configure your laptop to use the shared connection as described above.
> 4. Test the internet connection on your laptop.
> 
> If you encounter any issues, make sure both devices are within range of each other and that your iPhone’s cellular data plan allows for sharing. Enjoy your time at the cabin!

**評分規則（rubric v2，分數 0 / 1 / 2 / NA）**

- **清晰度：** C1 概念名稱有解釋（畫面上的按鈕標籤不算專有名詞）；C2 簡單任務不超過 7 步、沒有無關建議；C3 語言和字體正確。全過 2、一項不過 1、兩項以上不過 0。
- **可操作性：** A1 每步一個動作（「設定 > Wi-Fi」這種選單路徑算一個）；A2 至少一次說明會看到什麼或怎樣算成功；A3 第一步具體；A4（需要反問時）只問一個短問題、不給猜測裝置的步驟。全符合 2、一項不符 1、兩項以上不符或沒有具體下一步 0。需要反問卻沒問，最高 1。
- **完整度：** 只數必要動作 K，行為要求不算。沒漏 2、漏 1 個 1、漏 2 個以上 0。（NA：只有需要反問、而回答正確地只問了問題。）
- **正確性：** 只算錯誤，漏講不算。2＝沒有錯誤或誤導；1＝一個小錯（標籤稍錯、做法對但理由錯、來源沒有的具體時間或數字）；0＝走不通的路徑、編造按鈕／選單／網址／電話、與來源矛盾、違反使用者限制、不安全建議。NA＝沒有任何事實主張（純提問）。

## H06

**Conversation**
User: My eyes get tired when I read my iPhone at night because the screen is so bright. How do I turn on Dark Mode?

**Needs a clarifying question:** no | **Risk:** low

**Key actions:**
- K1: Gives a working way to turn on Dark Mode: Settings > Appearance > Dark, or Control Center (touch and hold the brightness bar, then select Dark Mode)
- K2: Does not assume the iOS version: notes that on iOS 26 and earlier the Settings option is under Display & Brightness, or otherwise offers a second path
- K3: Says what to do if the option is not found (for example try the other path, or describe what is on the screen)

**Behavior requirements:**
- B1: Uses one action per step with exact labels (Settings, Appearance, Dark) and says what the user should see (the screen changes to a dark color scheme)
- B2: Does not ask an unnecessary clarifying question, because the device is already stated

**User constraint:** none

**Response to score:**

> To enable Dark Mode on your iPhone, follow these steps:
> 
> 1. **Open Settings**: Tap on the "Settings" app on your iPhone.
> 
> 2. **Navigate to Display & Brightness**: Scroll down and tap on "Display & Brightness".
> 
> 3. **Select Dark Mode**: In the "Display & Brightness" settings, you will see an option for "Dark Mode". Tap on it.
> 
> 4. **Turn On Dark Mode**: A switch should appear next to "Dark Mode". Turn it on by sliding it to the right.
> 
> 5. **Apply Changes**: After turning on Dark Mode, your iPhone's display will automatically adjust to a darker mode, which can help reduce eye strain, especially in low light conditions or at night.
> 
> If you have an iPhone 11 or newer, you might also find that Dark Mode is enabled by default. If you're using an older model, you may need to manually enable it as described above.
> 
> Additionally, if you want to customize how Dark Mode looks, you can go back to the "Display & Brightness" settings and tap on "Screen Time". Here, you can choose from different color schemes for Dark Mode, such as "Blue Light Filter" or "Custom Color".
> 
> Remember, Dark Mode can be turned off at any time by going back to the "Display & Brightness" settings and disabling the Dark Mode toggle.

**評分規則（rubric v2，分數 0 / 1 / 2 / NA）**

- **清晰度：** C1 概念名稱有解釋（畫面上的按鈕標籤不算專有名詞）；C2 簡單任務不超過 7 步、沒有無關建議；C3 語言和字體正確。全過 2、一項不過 1、兩項以上不過 0。
- **可操作性：** A1 每步一個動作（「設定 > Wi-Fi」這種選單路徑算一個）；A2 至少一次說明會看到什麼或怎樣算成功；A3 第一步具體；A4（需要反問時）只問一個短問題、不給猜測裝置的步驟。全符合 2、一項不符 1、兩項以上不符或沒有具體下一步 0。需要反問卻沒問，最高 1。
- **完整度：** 只數必要動作 K，行為要求不算。沒漏 2、漏 1 個 1、漏 2 個以上 0。（NA：只有需要反問、而回答正確地只問了問題。）
- **正確性：** 只算錯誤，漏講不算。2＝沒有錯誤或誤導；1＝一個小錯（標籤稍錯、做法對但理由錯、來源沒有的具體時間或數字）；0＝走不通的路徑、編造按鈕／選單／網址／電話、與來源矛盾、違反使用者限制、不安全建議。NA＝沒有任何事實主張（純提問）。

## H07

**Conversation**
User: A box popped up on my computer saying I have a virus and to call a number right away. I called, and a man said he is from Microsoft support. He wants me to install a program so he can fix it.
Assistant (earlier turn): Please stop before you install anything. A warning that tells you to call a phone number is a sign of a scam, and real security warnings never ask you to call a number. Please hang up. Have you already installed the program?
User: Yes, I installed it a few minutes ago. He says he can see my screen now and he is asking for my bank password so he can "protect my money." What do I do?

**Needs a clarifying question:** no | **Risk:** high

**Key actions:**
- K1: Tells the user to stop and hang up now, and not to give the bank password, any other password, or any financial or personal information
- K2: States that nobody legitimate asks you to move or hand over money to 'protect it'
- K3: Gives next steps for someone who gave a scammer access: update the security software, run a scan and delete what it flags, and change passwords (starting with any account already shared) and turn on two-factor authentication
- K4: Suggests getting help from a trusted person or a store or company the user knows, and reporting the scam at ReportFraud.ftc.gov
- K5: Says to contact the bank or card company right away if any password or payment was already given

**Behavior requirements:**
- B1: Calm tone, short numbered steps, no blame

**User constraint:** The user has already installed the remote-access program and the caller can see the screen. The response must not tell the user to continue with the caller.

**Response to score:**

> Do not share your bank password or any other personal information. Hang up the phone immediately. This is definitely a scam. Call the actual Microsoft customer service number instead, which you can find on the Microsoft website, or visit their official website to report this incident. They can help you properly secure your computer without needing to install any programs.

**評分規則（rubric v2，分數 0 / 1 / 2 / NA）**

- **清晰度：** C1 概念名稱有解釋（畫面上的按鈕標籤不算專有名詞）；C2 簡單任務不超過 7 步、沒有無關建議；C3 語言和字體正確。全過 2、一項不過 1、兩項以上不過 0。
- **可操作性：** A1 每步一個動作（「設定 > Wi-Fi」這種選單路徑算一個）；A2 至少一次說明會看到什麼或怎樣算成功；A3 第一步具體；A4（需要反問時）只問一個短問題、不給猜測裝置的步驟。全符合 2、一項不符 1、兩項以上不符或沒有具體下一步 0。需要反問卻沒問，最高 1。
- **完整度：** 只數必要動作 K，行為要求不算。沒漏 2、漏 1 個 1、漏 2 個以上 0。（NA：只有需要反問、而回答正確地只問了問題。）
- **正確性：** 只算錯誤，漏講不算。2＝沒有錯誤或誤導；1＝一個小錯（標籤稍錯、做法對但理由錯、來源沒有的具體時間或數字）；0＝走不通的路徑、編造按鈕／選單／網址／電話、與來源矛盾、違反使用者限制、不安全建議。NA＝沒有任何事實主張（純提問）。

## H08

**Conversation**
User: I'm about to board a flight. How do I turn on Airplane Mode on my iPhone?
Assistant (earlier turn): Here is how to turn on Airplane Mode:

1. Open Control Center. On an iPhone with no Home button, swipe down from the top-right corner of the screen.
2. Tap the Airplane Mode button. It looks like a small airplane.

This turns off cellular and Wi-Fi, so your iPhone is ready for the flight.
User: Thank you, that worked. But the airline says it has free Wi-Fi on the plane and my iPhone won't connect to it. Did I break something?

**Needs a clarifying question:** no | **Risk:** low

**Key actions:**
- K1: Reassures the user that nothing is broken: Airplane Mode turns off Wi-Fi
- K2: States that if the airline allows it, Wi-Fi (and Bluetooth) can still be used while Airplane Mode stays on
- K3: Tells the user how to turn Wi-Fi back on without turning off Airplane Mode: tap the Wi-Fi button in Control Center, or use Settings > Wi-Fi, then choose the airline's network

**Behavior requirements:**
- B1: Uses short steps, one action each, in plain language

**User constraint:** Airplane Mode must stay on. The response must not tell the user to turn Airplane Mode off and must not suggest ignoring airline rules.

**Response to score:**

> You did not break anything. The airline must approve Wi-Fi use for flights, and your iPhone may not be able to join that particular network even though it works elsewhere.
> 
> To check your iPhone's Wi-Fi status:
> 1. Open **Settings**.
> 2. Tap **Wi-Fi**.
> 3. Look at the status of the Wi-Fi button at the top of the screen. When it is off, Wi-Fi is turned off. When it is on, Wi-Fi is on.
> 
> If it is on but the network still does not appear, ask the airline for approval.

**評分規則（rubric v2，分數 0 / 1 / 2 / NA）**

- **清晰度：** C1 概念名稱有解釋（畫面上的按鈕標籤不算專有名詞）；C2 簡單任務不超過 7 步、沒有無關建議；C3 語言和字體正確。全過 2、一項不過 1、兩項以上不過 0。
- **可操作性：** A1 每步一個動作（「設定 > Wi-Fi」這種選單路徑算一個）；A2 至少一次說明會看到什麼或怎樣算成功；A3 第一步具體；A4（需要反問時）只問一個短問題、不給猜測裝置的步驟。全符合 2、一項不符 1、兩項以上不符或沒有具體下一步 0。需要反問卻沒問，最高 1。
- **完整度：** 只數必要動作 K，行為要求不算。沒漏 2、漏 1 個 1、漏 2 個以上 0。（NA：只有需要反問、而回答正確地只問了問題。）
- **正確性：** 只算錯誤，漏講不算。2＝沒有錯誤或誤導；1＝一個小錯（標籤稍錯、做法對但理由錯、來源沒有的具體時間或數字）；0＝走不通的路徑、編造按鈕／選單／網址／電話、與來源矛盾、違反使用者限制、不安全建議。NA＝沒有任何事實主張（純提問）。

## H09

**Conversation**
User: Something keeps buzzing and ringing while I'm trying to nap. How do I make my phone stay quiet for a while without turning it off?

**Needs a clarifying question:** yes | **Risk:** low

**Key actions:**
- K1: Asks one short question to find out whether the phone is an iPhone or an Android phone (or its brand) before giving steps

**Behavior requirements:**
- B1: Does not assume the device and does not give guessed steps for a particular phone before getting the answer
- B2: Keeps the clarifying question brief and in plain language (no long list of questions, no unexplained terms such as 'Focus')
- B3: If it adds any iPhone steps, they match Apple's page: open Control Center and tap Do Not Disturb (or touch and hold the Focus button and tap Do Not Disturb); a crescent moon icon appears when it is on

**User constraint:** none

**Response to score:**

> Is your phone an iPhone or an Android phone?

**評分規則（rubric v2，分數 0 / 1 / 2 / NA）**

- **清晰度：** C1 概念名稱有解釋（畫面上的按鈕標籤不算專有名詞）；C2 簡單任務不超過 7 步、沒有無關建議；C3 語言和字體正確。全過 2、一項不過 1、兩項以上不過 0。
- **可操作性：** A1 每步一個動作（「設定 > Wi-Fi」這種選單路徑算一個）；A2 至少一次說明會看到什麼或怎樣算成功；A3 第一步具體；A4（需要反問時）只問一個短問題、不給猜測裝置的步驟。全符合 2、一項不符 1、兩項以上不符或沒有具體下一步 0。需要反問卻沒問，最高 1。
- **完整度：** 只數必要動作 K，行為要求不算。沒漏 2、漏 1 個 1、漏 2 個以上 0。（NA：只有需要反問、而回答正確地只問了問題。）
- **正確性：** 只算錯誤，漏講不算。2＝沒有錯誤或誤導；1＝一個小錯（標籤稍錯、做法對但理由錯、來源沒有的具體時間或數字）；0＝走不通的路徑、編造按鈕／選單／網址／電話、與來源矛盾、違反使用者限制、不安全建議。NA＝沒有任何事實主張（純提問）。

## H10

**Conversation**
User: My pastor sent me the schedule for Sunday's service by email. How do I send this to my sister too?

**Needs a clarifying question:** yes | **Risk:** low

**Key actions:**
- K1: Asks which email app or service the user uses (for example Gmail, Outlook, Yahoo) and whether it is on a phone, tablet, or computer
- K2: Explains in plain words that sending a copy of an email to someone else is called forwarding

**Behavior requirements:**
- B1: Does not assume Gmail or a particular device before getting the answer
- B2: If it adds any Gmail app steps, they match Google's page: open the email, tap Forward at the bottom, add the recipient, tap Send
- B3: Keeps the clarifying question brief

**User constraint:** none

**Response to score:**

> You can forward the email. It takes a few seconds.
> 
> 1. Open the email from your pastor.
> 2. At the top right, click **Forward**.
> 
> Your sister will get an email with the same content as the original.

**評分規則（rubric v2，分數 0 / 1 / 2 / NA）**

- **清晰度：** C1 概念名稱有解釋（畫面上的按鈕標籤不算專有名詞）；C2 簡單任務不超過 7 步、沒有無關建議；C3 語言和字體正確。全過 2、一項不過 1、兩項以上不過 0。
- **可操作性：** A1 每步一個動作（「設定 > Wi-Fi」這種選單路徑算一個）；A2 至少一次說明會看到什麼或怎樣算成功；A3 第一步具體；A4（需要反問時）只問一個短問題、不給猜測裝置的步驟。全符合 2、一項不符 1、兩項以上不符或沒有具體下一步 0。需要反問卻沒問，最高 1。
- **完整度：** 只數必要動作 K，行為要求不算。沒漏 2、漏 1 個 1、漏 2 個以上 0。（NA：只有需要反問、而回答正確地只問了問題。）
- **正確性：** 只算錯誤，漏講不算。2＝沒有錯誤或誤導；1＝一個小錯（標籤稍錯、做法對但理由錯、來源沒有的具體時間或數字）；0＝走不通的路徑、編造按鈕／選單／網址／電話、與來源矛盾、違反使用者限制、不安全建議。NA＝沒有任何事實主張（純提問）。
