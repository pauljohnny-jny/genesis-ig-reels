from gen import *
SEND = "நண்பருக்கு அனுப்புங்கள்."
DIM = "#7FA6C4"


def box(x, y, w, h, stroke=LINE, sw=2, fill="#123A57", rx=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def chip(x, y, w, lab, t, col="#fff", stroke=LINE):
    return (f'<g class="a" data-t="{t:.2f}">{box(x, y, w, 64, stroke, 3 if stroke != LINE else 2)}'
            f'<text x="{x + w/2:.0f}" y="{y + 43}" text-anchor="middle" style="font:700 26px Inter" fill="{col}">{esc(lab)}</text></g>')


# =====================================================================================================
# REEL 41: Clearance hole for an M8 bolt (ISO 273). Target 28 s. CTA: SAVE.
# Hook format: (3) wrong vs right. Options considered:
#   "M8 bolt: Ø8 hole?" (wrong value first, bolt stops on the plate at frame 1, answered Ø9 at 1.8 s; chosen: specific size,
#       motion from frame 1, answered in scene 1/2 and echoed in scene 5)
#   "M8-க்கு எந்த hole?" (countdown quiz 8 / 9 / 10) / "Clearance hole size எப்படி தேர்வு செய்வீர்கள்?" (interview question)
# Sources:
#   ISO 273:1979 "Fasteners – Clearance holes for bolts and screws" (iso.org/standard/4183; abstract: hole diameters in fine,
#     medium and coarse series for thread diameters 1–150 mm; reviewed and confirmed 2024, current).
#   M8 values fine 8.4 / medium 9 / coarse 10 mm: published ISO 273 tables (e.g. Optimas technical resources "Recommended Tapping
#     Drill and Clearance Hole Sizes": M8 close 8.4, medium 9, free 10) and ASME B18.2.8 metric clearance holes as reproduced in
#     Machinery's Handbook 31st ed. (states agreement with ISO 273): M8 close 8.4, normal 9, loose 10.
#   Tapped plate: Sandvik Coromant CoroTap 200 M8x1.25 (T200-MM101JA-M8B115) listed drilling diameter 6.8 mm; other taps differ
#     (e.g. CoroTap 300 T106 lists 6.9 mm), so the reel says "tap maker data".
#   Arithmetic: Ø9 − Ø8 = 1 mm on diameter, 0.5 mm each side when centred (nominal). Position error in the hook drawing is
#     exaggerated and labelled.
PX = 7.5  # px per mm in the hook drawing
H41 = dict(hook="M8 bolt: Ø8 hole?", hsize=90, hook2="தவறு! Clearance இல்லை.", h2size=52, s=0, e=4.4, flash_t=1.2, svg=f'''
<text class="fig" x="24" y="44">SIDE VIEW · SCHEMATIC · mm</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">ISO 273 · METRIC</text>
<g class="shake" data-t="1.2">
<rect x="40" y="330" width="360" height="60" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="180" y="328" width="60" height="64" fill="{PANEL}"/>
<rect x="40" y="392" width="360" height="100" fill="#3E6A8E" stroke="{LINE}" stroke-width="2.5"/>
<rect x="198" y="390" width="60" height="70" fill="{PANEL}"/>
<path d="M198 404h60M198 420h60M198 436h60M198 452h60" stroke="#7FA6C4" stroke-width="2"/>
<text x="120" y="368" text-anchor="middle" style="font:600 22px Inter" fill="#fff">PLATE A</text>
<text x="120" y="450" text-anchor="middle" style="font:600 22px Inter" fill="#fff">PLATE B · M8</text>
<g class="move" data-t="0" data-d="1.2" data-dy="120">
<rect x="183" y="70" width="90" height="44" rx="6" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<rect x="198" y="114" width="60" height="96" fill="{OR}" stroke="#fff" stroke-width="2.5"/>
<path d="M198 130l60 10M198 150l60 10M198 170l60 10M198 190l60 10" stroke="{PANEL}" stroke-width="3"/></g>
</g>
<text class="a" data-t="1.3" x="176" y="300" text-anchor="end" style="font:800 26px Inter" fill="{RED}">STOPS HERE</text>
<text x="220" y="540" text-anchor="middle" style="font:600 20px Plex" fill="#9FC3DD">HOLE OFFSET EXAGGERATED</text>
{box(440, 90, 308, 190, RED, 4, "#3A1A1A")}
<text x="594" y="150" text-anchor="middle" style="font:600 24px Plex" fill="#FFD2C9">WRONG</text>
<text x="594" y="236" text-anchor="middle" style="font:800 80px Inter" fill="{RED}">Ø8</text>
{cross(716, 122, 1.2)}
<g class="a" data-t="1.8">{box(440, 310, 308, 190, GRN, 4, "#0F3A2A")}
<text x="594" y="370" text-anchor="middle" style="font:600 24px Plex" fill="#CFF2D5">RIGHT</text>
<text x="594" y="456" text-anchor="middle" style="font:800 80px Inter" fill="{GRN}">Ø9</text></g>
{tick(716, 342, 1.8)}
<text class="a" data-t="2.2" x="389" y="650" text-anchor="middle" style="font:800 44px Inter" fill="#fff">M8 BOLT → Ø9 HOLE</text>
<text class="a" data-t="2.2" x="389" y="706" text-anchor="middle" style="font:600 26px Plex" fill="#9FC3DD">ISO 273 MEDIUM SERIES</text>''')

R41 = dict(id="41", slug="M8_Clearance_Hole_ISO273", scenes=[
 H41,
 dict(s=4.4, e=10.4, tag="ANSWER  /  02", title="M8 → Ø9 (medium)", tsize=72, sub="ISO 273: மூன்று series.", ssize=48,
      svg=fig("ISO 273 · M8 CLEARANCE HOLE · mm") + f'''
<g class="a" data-t="0.2">{box(40, 70, 698, 110)}
<text x="70" y="138" style="font:800 34px Inter" fill="#fff">FINE</text>
<text x="708" y="140" text-anchor="end" style="font:800 46px Inter" fill="#fff">Ø8.4</text></g>
<g class="a" data-t="0.6">{box(40, 200, 698, 110, GRN, 4)}
<text x="70" y="268" style="font:800 34px Inter" fill="{GRN}">MEDIUM</text>
<text x="708" y="270" text-anchor="end" style="font:800 46px Inter" fill="{GRN}">Ø9</text></g>
<g class="a" data-t="1.0">{box(40, 330, 698, 110)}
<text x="70" y="398" style="font:800 34px Inter" fill="#fff">COARSE</text>
<text x="708" y="400" text-anchor="end" style="font:800 46px Inter" fill="#fff">Ø10</text></g>
<text class="m a" data-t="1.3" x="389" y="490" text-anchor="middle" style="font-size:22px">DRAWING CALLOUT DECIDES WHICH ONE</text>''',
      body="Drawing-ல் கொடுத்த hole size-ஐயே drill செய்யுங்கள்.", body_t=1.7),
 dict(s=10.4, e=16.8, tag="WHY  /  03", title="Why clearance?", tsize=76, sub="Hole position சிறிது மாறும்.", ssize=46,
      svg=fig("TOP VIEW · SCHEMATIC · mm", "NOMINAL, CENTRED", orange=True) + f'''
<circle class="a" data-t="0.2" cx="230" cy="270" r="150" fill="{PANEL}" stroke="{GRN}" stroke-width="5"/>
<circle class="a" data-t="0.5" cx="230" cy="270" r="133" fill="{OR}" stroke="#fff" stroke-width="3"/>
<text class="a" data-t="0.5" x="230" y="282" text-anchor="middle" style="font:800 36px Inter" fill="{PANEL}">M8</text>
<text class="a" data-t="0.2" x="230" y="100" text-anchor="middle" style="font:700 28px Inter" fill="{GRN}">HOLE Ø9</text>
<g class="a" data-t="1.0">{box(420, 110, 318, 110)}
<text x="579" y="178" text-anchor="middle" style="font:800 36px Inter" fill="#fff">9 − 8 = 1 mm</text></g>
<g class="a" data-t="1.4">{box(420, 250, 318, 130, OR, 3)}
<text x="579" y="305" text-anchor="middle" style="font:800 36px Inter" fill="{OR}">0.5 mm</text>
<text x="579" y="350" text-anchor="middle" style="font:600 24px Plex" fill="#BFD6E8">EACH SIDE</text></g>
<text class="m a" data-t="1.6" x="579" y="460" text-anchor="middle" style="font-size:22px">GAP EXAGGERATED</text>''',
      body="இந்த இடைவெளியால், hole-கள் சிறிது விலகினாலும் bolt போகும்.", body_t=1.9),
 dict(s=16.8, e=23.2, tag="CHECK  /  04", title="Two plates, two holes", tsize=66, sub="Mix செய்யாதீர்கள்.", ssize=48,
      svg=fig("M8 JOINT") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "PLATE A: Ø9 DRILL", "Bolt கடந்து போகும் hole", 0.2)
          + checkrow(255, 2, "PLATE B: Ø6.8 → M8 TAP", "Tap maker data-படி drill", 0.7)
          + checkrow(395, 3, "DRAWING CALLOUT", "Size, depth முதலில் படியுங்கள்", 1.2),
      body="Tap drill size tap-ஐப் பொறுத்து மாறலாம் – catalogue பாருங்கள்.", body_t=1.7),
 dict(s=23.2, e=28.8, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="M8 bolt → Ø9 hole", ssize=50,
      svg=fig("HOW TO ANSWER") + chip(40, 66, 330, "CLEARANCE Ø9", 0.1, GRN, GRN) + chip(388, 66, 350, "TAPPED Ø6.8 → M8", 0.3, OR, OR)
          + chip(40, 150, 698, "FINE 8.4 · MEDIUM 9 · COARSE 10", 0.5) + '''
<text class="w a" data-t="0.9" x="40" y="300" style="font-size:30px">"முதலில் drawing callout,</text>
<text class="w a" data-t="0.9" x="40" y="346" style="font-size:30px"> பிறகு drill size."</text>
<text class="m a" data-t="1.2" x="40" y="440" style="font-size:22px">ISO 273 · METRIC M8 COARSE THREAD</text>''',
      cta=True, cta_t=1.5),
])

# =====================================================================================================
# REEL 42: Dial test indicator cosine error. Target 28 s. CTA: SAVE.
# Hook format: (1) cold-open demo. Options considered:
#   "0.05 → 0.0435?" (demo: stylus tilted 30°, dial shows 0.05 while the true value is about 0.0435; chosen: Mitutoyo's own
#       worked numbers, the surface moves from frame 1, answered at 1.6 s and echoed in scene 5)
#   "30°-ல் k = ?" (countdown quiz 0.98 / 0.87 / 0.50) / "DTI stylus-ஐ எப்படி வைப்பீர்கள்?" (interview question)
# Sources:
#   Mitutoyo dial test indicator user's manual (513-474-10E, No. 99MAH024): when the contact point cannot be set at a right angle to
#     the direction of measurement, true value (approximate) = reading × correction factor k; table 10° 0.98, 20° 0.94, 30° 0.87,
#     40° 0.77, 50° 0.64, 60° 0.50; example 30°, reading 0.05 mm × 0.87 = 0.0435 mm; use a contact point of the length specified
#     for the model.
#   Mitutoyo "Proper Use of a Dial Test Indicator" (cx.mitutoyo.com how-to 21005): keep the contact angle as close to parallel with
#     the measured surface as possible without shanking; view the reading straight on to avoid parallax.
#   The 30° tilt in the drawing is exaggerated for visibility and labelled; the reel says "approximate".
H42 = dict(hook="0.05 → 0.0435?", hsize=96, hook2="சாய்ந்தால் reading அதிகம்!", h2size=50, s=0, e=4.4, svg=f'''
<text class="fig" x="24" y="44">SIDE VIEW · SCHEMATIC</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">LEVER DTI · METRIC</text>
<rect x="60" y="110" width="200" height="110" rx="14" fill="#6C93B4" stroke="{LINE}" stroke-width="3"/>
<text x="160" y="176" text-anchor="middle" style="font:700 26px Inter" fill="#fff">DTI</text>
<circle cx="250" cy="250" r="12" fill="#fff"/>
<path d="M250 250L389 330" stroke="#fff" stroke-width="8" stroke-linecap="round"/>
<circle cx="389" cy="330" r="12" fill="{OR}" stroke="#fff" stroke-width="3"/>
<path d="M250 250L430 250" stroke="#7FA6C4" stroke-width="3" stroke-dasharray="10 8"/>
<path d="M330 250A80 80 0 0 1 320 290" fill="none" stroke="{OR}" stroke-width="4"/>
<text x="345" y="290" style="font:800 34px Inter" fill="{OR}">30°</text>
<g class="move" data-t="0" data-d="1.4" data-dy="-12">
<rect x="40" y="342" width="470" height="90" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<text x="275" y="398" text-anchor="middle" style="font:600 24px Inter" fill="#fff">SURFACE</text></g>
<text x="275" y="480" text-anchor="middle" style="font:600 20px Plex" fill="#9FC3DD">ANGLE EXAGGERATED FOR VISIBILITY</text>
{box(540, 100, 208, 170, OR, 4, "#0A2236")}
<text x="644" y="150" text-anchor="middle" style="font:600 24px Plex" fill="#BFD6E8">DIAL</text>
<text x="644" y="232" text-anchor="middle" style="font:800 56px Inter" fill="{OR}">0.050</text>
<g class="a" data-t="1.6">{box(540, 300, 208, 170, GRN, 4, "#0F3A2A")}
<text x="644" y="350" text-anchor="middle" style="font:600 24px Plex" fill="#CFF2D5">TRUE ≈</text>
<text x="644" y="432" text-anchor="middle" style="font:800 52px Inter" fill="{GRN}">0.0435</text></g>
<text class="a" data-t="2.0" x="389" y="640" text-anchor="middle" style="font:800 44px Inter" fill="#fff">0.05 × 0.87 = 0.0435 mm</text>
<text class="a" data-t="2.0" x="389" y="700" text-anchor="middle" style="font:600 26px Plex" fill="#9FC3DD">30° → k = 0.87 (MITUTOYO)</text>''')

R42 = dict(id="42", slug="DTI_Cosine_Error", scenes=[
 H42,
 dict(s=4.4, e=10.4, tag="ANSWER  /  02", title="True ≈ reading × k", tsize=70, sub="Angle பெரிது → error பெரிது.", ssize=44,
      svg=fig("MITUTOYO DTI MANUAL · CORRECTION k") + f'''
<g style="font:800 40px Inter">
<g class="a" data-t="0.2">{box(40, 70, 330, 90)}<text x="80" y="130" fill="#fff">10°</text><text x="330" y="130" text-anchor="end" fill="#fff">0.98</text></g>
<g class="a" data-t="0.4">{box(408, 70, 330, 90)}<text x="448" y="130" fill="#fff">20°</text><text x="698" y="130" text-anchor="end" fill="#fff">0.94</text></g>
<g class="a" data-t="0.6">{box(40, 180, 330, 90, OR, 4)}<text x="80" y="240" fill="{OR}">30°</text><text x="330" y="240" text-anchor="end" fill="{OR}">0.87</text></g>
<g class="a" data-t="0.8">{box(408, 180, 330, 90)}<text x="448" y="240" fill="#fff">40°</text><text x="698" y="240" text-anchor="end" fill="#fff">0.77</text></g></g>
<g class="a" data-t="1.2">{box(40, 300, 698, 130, GRN, 4)}
<text x="389" y="355" text-anchor="middle" style="font:600 24px Plex" fill="#BFD6E8">EXAMPLE · 30° · READING 0.05 mm</text>
<text x="389" y="408" text-anchor="middle" style="font:800 40px Inter" fill="{GRN}">0.05 × 0.87 = 0.0435 mm</text></g>
<text class="m a" data-t="1.5" x="389" y="480" text-anchor="middle" style="font-size:22px">APPROXIMATE VALUE</text>''',
      body="Stylus சாய்ந்திருந்தால் dial, உண்மையை விட அதிகமாகக் காட்டும்.", body_t=1.8),
 dict(s=10.4, e=16.8, tag="FIX  /  03", title="Stylus parallel", tsize=80, sub="Surface-க்கு இணையாக.", ssize=50,
      svg=fig("SIDE VIEW · SCHEMATIC", "MITUTOYO", orange=True) + f'''
<g class="a" data-t="0.2">{box(40, 66, 330, 330, RED, 3)}
<rect x="70" y="110" width="110" height="60" rx="10" fill="#6C93B4"/>
<path d="M175 150L280 230" stroke="#fff" stroke-width="7" stroke-linecap="round"/><circle cx="280" cy="230" r="10" fill="{OR}"/>
<rect x="60" y="240" width="290" height="60" fill="{STEEL}"/>
<text x="205" y="360" text-anchor="middle" style="font:800 30px Inter" fill="{RED}">TILTED</text></g>
{cross(340, 96, 0.4)}
<g class="a" data-t="0.8">{box(408, 66, 330, 330, GRN, 3)}
<rect x="438" y="140" width="110" height="60" rx="10" fill="#6C93B4"/>
<path d="M543 225L690 225" stroke="#fff" stroke-width="7" stroke-linecap="round"/><circle cx="690" cy="232" r="10" fill="{OR}"/>
<rect x="428" y="242" width="290" height="60" fill="{STEEL}"/>
<text x="573" y="360" text-anchor="middle" style="font:800 30px Inter" fill="{GRN}">PARALLEL</text></g>
{tick(708, 96, 1.0)}
<text class="m a" data-t="1.3" x="389" y="460" text-anchor="middle" style="font-size:22px">STYLUS SHANK MUST NOT TOUCH THE PART</text>''',
      body="முடியாவிட்டால் angle-ஐ அளந்து, k மூலம் திருத்துங்கள்.", body_t=1.8),
 dict(s=16.8, e=23.2, tag="CHECK  /  04", title="DTI: 3 checks", tsize=80, sub="அளக்கும் முன்.", ssize=50,
      svg=fig("BEFORE YOU TRUST THE DIAL") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "STYLUS ANGLE", "Parallel, அல்லது × k", 0.2)
          + checkrow(255, 2, "CONTACT POINT LENGTH", "Model-க்குரிய length மட்டும்", 0.7)
          + checkrow(395, 3, "READ STRAIGHT ON", "Parallax தவிர்க்க நேராகப் பாருங்கள்", 1.2),
      body="வேறு length stylus போட்டால் reading பெரிதாகத் தவறும்.", body_t=1.7),
 dict(s=23.2, e=28.8, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="30° → × 0.87", ssize=56,
      svg=fig("HOW TO ANSWER") + chip(40, 66, 330, "PARALLEL STYLUS", 0.1, GRN, GRN) + chip(388, 66, 350, "TILT → × k", 0.3, OR, OR)
          + chip(40, 150, 330, "RIGHT LENGTH", 0.5) + chip(388, 150, 350, "READ STRAIGHT", 0.6) + '''
<text class="w a" data-t="0.9" x="40" y="300" style="font-size:30px">"சாய்ந்த stylus, reading-ஐ</text>
<text class="w a" data-t="0.9" x="40" y="346" style="font-size:30px"> அதிகமாகக் காட்டும்."</text>
<text class="m a" data-t="1.2" x="40" y="440" style="font-size:22px">SOURCE: MITUTOYO DTI MANUAL · METRIC</text>''',
      cta=True, cta_t=1.5),
])

REELS = [R41, R42]
