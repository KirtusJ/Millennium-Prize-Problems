"""A1 Monte Carlo on an 8^4 periodic SU(2) Wilson lattice (heat bath, Kennedy-Pendleton), cold start.
Usage: python3 mc.py BETA NTHERM NMEAS SEED OUTFILE

Measured per sweep (after thermalization):
 - plaquette average <(1/2)Tr U_p> over all 6 orientations;
 - for every axis-1 line, every a, d=k-j in {1,2,3}: D_j.D_k with root on the plane s=a+j+k+1
   (straight transport), D = sum of the two scaled transported Im parts (sqrt(beta) Im, 3 colours);
 - |D|^2 (diagonal), and the mean square of the line average of L=2,4,8 consecutive faces
   transported to a common root on the line (root at the first face).
PREDICATES (fixed before first run):
 M0 (control): |<P> - (1 - 3/(4 beta))| <= 1/beta^2 + 4 sigma. Tolerance source: the next perturbative term
    of the SU(2) plaquette is c2/beta^2 with |c2| < 1 (literature value ~0.15); 1/beta^2 is a generous bound;
    sigma from binning (10 bins).  Finite-volume corrections O(1/(beta N^4)) are below this.
 M1 (for d=1,2,3): mean D_j.D_k <= +3 sigma (not significantly positive), as reflection positivity predicts.
 M2: L * MS(L) <= 3 * E|D|^2/2 ... measured; predicate M2: MS(L) <= (1/(2L)) E|D|^2 + 3 sigma (the target's
     inequality (2) step  L^-2 sum_j E|D_j|^2 = E|D|^2/(2L)), for L = 2, 4, 8.  (On the 8-torus L=8 is a full line.)
 Free comparison (measured only): 3 x one-colour torus value, printed by free_torus.py.
"""
import sys, numpy as np
from su2lib import *

beta = float(sys.argv[1]); NT = int(sys.argv[2]); NM = int(sys.argv[3]); seed = int(sys.argv[4]); out = sys.argv[5]
N = 8
rng = np.random.default_rng(seed)
U = np.zeros((4, N, N, N, N, 4)); U[..., 0] = 1.0
X = np.indices((N, N, N, N)).sum(0) % 2

def staple(U, mu):
    S = np.zeros(U.shape[1:])
    for nu in range(4):
        if nu == mu: continue
        # forward: U_nu(x+mu) U_mu(x+nu)^-1 U_nu(x)^-1
        S += qmul(qmul(shift(U[nu], mu, 1), qinv(shift(U[mu], nu, 1))), qinv(U[nu]))
        # backward: U_nu(x+mu-nu)^-1 U_mu(x-nu)^-1 U_nu(x-nu)
        Unm = shift(U[nu], nu, -1)
        S += qmul(qmul(qinv(shift(Unm, mu, 1)), qinv(shift(U[mu], nu, -1))), Unm)
    return S

def kp(alpha):
    x0 = np.empty(alpha.shape); todo = np.ones(alpha.shape, bool)
    while todo.any():
        al = alpha[todo]
        r1, r2, r3, r4 = (1 - rng.random((4,) + al.shape))
        lam2 = -(np.log(r1) + np.cos(2*np.pi*r2)**2*np.log(r3))/(2*al)
        ok = r4**2 <= 1 - lam2
        idx = np.flatnonzero(todo)
        x0.flat[idx[ok]] = 1 - 2*lam2[ok]
        todo.flat[idx[ok]] = False
    return x0

def sweep(U):
    for mu in range(4):
        for par in (0, 1):
            S = staple(U, mu)  # weight exp(beta Re(U S)), Re = a0 of quaternion
            m = X == par
            V = S[m]; k = np.linalg.norm(V, axis=-1); Vt = V/k[:, None]
            x0 = kp(beta*k)
            v = rng.normal(size=(len(x0), 3)); v /= np.linalg.norm(v, axis=1)[:, None]
            Xq = np.concatenate([x0[:, None], np.sqrt(np.clip(1-x0**2, 0, None))[:, None]*v], 1)
            # U S has distribution of Xq up to normalisation: U = Xq Vt^-1 with Re(U Vt) = x0
            Um = U[mu]; Um[m] = qmul(Xq, qinv(Vt))
            Um[m] /= np.linalg.norm(Um[m], axis=-1, keepdims=True)

def measure(U):
    pl = np.mean([plaq(U, m, n)[..., 0].mean() for m in range(4) for n in range(m+1, 4)])
    cross = {1: [], 2: [], 3: []}; diag = []
    for a in range(N):
        for d in (1, 2, 3):
            s = a + d + 1
            offs = [a-s, a+1-s, a+2*d-s, a+2*d+1-s]
            f = rooted_faces(U, s % N, offs, beta)
            Dj = f[offs[0]]+f[offs[1]]; Dk = f[offs[2]]+f[offs[3]]
            cross[d].append((Dj*Dk).sum(-1).mean())
            if d == 1: diag.append((Dj*Dj).sum(-1).mean())
    ms = {}
    for L in (2, 4, 8):
        vals = []
        for a in range(N):
            f = rooted_faces(U, a, list(range(L)), beta)
            A = sum(f[o] for o in range(L))/L
            vals.append((A*A).sum(-1).mean())
        ms[L] = np.mean(vals)
    return pl, [np.mean(cross[d]) for d in (1, 2, 3)], np.mean(diag), [ms[L] for L in (2, 4, 8)]

for i in range(NT): sweep(U)
rows = []
for i in range(NM):
    sweep(U); pl, cr, dg, ms = measure(U); rows.append([pl] + cr + [dg] + ms)
rows = np.array(rows)
nb = 10; B = rows[:(len(rows)//nb)*nb].reshape(nb, -1, rows.shape[1]).mean(1)
mean = rows.mean(0); err = B.std(0, ddof=1)/np.sqrt(nb)
names = ["plaq", "DjDk_d1", "DjDk_d2", "DjDk_d3", "Dsq", "MS_L2", "MS_L4", "MS_L8"]
lines = [f"beta {beta} N {N} therm {NT} meas {NM} seed {seed}"]
for nm, m_, e_ in zip(names, mean, err): lines.append(f"{nm} {m_:.6f} +- {e_:.6f}")
fails = 0
pt = 1 - 3/(4*beta); tol = 1/beta**2 + 4*err[0]
ok = abs(mean[0]-pt) <= tol; fails += not ok
lines.append(f"M0 plaquette vs 1-3/(4beta)={pt:.6f}: diff {mean[0]-pt:+.6f} tol {tol:.6f} {'MET' if ok else 'FAILED'}")
for i, d in enumerate((1, 2, 3)):
    ok = mean[1+i] <= 3*err[1+i]; fails += not ok
    lines.append(f"M1 d={d}: {mean[1+i]:+.6f} <= 3sigma={3*err[1+i]:.6f} {'MET' if ok else 'FAILED'}")
for i, L in enumerate((2, 4, 8)):
    bound = mean[4]/(2*L); ok = mean[5+i] <= bound + 3*err[5+i]; fails += not ok
    lines.append(f"M2 L={L}: MS {mean[5+i]:.6f} <= E|D|^2/(2L)={bound:.6f}(+3s) {'MET' if ok else 'FAILED'}; L*MS={L*mean[5+i]:.4f}")
with open(out, "x") as fh: fh.write("\n".join(lines)+"\n")
print("\n".join(lines))
sys.exit(1 if fails else 0)
