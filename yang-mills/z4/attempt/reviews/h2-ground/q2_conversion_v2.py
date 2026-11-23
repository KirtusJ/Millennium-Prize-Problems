"""q2_conversion.py -- checks for Q2 (zero-mode Hamiltonian from the Wilson action) and Q1 digit comparison.

Conventions: lattice units a=1, Wilson action S = beta * sum_P (1 - (1/2) tr U_P), beta = 4/g^2,
constant links U_i = exp(i A_i . sigma / 2), A_i in R^3 (coupling absorbed), box L^3, temporal spacing 1.

PREDICATES (fixed before first run):
 P1  For 200 random pairs (A,B) (seed 12345) with |A|,|B| = eps, eps in {1e-1, 1e-2}:
     1 - (1/2) tr(U_A U_B U_A^-1 U_B^-1) = |A x B|^2/8 * (1 + r), |r| <= 10*eps^2.
     (tolerance: next term of the expansion is relative O(eps^2); factor 10 covers angular prefactors)
 P2  For 200 random A, D (seed 12346), |D| = eps: 1 - (1/2) tr(U_{A+D} U_A^-1) = |D|^2/8 (1+r), |r| <= 10*eps^2
     for eps in {1e-1,1e-2}  (temporal plaquette -> kinetic term, mass M = beta L^3 / 4).
 P3  Symbolic: H = -(2/(beta L^3)) Lap_A + (beta L^3/8) sum_{i<j} |A_i x A_j|^2, A = s Y with s = 2 (beta L^3)^(-1/3)
     equals (beta L^3)^(-1/3) * ( -(1/2) Lap_Y + 2 sum |Y_i x Y_j|^2 ) exactly (sympy simplify == 0).
 P4  Symbolic: with beta = 4/g^2, (beta L^3)^(-1/3) * 4^(1/3) * e_vB / (1/L) ... i.e.
     e_h3 * beta^(-1/3) / L == 4^(-1/3) e_h3 g^(2/3) / L, and 4^(-1/3) e_h3 = e_vB. Exact.
 P5  Digits: 4^(-1/3) * (6.534885, 3.012539, 3.602838) agree with brief (4.1167196, 1.8977806, 2.2696457)
     to within 1e-6 (tolerance: brief quotes 6.534885 to 7 significant digits, rounding 5e-7 times 4^(-1/3) ~ 3.2e-7;
     1e-6 allows two roundings).
 P6  Ours e0 = 4.1167196 vs van Baal hep-ph/0008206 p.11 eps1 = 4.116719735: |diff| <= 1e-7
     (tolerance: ours given to 8 significant digits, rounding 5e-8; 1e-7 allows rounding on both sides).
Exit code 0 iff all predicates hold.
"""
import numpy as np, sys

out = open("q2_results.txt", "x")
def log(s):
    print(s); out.write(s + "\n")

sig = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex)]
def U(a):
    n = np.linalg.norm(a)
    if n == 0: return np.eye(2, dtype=complex)
    h = sum(a[k]*sig[k] for k in range(3)) / n
    return np.cos(n/2)*np.eye(2) + 1j*np.sin(n/2)*h

ok = True
rng = np.random.default_rng(12345)
for eps in (1e-1, 1e-2):
    worst = 0.0
    for _ in range(200):
        a = rng.normal(size=3); a *= eps/np.linalg.norm(a)
        b = rng.normal(size=3); b *= eps/np.linalg.norm(b)
        P = U(a) @ U(b) @ np.linalg.inv(U(a)) @ np.linalg.inv(U(b))
        lhs = 1 - 0.5*np.trace(P).real
        rhs = np.dot(np.cross(a,b), np.cross(a,b))/8
        if rhs < 1e-30: continue
        worst = max(worst, abs(lhs/rhs - 1))
    p = worst <= 10*eps**2
    ok &= p; log(f"P1 eps={eps}: worst |r|={worst:.3e} bound={10*eps**2:.1e} {'MET' if p else 'FAILED'}")
rng = np.random.default_rng(12346)
for eps in (1e-1, 1e-2):
    worst = 0.0
    for _ in range(200):
        a = rng.normal(size=3)
        d = rng.normal(size=3); d *= eps/np.linalg.norm(d)
        lhs = 1 - 0.5*np.trace(U(a+d) @ np.linalg.inv(U(a))).real
        rhs = eps**2/8
        worst = max(worst, abs(lhs/rhs - 1))
    p = worst <= 10*eps**2
    ok &= p; log(f"P2 eps={eps}: worst |r|={worst:.3e} bound={10*eps**2:.1e} {'MET' if p else 'FAILED'}")
    if not p: log("   note: nonabelian A (|A|~1) -> geodesic distance between U(a+d),U(a) is not |d|; see report")

# P3/P4 exact: monomials as dict base->Fraction exponent, bases '2','beta','L','g' (no sympy available)
from fractions import Fraction as F
def mul(*ms):
    r = {}
    for m_ in ms:
        for k, v in m_.items(): r[k] = r.get(k, F(0)) + v
    return {k: v for k, v in r.items() if v != 0}
def pw(m_, q): return {k: v*q for k, v in m_.items()}
X = {'beta': F(1), 'L': F(3)}
sval = mul({'2': F(1)}, pw(X, F(-1, 3)))
kin = mul({'2': F(1)}, pw(X, F(-1)), pw(sval, F(-2)))      # 2/X / s^2
pot = mul({'2': F(-3)}, X, pw(sval, F(4)))                  # X/8 * s^4
kap = pw(X, F(-1, 3))
d1 = (kin == mul(kap, {'2': F(-1)})); d2 = (pot == mul(kap, {'2': F(1)}))
p = d1 and d2; ok &= p
log(f"P3 kinetic coef = {kin} vs kappa/2 = {mul(kap,{'2':F(-1)})}; potential coef = {pot} vs 2 kappa = {mul(kap,{'2':F(1)})}: {'MET' if p else 'FAILED'}")
beta_sub = {'2': F(2), 'g': F(-2)}                           # beta = 4/g^2
m_ = mul(pw(beta_sub, F(-1, 3)), {'L': F(-1)})               # beta^(-1/3) L^-1 (times e_h3)
target = mul({'2': F(-2, 3)}, {'g': F(2, 3)}, {'L': F(-1)})  # 4^(-1/3) g^(2/3) / L
p = (m_ == target) and (pw(X, F(-1,3)) == mul({'beta':F(-1,3)}, {'L':F(-1)})); ok &= p
log(f"P4 beta^(-1/3)/L at beta=4/g^2 = {m_} vs 4^(-1/3) g^(2/3)/L = {target}: {'MET' if p else 'FAILED'}")

ours3 = [6.534885, 3.012539, 3.602838]; brief = [4.1167196, 1.8977806, 2.2696457]
for x, y in zip(ours3, brief):
    c = x*4**(-1/3); p = abs(c-y) <= 1e-6; ok &= p
    log(f"P5 4^(-1/3)*{x} = {c:.8f} vs {y}: diff {c-y:+.2e} {'MET' if p else 'FAILED'}")
vb = 4.116719735; dd = 4.1167196 - vb; p = abs(dd) <= 1e-7; ok &= p
log(f"P6 ours 4.1167196 vs vanBaal 4.116719735: diff {dd:+.2e} {'MET' if p else 'FAILED'}")
log(f"ratios (measured only): E-gap/e0 = {1.8977806/4.1167196:.5f}, scalar gap / J=2 gap = {2.2696457/1.8977806:.5f}")
log("ALL MET" if ok else "SOME FAILED")
out.close()
sys.exit(0 if ok else 1)
