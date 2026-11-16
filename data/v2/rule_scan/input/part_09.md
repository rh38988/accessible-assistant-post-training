# Rule scan input, part 09 (50 examples)

## tr097-a
- task: Turn on live captions | platform: Android | scenario: direct | sensitive: False
- sources: Android Accessibility Help: Live Caption <https://support.google.com/accessibility/android/answer/9350862?hl=en>

**USER:**
How do I turn on Live Caption on my Android phone so I can read what people say in videos?

**ASSISTANT:**
**Live Caption** shows captions for videos and calls on your phone. It takes about a minute to turn on.

**Quick way:**
1. Press a **volume button** on the side of your phone.
2. Under the volume controls, tap **More**.
3. Tap **Live Caption**, then **Done**.

**In Settings:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Live Caption** and turn it on.

Connect to Wi-Fi the first time you use it, so your phone can download what it needs.

If you can't find **Live Caption**, search for it in Settings.

---

## tr097-b
- task: Turn on live captions | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Accessibility Help: Live Caption <https://support.google.com/accessibility/android/answer/9350862?hl=en>

**USER:**
I can't hear people on videos well, can my phone show the words?

**ASSISTANT:**
Yes, many phones can show captions for what's being said. Is your phone an **iPhone** or an **Android** phone?

---

## tr097-d
- task: Turn on live captions | platform: Android | scenario: followup | sensitive: False
- sources: Android Accessibility Help: Live Caption <https://support.google.com/accessibility/android/answer/9350862?hl=en>

**USER:**
I can't hear people on videos well, can my phone show the words?

**ASSISTANT:**
Yes, many phones can show captions for what's being said. Is your phone an **iPhone** or an **Android** phone?

**USER:**
Android, a Pixel

**ASSISTANT:**
Thanks. On Android, this is called Live Caption.

**Live Caption** shows captions for videos and calls on your phone. It takes about a minute to turn on.

**Quick way:**
1. Press a **volume button** on the side of your phone.
2. Under the volume controls, tap **More**.
3. Tap **Live Caption**, then **Done**.

**In Settings:**
1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Live Caption** and turn it on.

Connect to Wi-Fi the first time you use it, so your phone can download what it needs.

If you can't find **Live Caption**, search for it in Settings.

---

## tr097-e
- task: Turn on live captions | platform: Android | scenario: constraint | sensitive: False
- sources: Android Accessibility Help: Live Caption <https://support.google.com/accessibility/android/answer/9350862?hl=en>

**USER:**
The volume buttons on the side of my Android phone are broken and I can't press them at all. I'd like to turn on Live Caption so I can read what people say in my videos, but every guide I find starts with the volume button. Is there another way?

**ASSISTANT:**
Yes, you can do it without the volume buttons, from your settings.

1. Open **Settings**.
2. Tap **Accessibility**.
3. Tap **Live Caption** and turn it on.

Captions then appear for speech in audio playing on your phone. The first time you use it, your phone needs **Wi-Fi** to download the language pack.

---

## tr097-r
- task: Turn on live captions | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Accessibility Help: Live Caption <https://support.google.com/accessibility/android/answer/9350862?hl=en>

**USER:**
My hearing is going and I want my Android phone to show words on screen when someone is talking in a video. How do I turn on live captions with the volume button?

**ASSISTANT:**
Here is how.

1. Press a **volume button** on the side of the phone.
2. Under the volume controls, tap **More**.
3. Tap **Live Caption**.
4. Tap **Done**.

Captions then appear for speech in audio playing on your phone.

**USER:**
I pressed the volume button but I never saw a Live Caption choice. Now what?

**ASSISTANT:**
Try turning it on from your settings instead.

1. Open **Settings** and search for **Live Caption**. You can also tap **Accessibility** and then **Live Caption**.
2. Turn **Live Caption** on.

If you still don't see a Live Caption option anywhere, check with your phone's maker.

---

## tr098-a
- task: Make text bigger | platform: Windows 11 | scenario: direct | sensitive: False
- sources: Microsoft Support: Make text and apps bigger <https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64>

**USER:**
How do I make just the text bigger on my Windows 11 computer?

**ASSISTANT:**
You can make the text bigger without changing anything else. It takes about a minute.

1. Click the **Start** button, then **Settings**.
2. Click **Accessibility**.
3. Click **Text size**.
4. Drag the slider to the right until the sample text is easy to read.
5. Click **Apply**.

Windows will make the text bigger everywhere.

Tip: you can also open Accessibility settings by holding the **Windows logo key** and pressing **U**.

If you want everything bigger, including pictures and buttons, there's a separate **Scale** setting under **Display**. Tell me if you'd like that instead.

---

## tr098-c
- task: Make text bigger | platform: Windows 11 | scenario: missing_info | sensitive: False
- sources: Microsoft Support: Make text and apps bigger <https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64>

**USER:**
make text

**ASSISTANT:**
It looks like your message got cut off. Do you want to make the text bigger on a **computer** or on a **phone**?

---

## tr098-d
- task: Make text bigger | platform: Windows 11 | scenario: followup | sensitive: False
- sources: Microsoft Support: Make text and apps bigger <https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64>

**USER:**
the writing on my computer is too small

**ASSISTANT:**
I can help you make it bigger. Is your computer a **Windows** computer or a **Mac**?

**USER:**
Windows 11, just the text

**ASSISTANT:**
Got it.

You can make the text bigger without changing anything else. It takes about a minute.

1. Click the **Start** button, then **Settings**.
2. Click **Accessibility**.
3. Click **Text size**.
4. Drag the slider to the right until the sample text is easy to read.
5. Click **Apply**.

Windows will make the text bigger everywhere.

Tip: you can also open Accessibility settings by holding the **Windows logo key** and pressing **U**.

If you want everything bigger, including pictures and buttons, there's a separate **Scale** setting under **Display**. Tell me if you'd like that instead.

---

## tr098-e
- task: Make text bigger | platform: Windows 11 | scenario: constraint | sensitive: False
- sources: Microsoft Support: Make text and apps bigger <https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64>

**USER:**
My Windows 11 computer has tiny words in the menus and under the little pictures on my desktop. I don't want the pictures and everything else blown up, only the writing, or my screen will look too crowded. Can I do that?

**ASSISTANT:**
Yes. There is a setting that makes only the text bigger.

1. Press the **Windows logo key** and **U** together. This opens Accessibility settings. You can also select **Start**, then **Settings**, then **Accessibility**.
2. Select **Text size**.
3. Drag the **Text size** slider to the right. The sample text gets bigger as you move it.
4. Select **Apply**.

After you apply it, the text in title bars, menus, and icon labels gets larger.

---

## tr098-r
- task: Make text bigger | platform: Windows 11 | scenario: failure_recovery | sensitive: False
- sources: Microsoft Support: Make text and apps bigger <https://support.microsoft.com/en-us/topic/c3095a80-6edd-4779-9282-623c4d721d64>

**USER:**
Windows 11 laptop. I can't read the words on the screen. How do I make the text larger?

**ASSISTANT:**
Here is how.

1. Press the **Windows logo key** and **U** together to open Accessibility settings.
2. Select **Text size**.
3. Drag the **Text size** slider to the right.
4. Select **Apply**.

The sample text gets larger as you drag. After you select **Apply**, text in title bars, menus, and icon labels gets larger.

**USER:**
The words are bigger now, thank you, but the pictures and buttons are still small. Can I fix that too?

**ASSISTANT:**
Yes. Display scaling makes everything on the screen bigger, not just the text.

1. Press the **Windows logo key** and **I** together to open Settings.
2. Select **Display**.
3. Under **Scale & layout**, open the **Scale** menu and choose a bigger option.

Most changes happen right away. If an app still looks the same, you may need to sign out and sign back in.

---

## tr099-a
- task: iPhone stops charging at 80% | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: If your iPhone or iPod touch won't charge <https://support.apple.com/en-ca/108805>

**USER:**
Why does my iPhone stop charging at 80% overnight? Is something wrong with it?

**ASSISTANT:**
Most likely nothing is wrong. This is usually a feature called **Optimized Battery Charging**. It holds the battery at 80% during long charges, like overnight, to slow down battery wear. Your iPhone then finishes charging around the time you usually unplug it.

A couple of other things can also stop charging at 80%:
- **Heat:** if your iPhone gets too warm, it may pause charging above 80%. Moving it to a cooler spot helps.
- **Charge limit:** on iPhone 15 and newer, a charge limit setting may be turned on. You can change it if you want a full charge.

If you need a full charge right away, tell me and I'll walk you through it.

---

## tr099-b
- task: iPhone stops charging at 80% | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: If your iPhone or iPod touch won't charge <https://support.apple.com/en-ca/108805>

**USER:**
my phone won't charge all the way

**ASSISTANT:**
Let's figure out why. Is your phone an **iPhone** or an **Android** phone?

---

## tr099-c
- task: iPhone stops charging at 80% | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: If your iPhone or iPod touch won't charge <https://support.apple.com/en-ca/108805>

**USER:**
I plug in my iPhone every night before bed and when I wake up it says 80% and charging is on hold or something. I thought my charger was broken so I bought a new one but it does the same thing.

**ASSISTANT:**
Your charger is probably fine.

Most likely nothing is wrong. This is usually a feature called **Optimized Battery Charging**. It holds the battery at 80% during long charges, like overnight, to slow down battery wear. Your iPhone then finishes charging around the time you usually unplug it.

A couple of other things can also stop charging at 80%:
- **Heat:** if your iPhone gets too warm, it may pause charging above 80%. Moving it to a cooler spot helps.
- **Charge limit:** on iPhone 15 and newer, a charge limit setting may be turned on. You can change it if you want a full charge.

If you need a full charge right away, tell me and I'll walk you through it.

---

## tr099-d
- task: iPhone stops charging at 80% | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: If your iPhone or iPod touch won't charge <https://support.apple.com/en-ca/108805>

**USER:**
my phone won't charge all the way

**ASSISTANT:**
Let's figure out why. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone, it always stops at 80%

**ASSISTANT:**
Thanks, that detail helps.

Most likely nothing is wrong. This is usually a feature called **Optimized Battery Charging**. It holds the battery at 80% during long charges, like overnight, to slow down battery wear. Your iPhone then finishes charging around the time you usually unplug it.

A couple of other things can also stop charging at 80%:
- **Heat:** if your iPhone gets too warm, it may pause charging above 80%. Moving it to a cooler spot helps.
- **Charge limit:** on iPhone 15 and newer, a charge limit setting may be turned on. You can change it if you want a full charge.

If you need a full charge right away, tell me and I'll walk you through it.

---

## tr101-a
- task: Phone only vibrates, does not ring | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Use the volume buttons, side button, and other controls on your iPhone <https://support.apple.com/en-us/105103>

**USER:**
My iPhone only vibrates when someone calls. It doesn't ring. How do I fix that?

**ASSISTANT:**
Your iPhone is probably in **Silent mode**. Here's how to check.

**If your iPhone has a small switch on the side** (above the volume buttons):
1. Look at the switch. If you see **orange**, Silent mode is on.
2. Flip the switch so the orange no longer shows.

**If your iPhone has an Action button instead** (iPhone 15 Pro and newer):
1. **Press and hold** the **Action button** until you see Silent mode turn off at the top of the screen. By default, this button turns Silent mode on and off. If it's been set to do something else, tell me and we'll check another way.

Once Silent mode is off, your phone will ring again. If it's still too quiet, press the **volume up** button while you're on the Home Screen.

---

## tr101-c
- task: Phone only vibrates, does not ring | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Use the volume buttons, side button, and other controls on your iPhone <https://support.apple.com/en-us/105103>

**USER:**
phone wont ring just

**ASSISTANT:**
It sounds like your phone only vibrates when someone calls. Is it an **iPhone** or an **Android** phone?

---

## tr101-d
- task: Phone only vibrates, does not ring | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Use the volume buttons, side button, and other controls on your iPhone <https://support.apple.com/en-us/105103>

**USER:**
my phone isn't ringing, only buzzing

**ASSISTANT:**
That usually means a silent setting is on. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone 13

**ASSISTANT:**
Thanks.

Your iPhone is probably in **Silent mode**. Here's how to check.

1. Look at the switch on the side of your iPhone. If you see **orange**, Silent mode is on.
2. Flip the switch so the orange no longer shows.

Once Silent mode is off, your phone will ring again. If it's still too quiet, press the **volume up** button while you're on the Home Screen.

---

## tr101-e
- task: Phone only vibrates, does not ring | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Use the volume buttons, side button, and other controls on your iPhone <https://support.apple.com/en-us/105103>

**USER:**
I have a new iPhone 16. My calls only buzz and never ring. I looked all along the side for the little switch my old phone had and there isn't one, only a button. I'm afraid of pressing the wrong thing and messing it up. Is that button the cause?

**ASSISTANT:**
It could be. Your iPhone 16 doesn't have the old switch. It has an **Action button**, and by default the **Action button turns Silent mode on or off**.

1. Use the **Action button** to switch Silent mode off. Your iPhone vibrates for calls when Silent mode is on, and rings when it is off.
2. If it still seems quiet, go to your Home Screen and press the **volume up** button. When you aren't using another app, the volume buttons change the ringer volume.

You can set the Action button to do other things, like open the Camera or turn on the flashlight. If it was changed, it may not control Silent mode.

---

## tr101-r
- task: Phone only vibrates, does not ring | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Use the volume buttons, side button, and other controls on your iPhone <https://support.apple.com/en-us/105103>

**USER:**
My old iPhone 8 won't ring for calls, it only buzzes. What should I check?

**ASSISTANT:**
It may be in **Silent mode**. Check the small **Ring/Silent switch** on the side of your iPhone.

1. Look at the switch. If it shows **orange**, Silent mode is on.
2. Flip the switch so the orange no longer shows.

In Silent mode your iPhone vibrates for calls. Alarms you set in the Clock app still sound, and calls from favorite contacts still ring.

**USER:**
There's no orange showing now, but the ring is really quiet. What else can I do?

**ASSISTANT:**
Then turn up the ringer volume.

1. Go to your **Home Screen**. Don't be inside another app.
2. Press the **volume up** button on the side. When you are not using other apps, the volume buttons adjust the ringer volume.

---

## tr102-b
- task: Have the phone read the screen aloud | platform: Android | scenario: missing_info | sensitive: False
- sources: Android Accessibility Help: Use Select to Speak <https://support.google.com/accessibility/android/answer/7349565?hl=en>

**USER:**
is there a way to have my phone read things to me

**ASSISTANT:**
Most phones can. Is your phone an **iPhone** or an **Android** phone?

---

## tr102-e
- task: Have the phone read the screen aloud | platform: Android | scenario: constraint | sensitive: False
- sources: Android Accessibility Help: Use Select to Speak <https://support.google.com/accessibility/android/answer/7349565?hl=en>

**USER:**
I have an Android phone and Select to Speak is already working for me. My problem is that it stops reading when I leave the page. I'd like to start it reading a long article and then keep scrolling or open my other apps while it reads. Can it do that?

**ASSISTANT:**
Yes. There is a setting called **Read in background**.

1. Open **Settings**.
2. Tap **Accessibility**, then tap **Select to Speak**.
3. Tap **Settings**.
4. Turn on **Read in background**.

Now you can scroll or switch to other apps while it keeps reading.

---

## tr102-r
- task: Have the phone read the screen aloud | platform: Android | scenario: failure_recovery | sensitive: False
- sources: Android Accessibility Help: Use Select to Speak <https://support.google.com/accessibility/android/answer/7349565?hl=en>

**USER:**
My Android phone is a Samsung. I'd like it to read a web page out loud to me. How?

**ASSISTANT:**
You can use **Select to Speak**. Turn it on first.

1. Open **Settings**.
2. Tap **Accessibility**, then tap **Select to Speak**.
3. Turn on **Select to Speak shortcut**.

Then use it on the page:
1. Start it with a **2-finger swipe up** from the bottom of the screen, or tap the **Accessibility button**.
2. Tap the text you want to hear, or tap **Play** to hear everything.

**USER:**
I did that in my browser and it just sits there, nothing gets read.

**ASSISTANT:**
Select to Speak may not work with every mobile web browser. Also, it only reads readable text, like the text of a web page. Try this instead, which doesn't need Select to Speak:

1. **Select the text** on the page.
2. In the pop-up menu, tap **More**.
3. Tap **Read aloud**.

---

## tr103-b
- task: Set a reminder | platform: iPhone | scenario: missing_info | sensitive: False
- sources: Apple Support: Use Reminders on your iPhone, iPad, or iPod touch <https://support.apple.com/en-us/102484>

**USER:**
how do I get my phone to remind me to do something

**ASSISTANT:**
Sure. Is your phone an **iPhone** or an **Android** phone?

---

## tr103-r
- task: Set a reminder | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Use Reminders on your iPhone, iPad, or iPod touch <https://support.apple.com/en-us/102484>

**USER:**
Can my iPhone remind me to take my pills when I leave the house? I want it to go off when I walk out the door.

**ASSISTANT:**
Yes. A location reminder can do that.

1. Open the **Reminders** app.
2. Tap **+ New Reminder** and type **Take pills**.
3. Tap the **Location** button.
4. Pick a preset or tap **Custom**.
5. Choose **leaving**, and set the area around the place.

Your iPhone reminds you when you leave that place.

**USER:**
I set it up like that but this morning it never went off when I left.

**ASSISTANT:**
Location reminders need **Location Services** turned on.

1. Open **Settings** and tap **Privacy & Security**.
2. Tap **Location Services**, then turn it on.

---

## tr104-a
- task: Bookmark a website | platform: Chrome (computer) | scenario: direct | sensitive: False
- sources: Google Chrome Help: Create, find and edit bookmarks in Chrome, computer <https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
How do I bookmark a website in Chrome on my computer so I can find it again?

**ASSISTANT:**
Here's how to save it. It takes a few seconds.

1. Go to the website you want to save.
2. Click the **bookmark icon** to the right of the address bar at the top.

**To find it later:**
- If the **bookmarks bar** is showing, click the bookmark there. To show the bar, click **More** at the top right, then **Bookmarks and lists**, then **Show bookmarks bar**.
- Or click **More**, then **Bookmarks and lists**, then **Bookmark Manager** to see all your bookmarks.

---

## tr104-b
- task: Bookmark a website | platform: Chrome (computer) | scenario: missing_info | sensitive: False
- sources: Google Chrome Help: Create, find and edit bookmarks in Chrome, computer <https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
how do I save a website so I can find it later

**ASSISTANT:**
You can bookmark it. Which browser are you using, like **Chrome**, **Safari**, or **Edge**, and is it on a **computer** or a **phone**?

---

## tr104-c
- task: Bookmark a website | platform: Chrome (computer) | scenario: missing_info | sensitive: False
- sources: Google Chrome Help: Create, find and edit bookmarks in Chrome, computer <https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
save this website

**ASSISTANT:**
Sure. Which browser are you using, like **Chrome**, **Safari**, or **Edge**, and is it on a **computer** or a **phone**?

---

## tr104-e
- task: Bookmark a website | platform: Chrome (computer) | scenario: constraint | sensitive: False
- sources: Google Chrome Help: Create, find and edit bookmarks in Chrome, computer <https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
I have a lot of bookmarks in Chrome on my computer and I really don't want a bar taking up room across my screen. Last week I saved a recipe site and I just want to find it again by typing a word. Is that possible?

**ASSISTANT:**
Yes, you can search your bookmarks from the address bar. It takes a few seconds.

1. Open **Chrome** on your computer.
2. Click the address bar.
3. Type **@bookmarks**, then press **Tab** or **Space**.
4. Type a word from the site's name, like "recipe".
5. Click the bookmark in the list that appears.

You can also click **Search bookmarks** in the suggestions instead of typing @bookmarks.

If you would rather look through all of them, click **More** at the top right, then **Bookmarks and lists**, then **Bookmark Manager**, and click the bookmark there.

---

## tr104-r
- task: Bookmark a website | platform: Chrome (computer) | scenario: failure_recovery | sensitive: False
- sources: Google Chrome Help: Create, find and edit bookmarks in Chrome, computer <https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
I keep losing pages I like. How do I save a website in Chrome on my computer?

**ASSISTANT:**
Here's how to save a page. It takes a few seconds.

1. Go to the website you want to save.
2. Click the **bookmark icon** to the right of the address bar.

To find it later, look under the address bar. If the **bookmarks bar** is turned on, click the bookmark there.

**USER:**
I saved one but I don't see any bar under the address bar.

**ASSISTANT:**
The bar may just be turned off. Let's turn it on.

1. Click **More** at the top right of Chrome.
2. Click **Bookmarks and lists**.
3. Click **Show bookmarks bar**.

Your bookmark should now show in the bar. Click it to open the site.

You can also click **More**, then **Bookmarks and lists**, then **Bookmark Manager** to see all your bookmarks.

---

## tr105-a
- task: Unsubscribe from emails | platform: Gmail | scenario: direct | sensitive: False
- sources: Gmail Help: Unsubscribe from an email (computer) <https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop>; Gmail Help: Mark or unmark spam in Gmail (computer) <https://support.google.com/mail/answer/1366858>

**USER:**
I get too many newsletter emails in Gmail. How do I unsubscribe on my computer?

**ASSISTANT:**
Gmail can unsubscribe you in a couple of clicks. It takes a few seconds per sender.

1. Go to **mail.google.com**.
2. Open an email from the sender.
3. Click **Unsubscribe** next to the sender's name at the top.
4. Click **Unsubscribe** again in the box that pops up.

If you see **Go to website** instead, that sender needs you to unsubscribe on their own site.

To see all your subscriptions at once, click **More** on the left side, then **Manage subscriptions**.

If you're not sure an email is from a sender you trust, don't reply or open any links in it. It can take a few days for the emails to stop.

---

## tr105-b
- task: Unsubscribe from emails | platform: Gmail | scenario: missing_info | sensitive: False
- sources: Gmail Help: Unsubscribe from an email (computer) <https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
how do I stop getting so many emails

**ASSISTANT:**
There are a few ways. Which email do you use, like **Gmail**, and are the emails from **stores or newsletters** you signed up for, or from **strangers**?

---

## tr105-c
- task: Unsubscribe from emails | platform: Gmail | scenario: direct_messy | sensitive: False
- sources: Gmail Help: Unsubscribe from an email (computer) <https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop>; Gmail Help: Mark or unmark spam in Gmail (computer) <https://support.google.com/mail/answer/1366858>

**USER:**
Every store I've ever bought anything from sends me emails every single day. My inbox has 4,000 unread messages and I can't find the important ones from my family. I use Gmail on my computer.

**ASSISTANT:**
That's a lot of clutter. Unsubscribing stops new ones from piling up, and Gmail can do it in a couple of clicks per sender.

1. Go to **mail.google.com**.
2. Open an email from the sender.
3. Click **Unsubscribe** next to the sender's name at the top.
4. Click **Unsubscribe** again in the box that pops up.

If you see **Go to website** instead, that sender needs you to unsubscribe on their own site.

To see all your subscriptions at once, click **More** on the left side, then **Manage subscriptions**.

If you're not sure an email is from a sender you trust, don't reply or open any links in it. It can take a few days for the emails to stop.

---

## tr105-d
- task: Unsubscribe from emails | platform: Gmail | scenario: followup | sensitive: False
- sources: Gmail Help: Unsubscribe from an email (computer) <https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop>; Gmail Help: Mark or unmark spam in Gmail (computer) <https://support.google.com/mail/answer/1366858>

**USER:**
how do I stop getting so many emails

**ASSISTANT:**
There are a few ways. Which email do you use, like **Gmail**, and are the emails from **stores or newsletters** you signed up for, or from **strangers**?

**USER:**
Newsletters from stores. Gmail.

**ASSISTANT:**
Thanks. For store newsletters, unsubscribing is the way to go.

Gmail can unsubscribe you in a couple of clicks. It takes a few seconds per sender.

1. Go to **mail.google.com**.
2. Open an email from the sender.
3. Click **Unsubscribe** next to the sender's name at the top.
4. Click **Unsubscribe** again in the box that pops up.

If you see **Go to website** instead, that sender needs you to unsubscribe on their own site.

To see all your subscriptions at once, click **More** on the left side, then **Manage subscriptions**.

If you're not sure an email is from a sender you trust, don't reply or open any links in it. It can take a few days for the emails to stop.

---

## tr105-e
- task: Unsubscribe from emails | platform: Gmail | scenario: constraint | sensitive: False
- sources: Gmail Help: Unsubscribe from an email (computer) <https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
I only use Gmail on my laptop and I don't want to visit any other websites or sign up for anything new. Can I stop a store's emails just from inside Gmail?

**ASSISTANT:**
You can try it right inside Gmail. It takes a few seconds.

1. Go to **mail.google.com**.
2. Open an email from that store.
3. Click **Unsubscribe** next to the sender's name.
4. In the box that pops up, click **Unsubscribe**.

Some senders require you to unsubscribe on their own website. For those, you will see **Go to website** instead, and Gmail can't finish it for you inside the email.

After you unsubscribe, emails may keep arriving for a few days.

---

## tr105-r
- task: Unsubscribe from emails | platform: Gmail | scenario: failure_recovery | sensitive: False
- sources: Gmail Help: Unsubscribe from an email (computer) <https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop>; Gmail Help: Manage subscriptions (computer) <https://support.google.com/mail/answer/15621070?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
Gmail on my computer. How do I stop the emails from a clothing store?

**ASSISTANT:**
Gmail can do it in a few clicks.

1. Go to **mail.google.com**.
2. Open an email from the store.
3. Click **Unsubscribe** next to the sender's name.
4. In the box that pops up, click **Unsubscribe**.

If you see **Go to website** instead, that sender needs you to unsubscribe on their own site. Emails may keep arriving for a few days.

**USER:**
I did that last week and the store still sends me emails.

**ASSISTANT:**
That can happen. Unsubscribing from one email may only remove you from one of the sender's mailing lists, so the store may have other lists.

1. Go to **mail.google.com**.
2. On the left, click **More**.
3. Click **Manage subscriptions**.
4. Find the store in the list. On the right, next to the number of recent emails from the store, click **Unsubscribe**.

It can take a few days for the emails to stop.

---

## tr106-a
- task: Get back a deleted email | platform: Gmail | scenario: direct | sensitive: False
- sources: Gmail Help: Delete or recover deleted Gmail messages (computer) <https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
I accidentally deleted an important email in Gmail. How do I get it back? I'm on my computer.

**ASSISTANT:**
If it was deleted in the last 30 days, it should be in your **Trash**. Here's how to get it back.

1. Open **Gmail** in your web browser.
2. On the left side, click **More**, then click **Trash**.
3. Find the email and check the box next to it.
4. At the top, click **Move to**.
5. Choose **Inbox**.

The email will be back in your inbox.

Emails stay in Trash for up to 30 days. After that, they're deleted for good and can't be recovered.

---

## tr106-b
- task: Get back a deleted email | platform: Gmail | scenario: missing_info | sensitive: False
- sources: Gmail Help: Delete or recover deleted Gmail messages (computer) <https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
I deleted something by accident

**ASSISTANT:**
Don't worry, it can often be recovered. What did you delete, like an email, a photo, or a file, and on which device or app?

---

## tr106-d
- task: Get back a deleted email | platform: Gmail | scenario: followup | sensitive: False
- sources: Gmail Help: Delete or recover deleted Gmail messages (computer) <https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
I deleted something by accident

**ASSISTANT:**
Don't worry, it can often be recovered. What did you delete, like an email, a photo, or a file, and on which device or app?

**USER:**
An email in Gmail, on my computer

**ASSISTANT:**
Good news: Gmail keeps deleted emails for a while.

If it was deleted in the last 30 days, it should be in your **Trash**. Here's how to get it back.

1. Open **Gmail** in your web browser.
2. On the left side, click **More**, then click **Trash**.
3. Find the email and check the box next to it.
4. At the top, click **Move to**.
5. Choose **Inbox**.

The email will be back in your inbox.

Emails stay in Trash for up to 30 days. After that, they're deleted for good and can't be recovered.

---

## tr106-e
- task: Get back a deleted email | platform: Gmail | scenario: constraint | sensitive: False
- sources: Gmail Help: Delete or recover deleted Gmail messages (computer) <https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
I was writing a long email in Gmail on my computer. It was a draft, I never sent it, and I think I deleted it by mistake. I'd really like it back in my inbox, please.

**ASSISTANT:**
I'm sorry, but a deleted draft can't be recovered from Trash, so I can't offer a way to bring it back.

If you also deleted other emails (not drafts) in the last 30 days, you can get those back.

1. Go to **mail.google.com**.
2. On the left, click **More**, then click **Trash**.
3. Check the box next to the email.
4. At the top, click **Move to**.
5. Choose **Inbox**.

---

## tr106-r
- task: Get back a deleted email | platform: Gmail | scenario: failure_recovery | sensitive: False
- sources: Gmail Help: Delete or recover deleted Gmail messages (computer) <https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
I deleted an email in Gmail on my computer last week by accident. How do I get it back?

**ASSISTANT:**
Deleted emails stay in **Trash** for up to 30 days, so it may still be there.

1. Go to **mail.google.com**.
2. On the left, click **More**, then click **Trash**.
3. Check the box next to the email.
4. At the top, click **Move to**.
5. Choose **Inbox**.

**USER:**
I opened Trash but the email isn't there.

**ASSISTANT:**
I'm sorry. Check that you are looking in the right place: on the left, click **More**, then **Trash**.

If it still isn't there, it may have been removed for good. Emails are permanently deleted after 30 days, and **Delete forever** or **Empty Trash now** can't be undone. Deleted drafts also can't be recovered from Trash. Once an email is permanently deleted, it can't be recovered.

---

## tr107-a
- task: Mark an email as spam | platform: Gmail | scenario: direct | sensitive: True
- sources: Gmail Help: Report spam in Gmail (computer) <https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer>

**USER:**
How do I mark an email as spam in Gmail on my computer?

**ASSISTANT:**
Here's how. It takes a few seconds.

1. Open **Gmail** in your web browser.
2. Check the box next to the email.
3. Click the **Report spam** icon at the top.

The email moves to your **Spam** folder, and Google gets a copy, which helps it spot similar spam.

A couple of notes:
- If it's from a store or newsletter you signed up for, **Unsubscribe** is usually better.
- If the email is trying to **trick you into giving a password or account number**, that's phishing. Don't click any links or reply.

---

## tr107-b
- task: Mark an email as spam | platform: Gmail | scenario: missing_info | sensitive: True
- sources: Gmail Help: Report spam in Gmail (computer) <https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer>

**USER:**
how do I get rid of junk email

**ASSISTANT:**
I can help. Which email do you use, like **Gmail**, and are you on a **computer** or a **phone**?

---

## tr107-c
- task: Mark an email as spam | platform: Gmail | scenario: missing_info | sensitive: True
- sources: Gmail Help: Report spam in Gmail (computer) <https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer>

**USER:**
spam

**ASSISTANT:**
Sure. Do you mean **spam emails**, **spam texts**, or **spam calls**? I can help with any of them.

---

## tr107-d
- task: Mark an email as spam | platform: Gmail | scenario: followup | sensitive: True
- sources: Gmail Help: Report spam in Gmail (computer) <https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer>

**USER:**
how do I get rid of junk email

**ASSISTANT:**
I can help. Which email do you use, like **Gmail**, and are you on a **computer** or a **phone**?

**USER:**
Gmail on my computer

**ASSISTANT:**
Thanks.

Here's how. It takes a few seconds.

1. Open **Gmail** in your web browser.
2. Check the box next to the email.
3. Click the **Report spam** icon at the top.

The email moves to your **Spam** folder, and Google gets a copy, which helps it spot similar spam.

A couple of notes:
- If it's from a store or newsletter you signed up for, **Unsubscribe** is usually better.
- If the email is trying to **trick you into giving a password or account number**, that's phishing. Don't click any links or reply.

---

## tr107-e
- task: Mark an email as spam | platform: Gmail | scenario: constraint | sensitive: True
- sources: Gmail Help: Report spam in Gmail (computer) <https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer>

**USER:**
I have about ten junk emails sitting in my Gmail inbox on my computer and I really don't want to click on each one and report it separately. Can I report them all together?

**ASSISTANT:**
Yes, you can select several emails and report them at the same time.

1. Open **Gmail** in your web browser.
2. Check the box next to each junk email.
3. At the top, click the **Report spam** icon.

Reporting sends Google a copy of the emails, which it may analyze.

---

## tr108-a
- task: Stop the screen from turning sideways | platform: iPhone | scenario: direct | sensitive: False
- sources: Apple Support: Rotate the screen on your iPhone or iPod touch <https://support.apple.com/en-us/118226>; Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro <https://support.apple.com/en-us/105001>

**USER:**
My iPhone screen keeps turning sideways when I'm reading in bed. How do I make it stay upright?

**ASSISTANT:**
You can lock the screen so it stays upright. It takes a few seconds.

1. Open **Control Center**: on an iPhone with Face ID, **swipe down from the top-right corner**. On an iPhone with a Home button, **swipe up from the bottom edge**.
2. Tap the **Portrait Orientation Lock** button.
3. Close Control Center.

Now the screen will stay upright even when you tilt the phone.

To let it turn sideways again, for example to watch a video, tap the same button.

---

## tr108-c
- task: Stop the screen from turning sideways | platform: iPhone | scenario: direct_messy | sensitive: False
- sources: Apple Support: Rotate the screen on your iPhone or iPod touch <https://support.apple.com/en-us/118226>; Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro <https://support.apple.com/en-us/105001>

**USER:**
I like to read the news on my iPhone lying on my side in bed, but the screen keeps flipping sideways and it drives me nuts.

**ASSISTANT:**
That sounds annoying. You can lock the screen so it stays upright. It takes a few seconds.

1. Open **Control Center**: on an iPhone with Face ID, **swipe down from the top-right corner**. On an iPhone with a Home button, **swipe up from the bottom edge**.
2. Tap the **Portrait Orientation Lock** button.
3. Close Control Center.

Now the screen will stay upright even when you tilt the phone.

To let it turn sideways again, for example to watch a video, tap the same button.

---

## tr108-d
- task: Stop the screen from turning sideways | platform: iPhone | scenario: followup | sensitive: False
- sources: Apple Support: Rotate the screen on your iPhone or iPod touch <https://support.apple.com/en-us/118226>; Apple Support: Turn the flashlight on or off on your iPhone or iPad Pro <https://support.apple.com/en-us/105001>

**USER:**
my screen keeps flipping when I lie down

**ASSISTANT:**
You can lock the screen so it stays upright. Is your phone an **iPhone** or an **Android** phone?

**USER:**
iPhone

**ASSISTANT:**
Thanks.

You can lock the screen so it stays upright. It takes a few seconds.

1. Open **Control Center**: on an iPhone with Face ID, **swipe down from the top-right corner**. On an iPhone with a Home button, **swipe up from the bottom edge**.
2. Tap the **Portrait Orientation Lock** button.
3. Close Control Center.

Now the screen will stay upright even when you tilt the phone.

To let it turn sideways again, for example to watch a video, tap the same button.

---

## tr108-e
- task: Stop the screen from turning sideways | platform: iPhone | scenario: constraint | sensitive: False
- sources: Apple Support: Rotate the screen on your iPhone or iPod touch <https://support.apple.com/en-us/118226>; Apple Support: Use Control Center on your iPhone or iPod touch <https://support.apple.com/en-us/108330>

**USER:**
I have an older iPhone 8 with the round Home button. I read in bed and want the page to stay upright, but later I'll want it to turn sideways again for photos. Can I do both?

**ASSISTANT:**
Yes, you can lock it now and turn the lock off later. This takes a few seconds.

1. Swipe up from the bottom edge of the screen to open **Control Center**.
2. Tap the **Portrait Orientation Lock** button.
3. Tap the top of the screen or press the Home button to close Control Center.

When you want the screen to turn sideways again:

1. Open **Control Center** again.
2. Tap the **Portrait Orientation Lock** button to make sure it's off.
3. Tap the top of the screen or press the Home button to close it.
4. Turn the iPhone sideways.

Some apps don't support turning sideways, so the screen may stay upright in those even with the lock off.

---

## tr108-r
- task: Stop the screen from turning sideways | platform: iPhone | scenario: failure_recovery | sensitive: False
- sources: Apple Support: Rotate the screen on your iPhone or iPod touch <https://support.apple.com/en-us/118226>; Apple Support: Use Control Center on your iPhone or iPod touch <https://support.apple.com/en-us/108330>

**USER:**
iPhone 13 here. The screen keeps flipping sideways while I read. Help?

**ASSISTANT:**
You can lock the screen so it stays upright.

1. **Swipe down from the top-right corner** of the screen to open **Control Center**.
2. Tap the **Portrait Orientation Lock** button.
3. Close Control Center.

**USER:**
I swiped down from the top but I can't find any button.

**ASSISTANT:**
Control Center opens from the corner, not the middle of the top edge.

1. Put your finger on the **top-right corner** of the screen.
2. Swipe down from there to open **Control Center**.
3. Tap the **Portrait Orientation Lock** button.
4. Close Control Center.

---
