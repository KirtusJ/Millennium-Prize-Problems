"""g2-fid own recomputation of the scalar claims of main.tex (independent of the child).

Predicates fixed before the first run (tolerances and their source in brackets):
 Q1  C := pi^2 sqrt(e)/4 equals (theta^3/3) / ((4/pi^2) e^{-1/2} (1/3)(1+k)^{-3/2}) / ((1+k)^{3/2} theta^3)
     [float rel 1e-14: double rounding of a few operations]
 Q2  for all (k,theta) on the grid k in {0,0.1,...} up to 400, theta in (0,pi]: p_k(theta) <= min(1, C(1+k)^{3/2} theta^3)
     [slack 1e-12: composite Gauss-Legendre with 400 nodes per panel, error far below]; report qualifying count.
 Q3  at beta=3.399810242, k=6beta: p_k(0.05), p_k(0.2), p_k(0.6) round to 0.00307, 0.156, 0.935
     [half unit of last stated digit, as printed in main.tex:371].
 Q4  M*C*(1+6b)^{3/2}*theta^3 = (3 pi^2 sqrt(e)/32) c^3/N for M=3(N/2)^3, theta=c(1+6b)^{-1/2}N^{-4/3}
     [rel 1e-13, float].
 Q5  exact power series (Fractions) of R=I2/I1: R = k/4 - k^3/96 + ..., p-q = -k^2/48 + O(k^4),
     p' = -k/16 + O(k^3), w' = k/2 + O(k^3)   [exact].
 Q6  identities at a zero, checked at 200 random rational points (fixed seed 20261124) exactly:
     (a) p=q  => -(2R+3/k)p + 3R/k^2 = -2Rq;
     (b) p'=0 => p'' (general formula from differentiating) = -2p^2 + 6(p-q)/k^2;
     (c) w'=0 => w'' = p(4-2w) with w=k^2 p; and w = 3R/(2R+1/k) < 3/2 for R>0.
     Also the ODE p = 1 - 3R/k - R^2 against termwise series derivative at k=0.5,2,6 [rel 1e-40, 33+ exact terms].
 Q7  0.036885895 < R'(6) < 0.036885896 by exact rational enclosure: 33 series terms of I1(6), I2(6), geometric tail
     bound; enclosure propagated by interval arithmetic in Fractions [exact].
 M1  (measured only) R'(6)/beta^2 at beta=3.276133577, floor 1/(165888 beta^2), and the ratios to measured J
     values J1=0.0077296, J4=0.0029112 (records/e2-repair/report.md:59) -- for Remark r:haar.
 M2  (measured only) e2-cross E_f/E_c bound and variance ratio arithmetic: 1/0.0034.
Output: results_<tag>.txt opened with mode 'x'.
"""
import math, random, sys
from fractions import Fraction as F

tag = sys.argv[1]
out = open(f"results_{tag}.txt", "x")
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.write(s + "\n")
met = failed = 0
def pred(name, ok, info=""):
    global met, failed
    if ok: met += 1
    else: failed += 1
    log(f"{name}: {'MET' if ok else 'FAILED'} {info}")

# Gauss-Legendre nodes (numpy-free): use numpy if available
import numpy as np
xg, wg = np.polynomial.legendre.leggauss(400)
def integ(f, a, b, panels=8):
    s = 0.0
    h = (b - a) / panels
    for i in range(panels):
        lo = a + i*h; hi = lo + h
        x = 0.5*(hi-lo)*xg + 0.5*(hi+lo)
        s += 0.5*(hi-lo)*np.sum(wg*f(x))
    return s
def pk(k, th):
    f = lambda r: np.sin(r)**2*np.exp(k*(np.cos(r)-1))
    return integ(f, 0, th) / integ(f, 0, math.pi)

C = math.pi**2*math.sqrt(math.e)/4
log("C = pi^2 sqrt(e)/4 =", repr(C))
# Q1
worst = 0
for k in [0, 0.3, 1, 7, 20.4, 100]:
    for th in [0.01, 0.3, 1.0]:
        ratio = (th**3/3) / ((4/math.pi**2)*math.exp(-0.5)*(1/3)*(1+k)**-1.5)
        worst = max(worst, abs(ratio/((1+k)**1.5*th**3)/C - 1))
pred("Q1", worst < 1e-14, f"max rel dev {worst:.2e}")
# Q2
cases = 0; qual = 0; viol = 0; mx = 0
for k in list(np.arange(0, 10, 0.5)) + [15, 20.398861452, 30, 50, 100, 200, 400]:
    for th in list(np.linspace(0.001, math.pi, 60)) + [(1+k)**-0.5]:
        cases += 1
        if 0 <= th <= math.pi: qual += 1
        else: continue
        p = pk(k, th); b = min(1.0, C*(1+k)**1.5*th**3)
        mx = max(mx, p/b)
        if p > b + 1e-12: viol += 1
pred("Q2", viol == 0, f"cases {cases}, qualifying {qual}, violations {viol}, max p/bound {mx:.6f}")
# Q3
beta = 3.399810242; k = 6*beta
vals = [pk(k, t) for t in (0.05, 0.2, 0.6)]
log("Q3 values:", ["%.9f" % v for v in vals])
pred("Q3", abs(vals[0]-0.00307) <= 5e-6 and abs(vals[1]-0.156) <= 5e-4 and abs(vals[2]-0.935) <= 5e-4)
log("   cubic envelope at these theta:", ["%.4g" % (C*(1+k)**1.5*t**3) for t in (0.05, 0.2, 0.6)])
# Q4
w = 0
for N in (6, 8, 16, 64, 1024):
    for c in (0.1, 0.5, 1.0):
        for b in (0, 1, 3.4):
            M = 3*(N/2)**3; th = c*(1+6*b)**-0.5*N**(-4/3)
            lhs = M*C*(1+6*b)**1.5*th**3; rhs = 3*math.pi**2*math.sqrt(math.e)/32*c**3/N
            w = max(w, abs(lhs/rhs-1))
pred("Q4", w < 1e-13, f"max rel dev {w:.1e}; 3pi^2sqrt(e)/32 = {3*math.pi**2*math.sqrt(math.e)/32:.9f}")

# ---- exact series
NT = 40
def I_series(nu):  # coefficients of k^(nu+2m): 1/(m!(m+nu)! 2^(2m+nu))
    return {nu+2*m: F(1, math.factorial(m)*math.factorial(m+nu)*2**(2*m+nu)) for m in range(NT)}
def poly_mul(a, b, deg):
    c = {}
    for i, x in a.items():
        for j, y in b.items():
            if i+j <= deg: c[i+j] = c.get(i+j, 0) + x*y
    return c
I1 = I_series(1); I2 = I_series(2)
# R = I2/I1 = (I2/k)/(I1/k); series division
D = 30
a = {i-1: v for i, v in I2.items() if i-1 <= D}
bq = {i-1: v for i, v in I1.items() if i-1 <= D}
Rs = {}
for n in range(D+1):
    s = a.get(n, 0) - sum(Rs.get(j, 0)*bq.get(n-j, 0) for j in range(n))
    Rs[n] = s / bq[0]
deriv = lambda s: {i-1: i*v for i, v in s.items() if i >= 1}
p = deriv(Rs); q = {i-1: v for i, v in Rs.items() if i >= 1}
pmq = {i: p.get(i, 0) - q.get(i, 0) for i in range(8)}
pp = deriv(p)
w_ = {i+2: v for i, v in p.items()}; wp = deriv(w_)
log("R series:", [(i, str(Rs[i])) for i in range(6) if Rs[i] != 0])
log("p-q:", [(i, str(v)) for i, v in pmq.items() if v != 0][:3])
log("p':", [(i, str(pp[i])) for i in range(5) if pp.get(i, 0) != 0][:2])
log("w':", [(i, str(wp[i])) for i in range(5) if wp.get(i, 0) != 0][:2])
pred("Q5", Rs[1] == F(1, 4) and Rs[3] == F(-1, 96) and pmq[0] == 0 and pmq[1] == 0 and pmq[2] == F(-1, 48)
     and pp.get(0, 0) == 0 and pp[1] == F(-1, 16) and pp.get(2, 0) == 0 and wp.get(0, 0) == 0 and wp[1] == F(1, 2) and wp.get(2, 0) == 0)

# Q6 exact random identities
rnd = random.Random(20261124); ok = True
for _ in range(200):
    kk = F(rnd.randint(1, 500), rnd.randint(1, 100)); R = F(rnd.randint(1, 500), rnd.randint(1, 600))
    # (a)
    pa = R/kk; qa = R/kk
    ok &= (-(2*R+3/kk)*pa + 3*R/kk**2 == -2*R*qa)
    # (b) general p'' = -(2R'-3/k^2)p - (2R+3/k)p' + 3R'/k^2 - 6R/k^3 with R'=p, p'=0
    pb = F(rnd.randint(1, 500), rnd.randint(1, 600)); qb = R/kk
    ok &= (-(2*pb-3/kk**2)*pb - (2*R+3/kk)*0 + 3*pb/kk**2 - 6*R/kk**3 == -2*pb**2 + 6*(pb-qb)/kk**2)
    # (c) w'=0: w = 3R/(2R+1/k); p = w/k^2; w'' = 3p - (2p-1/k^2)w
    wc = 3*R/(2*R+1/kk); pc = wc/kk**2
    ok &= (3*pc - (2*pc-1/kk**2)*wc == pc*(4-2*wc)) and wc < F(3, 2)
# check the p' formula itself as a derivative identity: p = 1-3R/k-R^2 => p' = -3R'/k+3R/k^2-2RR' = -(2R+3/k)p+3R/k^2 (R'=p)
for _ in range(50):
    kk = F(rnd.randint(1, 500), rnd.randint(1, 100)); R = F(rnd.randint(1, 500), rnd.randint(1, 600)); pr = F(rnd.randint(1, 99), 100)
    ok &= (-3*pr/kk + 3*R/kk**2 - 2*R*pr == -(2*R+3/kk)*pr + 3*R/kk**2)
    # q' = R'/k - R/k^2 = (p-q)/k ; w' = 2kp + k^2 p' = 3R-(2R+1/k)w
    ok &= (pr/kk - R/kk**2 == (pr - R/kk)/kk)
    ppr = -(2*R+3/kk)*pr + 3*R/kk**2
    ok &= (2*kk*pr + kk**2*ppr == 3*R - (2*R+1/kk)*kk**2*pr)
def ev(series, x, n):  # evaluate Fraction power series at rational x
    return sum(v*x**i for i, v in series.items() if i <= n)
worst = F(0)
for xs in (F(1, 2), F(2), F(6)):
    i1 = ev(I1, xs, 200); i2 = ev(I2, xs, 200)
    i1p = ev(deriv(I1), xs, 200); i2p = ev(deriv(I2), xs, 200)
    Rv = i2/i1; Rp = (i2p*i1 - i2*i1p)/i1**2
    worst = max(worst, abs(Rp - (1 - 3*Rv/xs - Rv**2))/Rp)
pred("Q6", ok and worst < F(1, 10**40), f"random exact identities all hold: {ok}; ODE rel dev {float(worst):.1e}")

# Q7 rational enclosure of R'(6) = 1 - 3R/6 - R^2, R = I2(6)/I1(6), 33 terms + geometric tail
x = F(6); nterm = 33
def enclose(nu):
    t = [F(1, math.factorial(m)*math.factorial(m+nu))*(x/2)**(2*m+nu) for m in range(nterm+1)]
    s = sum(t[:nterm])
    r = (x/2)**2 / (nterm*(nterm+nu))  # ratio t_{m+1}/t_m for m>=nterm-... bound: t_{m+1}/t_m = (x/2)^2/((m+1)(m+1+nu)) <= r for m >= nterm-1
    tail = t[nterm] / (1 - r)
    return s, s + tail  # all terms positive
l1, u1 = enclose(1); l2, u2 = enclose(2)
Rlo, Rhi = l2/u1, u2/l1
# p(R) = 1 - R/2 - R^2 decreasing in R>0
plo = 1 - Rhi/2 - Rhi**2; phi = 1 - Rlo/2 - Rlo**2
log("R'(6) in [%.18f, %.18f], width %.1e" % (float(plo), float(phi), float(phi-plo)))
log("   decimal:", f"{plo.numerator*10**25//plo.denominator}")
pred("Q7", plo > F(36885895, 10**9) and phi < F(36885896, 10**9))

# M1
Rp6 = float(plo)
for b in (3.276133577, 3.399810242):
    fl = 1/(165888*b*b)
    log(f"M1 beta={b}: R'(6)/beta^2={Rp6/b**2:.6g}; J-floor 1/(165888 b^2)={fl:.6g}; "
        f"J1/(R'(6)/b^2)={0.0077296/(Rp6/b**2):.3g}, J4/(R'(6)/b^2)={0.0029112/(Rp6/b**2):.3g}; "
        f"J1/floor={0.0077296/fl:.3g}, J4/floor={0.0029112/fl:.3g}")
log(f"M2 1/0.0034 = {1/0.0034:.1f}; E-ratio 0.00407+2*0.00005 = {0.00407+2*0.00005:.5f}")
log(f"COUNTS met {met} failed {failed} measured-only 2")
out.close()
