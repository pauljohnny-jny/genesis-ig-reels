from gen import *

SEND = "நண்பருக்கு அனுப்புங்கள்."


def box(x, y, w, h, stroke=LINE, sw=2, fill="#123A57", rx=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def chip(x, y, w, lab, t, col="#fff", stroke=LINE):
    return (f'<g class="a" data-t="{t:.2f}">{box(x, y, w, 64, stroke, 3 if stroke != LINE else 2)}'
            f'<text x="{x + w/2:.0f}" y="{y + 43}" text-anchor="middle" style="font:700 26px Inter" fill="{col}">{esc(lab)}</text></g>')


def teeth(x, y, w, h, p=16, fill="#9DB9D0", stroke=LINE):
    """Vertical threaded cylinder (side view, schematic): body x..x+w, y..y+h, saw-tooth flanks of pitch p."""
    n = int(h // p)
    L = "".join(f"L{x - 7} {y + k*p + p/2:.0f}L{x} {y + (k+1)*p:.0f}" for k in range(n))
    R = "".join(f"L{x + w + 7} {y + h - k*p - p/2:.0f}L{x + w} {y + h - (k+1)*p:.0f}" for k in range(n))
    return f'<path d="M{x} {y}{L}L{x} {y + h}L{x + w} {y + h}{R}L{x + w} {y}Z" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>'


def plug_gauge(cx, top, go_h=120, hd_h=140, ng_h=80, w=84):
    """Double-ended thread plug gauge, GO end up (green band), NOT GO end down (red band). Schematic."""
    x = cx - w/2
    y1 = top + go_h; y2 = y1 + hd_h
    return (teeth(x, top, w, go_h) + f'<rect x="{x - 4}" y="{y1 - 14}" width="{w + 8}" height="14" fill="{GRN}"/>'
            + f'<rect x="{cx - 30}" y="{y1}" width="60" height="{hd_h}" rx="8" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>'
            + f'<text x="{cx}" y="{y1 + hd_h/2 - 8:.0f}" text-anchor="middle" style="font:700 20px Inter" fill="{GRN}">GO</text>'
            + f'<text x="{cx}" y="{y1 + hd_h/2 + 26:.0f}" text-anchor="middle" style="font:700 20px Inter" fill="{RED}">NG</text>'
            + f'<rect x="{x - 4}" y="{y2}" width="{w + 8}" height="14" fill="{RED}"/>' + teeth(x, y2 + 14, w, ng_h))


# =====================================================================================================
# REEL 45: Thread plug gauge GO / NOT GO (ISO metric internal thread). Target ~28 s. CTA: SAVE.
# Hook format: (4) verbatim interview question. Options considered:
#   "NOT GO: எத்தனை turns?" (interview question; chosen: the number 2 is the answer, the NOT GO end screws in at frame 1,
#       answered in scene 2 and echoed in scene 5)
#   "NOT GO: 0, 2 or full?" (countdown quiz) / "NOT GO 3 turns = OK?" (wrong vs right)
# Source (read 22 Nov 2026): ISO 1502:1978 "ISO general purpose metric screw threads – Gauges", clause 7 (standards.iteh.ai
#   sample, cdn.standards.iteh.ai/samples/6091/.../ISO-1502-1978.pdf); current edition ISO 1502:1996 (same gauge system).
#   7.2.1 GO screw plug gauge: a) "checks the virtual size of the internal thread on the GO side (gauging the virtual pitch
#     diameter) ... by checking the minimum limit of the pitch diameter ... In addition it checks the minimum limit of the
#     major diameter ... It does not check the minor diameter of the internal thread." b) "It is recommended that the GO screw
#     plug gauge be checked regularly for wear." c) "The GO screw plug gauge screwed by hand, without using excessive force,
#     shall pass over the whole length of the workpiece thread. If this is not possible, the workpiece thread does not comply."
#   7.2.2 NOT GO screw plug gauge: a) "checks whether the actual pitch diameter exceeds the specified maximum size."
#     c) "screwed by hand, without using excessive force, may enter into both ends of the threaded part, but not more than two
#     turns of thread. If it can be screwed in more than two turns of thread, the workpiece thread does not comply."
# REV 2 (23 Nov 2026, after ChatGPT CHANGES REQUIRED on rev 2f9380d3): re-read ISO 1502:1996 sample (cdn.standards.iteh.ai
#   samples/6092): 7.2.1 c) GO "shall enter the whole length of the workpiece thread"; 7.2.2 c) NOT GO by hand, no excessive
#   force, "may enter into both ends of the threaded part, but by not more than two turns of thread" – footnote 6 "The two
#   turns of thread are determined when withdrawing the gauge" – and "shall not pass completely through a workpiece with a
#   length of thread of three threads or less"; 7.2.2 b) NOT GO checked regularly for wear. Added the short-thread rule and
#   withdrawal counting; replaced "BOTH PASS"; removed the inch aside.
#   Secondary: Thread Check Inc. (gauge maker) in Quality Magazine "Internal part thread inspection": metric No-Go plug may
#     enter up to two turns; inch (ASME B1.2) up to three – so the reel states "ISO METRIC".
R45_H = dict(hook="NOT GO: எத்தனை turns?", hsize=58, hook2="Interview கேள்வி · ISO metric", h2size=44, s=0, e=4.2, svg=f'''
<text class="fig" x="24" y="44">THREAD PLUG GAUGE · SCHEMATIC</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">ISO METRIC</text>
<rect x="120" y="470" width="221" height="160" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="437" y="470" width="221" height="160" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<path d="{"".join(f"M341 {470 + k*16}l-7 8l7 8M437 {470 + k*16}l7 8l-7 8" for k in range(10))}" stroke="{LINE}" stroke-width="2" fill="none"/>
<text x="230" y="560" text-anchor="middle" style="font:600 22px Inter" fill="#fff">PART</text>
<g class="move" data-t="0" data-d="1.6" data-dy="32">{plug_gauge(389, 116)}</g>
<text class="a" data-t="0.6" x="560" y="330" style="font:800 30px Inter" fill="{OR}">1 TURN</text>
<text class="a" data-t="1.3" x="560" y="380" style="font:800 30px Inter" fill="{OR}">2 TURNS</text>
<text class="a" data-t="2.0" x="560" y="430" style="font:800 30px Inter" fill="{RED}">3 ?</text>
{chip(40, 658, 220, "≤ 2 TURNS", 0.0)}{chip(279, 658, 220, "≤ 5 TURNS", 0.0)}{chip(518, 658, 220, "FULL LENGTH", 0.0)}
<text class="m a" data-t="2.4" x="389" y="740" text-anchor="middle" style="font-size:20px">ANSWER IN THIS REEL · SCHEMATIC</text>''')

R45 = dict(id="45", slug="Thread_Plug_Gauge_GO_NOT_GO", scenes=[
 R45_H,
 dict(s=4.2, e=10.2, tag="ANSWER  /  02", title="NOT GO ≤ 2 turns", tsize=74, sub="அதற்கு மேல் போனால் REJECT.", ssize=46,
      svg=fig("ISO 1502 · CLAUSE 7.2", "INTERNAL THREAD", orange=True) + f'''
<g class="a" data-t="0.2">{box(40, 62, 698, 120, GRN, 3)}
<text x="66" y="108" style="font:800 32px Inter" fill="{GRN}">GO END</text>
<text x="66" y="156" style="font:700 27px Inter" fill="#fff">ENTERS WHOLE THREAD LENGTH</text></g>
<g class="a" data-t="0.8">{box(40, 194, 698, 160, RED, 3)}
<text x="66" y="240" style="font:800 32px Inter" fill="{RED}">NOT GO END</text>
<text x="66" y="286" style="font:700 27px Inter" fill="#fff">MAX 2 TURNS · EACH END</text>
<text x="66" y="328" style="font:600 23px Plex" fill="#BFD6E8">TURNS COUNTED ON WITHDRAWAL</text></g>
<g class="a" data-t="1.3">{box(40, 366, 698, 96, OR, 3)}
<text x="66" y="406" style="font:700 24px Inter" fill="{OR}">SHORT THREAD (≤ 3 THREADS):</text>
<text x="66" y="442" style="font:700 24px Inter" fill="#fff">NOT GO MUST NOT PASS THROUGH</text></g>
<text class="m a" data-t="1.6" x="389" y="488" text-anchor="middle" style="font-size:20px">BY HAND · NO EXCESSIVE FORCE · ISO 1502:1996</text>''',
      body="ISO 1502: கையால், அதிக force இல்லாமல்.", body_t=1.5),
 dict(s=10.2, e=16.4, tag="WHY  /  03", title="Two limits", tsize=80, sub="GO = min · NOT GO = max", ssize=48,
      svg=fig("WHAT EACH END CHECKS", "ISO 1502", orange=True) + f'''
<g class="a" data-t="0.2">{box(40, 66, 698, 150, GRN, 3)}
<text x="66" y="116" style="font:800 30px Inter" fill="{GRN}">GO</text>
<text x="160" y="116" style="font:700 28px Inter" fill="#fff">MIN PITCH Ø (VIRTUAL)</text>
<text x="160" y="160" style="font:700 28px Inter" fill="#fff">+ MIN MAJOR Ø</text>
<text x="160" y="198" style="font:600 22px Plex" fill="#BFD6E8">NOT THE MINOR Ø</text></g>
<g class="a" data-t="0.8">{box(40, 236, 698, 110, RED, 3)}
<text x="66" y="300" style="font:800 30px Inter" fill="{RED}">NOT GO</text>
<text x="210" y="300" style="font:700 28px Inter" fill="#fff">MAX PITCH Ø (ACTUAL)</text></g>
<g class="a" data-t="1.3">{box(40, 366, 698, 120, OR, 3)}
<text x="389" y="412" text-anchor="middle" style="font:700 25px Inter" fill="#fff">GO GOES THROUGH + NOT GO ≤ 2 TURNS</text>
<text x="389" y="456" text-anchor="middle" style="font:800 28px Inter" fill="{OR}">→ THREAD IN LIMITS</text></g>''',
      body="2 turns ஏன்? முதல் threads முழுமையாக இருக்காது.", body_t=1.7),
 dict(s=16.4, e=22.6, tag="CHECK  /  04", title="Gauge it right", tsize=80, sub="மூன்று பழக்கம்.", ssize=50,
      svg=fig("THREAD PLUG GAUGE") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "BY HAND, NO FORCE", "Wrench, அதிக force வேண்டாம்", 0.2)
          + checkrow(255, 2, "GO: FULL LENGTH", "முழு thread நீளமும் போக வேண்டும்", 0.7)
          + checkrow(395, 3, "NOT GO: BOTH ENDS", "ஒவ்வொரு பக்கமும் ≤ 2 turns", 1.2),
      body="Gauge-களை wear-க்கு regular-ஆக check செய்யுங்கள்.", body_t=1.7),
 dict(s=22.6, e=28.2, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="NOT GO: 2 turns வரை மட்டும்.", ssize=44,
      svg=fig("HOW TO ANSWER") + chip(40, 66, 330, "GO: FULL LENGTH", 0.1, GRN, GRN) + chip(388, 66, 350, "NOT GO ≤ 2 TURNS", 0.25, RED, RED)
          + chip(40, 150, 698, "ISO 1502 · METRIC INTERNAL THREAD", 0.4) + '''
<text class="w a" data-t="0.8" x="40" y="300" style="font-size:30px">"GO முழுதும் கையால் போக வேண்டும்;</text>
<text class="w a" data-t="0.8" x="40" y="346" style="font-size:30px"> NOT GO 2 turns-க்கு மேல் போனால் reject."</text>
<text class="m a" data-t="1.2" x="40" y="440" style="font-size:22px">≤ 3 THREADS LONG: NOT GO MUST NOT PASS THROUGH</text>''',
      cta=True, cta_t=1.6),
])


# =====================================================================================================
# REEL 46: Blind-hole tapping – drill deeper than the thread. Target ~28 s. CTA: SEND.
# Hook format: (1) cold-open demo. Options considered:
#   "Drill 12, thread 12?" (demo: the tap runs to the bottom of a 12 mm hole and stops short of full thread; chosen: specific
#       numbers, tap moves at frame 1, answered in scene 2 (17 mm) and echoed in scene 5)
#   "M8 thread 12: drill எவ்வளவு ஆழம்?" (interview question) / "Drill 12, 15 or 17?" (countdown quiz)
# Source (read 22 Nov 2026): Kennametal Technical Tip #65 "Tap Chamfer Length vs. Tool Life in Threading"
#   (cdn.mscdirect.com/global/media/pdf/product/kmt-tech-tips-chamfer.pdf; same text on kennametal.com): "To determine the
#   longest chamfer for blind holes: Subtract the full thread length required plus one pitch from the drill depth (the extra
#   pitch enables clearance at the bottom of the hole for spindle over-spin and chips). Then divide this figure by the
#   [pitch]." Example 1/4-20: .473 − .250 − .050 = .173; .173 ÷ .050 = 3.5 → "select a standard tap with thread chamfer no
#   longer than 3.5". "A 4-flute semi-bottoming tap has 12 working teeth; a bottoming tap has 8" (i.e. 3 and 2 chamfer
#   threads). "An increase in chamfer length will result in an increase in tap life."
#   Rearranged (same relation): drill depth ≥ full thread length + chamfer length + 1 pitch.
#   Our metric worked example: M8 × 1.25, full thread 12 mm, 3-thread chamfer = 3 × 1.25 = 3.75 mm, + 1 pitch 1.25 mm
#   → 12 + 3.75 + 1.25 = 17.0 mm. Assumption: depth to the end of the full drill diameter (drill point extra), cut tap.
def tap(x, y, w=64, body=250, chamfer=48, shank=150):
    """Schematic tap pointing down: shank above y, threaded body y..y+body, tapered chamfer at the tip."""
    tb = teeth(x, y, w, body, 14, "#9DB9D0")
    tip = f'<path d="M{x} {y + body}L{x + 12} {y + body + chamfer}H{x + w - 12}L{x + w} {y + body}Z" fill="#C9DCEB" stroke="{LINE}" stroke-width="2.5"/>'
    return f'<rect x="{x + 10}" y="{y - shank}" width="{w - 20}" height="{shank}" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>' + tb + tip


R46_H = dict(hook="Drill 12, thread 12?", hsize=84, hook2="Tap அடியில் இடிக்கலாம்!", h2size=54, s=0, e=4.2, flash_t=1.5, svg=f'''
<text class="fig" x="24" y="44">SECTION · SCHEMATIC · mm</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">M8 × 1.25 · BLIND HOLE</text>
<g class="shake" data-t="1.5">
<rect x="60" y="330" width="250" height="330" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="410" y="330" width="250" height="330" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="310" y="580" width="100" height="80" fill="{STEEL}"/>
<path d="M310 330V580H410V330" stroke="{LINE}" stroke-width="2.5" fill="none"/>
<g class="move" data-t="0" data-d="1.5" data-dy="118">{tap(328, 160, shank=80)}</g>
<path d="M690 330V580" stroke="{OR}" stroke-width="3" marker-start="url(#ao)" marker-end="url(#ao)"/>
<text x="702" y="462" style="font:800 30px Inter" fill="{OR}">12</text>
</g>
<text class="a" data-t="1.6" x="389" y="710" text-anchor="middle" style="font:800 34px Inter" fill="{RED}">NO ROOM: CHAMFER + CHIPS</text>
<text class="m a" data-t="2.0" x="389" y="740" text-anchor="middle" style="font-size:20px">DRILL DEPTH = THREAD DEPTH (WRONG)</text>''')

R46 = dict(id="46", slug="Blind_Hole_Tapping_Drill_Depth", scenes=[
 R46_H,
 dict(s=4.2, e=10.2, tag="ANSWER  /  02", title="Drill ≥ 17 mm", tsize=80, sub="M8 × 1.25 · full thread 12 mm", ssize=44,
      svg=fig("KENNAMETAL TECH TIP #65", "BLIND HOLE", orange=True) + f'''
<g class="a" data-t="0.2">{box(40, 66, 698, 80)}
<text x="66" y="117" style="font:700 30px Inter" fill="#fff">FULL THREAD</text><text x="712" y="118" text-anchor="end" style="font:800 32px Inter" fill="#fff">12.00</text></g>
<g class="a" data-t="0.6">{box(40, 162, 698, 80, OR, 3)}
<text x="66" y="213" style="font:700 30px Inter" fill="#fff">+ CHAMFER 3 × 1.25</text><text x="712" y="214" text-anchor="end" style="font:800 32px Inter" fill="{OR}">3.75</text></g>
<g class="a" data-t="1.0">{box(40, 258, 698, 80, OR, 3)}
<text x="66" y="309" style="font:700 30px Inter" fill="#fff">+ ONE PITCH</text><text x="712" y="310" text-anchor="end" style="font:800 32px Inter" fill="{OR}">1.25</text></g>
<g class="a" data-t="1.4">{box(40, 362, 698, 90, GRN, 3)}
<text x="66" y="419" style="font:800 34px Inter" fill="{GRN}">MIN DRILL DEPTH</text><text x="712" y="420" text-anchor="end" style="font:800 38px Inter" fill="{GRN}">17.00 mm</text></g>''',
      body="Thread + chamfer + 1 pitch (Kennametal).", body_t=1.8),
 dict(s=10.2, e=16.4, tag="WHY  /  03", title="Why the extra?", tsize=80, sub="Tap முனையில் full thread இல்லை.", ssize=38,
      svg=fig("TAP · SCHEMATIC", "NOT TO SCALE", orange=True) + f'''
{tap(110, 170, 80, 230, 70, 110)}
<path d="M220 400H250M220 470H250" stroke="{OR}" stroke-width="2"/>
<g class="a" data-t="0.3"><path d="M235 400V470" stroke="{OR}" stroke-width="3" marker-start="url(#ao)" marker-end="url(#ao)"/>
<text x="270" y="430" style="font:800 28px Inter" fill="{OR}">CHAMFER</text>
<text x="270" y="466" style="font:600 22px Plex" fill="#BFD6E8">TAPERED · PARTIAL THREAD</text></g>
<g class="a" data-t="0.9">{box(270, 70, 468, 130, LINE, 2)}
<text x="292" y="122" style="font:800 28px Inter" fill="#fff">+ ONE PITCH</text>
<text x="292" y="168" style="font:600 22px Plex" fill="#BFD6E8">SPINDLE OVER-SPIN + CHIPS</text></g>
<g class="a" data-t="1.4">{box(270, 230, 468, 130, GRN, 3)}
<text x="292" y="282" style="font:800 28px Inter" fill="{GRN}">LONGER CHAMFER</text>
<text x="292" y="328" style="font:600 22px Plex" fill="#BFD6E8">→ LONGER TAP LIFE</text></g>''',
      body="Chamfer நீளம் tap type-ஐப் பொறுத்து மாறும்.", body_t=1.8),
 dict(s=16.4, e=22.6, tag="CHECK  /  04", title="Before you tap", tsize=80, sub="மூன்று check.", ssize=50,
      svg=fig("BLIND HOLE") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "FULL THREAD LENGTH", "Drawing-ல் உள்ள அளவு", 0.2)
          + checkrow(255, 2, "TAP CHAMFER", "Chamfer threads × pitch", 0.7)
          + checkrow(395, 3, "+ ONE PITCH", "Over-spin, chip-க்கு இடம்", 1.2),
      body="Chamfer threads-ஐ tap catalogue-ல் பாருங்கள்.", body_t=1.7),
 dict(s=22.6, e=28.2, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="Drill 12 இல்லை: 17 mm.", ssize=48,
      svg=fig("HOW TO ANSWER") + chip(40, 66, 400, "12 + 3.75 + 1.25", 0.1, OR, OR) + chip(458, 66, 280, "= 17 mm", 0.25, GRN, GRN)
          + chip(40, 150, 698, "THREAD + CHAMFER + 1 PITCH", 0.4) + '''
<text class="w a" data-t="0.8" x="40" y="300" style="font-size:30px">"Thread நீளம் மட்டும் அல்ல; chamfer-ம்</text>
<text class="w a" data-t="0.8" x="40" y="346" style="font-size:30px"> ஒரு pitch-ம் சேர்த்து drill செய்வேன்."</text>
<text class="m a" data-t="1.2" x="40" y="440" style="font-size:22px">CUT TAP · FULL-Ø DEPTH · DRILL POINT EXTRA</text>''',
      cta=True, cta_t=1.6, cta_icon="send", cta_text=SEND),
])

REELS = [R45, R46]
