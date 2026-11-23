"""tube_ratio.py -- worker p1-lower2 (T146). Monte Carlo of (T phi)(x)/phi(x) on SU(2)^2 along the valley tube.

MODEL. U = x0 + u unit quaternion; step U -> U g, g ~ density prop. exp(beta cos theta) w.r.t. Haar (exact sampler:
t = 1 - cos theta ~ Gamma(3/2, 1/beta) accepted w.p. sqrt(1 - t/2)). One step of K = K1 K2 moves both links independently.
V = 2 beta |u1 x u2|^2, (T phi)(x) = e^{-V(x)/2} E[e^{-V(x')/2} phi(x')].
eps(s) = 2 asinh s, alpha(S) = 2 S sqrt(1+S^2), S^2 = sin^2 a1 + sin^2 a2, q = |u1 x u2|^2 / S^2.

TEST FUNCTIONS.
 (core)  phi0 = exp(-sqrt(beta) Psi0(a1)) * G,     G = exp(-beta alpha(S) q / 2),  Psi0' = sqrt(2 eps(sin a1)).
         prediction: -log R = eps(S) - eps(sin a1) =: pred  (Psi0'^2/2 = eps(sin a1)).
 (cut)   phi1 = exp(-sqrt(beta) (Psi_eta(a1))) * (G - c1)_+ * (E - c2)_+,  E = exp(-sqrt(beta) Theta(a2)),
         Psi_eta' = sqrt(2 (eps(sin a1) + eta)), Theta(a) = th0 (sqrt(a^2 + l^2) - l),
         eta = 0.25, th0 = 1, l = 0.02, r0 = 0.1, c1 = exp(-M^2) with M = 2, c2 = exp(-sqrt(beta) Theta(r0)).
         This is the cut-off subsolution of TUNNEL_LOWER2.md Lemma S4; the claim is T phi1 >= lambda phi1 on its support
         (lambda <= 1), i.e. R1 >= 1.

POINTS. U1 = cos a1 + sin a1 e3; U2 = exp(c e3 + d e1), d = y/sqrt(beta).
 core grid: a1 in {0.5, pi/2, 2.5}, c in {0, 0.1}, y in {0, 1}  (12 points; same as the child's T147 points).
 cut grid:  a1 in {0.5, 1.2, pi/2}, c in {0, 0.05, 0.09}, y in {0, 1.0, edge}, edge = 0.95 * the q-edge where G = c1.

PREDICATES (fixed before the first run).
 Q1 sampler: |mean cos theta - (I0/I1 - 2/beta)| <= 4 SE at beta = 256, 1024, 4096 (SE = sample std/sqrt(n); 4 SE gives a
    false-alarm rate ~6e-5 per case).
 Q2 (expectation) core: |diff| := |-log R - pred| <= 3/sqrt(beta) + 4 SE at every core point and beta.
    Source of tolerance: the claimed error is O(beta^{-1/2}) (curvature, Psi'' and alpha(S') - alpha(S) terms);
    the constant 3 is my guess, not derived.
 Q3 (expectation) core: worst |diff| at beta = 4096 is <= 0.5 * worst |diff| at beta = 256 (beta^{-1/2} would give 0.25).
 Q4 (claim of Lemma S4) cut: R1 >= 1 at every cut point with phi1 > 0, beta in {1024, 4096} (tolerance: R1 - 4 SE >= 1).
    beta = 256 is measured only (o(1) errors are not small there).
Fixed seed 20261123. Output file results_<tag>.txt opened with mode "x".
"""
import sys, math
import numpy as np


def ive(nu, z, m=200001):
    """exp(-z) I_nu(z) = (1/pi) int_0^pi exp(z(cos t - 1)) cos(nu t) dt (trapezoid; periodic, spectrally accurate)."""
    t = np.linspace(0, math.pi, m)
    f = np.exp(z * (np.cos(t) - 1)) * np.cos(nu * t)
    return float((f.sum() - (f[0] + f[-1]) / 2) * (t[1] - t[0]) / math.pi)

SEED = 20261123


def qmul(p, q):
    a0, a = p[..., 0], p[..., 1:]
    b0, b = q[..., 0], q[..., 1:]
    r0 = a0 * b0 - np.sum(a * b, axis=-1)
    r = a0[..., None] * b + b0[..., None] * a + np.cross(a, b)
    return np.concatenate([r0[..., None], r], axis=-1)


def sample_g(rng, beta, n):
    out = []
    got = 0
    while got < n:
        m = int((n - got) * 1.3) + 100
        t = rng.gamma(1.5, 1.0 / beta, size=m)
        ok = (t < 2) & (rng.random(m) < np.sqrt(np.clip(1 - t / 2, 0, 1)))
        out.append(t[ok])
        got += ok.sum()
    t = np.concatenate(out)[:n]
    c = 1 - t
    s = np.sqrt(np.clip(1 - c * c, 0, None))
    v = rng.normal(size=(n, 3))
    v /= np.linalg.norm(v, axis=1)[:, None]
    return np.concatenate([c[:, None], s[:, None] * v], axis=1)


def eps(s):
    return 2 * np.arcsinh(s)


def alpha(S):
    return 2 * S * np.sqrt(1 + S * S)


GL_x, GL_w = np.polynomial.legendre.leggauss(12)


def dpsi(a, b, eta):
    """int_a^b sqrt(2(eps(sin t)+eta)) dt, vectorised (a scalar, b array)."""
    mid = (a + b) / 2
    half = (b - a) / 2
    t = mid[..., None] + half[..., None] * GL_x
    return half * np.sum(GL_w * np.sqrt(2 * (eps(np.sin(t)) + eta)), axis=-1)


def invariants(U1, U2):
    a1 = np.arccos(np.clip(U1[..., 0], -1, 1))
    a2 = np.arccos(np.clip(U2[..., 0], -1, 1))
    cr = np.cross(U1[..., 1:], U2[..., 1:])
    w2 = np.sum(cr * cr, axis=-1)
    S2 = np.sin(a1) ** 2 + np.sin(a2) ** 2
    return a1, a2, w2, S2


def point(a1, c, d):
    U1 = np.array([math.cos(a1), 0, 0, math.sin(a1)])
    r = math.hypot(c, d)
    if r == 0:
        U2 = np.array([1.0, 0, 0, 0])
    else:
        U2 = np.array([math.cos(r), math.sin(r) * d / r, 0, math.sin(r) * c / r])
    return U1, U2


def Theta(a, th0, l):
    return th0 * (np.sqrt(a * a + l * l) - l)


def ratios(beta, U1, U2, g1, g2, mode, par):
    sb = math.sqrt(beta)
    a1, a2, w2, S2 = invariants(U1, U2)
    V = 2 * beta * w2
    U1p = qmul(U1[None, :], g1)
    U2p = qmul(U2[None, :], g2)
    b1, b2, w2p, S2p = invariants(U1p, U2p)
    Vp = 2 * beta * w2p
    qx, qp = w2 / S2, w2p / S2p
    Gx = math.exp(-beta * alpha(math.sqrt(S2)) * qx / 2)
    Gp = np.exp(-beta * alpha(np.sqrt(S2p)) * qp / 2)
    if mode == "core":
        tilt = np.exp(-sb * dpsi(np.full_like(b1, a1), b1, 0.0))
        w = math.exp(-V / 2) * np.exp(-Vp / 2) * tilt * Gp / Gx
        return w, (eps(math.sqrt(S2)) - eps(math.sin(a1))), 1.0
    eta, th0, l, r0, M = par
    c1 = math.exp(-M * M)
    c2 = math.exp(-sb * Theta(r0, th0, l))
    Ex = math.exp(-sb * Theta(a2, th0, l))
    Ep = np.exp(-sb * Theta(b2, th0, l))
    fx = max(Gx - c1, 0) * max(Ex - c2, 0)
    if fx <= 0:
        return None, None, 0.0
    tilt = np.exp(-sb * dpsi(np.full_like(b1, a1), b1, eta))
    fp = np.clip(Gp - c1, 0, None) * np.clip(Ep - c2, 0, None)
    w = math.exp(-V / 2) * np.exp(-Vp / 2) * tilt * fp / fx
    return w, None, fx


def main(tag, n):
    out = open(f"results_{tag}.txt", "x")
    def P(*a):
        s = " ".join(str(x) for x in a)
        print(s); out.write(s + "\n"); out.flush()
    P(f"# tube_ratio.py tag={tag} n={n} seed={SEED}")
    betas = [256, 1024, 4096]
    res = {"Q1": [], "Q2": [], "Q3": [], "Q4": []}
    worst = {}
    par = (0.25, 1.0, 0.02, 0.1, 2.0)
    for beta in betas:
        rng = np.random.default_rng(SEED + beta)
        g1 = sample_g(rng, beta, n)
        g2 = sample_g(rng, beta, n)
        mc = np.concatenate([g1[:, 0], g2[:, 0]])
        exact = ive(0, beta) / ive(1, beta) - 2 / beta
        se = mc.std() / math.sqrt(len(mc))
        ok = abs(mc.mean() - exact) <= 4 * se
        res["Q1"].append(ok)
        P(f"Q1 beta={beta} mean_cos={mc.mean():.8f} exact={exact:.8f} SE={se:.2e} {'MET' if ok else 'FAILED'}")
        sb = math.sqrt(beta)
        worst[beta] = 0.0
        for a1 in [0.5, math.pi / 2, 2.5]:
            for c in [0.0, 0.1]:
                for y in [0.0, 1.0]:
                    U1, U2 = point(a1, c, y / sb)
                    w, pred, _ = ratios(beta, U1, U2, g1, g2, "core", None)
                    R = w.mean(); se = w.std() / math.sqrt(n) / R
                    d = -math.log(R) - pred
                    ok = abs(d) <= 3 / sb + 4 * se
                    res["Q2"].append(ok)
                    worst[beta] = max(worst[beta], abs(d))
                    P(f"Q2 beta={beta} a1={a1:.4f} c={c} y={y} -logR={-math.log(R):.5f} pred={pred:.5f} diff={d:+.5f} "
                      f"sqrtb*diff={sb*d:+.3f} SE={se:.1e} {'MET' if ok else 'FAILED'}")
        # cut-off subsolution
        eta, th0, l, r0, M = par
        for a1 in [0.5, 1.2, math.pi / 2]:
            for c in [0.0, 0.05, 0.09]:
                S = math.sqrt(math.sin(a1) ** 2 + math.sin(c) ** 2)
                qedge = 2 * M * M / (beta * alpha(S))  # G = c1 at q = qedge
                yedge = 0.95 * math.sqrt(qedge) * S / math.sin(a1) * sb  # approx d*sqrt(beta) giving q ~ 0.95^2 qedge
                for y in [0.0, 1.0, yedge]:
                    U1, U2 = point(a1, c, y / sb)
                    w, _, fx = ratios(beta, U1, U2, g1, g2, "cut", par)
                    if w is None:
                        P(f"Q4 beta={beta} a1={a1:.4f} c={c} y={y:.3f} phi1=0 (outside support) skipped")
                        continue
                    R = w.mean(); se = w.std() / math.sqrt(n) / R
                    if beta >= 1024:
                        ok = R * (1 - 4 * se) >= 1
                        res["Q4"].append(ok); lab = "MET" if ok else "FAILED"
                    else:
                        lab = "measured-only"
                    P(f"Q4 beta={beta} a1={a1:.4f} c={c} y={y:.3f} R1={R:.5f} log R1={math.log(R):+.5f} SE={se:.1e} {lab}")
    ok = worst[4096] <= 0.5 * worst[256]
    res["Q3"].append(ok)
    P(f"Q3 worst|diff|: " + ", ".join(f"beta={b}: {worst[b]:.5f}" for b in betas) + f" {'MET' if ok else 'FAILED'}")
    for k, v in res.items():
        P(f"SUMMARY {k}: met {sum(v)}, failed {len(v) - sum(v)} of {len(v)}")
    out.close()
    return 0


if __name__ == "__main__":
    tag = sys.argv[1]
    n = int(sys.argv[2])
    sys.exit(main(tag, n))
