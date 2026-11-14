from gen import *
W = "#E6F0F7"
SEND = "நண்பருக்கு அனுப்புங்கள்."
DIM = "#7FA6C4"


def box(x, y, w, h, stroke=LINE, sw=2, fill="#123A57", rx=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


# =====================================================================================================
# REEL 34: Feed / rapid override check before cycle start (Haas mill example, metric). Target 20 s.
# Hook format: (1) cold-open demo. Options considered:
#   "F500. ஆனால் 250?" (demo: override at 50% halves the real feed; chosen, has the code and number)
#   "RAPID 5% மறந்துவிட்டீர்களா?" (wrong vs right) / "Override பார்ப்பீர்களா?" (interview question)
# Sources: Productivity Inc. (Haas distributor) "Mill Operator 2025" p.30: feed override keys [-10% FEEDRATE] [100% FEEDRATE]
#   [+10% FEEDRATE] [HANDLE FEED]; 100% "sets an overridden feedrate back to the programmed feed rate"; rapid keys [5% RAPID]
#   [25% RAPID] [50% RAPID] [100% RAPID] "limits machine rapids to the value on the key"; "slow down rapids while you prove out
#   a program"; Settings 83, 87, 88 make M30, M06 or RESET "change overridden values back to their defaults";
#   p.24 RESET "sets overrides to default values if Setting 88 is ON".
#   Worked number is arithmetic on that definition: F500 at 50% = 250 mm/min.
H34 = dict(hook="F500. → 250?", hsize=100, hook2="Override-ஐ பார்த்தீர்களா?", h2size=54, s=0, e=3.6, svg=f'''
<text class="fig" x="24" y="44">SCHEMATIC · mm/min</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">HAAS MILL EXAMPLE</text>
<rect x="30" y="74" width="718" height="84" rx="10" fill="#0A2236" stroke="#2E5878" stroke-width="2"/>
<text class="code" x="52" y="128" style="font-size:38px">G01 X150. F500.</text>
{box(30, 186, 340, 130, RED, 3)}
<text x="200" y="230" text-anchor="middle" style="font:600 24px Inter" fill="#BFD6E8">FEED OVERRIDE</text>
<text x="200" y="292" text-anchor="middle" style="font:800 56px Inter" fill="{RED}">50%</text>
<rect class="pulse" data-t="0" x="24" y="180" width="352" height="142" rx="16" fill="none" stroke="{RED}" stroke-width="4"/>
{box(408, 186, 340, 130)}
<text x="578" y="230" text-anchor="middle" style="font:600 24px Inter" fill="#BFD6E8">PROGRAMMED</text>
<text x="578" y="292" text-anchor="middle" style="font:800 56px Inter" fill="#fff">F500</text>
<text x="60" y="392" style="font:700 26px Inter" fill="{GRN}">100%: F500</text>
<path d="M80 440H700" stroke="#2E5878" stroke-width="2"/>
<rect class="grow" data-t="0" data-d="2.0" data-w="500" x="100" y="437" width="0" height="6" fill="{GRN}" opacity="0.6"/>
<g class="move" data-t="0" data-d="2.0" data-dx="500"><circle cx="100" cy="440" r="30" fill="none" stroke="{GRN}" stroke-width="4" stroke-dasharray="9 7"/></g>
<text x="60" y="522" style="font:700 26px Inter" fill="{OR}">ACTUAL AT 50%</text>
<path d="M80 570H700" stroke="#2E5878" stroke-width="2"/>
<rect class="grow" data-t="0" data-d="2.0" data-w="250" x="100" y="567" width="0" height="6" fill="{OR}"/>
<g class="move" data-t="0" data-d="2.0" data-dx="250"><circle cx="100" cy="570" r="30" fill="{OR}" stroke="#fff" stroke-width="3"/><circle cx="100" cy="570" r="7" fill="{PANEL}"/></g>
<text class="a" data-t="2.0" x="389" y="690" text-anchor="middle" style="font:800 40px Inter" fill="{RED}">500 × 50% = 250 mm/min</text>''')

R34 = dict(id="34", slug="Feed_Rapid_Override_Check", scenes=[
 H34,
 dict(s=3.6, e=7.8, tag="ANSWER  /  02", title="Override = % of F", tsize=74, sub="500 × 50% = 250", ssize=50,
      svg=fig("HAAS OVERRIDE KEYS", "HAAS MILL EXAMPLE", orange=True) + f'''
<text class="a" data-t="0.1" x="40" y="100" style="font:700 28px Inter" fill="#fff">FEED</text>
{"".join(f'<g class="a" data-t="0.2">{box(170 + k*196, 66, 176, 54, OR if lab == "100%" else LINE, 3 if lab == "100%" else 2)}<text x="{258 + k*196}" y="103" text-anchor="middle" style="font:700 28px Inter" fill="{OR if lab == "100%" else "#fff"}">{lab}</text></g>' for k, lab in enumerate(["-10%", "100%", "+10%"]))}
<text class="a" data-t="0.6" x="40" y="200" style="font:700 28px Inter" fill="#fff">RAPID</text>
{"".join(f'<g class="a" data-t="0.7">{box(170 + k*146, 166, 130, 54, OR if lab == "100%" else LINE, 3 if lab == "100%" else 2)}<text x="{235 + k*146}" y="203" text-anchor="middle" style="font:700 28px Inter" fill="{OR if lab == "100%" else "#fff"}">{lab}</text></g>' for k, lab in enumerate(["5%", "25%", "50%", "100%"]))}
<text class="m a" data-t="1.1" x="40" y="290" style="font-size:24px">FEED 100% = BACK TO PROGRAMMED F</text>
<text class="m a" data-t="1.4" x="40" y="335" style="font-size:24px">RAPID KEY = LIMIT ON RAPID MOVES</text>
<g class="a" data-t="1.8">{box(40, 380, 698, 100, OR, 3)}
<text x="389" y="446" text-anchor="middle" style="font:800 44px Inter" fill="{OR}">F500 at 50% → 250</text></g>''',
      body="Override, program-ல் உள்ள F-ஐ % ஆக மாற்றும்.", body_t=0.6),
 dict(s=7.8, e=12.0, tag="CHECK  /  03", title="Before cycle start", tsize=70, sub="மூன்றையும் பாருங்கள்.", ssize=48,
      svg=fig("OPERATOR CHECK") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "FEED %", "திட்டமிட்ட அளவில் உள்ளதா?", 0.2)
          + checkrow(255, 2, "SPINDLE %", "முந்தைய job-ல் மாற்றியதா?", 0.6)
          + checkrow(395, 3, "RAPID 5/25/50/100%", "Prove-out-க்கு எது தேவை?", 1.0),
      body="அளவு உங்கள் shop procedure-படி.", body_t=1.4),
 dict(s=12.0, e=16.2, tag="TRAP  /  04", title="RESET → 100%?", tsize=76, sub="Setting-ஐப் பொறுத்தது.", ssize=48,
      svg=fig("HAAS SETTINGS 83 · 87 · 88", "MODEL-SPECIFIC", orange=True) + f'''
{"".join(f'<g class="a" data-t="{0.2 + k*0.3:.1f}">{box(40 + k*240, 70, 218, 90)}<text x="{149 + k*240}" y="128" text-anchor="middle" style="font:800 38px Inter" fill="#fff">{lab}</text></g>' for k, lab in enumerate(["M30", "M06", "RESET"]))}
<path class="a" data-t="1.1" d="M389 175v50" stroke="{OR}" stroke-width="5" marker-end="url(#ao)"/>
<text class="a" data-t="1.2" x="389" y="280" text-anchor="middle" style="font:700 30px Inter" fill="#fff">OVERRIDES BACK TO DEFAULT</text>
<text class="a" data-t="1.5" x="389" y="340" text-anchor="middle" style="font:800 34px Inter" fill="{OR}">ONLY IF THAT SETTING IS ON</text>
<text class="m a" data-t="1.8" x="389" y="430" text-anchor="middle" style="font-size:24px">CHECK THE SCREEN, NOT YOUR MEMORY</text>''',
      body="Setting OFF என்றால் பழைய % தொடரலாம்.", body_t=1.0),
 dict(s=16.2, e=20.4, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="F500 at 50% → 250", ssize=50,
      svg=fig("HOW TO ANSWER") + f'''
<g class="a" data-t="0.2">{box(40, 70, 210, 120, LINE, 3)}<text x="145" y="122" text-anchor="middle" style="font:600 24px Inter" fill="#BFD6E8">PROGRAM</text><text x="145" y="168" text-anchor="middle" style="font:800 38px Inter" fill="#fff">F500</text></g>
<g class="a" data-t="0.4">{box(284, 70, 210, 120, RED, 3)}<text x="389" y="122" text-anchor="middle" style="font:600 24px Inter" fill="#BFD6E8">OVERRIDE</text><text x="389" y="168" text-anchor="middle" style="font:800 38px Inter" fill="{RED}">50%</text></g>
<g class="a" data-t="0.6">{box(528, 70, 210, 120, OR, 3)}<text x="633" y="122" text-anchor="middle" style="font:600 24px Inter" fill="#BFD6E8">ACTUAL</text><text x="633" y="168" text-anchor="middle" style="font:800 38px Inter" fill="{OR}">250</text></g>
<text class="w a" data-t="0.9" x="40" y="280" style="font-size:30px">"Cycle start-க்கு முன் override</text>
<text class="w a" data-t="0.9" x="40" y="326" style="font-size:30px"> பார்ப்பேன்."</text>
<text class="m a" data-t="1.3" x="40" y="420" style="font-size:22px">KEYS DIFFER BY CONTROL. CHECK YOUR MANUAL.</text>''',
      cta=True, cta_t=1.6, cta_icon="send", cta_text=SEND),
])

# =====================================================================================================
# REEL 35: G17 / G18 / G19 plane selection (Haas mill example). Target 30 s.
# Hook format: (2) countdown quiz. Options considered:
#   "G18 = எந்த plane?" (quiz with XY / XZ / YZ options; chosen) / "G18-ல் G02 = XY arc?" (wrong vs right) /
#   "G17 என்றால் என்ன?" (interview question)
# Sources: Haas Mill Programming Workbook (Haas Automation, June 2000; engr.psu.edu/cim/mllwrkb.pdf):
#   "G17 for the XY plane, G18 for the XZ plane, and G19 for the YZ plane"; "plane selection is modal and stays in effect ...
#   until you command another plane selection code"; "default plane selection when the machine is powered on is G17";
#   I, J, K "specific to the selected plane (IJ for G17, IK for G18, JK for G19)". Current Haas Mill Programming Workbook
#   (haascnc.com) p.14 "G17* ... Circular Motion XY Plane Selection (G02 or G03)", "* = default G code in a group".
#   Productivity Inc. "Mill Programming 2025" p.37: "Cutter compensation is only available in the X Axis and the Y Axis for
#   2D machining (G17)". (Haas 2000 workbook adds G141 for 3D comp; not shown, out of scope.)


def plane_card(x, code_, plane, a1, a2, ijk, t, hl=False):
    col = OR if hl else "#fff"
    return f'''<g class="a" data-t="{t}">{box(x, 70, 226, 380, OR if hl else LINE, 3 if hl else 2)}
<text x="{x+113}" y="130" text-anchor="middle" style="font:800 44px Inter" fill="{col}">{code_}</text>
<path d="M{x+60} 330H{x+180}" stroke="{GRN}" stroke-width="4" marker-end="url(#aw)"/><text x="{x+190}" y="340" style="font:700 26px Inter" fill="{GRN}">{a1}</text>
<path d="M{x+60} 330V210" stroke="{OR}" stroke-width="4" marker-end="url(#ao)"/><text x="{x+48}" y="200" style="font:700 26px Inter" fill="{OR}">{a2}</text>
<path class="draw" data-t="{t+0.3}" data-d="0.6" pathLength="1" d="M{x+150} 330A90 90 0 0 0 {x+60} 240" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="1"/>
<text x="{x+113}" y="395" text-anchor="middle" style="font:700 30px Inter" fill="{col}">{plane}</text>
<text x="{x+113}" y="435" text-anchor="middle" style="font:600 24px Plex" fill="#9FC3DD">{ijk}</text></g>'''


H35 = dict(hook="G18 = எந்த plane?", hsize=86, hook2="3 வினாடியில் பதில்?", s=0, e=4.0, svg=f'''
<text class="fig" x="24" y="44">QUICK CHECK</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">HAAS MILL EXAMPLE</text>
<circle class="until" data-end="3.0" cx="389" cy="250" r="140" fill="none" stroke="#2E5878" stroke-width="18"/>
<circle class="draw" data-t="0" data-d="3.0" data-lin="1" data-hide="1" pathLength="1" cx="389" cy="250" r="140" fill="none" stroke="{OR}" stroke-width="18" transform="rotate(-90 389 250)"/>
<text class="count" data-t="0" data-n="3" x="389" y="295" text-anchor="middle" style="font:800 130px Inter" fill="#fff">3</text>
<g style="font:700 50px Inter" fill="#fff">
<rect x="40" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="145" y="553" text-anchor="middle">XY</text>
<rect x="284" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="389" y="553" text-anchor="middle">XZ</text>
<rect x="528" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="633" y="553" text-anchor="middle">YZ</text></g>
<text x="389" y="690" text-anchor="middle" style="font:600 30px Inter" fill="#9FC3DD">ANSWER IN THIS REEL</text>''')

R35 = dict(id="35", slug="G17_G18_G19_Planes", scenes=[
 H35,
 dict(s=4.0, e=10.5, tag="ANSWER  /  02", title="G18 = XZ plane", tsize=78, sub="G17 XY · G18 XZ · G19 YZ", ssize=44,
      svg=fig("ARC PLANE (G02 / G03)", "HAAS MILL EXAMPLE", orange=True)
          + plane_card(40, "G17", "XY", "X", "Y", "I  J", 0.2)
          + plane_card(276, "G18", "XZ", "X", "Z", "I  K", 0.6, hl=True)
          + plane_card(512, "G19", "YZ", "Y", "Z", "J  K", 1.0)
          + '<text class="m a" data-t="1.6" x="389" y="495" text-anchor="middle" style="font-size:22px">ARC CENTRE LETTERS FOLLOW THE PLANE</text>',
      body="Arc எந்த இரண்டு axis-ல் நகரும் என்பதை plane தீர்மானிக்கும்.", body_t=1.2),
 dict(s=10.5, e=17.0, tag="EXAMPLE  /  03", title="Same G02, new plane", tsize=66, sub="G17 → XY-ல் arc", ssize=48,
      svg=fig("SCHEMATIC", "HAAS MILL EXAMPLE", orange=True) + code(30, 60, [
          [("G17 ", GRN), ("G02 X__ Y__ I__ J__", W)],
          [("G18 ", OR), ("G02 X__ Z__ I__ K__", W)],
          [("G19 ", "#9FC3DD"), ("G02 Y__ Z__ J__ K__", W)],
      ], t0=0.2, dt=0.5, size=30, lh=52, w=718) + f'''
<text class="a" data-t="1.8" x="40" y="300" style="font:700 30px Inter" fill="#fff">ONE PLANE ACTIVE AT A TIME</text>
<text class="a" data-t="2.2" x="40" y="350" style="font:700 30px Inter" fill="{OR}">ARC USES ONLY THOSE TWO AXES</text>
<text class="m a" data-t="2.6" x="40" y="420" style="font-size:22px">__ = YOUR PROGRAM'S VALUES</text>
<text class="m a" data-t="2.6" x="40" y="460" style="font-size:22px">A THIRD-AXIS VALUE GIVES A HELIX (SEE MANUAL)</text>''',
      body="தவறான plane-ல் arc வேறு முகத்தில் வெட்டும்.", body_t=3.0),
 dict(s=17.0, e=23.5, tag="CHECK  /  04", title="Modal + default", tsize=74, sub="Power-on: G17", ssize=50,
      svg=fig("HAAS MILL EXAMPLE") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "G17 = POWER-ON DEFAULT", "Haas workbook-படி", 0.3)
          + checkrow(255, 2, "MODAL", "அடுத்த plane code வரை தொடரும்", 0.8)
          + checkrow(395, 3, "G41 / G42 → G17 (XY)", "Haas 2D cutter comp XY-ல் மட்டும்", 1.3),
      body="மற்ற control-களுக்கு அவற்றின் manual பாருங்கள்.", body_t=1.8),
 dict(s=23.5, e=30.0, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="G18 = XZ", ssize=50,
      svg=fig("HOW TO ANSWER") + f'''
{"".join(f'<g class="a" data-t="{0.2 + k*0.3:.1f}">{box(40 + k*244, 70, 210, 140, OR if c == "G18" else LINE, 3)}<text x="{145 + k*244}" y="132" text-anchor="middle" style="font:800 44px Inter" fill="{OR if c == "G18" else "#fff"}">{c}</text><text x="{145 + k*244}" y="182" text-anchor="middle" style="font:700 32px Inter" fill="#fff">{p}</text></g>' for k, (c, p) in enumerate([("G17", "XY"), ("G18", "XZ"), ("G19", "YZ")]))}
<text class="w a" data-t="1.2" x="40" y="290" style="font-size:30px">"Arc-க்கு முன் plane-ஐ சரிபார்ப்பேன்."</text>
<text class="m a" data-t="1.6" x="40" y="370" style="font-size:24px">IJ · IK · JK</text>
<text class="m a" data-t="1.8" x="40" y="430" style="font-size:22px">G-CODES CAN DIFFER BY CONTROL. CHECK YOUR MANUAL.</text>''',
      body="I, J, K எழுத்துகளையும் சேர்த்துச் சொல்லுங்கள்.", body_t=1.8, cta=True, cta_t=2.6),
])

# =====================================================================================================
# REEL 36: Reading a Haas safe-start line (Haas mill example). Target 30 s.
# Hook format: (3) wrong vs right. Options considered:
#   "Tool 2: X50. → X90?" (wrong value first, G91 left over from tool 1; chosen) / "G00 G90 G17 G40 G49 G54?" (interview) /
#   "Safe line இல்லாமல் tool change" (cold-open demo)
# Sources: Productivity Inc. "Mill Programming 2025" p.34: "G00 G90 G17 G40 G49 G54 (Safe startup)"; "It is good machining
#   practice to place this block of code after every tool change"; G00 rapid, G90 absolute, G17 XY plane, G40 cancels cutter
#   comp, G49 cancels tool length comp, G54 selects the G54 work offset. G80 is NOT in that line: Haas Mill Programming
#   Workbook (2000) "G80 Canned Cycle Cancel", "a canned cycle is active until canceled with the G80 code", and G80 is in the
#   power-up defaults list; so G80 is shown only as "check your shop template". G91 modal (reel 17 sources).
#   From X40: G91 left on -> X50. ends at X90; after the safe line (G90) -> X50.


def xl(mm):
    return 60 + mm * 4


H36 = dict(hook="Tool 2: X50. → X90?", hsize=80, hook2="Tool 1-ன் G91 மீதம்!", s=0, e=4.2, svg=f'''
<text class="fig" x="24" y="44">TOP VIEW · SCHEMATIC · mm</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">HAAS MILL EXAMPLE</text>
<rect x="30" y="74" width="718" height="120" rx="10" fill="#0A2236" stroke="{RED}" stroke-width="3"/>
<text class="code" x="52" y="122" style="font-size:32px"><tspan fill="#7FA6C4">N20 </tspan>T2 M06</text>
<text class="code" x="52" y="170" style="font-size:32px"><tspan fill="#7FA6C4">N30 </tspan>G00 X50. <tspan fill="{RED}"> (G91 STILL ON)</tspan></text>
<text x="40" y="250" style="font:800 34px Inter" fill="{RED}">WRONG: X40 + 50 = X90</text>
<rect class="grow" data-t="0" data-d="1.6" data-w="200" x="{xl(40)}" y="307" width="0" height="6" fill="{RED}"/>
<g class="move" data-t="0" data-d="1.6" data-dx="200"><circle cx="{xl(40)}" cy="310" r="26" fill="{RED}" stroke="#fff" stroke-width="3"/></g>
<g class="a" data-t="1.8"><rect x="30" y="400" width="718" height="120" rx="10" fill="#0A2236" stroke="{GRN}" stroke-width="3"/>
<text class="code" x="52" y="448" style="font-size:30px"><tspan fill="#7FA6C4">N30 </tspan><tspan fill="{GRN}">G00 G90 G17 G40 G49 G54</tspan></text>
<text class="code" x="52" y="496" style="font-size:30px"><tspan fill="#7FA6C4">N40 </tspan>X50.</text></g>
<g class="a" data-t="2.2"><text x="40" y="580" style="font:800 34px Inter" fill="{GRN}">RIGHT: X50</text>
<circle cx="{xl(50)}" cy="310" r="26" fill="none" stroke="{GRN}" stroke-width="4" stroke-dasharray="9 7"/></g>
<path d="M40 680H740" stroke="#7FA6C4" stroke-width="2"/>
<g style="font:600 26px Plex"><path d="M{xl(40)} 680v-14M{xl(50)} 680v-14M{xl(90)} 680v-14" stroke="#7FA6C4" stroke-width="2"/>
<text x="{xl(40)-10}" y="720" text-anchor="end" fill="#BFD6E8">X40</text><text x="{xl(50)+10}" y="720" fill="{GRN}">X50</text>
<text x="{xl(90)}" y="720" text-anchor="middle" fill="{RED}">X90</text></g>''')

SAFE = [("G00", "RAPID MODE"), ("G90", "ABSOLUTE"), ("G17", "XY PLANE"), ("G40", "CUTTER COMP CANCEL"),
        ("G49", "TOOL LENGTH COMP CANCEL"), ("G54", "WORK OFFSET G54")]

R36 = dict(id="36", slug="Haas_Safe_Start_Line", scenes=[
 H36,
 dict(s=4.2, e=11.0, tag="READ  /  02", title="Safe start line", tsize=76, sub="ஒவ்வொரு code-ம் ஒரு mode", ssize=46,
      svg=fig("HAAS MILL EXAMPLE", "SOURCE: PRODUCTIVITY INC.", orange=True) + f'''
<rect x="30" y="60" width="718" height="70" rx="10" fill="#0A2236" stroke="#2E5878" stroke-width="2"/>
<text class="code a" data-t="0.1" x="52" y="107" style="font-size:34px" fill="{GRN}">G00 G90 G17 G40 G49 G54</text>
''' + "".join(f'<g class="a" data-t="{0.4 + k*0.35:.2f}"><text x="60" y="{186 + k*55}" style="font:700 30px Plex" fill="{OR}">{c}</text><text x="170" y="{186 + k*55}" style="font:700 28px Inter" fill="#fff">{d}</text></g>' for k, (c, d) in enumerate(SAFE)),
      body="Tool change-க்குப் பின் mode-களை தெரிந்த நிலைக்குக் கொண்டுவரும்.", body_t=2.6),
 dict(s=11.0, e=17.6, tag="WRONG vs RIGHT  /  03", title="Leftover modes", tsize=76, sub="G90 → X50, X90 அல்ல", ssize=46,
      svg=fig("LEFT ON FROM TOOL 1", "SCHEMATIC") + f'''
<text x="40" y="92" style="font:600 22px Plex" fill="#9FC3DD">LEFT ON</text><text x="200" y="92" style="font:600 22px Plex" fill="#9FC3DD">WHAT GOES WRONG</text><text x="738" y="92" text-anchor="end" style="font:600 22px Plex" fill="#9FC3DD">FIX</text>
''' + "".join(f'''<g class="a" data-t="{0.3 + k*0.6:.1f}">{box(30, 112 + k*118, 718, 100, LINE, 2)}
<text x="50" y="{173 + k*118}" style="font:800 34px Plex" fill="{RED}">{a}</text>
<text x="200" y="{173 + k*118}" style="font:700 26px Inter" fill="#fff">{b}</text>
<text x="728" y="{173 + k*118}" text-anchor="end" style="font:800 34px Plex" fill="{GRN}">{c}</text></g>''' for k, (a, b, c) in enumerate([
          ("G91", "X50. → X90, NOT X50", "G90"),
          ("G18", "G02 ARC IN XZ, NOT XY", "G17"),
          ("G41", "PATH STILL OFFSET BY COMP", "G40")])) + '''
<text class="m a" data-t="2.2" x="389" y="490" text-anchor="middle" style="font-size:22px">START X40 · METRIC · HAAS MILL EXAMPLE</text>''',
      body="Safe line இல்லையெனில் முந்தைய mode தொடரலாம்.", body_t=2.4),
 dict(s=17.6, e=24.0, tag="CHECK  /  04", title="Where and what", tsize=74, sub="Shop template பாருங்கள்.", ssize=46,
      svg=fig("OPERATOR CHECK") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "AFTER EVERY TOOL CHANGE", "Productivity Inc. பரிந்துரை", 0.3)
          + checkrow(255, 2, "G80 IN YOUR LINE?", "G80 = canned cycle cancel", 0.8)
          + checkrow(395, 3, "NOT UNIVERSAL", "Control, shop-க்கு ஏற்ப மாறும்", 1.3),
      body="உங்கள் program-ன் முதல் வரிகளைப் படித்துப் பாருங்கள்.", body_t=1.8),
 dict(s=24.0, e=30.4, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="G90 → X50, X90 அல்ல", ssize=46,
      svg=fig("HOW TO ANSWER", "HAAS MILL EXAMPLE", orange=True) + f'''
<rect x="30" y="66" width="718" height="80" rx="10" fill="#0A2236" stroke="{GRN}" stroke-width="3"/>
<text class="code a" data-t="0.2" x="52" y="119" style="font-size:36px" fill="{GRN}">G00 G90 G17 G40 G49 G54</text>
<text class="a" data-t="0.6" x="40" y="215" style="font:700 28px Inter" fill="#fff">RAPID · ABSOLUTE · XY · COMP OFF</text>
<text class="a" data-t="0.8" x="40" y="260" style="font:700 28px Inter" fill="#fff">LENGTH COMP OFF · G54</text>
<text class="w a" data-t="1.2" x="40" y="350" style="font-size:30px">"தெரிந்த நிலையில் ஆரம்பிக்க safe line."</text>
<text class="m a" data-t="1.6" x="40" y="440" style="font-size:22px">G-CODES CAN DIFFER BY CONTROL. CHECK YOUR MANUAL.</text>''',
      body="ஒவ்வொரு code-ன் வேலையையும் சொல்லுங்கள்.", body_t=1.8, cta=True, cta_t=2.6),
])

# =====================================================================================================
# REEL 37: Interview "Tell me about your machine". Target 30 s.
# Hook format: (4) verbatim interview question. Options considered:
#   "“Tell me about your machine.”" + "5 விஷயம்" (chosen; number = 5 facts) / "Travels X ___ Y ___ Z ___?" (quiz) /
#   "Machine spec-ஐ ஊகிக்காதீர்கள்" (wrong vs right)
# No machine numbers stated as fact: every value is a blank placeholder. Generic interview guidance; no technical source needed.
FACTS = [("CONTROL", "______"), ("TRAVELS", "X ___  Y ___  Z ___  mm"), ("TOOLS (ATC)", "___ tools"),
         ("MATERIALS", "______"), ("PARTS / WORK", "______")]

H37 = dict(hook="“Tell me about your machine.”", hsize=55, hook2="5 விஷயங்களில் பதில்.", h2size=56, s=0, e=4.2, svg=f'''
<text class="fig" x="24" y="44">INTERVIEW QUESTION</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">FILL WITH YOUR OWN FACTS</text>
''' + "".join(f'''<g><circle cx="70" cy="{120 + k*120}" r="30" fill="{OR}"/><text x="70" y="{131 + k*120}" text-anchor="middle" style="font:700 32px Inter" fill="{PANEL}">{k+1}</text>
<text x="124" y="{112 + k*120}" style="font:700 30px Inter" fill="#fff">{lab}</text>
<rect class="grow" data-t="{k*0.45:.2f}" data-d="0.5" data-w="560" x="124" y="{140 + k*120}" width="0" height="4" fill="{OR}"/>
<text class="a" data-t="{0.2 + k*0.45:.2f}" x="124" y="{170 + k*120}" style="font:600 26px Plex" fill="#9FC3DD" xml:space="preserve">{val}</text></g>''' for k, (lab, val) in enumerate(FACTS)) + f'''
<text class="a" data-t="2.8" x="389" y="730" text-anchor="middle" style="font:800 30px Inter" fill="{OR}">ONLY WHAT YOU ACTUALLY RAN</text>''')

R37 = dict(id="37", slug="Tell_Me_About_Your_Machine", scenes=[
 H37,
 dict(s=4.2, e=11.0, tag="ANSWER  /  02", title="5 facts", tsize=86, sub="நீங்கள் ஓட்டியது மட்டும்.", ssize=48,
      svg=fig("YOUR MACHINE · YOUR FACTS") + "".join(
          f'<g class="a" data-t="{0.2 + k*0.35:.2f}"><text x="40" y="{100 + k*86}" style="font:800 34px Inter" fill="{OR}">{k+1}</text>'
          f'<text x="90" y="{100 + k*86}" style="font:700 30px Inter" fill="#fff">{lab}</text>'
          f'<text x="90" y="{138 + k*86}" class="ta" style="font-size:26px">{ta}</text></g>'
          for k, (lab, ta) in enumerate([("CONTROL", "எந்த control-ல் வேலை செய்தீர்கள்"), ("AXIS TRAVELS", "X, Y, Z – manual / spec sheet-ல்"),
                                         ("TOOL CAPACITY", "ATC-ல் எத்தனை tool"), ("MATERIALS", "நீங்கள் வெட்டிய material"),
                                         ("PARTS AND YOUR ROLE", "என்ன part, நீங்கள் என்ன செய்தீர்கள்")])),
      body="ஒவ்வொன்றையும் உங்கள் உண்மை விவரத்தால் நிரப்புங்கள்.", body_t=2.2),
 dict(s=11.0, e=17.6, tag="EXAMPLE  /  03", title="Answer shape", tsize=80, sub="Blank = உங்கள் விவரம்", ssize=48,
      svg=fig("TEMPLATE · NOT REAL DATA", "PLACEHOLDERS", orange=True) + code(30, 60, [
          [("“I ran a VMC with ", W), ("___", OR), (" control.”", W)],
          [("“Travels X ", W), ("___", OR), (" Y ", W), ("___", OR), (" Z ", W), ("___", OR), (" mm.”", W)],
          [("“", W), ("___", OR), ("-tool ATC.”", W)],
          [("“Material: ", W), ("___", OR), (". Parts: ", W), ("___", OR), (".”", W)],
          [("“I did ", W), ("___", OR), (" (setup / offsets).”", W)],
      ], t0=0.2, dt=0.45, size=28, lh=72, w=718, h=400),
      body="ஒவ்வொரு வரியும் நீங்கள் செய்ததைக் காட்டட்டும்.", body_t=2.6),
 dict(s=17.6, e=24.0, tag="CHECK  /  04", title="Don't guess", tsize=80, sub="எண் தெரியாவிட்டால்?", ssize=48,
      svg=fig("HONEST ANSWER") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "NO INVENTED NUMBERS", "“நினைவில்லை” என்று சொல்லலாம்", 0.3)
          + checkrow(255, 2, "CHECK BEFOREHAND", "Machine manual / spec sheet பாருங்கள்", 0.8)
          + checkrow(395, 3, "SAY WHAT YOU DID", "Setup, offset, inspection – உங்கள் பங்கு", 1.3),
      body="இல்லாத machine அனுபவத்தைச் சொல்லாதீர்கள்.", body_t=1.8),
 dict(s=24.0, e=30.4, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="5 facts, உங்கள் machine", ssize=48,
      svg=fig("HOW TO ANSWER") + "".join(
          f'<g class="a" data-t="{0.2 + k*0.2:.1f}">{box(x, y, w, 70, OR, 3)}<text x="{x + w/2:.0f}" y="{y + 47}" text-anchor="middle" style="font:700 28px Inter" fill="#fff">{lab}</text></g>'
          for k, (lab, x, y, w) in enumerate([("CONTROL", 40, 66, 220), ("TRAVELS", 280, 66, 220), ("TOOLS", 520, 66, 218),
                                              ("MATERIALS", 40, 156, 340), ("PARTS / ROLE", 398, 156, 340)])) + '''
<text class="w a" data-t="1.4" x="40" y="320" style="font-size:30px">"நான் ஓட்டியதை மட்டும் சொல்வேன்."</text>
<text class="m a" data-t="1.8" x="40" y="420" style="font-size:22px">NO MACHINE NUMBERS ARE GIVEN HERE ON PURPOSE</text>''',
      body="முன்பே ஒரு முறை சொல்லிப் பழகுங்கள்.", body_t=2.0, cta=True, cta_t=2.6, cta_icon="send", cta_text=SEND),
])

# =====================================================================================================
# REEL 38: 5S on the shop floor. Target 20 s.
# Hook format: (2) countdown quiz. Options considered:
#   "Seiton = ?" (quiz: SORT / SET IN ORDER / SHINE; chosen, specific term) / "5S-ல் 5 என்ன?" (interview question) /
#   "Seiso = Sort?" (wrong vs right)
# Sources: ASQ "What is 5S?" (asq.org/quality-resources/five-s-tutorial): Seiri = Sort, Seiton = Set in order, Seiso = Shine,
#   Seiketsu = Standardize, Shitsuke = Sustain, with definitions ("set in order, organize, and arrange ... tools ... for ease of
#   use"; "shine by ... cleaning, and inspecting"; "sustain ... forming the habit of always following the first four S's").
#   Lean Enterprise Institute lexicon "5S": same Japanese terms; LEI translates Seiton as "Straighten" (shown in caption).
#   VMC examples are illustrations of those definitions, not quoted from the sources.
H38 = dict(hook="Seiton = ?", hsize=104, hook2="3 வினாடியில் பதில்?", s=0, e=3.6, svg=f'''
<text class="fig" x="24" y="44">QUICK CHECK · 5S</text>
<circle class="until" data-end="3.0" cx="389" cy="250" r="140" fill="none" stroke="#2E5878" stroke-width="18"/>
<circle class="draw" data-t="0" data-d="3.0" data-lin="1" data-hide="1" pathLength="1" cx="389" cy="250" r="140" fill="none" stroke="{OR}" stroke-width="18" transform="rotate(-90 389 250)"/>
<text class="count" data-t="0" data-n="3" x="389" y="295" text-anchor="middle" style="font:800 130px Inter" fill="#fff">3</text>
<g style="font:700 34px Inter" fill="#fff">
<rect x="40" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="145" y="547" text-anchor="middle">SORT</text>
<rect x="284" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="389" y="527" text-anchor="middle">SET IN</text><text x="389" y="569" text-anchor="middle">ORDER</text>
<rect x="528" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="633" y="547" text-anchor="middle">SHINE</text></g>
<text x="389" y="690" text-anchor="middle" style="font:600 30px Inter" fill="#9FC3DD">ANSWER IN THIS REEL</text>''')

FIVE_S = [("SEIRI", "SORT"), ("SEITON", "SET IN ORDER"), ("SEISO", "SHINE"), ("SEIKETSU", "STANDARDISE"), ("SHITSUKE", "SUSTAIN")]

R38 = dict(id="38", slug="5S_Shop_Floor", scenes=[
 H38,
 dict(s=3.6, e=7.8, tag="ANSWER  /  02", title="Seiton = Set in order", tsize=64, sub="5S: ஐந்து படிகள்", ssize=48,
      svg=fig("5S", "SOURCE: ASQ", orange=True) + "".join(
          f'<g class="a" data-t="{0.1 + k*0.25:.2f}">{box(40, 62 + k*88, 698, 74, OR if k == 1 else LINE, 3 if k == 1 else 2)}'
          f'<text x="64" y="{110 + k*88}" style="font:800 30px Inter" fill="{OR}">{k+1}</text>'
          f'<text x="110" y="{110 + k*88}" style="font:700 30px Plex" fill="{OR if k == 1 else "#fff"}">{j}</text>'
          f'<text x="714" y="{110 + k*88}" text-anchor="end" style="font:700 30px Inter" fill="{OR if k == 1 else "#fff"}">{e}</text></g>'
          for k, (j, e) in enumerate(FIVE_S)),
      body="ஒவ்வொரு பொருளுக்கும் ஓர் இடம்.", body_t=1.4),
 dict(s=7.8, e=12.0, tag="AT THE VMC  /  03", title="S1 – S3", tsize=80, sub="VMC உதாரணங்கள்", ssize=48,
      svg=fig("VMC EXAMPLE") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "SORT", "தேவையில்லாத holder-ஐ அகற்று", 0.2)
          + checkrow(255, 2, "SET IN ORDER", "Tool rack-ல் label, நிலையான இடம்", 0.6)
          + checkrow(395, 3, "SHINE", "Table, vise chip சுத்தம் + பார்வை", 1.0)),
 dict(s=12.0, e=16.2, tag="AT THE VMC  /  04", title="S4 – S5", tsize=80, sub="பழக்கமாக மாற்றுங்கள்", ssize=48,
      svg=fig("VMC EXAMPLE") + '<path d="M30 260H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(150, 4, "STANDARDISE", "Shift-end 5S checklist", 0.2)
          + checkrow(370, 5, "SUSTAIN", "ஒவ்வொரு shift-ம் பின்பற்று", 0.6),
      body="முதல் மூன்றையும் தினமும் செய்வதே S4, S5.", body_t=1.0),
 dict(s=16.2, e=20.4, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="Seiton = Set in order", ssize=48,
      svg=fig("HOW TO ANSWER") + "".join(
          f'<g class="a" data-t="{0.1 + k*0.15:.2f}">{box(x, y, w, 70, OR if k == 1 else LINE, 3)}<text x="{x + w/2:.0f}" y="{y + 47}" text-anchor="middle" style="font:700 28px Inter" fill="{OR if k == 1 else "#fff"}">{lab}</text></g>'
          for k, (lab, x, y, w) in enumerate([("SORT", 40, 66, 200), ("SET IN ORDER", 258, 66, 280), ("SHINE", 556, 66, 182),
                                              ("STANDARDISE", 40, 156, 340), ("SUSTAIN", 398, 156, 340)])) + '''
<text class="w a" data-t="1.0" x="40" y="320" style="font-size:30px">"ஒவ்வொரு S-க்கும் ஒரு VMC உதாரணம்."</text>
<text class="m a" data-t="1.3" x="40" y="420" style="font-size:22px">TERMS: ASQ · LEAN ENTERPRISE INSTITUTE</text>''',
      cta=True, cta_t=1.6),
])

REELS = [R34, R35, R36, R37, R38]
