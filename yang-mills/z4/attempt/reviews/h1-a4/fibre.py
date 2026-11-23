"""fibre.py -- h1-a4, item (b): M1 (1)  I - K_j + V_ij >= c r  on one link fibre.

Reduction: V_ij = 2 beta r^2 rho^2, rho = |z2| = sin(eta) in Hopf coordinates
v = (cos eta e^{i phi1}, sin eta e^{i phi2}) with the axis e of U_i as the complex unit.
V and K_j are invariant under the torus U(1)xU(1) (left/right multiplication by
exp(alpha e)); K_j is positivity improving, so the lowest eigenvalue lies in the
torus-invariant sector.  Reduced kernel w.r.t. prob. measure 2 sin(eta)cos(eta)d eta:
  k(eta,eta') = beta/(2 I_1(beta)) I_0(beta c c') I_0(beta s s').
Midpoint grid, N points on (0, pi/2). Bessel functions from besselnp.py (numpy only;
scipy is not installed; fixed before the first recorded run that executed).

PREDICATES (fixed before first run):
 F1  max |K1 - 1| < 1e-6 for each beta (tolerance: quadrature error of a smooth
     kernel of width beta^-1/2 on a grid of spacing ~8e-4; 1e-6 is my expectation).
 F2  for each beta in {64,256} and every r in the grid with h <= r <= 1:
     mu(r)/r >= 0.2, mu = lowest eigenvalue of I-K+V (expectation: transverse
     oscillator gives ~2 for intermediate r; 0.2 leaves a factor 10).  Per-case count reported.
 F3  uniformity: min_{h<=r<=1} mu/r at beta=256 >= 0.5 * the same at beta=64.
 F4  ground-state identity, exact algebra: for f = phi*psi,
     <f,(I-K+V)f> = sum w psi^2 phi (I-K+V)phi + 1/2 sum w_a k_ab w_b phi_a phi_b (psi_a-psi_b)^2,
     relative error < 1e-10 on 20 random psi (seed 7) (double rounding over N^2 terms).
 F5  telescoping with B=(1+V)^{-1}K, phi = sum_{a<m} B^a 1, m = ceil(8/r):
     (I+V-K)phi = (1+V)(1 - B^m 1) pointwise, max rel error < 1e-10.
 F6  min_x [(I-K+V)phi/phi](x) <= mu(r) * (1+1e-10)  (ground-state lower bound valid).
 M   measured only: kappa_eff = 1 - max B^m 1, kappa_eff/m vs mu, and mu/r for r < h.
"""
import json, sys, numpy as np
from besselnp import ive0, ive1
np.random.seed(7)
out = open(sys.argv[1], "x")
N = 2000
res = {"N": N, "cases": []}
fails = []
def kernel(beta):
    eta = (np.arange(N)+0.5)*(np.pi/2)/N
    d = (np.pi/2)/N
    c, s = np.cos(eta), np.sin(eta)
    A = np.outer(c, c); Bm = np.outer(s, s)
    k = beta/(2*ive1(beta)) * ive0(beta*A)*ive0(beta*Bm)*np.exp(beta*(A+Bm-1))
    w = 2*s*c*d
    return eta, s, k, w
minratio = {}
for beta in [64, 256]:
    h = beta**(-1/3)
    eta, s, k, w = kernel(beta)
    Kop = k*w[None, :]                     # (K f)_a = sum_b k_ab w_b f_b
    rs = np.abs(Kop.sum(1)-1).max()
    ok1 = rs < 1e-6; res["cases"].append({"beta": beta, "F1_rowsum_err": rs, "F1": bool(ok1)})
    if not ok1: fails.append(f"F1 beta={beta}")
    sq = np.sqrt(w)
    S = sq[:, None]*k*sq[None, :]          # symmetric form of K
    rgrid = sorted(set(list(np.geomspace(h/8, 1, 25)) + [h, 1.0]))
    rows = []
    for r in rgrid:
        V = 2*beta*r**2*s**2
        A = np.eye(N) - S + np.diag(V)
        mu = np.linalg.eigvalsh(A)[0]
        row = {"r": r, "r_over_h": r/h, "mu": mu, "mu_over_r": mu/r}
        if r >= h*(1-1e-12):
            m = int(np.ceil(8/r))
            # killed walk
            Bop = Kop/(1+V)[:, None]
            u = np.ones(N); phi = np.zeros(N)
            for a in range(m):
                phi += u; u = Bop@u
            Bm1 = u
            lhs = (1+V)*phi - Kop@phi
            rhs = (1+V)*(1-Bm1)
            e5 = np.abs(lhs-rhs).max()/np.abs(rhs).max()
            ratio_min = (lhs/phi).min()
            row.update({"m": m, "kappa_eff": 1-Bm1.max(), "kappa_eff_over_m": (1-Bm1.max())/m,
                        "F5_err": e5, "F5": bool(e5 < 1e-10),
                        "supersol_min_ratio": ratio_min, "F6": bool(ratio_min <= mu*(1+1e-10))})
            if not row["F5"]: fails.append(f"F5 beta={beta} r={r}")
            if not row["F6"]: fails.append(f"F6 beta={beta} r={r}")
            # F4 ground-state identity on random psi
            errs = []
            for t in range(20 if r == h else 3):
                psi = np.random.randn(N); f = phi*psi
                Af = (1+V)*f - Kop@f
                L = np.sum(w*f*Af)
                Aphi = (1+V)*phi - Kop@phi
                R1 = np.sum(w*psi**2*phi*Aphi)
                D = (psi[:, None]-psi[None, :])**2
                R2 = 0.5*np.sum((w[:, None]*k*w[None, :])*np.outer(phi, phi)*D)
                errs.append(abs(L-(R1+R2))/abs(L))
            row["F4_err"] = max(errs); row["F4"] = bool(max(errs) < 1e-10)
            if not row["F4"]: fails.append(f"F4 beta={beta} r={r}")
            row["F2"] = bool(mu/r >= 0.2)
            if not row["F2"]: fails.append(f"F2 beta={beta} r={r}")
        rows.append(row)
        print(beta, f"r/h={r/h:.3f} mu={mu:.5g} mu/r={mu/r:.4f}", {k2: row[k2] for k2 in row if k2 in ("m", "kappa_eff", "supersol_min_ratio", "F4_err", "F5_err")}, flush=True)
    q = [x["mu_over_r"] for x in rows if x["r"] >= h*(1-1e-12)]
    minratio[beta] = min(q)
    res["cases"].append({"beta": beta, "rows": rows, "F2_count_met": sum(x.get("F2", False) for x in rows),
                         "F2_count_cases": len(q), "min_mu_over_r": min(q)})
ok3 = minratio[256] >= 0.5*minratio[64]
res["F3"] = {"min64": minratio[64], "min256": minratio[256], "met": bool(ok3)}
if not ok3: fails.append("F3")
res["fails"] = fails
json.dump(res, out, indent=1, default=float); out.close()
print("FAILS:", fails); sys.exit(1 if fails else 0)
