from gen import *
W = "#E6F0F7"
SEND = "நண்பருக்கு அனுப்புங்கள்."

# ---------------- REEL 15: reading a metric micrometer (0.01 mm) ----------------
# Sources: Mitutoyo Quick Guide p.08 "Micrometers – How to read the scale" (7.37 mm example);
# Bharat Skills (DGT) Mechanical Diesel wk 5: pitch 0.5 mm, 50 thimble divisions, 0.01 mm, 4.55 mm example.
PX = 40  # px per mm on the sleeve

def mic(reading, t=0.0, hl_half=False, hl_thim=True, x0=90):
    edge = x0 + reading * PX
    th = round((reading * 100) % 50)  # thimble divisions past last visible sleeve line
    ticks = []
    for k in range(0, 20):
        mm = k * 0.5
        x = x0 + mm * PX
        if x > edge - 2:
            break
        if k % 2 == 0:
            ticks.append(f'<path d="M{x:.0f} 262V{236 if (k//2)%5 else 228}" stroke="{PANEL}" stroke-width="3"/>')
            if (k // 2) % 5 == 0:
                ticks.append(f'<text x="{x:.0f}" y="222" text-anchor="middle" style="font:700 26px Inter" fill="#fff">{k//2}</text>')
        else:
            last = hl_half and x + 0.5 * PX > edge - 2
            ticks.append(f'<path d="M{x:.0f} 262V{292 if last else 286}" stroke="{OR if last else PANEL}" stroke-width="{6 if last else 3}"/>')
    gr = []
    for v in range(th - 6, th + 7):
        y = 262 + (th - v) * 14
        vv = v % 50
        L = 34 if vv % 5 == 0 else 22
        col = OR if (v == th and hl_thim) else PANEL
        gr.append(f'<path d="M{edge:.0f} {y}h{L}" stroke="{col}" stroke-width="{4 if v == th else 2.5}"/>')
        if vv % 5 == 0:
            gr.append(f'<text x="{edge+44:.0f}" y="{y+9}" style="font:700 24px Inter" fill="{PANEL}">{vv}</text>')
    return f'''<g class="a" data-t="{t}">
<rect x="40" y="230" width="{edge-40+10:.0f}" height="64" fill="#B8CCDB" stroke="{LINE}" stroke-width="2"/>
<path d="M{x0-10} 262H{edge:.0f}" stroke="{PANEL}" stroke-width="3"/>
{''.join(ticks)}
<rect x="{edge:.0f}" y="168" width="{738-edge:.0f}" height="188" rx="6" fill="#9FB7C9" stroke="{LINE}" stroke-width="2"/>
<rect x="{edge+96:.0f}" y="168" width="{738-edge-96:.0f}" height="188" fill="#7E9DB5"/>
{''.join(gr)}
<text class="m" x="60" y="330" style="font-size:22px">SLEEVE</text>
<text class="m" x="{edge+104:.0f}" y="390" style="font-size:22px">THIMBLE</text>
</g>'''

R15 = dict(id="15", slug="Metric_Micrometer_Reading", scenes=[
 dict(s=0, e=5.5, tag="MEASUREMENT  /  01", title="7.37 or 7.87?", tsize=76, sub="Reading என்ன?",
      svg=fig("METRIC MICROMETER · 0.01 mm", "SCHEMATIC") + mic(7.87, 0.0, hl_thim=False)
          + f'<text class="a" data-t="0.8" x="389" y="470" text-anchor="middle" style="font:700 36px Inter" fill="{OR}">7.37 mm ?  7.87 mm ?</text>',
      body="Micrometer reading-ல் ஒரு சிறிய கோடு 0.5 mm வித்தியாசம் தரும்."),
 dict(s=5.5, e=12, tag="SCALE  /  02", title="Two scales", sub="Sleeve + thimble.",
      svg=fig("0.01 mm MICROMETER", "SCHEMATIC") + mic(7.37, 0.0, hl_thim=False) + f'''
<text class="w a" data-t="0.6" x="40" y="80" style="font-size:26px">SLEEVE: 1 mm lines (upper)</text>
<text class="w a" data-t="1.0" x="40" y="118" style="font-size:26px">+ 0.5 mm lines (lower)</text>
<text class="mo a" data-t="1.6" x="40" y="440" style="font-size:24px">THIMBLE: 50 DIVISIONS = 0.5 mm TURN</text>
<text class="mo a" data-t="2.0" x="40" y="478" style="font-size:24px">1 DIVISION = 0.5 ÷ 50 = 0.01 mm</text>''',
      body="Thimble ஒரு சுற்று = 0.5 mm. அதில் 50 பிரிவு; ஒரு பிரிவு = 0.01 mm."),
 dict(s=12, e=18.5, tag="WORKED  /  03", title="Worked example", tsize=72, sub="7.00 + 0.37 = 7.37 mm", ssize=46,
      svg=fig("EXAMPLE READING", "SOURCE: MITUTOYO", orange=True) + mic(7.37, 0.0) + f'''
<text class="w a" data-t="0.6" x="40" y="80" style="font-size:28px">1  SLEEVE        7.00 mm</text>
<text class="w a" data-t="1.1" x="40" y="120" style="font-size:28px">2  HALF LINE?    NO</text>
<text class="mo a" data-t="1.6" x="40" y="440" style="font-size:28px">3  THIMBLE      + 0.37 mm</text>
<text class="a" data-t="2.2" x="40" y="490" style="font:700 32px Inter" fill="#fff">= 7.37 mm</text>''',
      body="Sleeve-ல் தெரியும் கடைசி mm கோடு, பிறகு thimble line-ஐக் கூட்டுங்கள்."),
 dict(s=18.5, e=25, tag="ERROR CHECK  /  04", title="Half line?", sub="0.5 mm-ஐ மறக்காதீர்கள்.", ssize=46,
      svg=fig("SAME THIMBLE, HALF LINE VISIBLE", "SCHEMATIC") + mic(7.87, 0.0, hl_half=True) + f'''
<text class="w a" data-t="0.6" x="40" y="92" style="font-size:28px">7.00 + 0.50 + 0.37</text>
<text class="a" data-t="1.0" x="40" y="136" style="font:700 32px Inter" fill="{GRN}">= 7.87 mm</text>
<text class="a" data-t="1.6" x="40" y="440" style="font:600 26px Inter" fill="{RED}">7.37 = HALF LINE MISSED</text>
<text class="m a" data-t="2.2" x="40" y="482" style="font-size:22px">SCALE LAYOUT CAN VARY BY MODEL</text>''',
      body="Thimble edge-க்கு முன் 0.5 mm கோடு தெரிந்தால், 0.50 சேர்க்க வேண்டும்."),
 dict(s=25, e=31.5, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="நான்கு படிகள்.",
      svg=fig("READING ORDER") + '<path d="M30 140H748M30 250H748M30 360H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(88, 1, "WHOLE mm", "Sleeve-ன் கடைசி mm கோடு", 0.3)
          + checkrow(198, 2, "HALF LINE", "தெரிந்தால் + 0.50", 0.8)
          + checkrow(308, 3, "THIMBLE", "Datum line-ல் உள்ள பிரிவு × 0.01", 1.3)
          + checkrow(418, 4, "ADD", "மூன்றையும் கூட்டுங்கள்", 1.8),
      body="முதலில் zero check, ratchet அல்லது friction thimble.", body_t=2.0, cta=True, cta_t=2.5),
])

# ---------------- REEL 16: thermal drift, morning vs afternoon ----------------
# Sources: Okuma "Thermo-Friendly Concept helps CNC machines take the heat" (ambient, machine heat,
# machining heat; variation over long runs; warm-up); Mitutoyo Temperature effects handout
# (most steels 10.5 ±1.5 ×10^-6/°C, change measured from 20 °C, thermal soak); ISO 1 via NIST (20 °C reference).

def clockpart(cx, label, time, ok, t):
    mark = tick(cx + 130, 96, t + 0.5) if ok else f'<g class="a" data-t="{t+0.5}"><circle cx="{cx+130}" cy="96" r="20" fill="{OR}"/><text x="{cx+130}" y="107" text-anchor="middle" style="font:700 30px Inter" fill="{PANEL}">?</text></g>'
    return f'''<g class="a" data-t="{t}"><text x="{cx}" y="110" text-anchor="middle" style="font:700 40px Inter" fill="#fff">{time}</text>
<text class="m" x="{cx}" y="150" text-anchor="middle" style="font-size:22px">{label}</text>
<rect x="{cx-110}" y="200" width="220" height="150" rx="8" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/>
<circle cx="{cx}" cy="275" r="40" fill="{PANEL}" stroke="{LINE}" stroke-width="2"/>
<path d="M{cx-110} 395H{cx+110}" stroke="{LINE}" stroke-width="2" marker-start="url(#aw)" marker-end="url(#aw)"/></g>{mark}'''

R16 = dict(id="16", slug="Thermal_Drift_Morning_vs_Afternoon", scenes=[
 dict(s=0, e=5.5, tag="ACCURACY  /  01", title="Size drift?", sub="காலை OK, மதியம்?",
      svg=fig("SAME PROGRAM · SAME TOOL", "SCHEMATIC") + clockpart(200, "FIRST PART", "08:00", True, 0.0)
          + clockpart(578, "AFTER A LONG RUN", "15:00", False, 0.6)
          + f'<text class="a" data-t="1.4" x="389" y="470" text-anchor="middle" style="font:700 32px Inter" fill="{OR}">WHY DID THE SIZE CHANGE?</text>',
      body="ஒரே program, ஒரே tool. ஆனால் மதியம் size மாறுகிறது. ஏன்?"),
 dict(s=5.5, e=12, tag="CAUSE  /  02", title="Heat", sub="மூன்று வெப்ப மூலங்கள்.",
      svg=fig("THERMAL DISPLACEMENT", "SOURCE: OKUMA", orange=True) + "".join(
          f'''<g class="a" data-t="{0.3+k*0.5:.1f}"><rect x="30" y="{75+k*110}" width="718" height="92" rx="12" fill="#123A57" stroke="{OR if k==0 else LINE}" stroke-width="2.5"/>
<text x="56" y="{116+k*110}" style="font:700 32px Inter" fill="#fff">{a}</text><text class="ta" x="56" y="{152+k*110}" style="font-size:26px">{esc(b)}</text></g>'''
          for k, (a, b) in enumerate([("MACHINE HEAT", "spindle, motors, hydraulics, coolant"), ("CUTTING HEAT", "வெட்டும்போது part, chips சூடாகும்"), ("AMBIENT", "காலை, மதியம் shop வெப்பநிலை")]))
          + '<text class="m a" data-t="2.0" x="30" y="490" style="font-size:22px">MACHINE AND PART BOTH GROW WITH HEAT</text>',
      body="வெப்பத்தால் machine-ம் part-ம் சிறிது விரிவடையும்; அதனால் size மாறலாம்."),
 dict(s=12, e=18.5, tag="WORKED  /  03", title="Part heat", sub="100 mm steel, +10 °C", ssize=46,
      svg=fig("ILLUSTRATIVE", "MITUTOYO · ISO 1", orange=True) + f'''
<text class="code a" data-t="0.3" x="40" y="100" style="font-size:28px"><tspan fill="{W}">ΔL = L × α × ΔT</tspan></text>
<text class="m a" data-t="0.7" x="40" y="145" style="font-size:22px">α ≈ 10.5 × 10⁻⁶ /°C (MOST STEELS)</text>
<text class="code a" data-t="1.1" x="40" y="205" style="font-size:28px"><tspan fill="{W}">= 100 × 0.0000105 × 10</tspan></text>
<text class="a" data-t="1.6" x="40" y="262" style="font:700 36px Inter" fill="{OR}">≈ 0.01 mm (≈ 10 µm)</text>
<g class="a" data-t="2.0"><rect x="40" y="320" width="300" height="90" rx="6" fill="{STEEL}" stroke="{LINE}" stroke-width="2"/>
<text x="190" y="377" text-anchor="middle" style="font:700 30px Inter" fill="#fff">20 °C</text>
<rect x="420" y="320" width="318" height="90" rx="6" fill="{OR}" stroke="{LINE}" stroke-width="2"/>
<text x="579" y="377" text-anchor="middle" style="font:700 30px Inter" fill="{PANEL}">30 °C</text></g>
<text class="m a" data-t="2.4" x="40" y="470" style="font-size:22px">REFERENCE TEMPERATURE FOR SIZE: 20 °C (ISO 1)</text>''',
      body="சூடான part-ஐ உடனே அளந்தால், அது பெரிதாகத் தெரியலாம்."),
 dict(s=18.5, e=25, tag="CHECK  /  04", title="What to do", tsize=74, sub="மூன்று பழக்கங்கள்.",
      svg=fig("ON THE SHOP FLOOR") + '<path d="M30 190H748M30 330H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(115, 1, "WARM-UP", "Machine-ன் warm-up procedure", 0.3)
          + checkrow(255, 2, "SAME TEMP", "Part, gauge ஒரே வெப்பநிலையில்", 0.8)
          + checkrow(395, 3, "TREND", "Size-ஐ இடைவெளியில் பதிவு செய்யுங்கள்", 1.3),
      body="Offset மாற்றம் shop procedure-படி மட்டுமே; compensation machine-க்கு மாறும்.", body_t=1.8),
 dict(s=25, e=31.5, tag="REMEMBER  /  05", title="Interview answer", tsize=72, sub="Heat → size drift.",
      svg=fig("HOW TO ANSWER") + f'''
<text class="w a" data-t="0.3" x="40" y="110">"Drift வந்தால் முதலில்</text>
<text class="w a" data-t="0.6" x="40" y="160">வெப்பத்தைச் சோதிப்பேன்."</text>
<g class="a" data-t="1.1"><rect x="40" y="220" width="210" height="90" rx="12" fill="#123A57" stroke="{OR}" stroke-width="2.5"/><text x="145" y="277" text-anchor="middle" style="font:700 28px Inter" fill="#fff">WARM-UP</text></g>
<g class="a" data-t="1.4"><rect x="284" y="220" width="210" height="90" rx="12" fill="#123A57" stroke="{OR}" stroke-width="2.5"/><text x="389" y="277" text-anchor="middle" style="font:700 28px Inter" fill="#fff">SAME TEMP</text></g>
<g class="a" data-t="1.7"><rect x="528" y="220" width="210" height="90" rx="12" fill="#123A57" stroke="{OR}" stroke-width="2.5"/><text x="633" y="277" text-anchor="middle" style="font:700 28px Inter" fill="#fff">TREND</text></g>
<text class="m a" data-t="2.0" x="40" y="400" style="font-size:22px">TOOL WEAR CAN ALSO CHANGE SIZE.</text>
<text class="m a" data-t="2.0" x="40" y="436" style="font-size:22px">FIND THE CAUSE BEFORE CHANGING OFFSETS.</text>''',
      body="நீங்கள் உண்மையில் பார்த்த drift-ஐ உதாரணமாகச் சொல்லுங்கள்.", body_t=1.8, cta=True, cta_t=2.5),
])

REELS = [R15, R16]
