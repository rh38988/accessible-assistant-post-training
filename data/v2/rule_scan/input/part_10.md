# Rule scan input, part 10 (50 examples)

## tr109-a
- task: Stop the screen from turning sideways | platform: Android | scenario: direct | sensitive: False
- sources: Android Accessibility Help: How to make your screen rotate all by itself <https://support.google.com/accessibility/android/answer/6006961?hl=en>

**USER:**
How do I stop my Android phone screen from turning sideways?

**ASSISTANT:**
You can turn off auto-rotate. It takes a few seconds.

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Tap **Auto-rotate screen** to turn it off.

Now the screen will stay the way it is, even when you tilt the phone.

To let it turn again, for example when watching a video, turn **Auto-rotate screen** back on.

Menu names can be a little different on some phones. If you don't see **Display & touch**, tell me what you see in Settings.

---

## tr109-c
- task: Stop the screen from turning sideways | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Accessibility Help: How to make your screen rotate all by itself <https://support.google.com/accessibility/android/answer/6006961?hl=en>

**USER:**
rotate screen

**ASSISTANT:**
Sure. Is it an **iPhone** or an **Android** phone, and do you want the screen to **stop turning sideways**, or to **turn sideways** when it won't?

---

## tr109-d
- task: Stop the screen from turning sideways | platform: Android | scenario: followup | sensitive: False
- sources: Android Accessibility Help: How to make your screen rotate all by itself <https://support.google.com/accessibility/android/answer/6006961?hl=en>

**USER:**
screen keeps turning

**ASSISTANT:**
You can stop it from rotating. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android

**ASSISTANT:**
Thanks.

You can turn off auto-rotate. It takes a few seconds.

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Tap **Auto-rotate screen** to turn it off.

Now the screen will stay the way it is, even when you tilt the phone.

To let it turn again, for example when watching a video, turn **Auto-rotate screen** back on.

Menu names can be a little different on some phones. If you don't see **Display & touch**, tell me what you see in Settings.

---

## tr109-e
- task: Stop the screen from turning sideways | platform: Android | scenario: constraint | sensitive: False
- sources: Android Accessibility Help: How to make your screen rotate all by itself <https://support.google.com/accessibility/android/answer/6006961?hl=en>

**USER:**
I use TalkBack on my Android phone because my eyesight is poor. When I turn the phone in my hand the screen turns too and it interrupts the voice. How do I stop the screen rotating?

**ASSISTANT:**
Turning off auto-rotate is the right fix. If you use TalkBack, auto-rotate must be off, because turning the screen can interrupt the spoken voice.

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Select **Auto-rotate screen** to turn it off.

---

## tr109-r
- task: Stop the screen from turning sideways | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Accessibility Help: How to make your screen rotate all by itself <https://support.google.com/accessibility/android/answer/6006961?hl=en>

**USER:**
My Android screen won't stop turning when I tilt the phone. How do I turn that off?

**ASSISTANT:**
You can turn off auto-rotate. It takes a few seconds.

1. Open the **Settings** app.
2. Tap **Display & touch**.
3. Select **Auto-rotate screen** to turn it off.

**USER:**
I opened Settings but there is no Display & touch on my phone.

**ASSISTANT:**
I'm sorry about that. The steps I have use **Display & touch**, and I can't confirm another place for this setting on your phone.

For more accessibility help, you can reach the Disability Support team here: https://support.google.com/accessibility/answer/7641084

Tell me what you see in Settings and I'll try to help.

---

## tr110-a
- task: Restart a frozen iPhone | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Restart an unresponsive iPhone <https://support.apple.com/en-us/116940>

**USER:**
My iPhone is frozen and won't respond when I touch it. What do I do?

**ASSISTANT:**
You can **force restart** it. The steps depend on your model.

**iPhone with Face ID (no Home button):**
1. Press and quickly release the **volume up** button.
2. Press and quickly release the **volume down** button.
3. Press and **hold** the **side button** until you see the **Apple logo**. This can take more than 10 seconds, so keep holding.

**iPhone 7:** press and hold the **side button** and **volume down** together until you see the Apple logo.

**iPhone 6s or older (with a Home button):** press and hold the **Home button** and the **side or top button** together for about 10 seconds, until you see the Apple logo.

If it still won't turn on, charge it for an hour and try again.

---

## tr110-b
- task: Restart a frozen iPhone | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Restart an unresponsive iPhone <https://support.apple.com/en-us/116940>

**USER:**
my phone is stuck and won't do anything

**ASSISTANT:**
Let's get it working again. Is it an **iPhone** or an **Android** phone, and if it's an iPhone, does it have a round **Home button** below the screen?

---

## tr110-c
- task: Restart a frozen iPhone | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Restart an unresponsive iPhone <https://support.apple.com/en-us/116940>; Apple Support: If your iPhone or iPod touch won't charge <https://support.apple.com/en-ca/108805>

**USER:**
I was in the middle of a FaceTime with my grandson and the screen froze on his face. Nothing I press does anything and I can't even turn it off. It's an iPhone 14.

**ASSISTANT:**
That's frustrating. You can **force restart** it. On an iPhone 14, do this:

1. Press and quickly release the **volume up** button.
2. Press and quickly release the **volume down** button.
3. Press and **hold** the **side button** until you see the **Apple logo**. This can take more than 10 seconds, so keep holding.

If it still won't turn on, charge it for an hour and try again.

---

## tr110-d
- task: Restart a frozen iPhone | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Restart an unresponsive iPhone <https://support.apple.com/en-us/116940>

**USER:**
my phone is stuck and won't do anything

**ASSISTANT:**
Let's get it working again. Is it an **iPhone** or an **Android** phone, and if it's an iPhone, does it have a round **Home button** below the screen?

**USER:**
iPhone 12, no home button

**ASSISTANT:**
Thanks. Since your iPhone has no Home button, **force restart** it like this:

1. Press and quickly release the **volume up** button.
2. Press and quickly release the **volume down** button.
3. Press and **hold** the **side button** until you see the **Apple logo**. This can take more than 10 seconds, so keep holding.

If it still won't turn on, charge it for an hour and try again.

---

## tr110-e
- task: Restart a frozen iPhone | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Restart an unresponsive iPhone <https://support.apple.com/en-us/116940>

**USER:**
I have arthritis in my hands and I can't press two buttons at once. My iPhone has Face ID, it's frozen and the screen won't respond at all. Is there a way to restart it?

**ASSISTANT:**
Yes. For an iPhone with Face ID, you press one button at a time. No step needs two buttons together.

1. Press and quickly release the **volume up** button.
2. Press and quickly release the **volume down** button.
3. Press and **hold** the **side button** until you see the **Apple logo**. This might take longer than 10 seconds, so keep holding.

If it still doesn't turn on, charge it for one hour and try again. If it still won't turn on after that, it might need service.

---

## tr110-r
- task: Restart a frozen iPhone | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Restart an unresponsive iPhone <https://support.apple.com/en-us/116940>

**USER:**
My iPhone 7 froze and won't respond to anything. How do I restart it?

**ASSISTANT:**
For an iPhone 7, you force restart it with two buttons.

1. Press and hold the **side button** and the **volume down** button at the same time.
2. Keep holding both until you see the **Apple logo**. This might take longer than 10 seconds.

**USER:**
I held both for a long time and the screen is still black.

**ASSISTANT:**
Let's try charging it first.

1. Charge the iPhone for one hour.
2. Then try again: hold the **side button** and **volume down** together until you see the **Apple logo**.

If it still won't turn on, it might need service.

---

## tr111-a
- task: Phone is not charging | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: If your iPhone or iPod touch won't charge <https://support.apple.com/en-ca/108805>

**USER:**
My iPhone won't charge when I plug it in. What should I try?

**ASSISTANT:**
Let's go through a few checks. This can take up to an hour, mostly waiting.

1. **Restart your iPhone.**
2. **Check the cable and adapter** for damage, like breakage or bent prongs. Don't use a damaged one.
3. **Plug into a wall outlet** and make sure the cable, adapter, and outlet are firmly connected, or try a different outlet.
4. **Look in the charging port** on the bottom of the phone. If there's lint or dirt, carefully clear it out, then plug in firmly again.
5. **Leave it charging for half an hour.**
6. If it still won't turn on or only shows a battery picture, **force restart** it. On an iPhone 8 or later:
   - Press and quickly release **volume up**.
   - Press and quickly release **volume down**.
   - Press and hold the **side button** until you see the **Apple logo**.
   On an older iPhone, tell me the model and I'll give you those steps.
7. **Charge it for another half hour.**

If none of this works, it may need service from Apple.

**If it stops at 80%:** that's usually a battery-saving feature, not a problem.

---

## tr111-b
- task: Phone is not charging | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: If your iPhone or iPod touch won't charge <https://support.apple.com/en-ca/108805>

**USER:**
my phone won't charge

**ASSISTANT:**
Let's figure it out. Is your phone an **iPhone** or an **Android** phone, and does it **not charge at all** or **stop partway**?

---

## tr111-c
- task: Phone is not charging | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: If your iPhone or iPod touch won't charge <https://support.apple.com/en-ca/108805>

**USER:**
charger not

**ASSISTANT:**
It looks like your message got cut off. Is your phone **not charging**, and is it an **iPhone** or an **Android** phone?

---

## tr111-e
- task: Phone is not charging | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: If your iPhone or iPod touch won't charge <https://support.apple.com/en-ca/108805>

**USER:**
My iPhone 12 only shows a little picture of a battery and won't charge. I have just the one cable and charger, so I can't borrow another one. What can I do with only what I have?

**ASSISTANT:**
You can try these with your own cable and charger. This takes about an hour, mostly waiting.

1. Check the cable and the adapter for damage. If either is damaged, don't use it.
2. Plug into a wall outlet. Make sure the cable, the adapter, and the outlet connect firmly, or try a different outlet.
3. Look at the charging port on the bottom of the phone and remove any debris. Then plug the cable in firmly.
4. Let it charge for half an hour.
If it still won't turn on or still shows the battery picture, force restart it:
5. Press and quickly release the **volume up** button.
6. Press and quickly release the **volume down** button.
7. Press and **hold** the **side button** until you see the **Apple logo**.
8. Let it charge for another half hour.

If it still won't charge, it might need service.

---

## tr111-r
- task: Phone is not charging | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: If your iPhone or iPod touch won't charge <https://support.apple.com/en-ca/108805>

**USER:**
iPhone 11 isn't charging when I plug it in. What can I check?

**ASSISTANT:**
Let's go through some checks. This takes about an hour, mostly waiting.

1. Check the cable and the adapter for damage. Don't use damaged ones.
2. Plug into a wall outlet. Make sure everything connects firmly, or try a different outlet.
3. Remove any debris from the charging port on the bottom of the phone, then plug the cable in firmly.
4. Let it charge for half an hour.
If it still won't turn on or shows a battery picture, force restart it:
5. Press and quickly release **volume up**.
6. Press and quickly release **volume down**.
7. Press and **hold** the **side button** until you see the **Apple logo**.
8. Let it charge for another half hour.

**USER:**
Now it shows a message that the accessory is not supported or certified.

**ASSISTANT:**
Try these.

1. Plug the iPhone straight into the charger, with no adapters or other equipment in between.
2. Remove any debris from the charging port on the bottom of the phone.
3. Restart the iPhone.
4. Try a different USB cable or charger.

Also make sure your iPhone has the latest version of iOS. If it still won't charge, it might need service.

---

## tr117-a
- task: Take a screenshot | platform: Mac | scenario: direct | sensitive: False
- sources: Apple Support: How to take a screenshot on your Mac <https://support.apple.com/en-us/102646>

**USER:**
How do I take a picture of my whole screen on my Mac?

**ASSISTANT:**
You can do this with three keys on the keyboard.

1. Press and release **Shift-Command-3** all together.
2. If a small picture appears in the corner of the screen, click it if you want to edit the screenshot.

If no small picture appears, the screenshot was saved on your desktop.

---

## tr117-c
- task: Take a screenshot | platform: Mac | scenario: direct_messy | sensitive: False
- sources: Apple Support: How to take a screenshot on your Mac <https://support.apple.com/en-us/102646>

**USER:**
My daughter set up this MacBook for me and my doctor's office sent me a long message in my email. I only want to save the small part with my appointment time, not the whole screen, because the rest has other stuff on it. How would I take a screenshot of just that part on my Mac?

**ASSISTANT:**
You can pick just the part you want.

1. Press and release **Shift-Command-4**. The pointer turns into a crosshair.
2. Click and hold the mouse or trackpad button.
3. Drag to cover the part with your appointment time.
4. Let go of the button to take the screenshot.

A small picture may appear in the corner of the screen. You can click it to edit the screenshot, or wait and the screenshot is saved on your desktop.

If you change your mind, press **Esc** before you let go and nothing is saved.

---

## tr117-d
- task: Take a screenshot | platform: Mac | scenario: followup | sensitive: False
- sources: Apple Support: How to take a screenshot on your Mac <https://support.apple.com/en-us/102646>

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

---

## tr117-e
- task: Take a screenshot | platform: Mac | scenario: constraint | sensitive: False
- sources: Apple Support: How to take a screenshot on your Mac <https://support.apple.com/en-us/102646>

**USER:**
I'm on a Mac and I want to screenshot my whole screen and paste it into an email to my son. I don't want a file left sitting on my desktop, I have too many already. Is there a way to skip that?

**ASSISTANT:**
Yes, you can copy the screenshot instead of saving it as a file.

1. Press and release **Control-Shift-Command-3** all together.

Adding the **Control** key sends the screenshot to the Clipboard instead of saving a file on your desktop.

If a small picture appears in the corner, you can also Control-click it and choose **Save to Clipboard**.

---

## tr117-r
- task: Take a screenshot | platform: Mac | scenario: failure_recovery | sensitive: False
- sources: Apple Support: How to take a screenshot on your Mac <https://support.apple.com/en-us/102646>

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

---

## tr118-a
- task: Back up the phone | platform: Android | scenario: direct | sensitive: False
- sources: Android Help: Back up or restore data on your Android device <https://support.google.com/android/answer/2819582?hl=en>

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

---

## tr118-b
- task: Back up the phone | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Help: Back up or restore data on your Android device <https://support.google.com/android/answer/2819582?hl=en>

**USER:**
I want to back up my phone so I don't lose my stuff

**ASSISTANT:**
I can help with that. Is your phone an **iPhone** or an **Android** phone?

---

## tr118-c
- task: Back up the phone | platform: Android | scenario: direct_messy | sensitive: False
- sources: Android Help: Back up or restore data on your Android device <https://support.google.com/android/answer/2819582?hl=en>

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

---

## tr118-d
- task: Back up the phone | platform: Android | scenario: followup | sensitive: False
- sources: Android Help: Back up or restore data on your Android device <https://support.google.com/android/answer/2819582?hl=en>

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

---

## tr118-e
- task: Back up the phone | platform: Android | scenario: constraint | sensitive: False
- sources: Android Help: Back up or restore data on your Android device <https://support.google.com/android/answer/2819582?hl=en>

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

---

## tr118-r
- task: Back up the phone | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Help: Back up or restore data on your Android device <https://support.google.com/android/answer/2819582?hl=en>

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

---

## tr119-c
- task: Install an app from the Microsoft Store | platform: Windows 11 | scenario: direct_messy | sensitive: False
- sources: Microsoft Support: Get apps from Microsoft Store on your Windows PC <https://support.microsoft.com/en-us/help/4479732/get-apps-from-microsoft-store-on-windows-10-pc>

**USER:**
My nephew put a new Windows 11 laptop on my desk and said I could pick up a few games from the Microsoft Store. I have the Store icon down on the bottom bar of the screen, I think. How would I look at the games the store has?

**ASSISTANT:**
You can start from that icon.

1. Select the **Microsoft Store** icon on the taskbar, the bar at the bottom of the screen.
2. In the Store, choose **Gaming**.
3. To see more games, select **Show all**.

Many games are free to download and play. Games you install update automatically.

If you do not see the icon, select **Start**, then select **Microsoft Store**.

---

## tr119-e
- task: Install an app from the Microsoft Store | platform: Windows 11 | scenario: constraint | sensitive: False
- sources: Microsoft Support: Get apps from Microsoft Store on your Windows PC <https://support.microsoft.com/en-us/help/4479732/get-apps-from-microsoft-store-on-windows-10-pc>

**USER:**
I got an app from the Microsoft Store last year on my old computer and now I have a new Windows 11 PC. I don't want to buy it again. How do I put it on this one?

**ASSISTANT:**
You can look for it in your Library and download it again.

1. Select the **Microsoft Store** icon on the taskbar.
2. Select **More info** next to your account picture.
3. Select **My Library**.
4. Find your app. If it has a **Download** icon next to it, it has not been downloaded on this PC yet.
5. Select the **Download** icon.

If you do not see the app, look in **Order history** for apps you have not installed.

---

## tr120-a
- task: Someone urges the user to invest or pay with cryptocurrency | platform: any | scenario: direct | sensitive: True
- sources: FTC Consumer Advice: What To Know About Cryptocurrency and Scams <https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams>

**USER:**
A man I met online says he is an investment manager and wants me to buy cryptocurrency and send it to his site. He says I will make a lot of money. Is this real?

**ASSISTANT:**
Please do not buy or send any cryptocurrency. This is very likely a scam.

Scammers promise easy profits and steer people to send crypto to a fake investment account. The site can look real, but you may never be able to take your money out.

1. Do not click any more links from him or pay him.
2. Search his name and the crypto name with words like **review**, **scam**, or **complaint**.
3. Report him at **ReportFraud.ftc.gov**.

Nobody can truly guarantee profits.

---

## tr120-c
- task: Someone urges the user to invest or pay with cryptocurrency | platform: any | scenario: direct_messy | sensitive: True
- sources: FTC Consumer Advice: What To Know About Cryptocurrency and Scams <https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams>

**USER:**
I got a text yesterday saying it was from the power company. It said my account has a legal problem and I have to buy cryptocurrency and send it today or they will shut off my power. I am a widow and I live alone and I am scared. I have not done anything yet. What should I do?

**ASSISTANT:**
Do not pay, and do not click the link in that text. Only scammers demand payment in cryptocurrency.

Scammers pretend to be utilities or government offices, claim there is a problem, and tell you to buy crypto to fix it. You have done nothing wrong.

1. Do not click any links in the text, even if it looks like it is from a company you know.
2. Do not send any money to the person who contacted you.
3. Report the text at **ReportFraud.ftc.gov**.

---

## tr120-e
- task: Someone urges the user to invest or pay with cryptocurrency | platform: any | scenario: constraint | sensitive: True
- sources: FTC Consumer Advice: What To Know About Cryptocurrency and Scams <https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams>

**USER:**
A woman on a dating app has been teaching me to invest in crypto. Her website shows my money has doubled. She says I must add more by tonight or I lose my profits, but when I tried to take some out it would not let me. What do I do?

**ASSISTANT:**
Do not add any more money. This looks like an investment scam.

The site can look real but be fake, and scammers often make it hard to withdraw. A love interest who gives investment advice is a warning sign, and so is pressure to pay someone who contacted you first.

1. Stop sending money and stop clicking her links.
2. Report it at **ReportFraud.ftc.gov**.
3. You can also report it at **sec.gov/tcr** and **CFTC.gov/complaint**.
4. If you sent crypto already, contact the exchange you used.

---

## tr120-f
- task: Someone urges the user to invest or pay with cryptocurrency | platform: any | scenario: helper | sensitive: True
- sources: FTC Consumer Advice: What To Know About Cryptocurrency and Scams <https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams>

**USER:**
My mother says someone who emailed her out of the blue is going to help her invest in a new coin. She wants to buy cryptocurrency and send it to him. How can I help her?

**ASSISTANT:**
Ask her not to send anything to him. This has the signs of a scam.

Unexpected contact from an "investment manager" is a warning sign. So is pressure to pay someone who contacted her first.

1. Ask her not to click links in that email or pay him.
2. Together, search his name and the coin name with words like **review**, **scam**, or **complaint**.
3. Report the email at **ReportFraud.ftc.gov**.
4. If she already sent crypto, contact the exchange she used.

---

## tr120-g
- task: Someone urges the user to invest or pay with cryptocurrency | platform: any | scenario: prevention | sensitive: True
- sources: FTC Consumer Advice: What To Know About Cryptocurrency and Scams <https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams>

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

---

## tr120-r
- task: Someone urges the user to invest or pay with cryptocurrency | platform: any | scenario: already_acted | sensitive: True
- sources: FTC Consumer Advice: What To Know About Cryptocurrency and Scams <https://consumer.ftc.gov/articles/what-know-about-cryptocurrency-and-scams>

**USER:**
I already sent a lot of cryptocurrency to a person I met on social media for an investment. Now they want more money to let me withdraw. Can I get my money back?

**ASSISTANT:**
Do not send anything more. I am sorry this happened. It is not your fault.

Crypto payments are usually not reversible. You can generally only get the money back if the person who received it sends it back, so please act quickly on these steps.

1. Contact the crypto exchange you used to send the money.
2. Report it at **ReportFraud.ftc.gov**.
3. Also report it at **CFTC.gov/complaint**, **sec.gov/tcr**, and **ic3.gov/Home/FileComplaint**.

---

## tr121-a
- task: Take a screenshot | platform: iPad | scenario: direct | sensitive: False
- sources: Apple Support: Take a screenshot on your iPad <https://support.apple.com/102500>

**USER:**
How do I take a screenshot on my iPad? It is the newer kind with no round Home button.

**ASSISTANT:**
Here is how to take a screenshot on an iPad that has no Home button.

1. Press the top button and either volume button at the same time.
2. Quickly let go of both buttons.
3. A small picture of the screenshot shows in the lower-left corner for a moment. Tap it to open the screenshot, or swipe it left to dismiss it.

To find it later, open **Photos**, tap **Collections**, swipe up, tap **Media Types**, then tap **Screenshots**.

---

## tr121-c
- task: Take a screenshot | platform: iPad | scenario: direct_messy | sensitive: False
- sources: Apple Support: Take a screenshot on your iPad <https://support.apple.com/102500>

**USER:**
My neighbor sent me a recipe on my iPad and I want to keep a picture of it so I can look at it in the kitchen. My iPad is the older one with the round Home button at the bottom of the screen. My grandson told me about taking a screenshot but I forgot how. What do I press?

**ASSISTANT:**
Your iPad has a Home button, so here is how to do it.

1. Open the recipe so it is on the screen.
2. Press the top button and the Home button at the same time.
3. Quickly let go of both buttons.
4. A small picture of the screenshot shows in the lower-left corner for a moment. Tap it to open the screenshot, or swipe it left to dismiss it.

To find it later, open **Photos**, tap **Collections**, swipe up, tap **Media Types**, then tap **Screenshots**.

---

## tr121-d
- task: Take a screenshot | platform: iPad | scenario: followup | sensitive: False
- sources: Apple Support: Take a screenshot on your iPad <https://support.apple.com/102500>

**USER:**
I want to save a picture of what is on my iPad screen to show my daughter. How?

**ASSISTANT:**
I can help with that. Does your iPad have a round **Home button** at the bottom, or **no Home button**?

**USER:**
No button, the bottom is all smooth

**ASSISTANT:**
Thank you. Here is how to do it on an iPad with no Home button.

1. Press the top button and either volume button at the same time.
2. Quickly let go of both buttons.
3. A small picture of the screenshot shows in the lower-left corner for a moment. Tap it to open the screenshot, or swipe it left to dismiss it.

To find it later, open **Photos**, tap **Collections**, swipe up, tap **Media Types**, then tap **Screenshots**.

---

## tr121-r
- task: Take a screenshot | platform: iPad | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Take a screenshot on your iPad <https://support.apple.com/102500>

**USER:**
How do I take a screenshot on my iPad with a Home button?

**ASSISTANT:**
Here is how to take a screenshot on an iPad with a Home button.

1. Press the top button and the Home button at the same time.
2. Quickly let go of both buttons.
3. A small picture of the screenshot shows in the lower-left corner for a moment. Tap it to open the screenshot, or swipe it left to dismiss it.

If you do not tap the picture right away, it goes away on its own.

**USER:**
I did it but I was too slow and the little picture went away. Did I lose it?

**ASSISTANT:**
It is not lost, the little picture just goes away by itself. Here is where to find your screenshot.

1. Open **Photos**.
2. Tap **Collections**.
3. Swipe up, then tap **Media Types**.
4. Tap **Screenshots**.

---

## tr122-a
- task: Update the Mac's software (macOS) | platform: Mac | scenario: direct | sensitive: False
- sources: Apple Support: Update macOS on Mac <https://support.apple.com/en-us/108382>

**USER:**
How do I update the software on my MacBook?

**ASSISTANT:**
Here is how to update your Mac.

1. Click the **Apple** menu at the top left of the screen and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Software Update** on the right. Your Mac checks for updates by itself.
4. If an update is shown, click the button to update, upgrade, or restart now.
5. If asked, type your administrator password. This is the password you use to log in to your Mac.
6. Let it finish. Do not let the Mac go to sleep or close its lid. It may restart a few times and show a progress bar or a blank screen.

It is a good idea to back up your Mac before you install new software.

---

## tr122-b
- task: Update the Mac's software (macOS) | platform: Mac | scenario: missing_info | sensitive: False
- sources: Apple Support: Update macOS on Mac <https://support.apple.com/en-us/108382>

**USER:**
it says i need to update my apple thing. what do i do

**ASSISTANT:**
I can help with that. Which device is it: a **Mac**, an **iPhone**, or an **iPad**?

---

## tr122-c
- task: Update the Mac's software (macOS) | platform: Mac | scenario: direct_messy | sensitive: False
- sources: Apple Support: Update macOS on Mac <https://support.apple.com/en-us/108382>

**USER:**
Hello, my iMac keeps telling me something about software but I never know what to do and I do not want to break anything. My nephew set it up for me last year. I would like to update the macOS on it. Is there a quick way to get to the update screen using search instead of clicking through lots of menus?

**ASSISTANT:**
Yes, you can use search to get there.

1. Click the **Spotlight** or **Siri** icon in the menu bar at the top of the screen.
2. Type **Software Update** and open it from the results.
3. Your Mac checks for updates by itself. If one is shown, click the button to update, upgrade, or restart now.
4. If asked, type your administrator password. This is the password you use to log in to your Mac.
5. Let it finish. Do not let the Mac go to sleep. It may restart a few times and show a progress bar or a blank screen.

Before installing, it is wise to back up your Mac.

---

## tr122-d
- task: Update the Mac's software (macOS) | platform: Mac | scenario: followup | sensitive: False
- sources: Apple Support: Update macOS on Mac <https://support.apple.com/en-us/108382>

**USER:**
it says i need to update my apple thing. what do i do

**ASSISTANT:**
I can help with that. Which device is it: a **Mac**, an **iPhone**, or an **iPad**?

**USER:**
its my mac

**ASSISTANT:**
Thank you. Here is how to update your Mac. Before you install anything, it is a good idea to back up your Mac.

1. Click the **Apple** menu at the top left of the screen and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Software Update** on the right. Your Mac checks for updates by itself.
4. If an update is shown, click the button to update, upgrade, or restart now.
5. If asked, type your administrator password. This is the password you use to log in to your Mac.
6. Let it finish. Do not let the Mac go to sleep or close its lid.

---

## tr122-e
- task: Update the Mac's software (macOS) | platform: Mac | scenario: constraint | sensitive: False
- sources: Apple Support: Update macOS on Mac <https://support.apple.com/en-us/108382>

**USER:**
I am not ready to install anything on my Mac today because I am in the middle of tax paperwork. I only want to look and see whether an update is waiting for me, without actually installing it. How do I look?

**ASSISTANT:**
You can look without installing anything.

1. Click the **Apple** menu at the top left of the screen and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Software Update** on the right. Your Mac checks for updates by itself.
4. Read what it shows. If an update is waiting, you will see a button to update, upgrade, or restart now. Do not click it, and nothing will install.
5. If it says your Mac is up to date, there is nothing waiting.

---

## tr122-r
- task: Update the Mac's software (macOS) | platform: Mac | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Update macOS on Mac <https://support.apple.com/en-us/108382>

**USER:**
How do I check for a macOS update on my Mac?

**ASSISTANT:**
Here is how to check for an update on your Mac.

1. Click the **Apple** menu at the top left of the screen and choose **System Settings**.
2. Click **General** in the sidebar.
3. Click **Software Update** on the right. Your Mac checks for updates by itself.
4. If an update is shown, click the button to update, upgrade, or restart now.
5. If asked, type your administrator password.
6. Let it finish and do not close the lid.

**USER:**
It just says my Mac is up to date, but my friend has a newer version on hers. Is it wrong?

**ASSISTANT:**
It may not be wrong. Here is what to try.

1. Click **Check for Updates** to look again. You can also press Command-R, or close and reopen **Software Update**.
2. If it still says up to date, that may be because Software Update only shows updates that work with your Mac model. A newer version that does not work with your Mac will not be offered.

---

## tr123-a
- task: Connect to a Wi-Fi network | platform: Mac | scenario: direct | sensitive: False
- sources: Apple Support: Connect your Mac to the internet using Wi-Fi <https://support.apple.com/guide/mac-help/mchlp1180>

**USER:**
How do I connect my MacBook to the Wi-Fi at my house?

**ASSISTANT:**
Here is how to join a Wi-Fi network on your Mac. Make sure Wi-Fi is turned on and have the Wi-Fi password ready.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen. It is the Wi-Fi icon.
2. Click the name of your network in the list.
3. If it asks for a password, type it and click **Join**.

If you do not see your network in the list, click **Other Networks** to show the nearby networks.

---

## tr123-b
- task: Connect to a Wi-Fi network | platform: Mac | scenario: missing_info | sensitive: False
- sources: Apple Support: Connect your Mac to the internet using Wi-Fi <https://support.apple.com/guide/mac-help/mchlp1180>

**USER:**
my laptop is not on the internet, how do i get it on the wifi

**ASSISTANT:**
I can help with that. Is your laptop a **Mac** (MacBook) or a **Windows** laptop?

---

## tr123-c
- task: Connect to a Wi-Fi network | platform: Mac | scenario: direct_messy | sensitive: False
- sources: Apple Support: Connect your Mac to the internet using Wi-Fi <https://support.apple.com/guide/mac-help/mchlp1180>

**USER:**
My son set up a new router for me and he told me the network is hidden so my neighbors cannot see it. He wrote the network name and the password on a sticky note. Now my iMac will not find it anywhere in the list. How do I connect my iMac to a hidden network?

**ASSISTANT:**
For a hidden network, you type the name yourself. Make sure Wi-Fi is turned on, and have the network name, security type, and password from the sticky note ready.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen.
2. Click **Other Networks**.
3. Click **Other** at the bottom of the list.
4. In the **Network Name** box, type the network name from your sticky note.
5. Click the **Security** pop-up menu and choose the security type your network uses.
6. Fill in any other boxes that appear, such as a user name and the password, then click **Join**.

---

## tr123-d
- task: Connect to a Wi-Fi network | platform: Mac | scenario: followup | sensitive: False
- sources: Apple Support: Connect your Mac to the internet using Wi-Fi <https://support.apple.com/guide/mac-help/mchlp1180>

**USER:**
my laptop is not on the internet, how do i get it on the wifi

**ASSISTANT:**
I can help with that. Is your laptop a **Mac** (MacBook) or a **Windows** laptop?

**USER:**
macbook

**ASSISTANT:**
Thank you. Here is how to join a Wi-Fi network on your MacBook. Make sure Wi-Fi is turned on and have the Wi-Fi password ready.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen. It is the Wi-Fi icon.
2. Click the name of your network in the list.
3. If it asks for a password, type it and click **Join**.

If you do not see your network, click **Other Networks** to show the nearby networks.

---

## tr123-e
- task: Connect to a Wi-Fi network | platform: Mac | scenario: constraint | sensitive: False
- sources: Apple Support: Connect your Mac to the internet using Wi-Fi <https://support.apple.com/guide/mac-help/mchlp1180>

**USER:**
I am at the library with my MacBook and I do not want to dig around in settings, I get lost in there. Just tell me the quickest way to connect to the library Wi-Fi from the top of the screen.

**ASSISTANT:**
You can do it from the top of the screen, no settings needed. Make sure Wi-Fi is turned on.

1. Click the **Wi-Fi status menu** in the menu bar at the top of the screen. It is the Wi-Fi icon.
2. Click the library network in the list.
3. If it asks for a password, type it and click **Join**.

If you do not see the library network, click **Other Networks** to show the nearby networks.

---
