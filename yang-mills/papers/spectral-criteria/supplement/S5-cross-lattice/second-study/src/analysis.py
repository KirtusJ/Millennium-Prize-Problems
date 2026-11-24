"""e2-cross analysis (worker under T231).  Usage: python3 -I src/analysis.py COARSE FINE OUTFILE
COARSE/FINE = ensemble labels under results/ (c2,f2) or (c4,f4).  OUTFILE opened with mode "x".

PREDICATES (fixed before any production run; identical text in src/analysis_predicates.txt):
Split: TRAIN = chains with i%4 in {0,1}; HELD = i%4 in {2,3} (each half 4 cold + 4 hot).
P1 thermalisation (per ensemble): |mean plaq(hot) - mean plaq(cold)| < 3 * combined SE (chain scatter, 8 per group)
   AND |first-half - second-half production mean| < 3 SE (chain scatter of the per-chain difference).
   Tolerance 3 SE: my choice (~0.3% two-sided false alarm per test under normality).
P2 autocorrelation: integrated autocorrelation time (Sokal window c=6) of per-config time-averaged Pa1 and Wa1,
   pooled over chains, in measurement units, < 25 (= 500/20).
P3 (measured only) hot vs cold single-observable R within 3 combined SE; count of disagreements reported.
Main measurement: numbers only. fine-optimal f (min R_fine on TRAIN), coarse-optimal f (min R_coarse on TRAIN),
   ratio-optimal f (min E_fine/E_coarse on TRAIN, both lattices' TRAIN), standardized span, eigen cutoff 1e-10 relative.
   Frozen, evaluated on HELD of both lattices; delete-one-chain jackknife within each lattice, errors combined in
   quadrature (independent lattices).
Interpretation rule: a frozen eligible test with held-out R_fine/R_coarse < x at both temporal circumferences defeats
   an energy comparison with constant c >= x for that pair; it does NOT defeat the spectral deficit inequality.
   "Significantly below y": ratio + 2 SE < y (my choice).
"""
import sys, glob, numpy as np

ROOT = "/home/user/z4-workers/e2-cross/results/"
NAMES = ["W_x", "W_y", "W_z", "P_yz", "P_xz", "P_xy", "R_yz", "R_xz", "R_xy", "Pa1^2", "Wa1^2", "Wa1*Pa1",
         "Ra1^2", "Pe^2", "We^2", "sumW_iP_i"]
K = 16


def load(label):
    chains = []
    for i in range(16):
        f = f"{ROOT}{label}/chain-{i}.txt"
        L = open(f).read().splitlines()
        assert L[-1] == "END", f
        d = {"S00": np.zeros((K, K)), "SL": np.zeros((K, K))}
        M = []
        for l in L:
            p = l.split(",")
            if p[0] == "NS": d["NS"] = float(p[1])
            elif p[0] == "S1": d["S1"] = np.array(p[1:], float)
            elif p[0] in ("S00", "SL"): d[p[0]][int(p[1])] = np.array(p[2:], float)
            elif p[0] == "M": M.append(np.array(p[2:], float))
        d["M"] = np.array(M)  # col0 plaq, cols 1.. obs time-averaged
        d["i"] = i
        chains.append(d)
    return chains


def mats(chains):
    ns = sum(c["NS"] for c in chains)
    mu = sum(c["S1"] for c in chains) / ns
    C0 = sum(c["S00"] for c in chains) / ns - np.outer(mu, mu)
    CL = sum(c["SL"] for c in chains) / ns - np.outer(mu, mu)
    return C0, (CL + CL.T) / 2


def quant(a, chains):
    C0, CL = mats(chains)
    v = a @ C0 @ a; e = a @ (C0 - CL) @ a
    return v, e, e / v


def jk(a, chains, fn):
    n = len(chains)
    full = fn(quant(a, chains))
    rep = np.array([fn(quant(a, chains[:k] + chains[k + 1:])) for k in range(n)])
    return full, np.sqrt((n - 1) / n * ((rep - rep.mean()) ** 2).sum()), rep


def basis(C0):
    s = np.sqrt(np.diag(C0))
    Cn = C0 / np.outer(s, s)
    w, U = np.linalg.eigh(Cn)
    keep = w > 1e-10 * w.max()
    B = (U[:, keep] / np.sqrt(w[keep])) / s[:, None]  # columns: C0-whitened directions in original units
    return B, int(keep.sum())


def min_gen(A, Bm):
    """min a^T A a / a^T Bm a over span where Bm is well-conditioned (whitened basis of Bm)."""
    T, k = basis(Bm)
    M = T.T @ A @ T
    w, U = np.linalg.eigh((M + M.T) / 2)
    a = T @ U[:, 0]
    return a / np.abs(a).max(), w[0], k


def tau_int(series_list):
    x = [s - np.mean(np.concatenate(series_list)) for s in series_list]
    n = min(len(s) for s in x)
    c0 = np.mean([np.mean(s * s) for s in x])
    tau = 0.5
    for t in range(1, n // 2):
        ct = np.mean([np.mean(s[:-t] * s[t:]) for s in x])
        tau += ct / c0
        if t >= 6 * tau: return tau, t
    return tau, n // 2


def thermal(ch):
    pl = np.array([c["M"][:, 0].mean() for c in ch])
    hot, cold = pl[1::2], pl[0::2]
    se = np.hypot(hot.std(ddof=1) / np.sqrt(len(hot)), cold.std(ddof=1) / np.sqrt(len(cold)))
    d1 = hot.mean() - cold.mean()
    h = len(ch[0]["M"]) // 2
    dd = np.array([c["M"][:h, 0].mean() - c["M"][h:, 0].mean() for c in ch])
    se2 = dd.std(ddof=1) / np.sqrt(len(dd))
    return d1, se, abs(d1) < 3 * se, dd.mean(), se2, abs(dd.mean()) < 3 * se2, pl.mean()


def main():
    cl, fl, out = sys.argv[1:4]
    o = open(out, "x")
    def P(*a):
        s = " ".join(str(x) for x in a); print(s); o.write(s + "\n")
    C, F = load(cl), load(fl)
    tr = lambda ch: [c for c in ch if c["i"] % 4 in (0, 1)]
    he = lambda ch: [c for c in ch if c["i"] % 4 in (2, 3)]
    fails = []
    P(f"# analysis coarse={cl} fine={fl}")
    for lab, ch in ((cl, C), (fl, F)):
        d1, se, ok1, d2, se2, ok2, pm = thermal(ch)
        P(f"P1 {lab}: plaq={pm:.6f} hot-cold={d1:+.2e}+-{se:.1e} {'met' if ok1 else 'FAILED'}; "
          f"half1-half2={d2:+.2e}+-{se2:.1e} {'met' if ok2 else 'FAILED'}")
        if not ok1: fails.append(f"P1a {lab}")
        if not ok2: fails.append(f"P1b {lab}")
        for nm, cols in (("Pa1", [4, 5, 6]), ("Wa1", [1, 2, 3])):
            t, w = tau_int([c["M"][:, cols].mean(1) for c in ch])
            ok = t < 25
            P(f"P2 {lab} {nm}: tau_int={t:.2f} (window {w}) {'met' if ok else 'FAILED'}")
            if not ok: fails.append(f"P2 {lab} {nm}")
        # P3 hot/cold single-observable R
        dis = 0
        for j in range(K):
            a = np.eye(K)[j]
            rh = jk(a, ch[1::2], lambda q: q[2]); rc = jk(a, ch[0::2], lambda q: q[2])
            if abs(rh[0] - rc[0]) > 3 * np.hypot(rh[1], rc[1]): dis += 1
        P(f"P3 {lab}: hot/cold single-observable R disagreements (>3SE): {dis} of {K} (measured only)")
    # training
    C0c, CLc = mats(tr(C)); C0f, CLf = mats(tr(F))
    af, rf, kf = min_gen(C0f - CLf, C0f)
    ac, rc, kc = min_gen(C0c - CLc, C0c)
    # ratio-optimal: min E_f/E_c ; E_c must be positive definite on the span
    ar, rr, kr = min_gen(C0f - CLf, C0c - CLc)
    P(f"TRAIN: fine-opt R_f={rf:.5f} (rank {kf}); coarse-opt R_c={rc:.5f} (rank {kc}); ratio-opt E_f/E_c={rr:.5f} (rank {kr})")
    tests = [("fine-opt", af), ("coarse-opt", ac), ("ratio-opt", ar)]
    tests += [(NAMES[j], np.eye(K)[j]) for j in range(K)]
    tests += [("Wa1", np.r_[np.ones(3) / 3, np.zeros(13)]), ("Pa1", np.r_[0, 0, 0, np.ones(3) / 3, np.zeros(10)]),
              ("Ra1", np.r_[np.zeros(6), np.ones(3) / 3, np.zeros(7)]),
              ("PE:P_yz-P_xz", np.r_[0, 0, 0, 1, -1, np.zeros(11)]), ("WE:W_x-W_y", np.r_[1, -1, np.zeros(14)])]
    for nm, a in tests[:3]:
        P(f"COEF {nm}: " + " ".join(f"{v:+.4g}" for v in a))
    P("HELD-OUT: test | R_fine +- se | R_coarse +- se | R_f/R_c +- se | E_f/E_c +- se | Var_f/Var_c +- se")
    rows = []
    hf, hc = he(F), he(C)
    for nm, a in tests:
        Rf = jk(a, hf, lambda q: q[2]); Rc = jk(a, hc, lambda q: q[2])
        Vf = jk(a, hf, lambda q: q[0]); Vc = jk(a, hc, lambda q: q[0])
        Ef = jk(a, hf, lambda q: q[1]); Ec = jk(a, hc, lambda q: q[1])
        rat = Rf[0] / Rc[0]; srat = rat * np.hypot(Rf[1] / Rf[0], Rc[1] / Rc[0])
        er = Ef[0] / Ec[0]; ser = abs(er) * np.hypot(Ef[1] / Ef[0], Ec[1] / Ec[0])
        vr = Vf[0] / Vc[0]; svr = vr * np.hypot(Vf[1] / Vf[0], Vc[1] / Vc[0])
        rows.append((nm, rat, srat))
        P(f"{nm:14s} | {Rf[0]:.5f} +- {Rf[1]:.5f} | {Rc[0]:.5f} +- {Rc[1]:.5f} | {rat:.4f} +- {srat:.4f} | "
          f"{er:.4g} +- {ser:.2g} | {vr:.4g} +- {svr:.2g}")
    m = min(rows, key=lambda r: r[1])
    P(f"SMALLEST held-out R_f/R_c: {m[0]} {m[1]:.4f} +- {m[2]:.4f}")
    for y in (1.0, 0.5, 0.1):
        sig = [r[0] for r in rows if r[1] + 2 * r[2] < y]
        P(f"significantly below {y}: {len(sig)} tests {sig}")
    P(f"FAILED predicates: {fails if fails else 'none'}")
    # per-chain held-out moment matrices summary for the frozen optima (for audit / child)
    import os; assert not os.path.exists(out + ".coef")
    np.savetxt(out + ".coef", np.array([af, ac, ar]), header="rows: fine-opt, coarse-opt, ratio-opt (coefficients on x0..x15)")
    o.close()


if __name__ == "__main__":
    main()
