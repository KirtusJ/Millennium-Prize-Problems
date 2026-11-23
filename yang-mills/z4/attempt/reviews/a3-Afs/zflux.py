"""zflux.py -- TEST (iii) of brief a3-Afs: finite-volume flux coupling z(L) = L * m_L
in 4D lattice gauge theory, SU(2) vs compact U(1), Wilson action, same beta.

Lattice L^3 x T periodic (L, T even, checkerboard updates). SU(2): weight exp((beta/2) Re Tr U_p),
heatbath (Creutz/Kennedy-Pendleton) + no overrelaxation. U(1): weight exp(beta cos theta_p),
Metropolis with 4 hits. Observable: spatial Polyakov loops winding in direction x,
p(t) = mean over (y,z) of Re (1/N)Tr prod_x U_x(x,y,z,t); C(t) = <p(t0) p(t0+t)> (t0-averaged).
For SU(2), <p> = 0 exactly by center symmetry on a finite lattice; for U(1) <p> = 0 by charge
conjugation-free argument (the U(1) global center rotation of x-links on one x-slice). So C is
already connected; no subtraction. m_L := m_eff(t=1) = arccosh((C(0)+C(2))/(2C(1))) and
m_eff(2) for comparison (finite-T cosh effective mass). z(L) = L * m_L. Errors: jackknife, 10 bins.

PREDICATES (fixed before the first run):
 C1 (code control, strong coupling) beta = 0.5: mean plaquette within 0.01 of the one-plaquette value
    a(beta) (SU(2): I2/I1; U(1): I1/I0). Tolerance source: 4D strong-coupling expansion, first
    correction is O(a^5) with coefficient of order 2(d-2)=4: 4*0.2425^5 = 0.0034 < 0.01.
 C2 (code control, weak coupling U(1)) beta = 2.3: 1 - <cos theta_p> within 25% of 1/(4 beta)
    (equipartition of the Gaussian photon, d=4: <theta_p^2> = 2/(d beta)). Tolerance: O(1/beta) relative
    anharmonic corrections, 1/2.3 ~ 0.4 times small coefficient; 25% chosen generously.
 P_A (SU(2) running) at beta = 2.3: z_SU2(L) strictly increasing over L = 2, 4, 6 by more than 2 sigma
    at each step.
 P_B (U(1) not running) at beta = 2.3: z_U1(6) - z_U1(4) < max(3 sigma, 0.2 z_U1(4)) and z_U1(6) < 1.
 P_C (discrimination) z_SU2(6) / z_U1(6) > 2.
 P_D (U(1) tree level) z_U1(L) for L = 4, 6 within a factor 2 of g^2/2 = 1/(2 beta) (zero-mode electric
    flux energy g^2/(2L) of the free photon). Tolerance: excited-state contamination at t=1 and
    compact corrections; factor 2 generous.
 Rule 4: for each (group, L) report whether C(2) > 3 sigma(C(2)) (the case "qualifies": m_eff(1) defined).
Seeds fixed: numpy default_rng(12345 + hash-free integer per run).
Usage: python3 zflux.py <outfile>   (outfile opened with mode "x")
"""
import sys, time, json
import numpy as np

def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3,
                     a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1,
                     a0*b3 + a1*b2 - a2*b1 + a3*b0], axis=-1)

def qconj(a):
    return a * np.array([1, -1, -1, -1])

class SU2:
    N = 2
    def __init__(s, shape, rng):
        s.U = np.zeros((4,) + shape + (4,)); s.U[..., 0] = 1.0; s.rng = rng
    def mul(s, a, b): return qmul(a, b)
    def dag(s, a): return qconj(a)
    def retr(s, a): return a[..., 0]          # (1/2) Re Tr
    def update(s, mu, mask, staple, beta):
        # staple A = sum of staples, weight exp((beta/2) Re Tr(U A)) ; A = k * V, V in SU(2) (quaternion sum)
        A = staple[mask]
        k = np.sqrt((A**2).sum(-1)); V = A / k[:, None]
        a = beta * k  # density of x0: sqrt(1-x0^2) exp(a x0)
        n = len(a); x0 = np.empty(n); todo = np.arange(n)
        while len(todo):
            aa = a[todo]
            r1, r2, r3, r4 = (s.rng.random(len(todo)) for _ in range(4))
            lam2 = -(np.log(1 - r1) + np.cos(2*np.pi*r2)**2 * np.log(1 - r3)) / (2*aa)
            ok = r4**2 <= 1 - lam2
            x0[todo[ok]] = 1 - 2*lam2[ok]; todo = todo[~ok]
        r = np.sqrt(np.maximum(1 - x0**2, 0))
        v = s.rng.normal(size=(n, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
        X = np.concatenate([x0[:, None], r[:, None]*v], axis=1)
        # U = X * V^dagger  (Tr(U A) = k Tr(X V^dag V))
        s.U[mu][mask] = qmul(X, qconj(V))

class U1:
    N = 1
    def __init__(s, shape, rng):
        s.U = np.zeros((4,) + shape + (2,)); s.U[..., 0] = 1.0; s.rng = rng
    def mul(s, a, b):
        return np.stack([a[..., 0]*b[..., 0] - a[..., 1]*b[..., 1], a[..., 0]*b[..., 1] + a[..., 1]*b[..., 0]], -1)
    def dag(s, a): return a * np.array([1, -1])
    def retr(s, a): return a[..., 0]
    def update(s, mu, mask, staple, beta):
        A = staple[mask]; U = s.U[mu][mask]
        for _ in range(4):
            d = s.rng.uniform(-1.2, 1.2, len(A))
            R = np.stack([np.cos(d), np.sin(d)], -1)
            Un = s.mul(R, U)
            dS = beta * ((Un[:, 0]*A[:, 0] - Un[:, 1]*A[:, 1]) - (U[:, 0]*A[:, 0] - U[:, 1]*A[:, 1]))
            acc = s.rng.random(len(A)) < np.exp(np.minimum(dS, 0))
            U[acc] = Un[acc]
        s.U[mu][mask] = U

def staple(g, mu):
    U = g.U; S = 0
    for nu in range(4):
        if nu == mu: continue
        Unu_xpmu = np.roll(U[nu], -1, axis=mu)
        Umu_xpnu = np.roll(U[mu], -1, axis=nu)
        S = S + g.mul(g.mul(Unu_xpmu, g.dag(Umu_xpnu)), g.dag(U[nu]))
        # backward: U_nu(x+mu-nu)^dag U_mu(x-nu)^dag U_nu(x-nu)
        a = np.roll(np.roll(U[nu], -1, axis=mu), 1, axis=nu)
        b = np.roll(U[mu], 1, axis=nu); c = np.roll(U[nu], 1, axis=nu)
        S = S + g.mul(g.mul(g.dag(a), g.dag(b)), c)
    return S  # U_mu(x) * S is the sum of plaquettes through the link; Re Tr(U S)

def masks(shape):
    idx = np.indices(shape)
    out = {}
    for mu in range(4):
        par = sum(idx[nu] for nu in range(4) if nu != mu) % 2
        out[mu] = [par == 0, par == 1]
    return out

def sweep(g, beta, M):
    for mu in range(4):
        for m in M[mu]:
            g.update(mu, m, staple(g, mu), beta)

def plaq(g):
    U = g.U; s = 0; n = 0
    for mu in range(4):
        for nu in range(mu+1, 4):
            P = g.mul(g.mul(U[mu], np.roll(U[nu], -1, axis=mu)), g.dag(g.mul(U[nu], np.roll(U[mu], -1, axis=nu))))
            s += g.retr(P).mean(); n += 1
    return s / n

def poly_t(g):
    P = g.U[0][0]
    for x in range(1, g.U.shape[1]):
        P = g.mul(P, g.U[0][x])
    return g.retr(P).mean(axis=(0, 1))   # over y,z -> function of t

def run(G, beta, L, T, ntherm, nmeas, seed, meas_poly=True):
    rng = np.random.default_rng(seed)
    shape = (L, L, L, T); g = G(shape, rng); M = masks(shape)
    for _ in range(ntherm): sweep(g, beta, M)
    pl = []; Cs = []
    for _ in range(nmeas):
        sweep(g, beta, M); pl.append(plaq(g))
        if meas_poly:
            p = poly_t(g); Cs.append([np.mean(p*np.roll(p, -t)) for t in range(4)])
    return np.array(pl), np.array(Cs)

def jack(Cs, nb=10):
    n = len(Cs) // nb * nb; B = Cs[:n].reshape(nb, -1, Cs.shape[1]).mean(1)
    full = B.mean(0); samples = [(B.sum(0) - B[i]) / (nb - 1) for i in range(nb)]
    def est(C):
        r1 = (C[0] + C[2]) / (2*C[1]); r2 = (C[1] + C[3]) / (2*C[2])
        m1 = np.arccosh(r1) if r1 > 1 else np.nan; m2 = np.arccosh(r2) if (C[2] > 0 and r2 > 1) else np.nan
        return np.array([m1, m2])
    e = est(full); js = np.array([est(s) for s in samples])
    err = np.sqrt((nb - 1) / nb * ((js - js.mean(0))**2).sum(0))
    cerr = np.sqrt((nb - 1) / nb * ((np.array(samples) - np.array(samples).mean(0))**2).sum(0))
    return full, cerr, e, err

def bessel_ratio(n, x, K=200000):
    t = np.linspace(0, np.pi, K + 1)
    f = lambda m: np.trapezoid(np.exp(x*np.cos(t))*np.cos(m*t), t)
    return f(n) / f(n - 1)

def main():
    out = open(sys.argv[1], "x"); t0 = time.time(); res = {}
    def log(s):
        print(s); out.write(s + "\n"); out.flush()
    # controls
    for name, G, a in [("SU2", SU2, bessel_ratio(2, 0.5)), ("U1", U1, bessel_ratio(1, 0.5))]:
        pl, _ = run(G, 0.5, 4, 4, 50, 100, 11, meas_poly=False)
        m = pl.mean(); ok = abs(m - a) < 0.01
        log(f"C1 {name} beta=0.5 plaq={m:.4f}+-{pl.std()/np.sqrt(len(pl)):.4f} onePlaq={a:.4f} {'MET' if ok else 'FAILED'}")
    pl, _ = run(U1, 2.3, 4, 4, 100, 100, 12, meas_poly=False)
    d = 1 - pl.mean(); ok = abs(d / (1/(4*2.3)) - 1) < 0.25
    log(f"C2 U1 beta=2.3 1-plaq={d:.4f} 1/(4b)={1/9.2:.4f} {'MET' if ok else 'FAILED'}")
    beta = 2.3; T = 12
    budget = {2: (200, 3000), 4: (200, 2000), 6: (150, 700)}
    for name, G in [("SU2", SU2), ("U1", U1)]:
        for L in (2, 4, 6):
            nth, nm = budget[L]
            pl, Cs = run(G, beta, L, T, nth, nm, 1000 + 10*L + (0 if name == "SU2" else 1))
            C, ce, m, me = jack(Cs)
            qual = C[2] > 3*ce[2]
            res[(name, L)] = (L*m[0], L*me[0], qual)
            log(f"{name} L={L} T={T} nmeas={nm} plaq={pl.mean():.4f} C={np.round(C,5).tolist()} dC={np.round(ce,5).tolist()} "
                f"meff1={m[0]:.4f}+-{me[0]:.4f} meff2={m[1]:.4f}+-{me[1]:.4f} z=L*meff1={L*m[0]:.4f}+-{L*me[0]:.4f} qualifies={qual} t={time.time()-t0:.0f}s")
    zs = {k: v[0] for k, v in res.items()}; dz = {k: v[1] for k, v in res.items()}
    PA = all(zs[("SU2", b)] - zs[("SU2", a)] > 2*np.hypot(dz[("SU2", a)], dz[("SU2", b)]) for a, b in [(2, 4), (4, 6)])
    PB = (zs[("U1", 6)] - zs[("U1", 4)] < max(3*np.hypot(dz[("U1", 4)], dz[("U1", 6)]), 0.2*zs[("U1", 4)])) and zs[("U1", 6)] < 1
    PC = zs[("SU2", 6)] / zs[("U1", 6)] > 2
    PD = all(0.5 < zs[("U1", L)] / (1/(2*beta)) < 2 for L in (4, 6))
    for n, v in [("P_A", PA), ("P_B", PB), ("P_C", PC), ("P_D", PD)]:
        log(f"{n} {'MET' if v else 'FAILED'}")
    log(f"qualifying cases (C(2)>3sigma): {sum(v[2] for v in res.values())}/{len(res)}; total {time.time()-t0:.0f}s")

if __name__ == "__main__":
    main()
