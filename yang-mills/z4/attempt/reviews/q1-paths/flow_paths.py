"""flow_paths.py -- worker q1-paths (T151). Numerical test of Lemma P'c (flow / chain-of-balls form of
the canonical-path lemma, PATHS.md section 2) on the one-dimensional circle model, finely discretised.

Model (as oned_split.build): grid x_i = -pi + i*dx, dx = kappa/sqrt(beta), Nx % 8 == 0, eps = 2 asinh|sin|,
T_ij = e^{-eps_i/2} K_ij e^{-eps_j/2}, K_ij = dx * sum_{k=-1,0,1} sqrt(beta/2pi) e^{-beta(x_i-x_j+2pi k)^2/2}.
sigma: i -> i + Nx/2.  Lemma P'c is a statement on an ARBITRARY measure space, so it must hold exactly
on this discrete space (counting measure); the fine grid (kappa = 0.25) stands in for the continuum.
g, f from the sector matrices on A = [-pi/2, pi/2) with Agmon conjugation (as oned_split), vector norm 1.
Delta from the exact identity Delta <f,g>_A = 2 <f,R g>_A.  Also E(h) = 1/2 sum T g g (h_i - h_j)^2 (= Delta, GS).

Flow (PATHS.md 2.3): S = whole circle. For start x, z_0 = x, z_k = x + k*Sg + U_k (k = 1..n-1), z_n = x + Nx/2,
Sg = 4 grid points (step = 4 dx = 1/sqrt(beta) at kappa = 0.25), n = Nx/(2 Sg), U_k iid uniform on {-Rg..Rg}, Rg = 2
(ball radius 2 dx = 1/(2 sqrt beta)).  pi_k = law of (z_k, z_{k+1}) under g_x^2.  rho = max_{(a,b)} sum_k pi_k(a,b) / Q(a,b),
Q(a,b) = T_ab g_a g_b.  Bflow = 2 sum_S f^2 / (n rho) = 2/(n rho).
Crude bound (PATHS.md 2.4): Bcrude = 2 Qmin / (n^2 gmax^2 * max(1/(2Rg+1), Nx/(2Rg+1)^2)) where Qmin = min of Q over the support
of the flow; derivation: pi_k(a,b) <= gmax^2 * max(...) for each k.

PREDICATES (fixed before the first run):
 F0 (GS identity, check of inputs) |E(h) - Delta| / Delta < 1e-6 for all beta. Tolerance: eigenvector errors ~1e-12 relative
    after Agmon conjugation; h at the saddle has relative error ~ that; 1e-6 leaves margin.
 F1 (theorem, Lemma P'c) Bflow <= Delta * (1 + 1e-9) for all beta. Tolerance: rounding.
 F2 (theorem, crude bound) Bcrude <= Bflow * (1 + 1e-9) for all beta.
 F3 (expectation: loss is polynomial) log(Delta/Bflow) <= 3 log(beta) for all beta >= 64.
 F4 (expectation: exponent) |(-log Bflow)/sqrt(beta) - c*| decreases from beta = 64 to beta = 1024 and to 4096.
 F5 (expectation: exponent of crude bound) (-log Bcrude - (-log Delta))/sqrt(beta) decreasing in beta over 64..4096.
No randomness (seed 0 for form).  Output results_flow_<tag>.txt opened with mode "x".
"""
import sys, math
import numpy as np
import oned_split as o

np.random.seed(0)


def run(beta, kappa=0.25, Sg=4, Rg=2):
    sb = math.sqrt(beta)
    Nx = int(math.ceil(2 * math.pi * sb / kappa / 8.0)) * 8
    x, T = o.build(beta, Nx)
    half = Nx // 2
    A = np.arange(Nx // 4, 3 * Nx // 4)
    sA = (A + half) % Nx
    TAA = T[np.ix_(A, A)]; R = T[np.ix_(A, sA)]
    P = o.psi(x[A])
    Wl = np.exp(sb * (P[:, None] - P[None, :]))
    le, gw = o.top((TAA + R) * Wl)
    lo, fw = o.top((TAA - R) * Wl)
    s = np.exp(-sb * P)
    gA = gw * s; fA = fw * s
    if fA @ gA < 0:
        fA = -fA
    Delta = 2 * float(fA @ R @ gA) / float(fA @ gA)
    g = np.zeros(Nx); f = np.zeros(Nx)
    g[A] = gA; g[sA] = gA; f[A] = fA; f[sA] = -fA
    g /= math.sqrt(g @ g); f /= math.sqrt(f @ f)
    h = f / g
    # GS energy, written in a cancellation-safe form: T g g (h_i-h_j)^2 = T (f_i g_j - f_j g_i)^2/(g_i g_j)
    Fg = f[:, None] * g[None, :] - f[None, :] * g[:, None]
    with np.errstate(divide='ignore', invalid='ignore'):
        Eh = 0.5 * float(np.nansum(T * Fg ** 2 / (g[:, None] * g[None, :])))
    n = half // Sg
    assert n * Sg == half
    u = 1.0 / (2 * Rg + 1)
    g2 = g ** 2
    # Pi[a, d] for d = b - a in [Sg-2Rg, Sg+2Rg]
    ds = np.arange(Sg - 2 * Rg, Sg + 2 * Rg + 1)
    Pi = np.zeros((Nx, len(ds)))
    idx = np.arange(Nx)
    ys = np.arange(-Rg, Rg + 1)
    for jd, d in enumerate(ds):
        # k = 0: (x, x + Sg + U), prob u if |d - Sg| <= Rg
        if abs(d - Sg) <= Rg:
            Pi[:, jd] += g2 * u
        # k = n-1: a = b - Sg + U, b = x + half: pi(a,b) = g_b^2 u(Sg - d)  (g sigma-even)
        if abs(Sg - d) <= Rg:
            Pi[:, jd] += g2[(idx + d) % Nx] * u
        # middle k = 1..n-2: G_d(c) = sum_y g^2_{c-y} u(y) u(y+d-Sg), c = a - k Sg
        w = np.array([u * u if abs(y + d - Sg) <= Rg else 0.0 for y in ys])
        if w.sum() > 0:
            Gd = np.zeros(Nx)
            for y, wy in zip(ys, w):
                if wy:
                    Gd += wy * g2[(idx - y) % Nx]
            acc = np.zeros(Nx)
            for k in range(1, n - 1):
                acc += Gd[(idx - k * Sg) % Nx]
            Pi[:, jd] += acc
    Qm = np.zeros_like(Pi)
    for jd, d in enumerate(ds):
        b = (idx + d) % Nx
        Qm[:, jd] = T[idx, b] * g * g[b]
    mask = Pi > 0
    rho = float(np.max(Pi[mask] / Qm[mask]))
    Bflow = 2.0 * float(f @ f) / (n * rho)
    Qmin = float(Qm[mask].min())
    pmax = g2.max() * max(u, Nx * u * u)
    Bcrude = 2.0 * Qmin / (n * n * pmax)
    return dict(Nx=Nx, n=n, Delta=Delta, Eh=Eh, Bflow=Bflow, Bcrude=Bcrude, rho=rho, Qmin=Qmin,
                gmax=float(g.max()), le=le)


def main():
    tag = sys.argv[1]
    betas = [float(b) for b in sys.argv[2].split(",")]
    cs = o.cstar()
    out = open(f"results_flow_{tag}.txt", "x")
    def w(s_):
        print(s_); out.write(s_ + "\n"); out.flush()
    w(f"c* = {cs:.7f}")
    w("beta Nx n Delta E(h) Bflow Bcrude Delta/Bflow log(D/Bflow)/log(b) -logD/sqb -logBflow/sqb -logBcrude/sqb lam_e")
    rows = []
    for b in betas:
        r = run(b); r['beta'] = b; rows.append(r)
        sb = math.sqrt(b)
        w(f"{b:g} {r['Nx']} {r['n']} {r['Delta']:.6e} {r['Eh']:.6e} {r['Bflow']:.6e} {r['Bcrude']:.6e} "
          f"{r['Delta']/r['Bflow']:.4g} {math.log(r['Delta']/r['Bflow'])/math.log(b):.3f} "
          f"{-math.log(r['Delta'])/sb:.4f} {-math.log(r['Bflow'])/sb:.4f} {-math.log(r['Bcrude'])/sb:.4f} {r['le']:.6f}")
    res = []
    def pred(nm, ok, info=""):
        res.append(ok); w(f"{nm}: {'MET' if ok else 'FAILED'} {info}")
    pred("F0", all(abs(r['Eh'] - r['Delta']) / r['Delta'] < 1e-6 for r in rows),
         ",".join(f"{abs(r['Eh']-r['Delta'])/r['Delta']:.1e}" for r in rows))
    pred("F1", all(r['Bflow'] <= r['Delta'] * (1 + 1e-9) for r in rows), f"{sum(r['Bflow'] <= r['Delta']*(1+1e-9) for r in rows)}/{len(rows)}")
    pred("F2", all(r['Bcrude'] <= r['Bflow'] * (1 + 1e-9) for r in rows), f"{sum(r['Bcrude'] <= r['Bflow']*(1+1e-9) for r in rows)}/{len(rows)}")
    big = [r for r in rows if r['beta'] >= 64]
    pred("F3", all(math.log(r['Delta'] / r['Bflow']) <= 3 * math.log(r['beta']) for r in big),
         f"{sum(math.log(r['Delta']/r['Bflow']) <= 3*math.log(r['beta']) for r in big)}/{len(big)}")
    by = {r['beta']: r for r in rows}
    if all(b in by for b in (64.0, 1024.0, 4096.0)):
        d = [abs(-math.log(by[b]['Bflow']) / math.sqrt(b) - cs) for b in (64.0, 1024.0, 4096.0)]
        pred("F4", d[0] > d[1] > d[2], ",".join(f"{v:.4f}" for v in d))
        e = [(math.log(by[b]['Delta']) - math.log(by[b]['Bcrude'])) / math.sqrt(b) for b in (64.0, 256.0, 1024.0, 4096.0) if b in by]
        pred("F5", all(e[i] > e[i + 1] for i in range(len(e) - 1)), ",".join(f"{v:.4f}" for v in e))
    w(f"SUMMARY met={sum(res)} failed={len(res)-sum(res)}")
    out.close()


if __name__ == "__main__":
    main()
