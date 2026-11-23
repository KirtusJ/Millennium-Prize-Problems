"""assembly1d.py OUTFILE ETA BETA [BETA ...]  -- worker s1-chalA (T164).

Builds the ASSEMBLED lower bound of TUNNEL_LOWER_FULL.md (§2 Lemma C with the tent phi = max(phi_L, phi_R),
§3 mu placed inside phi, §4 chain x -> sigma x with balls, Corollary B of PATHS §2.1) for the 1D model and
compares it with the true splitting.  No randomness (deterministic linear algebra; seed n/a).

MODEL (grid version of the 1D continuum model; Lemma C and P'c hold on ANY measure space, so the grid model is a
legitimate instance of every abstract step):
  circle, midpoint grid x_i=(i+1/2)h, 4*nr points, h = pi/(2 nr); eps(a)=2 asinh|sin a|;
  kernel density k(d)=sqrt(beta/2pi) sum_{j=-2..2} exp(-beta (d+2 pi j)^2/2); T_ij = e^{-eps_i/2} k(x_i-x_j) e^{-eps_j/2} h;
  sigma: a -> a+pi.  Reduced to [0,pi/2] by the reflections a->-a, a->pi-a (even: all 4 images +; odd: images pi-y,
  pi+y with sign -). Reduced matrices are entrywise >= 0 (checked), so g, f are computed by repeated squaring with
  elementwise relative accuracy; Delta from the exact identity Delta<f,g> = 2<f,W g>, W = cross images.
  Grid: n = ceil(pi sqrt(beta)) chain steps, s = pi/n, nr = 4n, so h = s/8 (h sqrt(beta) ~ 1/8), ball radius r = 4h = s/2
  (9 grid points, v = 9h); consecutive ball points are within 2s.
ASSEMBLY INGREDIENTS (1D analogues): a_- = arcsin(sinh eta) (eps(a_-)=2 eta); Psi' = chi(a) sqrt(2(eps+eta)),
  chi = C^1 smoothstep 0 on [0,a_-/2] -> 1 on [a_-, pi]; Psi_tent(a)=min(Psi(d),Psi(pi-d)), d = dist(a, 0) in [0,pi];
  phi = mu exp(-sqrt(beta) Psi_tent); Omega = {d in [a_-, pi-a_-]} (contains pi/2 in its interior; NO cut there);
  R_well = complement; mu := min_{R_well} g exp(sqrt(beta) Psi)  (largest mu allowed by 'phi <= g on Omega^c').
  S = {d < a_-} U {d > pi - a_-} (the wells, sigma-invariant); path from x: z_k = x + k s + U(ball radius r).
  Corollary B (1D grid form): Delta >= Delta_LB := 2 int_S f^2 * v * Q_min / (n^2 sup_S g^2),
  Q_min >= T_min * (min_chain phi)^2, T_min = e^{-2 asinh 1} sqrt(beta/2pi) e^{-beta (2s)^2/2}.

PREDICATES (fixed before the first run):
 Q1 identity: at BETA <= 36 the identity Delta equals full-circle eigenvalue subtraction within tol
    = max(1e-8, 50 * 2.2e-16 * lam/Delta) (rounding amplified by cancellation; 50 = safety factor, my choice).
 Q2 reduced matrices entrywise >= 0 (exact sign check; tolerance 0).
 Q3 restriction norm: ||T_{Omega Omega}|| < lam_e  (and measured vs the bound e^{-2 eta}).
 Q4 subsolution: min_{x in Omega} (T phi)(x)/(lam_e phi(x)) >= 1 (per beta).  Expectation: holds for eta=0.25 at
    beta>=256 (TUNNEL_LOWER P8 saw 1.37-1.42); for small eta the O(H/sqrt(beta)) Taylor error may exceed e^eta - 1:
    a failure there is a finite-beta effect, not a defect.
 Q5 Lemma C conclusion: min_all g/phi >= 1 - 1e-9 (tolerance: elementwise relative float error of products of
    positive matrices, ~ 25 squarings * nr * 2.2e-16 < 1e-9).  Only asserted when Q3 and Q4 hold.
 Q6 the assembled bound is below the truth: Delta_LB <= Delta.
 Q7 exponent bookkeeping: | -log Delta_LB - [2 sqrt(b) Psi(pi/2) + 2(-log mu) + P(beta)] | <= 1e-6 where P is the
    explicit polynomial-factor term (identity check of the §4/(f) arithmetic; tolerance = float rounding).
 Q8 not 2c*: -log(Delta_LB)/sqrt(beta) < 2 c* - 1.5 at the largest beta (2c* = 9.21; the c* reading predicts
    about c*(eta) + 2(-log mu)/sqrt(beta) + O(log b/sqrt b)).
 Measured only: E_LB = -log Delta_LB/sqrt b, E_true = -log Delta/sqrt b, gap E_LB - E_true, (log g(0)-log g(pi/2))/sqrt b,
    the 'monotone reading' exponent 2 Psi(pi - a_-) + 2(-log mu)/sqrt b, and the min of T phi/(lam phi).
"""
import sys, json, math
import numpy as np

def kdens(d, beta):
    s = np.zeros_like(d, dtype=float)
    for j in range(-2, 3):
        s += np.exp(-beta * (d + 2 * np.pi * j) ** 2 / 2)
    return math.sqrt(beta / (2 * np.pi)) * s

def eps(a):
    return 2 * np.arcsinh(np.abs(np.sin(a)))

def topvec(M, nsq=30):
    """Perron vector of an entrywise nonnegative matrix by repeated squaring (elementwise-relative accurate)."""
    A = M / M.max()
    for _ in range(nsq):
        A = A @ A
        A /= A.max()
    v = A.sum(axis=1)
    v /= v.max()
    for _ in range(3):  # polish
        w = M @ v
        lam = w.max() / v[np.argmax(w)]
        v = w / w.max()
    w = M @ v
    i = np.argmax(v)
    lam = w[i] / v[i]
    return lam, v

def psi_funcs(eta):
    am = math.asin(math.sinh(eta))
    N = 200001
    a = np.linspace(0, np.pi, N)
    t = np.clip((a - am / 2) / (am / 2), 0, 1)
    chi = 3 * t ** 2 - 2 * t ** 3
    dpsi = chi * np.sqrt(2 * (eps(a) + eta))
    Psi = np.concatenate([[0], np.cumsum((dpsi[1:] + dpsi[:-1]) / 2 * np.diff(a))])
    return am, (lambda d: np.interp(d, a, Psi)), (lambda d: np.interp(d, a, dpsi))

def run(beta, eta, out):
    sb = math.sqrt(beta)
    n = math.ceil(np.pi * sb)
    s = np.pi / n
    nr = 4 * n
    h = np.pi / (2 * nr)
    x = (np.arange(nr) + 0.5) * h
    X, Y = np.meshgrid(x, x, indexing="ij")
    D = np.exp(-eps(x) / 2)
    Dm = np.outer(D, D) * h
    k0 = kdens(X - Y, beta) + kdens(X + Y, beta)
    kc = kdens(X - np.pi + Y, beta) + kdens(X - np.pi - Y, beta)
    Te = Dm * (k0 + kc)
    To = Dm * (k0 - kc)
    W = Dm * kc
    rec = {"beta": beta, "eta": eta, "n": n, "nr": nr, "h_sqrtb": h * sb}
    rec["Q2_minTo"] = float(To.min()); rec["Q2"] = bool(To.min() >= 0 and Te.min() >= 0)
    lam_e, g = topvec(Te)
    lam_o, f = topvec(np.clip(To, 0, None))
    Delta = 2 * (f @ (W @ g)) / (f @ g)
    rec.update(lam_e=float(lam_e), lam_o=float(lam_o), Delta=float(Delta), E_true=float(-math.log(Delta) / sb))
    if beta <= 36:  # Q1 direct full-circle check
        N = 4 * nr
        xf = (np.arange(N) + 0.5) * h
        Df = np.exp(-eps(xf) / 2)
        T = np.outer(Df, Df) * h * kdens(xf[:, None] - xf[None, :], beta)
        ev = np.linalg.eigh(T)
        V = ev[1]
        sh = np.roll(np.arange(N), -2 * nr)  # sigma: index + N/2
        par = np.array([V[sh, j] @ V[:, j] for j in range(N)])
        le = max(ev[0][par > 0.5]); lo = max(ev[0][par < -0.5])
        rec["Delta_direct"] = float(le - lo)
        tol = max(1e-8, 50 * 2.2e-16 * lam_e / Delta)
        rec["Q1_rel"] = float(abs(le - lo - Delta) / Delta); rec["Q1_tol"] = tol; rec["Q1"] = bool(rec["Q1_rel"] <= tol)
    # normalise to full circle: ||g||^2 = 4 sum g^2 h
    g = g / math.sqrt(4 * (g @ g) * h)
    f = f / math.sqrt(4 * (f @ f) * h)
    rec["logratio_g"] = float((math.log(g[0]) - math.log(g[-1])) / sb)
    am, Psi, dPsi = psi_funcs(eta)
    rec["a_minus"] = am
    d = x  # reduced coordinate is the distance to well 0, in [0, pi/2]
    Pt = np.minimum(Psi(d), Psi(np.pi - d))
    Omega = d >= am
    well = ~Omega
    mu = float(np.min(g[well] * np.exp(sb * Pt[well])))
    phi = mu * np.exp(-sb * Pt)
    rec["mlogmu_over_sqrtb"] = -math.log(mu) / sb
    # Q3
    TO = Te[np.ix_(Omega, Omega)]
    normO = float(np.linalg.eigvalsh(TO).max())
    rec.update(normTOO=normO, bound_e_m2eta=math.exp(-2 * eta), Q3=bool(normO < lam_e))
    # Q4
    ratio = (Te @ phi)[Omega] / (lam_e * phi[Omega])
    rec["Q4_min_ratio"] = float(ratio.min()); rec["Q4_argmin_d"] = float(d[Omega][np.argmin(ratio)])
    rec["Q4"] = bool(ratio.min() >= 1)
    # Q5
    rec["Q5_min_g_over_phi"] = float(np.min(g / phi))
    rec["Q5"] = bool(rec["Q5_min_g_over_phi"] >= 1 - 1e-9) if (rec["Q3"] and rec["Q4"]) else None
    # Corollary B
    S = d < am
    intS_f2 = float(4 * np.sum(f[S] ** 2) * h)
    supS_g2 = float(np.max(g[S]) ** 2)
    v = 9 * h
    Tmin = math.exp(-2 * math.asinh(1)) * sb / math.sqrt(2 * np.pi) * math.exp(-beta * (2 * s) ** 2 / 2)
    minphi = float(phi.min())
    Qmin = Tmin * minphi ** 2
    logLB = math.log(2 * intS_f2 * v * Qmin / (n ** 2 * supS_g2))
    rec.update(intS_f2=intS_f2, supS_g2=supS_g2, Tmin=Tmin, minphi=minphi, Delta_LB_log=logLB,
               E_LB=-logLB / sb)
    rec["Q6"] = bool(logLB <= math.log(Delta))
    Ppoly = -math.log(2 * intS_f2 * v * Tmin / (n ** 2 * supS_g2))
    pred = 2 * sb * float(Pt.max()) + 2 * (-math.log(mu)) + Ppoly
    rec["Q7_diff"] = float(abs(-logLB - pred)); rec["Q7"] = bool(rec["Q7_diff"] <= 1e-6 * max(1, abs(logLB)))
    rec["twoPsi_mid"] = 2 * float(Psi(np.pi / 2)); rec["twoPsi_mid_grid"] = 2 * float(Pt.max())
    rec["mono_exponent"] = 2 * float(Psi(np.pi - am)) + 2 * rec["mlogmu_over_sqrtb"]
    rec["Ppoly_over_sqrtb"] = Ppoly / sb
    return rec

if __name__ == "__main__":
    out = sys.argv[1]; eta = float(sys.argv[2]); betas = [float(b) for b in sys.argv[3:]]
    cstar = 4.6054132
    res = []
    with open(out, "x") as fh:
        for b in betas:
            r = run(b, eta, out)
            res.append(r)
            fh.write(json.dumps(r) + "\n"); fh.flush()
            print(json.dumps({k: r[k] for k in r if not isinstance(r[k], list)}), flush=True)
        big = res[-1]
        q8 = big["E_LB"] < 2 * cstar - 1.5
        summ = {"Q8_E_LB_at_max_beta": big["E_LB"], "Q8": bool(q8)}
        for q in ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7"]:
            vals = [r.get(q) for r in res if r.get(q) is not None]
            summ[q] = f"{sum(vals)}/{len(vals)} met"
        fh.write(json.dumps(summ) + "\n")
        print(json.dumps(summ))
