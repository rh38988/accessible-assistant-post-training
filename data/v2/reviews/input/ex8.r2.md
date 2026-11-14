# Review input: batch ex8, round 2 (22 examples)

## tr104-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chrome (computer)
- task: Bookmark a website (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
How do I bookmark a website in Chrome on my computer so I can find it again?

**ASSISTANT:**
Here's how to save it. It takes a few seconds.

1. Go to the website you want to save.
2. Click the **bookmark icon** to the right of the address bar at the top.

**To find it later:**
- If the **bookmarks bar** is showing, click the bookmark there. To show the bar, click **More** at the top right, then **Bookmarks and lists**, then **Show bookmarks bar**.
- Or click **More**, then **Bookmarks and lists**, then **Bookmark Manager** to see all your bookmarks.

## tr104-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Bookmark a website (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
how do I save a website so I can find it later

**ASSISTANT:**
You can bookmark it. Which browser are you using, like **Chrome**, **Safari**, or **Edge**, and is it on a **computer** or a **phone**?

## tr104-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Bookmark a website (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
save this website

**ASSISTANT:**
Sure. Which browser are you using, like **Chrome**, **Safari**, or **Edge**, and is it on a **computer** or a **phone**?

## tr104-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chrome (computer)
- task: Bookmark a website (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
how do I save a website so I can find it later

**ASSISTANT:**
You can bookmark it. Which browser are you using, like **Chrome**, **Safari**, or **Edge**, and is it on a **computer** or a **phone**?

**USER:**
Chrome on my computer

**ASSISTANT:**
Thanks.

Here's how to save it. It takes a few seconds.

1. Go to the website you want to save.
2. Click the **bookmark icon** to the right of the address bar at the top.

**To find it later:**
- If the **bookmarks bar** is showing, click the bookmark there. To show the bar, click **More** at the top right, then **Bookmarks and lists**, then **Show bookmarks bar**.
- Or click **More**, then **Bookmarks and lists**, then **Bookmark Manager** to see all your bookmarks.

## tr105-a
- scenario: direct | style: plain | specification: fully_specified | platform: Gmail
- task: Unsubscribe from emails (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop ; https://support.google.com/mail/answer/1366858

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

## tr105-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Unsubscribe from emails (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
how do I stop getting so many emails

**ASSISTANT:**
There are a few ways. Which email do you use, like **Gmail**, and are the emails from **stores or newsletters** you signed up for, or from **strangers**?

## tr105-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Gmail
- task: Unsubscribe from emails (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop ; https://support.google.com/mail/answer/1366858

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

## tr105-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Gmail
- task: Unsubscribe from emails (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop ; https://support.google.com/mail/answer/1366858

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

## tr106-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Get back a deleted email (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
I deleted something by accident

**ASSISTANT:**
Don't worry, it can often be recovered. What did you delete, like an email, a photo, or a file, and on which device or app?

## tr106-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Get back a deleted email (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
deleted email from my

**ASSISTANT:**
It looks like your message got cut off. Which email do you use, like **Gmail**, and are you on a **computer** or a **phone**?

## tr107-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Mark an email as spam (Gmail) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer

**USER:**
how do I get rid of junk email

**ASSISTANT:**
I can help. Which email do you use, like **Gmail**, and are you on a **computer** or a **phone**?

## tr108-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Stop the screen from turning sideways (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118226 ; https://support.apple.com/en-us/105001

**USER:**
My iPhone screen keeps turning sideways when I'm reading in bed. How do I make it stay upright?

**ASSISTANT:**
You can lock the screen so it stays upright. It takes a few seconds.

1. Open **Control Center**: on an iPhone with Face ID, **swipe down from the top-right corner**. On an iPhone with a Home button, **swipe up from the bottom edge**.
2. Tap the **Portrait Orientation Lock** button.
3. Close Control Center.

Now the screen will stay upright even when you tilt the phone.

To let it turn sideways again, for example to watch a video, tap the same button.

## tr108-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Stop the screen from turning sideways (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118226 ; https://support.apple.com/en-us/105001

**USER:**
I like to read the news on my iPhone lying on my side in bed, but the screen keeps flipping sideways and it drives me nuts.

**ASSISTANT:**
That sounds annoying. You can lock the screen so it stays upright. It takes a few seconds.

1. Open **Control Center**: on an iPhone with Face ID, **swipe down from the top-right corner**. On an iPhone with a Home button, **swipe up from the bottom edge**.
2. Tap the **Portrait Orientation Lock** button.
3. Close Control Center.

Now the screen will stay upright even when you tilt the phone.

To let it turn sideways again, for example to watch a video, tap the same button.

## tr108-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Stop the screen from turning sideways (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118226 ; https://support.apple.com/en-us/105001

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

## tr109-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Stop the screen from turning sideways (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/6006961?hl=en

**USER:**
rotate screen

**ASSISTANT:**
Sure. Is it an **iPhone** or an **Android** phone, and do you want the screen to **stop turning sideways**, or to **turn sideways** when it won't?

## tr110-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Restart a frozen iPhone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/116940

**USER:**
my phone is stuck and won't do anything

**ASSISTANT:**
Let's get it working again. Is it an **iPhone** or an **Android** phone, and if it's an iPhone, does it have a round **Home button** below the screen?

## tr110-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Restart a frozen iPhone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/116940 ; https://support.apple.com/en-ca/108805

**USER:**
I was in the middle of a FaceTime with my grandson and the screen froze on his face. Nothing I press does anything and I can't even turn it off. It's an iPhone 14.

**ASSISTANT:**
That's frustrating. You can **force restart** it. On an iPhone 14, do this:

1. Press and quickly release the **volume up** button.
2. Press and quickly release the **volume down** button.
3. Press and **hold** the **side button** until you see the **Apple logo**. This can take more than 10 seconds, so keep holding.

If it still won't turn on, charge it for an hour and try again.

## tr110-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Restart a frozen iPhone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/116940

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

## tr111-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Phone is not charging (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

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

## tr111-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Phone is not charging (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
my phone won't charge

**ASSISTANT:**
Let's figure it out. Is your phone an **iPhone** or an **Android** phone, and does it **not charge at all** or **stop partway**?

## tr111-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Phone is not charging (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
charger not

**ASSISTANT:**
It looks like your message got cut off. Is your phone **not charging**, and is it an **iPhone** or an **Android** phone?

## tr111-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Phone is not charging (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
my phone won't charge

**ASSISTANT:**
Let's figure it out. Is your phone an **iPhone** or an **Android** phone, and does it **not charge at all** or **stop partway**?

**USER:**
iPhone, it doesn't charge at all

**ASSISTANT:**
Thanks. Let's go through a few checks. This can take up to an hour, mostly waiting.

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
