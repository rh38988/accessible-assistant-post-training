# Review input: batch ny5b, round 1 (36 examples)

## tr180-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Fix the wrong date or time (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/dfaa7122-479f-5b98-2a7b-fa0b6e01b261

**USER:**
The clock on my Windows 11 computer is showing the wrong time. How can I get it to set itself correctly?

**ASSISTANT:**
Windows can set the time for you. Here is how.

1. Click **Start**, then **Settings**.
2. Click **Time & language**.
3. Click **Date & time**.
4. Turn on **Set time automatically**.

If the time is still wrong, check that **Set time zone automatically** is also turned on in the same screen.

## tr180-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Fix the wrong date or time (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/dfaa7122-479f-5b98-2a7b-fa0b6e01b261

**USER:**
My husband says the clocks went back an hour last weekend but my Windows 11 laptop is now showing one hour off. I turned off the automatic time zone thing a while ago because it kept putting me in the wrong city. I would like it to follow the daylight saving change without me doing it by hand each time. Can you tell me what to do?

**ASSISTANT:**
You can turn on a setting that changes the clock for daylight saving time on its own.

1. Click **Start**, then **Settings**.
2. Click **Time & language**.
3. Click **Date & time**.
4. Turn on **Adjust for daylight saving time automatically**.

Since your automatic time zone is off, this is the setting that handles the change. Your time zone stays as you chose it.

## tr180-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Fix the wrong date or time (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/dfaa7122-479f-5b98-2a7b-fa0b6e01b261

**USER:**
my computer clock is wrong again, can you help me fix it

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

## tr180-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Fix the wrong date or time (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/dfaa7122-479f-5b98-2a7b-fa0b6e01b261

**USER:**
my computer clock is wrong again, can you help me fix it

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

**USER:**
Windows 11

**ASSISTANT:**
Thanks. Here is how to let Windows set the time itself.

1. Click **Start**, then **Settings**.
2. Click **Time & language**.
3. Click **Date & time**.
4. Turn on **Set time automatically**.

If it is still wrong, make sure **Set time zone automatically** is turned on too.

## tr180-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Fix the wrong date or time (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/dfaa7122-479f-5b98-2a7b-fa0b6e01b261

**USER:**
I have a Windows 11 PC and I do not want Windows to change the time by itself, I want to type in the date and time myself. Today is the right date but it shows the wrong hour. How do I type it in?

**ASSISTANT:**
You can set it by hand. Here is how.

1. Click **Start**, then **Settings**.
2. Click **Time & language**.
3. Click **Date & time**.
4. Turn off **Set time automatically**.
5. Click **Change** next to **Set the date and time**. A **Change date and time** window opens.
6. Enter the **Date** and **Time**.
7. Click **Change**.

## tr180-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Fix the wrong date or time (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/dfaa7122-479f-5b98-2a7b-fa0b6e01b261

**USER:**
My Windows 11 computer has the wrong date. I want to type in the right one myself. What do I do?

**ASSISTANT:**
You can change it by hand.

1. Click **Start**, then **Settings**.
2. Click **Time & language**.
3. Click **Date & time**.
4. Turn off **Set time automatically**.
5. Click **Change** next to **Set the date and time**.
6. Enter the **Date** and **Time**, then click **Change**.

**USER:**
I opened Date & time but I can't find a Change button to click, or it won't let me click it.

**ASSISTANT:**
The **Change** button works only after you turn off the automatic setting.

1. On the **Date & time** screen, find **Set time automatically**.
2. Turn it off.
3. Now click **Change** next to **Set the date and time**.

A **Change date and time** window should open so you can enter the date.

## tr181-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Create a folder and move files into it (Windows 11 (File Explorer)) | sensitive: False | reviewed by a person: False
- sources: https://www.microsoft.com/en-us/windows/learning-center/create-new-folders-to-organize-files

**USER:**
On my Windows 11 computer, how do I make a new folder and put a file in it?

**ASSISTANT:**
Here is how to make a folder and move a file into it.

1. Open **File Explorer**.
2. Select **Home** in the upper-left corner of the window.
3. Click the **New folder** icon. A new folder appears, ready for a name.
4. Right-click the name of the new folder and type the name you want.
5. Select the file you want to move.
6. Drag the file into the new folder.

## tr181-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Create a folder and move files into it (Windows 11 (File Explorer)) | sensitive: False | reviewed by a person: False
- sources: https://www.microsoft.com/en-us/windows/learning-center/create-new-folders-to-organize-files

**USER:**
My grandson set up this Windows 11 computer for me and now everything I save piles up in one big mess. I want a folder just for my recipes and then to put my recipe documents in it. I only know how to use File Explorer a little bit. Could you walk me through making the folder first and then moving them over?

**ASSISTANT:**
Happy to. Start with the folder.

1. Open **File Explorer**.
2. Select **Home** in the upper-left corner of the window.
3. Click the **New folder** icon.
4. Right-click the name of the new folder and type **Recipes**.

Now move the recipes.

5. Select one recipe document.
6. Drag it into the new folder.

To move several at once, select each one first, then drag the group into the folder together.

## tr181-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Create a folder and move files into it (Windows 11 (File Explorer)) | sensitive: False | reviewed by a person: False
- sources: https://www.microsoft.com/en-us/windows/learning-center/create-new-folders-to-organize-files

**USER:**
I need to make a folder so I can put my tax papers in it

**ASSISTANT:**
I can help with that. Are you using a **Windows PC** or a **Mac**?

## tr181-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Create a folder and move files into it (Windows 11 (File Explorer)) | sensitive: False | reviewed by a person: False
- sources: https://www.microsoft.com/en-us/windows/learning-center/create-new-folders-to-organize-files

**USER:**
I need to make a folder so I can put my tax papers in it

**ASSISTANT:**
I can help with that. Are you using a **Windows PC** or a **Mac**?

**USER:**
windows 11

**ASSISTANT:**
Here is how to make the folder and move your papers into it.

1. Open **File Explorer**.
2. Select **Home** in the upper-left corner of the window.
3. Click the **New folder** icon.
4. Right-click the name of the new folder and type a name such as Taxes.
5. Select a tax file.
6. Drag it into the new folder.

## tr181-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Create a folder and move files into it (Windows 11 (File Explorer)) | sensitive: False | reviewed by a person: False
- sources: https://www.microsoft.com/en-us/windows/learning-center/create-new-folders-to-organize-files

**USER:**
I have a Windows 11 PC and about twenty vacation photos in File Explorer that I want in one new folder. I do not want to drag them one at a time because my hand shakes, so is there a way to move all of them together?

**ASSISTANT:**
Yes, you can select them all and move them in one drag.

1. In **File Explorer**, select **Home** in the upper-left corner.
2. Click the **New folder** icon, or press **Ctrl + Shift + N**.
3. Right-click the name of the new folder and type a name for it.
4. Select each of your photos.
5. Drag the whole group into the new folder at once.

## tr181-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Create a folder and move files into it (Windows 11 (File Explorer)) | sensitive: False | reviewed by a person: False
- sources: https://www.microsoft.com/en-us/windows/learning-center/create-new-folders-to-organize-files

**USER:**
Windows 11 here. How do I make a new folder in File Explorer?

**ASSISTANT:**
Here is how.

1. Open **File Explorer**.
2. Select **Home** in the upper-left corner of the window.
3. Click the **New folder** icon.

A new folder appears in the window, ready for a name.

**USER:**
OK I made it but it just has a plain name and I want to call it Insurance. How do I change the name?

**ASSISTANT:**
You can rename it from the folder's name.

1. Right-click the name of the new folder.
2. Type **Insurance** as the new name.

Next time you can also press **Ctrl + Shift + N** to make a new folder without using the menu.

## tr182-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Change mouse settings such as speed (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/hardware/input-devices/change-mouse-settings

**USER:**
The mouse pointer on my Windows 11 computer moves too fast and I keep overshooting. How can I slow it down?

**ASSISTANT:**
You can change the pointer speed with a slider.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Mouse**.
4. Move the slider next to **Mouse pointer speed** to change how fast the pointer moves.

Try the mouse on the screen after each change to see if the speed feels right.

## tr182-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Change mouse settings such as speed (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/hardware/input-devices/change-mouse-settings

**USER:**
I am left handed and I have always used my mouse in my left hand, but on my new Windows 11 computer the left button does the clicking that the right button should do for me. I would like the right button to be the main one. Where is that setting?

**ASSISTANT:**
There is a setting for exactly that.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Mouse**.
4. Open the drop-down next to **Primary mouse button**.
5. Choose **Right**.

## tr182-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Change mouse settings such as speed (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/hardware/input-devices/change-mouse-settings

**USER:**
my mouse is too slow, how do i change it

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

## tr182-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Change mouse settings such as speed (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/hardware/input-devices/change-mouse-settings

**USER:**
my mouse is too slow, how do i change it

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

**USER:**
it's a windows 11 pc

**ASSISTANT:**
Thanks. You can change the pointer speed with a slider.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Mouse**.
4. Move the slider next to **Mouse pointer speed**.

Try the pointer after each change to find a speed you like.

## tr182-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Change mouse settings such as speed (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/hardware/input-devices/change-mouse-settings

**USER:**
On my Windows 11 PC the pointer speed is fine and so is the left button. The only thing that bothers me is that I have to click twice so fast to open a file that I often miss. Please don't change anything else, just the double click timing.

**ASSISTANT:**
That is a separate setting, so nothing else will change.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Mouse**.
4. Under **Related settings**, click **Additional mouse settings**.
5. Click the **Buttons** tab.
6. Under **Double-click speed**, adjust the **Speed:** slider.
7. Click **OK**.

## tr182-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Change mouse settings such as speed (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/hardware/input-devices/change-mouse-settings

**USER:**
Windows 11 computer. I double click too slowly and the computer thinks I only clicked once. How do I give myself more time between the clicks?

**ASSISTANT:**
You can change the double-click speed.

1. Click **Start**, then **Settings**.
2. Click **Bluetooth & devices**.
3. Click **Mouse**.
4. Click **Additional mouse settings**.
5. Click the **Buttons** tab.
6. Under **Double-click speed**, adjust the **Speed:** slider.
7. Click **OK**.

**USER:**
I'm on the Mouse page but I don't see anything called Additional mouse settings.

**ASSISTANT:**
It is a link lower down on the same **Mouse** page.

1. Scroll down the **Mouse** page until you see **Related settings**.
2. Click **Additional mouse settings** there.
3. Then continue with the **Buttons** tab as before.

## tr183-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Run a virus scan with Windows Security (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/virus-and-threat-protection-in-the-windows-security-app-1362f4cd-d71a-b52a-0b66-c2820032b65e

**USER:**
How do I check my Windows 11 computer for viruses with the built in security program?

**ASSISTANT:**
You can run a quick scan in Windows Security.

1. Search for **Windows Security** in the Start menu and open it.
2. Select **Virus & threat protection**.
3. Under **Current threats**, select **Start a quick scan**.

The scan runs and reports when it finishes. You can see the last scan time and how many files were scanned in the same place.

## tr183-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Run a virus scan with Windows Security (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/virus-and-threat-protection-in-the-windows-security-app-1362f4cd-d71a-b52a-0b66-c2820032b65e

**USER:**
My Windows 11 laptop has been acting strange since I opened an email attachment last night and I am worried something got on it. I do not have time for a long scan right now, I just want the fastest check Windows can do. Which button do I press?

**ASSISTANT:**
The quick scan is the faster option.

1. Search for **Windows Security** in the Start menu and open it.
2. Select **Virus & threat protection**.
3. Under **Current threats**, select **Start a quick scan**.

When it finishes, look under **Current threats** to see what was scanned and whether any threats were quarantined.

## tr183-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Run a virus scan with Windows Security (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/virus-and-threat-protection-in-the-windows-security-app-1362f4cd-d71a-b52a-0b66-c2820032b65e

**USER:**
i think i have a virus, how do i scan my computer

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

## tr183-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Run a virus scan with Windows Security (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/virus-and-threat-protection-in-the-windows-security-app-1362f4cd-d71a-b52a-0b66-c2820032b65e

**USER:**
i think i have a virus, how do i scan my computer

**ASSISTANT:**
I can help with that. Is your computer a **Windows PC** or a **Mac**?

**USER:**
Windows 11

**ASSISTANT:**
Thanks. Windows has a scan built in.

1. Search for **Windows Security** in the Start menu and open it.
2. Select **Virus & threat protection**.
3. Under **Current threats**, select **Start a quick scan**.

When it finishes, the same area shows what was scanned and any threats that were quarantined.

## tr183-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Run a virus scan with Windows Security (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/virus-and-threat-protection-in-the-windows-security-app-1362f4cd-d71a-b52a-0b66-c2820032b65e

**USER:**
I have a Windows 11 PC and I want the most thorough virus check possible, even if it takes a long time. I plan to leave it running overnight. Which scan should I pick in Windows Security?

**ASSISTANT:**
The full scan checks everything.

1. Search for **Windows Security** in the Start menu and open it.
2. Select **Virus & threat protection**.
3. Under **Current threats**, select **Scan options**.
4. Select **Start a full scan**.

A full scan checks every file and program on your device, so it takes longer than a quick scan.

## tr183-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Run a virus scan with Windows Security (Windows 11) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/windows/virus-and-threat-protection-in-the-windows-security-app-1362f4cd-d71a-b52a-0b66-c2820032b65e

**USER:**
How do I run a virus scan on my Windows 11 PC?

**ASSISTANT:**
Here is a quick way.

1. Search for **Windows Security** in the Start menu and open it.
2. Select **Virus & threat protection**.
3. Under **Current threats**, select **Start a quick scan**.

**USER:**
It says the scans aren't running and I think I installed another antivirus program a while ago. What now?

**ASSISTANT:**
That is likely the reason. When a compatible antivirus program from another company is installed, Microsoft Defender Antivirus turns itself off on its own.

1. Open that other antivirus program.
2. Run the scan from there instead.

## tr184-a
- scenario: direct | style: plain | specification: fully_specified | platform: Windows 11
- task: Back up photos and folders with OneDrive (Windows 11 (OneDrive)) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/back-up-your-folders-with-onedrive-d61a7930-a6fb-4b95-b28a-6552e77c3057

**USER:**
How can I back up the pictures on my Windows 11 computer using OneDrive?

**ASSISTANT:**
You can turn on backup for your Pictures folder in OneDrive.

1. Select the OneDrive cloud icon in the notification area.
2. Select the **Help & Settings** icon, then select **Settings**.
3. Select the **Sync and backup** tab.
4. Select **Manage backup**.
5. Turn on the toggle for **Pictures**.
6. Select **Save changes**.

Your backed up folders then show up in File Explorer under OneDrive.

## tr184-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Windows 11
- task: Back up photos and folders with OneDrive (Windows 11 (OneDrive)) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/back-up-your-folders-with-onedrive-d61a7930-a6fb-4b95-b28a-6552e77c3057

**USER:**
My old computer died last year and I lost everything, so I never want that to happen again. I have a Windows 11 PC now with OneDrive already on it. I keep my letters in Documents and my family photos in Pictures. Please show me how to have OneDrive keep copies of both.

**ASSISTANT:**
OneDrive can back up both folders.

1. Select the OneDrive cloud icon in the notification area.
2. Select the **Help & Settings** icon, then select **Settings**.
3. Select the **Sync and backup** tab.
4. Select **Manage backup**.
5. Turn on the toggle for **Documents** and for **Pictures**.
6. Select **Save changes**.

Your backed up folders then show up in File Explorer under OneDrive.

## tr184-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Back up photos and folders with OneDrive (Windows 11 (OneDrive)) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/back-up-your-folders-with-onedrive-d61a7930-a6fb-4b95-b28a-6552e77c3057

**USER:**
I want to make sure my photos are safe, can you help me back them up with OneDrive?

**ASSISTANT:**
I can help with that. Are your photos on a **Windows PC** or a **Mac**?

## tr184-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Windows 11
- task: Back up photos and folders with OneDrive (Windows 11 (OneDrive)) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/back-up-your-folders-with-onedrive-d61a7930-a6fb-4b95-b28a-6552e77c3057

**USER:**
I want to make sure my photos are safe, can you help me back them up with OneDrive?

**ASSISTANT:**
I can help with that. Are your photos on a **Windows PC** or a **Mac**?

**USER:**
Windows 11 PC

**ASSISTANT:**
Thanks. Here is how to back up your Pictures folder.

1. Select the OneDrive cloud icon in the notification area.
2. Select the **Help & Settings** icon, then select **Settings**.
3. Select the **Sync and backup** tab.
4. Select **Manage backup**.
5. Turn on the toggle for **Pictures**.
6. Select **Save changes**.

## tr184-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Windows 11
- task: Back up photos and folders with OneDrive (Windows 11 (OneDrive)) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/back-up-your-folders-with-onedrive-d61a7930-a6fb-4b95-b28a-6552e77c3057

**USER:**
I use Windows 11 and OneDrive. I only want my photos backed up. My Desktop is full of things I do not want in the cloud and I do not want my Documents copied either. How do I back up just Pictures?

**ASSISTANT:**
You choose each folder with its own toggle, so you can pick only Pictures.

1. Select the OneDrive cloud icon in the notification area.
2. Select the **Help & Settings** icon, then select **Settings**.
3. Select the **Sync and backup** tab.
4. Select **Manage backup**.
5. Turn on the toggle for **Pictures** only. Leave **Desktop** and **Documents** off.
6. Select **Save changes**.

## tr184-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Windows 11
- task: Back up photos and folders with OneDrive (Windows 11 (OneDrive)) | sensitive: False | reviewed by a person: False
- sources: https://support.microsoft.com/en-us/office/back-up-your-folders-with-onedrive-d61a7930-a6fb-4b95-b28a-6552e77c3057

**USER:**
Windows 11 PC. How do I make OneDrive back up my Pictures folder?

**ASSISTANT:**
Here is how.

1. Select the OneDrive cloud icon in the notification area.
2. Select the **Help & Settings** icon, then select **Settings**.
3. Select the **Sync and backup** tab.
4. Select **Manage backup**.
5. Turn on the toggle for **Pictures**.
6. Select **Save changes**.

**USER:**
It gave me an error saying some of my files are online only and need to be downloaded first. What should I do?

**ASSISTANT:**
Those files are stored only in the cloud, which blocks the move. Set them to keep a copy on your computer first.

1. Find the online only files in your Pictures folder.
2. Set them to **Always keep on this device**.
3. Go back to **Manage backup** and try **Save changes** again.

## tr185-a
- scenario: direct | style: plain | specification: fully_specified | platform: Microsoft account
- task: Reset a forgotten Microsoft account password (Microsoft account) | sensitive: True | reviewed by a person: False
- sources: https://support.microsoft.com/help/4026971

**USER:**
I forgot the password for my Microsoft account and I'm on the sign in screen. What do I do?

**ASSISTANT:**
You can reset it with a code that Microsoft sends you.

1. On the **Enter password** window, select **Forgotten your password?**
2. Choose how you want to get a verification code, then select **Next**.
3. Retype the first part of the email address, or the last four digits of the phone number, that is shown. Select **Get code**.
4. Check that email or phone, then type the code and select **Next**.
5. Type your new password and select **Next** again.

## tr185-c
- scenario: direct_messy | style: verbose | specification: fully_specified | platform: Microsoft account
- task: Reset a forgotten Microsoft account password (Microsoft account) | sensitive: True | reviewed by a person: False
- sources: https://support.microsoft.com/help/4026971

**USER:**
I closed the sign in box on my Microsoft account by mistake and now I don't remember my password at all. I haven't used the account in months. I do still have my phone, which I think is the number linked to the account. How can I reset the password using my phone?

**ASSISTANT:**
You can start the reset again and have a code sent to your phone.

1. Select **Reset password**, enter the username for your account, and select **Next**.
2. Choose the phone option to get a verification code, then select **Next**.
3. Retype the last four digits of the phone number shown, then select **Get code**.
4. Check your phone, then type the code and select **Next**.
5. Type your new password and select **Next** again.

## tr185-b
- scenario: missing_info | style: under_specified | specification: underspecified | platform: unknown
- task: Reset a forgotten Microsoft account password (Microsoft account) | sensitive: True | reviewed by a person: False
- sources: https://support.microsoft.com/help/4026971

**USER:**
i forgot my password and cant get in, please help

**ASSISTANT:**
I can help with that. Is this the password for your **Microsoft account**, or for something else?

## tr185-d
- scenario: followup | style: under_specified | specification: fully_specified | platform: Microsoft account
- task: Reset a forgotten Microsoft account password (Microsoft account) | sensitive: True | reviewed by a person: False
- sources: https://support.microsoft.com/help/4026971

**USER:**
i forgot my password and cant get in, please help

**ASSISTANT:**
I can help with that. Is this the password for your **Microsoft account**, or for something else?

**USER:**
its my microsoft account

**ASSISTANT:**
Thanks. You can reset it with a code that Microsoft sends you.

1. Select **Forgotten your password?** if the **Enter password** window is open. If not, select **Reset password**, enter your username, and select **Next**.
2. Choose how to get a verification code, then select **Next**.
3. Retype the first part of the email address, or the last four digits of the phone number, shown. Select **Get code**.
4. Type the code and select **Next**.
5. Type your new password and select **Next** again.

## tr185-e
- scenario: constraint | style: over_specified | specification: fully_specified | platform: Microsoft account
- task: Reset a forgotten Microsoft account password (Microsoft account) | sensitive: True | reviewed by a person: False
- sources: https://support.microsoft.com/help/4026971

**USER:**
I forgot my Microsoft account password. I don't want to call anyone or wait for a person to help me. Is there a way to do the whole reset myself on the computer? I can read my email.

**ASSISTANT:**
Yes, you can do the whole reset yourself. A support agent can't send reset links or change account details for you anyway.

1. Select **Reset password**, enter your username, and select **Next**.
2. Choose the email option for a verification code, then select **Next**.
3. Retype the first part of the email address shown, then select **Get code**.
4. Open that email, then type the code and select **Next**.
5. Type your new password and select **Next** again.

## tr185-r
- scenario: failure_recovery | style: failure_recovery | specification: fully_specified | platform: Microsoft account
- task: Reset a forgotten Microsoft account password (Microsoft account) | sensitive: True | reviewed by a person: False
- sources: https://support.microsoft.com/help/4026971

**USER:**
I forgot my Microsoft account password. How do I reset it?

**ASSISTANT:**
You can reset it with a code that Microsoft sends you.

1. Select **Forgotten your password?** on the **Enter password** window. If you do not see it, select **Reset password**, enter your username, and select **Next**.
2. Choose how to get a verification code, then select **Next**.
3. Retype the first part of the email address, or the last four digits of the phone number, shown. Select **Get code**.
4. Type the code and select **Next**.
5. Type your new password and select **Next** again.

**USER:**
It only shows an old email address and a phone number I don't have anymore, so I can't get a code.

**ASSISTANT:**
Then use Microsoft's sign-in helper tool. It is meant for when you no longer have access to any of the options shown.

1. Go to https://go.microsoft.com/fwlink/?linkid=2242650
2. Follow the steps the tool gives you.

Support agents can't send reset links or change your account details, so the tool is the way forward.
