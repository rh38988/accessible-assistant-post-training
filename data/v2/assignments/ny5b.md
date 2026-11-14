# Assignment: batch ny5b

Spec file: `data/v2/specs/ny5b.py`

Publisher: Microsoft (support.microsoft.com). Use the Windows 11 steps when a page covers both Windows 10 and 11.

Write these 6 tasks, 6 examples each. Use the task_id and task_type exactly as given. Each task must use a different official page.

| task_id | task_type | task | platform | category | sensitive |
|---|---|---|---|---|---|
| TR-180 | date_time | Fix the wrong date or time | Windows 11 | technical_support | False |
| TR-181 | organize_files | Create a folder and move files into it | Windows 11 (File Explorer) | technical_support | False |
| TR-182 | restore_deleted_file | Get back a deleted file from the Recycle Bin | Windows 11 | technical_support | False |
| TR-183 | virus_scan | Run a virus scan with Windows Security | Windows 11 | technical_support | False |
| TR-184 | backup_photos | Back up photos and folders with OneDrive | Windows 11 (OneDrive) | technical_support | False |
| TR-185 | account_password_reset | Reset a forgotten Microsoft account password | Microsoft account | online_services | True |

Backup topics (if a topic's page cannot be read or does not cover the core action, replace it with one of these and reuse that topic's task_id; if you run out, deliver fewer tasks):

- mouse_settings | Change mouse settings such as speed | Windows 11 | technical_support | False
- two_step_verification | Turn on two-step verification for the Microsoft account | Microsoft account | online_services | True

Tasks marked sensitive True that are about settings or accounts (not scams) still use the normal device table (a, c, b, d, e, r).

Notes: For brightness, write only about brightness (not night light or dark mode). On computer tasks the missing detail is usually Windows PC versus Mac.
