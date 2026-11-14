S2 = {"steps": 2, "ask_or_answer": 2, "constraints": 2, "actionable": 2, "plain": 2, "realistic_user": 2}
def sc(**k):
    d = dict(S2); d.update(k); return d
G = {"source": "pass", "safety": "pass", "duplicate": "pass"}
def gs(**k):
    d = dict(G); d.update(k); return d
REVIEWS = []

# ---- Page 1: Outlook attach (tr199) ----
_RA199 = ["Attach a file from this computer: select Attach (page, New Outlook tab: Attach File) (critical)",
          "Choose Browse this computer (page: Browse This Computer) (critical)",
          "Pick the file, then Open (critical)"]
_UNV = "WebFetch twice returned only the New Outlook (desktop app) tab; the Outlook.com / Outlook on the web tab text was not available, so these web labels could not be verified."
_FIXU = "Source page text for the Outlook.com (Web) tab could not be read. Re-verify against the Web tab (or add a readable official Microsoft page for Outlook on the web) and confirm the exact labels Attach, Browse this computer, Browse cloud locations, Next, More actions, Manage access, and the CTRL/Command multi-select claim before re-submitting. Do not change the text until the labels are confirmed."
REVIEWS += [
 {"id": "tr199-a", "required_actions": _RA199, "covered": [True, True, True], "needs_clarification": False,
  "gates": gs(source="unverified"),
  "unsupported_claims": ["'select **Attach**' / '**Browse this computer**' / 'hold the CTRL key' -> " + _UNV + " The only readable text (New Outlook) says 'Attach File' and 'Browse This Computer'; CTRL multi-select is not on the readable page."],
  "scores": sc(), "decision": "revise", "reasons": "source unreadable. " + _UNV, "fix": _FIXU},
 {"id": "tr199-c", "required_actions": _RA199 + ["Select several files at once (multi-select key) (critical for this user)"], "covered": [True, True, True, True], "needs_clarification": False,
  "gates": gs(source="unverified"),
  "unsupported_claims": ["'Hold down the Command key, then click each of the other three pictures.' -> not on the readable page; Mac Command-key multi-select is not stated in the readable source text. " + _UNV],
  "scores": sc(), "decision": "revise", "reasons": "source unreadable. " + _UNV, "fix": _FIXU},
 {"id": "tr199-b", "required_actions": [], "covered": [], "needs_clarification": True,
  "gates": gs(), "unsupported_claims": [],
  "scores": sc(steps="NA"), "decision": "keep", "reasons": "", "fix": ""},
 {"id": "tr199-d", "required_actions": _RA199, "covered": [True, True, True], "needs_clarification": False,
  "gates": gs(source="unverified"),
  "unsupported_claims": ["'Select **Attach**' / '**Browse this computer**' -> " + _UNV, "'you can also drag the document from your computer into the message' -> readable page mentions drag and drop only for attaching an email in New Outlook, not for files from the computer."],
  "scores": sc(), "decision": "revise", "reasons": "source unreadable. " + _UNV, "fix": _FIXU},
 {"id": "tr199-e", "required_actions": ["Attach, then pick a OneDrive/cloud location (critical)", "Choose the file (critical)", "Choose link or copy (page says OneDrive files can be sent as a link)", "Optional: set permissions / Manage access"], "covered": [True, True, True, True], "needs_clarification": False,
  "gates": gs(source="unverified"),
  "unsupported_claims": ["'Select **Browse cloud locations**' and 'Select **Next**' -> not on the readable page (page says 'Locations include OneDrive, SharePoint sites, or connected third-party cloud storage providers').", "'select **More actions**, then **Manage access**' -> readable page only says to select Manage access to resolve a warning, and set permissions via the arrow beside the attachment name; 'More actions' is not supported. " + _UNV],
  "scores": sc(), "decision": "revise", "reasons": "source unreadable. " + _UNV, "fix": _FIXU},
 {"id": "tr199-r", "required_actions": _RA199 + ["Select several files at once (multi-select key) (critical for the follow-up)"], "covered": [True, True, True, True], "needs_clarification": False,
  "gates": gs(source="unverified"),
  "unsupported_claims": ["'Hold down the CTRL key (the Command key on a Mac)' -> not on the readable page.", "'You can also drag the pictures from your computer into the message.' -> readable page mentions drag and drop only for attaching an email. " + _UNV],
  "scores": sc(), "decision": "revise", "reasons": "source unreadable. " + _UNV, "fix": _FIXU},
]

# ---- Page 2: Outlook.com can't receive (tr200) ----
_RA200 = ["Check the Other tab and make sure no filters hide messages", "Check the Junk Email folder", "Right-click a wrongly filtered message and choose Mark as not junk (moves it to Inbox)", "Check email forwarding is not enabled", "Check email rules", "Check Microsoft cloud storage is not full", "If one email is missing, ask the sender to review Sender Support in Outlook.com", "Filter > Sort > Date restores chronological order"]
REVIEWS += [
 {"id": "tr200-a", "required_actions": ["Check the Other tab and ensure no filters hide messages", "Check Junk Email folder", "Right-click message, Mark as not junk (moves to inbox)", "Check forwarding / rules / storage / sender support (for the remaining case)"], "covered": [True, True, True, True], "needs_clarification": False,
  "gates": gs(), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
 {"id": "tr200-c", "required_actions": ["Recognize full Microsoft cloud storage blocks send and receive (critical)", "Check mailbox storage to see what is taking up space (critical)", "Free up space (critical)", "Note that messages sent while storage was full bounced and cannot be recovered; sender must resend"], "covered": [True, True, True, True], "needs_clarification": False,
  "gates": gs(), "unsupported_claims": [],
  "scores": sc(actionable=1), "decision": "revise",
  "reasons": "Steps 1 and 2 have no starting point: 'Open your mailbox storage page' and 'Free up some space' do not say where the page is or how to free space. The cited page gives no menu path either ('Check your mailbox storage to see what's taking up space').",
  "fix": "Add a second official source that gives the path and ways to free space, e.g. https://support.microsoft.com/office/storage-limits-in-outlook-com-7ac99134-69e5-4619-ac0b-2d313bba5e9e (verify it first), then rewrite steps 1-2 with the exact Settings path and the exact label(s) for what to delete or empty. If the path cannot be verified, state the cited-page wording only ('Check your mailbox storage to see what is taking up space') and say plainly that deleting large or old messages and emptying Deleted Items frees space only if the second page supports it."},
 {"id": "tr200-b", "required_actions": [], "covered": [], "needs_clarification": True,
  "gates": gs(), "unsupported_claims": [], "scores": sc(steps="NA"), "decision": "keep", "reasons": "", "fix": ""},
 {"id": "tr200-d", "required_actions": ["Open Junk Email folder; Mark as not junk", "Check forwarding is not enabled", "Check email rules", "Check storage not full", "Sender Support for single missing sender"], "covered": [True, True, True, True, True], "needs_clarification": False,
  "gates": gs(), "unsupported_claims": [],
  "scores": sc(actionable=1), "decision": "revise",
  "reasons": "Steps 2 and 3 ('Check whether email forwarding is turned on', 'Check for email rules') and step 4 give no starting point or what the user will see; the cited page itself gives no Settings path for these. Step 1 also lacks where to find the Junk Email folder, but the folder name is on the page. Also omits the Other tab/filter check, which the page lists.",
  "fix": "Either add a second verified Microsoft page that gives the Settings path for forwarding and rules, and write those steps with exact labels, or cut steps 2-3 to the cited-page wording and keep the reply short. Add the page's 'Check your Other tab and ensure there are no filters preventing you from accessing all your messages' check. For storage, give the path only if a second page supports it."},
 {"id": "tr200-e", "required_actions": ["Check the Other tab and ensure no filters hide messages", "Open Junk Email and look for the message", "Right-click, Mark as not junk (moves to inbox)"], "covered": [True, True, True], "needs_clarification": False,
  "gates": gs(source="fail"),
  "unsupported_claims": ["'This only moves that one message to your Inbox.' -> the page says only that Mark as not junk moves the message back to the inbox; it does not say nothing else happens.", "'None of these steps changes your settings or rules.' -> 'Make sure you can see all of your messages' on the Other tab may require changing a filter; the page does not support this blanket claim."],
  "scores": sc(constraints=1), "decision": "revise",
  "reasons": "Two unsupported reassurance claims, and the Other-tab step ('Make sure you can see all of your messages') could lead the user to change a filter, against their stated limit.",
  "fix": "Delete 'This only moves that one message to your Inbox.' and 'None of these steps changes your settings or rules.' Keep: 'Right-click it and select Mark as not junk. This moves it back to your inbox.' Make step 1 look-only: 'Click the Other tab and look through it for the message.' (do not tell the user to adjust filters), and tell them to tell you if they see a filter applied."},
 {"id": "tr200-r", "required_actions": ["Select the Filter icon", "Choose Sort", "Choose Date (restores chronological order)"], "covered": [True, True, True], "needs_clarification": False,
  "gates": gs(), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": ""},
]

# ---- Page 3: Recover deleted email (tr201) ----
_K = {"gates": gs(), "unsupported_claims": [], "scores": sc(), "decision": "keep", "reasons": "", "fix": "", "needs_clarification": False}
REVIEWS += [
 {"id": "tr201-a", "required_actions": ["Open Deleted Items (critical)", "Select the message, select Restore (critical)", "If not there: select Recover items deleted from this folder above the message list, select message, Restore"], "covered": [True, True, True], **_K},
 {"id": "tr201-c", "required_actions": ["Open Deleted Items", "Select Recover items deleted from this folder (above the message list) (critical)", "Select the message (critical)", "Select Restore (critical)", "Computer needed; removed items recoverable for 30 days"], "covered": [True, True, True, True, True], **_K},
 {"id": "tr201-b", "required_actions": [], "covered": [], **{**_K, "needs_clarification": True, "scores": sc(steps="NA")}},
 {"id": "tr201-d", "required_actions": ["Open Deleted Items, select message, Restore (critical)", "Else Recover items deleted from this folder, select message, Restore", "30 days"], "covered": [True, True, True], **_K},
 {"id": "tr201-e", "required_actions": ["Phone/mobile: open Deleted Items, select message (critical)", "More options > Move to folder > Inbox (critical)", "Recover items deleted from this folder needs a computer"], "covered": [True, True, True], **_K},
 {"id": "tr201-r", "required_actions": ["Check Archive: select message, Move to > Inbox", "Past 30 days may not be recoverable", "(Also on page) Check Junk Email and the Other tab; filter set to All"], "covered": [True, True, False], "needs_clarification": False,
  "gates": gs(source="fail"),
  "unsupported_claims": ["'Archived messages do not show in your inbox.' -> not stated on the page; the page only says 'If you archived the message' select it and Move to > Inbox."],
  "scores": sc(), "decision": "revise",
  "reasons": "One unsupported sentence. Also the page's other 'if nothing turns up' checks (Junk Email, Other tab, filter set to All) are missing, which is a non-critical gap.",
  "fix": "Replace 'Check your Archive folder next. Archived messages do not show in your inbox.' with 'Check your Archive folder next, in case the message was archived.' Optionally add after the 30-day line: 'You can also check your Junk Email folder and the Other tab, and make sure your filter is set to All.' Keep the Archive steps (Open Archive, select the message, Move to, then Inbox)."},
]

# ---- Page 4: Gmail labels (tr202) ----
_PLUS = "'It looks like a plus icon.' -> the page says only 'click Create new label'; its icon has empty alt text and no text describes a plus symbol."
REVIEWS += [
 {"id": "tr202-a", "required_actions": ["Open Gmail on computer", "On the left next to Labels, click Create new label (critical)", "Enter a name (critical)", "Click Create (critical)"], "covered": [True, True, True, True], "needs_clarification": False,
  "gates": gs(source="fail"), "unsupported_claims": [_PLUS],
  "scores": sc(), "decision": "revise", "reasons": "Unsupported icon description.",
  "fix": "Delete 'It looks like a plus icon.' Keep 'On the left, next to **Labels**, click **Create new label**.' If you want to describe the control, only do so if another official Google page states it."},
 {"id": "tr202-c", "required_actions": ["Click Create new label next to Labels (critical)", "Enter the name (critical)", "Check Nest label under (critical)", "Choose the parent label (critical)", "Click Create (critical)"], "covered": [True, True, True, True, True], "needs_clarification": False, **{k: v for k, v in _K.items() if k != "needs_clarification"}},
 {"id": "tr202-b", "required_actions": [], "covered": [], **{**_K, "needs_clarification": True, "scores": sc(steps="NA")}},
 {"id": "tr202-d", "required_actions": ["Create new label next to Labels, enter name, Create (critical)", "Check the box next to an email (critical)", "Click Labels icon at the top and select the label (critical)"], "covered": [True, True, True], **_K},
 {"id": "tr202-e", "required_actions": ["Check the email's box (critical)", "Click Labels at the top (critical)", "Uncheck the current label (Misc) (critical)", "Select the new label (Recipes) (critical)"], "covered": [True, True, True, True], **_K},
 {"id": "tr202-r", "required_actions": ["Click Settings at the top right, then See all settings (critical)", "Click the Labels tab at the top (critical)", "Click Show next to the label (critical)"], "covered": [True, True, True], "needs_clarification": False,
  "gates": gs(source="fail"), "unsupported_claims": ["'**Settings**, the gear icon' -> the page gives the icon alt text 'Settings' only and does not describe a gear."],
  "scores": sc(), "decision": "revise", "reasons": "Unsupported icon description.",
  "fix": "Change step 1 to: 'At the top right, click **Settings**, then **See all settings**.' (drop 'the gear icon')."},
]

# ---- Page 5: Gmail vacation responder (tr203) ----
_NC = {k: v for k, v in _K.items() if k != "needs_clarification"}
REVIEWS += [
 {"id": "tr203-a", "required_actions": ["Settings at top right, See all settings (critical)", "General tab, scroll to Vacation responder (critical)", "Select Vacation responder on (critical)", "Enter date range, subject, message (critical)", "Click Save Changes at the bottom (critical)"], "covered": [True]*5, "needs_clarification": False, **_NC},
 {"id": "tr203-c", "required_actions": ["Settings, See all settings (critical)", "General tab, Vacation responder (critical)", "Vacation responder on (critical)", "Date range, subject, message (critical)", "Save Changes (critical)"], "covered": [True]*5, "needs_clarification": False, **_NC},
 {"id": "tr203-b", "required_actions": [], "covered": [], **{**_K, "needs_clarification": True, "scores": sc(steps="NA")}},
 {"id": "tr203-d", "required_actions": ["Settings, See all settings (critical)", "General tab, Vacation responder (critical)", "Vacation responder on (critical)", "Date range, subject, message (critical)", "Save Changes (critical)"], "covered": [True]*5, "needs_clarification": False, **_NC},
 {"id": "tr203-e", "required_actions": ["Settings, See all settings, General, Vacation responder on (critical)", "Enter date range, subject, message (critical)", "Check the box under the message to send replies only to contacts (critical)", "Save Changes (critical)"], "covered": [True]*4, "needs_clarification": False, **_NC},
 {"id": "tr203-r", "required_actions": ["Open inbox; banner across the top (critical)", "Click End now (critical)"], "covered": [True, True], "needs_clarification": False, **_NC},
]
