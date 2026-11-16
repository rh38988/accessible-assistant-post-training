# The 31 corpus notes retrieved in the 15 development scenarios

This is a read-only convenience export of the **complete indexed note text** for each unique document in the original SFT v2 + RAG and v6 top-three results. The active corpus has 44 documents; only 31 appeared in these 15 rankings. These notes are source-checked paraphrases, **not the full text of the linked official webpages**. For exact query order, passages, and routing, use the two saved plan files.

- Original plan: `eval/outputs/dev-sft-v2-rag-20261115.plan.json`
- V6 plan: `eval/outputs/dev-sft-v2-rag-verified-action-plan-v6-20261115.plan.json`
- V6 checks: `eval/outputs/dev-sft-v2-rag-verified-action-plan-v6-20261115.checks.jsonl`
- Corpus manifest SHA256 in both plans: `98ba12590680b3f0576083c84187a5570e234111c0f658b38b5b986cafa0e501`
- Verification: all 15 scenario IDs and evidence lists match across the two plans; every exported note exactly matches the corresponding saved passage and source URL.

## Scenario to document IDs

| Scenario | Route | Retrieved IDs in rank order |
|---|---|---|
| `EVAL-PHONE-001` | answer | `apple-dark`, `samsung-dark`, `pixel-display` |
| `EVAL-PHONE-002` | clarify | `android-focus`, `android-speaker`, `apple-focus` |
| `EVAL-PHONE-003` | clarify | `google-messages-media`, `pixel-wallpaper`, `apple-wallpaper` |
| `EVAL-PHONE-004` | answer | `apple-airplane`, `apple-wifi`, `apple-update` |
| `EVAL-PHONE-005` | answer | `apple-wifi`, `apple-captive`, `apple-hotspot` |
| `EVAL-COMM-001` | clarify | `apple-screenshot`, `bank-screen-sharing-containment`, `android-permissions` |
| `EVAL-COMM-002` | answer | `android-speaker`, `zoom-mobile-audio`, `android-video` |
| `EVAL-COMM-003` | answer | `zoom-mobile-audio`, `zoom-host-mute`, `apple-focus` |
| `EVAL-COMM-004` | clarify | `gmail-forward`, `google-messages-media`, `ftc-phishing` |
| `EVAL-COMM-005` | answer | `line-unsend`, `taiwan-atm-fraud`, `ftc-remote-recovery` |
| `EVAL-SAFE-001` | answer | `ftc-tech-impersonation`, `police-remove-remote-access`, `bank-screen-sharing-containment` |
| `EVAL-SAFE-002` | answer | `ftc-medicare`, `ftc-remote-recovery`, `ftc-gift-cards` |
| `EVAL-SAFE-003` | answer | `ftc-utility`, `ftc-mobile-payments`, `apple-update` |
| `EVAL-SAFE-004` | answer | `taiwan-atm-fraud`, `line-unsend`, `ftc-remote-recovery` |
| `EVAL-SAFE-005` | clarify | `gmail-forward`, `google-messages-media`, `ftc-remote-recovery` |

## Complete indexed notes

### `android-focus` ? Android interruption filters and quiet mode

- Corpus file: `retrieval/corpus/android-focus.json`
- Official source: https://support.google.com/android/answer/9069335?hl=en
- Organization: Google
- Section: Quickly turn interruptions off or back on
- Platform / version: Android / Some steps require Android 14 or later
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `2005bb9890f22c48f4eea4fd01b99ce417eca8576c796af40b383bde81073b8f`
- Applicability / freshness: OEM and Android version change the Modes path, filters and duration controls.

Full indexed `text` field:

```text
Swipe down to Quick Settings and toggle Do Not Disturb. On the documented newer interface, Settings > Modes > Do Not Disturb > Turn on now is another route. Configure notification filters and the Quick Settings duration to control exceptions and how long silence lasts. Manufacturer settings differ and critical security notifications may remain visible.
```

### `android-permissions` ? Manage camera and microphone app permissions

- Corpus file: `retrieval/corpus/android-permissions.json`
- Official source: https://support.google.com/android/answer/9431959?hl=en
- Organization: Google
- Section: Change app permissions
- Platform / version: Android / Some Pixel steps require Android 11 or later
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `4f0704d9e810c9917b2fe7a412c1bbc2aa833861d741f3392b8ea9221f829b54`
- Applicability / freshness: Confirm device/app version before relying on exact menu labels.

Full indexed `text` field:

```text
Open Settings > Apps and select the relevant application, using See all apps if needed. Choose Permissions and select the permission to change. Set Allow or Do not allow as appropriate. Microphone and camera permissions can be limited to use while the app is open or requested each time on supported versions.
```

### `android-speaker` ? Hands-free audio during an Android telephone call

- Corpus file: `retrieval/corpus/android-speaker.json`
- Official source: https://support.google.com/phoneapp/answer/2811745?hl=en
- Organization: Google
- Section: Use phone call options
- Platform / version: Android / Some steps require Android 7 or later
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `baa6c16dc7027cf95f5fea2e570e206b597b9c027570cb3f08f72ab90ad6e1a8`
- Applicability / freshness: Phone-app and OEM layouts differ; a connected Bluetooth device may appear as another audio route. Editorial audit caution: Speaker is a call control, not the ringtone-volume setting.

Full indexed `text` field:

```text
During an active call in Google Phone, use Speaker to switch between the earpiece, speakerphone and a connected Bluetooth headset. Mute affects the microphone instead; Hold pauses a conversation without ending it.
```

### `android-video` ? Android video conversations using Meet

- Corpus file: `retrieval/corpus/android-video.json`
- Official source: https://support.google.com/android/answer/14103893?hl=en
- Organization: Google
- Section: Start a video call
- Platform / version: Android / Not specified by the selected section
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `59001dcb3c787919ea35a210f2aa938598864d425cffa729577dfab7bb705199`
- Applicability / freshness: Identify devices and a mutually compatible app first; different Phone and messaging apps expose different video controls.

Full indexed `text` field:

```text
In Meet on Android, select New, choose a contact and tap Call for a video conversation. Group calls use Create group, contact selection and Start. Android Chrome can receive a FaceTime invitation link from an Apple host, but cannot originate FaceTime calls; camera and microphone permissions and host admission may be required.
```

### `apple-airplane` ? Air travel radio settings and permitted Wi-Fi

- Corpus file: `retrieval/corpus/apple-airplane.json`
- Official source: https://support.apple.com/en-us/108785
- Organization: Apple
- Section: Turn on Airplane Mode
- Platform / version: iOS / iPadOS / Not specified by the selected section
- Accessed: 2026-10-28; page update: 2026-02-11
- Content SHA256: `9f0fa5f8a7243c5a6797b512ab9c8c01847c15109bd992b81b9818142d7660b6`
- Applicability / freshness: Airline permission is required. This section does not provide network joining or captive-login steps. Editorial audit caution: Airplane Mode temporarily disables radios; it does not mean the device is broken.

Full indexed `text` field:

```text
Open Control Center and select Airplane Mode to disable cellular and Wi-Fi radios while keeping Bluetooth available. If the airline permits it, Wi-Fi and Bluetooth can be used while Airplane Mode remains enabled. Airline permission remains necessary.
```

### `apple-captive` ? Sign in to public Wi-Fi on iPhone and iPad

- Corpus file: `retrieval/corpus/apple-captive.json`
- Official source: https://support.apple.com/en-us/102554
- Organization: Apple
- Section: Join a captive Wi-Fi network
- Platform / version: iOS / iPadOS / Not specified by the selected section
- Accessed: 2026-10-28; page update: 2026-04-23
- Content SHA256: `b55a2f1b94182887c4a3eaca006a523f1880e19feb0fe860837f6defffc7ffe4`
- Applicability / freshness: Network-provider login requirements vary; this does not establish airline permission or free access.

Full indexed `text` field:

```text
For a public network requiring a login, open Settings > Wi-Fi and select its name. Wait for its login screen. Alternatively open the information button next to the network and select Join Network. Provide only the login details or terms requested by the legitimate network provider. Charges can apply.
```

### `apple-dark` ? iPhone and iPad dark display controls

- Corpus file: `retrieval/corpus/apple-dark.json`
- Official source: https://support.apple.com/en-us/108350
- Organization: Apple
- Section: Dark Mode in Settings and Control Center
- Platform / version: iOS / iPadOS / Current page; separate iOS 26 and earlier route
- Accessed: 2026-10-28; page update: 2026-10-26
- Content SHA256: `3be1fc50a795e620847853102d9e424d4e431224d81e308263340c6302efd0c8`
- Applicability / freshness: Recently changed Appearance label; use the documented older-version route when needed.

Full indexed `text` field:

```text
For a darker display in low light, open Settings, then Appearance, and choose Dark. On iOS 26 and earlier the setting is under Display & Brightness. Alternatively, open Control Center, hold the brightness control, and toggle Dark Mode. Automatic mode can follow a schedule through Options.
```

### `apple-focus` ? iPhone quiet mode and notification exceptions

- Corpus file: `retrieval/corpus/apple-focus.json`
- Official source: https://support.apple.com/en-us/105112
- Organization: Apple
- Section: Focus menu and Do Not Disturb settings
- Platform / version: iOS / iPadOS / iOS / iPadOS 15 and later
- Accessed: 2026-10-28; page update: 2026-06-23
- Content SHA256: `4e08d56f3bfca726ee70df98697273da1b75bd643399f82d382dfbbf61cc3a6b`
- Applicability / freshness: Confirm device/app version before relying on exact menu labels.

Full indexed `text` field:

```text
Do Not Disturb silences incoming calls, alerts and notifications. Open Control Center, hold Focus, and select Do Not Disturb. Control Center opens from the top-right on newer iPhones and iPads, or bottom edge on older Home-button iPhones. Settings > Focus > Do Not Disturb controls schedules and notification exceptions; allowed people or apps can still interrupt.
```

### `apple-hotspot` ? Share iPhone cellular internet with a computer

- Corpus file: `retrieval/corpus/apple-hotspot.json`
- Official source: https://support.apple.com/en-us/111785
- Organization: Apple
- Section: Use Wi-Fi to connect to Personal Hotspot
- Platform / version: iOS / iPadOS / Not specified by the selected section
- Accessed: 2026-10-28; page update: 2026-05-07
- Content SHA256: `9a203a0a886795867718dd92952709dc09252106b4001b45f37109e81a54cdda`
- Applicability / freshness: Carrier eligibility, cellular data allowance and laptop Wi-Fi controls vary; do not promise free tethering.

Full indexed `text` field:

```text
Personal Hotspot shares cellular data as a portable Wi-Fi network. On the supplying iPhone open Settings > Personal Hotspot, or Cellular > Personal Hotspot, then enable Allow Others to Join. Keep that screen open. On the computer choose the phone hotspot from nearby Wi-Fi networks and enter the password displayed on the phone. The carrier must support tethering and may charge extra. Disable Allow Others to Join when finished.
```

### `apple-screenshot` ? Capture the iPhone screen with hardware buttons

- Corpus file: `retrieval/corpus/apple-screenshot.json`
- Official source: https://support.apple.com/en-us/102616
- Organization: Apple
- Section: Screenshot button combinations
- Platform / version: iOS / Not specified by the selected section
- Accessed: 2026-10-28; page update: 2026-10-15
- Content SHA256: `c820616ef5784c441bf9e9910c624040ee270bbd7f497a9600239ab4f6fb0afc`
- Applicability / freshness: Confirm device/app version before relying on exact menu labels.

Full indexed `text` field:

```text
On a Face ID iPhone, press Side and Volume Up together and quickly release them. On a Touch ID model, use Home together with the Side or Top button according to the device. Screenshots can be edited, shared and saved; the preview interface differs between iOS 26 and iOS 18 or earlier.
```

### `apple-update` ? Install Apple phone or tablet software updates

- Corpus file: `retrieval/corpus/apple-update.json`
- Official source: https://support.apple.com/en-us/118575
- Organization: Apple
- Section: Update wirelessly
- Platform / version: iOS / iPadOS / Not specified by the selected section
- Accessed: 2026-10-28; page update: 2026-09-15
- Content SHA256: `063a856ba2efee67b82acd1dbd62622de2f30c685aaa26487e8c054179f79a83`
- Applicability / freshness: Confirm device/app version before relying on exact menu labels.

Full indexed `text` field:

```text
Back up the device before updating. Connect power and Wi-Fi, then open Settings > General > Software Update. Check the installed version and available update; choose Download and Install if offered and follow prompts. A computer can be used if a wireless update is unavailable.
```

### `apple-wallpaper` ? Personal photo as an iPhone lock or home background

- Corpus file: `retrieval/corpus/apple-wallpaper.json`
- Official source: https://support.apple.com/en-us/102638
- Organization: Apple
- Section: Add a new wallpaper
- Platform / version: iOS / Not specified by the selected section
- Accessed: 2026-10-28; page update: 2026-02-02
- Content SHA256: `26710e31d4302c2b23ac8a1dc9ef15649c4650994b53566abb159e39c1899ee6`
- Applicability / freshness: Home and Lock Screen choices differ; 3D effects have additional model/version requirements not covered by this note.

Full indexed `text` field:

```text
In Settings, open Wallpaper and choose Add New Wallpaper. Choose Photos to pick a personal picture. Adjust it as desired, then use Add. Set as Wallpaper Pair applies it to both the Home Screen and Lock Screen; Customize Home Screen permits a different Home Screen background.
```

### `apple-wifi` ? Join an available wireless network on iPhone or iPad

- Corpus file: `retrieval/corpus/apple-wifi.json`
- Official source: https://support.apple.com/en-us/111107
- Organization: Apple
- Section: Connect to a Wi-Fi network
- Platform / version: iOS / iPadOS / Not specified by the selected section
- Accessed: 2026-10-28; page update: 2026-09-14
- Content SHA256: `d7efbeecec72864de3ce545785bc8850e9dbcfd4b2f0ccc330112bbd6a37ff90`
- Applicability / freshness: Joining instructions alone do not explain airline radio rules or captive-login troubleshooting.

Full indexed `text` field:

```text
Open Settings > Wi-Fi and enable Wi-Fi. Select the intended network, enter its password or accept its terms if requested. A blue checkmark by the network and the Wi-Fi status icon confirm connection. Ask the network administrator if its password is unknown.
```

### `bank-screen-sharing-containment` ? Stop a screen-sharing or remote-access banking scam

- Corpus file: `retrieval/corpus/bank-screen-sharing-containment.json`
- Official source: https://www.natwest.com/business/security/screen-sharing-scams.html
- Organization: National Westminster Bank plc
- Section: How to avoid it; Actions you can take
- Platform / version: Platform neutral / UK / Not specified by the selected section
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `3e92464ff963e2d26605b98bfc9c9dfb14eb7b694fbedadec8929623f2587c85`
- Applicability / freshness: UK bank business guidance; contact your own bank through its independently verified channel. No page update date displayed.

Full indexed `text` field:

```text
If an unexpected caller pressures you to grant remote access or share your screen, end the call. Never share passwords or online banking details, including typing them while someone can see your screen. If someone already has remote access, disconnect the device from the internet. Notify your IT department where applicable, run an antivirus scan after installing screen-sharing software, and change payment-account and email passwords. Contact your bank if personal information may have been shared.
```

### `ftc-gift-cards` ? Recognize demands for gift-card numbers and PINs

- Corpus file: `retrieval/corpus/ftc-gift-cards.json`
- Official source: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams
- Organization: US Federal Trade Commission
- Section: Avoid and recover from gift-card scams
- Platform / version: Platform neutral / US / Not specified by the selected section
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `e947d4a47732aa5eee2839953c83a3f28d34ac8f368d5f92e058c98a348597ab`
- Applicability / freshness: No page update date displayed; verify current app/device menus before use. Editorial audit caution: Legitimate birthday gifts are different from demands to pay an impersonator.

Full indexed `text` field:

```text
Urgent demands to pay a business or government agency with gift cards are scams. Stop the call and do not disclose a card number or PIN. If already disclosed, keep the card and receipt, notify its issuer immediately and ask for a refund. Report the fraud to the FTC.
```

### `ftc-medicare` ? Unexpected Medicare card calls requesting account numbers

- Corpus file: `retrieval/corpus/ftc-medicare.json`
- Official source: https://consumer.ftc.gov/consumer-alerts/2025/09/medicare-open-enrollment-season-learn-how-protect-yourself-scams
- Organization: US Federal Trade Commission
- Section: Protect yourself from Medicare scams
- Platform / version: Platform neutral / US / Not specified by the selected section
- Accessed: 2026-10-28; page update: 2025-09
- Content SHA256: `37a4141f1d8b9772e588946cad5ca8b6491952c267ed2be64ae6f56327998c1d`
- Applicability / freshness: US Medicare guidance and phone number; confirm jurisdiction before supplying regional contacts.

Full indexed `text` field:

```text
Unsolicited callers requesting Medicare or banking numbers for a new card are impersonators. Real Medicare cards are free and automatically mailed; Medicare does not unexpectedly solicit these numbers or a payment. Do not disclose personal or financial information. Hang up and independently call 1-800-MEDICARE to check and report; also report to the FTC.
```

### `ftc-mobile-payments` ? Safer legitimate mobile money transfers

- Corpus file: `retrieval/corpus/ftc-mobile-payments.json`
- Official source: https://consumer.ftc.gov/articles/mobile-payment-apps-how-avoid-scam-when-you-use-one
- Organization: US Federal Trade Commission
- Section: App setup; recipient verification; reporting scam payments
- Platform / version: Platform neutral / US / Not specified by the selected section
- Accessed: 2026-11-15; page update: 2022-05
- Content SHA256: `b8ab8f6b70e17097d646d7e82729c4f99bb63070987fdeb05e027a7a01862603`
- Applicability / freshness: FTC page dated May 2022, checked 2026-11-15. Reporting paths are what FTC states, not a fresh first-party app UI validation. No Zelle sending instructions or accidental-transfer refund procedure.

Full indexed `text` field:

```text
Payment apps require an account and funding method. Verify recipient details before payment and independently confirm unexpected requests from familiar accounts. Do not pay to collect a prize or share login credentials with unsolicited contacts. Enable multi-factor authentication or a PIN. Payments can be hard to recover. To report suspected scam payments: in Cash App use profile > Support; in Venmo use profile > Get Help; for PayPal use its online Resolution Center. Report to ReportFraud.ftc.gov. App-specific sending controls depend on the chosen service.
```

### `ftc-phishing` ? Suspicious email and text links requesting personal information

- Corpus file: `retrieval/corpus/ftc-phishing.json`
- Official source: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams
- Organization: US Federal Trade Commission
- Section: Protection and suspected phishing
- Platform / version: Platform neutral / US / Not specified by the selected section
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `f25b970d672503debd6666bd80f3f0e8d6cf8091376d86ddf5485cd12385f3b7`
- Applicability / freshness: No page update date displayed; verify current app/device menus before use.

Full indexed `text` field:

```text
Fraudulent email or texts can imitate banks and payment services to steal credentials or financial information. Unexpected links and attachments may be malicious. Protect devices with updates and security software, use multi-factor authentication and keep backups. Verify suspicious requests with a company through a contact you independently know, not a link or number in the message.
```

### `ftc-remote-recovery` ? Recovery after giving a scammer computer or account access

- Corpus file: `retrieval/corpus/ftc-remote-recovery.json`
- Official source: https://consumer.ftc.gov/articles/what-do-if-you-were-scammed
- Organization: US Federal Trade Commission
- Section: Payment recovery; personal information; computer access
- Platform / version: Platform neutral / US / Not specified by the selected section
- Accessed: 2026-11-15; page update: 2026-06
- Content SHA256: `bcce7f9248ef644985234ff63dcce813ac521f226729b70cd2690d6af0c03036`
- Applicability / freshness: US guidance. Does not cover accidental-payment refund requests, app-specific sending controls, explicit immediate network disconnection or remote-access-software removal. Existing bank/police containment records remain necessary.

Full indexed `text` field:

```text
If money was sent to a scammer, promptly contact the provider and ask about reversal or a refund: your bank or credit union for Zelle, bank transfers or debit cards; the issuer for credit cards; the wire service, gift card issuer, payment app, or cryptocurrency exchange/ATM operator for those payments. Recovery is not guaranteed. Keep gift cards and receipts. After computer or phone access, update security software, scan and remove identified threats, and change passwords and enable two-factor authentication. Seek trusted help with malware if needed. For misuse of a Social Security number, obtain a recovery plan at IdentityTheft.gov. Report to ReportFraud.ftc.gov.
```

### `ftc-tech-impersonation` ? Recognize fake technical support and protect accounts

- Corpus file: `retrieval/corpus/ftc-tech-impersonation.json`
- Official source: https://consumer.ftc.gov/articles/how-spot-avoid-and-report-tech-support-scams
- Organization: US Federal Trade Commission
- Section: How scams work; avoidance; compromised credentials; reports
- Platform / version: Platform neutral / US / Not specified by the selected section
- Accessed: 2026-11-15; page update: 2025-09
- Content SHA256: `26862fd179d0ecd578b88baead518ea85739e025ef58dfb6181cd7b0706d3596`
- Applicability / freshness: US consumer guidance; recognition and account protection do not supply full remote-access incident containment. Do not attribute disconnection or remote-software removal to this page.

Full indexed `text` field:

```text
Unexpected computer warnings or callers may be tech support impersonators seeking remote access or payment. Real security pop-ups do not ask you to call; legitimate tech companies do not initiate contact about computer problems. A demand to move money to protect it is fraudulent. For a suspicious subscription renewal, contact the company using a known number, not the message number. Check statements for unauthorized charges and ask the bank or card issuer about reversal. Change exposed and reused passwords. Report to ReportFraud.ftc.gov.
```

### `ftc-utility` ? Urgent power disconnection and payment-app demands

- Corpus file: `retrieval/corpus/ftc-utility.json`
- Official source: https://consumer.ftc.gov/articles/scammers-pretend-be-your-utility-company
- Organization: US Federal Trade Commission
- Section: Avoid and report utility scams
- Platform / version: Platform neutral / US / Not specified by the selected section
- Accessed: 2026-10-28; page update: 2026-06
- Content SHA256: `66de17131607076789ebf5633fcd6f22190aaed2ec7b3779be448a3dbdf613e7`
- Applicability / freshness: US reporting advice; bill-based independent verification is broadly useful but regional shutoff processes vary.

Full indexed `text` field:

```text
A caller threatening immediate gas, electric or water disconnection unless paid on the spot is a scammer. Hang up and do not pay or follow links. Verify the account by calling the utility using the number printed on a bill or its independently located official website. Utility companies do not demand payment only by a payment app, wire, cryptocurrency or gift cards. Report the impersonation to the utility and FTC.
```

### `gmail-forward` ? Forward received email in Gmail for Android

- Corpus file: `retrieval/corpus/gmail-forward.json`
- Official source: https://support.google.com/mail/answer/15162918?hl=en&co=GENIE.Platform%3DAndroid
- Organization: Google
- Section: Forward a single email
- Platform / version: Android / Not specified by the selected section
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `c450af6cd1f1567996d001c9cabb476c7671c101a74bff1cdd26541da0e869f5`
- Applicability / freshness: No page update date displayed; verify current app/device menus before use. Editorial audit caution: These controls are specific to Gmail for Android.

Full indexed `text` field:

```text
Open the Gmail app on an Android phone or tablet, then open the received email. Select Forward below the email, add the intended new recipients and send. For a particular email inside a conversation, use its More menu and Forward.
```

### `google-messages-media` ? Send a photo in an Android text conversation

- Corpus file: `retrieval/corpus/google-messages-media.json`
- Official source: https://support.google.com/messages/answer/6159880?hl=en
- Organization: Google
- Section: Send photos, videos, files or GIFs
- Platform / version: Android / Some steps require Android 6 or later
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `c2698064fd211c523d228fafb98af4bbad191df2d47b21c5f827386aadf1ae82`
- Applicability / freshness: No page update date displayed; verify current app/device menus before use.

Full indexed `text` field:

```text
Open a Google Messages conversation and select Image beside the text field. Choose a file or take a photo, select media quality if offered, and send. File access requires permissions; carrier MMS compression can reduce quality and RCS can improve it. Taking a picture inside Messages does not save it to the device.
```

### `line-unsend` ? LINE 誤傳訊息：收回與刪除的差別

- Corpus file: `retrieval/corpus/line-unsend.json`
- Official source: https://help.line.me/line/smartphone?contentId=20007159&lang=zh-Hant
- Organization: LY Corporation / LINE
- Section: 收回訊息及刪除訊息的差異；操作方法
- Platform / version: iOS / Android / desktop / Not specified by the selected section
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `a4cd0a94ac97e5a4d4631236d879d1ee2046a0126018601d3e9b799e41469efe`
- Applicability / freshness: Time limits and Premium availability change by client, region and membership. Current page differs from older 24-hour general rules.

Full indexed `text` field:

```text
在 LINE 聊天室長按已送出的訊息，選擇「收回」，可移除自己及對方聊天室內的內容。「刪除」只影響自己的畫面，對方仍能看見。一般收回期限是送出後一小時；Premium 為七天，社群則為二十四小時。收回前對方可能已看過內容或通知，不能保證未被看見。
```

### `pixel-display` ? Pixel display brightness and dark theme

- Corpus file: `retrieval/corpus/pixel-display.json`
- Official source: https://support.google.com/pixelphone/answer/6111557?hl=en
- Organization: Google
- Section: Display settings and Dark theme
- Platform / version: Android / Pixel / Pixel; feature availability varies by model
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `0e0c7a7d3bf4f820b1d3e112d056e5e2b3831783c0345ea8db2d1dc1d15a1abf`
- Applicability / freshness: Pixel-specific menu names should not be transferred to iPhone or other Android manufacturers.

Full indexed `text` field:

```text
Open Pixel Settings > Display & touch. Brightness level changes screen brightness; Dark theme darkens supported screens and can be scheduled. Display size and text controls the font slider. Adaptive brightness learns preferences and is distinct from Dark theme.
```

### `pixel-wallpaper` ? Choose a personal photograph for a Pixel background

- Corpus file: `retrieval/corpus/pixel-wallpaper.json`
- Official source: https://support.google.com/pixelphone/answer/7289143?hl=en
- Organization: Google
- Section: Change wallpapers
- Platform / version: Android / Pixel / Not specified by the selected section
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `2b21016a1e8935bcef6c5f351b5e637979c122cdf025be949ac911a7b44b2161`
- Applicability / freshness: Pixel interface varies by software version; confirm which screen should change.

Full indexed `text` field:

```text
Hold an empty Home screen area, then open Wallpapers & style and Change wallpaper. Use Choose a photo to select a personal picture. Choose Home screen or Lock screen as offered, preview it, then apply it. More wallpapers may expose additional photo choices depending on the interface.
```

### `police-remove-remote-access` ? Remove remote-access software after a fake computer support call

- Corpus file: `retrieval/corpus/police-remove-remote-access.json`
- Official source: https://www.rushcliffe.gov.uk/media/giyh0loo/fraud-advice-booklet.pdf
- Organization: Nottinghamshire Police; hosted by Rushcliffe Borough Council
- Section: PDF page 16 (printed pages 30-31): Computer service software fraud; Removing software
- Platform / version: Platform neutral / UK / Not specified by the selected section
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `4f5854b85f1dd9da3cd28666177d052e078cdaa39907e64bc80e319c19b14bff`
- Applicability / freshness: UK police booklet has no explicit update date. Retain generic software-removal principles without inferring Windows/macOS or using UK reporting numbers for an unspecified jurisdiction.

Full indexed `text` field:

```text
A caller pretending to be Microsoft or another service company may ask you to install software and give remote access to your computer, tablet or phone. Legitimate companies do not cold-call to request this access or financial details. Uninstall the remote-access software if confident, or ask a trusted friend, family member or local computer expert for help removing it. Notify your bank if a payment was made to the suspected scammer. Consider what personal documents were accessible and report the incident through the appropriate local fraud-reporting service.
```

### `samsung-dark` ? Galaxy dark theme from Quick Settings

- Corpus file: `retrieval/corpus/samsung-dark.json`
- Official source: https://www.samsung.com/us/support/answer/ANS10002537/
- Organization: Samsung
- Section: Manually turn on Dark mode
- Platform / version: Android / Samsung Galaxy / Android 10 and later Settings route
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `4dd8ad7b5a49a34fba53744cde0f6b626fdbc794ca32eb4aab04f9a7b0211412`
- Applicability / freshness: Not all apps/themes honor dark mode; page does not display an update date.

Full indexed `text` field:

```text
Swipe down from the screen top with two fingers to open Quick Settings, then tap Dark mode. Tap again to disable it. Android 10 and later also expose Dark mode through Settings > Display. Certain third-party apps, themes and high contrast fonts may not follow Dark mode; keep software current.
```

### `taiwan-atm-fraud` ? 假網購客服要求用 ATM 取消分期

- Corpus file: `retrieval/corpus/taiwan-atm-fraud.json`
- Official source: https://www.cib.npa.gov.tw/ch/app/data/view?module=wg116&id=1909&serno=a61af506-a4ac-49eb-9c79-ef75ddc6f237
- Organization: Taiwan National Police Agency / Criminal Investigation Bureau
- Section: 第三章：手法解析與預防策略
- Platform / version: Platform neutral / Taiwan / Not specified by the selected section
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `7840cde4d4509ec3901974a51271527e1673172d29d2644f7ab874a4706650c4`
- Applicability / freshness: Taiwan-specific hotline; article has no update date. Its broad claim about ATM functions should not be generalized to every banking service.

Full indexed `text` field:

```text
假客服或銀行來電，稱購物設定錯誤、重複扣款或分期付款，並要求操作 ATM、網銀或購買點數，是詐騙話術。即使對方說得出交易紀錄也不能證明身分。不要按指示操作；掛斷後自行查詢官方客服電話確認，在臺灣也可撥 165 諮詢。ATM 不能取消分期或辦理這類退款。
```

### `zoom-host-mute` ? Host restrictions on participant microphone unmuting

- Corpus file: `retrieval/corpus/zoom-host-mute.json`
- Official source: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066716
- Organization: Zoom
- Section: Participant permissions and consent
- Platform / version: iOS / iPadOS / Android / Web / desktop / Not specified by the selected section
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `b2744590e10b3a35c85b369c5055373a73cd815ec3b734cc93dd620c88bd2681`
- Applicability / freshness: Explains host restrictions only; does not cover app permissions or joining audio.

Full indexed `text` field:

```text
Meeting hosts can mute participants and disallow participant self-unmuting. Participants can otherwise mute or unmute themselves. Host unmuting normally requires participant consent; pre-approved consent changes the available controls. A participant prevented from unmuting needs host assistance rather than repeated taps on their microphone.
```

### `zoom-mobile-audio` ? Troubleshoot an unheard microphone in a mobile Zoom meeting

- Corpus file: `retrieval/corpus/zoom-mobile-audio.json`
- Official source: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066222
- Organization: Zoom
- Section: If other participants cannot hear you
- Platform / version: iOS / iPadOS / Android / Not specified by the selected section
- Accessed: 2026-10-28; page update: not recorded
- Content SHA256: `1dcf76a2ff235202f08a295326daf84c883544a32a7842fecfb53f80e66d92c2`
- Applicability / freshness: Older Privacy label and Home-button app-switching examples; current iPadOS permission location may be Privacy & Security. Do not diagnose host restriction as certain.

Full indexed `text` field:

```text
If the meeting Audio icon indicates mute, tap to unmute. If it stays muted, ask the host through chat to permit unmuting. If Join Audio appears, select it and Call Over Internet, allowing microphone access. On iOS check Settings > Privacy > Microphone for Zoom permission. Close other apps using the microphone; restart if needed. Multiple causes are possible.
```
