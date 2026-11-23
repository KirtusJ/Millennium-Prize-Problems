"""SU(2) Wilson Monte Carlo on 8^4 (periodic), test of the strip bound.

Usage: python3 mc_strip.py BETA NTHERM NMEAS SEED OUTFILE

Observables (averaged over all base points and all 12 ordered planes (i,j)):
  W(w)   = <1/2 tr U_{1 x w}>  rectangle width 1 along i, length w along j, w=1..8
  Wsq(m) = <1/2 tr U_{m x m}>  m=2,3,4
  Q(r)   = <1/2 tr L_x U_0(x) L_{x+e0}^{-1}>, x=(0,r,r,r) spatial, L = time first then axes 1,2,3
           (the ordered-root quantity of strip/README.md eq. (2)), r=1..4, rooted at every site.
  Norm identity: E|1-U|^2 = 2(1-W) for unit quaternions (checked per configuration on the plaquette).

PREDICATES (fixed before first run):
  C0 control: |W(1) - (1 - 3/(4 beta))| <= 1/beta^2 + 4 sigma.
     Tolerance source: next-order weak-coupling term of SU(2) plaquette is c2/beta^2 with |c2| < 1
     (my estimate, not a quoted literature value); finite-volume zero-mode corrections O(1/(V beta)) are smaller.
  P1 for all w in 1..8: 1-W(w) <= w (1-W(1)) + 3 sigma_w        [strip eq. (1), deficit form]
     (w>4 exceeds L/2=4: the finite-torus Gram argument does not cover it; reported separately.)
  P2 for all m in 2..4: 1-Wsq(m) <= m^2 (1-W(1)) + 3 sigma       [rectangles.md eq. (1)]
  P3 for all r in 1..4: 2(1-Q(r)) <= 9 * 2 r (1-W(1)) + 3 sigma   [strip eq. (2) with explicit constant:
     ||1-Q|| <= sum over 3 swaps of ||1-U_{1xr}|| <= 3 sqrt(2 r (1-W(1)))]
  P4 identity |mean|1-U_p|^2 - 2(1-W(1))| <= 1e-10 per configuration (float64 roundoff).
  Measured only: ratios (1-W(w))/(w(1-W(1))), beta*(1-W(w)), local exponents of the deficit in w and r.
Errors: binning of measurements in 10 bins.
"""
import sys, os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np

L = 8
D = 4

def qmul(a, b):
    a0, av = a[..., 0], a[..., 1:]
    b0, bv = b[..., 0], b[..., 1:]
    out = np.empty(np.broadcast(a, b).shape)
    out[..., 0] = a0 * b0 - np.sum(av * bv, axis=-1)
    out[..., 1:] = a0[..., None] * bv + b0[..., None] * av - np.cross(av, bv)
    return out

def qconj(a):
    c = a.copy(); c[..., 1:] *= -1; return c

def sh(a, mu, n):
    """field value at x + n e_mu."""
    return np.roll(a, -n, axis=mu)

def staple_sum(U, mu):
    A = np.zeros(U.shape[1:])
    for nu in range(D):
        if nu == mu: continue
        Unu = U[nu]; Umu = U[mu]
        up = qmul(qmul(sh(Unu, mu, 1), qconj(sh(Umu, nu, 1))), qconj(Unu))
        xm = sh(Unu, nu, -1)
        dn = qmul(qmul(qconj(sh(xm, mu, 1)), qconj(sh(Umu, nu, -1))), xm)
        A += up + dn
    return A

def kp_sample(alpha, rng):
    n = alpha.size
    a0 = np.empty(n); todo = np.arange(n)
    while todo.size:
        al = alpha[todo]
        r1, r2, r3, r4 = (1 - rng.random((4, todo.size)))
        X = -(np.log(r1) + np.cos(2 * np.pi * r2) ** 2 * np.log(r3)) / al
        ok = r4 ** 2 <= 1 - X / 2
        a0[todo[ok]] = 1 - X[ok]
        todo = todo[~ok]
    v = rng.normal(size=(n, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
    v *= np.sqrt(np.clip(1 - a0 ** 2, 0, None))[:, None]
    return np.concatenate([a0[:, None], v], axis=1)

par = np.indices((L,) * D).sum(axis=0) % 2

def sweep(U, beta, rng):
    for mu in range(D):
        for p in (0, 1):
            A = staple_sum(U, mu)
            m = par == p
            Am = A[m]
            k = np.linalg.norm(Am, axis=1)
            Vh = Am / k[:, None]
            W = kp_sample(beta * k, rng)
            U[mu][m] = qmul(W, qconj(Vh))
    # reunitarize
    U /= np.linalg.norm(U, axis=-1)[..., None]

def path_trace(U, steps):
    """mean over base points of 1/2 tr of the transporter along signed steps (+mu+1 / -(mu+1))."""
    P = np.zeros(U.shape[1:]); P[..., 0] = 1
    off = [0] * D
    for s in steps:
        mu = abs(s) - 1
        if s > 0:
            link = U[mu]
            for nu in range(D):
                if off[nu]: link = sh(link, nu, off[nu])
            P = qmul(P, link); off[mu] += 1
        else:
            off[mu] -= 1
            link = U[mu]
            for nu in range(D):
                if off[nu]: link = sh(link, nu, off[nu])
            P = qmul(P, qconj(link))
    assert all(o % L == 0 for o in off), off
    return P[..., 0].mean()

def rect(i, j, a, b):
    return [i + 1] * a + [j + 1] * b + [-(i + 1)] * a + [-(j + 1)] * b

def measure(U):
    planes = [(i, j) for i in range(D) for j in range(D) if i != j]
    W = [np.mean([path_trace(U, rect(i, j, 1, w)) for i, j in planes]) for w in range(1, 9)]
    Wsq = [np.mean([path_trace(U, rect(i, j, m, m)) for i, j in planes[:6]]) for m in (2, 3, 4)]
    Q = []
    for r in range(1, 5):
        Lx = [2] * r + [3] * r + [4] * r                        # L_x, x=(0,r,r,r): time seg empty
        Lxe = [1] + [2] * r + [3] * r + [4] * r                 # L_{x+e0}
        steps = Lx + [1] + [-s for s in reversed(Lxe)]
        Q.append(path_trace(U, steps))
    # identity P4 on plaquette (0,1)
    pl = qmul(qmul(U[0], sh(U[1], 0, 1)), qmul(qconj(sh(U[0], 1, 1)), qconj(U[1])))
    one = np.zeros(4); one[0] = 1
    idgap = abs(np.mean(np.sum((one - pl) ** 2, axis=-1)) - 2 * (1 - pl[..., 0].mean()))
    return np.array(W + Wsq + Q), idgap

def main():
    beta = float(sys.argv[1]); nth = int(sys.argv[2]); nme = int(sys.argv[3])
    seed = int(sys.argv[4]); out = sys.argv[5]
    rng = np.random.default_rng(seed)
    U = np.zeros((D,) + (L,) * D + (4,)); U[..., 0] = 1   # cold start
    for _ in range(nth): sweep(U, beta, rng)
    data = []; idmax = 0
    for _ in range(nme):
        for _ in range(2): sweep(U, beta, rng)
        v, g = measure(U); data.append(v); idmax = max(idmax, g)
    data = np.array(data)
    nb = 10; bins = np.array([b.mean(0) for b in np.array_split(data, nb)])
    mean = data.mean(0); err = bins.std(0, ddof=1) / np.sqrt(nb)
    W, Wsq, Q = mean[:8], mean[8:11], mean[11:15]
    eW, eS, eQ = err[:8], err[8:11], err[11:15]
    d1 = 1 - W[0]
    lines = [f"beta={beta} L={L} ntherm={nth} nmeas={nme} (2 sweeps apart) seed={seed}"]
    fails = []
    tolc = 1 / beta ** 2 + 4 * eW[0]
    dev = W[0] - (1 - 3 / (4 * beta))
    ok = abs(dev) <= tolc
    lines.append(f"C0 plaquette {W[0]:.6f} +- {eW[0]:.1e}; 1-3/(4b)={1-3/(4*beta):.6f}; dev {dev:+.2e} tol {tolc:.2e} -> {'MET' if ok else 'FAILED'}")
    if not ok: fails.append("C0")
    lines.append("w  1-W(1xw)  sigma  ratio(1-W)/(w(1-W1))  beta(1-W)  P1")
    for w in range(1, 9):
        dw = 1 - W[w - 1]; ok = dw <= w * d1 + 3 * eW[w - 1]
        if not ok: fails.append(f"P1 w={w}")
        lines.append(f"{w}  {dw:.6e}  {eW[w-1]:.1e}  {dw/(w*d1):.4f}  {beta*dw:.4f}  {'MET' if ok else 'FAILED'}{'  (w>L/2)' if w > 4 else ''}")
    for k, m in enumerate((2, 3, 4)):
        dm = 1 - Wsq[k]; ok = dm <= m * m * d1 + 3 * eS[k]
        if not ok: fails.append(f"P2 m={m}")
        lines.append(f"P2 {m}x{m}: 1-W={dm:.6e} +- {eS[k]:.1e}; ratio to m^2(1-W1) {dm/(m*m*d1):.4f}; to m(1-W1) {dm/(m*d1):.4f} {'MET' if ok else 'FAILED'}")
    for r in range(1, 5):
        q = 2 * (1 - Q[r - 1]); ok = q <= 18 * r * d1 + 6 * eQ[r - 1]
        if not ok: fails.append(f"P3 r={r}")
        lines.append(f"P3 r={r} w=1+3r={1+3*r}: ||1-Q||_2^2={q:.6e} +- {2*eQ[r-1]:.1e}; bound 18 r(1-W1)={18*r*d1:.4e}; ratio {q/(18*r*d1):.4f}; beta*||1-Q||^2={beta*q:.4f} {'MET' if ok else 'FAILED'}")
    okid = idmax <= 1e-10
    if not okid: fails.append("P4")
    lines.append(f"P4 max identity gap {idmax:.2e} {'MET' if okid else 'FAILED'}")
    dd = 1 - W
    lines.append("local exponent of 1-W(1xw) in w (w=2..4 vs 1..2): " + " ".join(f"{np.log(dd[w]/dd[w-1])/np.log((w+1)/w):.3f}" for w in range(1, 4)))
    qq = 1 - Q
    lines.append("local exponent of ||1-Q(r)||^2 in r: " + " ".join(f"{np.log(qq[r]/qq[r-1])/np.log((r+1)/r):.3f}" for r in range(1, 4)))
    lines.append(f"FAILED: {fails}" if fails else "all predicates met")
    txt = "\n".join(lines) + "\n"
    with open(out, "x") as f: f.write(txt)
    print(txt)
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
