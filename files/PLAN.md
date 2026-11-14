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

## Batch 6–15 Nov (one slot each, IST; approved by Johnny 5 Nov; each publishes only if its hosted MP4 and caption match reels/SHA256SUMS_batch_19-38_approved.txt)
| ID | Topic | Status | Length | Hook | CTA | Spec |
|---|---|---|---|---|---|---|
| 22 | What Ra 1.6 means | approved (ChatGPT audit + Johnny directly, 5 Nov; caption v2); original slot 6 Nov 09:00 IST missed (files not hosted) → recovery slot 15 Nov 06:00 IST | 20 s | countdown quiz | SAVE | batchH.py |
| 19 | Reading a metric vernier caliper (0.02 mm) | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 6 Nov 19:30 IST missed (files not hosted) → recovery slot 15 Nov 06:18 IST | 30 s | wrong vs right | SAVE | batchH.py |
| 29 | H7 in plain words (ISO 286) | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 7 Nov 09:00 IST missed (files not hosted) → recovery slot 15 Nov 06:36 IST | 30 s | interview question | SAVE | batchJ.py |
| 20 | Reading a dial indicator (counter + pointer) | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 7 Nov 19:30 IST missed (files not hosted) → recovery slot 15 Nov 06:54 IST | 20 s | cold-open demo | SAVE | batchH.py |
| 28 | Inch ↔ mm (25.4 exactly; Haas G20/G21) | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 8 Nov 09:00 IST missed (files not hosted) → recovery slot 15 Nov 07:12 IST | 21 s | countdown quiz | SAVE | batchI.py |
| 24 | Tool wear: flank vs crater vs BUE | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 8 Nov 19:30 IST missed (files not hosted) → recovery slot 15 Nov 07:30 IST | 30 s | interview question | SAVE | batchI.py |
| 21 | GO / NO-GO plug gauge | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 9 Nov 09:00 IST missed (files not hosted) → recovery slot 15 Nov 07:48 IST | 30 s | interview question | SEND | batchH.py |
| 30 | What M10 × 1.5 means | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 9 Nov 19:30 IST missed (files not hosted) → recovery slot 15 Nov 08:06 IST | 20 s | countdown quiz | SAVE | batchJ.py |
| 25 | Chatter and tool stick-out | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 10 Nov 09:00 IST missed (files not hosted) → recovery slot 15 Nov 08:24 IST | 20 s | cold-open demo | SEND | batchI.py |
| 23 | Height gauge: zero on the plate | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 10 Nov 19:30 IST missed (files not hosted) → recovery slot 15 Nov 08:42 IST | 30 s | cold-open demo | SAVE | batchH.py |
| 31 | Tap drill size for a cut tap (D − P) | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 11 Nov 09:00 IST missed (files not hosted) → recovery slot 15 Nov 09:00 IST | 30 s | wrong vs right | SEND | batchJ.py |
| 33 | Edge finder vs probe | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 11 Nov 19:30 IST missed (files not hosted) → recovery slot 15 Nov 09:18 IST | 20 s | interview question | SAVE | batchJ.py |
| 34 | Feed / rapid override check (Haas mill example) | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 12 Nov 09:00 IST missed (files not hosted) → recovery slot 15 Nov 09:36 IST | 20 s | cold-open demo | SEND | batchK.py |
| 26 | Roughing vs finishing | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 12 Nov 19:30 IST missed (files not hosted) → recovery slot 15 Nov 09:54 IST | 30 s | wrong vs right | SAVE | batchI.py |
| 35 | G17 / G18 / G19 planes (Haas mill example) | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 13 Nov 09:00 IST missed (files not hosted) → recovery slot 15 Nov 10:12 IST | 30 s | countdown quiz | SAVE | batchK.py |
| 27 | Coolant and chip evacuation | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 13 Nov 19:30 IST missed (files not hosted) → recovery slot 15 Nov 10:30 IST | 20 s | cold-open demo | SAVE | batchI.py |
| 38 | 5S on the shop floor | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 14 Nov 09:00 IST missed (files not hosted) → recovery slot 15 Nov 10:48 IST | 20 s | countdown quiz | SAVE | batchK.py |
| 32 | Tramming a vise with a dial indicator | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 14 Nov 19:30 IST missed (files not hosted) → recovery slot 15 Nov 11:06 IST | 30 s | cold-open demo | SAVE | batchJ.py |
| 36 | Haas safe-start line | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 15 Nov 09:00 IST missed (files not hosted) → recovery slot 15 Nov 11:24 IST | 30 s | wrong vs right | SAVE | batchK.py |
| 37 | "Tell me about your machine" | approved (ChatGPT audit + Johnny directly, 5 Nov); original slot 15 Nov 19:30 IST missed (files not hosted) → recovery slot 15 Nov 19:30 IST | 30 s | interview question | SEND | batchK.py |

## Queue (IDs assigned when produced; verify each teaching point with the named source first)
- Proving out a new program (single block, reduced rapid, distance-to-go, first-piece check; aids never guarantee clearance) – Haas operator manual
- Running an outdated program (match program revision to the released drawing revision)
- Probing a work offset in detail (cycle updates or only reports, by system) – Renishaw / Haas probing docs
- Builder-specific M-codes (beyond common M-codes, check the manual)
- Thread milling vs tapping – tool maker guidance

Later: G28 intermediate point (label by control), weekly recap quiz.
