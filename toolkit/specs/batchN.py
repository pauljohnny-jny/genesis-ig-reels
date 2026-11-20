from gen import *


def box(x, y, w, h, stroke=LINE, sw=2, fill="#123A57", rx=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def chip(x, y, w, lab, t, col="#fff", stroke=LINE):
    return (f'<g class="a" data-t="{t:.2f}">{box(x, y, w, 64, stroke, 3 if stroke != LINE else 2)}'
            f'<text x="{x + w/2:.0f}" y="{y + 43}" text-anchor="middle" style="font:700 26px Inter" fill="{col}">{esc(lab)}</text></g>')


def reamer(x, y, w=100, h=230):
    """Schematic straight-flute reamer, body x..x+w, shank above."""
    return (f'<rect x="{x + w*0.2:.0f}" y="{y - 90}" width="{w*0.6:.0f}" height="92" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#9DB9D0" stroke="{LINE}" stroke-width="2.5"/>'
            f'<path d="M{x + w*0.33:.0f} {y}v{h}M{x + w*0.66:.0f} {y}v{h}" stroke="{PANEL}" stroke-width="3"/>'
            f'<path d="M{x} {y + h}l10 12h{w - 20}l10 -12" fill="#9DB9D0" stroke="{LINE}" stroke-width="2.5"/>')


# =====================================================================================================
# REEL 43: Reaming stock allowance – don't drill to reamer size. Target ~28 s. CTA: SAVE.
# Hook format: (3) wrong vs right. Options considered:
#   "Ø10 reamer, Ø10 drill?" (wrong value first: zero stock, reamer rubs; then Ø9.8 drill leaves 0.2 mm; chosen: specific
#       numbers, reamers move at frame 1, answered in scene 2 and echoed in scene 5)
#   "Ø10 ream: drill 9.8, 9.9 or 10?" (countdown quiz) / "Ream செய்ய எவ்வளவு stock விடுவீர்கள்?" (interview question)
# Sources (read 20 Nov 2026):
#   Sandvik Coromant, "How to ream a hole" (sandvik.coromant.com/en-gb/knowledge/reaming/how-to-ream-a-hole): "The recommended
#     stock removal in reaming operations is dependent on the application material and the surface finish of the pre-drilled
#     hole." Table row P1: Ø1-3 0.1-0.2 · 3-5 0.1-0.2 · 5.1-10 0.2 · 10.1-20 0.2-0.3 · 20.1-30 0.3-0.4 · >30 0.4-0.5 mm.
#     Same page: straightness of the pre-machined hole < 0.05 mm; reaming should not be expected to correct positional or
#     straightness errors of the pre-machined hole.
#   Sandvik Coromant, "How to use CoroReamer 835": "It is a common mistake to prepare holes for reaming with too little stock
#     left. If insufficient stock is left in the hole before reaming, the reamer will rub and quickly show wear, resulting in a
#     loss of diameter. For performance, it is equally important not to leave too much stock in the hole."
#   Sandvik Coromant, "Troubleshooting reaming": undersized bore and chattermarks both list "Allowance for reaming is too small".
#   Taylor & Jones reamer technical section (reamer maker) gives the same warning and a free-cutting mild steel guide
#     (over 6 up to 12 mm dia: 0.2-0.3 mm), consistent with Sandvik.
#   Stock is shown as reamer Ø − pre-drill Ø (Ø10 − Ø9.8 = 0.2 mm), the reading of the table stated in the caption.
R43_H = dict(hook="Ø10 reamer, Ø10 drill?", hsize=72, hook2="Stock 0 → reamer rub ஆகும்!", h2size=50, s=0, e=4.2, svg=f'''
<text class="fig" x="24" y="44">SECTION · SCHEMATIC · mm</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">SANDVIK · P1 STEEL</text>
<text x="200" y="100" text-anchor="middle" style="font:800 34px Inter" fill="{RED}">WRONG</text>
<text x="580" y="100" text-anchor="middle" style="font:800 34px Inter" fill="{GRN}">RIGHT</text>
<path d="M389 70V640" stroke="#2E5878" stroke-width="2"/>
<rect x="40" y="390" width="110" height="170" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="250" y="390" width="110" height="170" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="420" y="390" width="110" height="170" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="630" y="390" width="110" height="170" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="530" y="390" width="12" height="170" fill="{OR}"/><rect x="618" y="390" width="12" height="170" fill="{OR}"/>
<g class="shake" data-t="1.3"><g class="move" data-t="0" data-d="1.3" data-dy="60">{reamer(150, 200)}</g></g>
<g class="move" data-t="0" data-d="1.6" data-dy="100">{reamer(530, 200)}</g>
<text x="200" y="600" text-anchor="middle" style="font:700 26px Inter" fill="#fff">DRILL Ø10 · REAM Ø10</text>
<text x="200" y="640" text-anchor="middle" style="font:800 28px Inter" fill="{RED}">STOCK 0 → RUBS</text>
<text x="580" y="600" text-anchor="middle" style="font:700 26px Inter" fill="#fff">DRILL Ø9.8 · REAM Ø10</text>
<text x="580" y="640" text-anchor="middle" style="font:800 28px Inter" fill="{GRN}">0.2 mm STOCK → CUTS</text>
{cross(330, 350, 1.4)}{tick(712, 350, 1.7)}
<text class="m a" data-t="2.0" x="389" y="712" text-anchor="middle" style="font-size:22px">STOCK EXAGGERATED FOR VISIBILITY</text>''')

R43 = dict(id="43", slug="Reaming_Stock_Allowance", scenes=[
 R43_H,
 dict(s=4.2, e=10.2, tag="ANSWER  /  02", title="Drill Ø9.8 → Ream Ø10", tsize=64, sub="0.2 mm stock விடுங்கள்.", ssize=48,
      svg=fig("SANDVIK COROMANT · STOCK mm", "P1 STEEL", orange=True)
          + "".join(f'''<g class="a" data-t="{0.15 + k*0.15:.2f}">{box(40, 62 + k*72, 698, 62, OR if hl else LINE, 3 if hl else 2)}
<text x="70" y="{104 + k*72}" style="font:700 30px Inter" fill="#fff">Ø {d}</text>
<text x="708" y="{105 + k*72}" text-anchor="end" style="font:800 32px Inter" fill="{OR if hl else "#BFD6E8"}">{v}</text></g>'''
                    for k, (d, v, hl) in enumerate([("1 – 3", "0.1 – 0.2", 0), ("3 – 5", "0.1 – 0.2", 0), ("5.1 – 10", "0.2", 1),
                                                    ("10.1 – 20", "0.2 – 0.3", 0), ("20.1 – 30", "0.3 – 0.4", 0), ("> 30", "0.4 – 0.5", 0)])),
      body="Stock = reamer Ø − drill Ø = 0.2 mm.", body_t=1.4),
 dict(s=10.2, e=16.4, tag="WHY  /  03", title="Too little = rubbing", tsize=70, sub="Stock குறைந்தால்?", ssize=48,
      svg=fig("SANDVIK COROMANT", "TROUBLESHOOTING", orange=True)
          + "".join(f'''<g class="a" data-t="{0.2 + k*0.4:.2f}">{box(40, 66 + k*96, 698, 80, RED, 3)}
<text x="70" y="{117 + k*96}" style="font:800 34px Inter" fill="{RED}">{lab}</text>
<text x="708" y="{117 + k*96}" text-anchor="end" style="font:600 26px Plex" fill="#FFD2C9">{note}</text></g>'''
                    for k, (lab, note) in enumerate([("REAMER RUBS", "NOT CUTTING"), ("WEARS QUICKLY", "SHORT LIFE"), ("LOSS OF DIAMETER", "UNDERSIZE")]))
          + f'''<g class="a" data-t="1.5">{box(40, 362, 698, 80, OR, 3)}
<text x="389" y="414" text-anchor="middle" style="font:800 32px Inter" fill="{OR}">TOO MUCH STOCK: ALSO BAD</text></g>''',
      body="அதிக stock-ம் நல்லதல்ல: maker table-படி.", body_t=1.9),
 dict(s=16.4, e=22.6, tag="CHECK  /  04", title="Before you ream", tsize=78, sub="மூன்று check.", ssize=50,
      svg=fig("BEFORE YOU REAM") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "PRE-DRILL SIZE", "Drill Ø-ஐ உறுதிசெய்யுங்கள்", 0.2)
          + checkrow(255, 2, "MATERIAL + TOOL TABLE", "Material மாறினால் stock மாறும்", 0.7)
          + checkrow(395, 3, "STRAIGHT PILOT HOLE", "Reamer position-ஐத் திருத்தாது", 1.2),
      body="Pilot hole straightness < 0.05 mm (Sandvik).", body_t=1.7),
 dict(s=22.6, e=28.2, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="Ø10 ream → Ø10 drill இல்லை.", ssize=44,
      svg=fig("HOW TO ANSWER") + chip(40, 66, 250, "DRILL Ø9.8", 0.1) + chip(308, 66, 430, "REAM Ø10", 0.25, OR, OR)
          + chip(40, 150, 698, "0.2 mm STOCK · SANDVIK P1 TABLE", 0.4, GRN, GRN) + '''
<text class="w a" data-t="0.8" x="40" y="300" style="font-size:30px">"Reamer அளவுக்கே drill செய்யமாட்டேன்;</text>
<text class="w a" data-t="0.8" x="40" y="346" style="font-size:30px"> maker table-படி stock விடுவேன்."</text>
<text class="m a" data-t="1.2" x="40" y="440" style="font-size:22px">MACHINE REAMING · METRIC · CHECK YOUR TOOL</text>''',
      cta=True, cta_t=1.6),
])

# =====================================================================================================
# REEL 44: Caliper – measure close to the beam (Abbe's principle). Target ~28 s. CTA: SAVE.
# Hook format: (1) cold-open demo. Options considered:
#   "Tip-ல் 0.008 mm பிழை?" (demo: part at the jaw tips, slider tilts, error appears; chosen: specific number from the
#       Mitutoyo example, motion at frame 1, answered in scene 2 and echoed in scene 5)
#   "h 40 vs h 10: பிழை?" (countdown quiz) / "Caliper-ல் Abbe error என்றால் என்ன?" (interview question)
# Sources (read 20 Nov 2026): Mitutoyo "Quick Guide to Measurement" (E11003, mitutoyo.com):
#   Abbe's principle: "maximum accuracy is obtained when the scale and the measurement axes are common"; variation in the
#     relative angle θ of the moving jaw of an instrument such as a caliper causes displacement not measured on the scale.
#   Caliper, "Moving Jaw Tilt Error": "This error can be represented by the same calculation formula for errors caused by
#     nonconformance to Abbe's Principle. Example: ... error slope of the jaws due to tilt of the slider is 0.01 mm in 50 mm
#     and the outside measuring jaws are 40 mm deep, then the error (at the jaw tip) is ... (40/50)x0.010 mm = 0.008 mm."
#   General notes (JIS handling note): the caliper has no constant-force device – measure with an appropriate even force;
#     "Take extra care when you measure it with the root or tip of the jaw because a large error could occur."
#   Mitutoyo "Calipers" (E12029): the caliper does not comply with Abbe's Principle because its scale is not coaxial with
#     the measurement axis.
#   h = 10 mm → 10 × 0.01 ÷ 50 = 0.002 mm is the same Mitutoyo formula with a smaller h (our arithmetic, same tilt).
R44_H = dict(hook="Tip-ல் 0.008 mm பிழை?", hsize=64, hook2="Abbe error: h முக்கியம்!", h2size=56, s=0, e=4.2, svg=f'''
<text class="fig" x="24" y="44">CALIPER · SCHEMATIC</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">MITUTOYO EXAMPLE</text>
<rect x="40" y="110" width="660" height="70" rx="6" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<path d="{"".join(f"M{60 + k*20} 110v{18 if k % 5 else 30}" for k in range(32))}" stroke="{PANEL}" stroke-width="2"/>
<text x="60" y="166" style="font:600 20px Plex" fill="{PANEL}">SCALE</text>
<path d="M70 180H140V500L105 540L70 500Z" fill="#9DB9D0" stroke="{LINE}" stroke-width="2.5"/>
<rect x="140" y="420" width="250" height="80" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<text x="265" y="492" text-anchor="middle" style="font:600 20px Inter" fill="#fff">PART</text>
<g class="until" data-end="1.2"><g class="move" data-t="0" data-d="1.0" data-dx="-110">
<rect x="460" y="96" width="150" height="98" rx="8" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<path d="M500 194H570V500L535 540L500 500Z" fill="#9DB9D0" stroke="{LINE}" stroke-width="2.5"/></g></g>
<g class="a" data-t="1.2" transform="rotate(-4 425 145)">
<rect x="350" y="96" width="150" height="98" rx="8" fill="#6C93B4" stroke="{RED}" stroke-width="3"/>
<path d="M390 194H460V500L425 540L390 500Z" fill="#9DB9D0" stroke="{RED}" stroke-width="3"/></g>
<path class="a" data-t="1.5" d="M630 145V460" stroke="{OR}" stroke-width="3" marker-start="url(#ao)" marker-end="url(#ao)"/>
<text class="a" data-t="1.5" x="650" y="312" style="font:800 34px Inter" fill="{OR}">h</text>
<path d="M40 145H700" stroke="{OR}" stroke-width="2" stroke-dasharray="8 8"/><path d="M140 460H700" stroke="#fff" stroke-width="2" stroke-dasharray="8 8"/>
<text class="a" data-t="1.6" x="389" y="606" text-anchor="middle" style="font:800 34px Inter" fill="{RED}">SLIDER TILT 0.01 / 50 mm</text>
<text class="a" data-t="2.0" x="389" y="660" text-anchor="middle" style="font:800 34px Inter" fill="{OR}">h 40 mm → ERROR 0.008 mm</text>
<text class="m a" data-t="2.2" x="389" y="716" text-anchor="middle" style="font-size:22px">TILT EXAGGERATED FOR VISIBILITY</text>''')

R44 = dict(id="44", slug="Caliper_Abbe_Error", scenes=[
 R44_H,
 dict(s=4.2, e=10.2, tag="ANSWER  /  02", title="Error = h × tilt", tsize=80, sub="Mitutoyo: tilt 0.01 / 50 mm", ssize=46,
      svg=fig("MOVING JAW TILT ERROR", "MITUTOYO QUICK GUIDE", orange=True) + f'''
<g class="a" data-t="0.2">{box(40, 70, 698, 110)}
<text x="64" y="118" style="font:800 30px Inter" fill="#fff">h = SCALE → MEASURING POINT</text>
<text x="64" y="160" style="font:600 25px Plex" fill="#BFD6E8">DISTANCE FROM THE BEAM</text></g>
<g class="a" data-t="0.7">{box(40, 200, 698, 120, RED, 3)}
<text x="64" y="250" style="font:800 30px Inter" fill="#fff">h 40 mm (JAW TIP)</text>
<text x="64" y="300" style="font:800 32px Inter" fill="{RED}">40 × 0.01 ÷ 50 = 0.008 mm</text></g>
<g class="a" data-t="1.3">{box(40, 340, 698, 120, GRN, 3)}
<text x="64" y="390" style="font:800 30px Inter" fill="#fff">h 10 mm (NEAR THE BEAM)</text>
<text x="64" y="440" style="font:800 32px Inter" fill="{GRN}">10 × 0.01 ÷ 50 = 0.002 mm</text></g>''',
      body="Part beam-க்கு அருகில் → h சிறிது → பிழை சிறிது.", body_t=1.8),
 dict(s=10.2, e=16.4, tag="WHY  /  03", title="Scale ≠ measuring line", tsize=64, sub="Caliper Abbe-ஐப் பின்பற்றாது.", ssize=44,
      svg=fig("ABBE'S PRINCIPLE · SCHEMATIC", "MITUTOYO", orange=True) + f'''
<rect x="40" y="90" width="698" height="60" rx="6" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<path d="M40 120H738" stroke="{OR}" stroke-width="3" stroke-dasharray="10 8"/>
<text x="389" y="80" text-anchor="middle" style="font:700 24px Inter" fill="{OR}">SCALE AXIS</text>
<path d="M80 150H140V400L110 430L80 400Z" fill="#9DB9D0" stroke="{LINE}" stroke-width="2.5"/>
<path d="M560 150H620V400L590 430L560 400Z" fill="#9DB9D0" stroke="{LINE}" stroke-width="2.5"/>
<rect x="140" y="320" width="420" height="70" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<path class="draw" data-t="0.4" data-d="0.8" pathLength="1" d="M40 355H738" stroke="#fff" stroke-width="3"/>
<text class="a" data-t="0.8" x="389" y="300" text-anchor="middle" style="font:700 24px Inter" fill="#fff">MEASURING LINE</text>
<path class="a" data-t="1.1" d="M680 124V351" stroke="{RED}" stroke-width="3" marker-start="url(#ar)" marker-end="url(#ar)"/>
<text class="a" data-t="1.1" x="700" y="250" style="font:800 32px Inter" fill="{RED}">h</text>
<text class="a" data-t="1.5" x="389" y="480" text-anchor="middle" style="font:800 30px Inter" fill="{GRN}">BEST: SCALE AND LINE IN LINE</text>''',
      body="Scale-க்கும் அளக்கும் வரிக்கும் இடைவெளி h.", body_t=1.9),
 dict(s=16.4, e=22.6, tag="CHECK  /  04", title="Measure smart", tsize=80, sub="மூன்று பழக்கம்.", ssize=50,
      svg=fig("CALIPER HABITS") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "SMALL h", "Part-ஐ beam பக்கம் வையுங்கள்", 0.2)
          + checkrow(255, 2, "EVEN FORCE", "அதிகமாக அழுத்தாதீர்கள்", 0.7)
          + checkrow(395, 3, "ROOT / TIP OF JAW", "கூடுதல் கவனம் (Mitutoyo)", 1.2),
      body="Caliper-ல் constant-force device இல்லை.", body_t=1.7),
 dict(s=22.6, e=28.2, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="Tip-ல் 0.008, beam அருகில் 0.002", ssize=42,
      svg=fig("HOW TO ANSWER") + chip(40, 66, 250, "SMALL h", 0.1, GRN, GRN) + chip(308, 66, 430, "ERROR = h × TILT", 0.25, OR, OR)
          + chip(40, 150, 698, "ABBE'S PRINCIPLE · MITUTOYO", 0.4) + '''
<text class="w a" data-t="0.8" x="40" y="300" style="font-size:30px">"Scale-ம் அளவும் ஒரே வரியில் இல்லை;</text>
<text class="w a" data-t="0.8" x="40" y="346" style="font-size:30px"> part-ஐ beam அருகில் வைப்பேன்."</text>
<text class="m a" data-t="1.2" x="40" y="440" style="font-size:22px">VERNIER / DIAL / DIGITAL CALIPER · mm</text>''',
      cta=True, cta_t=1.6),
])

REELS = [R43, R44]
