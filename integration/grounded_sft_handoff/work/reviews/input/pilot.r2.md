# Review input: pilot, round 2 (6 candidates)

## gsft-battery_saver-05
- candidate_id: gsft-battery_saver-05-v2
- conversation_sha256: 90b75967b0f58c289489aed46a4bcbb2887d07f17a44977488db9319150b59e9
- task_group: battery_saver | behavior: clarify | tags: none
- route: clarify | routed question: Is your phone a Samsung Galaxy, or another brand of Android phone?
- decision basis (writer's): The user says Android but not the brand. The Samsung Galaxy steps (Settings, Battery, Power saving) and the generic Android steps (Settings, Battery, Battery Saver) differ, so the brand must be known first.

Conversation (the model sees only the user turns, joined):
> **user:** My Android phone keeps running out of charge before the day ends. Is there a power saving setting I can use?

Passages the model sees: none (clarify route)

Source references to check:
- battery-saver-samsung-power-saving: Samsung, "Get the most out of your Galaxy phone or tablet battery" <https://www.samsung.com/us/support/answer/ANS10002534> | section: Power saving mode | applicability: Samsung Galaxy phone or tablet; the page says available screens and settings may vary by wireless service provider, software version, and model | excerpt: "apps running in the background may not receive updates or send you notifications when Power saving mode is enabled."
- battery-saver-android-manual: Google, "Get the most life from your Android device's battery" <https://support.google.com/android/answer/7664692?hl=en> | section: Stretch a low battery > Turn on battery saver mode manually | applicability: Android; the page says some of these steps work only on Android 13 and up, without saying which ones | excerpt: "Some of these steps work only on Android 13 and up."

TARGET (read only after step 2)

> Is your phone a Samsung Galaxy, or another brand of Android phone?

---

## gsft-find_downloads-02
- candidate_id: gsft-find_downloads-02-v2
- conversation_sha256: 5664a7ad39cc5985c98e7be77b80d67f770daff272716505f709e8cf899b9791
- task_group: find_downloads | behavior: direct | tags: conditional, distractor
- route: answer
- decision basis (writer's): The user states a Windows 11 laptop and asks how to reach the Downloads folder, so the Windows 11 File Explorer passages apply. The Chrome passage is the inapplicable distractor. The page says Downloads is one of the known folders in Quick access and that files can be searched from a folder like Downloads. It does not say where email attachments are saved, so the reply does not claim that.

Conversation (the model sees only the user turns, joined):
> **user:** I'm on my Windows 11 laptop. Yesterday I saved an attachment from an email, and I think it went into my Downloads folder, but I don't know how to get there. How do I find the Downloads folder and look for the file?

Passages the model sees (in this order):
- [find-downloads-win11-taskbar] platform: Windows 11 | app: File Explorer
  > On Windows 11: 1. Select File Explorer from the taskbar. 2. To find files stored inside a folder, search from a folder like Downloads.
- [find-downloads-win11-quickaccess] platform: Windows 11 | app: File Explorer
  > On Windows 11: In File Explorer, the Quick access view displays all 6 known Windows folders: Desktop, Documents, Downloads, Pictures, Music, and Videos.
- [find-downloads-chrome-menu] platform: Chrome on computer | app: Chrome
  > On Chrome on a computer: 1. At the top right, click More, then Downloads. 2. To open a file, click its name. It will open in your computer's default application for the file type.

Source references to check:
- find-downloads-win11-taskbar: Microsoft, "Find your files and apps in Windows | Microsoft Support" <https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/find-your-files-and-apps-in-windows> | section: Find your files > Search from File Explorer | applicability: Windows 11 (the page's Applies To line names Windows 11 and Windows 10) | excerpt: "To find files stored inside a folder, search from a folder like Downloads."
- find-downloads-win11-quickaccess: Microsoft, "File Explorer in Windows | Microsoft Support" <https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8> | section: Quick access | applicability: Windows 11 and Windows 10 (the page's Applies To line) | excerpt: "This view displays all 6 known Windows folders: Desktop, Documents, Downloads, Pictures, Music, and Videos."
- find-downloads-chrome-menu: Google, "Download a file - Computer - Google Chrome Help" <https://support.google.com/chrome/answer/95759?hl=en> | section: Find a list of files you've downloaded | applicability: Google Chrome on a computer | excerpt: "At the top right, click More ... and then Downloads."

TARGET (read only after step 2)

> Here is how to find your Downloads folder on your Windows 11 laptop:
> 1. Select **File Explorer** from the taskbar.
> 2. In **Quick access**, find **Downloads**. It is one of the main folders shown there.
> 3. To find your file, search from the **Downloads** folder.
> 
> If the file is not in Downloads, search from the folder where you think you saved it.

---

## gsft-gift_card_scam-01
- candidate_id: gsft-gift_card_scam-01-v2
- conversation_sha256: fed5e6afdc8815dd5c1fa74e0e69bf31e1391db78817ec63d22574a38d0fd5bf
- task_group: gift_card_scam | behavior: direct | tags: safety
- route: answer
- decision basis (writer's): The user describes a gift card payment request by phone, which the FTC passage addresses directly. Protective actions come first: do not pay, hang up, and do not share the numbers or a photo. The no-agency statement supports the refusal.

Conversation (the model sees only the user turns, joined):
> **user:** I'm on my phone right now. A man said he's from my bank's fraud department. He says I have to buy gift cards to protect my account and then read him the numbers on the back. Should I do it?

Passages the model sees (in this order):
- [gift-card-stop] platform: Any device | app: none
  > Gift card scammers don't want you to have time to think about what they're saying or talk to someone you trust. Slow down. Don't pay. It's a scam. If this happens to you, hang up. It's a scam.
- [gift-card-numbers] platform: Any device | app: none
  > Don't give them those numbers or send them a photo of the card. It's a scam.
- [gift-card-no-agency] platform: Any device | app: none
  > No real business or government agency will ever tell you to buy a gift card to pay them. Government agencies won't contact you to demand immediate payment, and they never demand payment by gift card.

Source references to check:
- gift-card-stop: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How Gift Card Scams Work | applicability: Any device; gift card payment requests | excerpt: "They don't want you to have time to think about what they're saying or talk to someone you trust. Slow down. Don't pay. It's a scam."
- gift-card-numbers: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How Gift Card Scams Work | applicability: Any device; gift card payment requests | excerpt: "Don't give them those numbers or send them a photo of the card. It's a scam."
- gift-card-no-agency: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: Companies and agencies that never ask for gift card payment | applicability: Any device | excerpt: "No real business or government agency will ever tell you to buy a gift card to pay them."

TARGET (read only after step 2)

> Slow down and don't pay. It's a scam.
> 1. Hang up.
> 2. Don't give them those numbers or send them a photo of the card.
> 
> No real business or government agency will ever tell you to buy a gift card to pay them.

---

## gsft-gift_card_scam-02
- candidate_id: gsft-gift_card_scam-02-v2
- conversation_sha256: 31f9e822112be760fffb63531afd93012ee4da85c9141d1d3406ae3707ac800b
- task_group: gift_card_scam | behavior: direct | tags: safety
- route: answer
- decision basis (writer's): The user describes a prize-claim gift card payment. The FTC passage says to slow down and not pay, to not share card numbers or a photo, and that no honest business or agency asks for gift card payment for a prize.

Conversation (the model sees only the user turns, joined):
> **user:** I'm on my computer. I got a text saying I won a free prize, but I have to buy Apple gift cards first to cover the shipping fee. Is this real?

Passages the model sees (in this order):
- [gift-card-stop] platform: Any device | app: none
  > Gift card scammers don't want you to have time to think about what they're saying or talk to someone you trust. Slow down. Don't pay. It's a scam. If this happens to you, hang up. It's a scam.
- [gift-card-prize] platform: Any device | app: none
  > No honest business or agency will ever make you buy a gift card to pay them for a prize.
- [gift-card-numbers] platform: Any device | app: none
  > Don't give them those numbers or send them a photo of the card. It's a scam.

Source references to check:
- gift-card-stop: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How Gift Card Scams Work | applicability: Any device; gift card payment requests | excerpt: "They don't want you to have time to think about what they're saying or talk to someone you trust. Slow down. Don't pay. It's a scam."
- gift-card-prize: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: Common Gift Card Scams (Scammers say you've won a prize) | applicability: Any device | excerpt: "No honest business or agency will ever make you buy a gift card to pay them for a prize."
- gift-card-numbers: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How Gift Card Scams Work | applicability: Any device; gift card payment requests | excerpt: "Don't give them those numbers or send them a photo of the card. It's a scam."

TARGET (read only after step 2)

> Slow down. Don't pay. It's a scam.
> 1. Don't pay with gift cards.
> 2. Don't give them those numbers or send them a photo of the card.
> 
> No honest business or agency will ever make you buy a gift card to pay them for a prize.

---

## gsft-gift_card_scam-03
- candidate_id: gsft-gift_card_scam-03-v2
- conversation_sha256: 64d29f7c2044458d9224a3fc5b17be83cbc787e7b81e02da42beb10854ed33c1
- task_group: gift_card_scam | behavior: constraint | tags: safety
- route: answer
- decision basis (writer's): The user is on a live call with a gift card payment demand and has a time limit. The constraint is respected by a short reply that leads with hanging up, followed by the no-numbers rule and the government-demand statement.

Conversation (the model sees only the user turns, joined):
> **user:** Someone is on the phone with me right now. They say I must buy gift cards in the next ten minutes or my benefits will stop. I can't stay on the line long and I'm scared. What do I do?

Passages the model sees (in this order):
- [gift-card-stop] platform: Any device | app: none
  > Gift card scammers don't want you to have time to think about what they're saying or talk to someone you trust. Slow down. Don't pay. It's a scam. If this happens to you, hang up. It's a scam.
- [gift-card-numbers] platform: Any device | app: none
  > Don't give them those numbers or send them a photo of the card. It's a scam.
- [gift-card-no-agency] platform: Any device | app: none
  > No real business or government agency will ever tell you to buy a gift card to pay them. Government agencies won't contact you to demand immediate payment, and they never demand payment by gift card.

Source references to check:
- gift-card-stop: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How Gift Card Scams Work | applicability: Any device; gift card payment requests | excerpt: "They don't want you to have time to think about what they're saying or talk to someone you trust. Slow down. Don't pay. It's a scam."
- gift-card-numbers: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How Gift Card Scams Work | applicability: Any device; gift card payment requests | excerpt: "Don't give them those numbers or send them a photo of the card. It's a scam."
- gift-card-no-agency: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: Companies and agencies that never ask for gift card payment | applicability: Any device | excerpt: "No real business or government agency will ever tell you to buy a gift card to pay them."

TARGET (read only after step 2)

> Hang up now. It's a scam.
> 1. Hang up.
> 2. Don't give them those numbers or send them a photo of the card.
> 
> Government agencies won't contact you to demand immediate payment, and they never demand payment by gift card.

---

## gsft-gift_card_scam-05
- candidate_id: gsft-gift_card_scam-05-v2
- conversation_sha256: 88d48932aa749c56c04cc6076d818b0755af85fd11e4190f66ca5796540f46ab
- task_group: gift_card_scam | behavior: multiturn | tags: safety
- route: answer
- decision basis (writer's): The user already gave gift card numbers and needs the reporting steps. The passage says to report to the gift card company right away, ask for money back, and tell the FTC. The conditional about missing contact information is kept.

Conversation (the model sees only the user turns, joined):
> **user:** Someone called and said I owe back taxes and must pay with gift cards today or the police will come. Is that real?
> **assistant:** It's a scam. Government agencies won't contact you to demand immediate payment, and they never demand payment by gift card. Hang up.
> **user:** I hung up, but before that I already bought two gift cards and read the numbers to them over the phone. What do I do now?

Passages the model sees (in this order):
- [gift-card-report-company] platform: Any device | app: none
  > If you gave a gift card to a scammer: Report the gift card scam to the gift card company right away. Ask for your money back. Tell the FTC at ReportFraud.ftc.gov.
- [gift-card-report-no-contact] platform: Any device | app: none
  > If you can't find the contact information or the card issuer doesn't want to talk to you, report it to the FTC.

Source references to check:
- gift-card-report-company: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: What To Do If You Gave a Gift Card to a Scammer | applicability: Any device; the person already gave a gift card to a scammer | excerpt: "Report the gift card scam to the gift card company right away."
- gift-card-report-no-contact: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How To Contact Gift Card Companies | applicability: Any device; the person cannot find the company's contact information or the card issuer does not want to talk to them | excerpt: "If you can't find the contact information or the card issuer doesn't want to talk to you, report it to the FTC."

TARGET (read only after step 2)

> Here is what to do now that the caller has the card numbers:
> 1. Report the gift card scam to the gift card company right away.
> 2. Ask the company for your money back.
> 3. Tell the FTC at **ReportFraud.ftc.gov**.
> 
> If you can't find the company's contact information, or the company won't talk to you, report it to the FTC.

---
