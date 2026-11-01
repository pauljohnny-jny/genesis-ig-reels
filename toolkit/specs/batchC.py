from gen import *
W = "#E6F0F7"

# ---------------- REEL 09: G41 / G42 ----------------
def path_line(t=0.2):
    return f'''<g class="a" data-t="{t}"><path d="M70 270H690" stroke="#fff" stroke-width="4" stroke-dasharray="16 10" marker-end="url(#aw)"/>
<text class="m" x="70" y="250" style="fill:#fff">PROGRAMMED PATH</text><text class="m" x="600" y="320">TRAVEL</text></g>'''

def tool(cx, cy, r=46, col="#6C93B4", lab="", labcol="#fff", t=0.6):
    return f'''<g class="a" data-t="{t}"><circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" stroke="{LINE}" stroke-width="3"/>
{f'<text x="{cx}" y="{cy+12}" text-anchor="middle" style="font:700 34px Inter" fill="{labcol}">{esc(lab)}</text>' if lab else ""}</g>'''

R09 = dict(id="09", slug="G41_vs_G42", scenes=[
 dict(s=0, e=5, tag="CUTTER COMP  /  01", title="G41 or G42?", sub="எந்தப் பக்கம்?",
      svg=fig("TOP VIEW", "SCHEMATIC") + path_line(0) + tool(389, 200, lab="?", t=0) + tool(389, 340, lab="?", t=0),
      body="Program path ஒன்றுதான். Tool அதன் இடது பக்கமா, வலது பக்கமா?"),
 dict(s=5, e=11.5, tag="RULE  /  02", title="Look along travel", tsize=68, sub="பயணத் திசையில் பாருங்கள்.", ssize=42,
      svg=fig("TOP VIEW", "SCHEMATIC") + path_line(0) + tool(389, 200, col=OR, lab="", t=0.3) + tool(389, 340, lab="", t=0.6) + f'''
<text class="a" data-t="0.9" x="460" y="190" style="font:700 36px Inter" fill="{OR}">G41 · LEFT</text>
<text class="a" data-t="1.3" x="460" y="370" style="font:700 36px Inter" fill="#fff">G42 · RIGHT</text>
<g class="a" data-t="1.8"><path d="M80 420H200" stroke="{OR}" stroke-width="4" marker-end="url(#ao)"/><text class="mo" x="40" y="470">YOU, FACING THE TRAVEL</text></g>''',
      body="Tool செல்லும் திசையை நோக்கி நின்றால்: இடது = G41, வலது = G42."),
 dict(s=11.5, e=18, tag="CLIMB  /  03", title="G41 + M03", sub="= Climb milling.",
      svg=fig("OUTSIDE PROFILE", "SCHEMATIC") + f'''
<g class="a" data-t="0.2"><rect x="230" y="150" width="320" height="230" fill="{STEEL}" stroke="#fff" stroke-width="3"/><text class="m" x="390" y="275" text-anchor="middle" style="fill:#fff">PART</text></g>
<rect class="a" data-t="0.6" x="192" y="112" width="396" height="306" rx="38" fill="none" stroke="{OR}" stroke-width="3" stroke-dasharray="12 8"/>
<g class="a" data-t="1.0"><path d="M300 112H470" stroke="{OR}" stroke-width="5" marker-end="url(#ao)"/><path d="M588 200V330" stroke="{OR}" stroke-width="5" marker-end="url(#ao)"/>
<path d="M480 418H310" stroke="{OR}" stroke-width="5" marker-end="url(#ao)"/><path d="M192 330V200" stroke="{OR}" stroke-width="5" marker-end="url(#ao)"/></g>
{tool(389, 112, r=38, t=1.4)}
<text class="mo a" data-t="1.8" x="24" y="478">CLOCKWISE · TOOL LEFT OF PATH → G41</text>''',
      body="M03 spindle-உடன், G41 பயன்படுத்தினால் climb milling."),
 dict(s=18, e=24.5, tag="SWITCH ON  /  04", title="Turning it on", sub="இந்த விதிகள்.",
      svg=fig("RULES", "SOURCE: HAAS TRAINING") + code(30, 90, [[("G01 ", W), ("G41 D01", OR), (" X0. Y0. F300.", W)], [("(... profile ...)", "#7FA6C4")], [("G01 ", W), ("G40", OR), (" X-20. Y-20.", W)]], t0=0.2, dt=0.3, w=718, label="EXAMPLE · HAAS-STYLE")
          + tick(52, 320, 1.2) + '<text class="w a" data-t="1.2" x="90" y="331">Lead-in: G01 line ≥ tool radius</text>'
          + cross(52, 385, 1.7) + '<text class="w a" data-t="1.7" x="90" y="396">Not on a G02 / G03 arc</text>'
          + tick(52, 450, 2.2) + '<text class="w a" data-t="2.2" x="90" y="461">Cancel with G40</text>',
      body="G41/G42-ஐ G01 நேர்க்கோட்டு நகர்வில் ஆன் செய்யுங்கள்; arc-ல் அல்ல."),
 dict(s=24.5, e=31, tag="INTERVIEW  /  05", title="Interview tip", sub="D-ல் என்ன இருக்கிறது?",
      svg=fig("Ø10 CUTTER", "EXAMPLE VALUES", orange=True) + f'''
<g class="a" data-t="0.3"><rect x="30" y="80" width="718" height="150" rx="12" fill="#123A57" stroke="{LINE}" stroke-width="2.5"/>
<text class="m" x="60" y="130">DIAMETER MODE</text><text x="60" y="195" style="font:600 42px Inter" fill="#fff">D01 = 10.000</text></g>
<g class="a" data-t="0.9"><rect x="30" y="255" width="718" height="150" rx="12" fill="#123A57" stroke="{LINE}" stroke-width="2.5"/>
<text class="m" x="60" y="305">RADIUS MODE</text><text x="60" y="370" style="font:600 42px Inter" fill="#fff">D01 = 5.000</text></g>
<text class="mo a" data-t="1.5" x="30" y="460">HAAS: SETTING 40 SELECTS THE MODE</text>''',
      body="உங்கள் machine D-ஐ radius-ஆ, diameter-ஆ எடுக்கிறது?", body_t=1.8, cta=True, cta_t=2.4),
])

# ---------------- REEL 10: G81 / G83 / G73 ----------------
TOPY, RY, ZY = 300, 250, 460

def block(t=0.1, label=True):
    lab = f'<text class="m" x="44" y="{RY-10}" style="font-size:22px;fill:#fff">R PLANE</text><text class="m" x="50" y="482" style="fill:{PANEL};font-size:22px">PART</text>' if label else ""
    return f'''<g class="a" data-t="{t}"><rect x="30" y="{TOPY}" width="718" height="200" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<path d="M30 {RY}H748" stroke="#fff" stroke-width="2" stroke-dasharray="10 8"/>{lab}</g>'''

def drill_path(x, kind, t0=0.4, step=0.35):
    """feed strokes orange solid; retracts white dashed. kind: g81/g83/g73"""
    segs = []
    if kind == "g81":
        segs = [("f", RY, ZY), ("r", ZY, RY)]
    elif kind == "g83":
        segs = [("f", RY, 330), ("r", 330, RY), ("f", RY + 5, 400), ("r", 400, RY), ("f", RY + 5, ZY), ("r", ZY, RY)]
    elif kind == "g73":
        segs = [("f", RY, 330), ("r", 330, 314), ("f", 314, 400), ("r", 400, 384), ("f", 384, ZY), ("r", ZY, RY)]
    out = []
    for k, (typ, a, b) in enumerate(segs):
        xx = x - 18 + k * 7
        if typ == "f":
            out.append(f'<path class="draw" data-t="{t0 + k*step:.2f}" data-d="{step:.2f}" pathLength="1" d="M{xx} {a}V{b}" stroke="{OR}" stroke-width="5" fill="none"/>')
        else:
            out.append(f'<path class="a" data-t="{t0 + k*step:.2f}" d="M{xx} {a}V{b}" stroke="#fff" stroke-width="3" stroke-dasharray="6 6" fill="none"/>')
    return "".join(out)

R10 = dict(id="10", slug="G81_G83_G73_Drilling", scenes=[
 dict(s=0, e=5.5, tag="DRILLING  /  01", title="G81, G83, G73", sub="எது எப்போது?",
      svg=fig("SIDE VIEW", "SCHEMATIC") + block(0, label=False) + drill_path(150, "g81", 0.2, 0.3) + drill_path(389, "g83", 0.2, 0.3) + drill_path(628, "g73", 0.2, 0.3)
          + "".join(f'<text x="{x}" y="150" text-anchor="middle" style="font:700 44px Inter" fill="#fff">{g}</text>' for x, g in ((150, "G81"), (389, "G83"), (628, "G73")))
          + f'<text class="m" x="44" y="{RY-10}" style="font-size:22px;fill:#fff">R</text>',
      body="மூன்றும் drilling cycle. வித்தியாசம் chip-ஐ வெளியேற்றும் விதத்தில்."),
 dict(s=5.5, e=11.5, tag="G81  /  02", title="G81", sub="நேராக, ஒரே முறை.",
      svg=fig("SIDE VIEW", "SCHEMATIC") + block() + drill_path(300, "g81", 0.4, 0.6) + f'''
<text class="mo a" data-t="0.6" x="360" y="160">FEED TO Z DEPTH</text><text class="m a" data-t="1.4" x="360" y="205" style="fill:#fff">RAPID OUT (DASHED)</text>
<text class="a" data-t="0.2" x="40" y="150" style="font:700 44px Inter" fill="#fff">G81</text>''',
      body="ஆழம் குறைந்த துளைகளுக்கு, அல்லது through-spindle coolant உடன்."),
 dict(s=11.5, e=18, tag="G83  /  03", title="G83", sub="Peck + முழு retract.",
      svg=fig("SIDE VIEW", "SCHEMATIC") + block() + drill_path(300, "g83", 0.3, 0.4) + f'''
<g class="a" data-t="0.8"><path d="M250 {RY}V330" stroke="{OR}" stroke-width="2.5" marker-start="url(#ao)" marker-end="url(#ao)"/><text class="mo" x="100" y="300">Q = PECK</text></g>
<text class="m a" data-t="1.5" x="360" y="200" style="fill:#fff">FULL RETRACT TO R</text>
<text class="a" data-t="0.2" x="40" y="150" style="font:700 44px Inter" fill="#fff">G83</text>''',
      body="ஒவ்வொரு Q ஆழத்துக்கும் R plane வரை வெளியே வந்து chip-ஐ வெளியேற்றும்."),
 dict(s=18, e=24, tag="G73  /  04", title="G73", sub="Peck + சிறிய retract.",
      svg=fig("SIDE VIEW", "SCHEMATIC") + block() + drill_path(300, "g73", 0.3, 0.4) + f'''
<g class="a" data-t="1.0"><path d="M330 322L420 170" stroke="#fff" stroke-width="2"/><text class="m" x="430" y="160" style="fill:#fff">SMALL RETRACT</text>
<text class="m" x="430" y="196">(MACHINE SETTING)</text></g>
<text class="mo a" data-t="1.6" x="430" y="236">BREAKS THE CHIP</text>
<text class="a" data-t="0.2" x="40" y="150" style="font:700 44px Inter" fill="#fff">G73</text>''',
      body="சிறிது மட்டும் பின்வாங்கி chip-ஐ உடைக்கும்; retract அளவு machine setting-ல்."),
 dict(s=24, e=31, tag="CODE CHECK  /  05", title="Code check", sub="ஒவ்வொரு எழுத்தும் என்ன?", ssize=44,
      svg=fig("G83", "VALUES ILLUSTRATIVE", orange=True) + code(30, 100, [[("G98 G83 ", W), ("Z-30.", OR), (" ", W), ("R2.", OR), (" ", W), ("Q5.", OR), (" F120.", W)], [("X20.", W)], [("G80", OR)]], t0=0.2, dt=0.3, w=718, label="EXAMPLE · HAAS / FANUC-STYLE")
          + "".join(f'<text class="a" data-t="{1.0+k*0.35:.2f}" x="{40 if k<2 else 400}" y="{340 + (k%2)*60}" style="font:500 28px Plex"><tspan fill="{OR}">{a}</tspan><tspan fill="#fff"> = {b}</tspan></text>'
                    for k, (a, b) in enumerate([("Z", "final depth"), ("R", "retract plane"), ("Q", "peck depth"), ("G80", "cancel")])),
      body="Cycle முடிந்ததும் G80 மூலம் cancel செய்ய மறக்காதீர்கள்.", body_t=1.8, cta=True, cta_t=2.4),
])

# ---------------- REEL 11: rigid tapping feed ----------------
def options(correct=None, t0=0.3):
    out = []
    for k, (L, v) in enumerate([("A", "F600"), ("B", "F900"), ("C", "F150")]):
        y = 90 + k * 130
        ok = correct == L
        stroke = GRN if ok else "#2E5878"
        op = "" if (correct is None or ok) else ' opacity="0.35"'
        out.append(f'''<g class="a" data-t="{t0 + k*0.3:.1f}"{op}><rect x="30" y="{y}" width="380" height="100" rx="14" fill="#123A57" stroke="{stroke}" stroke-width="{4 if ok else 2}"/>
<circle cx="85" cy="{y+50}" r="30" fill="{OR}"/><text x="85" y="{y+62}" text-anchor="middle" style="font:700 32px Inter" fill="{PANEL}">{L}</text>
<text x="140" y="{y+66}" style="font:700 46px Inter" fill="#fff">{v}</text></g>''')
        if ok:
            out.append(tick(370, y + 50, t0 + 0.6))
    return "".join(out)

def tap(x=560, t=0.2, pitch_lab=True):
    zig = " ".join(f"L{x-40 if i%2 else x-30} {200+i*15}" for i in range(1, 15))
    zig2 = " ".join(f"L{x+40 if i%2 else x+30} {200+i*15}" for i in range(1, 15))
    pl = f'''<g class="a" data-t="{t+0.8}"><path d="M{x+60} 260H{x+90}M{x+60} 290H{x+90}" stroke="#fff" stroke-width="2"/>
<path d="M{x+80} 230V256M{x+80} 320V294" stroke="{OR}" stroke-width="3" marker-end="url(#ao)"/><text class="mo" x="{x-120}" y="480">1 REV = 1 PITCH</text></g>''' if pitch_lab else ""
    return f'''<g class="a" data-t="{t}"><rect x="{x-22}" y="70" width="44" height="130" fill="#6C93B4" stroke="{LINE}" stroke-width="2"/>
<path d="M{x-30} 200 {zig} L{x} 430 L{x+30} 410 L{x+30} 200" fill="none" stroke="{LINE}" stroke-width="3"/>
<path d="M{x+30} 200 {zig2}" fill="none" stroke="{LINE}" stroke-width="3"/>
<path d="M{x-60} 120A62 22 0 1 0 {x+60} 120" stroke="{OR}" stroke-width="3" fill="none" marker-end="url(#ao)"/></g>{pl}'''

R11 = dict(id="11", slug="Rigid_Tapping_Feed", scenes=[
 dict(s=0, e=5.5, tag="QUICK MATHS  /  01", title="Tapping feed?", sub="M10 × 1.5, S600.",
      svg=fig("RIGID TAP · G94 · METRIC", "EXAMPLE", orange=True) + options(None, 0) + tap(600, 0, pitch_lab=False),
      body="Rigid tapping-க்கு F எவ்வளவு? உங்கள் பதில்?"),
 dict(s=5.5, e=12, tag="ANSWER  /  02", title="Answer: F900", tsize=72, sub="F = pitch × RPM.",
      svg=fig("RIGID TAP · G94 · METRIC", "SOURCE: HAAS") + options("B", 0.1) + f'''
<text class="a" data-t="1.0" x="460" y="230" style="font:600 44px Inter" fill="#fff">1.5 × 600</text>
<text class="a" data-t="1.5" x="460" y="300" style="font:700 46px Inter" fill="{OR}">= 900</text>
<text class="m a" data-t="1.8" x="460" y="345">mm/min</text>''',
      body="ஒரு சுற்றுக்கு tap ஒரு pitch (1.5 mm) முன்னேற வேண்டும்: 1.5 × 600 = 900."),
 dict(s=12, e=18, tag="WHY  /  03", title="Why exact?", sub="Spindle, feed ஒத்திசைவு.",
      svg=fig("SIDE VIEW", "SCHEMATIC") + tap(420, 0.2) + f'''
<text class="w a" data-t="1.4" x="30" y="150">F and S</text><text class="w a" data-t="1.4" x="30" y="195">must match</text>
<text class="m a" data-t="2.0" x="30" y="260" style="fill:{RED}">MISMATCH →</text><text class="m a" data-t="2.0" x="30" y="296" style="fill:{RED}">THREAD DAMAGE,</text><text class="m a" data-t="2.0" x="30" y="332" style="fill:{RED}">TAP BREAKAGE</text>''',
      body="F, S-உடன் பொருந்தாவிட்டால் thread சேதமாகலாம்; tap உடையலாம்."),
 dict(s=18, e=24.5, tag="FEED MODE  /  04", title="G94 or G95?", sub="Feed mode பாருங்கள்.",
      svg=fig("METRIC TAP · PITCH 1.5", "SOURCE: HAAS") + f'''
<g class="a" data-t="0.3"><rect x="30" y="80" width="345" height="300" rx="14" fill="#123A57" stroke="{LINE}" stroke-width="2.5"/>
<text x="55" y="135" style="font:700 36px Inter" fill="{OR}">G94</text><text class="m" x="55" y="175">PER MINUTE</text>
<text x="55" y="250" style="font:600 34px Inter" fill="#fff">F = 1.5 × S</text><text x="55" y="320" style="font:600 34px Inter" fill="#fff">S600 → F900.</text></g>
<g class="a" data-t="0.9"><rect x="403" y="80" width="345" height="300" rx="14" fill="#123A57" stroke="{LINE}" stroke-width="2.5"/>
<text x="428" y="135" style="font:700 36px Inter" fill="{OR}">G95</text><text class="m" x="428" y="175">PER REVOLUTION</text>
<text x="428" y="250" style="font:600 34px Inter" fill="#fff">F = pitch</text><text x="428" y="320" style="font:600 34px Inter" fill="#fff">F1.5</text></g>
<text class="mo a" data-t="1.6" x="30" y="450">HAAS: BACK TO G94 BEFORE MILLING</text>''',
      body="G95-ல் F = pitch. Tapping முடிந்ததும் G94-க்குத் திரும்புங்கள்."),
 dict(s=24.5, e=31, tag="INTERVIEW  /  05", title="Interview tip", sub="Pitch-ஐ drawing-ல் பாருங்கள்.", ssize=44,
      svg=fig("ISO METRIC · M10", "EXAMPLES") + "".join(
          f'''<g class="a" data-t="{0.3+k*0.5:.1f}"><rect x="30" y="{80+k*125}" width="718" height="100" rx="12" fill="#123A57" stroke="{OR if k==0 else '#2E5878'}" stroke-width="{3 if k==0 else 2}"/>
<text x="60" y="{144+k*125}" style="font:700 42px Inter" fill="#fff">{a}</text><text x="400" y="{144+k*125}" style="font:600 36px Inter" fill="{OR if k==0 else '#fff'}">{b}</text></g>'''
          for k, (a, b) in enumerate([("M10", "coarse · 1.5"), ("M10 × 1.25", "fine · 1.25"), ("M10 × 1", "fine · 1.0")])),
      body="M10 எப்போதும் 1.5 அல்ல; fine pitch drawing-ல் இருக்கும்.", body_t=1.8, cta=True, cta_t=2.4),
])

REELS = [R09, R10, R11]
