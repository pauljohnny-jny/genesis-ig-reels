from gen import *
import math
W = "#E6F0F7"
SEND = "நண்பருக்கு அனுப்புங்கள்."
DARK = "#11324F"

# =====================================================================================
# Batch H: measurement reels 19-23 (drafts, 5 Nov 2026). Sources are listed per reel.
# =====================================================================================

# ---------------- REEL 19: reading a metric vernier caliper (0.02 mm) ----------------
# Hook format: (3) wrong vs right. Options considered:
#   "16.12 mm? தவறு." (wrong value first, chosen) / "12-வது கோடு = 0.12?" / "Vernier எப்படிப் படிப்பீர்கள்?"
# Sources: Mitutoyo Quick Guide to Measurement (PG 19-21, Calipers): the vernier value "is read at the position where a
# main scale graduation line corresponds with a vernier graduation line"; on 0.02 mm calipers 50 vernier divisions
# span 49 mm (so one vernier division = 0.98 mm, difference 0.02 mm; source note corrected 5 Nov, media unchanged); check that the vernier
# reads zero with the jaws closed; look straight at the lines (parallax); measure with an appropriate even force.
# Mitutoyo 530-series catalogue: 0.02 mm vernier calipers are a current model (graduation is model-specific).
# Worked reading (schematic): vernier zero at 16.24 mm; line 12 coincides (16.24 + 12 x 0.98 = 28.00, a main-scale line).
PXV = 11  # px per mm

def vx(mm):
    return 40 + (mm - 10) * PXV

def vernier(zero, B, t=0.0, hl=None, move_dx=0, move_t=0.0, move_d=1.2, mark=True):
    main = [f'<rect x="20" y="{B-82}" width="738" height="82" fill="#B8CCDB"/>']
    for mm in range(10, 74):
        x = vx(mm)
        if x > 750: break
        L = 34 if mm % 10 == 0 else (26 if mm % 5 == 0 else 16)
        main.append(f'<path d="M{x} {B}v-{L}" stroke="{PANEL}" stroke-width="2"/>')
        if mm % 10 == 0:
            main.append(f'<text x="{x}" y="{B-46}" text-anchor="middle" style="font:700 24px Inter" fill="{PANEL}">{mm}</text>')
    x0, x1 = vx(zero), vx(zero + 49)
    ver = [f'<rect x="{x0-26:.1f}" y="{B}" width="{x1-x0+52:.1f}" height="86" fill="#8FAEC6" stroke="{LINE}" stroke-width="2"/>']
    for k in range(0, 51):
        x = vx(zero + k * 0.98)
        L = 30 if k % 5 == 0 else 17
        ver.append(f'<path d="M{x:.1f} {B}v{L}" stroke="{PANEL}" stroke-width="2"/>')
        if k % 5 == 0:
            ver.append(f'<text x="{x:.1f}" y="{B+58}" text-anchor="middle" style="font:700 22px Inter" fill="{PANEL}">{k//5}</text>')
    mv = f' class="move" data-t="{move_t}" data-d="{move_d}" data-dx="{move_dx}"' if move_dx else ""
    out = f'<g class="a" data-t="{t}">' + "".join(main) + f'<g{mv}>' + "".join(ver) + "</g></g>"
    if hl is not None and mark:
        x = vx(zero + hl * 0.98)
        out += (f'<g class="a" data-t="{t if not move_dx else move_t + move_d + 0.1}">'
                f'<path d="M{x:.1f} {B-30}V{B+30}" stroke="{OR}" stroke-width="5"/>'
                f'<path d="M{x:.1f} {B+92}l-13 22h26z" fill="{OR}"/></g>')
    return out

VZ = 16.24

R19 = dict(id="19", slug="Vernier_Caliper_Reading", scenes=[
 dict(hook="16.12 mm? தவறு.", hsize=88, hook2="Graduation என்ன?", s=0, e=4.2, svg=
      fig("VERNIER CALIPER · SCHEMATIC", "WRONG READING", orange=True)
      + vernier(VZ, 250, 0, hl=12, move_dx=6 * PXV, move_t=0.0, move_d=1.2) + f'''
<text class="a" data-t="1.2" x="40" y="430" style="font:700 30px Inter" fill="#fff">MAIN SCALE: 16 mm</text>
<text class="a" data-t="1.5" x="40" y="480" style="font:700 30px Inter" fill="{OR}">COINCIDING LINE: 12th</text>
<g class="a" data-t="1.9"><rect x="30" y="520" width="718" height="92" rx="14" fill="#123A57" stroke="{RED}" stroke-width="3"/>
<text x="56" y="580" style="font:800 36px Inter" fill="{RED}">12 × 0.01 → 16.12 mm</text></g>{cross(700, 566, 2.2)}
<text class="a" data-t="2.6" x="40" y="680" style="font:700 28px Inter" fill="{OR}">THIS SCALE: 0.02 mm PER LINE</text>'''),
 dict(s=4.2, e=10.8, tag="ANSWER  /  02", title="16.24 mm", tsize=86, sub="16 + 12 × 0.02", ssize=50,
      svg=fig("0.02 mm VERNIER · SCHEMATIC", "SOURCE: MITUTOYO", orange=True) + vernier(VZ, 150, 0, hl=12) + f'''
<text class="code a" data-t="0.4" x="40" y="300" style="font-size:28px" xml:space="preserve"><tspan fill="{W}">1 MAIN SCALE (LEFT OF 0)  16.00</tspan></text>
<text class="code a" data-t="0.9" x="40" y="345" style="font-size:28px" xml:space="preserve"><tspan fill="{W}">2 COINCIDING LINE         12th</tspan></text>
<text class="code a" data-t="1.4" x="40" y="390" style="font-size:28px" xml:space="preserve"><tspan fill="{OR}">3 12 × 0.02             + 0.24</tspan></text>
<g class="a" data-t="1.9"><rect x="40" y="415" width="698" height="86" rx="16" fill="#123A57" stroke="{OR}" stroke-width="4"/>
<text x="389" y="474" text-anchor="middle" style="font:800 46px Inter" fill="{OR}">= 16.24 mm</text></g>''',
      body="Vernier 0-க்கு முன் உள்ள mm, பிறகு ஒத்துப்போகும் கோடு × 0.02."),
 dict(s=10.8, e=17.4, tag="CHECK  /  03", title="Cross-check", tsize=78, sub="எண் 2 + 2 கோடுகள்", ssize=50,
      svg=fig("SAME SCALE, READ BY NUMBERS", "SCHEMATIC") + vernier(VZ, 150, 0, hl=12) + f'''
<path class="a" data-t="0.3" d="M{vx(VZ+10*0.98):.1f} 150V180" stroke="{GRN}" stroke-width="5"/>
<text class="code a" data-t="0.5" x="40" y="300" style="font-size:28px" xml:space="preserve"><tspan fill="{W}">EACH NUMBER = 5 LINES = 0.10</tspan></text>
<text class="code a" data-t="1.0" x="40" y="345" style="font-size:28px" xml:space="preserve"><tspan fill="{GRN}">NUMBER 2               = 0.20</tspan></text>
<text class="code a" data-t="1.5" x="40" y="390" style="font-size:28px" xml:space="preserve"><tspan fill="{W}">+ 2 LINES × 0.02       = 0.04</tspan></text>
<text class="a" data-t="2.0" x="40" y="450" style="font:800 36px Inter" fill="{OR}">0.20 + 0.04 = 0.24 mm</text>{tick(700, 438, 2.2)}
<text class="m a" data-t="2.4" x="40" y="496" style="font-size:22px">50 LINES = 49 mm ON THIS 0.02 mm SCALE</text>''',
      body="Graduation scale-ல் எழுதியிருக்கும்; அது model-ஐப் பொறுத்தது."),
 dict(s=17.4, e=24.0, tag="HABITS  /  04", title="Before reading", tsize=74, sub="மூன்று பழக்கங்கள்.",
      svg=fig("CALIPER CHECKS", "SOURCE: MITUTOYO", orange=True) + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "CLEAN + ZERO", "Jaws மூடினால் 0 காட்ட வேண்டும்", 0.3)
          + checkrow(255, 2, "LOOK STRAIGHT", "சாய்வாகப் பார்த்தால் parallax பிழை", 0.8)
          + checkrow(395, 3, "EVEN FORCE", "Jaw-ஐ அதிகமாக அழுத்தாதீர்கள்", 1.3),
      body="Zero சரியில்லை என்றால் reading-ம் சரியில்லை.", body_t=1.8),
 dict(s=24.0, e=30.6, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="16.12 அல்ல: 16.24 mm", ssize=50,
      svg=fig("HOW TO ANSWER") + f'''
<g class="a" data-t="0.3"><rect x="40" y="80" width="300" height="130" rx="14" fill="#123A57" stroke="{LINE}" stroke-width="3"/>
<text x="190" y="135" text-anchor="middle" style="font:800 34px Inter" fill="#fff">MAIN SCALE</text>
<text x="190" y="180" text-anchor="middle" style="font:600 26px Inter" fill="#9FC3DD">WHOLE mm</text></g>
<text class="a" data-t="0.5" x="374" y="160" text-anchor="middle" style="font:800 44px Inter" fill="#fff">+</text>
<g class="a" data-t="0.7"><rect x="408" y="80" width="330" height="130" rx="14" fill="#123A57" stroke="{OR}" stroke-width="3"/>
<text x="573" y="135" text-anchor="middle" style="font:800 34px Inter" fill="{OR}">LINE × GRAD.</text>
<text x="573" y="180" text-anchor="middle" style="font:600 26px Inter" fill="#9FC3DD">12 × 0.02</text></g>
<text class="code a" data-t="1.1" x="40" y="290" style="font-size:32px"><tspan fill="{W}">16 + 12 × 0.02 = </tspan><tspan fill="{OR}">16.24 mm</tspan></text>
<text class="w a" data-t="1.5" x="40" y="370" style="font-size:30px">"முதலில் graduation-ஐப் பார்ப்பேன்."</text>
<text class="m a" data-t="1.9" x="40" y="440" style="font-size:22px">GRADUATION IS MODEL-SPECIFIC. CHECK YOUR CALIPER.</text>''',
      body="உங்கள் caliper-ன் graduation-ஐச் சொல்லுங்கள்.", body_t=2.0, cta=True, cta_t=2.6),
])

# ---------------- REEL 20: reading a dial indicator (0.01 mm, revolution counter) ----------------
# Hook format: (1) cold-open demo (the pointer spins past a full turn and stops at 35). Options considered:
#   "35 = 0.35 mm?" (demo, chosen) / "0.35 or 1.35?" (wrong vs right) / "Revolution counter எதற்கு?" (interview question)
# Sources: Mitutoyo Dial Indicators catalogue (Series 2, 2046S: graduation 0.01 mm, range 10 mm, 1 mm per revolution;
# reverse-reading example is 2902S (dial 100-0); 2047S is balanced 0-50-0 – source note corrected 5 Nov, media unchanged); Mitutoyo Dial Indicator User's Manual No. 99MAG014A1 (short pointer = revolution
# counting device; set the pointer to the reference with a master and read the short pointer too; measure in the same
# orientation and conditions as the reference setting; read the pointer from the front).
# Reading: 1 revolution (1 mm) + 35 divisions x 0.01 mm = 1.35 mm. Counter drawn as 1 mm per division.

def dialg(cx, cy, r, long_deg=0.0, short_deg=0.0, t=0.0, spin_until=None, counter=True, num=True):
    p = [f'<circle cx="{cx}" cy="{cy}" r="{r+10}" fill="#6C93B4" stroke="{LINE}" stroke-width="3"/>',
         f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#EEF4F9"/>']
    for k in range(100):
        a = math.radians(k * 3.6)
        L = 0.13 * r if k % 10 == 0 else (0.09 * r if k % 5 == 0 else 0.055 * r)
        x1, y1 = cx + (r - 4) * math.sin(a), cy - (r - 4) * math.cos(a)
        x2, y2 = cx + (r - 4 - L) * math.sin(a), cy - (r - 4 - L) * math.cos(a)
        p.append(f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" stroke="{PANEL}" stroke-width="{2.5 if k % 5 == 0 else 1.5}"/>')
        if num and k % 10 == 0 and r >= 140:
            rr = r - 0.13 * r - 26
            p.append(f'<text x="{cx + rr*math.sin(a):.1f}" y="{cy - rr*math.cos(a) + 9:.1f}" text-anchor="middle" style="font:700 24px Inter" fill="{PANEL}">{k}</text>')
    if counter:
        sx, sy, sr = cx, cy - 0.42 * r, 0.2 * r
        p.append(f'<circle cx="{sx}" cy="{sy:.1f}" r="{sr:.1f}" fill="#fff" stroke="{STEEL}" stroke-width="2"/>')
        for k in range(10):
            a = math.radians(k * 36)
            p.append(f'<path d="M{sx + sr*math.sin(a):.1f} {sy - sr*math.cos(a):.1f}L{sx + (sr-8)*math.sin(a):.1f} {sy - (sr-8)*math.cos(a):.1f}" stroke="{PANEL}" stroke-width="2"/>')
        sp = f'<path d="M{sx} {sy+6:.1f}V{sy - sr + 6:.1f}" stroke="{PANEL}" stroke-width="4" stroke-linecap="round"/>'
    lp = f'<path d="M{cx} {cy + 0.18*r:.1f}V{cy - r + 0.1*r:.1f}" stroke="{RED}" stroke-width="5" stroke-linecap="round"/>'
    hub = f'<circle cx="{cx}" cy="{cy}" r="{0.06*r:.1f}" fill="{PANEL}"/>'
    out = "".join(p)
    if spin_until:
        T = spin_until
        if counter:
            out += (f'<g class="spin until" data-cx="{sx}" data-cy="{sy:.1f}" data-r="{short_deg/(120*T):.5f}" data-end="{T}">{sp}</g>'
                    f'<g class="draw" data-t="{T-0.03}" data-d="0.02" transform="rotate({short_deg} {sx} {sy:.1f})">{sp}</g>')
        out += (f'<g class="spin until" data-cx="{cx}" data-cy="{cy}" data-r="{long_deg/(120*T):.5f}" data-end="{T}">{lp}</g>'
                f'<g class="draw" data-t="{T-0.03}" data-d="0.02" transform="rotate({long_deg} {cx} {cy})">{lp}</g>')
    else:
        if counter:
            out += f'<g transform="rotate({short_deg} {sx} {sy:.1f})">{sp}</g>'
        out += f'<g transform="rotate({long_deg} {cx} {cy})">{lp}</g>'
    return f'<g class="a" data-t="{t}">{out}{hub}</g>'

def arc(cx, cy, R, a0, a1, col, t, sweep=1):
    p0 = (cx + R * math.sin(math.radians(a0)), cy - R * math.cos(math.radians(a0)))
    p1 = (cx + R * math.sin(math.radians(a1)), cy - R * math.cos(math.radians(a1)))
    return (f'<path class="a" data-t="{t}" d="M{p0[0]:.1f} {p0[1]:.1f}A{R} {R} 0 0 {sweep} {p1[0]:.1f} {p1[1]:.1f}" '
            f'stroke="{col}" stroke-width="7" fill="none" marker-end="url(#{"ao" if col == OR else "aw"})"/>')

R20 = dict(id="20", slug="Dial_Indicator_Reading", scenes=[
 dict(hook="35 = 0.35 mm?", hsize=100, hook2="Counter-ஐப் பாருங்கள்!", h2size=56, s=0, e=3.8, svg=
      fig("DIAL INDICATOR · 0.01 mm", "SCHEMATIC", orange=True)
      + dialg(389, 290, 200, long_deg=486, short_deg=36, t=0, spin_until=1.8) + f'''
<g class="move" data-t="0" data-d="1.8" data-dy="-26"><rect x="377" y="500" width="24" height="96" fill="#B8CCDB" stroke="{LINE}" stroke-width="2"/>
<circle cx="389" cy="602" r="12" fill="#B8CCDB" stroke="{LINE}" stroke-width="2"/><rect x="290" y="614" width="198" height="80" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/></g>
<rect x="369" y="490" width="40" height="22" fill="#6C93B4"/>
<text class="a" data-t="1.9" x="40" y="560" style="font:800 36px Inter" fill="{RED}">0.35 mm ?</text>{cross(290, 547, 2.1)}
<circle class="a" data-t="2.3" cx="389" cy="206" r="50" fill="none" stroke="{OR}" stroke-width="6"/>
<text class="a" data-t="2.4" x="738" y="560" text-anchor="end" style="font:800 32px Inter" fill="{OR}">COUNTER: 1</text>'''),
 dict(s=3.8, e=8.0, tag="ANSWER  /  02", title="= 1.35 mm", tsize=84, sub="1 mm + 35 × 0.01", ssize=50,
      svg=fig("2046S EXAMPLE · 1 mm / REV", "SOURCE: MITUTOYO", orange=True) + dialg(200, 290, 150, 126, 36) + f'''
<text class="a" data-t="0.3" x="400" y="150" style="font:700 30px Inter" fill="#fff">COUNTER 1</text>
<text class="a" data-t="0.5" x="738" y="150" text-anchor="end" style="font:700 30px Inter" fill="#fff">1.00</text>
<text class="a" data-t="0.8" x="400" y="230" style="font:700 30px Inter" fill="#fff">POINTER 35</text>
<text class="a" data-t="1.0" x="738" y="230" text-anchor="end" style="font:700 30px Inter" fill="#fff">+ 0.35</text>
<g class="a" data-t="1.4"><rect x="390" y="280" width="348" height="100" rx="16" fill="#123A57" stroke="{OR}" stroke-width="4"/>
<text x="564" y="346" text-anchor="middle" style="font:800 44px Inter" fill="{OR}">1.35 mm</text></g>''',
      body="ஒரு முழுச் சுற்று = 1 mm (இந்த model)."),
 dict(s=8.0, e=12.2, tag="DIRECTION  /  03", title="Which way?", tsize=78, sub="80 அல்ல: 20 பிரிவு", ssize=50,
      svg=fig("SAME 20 DIVISIONS", "SCHEMATIC") + dialg(200, 250, 140, 72, 0, counter=False)
          + dialg(578, 250, 140, 288, 0, counter=False)
          + arc(200, 250, 165, 4, 66, "#fff", 0.4) + arc(578, 250, 165, -4, -66, OR, 0.6, sweep=0) + f'''
<text class="a" data-t="0.8" x="200" y="460" text-anchor="middle" style="font:700 30px Inter" fill="#fff">→ 20 DIV</text>
<text class="a" data-t="1.0" x="578" y="460" text-anchor="middle" style="font:700 30px Inter" fill="{OR}">← 20, NOT 80</text>
<text class="m a" data-t="1.4" x="389" y="504" text-anchor="middle" style="font-size:22px">+ OR −: CHECK YOUR MODEL (REVERSE TYPES EXIST)</text>''',
      body="Pointer எந்தத் திசையில் நகர்ந்தது என்று பாருங்கள்."),
 dict(s=12.2, e=16.4, tag="CHECK  /  04", title="Before reading", tsize=74, sub="Mitutoyo manual-படி.", ssize=48,
      svg=fig("DIAL INDICATOR CHECKS", "SOURCE: MITUTOYO", orange=True) + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "MASTER ZERO", "Master-ல் zero; counter-ஐயும் படி", 0.2)
          + checkrow(255, 2, "SAME SETUP", "அதே திசை, அதே நிலையில் அள", 0.6)
          + checkrow(395, 3, "READ FROM FRONT", "நேராகப் பார்த்துப் படி", 1.0)),
 dict(s=16.4, e=20.6, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="0.35 அல்ல: 1.35 mm", ssize=50,
      svg=fig("HOW TO ANSWER") + f'''
<g class="a" data-t="0.2"><rect x="40" y="80" width="330" height="140" rx="14" fill="#123A57" stroke="{LINE}" stroke-width="3"/>
<text x="205" y="138" text-anchor="middle" style="font:800 36px Inter" fill="#fff">COUNTER</text>
<text x="205" y="188" text-anchor="middle" style="font:600 28px Inter" fill="#9FC3DD">× 1 mm</text></g>
<g class="a" data-t="0.4"><rect x="408" y="80" width="330" height="140" rx="14" fill="#123A57" stroke="{OR}" stroke-width="3"/>
<text x="573" y="138" text-anchor="middle" style="font:800 36px Inter" fill="{OR}">POINTER</text>
<text x="573" y="188" text-anchor="middle" style="font:600 28px Inter" fill="#9FC3DD">× 0.01 mm</text></g>
<text class="code a" data-t="0.8" x="40" y="300" style="font-size:32px"><tspan fill="{W}">1 + 35 × 0.01 = </tspan><tspan fill="{OR}">1.35 mm</tspan></text>
<text class="m a" data-t="1.1" x="40" y="380" style="font-size:22px">2046S EXAMPLE. mm PER REV IS MODEL-SPECIFIC.</text>''',
      body="Counter, pointer, திசை: மூன்றையும் சொல்லுங்கள்.", body_t=1.3, cta=True, cta_t=1.9),
])

# ---------------- REEL 21: GO / NO-GO plain plug gauge for a hole ----------------
# Hook format: (4) verbatim interview question. Options considered:
#   "Ø20 H7: GO, NO-GO?" (interview question, chosen) / "GO போனது. Hole OK-வா?" (wrong vs right) /
#   "NO-GO உள்ளே போனால்?" (cold-open demo)
# Sources: Organa Metrisis gauges page (GO plug = lower limit of the hole diameter, NO GO = upper limit; GO "must enter
# over the whole specified length while the NO GO plug must not enter"; GO not entering = bore too small or form defect;
# NO GO entering = bore too large; NO GO end "is shorter and often carries a red band");
# Niigata Seiki limit plug gauge (via Sumipol): GO checks the minimum tolerable hole size and should pass, NO-GO checks the
# maximum tolerable size and should not pass; Insize 4124 GO/NO-GO plain plug gauge (DIN 7150-2): GO fits a hole at the
# minimum size. No tolerance values are shown: sizes "as marked on the gauge".

def section(cx, top, bot, hw, t=0.0):
    return (f'<g class="a" data-t="{t}"><rect x="{cx-hw-150}" y="{top}" width="150" height="{bot-top}" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>'
            f'<rect x="{cx+hw}" y="{top}" width="150" height="{bot-top}" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>'
            f'<path d="M{cx-hw-150} {top+24}l24 -24M{cx-hw-150} {top+64}l64 -64M{cx+hw+150} {bot-24}l-24 24M{cx+hw+150} {bot-64}l-64 64" stroke="{LINE}" stroke-width="1.5" opacity=".5"/>'
            f'<text x="{cx-hw-75}" y="{bot-22}" text-anchor="middle" style="font:600 22px Inter" fill="#fff">PART</text></g>')

def plug(cx, bottom, length, w, label, col, band=False):
    top = bottom - length
    b = f'<rect x="{cx-w/2}" y="{top}" width="{w}" height="22" fill="{RED}"/>' if band else ""
    return (f'<rect x="{cx-36}" y="{top-90}" width="72" height="90" rx="8" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>'
            f'<rect x="{cx-w/2}" y="{top}" width="{w}" height="{length}" fill="#D7E3EC" stroke="{LINE}" stroke-width="2"/>{b}'
            f'<text x="{cx}" y="{top + length/2 + 14 + (11 if band else 0)}" text-anchor="middle" style="font:800 {30 if len(label) < 4 else 26}px Inter" fill="{col}">{label}</text>')

R21 = dict(id="21", slug="Go_NoGo_Plug_Gauge", scenes=[
 dict(hook="Ø20 H7: GO, NO-GO?", hsize=78, hook2="Interview கேள்வி: பதில்?", h2size=54, s=0, e=4.2, svg=
      fig("PLAIN PLUG GAUGE · HOLE", "SCHEMATIC", orange=True) + section(389, 380, 620, 60) + f'''
<g class="move" data-t="0" data-d="1.6" data-dy="200">{plug(389, 360, 200, 112, "GO", DARK)}</g>
<text class="a" data-t="1.7" x="614" y="470" style="font:800 30px Inter" fill="{GRN}">GO</text>{tick(724, 460, 1.8)}
<text class="a" data-t="1.9" x="614" y="520" style="font:600 24px Inter" fill="{GRN}">ENTERS</text>
<text class="a" data-t="2.3" x="40" y="690" style="font:800 34px Inter" fill="{OR}">NO-GO END: ?  EACH PROVES WHAT?</text>
<text class="m a" data-t="2.7" x="40" y="738" style="font-size:22px">SIZES: AS MARKED ON THE GAUGE</text>'''),
 dict(s=4.2, e=10.8, tag="ANSWER  /  02", title="GO end", tsize=84, sub="Min limit: நுழையும்", ssize=48,
      svg=fig("GO SIDE", "SCHEMATIC") + section(560, 200, 460, 60) + plug(560, 440, 240, 112, "GO", DARK) + f'''
<text class="a" data-t="0.3" x="40" y="120" style="font:800 36px Inter" fill="{GRN}">GO END</text>
<text class="a" data-t="0.6" x="40" y="180" style="font:700 28px Inter" fill="#fff">= LOWER LIMIT</text>
<text class="a" data-t="0.9" x="40" y="225" style="font:700 28px Inter" fill="#fff">OF THE HOLE</text>
<text class="a" data-t="1.3" x="40" y="300" style="font:700 26px Inter" fill="{GRN}">MUST ENTER</text>
<text class="a" data-t="1.5" x="40" y="340" style="font:700 26px Inter" fill="{GRN}">FULL LENGTH</text>{tick(300, 320, 1.8)}''',
      body="GO முழுதும் நுழைந்தால்: hole சிறியதாக இல்லை."),
 dict(s=10.8, e=17.4, tag="ANSWER  /  03", title="NO-GO end", tsize=84, sub="Max limit: நுழையாது", ssize=48,
      svg=fig("NO-GO SIDE", "SCHEMATIC") + section(560, 290, 500, 60) + plug(560, 288, 110, 124, "NO-GO", DARK, band=True) + f'''
<text class="a" data-t="0.3" x="40" y="120" style="font:800 36px Inter" fill="{RED}">NO-GO END</text>
<text class="a" data-t="0.6" x="40" y="180" style="font:700 28px Inter" fill="#fff">= UPPER LIMIT</text>
<text class="a" data-t="0.9" x="40" y="225" style="font:700 28px Inter" fill="#fff">OF THE HOLE</text>
<text class="a" data-t="1.3" x="40" y="300" style="font:700 26px Inter" fill="{RED}">MUST NOT ENTER</text>{cross(312, 292, 1.6)}
<text class="m a" data-t="2.0" x="40" y="380" style="font-size:22px">OFTEN SHORTER,</text>
<text class="m a" data-t="2.1" x="40" y="414" style="font-size:22px">OFTEN A RED BAND</text>''',
      body="NO-GO நுழையவில்லை: hole பெரியதாக இல்லை."),
 dict(s=17.4, e=24.0, tag="RESULT  /  04", title="Three results", tsize=76, sub="இரண்டு end-ம் தேவை.", ssize=48,
      svg=fig("READ THE RESULT") + f'''
<g class="a" data-t="0.3"><rect x="30" y="70" width="718" height="120" rx="12" fill="#123A57" stroke="{GRN}" stroke-width="3"/>
<text x="56" y="120" style="font:700 28px Inter" fill="#fff">GO enters + NO-GO stops</text>
<text x="56" y="165" style="font:800 30px Inter" fill="{GRN}">WITHIN LIMITS</text></g>{tick(700, 130, 0.6)}
<g class="a" data-t="0.9"><rect x="30" y="210" width="718" height="120" rx="12" fill="#123A57" stroke="{RED}" stroke-width="3"/>
<text x="56" y="260" style="font:700 28px Inter" fill="#fff">GO does not enter</text>
<text x="56" y="305" style="font:800 30px Inter" fill="{RED}">TOO SMALL OR FORM ERROR</text></g>{cross(700, 270, 1.2)}
<g class="a" data-t="1.5"><rect x="30" y="350" width="718" height="120" rx="12" fill="#123A57" stroke="{RED}" stroke-width="3"/>
<text x="56" y="400" style="font:700 28px Inter" fill="#fff">NO-GO enters</text>
<text x="56" y="445" style="font:800 30px Inter" fill="{RED}">TOO LARGE</text></g>{cross(700, 410, 1.8)}''',
      body="Gauge size: gauge-ல் உள்ள marking-படி.", body_t=2.1),
 dict(s=24.0, e=30.6, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="GO = min, NO-GO = max", ssize=50,
      svg=fig("Ø20 H7 HOLE · HOW TO ANSWER") + f'''
<g class="a" data-t="0.3"><rect x="40" y="80" width="330" height="150" rx="14" fill="#123A57" stroke="{GRN}" stroke-width="3"/>
<text x="205" y="138" text-anchor="middle" style="font:800 40px Inter" fill="{GRN}">GO</text>
<text x="205" y="188" text-anchor="middle" style="font:600 26px Inter" fill="#fff">ENTERS: NOT SMALL</text></g>
<g class="a" data-t="0.6"><rect x="408" y="80" width="330" height="150" rx="14" fill="#123A57" stroke="{RED}" stroke-width="3"/>
<text x="573" y="138" text-anchor="middle" style="font:800 40px Inter" fill="{RED}">NO-GO</text>
<text x="573" y="188" text-anchor="middle" style="font:600 26px Inter" fill="#fff">STOPS: NOT LARGE</text></g>
<text class="w a" data-t="1.1" x="40" y="300" style="font-size:30px">"GO போகணும், NO-GO போகக்கூடாது."</text>
<text class="m a" data-t="1.5" x="40" y="370" style="font-size:22px">GAUGE SIZES: AS MARKED ON THE GAUGE.</text>''',
      body="இரண்டும் சரியானால் மட்டுமே hole limits-க்குள்.", body_t=1.8,
      cta=True, cta_t=2.6, cta_icon="send", cta_text=SEND),
])

# ---------------- REEL 22: what Ra 1.6 means ----------------
# Hook format: (2) countdown quiz. Options considered:
#   "Ra 1.6 = ?" with 1.6 mm / 1.6 µm / 16 µm (quiz, chosen) / "Ra 1.6 = 1.6 mm?" (wrong vs right) /
#   "Ra என்றால் என்ன?" (interview question)
# Sources: Mitutoyo "Quick Guide to Surface Roughness Measurement" (Bulletin No. 2229): "Ra - arithmetical mean roughness
# value: The arithmetical mean of the absolute values of the profile deviations (Zi) from the mean line of the roughness
# profile"; evaluation length ln "generally consists of five sampling lengths lr"; "the sampling length corresponds to the
# cut-off wavelength lambda-c"; ISO 4288 table (non-periodic profiles, Ra > 0.1...2 um): lambda-c = lr = 0.8 mm, ln = 4 mm;
# "Ra is hardly affected by individual peaks or valleys because it is the mean value of the whole profile";
# drawing examples state Ra values in um. Mirror-image profiles have identical Ra (same |Z|) but different shapes.

def profile(x0, x1, ym, amp, fn, n=240):
    pts = []
    for i in range(n + 1):
        u = i / n
        pts.append((x0 + (x1 - x0) * u, ym - amp * fn(u)))
    return pts

def p_rough(u):
    return (0.55 * math.sin(2 * math.pi * 9 * u) + 0.3 * math.sin(2 * math.pi * 23 * u + 1.1)
            + 0.18 * math.sin(2 * math.pi * 41 * u + 0.4))

def p_peaks(u):
    f = (u * 8) % 1.0
    return math.exp(-((f - 0.5) / 0.09) ** 2) * 1.6 - 0.28

def pathd(pts):
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)

def area(pts, ym):
    return pathd(pts) + f" L{pts[-1][0]:.1f} {ym} L{pts[0][0]:.1f} {ym} Z"

RA = profile(40, 738, 250, 70, p_rough)
QUIZ_RA = dict(hook="Ra 1.6 = ?", hsize=104, hook2="Unit என்ன? 3 வினாடி!", s=0, e=4.0, svg=f'''
<text class="fig" x="24" y="44">QUICK CHECK · SURFACE ROUGHNESS</text>
<circle class="until" data-end="3.0" cx="389" cy="250" r="140" fill="none" stroke="#2E5878" stroke-width="18"/>
<circle class="draw" data-t="0" data-d="3.0" data-lin="1" data-hide="1" pathLength="1" cx="389" cy="250" r="140" fill="none" stroke="{OR}" stroke-width="18" transform="rotate(-90 389 250)"/>
<text class="count" data-t="0" data-n="3" x="389" y="295" text-anchor="middle" style="font:800 130px Inter" fill="#fff">3</text>
<g style="font:700 46px Inter" fill="#fff">
<rect x="40" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="145" y="551" text-anchor="middle">1.6 mm</text>
<rect x="284" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="389" y="551" text-anchor="middle">1.6 µm</text>
<rect x="528" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="633" y="551" text-anchor="middle">16 µm</text></g>
<text x="389" y="690" text-anchor="middle" style="font:600 30px Inter" fill="#9FC3DD">ANSWER IN THIS REEL</text>''')

def seg_lines():
    out = []
    for k in range(6):
        x = 40 + k * (698 / 5)
        out.append(f'<path d="M{x:.1f} 150V330" stroke="#7FA6C4" stroke-width="2" stroke-dasharray="6 6"/>')
    for k in range(5):
        x = 40 + (k + 0.5) * (698 / 5)
        out.append(f'<text x="{x:.1f}" y="360" text-anchor="middle" style="font:500 24px Plex" fill="#9FC3DD">lr</text>')
    return "".join(out)

PK = profile(40, 738, 175, 55, p_peaks)
VL = profile(40, 738, 375, 55, lambda u: -p_peaks(u))

R22 = dict(id="22", slug="Ra_1p6_Surface_Roughness", scenes=[
 dict(QUIZ_RA),
 dict(s=4.0, e=8.1, tag="ANSWER  /  02", title="Ra 1.6 = 1.6 µm", tsize=74, sub="Arithmetical mean", ssize=50,
      svg=fig("ROUGHNESS PROFILE · EXAGGERATED", "SOURCE: MITUTOYO", orange=True) + f'''
<path class="a" data-t="0.3" d="{area(RA, 250)}" fill="{OR}" fill-opacity=".35"/>
<path class="a" data-t="0" d="{pathd(RA)}" stroke="#fff" stroke-width="3" fill="none"/>
<path class="a" data-t="0.2" d="M40 250H738" stroke="{GRN}" stroke-width="3" stroke-dasharray="12 8"/>
<text class="a" data-t="0.2" x="738" y="150" text-anchor="end" style="font:700 24px Inter" fill="{GRN}">MEAN LINE</text>
<text class="a" data-t="0.7" x="40" y="410" style="font:700 30px Inter" fill="#fff">Ra = MEAN OF |Z| FROM MEAN LINE</text>
<text class="a" data-t="1.1" x="40" y="470" style="font:800 34px Inter" fill="{OR}">UNIT: µm (1.6 µm = 0.0016 mm)</text>''',
      body="மேடு, பள்ளம் இரண்டின் விலகல் சராசரி."),
 dict(s=8.1, e=12.2, tag="LENGTH  /  03", title="Cut-off λc", tsize=80, sub="5 sampling lengths", ssize=50,
      svg=fig("ISO 4288 EXAMPLE · Ra 0.1–2 µm", "SOURCE: MITUTOYO", orange=True) + seg_lines()
          + f'<path class="a" data-t="0" d="{pathd(profile(40, 738, 240, 55, p_rough))}" stroke="#fff" stroke-width="3" fill="none"/>' + f'''
<text class="code a" data-t="0.4" x="40" y="420" style="font-size:30px;fill:#fff">λc = lr = 0.8 mm</text>
<text class="code a" data-t="0.8" x="40" y="465" style="font-size:30px;fill:{OR}">ln = 5 × 0.8 = 4 mm</text>
<text class="m a" data-t="1.2" x="40" y="505" style="font-size:22px">NON-PERIODIC TABLE · DRAWING / STANDARD DECIDES</text>''',
      body="Cut-off, length: drawing அல்லது standard-படி."),
 dict(s=12.2, e=16.3, tag="LIMIT  /  04", title="Same Ra?", tsize=84, sub="வடிவம் வேறு!", ssize=50,
      svg=fig("MIRROR PROFILES · EXAGGERATED", "SCHEMATIC") + f'''
<path class="a" data-t="0" d="M40 175H738M40 375H738" stroke="{GRN}" stroke-width="2" stroke-dasharray="10 8"/>
<path class="a" data-t="0" d="{pathd(PK)}" stroke="#fff" stroke-width="3" fill="none"/>
<text class="a" data-t="0.3" x="40" y="100" style="font:700 26px Inter" fill="#fff">SHARP PEAKS</text>
<path class="a" data-t="0.5" d="{pathd(VL)}" stroke="{OR}" stroke-width="3" fill="none"/>
<text class="a" data-t="0.7" x="40" y="300" style="font:700 26px Inter" fill="{OR}">SHARP VALLEYS</text>
<text class="a" data-t="1.1" x="389" y="490" text-anchor="middle" style="font:800 32px Inter" fill="#fff">SAME Ra, DIFFERENT SURFACE</text>''',
      body="Ra தனியாக முழு surface-ஐயும் சொல்லாது."),
 dict(s=16.3, e=20.6, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="Ra 1.6 = 1.6 µm", ssize=50,
      svg=fig("HOW TO ANSWER") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "UNIT µm", "Ra 1.6 = 1.6 µm", 0.2)
          + checkrow(255, 2, "MEAN OF |Z|", "Mean line-இலிருந்து சராசரி", 0.5)
          + checkrow(395, 3, "READ THE DRAWING", "Cut-off, மற்ற parameter", 0.8),
      cta=True, cta_t=1.4),
])

# ---------------- REEL 23: height gauge on a surface plate ----------------
# Hook format: (1) cold-open demo (the mistake: not zeroing on the plate). Options considered:
#   "Plate-ல் 0.30 mm!" (demo, chosen) / "25.30 or 25.00?" (wrong vs right) / "Height gauge zero எங்கே?" (interview q.)
# Sources: Mitutoyo Quick Guide to Measurement (PG 25-26, Height Gages): make sure the surface plate and the height gage
# base reference surface are free of dust or burrs; the base may lift from the surface plate if excessive downward force is
# used on the slider - move the slider slowly; lock the slider and confirm the setting after clamping; "if the main scale
# of the height gage can be moved, move it as required to set the zero point"; look straight at the graduations (parallax).
# Mitutoyo Series 514 height gage leaflet: main scale "slides and clamps within the column for quick and convenient
# zero-setting"; minimum reading 0.02 mm. Values 0.30 / 25.30 / 25.00 are illustrative (multiples of 0.02 mm).
# "Same reference" panel is plain geometry: a reading from the plate includes anything the part stands on.

def hgauge(gx, sy, col_top=110, plate_y=640, inner=None):
    """gx = base left x; sy = scriber bottom y. inner wraps the slider in nested .move groups (list of attr strings)."""
    slider = (f'<rect x="{gx+44}" y="{sy-78}" width="62" height="64" rx="6" fill="#9FB7C9" stroke="{LINE}" stroke-width="2"/>'
              f'<rect x="{gx+106}" y="{sy-16}" width="150" height="16" fill="#D7E3EC" stroke="{LINE}" stroke-width="2"/>'
              f'<path d="M{gx+256} {sy-16}l14 16h-14z" fill="{OR}"/>')
    if inner:
        for a in reversed(inner):
            slider = f'<g class="move" {a}>{slider}</g>'
    return (f'<rect x="{gx}" y="{plate_y-40}" width="170" height="40" rx="6" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>'
            f'<rect x="{gx+60}" y="{col_top}" width="30" height="{plate_y-40-col_top}" fill="#B8CCDB" stroke="{LINE}" stroke-width="2"/>'
            + slider)

def plate(y, h=56):
    return (f'<rect x="20" y="{y}" width="738" height="{h}" fill="#3E6F96" stroke="{LINE}" stroke-width="2.5"/>'
            f'<text x="738" y="{y+36}" text-anchor="end" style="font:600 22px Inter" fill="#fff">SURFACE PLATE</text>')

def readout(x, y, w, val_svg):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="120" rx="12" fill="#0A2236" stroke="#2E5878" stroke-width="2"/>'
            f'<text class="m" x="{x+20}" y="{y+36}" style="font-size:22px">READING</text>{val_svg}')

R23 = dict(id="23", slug="Height_Gauge_Zero_on_Plate", scenes=[
 dict(hook="Plate-ல் 0.30 mm!", hsize=88, hook2="அப்போ 25.30 சரியா?", s=0, e=4.4, flash_t=2.9, svg=
      fig("HEIGHT GAUGE · SCHEMATIC", "EXAMPLE VALUES", orange=True) + plate(640) + f'''
<rect x="420" y="440" width="200" height="200" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<text x="520" y="548" text-anchor="middle" style="font:700 26px Inter" fill="#fff">PART</text>
<g class="move" data-t="1.8" data-d="0.6" data-dx="180">{hgauge(40, 380, inner=['data-t="0" data-d="1.1" data-dy="260"', 'data-t="1.3" data-d="0.5" data-dy="-240"', 'data-t="2.4" data-d="0.3" data-dy="20"'])}</g>
{readout(470, 70, 268, f'<g class="until" data-end="2.7"><text class="a" data-t="1.1" x="718" y="160" text-anchor="end" style="font:800 52px Inter" fill="{RED}">0.30</text></g><text class="a" data-t="2.75" x="718" y="160" text-anchor="end" style="font:800 52px Inter" fill="{RED}">25.30</text>')}
<g class="until" data-end="2.7"><text class="a" data-t="1.15" x="470" y="240" style="font:700 24px Inter" fill="{RED}">ON PLATE: NOT 0.00</text></g>
<text class="a" data-t="2.75" x="470" y="240" style="font:700 24px Inter" fill="{RED}">ON PART: +0.30 ERROR</text>
<text class="a" data-t="3.0" x="40" y="740" style="font:800 30px Inter" fill="{RED}">NOT ZEROED → EVERY HEIGHT +0.30</text>'''),
 dict(s=4.4, e=11.0, tag="ANSWER  /  02", title="Zero on the plate", tsize=72, sub="பிறகு part: 25.00 mm", ssize=50,
      svg=fig("SAME PLATE, ZERO FIRST", "SCHEMATIC") + plate(440, 50) + f'''
<rect x="440" y="240" width="200" height="200" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<text x="540" y="350" text-anchor="middle" style="font:700 26px Inter" fill="#fff">PART</text>
{hgauge(260, 240, col_top=70, plate_y=440)}
<g class="a" data-t="0.3"><text x="40" y="110" style="font:700 26px Inter" fill="#fff">1 ON PLATE</text>
<text x="40" y="150" style="font:800 36px Inter" fill="{GRN}">0.00</text></g>{tick(180, 138, 0.6)}
<g class="a" data-t="1.0"><text x="40" y="240" style="font:700 26px Inter" fill="#fff">2 ON PART</text>
<text x="40" y="280" style="font:800 36px Inter" fill="{OR}">25.00</text></g>''',
      body="Scriber-ஐ plate-ல் தொட்டு zero; பிறகு அதே plate-இலிருந்து அளவு."),
 dict(s=11.0, e=17.6, tag="CHECK  /  03", title="Before zeroing", tsize=74, sub="மூன்று சோதனைகள்.",
      svg=fig("HEIGHT GAUGE CHECKS", "SOURCE: MITUTOYO", orange=True) + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "CLEAN PLATE + BASE", "தூசி, burr இல்லாமல்", 0.3)
          + checkrow(255, 2, "LOWER GENTLY", "அதிக force: base தூக்கும்", 0.8)
          + checkrow(395, 3, "LOCK + RECHECK", "Clamp செய்த பின் மீண்டும் பார்", 1.3),
      body="Zero முறை model-ஐப் பொறுத்தது; manual-ஐப் பாருங்கள்.", body_t=1.8),
 dict(s=17.6, e=24.2, tag="REFERENCE  /  04", title="Same reference", tsize=74, sub="Zero எங்கே? அளவும் அங்கே.", ssize=48,
      svg=fig("PART ON A PARALLEL", "EXAMPLE VALUES", orange=True) + plate(440, 50) + f'''
<rect x="440" y="360" width="220" height="80" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<text x="550" y="410" text-anchor="middle" style="font:600 22px Inter" fill="#fff">PARALLEL 10.00</text>
<rect x="450" y="160" width="200" height="200" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<text x="550" y="270" text-anchor="middle" style="font:700 26px Inter" fill="#fff">PART 25.00</text>
{hgauge(240, 160, col_top=70, plate_y=440)}
<text class="a" data-t="0.4" x="40" y="120" style="font:700 26px Inter" fill="#fff">READS</text>
<text class="a" data-t="0.6" x="40" y="165" style="font:800 40px Inter" fill="{OR}">35.00</text>
<text class="a" data-t="1.1" x="40" y="250" style="font:700 22px Inter" fill="#9FC3DD">= PART</text>
<text class="a" data-t="1.3" x="40" y="285" style="font:700 22px Inter" fill="#9FC3DD">+ PARALLEL</text>''',
      body="Reading எந்த surface-இலிருந்து என்று தெரிந்து சொல்லுங்கள்."),
 dict(s=24.2, e=30.8, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="0.30 அல்ல: plate-ல் 0.00", ssize=48,
      svg=fig("HOW TO ANSWER") + f'''
<g class="a" data-t="0.3"><rect x="30" y="80" width="220" height="120" rx="14" fill="#123A57" stroke="{LINE}" stroke-width="3"/>
<text x="140" y="152" text-anchor="middle" style="font:800 32px Inter" fill="#fff">CLEAN</text></g>
<g class="a" data-t="0.6"><rect x="279" y="80" width="220" height="120" rx="14" fill="#123A57" stroke="{GRN}" stroke-width="3"/>
<text x="389" y="132" text-anchor="middle" style="font:800 30px Inter" fill="{GRN}">ZERO ON</text>
<text x="389" y="172" text-anchor="middle" style="font:800 30px Inter" fill="{GRN}">PLATE</text></g>
<g class="a" data-t="0.9"><rect x="528" y="80" width="220" height="120" rx="14" fill="#123A57" stroke="{OR}" stroke-width="3"/>
<text x="638" y="152" text-anchor="middle" style="font:800 32px Inter" fill="{OR}">MEASURE</text></g>
<text class="w a" data-t="1.3" x="40" y="290" style="font-size:30px">"Plate-ல் zero, அதே plate-இலிருந்து அளவு."</text>
<text class="m a" data-t="1.7" x="40" y="360" style="font-size:22px">LOOK STRAIGHT AT THE SCALE. ZERO METHOD:</text>
<text class="m a" data-t="1.8" x="40" y="392" style="font-size:22px">MODEL-SPECIFIC. CHECK YOUR MANUAL.</text>''',
      body="நீங்கள் zero செய்யும் முறையைச் சொல்லுங்கள்.", body_t=2.0, cta=True, cta_t=2.6),
])

REELS = [R19, R20, R21, R22, R23]
