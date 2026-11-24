"""c2-grow analysis of z1mx4 runs. usage: python3 an4.py <tag> -> results/<tag>/an4.json, an4.txt, w_<list>.txt, mats/ (mode 'x')

Estimators (same as the prior analyze.py, fixed before the first run):
  C(S) pooled covariance over streams S (centred by the pooled mean of S, ddof 0), via per-stream sums.
  D(S) mean over streams of D_s (z1mx4 line 1 = mean over colours of per-colour mean (X'-X'')(X'-X'')^T/2).
  TRAIN streams 0..15, HELD 16..31. Generalised eigenproblem on TRAIN by C-whitening; directions with C-eigenvalue
  < 1e-10 * max truncated (reported). w normalised to max |w| = 1. Held-out q = w'D(HELD)w / w'C(HELD)w,
  delete-one-stream jackknife over HELD. Optimism gap = q_held - lambda_train.
Nested lists (by name, fixed before the first run):
  L1 = prior 15 (B.xy000.{g00,g10,g01,g11,Rv,Rh,L_no11}, B.xy200.g**, B.yz204.g**)
  L2 = all ring-1 B marks (7 faces x 7 = 49);  L3 = L2 + ring-2 B plaquettes (181);  L4 = all 308 (+ ring-2 B partial, ring-1 T plaquettes).
  Also reported (measured only): L1 sub-lists and L2 minus the four i-type faces.
Predicates (fixed before the first run):
  G1 'the optimum has stopped falling' between L_n and L_{n+1}: |q_{n+1} - q_n| <= 2 sqrt(e_n^2 + e_{n+1}^2) (held-out values,
     combined standard error as the brief states; the paired jackknife difference is reported as measured only).
  G2 (statistics rule of the brief) held-out relative error <= 4 % for every list; if failed, more streams are needed.
  A1 every D_s symmetric PSD to -1e-12 * trace (rounding).  A3 held q >= lambda_train - 3 e (else defect in my code).
  A4 hot/cold (cold = even streams, hot = odd) for w(L4), f1, f4 on all 32: |cold-hot| <= 2 * (2 e_32) (prior T2 convention).
  A5 (tags ending d0) f1, f4 on 32 streams vs prior large run r1 .0613(4), r4 .0469(5): |z| <= 2.
  A6 (tags ending d0) L1 held optimum vs prior Y-d0 marked+xp+yz .02157(46): |z| <= 2 (independent seeds).
Weights' support by face: s_k = w_k sqrt(C_train,kk); face share = sum_{k in face} s_k^2 / sum s_k^2.
"""
import json, sys, re
import numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve().parent
BETA = 3.276133577
RING1 = ["xy000", "xz000", "xy200", "xz200", "yz200", "yz204", "yz240"]

def load(tag, ns=32):
    d = ROOT / "results" / tag
    names = (d / "s0.X.csv").read_text().splitlines()[0].split(",")
    n = len(names); st = []
    for i in range(ns):
        X = np.loadtxt(d / f"s{i}.X.csv", delimiter=",", skiprows=1)
        lines = [l for l in (d / f"s{i}.Dc.txt").read_text().splitlines() if not l.startswith("#")]
        D = np.array([float(v) for v in lines[0].split()]).reshape(n, n)
        dg = np.array([[float(v) for v in l.split()] for l in lines[1:25]])
        st.append({"m": len(X), "s1": X.sum(0), "s2": X.T @ X, "D": D, "dg": dg, "X": X})
    return names, st

def CD(st, idx, sel):
    m = sum(st[i]["m"] for i in idx); s1 = sum(st[i]["s1"] for i in idx)[sel]
    s2 = sum(st[i]["s2"] for i in idx)[np.ix_(sel, sel)]
    mu = s1 / m; C = s2 / m - np.outer(mu, mu)
    D = np.mean([st[i]["D"][np.ix_(sel, sel)] for i in idx], axis=0)
    return C, D

def gsolve(C, D, rel=1e-10):
    l, V = np.linalg.eigh(C); keep = l > rel * l.max()
    T = V[:, keep] / np.sqrt(l[keep]); M = T.T @ D @ T; M = (M + M.T) / 2
    mu, U = np.linalg.eigh(M); w = T @ U[:, 0]; w = w / w[np.argmax(np.abs(w))]
    return float(mu[0]), w, int((~keep).sum())

def qv(w, C, D): return float(w @ D @ w / (w @ C @ w))

def jack(idx, f):
    full = f(idx); n = len(idx)
    dr = np.array([f(idx[:k] + idx[k + 1:]) for k in range(n)])
    return full, float(np.sqrt((n - 1) / n * np.sum((dr - dr.mean(0)) ** 2))), dr

def face_of(nm): return nm.split(".")[1]

def lists(names):
    L1 = ["B.xy000." + s for s in ("g00", "g10", "g01", "g11", "Rv", "Rh", "L_no11")] + [f"B.{f}.g{c}" for f in ("xy200", "yz204") for c in ("00", "10", "01", "11")]
    L2 = [nm for nm in names if nm.startswith("B.") and face_of(nm) in RING1]
    L3 = L2 + [nm for nm in names if nm.startswith("B.") and face_of(nm) not in RING1 and re.search(r"\.g\d\d$", nm)]
    L4 = list(names)
    assert set(L1) <= set(L2) <= set(L3) <= set(L4) and len(L1) == 15 and len(L2) == 49 and len(L3) == 181 and len(L4) == 308
    extra = {"L2_minus_i_faces": [nm for nm in L2 if face_of(nm) in ("xy000", "xy200", "yz204")],
             "L1_marked_only": L1[:7]}
    return {"L1": L1, "L2": L2, "L3": L3, "L4": L4}, extra

def solve_list(st, names, sub, TR, HE):
    idx = {nm: k for k, nm in enumerate(names)}; sel = [idx[n] for n in sub]
    Ct, Dt = CD(st, TR, sel); lam, w, nd = gsolve(Ct, Dt)
    qh, eh, dr = jack(HE, lambda ii: qv(w, *CD(st, ii, sel)))
    s = w * np.sqrt(np.diag(Ct)); share = {}
    for nm, v in zip(sub, s): share[face_of(nm)] = share.get(face_of(nm), 0) + v * v
    tot = sum(share.values()); share = dict(sorted(((k, v / tot) for k, v in share.items()), key=lambda kv: -kv[1]))
    return {"n": len(sub), "cond_C_train": float(np.linalg.cond(Ct)), "cond_C_held": float(np.linalg.cond(CD(st, HE, sel)[0])), "dropped": nd,
            "train_lambda": lam, "held_q": [qh, eh], "rel_err": eh / qh, "optimism_gap": qh - lam, "beta_held_q": BETA * qh,
            "face_share": share, "w": dict(zip(sub, w.tolist()))}, dr, w, sel

def main():
    tag = sys.argv[1]; out_d = ROOT / "results" / tag
    names, st = load(tag)
    TR, HE, ALL = list(range(16)), list(range(16, 32)), list(range(32))
    L, extra = lists(names); res = {"tag": tag, "n_marks": len(names), "M_per_stream": [s["m"] for s in st]}
    mins = [float(np.linalg.eigvalsh((s["D"] + s["D"].T) / 2).min() / np.trace(s["D"])) for s in st]
    asym = max(float(np.abs(s["D"] - s["D"].T).max()) for s in st)
    res["A1"] = {"min_eig_over_trace": min(mins), "max_asym": asym, "met": bool(min(mins) >= -1e-12 and asym < 1e-12)}
    drops, ws, sels = {}, {}, {}
    for lab, sub in list(L.items()) + list(extra.items()):
        r, dr, w, sel = solve_list(st, names, sub, TR, HE)
        res[lab] = r; drops[lab] = dr; ws[lab] = w; sels[lab] = sel
        r["A3_met"] = bool(r["held_q"][0] >= r["train_lambda"] - 3 * r["held_q"][1])
        with open(out_d / f"w_{lab}.txt", "x") as fh:
            for nm, v in zip(sub, w): fh.write(f"{nm} {v:.12e}\n")
    G = {}
    for a, b in (("L1", "L2"), ("L2", "L3"), ("L3", "L4")):
        qa, ea = res[a]["held_q"]; qb, eb = res[b]["held_q"]; comb = float(np.hypot(ea, eb))
        dd = drops[b] - drops[a]; n = len(dd); pe = float(np.sqrt((n - 1) / n * np.sum((dd - dd.mean()) ** 2)))
        G[f"{a}->{b}"] = {"diff": qb - qa, "comb_se": comb, "z": (qb - qa) / comb, "stopped_falling_met": bool(abs(qb - qa) <= 2 * comb),
                          "paired_jack_se": pe, "paired_z": (qb - qa) / pe}
    res["G1"] = G
    res["G2"] = {lab: {"rel_err": res[lab]["rel_err"], "met": bool(res[lab]["rel_err"] <= 0.04)} for lab in L}
    idx = {nm: k for k, nm in enumerate(names)}
    f1 = np.zeros(len(names)); f1[idx["B.xy000.g00"]] = 1
    f4 = np.zeros(len(names)); f4[[idx[f"B.xy000.g{c}"] for c in ("00", "10", "01", "11")]] = .25
    full = list(range(len(names)))
    a4 = {}
    for lab, vec, sel in (("opt_L4", ws["L4"], sels["L4"]), ("f1", f1, full), ("f4", f4, full)):
        fa = lambda ii: qv(vec, *CD(st, ii, sel))
        q32, e32, _ = jack(ALL, fa); cold, hot = fa(ALL[0::2]), fa(ALL[1::2]); z = (cold - hot) / (2 * e32)
        a4[lab] = {"all32": [q32, e32], "cold": cold, "hot": hot, "z": z, "met": bool(abs(z) <= 2)}
    res["A4"] = a4
    if tag.endswith("d0"):
        r1, r4 = a4["f1"]["all32"], a4["f4"]["all32"]
        z1 = (r1[0] - .0613) / np.hypot(r1[1], .0004); z4 = (r4[0] - .0469) / np.hypot(r4[1], .0005)
        res["A5"] = {"z_r1": z1, "z_r4": z4, "met": bool(abs(z1) <= 2 and abs(z4) <= 2)}
        z6 = (res["L1"]["held_q"][0] - .02157) / np.hypot(res["L1"]["held_q"][1], .00046)
        res["A6"] = {"z": z6, "met": bool(abs(z6) <= 2)}
    # colour support of w(L4) on HELD via per-colour diagonal only (measured only): share of sum_k w_k^2 dg_ck
    wL4 = ws["L4"]; dg = np.mean([st[i]["dg"] for i in HE], axis=0)
    cs = (dg * wL4[None, :] ** 2).sum(1); res["colour_diag_share_L4"] = (cs / cs.sum()).round(4).tolist()
    # matrices for the child (per-stream sufficient stats for L4)
    md = out_d / "mats"; md.mkdir(exist_ok=False)
    for i, s in enumerate(st):
        np.savetxt(md / f"s{i}.sum1.txt", s["s1"], fmt="%.17e"); np.savetxt(md / f"s{i}.sum2.txt", s["s2"], fmt="%.17e")
        np.savetxt(md / f"s{i}.D.txt", s["D"], fmt="%.17e")
        with open(md / f"s{i}.m.txt", "x") as fh: fh.write(f"{s['m']}\n")
    with open(md / "names.txt", "x") as fh: fh.write("\n".join(names) + "\n")
    with open(out_d / "an4.json", "x") as fh: json.dump(res, fh, indent=1, default=float)
    lines = [f"tag {tag}  marks {len(names)}  A1 {res['A1']['met']}"]
    for lab in list(L) + list(extra):
        r = res[lab]; top = list(r["face_share"].items())[:6]
        lines.append(f"{lab:18s} n {r['n']:3d} cond {r['cond_C_train']:.3g} drop {r['dropped']} train {r['train_lambda']:.5f} held {r['held_q'][0]:.5f}({r['held_q'][1]:.5f}) rel {r['rel_err']:.3f} gap {r['optimism_gap']:+.5f} beta*q {r['beta_held_q']:.4f} A3 {r['A3_met']} faces " + " ".join(f"{k}:{v:.3f}" for k, v in top))
    for k, v in G.items(): lines.append(f"G1 {k}: diff {v['diff']:+.5f} comb_se {v['comb_se']:.5f} z {v['z']:+.2f} stopped_falling {v['stopped_falling_met']} (paired z {v['paired_z']:+.2f})")
    lines.append("G2 " + str({k: (round(v['rel_err'], 4), v['met']) for k, v in res['G2'].items()}))
    lines.append("A4 " + str({k: (round(v['all32'][0], 5), round(v['all32'][1], 5), round(v['z'], 2), v['met']) for k, v in a4.items()}))
    if "A5" in res: lines.append(f"A5 {res['A5']}  A6 {res['A6']}")
    lines.append("colour diag share L4 (nonzero) " + str({c: v for c, v in enumerate(res['colour_diag_share_L4']) if v > 0.002}))
    txt = "\n".join(lines); print(txt)
    with open(out_d / "an4.txt", "x") as fh: fh.write(txt + "\n")

if __name__ == "__main__":
    main()
