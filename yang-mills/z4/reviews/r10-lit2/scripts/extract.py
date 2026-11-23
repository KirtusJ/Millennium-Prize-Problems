import sys
sys.path.append("C:/Users/donke/AppData/Roaming/Python/Python314/site-packages")
import os, pypdf
ref = sys.argv[1]; out = sys.argv[2]
os.makedirs(out, exist_ok=True)
for f in sorted(os.listdir(ref)):
    if not f.endswith(".pdf"): continue
    p = os.path.join(ref, f)
    r = pypdf.PdfReader(p)
    txt = []
    for i, pg in enumerate(r.pages):
        txt.append(f"\n=== PAGE {i+1} ===\n" + (pg.extract_text() or ""))
    t = "".join(txt)
    open(os.path.join(out, f[:-4] + ".txt"), "w", encoding="utf-8").write(t)
    print(f, os.path.getsize(p), "bytes", len(r.pages), "pages", len(t), "chars")
