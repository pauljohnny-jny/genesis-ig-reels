# Genesis IG reels – operating rules (read before any work)

Owner and approver: Johnny Paul (Genesis Management Solutions). Account: @genesis.managementsolutions.
Claude manages production and, with approval, publishing. ChatGPT is the auditor only (21:00 IST daily audit, at most 3 proposals).

## Hard rules
1. **Approval gate.** Nothing is published, scheduled, replied to, commented or DMed unless Johnny has approved that exact item in chat (file, caption, account, settings, AI-label choice). A scheduled run prepares drafts and stops; it never publishes.
2. **No engagement on other accounts** (likes, comments, follows, DMs). Johnny does that manually. Replies only on our own posts, only after approval.
3. **Education only on both accounts.** Keep reels, captions and replies educational. Do not invite applications, recruitment enquiries or contact. For job or visa questions on our posts, say the page shares learning content only and does not take applications. Do not direct the commenter to WhatsApp, DMs, the bio or another link. Never state or imply an opening, employer, salary, deductions, visa outcome, deadline or selection guarantee. No client names, proprietary drawings or candidate details. Never ask for personal details in comments; never invent a contact number.
4. **Accuracy.** Verify every teaching point against manufacturer or official documentation before production. Label controller-specific code ("Haas mill example"). No universal tolerances. Turning: workpiece rotates, tool feeds. Milling: cutter rotates, relative feed between cutter and workpiece. Don't say the tool or job "never moves".
5. **Provenance.** Keep content credentials and AI disclosures. Don't strip metadata, don't re-encode an approved file, don't use detection-evasion tools.
6. **Public repo.** Store only the toolkit, reel specs, captions, PLAN.md and approved MP4s (an MP4 goes into `reels/` only after approval). Analytics, enquiry counts, approvals and internal notes stay in the private claude.ai Project (claude/publication-log.md).

## Daily run (scheduled, 07:07 IST)
Prepare the **next day's** two reels: next two `queued` IDs in PLAN.md → verify sources → spec in `toolkit/specs/` → render → QC → caption. Commit specs, captions and PLAN.md (status `draft`), never the MP4. If two or more drafts are already awaiting approval, don't make more – re-send those. Then list new comments on our own reels and draft replies (don't post). Send Johnny one message: files, captions with English meaning, proposed times (09:00 and 19:30 IST next day), reply drafts. After he approves in that session, set wake-ups for the approved times and publish then.

## Reel format
Silent vertical motion graphics, 1080×1920, 20–35 s, Tamil text with English shop-floor terms. Five scenes: hook → explanation → worked example/check → interview takeaway → one CTA (save, or send to a friend).
**Hook standard (Johnny approved 2 Nov 2026; reels 17+).** Scene 1 is a 3–4.5 s hook scene built with `hook=` in the spec (see `toolkit/specs/hook_examples.py`): no tag/title card; one giant line of at most ~6 words visible at 0.0 s, a Tamil follow-up by ~0.35 s, and motion in the panel from frame 1. Rotate four formats and note which one each reel uses in PLAN.md: (1) cold-open demo – watch the mistake happen; (2) countdown quiz – 3-2-1 with options, answered later; (3) wrong vs right – the wrong value first; (4) verbatim interview question. Write three hook options per reel and pick one that has a specific code or number, shows motion or the mistake at frame 1, is answered before the halfway mark (echo it in the last scene), and is true and sourced: no clickbait, no job, salary, visa or selection hooks. Caption line 1 opens with the same hook, then the topic. All reels stay silent. Do not add AI voice or any other audio track. Text stays within y 230–1440 and x ≤ 850.

## Caption format
Topic in line 1; one useful added detail; assumptions stated (e.g. metric G94, single-start thread); "VMC operator" in the text; one CTA; at most 3 specific hashtags.

## Produce
```
cd toolkit && npm ci            # fonts (Playwright Chromium and ffmpeg are preinstalled)
python3 render.py specs/batchE.py 14 --stills-only   # build + safe-zone check + qc/<id>_sheet.png
python3 render.py specs/batchE.py 14                 # full MP4 to out/
./qcmp4.sh out/<file>.mp4 14                         # spec line + 1-fps contact sheet qc/14_mp4.png
```
`check()` must report 0 issues, and look at both QC sheets before calling a reel done. New reels: add a spec file in `toolkit/specs/` using `gen.py` helpers.

## Publish (after approval only)
1. Commit the final MP4 to `reels/` and the caption to `captions/`; push to `main`.
2. Raw URL: `https://raw.githubusercontent.com/pauljohnny07/genesis-ig-reels/main/reels/<file>.mp4`
3. vidIQ: `vidiq_video_upload` from that URL → `vidiq_instagram_publish_reel` with the approved caption and settings.
4. Confirm the permalink, then record it in the Project's publication log.
