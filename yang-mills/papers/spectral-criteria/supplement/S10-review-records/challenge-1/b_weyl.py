#!/usr/bin/env python3
"""Item (b): convolution by exp(beta*(1/2)Tr) on SU(2), spin-n/2 multiplier.

PREDICATES (fixed before the first run):
 B1  For n=0..6 and beta in {0.3,1,2,3.276133577,5,8}: the Weyl-formula value
     m_W(n,beta) = (1/(n+1)) * (2/pi) * int_0^pi e^{beta cos t} sin((n+1)t) sin t dt
     agrees with 2 I_{n+1}(beta)/beta (I by power series) to relative error <= 1e-12.
     Basis of tolerance: Gauss-Legendre with 200 nodes on an entire integrand; double precision.
 B2  Direct test that does not presuppose Schur orthogonality: for f(V) = a(V)^n
     (a = upper-left entry; a matrix coefficient of the spin-n/2 representation) and
     3 fixed-seed random U in SU(2), (Cf)(U) = int exp(beta*(1/2)Tr(U V^{-1})) f(V) dV
     (Haar probability, product quadrature on S^3) equals m(n,beta) f(U), relative
     error <= 1e-10 in |Cf(U) - m f(U)| / (m |f(U)|).  Instances with |f(U)| < 1e-3 are
     reported as not qualifying (ratio ill-conditioned).
 B3  All multipliers > 0 (positive, injective) for the tested (n,beta).
 B4  "Without bounded inverse": for each beta, multiplier(n) is strictly decreasing in n
     for n = 0..40 and multiplier(40) < 1e-20 * multiplier(0) (tends to 0).
Command: python3 /home/user/z4-workers/chal5/b_weyl.py   (no arguments; seed 20261124)
Result file: /home/user/z4-workers/chal5/b_weyl_result.txt (opened with mode 'x').
"""
import math, sys
import numpy as np

SEED = 20261124
out = open('/home/user/z4-workers/chal5/b_weyl_result.txt', 'x')
def P(*a):
    s = ' '.join(str(x) for x in a)
    print(s); out.write(s + '\n'); out.flush()

def besseli(nu, x, terms=200):
    s = 0.0
    for k in range(terms):
        s += math.exp((2*k+nu)*math.log(x/2) - math.lgamma(k+1) - math.lgamma(k+nu+1))
    return s

betas = [0.3, 1.0, 2.0, 3.276133577, 5.0, 8.0]
xs, ws = np.polynomial.legendre.leggauss(200)
t = (xs+1)*math.pi/2; wt = ws*math.pi/2

P('B1 Weyl formula vs 2 I_{n+1}(beta)/beta')
b1max = 0.0; b3 = True
for beta in betas:
    for n in range(7):
        mW = (1/(n+1))*(2/math.pi)*np.sum(wt*np.exp(beta*np.cos(t))*np.sin((n+1)*t)*np.sin(t))
        mB = 2*besseli(n+1, beta)/beta
        rel = abs(mW-mB)/mB
        b1max = max(b1max, rel); b3 = b3 and mW > 0 and mB > 0
        P(f'  beta={beta} n={n} weyl={mW:.15e} bessel={mB:.15e} rel={rel:.2e}')
P('B1 max rel err', b1max, 'PASS' if b1max <= 1e-12 else 'FAIL')
P('B3 all positive', 'PASS' if b3 else 'FAIL')

# B2 direct quadrature on S^3: q=(cos p, sin p cos th, sin p sin th cos ph, sin p sin th sin ph)
rng = np.random.default_rng(SEED)
npsi, nth, nph = 80, 60, 64
xp, wp = np.polynomial.legendre.leggauss(npsi); psi = (xp+1)*math.pi/2; wpsi = wp*math.pi/2*(2/math.pi)*np.sin(psi)**2
xc, wc = np.polynomial.legendre.leggauss(nth); wth = wc/2   # c = cos theta
phi = 2*math.pi*np.arange(nph)/nph; wph = np.ones(nph)/nph
PS, C, PH = np.meshgrid(psi, xc, phi, indexing='ij')
Wt = wpsi[:, None, None]*wth[None, :, None]*wph[None, None, :]
S = np.sqrt(1-C**2)
q0 = np.cos(PS); q1 = np.sin(PS)*C; q2 = np.sin(PS)*S*np.cos(PH); q3 = np.sin(PS)*S*np.sin(PH)
P('quadrature weight total (should be 1):', Wt.sum())
# V = [[a, b],[-conj b, conj a]], a = q0 + i q1, b = q2 + i q3 ; (1/2)Tr(U V^{-1}) = <u,q> in R^4
aV = q0 + 1j*q1
b2max = 0.0; qual = 0; tot = 0
for beta in betas:
    for n in range(7):
        m = 2*besseli(n+1, beta)/beta
        for _ in range(3):
            u = rng.normal(size=4); u /= np.linalg.norm(u)
            tot += 1
            fU = (u[0]+1j*u[1])**n
            if abs(fU) < 1e-3:
                P(f'  beta={beta} n={n} not qualifying |f(U)|={abs(fU):.2e}'); continue
            qual += 1
            ker = np.exp(beta*(u[0]*q0+u[1]*q1+u[2]*q2+u[3]*q3))
            Cf = np.sum(Wt*ker*aV**n)
            rel = abs(Cf - m*fU)/(m*abs(fU))
            b2max = max(b2max, rel)
P(f'B2 instances total={tot} qualifying={qual} max rel err={b2max:.3e}', 'PASS' if b2max <= 1e-10 else 'FAIL')

b4 = True
for beta in betas:
    ms = [2*besseli(n+1, beta)/beta for n in range(41)]
    dec = all(ms[i+1] < ms[i] for i in range(40))
    small = ms[40] < 1e-20*ms[0]
    b4 = b4 and dec and small
    P(f'B4 beta={beta} m(0)={ms[0]:.6e} m(6)={ms[6]:.6e} m(40)={ms[40]:.6e} decreasing={dec} small={small}')
P('B4', 'PASS' if b4 else 'FAIL')
out.close()
