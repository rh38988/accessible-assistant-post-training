# Review input: pilot, round 3 (3 candidates)

## gsft-find_downloads-02
- candidate_id: gsft-find_downloads-02-v3
- conversation_sha256: bebc6783a518a9f2853480ccc66bebbec9f98572320b6f5fbeb81719b595d4bd
- task_group: find_downloads | behavior: direct | tags: distractor
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
- find-downloads-win11-quickaccess: Microsoft, "File Explorer in Windows | Microsoft Support" <https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8> | section: Restore known folders if you have unpinned them | applicability: Windows 11 and Windows 10 (the page's Applies To line) | excerpt: "This view displays all 6 known Windows folders: Desktop, Documents, Downloads, Pictures, Music, and Videos."
- find-downloads-chrome-menu: Google, "Download a file - Computer - Google Chrome Help" <https://support.google.com/chrome/answer/95759?hl=en> | section: Find a list of files you've downloaded | applicability: Google Chrome on a computer | excerpt: "At the top right, click More ... and then Downloads."

TARGET (read only after step 2)

> Here is how to find your Downloads folder on your Windows 11 laptop:
> 1. Select **File Explorer** from the taskbar.
> 2. In **Quick access**, find **Downloads**. It is one of the main folders shown there.
> 3. To find your file, search from the **Downloads** folder.

---

## gsft-gift_card_scam-02
- candidate_id: gsft-gift_card_scam-02-v3
- conversation_sha256: 4bc9809e15b0e099411830684bbda0934aa127a7fdae2b7e6be041e33d2246bf
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
- gift-card-prize: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: Common Gift Card Scams | applicability: Any device | excerpt: "No honest business or agency will ever make you buy a gift card to pay them for a prize."
- gift-card-numbers: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: How Gift Card Scams Work | applicability: Any device; gift card payment requests | excerpt: "Don't give them those numbers or send them a photo of the card. It's a scam."

TARGET (read only after step 2)

> Don't pay. It's a scam. No honest business or agency will ever make you buy a gift card to pay them for a prize.
> 
> If they ask for gift card numbers, don't give them those numbers or send them a photo of the card.

---

## gsft-gift_card_scam-03
- candidate_id: gsft-gift_card_scam-03-v3
- conversation_sha256: cc42f92c656c0f676373fcbc6e8778edcf97ecf5e6783fee4eb445fc5528c4b7
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
- gift-card-no-agency: FTC, "Avoiding and Reporting Gift Card Scams | Consumer Advice" <https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams> | section: Introduction (first sentence); Common Gift Card Scams (second sentence, page starts it with 'But') | applicability: Any device | excerpt: "No real business or government agency will ever tell you to buy a gift card to pay them."

TARGET (read only after step 2)

> Hang up now. It's a scam.
> 
> Don't pay, and don't give them gift card numbers or send them a photo of a card. Government agencies won't contact you to demand immediate payment, and they never demand payment by gift card.

---
