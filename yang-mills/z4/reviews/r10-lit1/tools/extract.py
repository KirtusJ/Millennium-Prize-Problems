"""Extract text from each PDF in ref/ to text/<name>.txt with page markers.
Predicates fixed before first run:
 E1 each PDF opens with pypdf and reports a page count (expectation).
 E2 text extraction 'works' for a file iff >= 80% of pages yield >= 200 characters
    (tolerance: chosen by me; a typeset page has ~2000-4000 chars, a scanned page with no text layer ~0;
     200 allows title/figure pages). Driver 1987 is expected possibly to FAIL E2 (scan).
 E3 output files are never overwritten: if text/<name>.txt exists, write text/<name>.N.txt.
Summary written to extract_summary.txt (appended). Exit 0 if E1 holds for all files, else 1.
"""
import sys, os
sys.path.append("C:/Users/donke/AppData/Roaming/Python/Python314/site-packages")
import pypdf
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ref = os.path.join(root, "ref"); out = os.path.join(root, "text"); os.makedirs(out, exist_ok=True)
ok = True; lines = []
for fn in sorted(os.listdir(ref)):
    p = os.path.join(ref, fn)
    try:
        r = pypdf.PdfReader(p); n = len(r.pages)
    except Exception as e:
        ok = False; lines.append(f"{fn} E1=FAILED {e!r}"); continue
    texts = []
    for i, pg in enumerate(r.pages):
        try: t = pg.extract_text() or ""
        except Exception as e: t = f"[extract error {e!r}]"
        texts.append(t)
    good = sum(len(t) >= 200 for t in texts)
    e2 = "met" if good >= 0.8 * n else "FAILED"
    base = os.path.join(out, fn[:-4]); dst = base + ".txt"; k = 1
    while os.path.exists(dst): dst = f"{base}.{k}.txt"; k += 1
    with open(dst, "w", encoding="utf-8") as f:
        for i, t in enumerate(texts): f.write(f"\n=== PAGE {i+1} ===\n{t}\n")
    lines.append(f"{fn} size={os.path.getsize(p)} pages={n} pages_with_text>=200={good} E1=met E2={e2} -> {os.path.basename(dst)}")
with open(os.path.join(root, "extract_summary.txt"), "a", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print("\n".join(lines)); sys.exit(0 if ok else 1)
