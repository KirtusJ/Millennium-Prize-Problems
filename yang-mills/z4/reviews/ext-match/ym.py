#!/usr/bin/env python3
"""ym.py -- SU(2) Wilson-action lattice gauge theory: heat-bath + overrelaxation,
spatial (per time slice, 3D) Wilson flow by Luscher RK3, magnetic slice densities.

Representation: U = a0 + i a.sigma, stored as quaternion (a0,a1,a2,a3), (1/2)Tr U = a0.
Array U[mu, t, x, y, z, 4], mu=0 is time.  Action S = beta * sum_{unoriented p} (1 - 1/2 Tr U_p).
Heat bath: Creutz (alpha=beta*k < 2) / Kennedy-Pendleton (alpha >= 2), checkerboard, then n_or
overrelaxation sweeps.  Flow: for spatial links only, dV/ds = -P_ta(V * Sigma_spatial_staples) V,
Sigma over the 4 spatial staples (3D action of that slice); temporal links untouched.
RK3 (Luscher 2010, eq. C.1-C.3).  Lattice flow time s/a^2.
Observable: Ebar_n = slice average of sum_{i<j} (1 - 1/2 Tr U_ij), PLAQUETTE form (not clover).

Subcommands
  run      : --L --beta --ncfg --nsweep --seed --s --eps [--nor --ntherm --out --resume]
             appends one line per configuration to --out:
             cfg_index  plaq_unflowed  Ebar_n(s/4) x L  Ebar_n(s/2) x L  Ebar_n(s) x L  seconds
  controls : runs M1/M2 controls, writes controls_<seed>.txt (mode "x").

PREDICATES (fixed before the first run; tolerance sources stated)
 C1 strong coupling, beta=0.5, 4^4: |<1-1/2TrU_p> - (1 - I2(.5)/I1(.5))| <= 3 sigma_stat + 1e-3
    (1e-3: neglected higher-order strong-coupling corrections, O(u^4..u^5) with u~0.124, coefficient <~ 10..30).
 C2 average plaquette at beta 2.3 (6^4) and 2.5 (12^4) vs FHK Table 8 (hep-lat/9208012) linearly
    interpolated to beta=2.3, 2.5 from 2.2986/2.3726 and 2.4265/2.5115:
    |diff| <= 3*sqrt(sig_pub^2 + sig_interp^2 + sig_mine^2); sig_interp = |lin - quadratic interp| (3-point).
    Finite-volume shift on 6^4 / 12^4 not included: a failure here may be finite-size, not a code defect.
 C3 gauge invariance: plaquette and all flowed Ebar_n identical under a random gauge transformation
    to 1e-10 (absolute; double precision roundoff over ~1e3 RK steps is ~1e-13).
 C4 flowed spatial action (sum over slices) non-increasing at every RK step (to 1e-12 roundoff).
 C5 step halving: |Ebar(eps) - Ebar(eps/2)| / Ebar < 1e-4 at the target s (1e-4 chosen to be well below the
    expected statistical relative error ~1e-3 of <Ebar>).
 C6 free field: beta=40, 6^4, s/a^2 in {0.5, 1.0}: s^2 <Ebar> within 20% (brief) of s^2 E_free(s),
    E_free(s) = (3/beta) (1/V) sum_{k != 0} khat_s^2 exp(-2 s khat_s^2) / khat^2, khat^2 = sum 4 sin^2(k/2)
    (derived in notes.md; t=0 limit reproduces 3 plaquettes x 3/(4 beta)).
"""
import argparse, math, os, sys, time
import numpy as np

# ---------------- quaternion algebra ----------------
def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    c = np.empty(np.broadcast_shapes(a.shape, b.shape))
    c[..., 0] = a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3
    c[..., 1] = a0 * b1 + b0 * a1 - (a2 * b3 - a3 * b2)
    c[..., 2] = a0 * b2 + b0 * a2 - (a3 * b1 - a1 * b3)
    c[..., 3] = a0 * b3 + b0 * a3 - (a1 * b2 - a2 * b1)
    return c

def qdag(a):
    c = a.copy(); c[..., 1:] *= -1; return c

def qexp(v):  # exp(i v.sigma), v real 3-vector field
    n = np.sqrt((v * v).sum(-1))
    out = np.empty(v.shape[:-1] + (4,))
    out[..., 0] = np.cos(n)
    s = np.where(n > 1e-300, np.sin(n) / np.where(n > 1e-300, n, 1.0), 1.0)
    out[..., 1:] = v * s[..., None]
    return out

def sh(f, axis, d):  # f(x + d*e_axis)
    return np.roll(f, -d, axis=axis)

def staple(U, mu, dirs):
    V = np.zeros(U.shape[1:])
    for nu in dirs:
        if nu == mu: continue
        Unu = U[nu]; Umu = U[mu]
        V += qmul(qmul(sh(Unu, mu, 1), qdag(sh(Umu, nu, 1))), qdag(Unu))
        Unu_m = sh(Unu, nu, -1)
        V += qmul(qmul(qdag(sh(Unu_m, mu, 1)), qdag(sh(Umu, nu, -1))), Unu_m)
    return V

def plaq_field(U, mu, nu):
    return qmul(qmul(U[mu], sh(U[nu], mu, 1)), qdag(qmul(U[nu], sh(U[mu], nu, 1))))

def mean_plaq(U):
    s = 0.0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            s += plaq_field(U, mu, nu)[..., 0].mean()
    return s / 6.0

def slice_Ebar(U):
    """Ebar_n = slice average over (x,y,z) of sum_{i<j} (1 - a0(U_ij)), spatial i,j in 1..3."""
    e = 0.0
    for i in (1, 2, 3):
        for j in range(i + 1, 4):
            e = e + (1.0 - plaq_field(U, i, j)[..., 0])
    return e.mean(axis=(1, 2, 3))

# ---------------- heat bath ----------------
def sample_x0(alpha, rng):
    n = alpha.size
    x = np.empty(n); todo = np.arange(n)
    while todo.size:
        al = alpha[todo]
        small = al < 2.0
        xs = np.empty(todo.size); acc = np.zeros(todo.size, bool)
        # Creutz
        if small.any():
            a = al[small]
            r = rng.uniform(np.exp(-2 * a), 1.0)
            x0 = 1.0 + np.log(r) / a
            ok = rng.uniform(size=a.size) <= np.sqrt(np.clip(1 - x0 * x0, 0, None))
            xs[small] = x0; acc[small] = ok
        big = ~small
        if big.any():
            a = al[big]
            r1 = 1.0 - rng.uniform(size=a.size); r2 = rng.uniform(size=a.size); r3 = 1.0 - rng.uniform(size=a.size)
            lam2 = -(np.log(r1) + np.cos(2 * np.pi * r2) ** 2 * np.log(r3)) / (2 * a)
            ok = rng.uniform(size=a.size) ** 2 <= 1 - lam2
            xs[big] = 1 - 2 * lam2; acc[big] = ok
        x[todo[acc]] = xs[acc]
        todo = todo[~acc]
    return x

def random_su2_from_x0(x0, rng):
    n = x0.size
    r = np.sqrt(np.clip(1 - x0 * x0, 0, None))
    ct = rng.uniform(-1, 1, n); st = np.sqrt(1 - ct * ct); ph = rng.uniform(0, 2 * np.pi, n)
    return np.stack([x0, r * st * np.cos(ph), r * st * np.sin(ph), r * ct], -1)

def parity_masks(L):
    g = np.indices((L, L, L, L)).sum(0) % 2
    return [g == 0, g == 1]

def sweep(U, beta, rng, masks, n_or):
    for mu in range(4):
        for m in masks:
            V = staple(U, mu, range(4))[m]
            k = np.sqrt((V * V).sum(-1))
            Vh = V / k[:, None]
            X = random_su2_from_x0(sample_x0(beta * k, rng), rng)
            U[mu][m] = qmul(X, qdag(Vh))
    for _ in range(n_or):
        for mu in range(4):
            for m in masks:
                V = staple(U, mu, range(4))[m]
                Vh = V / np.sqrt((V * V).sum(-1))[:, None]
                Vd = qdag(Vh)
                U[mu][m] = qmul(qmul(Vd, qdag(U[mu][m])), Vd)
    # reunitarize against drift
    U /= np.sqrt((U * U).sum(-1))[..., None]

# ---------------- spatial flow ----------------
def flow_force(W):
    """Z_i = -P_ta(W_i * sum spatial staples), returned as real 3-vectors z with Z = i z.sigma."""
    Z = np.zeros((3,) + W.shape[1:-1] + (3,))
    for i in (1, 2, 3):
        Om = qmul(W[i], staple(W, i, (1, 2, 3)))
        Z[i - 1] = -Om[..., 1:]
    return Z

def spatial_action(W):
    return float(slice_Ebar(W).sum())

def flow(U, s_targets, eps, check_monotone=False):
    """Luscher RK3 on spatial links. returns dict s->Ebar_n, list of actions (if check)."""
    W = U.copy(); out = {}; acts = []
    nsteps = int(round(max(s_targets) / eps))
    marks = {int(round(st / eps)): st for st in s_targets}
    if check_monotone: acts.append(spatial_action(W))
    for n in range(1, nsteps + 1):
        Z0 = eps * flow_force(W)
        for i in range(3): W[i + 1] = qmul(qexp(0.25 * Z0[i]), W[i + 1])
        Z1 = eps * flow_force(W)
        for i in range(3): W[i + 1] = qmul(qexp(8 / 9 * Z1[i] - 17 / 36 * Z0[i]), W[i + 1])
        Z2 = eps * flow_force(W)
        for i in range(3): W[i + 1] = qmul(qexp(0.75 * Z2[i] - 8 / 9 * Z1[i] + 17 / 36 * Z0[i]), W[i + 1])
        if check_monotone: acts.append(spatial_action(W))
        if n in marks: out[marks[n]] = slice_Ebar(W)
    return out, acts, W

def hot_start(L, rng):
    q = rng.normal(size=(4, L, L, L, L, 4))
    return q / np.sqrt((q * q).sum(-1))[..., None]

def cold_start(L):
    U = np.zeros((4, L, L, L, L, 4)); U[..., 0] = 1.0; return U

# ---------------- run ----------------
def cmd_run(a):
    rng = np.random.default_rng(a.seed)
    ck = a.out + ".ckpt.npz"
    masks = parity_masks(a.L)
    s_list = [a.s / 4, a.s / 2, a.s]
    if a.resume:
        d = np.load(ck, allow_pickle=True)
        U = d["U"]; rng.bit_generator.state = d["rng"].item(); start = int(d["next"])
        f = open(a.out, "a")
    else:
        U = hot_start(a.L, rng)
        t0 = time.time()
        for _ in range(a.ntherm): sweep(U, a.beta, rng, masks, a.nor)
        print(f"# therm {a.ntherm} sweeps {time.time()-t0:.1f}s", flush=True)
        start = 0
        f = open(a.out, "x")
        f.write(f"# L={a.L} beta={a.beta} nsweep={a.nsweep} nor={a.nor} seed={a.seed} s={a.s} eps={a.eps} ntherm={a.ntherm}\n")
        f.write("# cfg plaq Ebar(s/4)[L] Ebar(s/2)[L] Ebar(s)[L] sec\n"); f.flush()
    for c in range(start, start + a.ncfg):
        t0 = time.time()
        for _ in range(a.nsweep): sweep(U, a.beta, rng, masks, a.nor)
        p = mean_plaq(U)
        out, _, _ = flow(U, s_list, a.eps)
        vals = [p] + [x for st in s_list for x in out[st]]
        f.write(f"{c} " + " ".join(f"{v:.12e}" for v in vals) + f" {time.time()-t0:.2f}\n"); f.flush()
        if (c + 1) % 5 == 0 or c == start + a.ncfg - 1:
            np.savez(ck + ".tmp.npz", U=U, rng=np.array(rng.bit_generator.state, dtype=object), next=c + 1)
            os.replace(ck + ".tmp.npz", ck)
    f.close()

# ---------------- controls ----------------
def besselI(n, x):
    return sum((x / 2) ** (2 * k + n) / math.factorial(k) / math.factorial(k + n) for k in range(60))

def E_free(L, beta, s):
    k = 2 * np.pi * np.arange(L) / L
    kh2 = 4 * np.sin(k / 2) ** 2
    K0, K1, K2, K3 = np.meshgrid(kh2, kh2, kh2, kh2, indexing="ij")
    ks = K1 + K2 + K3; kk = K0 + ks
    m = kk > 0
    return 3.0 / beta * (ks[m] * np.exp(-2 * s * ks[m]) / kk[m]).sum() / L ** 4

def jk_err(x, nb=10):
    x = np.asarray(x); n = len(x) // nb * nb; b = x[:n].reshape(nb, -1).mean(1)
    return float(np.sqrt(b.var() / (nb - 1)))  # fixed: was sqrt((nb-1)*var), overstated x(nb-1)

def cmd_controls(a):
    rng = np.random.default_rng(a.seed)
    f = open(f"controls_{a.seed}.txt", "x")
    def log(s):
        print(s, flush=True); f.write(s + "\n"); f.flush()
    res = {}
    # C1
    L = 4; U = hot_start(L, rng); masks = parity_masks(L); beta = 0.5
    for _ in range(50): sweep(U, beta, rng, masks, 1)
    d = []
    for _ in range(400):
        sweep(U, beta, rng, masks, 1); d.append(1 - mean_plaq(U))
    m, e = np.mean(d), jk_err(d, 20)
    ex = 1 - besselI(2, beta) / besselI(1, beta)
    ok = abs(m - ex) <= 3 * e + 1e-3
    log(f"C1 strong coupling beta=0.5 4^4: <1-P>={m:.6f}+-{e:.6f} expected {ex:.6f} diff={m-ex:+.2e} tol={3*e+1e-3:.2e} -> {'MET' if ok else 'FAILED'}")
    # C6 free field
    L = 6; beta = 40.0; U = cold_start(L); masks = parity_masks(L)
    for _ in range(60): sweep(U, beta, rng, masks, 2)
    acc = {0.5: [], 1.0: []}
    for _ in range(12):
        for _ in range(3): sweep(U, beta, rng, masks, 2)
        out, _, _ = flow(U, [0.5, 1.0], 0.01)
        for st in acc: acc[st].append(out[st].mean())
    for st in acc:
        m = np.mean(acc[st]); e = np.std(acc[st]) / np.sqrt(len(acc[st]) - 1); ef = E_free(L, beta, st)
        rel = m / ef - 1
        log(f"C6 free field beta=40 6^4 s={st}: s^2<Ebar>={st*st*m:.4e}+-{st*st*e:.1e} free={st*st*ef:.4e} rel={rel:+.3f} -> {'MET' if abs(rel)<0.2 else 'FAILED'}")
    log(f"C6 aux: unflowed free mode sum (s=0) {E_free(L,beta,0.0):.5e} vs 9/(4beta) {9/(4*beta):.5e} (finite-volume)")
    # C3, C4, C5 on thermalised beta=2.3 6^4 and a 12^4 beta=2.5 short therm
    for (L, beta, s, eps, nth) in [(6, 2.3, 0.5, 0.025, 100), (12, 2.5, 2.0, 0.05, 40)]:
        U = hot_start(L, rng); masks = parity_masks(L)
        for _ in range(nth): sweep(U, beta, rng, masks, 3)
        out, acts, _ = flow(U, [s / 4, s / 2, s], eps, check_monotone=True)
        dif = np.diff(acts); ok4 = bool((dif <= 1e-12).all())
        log(f"C4 L={L} beta={beta}: spatial action {acts[0]:.4f} -> {acts[-1]:.4f}, max step change {dif.max():+.3e} -> {'MET' if ok4 else 'FAILED'}")
        out2, _, _ = flow(U, [s], eps / 2)
        r = abs(out[s].mean() - out2[s].mean()) / out2[s].mean()
        log(f"C5 L={L} step eps={eps} vs {eps/2}: rel diff of slice-mean Ebar at s={s}: {r:.2e}; max per slice {np.max(np.abs(out[s]-out2[s])/out2[s]):.2e} -> {'MET' if r<1e-4 else 'FAILED'}")
        # gauge transformation
        g = rng.normal(size=(L, L, L, L, 4)); g /= np.sqrt((g * g).sum(-1))[..., None]
        Ug = np.empty_like(U)
        for mu in range(4): Ug[mu] = qmul(qmul(g, U[mu]), qdag(sh(g, mu, 1)))
        outg, _, _ = flow(Ug, [s / 4, s / 2, s], eps)
        dp = abs(mean_plaq(U) - mean_plaq(Ug))
        de = max(np.max(np.abs(out[k] - outg[k])) for k in out)
        dn = np.max(np.abs(slice_Ebar(U) - slice_Ebar(Ug)))
        log(f"C3 L={L} gauge invariance: |dplaq|={dp:.2e} |dEbar unflowed|={dn:.2e} |dEbar flowed| max={de:.2e} -> {'MET' if max(dp,de,dn)<1e-10 else 'FAILED'}")
    f.close()

def cmd_freefield(a):
    """C6 diagnostic (added after C6 s=1.0 FAILED on 6^4; predicate unchanged: |rel| < 0.2).
    Tests whether the s=1.0 discrepancy shrinks with L (finite-volume zero modes)."""
    rng = np.random.default_rng(a.seed)
    f = open(f"freefield_L{a.L}_{a.seed}.txt", "x")
    L = a.L; beta = 40.0; U = cold_start(L); masks = parity_masks(L)
    for _ in range(60): sweep(U, beta, rng, masks, 2)
    acc = {0.5: [], 1.0: []}
    for _ in range(a.n):
        for _ in range(3): sweep(U, beta, rng, masks, 2)
        out, _, _ = flow(U, [0.5, 1.0], 0.025)
        for st in acc: acc[st].append(out[st].mean())
    for st in acc:
        m = np.mean(acc[st]); e = np.std(acc[st]) / np.sqrt(len(acc[st]) - 1); ef = E_free(L, beta, st)
        rel = m / ef - 1
        s_ = f"C6' free field beta=40 {L}^4 s={st}: s^2<Ebar>={st*st*m:.4e}+-{st*st*e:.1e} free={st*st*ef:.4e} rel={rel:+.3f} -> {'MET' if abs(rel)<0.2 else 'FAILED'}"
        print(s_); f.write(s_ + "\n")
    f.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    r = sp.add_parser("run")
    r.add_argument("--L", type=int, required=True); r.add_argument("--beta", type=float, required=True)
    r.add_argument("--ncfg", type=int, required=True); r.add_argument("--nsweep", type=int, required=True)
    r.add_argument("--seed", type=int, required=True); r.add_argument("--s", type=float, required=True)
    r.add_argument("--eps", type=float, required=True); r.add_argument("--nor", type=int, default=3)
    r.add_argument("--ntherm", type=int, default=100); r.add_argument("--out", required=True)
    r.add_argument("--resume", action="store_true")
    c = sp.add_parser("controls"); c.add_argument("--seed", type=int, default=7)
    ff = sp.add_parser("freefield"); ff.add_argument("--L", type=int, required=True); ff.add_argument("--seed", type=int, default=11); ff.add_argument("--n", type=int, default=12)
    a = ap.parse_args()
    {"run": cmd_run, "controls": cmd_controls, "freefield": cmd_freefield}[a.cmd](a)
