"""A3: L, U, w of A4's interval in units of Lambda along beta = c*log(1/(b*Lambda)).

Conventions (derived in notes.md step 1): kappa_A = 2/(beta b), g = beta^2/2, lambda = beta/b.
Two readings of D: D (A4 excited_band) and D_* = kappa_A^2 min{(6+8 sqrt B)^2, 86401} (A4 third_moment).
c in {1, 0.5} and Lambda are ILLUSTRATIVE; Lambda = 1 sets the unit.
Grid: b*Lambda in {1e-1,1e-2,1e-4,1e-8} x c in {1, 0.5}: 8 cases (x2 readings for P1).

Predicates (fixed before the first run):
 P1 (for all 16 case-readings): 0 < L < U and 0 < w <= 1 (A4 claims 0<L<U; mass <= 4 -> w must be small).
 P2 (for all 8): closed form L = 9/(64 beta b (1+B)) equals A/16 computed from (kappa_A, lambda) to rel 1e-12
     (tolerance: double precision 2.2e-16 times ~1e4 safety for a handful of operations).
 P3 (for all 8): Lean bounds hold numerically: L >= (9/64)/(beta(1+2beta)b), w_* <= 9/(512(1+beta)^2).
 P4 (for each c): L/Lambda strictly increases as b*Lambda decreases (expectation: L -> infinity).
 P5 (for each c): w strictly decreases as b*Lambda decreases (expectation: w -> 0).
 P6 (for all 8): D_* < D strictly, i.e. the third-moment improvement is active on this grid.
     (my expectation: it is NOT active, since (6+8 sqrt B)^2 > 86401 needs B > 1296; I record it as a
      predicate I expect to FAIL so the failure is my expectation being tested, not a target defect.)
 Measured only: the numbers in the table; U/L ratio.
Output: results/a3_<timestamp>.txt, never overwritten. No randomness (no seed needed).
"""
import math, os, sys, time

TOL = 1e-12
def Bf(g): return min(g, 17*math.sqrt(g)/8 + 3/16)

def quantities(beta, b):
    kA = 2/(beta*b); lam = beta/b; g = lam/kA
    B = Bf(g)
    A = 9*kA/(8*(1+B))
    D = kA**2*(6+8*math.sqrt(B))**2
    Ds = kA**2*min((6+8*math.sqrt(B))**2, 86401)
    return dict(g=g, B=B, A=A, L=A/16, U=4*D/A, w=A*A/(8*D), Us=4*Ds/A, ws=A*A/(8*Ds), D=D, Ds=Ds)

met = failed = 0; lines = []; fails = []
def pred(name, ok, info=""):
    global met, failed
    if ok: met += 1
    else: failed += 1; fails.append(f"{name} {info}")
    lines.append(f"{'MET ' if ok else 'FAIL'} {name} {info}")

rows = []
for c in (1.0, 0.5):
    seq = []
    for bl in (1e-1, 1e-2, 1e-4, 1e-8):
        beta = c*math.log(1/bl); b = bl  # Lambda = 1
        q = quantities(beta, b)
        rows.append((c, bl, beta, q)); seq.append(q)
        for tag, U, w in (("D", q["U"], q["w"]), ("D*", q["Us"], q["ws"])):
            pred(f"P1[c={c},bL={bl:g},{tag}]", 0 < q["L"] < U and 0 < w <= 1)
        Lc = 9/(64*beta*b*(1+q["B"]))
        pred(f"P2[c={c},bL={bl:g}]", abs(Lc-q["L"]) <= TOL*abs(Lc), f"rel={abs(Lc-q['L'])/Lc:.1e}")
        pred(f"P3[c={c},bL={bl:g}]", q["L"] >= (9/64)/(beta*(1+2*beta)*b) and q["ws"] <= 9/(512*(1+beta)**2))
        pred(f"P6[c={c},bL={bl:g}]", q["Ds"] < q["D"], f"B={q['B']:.3f}")
    pred(f"P4[c={c}]", all(seq[i+1]["L"] > seq[i]["L"] for i in range(3)))
    pred(f"P5[c={c}]", all(seq[i+1]["w"] < seq[i]["w"] for i in range(3)))

out = ["A3 table (Lambda = 1 unit; c, Lambda illustrative)",
       f"{'c':>4} {'bLam':>7} {'beta':>8} {'B':>8} {'L/Lam':>11} {'U/Lam':>11} {'w':>10} {'U*/Lam':>11} {'w*':>10} {'U/L':>9}"]
for c, bl, beta, q in rows:
    out.append(f"{c:>4} {bl:>7.0e} {beta:>8.3f} {q['B']:>8.3f} {q['L']:>11.3e} {q['U']:>11.3e} {q['w']:>10.3e} {q['Us']:>11.3e} {q['ws']:>10.3e} {q['U']/q['L']:>9.2e}")
out += ["", *lines, "", f"COUNTS met={met} failed={failed} measured_only={len(rows)} rows",
        "FAILED: " + ("; ".join(fails) if fails else "none")]
os.makedirs("results", exist_ok=True)
fn = f"results/a3_{time.strftime('%Y%m%d_%H%M%S')}.txt"
assert not os.path.exists(fn)
open(fn, "x", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out)); print("wrote", fn)
# exit code: 0 iff the only failures are the P6 family (expected failures)
sys.exit(0 if all(f.startswith("P6") for f in fails) else 1)
