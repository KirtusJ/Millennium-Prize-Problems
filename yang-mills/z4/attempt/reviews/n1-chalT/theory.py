"""theory.py -- constants of the corrected prediction (double precision, composite Simpson after a=u^2 substitution).
Predicates (fixed before first run):
 T1 c = int_0^pi sqrt(2 arccosh(1+2 sin^2 a)) da agrees with 4.6054132 to 1e-6 (tolerance: 7 printed digits of brief).
 T2 c_cont = int_0^pi sqrt(4 sin a) da agrees with 4.7925610 to 1e-6.
 T3 d = int_0^pi da / sqrt(2 eps(a)) is finite (integrand ~ 1/(2 sqrt a) at ends); Simpson with n=2000 and n=4000 agree to 1e-8.
 T4 exact discrete oscillator: Z_n = prod_k (2cosh e - 2cos(2 pi k/n))^{-1/2} equals sum_m exp(-(m+1/2) n e) for n=7, w/beta=2 (rel 1e-12, rounding).
"""
import math, sys
def eps(a): return math.acosh(1+2*math.sin(a)**2)
def simpson_sym(f, n):
    # int_0^pi f = 2 int_0^{pi/2} f ; substitute a=u^2, da=2u du
    U = math.sqrt(math.pi/2); h = U/n; s = 0
    for i in range(n+1):
        u = i*h; w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w*f(u*u)*2*u if u > 0 else (w*f(1e-300)*0 if False else 0) + (w*(2*u*f(u*u)) if u>0 else 0)
    return 2*s*h/3
def fd(a): return 1/math.sqrt(2*eps(a)) if a > 0 else 0
# 2u/sqrt(2 eps(u^2)) -> 2u/sqrt(4u^2)=1 at u=0: handle limit
def gd(u): return 1.0 if u == 0 else 2*u/math.sqrt(2*eps(u*u))
def simpson_u(g, n):
    U = math.sqrt(math.pi/2); h = U/n
    return 2*h/3*sum((1 if i in (0, n) else (4 if i % 2 else 2))*g(i*h) for i in range(n+1))
c = simpson_u(lambda u: 2*u*math.sqrt(2*eps(u*u)), 4000)
cc = simpson_u(lambda u: 2*u*math.sqrt(4*math.sin(u*u)), 4000)
d1 = simpson_u(gd, 2000); d2 = simpson_u(gd, 4000)
dc = simpson_u(lambda u: 1.0 if u == 0 else 2*u/math.sqrt(4*math.sin(u*u)), 4000)
e = math.acosh(1+2); n = 7
Z = 1.0
for k in range(n): Z *= (2*math.cosh(e)-2*math.cos(2*math.pi*k/n))**-0.5
Zs = sum(math.exp(-(m+.5)*n*e) for m in range(50))
P = {'T1': abs(c-4.6054132) < 1e-6, 'T2': abs(cc-4.7925610) < 1e-6, 'T3': abs(d1-d2) < 1e-8, 'T4': abs(Z/Zs-1) < 1e-12}
E0 = 3.3505330
out = dict(c=c, c_cont=cc, d=d2, d_cont=dc, E0=E0, coef_beta16=-E0*d2, Z=Z, Zsum=Zs, predicates=P)
with open('results/theory.txt', 'x') as fh: fh.write(repr(out)+'\n')
print(out); sys.exit(0 if all(P.values()) else 1)
