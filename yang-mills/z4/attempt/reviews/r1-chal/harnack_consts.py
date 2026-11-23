"""harnack_consts.py -- recheck HARNACK.md constants.
Predicates (fixed before first run):
 HP1 min over d in [0.5,10], rho in (0,1/2] of l(K0)/d equals 8.35 within 0.01 (2-digit claim), attained near d=3.65, rho=0.265.
 HP2 l(K_K)/d at d=3.65, rho=0.265, K=1 equals 9.09 within 0.01.
 HP3 8.35(2a+r)+9.09a <= 35(a+r) and 8.35*3a+9.09a <= 35(a+r) for all a,r >= 0 (algebra; checked on grid).
 HP4 Haar ball volume v(r)=(2r-sin2r)/(2pi) >= 11 r^3/(24 pi) on r in (0,1/2] (grid 10^4).
 HP5 I1(z) <= (pi/2) e^z/sqrt(2 pi z) for z in [0.5, 2000] (quadrature; tol 1e-9 relative).
 HP6 phase-0 length: for random unit axes n1,n2 and s1,s2 in (0,1] with s1 s2 sin psi <= M/sqrt(beta): min(s) psi <= (pi/2) sqrt(M) beta^{-1/4}  (10^5 samples, seed 7).
"""
import numpy as np, sys
out = open(sys.argv[1], 'x')
def log(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
def ell(Kp, d, r): R = d+2*r; return Kp + R*R + np.log(np.pi/2) + 2*np.log(24*np.pi/(11*r**3))
D, Rr = np.meshgrid(np.linspace(0.5,10,1901), np.linspace(0.005,0.5,991))
K0 = 2*(2*Rr+Rr**2)**2
f = ell(K0, D, Rr)/D; i = np.unravel_index(np.argmin(f), f.shape)
log('HP1 min l(K0)/d =', f[i], 'at d,rho', D[i], Rr[i], 'MET' if abs(f[i]-8.35) < 0.01 else 'FAILED')
d, r = 3.65, 0.265; KK = 2*(np.sqrt(0.5)+2*r+r*r)**2
v = ell(KK, d, r)/d; log('HP2 l(K_K)/d =', v, 'l(K0)/d at same', ell(2*(2*r+r*r)**2, d, r)/d, 'MET' if abs(v-9.09) < 0.01 else 'FAILED')
A, Rg = np.meshgrid(np.linspace(0,1,201), np.linspace(0,1,201))
ok = np.all(8.35*(2*A+Rg)+9.09*A <= 35*(A+Rg)+1e-12) and np.all(8.35*3*A+9.09*A <= 35*(A+Rg)+1e-12)
log('HP3', 'MET' if ok else 'FAILED', 'max coeff ratios', (2*8.35+9.09)/35, (3*8.35+9.09)/35)
rr = np.linspace(1e-4, 0.5, 10000); vv = (2*rr-np.sin(2*rr))/(2*np.pi)
log('HP4 min v/(11r^3/24pi) =', np.min(vv/(11*rr**3/(24*np.pi))), 'MET' if np.all(vv >= 11*rr**3/(24*np.pi)) else 'FAILED')
gx, gw = np.polynomial.legendre.leggauss(400)
worst = 0
for z in np.geomspace(0.5, 2000, 200):
    t = 0.5*np.pi*(gx+1); I1e = 0.5*np.pi*np.sum(gw*np.exp(z*(np.cos(t)-1))*np.cos(t))/np.pi
    worst = max(worst, I1e/((np.pi/2)/np.sqrt(2*np.pi*z)))
log('HP5 max I1/bound =', worst, 'MET' if worst <= 1+1e-9 else 'FAILED')
rng = np.random.default_rng(7); viol = 0; qual = 0; wr = 0
for _ in range(100000):
    beta = 10**rng.uniform(1,6); Mm = rng.uniform(0.5,4)
    s1, s2 = rng.uniform(0,1,2); psi = rng.uniform(0, np.pi/2)
    if s1*s2*np.sin(psi) > Mm/np.sqrt(beta): continue
    qual += 1; ratio = min(s1,s2)*psi/((np.pi/2)*np.sqrt(Mm)*beta**-0.25)
    wr = max(wr, ratio); viol += ratio > 1
log('HP6 qualifying', qual, 'violations', viol, 'worst ratio', wr, 'MET' if viol == 0 else 'FAILED')
