#!/usr/bin/env python3
"""Follow-up to b_weyl.py, whose predicates B1 (1e-12) and B2 (1e-10) FAILED and are kept.
Diagnosis to test: the failures are cancellation at small multipliers (n large, beta small:
multiplier ~1e-9 against integrand of size ~1), not a wrong formula.
PREDICATES (fixed before this run):
 F1  Absolute error |weyl - 2I_{n+1}/beta| <= 1e-13 * m(0,beta) for all n=0..6 and the six betas
     (basis: double rounding of a sum of terms of size e^{beta}, 200 nodes).
 F2  Direct S^3 quadrature: |Cf(U) - m f(U)| <= 1e-12 * m(0,beta) for all 126 instances (no
     instance excluded), three fixed-seed U each.
 F3  Relative errors restricted to instances with m(n,beta) >= 1e-3*m(0,beta): <= 1e-10.
Command: python3 /home/user/z4-workers/chal5/b_weyl_followup.py   (seed 20261124)
Result: /home/user/z4-workers/chal5/b_weyl_followup_result.txt (mode 'x')
"""
import math, numpy as np
out = open('/home/user/z4-workers/chal5/b_weyl_followup_result.txt', 'x')
def P(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s+'\n')
def besseli(nu, x):
    return sum(math.exp((2*k+nu)*math.log(x/2)-math.lgamma(k+1)-math.lgamma(k+nu+1)) for k in range(200))
betas = [0.3, 1.0, 2.0, 3.276133577, 5.0, 8.0]
xs, ws = np.polynomial.legendre.leggauss(200); t = (xs+1)*math.pi/2; wt = ws*math.pi/2
rng = np.random.default_rng(20261124)
xp, wp = np.polynomial.legendre.leggauss(80); psi = (xp+1)*math.pi/2; wpsi = wp*math.pi/2*(2/math.pi)*np.sin(psi)**2
xc, wc = np.polynomial.legendre.leggauss(60); phi = 2*math.pi*np.arange(64)/64
PS, C, PH = np.meshgrid(psi, xc, phi, indexing='ij'); Wt = wpsi[:, None, None]*(wc/2)[None, :, None]/64
S = np.sqrt(1-C**2); q0 = np.cos(PS); q1 = np.sin(PS)*C; q2 = np.sin(PS)*S*np.cos(PH); q3 = np.sin(PS)*S*np.sin(PH)
f1 = f2 = f3 = 0.0; n3 = 0
for beta in betas:
    m0 = 2*besseli(1, beta)/beta
    for n in range(7):
        m = 2*besseli(n+1, beta)/beta
        mW = (1/(n+1))*(2/math.pi)*np.sum(wt*np.exp(beta*np.cos(t))*np.sin((n+1)*t)*np.sin(t))
        f1 = max(f1, abs(mW-m)/m0)
        for _ in range(3):
            u = rng.normal(size=4); u /= np.linalg.norm(u)
            fU = (u[0]+1j*u[1])**n
            Cf = np.sum(Wt*np.exp(beta*(u[0]*q0+u[1]*q1+u[2]*q2+u[3]*q3))*(q0+1j*q1)**n)
            f2 = max(f2, abs(Cf-m*fU)/m0)
            if m >= 1e-3*m0 and abs(fU) > 1e-3:
                n3 += 1; f3 = max(f3, abs(Cf-m*fU)/(m*abs(fU)), abs(mW-m)/m)
P(f'F1 max abs err / m(0) = {f1:.3e}', 'PASS' if f1 <= 1e-13 else 'FAIL')
P(f'F2 max abs err / m(0) = {f2:.3e}', 'PASS' if f2 <= 1e-12 else 'FAIL')
P(f'F3 instances {n3}, max rel err = {f3:.3e}', 'PASS' if f3 <= 1e-10 else 'FAIL')
out.close()
