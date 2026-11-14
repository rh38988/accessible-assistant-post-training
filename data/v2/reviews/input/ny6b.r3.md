# Review input: batch ny6b, round 3 (2 examples)

## tr194-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Chrome (computer)
- task: Turn on Live Caption (Chrome (computer)) | sensitive: False | reviewed by a person: False
- sources: https://support.google.com/chrome/answer/10538231

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
The total can take 48 to 72 hours to update after a large deletion, so please wait that long first.

If it is still full after 48 to 72 hours, some photos and videos may be set to back up automatically. Automatic backup can be turned off, and then files waiting to be backed up will stop using the free space.
