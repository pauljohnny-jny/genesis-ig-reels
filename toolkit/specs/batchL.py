from gen import *
W = "#E6F0F7"
SEND = "நண்பருக்கு அனுப்புங்கள்."
DIM = "#7FA6C4"


def box(x, y, w, h, stroke=LINE, sw=2, fill="#123A57", rx=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def chip(x, y, w, lab, t, col="#fff", stroke=LINE):
    return (f'<g class="a" data-t="{t:.2f}">{box(x, y, w, 64, stroke, 3 if stroke != LINE else 2)}'
            f'<text x="{x + w/2:.0f}" y="{y + 43}" text-anchor="middle" style="font:700 26px Inter" fill="{col}">{esc(lab)}</text></g>')


# =====================================================================================================
# REEL 39: Proving out a new program (Haas mill example, metric). Target 28 s. CTA: SAVE.
# Hook format: (1) cold-open demo. Options considered:
#   "To-go 25, gap 20?" (demo: DIST TO GO larger than the real gap -> tool would end 5 mm inside the part; chosen:
#       specific numbers, motion at frame 1, answered in scene 2 and echoed in scene 5)
#   "முதல் run: 100% rapid?" (wrong vs right) / "New program-ஐ எப்படி prove செய்வீர்கள்?" (interview question)
# Sources (Haas Automation, Mill Operator's Manual, online edition, haascnc.com/service/online-operator-s-manuals/
#   mill-operator-s-manual; read via web.archive.org 2025 copy, haascnc.com blocked from this session):
#   Control Pendant > Mode keys: "[SINGLE BLOCK] Toggles single block on or off. When single block is on, the control runs only
#     one program block each time you press CYCLE START." "[GRAPHICS] Opens Graphics mode."
#   Control Pendant > Override keys: "you can slow down rapids while you prove out a program"; "[5% RAPID]/[25% RAPID]/[50% RAPID]/
#     [100% RAPID] Limits machine rapids to the value on the key." "FEED HOLD Stops all axis motion during a program. The spindle
#     continues to run."
#   Control Display > Position display: "DIST TO GO This tab displays the distance remaining before the axes reach their commanded
#     position."
#   Operation > 11.6 Graphics Mode: "A safe way to troubleshoot a program is to press GRAPHICS ... No movement occurs on the machine,
#     instead the movement is illustrated on the screen."
#   Operation > 11.4 Safe Run: "It does not prevent crashes"; "only active during rapid motions"; "intended for running a program for
#     the first time after writing or changing it."
#   Worked numbers are arithmetic on the schematic: tool tip 20 mm above the part top, block moves 25 mm -> ends 5 mm inside.
#   First-part check: measure the first part to the drawing before continuing (shop procedure decides who signs it off).
Z0 = 560   # part top (y), 8 px per mm
TIP = Z0 - 160   # tool tip 20 mm above the part
H39 = dict(hook="To-go 25, gap 20?", hsize=88, hook2="5 mm part-க்குள் போகும்!", h2size=56, s=0, e=4.2, svg=f'''
<text class="fig" x="24" y="44">SIDE VIEW · SCHEMATIC · mm</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">HAAS MILL EXAMPLE</text>
<rect x="30" y="70" width="718" height="78" rx="10" fill="#0A2236" stroke="#2E5878" stroke-width="2"/>
<text class="code" x="52" y="122" style="font-size:34px"><tspan fill="{DIM}">N50 </tspan>G00 Z-5.<tspan fill="{OR}">   RAPID 5%</tspan></text>
<rect x="60" y="{Z0}" width="330" height="120" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<text x="225" y="{Z0 + 70}" text-anchor="middle" style="font:600 24px Inter" fill="#fff">PART · Z0 = TOP</text>
<rect x="200" y="{TIP + 40}" width="60" height="160" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="10 8"/>
<text x="188" y="{Z0 + 34}" text-anchor="end" style="font:800 26px Inter" fill="#FFD2C9">END: −5</text>
<path d="M330 {TIP}V{Z0}" stroke="{GRN}" stroke-width="3" marker-start="url(#aw)" marker-end="url(#aw)"/>
<text x="342" y="{TIP + 88}" style="font:800 30px Inter" fill="{GRN}">20</text>
<g class="move" data-t="0" data-d="1.5" data-dy="80">
<rect x="180" y="{TIP - 230}" width="100" height="70" rx="6" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<rect x="200" y="{TIP - 160}" width="60" height="160" fill="{OR}" stroke="#fff" stroke-width="3"/>
<path d="M200 {TIP - 120}l60 30M200 {TIP - 70}l60 30M200 {TIP - 20}l60 20" stroke="{PANEL}" stroke-width="4"/></g>
{box(430, 180, 318, 150, OR, 3, "#0A2236")}
<text x="589" y="222" text-anchor="middle" style="font:600 22px Plex" fill="#BFD6E8">DIST TO GO · N50 START</text>
<text x="589" y="300" text-anchor="middle" style="font:800 52px Inter" fill="{OR}">Z -25.000</text>
{box(430, 360, 318, 150, GRN, 3, "#0A2236")}
<text x="589" y="408" text-anchor="middle" style="font:600 24px Plex" fill="#BFD6E8">GAP TO PART</text>
<text x="589" y="480" text-anchor="middle" style="font:800 52px Inter" fill="{GRN}">20 mm</text>
<g class="a" data-t="1.5">{box(430, 540, 318, 100, RED, 4, "#3A1A1A")}
<text x="589" y="604" text-anchor="middle" style="font:800 40px Inter" fill="{RED}">FEED HOLD</text></g>
<text class="a" data-t="1.9" x="389" y="728" text-anchor="middle" style="font:800 40px Inter" fill="{RED}">25 &gt; 20 → STOP</text>''')

R39 = dict(id="39", slug="Proving_Out_New_Program", scenes=[
 H39,
 dict(s=4.2, e=10.2, tag="ANSWER  /  02", title="To-go > gap = STOP", tsize=70, sub="FEED HOLD அழுத்துங்கள்.", ssize=48,
      svg=fig("HAAS MILL EXAMPLE", "SCHEMATIC", orange=True) + f'''
<g class="a" data-t="0.2">{box(40, 66, 698, 120)}
<text x="64" y="112" style="font:800 32px Inter" fill="{OR}">DIST TO GO</text>
<text x="64" y="160" style="font:600 25px Plex" fill="#BFD6E8">DISTANCE LEFT IN THE MOVE</text></g>
<g class="a" data-t="0.7">{box(40, 206, 698, 120)}
<text x="64" y="252" style="font:800 32px Inter" fill="{RED}">FEED HOLD</text>
<text x="64" y="300" style="font:600 25px Plex" fill="#BFD6E8">AXES STOP · SPINDLE KEEPS TURNING</text></g>
<g class="a" data-t="1.3">{box(40, 352, 698, 120, OR, 3)}
<text x="389" y="426" text-anchor="middle" style="font:800 40px Inter" fill="{OR}">25 − 20 = 5 mm INSIDE</text></g>''',
      body="Tool part-ஐ நெருங்கும்போது DIST TO GO-ஐ gap-உடன் ஒப்பிடுங்கள்.", body_t=1.8),
 dict(s=10.2, e=16.6, tag="STEPS  /  03", title="First run: slow", tsize=76, sub="மூன்று key-கள்.", ssize=48,
      svg=fig("HAAS MILL EXAMPLE") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "GRAPHICS", "Machine நகராது; path screen-ல்", 0.2)
          + checkrow(255, 2, "SINGLE BLOCK", "ஒரு CYCLE START = ஒரு block", 0.7)
          + checkrow(395, 3, "RAPID 5% / 25%", "Rapid வேகம் குறையும்", 1.2),
      body="Key பெயர்கள் control-க்கு control மாறும்.", body_t=1.7),
 dict(s=16.6, e=23.0, tag="TRAP  /  04", title="Aids ≠ guarantee", tsize=76, sub="Clearance: நீங்களே பாருங்கள்.", ssize=40,
      svg=fig("WHAT EACH AID DOES", "HAAS MILL EXAMPLE", orange=True) + f'''
<g class="a" data-t="0.2"><text x="40" y="106" style="font:700 28px Inter" fill="#fff">5% RAPID</text>
<text x="330" y="106" style="font:600 25px Plex" fill="#BFD6E8">SLOWER, STILL MOVES</text></g>
<g class="a" data-t="0.6"><text x="40" y="176" style="font:700 28px Inter" fill="#fff">SINGLE BLOCK</text>
<text x="330" y="176" style="font:600 25px Plex" fill="#BFD6E8">STOPS AFTER THE BLOCK</text></g>
<g class="a" data-t="1.0"><text x="40" y="246" style="font:700 28px Inter" fill="#fff">SAFE RUN</text>
<text x="330" y="246" style="font:600 25px Plex" fill="#BFD6E8">"DOES NOT PREVENT</text>
<text x="330" y="282" style="font:600 25px Plex" fill="#BFD6E8"> CRASHES" (HAAS)</text></g>
<path class="a" data-t="1.4" d="M30 320H748" stroke="#2E5878" stroke-width="2"/>
<g class="a" data-t="1.5">{box(40, 344, 698, 130, GRN, 3)}
<text x="389" y="400" text-anchor="middle" style="font:800 36px Inter" fill="{GRN}">FIRST PART → MEASURE</text>
<text x="389" y="446" text-anchor="middle" style="font:600 25px Plex" fill="#BFD6E8">TO THE DRAWING, THEN CONTINUE</text></g>''',
      body="முதல் part-ஐ drawing-படி அளந்த பிறகே அடுத்தது.", body_t=2.0),
 dict(s=23.0, e=28.6, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="To-go 25, gap 20 → HOLD", ssize=46,
      svg=fig("HOW TO ANSWER") + chip(40, 66, 210, "GRAPHICS", 0.1) + chip(268, 66, 250, "SINGLE BLOCK", 0.25)
          + chip(536, 66, 202, "5% RAPID", 0.4) + chip(40, 150, 300, "DIST TO GO", 0.55, OR, OR) + chip(358, 150, 380, "FIRST PART CHECK", 0.7, GRN, GRN) + '''
<text class="w a" data-t="1.0" x="40" y="300" style="font-size:30px">"ஒவ்வொரு step-ஐயும் ஒரு</text>
<text class="w a" data-t="1.0" x="40" y="346" style="font-size:30px"> காரணத்துடன் சொல்லுங்கள்."</text>
<text class="m a" data-t="1.3" x="40" y="440" style="font-size:22px">KEYS DIFFER BY CONTROL. CHECK YOUR MANUAL.</text>''',
      cta=True, cta_t=1.6),
])

# =====================================================================================================
# REEL 40: Running an outdated program – match the program to the released drawing revision. Target 28 s. CTA: SEND.
# Hook format: (2) countdown quiz. Options considered:
#   "Rev C vs Rev B?" (quiz: drawing Rev C, program Rev B: RUN IT / EDIT IT / STOP & ASK; chosen, specific revision letters,
#       ring moves from frame 1, answered in scene 2 and echoed in scene 5)
#   "Size OK, part reject?" (wrong vs right) / "Program rev-ஐ எப்படி check செய்வீர்கள்?" (interview question)
# Sources: ISO/TC 176/SC 2/N1286 "Guidance on the requirements for Documented Information of ISO 9001:2015" (iso.org, read via
#   web.archive.org 2026-10-11 copy): clause 7.5.3 "Control of documented information" applies to documents in any medium, and the
#   documented information an organization maintains includes "Specifications", "Work and/or test instructions", "Production
#   schedules", "Test and inspection plans". Clause title only is shown on screen; no clause text is quoted.
#   Teaching point (no universal rule claimed): the drawing revision is read from the title block; the program used must be the one
#   released for that revision; who confirms it and how revisions are marked in a program (header comment, file name) is set by the
#   shop's document control procedure. Rev letters, O-number, part name and hole sizes are invented example values.
H40 = dict(hook="Rev C vs Rev B?", hsize=100, hook2="என்ன செய்வீர்கள்?", h2size=58, s=0, e=4.0, svg=f'''
<text class="fig" x="24" y="44">QUICK CHECK · EXAMPLE</text>
{box(40, 66, 330, 120, OR, 3)}
<text x="205" y="112" text-anchor="middle" style="font:600 24px Plex" fill="#BFD6E8">DRAWING</text>
<text x="205" y="164" text-anchor="middle" style="font:800 44px Inter" fill="{OR}">REV C</text>
{box(408, 66, 330, 120, RED, 3)}
<text x="573" y="112" text-anchor="middle" style="font:600 24px Plex" fill="#BFD6E8">PROGRAM</text>
<text x="573" y="164" text-anchor="middle" style="font:800 44px Inter" fill="{RED}">REV B</text>
<circle class="until" data-end="3.0" cx="389" cy="330" r="100" fill="none" stroke="#2E5878" stroke-width="16"/>
<circle class="draw" data-t="0" data-d="3.0" data-lin="1" data-hide="1" pathLength="1" cx="389" cy="330" r="100" fill="none" stroke="{OR}" stroke-width="16" transform="rotate(-90 389 330)"/>
<text class="count" data-t="0" data-n="3" x="389" y="366" text-anchor="middle" style="font:800 104px Inter" fill="#fff">3</text>
<g style="font:700 38px Inter" fill="#fff">
<rect x="40" y="480" width="210" height="120" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="145" y="553" text-anchor="middle">RUN IT</text>
<rect x="284" y="480" width="210" height="120" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="389" y="553" text-anchor="middle">EDIT IT</text>
<rect x="528" y="480" width="210" height="120" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="633" y="553" text-anchor="middle" style="font-size:32px">STOP &amp; ASK</text></g>
<text x="389" y="690" text-anchor="middle" style="font:600 30px Inter" fill="#9FC3DD">ANSWER IN THIS REEL</text>''')

R40 = dict(id="40", slug="Outdated_Program_Revision_Check", scenes=[
 H40,
 dict(s=4.0, e=10.0, tag="ANSWER  /  02", title="STOP & ASK", tsize=84, sub="Rev வேறு = run இல்லை.", ssize=46,
      svg=fig("EXAMPLE VALUES") + f'''
<g class="a" data-t="0.2">{box(40, 66, 698, 110)}
<text x="64" y="110" style="font:600 22px Plex" fill="#BFD6E8">TITLE BLOCK</text>
<text x="64" y="152" style="font:700 30px Inter" fill="#fff">PART 101</text>
<text x="714" y="152" text-anchor="end" style="font:800 36px Inter" fill="{OR}">REV C</text></g>
<g class="a" data-t="0.6">{box(40, 196, 698, 110, RED, 3, "#0A2236")}
<text x="64" y="240" style="font:600 22px Plex" fill="#BFD6E8">PROGRAM HEADER</text>
<text class="code" x="64" y="284" style="font-size:30px">O01234 (PART 101 <tspan fill="{RED}">REV B</tspan>)</text></g>
{cross(700, 251, 1.0)}
<g class="a" data-t="1.3">{box(40, 330, 698, 150, OR, 3)}
<text x="389" y="390" text-anchor="middle" style="font:800 32px Inter" fill="{OR}">ASK: WHICH REV IS RELEASED?</text>
<text x="389" y="440" text-anchor="middle" style="font:600 24px Plex" fill="#BFD6E8">SUPERVISOR / PROGRAMMER CONFIRMS</text></g>''',
      body="Program-ஐ நீங்களே மாற்றாதீர்கள்; shop procedure-படி கேளுங்கள்.", body_t=1.8),
 dict(s=10.0, e=16.4, tag="WHY  /  03", title="Old rev = wrong part", tsize=70, sub="Program சரி, rev தவறு.", ssize=48,
      svg=fig("EXAMPLE CHANGE · SCHEMATIC") + f'''
<g class="a" data-t="0.2">{box(40, 66, 330, 300)}
<text x="205" y="110" text-anchor="middle" style="font:700 28px Inter" fill="#fff">REV B</text>
<rect x="95" y="140" width="220" height="150" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<circle cx="205" cy="215" r="32" fill="{PANEL}" stroke="{LINE}" stroke-width="2.5"/>
<text x="205" y="340" text-anchor="middle" style="font:700 30px Inter" fill="#BFD6E8">HOLE Ø8</text></g>
<g class="a" data-t="0.7">{box(408, 66, 330, 300, OR, 3)}
<text x="573" y="110" text-anchor="middle" style="font:700 28px Inter" fill="{OR}">REV C</text>
<rect x="463" y="140" width="220" height="150" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<circle cx="573" cy="215" r="40" fill="{PANEL}" stroke="{OR}" stroke-width="3"/>
<text x="573" y="340" text-anchor="middle" style="font:700 30px Inter" fill="{OR}">HOLE Ø10</text></g>
<text class="a" data-t="1.3" x="389" y="430" text-anchor="middle" style="font:800 34px Inter" fill="{RED}">REV B PROGRAM → Ø8 → REJECT</text>
<text class="m a" data-t="1.6" x="389" y="486" text-anchor="middle" style="font-size:22px">SIZE EXAGGERATED FOR VISIBILITY</text>''',
      body="பழைய rev-படி சரியாக வெட்டினாலும் part reject ஆகலாம்.", body_t=2.0),
 dict(s=16.4, e=22.6, tag="CHECK  /  04", title="Rev check: 3 points", tsize=70, sub="Cycle start-க்கு முன்.", ssize=48,
      svg=fig("BEFORE THE FIRST PART") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "DRAWING REV", "Title block-ல் உள்ள Rev", 0.2)
          + checkrow(255, 2, "PROGRAM REV", "Header / file name (shop முறைப்படி)", 0.7)
          + checkrow(395, 3, "RELEASED?", "Supervisor அல்லது release list", 1.2),
      body="பழைய print machine அருகே இருந்தால் ஒப்படையுங்கள்.", body_t=1.7),
 dict(s=22.6, e=28.2, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="Rev C vs Rev B → STOP", ssize=48,
      svg=fig("HOW TO ANSWER") + f'''
<g class="a" data-t="0.2">{box(40, 66, 210, 110, OR, 3)}<text x="145" y="112" text-anchor="middle" style="font:600 22px Plex" fill="#BFD6E8">DRAWING</text><text x="145" y="156" text-anchor="middle" style="font:800 34px Inter" fill="{OR}">REV C</text></g>
<g class="a" data-t="0.4">{box(284, 66, 210, 110, RED, 3)}<text x="389" y="112" text-anchor="middle" style="font:600 22px Plex" fill="#BFD6E8">PROGRAM</text><text x="389" y="156" text-anchor="middle" style="font:800 34px Inter" fill="{RED}">REV B</text></g>
<g class="a" data-t="0.6">{box(528, 66, 210, 110, GRN, 3)}<text x="633" y="112" text-anchor="middle" style="font:600 22px Plex" fill="#BFD6E8">ACTION</text><text x="633" y="156" text-anchor="middle" style="font:800 30px Inter" fill="{GRN}">STOP &amp; ASK</text></g>
<text class="w a" data-t="0.9" x="40" y="260" style="font-size:30px">"இரண்டு Rev-ம் பொருந்திய</text>
<text class="w a" data-t="0.9" x="40" y="306" style="font-size:30px"> பிறகே cycle start."</text>
<text class="m a" data-t="1.3" x="40" y="400" style="font-size:22px">DOCUMENT CONTROL: ISO 9001:2015 CL. 7.5.3</text>
<text class="m a" data-t="1.3" x="40" y="440" style="font-size:22px">YOUR SHOP PROCEDURE DECIDES WHO APPROVES</text>''',
      cta=True, cta_t=1.6, cta_icon="send", cta_text=SEND),
])

REELS = [R39, R40]
