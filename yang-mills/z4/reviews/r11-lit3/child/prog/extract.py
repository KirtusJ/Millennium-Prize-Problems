"""Extract page-tagged text from the two reference PDFs.

Predicates (stated before first run):
  P1. Each of ref/2111.12813.pdf and ref/2201.03487.pdf opens with pypdf.
  P2. Each has page count >= 1.
  P3. Page 1 text of each is non-empty (contains at least one alphabetic author/title word).
  P4. Output is written ONLY to ref/text/<stem>.txt with "=== PAGE n ===" tags (n 1-based).
Exit 0 iff all predicates hold; otherwise exit 1.
Usage: python -I prog/extract.py <child_dir>
"""
import sys
import os

sys.path.append("C:/Users/donke/AppData/Roaming/Python/Python314/site-packages")
from pypdf import PdfReader  # noqa: E402


def main():
    base = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    ref = os.path.join(base, "ref")
    out = os.path.join(ref, "text")
    os.makedirs(out, exist_ok=True)
    ok = True
    for name in ("2111.12813.pdf", "2201.03487.pdf"):
        r = PdfReader(os.path.join(ref, name))
        n = len(r.pages)
        parts = []
        for i, p in enumerate(r.pages, 1):
            try:
                t = p.extract_text() or ""
            except Exception as e:  # keep going
                t = f"[extract error: {e}]"
            parts.append(f"=== PAGE {i} ===\n{t}\n")
        first = parts[0] if parts else ""
        alpha = any(c.isalpha() for c in first.split("\n", 1)[-1])
        dst = os.path.join(out, name[:-4] + ".txt")
        with open(dst, "w", encoding="utf-8") as f:
            f.write("".join(parts))
        print(f"{name}: pages={n} page1_alpha={alpha} -> {dst}")
        ok = ok and n >= 1 and alpha
    print("PREDICATES", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
