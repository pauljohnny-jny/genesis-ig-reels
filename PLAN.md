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
| 14 | Toolholder runout (TIR) | approved – 2 Nov 19:30 IST |
| 15 | Reading a metric micrometer | approved – 3 Nov 09:00 IST |
| 16 | Thermal drift: morning vs afternoon part | approved – 3 Nov 19:30 IST |

## Queue (take from the top; verify each teaching point with the named source first)
| ID | Topic | Lesson (no universal tolerances) | Source to verify | CTA |
|---|---|---|---|---|
| 17 | G90 vs G91 | Absolute vs incremental; a forgotten G91 makes later moves relative (Haas mill example) | Haas / Productivity training manual | SEND |
| 18 | 0.01 mm = ? µm | 0.01 mm = 10 µm; 0.010 is the same value to 3 decimals | SI | SAVE |
| 19 | Reading a metric vernier caliper | Main scale + coinciding vernier line × graduation (model-specific) | Mitutoyo | SAVE |
| 20 | Proving out a new program | Single block, reduced rapid, distance-to-go, first-piece check; aids never guarantee clearance | Haas operator manual | SEND |
| 21 | Reading a Haas startup block | G00 G90 G17 G40 G49 G54 explained; not universal | Productivity training manual | SAVE |
| 22 | Tool wear: flank vs crater vs built-up edge | Recognise the pattern, then the likely cause | Sandvik / Seco wear guides | SAVE |
| 23 | Running an outdated program | Match program revision to the released drawing revision | Tormach operator-error list | SEND |
| 24 | Feed override left at 10% or 150% | Check overrides before cycle start | Tormach operator-error list | SAVE |
| 25 | Chatter and tool stick-out | Shortest practical overhang, rigid holding; other levers | Sandvik troubleshooting | SAVE |
| 26 | Go / no-go plug gauge for an H7 hole | What each end proves | Gauge maker documentation | SAVE |
| 27 | H7/g6 in plain words | Hole-basis fit letters and grades; read limits from an ISO 286 table | ISO 286 table source | SAVE |
| 28 | G17 / G18 / G19 planes | Arc and cutter-comp plane; control-specific | Haas / Productivity manual | SAVE |
| 29 | Tramming a vise with a dial indicator | Sweep the fixed jaw, adjust, re-check | Manufacturer / training source | SAVE |
| 30 | "Tell me about your machine" | Controller, travels, tool count, materials – only what you actually ran | Interview-prep sources | SAVE |
| 31 | Probing a work offset | Cycle measures and updates or only reports, by system; still verify | Renishaw / Haas probing docs | SAVE |
| 32 | Builder-specific M-codes | Beyond common M-codes, check the manual | Machine manuals | SAVE |
| 33 | What Ra 1.6 means | Ra in µm; cut-off and evaluation length per drawing standard | Mitutoyo SJ docs | SAVE |
| 34 | Thread milling vs tapping | When each is chosen; machine and tool limits | Tool maker guidance | SAVE |
| 35 | 5S on the shop floor | Five steps with one shop example each | Recognised 5S reference | SAVE |

Later: G28 intermediate point (label by control), roughing vs finishing, inch ↔ mm, coolant and chip evacuation, edge finder vs probe, weekly recap quiz.
