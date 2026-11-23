"""mc.py -- SU(2) Wilson lattice gauge theory, 4D periodic L^4, numpy checkerboard heat bath.

Usage: python mc.py BETA L NTHERM NMEAS BLOCK SEED OUTDIR [NOR]
  One sweep = for each direction mu and each parity: Kennedy-Pendleton/Creutz heat bath
  (Creutz for a=beta*k<2, KP otherwise), followed by NOR (default 2) overrelaxation sweeps.
  Cold start. NTHERM sweeps discarded. NMEAS measured sweeps, written in blocks of BLOCK
  configs to OUTDIR/blk_XXXX.npz (a block file is never overwritten: the program aborts with
  exit 3 if it exists).

Per configuration stored: plaq (mean (1/2)Tr U_p over all 6 planes), and for R=1,2 spatial
R x R loops (planes 12,13,23; all positions; all time slices):
  m[R]  = mean W ;  c[R][n] = mean over positions, orientations, t of W(t) W(t+n), n=0..3
  (n=0 gives <W^2>).

PREDICATES of this program (fixed before first run; checked at runtime, exit 2 on failure):
  M1 links stay unitary: max | |q|^2 - 1 | < 1e-10 at every block end (tolerance: float64
     roundoff accumulates ~1e-15 per update; we renormalise each update, 1e-10 is generous).
  M2 every plaq and W lies in [-1, 1] (+1e-12 roundoff).
  M3 cold-start plaquette at sweep 0 equals 1 to 1e-12 (exact identity links).
Physics predicates (P1, P2) are evaluated in analyze.py, not here.
"""
import sys, os, time
import numpy as np

def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    # U = a0 + i a.sigma ; product c0 = a0b0 - a.b, c = a0 b + b0 a - a x b
    return np.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3,
                     a0*b1 + b0*a1 - (a2*b3 - a3*b2),
                     a0*b2 + b0*a2 - (a3*b1 - a1*b3),
                     a0*b3 + b0*a3 - (a1*b2 - a2*b1)], axis=-1)

def qdag(a):
    return a * np.array([1., -1., -1., -1.])

def sh(x, mu, s):
    """x(site + s*e_mu): roll by -s along lattice axis mu (axes 0..3)."""
    return np.roll(x, -s, axis=mu)

def staple(U, mu):
    A = np.zeros_like(U[0])
    for nu in range(4):
        if nu == mu:
            continue
        # U_nu(x+mu) U_mu(x+nu)^dag U_nu(x)^dag
        A += qmul(qmul(sh(U[nu], mu, 1), qdag(sh(U[mu], nu, 1))), qdag(U[nu]))
        # U_nu(x+mu-nu)^dag U_mu(x-nu)^dag U_nu(x-nu)
        Unm = sh(U[nu], nu, -1)
        A += qmul(qmul(qdag(sh(Unm, mu, 1)), qdag(sh(U[mu], nu, -1))), Unm)
    return A

def sample_a0(a, rng):
    """density ~ sqrt(1-x^2) exp(a x) on [-1,1]; Creutz for a<2, Kennedy-Pendleton for a>=2."""
    x = np.empty_like(a)
    todo = np.arange(a.size)
    while todo.size:
        aa = a[todo]
        r = rng.random((4, todo.size))
        small = aa < 2.0
        xs = np.empty_like(aa); ok = np.empty(aa.size, bool)
        # Creutz: x = 1 + ln(u)/a, u uniform in (e^{-2a}, 1]; accept with sqrt(1-x^2)
        u = np.exp(-2*aa) + (1 - np.exp(-2*aa)) * (1 - r[0])
        xc = 1 + np.log(u) / aa
        okc = r[1] <= np.sqrt(np.clip(1 - xc*xc, 0, 1))
        # KP
        X = -(np.log(1 - r[0]) + np.cos(2*np.pi*r[1])**2 * np.log(1 - r[2])) / aa
        xk = 1 - X
        okk = (r[3]**2 <= 1 - X/2) & (xk >= -1)
        xs = np.where(small, xc, xk); ok = np.where(small, okc, okk)
        x[todo[ok]] = xs[ok]
        todo = todo[~ok]
    return x

def heatbath(U, mu, mask, beta, rng):
    A = staple(U, mu)[mask]                       # (n,4)
    k = np.sqrt((A*A).sum(-1))
    V = A / k[:, None]
    a0 = sample_a0(beta * k, rng)
    n = a0.size
    cth = 2*rng.random(n) - 1; ph = 2*np.pi*rng.random(n)
    s = np.sqrt(np.clip(1 - a0*a0, 0, 1)); sth = np.sqrt(1 - cth*cth)
    X = np.stack([a0, s*sth*np.cos(ph), s*sth*np.sin(ph), s*cth], -1)
    # weight exp(beta/2 Tr(U A)) = exp(beta k (U V)_0); X = U V  ->  U = X V^dag
    new = qmul(X, qdag(V))
    new /= np.sqrt((new*new).sum(-1))[:, None]
    U[mu][mask] = new

def overrelax(U, mu, mask):
    A = staple(U, mu)[mask]
    k2 = (A*A).sum(-1)
    Vd = qdag(A) / np.sqrt(k2)[:, None]
    new = qmul(qmul(Vd, qdag(U[mu][mask])), Vd)
    new /= np.sqrt((new*new).sum(-1))[:, None]
    U[mu][mask] = new

def plaquette(U):
    s = 0.0
    for mu in range(4):
        for nu in range(mu+1, 4):
            P = qmul(qmul(U[mu], sh(U[nu], mu, 1)), qmul(qdag(sh(U[mu], nu, 1)), qdag(U[nu])))
            s += P[..., 0].mean()
    return s / 6

def line(U, mu, R):
    """product U_mu(x) U_mu(x+mu) ... (R links) starting at every x."""
    P = U[mu]
    for r in range(1, R):
        P = qmul(P, sh(U[mu], mu, r))
    return P

def loops(U, R):
    """W[o, x,y,z,t] for spatial R x R loops in planes (0,1),(0,2),(1,2)."""
    out = []
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        Li = line(U, i, R); Lj = line(U, j, R)
        P = qmul(qmul(Li, sh(Lj, i, R)), qmul(qdag(sh(Li, j, R)), qdag(Lj)))
        out.append(P[..., 0])
    return np.stack(out)

def sweep(U, beta, rng, masks, nor):
    for mu in range(4):
        for m in masks:
            heatbath(U, mu, m, beta, rng)
    for _ in range(nor):
        for mu in range(4):
            for m in masks:
                overrelax(U, mu, m)

def main():
    beta = float(sys.argv[1]); L = int(sys.argv[2]); nth = int(sys.argv[3]); nmeas = int(sys.argv[4])
    blk = int(sys.argv[5]); seed = int(sys.argv[6]); outdir = sys.argv[7]
    nor = int(sys.argv[8]) if len(sys.argv) > 8 else 2
    os.makedirs(outdir, exist_ok=True)
    rng = np.random.default_rng(seed)
    U = np.zeros((4, L, L, L, L, 4)); U[..., 0] = 1.0
    p0 = plaquette(U)
    if abs(p0 - 1) > 1e-12:
        print("M3 FAIL", p0); sys.exit(2)
    g = np.indices((L,)*4).sum(0) % 2
    masks = [g == 0, g == 1]
    t0 = time.time()
    therm = []
    for i in range(nth):
        sweep(U, beta, rng, masks, nor)
        therm.append(plaquette(U))
    np.save(os.path.join(outdir, "therm_%d.npy" % seed), np.array(therm)) if not os.path.exists(os.path.join(outdir, "therm_%d.npy" % seed)) else None
    print("therm done %.1fs plaq_last=%.5f" % (time.time()-t0, therm[-1] if therm else p0), flush=True)
    rec = {k: [] for k in ["plaq", "m1", "m2", "c1", "c2"]}
    ib = 0
    for i in range(nmeas):
        sweep(U, beta, rng, masks, nor)
        rec["plaq"].append(plaquette(U))
        for R in (1, 2):
            W = loops(U, R)
            if np.abs(W).max() > 1 + 1e-12:
                print("M2 FAIL"); sys.exit(2)
            rec["m%d" % R].append(W.mean())
            rec["c%d" % R].append([(W * np.roll(W, -n, axis=4)).mean() for n in range(4)])
        if (i + 1) % blk == 0:
            dev = np.abs((U*U).sum(-1) - 1).max()
            if dev > 1e-10:
                print("M1 FAIL", dev); sys.exit(2)
            fn = os.path.join(outdir, "blk_%04d.npz" % ib)
            if os.path.exists(fn):
                print("refusing to overwrite", fn); sys.exit(3)
            np.savez(fn, beta=beta, L=L, seed=seed, nor=nor, **{k: np.array(v) for k, v in rec.items()})
            rec = {k: [] for k in rec}
            print("block %d  %.1fs  plaq %.5f" % (ib, time.time()-t0, np.mean(np.load(fn)["plaq"])), flush=True)
            ib += 1
    print("DONE")

if __name__ == "__main__":
    main()
