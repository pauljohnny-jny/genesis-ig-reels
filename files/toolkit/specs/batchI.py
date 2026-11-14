from gen import *
W = "#E6F0F7"
SEND = "நண்பருக்கு அனுப்புங்கள்."
SANDVIK = "SOURCE: SANDVIK COROMANT"


def vib(inner, t0=0.0, t1=4.0, step=0.4):
    """Continuous schematic vibration: nested .shake groups, one per step (each shakes 0.4 s)."""
    n = int(round((t1 - t0) / step))
    out = inner
    for k in range(n):
        out = f'<g class="shake" data-t="{t0 + k*step:.2f}">{out}</g>'
    return out


def wave(x, y0, y1, amp=7, step=14):
    """Vertical zig-zag (chatter marks on a wall at x)."""
    d = f"M{x} {y0}"
    k = 0
    y = y0
    while y < y1:
        y = min(y1, y + step); k += 1
        d += f"L{x + (amp if k % 2 else -amp)} {y}"
    return d


def zig(x0, x1, y, amp=8, step=20):
    d = f"M{x0} {y}"
    k = 0; x = x0
    while x < x1:
        x = min(x1, x + step); k += 1
        d += f"L{x} {y + (amp if k % 2 else -amp)}"
    return d


# =====================================================================================================
# REEL 24: Tool wear – flank wear vs crater wear vs built-up edge. Target 30 s. CTA SAVE.
# Hook format: (4) verbatim interview question. Options considered:
#   "“இந்த 3 wear என்ன?”" (interview question, chosen: has the number 3, three wear patterns grow in the panel from frame 1,
#   named in scene 2 at 4.2 s, echoed in scene 5) / "Flank wear = bad?" (wrong vs right) / "BUE: speed ஏற்றவா?" (demo).
# Sources: Sandvik Coromant "Tool wear: Wear on cutting edges"
#   https://www.sandvik.coromant.com/en-gb/knowledge/materials/wear-on-cutting-edges
#   Flank wear (Abrasive): "most common type of tool wear and the preferred wear type ... predictable and stable tool life";
#   "occurs due to abrasion, caused by hard constituents in the workpiece material".
#   Crater wear (Chemical): "localized to the rake side of the insert"; "chemical reaction between the workpiece material and the
#   cutting tool and is amplified by cutting speed"; "weakens the cutting edge and may lead to fracture".
#   BUE (Adhesive): "pressure welding of the chip to the insert"; "most common when machining sticky materials, such as low carbon
#   steel, stainless steel and aluminium"; "Low cutting speed increases the formation of built-up edge".
# Sandvik "Milling troubleshooting" https://www.sandvik.coromant.com/en-gb/knowledge/milling/troubleshooting-milling
#   Flank wear: cause "Cutting speed too high ... Feed, fz, too low"; Crater wear: "Diffusion wear due to cutting temperatures that
#   are too high on the rake face" -> "Reduce the speed ... and then reduce the feed"; BUE: "Cutting zone temperature is too low",
#   "Low cutting speed, vc" -> "Increase cutting speed". "always remember to check the insert/cutting edge after machining".
# Drawings are schematic edge views; wear is exaggerated for visibility.

def insert(x, y, s=1.0, wear=None, t=0.0, d=1.8):
    """Edge view of an insert corner: rake face on top, flank face on the left; cutting edge at the top-left corner."""
    ex, ey = x - 70 * s, y
    body = (f'<path d="M{ex} {ey}H{x + 80*s}V{y + 200*s}H{x - 50*s}Z" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>')
    w = ""
    if wear == "flank":  # wear land growing down the flank face from the edge
        w = (f'<path class="draw" data-t="{t}" data-d="{d}" pathLength="1" d="M{ex + 3*s} {ey + 2}L{ex + 3*s + 6*s} {ey + 70*s}" '
             f'stroke="{OR}" stroke-width="{14*s:.0f}" stroke-linecap="round" fill="none"/>')
    elif wear == "crater":  # hollow on the rake face, a little behind the edge
        w = (f'<path class="draw" data-t="{t}" data-d="{d}" d="M{ex + 30*s} {ey}Q{ex + 75*s} {ey + 50*s} {ex + 120*s} {ey}Z" fill="{RED}"/>')
    elif wear == "bue":  # chip material welded onto the edge, building up
        w = "".join(f'<circle class="a" data-t="{t + k*0.45:.2f}" cx="{ex + dx*s}" cy="{ey + dy*s}" r="{r*s:.0f}" fill="#C9B79A" stroke="#fff" stroke-width="1.5"/>'
                    for k, (dx, dy, r) in enumerate([(8, -6, 16), (-6, 8, 15), (22, -18, 13), (-2, -22, 12)]))
    return body + w


R24_HOOK = dict(hook="“3 wear என்ன?”", hsize=88, hook2="Interview கேள்வி.", s=0, e=4.2, svg=f'''
{fig("EDGE VIEW · SCHEMATIC", "EXAGGERATED FOR VISIBILITY", orange=True)}
<g style="font:600 22px Plex" fill="#9FC3DD"><text x="40" y="104">RAKE FACE = TOP</text><text x="738" y="104" text-anchor="end">FLANK FACE = SIDE</text></g>
{insert(145, 170, 1.25, "flank", 0.0, 2.6)}
{insert(400, 170, 1.25, "crater", 0.0, 2.6)}
{insert(655, 170, 1.25, "bue", 0.0)}
<g style="font:800 64px Inter" text-anchor="middle" fill="#fff"><text x="155" y="510">A</text><text x="405" y="510">B</text><text x="655" y="510">C</text></g>
<g class="a" data-t="1.2" style="font:700 30px Inter" text-anchor="middle" fill="{OR}"><text x="155" y="560">?</text><text x="405" y="560">?</text><text x="655" y="560">?</text></g>
<text class="a" data-t="1.8" x="389" y="650" text-anchor="middle" style="font:700 34px Inter" fill="#fff">NAME IT. THEN THE CAUSE.</text>
<text x="389" y="712" text-anchor="middle" style="font:600 24px Inter" fill="#9FC3DD">ANSWER IN THIS REEL</text>''')


def wear_col(x, name, where, mech, col, t):
    return (f'<g class="a" data-t="{t}" text-anchor="middle"><text x="{x}" y="318" style="font:700 28px Inter" fill="#fff">{esc(name)}</text>'
            f'<text x="{x}" y="358" class="m" style="font-size:22px">{esc(where)}</text>'
            f'<text x="{x}" y="404" style="font:700 26px Inter" fill="{col}">{esc(mech)}</text></g>')


R24 = dict(id="24", slug="Flank_Crater_BUE_Tool_Wear", scenes=[
 R24_HOOK,
 dict(s=4.2, e=10.8, tag="ANSWER  /  02", title="Where is the wear?", tsize=66, sub="இடத்தைப் பாருங்கள்.", ssize=48,
      svg=fig("EDGE VIEW · SCHEMATIC", "EXAGGERATED", orange=True)
          + insert(150, 90, 0.75, "flank", 0.2, 0.8) + insert(400, 90, 0.75, "crater", 0.5, 0.8) + insert(650, 90, 0.75, "bue", 0.8)
          + wear_col(140, "FLANK WEAR", "FLANK FACE", "ABRASIVE", OR, 0.3)
          + wear_col(389, "CRATER WEAR", "RAKE FACE (TOP)", "CHEMICAL", RED, 0.7)
          + wear_col(640, "BUILT-UP EDGE", "ON THE EDGE", "ADHESIVE", "#E8D7B9", 1.1)
          + f'<text class="fig a" data-t="1.4" x="389" y="470" text-anchor="middle">{SANDVIK}</text>',
      body="Flank: பக்க face. Crater: மேல் rake face. BUE: edge-ல் ஒட்டிய chip."),
 dict(s=10.8, e=17.4, tag="CAUSE  /  03", title="Likely cause", tsize=74, sub="Sandvik guide-படி.", ssize=48,
      svg=fig("PATTERN → LIKELY CAUSE", SANDVIK, orange=True) + '<path d="M30 200H748M30 340H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(125, "A", "FLANK → ABRASION", "எதிர்பார்க்கும் wear. Speed (vc) அதிகமா?", 0.3)
          + checkrow(265, "B", "CRATER → HEAT, CHEMICAL", "Rake face சூடு. vc, feed அதிகமா?", 0.8)
          + checkrow(405, "C", "BUE → STICKY, LOW SPEED", "Low carbon steel, SS, Al. vc குறைவா?", 1.3),
      body="மாற்றும் முன் tool maker cutting data-வைப் பாருங்கள்.", body_t=1.8),
 dict(s=17.4, e=23.8, tag="INTERVIEW  /  04", title="Interview answer", tsize=72, sub="முதலில் இடம், பிறகு காரணம்.", ssize=44,
      svg=fig("HOW TO ANSWER") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "WHERE?", "Flank face / rake face / edge", 0.3)
          + checkrow(255, 2, "WHY?", "Abrasion / chemical / adhesion", 0.8)
          + checkrow(395, 3, "CHECK THE DATA", "vc, fz: tool maker data-படி", 1.3),
      body="ஒவ்வொரு job முடிந்ததும் insert edge-ஐப் பாருங்கள்.", body_t=1.8),
 dict(s=23.8, e=30.4, tag="REMEMBER  /  05", title="Flank · Crater · BUE", tsize=64, sub="“3 wear என்ன?”", ssize=50,
      svg=fig("3 PATTERNS", SANDVIK, orange=True) + f'''
<g class="a" data-t="0.3"><rect x="30" y="80" width="230" height="300" rx="16" fill="#123A57" stroke="{OR}" stroke-width="3"/>
<text x="145" y="150" text-anchor="middle" style="font:800 36px Inter" fill="{OR}">FLANK</text>
<text x="145" y="230" text-anchor="middle" class="m" style="font-size:22px">ABRASIVE</text>
<text x="145" y="300" text-anchor="middle" style="font:600 24px Inter" fill="#fff">EXPECTED,</text>
<text x="145" y="334" text-anchor="middle" style="font:600 24px Inter" fill="#fff">STEADY</text></g>
<g class="a" data-t="0.6"><rect x="274" y="80" width="230" height="300" rx="16" fill="#123A57" stroke="{RED}" stroke-width="3"/>
<text x="389" y="150" text-anchor="middle" style="font:800 36px Inter" fill="{RED}">CRATER</text>
<text x="389" y="230" text-anchor="middle" class="m" style="font-size:22px">CHEMICAL</text>
<text x="389" y="300" text-anchor="middle" style="font:600 24px Inter" fill="#fff">HEAT ON</text>
<text x="389" y="334" text-anchor="middle" style="font:600 24px Inter" fill="#fff">RAKE FACE</text></g>
<g class="a" data-t="0.9"><rect x="518" y="80" width="230" height="300" rx="16" fill="#123A57" stroke="#E8D7B9" stroke-width="3"/>
<text x="633" y="150" text-anchor="middle" style="font:800 36px Inter" fill="#E8D7B9">BUE</text>
<text x="633" y="230" text-anchor="middle" class="m" style="font-size:22px">ADHESIVE</text>
<text x="633" y="300" text-anchor="middle" style="font:600 24px Inter" fill="#fff">STICKY,</text>
<text x="633" y="334" text-anchor="middle" style="font:600 24px Inter" fill="#fff">LOW SPEED</text></g>
<text class="m a" data-t="1.3" x="389" y="450" text-anchor="middle" style="font-size:22px">CAUSES VARY: CHECK YOUR TOOL MAKER'S GUIDE</text>''',
      body="பெயர், இடம், காரணம்: மூன்றும் சொல்லுங்கள்.", body_t=1.6, cta=True, cta_t=2.4),
])


# =====================================================================================================
# REEL 25: Chatter and tool stick-out. Target 20 s. CTA SEND.
# Hook format: (1) cold-open demo (long overhang vibrating from frame 1, labelled EXAGGERATED FOR VISIBILITY). Options considered:
#   "5×D stick-out." (demo, chosen: a number, the long tool chatters from frame 1, answered in scene 2 at 3.6 s, echoed in
#   scene 5) / "Long tool = OK?" (wrong vs right) / "Chatter வந்தா என்ன செய்வீங்க?" (interview question).
# Sources: Sandvik Coromant "How to reduce vibration in milling" https://www.sandvik.coromant.com/en-gb/knowledge/milling/vibration
#   "Keep the tool assembly as rigid and short as possible"; "Choose the largest possible adaptor diameter/size";
#   "Always use the shortest possible tool length"; "For overhangs greater than four times the tool diameter, milling vibration
#   tendencies can become more apparent" (shown as GUIDANCE, not a rule); workpiece/fixture: "fixture should be close to the
#   machine table"; "Even a small increase, as low as 50 rpm, can move a cutting process from unstable, with vibration, to stable".
#   Sandvik "Milling troubleshooting" https://www.sandvik.coromant.com/en-gb/knowledge/milling/troubleshooting-milling
#   Too long tool overhang: "Minimize overhang", "Increase feed per tooth", "Reduce axial depth of cut"; Axially weak workpiece:
#   "Improve clamping of tool"; Weak fixture: "provide adequate support or improve the fixture"; Bad stability: "Reduce overhang".
# The 5×D drawing is schematic; vibration amplitude is exaggerated.

D25 = 50  # schematic tool diameter in px

def mill_assy(cx, top, L, col, t_vib=None, t1=4.0, marks=True, mark_t=0.0, mark_d=3.0, label=None):
    """Side view: spindle nose, holder, end mill of length L (stick-out), cutting the wall of a block on its right."""
    tool = (f'<rect x="{cx - D25/2}" y="{top + 120}" width="{D25}" height="{L}" fill="{LINE}" stroke="#fff" stroke-width="2"/>'
            + "".join(f'<path d="M{cx - D25/2} {top + 140 + k*34}l{D25} 22" stroke="{STEEL}" stroke-width="5"/>' for k in range(int((L - 30) / 34)))
            + f'<path d="M{cx - 60} {top + 60}H{cx + 60}L{cx + 40} {top + 120}H{cx - 40}Z" fill="#6C93B4" stroke="{LINE}" stroke-width="2"/>')
    if t_vib is not None:
        tool = vib(tool, t_vib, t1)
    spindle = f'<rect x="{cx - 80}" y="{top}" width="160" height="60" rx="6" fill="#2E5878" stroke="{LINE}" stroke-width="2"/>'
    bx = cx + D25/2 + 2
    bh = min(140, int(L * 0.6))
    block = f'<rect x="{bx}" y="{top + 120 + L - bh}" width="{min(250, 740 - bx)}" height="{bh + 30}" fill="{STEEL}" stroke="{LINE}" stroke-width="2"/>'
    m = ""
    if marks:
        m = (f'<path class="draw" data-t="{mark_t}" data-d="{mark_d}" data-lin="1" pathLength="1" d="{wave(bx + 10, top + 120 + L - bh + 8, top + 120 + L + 22, 10, 12)}" '
             f'stroke="{col}" stroke-width="5" fill="none"/>')
    lab = f'<text x="{cx}" y="{top + 120 + L + 70}" text-anchor="middle" style="font:700 26px Inter" fill="{col}">{esc(label)}</text>' if label else ""
    return spindle + block + m + tool + lab


R25_HOOK = dict(hook="5×D stick-out.", hsize=100, hook2="Chatter ஆரம்பம்!", s=0, e=3.6, svg=f'''
{fig("SIDE VIEW · SCHEMATIC", "EXAGGERATED FOR VISIBILITY", orange=True)}
{mill_assy(330, 80, 5 * D25, RED, t_vib=0.0, t1=3.6, mark_t=0.0, mark_d=3.0)}
<path d="M200 200V450" stroke="{OR}" stroke-width="3" marker-start="url(#ao)" marker-end="url(#ao)"/>
<text x="186" y="335" text-anchor="end" style="font:800 34px Inter" fill="{OR}">L = 5×D</text>
<path d="M305 488H355" stroke="#fff" stroke-width="2.5" marker-start="url(#aw)" marker-end="url(#aw)"/>
<text x="330" y="526" text-anchor="middle" style="font:700 26px Inter" fill="#fff">D</text>
<text class="a" data-t="0.8" x="580" y="590" text-anchor="middle" style="font:800 30px Inter" fill="{RED}">CHATTER MARKS</text>
<text class="a" data-t="1.6" x="389" y="680" text-anchor="middle" style="font:700 26px Inter" fill="#BFD6E8">SANDVIK: OVER 4×D, VIBRATION MORE LIKELY</text>
<text class="m a" data-t="1.6" x="389" y="722" text-anchor="middle" style="font-size:22px">GUIDANCE, NOT A FIXED LIMIT</text>''')

R25 = dict(id="25", slug="Chatter_Tool_Stick_Out", scenes=[
 R25_HOOK,
 dict(s=3.6, e=7.8, tag="ANSWER  /  02", title="Shortest stick-out", tsize=68, sub="தேவையான அளவு மட்டும்.", ssize=46,
      svg=fig("SIDE VIEW · SCHEMATIC", "EXAGGERATED", orange=True)
          + mill_assy(150, 60, 4 * D25 + 40, RED, t_vib=0.0, t1=4.2, mark_t=0.0, mark_d=2.0, label="LONG ✗")
          + mill_assy(520, 60, 2 * D25 + 40, GRN, marks=False, label="SHORT ✓"),
      body="Part-ஐ அடைய தேவையான நீளம் மட்டும் நீட்டுங்கள்."),
 dict(s=7.8, e=12.0, tag="LEVERS  /  03", title="Other levers", tsize=74, sub="Sandvik பரிந்துரை.", ssize=48,
      svg=fig("CHATTER CHECK", SANDVIK, orange=True) + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "RIGID TOOL HOLDING", "பெரிய holder, சரியான clamping", 0.2)
          + checkrow(255, 2, "SUPPORT THE PART", "Fixture-ஐ உறுதியாக்குங்கள்", 0.6)
          + checkrow(395, 3, "CUTTING DATA", "ap குறை, fz கூட்டு, rpm சிறிது மாற்று", 1.0)),
 dict(s=12.0, e=16.2, tag="INTERVIEW  /  04", title="Interview answer", tsize=72, sub="நான்கையும் சொல்லுங்கள்.", ssize=46,
      svg=fig("CHATTER: WHAT I CHECK") + f'''
<g style="font:700 30px Inter" text-anchor="middle">
<g class="a" data-t="0.2"><rect x="30" y="70" width="350" height="120" rx="14" fill="#123A57" stroke="{OR}" stroke-width="3"/><text x="205" y="142" fill="#fff">1 · STICK-OUT</text></g>
<g class="a" data-t="0.4"><rect x="398" y="70" width="350" height="120" rx="14" fill="#123A57" stroke="{OR}" stroke-width="3"/><text x="573" y="142" fill="#fff">2 · HOLDING</text></g>
<g class="a" data-t="0.6"><rect x="30" y="210" width="350" height="120" rx="14" fill="#123A57" stroke="{OR}" stroke-width="3"/><text x="205" y="282" fill="#fff">3 · PART SUPPORT</text></g>
<g class="a" data-t="0.8"><rect x="398" y="210" width="350" height="120" rx="14" fill="#123A57" stroke="{OR}" stroke-width="3"/><text x="573" y="282" fill="#fff">4 · CUTTING DATA</text></g></g>
<text class="m a" data-t="1.1" x="389" y="400" text-anchor="middle" style="font-size:22px">4×D = SANDVIK GUIDANCE, NOT A RULE</text>
<text class="m a" data-t="1.1" x="389" y="440" text-anchor="middle" style="font-size:22px">CHECK YOUR TOOL MAKER'S DATA</text>''',
      body="உங்கள் job-ல் நீங்கள் செய்ததைச் சொல்லுங்கள்.", body_t=1.4),
 dict(s=16.2, e=20.6, tag="REMEMBER  /  05", title="5×D? Shorten it.", tsize=72, sub="Shortest practical stick-out.", ssize=44,
      svg=fig("SIDE VIEW · SCHEMATIC")
          + mill_assy(180, 80, 2 * D25 + 40, GRN, marks=False) + tick(610, 160, 0.4)
          + f'<text class="a" data-t="0.6" x="610" y="250" text-anchor="middle" style="font:700 28px Inter" fill="{GRN}">SHORT + RIGID</text>'
          + f'<text class="a" data-t="0.8" x="610" y="300" text-anchor="middle" style="font:600 24px Inter" fill="#BFD6E8">LESS VIBRATION</text>'
          + f'<text class="m a" data-t="1.0" x="389" y="470" text-anchor="middle" style="font-size:22px">REACH THE PART, NO LONGER</text>',
      cta=True, cta_t=1.4, cta_icon="send", cta_text=SEND),
])


# =====================================================================================================
# REEL 26: Roughing vs finishing. Target 30 s. CTA SAVE.
# Hook format: (3) wrong vs right. Options considered:
#   "Rough = Finish?" (wrong vs right, chosen: the finish pass is run at roughing ap/fz first and leaves a rough surface, then the
#   right light pass appears at 2.0 s; answered in scene 2 at 4.2 s; echoed in scene 5) /
#   "Finish pass-ல் heavy cut?" (demo) / "Roughing, finishing வித்தியாசம்?" (interview question).
# Sources: Sandvik Coromant "How to choose correct turning insert"
#   https://www.sandvik.coromant.com/en-gb/knowledge/general-turning/how-to-choose-correct-turning-insert
#   Roughing: "High depth of cut and feed rate combinations. Operations requiring the highest edge security."
#   Finishing: "Operations at light depths of cut and low feed rates. Operations requiring low cutting forces."
#   Sandvik "What is profile milling?" https://www.sandvik.coromant.com/en-gb/knowledge/milling/profile-milling
#   "divided into at least three operation types: Roughing/semi-roughing, Semi-finishing, Finishing"; "Milling of remaining stock,
#   so-called rest milling, is included in semi-finishing and finishing"; finishing -> "better geometrical accuracy and a higher
#   surface structure quality". Sandvik "Shoulder milling": "Leave an allowance on both sides for subsequent finishing".
# No universal ap/fz values shown (Sandvik's figures are tool- and case-specific).

def pass_demo(y, depth, col, t0, d, label, tick_fn):
    """Side view: tool moves left to right removing `depth` px of stock; the new surface is drawn behind it."""
    surf = (zig(60, 700, y + depth, 9, 22) if col == RED else f"M60 {y + depth}H700")
    return f'''
<text class="a" data-t="{t0}" x="40" y="{y - 70}" style="font:700 28px Inter" fill="{col}">{esc(label)}</text>
<g class="a" data-t="{t0}"><rect x="40" y="{y}" width="700" height="150" fill="{STEEL}" stroke="{LINE}" stroke-width="2"/></g>
<rect class="grow" data-t="{t0}" data-d="{d}" data-w="640" x="40" y="{y - 2}" width="0" height="{depth + 2}" fill="{PANEL}"/>
<path class="draw" data-t="{t0}" data-d="{d}" data-lin="1" pathLength="1" d="{surf}" stroke="{col}" stroke-width="5" fill="none"/>
<g class="move a" data-t="{t0}" data-d="{d}" data-dx="640"><rect x="30" y="{y + depth - 110}" width="60" height="110" fill="{LINE}" stroke="#fff" stroke-width="2"/>
<rect x="45" y="{y + depth - 150}" width="30" height="40" fill="#6C93B4"/></g>
{tick_fn}'''


R26_HOOK = dict(hook="Rough = Finish?", hsize=100, hook2="ஒரே ap, ஒரே feed-ஆ?", s=0, e=4.2, svg=f'''
{fig("SIDE VIEW · SCHEMATIC", "WRONG vs RIGHT", orange=True)}
{pass_demo(200, 70, RED, 0.0, 1.8, "✗ FINISH AT ROUGHING ap, fz", cross(500, 120, 1.8))}
<text class="a" data-t="1.6" x="389" y="400" text-anchor="middle" style="font:700 26px Inter" fill="{RED}">ROUGH SURFACE, HIGH FORCE</text>
{pass_demo(560, 16, GRN, 2.0, 1.5, "✓ FINISH: LIGHT ap, LOWER fz", tick(500, 480, 3.4))}''')

R26 = dict(id="26", slug="Roughing_vs_Finishing", scenes=[
 R26_HOOK,
 dict(s=4.2, e=10.8, tag="ANSWER  /  02", title="What changes?", tsize=76, sub="ap, feed, நோக்கம்.", ssize=48,
      svg=fig("ROUGHING vs FINISHING", SANDVIK, orange=True) + f'''
<g style="font:700 30px Inter"><text class="a" data-t="0.1" x="330" y="96" fill="{OR}">ROUGHING</text><text class="a" data-t="0.1" x="560" y="96" fill="{GRN}">FINISHING</text></g>
<path d="M30 120H748M30 220H748M30 320H748" stroke="#2E5878" stroke-width="2"/>
<g class="a" data-t="0.4"><text x="40" y="178" class="m" style="font-size:24px">DEPTH (ap)</text>
<text x="330" y="180" style="font:700 30px Inter" fill="#fff">HIGH</text><text x="560" y="180" style="font:700 30px Inter" fill="#fff">LIGHT</text></g>
<g class="a" data-t="0.8"><text x="40" y="278" class="m" style="font-size:24px">FEED</text>
<text x="330" y="280" style="font:700 30px Inter" fill="#fff">HIGH</text><text x="560" y="280" style="font:700 30px Inter" fill="#fff">LOW</text></g>
<g class="a" data-t="1.2"><text x="40" y="378" class="m" style="font-size:24px">AIM</text>
<text x="330" y="378" style="font:600 26px Inter" fill="#fff">REMOVE STOCK,</text><text x="330" y="414" style="font:600 26px Inter" fill="#fff">EDGE SECURITY</text>
<text x="560" y="378" style="font:600 26px Inter" fill="#fff">SURFACE, SIZE,</text><text x="560" y="414" style="font:600 26px Inter" fill="#fff">LOW FORCES</text></g>
<text class="m a" data-t="1.6" x="389" y="480" text-anchor="middle" style="font-size:22px">NO FIXED VALUES: TOOL MAKER DATA</text>''',
      body="Roughing: அதிக ap, feed. Finishing: குறைந்த ap, feed."),
 dict(s=10.8, e=17.4, tag="EXAMPLE  /  03", title="Rough, then finish", tsize=68, sub="Finish-க்கு stock விடுங்கள்.", ssize=46,
      svg=fig("SECTION · SCHEMATIC", "NOT TO SCALE", orange=True) + f'''
<rect x="60" y="100" width="420" height="340" fill="#2E5878" stroke="{LINE}" stroke-width="2" stroke-dasharray="10 8"/>
<text x="270" y="140" text-anchor="middle" class="m" style="font-size:22px">RAW STOCK</text>
<g class="a" data-t="0.3"><rect x="60" y="250" width="420" height="190" fill="{STEEL}" stroke="{LINE}" stroke-width="2"/>
<rect x="60" y="250" width="420" height="34" fill="{OR}"/></g>
<text class="a" data-t="0.3" x="270" y="215" text-anchor="middle" style="font:700 26px Inter" fill="{OR}">1 ROUGH: REMOVED</text>
<text class="a" data-t="0.9" x="510" y="274" style="font:700 26px Inter" fill="{OR}">← FINISH STOCK</text>
<g class="a" data-t="1.5"><path d="M60 284H480" stroke="{GRN}" stroke-width="6"/></g>
<text class="a" data-t="1.5" x="510" y="330" style="font:700 26px Inter" fill="{GRN}">2 FINISH: TO SIZE</text>
<text class="m a" data-t="1.9" x="389" y="490" text-anchor="middle" style="font-size:22px">STOCK AMOUNT: PROCESS SHEET / TOOL DATA</text>''',
      body="Finish pass: குறைந்த stock, நல்ல surface, சரியான size.", body_t=2.0),
 dict(s=17.4, e=23.8, tag="INTERVIEW  /  04", title="Interview answer", tsize=72, sub="நோக்கமே வித்தியாசம்.", ssize=48,
      svg=fig("HOW TO ANSWER") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "ROUGHING", "அதிக ap, feed: stock நீக்க", 0.3)
          + checkrow(255, 2, "FINISHING", "குறைந்த ap, feed: surface, size", 0.8)
          + checkrow(395, 3, "NO FIXED NUMBERS", "Tool maker data, drawing-படி", 1.3),
      body="நீங்கள் செய்த ஒரு job-ன் உதாரணம் சொல்லுங்கள்.", body_t=1.8),
 dict(s=23.8, e=30.4, tag="REMEMBER  /  05", title="Rough ≠ Finish", tsize=78, sub="ஒரே ap, ஒரே feed அல்ல.", ssize=48,
      svg=fig("WRONG vs RIGHT") + f'''
<g class="a" data-t="0.3"><rect x="40" y="80" width="698" height="140" rx="14" fill="#123A57" stroke="{RED}" stroke-width="3"/>
<text x="70" y="138" style="font:700 30px Inter" fill="#fff">FINISH AT ROUGHING ap, fz</text>
<text x="70" y="186" class="m" style="font-size:22px">ROUGH SURFACE, HIGH FORCE</text></g>{cross(690, 150, 0.5)}
<g class="a" data-t="0.9"><rect x="40" y="260" width="698" height="140" rx="14" fill="#123A57" stroke="{GRN}" stroke-width="3"/>
<text x="70" y="318" style="font:700 30px Inter" fill="#fff">ROUGH HEAVY → FINISH LIGHT</text>
<text x="70" y="366" class="m" style="font-size:22px">LEAVE STOCK FOR THE FINISH PASS</text></g>{tick(690, 330, 1.1)}''',
      body="Roughing-ம் finishing-ம் தனித்தனி pass.", body_t=1.5, cta=True, cta_t=2.4),
])


# =====================================================================================================
# REEL 27: Coolant and chip evacuation. Target 20 s. CTA SAVE.
# Hook format: (1) cold-open demo. Options considered:
#   "1 chip, 2 cuts?" (demo, chosen: numbers; chips fall back into a pocket and one is recut at 1.5 s; answered in scene 2 at
#   3.6 s; echoed in scene 5 as "1 chip, 1 cut.") / "Chips in pocket = OK?" (wrong vs right) /
#   "Chip evacuation ஏன் முக்கியம்?" (interview question).
# Sources: Sandvik Coromant "Milling troubleshooting" https://www.sandvik.coromant.com/en-gb/knowledge/milling/troubleshooting-milling
#   Re-cutting of chips: "Appears in full slotting and pocketing ... Also common when milling deep cavities and pockets on
#   vertical machines"; effect "Cutting edge fractures / Harmful for tool life and security / Chip jamming"; solution "Evacuate chips
#   effectively by compressed air or copious cutting fluid flow – preferably internal coolant", "Change cutter position and tool
#   path strategy", "Reduce feed, fz", "Split deep cuts into several passes".
#   Sandvik "Dry milling or with cutting fluid" https://www.sandvik.coromant.com/en-gb/knowledge/milling/dry-milling-or-with-cutting-fluid
#   "If milling has to be performed wet, cutting fluid should be applied copiously" (and Sandvik prefers dry for rough milling with
#   carbide, so the reel does NOT say "always use coolant": air OR coolant, per tool maker data).
#   KYOCERA SGS Precision Tools Europe "Chip Evacuation in Machining" https://kyocera-sgstool.co.uk/?p=2570
#   "If chips remain in the cutting area, they get recut, which generates heat and accelerates tool wear"; "Recutting chips can
#   scratch and damage the workpiece, leading to poor surface finishes".

def chip(x, y, rot=0, col=OR):
    return f'<path d="M{x} {y}l26 -10 10 18 -22 14z" fill="{col}" stroke="#fff" stroke-width="1.5" transform="rotate({rot} {x} {y})"/>'

POCKET = f'''<path d="M60 220H290V600H490V220H718V680H60Z" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>'''

R27_HOOK = dict(hook="1 chip, 2 cuts?", hsize=100, hook2="Chip தங்கினால்…", s=0, e=3.6, flash_t=1.5, svg=f'''
{fig("SIDE VIEW · SCHEMATIC", "VERTICAL MACHINE", orange=True)}
{POCKET}
<g><rect x="350" y="100" width="80" height="480" fill="{LINE}" stroke="#fff" stroke-width="2"/>
{"".join(f'<path d="M350 {130 + k*40}l80 26" stroke="{STEEL}" stroke-width="6"/>' for k in range(11))}</g>
<text x="390" y="88" text-anchor="middle" class="m" style="font-size:22px">END MILL</text>
<g>{chip(296, 590, 10)}{chip(318, 570, 70)}{chip(440, 586, 30)}{chip(462, 566, 110)}</g>
<g class="move" data-t="0" data-d="1.5" data-dx="0" data-dy="300">{chip(470, 270, 40)}{chip(306, 250, 120)}</g>
<g class="move" data-t="0" data-d="1.5" data-dx="40" data-dy="-4">{chip(296, 548, 0, RED)}</g>
<circle class="a" data-t="1.5" cx="350" cy="548" r="38" fill="none" stroke="{RED}" stroke-width="5"/>
<text class="a" data-t="1.5" x="600" y="190" text-anchor="middle" style="font:800 44px Inter" fill="{RED}">RECUT!</text>
<text class="a" data-t="2.0" x="389" y="730" text-anchor="middle" style="font:700 26px Inter" fill="#BFD6E8">CHIPS LEFT IN THE CUT GET CUT AGAIN</text>''')

R27 = dict(id="27", slug="Chip_Evacuation_Coolant", scenes=[
 R27_HOOK,
 dict(s=3.6, e=7.8, tag="ANSWER  /  02", title="Why chips must go", tsize=66, sub="Recut: மூன்று பாதிப்பு.", ssize=46,
      svg=fig("RECUTTING CHIPS") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "TOOL LIFE ↓", "Edge உடையலாம் (Sandvik)", 0.2)
          + checkrow(255, 2, "HEAT ↑", "Recut-ல் சூடு கூடும் (Kyocera SGS)", 0.6)
          + checkrow(395, 3, "SURFACE FINISH ✗", "Part-ல் கீறல் (Kyocera SGS)", 1.0)),
 dict(s=7.8, e=12.0, tag="CHECK  /  03", title="Clear the chips", tsize=72, sub="Sandvik பரிந்துரை.", ssize=48,
      svg=fig("GET CHIPS OUT", SANDVIK, orange=True) + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "AIR OR COOLANT", "Compressed air, அல்லது ஏராளமான coolant", 0.2)
          + checkrow(255, 2, "THROUGH-TOOL COOLANT", "Internal coolant இருந்தால் சிறந்தது", 0.6)
          + checkrow(395, 3, "SPLIT DEEP CUTS", "ஆழமான cut-ஐ பல pass-ஆக", 1.0)),
 dict(s=12.0, e=16.2, tag="INTERVIEW  /  04", title="Interview answer", tsize=72, sub="Chip evacuation ஏன்?", ssize=48,
      svg=fig("HOW TO ANSWER") + f'''
<text class="w a" data-t="0.2" x="40" y="120" style="font-size:30px">“Chip cut-ல் தங்கினால் recut ஆகும்:</text>
<text class="w a" data-t="0.4" x="40" y="172" style="font-size:30px">tool life, finish இரண்டும் பாதிக்கும்.”</text>
<path d="M30 230H748" stroke="#2E5878" stroke-width="2"/>
<text class="m a" data-t="0.8" x="40" y="300" style="font-size:22px">WET OR DRY: FOLLOW TOOL MAKER DATA</text>
<text class="m a" data-t="1.0" x="40" y="350" style="font-size:22px">SANDVIK: IF WET, APPLY COOLANT COPIOUSLY</text>''',
      body="நீங்கள் chip-ஐ எப்படி அகற்றினீர்கள்?", body_t=1.3),
 dict(s=16.2, e=20.6, tag="REMEMBER  /  05", title="1 chip, 1 cut.", tsize=80, sub="Chip-ஐ வெளியேற்றுங்கள்.", ssize=48,
      svg=fig("SIDE VIEW · SCHEMATIC") + f'''
<path d="M60 160H290V440H490V160H718V500H60Z" transform="translate(0 -20)" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="350" y="70" width="80" height="330" fill="{LINE}" stroke="#fff" stroke-width="2"/>
<g class="move" data-t="0.2" data-d="1.4" data-dx="-170" data-dy="-310">{chip(312, 390, 20)}</g>
<g class="move" data-t="0.2" data-d="1.4" data-dx="170" data-dy="-310">{chip(446, 390, 80)}</g>
<path class="a" data-t="0.2" d="M320 380V150M460 380V150" stroke="#9FC3DD" stroke-width="4" marker-end="url(#aw)"/>
<g class="a" data-t="0.2" style="font:700 26px Inter" fill="#fff" text-anchor="middle"><text x="604" y="280">AIR OR</text><text x="604" y="314">COOLANT:</text><text x="604" y="348">CHIPS OUT</text></g>''',
      cta=True, cta_t=1.4),
])


# =====================================================================================================
# REEL 28: Inch ↔ mm. Target 20 s. CTA SAVE.
# Hook format: (2) countdown quiz. Options considered:
#   "0.001 in = ? mm" (quiz, chosen: specific number, 3-2-1 ring from frame 1, answered in scene 2 at 4.0 s, echoed in scene 5) /
#   "1 inch = 25 mm?" (wrong vs right) / "1 thou எத்தனை mm?" (interview question).
# Sources: NIST Office of Weights and Measures "SI Units – Length" https://www.nist.gov/pml/owm/si-units-length
#   "The value for the inch, derived from the value of the Yard effective July 1, 1959, is exactly equivalent to 25.4 mm."
#   -> 0.001 in × 25.4 = 0.0254 mm (= 25.4 µm, SI prefixes, as in reel 18).
#   Haas Automation "Mill Programming Workbook" (June 2000), section "INCH / METRIC SELECTION (G20, G21)", p.51
#   (https://www.engr.psu.edu/cim/mllwrkb.pdf): "G20 Inch programming selection / G21 metric programming selection";
#   "Selection between inch and metric programming can only be done from the Setting 9"; "in this control, the G20 (inch) and
#   G21 (mm) codes can only be used to ensure that the inch/metric setting is set correctly for that program".
#   Current Haas code page title (haascnc.com, page body blocked by bot check): "G20 Select Inches / G21 Select Metric (Group 06)".

R28_HOOK = dict(hook="0.001 in = ? mm", hsize=92, hook2="3 வினாடியில் பதில்?", s=0, e=4.0, svg=f'''
<text class="fig" x="24" y="44">QUICK CHECK</text>
<circle class="until" data-end="3.0" cx="389" cy="250" r="140" fill="none" stroke="#2E5878" stroke-width="18"/>
<circle class="draw" data-t="0" data-d="3.0" data-lin="1" data-hide="1" pathLength="1" cx="389" cy="250" r="140" fill="none" stroke="{OR}" stroke-width="18" transform="rotate(-90 389 250)"/>
<text class="count" data-t="0" data-n="3" x="389" y="295" text-anchor="middle" style="font:800 130px Inter" fill="#fff">3</text>
<g style="font:700 40px Inter" fill="#fff" text-anchor="middle">
<rect x="30" y="470" width="226" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="143" y="550">0.254</text>
<rect x="276" y="470" width="226" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="389" y="550">0.0254</text>
<rect x="522" y="470" width="226" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="635" y="550">0.00254</text></g>
<text x="389" y="660" text-anchor="middle" style="font:600 26px Inter" fill="#9FC3DD">mm · ANSWER IN THIS REEL</text>''')


def lrow(y, inch, mm, t, hl=False):
    col = OR if hl else "#fff"
    return f'''<g class="a" data-t="{t}"><rect x="40" y="{y}" width="698" height="78" rx="12" fill="#123A57" stroke="{OR if hl else LINE}" stroke-width="{3 if hl else 2}"/>
<text x="290" y="{y+52}" text-anchor="end" style="font:700 36px Inter" fill="{col}">{inch} in</text>
<text x="389" y="{y+52}" text-anchor="middle" style="font:700 36px Inter" fill="#9FC3DD">=</text>
<text x="700" y="{y+52}" text-anchor="end" style="font:700 36px Inter" fill="{col}">{mm} mm</text></g>'''


R28 = dict(id="28", slug="Inch_to_mm_25p4", scenes=[
 R28_HOOK,
 dict(s=4.0, e=8.2, tag="ANSWER  /  02", title="= 0.0254 mm", tsize=80, sub="1 in = 25.4 mm (exact)", ssize=48,
      svg=fig("INCH → mm", "SOURCE: NIST", orange=True) + f'''
<text class="a" data-t="0.2" x="40" y="110" style="font:700 36px Inter" fill="#fff">1 in = 25.4 mm  EXACTLY</text>
<text class="code a" data-t="0.6" x="40" y="190" style="font-size:34px"><tspan fill="{W}">0.001 × 25.4 = </tspan><tspan fill="{OR}">0.0254</tspan></text>
<g class="a" data-t="1.0"><rect x="40" y="250" width="698" height="120" rx="18" fill="#123A57" stroke="{OR}" stroke-width="4"/>
<text x="389" y="330" text-anchor="middle" style="font:800 52px Inter" fill="{OR}">0.001 in = 0.0254 mm</text></g>
<text class="m a" data-t="1.4" x="40" y="440" style="font-size:22px">= 25.4 µm</text>''',
      body="Inch-ஐ mm ஆக்க 25.4-ஆல் பெருக்குங்கள்."),
 dict(s=8.2, e=12.4, tag="LADDER  /  03", title="Inch ladder", tsize=76, sub="in → mm: × 25.4", ssize=48,
      svg=fig("in → mm") + lrow(64, "1", "25.4", 0.1) + lrow(156, "0.1", "2.54", 0.4)
          + lrow(248, "0.01", "0.254", 0.7) + lrow(340, "0.001", "0.0254", 1.0, hl=True)
          + '<text class="m a" data-t="1.3" x="40" y="470" style="font-size:22px">EACH STEP ÷ 10</text>'),
 dict(s=12.4, e=16.6, tag="CHECK  /  04", title="Check the unit mode", tsize=64, sub="Program எந்த unit?", ssize=48,
      svg=fig("HAAS MILL EXAMPLE", "CHECK YOUR MANUAL", orange=True) + f'''
<g class="a" data-t="0.2"><rect x="40" y="76" width="330" height="130" rx="14" fill="#123A57" stroke="{OR}" stroke-width="3"/>
<text x="205" y="134" text-anchor="middle" style="font:800 44px Inter" fill="{OR}">G20</text>
<text x="205" y="180" text-anchor="middle" style="font:600 26px Inter" fill="#fff">INCH</text></g>
<g class="a" data-t="0.4"><rect x="408" y="76" width="330" height="130" rx="14" fill="#123A57" stroke="{GRN}" stroke-width="3"/>
<text x="573" y="134" text-anchor="middle" style="font:800 44px Inter" fill="{GRN}">G21</text>
<text x="573" y="180" text-anchor="middle" style="font:600 26px Inter" fill="#fff">METRIC (mm)</text></g>
<text class="a" data-t="0.8" x="40" y="270" style="font:700 28px Inter" fill="#fff">SETTING 9 SELECTS INCH / mm</text>
<text class="a" data-t="1.1" x="40" y="320" style="font:700 28px Inter" fill="#fff">G20 / G21 MUST MATCH IT</text>
<text class="m a" data-t="1.4" x="40" y="390" style="font-size:22px">SOURCE: HAAS MILL PROGRAMMING WORKBOOK</text>
<text class="m a" data-t="1.4" x="40" y="430" style="font-size:22px">OTHER CONTROLS MAY DIFFER</text>''',
      body="Drawing, program, control: ஒரே unit?", body_t=1.6),
 dict(s=16.6, e=21.0, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="0.001 in = 0.0254 mm", ssize=48,
      svg=fig("HOW TO ANSWER") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "× 25.4", "in → mm: 25.4-ஆல் பெருக்கு", 0.2)
          + checkrow(255, 2, "÷ 25.4", "mm → in: 25.4-ஆல் வகு", 0.5)
          + checkrow(395, 3, "CHECK UNIT MODE", "Haas: G20 / G21, Setting 9", 0.8),
      cta=True, cta_t=1.4),
])

REELS = [R24, R25, R26, R27, R28]
