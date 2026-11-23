"""Extract text from the two Chatterjee reference PDFs.

Predicates (stated before the first run):
P1. Reads exactly ref/chatterjee_1602.01222.pdf and ref/chatterjee_2401.10507.pdf
    (paths relative to this script's directory) with pypdf; no network access.
P2. For each PDF writes text/<stem>.txt, containing for every page n (1-based,
    equal to the PDF page index + 1) a line "=== PAGE n ===" followed by that
    page's extracted text, in page order.
P3. Never overwrites: if an output file already exists, it is left untouched
    and the script reports "skip" for it (opened with mode "x").
P4. Prints, per PDF, the page count and number of characters written; exits 0
    on success and non-zero if a PDF is missing or unreadable.
"""
import sys
sys.path.append("C:/Users/donke/AppData/Roaming/Python/Python314/site-packages")
import os
from pypdf import PdfReader

HERE = os.path.dirname(os.path.abspath(__file__))
PDFS = ["chatterjee_1602.01222.pdf", "chatterjee_2401.10507.pdf"]


def main():
    outdir = os.path.join(HERE, "text")
    os.makedirs(outdir, exist_ok=True)
    for name in PDFS:
        src = os.path.join(HERE, "ref", name)
        dst = os.path.join(outdir, os.path.splitext(name)[0] + ".txt")
        if os.path.exists(dst):
            print(f"skip {dst} (exists)")
            continue
        reader = PdfReader(src)
        parts = []
        for i, page in enumerate(reader.pages, start=1):
            parts.append(f"=== PAGE {i} ===\n{page.extract_text() or ''}\n")
        text = "".join(parts)
        with open(dst, "x", encoding="utf-8") as f:
            f.write(text)
        print(f"{name}: pages={len(reader.pages)} chars={len(text)} -> {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
