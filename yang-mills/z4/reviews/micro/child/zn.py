"""Z_n plaquette gap check. Predicates (stated before first run):
P1 control.txt == '0.272341' (-ln tanh 1).
P2 for n in {3,4,5,6}, N=16: |M/A - 1| < 1e-6 with k=2 (k=2 correct; k=1 would give M/A=2).
P3 for N in {4,8,16} and n in {3,4,5,6}: M/A-1 within 5% (relative) of the analytic
   leading correction: n=4: +x^2/3 ; n!=4: -(1+cos(2pi/n)) x, x=exp(-N^2 d).
   (Derivation: m=2dx-2d(1+c)x^2+..., n=4 is exact: m=ln((1+x)/(1-x)).)
P4 for n=6 the shrink factor of |M/A-1| from N=4 to N=8 exceeds 1e6.
Results written to a new file result_<n>.txt; never overwritten (exits if exists).
"""
import os, sys
from mpmath import mp, mpf, exp, cos, log, pi, nstr
mp.dps = 320
out = 'result.txt'
if os.path.exists(out): sys.exit('result.txt exists; refusing to overwrite')
def M(n, N):
    b = mpf(N)**2
    w = [exp(b*(cos(2*pi*j/n)-1)) for j in range(n)]
    lam = lambda k: sum(w[j]*cos(2*pi*j*k/n) for j in range(n))
    return b*(-log(lam(1)/lam(0)))
def A(n, N, k=2):
    d = 1-cos(2*pi/n); return mpf(N)**2*k*d*exp(-mpf(N)**2*d)
def pred(n, N):
    d = 1-cos(2*pi/n); x = exp(-mpf(N)**2*d)
    return x**2/3 if n == 4 else -(1+cos(2*pi/n))*x
L = []; res = {}
ctl = open('control.txt').read().strip()
res['P1'] = ctl == '0.272341'
rel = {}
for n in (3, 4, 5, 6):
    for N in (2, 4, 8, 16):
        m = M(n, N); r = m/A(n, N); e = r-1; rel[n, N] = e
        L.append(f"n={n} N={N} M={nstr(m,15)} M/A={nstr(r,15)} M/A-1={nstr(e,8)} pred={nstr(pred(n,N),8)} ratio={nstr(e/pred(n,N),8)}")
res['P2'] = all(abs(rel[n, 16]) < mpf(10)**-6 for n in (3, 4, 5, 6))
res['P3'] = all(abs(rel[n, N]/pred(n, N)-1) < mpf('0.05') for n in (3, 4, 5, 6) for N in (4, 8, 16))
sh = abs(rel[6, 4]/rel[6, 8]); L.append('shrink n=6 N4->8: '+nstr(sh, 6))
res['P4'] = sh > 1e6
for n in (4, 6):
    L.append(f"n={n} N=2->4 shrink {nstr(abs(rel[n,2]/rel[n,4]),6)}; 4->8 {nstr(abs(rel[n,4]/rel[n,8]),6)}; 8->16 {nstr(abs(rel[n,8]/rel[n,16]),6)}")
L += [f"{k}: {'PASS' if v else 'FAIL'}" for k, v in res.items()]
open(out, 'w').write('\n'.join(L)+'\n'); print('\n'.join(L))
sys.exit(0 if all(res.values()) else 1)
