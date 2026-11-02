"""Genesis reel generator: spec -> self-contained animated HTML (1080x1920), safe-zone layout v3."""
import html as H

OR = "#F5A04A"; LAB = "#9FC3DD"; LINE = "#CFE3F2"; STEEL = "#4D7DA3"; PANEL = "#0F2D44"
RED = "#F06A55"; GRN = "#7FD18B"; WHITE = "#FFFFFF"; SUBT = "#BFD6E8"

CSS = """
@font-face{font-family:NTamil;font-weight:500;src:url(node_modules/@fontsource/noto-sans-tamil/files/noto-sans-tamil-tamil-500-normal.woff2)}
@font-face{font-family:NTamil;font-weight:600;src:url(node_modules/@fontsource/noto-sans-tamil/files/noto-sans-tamil-tamil-600-normal.woff2)}
@font-face{font-family:NTamil;font-weight:700;src:url(node_modules/@fontsource/noto-sans-tamil/files/noto-sans-tamil-tamil-700-normal.woff2)}
@font-face{font-family:NSans;font-weight:500;src:url(node_modules/@fontsource/noto-sans/files/noto-sans-latin-500-normal.woff2)}
@font-face{font-family:NSans;font-weight:600;src:url(node_modules/@fontsource/noto-sans/files/noto-sans-latin-600-normal.woff2)}
@font-face{font-family:NSans;font-weight:700;src:url(node_modules/@fontsource/noto-sans/files/noto-sans-latin-700-normal.woff2)}
@font-face{font-family:Inter;font-weight:600;src:url(node_modules/@fontsource/inter/files/inter-latin-600-normal.woff2)}
@font-face{font-family:Inter;font-weight:700;src:url(node_modules/@fontsource/inter/files/inter-latin-700-normal.woff2)}
@font-face{font-family:Plex;font-weight:400;src:url(node_modules/@fontsource/ibm-plex-mono/files/ibm-plex-mono-latin-400-normal.woff2)}
@font-face{font-family:Plex;font-weight:500;src:url(node_modules/@fontsource/ibm-plex-mono/files/ibm-plex-mono-latin-500-normal.woff2)}
*{box-sizing:border-box}
html,body{margin:0;width:1080px;height:1920px;background:#fff;overflow:hidden}
.logo{position:absolute;left:72px;top:240px;width:200px}
.hdr-r{position:absolute;right:230px;top:262px;font:400 24px Plex;color:#3F5F7A;letter-spacing:2px}
.rule{position:absolute;left:72px;width:778px;height:2px;background:#C9D6E0}
.scene{position:absolute;inset:0}
.tag{position:absolute;left:72px;top:344px;font:500 26px Plex;color:#1D4766;letter-spacing:2px;display:flex;align-items:center;gap:12px;white-space:nowrap}
.tag i{width:15px;height:15px;border-radius:4px;background:#E8770A;display:block}
.title{position:absolute;left:68px;top:380px;font:700 80px/1.05 Inter,NTamil;color:#11324F;letter-spacing:-1.2px;white-space:nowrap}
.sub{position:absolute;left:72px;top:476px;font:700 50px/1.3 NSans,NTamil;color:#11324F;white-space:nowrap}
.panel{position:absolute;left:72px;top:568px;width:778px;height:520px;border-radius:22px;overflow:hidden;
 background:#0F2D44;background-image:linear-gradient(rgba(130,180,220,.09) 2px,transparent 2px),linear-gradient(90deg,rgba(130,180,220,.09) 2px,transparent 2px);background-size:40px 40px;background-position:-1px -1px}
.panel svg{position:absolute;inset:0}
.body{position:absolute;left:72px;top:1114px;width:778px;font:500 42px/1.42 NSans,NTamil;color:#11324F}
.cta{position:absolute;left:72px;top:1262px;max-width:778px;padding:14px 26px 16px 22px;background:#E8F0F7;border-radius:14px;font:700 36px/1.3 NSans,NTamil;color:#11324F;display:flex;align-items:center;gap:16px;white-space:nowrap}
.foot{position:absolute;left:72px;top:1388px;font:400 22px Plex;color:#4E6B83;letter-spacing:2px;white-space:nowrap}
svg text{font-family:Plex}
.m{font:500 26px Plex;fill:#9FC3DD;letter-spacing:1px}
.mo{font:500 26px Plex;fill:#F5A04A;letter-spacing:1px}
.fig{font:400 22px Plex;fill:#7FA6C4;letter-spacing:2px}
.w{font:600 32px Inter,NTamil;fill:#fff}
.wb{font:700 40px Inter,NTamil;fill:#fff}
.ta{font:500 30px NSans,NTamil;fill:#BFD6E8}
.code{font:500 30px Plex;fill:#E6F0F7}
.hk{position:absolute;left:72px;top:346px;max-width:778px;font:800 104px/1.08 Inter,NTamil;color:#11324F;letter-spacing:-2px;white-space:nowrap}
.hk2{position:absolute;left:72px;top:470px;max-width:778px;font:700 62px/1.2 NSans,NTamil;color:#E8770A;white-space:nowrap}
.panel.hpanel{top:580px;height:760px;border-radius:26px}
.hflash{position:absolute;inset:0;background:#F06A55;opacity:0;pointer-events:none}
"""

JS = r"""
const scenes=[...document.querySelectorAll('.scene')];
const cl=x=>Math.max(0,Math.min(1,x)); const ease=x=>1-Math.pow(1-x,3);
window.render=function(t){
 scenes.forEach((s,i)=>{
  const st=+s.dataset.start,en=+s.dataset.end,last=i==scenes.length-1;
  let op=i==0?1:cl((t-st)/0.3); if(!last) op=Math.min(op,cl((en-t)/0.25)); if(t<st||t>en) op=0;
  s.style.opacity=op; s.style.visibility=op>0?'visible':'hidden'; const tl=t-st;
  s.querySelectorAll('.a').forEach(e=>{const a=+e.dataset.t; const p=(i==0&&a<=0)?1:ease(cl((tl-a)/0.4)); e.style.opacity=p;
    if(!(e instanceof SVGElement)) e.style.transform=`translateY(${(1-p)*18}px)`;});
  s.querySelectorAll('.draw').forEach(e=>{const a=+e.dataset.t,d=+(e.dataset.d||0.5); const p=ease(cl((tl-a)/d));
    if(e.hasAttribute('pathLength')){e.style.strokeDasharray='1';e.style.strokeDashoffset=1-p;} e.style.opacity=p>0?(e.hasAttribute('pathLength')?1:p):0;});
  s.querySelectorAll('.pulse').forEach(e=>{const a=+e.dataset.t; if(tl<a){e.style.opacity=0;return;}
    const ph=tl-a; e.style.opacity=cl(ph/0.3)*(0.45+0.55*Math.abs(Math.cos(ph*Math.PI/1.1)));});
  s.querySelectorAll('.move').forEach(e=>{const a=+e.dataset.t,d=+(e.dataset.d||1); const p=ease(cl((tl-a)/d));
    e.setAttribute('transform',`translate(${(+e.dataset.dx||0)*p} ${(+e.dataset.dy||0)*p})`);});
  s.querySelectorAll('.grow').forEach(e=>{const a=+e.dataset.t,d=+(e.dataset.d||1); const p=ease(cl((tl-a)/d));
    e.setAttribute('width',Math.max(0,(+e.dataset.w)*p));});
  s.querySelectorAll('.blink').forEach(e=>{const a=+e.dataset.t; e.style.opacity=tl<a?0:(+(e.dataset.o||0.35))*cl(1-(tl-a)/0.35);});
  s.querySelectorAll('.shake').forEach(e=>{const a=+e.dataset.t; const k=tl-a; const x=(k>=0&&k<0.4)?Math.sin(k*90)*8*(0.4-k)/0.4:0;
    e.setAttribute('transform',`translate(${x} 0)`);});
  s.querySelectorAll('.spin').forEach(e=>{const r=+(e.dataset.r||1); e.setAttribute('transform',`rotate(${(r*tl*120)%360} ${e.dataset.cx} ${e.dataset.cy})`);});
 });
};
window.check=function(){
 const out=[]; const fontsOK=document.fonts.check('500 42px NTamil','அ')&&document.fonts.check('700 80px Inter','A');
 if(!fontsOK) out.push('FONTS NOT LOADED');
 scenes.forEach((s,i)=>{
  render(+s.dataset.end-0.3);
  const pr=s.querySelector('.panel').getBoundingClientRect();
  s.querySelectorAll('.tag,.title,.sub,.hk,.hk2,.body,.cta,.foot').forEach(e=>{const r=e.getBoundingClientRect();
    let w=r.width; if(e.classList.contains('title')||e.classList.contains('sub')||e.classList.contains('hk')||e.classList.contains('hk2')||e.classList.contains('tag')||e.classList.contains('cta')) w=Math.max(r.width,e.scrollWidth);
    const right=r.left+w;
    if(right>852||r.top<228||r.bottom>1442) out.push(`S${i+1} ${e.className.split(' ')[0]} out of safe zone: right ${right|0} top ${r.top|0} bottom ${r.bottom|0}`);});
  const b=s.querySelector('.body'), c=s.querySelector('.cta');
  if(b&&c){const br=b.getBoundingClientRect(),cr=c.getBoundingClientRect(); if(br.bottom>cr.top-6) out.push(`S${i+1} body overlaps CTA (${br.bottom|0}>${cr.top|0})`);}
  if(b){const br=b.getBoundingClientRect(); if(br.bottom>1366) out.push(`S${i+1} body too low ${br.bottom|0}`);}
  s.querySelectorAll('.panel svg text').forEach(e=>{const r=e.getBoundingClientRect();
    if(r.right>pr.right-6||r.left<pr.left+4||r.top<pr.top+4||r.bottom>pr.bottom-4) out.push(`S${i+1} svg text outside panel: "${e.textContent.slice(0,24)}" [${r.left|0},${r.top|0},${r.right|0},${r.bottom|0}]`);});
 });
 render(0); return out;
};
render(0);
"""

DEFS = f"""<defs>
<marker id="aw" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" orient="auto-start-reverse"><path d="M0 1L12 6L0 11z" fill="#fff"/></marker>
<marker id="ao" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" orient="auto-start-reverse"><path d="M0 1L12 6L0 11z" fill="{OR}"/></marker>
<marker id="ar" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" orient="auto-start-reverse"><path d="M0 1L12 6L0 11z" fill="{RED}"/></marker>
</defs>"""


def esc(s):
    return H.escape(s, quote=False)


def fig(left, right="", orange=False):
    r = f'<text class="fig" x="754" y="42" text-anchor="end"{" style=\"fill:%s\"" % OR if orange else ""}>{esc(right)}</text>' if right else ""
    return f'<text class="fig" x="24" y="42">{esc(left)}</text>{r}'


def code(x, y, lines, t0=0.3, dt=0.25, size=30, lh=46, w=None, h=None, label=None):
    """lines: list of list of (text, color) segments."""
    n = len(lines)
    w = w or 700; h = h or (n * lh + 30)
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#0A2236" stroke="#2E5878" stroke-width="2"/>']
    if label:
        out.append(f'<text class="mo" x="{x}" y="{y-14}" style="font-size:22px">{esc(label)}</text>')
    for i, segs in enumerate(lines):
        sp = "".join(f'<tspan fill="{c}">{esc(tx)}</tspan>' for tx, c in segs)
        out.append(f'<text class="code a" data-t="{t0 + i*dt:.2f}" x="{x+22}" y="{y + 30 + i*lh + size*0.55:.0f}" style="font-size:{size}px" xml:space="preserve">{sp}</text>')
    return "\n".join(out)


def checkrow(cy, n, label, tamil, t):
    return f'''<g class="a" data-t="{t}"><circle cx="70" cy="{cy}" r="32" fill="{OR}"/><text x="70" y="{cy+12}" text-anchor="middle" style="font:700 34px Inter" fill="{PANEL}">{n}</text>
<text x="128" y="{cy-6}" style="font:700 34px Inter" fill="#fff">{esc(label)}</text>
<text x="128" y="{cy+38}" class="ta" style="font-size:28px">{esc(tamil)}</text></g>'''


def tick(cx, cy, t, color=GRN):
    return f'<g class="a" data-t="{t}"><circle cx="{cx}" cy="{cy}" r="20" fill="{color}"/><path d="M{cx-10} {cy}l7 8 13-15" stroke="{PANEL}" stroke-width="4.5" fill="none"/></g>'


def cross(cx, cy, t):
    return f'<g class="a" data-t="{t}"><circle cx="{cx}" cy="{cy}" r="20" fill="{RED}"/><path d="M{cx-8} {cy-8}l16 16M{cx+8} {cy-8}l-16 16" stroke="{PANEL}" stroke-width="4.5"/></g>'


def hook_scene_html(i, n, sc):
    """Hook scene (reels 17+): giant line visible at 0.0 s, Tamil follow-up at ~0.35 s, tall 778x760 panel with motion from frame 1.
    sc: hook (<= ~6 words), hook2, svg (viewBox 0 0 778 760), optional flash_t (red screen flash), s, e."""
    fl = f'<div class="hflash blink" data-t="{sc["flash_t"]}"></div>' if sc.get("flash_t") is not None else ""
    return f'''<div class="scene" data-start="{sc["s"]}" data-end="{sc["e"]}">
<div class="hk a" data-t="0">{esc(sc["hook"])}</div>
<div class="hk2 a" data-t="{sc.get("hook2_t", 0.35)}"{f' style="font-size:{sc["h2size"]}px"' if sc.get("h2size") else ""}>{esc(sc["hook2"])}</div>
<div class="panel hpanel a" data-t="0"><svg viewBox="0 0 778 760" width="778" height="760">{DEFS}{sc["svg"]}</svg></div>
<div class="foot">TECHNICAL SCREENING &nbsp;·&nbsp; {i+1:02d} / {n:02d}</div>{fl}
</div>'''


def scene_html(i, n, sc):
    if sc.get("hook"):
        return hook_scene_html(i, n, sc)
    tsize = f' style="font-size:{sc["tsize"]}px"' if sc.get("tsize") else ""
    ssize = f' style="font-size:{sc["ssize"]}px"' if sc.get("ssize") else ""
    cta = ""
    if sc.get("cta"):
        icon = ('<svg width="34" height="34" viewBox="0 0 34 34"><path d="M3 16L31 3L22 31L16 19Z M16 19L31 3" fill="none" stroke="#11324F" stroke-width="3.2" stroke-linejoin="round"/></svg>'
                if sc.get("cta_icon") == "send" else
                '<svg width="28" height="36" viewBox="0 0 30 38"><path d="M3 3h24v32l-12-9-12 9z" fill="none" stroke="#11324F" stroke-width="3.5" stroke-linejoin="round"/></svg>')
        cta = ('<div class="cta a" data-t="%s">%s%s</div>'
               % (sc.get("cta_t", 2.4), icon, esc(sc.get("cta_text", "நேர்முகத் தேர்வுக்காக சேமிக்கவும்."))))
    body = f'<div class="body a" data-t="{sc.get("body_t", 0.5 if i else 0.3)}">{esc(sc["body"])}</div>' if sc.get("body") else ""
    return f'''<div class="scene" data-start="{sc["s"]}" data-end="{sc["e"]}">
<div class="tag a" data-t="0"><i></i>{esc(sc["tag"])}</div>
<div class="title a" data-t="0"{tsize}>{esc(sc["title"])}</div>
<div class="sub a" data-t="0.1"{ssize}>{esc(sc["sub"])}</div>
<div class="panel a" data-t="0"><svg viewBox="0 0 778 520" width="778" height="520">{DEFS}{sc["svg"]}</svg></div>
{body}{cta}
<div class="foot">TECHNICAL SCREENING &nbsp;·&nbsp; {i+1:02d} / {n:02d}</div>
</div>'''


def build(reel, path):
    sc = reel["scenes"]
    scenes = "\n".join(scene_html(i, len(sc), s) for i, s in enumerate(sc))
    doc = f'''<!doctype html><html><head><meta charset="utf-8"><title>Genesis CNC {reel["id"]}</title><style>{CSS}</style></head>
<body><img class="logo" src="assets/logo.png"><div class="hdr-r">CNC &nbsp;/&nbsp; FIELD NOTES</div>
<div style="position:absolute;left:0;top:0;opacity:0;font:500 42px NTamil">அ<b style="font:700 80px Inter">A</b></div><div class="rule" style="top:326px"></div><div class="rule" style="top:1370px"></div>
{scenes}
<script>window.TOTAL={sc[-1]["e"]};{JS}</script></body></html>'''
    open(path, "w", encoding="utf-8").write(doc)
