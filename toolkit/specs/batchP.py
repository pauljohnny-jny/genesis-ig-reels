from gen import *


def box(x, y, w, h, stroke=LINE, sw=2, fill="#123A57", rx=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def chip(x, y, w, lab, t, col="#fff", stroke=LINE):
    return (f'<g class="a" data-t="{t:.2f}">{box(x, y, w, 64, stroke, 3 if stroke != LINE else 2)}'
            f'<text x="{x + w/2:.0f}" y="{y + 43}" text-anchor="middle" style="font:700 26px Inter" fill="{col}">{esc(lab)}</text></g>')


# ISO 513:2012 identification colours (schematic screen tints)
C_P = "#3D8BEA"; C_M = "#F2C94C"; C_K = RED; C_N = GRN; C_S = "#A0703F"; C_H = "#9AA5B1"


def grp_row(y, letter, col, name, eg, t, ink=PANEL):
    return (f'<g class="a" data-t="{t:.2f}">{box(40, y, 698, 62)}'
            f'<rect x="40" y="{y}" width="86" height="62" rx="12" fill="{col}"/>'
            f'<text x="83" y="{y + 45}" text-anchor="middle" style="font:800 38px Inter" fill="{ink}">{letter}</text>'
            f'<text x="148" y="{y + 41}" style="font:700 26px Inter" fill="#fff">{esc(name)}</text>'
            f'<text x="714" y="{y + 40}" text-anchor="end" style="font:600 20px Plex" fill="#BFD6E8">{esc(eg)}</text></g>')


# =====================================================================================================
# REEL 47: ISO material groups P M K N S H and their colour codes. Target ~28 s. CTA: SAVE.
# Hook format: (2) countdown quiz. Options considered:
#   "K = எந்த material?" (quiz: STEEL / CAST IRON / STAINLESS, 3-2-1 from frame 1; chosen: specific code letter, answered in
#       scene 2 and echoed in scene 5)
#   "Stainless = P? தவறு!" (wrong vs right) / "P M K N S H என்ன?" (interview question)
# Sources (read 23 Nov 2026):
#   ISO 513:2012 "Classification and application of hard cutting materials for metal removal with defined cutting edges –
#   Designation of the main groups and groups of application", Table 5 (standards.iteh.ai sample,
#   cdn.standards.iteh.ai/samples/59932/.../ISO-513-2012.pdf): identification letter / colour / materials –
#   P blue: all kinds of steel and cast steel except stainless steel with an austenitic structure;
#   M yellow: stainless austenitic and austenitic/ferritic steel and cast steel;
#   K red: grey cast iron, cast iron with spheroidal graphite, malleable cast iron;
#   N green: aluminium and other non-ferrous metals, non-metallic materials;
#   S brown: heat-resistant special alloys based on iron, nickel and cobalt, titanium and titanium alloys;
#   H grey: hardened steel, hardened cast iron materials, chilled cast iron.
#   Footnotes: a "Increasing speed, increasing wear resistance of cutting material"; b "Increasing feed, increasing toughness of
#   cutting material" (Table 6: wear resistance ← 01 … 50 → toughness).
#   Maker difference: Dormer Pramet "Workpiece material groups" page (dormerpramet.com/se/en/WMG): "Orange: High-temperature
#   alloys (S-group)" – so the reel tells viewers to trust the letter, not only the colour.
# REV 2 (24 Nov 2026, after ChatGPT CHANGES REQUIRED on rev 4a218da3): re-read ISO 513:2012 Table 5 on 24 Nov – application
#   ranges P01–P50, M01–M40, K01–K40, N01–N30, S01–S30, H01–H30; arrows a (speed / wear resistance) and b (feed / toughness)
#   within each group. Hook label "GRADE AREA" -> "ISO APPLICATION RANGE"; WHY card now a K-only K01–K40 scale with K10 vs K30,
#   scoped "within one group" and "same code ≠ same maker grade".
#   On-screen colours are schematic tints; group names shortened (full scope in caption).
H47 = dict(hook="K = எந்த material?", hsize=82, hook2="3…2…1 · ISO 513 code", h2size=50, s=0, e=4.2, svg=f'''
<text class="fig" x="24" y="44">INSERT BOX LABEL · EXAMPLE</text><text class="fig" x="754" y="44" text-anchor="end" style="fill:{OR}">ISO 513</text>
<g class="move" data-t="0" data-d="1.2" data-dx="0" data-dy="-12">{box(214, 70, 350, 120, OR, 3)}
<text x="389" y="122" text-anchor="middle" style="font:600 24px Plex" fill="#BFD6E8">ISO APPLICATION RANGE</text>
<text x="389" y="172" text-anchor="middle" style="font:800 50px Inter" fill="{OR}">K10 – K20</text></g>
<circle class="until" data-end="3.0" cx="389" cy="330" r="96" fill="none" stroke="#2E5878" stroke-width="16"/>
<circle class="draw" data-t="0" data-d="3.0" data-lin="1" data-hide="1" pathLength="1" cx="389" cy="330" r="96" fill="none" stroke="{OR}" stroke-width="16" transform="rotate(-90 389 330)"/>
<text class="count" data-t="0" data-n="3" x="389" y="366" text-anchor="middle" style="font:800 104px Inter" fill="#fff">3</text>
<g style="font:700 34px Inter" fill="#fff">
<rect x="40" y="480" width="210" height="120" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="145" y="553" text-anchor="middle">STEEL</text>
<rect x="284" y="480" width="210" height="120" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="389" y="553" text-anchor="middle">CAST IRON</text>
<rect x="528" y="480" width="210" height="120" rx="18" fill="#123A57" stroke="{LINE}" stroke-width="3"/><text x="633" y="553" text-anchor="middle">STAINLESS</text></g>
<text x="389" y="690" text-anchor="middle" style="font:600 30px Inter" fill="#9FC3DD">ANSWER IN THIS REEL</text>''')

R47 = dict(id="47", slug="ISO_Material_Groups_PMKNSH", scenes=[
 H47,
 dict(s=4.2, e=11.2, tag="ANSWER  /  02", title="K = Cast iron", tsize=80, sub="ISO 513: K-ன் colour red.", ssize=46,
      svg=fig("ISO 513 · TABLE 5", "LETTER + COLOUR", orange=True)
          + grp_row(64, "P", C_P, "STEEL", "NOT AUSTENITIC SS", 0.2)
          + grp_row(136, "M", C_M, "STAINLESS STEEL", "AUSTENITIC", 0.4)
          + grp_row(208, "K", C_K, "CAST IRON", "GREY · SG · MALLEABLE", 0.6, "#fff")
          + grp_row(280, "N", C_N, "NON-FERROUS", "ALUMINIUM", 0.8)
          + grp_row(352, "S", C_S, "SUPERALLOYS · TITANIUM", "Ni · Co · Fe BASED", 1.0, "#fff")
          + grp_row(424, "H", C_H, "HARDENED MATERIALS", "HARDENED STEEL", 1.2)
          + f'<rect class="a" data-t="1.6" x="36" y="204" width="706" height="70" rx="14" fill="none" stroke="{OR}" stroke-width="4"/>',
      body="Letter = வெட்டப்படும் workpiece material.", body_t=1.8),
 dict(s=11.2, e=17.0, tag="WHY  /  03", title="The number", tsize=80, sub="K10 vs K30: என்ன வித்தியாசம்?", ssize=40,
      svg=fig("ISO 513 · K APPLICATION RANGE", "SCHEMATIC", orange=True) + f'''
<g class="a" data-t="0.2">{box(40, 70, 698, 70)}
<text x="66" y="117" style="font:800 30px Inter" fill="#fff">K01</text>
<text x="389" y="117" text-anchor="middle" style="font:700 24px Inter" fill="#BFD6E8">CAST IRON GROUP</text>
<text x="712" y="117" text-anchor="end" style="font:800 30px Inter" fill="#fff">K40</text></g>
<g class="a" data-t="0.4"><rect x="40" y="160" width="698" height="26" rx="13" fill="#2E5878"/>
<rect class="grow" data-t="0.4" data-d="1.2" data-w="698" x="40" y="160" width="0" height="26" rx="13" fill="{OR}"/>
<path d="M201 150V196M559 150V196" stroke="#fff" stroke-width="4"/></g>
<g class="a" data-t="0.9">{box(40, 214, 336, 200, GRN, 3)}
<text x="208" y="262" text-anchor="middle" style="font:800 34px Inter" fill="{GRN}">K10</text>
<text x="208" y="312" text-anchor="middle" style="font:700 25px Inter" fill="#fff">MORE WEAR</text>
<text x="208" y="346" text-anchor="middle" style="font:700 25px Inter" fill="#fff">RESISTANCE</text>
<text x="208" y="392" text-anchor="middle" style="font:600 22px Plex" fill="#BFD6E8">HIGHER SPEED</text></g>
<g class="a" data-t="1.3">{box(402, 214, 336, 200, OR, 3)}
<text x="570" y="262" text-anchor="middle" style="font:800 34px Inter" fill="{OR}">K30</text>
<text x="570" y="312" text-anchor="middle" style="font:700 25px Inter" fill="#fff">MORE</text>
<text x="570" y="346" text-anchor="middle" style="font:700 25px Inter" fill="#fff">TOUGHNESS</text>
<text x="570" y="392" text-anchor="middle" style="font:600 22px Plex" fill="#BFD6E8">HIGHER FEED</text></g>
<text class="m a" data-t="1.6" x="389" y="450" text-anchor="middle" style="font-size:20px">WITHIN ONE GROUP · ISO 513 TABLES 5–6</text>
<text class="m a" data-t="1.6" x="389" y="482" text-anchor="middle" style="font-size:20px">SAME CODE ≠ SAME MAKER GRADE</text>''',
      body="ஒரே group-க்குள்: சிறிய எண் wear, பெரிய எண் toughness.", body_t=1.8),
 dict(s=17.0, e=22.8, tag="CHECK  /  04", title="Read the box", tsize=80, sub="மூன்று check.", ssize=50,
      svg=fig("INSERT BOX") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "LETTER = MATERIAL", "Job material-உடன் ஒப்பிடுங்கள்", 0.2)
          + checkrow(255, 2, "NUMBER = APPLICATION", "ஒரே group-க்குள் மட்டும் ஒப்பிடுங்கள்", 0.7)
          + checkrow(395, 3, "TRUST THE LETTER", "S colour: ISO brown, சில maker orange", 1.2),
      body="Grade தேர்வு tool maker catalogue-படி.", body_t=1.7),
 dict(s=22.8, e=28.2, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="K = cast iron · red.", ssize=48,
      svg=fig("HOW TO ANSWER") + chip(40, 66, 214, "P STEEL", 0.1, C_P, C_P) + chip(282, 66, 214, "M STAINLESS", 0.2, C_M, C_M)
          + chip(524, 66, 214, "K CAST IRON", 0.3, "#fff", C_K)
          + chip(40, 146, 214, "N NON-FE", 0.4, C_N, C_N) + chip(282, 146, 214, "S Ni / Ti", 0.5, "#D9A877", C_S)
          + chip(524, 146, 214, "H HARDENED", 0.6, C_H, C_H) + '''
<text class="w a" data-t="0.9" x="40" y="300" style="font-size:30px">"K என்பது cast iron group;</text>
<text class="w a" data-t="0.9" x="40" y="346" style="font-size:30px"> ISO 513 colour red."</text>
<text class="m a" data-t="1.2" x="40" y="440" style="font-size:22px">ISO 513:2012 · COLOURS SCHEMATIC</text>''',
      cta=True, cta_t=1.6),
])

REELS = [R47]
