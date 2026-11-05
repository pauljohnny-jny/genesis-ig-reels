from gen import *
from specs.hook_examples import G91 as G91_HOOK, QUIZ as QUIZ_HOOK
W = "#E6F0F7"
SEND = "நண்பருக்கு அனுப்புங்கள்."

# ---------------- REEL 17: G90 vs G91 (Haas mill example, metric) ----------------
# Hook format: (1) cold-open demo. Options considered: "ஒரு G91." (demo, chosen) /
# "X50. → X90?" (wrong vs right) / "G90, G91 வித்தியாசம்?" (interview question).
# Sources: Haas Mill Programming Workbook (G91 "is modal", "makes all subsequent commands incremental";
# modal codes "remain effective until replaced with another G code from the same group");
# Productivity Inc. Haas Mill Programming 2025 p.9 (G90 = relative to the origin of the coordinate system in use,
# G91 = relative to the current position). From X40: G90 X50. -> X50; G91 X50. -> X90; another X50. under G91 -> X140.

def xl(mm):  # schematic number line, 4 px per mm, X0 at x=60
    return 60 + mm * 4

def numline(y, marks, t=0.0):
    out = [f'<path d="M40 {y}H740" stroke="#7FA6C4" stroke-width="2"/>']
    for k, (mm, col) in enumerate(marks):
        x = xl(mm)
        dy = 70 if mm == 50 and k > 0 and marks[k-1][0] == 40 else 36  # stagger X50 under X40 (only 40 px apart)
        out.append(f'<path d="M{x} {y}v-14" stroke="#7FA6C4" stroke-width="2"/><text x="{x}" y="{y+dy}" text-anchor="middle" style="font:600 26px Plex" fill="{col}">X{mm}</text>')
    return f'<g class="a" data-t="{t}">' + "".join(out) + "</g>"

def arrow(x1, x2, y, col, mk, t):
    return (f'<g class="a" data-t="{t}"><circle cx="{x1}" cy="{y}" r="7" fill="{col}"/><path d="M{x1} {y}H{x2-14}" stroke="{col}" stroke-width="5"/>'
            f'<path d="M{x2} {y}l-18 -11v22z" fill="{col}"/></g>')

R17 = dict(id="17", slug="G90_vs_G91_Absolute_Incremental", scenes=[
 dict(G91_HOOK),
 dict(s=4.2, e=10.8, tag="ANSWER  /  02", title="G90 vs G91", tsize=76, sub="Start: X40", ssize=50,
      svg=fig("HAAS MILL EXAMPLE · mm", "SCHEMATIC", orange=True) + f'''
<rect x="30" y="66" width="718" height="64" rx="10" fill="#0A2236" stroke="#2E5878" stroke-width="2"/>
<text class="code a" data-t="0.2" x="52" y="109" style="font-size:30px"><tspan fill="{GRN}">G90</tspan><tspan fill="{W}"> G00 X50.  → X50</tspan></text>
<text class="a" data-t="0.5" x="40" y="172" style="font:700 26px Inter" fill="{GRN}">G90 = POSITION FROM WORK ZERO</text>
{arrow(xl(40), xl(50), 205, GRN, "aw", 0.7)}
<rect x="30" y="246" width="718" height="64" rx="10" fill="#0A2236" stroke="#2E5878" stroke-width="2"/>
<text class="code a" data-t="1.2" x="52" y="289" style="font-size:30px"><tspan fill="{OR}">G91</tspan><tspan fill="{W}"> G00 X50.  → X90</tspan></text>
<text class="a" data-t="1.5" x="40" y="352" style="font:700 26px Inter" fill="{OR}">G91 = DISTANCE FROM CURRENT POSITION</text>
{arrow(xl(40), xl(90), 385, OR, "ao", 1.7)}
{numline(428, [(40, "#BFD6E8"), (50, GRN), (90, OR)], 0)}''',
      body="G90: X50 என்ற இடத்துக்கு. G91: இப்போதைய இடத்திலிருந்து மேலும் 50 mm."),
 dict(s=10.8, e=17.6, tag="TRAP  /  03", title="Forgotten G91", tsize=74, sub="G91 அடுத்த வரியிலும்!", ssize=48,
      svg=fig("HAAS MILL EXAMPLE · mm", "SCHEMATIC", orange=True) + code(30, 64, [
          [("N10 ", "#7FA6C4"), ("G91", OR), (" G00 X50.", W), ("   X40 → X90", "#9FC3DD")],
          [("N20 ", "#7FA6C4"), ("X50.", W), ("  (G91 STILL ON)", RED)],
      ], t0=0.2, dt=0.6, size=30, lh=50, w=718) + f'''
{arrow(xl(40), xl(90), 225, OR, "ao", 0.6)}
{arrow(xl(90), xl(140), 265, RED, "ar", 1.4)}
<text class="a" data-t="1.8" x="40" y="330" style="font:800 34px Inter" fill="{RED}">X90 + 50 = X140</text>
<text class="m a" data-t="2.2" x="40" y="370" style="font-size:22px">MODAL: ACTIVE UNTIL G90 IS COMMANDED</text>
{numline(450, [(40, "#BFD6E8"), (90, OR), (140, RED)], 0)}''',
      body="G91 modal. G90 வரும் வரை ஒவ்வொரு X, Y, Z-ம் incremental ஆக நகரும்."),
 dict(s=17.6, e=24.2, tag="CHECK  /  04", title="Before cycle start", tsize=68, sub="மூன்று சோதனைகள்.",
      svg=fig("OPERATOR CHECK") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "FIND G91", "Program-ல் G91 எங்கே வருகிறது?", 0.3)
          + checkrow(255, 2, "FIND G90", "எங்கே மீண்டும் G90 ஆகிறது?", 0.8)
          + checkrow(395, 3, "READ THE MOVE", "X50. = இடமா, தூரமா?", 1.3),
      body="Program-ஐ prove-out செய்யும் முறை உங்கள் shop procedure-படி.", body_t=1.8),
 dict(s=24.2, e=31.0, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="ஒரு G91 → X90.", ssize=50,
      svg=fig("HOW TO ANSWER") + f'''
<g class="a" data-t="0.3"><rect x="40" y="80" width="330" height="150" rx="14" fill="#123A57" stroke="{GRN}" stroke-width="3"/>
<text x="205" y="140" text-anchor="middle" style="font:800 44px Inter" fill="{GRN}">G90</text>
<text x="205" y="190" text-anchor="middle" style="font:600 26px Inter" fill="#fff">WHERE TO GO</text></g>
<g class="a" data-t="0.6"><rect x="408" y="80" width="330" height="150" rx="14" fill="#123A57" stroke="{OR}" stroke-width="3"/>
<text x="573" y="140" text-anchor="middle" style="font:800 44px Inter" fill="{OR}">G91</text>
<text x="573" y="190" text-anchor="middle" style="font:600 26px Inter" fill="#fff">HOW FAR TO GO</text></g>
<text class="w a" data-t="1.1" x="40" y="300" style="font-size:30px">"G91 modal, G90 வரை தொடரும்."</text>
<text class="m a" data-t="1.5" x="40" y="360" style="font-size:22px">G-CODES CAN DIFFER BY CONTROL. CHECK YOUR MANUAL.</text>''',
      body="உங்கள் program-ன் உதாரணம் சொல்லுங்கள்.", body_t=1.8,
      cta=True, cta_t=2.6, cta_icon="send", cta_text=SEND),
])

# ---------------- REEL 18: 0.01 mm = ? µm ----------------
# Hook format: (2) countdown quiz. Options considered: "0.01 mm = ? µm" (quiz, chosen) /
# "0.01 mm = 1 µm?" (wrong vs right) / "10 micron எத்தனை mm?" (interview question).
# Sources: BIPM SI prefixes (milli = 10^-3, micro = 10^-6) -> 1 mm = 1,000 µm, so 0.01 mm = 10 µm;
# Mitutoyo Quick Guide (0.01 mm micrometer graduation).

def ladder_row(y, mm, um, t, hl=False):
    col = OR if hl else "#fff"
    stroke = OR if hl else LINE
    return f'''<g class="a" data-t="{t}"><rect x="40" y="{y}" width="698" height="78" rx="12" fill="#123A57" stroke="{stroke}" stroke-width="{3 if hl else 2}"/>
<text x="250" y="{y+52}" text-anchor="end" style="font:700 38px Inter" fill="{col}">{mm} mm</text>
<text x="389" y="{y+52}" text-anchor="middle" style="font:700 38px Inter" fill="#9FC3DD">=</text>
<text x="700" y="{y+52}" text-anchor="end" style="font:700 38px Inter" fill="{col}">{um} µm</text></g>'''

R18 = dict(id="18", slug="0p01mm_to_Micrometres", scenes=[
 dict(QUIZ_HOOK),
 dict(s=4.0, e=10.5, tag="ANSWER  /  02", title="= 10 µm", tsize=86, sub="1 mm = 1000 µm", ssize=50,
      svg=fig("SI PREFIXES", "SOURCE: BIPM", orange=True) + f'''
<text class="code a" data-t="0.2" x="40" y="100" style="font-size:32px"><tspan fill="{W}">1 mm = 10⁻³ m   (milli)</tspan></text>
<text class="code a" data-t="0.6" x="40" y="160" style="font-size:32px"><tspan fill="{W}">1 µm = 10⁻⁶ m   (micro)</tspan></text>
<text class="a" data-t="1.0" x="40" y="230" style="font:700 34px Inter" fill="#fff">1 mm = 1000 µm</text>
<text class="code a" data-t="1.4" x="40" y="300" style="font-size:32px"><tspan fill="{W}">0.01 × 1000 = </tspan><tspan fill="{OR}">10</tspan></text>
<g class="a" data-t="1.8"><rect x="40" y="350" width="698" height="120" rx="18" fill="#123A57" stroke="{OR}" stroke-width="4"/>
<text x="389" y="430" text-anchor="middle" style="font:800 56px Inter" fill="{OR}">0.01 mm = 10 µm</text></g>''',
      body="mm-ஐ µm ஆக மாற்ற 1000-ஆல் பெருக்குங்கள்."),
 dict(s=10.5, e=17.0, tag="LADDER  /  03", title="Decimal ladder", tsize=70, sub="ஒவ்வொரு படியும் ÷ 10", ssize=48,
      svg=fig("mm → µm") + ladder_row(64, "1", "1000", 0.2) + ladder_row(156, "0.1", "100", 0.6)
          + ladder_row(248, "0.01", "10", 1.0, hl=True) + ladder_row(340, "0.001", "1", 1.4)
          + '<text class="m a" data-t="1.8" x="40" y="470" style="font-size:22px">0.01 mm MICROMETER DIVISION = 10 µm</text>',
      body="ஒரு decimal இடம் மாறினால் மதிப்பு பத்து மடங்கு மாறும்."),
 dict(s=17.0, e=23.5, tag="CHECK  /  04", title="0.01 = 0.010", tsize=74, sub="0.001 அல்ல!", ssize=50,
      svg=fig("SAME VALUE?") + f'''
<g class="a" data-t="0.2"><rect x="40" y="70" width="698" height="96" rx="12" fill="#123A57" stroke="{GRN}" stroke-width="3"/>
<text x="70" y="132" style="font:700 38px Inter" fill="#fff">0.01 mm  =  0.010 mm</text></g>{tick(690, 118, 0.6)}
<text class="m a" data-t="0.7" x="40" y="205" style="font-size:22px">SAME VALUE, WRITTEN TO 3 DECIMALS = 10 µm</text>
<g class="a" data-t="1.2"><rect x="40" y="260" width="698" height="96" rx="12" fill="#123A57" stroke="{RED}" stroke-width="3"/>
<text x="70" y="322" style="font:700 38px Inter" fill="#fff">0.01 mm  ≠  0.001 mm</text></g>{cross(690, 308, 1.6)}
<text class="a" data-t="1.8" x="40" y="400" style="font:600 26px Inter" fill="{RED}">0.001 mm = 1 µm  (10× SMALLER)</text>''',
      body="Drawing-ல் உள்ள decimal இடங்களை கவனமாக எண்ணுங்கள்."),
 dict(s=23.5, e=30.0, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="0.01 mm = 10 µm", ssize=50,
      svg=fig("HOW TO ANSWER") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "× 1000", "mm → µm: 1000-ஆல் பெருக்கு", 0.3)
          + checkrow(255, 2, "0.01 mm = 10 µm", "Micrometer ஒரு பிரிவு", 0.8)
          + checkrow(395, 3, "COUNT DECIMALS", "0.010 = 0.01; 0.001 வேறு", 1.3),
      body="mm, µm இரண்டிலும் சொல்லிப் பழகுங்கள்.", body_t=1.8, cta=True, cta_t=2.6),
])

REELS = [R17, R18]
