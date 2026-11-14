# Review input: batch ny6a, round 3 (5 examples)

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
You can put it back in one step. On Windows, hold down the **Ctrl** key and press the **0** key. That resets the page to the default size.

Or you can go back to **Settings and more** and select **Zoom out** until it looks right.

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
3. Under **Passwords**, select the password.
4. On the right of your password, select **Show password**.

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
3. Under **Passwords**, select the password.
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

Once it is on, Windows Hello is used when Chrome fills in a saved password, and this check can also cover revealing, copying, or editing a password. The setting is optional and off by default, so it stays off until you turn it on.
