"""d2-time analysis of z1mx5 'time' runs. usage: python3 antime.py <tag> <weights file> -> results/<tag>/antime.{json,txt} (mode 'x')
Estimators (fixed before the first run):
  Pooled raw moments over a stream set S (sums / N, ddof 0). Blocks b = 2*ti + d, ti over slices t = 1, 2, 3, -1 (= 11), d = 0 loc, 1 tr.
  m_j = w_j . X(0), j = 0 w_L4, 1 w_L1, 2 f4 (rows of the weights file).
  rho_j(t, d) = Corr(m_j, w_j . Y(t)) over all 32 streams; error = delete-one-stream jackknife over the 32.
  R2_held_j(t, d): TRAIN 0..15 least squares m_j = a + beta.Y (beta = pseudo-inverse of C_YY with eigen-directions < 1e-10 max
  dropped; a from TRAIN means); R2_held = 1 - E_HELD[(m - a - beta.Y)^2] / Var_HELD(m), from HELD pooled moments; error =
  delete-one-HELD-stream jackknife (beta fixed; train-fit variance not included: stated limitation). Also R2_train (in-sample;
  = squared largest canonical correlation between m_j and span Y on TRAIN) and, measured only, R2_held with the 15 L1 Y marks only.
Predicates (fixed before the first run):
  M1 each stream's syy (full) symmetric PSD: smallest eigenvalue >= -1e-9 * trace (rounding of 11-digit printing).  [all 256 = 32 x 8]
  M2 |rho| <= 1 and R2_train in [0, 1] for every (j, t, d).
  A4 hot/cold (cold = even streams, hot = odd), on all 32: for rho_j(1, loc), j = 0, 2, and the slice-0 and slice-1 plaquette means
     (series.csv): |cold - hot| <= 2 * (2 e_32) (prior T2 convention; e_32 = jackknife se on all 32 streams).
  A7 burn-in: per stream first vs second half of the 1152 measurements for m_0 and plaq_t1, pooled over streams:
     |diff| <= 4 * se (se from per-stream half differences; the 2*(2 se) convention).
  S1 time-reflection symmetry: |x(1) - x(-1)| <= 3 sqrt(e(1)^2 + e(-1)^2) for x = rho_j and R2_held_j, j = 0, 1, 2, d = loc, tr
     (hypothesis: the conditioned ensemble is reflection-symmetric about slice 0; 3 se because of 12 tests).
Interpretation rule: see prodt.py docstring (applied in report, needs the clear run too).
"""
import json, sys
import numpy as np
from pathlib import Path
R = Path(__file__).resolve().parent
tag, wf = sys.argv[1], sys.argv[2]; d = R / "results" / tag
W = np.loadtxt(wf); K, NM = W.shape; NB = 8
SL = [1, 2, 3, -1]; iu = np.triu_indices(NM)
def load(i):
    L = {}
    for line in (d / f"s{i}.mom.txt").read_text().splitlines():
        if line.startswith("#"): continue
        f = line.split()
        if f[0] in ("sm", "smm"): L[f[0]] = np.array(f[1:], float)
        else: L[(f[0], int(f[1]))] = np.array(f[2:], float)
    N = 1152; st = {"N": N, "sm": L["sm"], "smm": L["smm"].reshape(K, K), "b": []}
    for b in range(NB):
        A = np.zeros((NM, NM)); A[iu] = L[("syy", b)]; A = A + A.T - np.diag(np.diag(A))
        st["b"].append((L[("sy", b)], L[("smy", b)].reshape(K, NM), A))
    return st
ST = [load(i) for i in range(32)]
res = {"tag": tag, "weights": wf}; out = []; pred = {"met": 0, "failed": 0, "list": []}
def P(name, ok, info):
    pred["met" if ok else "failed"] += 1; pred["list"].append(f"{name}: {'MET' if ok else 'FAILED'} {info}")
# M1
bad = 0; worst = 0.
for s in ST:
    for b in range(NB):
        A = s["b"][b][2]; e = np.linalg.eigvalsh(A)[0] / np.trace(A); worst = min(worst, e); bad += e < -1e-9
P("M1 (256 cases)", bad == 0, f"{256 - bad} qualify; min eig/trace {worst:.2e}")
def pooled(idx, b):
    N = sum(ST[i]["N"] for i in idx)
    Em = sum(ST[i]["sm"] for i in idx) / N; Emm = sum(ST[i]["smm"] for i in idx) / N
    Ey = sum(ST[i]["b"][b][0] for i in idx) / N; Emy = sum(ST[i]["b"][b][1] for i in idx) / N; Eyy = sum(ST[i]["b"][b][2] for i in idx) / N
    return Em, Emm, Ey, Emy, Eyy
def rho(idx, b, j):
    Em, Emm, Ey, Emy, Eyy = pooled(idx, b); w = W[j]
    cov = w @ Emy[j] - Em[j] * (w @ Ey); vm = Emm[j, j] - Em[j] ** 2; vy = w @ Eyy @ w - (w @ Ey) ** 2
    return cov / np.sqrt(vm * vy)
def jk(idx, f):
    full = f(idx); n = len(idx); dr = np.array([f(idx[:k] + idx[k + 1:]) for k in range(n)])
    return float(full), float(np.sqrt((n - 1) / n * np.sum((dr - dr.mean()) ** 2)))
TR, HE, ALL = list(range(16)), list(range(16, 32)), list(range(32))
def fit(b, j, sel):
    Em, Emm, Ey, Emy, Eyy = pooled(TR, b); C = Eyy - np.outer(Ey, Ey); c = Emy[j] - Em[j] * Ey
    C = C[np.ix_(sel, sel)]; c = c[sel]; l, V = np.linalg.eigh(C); keep = l > 1e-10 * l.max()
    beta = V[:, keep] @ ((V[:, keep].T @ c) / l[keep]); a = Em[j] - beta @ Ey[sel]
    r2tr = (beta @ c) / (Emm[j, j] - Em[j] ** 2)
    return beta, a, float(r2tr), int((~keep).sum())
def r2held(idx, b, j, beta, a, sel):
    Em, Emm, Ey, Emy, Eyy = pooled(idx, b); Ey = Ey[sel]; Emy = Emy[j][sel]; Eyy = Eyy[np.ix_(sel, sel)]
    mse = Emm[j, j] - 2 * a * Em[j] - 2 * beta @ Emy + a * a + 2 * a * beta @ Ey + beta @ Eyy @ beta
    return 1 - mse / (Emm[j, j] - Em[j] ** 2)
names = [l.strip() for l in open(R / "prior_weights/names.txt")]
L1 = [names.index(n) for n in [l.split()[0] for l in open(R / "prior_weights/w_L1.txt")]]
JN = ["wL4", "wL1", "f4"]; DN = ["loc", "tr"]; tab = {}
for ti, t in enumerate(SL):
    for dd in range(2):
        b = 2 * ti + dd
        for j in range(K):
            r, re = jk(ALL, lambda I: rho(I, b, j))
            beta, a, r2tr, nt = fit(b, j, list(range(NM)))
            h, he = jk(HE, lambda I: r2held(I, b, j, beta, a, list(range(NM))))
            beta1, a1, r2tr1, _ = fit(b, j, L1)
            h1, he1 = jk(HE, lambda I: r2held(I, b, j, beta1, a1, L1))
            key = f"{JN[j]} t={t} {DN[dd]}"
            tab[key] = dict(rho=r, rho_se=re, R2_held=h, R2_held_se=he, R2_train=r2tr, truncated=nt, R2_held_L1Y=h1, R2_held_L1Y_se=he1, R2_train_L1Y=r2tr1)
            if not (abs(r) <= 1 and 0 <= r2tr <= 1): P(f"M2 {key}", False, f"rho {r} R2_train {r2tr}")
P("M2 (all 24 (j,t,d))", all(abs(v["rho"]) <= 1 and 0 <= v["R2_train"] <= 1 for v in tab.values()), "")
res["table"] = tab
# A4 hot/cold
COLD, HOT = ALL[0::2], ALL[1::2]
for j in (0, 2):
    _, e = jk(ALL, lambda I: rho(I, 0, j)); c, h_ = rho(COLD, 0, j), rho(HOT, 0, j)
    P(f"A4 rho {JN[j]} t=1 loc", abs(c - h_) <= 4 * e, f"cold {c:.5f} hot {h_:.5f} e32 {e:.5f}")
S = [np.loadtxt(d / f"s{i}.series.csv", delimiter=",", skiprows=1) for i in ALL]
hdr = (d / "s0.series.csv").read_text().splitlines()[0].split(",")
for col in ("plaq_t0", "plaq_t1"):
    k = hdr.index(col); v = np.array([s[:, k].mean() for s in S]); e = v.std(ddof=1) / np.sqrt(32)
    P(f"A4 {col}", abs(v[0::2].mean() - v[1::2].mean()) <= 4 * e, f"cold {v[0::2].mean():.6f} hot {v[1::2].mean():.6f} e32 {e:.6f}")
    res[f"mean_{col}"] = [float(v.mean()), float(e)]
for col in ("m0", "plaq_t1"):
    k = hdr.index(col); dv = np.array([s[:576, k].mean() - s[576:, k].mean() for s in S]); e = dv.std(ddof=1) / np.sqrt(32)
    P(f"A7 burn-in {col}", abs(dv.mean()) <= 4 * e, f"first-second {dv.mean():.2e} se {e:.2e}")
# integrated autocorrelation of m0 (measured only)
def tau(x, cut=60):
    x = x - x.mean(); c0 = x @ x / len(x); s = 0.5
    for k in range(1, cut):
        c = x[:-k] @ x[k:] / len(x) / c0; s += c
        if c < 0.05: break
    return s
res["tau_int_m0_measured_only"] = float(np.mean([tau(s[:, 0]) for s in S]))
# S1 reflection symmetry
for j in range(K):
    for dd in range(2):
        a_, b_ = tab[f"{JN[j]} t=1 {DN[dd]}"], tab[f"{JN[j]} t=-1 {DN[dd]}"]
        for q in ("rho", "R2_held"):
            z = (a_[q] - b_[q]) / np.hypot(a_[q + "_se"], b_[q + "_se"])
            P(f"S1 {q} {JN[j]} {DN[dd]}", abs(z) <= 3, f"t=1 {a_[q]:.5f} t=-1 {b_[q]:.5f} z {z:.2f}")
res["predicates"] = pred
out.append(f"# antime {tag} weights {wf}")
out.append("key | rho(se) | R2_held(se) | R2_train | trunc | R2_held L1-Y only (se) | R2_train L1-Y")
for k, v in tab.items():
    out.append(f"{k} | {v['rho']:.5f}({v['rho_se']:.5f}) | {v['R2_held']:.5f}({v['R2_held_se']:.5f}) | {v['R2_train']:.5f} | {v['truncated']} | {v['R2_held_L1Y']:.5f}({v['R2_held_L1Y_se']:.5f}) | {v['R2_train_L1Y']:.5f}")
out.append(f"plaq_t0 {res['mean_plaq_t0']}, plaq_t1 {res['mean_plaq_t1']}, tau_int(m0) {res['tau_int_m0_measured_only']:.2f} measurements")
out.append(f"predicates met {pred['met']} failed {pred['failed']}"); out += pred["list"]
with open(d / "antime.json", "x") as fh: json.dump(res, fh, indent=1)
with open(d / "antime.txt", "x") as fh: fh.write("\n".join(out) + "\n")
print("\n".join(out))
