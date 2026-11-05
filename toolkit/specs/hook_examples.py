"""Reference hook scenes for reels 17+ (render with: python3 render.py specs/hook_examples.py --stills-only).
Copy a pattern into the real reel spec as scene 1 (s=0, e≈3.5–4.5). Not reels for publishing.
Revised 3 Nov 2026 after ChatGPT's pre-production audit: motion from frame 1, the collision is real in the drawing,
a true 3-2-1 countdown on one linear clock, the Tamil follow-up visible at frame 1 in darker orange, and hook QC frames."""
from gen import *

# Pattern 1: cold-open demo (watch the mistake happen). Haas mill example, metric, schematic, top view, 4 px per mm.
# Start X40 (x=270). G90 X50. would stop at X50 (x=310). G91 X50. targets X90 (x=470), and the clamp sits in that path:
# the cutter (r=34) touches the clamp face at x=450, i.e. after 146 px, so the move ends at contact and the flash fires then.
# The reel body must then show the "forgotten G91": a later X50. while G91 is still active moves another +50 mm.
G91 = dict(hook="ஒரு G91.", hook2="Tool எங்கே போகும்?", s=0, e=4.2, flash_t=1.4, svg=f'''
<text class="fig" x="24" y="44">TOP VIEW · SCHEMATIC · mm</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">HAAS MILL EXAMPLE</text>
<rect x="30" y="80" width="718" height="84" rx="10" fill="#0A2236" stroke="#2E5878" stroke-width="2"/>
<text class="code a" data-t="0" x="52" y="134" style="font-size:38px">G91 G00 X50.</text>
<g class="shake" data-t="1.4">
<path d="M60 560H720" stroke="#7FA6C4" stroke-width="2"/>
<g style="font:600 26px Plex" fill="#BFD6E8"><text x="270" y="600" text-anchor="middle">X40</text>
<text x="310" y="640" text-anchor="middle" fill="{GRN}">X50</text><text x="470" y="600" text-anchor="middle" fill="{RED}">X90</text></g>
<path d="M270 560v-14M310 560v-14M470 560v-14" stroke="#7FA6C4" stroke-width="2"/>
<text x="270" y="335" text-anchor="middle" style="font:700 24px Inter" fill="#fff">START X40</text>
<rect x="100" y="380" width="330" height="140" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/><text x="265" y="458" text-anchor="middle" style="font:600 24px Inter" fill="#fff">PART</text>
<rect x="450" y="190" width="100" height="120" rx="6" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<text x="500" y="257" text-anchor="middle" style="font:700 22px Inter" fill="#fff">CLAMP</text>
<path d="M310 250H470" stroke="{RED}" stroke-width="3" stroke-dasharray="10 8"/>
<g><circle cx="310" cy="250" r="34" fill="none" stroke="{GRN}" stroke-width="4" stroke-dasharray="10 8"/>
<text x="310" y="196" text-anchor="middle" style="font:700 24px Inter" fill="{GRN}">G90 → X50</text></g>
<rect class="grow" data-t="0" data-d="1.4" data-w="146" x="270" y="247" width="0" height="6" fill="{OR}"/>
<g class="move" data-t="0" data-d="1.4" data-dx="146"><circle cx="270" cy="250" r="34" fill="{OR}" stroke="#fff" stroke-width="3"/><circle cx="270" cy="250" r="8" fill="{PANEL}"/></g>
</g>
<text class="a" data-t="1.5" x="389" y="690" text-anchor="middle" style="font:800 40px Inter" fill="{RED}">OVERSHOOT: X40 + 50 = X90</text>''')

# Pattern 2: countdown quiz (answer later in the reel). 0.01 mm = 10 µm (1 mm = 1,000 µm, SI).
# Numeral 3-2-1 and the ring run on one linear 3 s clock, then both clear.
QUIZ = dict(hook="0.01 mm = ? µm", hsize=92, hook2="3 வினாடியில் பதில்?", s=0, e=4.0, svg=f'''
<text class="fig" x="24" y="44">QUICK CHECK</text>
<circle class="until" data-end="3.0" cx="389" cy="250" r="140" fill="none" stroke="#2E5878" stroke-width="18"/>
<circle class="draw" data-t="0" data-d="3.0" data-lin="1" data-hide="1" pathLength="1" cx="389" cy="250" r="140" fill="none" stroke="{OR}" stroke-width="18" transform="rotate(-90 389 250)"/>
<text class="count" data-t="0" data-n="3" x="389" y="295" text-anchor="middle" style="font:800 130px Inter" fill="#fff">3</text>
<g style="font:700 50px Inter" fill="#fff">
<rect x="40" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="145" y="553" text-anchor="middle">1 µm</text>
<rect x="284" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="389" y="553" text-anchor="middle">10 µm</text>
<rect x="528" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="633" y="553" text-anchor="middle">100 µm</text></g>
<text x="389" y="690" text-anchor="middle" style="font:600 30px Inter" fill="#9FC3DD">ANSWER IN THIS REEL</text>''')

REELS = [dict(id="H1", slug="Hook_ColdOpen_G91", scenes=[G91]), dict(id="H2", slug="Hook_Countdown_Quiz", scenes=[QUIZ])]
