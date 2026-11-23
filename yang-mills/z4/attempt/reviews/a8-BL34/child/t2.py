"""T2. usage: python3 t2.py BETA. For M in {1,3}: 20 shell data sets (seed 1000+int(beta)*10+M), each |psi|=M (sum over 48 shell links
of |sqrt(beta) x|^2 = M^2, Gaussian direction in R^144). Minimise r(phi)=(beta*S+7|psi|^2)/|phi|^2 over 7 links in the chart (|x_l|<pi, enforced
by x=pi*tanh(|y|)*y/|y|), 30 starts/sample: 10 near (|phi| ~ 0.3..3), 10 mid (|x_l| angle ~U(0,1.5)), 10 far (|x_l| ~ U(1.5,pi)), plus
own BFGS (scipy is NOT installed here; deviation from the task text) with central-difference gradient, 120 iterations max.
Predicates (fixed before first run):
 P2  : every one of the 120 (beta,M,sample) cases has c_eff_sample > 0.  (Note: trivially true since numerator >= 7M^2 > 0; reported honestly.)
 P2b : (informative) every case has c_eff_sample >= lambda/16 = 0.0523576 (lambda from t1).
 P3  : measured only: c_eff(beta,M)=min over samples vs lambda/16.
Hypothesis check (rule 4): number of cases qualifying for P2 / P2b is reported. Optimiser tolerance: gradient-norm 1e-7 relative or 120 its;
a minimiser is local, so c_eff is an UPPER bound of the true inf (min of found values)."""
import numpy as np, sys
from su2lib import *
beta = float(sys.argv[1]); LAM16 = 0.8377223398316209/16
def make_f(V1, V2, psi2, beta):
    def r_of_y(Y):  # Y: (B,21)
        y = Y.reshape(Y.shape[0], 7, 3); n = np.linalg.norm(y, axis=-1, keepdims=True)+1e-300
        x = np.pi*np.tanh(n)*y/n
        q = np.concatenate([np.tile(np.array([1., 0, 0, 0]), (Y.shape[0], 1, 1)), qexp(x)], 1)
        S = S_action(q, V1, V2)
        phi2 = beta*(x**2).sum((1, 2))
        return (beta*S + 7*psi2)/phi2
    return r_of_y
def bfgs(f, y0, iters=120):
    n = len(y0); y = y0.copy(); H = np.eye(n)
    def val_grad(y):
        h = 1e-6; E = np.eye(n)*h
        P = np.concatenate([y[None]+E, y[None]-E, y[None]], 0)
        v = f(P); return v[-1], (v[:n]-v[n:2*n])/(2*h)
    fv, g = val_grad(y)
    for it in range(iters):
        if np.linalg.norm(g) < 1e-7*max(1, abs(fv)): break
        d = -H@g
        if d@g >= 0: H = np.eye(n); d = -g
        t = 1.0; ok = False
        for _ in range(30):
            yn = y+t*d; fn = f(yn[None])[0]
            if fn <= fv + 1e-4*t*(g@d): ok = True; break
            t *= 0.5
        if not ok: break
        fn, gn = val_grad(yn); s = yn-y; yy = gn-g; sy = s@yy
        if sy > 1e-12:
            rho = 1/sy; I = np.eye(n)
            H = (I-rho*np.outer(s, yy))@H@(I-rho*np.outer(yy, s))+rho*np.outer(s, s)
        y, fv, g = yn, fn, gn
    return fv, y
rows = []
for M in (1, 3):
    rng = np.random.default_rng(1000+int(beta)*10+M)
    for smp in range(20):
        g = rng.normal(size=(48, 3)); psi = M*g/np.linalg.norm(g); x = psi/np.sqrt(beta)
        q = qexp(x); V1 = q[:24]; V2 = q[24:]
        f = make_f(V1, V2, M**2, beta)
        best = np.inf
        for k in range(30):
            if k < 10:  # near: small phi
                y0 = rng.normal(size=21)*rng.uniform(0.3, 3)/np.sqrt(beta)/np.sqrt(21)/np.pi
            elif k < 20:
                v = rng.normal(size=(7, 3)); v *= (rng.uniform(0, 1.5, (7, 1))/np.linalg.norm(v, axis=1, keepdims=True)); y0 = np.arctanh(np.minimum(np.linalg.norm(v, axis=1)/np.pi, 0.999))[:, None]*v/np.linalg.norm(v, axis=1, keepdims=True); y0 = y0.ravel()
            else:
                v = rng.normal(size=(7, 3)); nv = rng.uniform(1.5, np.pi*0.99, (7, 1)); y0 = (np.arctanh(nv/np.pi)*v/np.linalg.norm(v, axis=1, keepdims=True)).ravel()
            fv, _ = bfgs(f, y0)
            if np.isfinite(fv): best = min(best, fv)
        rows.append((beta, M, smp, best))
        with open("out/t2_progress.log", "a") as lg: lg.write(f"{beta} {M} {smp} {best}\n")
with open(f"out/t2_beta{int(beta)}.txt", "x") as f:
    f.write("beta M sample c_eff_sample\n")
    for r in rows: f.write(f"{r[0]:g} {r[1]} {r[2]} {r[3]:.8g}\n")
for M in (1, 3):
    c = np.array([r[3] for r in rows if r[1] == M])
    print(f"beta={beta:g} M={M}: c_eff(min)={c.min():.6g} median={np.median(c):.6g} n>0: {(c>0).sum()}/20  n>=lam/16: {(c>=LAM16).sum()}/20  lam/16={LAM16:.6g}")
