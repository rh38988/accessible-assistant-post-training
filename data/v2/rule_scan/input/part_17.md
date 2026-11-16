# Rule scan input, part 17 (50 examples)

## tr189-b
- task: Block pop-ups from a website in Chrome (Chrome already blocks pop-ups by default) | platform: Chrome (computer) | scenario: missing_info | sensitive: False
- sources: Chrome Help: Block or allow pop-ups in Chrome <https://support.google.com/chrome/answer/95472>

**USER:**
A shopping site keeps throwing pop-ups at me. Can you help me block them?

**ASSISTANT:**
I can help with that. Are you using Chrome on a **computer** or on a **phone**?

---

## tr189-c
- task: Block pop-ups from a website in Chrome (Chrome already blocks pop-ups by default) | platform: Chrome (computer) | scenario: direct_messy | sensitive: False
- sources: Chrome Help: Block or allow pop-ups in Chrome <https://support.google.com/chrome/answer/95472>

**USER:**
I'm on a Windows computer with Chrome. Whenever I visit a certain coupon website, little windows pop up all over and I have to close each one. I looked in the pop-ups settings and the site is not listed anywhere. I would like Chrome to block it. I know the address of the site. What do I do?

**ASSISTANT:**
Since the site is not on any list, you can add it to the blocked list:

1. Click **More** (top right), then **Settings**.
2. Click **Privacy and security**.
3. Click **Site Settings**.
4. Click **Pop-ups and redirects**.
5. Next to **Not allowed to send pop-ups or use redirects**, click **Add**.
6. Type the address of the coupon site.
7. Click **Add**.

---

## tr189-d
- task: Block pop-ups from a website in Chrome (Chrome already blocks pop-ups by default) | platform: Chrome (computer) | scenario: followup | sensitive: False
- sources: Chrome Help: Block or allow pop-ups in Chrome <https://support.google.com/chrome/answer/95472>

**USER:**
A shopping site keeps throwing pop-ups at me. Can you help me block them?

**ASSISTANT:**
I can help with that. Are you using Chrome on a **computer** or on a **phone**?

**USER:**
chrome on my computer

**ASSISTANT:**
Chrome blocks pop-ups on its own, but you can block this site on purpose. If the site is in the allowed list:

1. Click **More** (top right), then **Settings**.
2. Click **Privacy and security**, then **Site Settings**.
3. Click **Pop-ups and redirects**.
4. Under **Allowed to send pop-ups and use redirects**, find the shopping site.
5. To the right of it, click **More**, then **Block**.

If you do not see the site in that list, click **Add** next to **Not allowed to send pop-ups or use redirects**, type the address of the shopping site, then click **Add** again.

---

## tr189-e
- task: Block pop-ups from a website in Chrome (Chrome already blocks pop-ups by default) | platform: Chrome (computer) | scenario: constraint | sensitive: False
- sources: Chrome Help: Block or allow pop-ups in Chrome <https://support.google.com/chrome/answer/95472>

**USER:**
I volunteer at a library and use their Chrome computer. It is a Chrome device that the library's network manager looks after. Pop-ups keep showing up and I want to block them in Chrome's settings myself. Can I do that?

**ASSISTANT:**
On a Chrome device that is managed for work or school, you can't change this yourself. The network administrator manages the pop-up blocker. Please ask the library's network manager to change it for you.

---

## tr189-r
- task: Block pop-ups from a website in Chrome (Chrome already blocks pop-ups by default) | platform: Chrome (computer) | scenario: failure_recovery | sensitive: False
- sources: Chrome Help: Block or allow pop-ups in Chrome <https://support.google.com/chrome/answer/95472>

**USER:**
How do I block a site from sending me pop-ups in Chrome on my computer? It is in my allowed list.

**ASSISTANT:**
Here is how:

1. Click **More** (top right), then **Settings**.
2. Click **Privacy and security**, then **Site Settings**.
3. Click **Pop-ups and redirects**.
4. Under **Allowed to send pop-ups and use redirects**, find the site.
5. To the right of the site, click **More**, then **Block**.

**USER:**
I did all that but that same site is still showing me pop-ups.

**ASSISTANT:**
The site may have permission to send notifications. Try this:

1. Go to that site.
2. Click **View site information**.
3. Next to **Notifications**, choose **Block**.

---

## tr190-a
- task: Make Chrome the default browser | platform: Chrome (Windows computer) | scenario: direct | sensitive: False
- sources: Chrome Help: Make Chrome your default browser (computer section) <https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
How do I make Chrome my default browser on my Windows 11 computer?

**ASSISTANT:**
Here is how to do it on Windows 11:

1. Click **Start**.
2. Open **Settings**.
3. Click **Apps**, then **Default apps**.
4. Under **Set defaults for applications**, type **Chrome** in the search box.
5. Select **Google Chrome**.
6. At the top, click **Set default** next to **Make Google Chrome your default browser**.
7. Review the list under **Set default file types or link types** and check that Chrome is chosen for the types you need.

---

## tr190-b
- task: Make Chrome the default browser | platform: Chrome (Windows computer) | scenario: missing_info | sensitive: False
- sources: Chrome Help: Make Chrome your default browser (computer section) <https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
Please make chrome my main browser so links open there

**ASSISTANT:**
I can help with that. Is your computer a **Windows** PC or a **Mac**?

---

## tr190-c
- task: Make Chrome the default browser | platform: Chrome (Windows computer) | scenario: direct_messy | sensitive: False
- sources: Chrome Help: Make Chrome your default browser (computer section) <https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
My computer is a few years old and runs Windows 10. Links in my emails always open in a different browser that came with it and I find it confusing. I have already installed Chrome and I use it for everything else. How can I make Chrome the one that opens by default? I don't see a search box in my settings, if that matters.

**ASSISTANT:**
On Windows 10 you pick Chrome from a list instead of searching:

1. Click **Start**.
2. Open **Settings**.
3. Open **Default apps**. It is under **System** or under **Apps**, depending on your version of Windows.
4. At the bottom, under **Web browser**, click the browser that is there now.
5. In the **Choose an app** window, select **Google Chrome**.

---

## tr190-d
- task: Make Chrome the default browser | platform: Chrome (Windows computer) | scenario: followup | sensitive: False
- sources: Chrome Help: Make Chrome your default browser (computer section) <https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
Please make chrome my main browser so links open there

**ASSISTANT:**
I can help with that. Is your computer a **Windows** PC or a **Mac**?

**USER:**
windows 11

**ASSISTANT:**
Thanks. On Windows 11:

1. Click **Start**.
2. Open **Settings**, then click **Apps**, then **Default apps**.
3. Under **Set defaults for applications**, type **Chrome** in the search box.
4. Select **Google Chrome**.
5. At the top, click **Set default** next to **Make Google Chrome your default browser**.
6. Review the list under **Set default file types or link types** and check that Chrome is chosen for the types you need.

---

## tr190-e
- task: Make Chrome the default browser | platform: Chrome (Windows computer) | scenario: constraint | sensitive: False
- sources: Chrome Help: Make Chrome your default browser (computer section) <https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
Chrome is already installed on my Windows 11 laptop, so please don't tell me to download anything. I just want Chrome to be the browser that opens when I click a link. Keep it short, my patience is thin today.

**ASSISTANT:**
Since Chrome is already installed, here are the steps:

1. Click **Start**, then open **Settings**.
2. Click **Apps**, then **Default apps**.
3. Type **Chrome** in the search box under **Set defaults for applications**.
4. Select **Google Chrome**.
5. At the top, click **Set default** next to **Make Google Chrome your default browser**.
6. Review the list under **Set default file types or link types** and check that Chrome is chosen for the types you need.

---

## tr190-r
- task: Make Chrome the default browser | platform: Chrome (Windows computer) | scenario: failure_recovery | sensitive: False
- sources: Chrome Help: Make Chrome your default browser (computer section) <https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop>

**USER:**
Make Chrome the default browser on Windows 11, how?

**ASSISTANT:**
Here is how:

1. Click **Start**.
2. Open **Settings**, then click **Apps**, then **Default apps**.
3. Under **Set defaults for applications**, type **Chrome** in the search box.
4. Select **Google Chrome**.
5. At the top, click **Set default** next to **Make Google Chrome your default browser**.

**USER:**
I did it but some links still open in the other browser.

**ASSISTANT:**
On that same Google Chrome page, look at the list called **Set default file types or link types**. Check that Chrome is chosen for the types you need.

---

## tr191-a
- task: Find a file downloaded with Chrome | platform: Chrome (computer) | scenario: direct | sensitive: False
- sources: Chrome Help: Download a file on Chrome <https://support.google.com/chrome/answer/95759?hl=en>

**USER:**
I downloaded a file with Chrome on my computer but I can't find it. Where did it go?

**ASSISTANT:**
Chrome keeps a list of your downloads. To see it:

1. At the top right of Chrome, click **More**.
2. Click **Downloads**.
3. Click the file name to open the file.

Unless the setting was changed, Chrome saves downloads in the **Downloads** folder in your user folder.

---

## tr191-b
- task: Find a file downloaded with Chrome | platform: Chrome (computer) | scenario: missing_info | sensitive: False
- sources: Chrome Help: Download a file on Chrome <https://support.google.com/chrome/answer/95759?hl=en>

**USER:**
i downloaded something from a website and now i cant find it anywhere

**ASSISTANT:**
I can help with that. Which browser did you use to download it: **Chrome**, **Edge**, or something else?

---

## tr191-c
- task: Find a file downloaded with Chrome | platform: Chrome (computer) | scenario: direct_messy | sensitive: False
- sources: Chrome Help: Download a file on Chrome <https://support.google.com/chrome/answer/95759?hl=en>

**USER:**
My daughter emailed me a PDF of the family reunion schedule and I downloaded it using Chrome on my Mac computer. Now I want to look at it but I have no idea where Chrome puts things. I haven't changed any settings that I know of. Can you tell me where the file is and how I can open it from Chrome?

**ASSISTANT:**
Since you have not changed any settings, Chrome saves it in the **Downloads** folder inside your user folder on your Mac.

To open it from Chrome:

1. At the top right of Chrome, click **More**.
2. Click **Downloads**.
3. Click the file name. It opens in your Mac's usual program for PDF files.

---

## tr191-d
- task: Find a file downloaded with Chrome | platform: Chrome (computer) | scenario: followup | sensitive: False
- sources: Chrome Help: Download a file on Chrome <https://support.google.com/chrome/answer/95759?hl=en>

**USER:**
i downloaded something from a website and now i cant find it anywhere

**ASSISTANT:**
I can help with that. Which browser did you use to download it: **Chrome**, **Edge**, or something else?

**USER:**
chrome, on my computer

**ASSISTANT:**
Thanks. In Chrome you can see all your downloads:

1. At the top right of Chrome, click **More**.
2. Click **Downloads**.
3. Click the file name to open the file.

---

## tr191-e
- task: Find a file downloaded with Chrome | platform: Chrome (computer) | scenario: constraint | sensitive: False
- sources: Chrome Help: Download a file on Chrome <https://support.google.com/chrome/answer/95759?hl=en>

**USER:**
I just finished a download in Chrome on my computer and there is a little box at the top right with the file in it. I don't want to open the file, I want to see which folder it is sitting in so I can move it myself. What do I click?

**ASSISTANT:**
You can show the file's folder from that box:

1. In the box at the top right, point to the file name.
2. Click **Show in Folder** from the actions that appear.

That opens the folder where the file is saved, and you can move it from there.

---

## tr191-r
- task: Find a file downloaded with Chrome | platform: Chrome (computer) | scenario: failure_recovery | sensitive: False
- sources: Chrome Help: Download a file on Chrome <https://support.google.com/chrome/answer/95759?hl=en>

**USER:**
Where do I find the file I just downloaded in Chrome on my computer?

**ASSISTANT:**
After a download finishes, Chrome opens the **Download tray**. Recently downloaded files appear to the right of the address bar, and your file is listed there. Click the file to open it.

**USER:**
I don't see any box at the top. It's not there.

**ASSISTANT:**
That is fine. You can see all your downloads another way:

1. At the top right of Chrome, click **More**.
2. Click **Downloads**.
3. Click the file name to open the file.

---

## tr192-a
- task: Save and find passwords with Google Password Manager | platform: Chrome (computer) | scenario: direct | sensitive: True
- sources: Chrome Help: Manage passwords in Chrome <https://support.google.com/chrome/answer/95606?hl=en>

**USER:**
How do I have Chrome save my password on my computer, and how do I look at it later?

**ASSISTANT:**
Here is how to save a password in Chrome:

1. Go to the website's sign-in page.
2. Type your username and password, then submit the form.
3. When Chrome asks to save the password, select **Save**.

To find it later:
1. At the top right, click **More**.
2. Click **Passwords and autofill**, then **Google Password Manager**.
3. Under **Passwords**, select the password.
4. On the right of your password, select **Show password**.

---

## tr192-c
- task: Save and find passwords with Google Password Manager | platform: Chrome (computer) | scenario: direct_messy | sensitive: True
- sources: Chrome Help: Manage passwords in Chrome <https://support.google.com/chrome/answer/95606?hl=en>

**USER:**
I keep all my website passwords written in a little notebook next to my computer and my son says Chrome can hold them for me instead. I use Chrome on my Windows computer. Chrome has never offered to save any of them. Can I type one in myself so Chrome has it, without waiting for it to ask me?

**ASSISTANT:**
Yes, you can add a password yourself:

1. At the top right, click **More**.
2. Click **Passwords and autofill**, then **Google Password Manager**.
3. Select **Add**.
4. Enter the website, your username, and your password.
5. Select **Save**.

Repeat these steps for each password in your notebook.

---

## tr193-a
- task: Stop a website from sending notifications | platform: Chrome (computer) | scenario: direct | sensitive: False
- sources: Google Chrome Help: Manage notifications in Chrome <https://support.google.com/chrome/answer/3220216>

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

---

## tr193-b
- task: Stop a website from sending notifications | platform: Chrome (computer) | scenario: missing_info | sensitive: False
- sources: Google Chrome Help: Manage notifications in Chrome <https://support.google.com/chrome/answer/3220216>

**USER:**
A website keeps sending me notifications and I want it to stop. Can you help?

**ASSISTANT:**
I can help with that. Are you using **Chrome** on a computer, or on a phone or tablet?

---

## tr193-c
- task: Stop a website from sending notifications | platform: Chrome (computer) | scenario: direct_messy | sensitive: False
- sources: Google Chrome Help: Manage notifications in Chrome <https://support.google.com/chrome/answer/3220216>

**USER:**
I'm on my desktop computer using Chrome and every time I open a certain recipe website a box shows up in the corner asking Get notifications? and I keep closing it. It is happening right now. How do I tell it no so it stops asking?

**ASSISTANT:**
Since the box is showing right now, you can answer it directly:

1. In the **Get notifications?** box, select the **Settings** icon.
2. Select **Don't allow**.

You can also just swipe the box away, and that blocks it too.

---

## tr193-d
- task: Stop a website from sending notifications | platform: Chrome (computer) | scenario: followup | sensitive: False
- sources: Google Chrome Help: Manage notifications in Chrome <https://support.google.com/chrome/answer/3220216>

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

---

## tr193-e
- task: Stop a website from sending notifications | platform: Chrome (computer) | scenario: constraint | sensitive: False
- sources: Google Chrome Help: Manage notifications in Chrome <https://support.google.com/chrome/answer/3220216>

**USER:**
I use Chrome on my computer. I don't want to block websites one by one, and I might want to say yes to my bank's alerts someday. I just want the pop-up that asks me about notifications to stop showing up. Is there a setting for that?

**ASSISTANT:**
Yes. Chrome has a quieter setting that keeps those asking boxes away:

1. Open **Chrome**, then select the **More** icon at the top right and select **Settings**.
2. Select **Privacy and security**, then **Site Settings**, then **Notifications**.
3. Select **Allow quieter notification prompts**.
4. Choose **Allow sites to ask to send notifications**.
5. Select **Use quieter messaging**.

Sites can still ask, but no pop-up box appears. You will see a bell icon next to the address bar, and you can select it if you ever want to allow that site.

---

## tr193-r
- task: Stop a website from sending notifications | platform: Chrome (computer) | scenario: failure_recovery | sensitive: False
- sources: Google Chrome Help: Manage notifications in Chrome <https://support.google.com/chrome/answer/3220216>

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

If you do not see the site in that list, select **Add** next to **Not allowed to send pop-ups or use redirects**, type the site's web address, then select **Add**.

---

## tr194-a
- task: Turn on Live Caption | platform: Chrome (computer) | scenario: direct | sensitive: False
- sources: Google Chrome Help: Use Live Caption in Chrome <https://support.google.com/chrome/answer/10538231>

**USER:**
How do I turn on Live Caption in Chrome on my Windows computer? I want to read what people say in videos.

**ASSISTANT:**
Here is how to turn on Live Caption:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**.
3. Select **Accessibility**.
4. Turn **Live Caption** on.

Captions will show up in a bubble when a video plays sound.

---

## tr194-b
- task: Turn on Live Caption | platform: Chrome (computer) | scenario: missing_info | sensitive: False
- sources: Google Chrome Help: Use Live Caption in Chrome <https://support.google.com/chrome/answer/10538231>

**USER:**
Can you tell me how to get captions to show up on the videos I watch?

**ASSISTANT:**
I can help with that. Are you watching in **Chrome** on a computer, or on a phone or tablet?

---

## tr194-c
- task: Turn on Live Caption | platform: Chrome (computer) | scenario: direct_messy | sensitive: False
- sources: Google Chrome Help: Use Live Caption in Chrome <https://support.google.com/chrome/answer/10538231>

**USER:**
My husband and I watch lots of Spanish language shows in Chrome on our Mac and neither of us hears so well anymore. Someone said Chrome can write out the words for us. Can you show me how to turn that on and have it show Spanish?

**ASSISTANT:**
Chrome can show captions in a language other than English. Here is how:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**, then **Accessibility**.
3. Turn **Live Caption** on.
4. Next to **Manage languages**, select **Add languages**.
5. Choose the language you want from the list. Chrome downloads the language pack by itself.
6. Next to **Preferred caption language**, select the down arrow.
7. Choose the same language.

The words will appear in a bubble while the show plays. This page does not say whether Spanish is in the list, so if it is not there, Live Caption may not support Spanish.

---

## tr194-d
- task: Turn on Live Caption | platform: Chrome (computer) | scenario: followup | sensitive: False
- sources: Google Chrome Help: Use Live Caption in Chrome <https://support.google.com/chrome/answer/10538231>

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

---

## tr194-e
- task: Turn on Live Caption | platform: Chrome (computer) | scenario: constraint | sensitive: False
- sources: Google Chrome Help: Use Live Caption in Chrome <https://support.google.com/chrome/answer/10538231>

**USER:**
I use Chrome on a Linux computer. I want captions on my videos, but I don't want a big box covering the picture. Can I turn them on and keep them out of the way?

**ASSISTANT:**
Yes. First turn the captions on:

1. Open **Chrome**.
2. At the top right, select the **More** icon, then select **Settings**, then **Accessibility**.
3. Select **Captions**.
4. Turn **Live Caption** on.

The words appear in a bubble. To keep it out of the way, drag the bubble to a new spot. You can also select the arrow in the bubble to collapse it, and select it again to expand it.

---

## tr194-r
- task: Turn on Live Caption | platform: Chrome (computer) | scenario: failure_recovery | sensitive: False
- sources: Google Chrome Help: Use Live Caption in Chrome <https://support.google.com/chrome/answer/10538231>

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

---

## tr195-a
- task: Sign out of a Google Account on a shared computer or another device (from the account's devices page) | platform: Google Account | scenario: direct | sensitive: True
- sources: Google Account Help: See devices with account access <https://support.google.com/accounts/answer/3067630>

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

---

## tr195-b
- task: Sign out of a Google Account on a shared computer or another device (from the account's devices page) | platform: Google Account | scenario: missing_info | sensitive: True
- sources: Google Account Help: See devices with account access <https://support.google.com/accounts/answer/3067630>

**USER:**
I left my account open on a computer I don't own. How do I log out from here?

**ASSISTANT:**
I can help with that. Is it your **Google Account** (like Gmail or YouTube), or a different kind of account?

---

## tr195-c
- task: Sign out of a Google Account on a shared computer or another device (from the account's devices page) | platform: Google Account | scenario: direct_messy | sensitive: True
- sources: Google Account Help: See devices with account access <https://support.google.com/accounts/answer/3067630>

**USER:**
I was at the library this afternoon using one of their public computers to look at my Google account and I was in such a hurry to catch my bus that I left without logging out. I'm home now on my own computer. How can I make sure the library computer is signed out of my Google Account?

**ASSISTANT:**
You can do it from your own computer:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under the **Your devices** panel, select **Manage all devices**.
4. Select the library computer in the list, then select **Sign out**.

A device you are already signed out of shows **Signed out** in the list.

---

## tr195-d
- task: Sign out of a Google Account on a shared computer or another device (from the account's devices page) | platform: Google Account | scenario: followup | sensitive: True
- sources: Google Account Help: See devices with account access <https://support.google.com/accounts/answer/3067630>

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

---

## tr196-a
- task: Add a recovery phone number or email to a Google Account (computer) | platform: Google Account | scenario: direct | sensitive: True
- sources: Google Account Help: Add or update your recovery phone or email <https://support.google.com/accounts/answer/183723>

**USER:**
How do I add a recovery phone number to my Google Account? I'm on my computer.

**ASSISTANT:**
Here is how to add a recovery phone number:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Recovery phone**. You might need to sign in again.
4. Follow the on-screen steps to add your number.

Use a phone that gets text messages, belongs only to you, and that you carry regularly. Do not use a Google Voice number.

---

## tr196-b
- task: Add a recovery phone number or email to a Google Account (computer) | platform: Google Account | scenario: missing_info | sensitive: True
- sources: Google Account Help: Add or update your recovery phone or email <https://support.google.com/accounts/answer/183723>

**USER:**
I want to add a backup way to get back into my Google account in case I get locked out.

**ASSISTANT:**
I can help with that. Would you like to add a recovery **phone number** or a recovery **email**?

---

## tr196-c
- task: Add a recovery phone number or email to a Google Account (computer) | platform: Google Account | scenario: direct_messy | sensitive: True
- sources: Google Account Help: Add or update your recovery phone or email <https://support.google.com/accounts/answer/183723>

**USER:**
My grandson told me I should put a backup email address on my Gmail account in case I ever get locked out. I have an old email I check every day. I'm on my laptop right now. What do I click to add that as the recovery email?

**ASSISTANT:**
Your grandson gave good advice. Here is how:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Recovery email**. You might need to sign in again.
4. Follow the on-screen steps to add the address.

An email you check often is a good choice. It should be a different one from the email you sign in with.

---

## tr196-d
- task: Add a recovery phone number or email to a Google Account (computer) | platform: Google Account | scenario: followup | sensitive: True
- sources: Google Account Help: Add or update your recovery phone or email <https://support.google.com/accounts/answer/183723>

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

---

## tr196-e
- task: Add a recovery phone number or email to a Google Account (computer) | platform: Google Account | scenario: constraint | sensitive: True
- sources: Google Account Help: Add or update your recovery phone or email <https://support.google.com/accounts/answer/183723>

**USER:**
I forgot my Google password and I'm in the middle of the account recovery steps right now. I'd like to add a recovery phone number at the same time so this never happens again. Can I do that now?

**ASSISTANT:**
Not right now. Google does not let you add recovery info while you are locked out or in the account recovery process.

Once you are back in your account, you can add it:

1. Go to your Google Account at myaccount.google.com.
2. Select **Security & sign-in**.
3. Under **How you sign in to Google**, select **Recovery phone**.
4. Follow the on-screen steps to add your number.

---

## tr196-r
- task: Add a recovery phone number or email to a Google Account (computer) | platform: Google Account | scenario: failure_recovery | sensitive: True
- sources: Google Account Help: Add or update your recovery phone or email <https://support.google.com/accounts/answer/183723>

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

---

## tr197-a
- task: Free up Google account storage (Storage Manager on a computer; Android Google One WhatsApp backup) | platform: Google Account (Drive, Gmail, Photos) | scenario: direct | sensitive: False
- sources: Google One Help: Clean up & fix issues with your Google storage <https://support.google.com/googleone/answer/9776477>

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

---

## tr197-b
- task: Free up Google account storage (Storage Manager on a computer; Android Google One WhatsApp backup) | platform: Google Account (Drive, Gmail, Photos) | scenario: missing_info | sensitive: False
- sources: Google One Help: Clean up & fix issues with your Google storage <https://support.google.com/googleone/answer/9776477>

**USER:**
Google says my storage is full. What should I do?

**ASSISTANT:**
I can help with that. Are you using a **computer**, or the Google One app on an **Android** phone?

---

## tr197-c
- task: Free up Google account storage (Storage Manager on a computer; Android Google One WhatsApp backup) | platform: Google Account (Drive, Gmail, Photos) | scenario: direct_messy | sensitive: False
- sources: Google One Help: Clean up & fix issues with your Google storage <https://support.google.com/googleone/answer/9776477>

**USER:**
I have an Android phone and the Google One app. It says my storage is almost full and I think it's because of my WhatsApp backup, my daughter said something about that. Where do I go in the app to get rid of the old WhatsApp backup?

**ASSISTANT:**
Here is how to remove it in the Google One app:

1. Open the **Google One** app and tap **Storage**, then tap **Free up account storage**.
2. Under **Clean up other items**, tap **WhatsApp**.
3. Under the backup you want to remove, tap **Delete backup**.

Deleting a backup does not turn off future backups.

---

## tr197-d
- task: Free up Google account storage (Storage Manager on a computer; Android Google One WhatsApp backup) | platform: Google Account (Drive, Gmail, Photos) | scenario: followup | sensitive: False
- sources: Google One Help: Clean up & fix issues with your Google storage <https://support.google.com/googleone/answer/9776477>

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

---

## tr197-e
- task: Free up Google account storage (Storage Manager on a computer; Android Google One WhatsApp backup) | platform: Google Account (Drive, Gmail, Photos) | scenario: constraint | sensitive: False
- sources: Google One Help: Clean up & fix issues with your Google storage <https://support.google.com/googleone/answer/9776477>

**USER:**
Most of my storage is old photos in Google Photos. I'm on my computer and I don't want to lose any of them, I'd like copies on my own computer first. How do I free up space?

**ASSISTANT:**
You can save copies first, then clear the space:

1. Go to one.google.com and click **Storage**.
2. Select **Clean up space**.
3. Under **Clean up by service**, choose **Google Photos**.
4. Select the photos you want to remove.
5. Click **Download** to keep copies on your computer.
6. Click **Delete** at the top right.
7. If a box asks you to confirm, read the wording and check the box to continue.
8. Click **Move to trash**.

---

## tr198-a
- task: Get directions on a computer | platform: Google Maps (computer) | scenario: direct | sensitive: False
- sources: Google Maps Help: Get directions and show routes <https://support.google.com/maps/answer/144339>

**USER:**
How do I get driving directions on Google Maps on my computer?

**ASSISTANT:**
Here is how to get driving directions:

1. Open Google Maps in your browser, then click **Directions**.
2. Enter a starting point and a destination. You can type an address, type a place name, or click on the map.
3. Choose **Driving**.

The best route shows in blue, and other routes show in gray. Under the route, click **Details** to see the steps.

---

## tr198-c
- task: Get directions on a computer | platform: Google Maps (computer) | scenario: direct_messy | sensitive: False
- sources: Google Maps Help: Get directions and show routes <https://support.google.com/maps/answer/144339>; Google Maps Help: Share, send or print directions from Google Maps, Computer <https://support.google.com/maps/answer/7101463>

**USER:**
I'm going to walk to my sister's house on Saturday and I want to print out the route first. I'm at my desktop computer in the browser, on Google Maps. How do I get the walking directions from my house to hers?

**ASSISTANT:**
Here is how to get walking directions and print them:

1. Open Google Maps in your browser, then click **Directions**.
2. Enter your house as the starting point and your sister's address as the destination.
3. Choose **Walking**.
4. Pick the route you want.
5. Click the printer icon.
6. In the pop-up, select **Print including maps** or **Print text only**.
7. Click **Print**.

Under the route, click **Details** to see the step by step directions.

---

## tr198-d
- task: Get directions on a computer | platform: Google Maps (computer) | scenario: followup | sensitive: False
- sources: Google Maps Help: Get directions and show routes <https://support.google.com/maps/answer/144339>

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

---

## tr198-e
- task: Get directions on a computer | platform: Google Maps (computer) | scenario: constraint | sensitive: False
- sources: Google Maps Help: Get directions and show routes <https://support.google.com/maps/answer/144339>

**USER:**
I'm planning a drive from my computer using Google Maps in my browser. I really don't want to pay any tolls on the way. How do I get driving directions that avoid them?

**ASSISTANT:**
Here is how to get driving directions without tolls:

1. Open Google Maps in your browser, then click **Directions**.
2. Enter a starting point and a destination.
3. Choose **Driving**.
4. Click **Options**.
5. Check the box next to **Tolls**.

---
