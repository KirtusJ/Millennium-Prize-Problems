"""kin.py -- challenge of LIMINF.md K1, K2 and (2.1) (brief point (a)).

K is diagonal in Peter-Weyl degrees (n1,n2) with eigenvalue kappa_n1 kappa_n2, so the operator
inequality (2.1)  1-K >= theta (-Lap/2beta) P + c P^perp  is EQUIVALENT to the scalar inequalities
LOW and HIGH below for every (n1,n2). (Pf, P^perp f orthogonal, both sides diagonal.)

kappa_n(beta) = I_{n+1}(beta)/I_1(beta) = prod_{nu=1}^n r_nu, r_nu = I_{nu+1}/I_nu.
r computed by backward recurrence r_{nu-1} = 1/(2nu/x + r_nu), started 4000+20*nu_max steps above
the largest needed index with the bound-midpoint; cross-checked by trapezoid quadrature of
I_nu(x)e^{-x} = (1/pi) int_0^pi e^{x(cos t-1)} cos(nu t) dt (periodic integrand, spectral accuracy).

PREDICATES (fixed before the first run):
 Q0  recurrence vs quadrature: |kappa_rec/kappa_quad - 1| <= 1e-9 on the cross-check set
     (beta in {10,100,1000}, n in {0,1,2,5,10,30}).  Tolerance: quadrature with 2^16 nodes is
     exact to ~1e-13 for these x; 1e-9 leaves room for products of ~30 ratios.
 Q1  K1 lower:  n(n+2)/(2(beta+n+1/2)) <= -ln kappa_n  for all n in [0, nmax]
 Q2  K1 upper:  -ln kappa_n <= n(n+3)/(2beta)            for all n in [0, nmax]
 Q3  LOW (K2):  for all 0<=n1,n2<=M: 1-k1k2 >= theta*(l1+l2)/(2beta)
 Q4  HIGH (K2): for all n1,n2 in [0,3M+10], max>=M+1: 1-k1k2 >= c
 Q5  limits: theta(m,1e8) within 1e-3 of 1/(1+m^2); c(m,1e8) within 1e-3 of 1-exp(-m^2/2)
     (tolerance: theta-1/(1+m^2) = O(m/sqrt(beta)) = O(1e-4) at beta=1e8)
 Tolerance for Q1-Q4: a case FAILS if lhs < rhs*(1-1e-10) - 1e-14 (double rounding over <=2000 summed logs
 is < 1e-12 relative). Cases with relative slack below 1e-8 are reported as "within-tol" separately.
 MEASURED ONLY: min over LOW set of (1-k1k2)/((l1+l2)/2beta) compared with theta and 1/(1+m^2);
     where on the LOW set the minimum sits (n small or n=M).
Per rule 4: for each (beta,m) the number of qualifying (n1,n2) in LOW and HIGH is reported.
Exit code 0 iff all predicates hold.
"""
import json, math, sys
import numpy as np

def ratios(x, numax):
    N = numax + 4000 + 20 * numax
    nu = N
    c = nu + 0.75
    r = x / (c + math.sqrt(c * c + x * x))
    out = np.empty(numax + 1)
    for nu in range(N, 0, -1):
        r = 1.0 / (2.0 * nu / x + r)      # this is r_{nu-1}
        if nu - 1 <= numax:
            out[nu - 1] = r
    return out  # out[nu] = I_{nu+1}/I_nu

def lnkappa(x, nmax):
    r = ratios(x, nmax)
    lk = np.zeros(nmax + 1)
    lk[1:] = np.cumsum(np.log(r[1:nmax + 1]))
    return lk

def Iscaled_quad(nu, x, K=2 ** 16):
    t = np.arange(K) * (2 * np.pi / K)
    return float(np.mean(np.exp(x * (np.cos(t) - 1.0)) * np.cos(nu * t)))

res = {"Q0": [], "cases": [], "Q5": []}
fails = {k: 0 for k in ["Q0", "Q1", "Q2", "Q3", "Q4", "Q5"]}
met = {k: 0 for k in fails}
within = {k: 0 for k in fails}

def bad(lhs, rhs):
    return lhs < rhs * (1 - 1e-10) - 1e-14

# Q0
for b in [10.0, 100.0, 1000.0]:
    lk = lnkappa(b, 40)
    I1 = Iscaled_quad(1, b)
    for n in [0, 1, 2, 5, 10, 30]:
        kq = Iscaled_quad(n + 1, b) / I1
        kr = math.exp(lk[n])
        rel = abs(kr / kq - 1)
        ok = rel <= 1e-9
        met["Q0" if ok else "Q0"] += ok; fails["Q0"] += (not ok)
        res["Q0"].append({"beta": b, "n": n, "k_rec": kr, "k_quad": kq, "rel": rel, "ok": ok})

betas = [10.0, 30.0, 100.0, 300.0, 1000.0, 3000.0, 1e4, 3e4, 1e5]
ms = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5]
for b in betas:
    nmaxall = 3 * int(0.5 * math.sqrt(b)) + 12
    lk = lnkappa(b, max(nmaxall, 400))
    n = np.arange(len(lk)); lam = n * (n + 2.0)
    # Q1,Q2 for all n
    lo = n * (n + 2.0) / (2 * (b + n + 0.5)); hi = n * (n + 3.0) / (2 * b)
    for i in range(len(lk)):
        for key, l, r in (("Q1", -lk[i], lo[i]), ("Q2", hi[i], -lk[i])):
            if bad(l, r): fails[key] += 1
            else:
                met[key] += 1
                if r > 0 and (l - r) / r < 1e-8: within[key] += 1
    for m in ms:
        M = int(math.floor(m * math.sqrt(b)))
        th = (b / (b + M + 0.5)) / (1 + m * m + 3 * m / math.sqrt(b))
        cc = 1 - math.exp(-(M + 1) * (M + 3) / (2 * (b + M + 1.5)))
        # LOW
        a = np.arange(M + 1)
        L1, L2 = np.meshgrid(a, a, indexing="ij")
        lhs = -np.expm1(lk[L1] + lk[L2])
        rhs = th * (lam[L1] + lam[L2]) / (2 * b)
        f3 = lhs < rhs * (1 - 1e-10) - 1e-14
        nq3 = lhs.size
        fails["Q3"] += int(f3.sum()); met["Q3"] += int(nq3 - f3.sum())
        mask = rhs > 0
        ratio = (lhs[mask] / ((lam[L1] + lam[L2])[mask] / (2 * b))) if mask.any() else np.array([np.nan])
        imin = int(np.argmin(ratio)) if mask.any() else -1
        where = (int(L1[mask][imin]), int(L2[mask][imin])) if mask.any() else None
        slack3 = float(np.min((lhs[mask] - rhs[mask]) / rhs[mask])) if mask.any() else None
        # HIGH
        nh = 3 * M + 10
        a = np.arange(nh + 1)
        H1, H2 = np.meshgrid(a, a, indexing="ij")
        hm = np.maximum(H1, H2) >= M + 1
        lhsH = -np.expm1(lk[H1[hm]] + lk[H2[hm]])
        f4 = lhsH < cc * (1 - 1e-10) - 1e-14
        fails["Q4"] += int(f4.sum()); met["Q4"] += int(hm.sum() - f4.sum())
        slack4 = float(np.min((lhsH - cc) / cc))
        res["cases"].append({"beta": b, "m": m, "M": M, "theta": th, "lim_theta": 1 / (1 + m * m),
                             "c": cc, "lim_c": 1 - math.exp(-m * m / 2),
                             "n_low": int(nq3), "fail_low": int(f3.sum()), "min_ratio_low": float(np.min(ratio)),
                             "argmin_low": where, "min_rel_slack_low": slack3,
                             "n_high": int(hm.sum()), "fail_high": int(f4.sum()), "min_rel_slack_high": slack4,
                             "min_high_value": float(np.min(lhsH))})
for m in ms:
    b = 1e8; M = int(math.floor(m * math.sqrt(b)))
    th = (b / (b + M + 0.5)) / (1 + m * m + 3 * m / math.sqrt(b))
    cc = 1 - math.exp(-(M + 1) * (M + 3) / (2 * (b + M + 1.5)))
    ok = abs(th - 1 / (1 + m * m)) <= 1e-3 and abs(cc - (1 - math.exp(-m * m / 2))) <= 1e-3
    met["Q5"] += ok; fails["Q5"] += (not ok)
    res["Q5"].append({"m": m, "theta": th, "lim": 1 / (1 + m * m), "c": cc, "limc": 1 - math.exp(-m * m / 2), "ok": ok})
res["met"] = met; res["failed"] = fails; res["within_tol"] = within
out = sys.argv[1]
with open(out, "x") as fh:
    json.dump(res, fh, indent=1)
print("met", met); print("failed", fails); print("within", within)
for c in res["cases"]:
    print(f"b={c['beta']:>8} m={c['m']:.2f} M={c['M']:>3} th={c['theta']:.4f} minratioL={c['min_ratio_low']:.4f} at {c['argmin_low']} slackL={c['min_rel_slack_low']} nL={c['n_low']} nH={c['n_high']} slackH={c['min_rel_slack_high']:.3e}")
sys.exit(0 if sum(fails.values()) == 0 else 1)
