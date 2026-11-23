"""mc4d.py -- challenger a5-chalB, attack A2(iv): 4D SU(2) Wilson Monte Carlo test of S3a.

Usage: python3 mc4d.py L beta n_therm n_meas seed outfile
Heat bath (Kennedy-Pendleton), checkerboard over (direction, site parity), periodic L^4,
cold start.  SU(2) as unit quaternions; (1/2)Tr U = a0.  O_p = beta (1 - (1/2)Tr U_p),
all 6 orientations, all sites, every sweep after thermalisation.

PREDICATES (fixed before the first run):
 M1 control: w = <1 - (1/2)Tr U_p> against leading order 3/(4 beta):
    |w beta/0.75 - 1| <= 0.5/beta + 4 sigma_rel.  Tolerance: the O(beta^-2) term of w is,
    from memory (NOT checked), about 0.15/beta^2, i.e. 0.2/beta relative; finite-volume
    zero-mode corrections are O(1/L^4); 0.5/beta gives margin. sigma from 20 bins.
 M2 C_emp := max_t P(O>t) e^{t/8} (t on grid 0..20 step 0.25, only t with >= 50 counts)
    satisfies C_emp <= 10.  Expectation (mine) from the Gaussian limit O = (1/4) chi^2_3:
    max_t P(chi2_3 > 4t) e^{t/8} ~ 1.
 M3 tail rate: least-squares slope s of log P(O>t) on t in [2, t*] (t* = last t with
    >= 100 counts) satisfies -s >= 1/8 (the builder's c).  Expectation ~ 2.
 M4 Gaussian tail at t = 2: |P(O>2)/P(chi2_3>8) - 1| <= 0.3.  Tolerance: O(1/beta)
    corrections at beta = 4 (~ 0.2/beta in the mean) and finite volume; 30%.
Measured only: connected ratio R(n) = Cov(O_p(x), O_p(x+n e_rho))/Var(O_p), rho not in p,
    n = 1, 2, averaged over the 12 (orientation, direction) pairs; free infinite-volume
    value c(1) = 0.019, c(2) = 5.0e-4 (free_G.py).
"""
import numpy as np, sys, json, time, math

def qmul(a, b):
    a0, av = a[..., 0], a[..., 1:]; b0, bv = b[..., 0], b[..., 1:]
    out = np.empty(np.broadcast(a, b).shape)
    out[..., 0] = a0*b0 - np.sum(av*bv, axis=-1)
    out[..., 1:] = a0[..., None]*bv + b0[..., None]*av - np.cross(av, bv)
    return out

def qdag(a):
    o = a.copy(); o[..., 1:] *= -1; return o

def sh(X, mu, s):  # X(x + s e_mu)
    return np.roll(X, -s, axis=mu)

def staple(U, mu):
    A = np.zeros(U.shape[1:])
    for nu in range(4):
        if nu == mu: continue
        A += qmul(qmul(sh(U[nu], mu, 1), qdag(sh(U[mu], nu, 1))), qdag(U[nu]))
        b = sh(U[nu], nu, -1)  # U_nu(x - nu)
        A += qmul(qmul(qdag(sh(b, mu, 1)), qdag(sh(U[mu], nu, -1))), b)
    return A

def kp_x0(alpha, rng):
    x0 = np.empty_like(alpha); todo = np.ones(alpha.shape, bool)
    while todo.any():
        idx = np.nonzero(todo)[0]; a = alpha[idx]
        r1, r2, r3, r4 = (1 - rng.random((4, idx.size)))
        lam2 = -(np.log(r1) + np.cos(2*np.pi*r2)**2*np.log(r3))/(2*a)
        ok = r4**2 <= 1 - lam2
        x0[idx[ok]] = 1 - 2*lam2[ok]; todo[idx[ok]] = False
    return x0

def heatbath(U, beta, rng, parity):
    for mu in range(4):
        for par in (0, 1):
            A = staple(U, mu)[parity == par]
            k = np.sqrt(np.sum(A*A, axis=-1)); V = A/k[:, None]
            x0 = kp_x0(beta*k, rng)
            v = rng.normal(size=(x0.size, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
            X = np.concatenate([x0[:, None], v*np.sqrt(np.maximum(0, 1-x0**2))[:, None]], 1)
            new = qmul(X, qdag(V))
            Um = U[mu]; Um[parity == par] = new

def plaq(U, mu, nu):
    return qmul(qmul(U[mu], sh(U[nu], mu, 1)), qmul(qdag(sh(U[mu], nu, 1)), qdag(U[nu])))[..., 0]

def main():
    L, beta, nth, nme, seed, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    rng = np.random.default_rng(seed)
    U = np.zeros((4, L, L, L, L, 4)); U[..., 0] = 1
    g = np.indices((L,)*4).sum(0) % 2
    tgrid = np.arange(0, 20.0001, 0.25); counts = np.zeros(tgrid.size); ntot = 0
    wbins = []; s1 = 0.0; s2 = 0.0; cross = {1: 0.0, 2: 0.0}; ncross = {1: 0, 2: 0}
    t0 = time.time()
    for it in range(nth + nme):
        heatbath(U, beta, rng, g)
        if it < nth: continue
        Os = []; wsum = 0.0
        for mu in range(4):
            for nu in range(mu+1, 4):
                O = beta*(1 - plaq(U, mu, nu)); Os.append(O)
                counts += (O.ravel()[:, None] > tgrid[None, :]).sum(0); ntot += O.size
                wsum += O.sum()
                s1 += O.sum(); s2 += (O*O).sum()
                for rho in range(4):
                    if rho in (mu, nu): continue
                    for n in (1, 2):
                        cross[n] += (O*sh(O, rho, n)).sum(); ncross[n] += O.size
        wbins.append(wsum/(6*L**4)/beta)
    mean = s1/ntot; var = s2/ntot - mean**2
    R = {n: (cross[n]/ncross[n] - mean**2)/var for n in (1, 2)}
    wb = np.array(wbins); nb = 20; bm = wb[:len(wb)//nb*nb].reshape(nb, -1).mean(1)
    w = wb.mean(); sig = bm.std(ddof=1)/math.sqrt(nb)
    P = counts/ntot
    def chi3_tail(x):  # P(chi^2_3 > x) = erfc(sqrt(x/2)) + sqrt(2x/pi) e^{-x/2}
        return math.erfc(math.sqrt(x/2)) + math.sqrt(2*x/math.pi)*math.exp(-x/2)
    ok = counts >= 50
    Cemp = float(np.max(P[ok]*np.exp(tgrid[ok]/8)))
    sel = (tgrid >= 2) & (counts >= 100)
    slope = float(np.polyfit(tgrid[sel], np.log(P[sel]), 1)[0])
    i2 = int(np.argmin(abs(tgrid-2)))
    ratio2 = P[i2]/chi3_tail(8.0)
    preds = {
        "M1": abs(w*beta/0.75 - 1) <= 0.5/beta + 4*sig*beta/0.75,
        "M2": Cemp <= 10,
        "M3": -slope >= 1/8,
        "M4": abs(ratio2 - 1) <= 0.3,
    }
    res = dict(L=L, beta=beta, n_therm=nth, n_meas=nme, seed=seed, w=w, w_sigma=sig,
               w_beta_over_075=w*beta/0.75, Cemp=Cemp, slope=slope, P_t2=float(P[i2]),
               P_t2_over_gauss=float(ratio2), R1=R[1], R2=R[2], var_O=var, mean_O=mean,
               tgrid=tgrid.tolist(), P=P.tolist(), counts=counts.tolist(),
               gauss=[chi3_tail(4*t) for t in tgrid],
               predicates={k: bool(v) for k, v in preds.items()}, seconds=time.time()-t0)
    with open(out, "x") as f: json.dump(res, f, indent=1)
    print(f"L={L} beta={beta} w*beta/0.75={w*beta/0.75:.4f}+-{sig*beta/0.75:.4f} Cemp={Cemp:.3f} "
          f"slope={slope:.3f} P(O>2)/gauss={ratio2:.3f} R1={R[1]:.4f} R2={R[2]:.4f} "
          f"meanO={mean:.4f} varO={var:.4f} t={time.time()-t0:.0f}s")
    print({k: ("MET" if v else "FAILED") for k, v in preds.items()})
    return 0 if all(preds.values()) else 1

if __name__ == "__main__":
    sys.exit(main())
