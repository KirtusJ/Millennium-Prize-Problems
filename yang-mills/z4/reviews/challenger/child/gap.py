"""Task (a): M(N) = -N^2 ln(w_{1/2}/w_0), beta = 4 N^2, by direct Haar quadrature (no Bessel).
w(U) = exp((beta/2) tr U) = exp(beta cos t);  Haar class density (2/pi) sin^2 t on [0,pi].
w_0 = int dens * w ;  w_{1/2} = (1/2) int dens * w * 2cos t.  Factor exp(beta) cancels in the
ratio, so integrate exp(beta (cos t - 1)) for stability.
Quadrature: mpmath.quad tanh-sinh, mp.dps = 50, interval split at t = k/sqrt(beta), k=1,2,4,8,16,32
(peak width ~ 1/sqrt(beta)). Tolerance source: (i) mpmath error estimate (error=True);
(ii) independent recompute with Gauss-Legendre (method='gauss-legendre') at mp.dps = 60;
the difference in M between the two is reported as the quadrature tolerance.
PREDICATES (exit 1 if any fails; all failures printed):
 P1  quadrature agreement: |M_TS - M_GL| < 1e-25 for every N.
 P2  claimed value: |M(64) - 0.375011444266| < 1e-12.
 P3  M(N) > 3/8 for N = 4,8,16,32,64.
 P4  successive remainder ratios r(N/2)/r(N) in [3.5, 4.5] for N = 8,16,32,64.
Results written to gap_results.txt (new suffixed name if it exists; never overwritten).
"""
import os, sys
from mpmath import mp, mpf, quad, sin, cos, exp, log, pi, sqrt, nstr

def ratio(beta, method):
    b = mpf(beta)
    pts = [mpf(0)] + [k/sqrt(b) for k in (1, 2, 4, 8, 16, 32) if k/sqrt(b) < pi] + [pi]
    f0 = lambda t: sin(t)**2*exp(b*(cos(t)-1))
    f1 = lambda t: sin(t)**2*exp(b*(cos(t)-1))*cos(t)
    (w0, e0) = quad(f0, pts, method=method, error=True)
    (w1, e1) = quad(f1, pts, method=method, error=True)
    return w1/w0, max(e0/w0, e1/w1)  # (1/2)*2cos -> cos; 2/pi cancels

out = []; fails = []
Ms = {}
for N in (4, 8, 16, 32, 64):
    mp.dps = 50
    r_ts, est = ratio(4*N*N, 'tanh-sinh')
    M_ts = -N*N*log(r_ts)
    mp.dps = 60
    r_gl, _ = ratio(4*N*N, 'gauss-legendre')
    M_gl = -N*N*log(r_gl)
    mp.dps = 50
    d = abs(M_ts - M_gl)
    Ms[N] = M_ts
    out.append("N=%d beta=%d  w1/2/w0=%s  M=%s  M-3/8=%s  |TS-GL|=%s  relerr_est=%s" % (
        N, 4*N*N, nstr(r_ts, 30), nstr(M_ts, 30), nstr(M_ts - mpf(3)/8, 15), nstr(d, 3), nstr(est, 3)))
    if not d < mpf('1e-25'): fails.append("P1 N=%d diff=%s" % (N, nstr(d, 3)))
    if not M_ts > mpf(3)/8: fails.append("P3 N=%d" % N)
if not abs(Ms[64] - mpf('0.375011444266')) < mpf('1e-12'):
    fails.append("P2 M(64)=%s" % nstr(Ms[64], 20))
Ns = [4, 8, 16, 32, 64]
for a, b in zip(Ns, Ns[1:]):
    q = (Ms[a] - mpf(3)/8)/(Ms[b] - mpf(3)/8)
    out.append("remainder ratio r(%d)/r(%d) = %s" % (a, b, nstr(q, 15)))
    if not (3.5 <= q <= 4.5): fails.append("P4 %d/%d q=%s" % (a, b, nstr(q, 6)))
out.append("FAILS: " + (", ".join(fails) if fails else "none"))
txt = "\n".join(out)
print(txt)
name = "gap_results.txt"; k = 1
while os.path.exists(name):
    name = "gap_results_%d.txt" % k; k += 1
open(name, "w").write(txt + "\n")
sys.exit(1 if fails else 0)
