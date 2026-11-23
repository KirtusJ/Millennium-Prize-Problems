"""q2_v3_extra.py -- follow-up predicates fixed after K2, before this run.
 P2b For 200 random (A,D), seed 12347, |A| = 0.1, |D| = eps in {1e-2,1e-3}:
     1 - (1/2) tr(U_{A+D} U_A^-1) = |D|^2/8 (1+r) with |r| <= 10*(|A|^2 + eps^2) = ~0.1
     (tolerance: the chart metric deviates from flat at relative O(|A|^2) (sin^2(x)/x^2 ~ 1 - x^2/3 for transverse D); factor 10 margin).
 P6b |4^(-1/3)*6.534885 - 4.116719735| <= 4^(-1/3)*5e-7 + 5e-10 (rounding of the 7-digit k=3 value plus rounding of vB's 10-digit value).
 P6c (measured only) sign: is ours (Rayleigh-Ritz, an upper bound) below vB's value?
Exit 0 iff P2b and P6b hold.
"""
import numpy as np, sys
out = open("q2_v3_results.txt", "x")
def log(s): print(s); out.write(s+"\n")
sig = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex)]
def U(a):
    n = np.linalg.norm(a); h = sum(a[k]*sig[k] for k in range(3))/n
    return np.cos(n/2)*np.eye(2) + 1j*np.sin(n/2)*h
ok = True; rng = np.random.default_rng(12347)
for eps in (1e-2, 1e-3):
    worst = 0.0
    for _ in range(200):
        a = rng.normal(size=3); a *= 0.1/np.linalg.norm(a)
        d = rng.normal(size=3); d *= eps/np.linalg.norm(d)
        lhs = 1 - 0.5*np.trace(U(a+d) @ np.linalg.inv(U(a))).real
        worst = max(worst, abs(lhs/(eps**2/8) - 1))
    b = 10*(0.01+eps**2); p = worst <= b; ok &= p
    log(f"P2b |A|=0.1 eps={eps}: worst |r|={worst:.3e} bound={b:.3e} {'MET' if p else 'FAILED'}")
c = 4**(-1/3)*6.534885; vb = 4.116719735; tol = 4**(-1/3)*5e-7 + 5e-10
p = abs(c-vb) <= tol; ok &= p
log(f"P6b {c:.9f} vs {vb}: diff {c-vb:+.3e} tol {tol:.2e} {'MET' if p else 'FAILED'}")
log(f"P6c measured: ours - vB = {c-vb:+.3e} (negative = ours lower; within rounding, so no ordering conclusion)")
log("ALL MET" if ok else "SOME FAILED"); out.close(); sys.exit(0 if ok else 1)
