from gen import *

W = "#E6F0F7"

# ---------------- REEL 03: explaining a setup you handled ----------------
def vise(extra=""):
    return f'''
<rect x="40" y="440" width="698" height="40" fill="#1F4A6B" stroke="{LINE}" stroke-width="2"/>
<text class="m" x="60" y="469" style="font-size:22px">TABLE</text>
<rect x="150" y="400" width="480" height="40" fill="#2F5F84" stroke="{LINE}" stroke-width="2.5"/>
<rect x="150" y="220" width="70" height="180" fill="#3E6F96" stroke="{LINE}" stroke-width="2.5"/>
<rect x="560" y="250" width="70" height="150" fill="#3E6F96" stroke="{LINE}" stroke-width="2.5"/>
<path d="M630 325H700" stroke="{LINE}" stroke-width="6"/><circle cx="706" cy="325" r="10" fill="{LINE}"/>
<rect x="240" y="350" width="60" height="50" fill="#6C93B4" stroke="{LINE}" stroke-width="2"/>
<rect x="480" y="350" width="60" height="50" fill="#6C93B4" stroke="{LINE}" stroke-width="2"/>
<rect x="220" y="250" width="340" height="100" fill="{STEEL}" stroke="{LINE}" stroke-width="3"/>
<text class="w" x="390" y="311" text-anchor="middle">PART</text>
<text class="m" x="390" y="388" text-anchor="middle" style="font-size:22px">PARALLELS</text>
<text class="m" x="185" y="200" text-anchor="middle">FIXED JAW</text>
<text class="m" x="595" y="230" text-anchor="middle">MOVING JAW</text>
{extra}'''

R03 = dict(id="03", slug="Explain_Your_Setup", scenes=[
 dict(s=0, e=5, tag="SETUP  /  01", title="Your setup", sub="எப்படி விளக்குவீர்கள்?",
      svg=fig("FIG. 01", "VISE SETUP · EXAMPLE") + vise(),
      body='"Setup செய்திருக்கிறீர்களா?" என்று கேட்டால், "ஆம்" மட்டும் போதாது.'),
 dict(s=5, e=11, tag="STEP 1  /  02", title="Part & holding", sub="என்ன, எப்படிப் பிடித்தீர்கள்?", ssize=46,
      svg=fig("FIG. 02", "VISE SETUP · EXAMPLE") + vise(f'''
<rect class="pulse" data-t="1.2" x="143" y="213" width="84" height="194" rx="6" fill="none" stroke="{OR}" stroke-width="5"/>
<path class="draw" data-t="1.6" d="M220 250V350" pathLength="1" stroke="{OR}" stroke-width="8"/>
<text class="mo a" data-t="1.8" x="250" y="232">REFERENCE FACE</text>'''),
      body="Part, material, vise அல்லது fixture, எந்த முகம் reference என்று சொல்லுங்கள்."),
 dict(s=11, e=17, tag="STEP 2  /  03", title="Work zero", sub="எப்படி எடுத்தீர்கள்?",
      svg=fig("FIG. 03", "TOP VIEW · EXAMPLE") + f'''
<g class="a" data-t="0.2"><rect x="200" y="120" width="380" height="270" fill="{STEEL}" stroke="{LINE}" stroke-width="3"/>
<rect x="290" y="190" width="200" height="120" rx="14" fill="none" stroke="{LINE}" stroke-width="2.5"/></g>
<g class="a" data-t="0.9"><circle cx="186" cy="255" r="14" fill="#E6F0F7" stroke="{OR}" stroke-width="3"/>
<path d="M60 255H168" stroke="{OR}" stroke-width="3" marker-end="url(#ao)"/><text class="mo" x="40" y="236">EDGE FINDER</text><text class="mo" x="40" y="292">/ PROBE</text></g>
<g class="a" data-t="1.6"><circle cx="200" cy="390" r="12" fill="none" stroke="{OR}" stroke-width="4"/>
<path d="M200 390H300" stroke="{OR}" stroke-width="4" marker-end="url(#ao)"/><path d="M200 390V300" stroke="{OR}" stroke-width="4" marker-end="url(#ao)"/>
<text class="mo" x="310" y="420">X+</text><text class="mo" x="212" y="306">Y+</text><text class="w" x="214" y="455" style="fill:{OR}">X0 Y0</text></g>
<text class="m a" data-t="2.2" x="600" y="160">Z0 =</text><text class="m a" data-t="2.2" x="600" y="196">TOP FACE?</text>''',
      body="நீங்கள் உண்மையில் பயன்படுத்திய முறையைச் சொல்லுங்கள்."),
 dict(s=17, e=23, tag="STEP 3  /  04", title="First piece", sub="எதை அளந்தீர்கள்?",
      svg=fig("FIG. 04", "EXAMPLE") + f'''
<g class="a" data-t="0.2"><rect x="40" y="140" width="360" height="250" fill="{STEEL}" stroke="{LINE}" stroke-width="3"/>
<rect x="120" y="215" width="200" height="110" rx="12" fill="#2F5F84" stroke="{LINE}" stroke-width="2.5"/>
<text class="m" x="220" y="278" text-anchor="middle" style="font-size:22px;fill:#fff">POCKET</text></g>
<g class="a" data-t="0.8"><path d="M120 205V120M320 205V120" stroke="#fff" stroke-width="2"/>
<path d="M124 132H316" stroke="#fff" stroke-width="2.5" marker-start="url(#aw)" marker-end="url(#aw)"/>
<text x="220" y="116" text-anchor="middle" style="font:600 28px Inter" fill="{OR}">40.00 ±0.03</text></g>
<g class="a" data-t="1.2"><path d="M330 215H380M330 325H380" stroke="#fff" stroke-width="2"/><path d="M368 219V321" stroke="#fff" stroke-width="2.5" marker-start="url(#aw)" marker-end="url(#aw)"/>
<text x="60" y="440" style="font:600 26px Inter" fill="#fff">POCKET DEPTH 5.0</text></g>
<text class="m a" data-t="1.6" x="450" y="170">MEASURED WITH</text>
<g class="a" data-t="1.9"><text class="w" x="450" y="230">VERNIER</text></g>{tick(712, 220, 2.1)}
<g class="a" data-t="2.3"><text class="w" x="450" y="300">MICROMETER</text></g>{tick(712, 290, 2.5)}
<g class="a" data-t="2.7"><text class="w" x="450" y="370">DEPTH GAUGE</text></g>{tick(712, 360, 2.9)}''',
      body="முதல் part-ல் எந்த dimension-ஐ, எந்த instrument-ஆல் சரிபார்த்தீர்கள்?"),
 dict(s=23, e=30, tag="INTERVIEW  /  05", title="One-minute answer", tsize=72, sub="இந்த 3 படிகளில்.",
      svg=fig("CHECKLIST") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "PART & HOLDING", "என்ன part, எப்படிப் பிடித்தீர்கள்?", 0.3)
          + checkrow(255, 2, "WORK ZERO", "எப்படி எடுத்தீர்கள், சரிபார்த்தீர்கள்?", 0.8)
          + checkrow(395, 3, "FIRST PIECE", "எதை, எதைக் கொண்டு அளந்தீர்கள்?", 1.3),
      body="உங்கள் சொந்த job-ஐ வைத்தே பயிற்சி செய்யுங்கள்.", body_t=1.8, cta=True, cta_t=2.4),
])

# ---------------- REEL 04: types of offsets ----------------
R04 = dict(id="04", slug="Types_of_Offsets_v2", scenes=[
 dict(s=0, e=5, tag="INTERVIEW Q  /  01", title="Offsets", sub="எத்தனை வகை?",
      svg=fig("QUESTION") + f'''
<text x="389" y="215" text-anchor="middle" style="font:700 52px Inter" fill="#fff">"How many types</text>
<text x="389" y="285" text-anchor="middle" style="font:700 52px Inter" fill="#fff">of offsets?"</text>
<path d="M240 340H538" stroke="{OR}" stroke-width="3"/>
<text class="mo" x="389" y="392" text-anchor="middle">REPORTED BY VMC CANDIDATES</text>''',
      body="VMC interview-ல் கேட்கப்படும் கேள்வி. உங்கள் பதில் என்ன?"),
 dict(s=5, e=11.5, tag="TYPE 1  /  02", title="Work offset", sub="Part எங்கே இருக்கிறது?",
      svg=fig("TOP VIEW", "SCHEMATIC") + f'''
<g class="a" data-t="0.2"><rect x="40" y="80" width="698" height="400" fill="#16405F" stroke="{LINE}" stroke-width="2"/>
<text class="m" x="60" y="462" style="font-size:22px">MACHINE TABLE</text></g>
<g class="a" data-t="0.6"><circle cx="690" cy="120" r="16" fill="none" stroke="#fff" stroke-width="3"/><path d="M690 98V142M668 120H712" stroke="#fff" stroke-width="2"/>
<text class="m" x="660" y="175" text-anchor="end" style="fill:#fff">MACHINE ZERO</text></g>
<g class="a" data-t="1.0"><rect x="150" y="270" width="250" height="150" fill="{STEEL}" stroke="{LINE}" stroke-width="3"/><text class="m" x="275" y="400" text-anchor="middle" style="fill:#fff;font-size:22px">PART</text>
<circle cx="150" cy="270" r="13" fill="none" stroke="{OR}" stroke-width="4"/><text class="mo" x="168" y="305">WORK ZERO</text></g>
<path class="draw" data-t="1.6" data-d="0.7" pathLength="1" d="M672 120H150V255" stroke="{OR}" stroke-width="3" fill="none" stroke-dasharray="1"/>
<text class="mo a" data-t="2.2" x="420" y="156" text-anchor="middle">G54 X</text>
<text class="mo a" data-t="2.4" x="168" y="200">G54 Y</text>''',
      body="G54 போன்ற work offset, part zero எங்கே உள்ளது என்று machine-க்குச் சொல்கிறது."),
 dict(s=11.5, e=18, tag="TYPE 2  /  03", title="Tool offsets", sub="Tool-ன் அளவுகள்.",
      svg=fig("SIDE VIEW", "SCHEMATIC") + f'''
<g class="a" data-t="0.2"><rect x="170" y="70" width="140" height="80" fill="#3E6F96" stroke="{LINE}" stroke-width="2.5"/>
<path d="M120 150H360" stroke="#fff" stroke-width="2" stroke-dasharray="10 6"/><text class="m" x="318" y="140" style="font-size:20px">GAUGE LINE</text>
<rect x="215" y="150" width="50" height="250" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<path d="M215 250l50 30M215 300l50 30M215 350l50 30" stroke="{LINE}" stroke-width="2"/></g>
<g class="a" data-t="0.8"><path d="M140 154V396" stroke="{OR}" stroke-width="3" marker-start="url(#ao)" marker-end="url(#ao)"/>
<text class="mo" x="60" y="290">H</text></g>
<g class="a" data-t="1.3"><path d="M219 440H261" stroke="{OR}" stroke-width="3" marker-start="url(#ao)" marker-end="url(#ao)"/><path d="M215 405V455M265 405V455" stroke="#fff" stroke-width="2"/>
<text class="mo" x="240" y="490" text-anchor="middle">D</text></g>
<g class="a" data-t="1.8"><text class="wb" x="420" y="230" style="fill:{OR}">H</text><text class="w" x="460" y="230">LENGTH</text><text class="m" x="420" y="272">G43 · Z AXIS</text></g>
<g class="a" data-t="2.3"><text class="wb" x="420" y="345" style="fill:{OR}">D</text><text class="w" x="460" y="345">CUTTER COMP</text><text class="m" x="420" y="387">G41 / G42 · X-Y</text></g><g class="a" data-t="2.8"><text class="mo" x="420" y="432" style="font-size:20px">RADIUS OR DIA =</text><text class="mo" x="420" y="460" style="font-size:20px">CONTROL SETTING</text></g>''',
      body="H: tool length offset (Z அச்சு). D: cutter compensation offset (G41/G42)."),
 dict(s=18, e=24, tag="PLUS  /  04", title="Wear offset", sub="சிறிய திருத்தம்.",
      svg=fig("OFFSET PAGE", "EXAMPLE VALUES", orange=True) + f'''
<g class="a" data-t="0.2"><rect x="30" y="80" width="718" height="56" fill="#123A57" stroke="#2E5878" stroke-width="2"/>
<text class="m" x="44" y="117" style="font-size:22px">TOOL</text><text class="m" x="130" y="117" style="font-size:22px">LENGTH</text><text class="m" x="280" y="117" style="font-size:22px;fill:{OR}">L. WEAR</text>
<text class="m" x="440" y="117" style="font-size:22px">D GEOM</text><text class="m" x="580" y="117" style="font-size:22px;fill:{OR}">D WEAR</text></g>
<g class="a" data-t="0.6" style="font:500 28px Plex"><rect x="30" y="136" width="718" height="60" fill="#0F2D44" stroke="#2E5878" stroke-width="2"/>
<text x="56" y="176" fill="#fff">1</text><text x="130" y="176" fill="#fff">125.430</text><text x="280" y="176" fill="{OR}">-0.020</text><text x="440" y="176" fill="#fff">10.000</text><text x="580" y="176" fill="{OR}">-0.010</text></g>
<g class="a" data-t="0.9" style="font:500 28px Plex"><rect x="30" y="196" width="718" height="60" fill="#0F2D44" stroke="#2E5878" stroke-width="2"/>
<text x="56" y="236" fill="#fff">2</text><text x="130" y="236" fill="#fff">98.215</text><text x="280" y="236" fill="{OR}">0.000</text><text x="440" y="236" fill="#fff">6.000</text><text x="580" y="236" fill="{OR}">0.000</text></g>
<rect class="pulse" data-t="1.5" x="268" y="84" width="130" height="176" rx="8" fill="none" stroke="{OR}" stroke-width="4"/>
<rect class="pulse" data-t="1.5" x="568" y="84" width="140" height="176" rx="8" fill="none" stroke="{OR}" stroke-width="4"/>
<text class="w a" data-t="2.0" x="40" y="330">GEOMETRY = measured size</text>
<text class="w a" data-t="2.4" x="40" y="390" style="fill:{OR}">WEAR = small correction</text>
<text class="m a" data-t="2.8" x="40" y="450" style="font-size:22px">FIELD NAMES VARY BY CONTROL</text>''',
      body="சிறிய அளவுத் திருத்தங்களுக்குப் பல shop-களில் wear offset பயன்படுத்துகிறார்கள்."),
 dict(s=24, e=31, tag="ANSWER  /  05", title="Your answer", sub="இரண்டு முக்கிய வகை.",
      svg=fig("SUMMARY") + f'''
<g class="a" data-t="0.2"><rect x="294" y="60" width="190" height="64" rx="10" fill="{OR}"/><text x="389" y="104" text-anchor="middle" style="font:700 32px Inter" fill="{PANEL}">OFFSETS</text>
<path d="M389 124V160M200 160H580M200 160V200M580 160V200" stroke="{LINE}" stroke-width="3" fill="none"/></g>
<g class="a" data-t="0.7"><rect x="110" y="200" width="180" height="60" rx="10" fill="#123A57" stroke="{LINE}" stroke-width="2.5"/><text class="w" x="200" y="241" text-anchor="middle">WORK</text>
<text class="m" x="200" y="310" text-anchor="middle">G54–G59</text><text class="ta" x="200" y="356" text-anchor="middle" style="font-size:26px">part எங்கே</text></g>
<g class="a" data-t="1.2"><rect x="490" y="200" width="180" height="60" rx="10" fill="#123A57" stroke="{LINE}" stroke-width="2.5"/><text class="w" x="580" y="241" text-anchor="middle">TOOL</text>
<text class="m" x="580" y="310" text-anchor="middle">LENGTH · H</text><text class="m" x="580" y="356" text-anchor="middle">CUTTER COMP · D</text><text class="mo" x="580" y="402" text-anchor="middle">+ WEAR</text></g>''',
      body="Offset page-ஐக் காட்டி விளக்கிப் பழகுங்கள்.", body_t=1.8, cta=True, cta_t=2.4),
])

# ---------------- REEL 05 v2: G43 H register check (Haas mill example) ----------------
def gcode(h_col, h_txt, t_col=W, t0=0.0, dt=0.0):
    return code(30, 110, [
        [("T02", t_col), (" M06", W)],
        [("G00 G90 G54 X0. Y0. S2500 M03", W)],
        [("G43 ", W), (h_txt, h_col), (" Z50. M08", W)],
    ], t0=t0, dt=dt, w=718, label="EXAMPLE · HAAS MILL")

def outcome(y, head, sub, col, t):
    return f'<g class="a" data-t="{t}"><rect x="30" y="{y}" width="718" height="105" rx="12" fill="#123A57" stroke="{col}" stroke-width="2.5"/><text x="56" y="{y+46}" style="font:700 34px Inter" fill="{col}">{esc(head)}</text><text class="m" x="56" y="{y+84}" style="font-size:22px">{esc(sub)}</text></g>'

R05 = dict(id="05", slug="G43_H_Offset_Check_v2", scenes=[
 dict(s=0, e=5.5, tag="ERROR CHECK  /  01", title="Spot the error", sub="இந்த code-ல் தவறு எங்கே?",
      svg=fig("FIG. 01", "3 LINES") + gcode(W, "H01") + f'<text class="w a" data-t="0.6" x="30" y="370">Example setup: T02 → verified H02</text><text class="m a" data-t="1.1" x="30" y="420">LOOK AT LINE 3</text>',
      body="இந்த setup-ல் T02-க்குச் சரிபார்த்த length offset H02. Code-ஐப் பாருங்கள்."),
 dict(s=5.5, e=11.5, tag="ERROR  /  02", title="Wrong register", sub="Program: H01. Setup: H02.",
      svg=fig("FIG. 02", "HAAS MILL EXAMPLE") + gcode(RED, "H01", t_col=OR) + f"""
<rect class="pulse" data-t="0.5" x="112" y="225" width="72" height="44" rx="6" fill="none" stroke="{RED}" stroke-width="4"/>
<rect class="pulse" data-t="0.5" x="44" y="133" width="72" height="44" rx="6" fill="none" stroke="{OR}" stroke-width="4"/>
{cross(52, 360, 0.9)}<text class="w a" data-t="0.9" x="90" y="371" style="fill:{RED}">Program selects H01</text>
{tick(52, 430, 1.4)}<text class="w a" data-t="1.4" x="90" y="441">Setup: T02 → verified H02</text>""",
      body="H01 என்பது length offset register 01. இந்த setup-ல் அது T02-க்கு உரியது அல்ல."),
 dict(s=11.5, e=18, tag="RESULT  /  03", title="What can happen", tsize=72, sub="Control-ஐப் பொறுத்து.",
      svg=fig("POSSIBLE OUTCOMES") + outcome(70, "ALARM", "HAAS: SETTING 15 ON → ALARM 332", OR, 0.3)
          + outcome(190, "INCORRECT Z", "TOOL TIP NOT WHERE THE PROGRAM EXPECTS", "#FFFFFF", 0.9)
          + outcome(310, "COLLISION RISK", "IF THE WRONG LENGTH IS USED", RED, 1.5)
          + '<text class="m a" data-t="2.1" x="30" y="470" style="font-size:22px">NGC SOFTWARE BEHAVIOUR VARIES</text>',
      body="Alarm வரலாம்; இல்லையெனில் Z தவறாகி collision ஆபத்து ஏற்படலாம்."),
 dict(s=18, e=24, tag="FIX  /  04", title="Fix", sub="சரிபார்த்த H மட்டும்.",
      svg=fig("FIG. 04", "HAAS MILL EXAMPLE") + gcode(GRN, "H02", t_col=GRN) + tick(52, 370, 0.8) + f"""
<text class="w a" data-t="0.8" x="90" y="381">Example: T02 → verified H02</text>
<text class="m a" data-t="1.6" x="30" y="450" style="font-size:22px">H NUMBERING CAN DIFFER BY SHOP / CONTROL</text>""",
      body="இந்த setup-ல் T02-க்கு H02 சரிபார்க்கப்பட்டது; அதனால் G43 H02."),
 dict(s=24, e=31, tag="CHECK  /  05", title="Before cycle start", tsize=70, sub="இதைச் சரிபாருங்கள்.",
      svg=fig("CHECKLIST") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "LOADED T", "Spindle-ல் எந்த tool உள்ளது?", 0.3)
          + checkrow(255, 2, "ASSIGNED H", "அந்த tool-க்கு எந்த H?", 0.8)
          + checkrow(395, 3, "MEASURED VALUE", "அந்த H-ல் சரியான length உள்ளதா?", 1.3),
      body="Program-ஐயும் offset page-ஐயும் ஒப்பிட்டுப் பாருங்கள்.", body_t=1.8, cta=True, cta_t=2.4),
])

REELS = [R03, R04, R05]
