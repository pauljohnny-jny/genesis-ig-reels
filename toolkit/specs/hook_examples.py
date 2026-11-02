"""Reference hook scenes for reels 17+ (render with: python3 render.py specs/hook_examples.py --stills-only).
Copy a pattern into the real reel spec as scene 1 (s=0, e≈3.5). Not reels for publishing."""
from gen import *

# Pattern 1: cold-open demo (watch the mistake happen). Haas mill example, schematic, 4 px per mm.
G91 = dict(hook="ஒரு G91.", hook2="Tool எங்கே போகும்?", s=0, e=4.2, flash_t=2.4, svg=f'''
<text class="fig" x="24" y="44">TOP VIEW · SCHEMATIC</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">HAAS MILL EXAMPLE</text>
<rect x="30" y="80" width="718" height="84" rx="10" fill="#0A2236" stroke="#2E5878" stroke-width="2"/>
<text class="code a" data-t="0.2" x="52" y="134" style="font-size:38px">G91 G00 X50.</text>
<g class="shake" data-t="2.4">
<path d="M60 560H720" stroke="#7FA6C4" stroke-width="2"/>
<g style="font:500 24px Plex" fill="#9FC3DD"><text x="110" y="600" text-anchor="middle">X0</text><text x="270" y="600" text-anchor="middle">X40</text>
<text x="310" y="640" text-anchor="middle" fill="{GRN}">X50</text><text x="470" y="600" text-anchor="middle" fill="{RED}">X90</text></g>
<rect x="150" y="300" width="300" height="200" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<rect x="470" y="330" width="90" height="140" rx="6" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<text x="515" y="410" text-anchor="middle" style="font:700 22px Inter" fill="#fff">CLAMP</text>
<g class="a" data-t="0.9"><circle cx="310" cy="250" r="34" fill="none" stroke="{GRN}" stroke-width="4" stroke-dasharray="10 8"/>
<text x="310" y="200" text-anchor="middle" style="font:700 24px Inter" fill="{GRN}">G90 → X50</text></g>
<rect class="grow" data-t="1.3" data-d="1.1" data-w="200" x="270" y="247" width="0" height="6" fill="{RED}"/>
<g class="move" data-t="1.3" data-d="1.1" data-dx="200"><circle cx="270" cy="250" r="34" fill="{OR}" stroke="#fff" stroke-width="3"/><circle cx="270" cy="250" r="8" fill="{PANEL}"/></g>
</g>
<text class="a" data-t="2.5" x="389" y="700" text-anchor="middle" style="font:800 46px Inter" fill="{RED}">G91 → X40 + 50 = X90</text>''')

# Pattern 2: countdown quiz (answer later in the reel). 0.01 mm = 10 µm (SI).
QUIZ = dict(hook="0.01 mm = ?", hook2="3 வினாடியில் பதில்?", hook2_t=0.25, s=0, e=4.0, svg=f'''
<text class="fig" x="24" y="44">QUICK CHECK</text>
<circle cx="389" cy="250" r="140" fill="none" stroke="#2E5878" stroke-width="18"/>
<circle class="draw" data-t="0" data-d="3.0" pathLength="1" cx="389" cy="250" r="140" fill="none" stroke="{OR}" stroke-width="18" transform="rotate(-90 389 250)"/>
<text class="a" data-t="0" x="389" y="295" text-anchor="middle" style="font:800 130px Inter" fill="#fff">3</text>
<g style="font:700 50px Inter" fill="#fff">
<rect x="40" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="145" y="553" text-anchor="middle">1 µm</text>
<rect x="284" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="389" y="553" text-anchor="middle">10 µm</text>
<rect x="528" y="470" width="210" height="130" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="633" y="553" text-anchor="middle">100 µm</text></g>
<text x="389" y="690" text-anchor="middle" style="font:600 30px Inter" fill="#9FC3DD">ANSWER IN THIS REEL</text>''')

REELS = [dict(id="H1", slug="Hook_ColdOpen_G91", scenes=[G91]), dict(id="H2", slug="Hook_Countdown_Quiz", scenes=[QUIZ])]
