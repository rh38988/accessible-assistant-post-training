# ny6a revise1 report

Batch ny6a, N = 1. Revision list: data/v2/reviews/input/ny6a.revise1.md (built with review_io.py todo; it was missing). Snapshot before revision: data/v2/snapshots/ny6a.before_revise1.jsonl. Spec before edits: copied to /tmp (not kept). Builder: OK.

## Fixed (22)
- tr187-a, tr187-c, tr187-d, tr187-e, tr187-r: "(the three dots)" removed; "More" named by the page's own words ("To the right of the address bar, tap More"). tr187-r final reply now uses the page's folder sentence ("If you recently opened a folder, you'll find the same folder... tap Back at the top left") instead of "Recently opened folders show first." tr187-c adds "Tap a folder" before "Tap the bookmark". tr187-r first turn fixed as well.
- tr188-a, tr188-d, tr188-r: "(the three dots menu)" and "(the plus sign)" removed; labels only (Settings and more, Zoom in). tr188-r final: "(the minus sign)" removed. The first turn of tr188-r shares the tr188-a block and was fixed the same way. The Ctrl plus-sign keyboard tip is kept (the page names the shortcut).
- tr189-d: added the not-listed path after step 5 (Add next to "Not allowed to send pop-ups or use redirects", type the address, click Add again). The page gives this path.
- tr189-r: "in the address bar" removed; "Next to Notifications, choose Block" (page wording).
- tr190-a, tr190-d, tr190-e: added the review of "Set default file types or link types" as a final step (page: "review the list under..."). tr190-e kept short.
- tr191-a, tr191-c, tr191-d, tr191-r: "(the three dots at the top right)" removed; "At the top right of Chrome, click More". tr191-r first turn now names the page's "Download tray" and places recent downloads "to the right of the address bar" (page wording), replacing "small download box at the top right".
- tr192-a, tr192-c, tr192-d, tr192-e, tr192-r: "(the three dots at the top right)" removed; "At the top right, click More". tr192-a and tr192-d: "Show password icon" changed to "On the right of your password, select Show password" (page wording; the reviewer did not flag this, the change follows the page).

## Cannot fix
None.

## Page contradicted the reviewer
- tr190-a, tr190-d, tr190-e: the reviewer said the page gives no "at the top" position for Set default. The Chrome page (support.google.com/chrome/answer/95417, Windows 11 section) says: "At the top, next to 'Make Google Chrome your default browser,' select Set default." The reply keeps "At the top, click Set default next to ..." (checked twice).
- tr187-a/c/d/e/r, tr188, tr191, tr192: the reviewer's point holds. The pages name the controls "More" / "Settings and more" / "Zoom in" and describe no icon as dots, plus, or minus.

## Follow-ups and failure-recovery pairs touched
- tr187-r, tr188-r, tr191-r: first assistant turn edited (same icon wording as the final reply). Their user messages are unchanged.
- tr187-d, tr189-d, tr190-d, tr191-d, tr192-d: only the final assistant reply edited. The shared missing-information opening and question are unchanged.

## Not on the list, not edited (noticed while working)
- tr188-e: final reply still says "(the three dots menu)" in step 1. The Edge page does not describe that icon as dots. Needs a fix in a later round if the batch is re-reviewed.
- tr189-e: builder warning "no numbered steps in the reply" (the reply is a single prose answer, which is the constraint case). Not on the list.
- tr190-r first turn repeats the same Set default steps as tr190-d; it is not on the list, so unchanged (it still omits the file-types review step).
- tr186 (not on the list) untouched.
