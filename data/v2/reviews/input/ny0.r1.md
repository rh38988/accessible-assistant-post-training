# Review input: batch ny0, round 1 (21 examples)

## tr117-a
- scenario: direct | style: plain | specification: fully_specified | platform: Mac
- task: Take a screenshot (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102646

**USER:**
How do I take a picture of my whole screen on my Mac?

**ASSISTANT:**
You can do this with three keys on the keyboard.

1. Press and release **Shift-Command-3** all together.
2. If a small picture appears in the corner of the screen, click it if you want to edit the screenshot.

If no small picture appears, the screenshot was saved on your desktop.

## tr117-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Mac
- task: Take a screenshot (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102646

**USER:**
My daughter set up this MacBook for me and my doctor's office sent me a long message in my email. I only want to save the small part with my appointment time, not the whole screen, because the rest has other stuff on it. How would I take a screenshot of just that part on my Mac?

**ASSISTANT:**
You can pick just the part you want.

1. Press and release **Shift-Command-4**. The pointer turns into a crosshair.
2. Click and hold the mouse or trackpad button.
3. Drag to cover the part with your appointment time.
4. Let go of the button to take the screenshot.

The picture is saved on your desktop unless a small picture appears in the corner, which you can click to edit it.

If you change your mind, press **Esc** before you let go and nothing is saved.

## tr117-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Take a screenshot (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102646

**USER:**
how do i take a picture of what is on my screen

**ASSISTANT:**
I can help with that. Is your computer a **Mac** or a **Windows** PC?

## tr117-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Mac
- task: Take a screenshot (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102646

**USER:**
how do i take a picture of what is on my screen

**ASSISTANT:**
I can help with that. Is your computer a **Mac** or a **Windows** PC?

**USER:**
its a mac

**ASSISTANT:**
Thanks. On a Mac, three keys take a picture of the whole screen.

1. Press and release **Shift-Command-3** all together.
2. If a small picture appears in the corner of the screen, you can click it to edit the screenshot.

If no small picture appears, the screenshot was saved on your desktop.

## tr117-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Mac
- task: Take a screenshot (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102646

**USER:**
I'm on a Mac and I want to screenshot my whole screen and paste it into an email to my son. I don't want a file left sitting on my desktop, I have too many already. Is there a way to skip that?

**ASSISTANT:**
Yes, you can copy the screenshot instead of saving it as a file.

1. Press and release **Control-Shift-Command-3** all together.

Adding the **Control** key sends the screenshot to the Clipboard instead of saving a file on your desktop.

If a small picture appears in the corner, you can also Control-click it and choose **Save to Clipboard**.

## tr117-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Mac
- task: Take a screenshot (Mac) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/102646

**USER:**
How do I screenshot my entire screen on my Mac?

**ASSISTANT:**
Here is how.

1. Press and release **Shift-Command-3** all together.
2. If a small picture appears in the corner, click it to edit the screenshot.

If it does not appear, the screenshot was saved on your desktop.

**USER:**
I pressed those keys but no little picture showed up. Where did it go?

**ASSISTANT:**
That is fine. Your screenshot was saved on your desktop.

1. Look on your desktop for a file named **Screen Shot**, followed by the date and time.
2. If you want to see the small picture next time, press **Shift-Command-5**, open the **Options** menu, and choose to show the floating thumbnail.

## tr118-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Back up the phone (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2819582?hl=en

**USER:**
How can I make my Android phone save a copy of everything automatically?

**ASSISTANT:**
You can turn on automatic backup in Settings.

1. Open the **Settings** app on your phone.
2. Tap **Google services**, then tap **All services**.
3. Choose what to save: **Photos & videos**, **Device data**, or both.
4. Turn **Backup** on.

When your data is saved, the word **On** shows under what you chose.

If **On** does not show up, wait. A backup can take up to 24 hours.

## tr118-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Android
- task: Back up the phone (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2819582?hl=en

**USER:**
My son told me I should save everything on my phone before I go to the store to get a new one next week. I have a Samsung Android phone and I never changed anything in the settings. I want to do a backup right now, today, so I know it is done. What do I press?

**ASSISTANT:**
You can start a backup yourself right now.

1. Open the **Settings** app.
2. Tap **Google**, then tap **All services**.
3. Under **Backup and restore**, tap **Backup**.
4. Tap **Back up now**.

This saves your apps, contacts, call history, settings, and text messages. Photos and videos are saved through Google Photos.

If you cannot find **Backup**, your phone may be a work phone, and backup does not work on those.

## tr118-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Back up the phone (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2819582?hl=en

**USER:**
I want to back up my phone so I don't lose my stuff

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

## tr118-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Back up the phone (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2819582?hl=en

**USER:**
I want to back up my phone so I don't lose my stuff

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

**USER:**
android

**ASSISTANT:**
You can back it up right now.

1. Open the **Settings** app.
2. Tap **Google**, then tap **All services**.
3. Under **Backup and restore**, tap **Backup**.
4. Tap **Back up now**.

If you do not see **Backup**, your phone may be a work phone, and backup does not work on those.

## tr118-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Android
- task: Back up the phone (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2819582?hl=en

**USER:**
I have an Android phone and I only care about my photos and videos of the grandkids. I don't need apps or contacts backed up, I just don't want to lose the pictures. Can I back up only those?

**ASSISTANT:**
Yes, you can choose only photos and videos.

1. Open the **Settings** app.
2. Tap **Google services**, then tap **All services**.
3. Choose **Photos & videos** only. Leave **Device data** unselected.
4. Turn **Backup** on.

When your photos and videos are saved, the word **On** shows below **Photos & videos**.

If **On** does not show, wait. It can take up to 24 hours.

## tr118-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Android
- task: Back up the phone (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/android/answer/2819582?hl=en

**USER:**
Please help me turn on backup on my Android phone so it saves my contacts and settings.

**ASSISTANT:**
Here is how to turn it on.

1. Open the **Settings** app.
2. Tap **Google services**, then tap **All services**.
3. Choose **Device data**.
4. Turn **Backup** on.

When your data is saved, the word **On** shows below it.

**USER:**
I did all that this morning but I don't see the word On under it. Did it work?

**ASSISTANT:**
It may just need more time. A backup can take up to 24 hours.

1. Wait and look again later today or tomorrow.
2. Check that you turned **Backup** on and that **Device data** is chosen.

The word **On** will appear below it once your data is saved.

## tr119-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Install an app from the Microsoft Store (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/help/4479732/get-apps-from-microsoft-store-on-windows-10-pc

**USER:**
My nephew put a new Windows 11 laptop on my desk and said I could pick up a few games from the Microsoft Store. I have the Store icon down on the bottom bar of the screen, I think. How would I look at the games the store has?

**ASSISTANT:**
You can start from that icon.

1. Select the **Microsoft Store** icon on the taskbar, the bar at the bottom of the screen.
2. In the Store, choose **Gaming**.
3. To see more games, select **Show all**.

Many games are free to download and play. Games you install update automatically.

If you do not see the icon, select **Start**, then select **Microsoft Store**.

## tr119-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Install an app from the Microsoft Store (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/help/4479732/get-apps-from-microsoft-store-on-windows-10-pc

**USER:**
my grandson said i can get a weather app for my computer from the store. how

**ASSISTANT:**
I can help with that. Is your computer a **Windows** PC or a **Mac**?

## tr119-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Install an app from the Microsoft Store (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/help/4479732/get-apps-from-microsoft-store-on-windows-10-pc

**USER:**
I got an app from the Microsoft Store last year on my old computer and now I have a new Windows 11 PC. I don't want to buy it again. How do I put it on this one?

**ASSISTANT:**
You can install it again from your Library, with no new purchase.

1. Select the **Microsoft Store** icon on the taskbar.
2. Select **More info** next to your account picture.
3. Select **My Library**.
4. Find your app. If it has a **Download** icon next to it, it has not been downloaded on this PC yet.
5. Select the **Download** icon.

Make sure you are signed in with the same Microsoft account you used before.

If you do not see the app, look in **Order history** for apps you have not installed.

## tr120-a
- scenario: direct | style: plain | specification: fully_specified | platform: any
- task: Someone urges the user to invest or pay with cryptocurrency (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams

**USER:**
A man I met online says he is an investment manager and wants me to buy cryptocurrency and send it to his site. He says I will make a lot of money. Is this real?

**ASSISTANT:**
Please do not buy or send any cryptocurrency. This is very likely a scam.

Scammers promise easy profits and steer people to send crypto to a fake investment account. The site can look real, but you may never be able to take your money out.

1. Do not click any more links from him or pay him.
2. Search his name and the crypto name with words like **review**, **scam**, or **complaint**.
3. Report him at **ReportFraud.ftc.gov**.

Nobody can truly guarantee profits.

## tr120-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: any
- task: Someone urges the user to invest or pay with cryptocurrency (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams

**USER:**
I got a text yesterday saying it was from the power company. It said my account has a legal problem and I have to buy cryptocurrency and send it today or they will shut off my power. I am a widow and I live alone and I am scared. I have not done anything yet. What should I do?

**ASSISTANT:**
Do not pay, and do not click the link in that text. Only scammers demand payment in cryptocurrency.

Scammers pretend to be utilities or government offices, claim there is a problem, and tell you to buy crypto to fix it. You have done nothing wrong.

1. Do not click any links in the text, even if it looks like it is from a company you know.
2. Do not send any money to the person who contacted you.
3. Report the text at **ReportFraud.ftc.gov**.

## tr120-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: any
- task: Someone urges the user to invest or pay with cryptocurrency (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams

**USER:**
A woman on a dating app has been teaching me to invest in crypto. Her website shows my money has doubled. She says I must add more by tonight or I lose my profits, but when I tried to take some out it would not let me. What do I do?

**ASSISTANT:**
Do not add any more money. This looks like an investment scam.

The site can look real but be fake, and scammers often make it hard to withdraw. A love interest who gives investment advice is a warning sign, and so is pressure to pay someone who contacted you first.

1. Stop sending money and stop clicking her links.
2. Report it at **ReportFraud.ftc.gov**.
3. You can also report it at **sec.gov/tcr** and **CFTC.gov/complaint**.
4. If you sent crypto already, contact the exchange you used.

## tr120-r
- scenario: already_acted | style: failure_recovery | specification: fully_specified | platform: any
- task: Someone urges the user to invest or pay with cryptocurrency (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams

**USER:**
I already sent a lot of cryptocurrency to a person I met on social media for an investment. Now they want more money to let me withdraw. Can I get my money back?

**ASSISTANT:**
Do not send anything more. I am sorry this happened. It is not your fault.

Crypto payments are usually not reversible. You can generally only get the money back if the person who received it sends it back, so please act quickly on these steps.

1. Contact the crypto exchange you used to send the money.
2. Report it at **ReportFraud.ftc.gov**.
3. Also report it at **CFTC.gov/complaint**, **sec.gov/tcr**, and **ic3.gov/Home/FileComplaint**.

## tr120-f
- scenario: helper | style: plain | specification: fully_specified | platform: any
- task: Someone urges the user to invest or pay with cryptocurrency (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams

**USER:**
My mother says someone who emailed her out of the blue is going to help her invest in a new coin. She wants to buy cryptocurrency and send it to him. How can I help her?

**ASSISTANT:**
Ask her not to send anything to him. This has the signs of a scam.

Unexpected contact from an "investment manager" is a warning sign. So is pressure to pay someone who contacted her first.

1. Ask her not to click links in that email or pay him.
2. Together, search his name and the coin name with words like **review**, **scam**, or **complaint**.
3. Report the email at **ReportFraud.ftc.gov**.
4. If she already sent crypto, contact the exchange she used.

## tr120-g
- scenario: prevention | style: plain | specification: fully_specified | platform: any
- task: Someone urges the user to invest or pay with cryptocurrency (any) | sensitive: True | reviewed by a person: False
- sources: https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams

**USER:**
How can I tell if a crypto investment offer is a scam, and where do I report one?

**ASSISTANT:**
Never pay anyone who contacts you out of the blue and asks for crypto. Only scammers demand payment in cryptocurrency.

Warning signs:
1. Guaranteed profits or big, quick returns.
2. Unexpected contact from a company, agency, or "investment manager".
3. A love interest who gives investment advice or asks for money.
4. Vague explanations of how the investment works.

Do not click links in unexpected texts, emails, or social media messages. Before investing, search the name and the crypto name with words like **review**, **scam**, or **complaint**.

To report, go to **ReportFraud.ftc.gov**.
