from gen import *
W = "#E6F0F7"
SEND = "நண்பருக்கு அனுப்புங்கள்."
DIM = "#7FA6C4"


def box(x, y, w, h, stroke=LINE, t=None, fill="#123A57", sw=3, rx=14):
    r = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    return f'<g class="a" data-t="{t}">{r}' if t is not None else r


def txt(x, y, s, size=30, col="#fff", w=700, anchor="start", t=None, font="Inter"):
    a = f' class="a" data-t="{t}"' if t is not None else ""
    return f'<text{a} x="{x}" y="{y}" text-anchor="{anchor}" style="font:{w} {size}px {font},NTamil" fill="{col}">{esc(s)}</text>'


def seq(x, y, vals, size=40, col="#fff", anchor="middle", font="Inter"):
    """Readings that replace each other: vals = [(text, t_from, t_to, colour)]."""
    out = []
    for s, a, b, c in vals:
        out.append(f'<g class="a" data-t="{a}"><text class="until" data-end="{b}" x="{x}" y="{y}" text-anchor="{anchor}" '
                   f'style="font:800 {size}px {font}" fill="{c}">{esc(s)}</text></g>')
    return "".join(out)


# =====================================================================================
# REEL 29: H7 in plain words (ISO 286 hole-basis)
# Hook format: (4) verbatim interview question.
# Options: "Ø10 H7 என்றால்?" (interview question, chosen: specific size + code, answered in scene 2/3)
#          "H7 = ±0.007 mm?" (wrong vs right) / "Hole H7, shaft h7 – ஒன்றா?" (quiz)
# Sources: Roymech "How to use ISO tolerances" (upper case = holes, lower case = shafts; for an H hole the lower
# deviation EI is on the zero line, so min hole = basic size; the number is the IT grade = width of the zone;
# hole-basis: hole uses H, fit chosen by changing the shaft tolerance).
# Roymech ISO 286-2 hole limits table and CADforum ISO 286-2 table: H7, over 6 inc. 10 mm = +15 / 0 µm;
# over 10 inc. 18 mm = +18 / 0 µm. ISO 286-2:2010 (iso.org/standard/54915) is the table standard.
# => Ø10 H7 = 10.000 to 10.015 mm; Ø12 H7 = 12.000 to 12.018 mm.
# =====================================================================================

H7_HOOK = dict(hook="Ø10 H7 என்றால்?", hsize=86, hook2="Interview-ல் கேட்பார்கள்.", h2size=56, s=0, e=4.0, svg=f'''
<text class="fig" x="24" y="44">INTERVIEW QUESTION</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">DRAWING CALLOUT</text>
<rect x="30" y="74" width="718" height="96" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="2"/>
<path d="M90 170l-10 34 40-34z" fill="#123A57" stroke="{LINE}" stroke-width="2"/><path d="M83 168h36" stroke="#123A57" stroke-width="5"/>
<text x="389" y="136" text-anchor="middle" style="font:700 36px Inter" fill="#fff">“What does Ø10 H7 mean?”</text>
<rect x="60" y="250" width="420" height="380" rx="8" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<text x="80" y="290" style="font:600 22px Inter" fill="#fff">PART · TOP VIEW</text>
<circle class="draw" data-t="0" data-d="1.0" pathLength="1" cx="270" cy="440" r="110" fill="{PANEL}" stroke="#fff" stroke-width="4"/>
<path d="M150 440H390" stroke="{DIM}" stroke-width="2" stroke-dasharray="8 6"/>
<path class="draw" data-t="0.6" data-d="0.6" pathLength="1" d="M348 362L520 300H600" fill="none" stroke="{OR}" stroke-width="3"/>
<g class="a" data-t="0.9"><rect x="520" y="240" width="210" height="96" rx="12" fill="#0A2236" stroke="{OR}" stroke-width="3"/>
<text x="625" y="304" text-anchor="middle" style="font:800 44px Inter" fill="{OR}">Ø10 H7</text></g>
<g class="a" data-t="1.6"><text x="560" y="410" style="font:800 40px Inter" fill="#fff">H = ?</text></g>
<g class="a" data-t="2.1"><text x="560" y="480" style="font:800 40px Inter" fill="#fff">7 = ?</text></g>
<text class="a" data-t="2.6" x="389" y="700" text-anchor="middle" style="font:600 30px Inter" fill="#9FC3DD">ANSWER IN THIS REEL</text>''')


def zone_example():
    # zero line = nominal 10.000; H7 zone 0 to +15 µm, drawn tall (exaggerated)
    return f'''
<g class="a" data-t="0.2"><rect x="30" y="64" width="718" height="64" rx="10" fill="#0A2236" stroke="#2E5878" stroke-width="2"/>
<text x="50" y="106" style="font:500 26px Plex" fill="{W}">H7 · OVER 6 INC. 10 mm → </text><text x="508" y="106" style="font:600 26px Plex" fill="{OR}">+15 / 0 µm</text></g>
<path class="a" data-t="0.6" d="M40 400H738" stroke="#fff" stroke-width="3"/>
<text class="a" data-t="0.6" x="40" y="440" style="font:600 24px Plex" fill="#BFD6E8">ZERO LINE = NOMINAL Ø10</text>
<rect class="grow a" data-t="0.9" data-d="0.8" data-w="300" x="80" y="230" width="0" height="170" fill="{OR}" opacity="0.85"/>
<text class="a" data-t="1.3" x="230" y="325" text-anchor="middle" style="font:800 40px Inter" fill="{PANEL}">H7 ZONE</text>
<path class="a" data-t="1.6" d="M380 230H420M380 400H420" stroke="{DIM}" stroke-width="2"/>
<text class="a" data-t="1.6" x="430" y="242" style="font:700 30px Inter" fill="{GRN}">MAX 10.015 mm</text>
<text class="a" data-t="2.0" x="430" y="392" style="font:700 30px Inter" fill="{GRN}">MIN 10.000 mm</text>
<text class="a" data-t="2.2" x="430" y="300" style="font:600 24px Plex" fill="#9FC3DD">+0.015</text>
<text class="a" data-t="2.2" x="430" y="350" style="font:600 24px Plex" fill="#9FC3DD">LOWER DEV. 0</text>
<text class="a" data-t="2.4" x="40" y="495" style="font:500 22px Plex" fill="{OR}">ZONE HEIGHT EXAGGERATED FOR VISIBILITY</text>'''


def fits():
    y0 = 330
    return f'''
<path d="M40 {y0}H738" stroke="#fff" stroke-width="3"/>
<text x="40" y="{y0+40}" style="font:600 22px Plex" fill="#BFD6E8">ZERO LINE</text>
<g class="a" data-t="0.2"><rect x="60" y="{y0-90}" width="150" height="90" fill="{OR}" opacity="0.9"/>
<text x="135" y="{y0-36}" text-anchor="middle" style="font:800 32px Inter" fill="{PANEL}">HOLE H</text></g>
<g class="a" data-t="0.8"><rect x="250" y="{y0+20}" width="140" height="60" fill="{GRN}"/>
<text x="320" y="{y0+130}" text-anchor="middle" style="font:700 22px Inter" fill="{GRN}">CLEARANCE</text></g>
<g class="a" data-t="1.2"><rect x="420" y="{y0-60}" width="140" height="100" fill="#6FB3E8"/>
<text x="490" y="{y0+80}" text-anchor="middle" style="font:700 22px Inter" fill="#6FB3E8">TRANSITION</text></g>
<g class="a" data-t="1.6"><rect x="590" y="{y0-190}" width="140" height="80" fill="{RED}"/>
<text x="660" y="{y0-80}" text-anchor="middle" style="font:700 22px Inter" fill="{RED}">INTERFERENCE</text></g>
<text class="a" data-t="0.6" x="490" y="100" text-anchor="middle" style="font:700 26px Inter" fill="#fff">SHAFT ZONES (EXAMPLES)</text>
<text class="a" data-t="2.0" x="40" y="490" style="font:500 22px Plex" fill="#9FC3DD">SCHEMATIC · NOT TO SCALE</text>'''


R29 = dict(id="29", slug="H7_Hole_Tolerance_Plain_Words", scenes=[
 H7_HOOK,
 dict(s=4.0, e=10.5, tag="ANSWER  /  02", title="H7 = hole tolerance", tsize=70, sub="ISO 286 code", ssize=50,
      svg=fig("ISO 286 · LIMITS AND FITS", "SOURCE: ISO 286", orange=True) + f'''
{box(40, 72, 160, 150, OR, 0.2)}<text x="120" y="172" text-anchor="middle" style="font:800 84px Inter" fill="{OR}">H</text></g>
{txt(230, 128, "CAPITAL LETTER = HOLE", 30, "#fff", 700, t=0.5)}
{txt(230, 176, "H: LOWER DEVIATION = 0", 30, GRN, 700, t=0.9)}
{box(40, 258, 160, 150, LINE, 1.3)}<text x="120" y="358" text-anchor="middle" style="font:800 84px Inter" fill="#fff">7</text></g>
{txt(230, 314, "IT TOLERANCE GRADE", 30, "#fff", 700, t=1.6)}
{txt(230, 362, "= WIDTH OF THE ZONE", 30, GRN, 700, t=1.9)}
<text class="m a" data-t="2.3" x="40" y="470" style="font-size:22px">LOWER CASE (e.g. h7) = SHAFT</text>''',
      body="H: hole nominal-ஐ விடச் சிறியதாகாது. 7: அனுமதி அளவின் grade."),
 dict(s=10.5, e=17.0, tag="EXAMPLE  /  03", title="Ø10 H7 limits", tsize=74, sub="10.000 – 10.015 mm", ssize=50,
      svg=fig("ISO 286-2 TABLE", "Ø10 · HOLE", orange=True) + zone_example(),
      body="Limits size-ஐப் பொறுத்தது: Ø12 H7 = +0.018 / 0. Table பாருங்கள்."),
 dict(s=17.0, e=23.5, tag="SYSTEM  /  04", title="Hole-basis system", tsize=70, sub="Hole H, shaft மாறும்", ssize=48,
      svg=fig("HOLE-BASIS FITS", "SCHEMATIC", orange=True) + fits(),
      body="Hole-ஐ H-ஆக வைத்து, shaft tolerance மாற்றி fit தேர்வு செய்வார்கள்."),
 dict(s=23.5, e=30.0, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="Ø10 H7 = 10.000–10.015", ssize=46,
      svg=fig("HOW TO ANSWER") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "H = HOLE, LOWER DEV. 0", "குறைந்த அளவு = nominal", 0.3)
          + checkrow(255, 2, "7 = IT GRADE", "Zone அகலம் grade-ஐப் பொறுத்தது", 0.8)
          + checkrow(395, 3, "LIMITS: ISO 286 TABLE", "Size-க்கு ஏற்ற row-ஐப் படியுங்கள்", 1.3),
      body="மனப்பாடம் வேண்டாம்; table-ஐப் படிக்கத் தெரியணும்.", body_t=1.8, cta=True, cta_t=2.6),
])


# =====================================================================================
# REEL 30: What "M10 × 1.5" means
# Hook format: (2) countdown quiz.
# Options: "M10 × 1.5: 1.5 என்ன?" (quiz, chosen) / "M10 = 10 mm drill?" (wrong vs right) /
#          "M10 × 1.5 விளக்குங்கள்." (interview question)
# Sources: ISO 261:1998 (iteh.ai sample, Table 2): nominal Ø10 coarse pitch 1.5 mm; fine pitches 1.25, 1, 0.75 mm.
# Wikipedia "ISO metric screw thread" (cites ISO 261/262/724/965-1): M + nominal (major) diameter in mm, × pitch in mm;
# coarse pitch is the default and "can be omitted"; fine pitch is written. EngineeringToolbox ISO 724 table:
# M10 coarse 1.5; fine M10 × 1.25.
# =====================================================================================

M10_HOOK = dict(hook="M10 × 1.5: 1.5 என்ன?", hsize=74, hook2="3 வினாடியில் பதில்?", s=0, e=3.6, svg=f'''
<text class="fig" x="24" y="44">QUICK CHECK · ISO METRIC THREAD</text>
<circle class="until" data-end="3.0" cx="389" cy="250" r="140" fill="none" stroke="#2E5878" stroke-width="18"/>
<circle class="draw" data-t="0" data-d="3.0" data-lin="1" data-hide="1" pathLength="1" cx="389" cy="250" r="140" fill="none" stroke="{OR}" stroke-width="18" transform="rotate(-90 389 250)"/>
<text class="count" data-t="0" data-n="3" x="389" y="295" text-anchor="middle" style="font:800 130px Inter" fill="#fff">3</text>
<g style="font:700 40px Inter" fill="#fff">
<rect x="40" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="145" y="548" text-anchor="middle">PITCH</text>
<rect x="284" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="389" y="548" text-anchor="middle">DEPTH</text>
<rect x="528" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="633" y="548" text-anchor="middle">TPI</text></g>
<text x="389" y="690" text-anchor="middle" style="font:600 30px Inter" fill="#9FC3DD">ANSWER IN THIS REEL</text>''')


def thread_side(t=0.2):
    # schematic external thread, side view: crest lines y=150 / 410, pitch drawn 120 px
    P = 120; h = 52
    top = "M60 150" + "".join(f"l{P/2:.0f} {h}l{P/2:.0f} -{h}" for _ in range(5))
    bot = f"M60 {410-h}" + "".join(f"l{P/2:.0f} {h}l{P/2:.0f} -{h}" for _ in range(5))
    return f'''<g class="a" data-t="{t}">
<rect x="60" y="150" width="600" height="260" fill="{STEEL}" opacity="0.5"/>
<path d="{top}" fill="none" stroke="#fff" stroke-width="4"/><path d="{bot}" fill="none" stroke="#fff" stroke-width="4"/></g>
<g class="a" data-t="0.7"><path d="M180 130V95M300 130V95" stroke="{OR}" stroke-width="2"/>
<path d="M186 104H294" stroke="{OR}" stroke-width="3" marker-start="url(#ao)" marker-end="url(#ao)"/>
<text x="240" y="84" text-anchor="middle" style="font:700 30px Inter" fill="{OR}">P = 1.5 mm</text></g>
<g class="a" data-t="1.3"><path d="M680 150H730M680 410H730" stroke="{GRN}" stroke-width="2"/>
<path d="M710 158V402" stroke="{GRN}" stroke-width="3"/><path d="M710 150l-9 18h18zM710 410l-9 -18h18z" fill="{GRN}"/></g>
<text class="a" data-t="1.3" x="460" y="470" text-anchor="middle" style="font:700 30px Inter" fill="{GRN}">MAJOR Ø = 10 mm</text>
<text class="a" data-t="1.6" x="40" y="500" style="font:500 22px Plex" fill="#9FC3DD">SCHEMATIC · NOT TO SCALE</text>'''


R30 = dict(id="30", slug="M10x1p5_Thread_Meaning", scenes=[
 M10_HOOK,
 dict(s=3.6, e=7.7, tag="ANSWER  /  02", title="1.5 = pitch (mm)", tsize=74, sub="M = ISO metric", ssize=50,
      svg=fig("M10 × 1.5 · SIDE VIEW", "ISO 261", orange=True) + thread_side(),
      body="10 = major Ø (mm). 1.5 mm = ஒரு crest-லிருந்து அடுத்த crest.", body_t=0.4),
 dict(s=7.7, e=11.8, tag="COARSE  /  03", title="Coarse vs fine", tsize=74, sub="Fine pitch எழுதப்படும்", ssize=48,
      svg=fig("ISO METRIC DESIGNATION") + f'''
{box(40, 80, 698, 150, GRN, 0.2)}
<text x="70" y="148" style="font:800 46px Inter" fill="#fff">M10 × 1.5</text>
<text x="70" y="200" style="font:600 26px Inter" fill="{GRN}">COARSE PITCH (ISO 261 DEFAULT)</text></g>
{box(40, 270, 698, 150, OR, 0.9)}
<text x="70" y="338" style="font:800 46px Inter" fill="#fff">M10 × 1.25</text>
<text x="70" y="390" style="font:600 26px Inter" fill="{OR}">FINE PITCH – ALWAYS WRITTEN</text></g>
<text class="m a" data-t="1.4" x="40" y="480" style="font-size:22px">COARSE PITCH MAY BE LEFT OFF: "M10"</text>''',
      body="Pitch இல்லாத M10 = coarse 1.5.", body_t=0.4),
 dict(s=11.8, e=15.9, tag="TABLE  /  04", title="M10 pitches", tsize=76, sub="ISO 261", ssize=50,
      svg=fig("NOMINAL Ø10 · ISO 261", "PITCH mm", orange=True) + f'''
{box(40, 80, 698, 90, GRN, 0.2)}{txt(70, 140, "COARSE", 34, "#fff")}{txt(708, 140, "1.5", 40, GRN, 800, "end")}</g>
{box(40, 200, 698, 90, LINE, 0.6)}{txt(70, 260, "FINE", 34, "#fff")}{txt(708, 260, "1.25 · 1 · 0.75", 40, OR, 800, "end")}</g>
<text class="m a" data-t="1.0" x="40" y="360" style="font-size:22px">SAME Ø10, DIFFERENT PITCH = DIFFERENT THREAD</text>
<text class="m a" data-t="1.3" x="40" y="400" style="font-size:22px">MATCH TAP AND GAUGE TO THE DRAWING</text>''',
      body="Tap marking-ஐ drawing-உடன் ஒப்பிடுங்கள்.", body_t=0.4),
 dict(s=15.9, e=20.0, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="M10 × 1.5 = Ø10, P 1.5", ssize=48,
      svg=fig("HOW TO ANSWER") + f'''
{box(40, 80, 330, 170, OR, 0.2)}<text x="205" y="160" text-anchor="middle" style="font:800 56px Inter" fill="{OR}">M10</text>
<text x="205" y="215" text-anchor="middle" style="font:600 26px Inter" fill="#fff">MAJOR Ø 10 mm</text></g>
{box(408, 80, 330, 170, GRN, 0.5)}<text x="573" y="160" text-anchor="middle" style="font:800 56px Inter" fill="{GRN}">× 1.5</text>
<text x="573" y="215" text-anchor="middle" style="font:600 26px Inter" fill="#fff">PITCH 1.5 mm</text></g>
<text class="w a" data-t="0.9" x="40" y="330" style="font-size:30px">Coarse = default · fine = written</text>''',
      body="M, Ø, pitch – மூன்றையும் சொல்லுங்கள்.", body_t=0.5, cta=True, cta_t=1.6),
])


# =====================================================================================
# REEL 31: Tap drill size for a cut tap
# Hook format: (3) wrong vs right.
# Options: "M10 tap: Ø10 drill?" (wrong first, chosen) / "M10 tap drill = ?" (quiz) /
#          "Tap drill size எப்படிக் கணக்கிடுவீர்கள்?" (interview)
# Sources: Dormer Pramet (tap maker) "Which size should I pre-drill?": for cutting taps "the nominal size of the screw
# thread must be reduced with the pitch" (M6 × 1 -> 6 - 1 = 5 mm); "When manufacturing threads using a forming tap,
# larger pre-drilling is required" (use their tables). M10 × 1.5: 10 - 1.5 = 8.5 mm (arithmetic from the rule).
# EngineeringToolbox ISO 724 table lists M10 × 1.25 tap drill 8.80 (consistent with D - P).
# =====================================================================================

TAP_HOOK = dict(hook="M10 tap: Ø10 drill?", hsize=88, hook2="தவறு! சரியான size?", s=0, e=4.2, flash_t=1.5, svg=f'''
<text class="fig" x="24" y="44">SECTION · SCHEMATIC</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">CUT TAP · M10 × 1.5</text>
<rect x="60" y="400" width="300" height="300" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="418" y="400" width="300" height="300" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<g class="move" data-t="0" data-d="1.4" data-dy="220"><rect x="150" y="90" width="120" height="250" fill="#C9D6E0" stroke="#fff" stroke-width="2"/>
<path d="M150 340L210 380L270 340z" fill="#C9D6E0" stroke="#fff" stroke-width="2"/>
</g>
<text x="210" y="670" text-anchor="middle" style="font:800 44px Inter" fill="{RED}">Ø10</text>
<g class="a" data-t="1.5"><circle cx="210" cy="300" r="50" fill="{RED}"/><path d="M188 278l44 44M232 278l-44 44" stroke="{PANEL}" stroke-width="9"/></g>
<g class="move" data-t="1.9" data-d="1.2" data-dy="220"><rect x="525" y="90" width="86" height="250" fill="#C9D6E0" stroke="#fff" stroke-width="2"/>
<path d="M525 340L568 370L611 340z" fill="#C9D6E0" stroke="#fff" stroke-width="2"/>
</g>
<text class="a" data-t="1.9" x="568" y="670" text-anchor="middle" style="font:800 44px Inter" fill="{GRN}">Ø8.5</text>
<g class="a" data-t="3.1"><circle cx="568" cy="300" r="50" fill="{GRN}"/><path d="M546 300l16 18 30-34" stroke="{PANEL}" stroke-width="9" fill="none"/></g>''')


def tapped(cx, top, d_px, tooth, t, ok):
    """Section of a drilled hole; ok=True adds thread teeth cut into the wall (schematic)."""
    w = 260; x0 = cx - w // 2
    hl = cx - d_px // 2; hr = cx + d_px // 2
    out = [f'<g class="a" data-t="{t}"><rect x="{x0}" y="{top}" width="{w}" height="300" fill="{STEEL}" stroke="{LINE}" stroke-width="2"/>',
           f'<rect x="{hl}" y="{top}" width="{d_px}" height="300" fill="{PANEL}"/>']
    if ok:
        zl = f"M{hl} {top}" + "".join(f"l-{tooth} 15l{tooth} 15" for _ in range(10))
        zr = f"M{hr} {top}" + "".join(f"l{tooth} 15l-{tooth} 15" for _ in range(10))
        out.append(f'<path d="{zl}" fill="none" stroke="{GRN}" stroke-width="3"/><path d="{zr}" fill="none" stroke="{GRN}" stroke-width="3"/>')
    out.append("</g>")
    return "".join(out)


R31 = dict(id="31", slug="Tap_Drill_Size_Cut_Tap", scenes=[
 TAP_HOOK,
 dict(s=4.2, e=10.6, tag="RULE  /  02", title="Drill = D − P", tsize=80, sub="Cut tap-க்கு பொது விதி", ssize=48,
      svg=fig("CUT TAP · METRIC COARSE", "SOURCE: TAP MAKER", orange=True) + f'''
<text class="code a" data-t="0.2" x="40" y="110" style="font-size:32px"><tspan fill="{W}">D = nominal Ø   = 10 mm</tspan></text>
<text class="code a" data-t="0.6" x="40" y="170" style="font-size:32px"><tspan fill="{W}">P = pitch       = 1.5 mm</tspan></text>
<text class="code a" data-t="1.0" x="40" y="250" style="font-size:36px"><tspan fill="{W}">10 − 1.5 = </tspan><tspan fill="{OR}">8.5 mm</tspan></text>
<g class="a" data-t="1.5"><rect x="40" y="320" width="698" height="120" rx="18" fill="#123A57" stroke="{OR}" stroke-width="4"/>
<text x="389" y="400" text-anchor="middle" style="font:800 52px Inter" fill="{OR}">M10 × 1.5 → Ø8.5</text></g>''',
      body="Nominal Ø-லிருந்து pitch-ஐக் கழியுங்கள். M10 × 1.5 → Ø8.5 mm."),
 dict(s=10.6, e=17.0, tag="WHY  /  03", title="Why not Ø10?", tsize=78, sub="Thread-க்கு material வேண்டும்", ssize=46,
      svg=fig("SECTION · SCHEMATIC", "NOT TO SCALE", orange=True)
          + tapped(205, 110, 120, 22, 0.2, True) + tapped(573, 110, 160, 0, 0.8, False) + f'''
{txt(205, 455, "Ø8.5 → THREAD CUT", 26, GRN, 700, "middle", 0.5)}
{txt(573, 455, "Ø10 → NOTHING TO CUT", 26, RED, 700, "middle", 1.1)}
{tick(205, 70, 0.5)}{cross(573, 70, 1.1)}''',
      body="Tap, drill hole-ன் சுவரில் thread வெட்டும். Ø10 hole-ல் அந்த material இல்லை."),
 dict(s=17.0, e=23.6, tag="CHECK  /  04", title="Forming tap?", tsize=80, sub="Drill size வேறு!", ssize=50,
      svg=fig("TAP TYPE DECIDES THE DRILL") + f'''
{box(40, 80, 330, 330, GRN, 0.2)}
<text x="205" y="150" text-anchor="middle" style="font:800 38px Inter" fill="#fff">CUT TAP</text>
<text x="205" y="230" text-anchor="middle" style="font:700 36px Inter" fill="{GRN}">D − P</text>
<text x="205" y="300" text-anchor="middle" style="font:800 44px Inter" fill="{GRN}">Ø8.5</text>
<text x="205" y="360" text-anchor="middle" style="font:600 22px Inter" fill="#BFD6E8">M10 × 1.5</text></g>
{box(408, 80, 330, 330, OR, 0.9)}
<text x="573" y="150" text-anchor="middle" style="font:800 38px Inter" fill="#fff">FORMING TAP</text>
<text x="573" y="230" text-anchor="middle" style="font:700 36px Inter" fill="{OR}">LARGER DRILL</text>
<text x="573" y="300" text-anchor="middle" style="font:700 30px Inter" fill="{OR}">TAP MAKER</text>
<text x="573" y="340" text-anchor="middle" style="font:700 30px Inter" fill="{OR}">CHART</text></g>
<text class="m a" data-t="1.5" x="40" y="470" style="font-size:22px">FORMING TAPS PUSH MATERIAL, THEY DON'T CUT IT</text>''',
      body="Forming tap-க்கு drill பெரியது. Tap maker chart-ஐப் பாருங்கள்."),
 dict(s=23.6, e=30.0, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="M10 × 1.5 → Ø8.5", ssize=50,
      svg=fig("HOW TO ANSWER") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "CUT TAP: D − P", "10 − 1.5 = 8.5 mm", 0.3)
          + checkrow(255, 2, "Ø10 = NO THREAD", "Hole nominal Ø அல்ல", 0.8)
          + checkrow(395, 3, "FORMING TAP: CHART", "Tap maker chart-ஐப் பாருங்கள்", 1.3),
      body="Tap type-ஐ முதலில் உறுதி செய்யுங்கள்.", body_t=1.8, cta=True, cta_t=2.6, cta_icon="send", cta_text=SEND),
])


# =====================================================================================
# REEL 32: Tramming (aligning) a vise with a dial indicator
# Hook format: (1) cold-open demo (watch the reading change along the jaw).
# Options: "Sweep: 0 → 0.04 mm" (demo, chosen: a specific example reading, motion from frame 1) /
#          "Movable jaw-ஐ sweep செய்யலாமா?" (wrong vs right) / "Vise-ஐ எப்படி align செய்வீர்கள்?" (interview)
# Readings 0.00 -> 0.04 mm are an example only; no universal limit is stated.
# Sources: Tormach "The Beginner's Complete Guide to Machinist Vises" (tramming = sweep a vise jaw with an indicator,
# the fixed jaw, not the movable one; adjust until the sweep shows the jaw parallel to the axis);
# CIMCO CNC training book, Appendix A Project 1 "Install Vise" (indicator along the fixed jaw, move left to right,
# tap with a rubber mallet, tighten the bolts, re-check over the full jaw width);
# Travers Tool "How to tram a vise" and Cutwel "How to set up a machine vice" (sweep the fixed jaw along X,
# soft mallet, tighten evenly, re-check; Cutwel: you set your own limit).
# =====================================================================================

VISE_HOOK = dict(hook="Sweep: 0 → 0.04", hsize=90, hook2="X-ல் reading மாறுகிறது!", h2size=58, s=0, e=4.2, svg=f'''
<text class="fig" x="24" y="44">TOP VIEW · SCHEMATIC</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">EXAMPLE READINGS · mm</text>
<g transform="rotate(2.2 389 420)">
<rect x="110" y="330" width="560" height="220" rx="6" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="110" y="330" width="560" height="44" fill="#6C93B4" stroke="{LINE}" stroke-width="2"/>
<text x="390" y="362" text-anchor="middle" style="font:700 22px Inter" fill="#fff">FIXED JAW</text>
<text x="390" y="470" text-anchor="middle" style="font:600 24px Inter" fill="#fff">VISE</text></g>
<path d="M110 300H690" stroke="{DIM}" stroke-width="2" stroke-dasharray="10 8"/>
<text x="120" y="290" style="font:600 22px Plex" fill="#9FC3DD">X TRAVEL</text>
<g class="move" data-t="0" data-d="3.0" data-dx="420"><path d="M160 300V330" stroke="#fff" stroke-width="3"/>
<circle cx="160" cy="210" r="62" fill="#E8F0F7" stroke="#fff" stroke-width="3"/><circle cx="160" cy="210" r="6" fill="{PANEL}"/>
<path d="M160 272V300" stroke="#fff" stroke-width="4"/></g>
<g class="a" data-t="0"><rect x="30" y="600" width="718" height="120" rx="16" fill="#0A2236" stroke="#2E5878" stroke-width="2"/>
<text x="60" y="676" style="font:600 32px Inter" fill="#BFD6E8">DIAL</text></g>
{seq(460, 684, [("0.00", 0, 0.7, GRN), ("0.01", 0.7, 1.4, "#fff"), ("0.02", 1.4, 2.1, "#fff"), ("0.03", 2.1, 2.8, OR), ("0.04", 2.8, 9, RED)], 60)}
<text class="a" data-t="0" x="389" y="584" text-anchor="middle" style="font:500 22px Plex" fill="{OR}">ANGLE EXAGGERATED FOR VISIBILITY</text>''')


def jaw_angle(t=0.2):
    return f'''<g class="a" data-t="{t}">
<path d="M60 380H720" stroke="{DIM}" stroke-width="3" marker-end="url(#aw)"/>
<text x="60" y="425" style="font:600 24px Plex" fill="#BFD6E8">X AXIS TRAVEL</text>
<path d="M60 380L700 300" stroke="{RED}" stroke-width="8"/>
<text x="470" y="300" style="font:700 26px Inter" fill="{RED}">FIXED JAW</text>
<text x="80" y="365" style="font:700 26px Inter" fill="{GRN}">0.00</text><text x="640" y="280" style="font:700 26px Inter" fill="{RED}">0.04</text></g>'''


R32 = dict(id="32", slug="Tramming_Vise_Dial_Indicator", scenes=[
 VISE_HOOK,
 dict(s=4.2, e=10.6, tag="ANSWER  /  02", title="Jaw not parallel", tsize=76, sub="Vise-ஐ align செய்யணும்", ssize=48,
      svg=fig("SWEEP ALONG X", "SCHEMATIC", orange=True) + jaw_angle() + f'''
<text class="w a" data-t="0.8" x="40" y="110" style="font-size:30px">Reading changes along X</text>
<text class="w a" data-t="1.2" x="40" y="160" style="font-size:30px">= jaw angled to X travel</text>
<text class="a" data-t="1.6" x="40" y="490" style="font:500 22px Plex" fill="{OR}">ANGLE EXAGGERATED FOR VISIBILITY</text>''',
      body="Fixed jaw முழுவதும் reading மாறினால், jaw X-க்கு parallel இல்லை."),
 dict(s=10.6, e=17.2, tag="STEPS  /  03", title="Tram the vise", tsize=78, sub="Sweep → adjust → re-check", ssize=46,
      svg=fig("DIAL INDICATOR IN SPINDLE") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "SWEEP FIXED JAW IN X", "Movable jaw அல்ல; fixed jaw", 0.3)
          + checkrow(255, 2, "TAP GENTLY, ADJUST", "Soft mallet; ஒரு bolt pivot", 0.9)
          + checkrow(395, 3, "TIGHTEN, RE-CHECK", "இறுக்கிய பின் மீண்டும் sweep", 1.5),
      body="இறுக்கும்போது vise நகரலாம்; அதனால் மீண்டும் sweep.", body_t=2.0),
 dict(s=17.2, e=23.6, tag="LIMIT  /  04", title="How close?", tsize=80, sub="Job / shop procedure-படி", ssize=48,
      svg=fig("FINAL SWEEP · EXAMPLE") + f'''
<path class="a" data-t="0.2" d="M60 200H720" stroke="{GRN}" stroke-width="8"/>
<text class="a" data-t="0.2" x="60" y="180" style="font:700 26px Inter" fill="{GRN}">FIXED JAW</text>
<path class="a" data-t="0.2" d="M60 260H720" stroke="{DIM}" stroke-width="3" marker-end="url(#aw)"/>
<text class="a" data-t="0.2" x="60" y="300" style="font:600 22px Plex" fill="#BFD6E8">X AXIS TRAVEL</text>
<g class="a" data-t="0.6"><rect x="40" y="340" width="698" height="130" rx="16" fill="#123A57" stroke="{OR}" stroke-width="3"/>
<text x="389" y="398" text-anchor="middle" style="font:800 34px Inter" fill="{OR}">LIMIT = JOB / SHOP PROCEDURE</text>
<text x="389" y="446" text-anchor="middle" style="font:600 26px Inter" fill="#fff">NO UNIVERSAL NUMBER</text></g>''',
      body="அனுமதி அளவை drawing அல்லது shop procedure சொல்லும்."),
 dict(s=23.6, e=30.0, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="0 → 0.04 = re-tram", ssize=50,
      svg=fig("HOW TO ANSWER") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "FIXED JAW, ALONG X", "Indicator-ஐ jaw முழுவதும் நகர்த்து", 0.3)
          + checkrow(255, 2, "ADJUST, TIGHTEN", "மெதுவாகத் தட்டி, bolt இறுக்கு", 0.8)
          + checkrow(395, 3, "RE-CHECK TO LIMIT", "Shop limit-க்குள் வரும் வரை", 1.3),
      body="நீங்கள் செய்த setup-ஐ வைத்தே சொல்லுங்கள்.", body_t=1.8, cta=True, cta_t=2.6),
])


# =====================================================================================
# REEL 33: Edge finder vs probe (picking up a work offset)
# Hook format: (4) verbatim interview question.
# Options: "Edge finder vs probe?" (interview question, chosen; Ø6 tip / 3 mm shown in the panel from frame 1) /
#          "Edge finder radius-ஐ மறந்தால்?" (wrong vs right) / "Probe offset-ஐ update செய்யுமா?" (quiz)
# Sources: Starrett Edge & Centre Finders brochure (tip runs eccentric, then kicks at the edge; "The machine axis is then
# offset by half the tip diameter to establish the true datum"; metric contact diameters incl. 6 mm);
# Tormach "Precision Matters: Measuring Work and Tool Offsets" (edge finder used to set X/Y of work setups; 0.200 in tip);
# Renishaw "Inspection software for machining centres" (6093): "Tool and work offsets can be updated automatically
# based on measured dimensions"; "it is possible to print out the results"; "Some capabilities may vary by an
# individual controller". Example: Ø6 tip approaching the left edge from −X: edge X = spindle X + 3.000.
# =====================================================================================

EF_HOOK = dict(hook="Edge finder vs probe?", hsize=75, hook2="என்ன வித்தியாசம்?", s=0, e=3.6, svg=f'''
<text class="fig" x="24" y="44">INTERVIEW QUESTION</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">TOP VIEW · SCHEMATIC</text>
<rect x="400" y="110" width="330" height="560" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<text x="565" y="400" text-anchor="middle" style="font:700 26px Inter" fill="#fff">PART</text>
<text x="40" y="140" style="font:700 28px Inter" fill="{OR}">EDGE FINDER · Ø6 TIP</text>
<g class="move" data-t="0" data-d="1.4" data-dx="230"><g class="move" data-t="1.5" data-d="0.2" data-dy="22">
<circle cx="140" cy="250" r="30" fill="#E8F0F7" stroke="#fff" stroke-width="3"/><circle cx="140" cy="250" r="5" fill="{PANEL}"/></g></g>
<g class="a" data-t="1.6"><path d="M370 170V330" stroke="{OR}" stroke-width="2" stroke-dasharray="6 5"/>
<path d="M372 190H398" stroke="{OR}" stroke-width="3"/><path d="M370 190l10 -6v12zM400 190l-10 -6v12z" fill="{OR}"/>
<text x="360" y="200" text-anchor="end" style="font:700 26px Inter" fill="{OR}">R 3 mm</text>
<text x="360" y="372" text-anchor="end" style="font:600 22px Inter" fill="#BFD6E8">SPINDLE CENTRE</text></g>
<text x="40" y="470" style="font:700 28px Inter" fill="{GRN}">PROBE</text>
<g class="move" data-t="0.4" data-d="1.4" data-dx="262"><path d="M60 560H120" stroke="#C9D6E0" stroke-width="6"/><circle cx="120" cy="560" r="18" fill="{RED}" stroke="#fff" stroke-width="3"/></g>
<text class="a" data-t="1.9" x="40" y="640" style="font:700 26px Inter" fill="{GRN}">TRIGGER → CYCLE</text>''')


R33 = dict(id="33", slug="Edge_Finder_vs_Probe", scenes=[
 EF_HOOK,
 dict(s=3.6, e=7.7, tag="EDGE FINDER  /  02", title="You add the radius", tsize=70, sub="Ø6 tip → 3 mm", ssize=50,
      svg=fig("Ø6 TIP · FROM −X SIDE", "EXAMPLE", orange=True) + f'''
<rect x="420" y="90" width="320" height="360" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<path d="M420 70V470" stroke="{OR}" stroke-width="3" stroke-dasharray="8 6"/>
<g class="a" data-t="0.2"><circle cx="330" cy="250" r="90" fill="#E8F0F7" stroke="#fff" stroke-width="3"/>
<circle cx="330" cy="250" r="7" fill="{PANEL}"/><path d="M330 120V380" stroke="{PANEL}" stroke-width="2" stroke-dasharray="6 6"/></g>
<g class="a" data-t="0.6"><path d="M336 400H414" stroke="{OR}" stroke-width="3" marker-start="url(#ao)" marker-end="url(#ao)"/>
<text x="375" y="440" text-anchor="middle" style="font:700 26px Inter" fill="{OR}">3</text></g>
<text class="a" data-t="1.0" x="40" y="100" style="font:700 26px Inter" fill="#fff">SPINDLE</text>
<text class="a" data-t="1.0" x="40" y="132" style="font:700 26px Inter" fill="#fff">CENTRE</text>
<path class="a" data-t="1.0" d="M160 140L322 244" stroke="#fff" stroke-width="2"/>
<text class="code a" data-t="1.4" x="40" y="500" style="font-size:28px"><tspan fill="{W}">EDGE X = SPINDLE X </tspan><tspan fill="{OR}">+ 3.000</tspan></text>''',
      body="Kick ஆனதும் spindle centre edge-லிருந்து ஒரு radius தூரம்.", body_t=0.4),
 dict(s=7.7, e=11.8, tag="PROBE  /  03", title="Probe: cycle measures", tsize=66, sub="Update அல்லது report", ssize=50,
      svg=fig("PROBING CYCLE", "SYSTEM-SPECIFIC", orange=True) + f'''
{box(40, 80, 698, 110, LINE, 0.2)}{txt(389, 150, "TOUCH → CYCLE CALCULATES", 34, "#fff", 800, "middle")}</g>
{box(40, 230, 330, 150, GRN, 0.7)}{txt(205, 295, "UPDATES", 32, GRN, 800, "middle")}{txt(205, 340, "WORK OFFSET", 28, "#fff", 700, "middle")}</g>
{box(408, 230, 330, 150, OR, 1.0)}{txt(573, 295, "ONLY", 32, OR, 800, "middle")}{txt(573, 340, "REPORTS", 28, "#fff", 700, "middle")}</g>
<text class="m a" data-t="1.4" x="40" y="450" style="font-size:22px">DEPENDS ON CYCLE, SETTINGS AND CONTROL</text>''',
      body="எது நடக்கும் என்பது system-ஐப் பொறுத்தது.", body_t=0.4),
 dict(s=11.8, e=15.9, tag="CHECK  /  04", title="Then verify", tsize=80, sub="Offset page பாருங்கள்", ssize=50,
      svg=fig("AFTER EITHER METHOD") + f'''
{box(40, 80, 698, 130, GRN, 0.2)}{txt(70, 160, "READ THE WORK OFFSET", 34, "#fff", 800)}</g>
{box(40, 240, 698, 130, OR, 0.6)}{txt(70, 320, "CHECK IT BEFORE CUTTING", 34, "#fff", 800)}</g>
<text class="m a" data-t="1.0" x="40" y="440" style="font-size:22px">PROVE-OUT PER YOUR SHOP PROCEDURE</text>''',
      body="Offset சரியா என்று பார்த்தபின் தான் cut.", body_t=0.4),
 dict(s=15.9, e=20.0, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="Edge finder vs probe", ssize=50,
      svg=fig("HOW TO ANSWER") + f'''
{box(40, 80, 330, 200, OR, 0.2)}{txt(205, 145, "EDGE FINDER", 32, OR, 800, "middle")}
{txt(205, 200, "YOU ADD RADIUS", 26, "#fff", 700, "middle")}{txt(205, 240, "Ø6 → 3 mm", 26, "#fff", 700, "middle")}</g>
{box(408, 80, 330, 200, GRN, 0.5)}{txt(573, 145, "PROBE", 32, GRN, 800, "middle")}
{txt(573, 200, "CYCLE MEASURES", 26, "#fff", 700, "middle")}{txt(573, 240, "UPDATE OR REPORT", 26, "#fff", 700, "middle")}</g>''',
      body="நீங்கள் பயன்படுத்தியதை வைத்துச் சொல்லுங்கள்.", body_t=0.5, cta=True, cta_t=1.6),
])

REELS = [R29, R30, R31, R32, R33]
