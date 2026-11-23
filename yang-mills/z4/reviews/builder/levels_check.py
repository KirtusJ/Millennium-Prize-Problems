"""levels_check.py -- numerical cross-check of LevelsControl.lean (B1) on Z_n.

Setting: Z_n, levels c_j = cos(2 pi j/n), chi_j = cos(2 pi j/n), j = 0..n-1,
unique maximizer j = 0, spacing d = 1 - cos(2 pi/n), K = n, b = N^2.
gap(b) = -log(lam1/lam0), computed as log1p(E') - log1p(R') with
E' = sum_{j>0} exp(b(c_j-1)), R' = sum_{j>0} exp(b(c_j-1)) chi_j (exact rewriting,
avoids cancellation). Deterministic, no randomness (no seed needed).

Predicates, fixed before the first run:
 H  (hypothesis count, rule 4): for n in 2..8, N in 1..16, count cases with
    2*K*exp(-b d) <= 1 (the Lean hypothesis hsmall). Reported, not a pass/fail.
 P1 for all qualifying cases: 0 < lam1/lam0 <= 1 and
    b*gap <= 4*K*b*exp(-b d) * (1 + 1e-12).
    Tolerance 1e-12: float rounding of log1p/exp sums of <= 8 terms
    (each ~1e-16 relative); 1e-12 is a generous multiple.
 P2 the README section 3 table (Z2,Z3,Z5 at N=2,4,8,16), printed to 3 significant
    figures, is reproduced: |M - table|/table <= 5e-3 (half a unit in the 3rd
    significant figure is at most 0.5/100 = 5e-3 relative).
 P3 measured only: C_eff(n) = b*gap / (b*exp(-b d)) at N = 16, compared with
    the proved constant 4K (expected C_eff ~ k = 1 (n=2) or 2 (n>=3); the Lean
    constant is not sharp).
Result file results/levels_run1.txt; never overwritten (exit 3 if present).
Exit 0 iff P1 and P2 are met.
"""
import math, os, sys

OUT = os.path.join("results", "levels_run1.txt")
if os.path.exists(OUT):
    print("result file exists; refusing to overwrite"); sys.exit(3)
os.makedirs("results", exist_ok=True)

def gap(n, b):
    c = [math.cos(2*math.pi*j/n) for j in range(n)]
    E = sum(math.exp(b*(c[j]-1)) for j in range(1, n))
    R = sum(math.exp(b*(c[j]-1))*c[j] for j in range(1, n))
    ratio = (1+R)/(1+E)
    return math.log1p(E) - math.log1p(R), ratio

lines = []
qual = tot = 0; p1_fail = []
for n in range(2, 9):
    d = 1 - math.cos(2*math.pi/n); K = n
    for N in range(1, 17):
        b = N*N; tot += 1
        q = math.exp(-b*d)
        if 2*K*q > 1: continue
        qual += 1
        g, r = gap(n, b)
        bound = 4*K*b*q
        ok = (0 < r <= 1) and (b*g <= bound*(1+1e-12))
        if not ok: p1_fail.append((n, N, b*g, bound, r))
lines.append(f"H: {qual} of {tot} cases satisfy 2K exp(-bd) <= 1")
lines.append(f"P1: {'met' if not p1_fail else 'FAILED'}; failures {p1_fail}")

table = {2: [2.68e-3, 4.05e-13, 3.29e-54, 2.24e-220],
         3: [2.97e-2, 1.81e-9, 3.90e-40, 1.31e-164],
         5: [3.32e-1, 3.49e-4, 5.51e-18, 5.32e-75]}
p2_fail = []
for n, vals in table.items():
    for N, t in zip([2, 4, 8, 16], vals):
        M = N*N*gap(n, N*N)[0]
        rel = abs(M-t)/t
        lines.append(f"  Z{n} N={N}: M={M:.6e} table={t:.3e} rel={rel:.2e}")
        if rel > 5e-3: p2_fail.append((n, N, M, t))
lines.append(f"P2: {'met' if not p2_fail else 'FAILED'}; failures {p2_fail}")

for n in range(2, 9):
    d = 1 - math.cos(2*math.pi/n); b = 256
    g, _ = gap(n, b)
    lines.append(f"P3 (measured): n={n} C_eff={g/math.exp(-b*d):.6f} proved C=4K={4*n}")

txt = "\n".join(lines) + "\n"
open(OUT, "w", encoding="utf8").write(txt)
print(txt)
sys.exit(0 if not p1_fail and not p2_fail else 1)
