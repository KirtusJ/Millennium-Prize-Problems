"""extract.py -- fetch manifest and page-1 identity check for the six arXiv PDFs.

Predicates (fixed before first run):
 P1 (per file) the file in ref/ begins with b'%PDF-'.
 P2 (per file) pypdf opens it and reports >= 1 page.
 P3 (per file) page 1 text contains every expected author surname listed below
    (case-insensitive) -- the director's description, written from memory.
 P4 (per file) page 1 text contains every expected title keyword below (case-insensitive).
Tolerance: none (string containment). Expectations come from the task brief, so a P3/P4
failure is a mismatch of the director's description OR of my keyword choice; I say which.
No randomness (no seed needed). Text goes only to ref/text/. Result file
results/manifest.json is never overwritten (exit 3 if it exists).
Exit code: 0 if all predicates evaluated (failures are reported, not fatal); 2 on I/O error.
"""
import json, os, sys
sys.path.append("C:/Users/donke/AppData/Roaming/Python/Python314/site-packages")
from pypdf import PdfReader

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECT = {
    "2204.12737": (["Shen", "Zhu"], ["Yang", "Mills", "strong"]),
    "2006.16229": (["Chatterjee"], ["confinement"]),
    "2111.12813": (["Cao", "Chatterjee"], ["state space", "Yang"]),
    "2201.03487": (["Chandra", "Chevyrev", "Hairer", "Shen"], ["Yang", "Higgs"]),
    "2202.10375": (["Adhikari", "Cao"], ["correlation decay", "weak coupling"]),
    "1808.09896": (["Chatterjee"], ["Wilson loops", "Ising"]),
}

def main():
    out = os.path.join(BASE, "results", "manifest.json")
    if os.path.exists(out):
        print("result file exists; refusing to overwrite"); return 3
    os.makedirs(os.path.join(BASE, "results"), exist_ok=True)
    rows = []; met = failed = 0
    for pid, (auth, kw) in EXPECT.items():
        p = os.path.join(BASE, "ref", pid + ".pdf")
        row = {"id": pid, "bytes": os.path.getsize(p)}
        with open(p, "rb") as f:
            row["P1"] = f.read(5) == b"%PDF-"
        r = PdfReader(p)
        row["pages"] = len(r.pages); row["P2"] = row["pages"] >= 1
        texts = []
        for i, pg in enumerate(r.pages):
            try: t = pg.extract_text() or ""
            except Exception as e: t = f"[extract error {e}]"
            texts.append(f"\n=== PAGE {i+1} ===\n" + t)
        with open(os.path.join(BASE, "ref", "text", pid + ".txt"), "w", encoding="utf-8") as f:
            f.write("".join(texts))
        p1 = texts[0].lower()
        row["P3_missing"] = [a for a in auth if a.lower() not in p1]; row["P3"] = not row["P3_missing"]
        row["P4_missing"] = [k for k in kw if k.lower() not in p1]; row["P4"] = not row["P4_missing"]
        with open(os.path.join(BASE, "ref", "text", "heads.txt"), "a", encoding="utf-8") as f:
            f.write(pid + ": " + " ".join(texts[0].split()[:45]) + "\n")  # identity line, kept in ref/ only
        for k in ("P1", "P2", "P3", "P4"):
            met += row[k]; failed += (not row[k])
        rows.append(row); print(json.dumps(row, ensure_ascii=False))
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"rows": rows, "met": met, "failed": failed}, f, indent=1)
    print(f"met {met}, failed {failed}, measured only {len(rows)*2} (bytes, pages)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
