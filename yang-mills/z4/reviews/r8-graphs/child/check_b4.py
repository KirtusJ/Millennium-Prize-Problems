"""Known-answer check of B4's only explicit SU(2) coefficients (binary-experiment.md).

B4 states NO strong-coupling tube coefficient, so instead we check what it does state.
Predicates fixed before running (script exits 0 only if all hold):
 P1: r = I2(6)/I1(6), s = r**18, M = round(1/(4 s^2)) equals 4292   (binary-experiment.md:32)
 P2: sum_{n>=1}(n+1)^2 s^n == s(4-3s+s^2)/(1-s)^3 to rel 1e-10 for s in {0.01,0.1,0.5}  (line 6-7)
 P3: r_n(u)=I_{n+1}(u)/I_1(u) <= r_1(u)**n for n=1..12, u in {0.5,2,6,15}  (line 5)
 P4: Phi(-1) rounds to 0.158655  (line 32)
Bessel I_n computed by power series (numpy only). Results appended to result_check_b4.txt (never overwritten).
"""
import math, sys, os
import numpy as np

def I(n, x, K=200):
    k = np.arange(K)
    logt = (2*k + n) * math.log(x / 2) - np.array([math.lgamma(j + 1) + math.lgamma(j + n + 1) for j in k])
    return float(np.exp(logt).sum())

out = []
r = I(2, 6.0) / I(1, 6.0)
s = r ** 18
M = round(1 / (4 * s * s))
out.append(f"r1(6)={r:.12f} s=r^18={s:.6e} M={M}")
p1 = (M == 4292)
p2 = True
for sv in (0.01, 0.1, 0.5):
    lhs = sum((n + 1) ** 2 * sv ** n for n in range(1, 4000))
    rhs = sv * (4 - 3 * sv + sv * sv) / (1 - sv) ** 3
    p2 &= abs(lhs - rhs) <= 1e-10 * rhs
    out.append(f"s={sv}: series={lhs:.12g} closed={rhs:.12g}")
p3 = True
for u in (0.5, 2.0, 6.0, 15.0):
    r1 = I(2, u) / I(1, u)
    for n in range(1, 13):
        p3 &= I(n + 1, u) / I(1, u) <= r1 ** n * (1 + 1e-12)
phi = 0.5 * math.erfc(1 / math.sqrt(2))
p4 = (round(phi, 6) == 0.158655)
out.append(f"Phi(-1)={phi:.8f}")
out.append(f"P1={p1} P2={p2} P3={p3} P4={p4}")
txt = "\n".join(out)
print(txt)
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "result_check_b4.txt")
with open(path, "a", encoding="utf-8") as f:
    f.write(txt + "\n---\n")
sys.exit(0 if (p1 and p2 and p3 and p4) else 1)
