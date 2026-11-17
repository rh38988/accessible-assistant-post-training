# Review input: pilot, round 4 (1 candidates)

## gsft-find_downloads-02
- candidate_id: gsft-find_downloads-02-v4
- conversation_sha256: 3c6791e8d646386c86c872b3a646a4a84b9225226b3f7dd080f365f455fe237e
- task_group: find_downloads | behavior: direct | tags: conditional, distractor
- route: answer
- decision basis (writer's): The user states a Windows 11 laptop and asks how to reach the Downloads folder, so the Windows 11 File Explorer passages apply. The Chrome passage is the inapplicable distractor. The page says Downloads is one of the known folders in Quick access and that files can be searched from a folder like Downloads. It does not say where email attachments are saved, so the reply does not claim that. Microsoft lists the six known folders under 'Restore known folders if you have unpinned them', so Downloads may be missing from Quick access; the restore steps are kept as a condition.

Conversation (the model sees only the user turns, joined):
> **user:** I'm on my Windows 11 laptop. Yesterday I saved an attachment from an email, and I think it went into my Downloads folder, but I don't know how to get there. How do I find the Downloads folder and look for the file?

Passages the model sees (in this order):
- [find-downloads-win11-taskbar] platform: Windows 11 | app: File Explorer
  > On Windows 11: 1. Select File Explorer from the taskbar. 2. To find files stored inside a folder, search from a folder like Downloads.
- [find-downloads-win11-quickaccess] platform: Windows 11 | app: File Explorer
  > On Windows 11: In File Explorer, the Quick access view displays all 6 known Windows folders: Desktop, Documents, Downloads, Pictures, Music, and Videos.
- [find-downloads-win11-restore] platform: Windows 11 | app: File Explorer
  > On Windows 11, if you have unpinned a folder such as Downloads from Quick access: 1. Select Start > File Explorer, or select the File Explorer icon in the taskbar. 2. Select Home in the left navigation pane. 3. Select the Up arrow from the navigation buttons available to the left of the address bar. 4. Select and hold (or right-click) on the folder you wish to restore and select Pin to Quick access from the context menu.
- [find-downloads-chrome-menu] platform: Chrome on computer | app: Chrome
  > On Chrome on a computer: 1. At the top right, click More, then Downloads. 2. To open a file, click its name. It will open in your computer's default application for the file type.

Source references to check:
- find-downloads-win11-taskbar: Microsoft, "Find your files and apps in Windows | Microsoft Support" <https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/find-your-files-and-apps-in-windows> | section: Find your files > Search from File Explorer | applicability: Windows 11 (the page's Applies To line names Windows 11 and Windows 10) | excerpt: "To find files stored inside a folder, search from a folder like Downloads."
- find-downloads-win11-quickaccess: Microsoft, "File Explorer in Windows | Microsoft Support" <https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8> | section: Restore known folders if you have unpinned them | applicability: Windows 11 and Windows 10 (the page's Applies To line) | excerpt: "This view displays all 6 known Windows folders: Desktop, Documents, Downloads, Pictures, Music, and Videos."
- find-downloads-win11-restore: Microsoft, "File Explorer in Windows | Microsoft Support" <https://support.microsoft.com/en-us/windows/find-my-downloads-in-windows-10-de903ee9-7d37-256b-9145-f0f016c5aed8> | section: Restore known folders if you have unpinned them | applicability: Windows 11 and Windows 10 (the page's Applies To line) | excerpt: "Select and hold (or right-click) on the folder you wish to restore and select Pin to Quick access from the context menu."
- find-downloads-chrome-menu: Google, "Download a file - Computer - Google Chrome Help" <https://support.google.com/chrome/answer/95759?hl=en> | section: Find a list of files you've downloaded | applicability: Google Chrome on a computer | excerpt: "At the top right, click More ... and then Downloads."

TARGET (read only after step 2)

> Here is how to find your Downloads folder on your Windows 11 laptop:
> 1. Select **File Explorer** from the taskbar.
> 2. In **Quick access**, look for **Downloads**. It is one of the known Windows folders shown there.
> 3. To find your file, search from the **Downloads** folder.
> 
> If Downloads is not in Quick access because it was unpinned: select **Home** in the left navigation pane, select the **Up** arrow to the left of the address bar, then select and hold (or right-click) **Downloads** and select **Pin to Quick access**.

---
