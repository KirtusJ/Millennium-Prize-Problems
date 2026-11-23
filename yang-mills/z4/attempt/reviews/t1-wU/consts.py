"""consts.py -- numerical sanity checks of the constants and scalar identities used in tun_upper.tex.

Predicates (fixed before the first run):
 P1  c* = int_0^pi sqrt(2*2asinh(sin a)) da agrees with 4.6054132 to 5e-8
     (tolerance: the 8 digits quoted in the note; Gauss-Legendre with 4000 nodes on two halves).
 P2  L = sqrt(2*eps(pi/2)) = sqrt(4 asinh 1) agrees with 1.8776 to 5e-5 (4 digits quoted).
 P3  for s in a grid of 200 points of (0,1]: alpha/2 - s^2 = c/A and log A = 2 asinh s,
     to 1e-12 relative (float rounding).
 P4  Z = int e^{beta cos th} (2/pi) sin^2 th dth equals 2 I_1(beta)/beta for beta in {1, 8, 64},
     rel. 1e-10 (quadrature with 20000 midpoint nodes, error far below that for these beta).
 P5  K multiplier: (2/pi) int e^{beta cos th} sin((n+1)th) sin th dth / ((n+1) Z) = I_{n+1}/I_1,
     n = 0..6, beta in {1, 8}, rel. 1e-9 (same quadrature).
 P6  D(beta) = 1 - 1/(2beta) - sqrt(2 pi beta) e^{-beta}/2 > 0 for beta in {1.0001, 1.5, 2, 10, 125}.
 P7  outer exponent (I9): for 40 s-values x 40 r-values, max_q (p.q - c q2^2) + (c/A) r - 1
     <= -(r^2/64)(1-1/A^2)^2 + 1e-12 (max over q on a 20000-point grid of the circle; the grid
     max is <= the true max, so this tests the inequality only up to grid resolution: measured
     additionally the margin).
 P8  I1 lower bound (I7): I_1(z) >= e^z (1-1/(2z))/sqrt(2 pi z) - 1/2 for z in {0.5,1,2,5,20,100}.
 P9  e^{-z} I_0(z) <= min(1, H_delta(z)) for delta in {0.1,0.5,1}, z in {0.5,1,5,50,500}.
Exit code 0 iff all predicates met. Seed: none needed (deterministic grids).
Result file written with mode "x".
"""
import math, sys, json
import numpy as np
from numpy.polynomial.legendre import leggauss

out = sys.argv[1]
res = {}
ok = True

def gl(f, a, b, n=4000):
    x, w = leggauss(n)
    t = 0.5*(b-a)*x + 0.5*(b+a)
    return 0.5*(b-a)*np.sum(w*f(t))

eps = lambda a: 2*np.arcsinh(np.sin(a))
cstar = gl(lambda a: np.sqrt(2*eps(a)), 0, np.pi/2) + gl(lambda a: np.sqrt(2*eps(a)), np.pi/2, np.pi)
res['P1'] = dict(cstar=float(cstar), met=abs(cstar-4.6054132) < 5e-8)
L = math.sqrt(4*math.asinh(1))
res['P2'] = dict(L=L, met=abs(L-1.8776) < 5e-5)

s = np.linspace(0.005, 1, 200)
al = 2*s*np.sqrt(1+s*s); c = s*s+al/2; A = 1+2*c
e1 = np.max(np.abs(al/2-s*s-c/A)/(c/A)); e2 = np.max(np.abs(np.log(A)-2*np.arcsinh(s))/(2*np.arcsinh(s)))
res['P3'] = dict(err1=float(e1), err2=float(e2), met=bool(e1 < 1e-12 and e2 < 1e-12))

def Iquad(nu, z, N=20000):
    t = (np.arange(N)+0.5)*np.pi/N
    return np.sum(np.exp(z*np.cos(t))*np.cos(nu*t))/N
p4 = []
for b in [1, 8, 64]:
    N = 20000; t = (np.arange(N)+0.5)*np.pi/N
    Z = (2/np.pi)*np.sum(np.exp(b*np.cos(t))*np.sin(t)**2)*np.pi/N
    p4.append(abs(Z/(2*Iquad(1, b)/b)-1))
res['P4'] = dict(relerr=p4, met=max(p4) < 1e-10)
p5 = []
for b in [1, 8]:
    N = 20000; t = (np.arange(N)+0.5)*np.pi/N
    Z = (2/np.pi)*np.sum(np.exp(b*np.cos(t))*np.sin(t)**2)*np.pi/N
    for n in range(7):
        cn = (2/np.pi)*np.sum(np.exp(b*np.cos(t))*np.sin((n+1)*t)*np.sin(t))*np.pi/N
        p5.append(abs(cn/((n+1)*Z)/(Iquad(n+1, b)/Iquad(1, b))-1))
res['P5'] = dict(maxrel=max(p5), met=max(p5) < 1e-9)
Dv = {b: 1-1/(2*b)-math.sqrt(2*math.pi*b)*math.exp(-b)/2 for b in [1.0001, 1.5, 2, 10, 125]}
res['P6'] = dict(D=Dv, met=all(v > 0 for v in Dv.values()))
th = np.linspace(0, 2*np.pi, 20000, endpoint=False); q1, q2 = np.cos(th), np.sin(th)
worst = -1e9
for sv in np.linspace(0.025, 1, 40):
    a_ = 2*sv*math.sqrt(1+sv*sv); cc = sv*sv+a_/2; AA = 1+2*cc
    for r in np.linspace(0.0, 1, 40):
        R, rho = math.sqrt(1-r), math.sqrt(r)
        lhs = np.max(R*q1+rho*q2-cc*q2**2) + cc/AA*r - 1
        rhs = -(r*r/64)*(1-1/AA**2)**2
        worst = max(worst, lhs-rhs)
res['P7'] = dict(max_lhs_minus_rhs=float(worst), met=worst <= 1e-12)
p8 = []
for z in [0.5, 1, 2, 5, 20, 100]:
    p8.append(Iquad(1, z)*1 - (math.exp(z)*(1-1/(2*z))/math.sqrt(2*math.pi*z)-0.5))
res['P8'] = dict(margins=[float(x) for x in p8], met=min(p8) > 0)
p9 = []
for d in [0.1, 0.5, 1.0]:
    for z in [0.5, 1, 5, 50, 500]:
        N = 200000; t = (np.arange(N)+0.5)*np.pi/N
        e0 = np.sum(np.exp(z*(np.cos(t)-1)))/N
        H = (2*math.pi*z*(1-5*d*d/48))**-0.5 + math.exp(-z*(1-math.cos(d)))
        p9.append(min(1, H)-e0)
res['P9'] = dict(min_margin=float(min(p9)), met=min(p9) >= 0)
ok = all(v['met'] for v in res.values())
res['all_met'] = ok
with open(out, 'x') as fh:
    json.dump(res, fh, indent=1, default=float)
print({k: bool(v['met']) for k, v in res.items() if k != 'all_met'}, 'ALL' if ok else 'FAIL')
sys.exit(0 if ok else 1)
