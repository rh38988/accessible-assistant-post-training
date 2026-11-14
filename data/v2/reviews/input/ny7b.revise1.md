# Revision list: batch ny7b, after review round 1 (5 examples)

Edit ONLY these examples in data/v2/specs/ny7b.py, then rebuild.

## tr206-a
- reasons: Unsupported icon description; the fallback omits that the host or co-host must approve the request.
- fix requested: Delete the sentence 'It is the closed-captions icon.' In the last paragraph, after '...then click Send.', add: 'The host or a co-host has to approve your request before captions appear.'
- unsupported claims: 'It is the closed-captions icon.' -> the page names the icon only as 'Show captions' and gives no description of its look
- required actions missing from the reply: Host or co-host must approve the request
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762

## tr206-c
- reasons: Caption placement is not supported for mobile; the fallback omits host approval.
- fix requested: Replace 'The words people say will appear above the meeting buttons.' with 'The words people say will appear on your screen.' Add after the fallback steps: 'The host or a co-host has to approve your request.' Keep the Android-specific wording as is.
- unsupported claims: 'The words people say will appear above the meeting buttons.' -> the page gives this placement only for the desktop app, not mobile
- required actions missing from the reply: Host or co-host approves
- low scores: {'steps': 1} | gates not passed: {'source': 'fail'}
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762

## tr206-d
- reasons: Caption placement unsupported for mobile. The reply also omits that the Request CC icon may be in the toolbar, which is fine; the only problem is the placement claim.
- fix requested: In the final reply replace 'The words people say will appear above the meeting buttons.' with 'The words people say will appear on your screen.' Leave the rest unchanged.
- unsupported claims: 'The words people say will appear above the meeting buttons.' -> the page gives this placement only for the desktop app, not mobile
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762

## tr206-e
- reasons: The closing fallback gives an incomplete request path: it stops at 'Request captions' without the Send step or host approval, so the user cannot finish it. Also 'toward the large end' is an unsourced direction for the slider.
- fix requested: Change the last paragraph to: 'If nothing happens when you click **Show captions**, the host may have restricted them. Click **More**, then **Request captions**, then **Send**. The host or a co-host has to approve your request.' Change step 4 to 'Drag the **Font size** slider to make the letters bigger.' (or keep as is if the writer prefers; only the fallback is required).
- required actions missing from the reply: Fallback if restricted: Request captions, Send, host approval
- low scores: {'actionable': 1} | gates not passed: {}
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762

## tr206-r
- reasons: Final reply implies that requesting works even if the host turned captions off. Page: captions missing entirely means the host may have disabled them.
- fix requested: Rewrite the lead-in of the final reply to: 'The host may have limited captions. You can ask for them.' Add at the end after the approval sentence: 'If you do not see **Request captions** under **More**, the host may have turned captions off, so ask the host to turn them on.' (Page troubleshooting: 'Captions are missing entirely: the host may have disabled them.')
- unsupported claims: 'The host may have turned captions off or limited them. You can ask for them.' -> the page says Request captions applies when the host restricts captions but does not disable them; if captions are disabled, a request is not available
- low scores: {} | gates not passed: {'source': 'fail'}
- sources: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059762
