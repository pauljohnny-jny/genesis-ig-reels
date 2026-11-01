from gen import *
W = "#E6F0F7"
SEND = "நண்பருக்கு அனுப்புங்கள்."

# ---------------- REEL 13: G02/G03 I/J arc-centre offsets (Haas mill example) ----------------
def arcplot(vals=True, draw_t=0.0, q=False):
    lab_i = "I = ?" if q else "I = −40"
    lab_j = "J = ?" if q else "J = 0"
    v = f'''
<g class="a" data-t="{draw_t+1.0}"><path d="M500 432H306" stroke="{OR}" stroke-width="4" marker-end="url(#ao)"/>
<text x="400" y="470" text-anchor="middle" style="font:700 34px Inter" fill="{OR}">{lab_i}</text>
<text x="560" y="250" style="font:700 34px Inter" fill="{OR}">{lab_j}</text></g>''' if vals else ""
    return f'''
<path d="M260 400H640" stroke="#7FA6C4" stroke-width="2" marker-end="url(#aw)"/><text class="m" x="648" y="388">X+</text>
<path d="M300 440V130" stroke="#7FA6C4" stroke-width="2" marker-end="url(#aw)"/><text class="m" x="312" y="138">Y+</text>
<path class="draw" data-t="{draw_t}" data-d="1.0" pathLength="1" d="M500 400A200 200 0 0 0 300 200" stroke="#fff" stroke-width="5" fill="none"/>
<circle cx="500" cy="400" r="11" fill="#fff"/><text x="520" y="385" style="font:700 28px Inter" fill="#fff">START</text><text class="m" x="520" y="420">X40 Y0</text>
<circle cx="300" cy="200" r="11" fill="#fff"/><text x="282" y="196" text-anchor="end" style="font:700 28px Inter" fill="#fff">END</text><text class="m" x="282" y="230" text-anchor="end">X0 Y40</text>
<circle cx="300" cy="400" r="12" fill="{OR}"/><text x="282" y="385" text-anchor="end" style="font:700 28px Inter" fill="{OR}">CENTRE</text><text class="mo" x="282" y="420" text-anchor="end">X0 Y0</text>
{v}'''

R13 = dict(id="13", slug="G02_G03_IJ_Arc_Centre", scenes=[
 dict(s=0, e=5.5, tag="ARC  /  01", title="I, J = ?", sub="எங்கிருந்து அளப்பது?",
      svg=fig("G17 · XY PLANE", "HAAS MILL EXAMPLE", orange=True) + arcplot(vals=True, draw_t=0.0, q=True),
      body="G03 arc-ல் centre-ஐ I, J எப்படிச் சொல்கின்றன?"),
 dict(s=5.5, e=12, tag="RULE  /  02", title="From the start", tsize=72, sub="Start point → centre.",
      svg=fig("G17 · XY PLANE", "HAAS MILL EXAMPLE", orange=True) + arcplot(vals=False, draw_t=0.0) + f'''
<path class="draw" data-t="0.6" data-d="0.8" pathLength="1" d="M500 432H306" stroke="{OR}" stroke-width="4" fill="none"/>
<text class="w a" data-t="1.4" x="389" y="490" text-anchor="middle">I, J = distance START → CENTRE</text>''',
      body="I, J என்பது arc-ன் START point-லிருந்து centre வரை உள்ள தூரம் (Haas mill)."),
 dict(s=12, e=18.5, tag="WORKED  /  03", title="Worked example", tsize=72, sub="I = −40, J = 0.",
      svg=f'<text class="code" x="24" y="56" style="font-size:30px"><tspan fill="{W}">G03 X0. Y40. </tspan><tspan fill="{OR}">I-40. J0.</tspan></text>'
          + arcplot(vals=True, draw_t=0.0).replace('<path d="M300 440V130"', '<path d="M300 440V130"'),
      body="I = centre X − start X = 0 − 40. J = centre Y − start Y = 0 − 0."),
 dict(s=18.5, e=24.5, tag="ERROR CHECK  /  04", title="Common mistake", tsize=72, sub="Centre-ன் X, Y-ஐ நேரடியாக?", ssize=44,
      svg=fig("SAME ARC", "HAAS MILL EXAMPLE", orange=True) + f'''
<g class="a" data-t="0.3"><rect x="30" y="80" width="718" height="150" rx="12" fill="#123A57" stroke="{RED}" stroke-width="3"/>
<text class="code" x="110" y="140" style="font-size:32px"><tspan fill="{W}">G03 X0. Y40. </tspan><tspan fill="{RED}">I0. J0.</tspan></text>
<text class="m" x="110" y="192" style="font-size:22px">CENTRE X, Y WRITTEN AS I, J</text></g>{cross(68, 155, 0.6)}
<g class="a" data-t="1.4"><rect x="30" y="260" width="718" height="150" rx="12" fill="#123A57" stroke="{GRN}" stroke-width="3"/>
<text class="code" x="110" y="320" style="font-size:32px"><tspan fill="{W}">G03 X0. Y40. </tspan><tspan fill="{GRN}">I-40. J0.</tspan></text>
<text class="m" x="110" y="372" style="font-size:22px">DISTANCE FROM START TO CENTRE</text></g>{tick(68, 335, 1.7)}
<text class="m a" data-t="2.4" x="30" y="460" style="font-size:22px">SOME CONTROLS HAVE AN ABSOLUTE ARC-CENTRE MODE.</text>
<text class="m a" data-t="2.4" x="30" y="492" style="font-size:22px">CHECK YOUR MACHINE MANUAL.</text>''',
      body="தவறான I, J கொடுத்தால் arc தவறாகலாம் அல்லது alarm வரலாம்."),
 dict(s=24.5, e=31, tag="REMEMBER  /  05", title="Remember", sub="மூன்று விதிகள்.",
      svg=fig("CHECKLIST · HAAS MILL") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "FROM START", "Start point-லிருந்து centre வரை", 0.3)
          + checkrow(255, 2, "SIGN", "Centre இடது/கீழ் இருந்தால் minus", 0.8)
          + checkrow(395, 3, "FULL CIRCLE", "R அல்ல; I, J மட்டும்", 1.3),
      body="உங்கள் control-ன் arc mode-ஐ manual-ல் உறுதிசெய்யுங்கள்.", body_t=1.8, cta=True, cta_t=2.4),
])

# ---------------- REEL 14: toolholder runout ----------------
def topcutter(cx=389, cy=255, r=110, worn=True):
    teeth = ""
    for k, a in enumerate((0, 90, 180, 270)):
        col = RED if (worn and k == 0) else OR
        teeth += f'<path d="M{cx} {cy-r} l18 24 h-36z" fill="{col}" transform="rotate({a} {cx} {cy})"/>'
    return f'''<g class="spin" data-cx="{cx}" data-cy="{cy}" data-r="0.6"><circle cx="{cx}" cy="{cy}" r="{r}" fill="#6C93B4" stroke="{LINE}" stroke-width="3"/>{teeth}
<circle cx="{cx}" cy="{cy}" r="10" fill="{PANEL}"/></g>'''

def dial(cx, cy, t):
    return f'''<g class="a" data-t="{t}"><circle cx="{cx}" cy="{cy}" r="30" fill="#E6F0F7" stroke="{LINE}" stroke-width="2"/>
<path d="M{cx} {cy}L{cx+14} {cy-18}" stroke="{RED}" stroke-width="3"/><path d="M{cx-30} {cy}H{cx-80}" stroke="{LINE}" stroke-width="4"/></g>'''

def holder_tool(t=0.0, tilt=0.0):
    return f'''<g class="a" data-t="{t}"><path d="M40 90H738" stroke="#fff" stroke-width="2.5"/><text class="m" x="44" y="80" style="font-size:20px">SPINDLE</text>
<g transform="rotate({tilt} 389 200)"><rect x="330" y="90" width="118" height="110" fill="#3E6F96" stroke="{LINE}" stroke-width="2"/>
<rect x="370" y="200" width="38" height="250" fill="{STEEL}" stroke="{LINE}" stroke-width="2"/>
<path d="M370 300l38 22M370 350l38 22M370 400l38 22" stroke="{LINE}" stroke-width="2"/></g></g>'''

R14 = dict(id="14", slug="Toolholder_Runout", scenes=[
 dict(s=0, e=5, tag="TOOLING  /  01", title="Runout", sub="ஒரு பல் மட்டும் தேய்கிறதா?", ssize=46,
      svg=fig("TOP VIEW", "SCHEMATIC") + topcutter() + f'<text class="a" data-t="0.5" x="389" y="455" text-anchor="middle" style="font:700 32px Inter" fill="{RED}">ONE EDGE WEARS FASTER?</text>',
      body="எல்லாப் பல்லும் சமமாக வெட்டவில்லை என்றால், runout ஒரு காரணமாக இருக்கலாம்."),
 dict(s=5, e=11.5, tag="WHAT  /  02", title="What is runout", tsize=74, sub="மையத்திலிருந்து விலகல்.",
      svg=fig("SIDE VIEW", "EXAGGERATED") + holder_tool(0.0, -3.0) + f'''
<path d="M389 60V490" stroke="#fff" stroke-width="2" stroke-dasharray="12 8"/>
<path class="draw" data-t="0.5" data-d="0.6" pathLength="1" d="M389 200L402 470" stroke="{OR}" stroke-width="3" fill="none"/>
<text class="m a" data-t="0.4" x="150" y="300" style="fill:#fff">SPINDLE AXIS</text>
<text class="mo a" data-t="0.9" x="430" y="300">TOOL AXIS</text>
{dial(600, 440, 1.3)}<text class="m a" data-t="1.3" x="500" y="500">DIAL INDICATOR</text>
<text class="w a" data-t="1.9" x="30" y="490" style="font-size:24px">TIR = highest − lowest reading</text>''',
      body="Tool சுழலும்போது அதன் மையம் spindle மையத்திலிருந்து விலகினால், அது runout."),
 dict(s=11.5, e=18, tag="EFFECT  /  03", title="Effect", sub="ஒரு பல்லுக்கு அதிக load.",
      svg=fig("CHIP LOAD PER EDGE", "ILLUSTRATIVE", orange=True) + "".join(
          f'<rect class="a" data-t="{0.3+i*0.15:.2f}" x="{70+i*70}" y="{400-h}" width="48" height="{h}" rx="4" fill="#E6F0F7"/>' for i, h in enumerate([140, 140, 140, 140]))
          + "".join(f'<rect class="a" data-t="{1.2+i*0.15:.2f}" x="{440+i*70}" y="{400-h}" width="48" height="{h}" rx="4" fill="{OR if h>200 else "#6C93B4"}"/>' for i, h in enumerate([230, 140, 60, 140]))
          + f'''<path d="M50 400H350M420 400H720" stroke="{LINE}" stroke-width="2"/>
<text class="w a" data-t="0.3" x="200" y="450" text-anchor="middle">NO RUNOUT</text><text class="w a" data-t="1.2" x="570" y="450" text-anchor="middle" style="fill:{OR}">WITH RUNOUT</text>
<text class="m a" data-t="2.0" x="389" y="100" text-anchor="middle">ONE EDGE TAKES MORE LOAD → UNEVEN WEAR</text>''',
      body="ஒரு cutting edge அதிக load-ஐ எடுத்து விரைவாகத் தேயும்; tool life குறையும்."),
 dict(s=18, e=24.5, tag="MEASURE  /  04", title="Measure TIR", sub="மூன்று இடங்களில்.",
      svg=fig("SIDE VIEW", "SOURCE: BIG DAISHOWA") + holder_tool(0.0, 0.0)
          + dial(530, 185, 0.5) + '<text class="w a" data-t="0.5" x="580" y="195" style="font-size:28px">1 NOSE</text>'
          + dial(510, 320, 1.0) + '<text class="w a" data-t="1.0" x="560" y="330" style="font-size:28px">2 SHANK</text>'
          + dial(510, 435, 1.5) + '<text class="w a" data-t="1.5" x="560" y="445" style="font-size:28px">3 TIP</text>'
          + '<text class="mo a" data-t="2.1" x="30" y="500" style="font-size:22px">ROTATE ONE FULL TURN · TIR = HIGH − LOW</text>',
      body="Holder nose, shank நடு, tip: மூன்று இடத்திலும் அளந்து ஒப்பிடுங்கள்."),
 dict(s=24.5, e=31, tag="DIAGNOSE  /  05", title="Holder or tool?", tsize=74, sub="எங்கே பிரச்சனை?",
      svg=fig("TWO DIFFERENT CHECKS") + f'''
<g class="a" data-t="0.3"><rect x="30" y="75" width="718" height="130" rx="12" fill="#123A57" stroke="{LINE}" stroke-width="2.5"/>
<text x="56" y="128" style="font:700 32px Inter" fill="#fff">TOOLHOLDER RUNOUT</text><text class="ta" x="56" y="175" style="font-size:26px">holder / spindle taper மட்டும்</text></g>
<g class="a" data-t="0.8"><rect x="30" y="225" width="718" height="130" rx="12" fill="#123A57" stroke="{OR}" stroke-width="2.5"/>
<text x="56" y="278" style="font:700 32px Inter" fill="#fff">ASSEMBLED-TOOL RUNOUT</text><text class="ta" x="56" y="325" style="font-size:26px">holder + collet + tool சேர்ந்து</text></g>
<text class="m a" data-t="1.4" x="30" y="420" style="font-size:22px">ALLOWED VALUE = MANUFACTURER SPEC</text>
<text class="m a" data-t="1.4" x="30" y="452" style="font-size:22px">NO SINGLE UNIVERSAL NUMBER</text>''',
      body="TIR எங்கே அதிகரிக்கிறது? அதுவே காரணத்தைக் காட்டும்.", body_t=1.8, cta=True, cta_t=2.4, cta_text=SEND, cta_icon="send"),
])

REELS = [R13, R14]
