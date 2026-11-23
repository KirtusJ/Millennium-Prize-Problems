"""Completeness check of results2.json (rows for items a-e).
Predicates (fixed before first run; expectations are my own, tolerance-free):
 P1: every row has non-empty address, authors, title, year, locator, how_read, statement.
 P2: how_read in {FULL TEXT, ABSTRACT ONLY, SUMMARY ONLY, FROM MEMORY}.
 P3: a row whose locator is empty or says 'none' must have how_read == FROM MEMORY.
 P4 (for all rows): per-case test first; report number of qualifying rows.
 P5: control.txt is one line.
Exit 0 iff all pass. Output written to a new file (mode x), never overwritten.
"""
import json, sys
rows = json.load(open("results2.json"))
need = ["address","authors","title","year","locator","how_read","statement"]
ok_how = {"FULL TEXT","ABSTRACT ONLY","SUMMARY ONLY","FROM MEMORY"}
out = open(sys.argv[1], "x"); fails = 0
q = 0
for i, r in enumerate(rows):
    f = [k for k in need if not str(r.get(k, "")).strip()]
    if f: out.write(f"row {i} P1 FAIL missing {f}\n"); fails += 1
    if r.get("how_read") not in ok_how: out.write(f"row {i} P2 FAIL\n"); fails += 1
    if str(r.get("locator","")).strip().lower() in ("","none") and r.get("how_read") != "FROM MEMORY":
        out.write(f"row {i} P3 FAIL\n"); fails += 1
    if not f: q += 1
out.write(f"rows={len(rows)} complete={q}\n")
if len(open("control.txt").read().strip().splitlines()) != 1: out.write("P5 FAIL\n"); fails += 1
out.write(f"fails={fails}\n"); print(f"rows={len(rows)} complete={q} fails={fails}")
sys.exit(1 if fails else 0)
