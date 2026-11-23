"""Search 0810.2183.txt for key terms and print PDF page numbers.

Predicates fixed BEFORE first run (must find, else exit 1):
  P1: 'Polyakov' occurs on >=1 page
  P2: 'cusp' occurs on >=1 page
  P3: 'renormaliz' occurs on >=1 page
  P4: 'Dotsenko' occurs on >=1 page
  P5: 'Brandt' occurs on >=1 page
Non-predicate (reported only): perimeter, linear, Vergeles, Neri, Sato,
  self-intersect, multiplicativ, ultraviolet, Korchemsky, Wilson loop.
Writes results to scripts/find_terms_result.txt only if it does not exist.
"""
import os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "..", "0810.2183.txt")
txt = open(src, encoding="utf-8").read()
parts = re.split(r"=== PAGE (\d+) ===", txt)
pages = {int(parts[i]): parts[i+1] for i in range(1, len(parts), 2)}
terms = ["Polyakov","cusp","renormaliz","Dotsenko","Brandt","perimeter","linear",
         "Vergeles","Neri","Sato","self-intersect","intersect","multiplicativ",
         "ultraviolet","Korchemsky","divergen"]
out = []
hits = {}
for t in terms:
    pg = [n for n in sorted(pages) if t.lower() in pages[n].lower()]
    hits[t] = pg
    out.append(f"{t}: {pg}")
res = "\n".join(out)
print(res)
ok = all(hits[t] for t in ["Polyakov","cusp","renormaliz","Dotsenko","Brandt"])
print("PREDICATES", "PASS" if ok else "FAIL")
rf = os.path.join(here, "find_terms_result.txt")
if not os.path.exists(rf):
    open(rf, "w", encoding="utf-8").write(res + "\nPREDICATES " + ("PASS" if ok else "FAIL") + "\n")
sys.exit(0 if ok else 1)
