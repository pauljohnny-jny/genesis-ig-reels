from gen import *

def cutter(cx, cy, r, spin=True):
    teeth = "".join(f'<path d="M{cx} {cy-r} l14 18 h-28z" fill="{OR}" transform="rotate({a} {cx} {cy})"/>' for a in (0, 90, 180, 270))
    cls = f'class="spin" data-cx="{cx}" data-cy="{cy}"' if spin else ""
    return f'''<g {cls}><circle cx="{cx}" cy="{cy}" r="{r}" fill="#6C93B4" stroke="{LINE}" stroke-width="3"/>{teeth}
<circle cx="{cx}" cy="{cy}" r="8" fill="{PANEL}"/></g>'''

def given(rows, t0=0.3):
    out = []
    for k, (sym, val, lab, col) in enumerate(rows):
        y = 140 + k * 130
        out.append(f'<g class="a" data-t="{t0 + k*0.45:.2f}"><text x="40" y="{y}" style="font:700 46px Inter" fill="{col}">{sym}</text>'
                   f'<text x="120" y="{y}" style="font:600 42px Inter" fill="{col}">{esc(val)}</text>'
                   f'<text class="m" x="40" y="{y+42}">{esc(lab)}</text></g>')
    return "".join(out)

def steps(lines, t0=0.3, dt=0.6, y0=140, dy=95):
    out = []
    for k, (txt, col, size) in enumerate(lines):
        out.append(f'<text class="a" data-t="{t0 + k*dt:.2f}" x="40" y="{y0 + k*dy}" style="font:600 {size}px Inter" fill="{col}">{esc(txt)}</text>')
    return "".join(out)

def frac(cx, y, left, num, den, t=0.3, size=50):
    return f'''<g class="a" data-t="{t}"><text x="{cx-250}" y="{y+18}" style="font:700 {size+6}px Inter" fill="{OR}">{esc(left)}</text>
<text x="{cx+60}" y="{y-22}" text-anchor="middle" style="font:600 {size}px Inter" fill="#fff">{esc(num)}</text>
<path d="M{cx-110} {y}H{cx+230}" stroke="#fff" stroke-width="4"/>
<text x="{cx+60}" y="{y+62}" text-anchor="middle" style="font:600 {size}px Inter" fill="#fff">{esc(den)}</text></g>'''

# ---------------- REEL 06: spindle RPM ----------------
R06 = dict(id="06", slug="Spindle_RPM_Formula", scenes=[
 dict(s=0, e=5, tag="QUICK MATHS  /  01", title="RPM = ?", sub="கணக்கிட முடியுமா?",
      svg=fig("GIVEN", "EXAMPLE VALUES", orange=True) + given([("Vc", "= 120 m/min", "CUTTING SPEED", "#fff"), ("D", "= 10 mm", "CUTTER DIAMETER", "#fff"), ("n", "= ? rpm", "SPINDLE SPEED", OR)], t0=0) + cutter(600, 270, 95),
      body="Cutting speed-ஐ RPM-ஆக மாற்றத் தெரியுமா?"),
 dict(s=5, e=11, tag="FORMULA  /  02", title="Formula", sub="இதுதான் கணக்கு.",
      svg=fig("METRIC", "SOURCE: SANDVIK COROMANT") + frac(330, 220, "n =", "Vc × 1000", "π × D", t=0.2, size=54) + f'''
<text class="m a" data-t="1.0" x="389" y="400" text-anchor="middle">n: rpm · Vc: m/min · D: mm</text>
<text class="mo a" data-t="1.5" x="389" y="450" text-anchor="middle">× 1000 : metre → mm</text>''',
      body="Vc metre/min-ல், D mm-ல் இருப்பதால் 1000-ஆல் பெருக்குகிறோம்."),
 dict(s=11, e=17.5, tag="WORKED  /  03", title="Work it out", sub="படிப்படியாக.",
      svg=fig("EXAMPLE", "Vc 120 · D 10") + steps([("120 × 1000 = 120000", "#fff", 42), ("π × 10 = 31.42", "#fff", 42), ("120000 ÷ 31.42", "#fff", 42), ("≈ 3820 rpm", OR, 56)], t0=0.2, dt=0.7) + tick(420, 410, 2.6),
      body="பதில்: சுமார் 3820 rpm."),
 dict(s=17.5, e=23.5, tag="REAL JOB  /  04", title="Real values", sub="Vc எங்கிருந்து?",
      svg=fig("WHERE TO GET THEM") + "".join(
          f'''<g class="a" data-t="{0.3+k*0.6:.1f}"><text x="40" y="{130+k*135}" style="font:700 44px Inter" fill="{OR}">{s}</text>
<path d="M120 {118+k*135}H170" stroke="#fff" stroke-width="3" marker-end="url(#aw)"/>
<text class="w" x="190" y="{130+k*135}">{esc(a)}</text><text class="ta" x="190" y="{172+k*135}" style="font-size:26px">{esc(b)}</text></g>'''
          for k, (s, a, b) in enumerate([("Vc", "TOOL MAKER'S CATALOGUE", "material, tool grade-க்கு ஏற்ப"), ("D", "ACTUAL CUTTER DIAMETER", "drawing-ல் அல்ல, tool-ல்"), ("n", "CHECK MACHINE MAX RPM", "கணக்கு அதிகமானால் குறைக்கவும்")])),
      body="120 m/min ஒரு உதாரணம் மட்டுமே. உண்மையான மதிப்பு tool catalogue-ல் இருக்கும்."),
 dict(s=23.5, e=30, tag="REMEMBER  /  05", title="Remember", sub="சிறிய D → அதிக RPM.",
      svg=fig("SAME Vc = 120 m/min", "EXAMPLE VALUES", orange=True) + "".join(
          f'''<g class="a" data-t="{0.3+k*0.5:.1f}"><text class="wb" x="40" y="{150+k*125}">{d}</text>
<rect class="draw" data-t="{0.3+k*0.5:.1f}" x="150" y="{118+k*125}" width="{w}" height="44" rx="6" fill="{OR if k==0 else '#6C93B4'}"/>
<text class="w" x="{165+w}" y="{152+k*125}">{v} rpm</text></g>'''
          for k, (d, w, v) in enumerate([("Ø6", 400, "6366"), ("Ø10", 240, "3820"), ("Ø20", 120, "1910")])),
      body="அதே cutting speed-க்கு, சிறிய cutter வேகமாகச் சுழல வேண்டும்.", body_t=1.8, cta=True, cta_t=2.4),
])

# ---------------- REEL 07: table feed ----------------
R07 = dict(id="07", slug="Feed_Rate_Formula", scenes=[
 dict(s=0, e=5, tag="QUICK MATHS  /  01", title="Feed = ?", sub="F மதிப்பு எவ்வளவு?",
      svg=fig("GIVEN", "EXAMPLE VALUES", orange=True) + given([("n", "= 3820 rpm", "SPINDLE SPEED", "#fff"), ("z", "= 4 flutes", "NUMBER OF TEETH", "#fff"), ("fz", "= 0.04 mm", "FEED PER TOOTH", "#fff")], t0=0) + cutter(620, 270, 90) +
          f'<text x="520" y="440" style="font:700 44px Inter" fill="{OR}">F = ?</text>',
      body="RPM தெரியும். இப்போது table feed (F) எவ்வளவு?"),
 dict(s=5, e=11, tag="FORMULA  /  02", title="Formula", sub="ஒவ்வொரு பல்லுக்கும் chip.",
      svg=fig("METRIC", "SOURCE: SANDVIK COROMANT") + f'''
<text class="a" data-t="0.2" x="389" y="170" text-anchor="middle" style="font:700 60px Inter" fill="#fff"><tspan fill="{OR}">vf</tspan> = fz × z × n</text>
<g class="a" data-t="0.9" style="font:500 28px Plex"><text x="120" y="265" fill="{OR}">vf</text><text x="210" y="265" fill="#9FC3DD">mm/min (F in G94)</text></g>
<g class="a" data-t="1.3" style="font:500 28px Plex"><text x="120" y="320" fill="#fff">fz</text><text x="210" y="320" fill="#9FC3DD">mm per tooth</text></g>
<g class="a" data-t="1.7" style="font:500 28px Plex"><text x="120" y="375" fill="#fff">z</text><text x="210" y="375" fill="#9FC3DD">number of teeth</text></g>
<g class="a" data-t="2.1" style="font:500 28px Plex"><text x="120" y="430" fill="#fff">n</text><text x="210" y="430" fill="#9FC3DD">spindle rpm</text></g>''',
      body="fz என்பது ஒவ்வொரு பல்லுக்குமான feed (mm/tooth)."),
 dict(s=11, e=17.5, tag="WORKED  /  03", title="Work it out", sub="படிப்படியாக.",
      svg=fig("EXAMPLE", "fz 0.04 · z 4 · n 3820") + steps([("0.04 × 4 = 0.16 mm/rev", "#fff", 42), ("0.16 × 3820", "#fff", 42), ("= 611.2 mm/min", "#fff", 42), ("≈ F611 (G94)", OR, 54)], t0=0.2, dt=0.7) + tick(460, 410, 2.6),
      body="Feed per minute (G94) mode-ல் இது சுமார் F611."),
 dict(s=17.5, e=24, tag="ERROR CHECK  /  04", title="Watch out", sub="Flute எண்ணிக்கை.",
      svg=fig("4-FLUTE CUTTER", "EXAMPLE VALUES", orange=True) + f'''
<g class="a" data-t="0.3"><rect x="30" y="80" width="718" height="150" rx="12" fill="#123A57" stroke="{GRN}" stroke-width="3"/>
<text class="w" x="110" y="140">z = 4 used</text><text class="w" x="110" y="195">F611 → fz 0.04</text></g>{tick(68, 155, 0.6)}
<g class="a" data-t="1.4"><rect x="30" y="260" width="718" height="150" rx="12" fill="#123A57" stroke="{RED}" stroke-width="3"/>
<text class="w" x="110" y="320">z = 2 used by mistake</text><text class="w" x="110" y="375">F306 → actual fz 0.02</text></g>{cross(68, 335, 1.7)}
<text class="mo a" data-t="2.4" x="40" y="462" style="fill:{RED}">CHIP HALF AS THICK</text>''',
      body="4-flute cutter-க்கு 2 என்று கணக்கிட்டால், ஒவ்வொரு பல்லுக்கும் chip பாதியாகும்."),
 dict(s=24, e=30.5, tag="REMEMBER  /  05", title="Remember", sub="இரண்டு formula.",
      svg=fig("CHAIN") + f'''
<g class="a" data-t="0.3"><rect x="60" y="80" width="658" height="110" rx="14" fill="#123A57" stroke="{LINE}" stroke-width="2.5"/>
<text x="389" y="150" text-anchor="middle" style="font:600 40px Inter" fill="#fff">n = Vc × 1000 ÷ (π × D)</text></g>
<path class="a" data-t="0.8" d="M389 200V250" stroke="{OR}" stroke-width="4" marker-end="url(#ao)"/>
<g class="a" data-t="1.0"><rect x="60" y="262" width="658" height="110" rx="14" fill="#123A57" stroke="{OR}" stroke-width="3"/>
<text x="389" y="332" text-anchor="middle" style="font:600 40px Inter" fill="#fff">vf = fz × z × n</text></g>
<text class="mo a" data-t="1.5" x="389" y="440" text-anchor="middle">Vc, fz: FROM THE TOOL CATALOGUE</text>''',
      body="மதிப்புகள் உதாரணம் மட்டுமே; catalogue பாருங்கள்.", body_t=1.8, cta=True, cta_t=2.4),
])

# ---------------- REEL 08: climb vs conventional ----------------
def climb_diag(label=True, t=0.2):
    return f'''<g class="a" data-t="{t}">
<path d="M40 320H389A70 70 0 0 0 459 250H738V480H40Z" fill="{STEEL}" stroke="{LINE}" stroke-width="3"/>
<text class="m" x="600" y="440" style="fill:#fff">WORK</text></g>
{cutter(389, 250, 70)}
<g class="a" data-t="{t+0.3}"><path d="M150 110H560" stroke="#fff" stroke-width="3" marker-end="url(#aw)"/><text class="m" x="150" y="96">TOOL FEED</text>
<path d="M300 212A92 92 0 0 1 460 196" stroke="{LINE}" stroke-width="3" fill="none" marker-end="url(#aw)"/><text class="m" x="590" y="96" style="font-size:20px">M03 · CW</text></g>'''

def conv_diag(t=0.2):
    return f'''<g class="a" data-t="{t}">
<path d="M40 230H389A70 70 0 0 1 459 300H738V70H40Z" fill="{STEEL}" stroke="{LINE}" stroke-width="3"/>
<text class="m" x="600" y="120" style="fill:#fff">WORK</text></g>
{cutter(389, 300, 70)}
<g class="a" data-t="{t+0.3}"><path d="M150 440H560" stroke="#fff" stroke-width="3" marker-end="url(#aw)"/><text class="m" x="150" y="486">TOOL FEED</text>
<path d="M300 340A92 92 0 0 0 460 356" stroke="{LINE}" stroke-width="3" fill="none" marker-start="url(#aw)"/><text class="m" x="590" y="486" style="font-size:20px">M03 · CW</text></g>'''

R08 = dict(id="08", slug="Climb_vs_Conventional", scenes=[
 dict(s=0, e=5.5, tag="COMPARE  /  01", title="Climb or conventional?", tsize=60, sub="ஒரே cutter, இரண்டு வழி.",
      svg=fig("TOP VIEW", "SCHEMATIC") + f'''
<g transform="translate(10 60) scale(0.48)">{climb_diag(t=0)}</g><g transform="translate(398 60) scale(0.48)">{conv_diag(t=0)}</g>
<path d="M389 70V470" stroke="#2E5878" stroke-width="2"/>
<text class="mo" x="195" y="340" text-anchor="middle">CLIMB (DOWN)</text><text class="mo" x="583" y="340" text-anchor="middle">CONVENTIONAL (UP)</text>
<text class="ta a" data-t="1.0" x="389" y="430" text-anchor="middle" style="font-size:30px">Chip எப்படி உருவாகிறது?</text>''',
      body="Cutter ஒரே திசையில் சுழல்கிறது. Work எந்தப் பக்கம் என்பதால் chip மாறுகிறது."),
 dict(s=5.5, e=12, tag="CLIMB  /  02", title="Climb (down)", sub="Chip: தடிமன் → மெல்லியது.",
      svg=fig("TOP VIEW", "SCHEMATIC") + climb_diag() + f'''
<g class="a" data-t="1.2"><circle cx="459" cy="250" r="12" fill="{OR}"/><text class="mo" x="480" y="230">ENTRY: THICK</text></g>
<g class="a" data-t="1.8"><circle cx="389" cy="320" r="10" fill="#fff"/><text class="m" x="180" y="360" style="fill:#fff">EXIT: THIN</text></g>''',
      body="பல் தடிமனான chip-உடன் நுழைகிறது; உரசல் (rubbing) குறைவு."),
 dict(s=12, e=18.5, tag="CONVENTIONAL  /  03", title="Conventional (up)", tsize=70, sub="Chip: மெல்லியது → தடிமன்.",
      svg=fig("TOP VIEW", "SCHEMATIC") + conv_diag() + f'''
<g class="a" data-t="1.2"><circle cx="389" cy="230" r="12" fill="{RED}"/><path d="M290 268L376 238" stroke="{RED}" stroke-width="3"/><text x="40" y="292" style="font:500 24px Plex" fill="{RED}">ENTRY: ZERO → RUBS</text></g>
<g class="a" data-t="1.8"><circle cx="459" cy="300" r="10" fill="#fff"/><text class="m" x="480" y="345" style="fill:#fff">EXIT: THICK</text></g>''',
      body="பல் பூஜ்ஜிய தடிமனில் நுழைந்து முதலில் உரசுகிறது; flank wear கூடும்."),
 dict(s=18.5, e=24.5, tag="ON CNC  /  04", title="On CNC", sub="பொதுவாக climb.",
      svg=fig("COMPARISON", "SOURCE: MITSUBISHI MATERIALS") + f'''
<g style="font:500 26px Plex">
<text x="300" y="100" fill="{OR}" style="font:700 30px Inter">CLIMB</text><text x="540" y="100" fill="#fff" style="font:700 30px Inter">CONV.</text>
<path d="M30 122H748" stroke="#2E5878" stroke-width="2"/>
<g class="a" data-t="0.4"><text x="30" y="180" fill="#9FC3DD">ENTRY CHIP</text><text x="300" y="180" fill="#fff">THICK</text><text x="540" y="180" fill="#fff">ZERO</text></g>
<g class="a" data-t="0.9"><text x="30" y="260" fill="#9FC3DD">RUBBING</text><text x="300" y="260" fill="#fff">LESS</text><text x="540" y="260" fill="#fff">MORE</text></g>
<g class="a" data-t="1.4"><text x="30" y="340" fill="#9FC3DD">TOOL LIFE</text><text x="300" y="340" fill="{GRN}">USUALLY</text><text x="300" y="372" fill="{GRN}">BETTER</text><text x="540" y="340" fill="#fff">—</text></g>
<g class="a" data-t="1.9"><text x="30" y="440" fill="#9FC3DD">BACKLASH</text><text x="300" y="440" fill="{RED}">CAN PULL</text><text x="300" y="472" fill="{RED}">THE WORK</text><text x="540" y="440" fill="#fff">—</text></g>
</g>''',
      body="Tool life-க்கு பொதுவாக climb சிறந்தது; ஆனால் machine, cutter, job-ஐப் பொறுத்து மாறும்."),
 dict(s=24.5, e=31, tag="INTERVIEW  /  05", title="Interview tip", sub="'ஏன்?' என்று விளக்குங்கள்.",
      svg=fig("CHECKLIST") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "THICK ENTRY", "உரசல் குறைவு, tool life கூடும்.", 0.3)
          + checkrow(255, 2, "BACKLASH", "Backlash உள்ள machine-ல் கவனம்.", 0.8)
          + checkrow(395, 3, "YOUR JOB", "எந்த job-ல் எதைப் பயன்படுத்தினீர்கள்?", 1.3),
      body="நீங்கள் பயன்படுத்திய முறையை உதாரணத்துடன் சொல்லுங்கள்.", body_t=1.8, cta=True, cta_t=2.4),
])

REELS = [R06, R07, R08]
