#!/usr/bin/env python3
"""Item (e): constants of Remark r:ret (a),(b), Section s:local (iii), and Theorem t:ret envelope.

PREDICATES (fixed before the first run):
 E1  p_{6 beta}(theta) at beta=3.399810242, theta=0.05,0.2,0.6 rounds to 0.00307, 0.156, 0.935
     (three significant figures as quoted).
 E2  p_{6 beta}(theta) at beta=3.276133577, theta=0.1,0.2,1/beta,2/beta rounds to
     0.02, 0.15, 0.39, 0.93 (two decimals as quoted; "approx" in the paper).
 E3  Algebra: n_g * (pi^2 sqrt(e)/4) (1+6beta)^{3/2} theta^3 with n_g=3(N/2)^3,
     theta=c(1+6beta)^{-1/2}N^{-4/3} equals (3 pi^2 sqrt(e)/32) c^3/N, relative error <= 1e-13,
     over N in {6,8,16,64,1024}, beta in {0,0.5,3.276133577,10}, c in {0.1,1,3}.
     Hypothesis per instance: theta <= pi (count qualifying).
 E4  On the same qualifying instances n_g * p_{6beta}(theta) <= (3 pi^2 sqrt(e)/32) c^3/N.
 E5  Envelope of Theorem t:ret: p_k(theta) <= (pi^2 sqrt(e)/4)(1+k)^{3/2} theta^3 on a grid
     k in {0,0.1,1,5,19.66,20.4,60,300}, theta = pi*i/400, i=1..400.  Report the largest ratio
     p/envelope.
 E6  Lemma l:cap: for k in {0.5,5,20}, radius theta in {0.2,0.8,2.0}, centre at angle
     delta in {0.3,1.0,2.0,pi} from v: cap probability (2-d quadrature) <= p_k(theta)+1e-9,
     and p_k(theta) non-decreasing in k on k=0,0.5,...,40 for theta in {0.1,0.5,1,2}.
 E7  "of order theta^3 for fixed beta ... small only for theta well below (6 beta)^{-1/2}":
     report p_{6beta}((6beta)^{-1/2}) at the two couplings (no pass/fail; reported number).
Command: python3 /home/user/z4-workers/chal5/e_caps.py   (no arguments; no randomness)
Result file: /home/user/z4-workers/chal5/e_caps_result.txt (mode 'x').
"""
import math
import numpy as np
out = open('/home/user/z4-workers/chal5/e_caps_result.txt', 'x')
def P(*a):
    s = ' '.join(str(x) for x in a)
    print(s); out.write(s + '\n'); out.flush()

X, W = np.polynomial.legendre.leggauss(400)
def integ(f, a, b, pieces=8):
    s = 0.0
    for i in range(pieces):
        lo = a + (b-a)*i/pieces; hi = a + (b-a)*(i+1)/pieces
        x = (X+1)*(hi-lo)/2 + lo
        s += np.sum(W*f(x))*(hi-lo)/2
    return s
def p(k, th):
    f = lambda r: np.sin(r)**2*np.exp(k*(np.cos(r)-1))
    return integ(f, 0, th)/integ(f, 0, math.pi)

b1 = 3.399810242
vals = [p(6*b1, t) for t in (0.05, 0.2, 0.6)]
P('E1 values', vals)
ok1 = [f'{v:.3g}' for v in vals] == ['0.00307', '0.156', '0.935']
P('E1', 'PASS' if ok1 else 'FAIL', [f'{v:.3g}' for v in vals])
b2 = 3.276133577
vals2 = [p(6*b2, t) for t in (0.1, 0.2, 1/b2, 2/b2)]
P('E2 values', vals2)
ok2 = [f'{v:.2f}' for v in vals2] == ['0.02', '0.15', '0.39', '0.93']
P('E2', 'PASS' if ok2 else 'FAIL', [f'{v:.2f}' for v in vals2])

C0 = math.pi**2*math.sqrt(math.e)/4
tot = qual = 0; e3 = True; e4 = True; worst4 = 0.0
for N in (6, 8, 16, 64, 1024):
    for beta in (0, 0.5, 3.276133577, 10):
        for c in (0.1, 1, 3):
            tot += 1
            th = c*(1+6*beta)**-0.5*N**(-4/3)
            if th > math.pi: continue
            qual += 1
            ng = 3*(N/2)**3
            lhs = ng*C0*(1+6*beta)**1.5*th**3
            rhs = 3*math.pi**2*math.sqrt(math.e)/32*c**3/N
            if abs(lhs-rhs)/rhs > 1e-13: e3 = False; P('  E3 fail', N, beta, c, lhs, rhs)
            pv = ng*p(6*beta, th)
            worst4 = max(worst4, pv/rhs)
            if pv > rhs: e4 = False; P('  E4 fail', N, beta, c, pv, rhs)
P(f'E3 instances {tot} qualifying {qual}', 'PASS' if e3 else 'FAIL')
P(f'E4 largest n_g p / claimed bound = {worst4:.6f}', 'PASS' if e4 else 'FAIL')
P('  constant 3 pi^2 sqrt(e)/32 =', 3*math.pi**2*math.sqrt(math.e)/32)

worst = 0.0; e5 = True
for k in (0, 0.1, 1, 5, 19.66, 20.4, 60, 300):
    for i in range(1, 401):
        th = math.pi*i/400
        env = C0*(1+k)**1.5*th**3
        r = p(k, th)/env
        if r > worst: worst = r; arg = (k, th)
        if r > 1: e5 = False
P(f'E5 largest p/envelope = {worst:.6f} at (k,theta)={arg}', 'PASS' if e5 else 'FAIL')

# E6 cap centred at c (angle delta from v): 2-d quadrature.
# u = cos(r) c + sin(r)(cos(s) e + sin(s) w), e in plane of (c,v), w orthogonal S^1 direction;
# measure (2/pi) sin^2 r dr * (1/2) sin s ds ; u.v = cos r cos delta + sin r cos s sin delta
e6 = True; worst6 = -1.0
for k in (0.5, 5, 20):
    Z = integ(lambda r: (2/math.pi)*np.sin(r)**2*np.exp(k*np.cos(r)), 0, math.pi)
    for th in (0.2, 0.8, 2.0):
        for dl in (0.3, 1.0, 2.0, math.pi):
            def inner(r):
                res = np.zeros_like(r)
                for j, rr in enumerate(r):
                    g = lambda s: 0.5*np.sin(s)*np.exp(k*(math.cos(rr)*math.cos(dl)+math.sin(rr)*np.cos(s)*math.sin(dl)))
                    res[j] = integ(g, 0, math.pi, pieces=2)
                return (2/math.pi)*np.sin(r)**2*res
            pc = integ(inner, 0, th, pieces=2)/Z
            pk = p(k, th)
            worst6 = max(worst6, pc-pk)
            if pc > pk+1e-9: e6 = False; P('  E6 fail', k, th, dl, pc, pk)
mono = True
for th in (0.1, 0.5, 1, 2):
    seq = [p(0.5*i, th) for i in range(81)]
    mono = mono and all(seq[i+1] >= seq[i]-1e-13 for i in range(80))
P(f'E6 largest (off-centre cap - centred cap) = {worst6:.3e}; monotone in k: {mono}', 'PASS' if e6 and mono else 'FAIL')
for b in (b1, b2):
    P(f'E7 beta={b}: (6beta)^-1/2={(6*b)**-0.5:.4f} p there={p(6*b,(6*b)**-0.5):.4f}; p at half that={p(6*b,0.5*(6*b)**-0.5):.4f}')
out.close()
