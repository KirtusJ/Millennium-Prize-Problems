"""b2-matrix analysis. usage: python3 analyze.py <tag>  -> results/<tag>/analysis.json and analysis.txt (mode 'x')

Data per stream s (z1mx): X_s (M x n marks), Dc_s (24 x n x n: mean over measurements of (X'-X'')(X'-X'')^T/2
for colour c, X', X'' two independent exact conditional refreshes of colour c, as for f1, f4 in fixed.md).
Estimators (fixed before the first run):
  C(S) = pooled covariance over the streams of set S, centred by the pooled mean of S, ddof = 0 (G4's plug-in).
  D(S) = mean over streams in S of (1/24) sum_c Dc_s = (1/48) sum_c E[(X'-X'')(X'-X'')^T]   (equal M per stream).
  TRAIN = streams 0..15, HELD = 16..31. Generalised eigenproblem D w = lambda C w on TRAIN:
  C = V diag(l) V^T; keep directions with l > 1e-10 * max(l) (regularisation by truncation; reported);
  whiten, symmetric eigh, smallest eigenvalue, w normalised to max |w_k| = 1.
  Held-out quotient q = w^T D(HELD) w / w^T C(HELD) w; delete-one-stream jackknife over HELD streams,
  err = sqrt((n-1)/n sum (q_i - q_bar)^2), C re-centred in each deletion.
  Single-mark quotients D_kk/C_kk on HELD (same jackknife); best single = smallest held-out single quotient.
  Ratio optimum / best single: paired jackknife over HELD.
Predicates (fixed before the first run):
  A1 every per-stream D_s is symmetric positive semidefinite (min eigenvalue >= -1e-12 * trace; rounding).
  A2 (expectation) held-out optimum < held-out best single mark by more than 2 jackknife sigma of the ratio
     (i.e. the span helps).  Kept if it fails; a failure is an outcome, not a defect.
  A3 (expectation) held-out quotient of w_train lies within 3 sigma of the training eigenvalue OR above it
     (training eigenvalue is biased low); a held-out value BELOW train - 3 sigma would indicate a defect in my code.
  A4 thermalisation: with w fixed, quotient on the 16 cold vs 16 hot streams (all 32) differ by at most
     2 sigma_d, sigma_d = 2 * jackknife err of the 32-stream pooled quotient (prior record's T2 convention);
     same for f1 = B.g00 and f4 = mean of B.g00..B.g11.
  A5 (delta = 0 only) f1, f4 ratios on all 32 streams vs prior large run (24 x 1152): r1 .0613(4), r4 .0469(5);
     |z| <= 2 with combined errors.
Also reported: condition number of C(TRAIN), C(HELD); per-colour shares of w^T D_c w on HELD; swap test
(train on HELD, evaluate on TRAIN); in-sample minimum over all 32 streams.
"""
import json, sys
import numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve().parent
BETA = 3.276133577

def load(tag):
    d = ROOT / "results" / tag
    Xs, Dcs = [], []
    for i in range(32):
        X = np.loadtxt(d / f"s{i}.X.csv", delimiter=",", skiprows=1)
        lines = [l for l in (d / f"s{i}.Dc.txt").read_text().splitlines() if not l.startswith("#")]
        n = X.shape[1]
        Dc = np.array([[float(v) for v in l.split()] for l in lines]).reshape(24, n, n)
        Xs.append(X); Dcs.append(Dc)
    names = (d / "s0.X.csv").read_text().splitlines()[0].split(",")
    meta = (d / "s0.meta.txt").read_text().splitlines()
    minang = float([l for l in meta if l.startswith("min_angle")][0].split()[1])
    return names, Xs, Dcs, minang

def CD(Xs, Dcs, idx):
    X = np.concatenate([Xs[i] for i in idx]); Xc = X - X.mean(0)
    C = Xc.T @ Xc / len(X)
    D = np.mean([Dcs[i].mean(0) for i in idx], axis=0)
    return C, D

def gsolve(C, D, rel=1e-10):
    l, V = np.linalg.eigh(C)
    keep = l > rel * l.max()
    T = V[:, keep] / np.sqrt(l[keep])
    M = T.T @ D @ T; M = (M + M.T) / 2
    mu, U = np.linalg.eigh(M)
    w = T @ U[:, 0]; w = w / w[np.argmax(np.abs(w))]
    return mu[0], w, int((~keep).sum()), mu

def q(w, C, D): return float(w @ D @ w / (w @ C @ w))

def jack(idx, f):
    full = f(idx); n = len(idx)
    drops = np.array([f(idx[:k] + idx[k + 1:]) for k in range(n)])
    err = np.sqrt((n - 1) / n * np.sum((drops - drops.mean(0)) ** 2, axis=0))
    if np.ndim(full) == 0: return float(full), float(err)
    return full, err

def main():
    tag = sys.argv[1]
    names, Xs, Dcs, minang = load(tag)
    n = len(names); TR, HE, ALL = list(range(16)), list(range(16, 32)), list(range(32))
    out = {"tag": tag, "marks": names, "n_marks": n, "min_angle_from_minusI": minang, "M_per_stream": [len(x) for x in Xs]}
    # A1
    mins = [float(np.linalg.eigvalsh((Dc.mean(0) + Dc.mean(0).T) / 2).min() / np.trace(Dc.mean(0))) for Dc in Dcs]
    asym = max(float(np.abs(Dc - Dc.transpose(0, 2, 1)).max()) for Dc in Dcs)
    out["A1"] = {"min_eig_over_trace": min(mins), "max_asym": asym, "met": min(mins) >= -1e-12 and asym < 1e-15}
    Ct, Dt = CD(Xs, Dcs, TR); Ch, Dh = CD(Xs, Dcs, HE)
    out["cond_C_train"] = float(np.linalg.cond(Ct)); out["cond_C_held"] = float(np.linalg.cond(Ch))
    out["cond_D_train"] = float(np.linalg.cond(Dt))
    lam, w, ndrop, spec = gsolve(Ct, Dt)
    out["train"] = {"lambda_min": float(lam), "beta_lambda_min": float(BETA * lam), "dropped_dirs": ndrop, "spectrum": spec.tolist(), "w": dict(zip(names, w.tolist()))}
    # held-out
    fq = lambda idx: q(w, *CD(Xs, Dcs, idx))
    qh, eh = jack(HE, fq)
    single = lambda idx: (lambda C, D: np.diag(D) / np.diag(C))(*CD(Xs, Dcs, idx))
    sh, seh = jack(HE, single)
    sh = single(HE)
    kbest = int(np.argmin(sh))
    ratio, er = jack(HE, lambda idx: fq(idx) / single(idx)[kbest])
    f4w = np.zeros(n); f4w[:4] = 0.25
    f4h, f4e = jack(HE, lambda idx: q(f4w, *CD(Xs, Dcs, idx)))
    out["held"] = {"q_opt": [qh, eh], "beta_q_opt": BETA * qh, "single": {nm: [float(a), float(b)] for nm, a, b in zip(names, sh, seh)},
                   "best_single": [names[kbest], float(sh[kbest]), float(seh[kbest])], "ratio_opt_over_best_single": [ratio, er],
                   "f4_mean_g": [f4h, f4e], "ratio_best_single_over_opt": 1 / ratio}
    out["A2"] = {"met": bool(ratio + 2 * er < 1.0)}
    out["A3"] = {"met": bool(qh >= lam - 3 * eh), "z": (qh - lam) / eh if eh > 0 else None}
    # per-colour shares on held
    num = np.array([np.mean([w @ Dcs[i][c] @ w for i in HE]) for c in range(24)])
    out["colour_shares_held"] = (num / num.sum()).round(4).tolist()
    # swap test
    lam2, w2, _, _ = gsolve(Ch, Dh)
    out["swap"] = {"lambda_min_trained_on_held": float(lam2), "q_on_train": q(w2, Ct, Dt), "w": dict(zip(names, w2.tolist())),
                   "cos_angle_w_w2_in_C_metric": float(abs(w @ Ct @ w2) / np.sqrt((w @ Ct @ w) * (w2 @ Ct @ w2)))}
    Ca, Da = CD(Xs, Dcs, ALL); lam3, w3, _, _ = gsolve(Ca, Da)
    out["insample_all32"] = {"lambda_min": float(lam3), "w": dict(zip(names, w3.tolist()))}
    # A4 thermalisation
    a4 = {}
    for lab, vec in (("opt", w), ("f1", np.eye(n)[0]), ("f4", f4w)):
        fa = lambda idx: q(vec, *CD(Xs, Dcs, idx))
        full, e = jack(ALL, fa)
        cold, hot = fa(ALL[0::2]), fa(ALL[1::2])
        z = (cold - hot) / (2 * e)
        a4[lab] = {"all32": [full, e], "cold": cold, "hot": hot, "z": z, "met": bool(abs(z) <= 2)}
    out["A4"] = a4
    if tag.endswith("d0"):
        r1, r4 = a4["f1"]["all32"], a4["f4"]["all32"]
        z1 = (r1[0] - .0613) / np.hypot(r1[1], .0004); z4 = (r4[0] - .0469) / np.hypot(r4[1], .0005)
        out["A5"] = {"z_r1": z1, "z_r4": z4, "met": bool(abs(z1) <= 2 and abs(z4) <= 2)}
    d = ROOT / "results" / tag
    with open(d / "analysis.json", "x") as fh: json.dump(out, fh, indent=1, default=float)
    with open(d / "C_D_train_held.txt", "x") as fh:
        for lab, M in (("C_train", Ct), ("D_train", Dt), ("C_held", Ch), ("D_held", Dh)):
            fh.write(f"# {lab} marks {','.join(names)}\n"); np.savetxt(fh, M, fmt="%.12e")
    s = json.dumps({k: out[k] for k in out if k not in ("marks",)}, default=float)
    print(s[:6000])

if __name__ == "__main__":
    main()
