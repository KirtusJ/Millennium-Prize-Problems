"""test_c2.py -- corrected counterexample families for (C) (worker a3-C). Usage: python3 test_c2.py <result_file>
Written after P5, P6, P7 of test_c.py FAILED (own expectation: atom weights too large). Originals kept.
Result file mode "x"; no randomness.
Families (lattice scale 1, gap m = 1/xi), R := C(xi/2)/C(xi):
 H2': nu = w delta_m + delta_1, w = exp(-xi).
 HH': nu = w delta_m + eps^2 1[sqrt(m),3] d eps, w = exp(-sqrt(xi))  (hole between m and sqrt(m)).
 HHp: same hole, w = m^4 (polynomially small bottom weight): expected (C) HOLDS (measured, predicate Q4).
 DK': psi = T^xi phi, phi two-atom with w = exp(-3 xi + 3): R_psi = C_phi(2.5 xi)/C_phi(3 xi).
PREDICATES (fixed before first run):
 Q1 H2': R(xi) >= exp(xi/2)/3 for all xi in {4,...,256}.
 Q2 HH': R(4096)/R(64) > 100.
 Q3 DK': R_psi(xi) >= exp(xi/2)/3 for all xi in {4,...,256}.
 Q4 HHp: R(xi) <= 5 for all xi in {64,256,1024,4096,16384}  (atom dominates at n=xi/2 once e^{-sqrt(xi)/2}<<m^4).
     Tolerance: none needed beyond quadrature (trapezoid 2e5 points, smooth integrand).
 Q5 H2' limit shape: mu_beta(E = xi) -> 1/(1+e^{-1}) = 0.731 (mass escapes to infinity: not tight) at xi=256, |diff|<1e-3.
"""
import sys, math
import numpy as np
f = open(sys.argv[1], "x")
def w_(s): print(s); f.write(s + "\n")
XIS = [4, 8, 16, 32, 64, 128, 256]; met = []; fail = []
def rec(name, ok): (met if ok else fail).append(name); w_(f"{name}: {'MET' if ok else 'FAILED'}")
q = 0
for xi in XIS:
    m = 1 / xi; w = math.exp(-xi)
    C = lambda n: w * math.exp(-m * n) + math.exp(-n)
    R = C(xi / 2) / C(xi); q += R >= math.exp(xi / 2) / 3
    pa, pb = w * math.exp(-1), math.exp(-xi)
    w_(f"H2' xi={xi} R={R:.4e} mu(E=1)={pa/(pa+pb):.5f} mu(E=xi)={pb/(pa+pb):.5f}")
w_(f"Q1 cases {q}/{len(XIS)}"); rec("Q1", q == len(XIS))
rec("Q5", abs(pb / (pa + pb) - 1 / (1 + math.exp(-1))) < 1e-3)
def hole(xi, w):
    m = 1 / xi; eh = math.sqrt(m); e = np.linspace(eh, 3.0, 200001)
    def C(n):
        y = e ** 2 * np.exp(-n * e)
        return w * math.exp(-m * n) + float(np.sum((y[1:] + y[:-1]) / 2) * (e[1] - e[0]))
    return C(xi / 2) / C(xi), C(1) / C(0)
RH = {}
for xi in [64, 256, 1024, 4096]:
    RH[xi], c10 = hole(xi, math.exp(-math.sqrt(xi)))
    w_(f"HH' xi={xi} R={RH[xi]:.4e} C(1)/C(0)={c10:.4f}")
w_(f"Q2 ratio {RH[4096]/RH[64]:.3e}"); rec("Q2", RH[4096] / RH[64] > 100)
q = 0; L = [64, 256, 1024, 4096, 16384]
for xi in L:
    R, c10 = hole(xi, (1 / xi) ** 4); q += R <= 5
    w_(f"HHp xi={xi} R={R:.4e}")
w_(f"Q4 cases {q}/{len(L)}"); rec("Q4", q == len(L))
q = 0
for xi in XIS:
    m = 1 / xi; w = math.exp(-3 * xi + 3)
    C = lambda n: w * math.exp(-m * n) + math.exp(-n)
    R = C(2.5 * xi) / C(3 * xi); q += R >= math.exp(xi / 2) / 3
    w_(f"DK' xi={xi} R_psi={R:.4e}")
w_(f"Q3 cases {q}/{len(XIS)}"); rec("Q3", q == len(XIS))
w_(f"SUMMARY met={len(met)} {met} failed={len(fail)} {fail}")
f.close(); sys.exit(0 if not fail else 1)
