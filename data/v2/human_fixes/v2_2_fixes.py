"""v2.2 fixes: the 15 examples Shirley marked `fix` in spot_check_v2.csv.

Each entry replaces the example's whole `messages` list (and `sources` where a new
official page was needed). `follows` says how Shirley's suggestion was applied;
`page_differs` records where the official page did not support her wording, in
which case the page was followed. Pages were read on 2026-11-16.

Applied by: python3 data/v2/tools/apply_human_fixes.py
"""

ACCESSED = "2026-11-16"


def src(title, url):
    return {"title": title, "url": url, "accessed": ACCESSED}


GMAIL_ATTACH = src("Gmail Help: Send attachments with your Gmail message", "https://support.google.com/mail/answer/6584")
FTC_SCAMMED = src("FTC: What To Do if You Were Scammed", "https://consumer.ftc.gov/articles/what-do-if-you-were-scammed")
FTC_FAMILY = src("FTC: Talking Turkey (family emergency scams)", "https://www.ftc.gov/node/54353")
MS_SNIP = src("Microsoft Support: Use Snipping Tool to capture screenshots",
              "https://support.microsoft.com/en-us/windows/apps/use-snipping-tool-to-capture-screenshots")
MS_PRTSC = src("Microsoft Support: Keyboard shortcut for Print Screen",
               "https://support.microsoft.com/en-us/windows/experience/keyboard-shortcut-for-print-screen")
MS_FIND = src("Microsoft Support: Find your files in Windows",
              "https://support.microsoft.com/en-us/windows/find-your-files-in-windows-5c7c8cfe-c289-fae4-f5f8-6b3fdba418d2")
APPLE_BATTERY = src("Apple Support: iPhone battery and performance", "https://support.apple.com/en-us/101575")
APPLE_FINDMY = src("Apple Support: Share your location with your family", "https://support.apple.com/en-us/105104")
APPLE_DELETE = src("Apple Support: Delete apps on your iPhone", "https://support.apple.com/en-us/101550")
APPLE_SCREENTIME = src("iPhone User Guide: Block features or content with Screen Time",
                       "https://support.apple.com/guide/iphone/block-features-or-content-with-screen-time-iph3ff83f3b1/ios")
SAMSUNG_STORAGE = src("Samsung Support: How to clear or free up internal storage on your phone",
                      "https://www.samsung.com/uk/support/mobile-devices/how-to-clear-up-storage-space-on-your-smartphone")
GPHOTOS_DELETE = src("Google Photos Help: Delete and restore photos and videos", "https://support.google.com/photos/answer/6128858?hl=en")
APPLE_FLASH = src("Apple Support: Turn on the flashlight on your iPhone", "https://support.apple.com/en-us/105001")
APPLE_REMINDERS = src("Apple Support: Use Reminders on your iPhone", "https://support.apple.com/en-us/102484")
MAC_BT = src("Mac User Guide: Connect a Bluetooth device", "https://support.apple.com/en-us/guide/mac-help/blth1004/mac")
MAC_CC = src("Mac User Guide: Use Control Center on Mac", "https://support.apple.com/guide/mac-help/mchl50f94f8f/mac")
APPLE_SPAM = src("iPhone User Guide: Report spam and block senders",
                 "https://support.apple.com/guide/iphone/report-spam-and-block-senders-iph3f94d910d/ios")
CHROME_PW = src("Chrome Help: Use passwords across your devices (Google Password Manager)", "https://support.google.com/chrome/answer/95606?hl=en")
MS_ACCOUNTS = src("Microsoft Support: Manage user accounts in Windows",
                  "https://support.microsoft.com/en-us/windows/manage-user-accounts-in-windows-104dc19f-6430-4b49-6a2b-e4dbd1dcdf32")
MS_HELLO = src("Microsoft Support: Configure Windows Hello",
               "https://support.microsoft.com/en-us/windows/configure-windows-hello-dae28983-8242-bb2a-d3d1-87c9d265a5f0")
FTC_DEBT = src("FTC: Debt Collection FAQs", "https://www.consumer.ftc.gov/articles/debt-collection-faqs")
FTC_BLACKMAIL = src("FTC Consumer Alert: Scam emails demand Bitcoin, threaten blackmail",
                    "https://consumer.ftc.gov/consumer-alerts/2020/04/scam-emails-demand-bitcoin-threaten-blackmail")
FTC_MORTGAGE = src("FTC: Mortgage Relief Scams", "https://consumer.ftc.gov/articles/mortgage-relief-scams")


def u(t):
    return {"role": "user", "content": t}


def a(t):
    return {"role": "assistant", "content": t}


FIXES = [
    {
        "id": "tr012-e",
        "messages": [
            u("I'm writing an email in Gmail on my computer and my picture is already showing in a folder on the screen next to it. The little buttons at the bottom are hard for me to hit with my shaky hand. Can I just pull the picture over into the email instead of using the button?"),
            a("Yes, you can drag the picture into your email instead.\n\n"
              "1. Click the picture in the folder window and hold the mouse button down.\n"
              "2. Move it over the email you're writing, into the big area where you type your message.\n"
              "3. Let go of the mouse button.\n"
              "4. Check that the picture now shows in your email before you send it.\n\n"
              "If dragging is hard too, tell me which part is hardest, holding the button down or moving the mouse, and we can find another way."),
        ],
        "sources": [GMAIL_ATTACH],
        "follows": "Drop target is now the message area; added a check that the picture appears; removed the Attach-button fallback and ask which part of dragging is hard.",
        "page_differs": "",
    },
    {
        "id": "tr014-r",
        "messages": [
            u("Oh no. I think I got scammed. A woman said my grandson was in jail and I mailed $1,500 cash to an address she gave me. Now I called my grandson's real number and he is fine. What do I do now?"),
            a("I'm sorry this happened. It is not your fault, and you did the right thing by calling your grandson. Act quickly, because a package that hasn't been delivered yet may still be stopped.\n\n"
              "1. If you mailed it through the U.S. Postal Service, call the **U.S. Postal Inspection Service** right away at **1-877-876-2455** and ask them to intercept the package. There is a fee, and it only works if the package hasn't been delivered yet.\n"
              "2. If you sent it with another company, like FedEx or UPS, call that company as soon as you can.\n"
              "3. Report the scam to the FTC at **ReportFraud.ftc.gov**.\n"
              "4. Don't send any more money, even if the caller contacts you again.\n\n"
              "I can't promise you'll get the money back. Which company did you send it with, and has it been delivered yet?"),
        ],
        "sources": [FTC_SCAMMED, FTC_FAMILY],
        "follows": "Leads with intercepting the package (USPIS 1-877-876-2455; FedEx/UPS), asks which carrier and whether it was delivered, makes no recovery promise, reports at ReportFraud.ftc.gov. Added the FTC 'What To Do if You Were Scammed' page as the main source.",
        "page_differs": "",
    },
    {
        "id": "tr028-r",
        "messages": [
            u("How can I take a picture of my whole screen on my Windows 11 computer?"),
            a("You can use **Snipping Tool**.\n\n"
              "1. Select **Start**, type **snipping tool**, then select **Snipping Tool**.\n"
              "2. Select **Snipping Mode**, then choose **Full screen**.\n"
              "3. Select **New**.\n\n"
              "It captures the whole screen right away."),
            u("OK it took the picture but I can't tell where it went. How do I find it?"),
            a("Snipping Tool saves each snip automatically in your **Screenshots** folder. Here's how to find it.\n\n"
              "1. Select **File Explorer** on the taskbar.\n"
              "2. In the pane on the left, select **Pictures**, then open **Screenshots**.\n"
              "3. If you don't see **Pictures** there, select **Home** in File Explorer, type **Screenshots** in the search box, and press **Enter**. Then open the **Screenshots** folder from the results.\n\n"
              "Next time, you can also select **Save as** in Snipping Tool right after a snip, choose a place and a name, then select **Save**."),
        ],
        "sources": [MS_SNIP, MS_PRTSC, MS_FIND],
        "follows": "No longer assumes Screenshots shows in the side pane: the path is Pictures > Screenshots (Print Screen page), with a fallback search from Home for the folder name (Find your files page).",
        "page_differs": "Shirley said the control is called 'snipping area'. Microsoft's Snipping Tool page says 'select Snipping Mode', so that label was kept. The page shows icons for buttons but does not describe their shapes, so no icon descriptions were added.",
    },
    {
        "id": "tr050-a",
        "messages": [
            u("My iPhone battery seems to die quickly. How do I check the battery health?"),
            a("You can check it in Settings.\n\n"
              "1. Open the **Settings** app.\n"
              "2. Tap **Battery**.\n"
              "3. Tap **Battery Health**. On some versions the name is slightly different.\n"
              "4. Look at **Maximum Capacity**. It tells you how much charge your battery can hold now, compared with when it was new. As a battery gets older, it holds less charge, so you get fewer hours of use between charges.\n\n"
              "If you see the message **\"Your battery's health is significantly degraded,\"** it isn't a safety problem, and you can still use your iPhone. A new battery would bring back its full capacity. Apple offers battery service, and if your iPhone is out of warranty, there is a charge."),
        ],
        "sources": [APPLE_BATTERY],
        "follows": "Maximum Capacity explained in plain words from the page. Also removed 'It takes a minute' (duration not on the page) and the unsupported 'may be covered under warranty' line.",
        "page_differs": "",
    },
    {
        "id": "tr054-r",
        "messages": [
            u("My daughter has an iPhone too. How can I let her see where I am on my iPhone while I drive to her house?"),
            a("You can do this in the **Find My** app. Set it up before you start driving, while you're parked.\n\n"
              "1. Open **Find My**.\n"
              "2. Tap the **Me** tab and turn on **Share My Location**.\n"
              "3. Tap the **People** tab, tap the **Add** button, then tap **Share My Location**.\n"
              "4. Choose your daughter.\n"
              "5. Pick how long to share: an hour, until the end of the day, indefinitely, or a custom time period.\n\n"
              "Only share your location with people you trust."),
            u("When I tap the plus button I don't see Share My Location at all."),
            a("Let's check which screen you're on first. Please do this while you're parked.\n\n"
              "1. Tap the **Me** tab and check that **Share My Location** is turned on.\n"
              "2. Tap the **People** tab.\n"
              "3. Tap the **Add** button and look for **Share My Location** in the list that opens.\n\n"
              "If it's still not there, what choices do you see after you tap **Add**? Tell me, and I'll help you pick the right one."),
        ],
        "sources": [APPLE_FINDMY],
        "follows": "Set up while parked, before driving. The recovery reply now checks the Me and People tabs and asks what choices appear, instead of telling the user to update.",
        "page_differs": "Shirley said the custom duration is not in the source. Apple's page says 'Choose to share your location for an hour, until the end of the day, indefinitely, or a custom time period', so it was kept. '(a plus icon)' was removed because the page calls it the Add button.",
    },
    {
        "id": "tr058-r",
        "messages": [
            u("How can I take the Facebook app off my iPhone? I don't use it anymore."),
            a("You can delete it from the Home Screen.\n\n"
              "1. Touch and hold the app.\n"
              "2. Tap **Remove App**.\n"
              "3. Tap **Delete App**.\n"
              "4. Tap **Delete** to confirm.\n\n"
              "Deleting an app doesn't cancel subscriptions inside it, so cancel any you don't need first."),
            u("I held it but there is no Remove App choice, or it won't let me delete it."),
            a("Let's check what happens when you hold the app.\n\n"
              "1. Touch and hold the **Facebook** app. If the apps start to jiggle, tap the **Remove** icon in the upper-left corner of the Facebook app, then tap **Delete App**, then **Delete**.\n"
              "2. If you don't get a way to remove it, deleting apps may be turned off. Open **Settings**, tap **Screen Time**, then **Content & Privacy Restrictions**, then find **Deleting Apps** and make sure it is set to **Allow**.\n"
              "3. If your iPhone is managed by a company or school, ask its administrator.\n\n"
              "When you hold the Facebook app, what happens: a menu opens, the apps jiggle, or nothing changes?"),
        ],
        "sources": [APPLE_DELETE, APPLE_SCREENTIME],
        "follows": "Removed the built-in Apple apps branch. Added the jiggle path, a Screen Time path for the restriction, kept the administrator step, and asks what happens when the app is held.",
        "page_differs": "Apple's pages give Settings > Screen Time > Content & Privacy Restrictions and say 'Make sure Deleting Apps is set to Allow', but no official page found gives the menu between them (community posts say iTunes & App Store Purchases). The reply says 'find Deleting Apps' rather than naming an unverified menu.",
    },
    {
        "id": "tr062-d",
        "messages": [
            u("phone says storage full"),
            a("I can help you clear some space. Is your phone an **iPhone** or an **Android** phone?"),
            u("Android, Samsung"),
            a("Thanks. On a Samsung phone, here's how to see what's using space and clear some out.\n\n"
              "1. Open the **Settings** app.\n"
              "2. Tap **Battery and device care**. On some older phones, this is called **Device care**.\n"
              "3. Tap **Storage**.\n"
              "4. Tap **Unused apps**, select the apps you don't use, and tap **Uninstall**. You can also tap **Large files** or **Duplicate files**, select what you don't need, and tap **Delete**.\n\n"
              "**If your photos back up to Google Photos:** you can remove just the copies on your phone. In Google Photos, tap a photo, tap **More**, and scroll to **Details** to check that it's backed up. Then select the photos, tap **More**, and choose **Delete from device**. Don't use the regular **Delete** for this, because that removes the photos from Google Photos too, on every device where backup is on.\n\n"
              "If your Storage screen looks different, tell me what you see on it."),
        ],
        "sources": [SAMSUNG_STORAGE, GPHOTOS_DELETE],
        "follows": "Samsung path (Battery and device care > Storage) from Samsung's page. Photo advice now checks backup and uses Delete from device, with a warning that regular Delete also removes the backed-up copy. Asks the user to describe their Storage screen if it differs.",
        "page_differs": "Shirley suggested confirming the model or One UI version. The reply asks about the Storage screen instead, since Samsung's page only notes that older software calls it Device care.",
    },
    {
        "id": "tr063-d",
        "messages": [
            u("my phone is dark and I need some light, where is it"),
            a("I can help. Do you want to use your phone as a **flashlight**, or make your **screen brighter**?"),
            u("The flashlight. It's an iPhone."),
            a("Got it.\n\n"
              "There are a few quick ways.\n\n"
              "**From Control Center:**\n"
              "1. If your iPhone has Face ID (no Home button), **swipe down from the top-right corner** of the screen. If it has a Home button, **swipe up from the bottom edge**.\n"
              "2. Tap the **Flashlight** button.\n"
              "3. Tap it again to turn it off.\n\n"
              "**From the Lock Screen:** press and hold the **Flashlight** button in the bottom-left corner.\n\n"
              "**With Siri:** say \"Hey Siri, turn on my flashlight.\""),
        ],
        "sources": [APPLE_FLASH],
        "follows": "The first reply now asks what the user means (flashlight or brighter screen) instead of assuming flashlight; the user's answer gives both the goal and the device. Final reply unchanged (checked against the page).",
        "page_differs": "",
    },
    {
        "id": "tr103-e",
        "messages": [
            u("My iPhone is on silent almost all the time because I can't stand the noise. But I have a heart pill I must take at noon and I need the reminder to actually make a sound anyway. Can a reminder be loud even on silent? I want one for today at noon."),
            a("Yes. You can mark the reminder as **Urgent**, and its alarm sounds even when your iPhone is silenced.\n\n"
              "1. Open the **Reminders** app.\n"
              "2. Tap **+ New Reminder** and type **Take heart pill**.\n"
              "3. Tap the **Date and Time** button, tap **Custom**, and set it for today at **12:00 PM**.\n"
              "4. Tap the reminder, then tap the **Info** button.\n"
              "5. Under **Date & Time**, turn **Urgent** on.\n\n"
              "If you don't see **Urgent**, tell me. If the alarm doesn't sound at noon, open **Settings**, tap **Apps**, tap **Reminders**, and turn on **Alarms** under **Allow Reminders to Access**."),
        ],
        "sources": [APPLE_REMINDERS],
        "follows": "Removed the iOS 26.2 / iCloud requirement sentence and the Find My device sentence. Kept one short troubleshooting line.",
        "page_differs": "v2.1 had removed 'Custom' from step 3. Apple's page says 'Tap the Date and Time button ... or tap Custom to set your own day and time', so Custom is back for setting noon today.",
    },
    {
        "id": "tr129-e",
        "messages": [
            u("My Bluetooth headphones are already set up on my Mac, they just are not connected right now. I do not want to dig through System Settings every time. Is there a quicker way to connect them?"),
            a("Yes. You can use **Control Center**, which is in the menu bar at the top right of your screen.\n\n"
              "1. Make sure your headphones are on.\n"
              "2. In the menu bar at the top right of the screen, click the **Control Center** icon.\n"
              "3. Click **Bluetooth**, then select your headphones from the list.\n\n"
              "If you ever want the longer way, open the **Apple menu**, choose **System Settings**, click **Bluetooth**, point at the headphones, and click **Connect**."),
        ],
        "sources": [MAC_BT, MAC_CC],
        "follows": "Says where Control Center is and how to open it (menu bar, top right), from the Mac User Guide's Control Center page.",
        "page_differs": "The Control Center page does not describe what the icon looks like, so no icon description was added.",
    },
    {
        "id": "tr133-e",
        "messages": [
            u("A stranger texted my iPhone and I already wrote back to ask who they were. Now they keep texting. Can I still report them as spam?"),
            a("You can't use the **Report Spam** option in Messages for a message after you've replied to it. You can still block the sender.\n\n"
              "1. Open the conversation in **Messages**.\n"
              "2. Tap the person's icon at the top.\n"
              "3. Tap **Info**, scroll down, then tap **Block Contact**.\n\n"
              "This blocks this sender's number, and they won't know they've been blocked. If you'd like to report the texts another way, you can ask your phone carrier."),
        ],
        "sources": [APPLE_SPAM],
        "follows": "The limit is now scoped to Messages' built-in report option. Blocking is described as covering this sender's number only. Added the carrier as another reporting route.",
        "page_differs": "Shirley's note says 'Report Junk'. The current iPhone User Guide calls it 'Report Spam', so the page label was used.",
    },
    {
        "id": "tr192-e",
        "messages": [
            u("My husband and I share one Windows computer and Chrome has my passwords saved. I don't want him to be able to just click and see them. Can I make Chrome check that it is really me before it shows a saved password?"),
            a("Yes. Chrome can use **Windows Hello** to check before it fills in a saved password, and the same check can be used to reveal, copy, or edit a password. Windows Hello uses the PIN, face, or fingerprint set up for signing in to Windows. So it only keeps your husband out if he can't use that same sign-in.\n\n"
              "First, make sure the Windows sign-in is yours alone:\n"
              "1. If you both use the same Windows account, give him his own. Open **Settings**, select **Accounts** > **Other users**, then under **Add other user** select **Add account** and follow the instructions.\n"
              "2. If he knows your PIN, change it. Open **Settings**, select **Accounts** > **Sign-in options**, then select **PIN (Windows Hello)**.\n\n"
              "Then turn on the check in Chrome:\n"
              "3. At the top right, click **More**.\n"
              "4. Click **Passwords and autofill**, then **Google Password Manager**.\n"
              "5. Select **Settings**.\n"
              "6. Turn on **Use Windows Hello when filling passwords**, and follow the on-screen instructions.\n\n"
              "The check is off until you turn it on."),
        ],
        "sources": [CHROME_PW, MS_HELLO, MS_ACCOUNTS],
        "follows": "Explains that the check relies on the Windows sign-in, so it fails if they share an account or PIN. Recommends a separate account for the husband and a private PIN, then gives the Chrome steps. The account is added for him so her saved passwords stay in her own account.",
        "page_differs": "Microsoft's Windows Hello page gives Settings > Accounts > Sign-in options > PIN (Windows Hello) for setting up a PIN, and links to a separate 'Change your PIN' article that was not read. The reply stops at selecting PIN (Windows Hello).",
    },
    {
        "id": "tr214-g",
        "messages": [
            u("What can a debt collector not do, and where do I report one who breaks the rules?"),
            a("In the U.S., the federal Fair Debt Collection Practices Act sets these rules for household debts like credit cards, medical bills, and car loans. Business debts aren't covered, and your state may have its own rules too. Collectors can't:\n\n"
              "1. Harass you, threaten to hurt you, or use obscene or profane language.\n"
              "2. Lie to you, for example about how much you owe, or pretend to be an attorney or from the government.\n"
              "3. Contact you before 8 a.m. or after 9 p.m., unless you agree to it.\n"
              "4. Call you more than seven times in seven days, or call within seven days after talking with you by phone about a particular debt.\n"
              "5. Generally, discuss your debt with anyone except you or your spouse.\n\n"
              "If a lawyer represents you, tell the collector. The collector then has to contact your lawyer, not you.\n\n"
              "To report a collector who breaks the rules, contact the FTC at **ReportFraud.ftc.gov**, the Consumer Financial Protection Bureau at **cfpb.gov/complaint**, or your state attorney general's office."),
        ],
        "sources": [FTC_DEBT],
        "follows": "Framed as U.S. federal law for household debts, with state laws noted. Frequency rule restated as the page gives it, including the seven days after a phone conversation about a particular debt. Added the attorney exception. Kept all three reporting routes.",
        "page_differs": "The FTC page attaches 'about a particular debt' only to the seven-days-after-a-call limit, not clearly to the seven-calls-in-seven-days limit, so the reply follows that wording.",
    },
    {
        "id": "tr218-e",
        "messages": [
            u("The email says it will send the video to all of my friends and family within a few hours unless I pay. It says if I tell anyone or report it, it will be sent sooner. I'm so embarrassed I can't tell anyone. Should I just pay to make it go away?"),
            a("No, please don't pay. This is a known scam, and there's nothing to be embarrassed about. These emails often claim the sender got into your computer or webcam, but an email saying they have a video is not proof that they do.\n\n"
              "1. Don't pay, and don't reply.\n"
              "2. If the email shows a real password, change that password now. If you used the same password anywhere else, change it there too.\n"
              "3. Report the email to the FTC at **ReportFraud.ftc.gov**. After you've reported it, delete it.\n\n"
              "The deadline of a few hours is there to rush and scare you. If the email includes an actual picture or video of you, tell me, because that needs different steps."),
        ],
        "sources": [FTC_BLACKMAIL],
        "follows": "Calls it a known scam and says a claim is not proof, instead of 'all talk'. Report before deleting. Password change now covers reused passwords. A real picture or video is handled as a separate case.",
        "page_differs": "",
    },
    {
        "id": "tr224-e",
        "messages": [
            u("They told me not to call my lender and not to tell my counselor, or it would ruin the deal. They want a cashier's check today for $1,500. I already got a foreclosure notice and I am scared. What do I do?"),
            a("Do not send the cashier's check. Scammers often tell you not to contact your lender or housing counselor, and no company can tell you to stop talking to your lender. Don't pay this company any fee before it delivers the results you want.\n\n"
              "Don't stop your regular mortgage payments on your own, and never send them to this company. You could lose your home and damage your credit if you stop paying your mortgage, so talk about your options with your lender or a housing counselor.\n\n"
              "1. Contact your servicer or lender right away. You can do this even if the foreclosure process has already started.\n"
              "2. Talk to a certified housing counselor for free. Find one on HUD's list of approved agencies at **apps.hud.gov/offices/hsg/sfh/hcc/hcs.cfm**, or call **1-888-995-HOPE (4673)**.\n"
              "3. Report this company to the FTC at **ReportFraud.ftc.gov**."),
        ],
        "sources": [FTC_MORTGAGE],
        "follows": "'Do not pay anything' narrowed to this company's fee. Says not to stop regular mortgage payments on one's own or send them to the company, and to discuss options with the lender or a counselor. Help routes kept; FTC reporting added.",
        "page_differs": "",
    },
]
