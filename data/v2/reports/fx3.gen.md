# fx3 generation report

Batch: 13 tasks, 25 new examples (e and r for 12 tasks, e only for TR-041). Builder OK.

## Sources (all fetched and read)
- TR-033: https://support.google.com/android/answer/7680439?hl=en
- TR-034: https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/install-windows-updates ; r example also uses the same publisher's https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/troubleshoot-problems-updating-windows (troubleshooter path, Wi-Fi check, check again), because the install page only points to it.
- TR-035: https://support.google.com/photos/answer/6193313?hl=en&co=GENIE.Platform%3DAndroid
- TR-036: https://support.microsoft.com/en-us/windows/hardware/printer/add-or-install-a-printer-in-windows
- TR-037: https://support.google.com/mail/answer/6584?hl=en&co=GENIE.Platform%3DAndroid
- TR-038: https://support.google.com/accounts/answer/7682439?hl=en
- TR-039: https://consumer.ftc.gov/consumer-alerts/2023/03/scammers-use-ai-enhance-their-family-emergency-schemes ; r (already_acted) also uses https://consumer.ftc.gov/articles/what-do-if-you-were-scammed (wire transfer section) because the cited page has no after-payment advice.
- TR-040: https://consumer.ftc.gov/consumer-alerts/2025/04/think-text-message-usps-it-could-be-scam ; r (already_acted) also uses https://consumer.ftc.gov/articles/what-do-if-you-were-scammed (credit card section), same reason.
- TR-041: https://consumer.ftc.gov/articles/avoiding-and-reporting-gift-card-scams
- TR-042: https://support.apple.com/en-us/108380
- TR-043: https://support.google.com/contacts/answer/1069522?hl=en&co=GENIE.Platform%3DAndroid
- TR-045: https://support.apple.com/en-us/111104
- TR-046: https://support.google.com/phoneapp/answer/6325463?hl=en

No topics replaced by backups.

## Not fully sure the page supports
- tr033-e: "you can restart after your call" is an inference from "takes effect the next time you restart" on Pixel.
- tr034-e: "Download & install is the one that starts the installing, so leave it alone" is an inference from the page's step order.
- tr039-e: telling the user to also contact his parents despite the caller's request is applied advice ("another family member or friends"); the page does not mention secrecy demands.
- tr040-e: "check each order at each store you ordered from" applies the page's "go to the retailer or account where you ordered".
- tr043-r: "Linda may be saved somewhere else" is a hedged inference from "Google Account contacts sync to your Android devices"; the page has no troubleshooting.
- tr045-r: the unblock path (Settings, Privacy & Security, Blocked Contacts) is labelled iOS 26 on the page, so the reply says so.
- tr046-e: "covers every unknown caller" is a plain restatement of the Unknown toggle.

## Existing examples the source shows are wrong or unsupported (not edited)
- tr040-a, tr040-d: "call your bank right away using the number on the back of your card" for a card entered into a fake site, and "Then delete it", are not on the cited FTC page (the page has no after-click advice). The bank advice does match the separate "What to do if you were scammed" page for credit or debit cards.
- tr039-a, tr039-d: "If you already sent money, tell me right away" is not from the page; fine as chat, but the page gives no recovery steps.
- tr041-a, tr041-c, tr041-d, tr041-r: "call your pastor or the church office" is not in the source (page does not mention pastors; it says to reach a relative through a number you know). "Sometimes they can freeze what's left on the card" is only supported for Apple and Google cards. tr041-r step 5 ("tell your church office", pastor's email may be hacked) and "photo of both" are not on the page (photo of card and receipt is; church advice is not).
- tr042-a, tr042-d: the create-group steps omit tapping **Continue** after **Family**.
- tr043-a, tr043-d: "Now the name will show up when the office calls you" and "if your phone uses a different contacts app..." are not on the page.
- tr045-a, tr045-c, tr045-d: "Confirm if asked" / "tap Block Contact" confirmation is not described on the page for the Phone app path. tr045-c "calls won't ring" okay, voicemail note is supported.
- tr046-a, tr046-d: "Confirm if asked" is not on the page.
- tr034-a/c/d: button is "Check for Windows updates" on the page; examples say "Check for updates" (minor).
- tr038-a/c/d: describe the recovery page without its address and say "wait a few days"; supported, but the "create a new password you haven't used before" wording slightly differs (page: strong password not used with this account).
- tr037-d: "which the person can still open" about Drive links is not on the page.
