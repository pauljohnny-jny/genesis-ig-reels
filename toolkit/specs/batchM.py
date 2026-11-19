from gen import *
SEND = "நண்பருக்கு அனுப்புங்கள்."
DIM = "#7FA6C4"


def box(x, y, w, h, stroke=LINE, sw=2, fill="#123A57", rx=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def chip(x, y, w, lab, t, col="#fff", stroke=LINE):
    return (f'<g class="a" data-t="{t:.2f}">{box(x, y, w, 64, stroke, 3 if stroke != LINE else 2)}'
            f'<text x="{x + w/2:.0f}" y="{y + 43}" text-anchor="middle" style="font:700 26px Inter" fill="{col}">{esc(lab)}</text></g>')


# =====================================================================================================
# REEL 41: Clearance hole for an M8 bolt (ISO 273). Target ~28 s. CTA: SAVE.
# Hook format: (3) wrong vs right. Options considered:
#   "M8 bolt → Ø8 hole?" (wrong value first: Ø8 = zero gap; then Ø9 with 0.5 mm per side; chosen: specific numbers, bolt moves at
#       frame 1, answered in scene 2 and echoed in scene 5)
#   "8.4, 9 அல்லது 10?" (countdown quiz) / "M8-க்கு clearance hole எவ்வளவு?" (interview question)
# Sources: ISO 273:1979 "Fasteners – Clearance holes for bolts and screws" (identical EN 20273:1991; confirmed current, reviewed
#   2024): fine, medium and coarse series for threads 1 to 150 mm, tolerance fields H12 / H13 / H14; for general purpose
#   applications, special applications chosen from design requirements. M8 row: fine 8.4, medium 9, coarse 10 mm. The ISO
#   text could not be opened from this session (iso.org blocked); the M8 row and tolerance fields were cross-checked against
#   the IS 1821:1987 adoption (tolerance fields) and published ISO 273 charts (Albany County Fasteners, Engineering Hardware,
#   Noramark), which all agree. Gap arithmetic: (9 − 8) / 2 = 0.5 mm per side. The "why" scene is a general statement (the gap
#   lets two drilled parts line up when the hole positions are not perfect), shown schematic and exaggerated.
PX = 16  # px per mm in the hook drawing
H41 = dict(hook="M8 bolt → Ø8 hole?", hsize=82, hook2="Clearance இல்லை!", h2size=58, s=0, e=4.2, svg=f'''
<text class="fig" x="24" y="44">SECTION · SCHEMATIC · mm</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">ISO 273</text>
<text x="200" y="100" text-anchor="middle" style="font:800 34px Inter" fill="{RED}">WRONG</text>
<text x="580" y="100" text-anchor="middle" style="font:800 34px Inter" fill="{GRN}">RIGHT</text>
<path d="M389 70V640" stroke="#2E5878" stroke-width="2"/>
<rect x="40" y="420" width="96" height="110" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="264" y="420" width="96" height="110" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="418" y="420" width="90" height="110" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="652" y="420" width="90" height="110" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<g class="shake" data-t="1.3"><g class="move" data-t="0" data-d="1.3" data-dy="120">
<rect x="100" y="150" width="200" height="56" rx="6" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<text x="200" y="188" text-anchor="middle" style="font:700 24px Inter" fill="#fff">M8</text>
<rect x="136" y="206" width="128" height="94" fill="#9DB9D0" stroke="{LINE}" stroke-width="2.5"/>
<path d="M136 230h128M136 254h128M136 278h128" stroke="{PANEL}" stroke-width="3"/></g></g>
<g class="move" data-t="0" data-d="1.6" data-dy="214">
<rect x="480" y="150" width="200" height="56" rx="6" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<text x="580" y="188" text-anchor="middle" style="font:700 24px Inter" fill="#fff">M8</text>
<rect x="516" y="206" width="128" height="94" fill="#9DB9D0" stroke="{LINE}" stroke-width="2.5"/>
<path d="M516 230h128M516 254h128M516 278h128" stroke="{PANEL}" stroke-width="3"/></g>
<text x="200" y="580" text-anchor="middle" style="font:800 40px Inter" fill="{RED}">HOLE Ø8</text>
<text x="200" y="624" text-anchor="middle" style="font:600 26px Plex" fill="#FFD2C9">GAP 0</text>
<text x="580" y="580" text-anchor="middle" style="font:800 40px Inter" fill="{GRN}">HOLE Ø9</text>
<text x="580" y="624" text-anchor="middle" style="font:600 26px Plex" fill="#C9F0CF">0.5 mm / SIDE</text>
{cross(330, 360, 1.4)}{tick(712, 360, 1.7)}
<text class="m a" data-t="2.0" x="389" y="710" text-anchor="middle" style="font-size:22px">SIZES EXAGGERATED FOR VISIBILITY</text>''')

R41 = dict(id="41", slug="M8_Clearance_Hole_ISO273", scenes=[
 H41,
 dict(s=4.2, e=10.2, tag="ANSWER  /  02", title="M8: 8.4 / 9 / 10", tsize=80, sub="ISO 273: மூன்று series.", ssize=48,
      svg=fig("ISO 273 · M8 CLEARANCE HOLE · mm", "GENERAL PURPOSE", orange=True) + f'''
<g class="a" data-t="0.2">{box(40, 70, 698, 118)}
<text x="70" y="142" style="font:800 36px Inter" fill="#fff">FINE</text>
<text x="420" y="144" text-anchor="middle" style="font:800 50px Inter" fill="{OR}">Ø8.4</text>
<text x="708" y="142" text-anchor="end" style="font:600 28px Plex" fill="#BFD6E8">H12</text></g>
<g class="a" data-t="0.6">{box(40, 204, 698, 118, OR, 3)}
<text x="70" y="276" style="font:800 36px Inter" fill="#fff">MEDIUM</text>
<text x="420" y="278" text-anchor="middle" style="font:800 50px Inter" fill="{OR}">Ø9</text>
<text x="708" y="276" text-anchor="end" style="font:600 28px Plex" fill="#BFD6E8">H13</text></g>
<g class="a" data-t="1.0">{box(40, 338, 698, 118)}
<text x="70" y="410" style="font:800 36px Inter" fill="#fff">COARSE</text>
<text x="420" y="412" text-anchor="middle" style="font:800 50px Inter" fill="{OR}">Ø10</text>
<text x="708" y="410" text-anchor="end" style="font:600 28px Plex" fill="#BFD6E8">H14</text></g>''',
      body="Ø8 hole-ல் bolt-க்கு இடைவெளி இல்லை.", body_t=1.6),
 dict(s=10.2, e=16.4, tag="WHY  /  03", title="Gap = alignment room", tsize=66, sub="இரண்டு part, இரண்டு hole.", ssize=48,
      svg=fig("TWO PARTS · SCHEMATIC", "EXAGGERATED FOR VISIBILITY", orange=True) + f'''
<rect x="120" y="110" width="538" height="90" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="120" y="200" width="538" height="90" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<rect x="320" y="110" width="144" height="90" fill="{PANEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="338" y="200" width="144" height="90" fill="{PANEL}" stroke="{LINE}" stroke-width="2.5"/>
<text x="110" y="166" text-anchor="end" style="font:600 22px Plex" fill="#BFD6E8">A</text>
<text x="110" y="256" text-anchor="end" style="font:600 22px Plex" fill="#BFD6E8">B</text>
<g class="move" data-t="0.4" data-d="1.2" data-dy="280"><rect x="315" y="-220" width="170" height="40" rx="6" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/><rect x="345" y="-180" width="110" height="230" fill="#9DB9D0" stroke="{LINE}" stroke-width="2.5"/></g>
<text class="a" data-t="1.4" x="389" y="370" text-anchor="middle" style="font:800 34px Inter" fill="{GRN}">HOLES OFFSET · BOLT STILL PASSES</text>
<text class="a" data-t="1.8" x="389" y="440" text-anchor="middle" style="font:700 30px Inter" fill="{OR}">Ø9 − Ø8 = 1 mm → 0.5 / SIDE</text>''',
      body="Hole position சிறிது மாறினாலும் bolt போக இடம் வேண்டும்.", body_t=2.0),
 dict(s=16.4, e=22.6, tag="CHECK  /  04", title="Drawing decides", tsize=76, sub="எந்த series? Drill முன்.", ssize=48,
      svg=fig("BEFORE YOU DRILL") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "READ THE CALLOUT", "Drawing-ல் உள்ள Ø (உதா. Ø9)", 0.2)
          + checkrow(255, 2, "NO SIZE GIVEN?", "ஊகிக்காதீர்கள்; கேளுங்கள்", 0.7)
          + checkrow(395, 3, "SPECIAL JOB", "Design requirement-படி", 1.2),
      body="Series-ஐ drawing அல்லது engineer தீர்மானிப்பார்.", body_t=1.7),
 dict(s=22.6, e=28.2, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="M8 → Ø8 இல்லை.", ssize=48,
      svg=fig("HOW TO ANSWER") + chip(40, 66, 210, "FINE 8.4", 0.1) + chip(268, 66, 250, "MEDIUM 9", 0.25, OR, OR)
          + chip(536, 66, 202, "COARSE 10", 0.4) + chip(40, 150, 698, "ISO 273 · DRAWING DECIDES THE SERIES", 0.55, GRN, GRN) + '''
<text class="w a" data-t="0.9" x="40" y="300" style="font-size:30px">"M8-க்கு clearance hole Ø8 அல்ல;</text>
<text class="w a" data-t="0.9" x="40" y="346" style="font-size:30px"> drawing-ல் உள்ள series-படி."</text>
<text class="m a" data-t="1.3" x="40" y="440" style="font-size:22px">GENERAL PURPOSE VALUES · METRIC</text>''',
      cta=True, cta_t=1.6),
])

# =====================================================================================================
# REEL 42: Dial test indicator cosine error (lever-type DTI). Target ~28 s. CTA: SAVE.
# Hook format: (1) cold-open demo. Options considered:
#   "Dial 0.05, true 0.0435?" (demo: stylus at 30°, surface moves, dial reads 0.05; true ≈ 0.0435; chosen: specific numbers,
#       motion at frame 1, answered in scene 2 and echoed in scene 5)
#   "30° → × ? " (countdown quiz) / "Test indicator angle ஏன் முக்கியம்?" (interview question)
# Sources: Mitutoyo dial test indicator User's Manual (e.g. 513-474-10E): "True value (approximate value) = reading × correction
#   factor (k)"; worked example "0.05 mm (reading) x 0.87 (correction factor for 30°) = 0.0435 mm"; k 10° 0.98, 20° 0.94, 30° 0.87.
#   Mitutoyo Quick Guide to Precision Measuring Instruments (E11003) / catalogue: set the angle θ between contact point and
#   measuring face as small as possible; if θ is kept below 10° the effect can be ignored; the catalogue table rounds 30° to 0.86
#   (cos 30° = 0.866). Read via web search of the Mitutoyo documents (mitutoyo.com blocked from this session).
#   The on-screen k values follow the user's manual; labelled "MITUTOYO DTI MANUAL · CHECK YOUR MODEL".
H42 = dict(hook="Dial 0.05, true 0.0435?", hsize=70, hook2="Stylus சாய்ந்தால் பிழை!", h2size=56, s=0, e=4.2, svg=f'''
<text class="fig" x="24" y="44">LEVER-TYPE DTI · SCHEMATIC</text>
<rect x="60" y="130" width="270" height="100" rx="20" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<text x="195" y="192" text-anchor="middle" style="font:700 30px Inter" fill="#fff">DTI</text>
<path d="M330 210L520 320" stroke="#fff" stroke-width="6" stroke-linecap="round"/><circle cx="520" cy="320" r="9" fill="{OR}"/>
<path d="M450 320A70 70 0 0 1 459.4 285" fill="none" stroke="{OR}" stroke-width="3"/>
<text x="360" y="306" style="font:800 28px Inter" fill="{OR}">θ 30°</text>
<g class="move" data-t="0" data-d="1.5" data-dy="-36"><rect x="120" y="356" width="628" height="130" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<text x="434" y="436" text-anchor="middle" style="font:600 24px Inter" fill="#fff">PART SURFACE</text></g>
<circle cx="640" cy="170" r="100" fill="#F4F8FB" stroke="{LINE}" stroke-width="4"/>
<path d="M640 72v14M738 170h-14M542 170h14M709.3 100.7l-10 10M570.7 100.7l10 10" stroke="#11324F" stroke-width="3"/>
<text x="640" y="110" text-anchor="middle" style="font:700 22px Inter" fill="#11324F">0</text>
<path class="draw" data-t="0" data-d="1.5" data-lin="1" pathLength="1" d="M640 78A92 92 0 0 1 705.05 104.95" fill="none" stroke="{OR}" stroke-width="8"/>
<path class="a" data-t="1.5" d="M640 170L700.1 109.9" stroke="{RED}" stroke-width="5" stroke-linecap="round"/>
<circle cx="640" cy="170" r="10" fill="#11324F"/>
<text x="640" y="236" text-anchor="middle" style="font:600 18px Plex" fill="#11324F">0.01 mm</text>
<text class="a" data-t="1.6" x="389" y="570" text-anchor="middle" style="font:800 44px Inter" fill="{OR}">READS 0.05</text>
<text class="a" data-t="2.0" x="389" y="634" text-anchor="middle" style="font:800 36px Inter" fill="{GRN}">TRUE ≈ 0.05 × 0.87 = 0.0435</text>
<text class="m a" data-t="2.2" x="389" y="710" text-anchor="middle" style="font-size:22px">MOTION EXAGGERATED FOR VISIBILITY</text>''')

R42 = dict(id="42", slug="DTI_Cosine_Error", scenes=[
 H42,
 dict(s=4.2, e=10.2, tag="ANSWER  /  02", title="True ≈ reading × k", tsize=72, sub="30° → k = 0.87", ssize=50,
      svg=fig("LEVER-TYPE DTI", "MITUTOYO DTI MANUAL", orange=True) + f'''
<g class="a" data-t="0.2">{box(40, 70, 698, 120)}
<text x="64" y="118" style="font:800 32px Inter" fill="{OR}">θ = STYLUS ↔ SURFACE</text>
<text x="64" y="166" style="font:600 25px Plex" fill="#BFD6E8">ANGLE BETWEEN THEM</text></g>
<g class="a" data-t="0.7">{box(40, 210, 698, 120)}
<text x="64" y="258" style="font:800 32px Inter" fill="#fff">BIG θ → DIAL READS HIGH</text>
<text x="64" y="306" style="font:600 25px Plex" fill="#BFD6E8">MULTIPLY BY k (≤ 1)</text></g>
<g class="a" data-t="1.3">{box(40, 352, 698, 130, OR, 3)}
<text x="389" y="434" text-anchor="middle" style="font:800 40px Inter" fill="{OR}">0.05 × 0.87 = 0.0435 mm</text></g>''',
      body="Stylus-க்கும் surface-க்கும் இடையிலான கோணமே θ.", body_t=1.8),
 dict(s=10.2, e=16.4, tag="TABLE  /  03", title="k by angle", tsize=80, sub="கோணம் கூடினால் பிழை கூடும்.", ssize=38,
      svg=fig("CORRECTION FACTOR k", "CHECK YOUR MODEL", orange=True) + f'''
<g class="a" data-t="0.2">{box(40, 70, 698, 100)}
<text x="90" y="136" style="font:800 40px Inter" fill="#fff">10°</text><text x="690" y="136" text-anchor="end" style="font:800 44px Inter" fill="{GRN}">0.98</text></g>
<g class="a" data-t="0.6">{box(40, 186, 698, 100)}
<text x="90" y="252" style="font:800 40px Inter" fill="#fff">20°</text><text x="690" y="252" text-anchor="end" style="font:800 44px Inter" fill="{OR}">0.94</text></g>
<g class="a" data-t="1.0">{box(40, 302, 698, 100, RED, 3)}
<text x="90" y="368" style="font:800 40px Inter" fill="#fff">30°</text><text x="690" y="368" text-anchor="end" style="font:800 44px Inter" fill="{RED}">0.87</text></g>
<text class="m a" data-t="1.4" x="389" y="466" text-anchor="middle" style="font-size:22px">k ≈ cos θ · VALUES: MITUTOYO DTI MANUAL</text>''',
      body="30°-ல் true value reading-ஐ விட சுமார் 13% குறைவு.", body_t=1.8),
 dict(s=16.4, e=22.6, tag="FIX  /  04", title="Keep θ small", tsize=80, sub="10°-க்குக் குறைவு: பிழை சிறிது.", ssize=38,
      svg=fig("SET-UP · SCHEMATIC", "MITUTOYO GUIDE", orange=True) + f'''
<rect x="60" y="90" width="250" height="90" rx="18" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<text x="185" y="146" text-anchor="middle" style="font:700 28px Inter" fill="#fff">DTI</text>
<path d="M310 160L560 196" stroke="#fff" stroke-width="6" stroke-linecap="round"/><circle cx="560" cy="200" r="9" fill="{GRN}"/>
<rect x="100" y="209" width="640" height="110" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<text x="420" y="276" text-anchor="middle" style="font:600 24px Inter" fill="#fff">PART SURFACE</text>
{tick(690, 150, 0.6)}
<text class="a" data-t="0.9" x="389" y="384" text-anchor="middle" style="font:800 34px Inter" fill="{GRN}">STYLUS ALMOST PARALLEL</text>
<text class="a" data-t="1.3" x="389" y="444" text-anchor="middle" style="font:600 26px Plex" fill="#BFD6E8">SET θ AS SMALL AS POSSIBLE</text>''',
      body="அளக்கும் முன் stylus கோணத்தைச் சரிசெய்யுங்கள்.", body_t=1.8),
 dict(s=22.6, e=28.2, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="0.05 at 30° → 0.0435", ssize=48,
      svg=fig("HOW TO ANSWER") + chip(40, 66, 250, "θ SMALL", 0.1, GRN, GRN) + chip(308, 66, 430, "TRUE ≈ READING × k", 0.25, OR, OR)
          + chip(40, 150, 698, "30° → k 0.87 (MITUTOYO DTI MANUAL)", 0.4) + '''
<text class="w a" data-t="0.8" x="40" y="300" style="font-size:30px">"Stylus-ஐ surface-க்கு இணையாக</text>
<text class="w a" data-t="0.8" x="40" y="346" style="font-size:30px"> வைப்பேன்; சாய்ந்தால் k போடுவேன்."</text>
<text class="m a" data-t="1.2" x="40" y="440" style="font-size:22px">LEVER-TYPE DTI · k DEPENDS ON MODEL</text>''',
      cta=True, cta_t=1.6),
])

REELS = [R41, R42]
