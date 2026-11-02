"""Usage: python3 render.py batchX.py [reel_id ...] [--stills-only]
Builds HTML for each reel, runs the safe-zone check, saves QC stills, renders MP4 (30 fps, H.264)."""
import sys, subprocess, pathlib, importlib.util, json
from playwright.sync_api import sync_playwright
D = pathlib.Path(__file__).parent
sys.path.insert(0, str(D))
import gen

spec_path = D / sys.argv[1]
spec = importlib.util.spec_from_file_location("spec", spec_path); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
ids = [a for a in sys.argv[2:] if not a.startswith("--")]
stills_only = "--stills-only" in sys.argv
FPS = 30
(D / "qc").mkdir(exist_ok=True); (D / "out").mkdir(exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch()
    for reel in mod.REELS:
        if ids and reel["id"] not in ids:
            continue
        name = f'Genesis_CNC_{reel["id"]}_{reel["slug"]}_Tamil'
        html = D / f"{name}.html"
        gen.build(reel, html)
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        pg.goto(html.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
        issues = pg.evaluate("check()")
        total = pg.evaluate("window.TOTAL")
        print(f"== {name}  {total}s  issues: {len(issues)}")
        for i in issues: print("   ", i)
        # QC stills: end of every scene (fully built) for review
        shots = []
        for k, sc in enumerate(reel["scenes"]):
            t = sc["e"] - 0.35 if k < len(reel["scenes"]) - 1 else sc["e"] - 0.05
            pg.evaluate(f"render({t})"); f = D / "qc" / f'{reel["id"]}_s{k+1}.png'; pg.screenshot(path=str(f)); shots.append(str(f))
        subprocess.run(["ffmpeg", "-v", "error", "-y", *sum([["-i", s] for s in shots], []), "-filter_complex",
                        "".join(f"[{k}]crop=1080:1460:0:0,scale=360:-1[v{k}];" for k in range(len(shots))) + ("".join(f"[v{k}]" for k in range(len(shots))) + f"hstack=inputs={len(shots)}" if len(shots) > 1 else "[v0]null"),
                        str(D / "qc" / f'{reel["id"]}_sheet.png')], check=True)
        if not stills_only:
            out = D / "out" / f"{name}.mp4"
            ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
                                   "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                                   "-metadata", "artist=Johnny Paul", "-metadata", f'title=Genesis CNC {reel["id"]} - {reel["slug"].replace("_"," ")} (Tamil)',
                                   str(out)], stdin=subprocess.PIPE)
            for i in range(int(total * FPS)):
                pg.evaluate(f"render({i / FPS})"); ff.stdin.write(pg.screenshot(type="png"))
            ff.stdin.close(); ff.wait(); print("   rendered", out.name, "rc", ff.returncode)
        pg.close()
    b.close()
