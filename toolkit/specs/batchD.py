from gen import *

def lcd(x, y, w, h, txt, size=50, col="#DDF2D8", t=0.0):
    return f'''<g class="a" data-t="{t}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#0A1F14" stroke="{LINE}" stroke-width="2"/>
<text x="{x+w-16}" y="{y+h/2+size*0.36:.0f}" text-anchor="end" style="font:600 {size}px Inter" fill="{col}">{esc(txt)}</text></g>'''

def caliper(display="20.00", part=True, t=0.0):
    ticks = "".join(f'<path d="M{x} 232V{246 if i%5 else 252}" stroke="{PANEL}" stroke-width="2"/>' for i, x in enumerate(range(130, 730, 15)))
    pt = f'<rect x="110" y="320" width="190" height="100" fill="{STEEL}" stroke="{LINE}" stroke-width="2.5"/><text class="m" x="205" y="378" text-anchor="middle" style="fill:#fff;font-size:22px">PART</text>' if part else ""
    return f'''<g class="a" data-t="{t}">
<rect x="40" y="230" width="698" height="40" rx="4" fill="#9FB7C9" stroke="{LINE}" stroke-width="2"/>{ticks}
<path d="M40 230H110V440H70L40 300Z" fill="#B8CCDB" stroke="{LINE}" stroke-width="2"/>
<rect x="300" y="180" width="240" height="130" rx="10" fill="#6C93B4" stroke="{LINE}" stroke-width="2.5"/>
<path d="M300 310H350V440H316L300 330Z" fill="#B8CCDB" stroke="{LINE}" stroke-width="2"/>
{pt}</g>{lcd(318, 196, 204, 70, display, 46, t=t)}'''

R12 = dict(id="12", slug="Caliper_Resolution_vs_Accuracy", scenes=[
 dict(s=0, e=5, tag="MEASUREMENT  /  01", title="0.01 = ±0.01?", sub="Resolution = accuracy-ஆ?",
      svg=fig("DIGITAL CALIPER", "SCHEMATIC") + caliper("20.00") + f'''
<text class="a" data-t="0.8" x="600" y="160" text-anchor="middle" style="font:700 48px Inter" fill="{OR}">±0.01 ?</text>''',
      body="Display-ல் 0.01 mm படி இருக்கிறது. அப்படியென்றால் accuracy-யும் ±0.01 mm-ஆ?"),
 dict(s=5, e=11, tag="RESOLUTION  /  02", title="Resolution", sub="Display-ன் சிறிய படி.",
      svg=fig("DISPLAY", "EXAMPLE") + lcd(40, 100, 290, 100, "20.00", 60, t=0.3) + lcd(448, 100, 290, 100, "20.01", 60, col=OR, t=1.0) + f'''
<path class="a" data-t="0.8" d="M350 150H428" stroke="#fff" stroke-width="4" marker-end="url(#aw)"/>
<text class="w a" data-t="1.5" x="389" y="275" text-anchor="middle">1 display step = 0.01 mm</text>
<text class="mo a" data-t="2.2" x="389" y="355" text-anchor="middle">RESOLUTION = DISPLAY STEP</text>
<text class="m a" data-t="2.8" x="389" y="420" text-anchor="middle" style="fill:{RED}">NOT PROOF OF THE TRUE SIZE</text>''',
      body="20.00-லிருந்து 20.01 என மாறுவது display படி மட்டுமே; உண்மையான அளவின் துல்லியத்தை அது சொல்லாது."),
 dict(s=11, e=18, tag="ACCURACY  /  03", title="Accuracy", sub="மூன்றைப் பொறுத்தது.",
      svg=fig("WHAT ACCURACY DEPENDS ON", "SOURCE: MITUTOYO") + "".join(
          f'''<g class="a" data-t="{0.3+k*0.5:.1f}"><rect x="30" y="{75+k*110}" width="718" height="92" rx="12" fill="#123A57" stroke="{OR if k==0 else LINE}" stroke-width="2.5"/>
<text x="56" y="{116+k*110}" style="font:700 32px Inter" fill="#fff">{a}</text><text class="ta" x="56" y="{152+k*110}" style="font-size:26px">{esc(b)}</text></g>'''
          for k, (a, b) in enumerate([("MODEL SPECIFICATION", "உங்கள் caliper model-ன் spec"), ("CALIBRATION STATUS", "calibration பதிவு, காலாவதி தேதி"), ("MEASUREMENT METHOD", "நீங்கள் பயன்படுத்தும் முறை")]))
          + '<text class="m a" data-t="2.0" x="30" y="490" style="font-size:22px">"NO RELATIONSHIP BETWEEN RESOLUTION AND ACCURACY"</text>',
      body="Accuracy-க்குப் பொதுவான ± மதிப்பு இல்லை; model spec, calibration, முறை மூன்றையும் பாருங்கள்."),
 dict(s=18, e=25, tag="METHOD  /  04", title="Good practice", sub="இந்த நான்கும் முக்கியம்.",
      svg=fig("BEFORE YOU MEASURE") + '<path d="M30 140H748M30 250H748M30 360H748" stroke="#2E5878" stroke-width="2"/>'
          + checkrow(88, 1, "CLEAN FACES", "Measuring faces-ஐத் துடையுங்கள்", 0.3)
          + checkrow(198, 2, "ZERO CHECK", "Jaws மூடியதும் 0.00 காட்டுகிறதா?", 0.8)
          + checkrow(308, 3, "ALIGNMENT", "Jaws part-க்குச் சரியாக நேராக", 1.3)
          + checkrow(418, 4, "EVEN FORCE", "ஒரே மாதிரியான அழுத்தம்", 1.8),
      body="Zero check முழு calibration அல்ல; அது ஒரு அடிப்படைச் சோதனை மட்டுமே.", body_t=2.3),
 dict(s=25, e=31, tag="TAKEAWAY  /  05", title="Digits ≠ accuracy", tsize=74, sub="இலக்கங்கள் மட்டும் போதாது.", ssize=42,
      svg=fig("SUMMARY") + lcd(40, 90, 300, 100, "20.01", 60, t=0.2) + f'''
<text class="a" data-t="0.6" x="389" y="160" text-anchor="middle" style="font:700 64px Inter" fill="{RED}">≠</text>
<g class="a" data-t="0.9"><rect x="440" y="90" width="300" height="100" rx="12" fill="#123A57" stroke="{GRN}" stroke-width="3"/>
<text x="590" y="152" text-anchor="middle" style="font:700 36px Inter" fill="{GRN}">ACCURACY</text></g>
<text class="w a" data-t="1.4" x="389" y="290" text-anchor="middle">Spec · Calibration · Method</text>
<text class="mo a" data-t="1.9" x="389" y="370" text-anchor="middle">MATCH THE INSTRUMENT</text>
<text class="mo a" data-t="1.9" x="389" y="410" text-anchor="middle">TO THE DRAWING TOLERANCE</text>''',
      body="Drawing tolerance-க்கு ஏற்ற instrument-ஐத் தேர்வு செய்யுங்கள்.", body_t=1.8, cta=True, cta_t=2.4),
])

REELS = [R12]
