"""check_rows.py -- completeness checker for the a1-rig literature table, plus one
arithmetic recomputation from Shen-Zhu-Zhu (arXiv:2204.12737).

Usage: python3 check_rows.py rows.json OUTFILE
OUTFILE is opened with mode "x" (never overwritten). No randomness (no seed needed).

Predicates (fixed before the first run):
 P1 (for all rows) every row has non-empty q, addr, auth, title, year, loc, how.
 P2 (for all rows) how is one of FULL TEXT / ABSTRACT ONLY / SUMMARY ONLY / FROM MEMORY.
 P3 (for all rows) if how == "FROM MEMORY" then loc starts with "none"; if how != "FROM MEMORY"
    then loc does not start with "none"  (a row without a read locator must be FROM MEMORY).
 P4 every question R1, R2, R3a..R3e, R4, R5a, R5c, R5d, R5e, R5f, R6 has >= 1 row.
    (R5b is answered from the R5a row; it is excluded by design.)
 P5 (expected to hold) at least one row per question R1, R5a, R5e is FULL TEXT.
 P6 SZZ arithmetic, SU(N), d: K_S = alpha(N+2)/4 - 1 - 8 N beta (d-1) with alpha = 2
    (eq. (4.8) and Assumption 1.1). For N=2, d=4: Ricci constant = 1, beta threshold = 1/48,
    and K_S(beta) = 1 - 48 beta. Checked with tolerance 1e-12 (float rounding of exact
    rationals; source of tolerance: double precision of a handful of operations).
    Also (measured only, my convention conversion, not in the paper): conventional Wilson
    beta_W with action (beta_W/N) sum Re Tr equals N^2 beta, i.e. beta_W < 4/48 = 1/12 for SU(2), d=4.
 P7 (measured only) counts of rows per how-read class.
For each "for all" predicate the number of qualifying rows is reported first.
"""
import json, sys
from fractions import Fraction as F

rows = json.load(open(sys.argv[1]))
out = open(sys.argv[2], "x")
def w(s):
    print(s); out.write(s + "\n")

HOW = {"FULL TEXT", "ABSTRACT ONLY", "SUMMARY ONLY", "FROM MEMORY"}
KEYS = ["q", "addr", "auth", "title", "year", "loc", "how"]
met = failed = 0
def res(name, ok, detail):
    global met, failed
    met += ok; failed += (not ok)
    w(f"{name}: {'MET' if ok else 'FAILED'} {detail}")

w(f"rows qualifying for for-all predicates: {len(rows)}")
bad1 = [i for i, r in enumerate(rows) if any(not str(r.get(k, "")).strip() for k in KEYS)]
res("P1", not bad1, f"bad rows {bad1}")
bad2 = [i for i, r in enumerate(rows) if r["how"] not in HOW]
res("P2", not bad2, f"bad rows {bad2}")
bad3 = [i for i, r in enumerate(rows)
        if (r["how"] == "FROM MEMORY") != r["loc"].lower().startswith("none")]
res("P3", not bad3, f"bad rows {bad3}")
need = ["R1", "R2", "R3a", "R3b", "R3c", "R3d", "R3e", "R4", "R5a", "R5c", "R5d", "R5e", "R5f", "R6"]
miss = [q for q in need if not any(r["q"] == q for r in rows)]
res("P4", not miss, f"missing {miss}")
miss5 = [q for q in ["R1", "R5a", "R5e"] if not any(r["q"] == q and r["how"] == "FULL TEXT" for r in rows)]
res("P5", not miss5, f"no full text for {miss5}")

N, d, alpha = 2, 4, 2
ric = F(alpha * (N + 2), 4) - 1
thr = ric / (8 * N * (d - 1))
ks = lambda b: ric - 8 * N * b * (d - 1)
ok6 = ric == 1 and thr == F(1, 48) and all(abs(float(ks(F(k, 1000))) - (1 - 48 * k / 1000)) < 1e-12 for k in range(0, 21))
res("P6", ok6, f"Ric={ric} threshold={thr} K_S(1/96)={ks(F(1,96))}")
w(f"measured: beta_W threshold (SU(2),d=4) = N^2*thr = {N*N*thr}")
for h in sorted(HOW):
    w(f"measured P7: {h}: {sum(r['how']==h for r in rows)}")
w(f"SUMMARY met={met} failed={failed} measured_only=2")
out.close()
sys.exit(1 if failed else 0)
