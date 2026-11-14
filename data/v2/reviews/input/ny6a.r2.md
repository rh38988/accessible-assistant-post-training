# Review input: batch ny6a, round 2 (22 examples)

## tr187-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chrome (Android)
- task: Bookmark a website in Chrome on the phone (Chrome (Android)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
How do I bookmark a website in Chrome on my Android phone?

**ASSISTANT:**
Here is how to bookmark a page in Chrome on your Android phone:

1. Open Chrome and go to the page you want to save.
2. To the right of the address bar, tap **More**.
3. Tap **Add to bookmarks**.

## tr187-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Chrome (Android)
- task: Bookmark a website in Chrome on the phone (Chrome (Android)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
I have a Google Pixel phone and I use Chrome for the weather site every single day. My neighbor said I can save it so I don't have to search for it every time. I have the weather site open right now. How do I save it, and then how would I open it again tomorrow?

**ASSISTANT:**
You can bookmark it now and open it from your bookmarks tomorrow.

To save it:
1. With the weather site open, tap **More**, to the right of the address bar.
2. Tap **Add to bookmarks**.

To open it again:
1. Open Chrome.
2. Tap **More** at the top right.
3. Tap **Bookmarks**.
4. Tap a folder.
5. Tap the bookmark.

## tr187-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chrome (Android)
- task: Bookmark a website in Chrome on the phone (Chrome (Android)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
i want to save a website on my phone so i dont lose it. i use chrome

**ASSISTANT:**
I can help with that. Is your phone an **Android** phone or an **iPhone**?

**USER:**
android, a samsung

**ASSISTANT:**
Thanks. To bookmark a site in Chrome on your Android phone:

1. Open Chrome and go to the website.
2. To the right of the address bar, tap **More**.
3. Tap **Add to bookmarks**.

## tr187-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chrome (Android)
- task: Bookmark a website in Chrome on the phone (Chrome (Android)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
On my Android phone the Chrome address bar is at the bottom of the screen, not the top. My son changed something. I want to bookmark a recipe page I'm on and then find it again later. Where do I tap?

**ASSISTANT:**
You can do both with the bar at the bottom.

To save the recipe:
1. To the right of the address bar, tap **More**.
2. Tap **Add to bookmarks**.

To find it later:
1. Open Chrome.
2. Swipe up on the address bar.
3. Tap **Bookmarks**.
4. Tap a folder, then tap the bookmark.

## tr187-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chrome (Android)
- task: Bookmark a website in Chrome on the phone (Chrome (Android)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/188842?hl=en&co=GENIE.Platform%3DAndroid

**USER:**
Can you tell me how to bookmark a page in Chrome on my Android phone?

**ASSISTANT:**
Yes. Here is how:

1. Open Chrome and go to the page.
2. To the right of the address bar, tap **More**.
3. Tap **Add to bookmarks**.

**USER:**
ok I did that. but now how do I get back to it? I can't find where it went

**ASSISTANT:**
Your bookmark is saved. To open it:

1. Open Chrome.
2. At the top right, tap **More**, then tap **Bookmarks**.
3. Tap a folder. If you recently opened a folder, you will see that same folder. To see other folders, tap **Back** at the top left.
4. Tap the bookmark.

If your address bar is at the bottom, swipe up on it and tap **Bookmarks** instead. You can also type in the **Search your bookmarks** bar at the top.

## tr188-a
- scenario: direct | style: plain | specification: fully_specified | platform: Microsoft Edge (computer)
- task: Make web pages bigger (Microsoft Edge (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/microsoft-edge/accessibility-features-in-microsoft-edge-4c696192-338e-9465-b2cd-bd9b698ad19a

**USER:**
The writing on websites is too small in Edge on my computer. How do I make it bigger?

**ASSISTANT:**
You can zoom in on the page you are looking at:

1. Select **Settings and more**.
2. Select **Zoom in**.
3. Select **Zoom in** again until the page is the size you like.

You can also hold the **Ctrl** key and press the **plus sign** key.

## tr188-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Microsoft Edge (computer)
- task: Make web pages bigger (Microsoft Edge (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/microsoft-edge/accessibility-features-in-microsoft-edge-4c696192-338e-9465-b2cd-bd9b698ad19a

**USER:**
Everything on the websites I visit looks so tiny. Can you make the pages bigger?

**ASSISTANT:**
I can help with that. Which web browser are you using: **Edge**, **Chrome**, or something else?

**USER:**
Edge on my computer

**ASSISTANT:**
Thanks. To make the page you are on bigger in Edge:

1. Select **Settings and more**.
2. Select **Zoom in**.
3. Select **Zoom in** again until the page is big enough.

## tr188-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Microsoft Edge (computer)
- task: Make web pages bigger (Microsoft Edge (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/microsoft-edge/accessibility-features-in-microsoft-edge-4c696192-338e-9465-b2cd-bd9b698ad19a

**USER:**
How can I make a web page bigger in Edge on my computer?

**ASSISTANT:**
Here is how to zoom in:

1. Select **Settings and more**.
2. Select **Zoom in**.
3. Select **Zoom in** again until the page is the size you like.

**USER:**
I pressed it too many times and now the page is huge. How do I put it back to normal?

**ASSISTANT:**
You can put it back in one step. Hold down the **Ctrl** key and press the **0** key. That resets the page to the default size.

Or you can go back to **Settings and more** and select **Zoom out** until it looks right.

## tr189-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chrome (computer)
- task: Block pop-ups from a website in Chrome (Chrome already blocks pop-ups by default) (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/95472

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

## tr189-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chrome (computer)
- task: Block pop-ups from a website in Chrome (Chrome already blocks pop-ups by default) (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/95472

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

## tr190-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chrome (Windows computer)
- task: Make Chrome the default browser (Chrome (Windows computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop

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

## tr190-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chrome (Windows computer)
- task: Make Chrome the default browser (Chrome (Windows computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop

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

## tr190-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chrome (Windows computer)
- task: Make Chrome the default browser (Chrome (Windows computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/95417?hl=en&co=GENIE.Platform%3DDesktop

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

## tr191-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chrome (computer)
- task: Find a file downloaded with Chrome (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/95759?hl=en

**USER:**
I downloaded a file with Chrome on my computer but I can't find it. Where did it go?

**ASSISTANT:**
Chrome keeps a list of your downloads. To see it:

1. At the top right of Chrome, click **More**.
2. Click **Downloads**.
3. Click the file name to open the file.

Unless the setting was changed, Chrome saves downloads in the **Downloads** folder in your user folder.

## tr191-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Chrome (computer)
- task: Find a file downloaded with Chrome (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/95759?hl=en

**USER:**
My daughter emailed me a PDF of the family reunion schedule and I downloaded it using Chrome on my Mac computer. Now I want to look at it but I have no idea where Chrome puts things. I haven't changed any settings that I know of. Can you tell me where the file is and how I can open it from Chrome?

**ASSISTANT:**
Since you have not changed any settings, Chrome saves it in the **Downloads** folder inside your user folder on your Mac.

To open it from Chrome:

1. At the top right of Chrome, click **More**.
2. Click **Downloads**.
3. Click the file name. It opens in your Mac's usual program for PDF files.

## tr191-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chrome (computer)
- task: Find a file downloaded with Chrome (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/95759?hl=en

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

## tr191-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chrome (computer)
- task: Find a file downloaded with Chrome (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/95759?hl=en

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

## tr192-a
- scenario: direct | style: plain | specification: fully_specified | platform: Chrome (computer)
- task: Save and find passwords with Google Password Manager (Chrome (computer)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/95606?hl=en

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
3. Under **Passwords**, select the site.
4. On the right of your password, select **Show password**.

## tr192-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Chrome (computer)
- task: Save and find passwords with Google Password Manager (Chrome (computer)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/95606?hl=en

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

## tr192-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Chrome (computer)
- task: Save and find passwords with Google Password Manager (Chrome (computer)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/95606?hl=en

**USER:**
i want chrome to remember my passwords so i dont have to write them down

**ASSISTANT:**
I can help with that. Are you using Chrome on a **computer** or on a **phone**?

**USER:**
my computer

**ASSISTANT:**
Thanks. Chrome can save a password when you sign in to a site:

1. Go to the site's sign-in page.
2. Enter your username and password, then submit the form.
3. When Chrome asks to save the password, select **Save**.

To see it again later:
1. At the top right, click **More**.
2. Click **Passwords and autofill**, then **Google Password Manager**.
3. Under **Passwords**, select the site.
4. On the right of your password, select **Show password**.

## tr192-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Chrome (computer)
- task: Save and find passwords with Google Password Manager (Chrome (computer)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/95606?hl=en

**USER:**
My husband and I share one Windows computer and Chrome has my passwords saved. I don't want him to be able to just click and see them. Can I make Chrome check that it is really me before it shows a saved password?

**ASSISTANT:**
Yes. On Windows, you can turn on a check:

1. At the top right, click **More**.
2. Click **Passwords and autofill**, then **Google Password Manager**.
3. Select **Settings**.
4. Turn on **Use Windows Hello when filling passwords**.
5. Follow the on-screen instructions to confirm.

After that, Chrome asks you to verify who you are before it lets anyone reveal, copy, or edit a password.

## tr192-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Chrome (computer)
- task: Save and find passwords with Google Password Manager (Chrome (computer)) | sensitive: True | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/95606?hl=en

**USER:**
How do I get Chrome on my computer to save a password when I sign in to a website?

**ASSISTANT:**
Here is how:

1. Go to the site's sign-in page.
2. Enter your username and password, then submit the form.
3. When Chrome asks to save the password, select **Save**.

**USER:**
Chrome never asks me to save anything. I sign in and no question comes up.

**ASSISTANT:**
Let's check the setting:

1. At the top right, click **More**.
2. Click **Passwords and autofill**, then **Google Password Manager**.
3. Select **Settings** on the left.
4. Make sure **Offer to save passwords and passkeys** is turned on.

If you said no to that site before, find **Declined sites and apps** on the same page and remove the site. Chrome can then offer to save it again.
