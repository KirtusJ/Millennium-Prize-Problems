"""Conversion check h_3 -> van Baal/Luscher normalisation. Predicates and tolerance
sources fixed BEFORE the first run.

Inputs (only): inputs/grounding.md, inputs/A3_NOTES.md.
Conversion: h3 = -1/2 Lap + 2 S(x), vB = -1/2 Lap + 1/2 S(x), S = sum_{i<j}|x_i x x_j|^2.
Put x = a y: h3 = a^-2 [ -1/2 Lap_y + 2 a^6 S(y) ]. Need 2 a^6 = 1/2 -> a = 4^(-1/6),
so h3 = 4^(1/3) h_vB and e_vB = 4^(-1/3) e_h3 (claimed in both files).

Predicates:
 C1 (algebra): a=4^(-1/6) gives 2a^6 = 1/2 and a^-2 = 4^(1/3) to 1e-14 (float eps).
 C2 (cross-source): both files state the same factor 4^(-1/3) / Y=4^(-1/6)c  [read by hand;
    recorded as measured-only text check, not code].
 P1: |6.534885*4^(-1/3) - 4.116719735| <= tol_E0 = 5e-7*4^(-1/3) (rounding of the 6-decimal
    input; the published value is taken as exact to its 9 digits, +-5e-10 added).
 P2: the claim "difference 1.5e-7" holds: |diff| rounds to 1.5e-7 at 2 sig. figs, i.e.
    1.45e-7 <= |diff| < 1.55e-7 (sign reported separately).
 P3a: |3.012539*4^(-1/3) - 1.89778|   <= 5e-6 + 3.15e-7 (quoted value rounded to 5 decimals
      in A3_NOTES, plus input rounding).
 P3b: |3.012539*4^(-1/3) - 1.8977806| <= 5e-8 + 3.15e-7  (7-decimal value in grounding.md).
 P3c, P3d: same two for 3.602838 vs 2.26965 and 2.2696457.
 Measured only: the differences themselves.
Result file opened with mode 'x' (delete results.txt to rerun).
"""
import math
k = 4 ** (-1 / 3)
a = 4 ** (-1 / 6)
out = []
def rec(s): out.append(s); print(s)
res = {}
def pred(name, ok): res[name] = ok; rec(f"{name}: {'MET' if ok else 'FAILED'}")

rec(f"k=4^(-1/3)={k:.12f}; a=4^(-1/6)={a:.12f}")
pred("C1", abs(2*a**6-0.5) < 1e-14 and abs(a**-2-4**(1/3)) < 1e-14)
rec(f"2a^6={2*a**6!r} a^-2={a**-2!r} 4^(1/3)={4**(1/3)!r}")

e0 = 6.534885*k; pub = 4.116719735; d = e0 - pub
tol = 5e-7*k + 5e-10
rec(f"E0 conv={e0:.10f} published={pub} diff={d:.4e} tol(rounding)={tol:.4e} ratio={abs(d)/tol:.3f}")
pred("P1", abs(d) <= tol)
pred("P2", 1.45e-7 <= abs(d) < 1.55e-7)
rec(f"diff sign: ours - published = {d:+.4e}")

tolin = 5e-7*k
for name, g, q, qt in [("P3a", 3.012539, 1.89778, 5e-6), ("P3b", 3.012539, 1.8977806, 5e-8),
                       ("P3c", 3.602838, 2.26965, 5e-6), ("P3d", 3.602838, 2.2696457, 5e-8)]:
    c = g*k; dd = c - q; t = qt + tolin
    rec(f"{name}: conv={c:.10f} quoted={q} diff={dd:+.4e} tol={t:.4e}")
    pred(name, abs(dd) <= t)
with open("results.txt", "x") as f:
    f.write("\n".join(out)+"\n")
