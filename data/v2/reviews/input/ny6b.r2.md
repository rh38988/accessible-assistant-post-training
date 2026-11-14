# Review input: batch ny6b, round 2 (7 examples)

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
3. Select **Allow quieter notification prompts**.
4. Choose **Allow sites to ask to send notifications**.
5. Select **Use quieter messaging**.

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

If you do not see the site in that list, select **Add** next to **Not allowed to send pop-ups or use redirects**, type the site's web address, then select **Add**.

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
4. Next to **Manage languages**, select **Add languages**.
5. Choose Spanish. Chrome downloads the language pack by itself.
6. Next to **Preferred caption language**, select the down arrow.
7. Choose Spanish.

The words will appear in a bubble while the show plays.

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
6. Click **Delete** at the top right.
7. If a box asks you to confirm, read the wording and check the box to continue.
8. Click **Move to trash**.

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
The total can take 48 to 72 hours to update after a large deletion, so please wait that long first. If it is still full after that, automatic backup may be filling the space again. Files waiting to be backed up are added to fill the free space unless automatic backup is turned off.

## tr198-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Google Maps (computer)
- task: Get directions on a computer (Google Maps (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/maps/answer/144339 ; https://support.google.com/maps/answer/7101463

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
5. Check the box next to **Tolls**.
