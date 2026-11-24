# Reel plan and status

Statuses: `live` · `approved` (publish time set) · `draft` (spec + caption committed, awaiting Johnny) · `queued`.
Number = reel ID used in file names. Update this file in the same commit as any status change.

## Published / approved
| ID | Topic | Status |
|---|---|---|
| 01 | Milling versus turning | live |
| 02 | Reading a drawing | live |
| 03 | Explain your setup | live |
| 04 | Types of offsets | live |
| 05 | G43 H-offset check | live |
| 06 | Spindle RPM formula | live |
| 07 | Feed rate formula | live |
| 08 | Climb vs conventional milling | live |
| 09 | G41 vs G42 | live |
| 10 | G81 / G83 / G73 drilling cycles | live |
| 11 | Rigid tapping feed | live |
| 12 | Caliper: resolution vs accuracy | live |
| 13 | G02/G03 I, J arc centre (Haas mill example) | live – 2 Nov 2026 |
| 14 | Toolholder runout (TIR) | live – 2 Nov 2026 |
| 15 | Reading a metric micrometer | live – 3 Nov 2026 |
| 16 | Thermal drift: morning vs afternoon part | live – 3 Nov 2026 |
| 17 | G90 vs G91 (Haas mill example) | live – 5 Nov 2026 13:05:05 IST · [permalink](https://www.instagram.com/reel/DfWgcDRAgn_/) · hook: cold-open demo · spec batchG.py |
| 18 | 0.01 mm = ? µm | live – 5 Nov 2026 19:31:43 IST · [permalink](https://www.instagram.com/reel/DfXMrK8DrTi/) · hook: countdown quiz · spec batchG.py |

## Batch 6–15 Nov recovery (all times IST)

Content approved in the 5 Nov audit; Johnny directly confirmed the recovery schedule on 14 Nov. The originals uploaded on 15 Nov are preserved under `files/` at commit `e146b933aba38c315f4fcdae73e656492cbf05d3`.

Recovery source base: `https://raw.githubusercontent.com/pauljohnny-jny/genesis-ig-reels/e146b933aba38c315f4fcdae73e656492cbf05d3/files/`. Use `reels/<file>.mp4` and `captions/<file>.txt` relative to this base. Verify exact bytes against `files/reels/SHA256SUMS_batch_19-38_approved.txt` (v2). Root-level media paths are not the source for this recovery batch. Hosting and all 46 package checksums verified on 15 Nov. All 20 confirmed live on @genesis.managementsolutions on 15 Nov (owner media ID, permalink, time and approved caption reconciled 16 Nov).
| ID | Topic | Status | Length | Hook | CTA | Spec |
|---|---|---|---|---|---|---|
| 22 | What Ra 1.6 means | live – 15 Nov 2026 06:01:57 IST · [permalink](https://www.instagram.com/reel/Dfvf9hwDSzq/) (recovery batch, approved caption matched) | 20 s | countdown quiz | SAVE | batchH.py |
| 19 | Reading a metric vernier caliper (0.02 mm) | live – 15 Nov 2026 06:20:14 IST · [permalink](https://www.instagram.com/reel/DfviAvVoBdu/) (recovery batch, approved caption matched) | 30 s | wrong vs right | SAVE | batchH.py |
| 29 | H7 in plain words (ISO 286) | live – 15 Nov 2026 06:38:20 IST · [permalink](https://www.instagram.com/reel/DfvkECJjZRO/) (recovery batch, approved caption matched) | 30 s | interview question | SAVE | batchJ.py |
| 20 | Reading a dial indicator (counter + pointer) | live – 15 Nov 2026 06:55:37 IST · [permalink](https://www.instagram.com/reel/DfvmEZFCvqz/) (recovery batch, approved caption matched) | 20 s | cold-open demo | SAVE | batchH.py |
| 28 | Inch ↔ mm (25.4 exactly; Haas G20/G21) | live – 15 Nov 2026 07:13:32 IST · [permalink](https://www.instagram.com/reel/DfvoHXvkSSD/) (recovery batch, approved caption matched) | 21 s | countdown quiz | SAVE | batchI.py |
| 24 | Tool wear: flank vs crater vs BUE | live – 15 Nov 2026 07:31:23 IST · [permalink](https://www.instagram.com/reel/DfvqKPdiLdz/) (recovery batch, approved caption matched) | 30 s | interview question | SAVE | batchI.py |
| 21 | GO / NO-GO plug gauge | live – 15 Nov 2026 07:50:29 IST · [permalink](https://www.instagram.com/reel/DfvsW9jFEFJ/) (recovery batch, approved caption matched) | 30 s | interview question | SEND | batchH.py |
| 30 | What M10 × 1.5 means | live – 15 Nov 2026 08:07:40 IST · [permalink](https://www.instagram.com/reel/DfvuVJYHIXD/) (recovery batch, approved caption matched) | 20 s | countdown quiz | SAVE | batchJ.py |
| 25 | Chatter and tool stick-out | live – 15 Nov 2026 08:25:51 IST · [permalink](https://www.instagram.com/reel/DfvwYeAjW9-/) (recovery batch, approved caption matched) | 20 s | cold-open demo | SEND | batchI.py |
| 23 | Height gauge: zero on the plate | live – 15 Nov 2026 08:43:34 IST · [permalink](https://www.instagram.com/reel/Dfvyaa0Epz1/) (recovery batch, approved caption matched) | 30 s | cold-open demo | SAVE | batchH.py |
| 31 | Tap drill size for a cut tap (D − P) | live – 15 Nov 2026 09:02:13 IST · [permalink](https://www.instagram.com/reel/Dfv0i2cDP9J/) (recovery batch, approved caption matched) | 30 s | wrong vs right | SEND | batchJ.py |
| 33 | Edge finder vs probe | live – 15 Nov 2026 09:20:44 IST · [permalink](https://www.instagram.com/reel/Dfv2thnAJvS/) (recovery batch, approved caption matched) | 20 s | interview question | SAVE | batchJ.py |
| 34 | Feed / rapid override check (Haas mill example) | live – 15 Nov 2026 09:37:37 IST · [permalink](https://www.instagram.com/reel/Dfv4lmrD0P5/) (recovery batch, approved caption matched) | 20 s | cold-open demo | SEND | batchK.py |
| 26 | Roughing vs finishing | live – 15 Nov 2026 09:56:01 IST · [permalink](https://www.instagram.com/reel/Dfv6sgKHALG/) (recovery batch, approved caption matched) | 30 s | wrong vs right | SAVE | batchI.py |
| 35 | G17 / G18 / G19 planes (Haas mill example) | live – 15 Nov 2026 10:14:06 IST · [permalink](https://www.instagram.com/reel/Dfv8wzQGQWS/) (recovery batch, approved caption matched) | 30 s | countdown quiz | SAVE | batchK.py |
| 27 | Coolant and chip evacuation | live – 15 Nov 2026 10:32:00 IST · [permalink](https://www.instagram.com/reel/Dfv-0CilLRU/) (recovery batch, approved caption matched) | 20 s | cold-open demo | SAVE | batchI.py |
| 38 | 5S on the shop floor | live – 15 Nov 2026 10:49:56 IST · [permalink](https://www.instagram.com/reel/DfwA7b0k885/) (recovery batch, approved caption matched) | 20 s | countdown quiz | SAVE | batchK.py |
| 32 | Tramming a vise with a dial indicator | live – 15 Nov 2026 11:08:18 IST · [permalink](https://www.instagram.com/reel/DfwC-lSk0sH/) (recovery batch, approved caption matched) | 30 s | cold-open demo | SAVE | batchJ.py |
| 36 | Haas safe-start line | live – 15 Nov 2026 11:25:57 IST · [permalink](https://www.instagram.com/reel/DfwE_PeiZx7/) (recovery batch, approved caption matched) | 30 s | wrong vs right | SAVE | batchK.py |
| 37 | "Tell me about your machine" | live – 15 Nov 2026 19:32:41 IST · [permalink](https://www.instagram.com/reel/Dfw8rxoCMdS/) (recovery batch, approved caption matched) | 30 s | interview question | SEND | batchK.py |

## Approved: live or scheduled (vidIQ native schedule is pending, not live, until reconciled)
| ID | Topic | Status | Length | Hook | CTA | Spec |
|---|---|---|---|---|---|---|
| 39 | Proving out a new program (Haas mill example) | live – 19 Nov 2026 09:00:27 IST · [permalink](https://www.instagram.com/reel/Df6Hk2BitOI/) (approved caption matched) | 28.6 s | cold-open demo | SAVE | batchL.py |
| 40 | Running an outdated program: drawing rev vs program rev | live – 19 Nov 2026 19:30:34 IST · [permalink](https://www.instagram.com/reel/Df7Pr_SEgQJ/) (approved caption matched) | 28.2 s | countdown quiz | SEND | batchL.py |
| 41 | Clearance hole for an M8 bolt (ISO 273: 8.4 / 9 / 10 mm) | live – 20 Nov 2026 09:00:33 IST · [permalink](https://www.instagram.com/reel/Df8sX3Ygs02/) (approved caption matched) · MP4 in reels/ | 28.2 s | wrong vs right | SAVE | batchM.py |
| 42 | Dial test indicator cosine error (30° → × 0.87, Mitutoyo DTI manual) | live – 20 Nov 2026 19:31:31 IST · [permalink](https://www.instagram.com/reel/Df90kT9CbkV/) (approved caption matched) · MP4 in reels/ | 28.2 s | cold-open demo | SAVE | batchM.py |
| 43 | Reaming stock allowance: Ø10 reamer → Ø9.8 drill (Sandvik P1 table, 0.2 mm) | live – 22 Nov 2026 09:00:28 IST · [permalink](https://www.instagram.com/reel/DgB19d1DNvd/) (approved caption matched) · MP4 in reels/ | 28.2 s | wrong vs right | SAVE | batchN.py |
| 44 | Caliper: measure close to the beam (Abbe's principle, Mitutoyo 0.008 mm example) | live – 22 Nov 2026 19:31:48 IST · [permalink](https://www.instagram.com/reel/DgC-N0qlc0y/) (approved caption matched) · MP4 in reels/ | 28.2 s | cold-open demo | SAVE | batchN.py |
| 46 | Blind-hole tapping: drill ≥ thread + chamfer + 1 pitch (Kennametal Tech Tip #65; M8 × 1.25 → 17 mm) | live – 23 Nov 2026 19:31:33 IST · [permalink](https://www.instagram.com/reel/DgFi-exmfsb/) (approved caption matched) · MP4 in reels/ | 28.2 s | cold-open demo | SEND | batchO.py |

Open item: the approved MP4s for 39–40 are not yet in `reels/` (scheduled from the vidIQ-hosted copies). Add them unchanged when the bytes are available.

## Drafts awaiting approval (proposed slots IST)
| ID | Topic | Status | Length | Hook | CTA | Spec |
|---|---|---|---|---|---|---|
| 45 | Thread plug gauge GO / NOT GO: GO full length, NOT GO ≤ 2 turns at each accessible end, short-thread rule, minor Ø checked separately (ISO 1502:1996) | draft rev 3 (23 Nov audit corrections) – proposed 25 Nov 2026 09:00 IST · private vidIQ draft | 28.2 s | interview question | SAVE | batchO.py |
| 47 | ISO material groups P M K N S H and colour codes (ISO 513:2012; K = cast iron, red; K10 vs K30 within the K01–K40 range) | draft rev 2 (23 Nov audit corrections) – proposed 25 Nov 2026 19:30 IST · private vidIQ draft | 28.2 s | countdown quiz | SAVE | batchP.py |

## Queue – from 26 Nov 2026 (two a day, 09:00 and 19:30 IST)
Take topics in this order; IDs are assigned when produced (next is 48). Slot dates below are targets and now run about a day later than written (45 rev 3 and 47 rev 2 re-slotted to 25 Nov after the 23 Nov audit; 24 Nov slots unused). Each line: target slot · topic and angle · hook · CTA · source to verify against. The producer verifies every teaching point at production (Hard rule 4); if a point can't be verified, simplify it or take the next topic and say why. Order avoids two of the same hook or subject back to back.
- 24 Nov 09:00 · Bore gauge: zero on the setting ring and read at the turning point while rocking (smallest diameter) · cold-open demo · SAVE · Mitutoyo bore gauge instructions (Mitutoyo calls it the highest displayed value – word it carefully)
- 24 Nov 19:30 · G28 Z0 vs G91 G28 Z0: the intermediate point (label by control) · wrong vs right · SEND · Haas G28 code reference
- 25 Nov 09:00 · Spot drill angle equal to or slightly larger than the drill point angle (e.g. 118° drill → 120° spot) · countdown quiz · SAVE · ISCAR drilling handbook / drill maker
- 25 Nov 19:30 · ER collet: insert the shank at least 2/3 of the collet length · cold-open demo · SEND · REGO-FIX ER collet guidance
- 26 Nov 09:00 · Edge symbol (ISO 13715): + allows burr/passing, − requires undercut, with a size · wrong vs right · SAVE · ISO 13715
- 26 Nov 19:30 · Vise setup: seat the part on parallels and check they no longer move · cold-open demo · SEND · vise maker's instructions (e.g. Kurt) / Haas
- 27 Nov 09:00 · Reading a position tolerance frame: ⌖ Ø0.1 | A | B | C · countdown quiz · SAVE · ISO 1101
- 27 Nov 19:30 · Thread milling vs tapping: when each fits · interview question · SAVE · Sandvik Coromant threading guidance
- 28 Nov 09:00 · 25–50 mm micrometer: zero check reads 25.000 on the setting standard, not 0.000 · wrong vs right · SAVE · Mitutoyo micrometer instructions
- 28 Nov 19:30 · Recap quiz: tap drill size (D − P), dial indicator reading, vernier reading · countdown quiz · SAVE · sources of Reels 31, 20 and 19

Later: setting Z with a gauge block – subtract the block height (Haas mill example) · wrong vs right · SAVE · Haas mill operator's manual + Setting 64 (deferred 22 Nov: Haas manual pages could not be read from the producer session, so the Haas-specific offset steps were not verified; produce when they can be). Probing a work offset in detail (cycle updates or only reports, by system – Renishaw / Haas probing docs); builder-specific M-codes (beyond common M-codes, check the manual).
