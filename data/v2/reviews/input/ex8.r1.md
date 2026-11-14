# Review input: batch ex8, round 1 (32 examples)

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
- If you see the **bookmarks bar** under the address bar, click the bookmark there. To show the bar, click the **More** menu (three dots), then **Bookmarks and lists**, then **Show bookmarks bar**.
- Or click **More**, then **Bookmarks and lists**, then **Bookmark Manager** to see all your bookmarks.

## tr104-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Bookmark a website (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
how do I save a website so I can find it later

**ASSISTANT:**
You can bookmark it. Which browser are you using, like **Chrome**, **Safari**, or **Edge**? And is it on a **computer** or a **phone**?

## tr104-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Bookmark a website (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
save this website

**ASSISTANT:**
Sure. Do you want to **bookmark** it so you can visit again later, or **save a copy** of the page? And which browser are you using?

## tr104-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chrome (computer)
- task: Bookmark a website (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
how do I save a website so I can find it later

**ASSISTANT:**
You can bookmark it. Which browser are you using, like **Chrome**, **Safari**, or **Edge**? And is it on a **computer** or a **phone**?

**USER:**
Chrome on my computer

**ASSISTANT:**
Thanks.

Here's how to save it. It takes a few seconds.

1. Go to the website you want to save.
2. Click the **bookmark icon** to the right of the address bar at the top.

**To find it later:**
- If you see the **bookmarks bar** under the address bar, click the bookmark there. To show the bar, click the **More** menu (three dots), then **Bookmarks and lists**, then **Show bookmarks bar**.
- Or click **More**, then **Bookmarks and lists**, then **Bookmark Manager** to see all your bookmarks.

## tr105-a
- scenario: direct | style: plain | specification: fully_specified | platform: Gmail
- task: Unsubscribe from emails (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
I get too many newsletter emails in Gmail. How do I unsubscribe on my computer?

**ASSISTANT:**
Gmail can unsubscribe you in a couple of clicks. It takes a few seconds per sender.

1. Go to **mail.google.com** and open an email from the sender.
2. Click **Unsubscribe** next to the sender's name at the top.
3. Click **Unsubscribe** again in the box that pops up.

If you see **Go to website** instead, that sender needs you to unsubscribe on their own site.

To see all your subscriptions at once, click **More** on the left side, then **Manage subscriptions**.

Only unsubscribe from senders you recognize. If an email looks suspicious, report it as spam instead of clicking anything in it. It can take a few days for the emails to stop.

## tr105-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Unsubscribe from emails (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
how do I stop getting so many emails

**ASSISTANT:**
There are a few ways. Are they from **companies or newsletters** you signed up for, or from **strangers or scammers**? And which email do you use, like Gmail?

## tr105-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Gmail
- task: Unsubscribe from emails (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
Every store I've ever bought anything from sends me emails every single day. My inbox has 4,000 unread messages and I can't find the important ones from my family. I use Gmail on my computer.

**ASSISTANT:**
That's a lot of clutter. Unsubscribing will stop new ones from piling up:

Gmail can unsubscribe you in a couple of clicks. It takes a few seconds per sender.

1. Go to **mail.google.com** and open an email from the sender.
2. Click **Unsubscribe** next to the sender's name at the top.
3. Click **Unsubscribe** again in the box that pops up.

If you see **Go to website** instead, that sender needs you to unsubscribe on their own site.

To see all your subscriptions at once, click **More** on the left side, then **Manage subscriptions**.

Only unsubscribe from senders you recognize. If an email looks suspicious, report it as spam instead of clicking anything in it. It can take a few days for the emails to stop.

## tr105-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Gmail
- task: Unsubscribe from emails (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/15433283?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
how do I stop getting so many emails

**ASSISTANT:**
There are a few ways. Are they from **companies or newsletters** you signed up for, or from **strangers or scammers**? And which email do you use, like Gmail?

**USER:**
Newsletters from stores. Gmail.

**ASSISTANT:**
Thanks. For store newsletters, unsubscribing is the way to go.

Gmail can unsubscribe you in a couple of clicks. It takes a few seconds per sender.

1. Go to **mail.google.com** and open an email from the sender.
2. Click **Unsubscribe** next to the sender's name at the top.
3. Click **Unsubscribe** again in the box that pops up.

If you see **Go to website** instead, that sender needs you to unsubscribe on their own site.

To see all your subscriptions at once, click **More** on the left side, then **Manage subscriptions**.

Only unsubscribe from senders you recognize. If an email looks suspicious, report it as spam instead of clicking anything in it. It can take a few days for the emails to stop.

## tr106-a
- scenario: direct | style: plain | specification: fully_specified | platform: Gmail
- task: Get back a deleted email (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop

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

## tr106-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Get back a deleted email (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
I deleted something by accident

**ASSISTANT:**
Don't worry, it can often be recovered. **What did you delete** (an email, a photo, a file?), and on which device or app?

## tr106-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Get back a deleted email (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
deleted email from my

**ASSISTANT:**
It looks like your message got cut off. Which email do you use, like **Gmail**? And was it on a **computer** or a **phone**?

## tr106-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Gmail
- task: Get back a deleted email (Gmail) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/mail/answer/7401?hl=en&co=GENIE.Platform%3DDesktop

**USER:**
I deleted something by accident

**ASSISTANT:**
Don't worry, it can often be recovered. **What did you delete** (an email, a photo, a file?), and on which device or app?

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

## tr107-a
- scenario: direct | style: plain | specification: fully_specified | platform: Gmail
- task: Mark an email as spam (Gmail) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer

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

## tr107-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Mark an email as spam (Gmail) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer

**USER:**
how do I get rid of junk email

**ASSISTANT:**
I can help. Which email do you use, like **Gmail**? And are you on a **computer** or a **phone**?

## tr107-c
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Mark an email as spam (Gmail) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer

**USER:**
spam

**ASSISTANT:**
Sure. Do you mean **spam emails**, **spam texts**, or **spam calls**? I can help with any of them.

## tr107-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Gmail
- task: Mark an email as spam (Gmail) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/mail/answer/1366858/mark-or-unmark-spam-in-gmail-computer

**USER:**
how do I get rid of junk email

**ASSISTANT:**
I can help. Which email do you use, like **Gmail**? And are you on a **computer** or a **phone**?

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

## tr108-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Stop the screen from turning sideways (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118226 ; https://support.apple.com/en-us/105001

**USER:**
My iPhone screen keeps turning sideways when I'm reading in bed. How do I make it stay upright?

**ASSISTANT:**
You can lock the screen so it stays upright. It takes a few seconds.

1. Open **Control Center**: on an iPhone with Face ID, **swipe down from the top-right corner**. On an iPhone with a Home button, **swipe up from the bottom edge**.
2. Tap the **Portrait Orientation Lock** button. It has a **lock** icon.
3. Close Control Center.

Now the screen will stay upright even when you tilt the phone.

To let it turn sideways again, for example to watch a video, tap the same button.

## tr108-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Stop the screen from turning sideways (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118226 ; https://support.apple.com/en-us/105001

**USER:**
my screen keeps flipping when I lie down

**ASSISTANT:**
You can lock the screen so it stays upright. Is your phone an **iPhone** or an **Android** phone?

## tr108-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Stop the screen from turning sideways (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/118226 ; https://support.apple.com/en-us/105001

**USER:**
I like to read the news on my iPhone lying on my side in bed, but the screen keeps flipping sideways and it drives me nuts.

**ASSISTANT:**
You can stop that by locking the screen upright:

You can lock the screen so it stays upright. It takes a few seconds.

1. Open **Control Center**: on an iPhone with Face ID, **swipe down from the top-right corner**. On an iPhone with a Home button, **swipe up from the bottom edge**.
2. Tap the **Portrait Orientation Lock** button. It has a **lock** icon.
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
2. Tap the **Portrait Orientation Lock** button. It has a **lock** icon.
3. Close Control Center.

Now the screen will stay upright even when you tilt the phone.

To let it turn sideways again, for example to watch a video, tap the same button.

## tr109-a
- scenario: direct | style: plain | specification: fully_specified | platform: Android
- task: Stop the screen from turning sideways (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/6006961?hl=en

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

## tr109-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Stop the screen from turning sideways (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/6006961?hl=en

**USER:**
screen keeps turning

**ASSISTANT:**
You can stop it from rotating. Is your phone an **iPhone** or an **Android** phone?

## tr109-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Stop the screen from turning sideways (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/6006961?hl=en

**USER:**
rotate screen

**ASSISTANT:**
Sure. Do you want the screen to **stop turning sideways**, or do you want it to **turn sideways** and it won't? And is it an iPhone or an Android phone?

## tr109-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Android
- task: Stop the screen from turning sideways (Android) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/accessibility/android/answer/6006961?hl=en

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

## tr110-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Restart a frozen iPhone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/116940

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

## tr110-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Restart a frozen iPhone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/116940

**USER:**
my phone is stuck and won't do anything

**ASSISTANT:**
Let's get it working again. Is it an **iPhone** or an **Android** phone? If it's an iPhone, does it have a **round Home button** below the screen?

## tr110-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: iPhone
- task: Restart a frozen iPhone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/116940

**USER:**
I was in the middle of a FaceTime with my grandson and the screen froze on his face. Nothing I press does anything and I can't even turn it off. It's an iPhone 14.

**ASSISTANT:**
That's frustrating. An iPhone 14 has Face ID, so use the first set of steps:

You can **force restart** it. The steps depend on your model.

**iPhone with Face ID (no Home button):**
1. Press and quickly release the **volume up** button.
2. Press and quickly release the **volume down** button.
3. Press and **hold** the **side button** until you see the **Apple logo**. This can take more than 10 seconds, so keep holding.

**iPhone 7:** press and hold the **side button** and **volume down** together until you see the Apple logo.

**iPhone 6s or older (with a Home button):** press and hold the **Home button** and the **side or top button** together for about 10 seconds, until you see the Apple logo.

If it still won't turn on, charge it for an hour and try again.

## tr110-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Restart a frozen iPhone (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-us/116940

**USER:**
my phone is stuck and won't do anything

**ASSISTANT:**
Let's get it working again. Is it an **iPhone** or an **Android** phone? If it's an iPhone, does it have a **round Home button** below the screen?

**USER:**
iPhone 12, no home button

**ASSISTANT:**
Thanks. For your iPhone 12, use the first set of steps.

You can **force restart** it. The steps depend on your model.

**iPhone with Face ID (no Home button):**
1. Press and quickly release the **volume up** button.
2. Press and quickly release the **volume down** button.
3. Press and **hold** the **side button** until you see the **Apple logo**. This can take more than 10 seconds, so keep holding.

**iPhone 7:** press and hold the **side button** and **volume down** together until you see the Apple logo.

**iPhone 6s or older (with a Home button):** press and hold the **Home button** and the **side or top button** together for about 10 seconds, until you see the Apple logo.

If it still won't turn on, charge it for an hour and try again.

## tr111-a
- scenario: direct | style: plain | specification: fully_specified | platform: iPhone
- task: Phone is not charging (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
My iPhone won't charge when I plug it in. What should I try?

**ASSISTANT:**
Let's go through a few checks. This can take up to an hour, mostly waiting.

1. **Plug into a wall outlet** instead of a computer or power strip.
2. **Check the cable and adapter** for damage, like breaks or bent pins. Don't use a damaged one.
3. **Make sure everything is plugged in firmly**, or try a different outlet.
4. **Look in the charging port** on the bottom of the phone. If there's lint or dirt, carefully clear it out, then plug in firmly again.
5. **Leave it charging for 30 minutes.**
6. If it still won't turn on or only shows a battery picture, **force restart** it, then charge for another 30 minutes.

If none of this works, it may need service from Apple.

**If it stops at 80%:** that's usually a battery-saving feature, not a problem.

## tr111-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Phone is not charging (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
my phone won't charge

**ASSISTANT:**
Let's figure it out. Is your phone an **iPhone** or an **Android** phone? And does it **not charge at all**, or does it **stop partway**?

## tr111-c
- scenario: missing_info | style: incomplete | specification: underspecified | platform: unknown
- task: Phone is not charging (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
charger not

**ASSISTANT:**
It looks like your message got cut off. Is your charger **not working**, or is your phone **not charging**? And what kind of phone do you have?

## tr111-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: iPhone
- task: Phone is not charging (iPhone) | sensitive: False | reviewed by a person: False
- sources: https://support.apple.com/en-ca/108805

**USER:**
my phone won't charge

**ASSISTANT:**
Let's figure it out. Is your phone an **iPhone** or an **Android** phone? And does it **not charge at all**, or does it **stop partway**?

**USER:**
iPhone, it doesn't charge at all

**ASSISTANT:**
Thanks. Let's go through some checks.

Let's go through a few checks. This can take up to an hour, mostly waiting.

1. **Plug into a wall outlet** instead of a computer or power strip.
2. **Check the cable and adapter** for damage, like breaks or bent pins. Don't use a damaged one.
3. **Make sure everything is plugged in firmly**, or try a different outlet.
4. **Look in the charging port** on the bottom of the phone. If there's lint or dirt, carefully clear it out, then plug in firmly again.
5. **Leave it charging for 30 minutes.**
6. If it still won't turn on or only shows a battery picture, **force restart** it, then charge for another 30 minutes.

If none of this works, it may need service from Apple.

**If it stops at 80%:** that's usually a battery-saving feature, not a problem.
