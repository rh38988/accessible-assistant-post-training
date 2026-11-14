# Review input: batch ny6b, round 1 (36 examples)

## tr193-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chrome (computer)
- task: Stop a website from sending notifications (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/3220216

**USER:**
How do I stop a news website from sending me notifications in Chrome on my computer?

**ASSISTANT:**
Here is how to block one website in Chrome:

1. Open **Chrome** on your computer.
2. At the top right, select the **More** icon, then select **Settings**.
3. Select **Privacy and security**, then **Site Settings**, then **Notifications**.
4. Next to **Not allowed to send notifications**, select **Add**.
5. Type the website's web address, then select **Add**.

The site will now be on the blocked list.

## tr193-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Chrome (computer)
- task: Stop a website from sending notifications (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/3220216

**USER:**
I'm on my desktop computer using Chrome and every time I open a certain recipe website a box shows up in the corner asking Get notifications? and I keep closing it. It is happening right now. How do I tell it no so it stops asking?

**ASSISTANT:**
Since the box is showing right now, you can answer it directly:

1. In the **Get notifications?** box, select the **Settings** icon.
2. Select **Don't allow**.

You can also just swipe the box away, and that blocks it too.

## tr193-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Stop a website from sending notifications (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/3220216

**USER:**
A website keeps sending me notifications and I want it to stop. Can you help?

**ASSISTANT:**
I can help with that. Are you using **Chrome** on a computer, or on a phone or tablet?

## tr193-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chrome (computer)
- task: Stop a website from sending notifications (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/3220216

**USER:**
A website keeps sending me notifications and I want it to stop. Can you help?

**ASSISTANT:**
I can help with that. Are you using **Chrome** on a computer, or on a phone or tablet?

**USER:**
Chrome on my Windows laptop

**ASSISTANT:**
Here is how to block the website in Chrome on your computer:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**.
3. Select **Privacy and security**, then **Site Settings**, then **Notifications**.
4. Next to **Not allowed to send notifications**, select **Add**.
5. Type the website's web address, then select **Add**.

## tr193-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chrome (computer)
- task: Stop a website from sending notifications (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/3220216

**USER:**
I use Chrome on my computer. I don't want to block websites one by one, and I might want to say yes to my bank's alerts someday. I just want the pop-up that asks me about notifications to stop showing up. Is there a setting for that?

**ASSISTANT:**
Yes. Chrome has a quieter setting that keeps those asking boxes away:

1. Open **Chrome**, then select the **More** icon at the top right and select **Settings**.
2. Select **Privacy and security**, then **Site Settings**, then **Notifications**.
3. Under the default setting, choose the option that lets sites ask for notifications.
4. Select **Use quieter messaging**.

Sites can still ask, but no pop-up box appears. You will see a bell icon next to the address bar, and you can select it if you ever want to allow that site.

## tr193-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chrome (computer)
- task: Stop a website from sending notifications (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/3220216

**USER:**
I use Chrome on my PC. How do I block a website from sending notifications?

**ASSISTANT:**
Here is how to block one website:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**.
3. Select **Privacy and security**, then **Site Settings**, then **Notifications**.
4. Next to **Not allowed to send notifications**, select **Add**.
5. Type the website's web address, then select **Add**.

**USER:**
I did all that but the website is still putting little boxes on my screen.

**ASSISTANT:**
Those may be pop-ups, which use a different setting from notifications. Try this:

1. Go to **Privacy and security**, then **Site Settings**, then **Pop-ups and redirects**.
2. Find the site under **Allowed to send pop-ups and use redirects**.
3. Select **More**, then select **Block**.

## tr194-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chrome (computer)
- task: Turn on Live Caption (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/10538231

**USER:**
How do I turn on Live Caption in Chrome on my Windows computer? I want to read what people say in videos.

**ASSISTANT:**
Here is how to turn on Live Caption:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**.
3. Select **Accessibility**.
4. Turn **Live Caption** on.

Captions will show up in a bubble when a video plays sound.

## tr194-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Chrome (computer)
- task: Turn on Live Caption (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/10538231

**USER:**
My husband and I watch lots of Spanish language shows in Chrome on our Mac and neither of us hears so well anymore. Someone said Chrome can write out the words for us. Can you show me how to turn that on and have it show Spanish?

**ASSISTANT:**
Yes, Chrome can do that. Here is how:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**, then **Accessibility**.
3. Turn **Live Caption** on.
4. Next to **Manage languages**, select **Add languages** and choose Spanish. Chrome downloads the language pack by itself.
5. Next to **Preferred caption language**, open the down arrow and choose Spanish.

The words will appear in a bubble while the show plays.

## tr194-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Turn on Live Caption (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/10538231

**USER:**
Can you tell me how to get captions to show up on the videos I watch?

**ASSISTANT:**
I can help with that. Are you watching in **Chrome** on a computer, or on a phone or tablet?

## tr194-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chrome (computer)
- task: Turn on Live Caption (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/10538231

**USER:**
Can you tell me how to get captions to show up on the videos I watch?

**ASSISTANT:**
I can help with that. Are you watching in **Chrome** on a computer, or on a phone or tablet?

**USER:**
Chrome on my Mac

**ASSISTANT:**
Here is how to turn on Live Caption in Chrome:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**, then **Accessibility**.
3. Turn **Live Caption** on.

Captions will appear in a bubble when a video plays sound.

## tr194-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chrome (computer)
- task: Turn on Live Caption (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/10538231

**USER:**
I use Chrome on a Linux computer. I want captions on my videos, but I don't want a big box covering the picture. Can I turn them on and keep them out of the way?

**ASSISTANT:**
Yes. First turn the captions on:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**, then **Accessibility**.
3. Select **Captions**.
4. Turn **Live Caption** on.

The words appear in a bubble. To keep it out of the way, drag the bubble to a new spot. You can also select the arrow in the bubble to collapse it, and select it again to expand it.

## tr194-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chrome (computer)
- task: Turn on Live Caption (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/10538231

**USER:**
How do I turn on Live Caption in Chrome on my Windows PC?

**ASSISTANT:**
Here is how to turn on Live Caption:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**.
3. Select **Accessibility**.
4. Turn **Live Caption** on.

**USER:**
I turned it on but my video plays with no captions. It starts playing by itself with the sound off.

**ASSISTANT:**
Captions are made from the sound, so a silent video gives them nothing to write. Turn the video's volume on, and the words should start to appear in the bubble.

## tr195-a
- scenario: direct | style: plain | specification: fully_specified | platform: Google Account
- task: Sign out of a Google Account on a shared computer or another device (from the account's devices page) (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/3067630

**USER:**
I checked my Gmail on my neighbor's computer and forgot to sign out before I left. How do I sign out of my Google Account on that computer?

**ASSISTANT:**
You can sign that computer out from here:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under the **Your devices** panel, select **Manage all devices**.
4. Select the device you want to remove, then select **Sign out**.

That ends that device's access to your account.

If you see the same device name more than once, sign out of all the entries with that name, to be sure no other device still has access.

## tr195-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Google Account
- task: Sign out of a Google Account on a shared computer or another device (from the account's devices page) (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/3067630

**USER:**
I was at the library this afternoon using one of their public computers to look at my Google account and I was in such a hurry to catch my bus that I left without logging out. I'm home now on my own computer. How can I make sure the library computer is signed out of my Google Account?

**ASSISTANT:**
You can do it from your own computer:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under the **Your devices** panel, select **Manage all devices**.
4. Select the library computer in the list, then select **Sign out**.

A device you are already signed out of shows **Signed out** in the list.

## tr195-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Sign out of a Google Account on a shared computer or another device (from the account's devices page) (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/3067630

**USER:**
I left my account open on a computer I don't own. How do I log out from here?

**ASSISTANT:**
I can help with that. Is it your **Google Account** (like Gmail or YouTube), or a different kind of account?

## tr195-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Google Account
- task: Sign out of a Google Account on a shared computer or another device (from the account's devices page) (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/3067630

**USER:**
I left my account open on a computer I don't own. How do I log out from here?

**ASSISTANT:**
I can help with that. Is it your **Google Account** (like Gmail or YouTube), or a different kind of account?

**USER:**
Yes it's my Google account, Gmail

**ASSISTANT:**
Here is how to sign that computer out from where you are:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under the **Your devices** panel, select **Manage all devices**.
4. Select the computer you left it on, then select **Sign out**.

## tr195-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Google Account
- task: Sign out of a Google Account on a shared computer or another device (from the account's devices page) (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/3067630

**USER:**
My Google Account is still signed in on a hotel business center computer. I'm back in my room and can't go back down there. I only want that one computer signed out, and I want to keep using my phone and laptop as they are. What do I do?

**ASSISTANT:**
You can sign out only that computer:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under the **Your devices** panel, select **Manage all devices**.
4. Select the hotel computer in the list, then select **Sign out**.

This ends that one device's access to your account. Only choose the hotel computer in the list.

## tr195-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Google Account
- task: Sign out of a Google Account on a shared computer or another device (from the account's devices page) (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/3067630

**USER:**
How do I sign my Google Account out of a shared computer I used earlier?

**ASSISTANT:**
You can do it from your account page:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under the **Your devices** panel, select **Manage all devices**.
4. Select the shared computer, then select **Sign out**.

**USER:**
I see the same computer name listed three times. Which one do I pick?

**ASSISTANT:**
The same name can come from one device or from several. To be safe, sign out of all of them:

1. Select the first entry with that name, then select **Sign out**.
2. Do the same for each of the other entries with that name.

## tr196-a
- scenario: direct | style: plain | specification: fully_specified | platform: Google Account
- task: Add a recovery phone number or email to a Google Account (computer) (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/183723

**USER:**
How do I add a recovery phone number to my Google Account? I'm on my computer.

**ASSISTANT:**
Here is how to add a recovery phone number:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Recovery phone**. You might need to sign in again.
4. Follow the on-screen steps to add your number.

Use a phone that gets text messages, belongs only to you, and that you carry regularly. Do not use a Google Voice number.

## tr196-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Google Account
- task: Add a recovery phone number or email to a Google Account (computer) (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/183723

**USER:**
My grandson told me I should put a backup email address on my Gmail account in case I ever get locked out. I have an old email I check every day. I'm on my laptop right now. What do I click to add that as the recovery email?

**ASSISTANT:**
Your grandson gave good advice. Here is how:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Recovery email**. You might need to sign in again.
4. Follow the on-screen steps to add the address.

An email you check often is a good choice. It should be a different one from the email you sign in with.

## tr196-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Add a recovery phone number or email to a Google Account (computer) (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/183723

**USER:**
I want to add a backup way to get back into my Google account in case I get locked out.

**ASSISTANT:**
I can help with that. Would you like to add a recovery **phone number** or a recovery **email**?

## tr196-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Google Account
- task: Add a recovery phone number or email to a Google Account (computer) (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/183723

**USER:**
I want to add a backup way to get back into my Google account in case I get locked out.

**ASSISTANT:**
I can help with that. Would you like to add a recovery **phone number** or a recovery **email**?

**USER:**
phone number please

**ASSISTANT:**
Here is how to add a recovery phone number:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Recovery phone**. You might need to sign in again.
4. Follow the on-screen steps to add your number.

## tr196-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Google Account
- task: Add a recovery phone number or email to a Google Account (computer) (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/183723

**USER:**
I forgot my Google password and I'm in the middle of the account recovery steps right now. I'd like to add a recovery phone number at the same time so this never happens again. Can I do that now?

**ASSISTANT:**
Not right now. Google does not let you add recovery info while you are locked out or in the account recovery process.

Once you are back in your account, you can add it:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Recovery phone**.
4. Follow the on-screen steps to add your number.

## tr196-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Google Account
- task: Add a recovery phone number or email to a Google Account (computer) (Google Account) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/accounts/answer/183723

**USER:**
I'm on my PC and want to change the recovery phone number on my Google Account to my new number.

**ASSISTANT:**
Here is how to change it:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Recovery phone**. You might need to sign in again.
4. Select **Edit** next to the number.
5. Follow the on-screen steps.

**USER:**
It won't let me change it. I get stuck and it just doesn't go through.

**ASSISTANT:**
Try one of these:

1. Try again from a device you normally use to sign in.
2. Or try from a place where you normally sign in.
3. Or wait and try again next week from the device you are using now.

## tr197-a
- scenario: direct | style: plain | specification: fully_specified | platform: Google Account (Drive, Gmail, Photos)
- task: Free up Google account storage (Storage Manager on a computer; Android Google One WhatsApp backup) (Google Account (Drive, Gmail, Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleone/answer/9776477

**USER:**
My Google storage is full and my Gmail stopped getting new mail. How do I free up space? I'm on my computer.

**ASSISTANT:**
You can clear space with the Storage Manager:

1. Go to one.google.com and click **Storage**.
2. Select **Clean up space**.
3. Under **Clean up suggested items** or **Clean up by service**, choose a category or service.
4. Select the files you want to delete.
5. Click **Delete** at the top right.
6. Read the wording, then check the box to continue.
7. Click **Permanently delete**.

The storage total can take 48 to 72 hours to update after a big deletion.

## tr197-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Google Account (Drive, Gmail, Photos)
- task: Free up Google account storage (Storage Manager on a computer; Android Google One WhatsApp backup) (Google Account (Drive, Gmail, Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleone/answer/9776477

**USER:**
I have an Android phone and the Google One app. It says my storage is almost full and I think it's because of my WhatsApp backup, my daughter said something about that. Where do I go in the app to get rid of the old WhatsApp backup?

**ASSISTANT:**
Here is how to remove it in the Google One app:

1. Open the **Google One** app and tap **Storage**, then tap **Free up account storage**.
2. Under **Clean up other items**, tap **WhatsApp**.
3. Under the backup you want to remove, tap **Delete backup**.

Deleting a backup does not turn off future backups.

## tr197-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Free up Google account storage (Storage Manager on a computer; Android Google One WhatsApp backup) (Google Account (Drive, Gmail, Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleone/answer/9776477

**USER:**
Google says my storage is full. What should I do?

**ASSISTANT:**
I can help with that. Are you using a **computer**, or the Google One app on an **Android** phone?

## tr197-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Google Account (Drive, Gmail, Photos)
- task: Free up Google account storage (Storage Manager on a computer; Android Google One WhatsApp backup) (Google Account (Drive, Gmail, Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleone/answer/9776477

**USER:**
Google says my storage is full. What should I do?

**ASSISTANT:**
I can help with that. Are you using a **computer**, or the Google One app on an **Android** phone?

**USER:**
I'm on a computer

**ASSISTANT:**
Here is how to clear space on a computer:

1. Go to one.google.com and click **Storage**.
2. Select **Clean up space**.
3. Under **Clean up suggested items** or **Clean up by service**, choose a category or service.
4. Select the files you want to delete.
5. Click **Delete** at the top right.
6. Read the wording, then check the box to continue.
7. Click **Permanently delete**.

## tr197-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Google Account (Drive, Gmail, Photos)
- task: Free up Google account storage (Storage Manager on a computer; Android Google One WhatsApp backup) (Google Account (Drive, Gmail, Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleone/answer/9776477

**USER:**
Most of my storage is old photos in Google Photos. I'm on my computer and I don't want to lose any of them, I'd like copies on my own computer first. How do I free up space?

**ASSISTANT:**
You can save copies first, then clear the space:

1. Go to one.google.com and click **Storage**.
2. Select **Clean up space**.
3. Under **Clean up by service**, choose **Google Photos**.
4. Select the photos you want to remove.
5. Click **Download** to keep copies on your computer.
6. Click **Delete** at the top right, then click **Move to trash**.

## tr197-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Google Account (Drive, Gmail, Photos)
- task: Free up Google account storage (Storage Manager on a computer; Android Google One WhatsApp backup) (Google Account (Drive, Gmail, Photos)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/googleone/answer/9776477

**USER:**
My Google account storage is full. I'm on my computer. How do I free some up?

**ASSISTANT:**
Use the Storage Manager:

1. Go to one.google.com and click **Storage**.
2. Select **Clean up space**.
3. Under **Clean up suggested items** or **Clean up by service**, choose a category or service.
4. Select the files you want to delete.
5. Click **Delete** at the top right.
6. Read the wording, then check the box to continue.
7. Click **Permanently delete**.

**USER:**
I deleted a lot of stuff but it still says my storage is full.

**ASSISTANT:**
The total can take 48 to 72 hours to update after a large deletion, so please wait that long first. If it is still full after that, your photo backup may be filling the space again. Check your **Google Photos** backup settings.

## tr198-a
- scenario: direct | style: plain | specification: fully_specified | platform: Google Maps (computer)
- task: Get directions on a computer (Google Maps (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339

**USER:**
How do I get driving directions on Google Maps on my computer?

**ASSISTANT:**
Here is how to get driving directions:

1. Open Google Maps in your browser, then click **Directions**.
2. Enter a starting point and a destination. You can type an address, type a place name, or click on the map.
3. Choose **Driving**.

The best route shows in blue, and other routes show in gray. Under the route, click **Details** to see the steps.

## tr198-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Google Maps (computer)
- task: Get directions on a computer (Google Maps (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339

**USER:**
I'm going to walk to my sister's house on Saturday and I want to print out the route first. I'm at my desktop computer in the browser, on Google Maps. How do I get the walking directions from my house to hers?

**ASSISTANT:**
Here is how to get walking directions:

1. Open Google Maps in your browser, then click **Directions**.
2. Enter your house as the starting point and your sister's address as the destination.
3. Choose **Walking**.

Under the route, click **Details** to see the step by step directions.

## tr198-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Get directions on a computer (Google Maps (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339

**USER:**
how do i get directions to the dentist office on google maps

**ASSISTANT:**
I can help with that. Are you using Google Maps on a **computer**, or on a **phone or tablet**?

## tr198-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Google Maps (computer)
- task: Get directions on a computer (Google Maps (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339

**USER:**
how do i get directions to the dentist office on google maps

**ASSISTANT:**
I can help with that. Are you using Google Maps on a **computer**, or on a **phone or tablet**?

**USER:**
my computer

**ASSISTANT:**
Here is how to get directions on a computer:

1. Open Google Maps in your browser, then click **Directions**.
2. Enter your starting point, then type the dentist's office name or address as the destination.
3. Choose **Driving**, **Transit**, or **Walking**.

Under the route, click **Details** to see the steps.

## tr198-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Google Maps (computer)
- task: Get directions on a computer (Google Maps (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339

**USER:**
I'm planning a drive from my computer using Google Maps in my browser. I really don't want to pay any tolls on the way. How do I get driving directions that avoid them?

**ASSISTANT:**
Here is how to get driving directions without tolls:

1. Open Google Maps in your browser, then click **Directions**.
2. Enter a starting point and a destination.
3. Choose **Driving**.
4. Click **Options**.
5. Under **Avoid tolls & highways**, check **Tolls**.

## tr198-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Google Maps (computer)
- task: Get directions on a computer (Google Maps (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339

**USER:**
I'd like bus directions to the farmers market on Google Maps on my computer.

**ASSISTANT:**
Here is how to get bus directions:

1. Open Google Maps in your browser, then click **Directions**.
2. Enter your starting point and the farmers market as the destination.
3. Choose **Transit**.

**USER:**
I don't see any bus or transit option for my town.

**ASSISTANT:**
Transit only shows where your city's transit agency has added its route information to Google Maps. Your agency may not have added it yet. You can still choose **Driving** or **Walking** from the same screen to get directions.
