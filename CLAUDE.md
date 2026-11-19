# Genesis IG reels – operating rules (read before any work)

Owner and approver: Johnny Paul (Genesis Management Solutions). Account: @genesis.managementsolutions.
Claude manages production and, with approval, publishing. ChatGPT is the auditor only (21:00 IST daily audit, at most 3 proposals).

## Hard rules
1. **Approval gate.** Nothing is published, scheduled, replied to, commented or DMed unless Johnny has approved that exact item in chat (file, caption, account, settings, AI-label choice). A scheduled run prepares drafts and stops; it never publishes.
2. **No engagement on other accounts** (likes, comments, follows, DMs). Johnny does that manually. Replies only on our own posts, only after approval.
3. **Education only on both accounts.** Keep reels, captions and replies educational. Do not invite applications, recruitment enquiries or contact. For job or visa questions on our posts, say the page shares learning content only and does not take applications. Do not direct the commenter to WhatsApp, DMs, the bio or another link. Never state or imply an opening, employer, salary, deductions, visa outcome, deadline or selection guarantee. No client names, proprietary drawings or candidate details. Never ask for personal details in comments; never invent a contact number.
4. **Accuracy.** Verify every teaching point against manufacturer or official documentation before production. Label controller-specific code ("Haas mill example"). No universal tolerances. Turning: workpiece rotates, tool feeds. Milling: cutter rotates, relative feed between cutter and workpiece. Don't say the tool or job "never moves". When a drawing exaggerates scale (expansion, runout, deflection), label it on screen, e.g. 'EXAGGERATED FOR VISIBILITY'.
5. **Provenance.** Keep content credentials and AI disclosures. Don't strip metadata, don't re-encode an approved file, don't use detection-evasion tools.
6. **Public repo.** Store only the toolkit, reel specs, captions, PLAN.md and approved MP4s (an MP4 goes into `reels/` only after approval). Analytics, enquiry counts, approvals and internal notes stay in the private claude.ai Project (claude/publication-log.md). Where Project files are unavailable, use the private Drive log below, never this repo; existing Project records are preserved.

## Private records
Fingerprints, vidIQ upload/post IDs and approved revisions, Johnny's approvals, live-post evidence and 72-hour metrics go in the private Google Drive file "Genesis IG private log.md" (folder "Genesis IG private records", pj@ account, reached through Composio Google Drive). Read it before reconciling; append after every draft, approval, schedule and publication; never rewrite earlier entries or copy its contents into this repo. A fingerprint calculated later does not prove an earlier match: record such comparisons as unverified.
Compare reels only at comparable ages, using metrics captured once each reel is at least 72 hours old. Skip rate is Meta's share of initial views skipped in the first 3 seconds; read it with average watch time, saves and shares.

## Session and repository access
- Start every producer or publisher session, scheduled or manual, with `pauljohnny-jny/genesis-ig-reels` selected as the session's repository. It is the canonical repository.
- First check access with a read: `git remote get-url origin` names `pauljohnny-jny/genesis-ig-reels` and `git fetch origin main` succeeds.
- **A stale repository scope is a session fault, not a video fault.** If git or GitHub refuses access with a 403 or "not in this session's authorized repository set", stop. Don't re-render, re-encode, rename or re-upload the reel, don't change its files or PLAN.md status, and don't try other tokens, credentials or upload routes. Report the exact error to Johnny and ask for a fresh session with `pauljohnny-jny/genesis-ig-reels` selected.
- Push to `main` only if the session allows it. If pushes are limited to a session branch, push there, open a draft PR and report. Never force-push.

## Media source paths
- **Normal path, every reel except the batch below:** after approval the MP4 goes in `reels/` and the caption in `captions/` (see Publish). An immutable commit-pinned raw URL to those paths (`…/genesis-ig-reels/<commit-sha>/reels/<file>.mp4`) is also valid.
- **Exception, 15 Nov recovery batch, Reels 19–38 only:** publish from the hash-verified `files/` copies pinned to commit `e146b933aba38c315f4fcdae73e656492cbf05d3`, i.e. `https://raw.githubusercontent.com/pauljohnny-jny/genesis-ig-reels/e146b933aba38c315f4fcdae73e656492cbf05d3/files/reels/<file>.mp4` and `…/files/captions/<file>.txt`. Check the bytes against `files/reels/SHA256SUMS_batch_19-38_approved.txt` (v2) before each slot. Root-level `reels/` and `captions/` are not the source for this batch. `files/` is used only for this batch.

## Daily run (scheduled, 07:07 IST)
**Reconcile first.** Before the backlog check, reconcile PLAN.md with the owner account's (@genesis.managementsolutions) current published media and, when available, the private publication log (claude/publication-log.md). A reel is live only when its media ID, permalink and publication time are all confirmed and the post matches the approved caption; never infer live from an elapsed schedule, a wake-up or an intended status. Reconciliation is read-only on Instagram. Updating confirmed rows to live in PLAN.md is an authorized status correction and needs no extra approval, because it only records verified evidence. **Backlog** means approved reels that are overdue (their slot has passed) with no confirmed publication, plus failed or blocked releases. An approved reel whose vidIQ schedule is confirmed (native status `scheduled` with an exact `scheduledFor` time still in the future, checked with `vidiq_social_post_status`/`vidiq_social_post_list`) is pending, not missed, and does not block preparing the following day. If any backlog remains after checking owner media and vidIQ status, HOLD new production and report it. A stale PLAN.md stops blocking production only when that evidence actually clears the backlog. This step does not relax the exact-item approval gate or any provenance, education or privacy rule.
Prepare the **next day's** two reels: take the next two topics from the PLAN.md Queue (topics there have no IDs) and give them the next unused sequential IDs above the highest ID already in PLAN.md (38 as of 14 Nov), never reusing or renumbering existing IDs or the 15 Nov recovery slots → verify sources → spec in `toolkit/specs/` → render → QC → caption. Commit specs, captions and PLAN.md (status `draft`), never the MP4. If two or more drafts are already awaiting approval, don't make more – re-send those. Then list new comments on our own reels and draft replies (don't post). For regular reels, prepare each as a private vidIQ draft (see Publish, scheduled route) before messaging. Send Johnny one message: files, captions with English meaning, proposed times (09:00 and 19:30 IST next day), reply drafts, and for each vidIQ draft its account, publishAt in IST, regular Reel with no manual AI label, postId and revision. After he explicitly approves that exact draft revision, schedule it as in Publish; no session wake-ups or cron jobs are needed.

## Reel format
Silent vertical motion graphics, 1080×1920, 20–35 s, Tamil text with English shop-floor terms. Five scenes: hook → explanation → worked example/check → interview takeaway → one CTA (save, or send to a friend).
**Hook standard (Johnny approved 2 Nov 2026; reels 17+).** Scene 1 is a 3–4.5 s hook scene built with `hook=` in the spec (see `toolkit/specs/hook_examples.py`): no tag/title card; one giant line of at most ~6 words visible at 0.0 s, a Tamil follow-up by ~0.35 s, and motion in the panel from frame 1. Rotate four formats and note which one each reel uses in PLAN.md: (1) cold-open demo – watch the mistake happen; (2) countdown quiz – 3-2-1 with options, answered later; (3) wrong vs right – the wrong value first; (4) verbatim interview question. Write three hook options per reel and pick one that has a specific code or number, shows motion or the mistake at frame 1, is answered before the halfway mark (echo it in the last scene), and is true and sourced: no clickbait, no job, salary, visa or selection hooks. Caption line 1 opens with the same hook, then the topic. All reels stay silent. Do not add AI voice or any other audio track. Text stays within y 230–1440 and x ≤ 850.

## Caption format
Topic in line 1; one useful added detail; assumptions stated (e.g. metric G94, single-start thread); "VMC operator" in the text; one CTA; at most 3 specific hashtags. Write formulas in the caption exactly as the reel shows them, with units (e.g. 'aligned thimble division × 0.01 mm').

## Produce
```
cd toolkit && npm ci            # fonts (Playwright Chromium and ffmpeg are preinstalled)
python3 render.py specs/batchE.py 14 --stills-only   # build + safe-zone check + qc/<id>_sheet.png
python3 render.py specs/batchE.py 14                 # full MP4 to out/
./qcmp4.sh out/<file>.mp4 14                         # spec line + 1-fps contact sheet qc/14_mp4.png
```
`check()` must report 0 issues, and look at both QC sheets before calling a reel done. New reels: add a spec file in `toolkit/specs/` using `gen.py` helpers.

## Publish (after approval only)
1. Commit the final MP4 to `reels/` and the caption to `captions/`; push to `main`. (Reels 19–38: nothing to commit; use the pinned `files/` URLs under Media source paths.)
2. Raw URL: `https://raw.githubusercontent.com/pauljohnny-jny/genesis-ig-reels/main/reels/<file>.mp4`
3. vidIQ: `vidiq_video_upload` from that URL → `vidiq_instagram_publish_reel` with the approved caption and settings.
4. Confirm the permalink, then record it in the Project's publication log.

### Scheduled route for new regular reels (no Trial, no AI label)
For future regular Reels whose approved setting is no manual AI label. It does not apply to the 15 Nov recovery batch (Reels 19–38). Trial Reels and AI-labelled Reels can't use this route; they stay blocked until Johnny approves a supported route for them.
0. **No private upload available?** If the session's vidIQ upload tool takes only a public URL or a device picker, don't host the unapproved MP4 anywhere public. Send the MP4, caption and slot for approval first; after approval commit the MP4 unchanged to `reels/`, import it from the commit-pinned raw URL, check the hosted SHA-256, create the draft, and schedule only after Johnny approves that draft revision.
1. **Private draft, before Johnny sees the final version.** Render and QC as usual, then record `sha256sum` of `toolkit/out/<file>.mp4`. Upload that exact file privately with `vidiq_video_upload` `localFile` (path, sizeBytes, `video/mp4`). Run the transfer command it returns, then call it again with the `uploadId`. Download the hosted `videoUrl` and check that its SHA-256 matches. Nothing goes to GitHub or any public URL yet.
2. Create the draft with `vidiq_social_post_draft_create`: media = that uploadId, destination `INSTAGRAM` / `29321374914219700` (@genesis.managementsolutions), text = the caption, and `publishAt` set to the slot time (ISO 8601 with `+05:30`). Read it back with `vidiq_social_post_draft_get`.
3. **Show Johnny the exact final draft:** the video file (`SendUserFile`), caption, account, publishAt in IST, regular Reel with no manual AI label, postId and revision. Tell him that **once scheduled, a vidIQ post can't be changed or cancelled**. Any change means a new revision that needs approval again.
4. **Only after he explicitly approves that exact revision:** commit the unchanged MP4 to `reels/` and the caption to `captions/`, and push. Check that the bytes on GitHub and the vidIQ-hosted bytes both match the recorded SHA-256. Then call `vidiq_social_post_publish(postId, revision)`. If any check fails, stop and report.
5. **Record status.** `vidiq_social_post_status` or `vidiq_social_post_list` showing `scheduled` means scheduled, not live. A reel is live only after the next run's reconciliation confirms its media ID, permalink and publication time on the owner account.
