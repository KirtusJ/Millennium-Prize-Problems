"""Check closed forms (beta, b) against direct evaluation from (kA, lam).

Predicates (fixed before first run):
 P1: for each beta in {0.1,1,10,1000}, b in {1e-1,1e-4}, and each Q in {B,A,D,L,U,w}:
     |closed - direct| <= TOL * |direct|.
 P2: w closed form is independent of b (same w at both b, relative TOL).
 P3: at beta = 1e6, ratio of each quantity to its stated leading asymptotic form
     is within 0.01 of 1 (corrections are O(beta^-1/2) ~ 1e-3).
 P4: kA = 2/kB numerically reproduces Laplacian eigenvalue match: spectrum of
     -kA*sum X^2 = kA*j(j+1) equals (1/(2kB))*4j(j+1) for j in {1/2,1,3/2} (rel TOL).
TOL = 1e-12: source = double-precision eps (~2.2e-16) times a generous safety factor
(~1e4) for the handful of floating operations involved.
Exit code 0 iff all predicates met.
"""
import math, os, sys

TOL = 1e-12

def direct(beta, b):
    kB, lam = beta * b, beta / b
    kA = 2.0 / kB
    g = lam / kA
    B = min(g, 17 * math.sqrt(g) / 8 + 3 / 16)
    A = 9 * kA / (8 * (1 + B))
    D = kA**2 * (6 + 8 * math.sqrt(B))**2
    L = A / 16; U = 4 * D / A; w = A**2 / (8 * D)
    return dict(B=B, A=A, D=D, L=L, U=U, w=w)

def closed(beta, b):
    B = min(beta**2 / 2, 17 * beta / (8 * math.sqrt(2)) + 3 / 16)
    s = math.sqrt(B)
    return dict(B=B, A=9 / (4 * beta * b * (1 + B)),
                D=16 * (3 + 4 * s)**2 / (beta * b)**2,
                L=9 / (64 * beta * b * (1 + B)),
                U=256 * (1 + B) * (3 + 4 * s)**2 / (9 * beta * b),
                w=81 / (2048 * (1 + B)**2 * (3 + 4 * s)**2))

def lead(beta, b):
    r2 = math.sqrt(2)
    return dict(B=17 * beta / (8 * r2), A=18 * r2 / 17 / (b * beta**2),
                D=272 * r2 / (b**2 * beta), L=9 * r2 / 136 / (b * beta**2),
                U=9248 / 9 * beta / b, w=81 * r2 / 157216 / beta**3)

met = failed = 0
lines = []
def rec(name, ok, info):
    global met, failed
    met += ok; failed += (not ok)
    lines.append(f"{'MET ' if ok else 'FAIL'} {name}: {info}")

for beta in (0.1, 1, 10, 1000):
    for b in (1e-1, 1e-4):
        d, c = direct(beta, b), closed(beta, b)
        for q in d:
            rel = abs(c[q] - d[q]) / abs(d[q])
            rec(f"P1 beta={beta} b={b} {q}", rel <= TOL, f"direct={d[q]:.10g} closed={c[q]:.10g} rel={rel:.2e}")
    w1, w2 = closed(beta, 1e-1)["w"], closed(beta, 1e-4)["w"]
    rec(f"P2 beta={beta}", abs(w1 - w2) <= TOL * abs(w1), f"w={w1:.10g}")
beta = 1e6
d, l = direct(beta, 1e-1), lead(beta, 1e-1)
for q in d:
    r = d[q] / l[q]
    rec(f"P3 {q}", abs(r - 1) < 0.01, f"ratio={r:.6f}")
kB = 0.37; kA = 2 / kB
for j in (0.5, 1, 1.5):
    a, bb = kA * j * (j + 1), 4 * j * (j + 1) / (2 * kB)
    rec(f"P4 j={j}", abs(a - bb) <= TOL * abs(bb), f"{a:.12g} vs {bb:.12g}")

lines.append(f"SUMMARY met={met} failed={failed}")
here = os.path.dirname(os.path.abspath(__file__))
n = 1
while os.path.exists(os.path.join(here, f"results_run{n}.txt")):
    n += 1
out = os.path.join(here, f"results_run{n}.txt")
with open(out, "x", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print(f"wrote {out}"); print(lines[-1])
sys.exit(0 if failed == 0 else 1)
