"""Reduction for z1-mix6 runs. usage: python3 reduce.py <tag> [<tag> ...]  -> results/<tag>/summary.json (mode 'x')

Estimators (G4's, fixed.py): pooled plug-in variance (ddof=0) over all streams; J = mean of per-measurement
J over all streams; ratio = J/Var; errors = delete-one-stream jackknife, sqrt((n-1)/n * sum (drop - mean)^2).
Predicates (fixed before the first run, see run.py): T1 streams >= 4; T2 hot/cold strata agree on ratio1
and ratio4 within 2 sigma_d, sigma_d = 2 * jackknife error of the pooled ratio.
Per-colour: fraction of J carried by each of the 24 colours (colour = 8*plane + px + 2py + 4pz,
plane 0=xy,1=xz,2=yz), with jackknife errors.
"""
import json, sys
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COLS = ["single", "average", "spread", "j_single", "j_average", "single_tl", "average_tl", "j_single_tl", "j_average_tl", "mean_tries"]


def est(main):
    d = np.concatenate(main)
    v1, v4, v1t, v4t = d[:, 0].var(), d[:, 1].var(), d[:, 5].var(), d[:, 6].var()
    j1, j4, j1t, j4t = d[:, 3].mean(), d[:, 4].mean(), d[:, 7].mean(), d[:, 8].mean()
    return {"spread": d[:, 2].mean(), "mean_f1": d[:, 0].mean(), "mean_f4": d[:, 1].mean(),
            "var1": v1, "var4": v4, "J1": j1, "J4": j4, "ratio1": j1 / v1, "ratio4": j4 / v4,
            "var1_tl": v1t, "var4_tl": v4t, "J1_tl": j1t, "J4_tl": j4t,
            "ratio1_tl": j1t / v1t if v1t > 0 else float("nan"), "ratio4_tl": j4t / v4t if v4t > 0 else float("nan"),
            "mean_tries": d[:, 9].mean()}


def jack(items, f):
    full = f(items)
    n = len(items)
    drops = [f(items[:i] + items[i + 1:]) for i in range(n)]
    err = {}
    for k in full:
        x = np.array([dd[k] for dd in drops], dtype=float)
        err[k] = float(np.sqrt((n - 1) / n * np.sum((x - x.mean()) ** 2)))
    return {k: [float(full[k]), err[k]] for k in full}


def reduce(tag):
    d = ROOT / "results" / tag
    files = sorted(d.glob("s*.csv"), key=lambda p: p.name)
    main = [np.loadtxt(p, skiprows=1, delimiter=",") for p in files if not p.name.endswith("colours.csv")]
    idx = sorted(int(p.name[1:].split(".")[0]) for p in files if not p.name.endswith("colours.csv"))
    cols = [np.loadtxt(d / f"s{i}.colours.csv", skiprows=1, delimiter=",") for i in idx]
    meta = (d / "s0.meta.txt").read_text().splitlines()
    minang = float([l for l in meta if l.startswith("min_angle")][0].split()[1])
    angles = [float(v) for v in [l for l in meta if l.startswith("coarse_angles")][0].split()[1:]]
    n = len(main)
    res = {"tag": tag, "streams": n, "measurements_per_stream": [len(m) for m in main],
           "min_angle_from_minusI": minang, "n_coarse_faces": len(angles),
           "faces_within_pi/8": int(sum(a <= np.pi / 8 for a in angles)),
           "pooled": jack(main, est)}
    res["per_stream"] = [{"stream": i, "hot": i % 2, **{k: float(v) for k, v in est([m]).items()}} for i, m in zip(idx, main)]
    cold = est(main[0::2]); hot = est(main[1::2])
    res["strata"] = {"cold": {k: float(v) for k, v in cold.items()}, "hot": {k: float(v) for k, v in hot.items()}}
    t2 = {}
    for k in ("ratio1", "ratio4", "ratio1_tl", "ratio4_tl"):
        e = res["pooled"][k][1]
        z = (cold[k] - hot[k]) / (2 * e) if e > 0 else float("nan")
        t2[k] = {"z": float(z), "verdict": "MET" if abs(z) <= 2 else "FAILED"}
    res["T1_streams>=4"] = "MET" if n >= 4 else "FAILED"
    res["T2_hot_cold"] = t2
    # per-colour fractions of J (tests f1, f4)
    def colfrac(items):
        c = np.concatenate(items).mean(axis=0)  # 96 = 4 tests x 24 colours, each (f'-f'')^2/2
        out = {}
        for t, name in enumerate(["j1", "j4", "j1tl", "j4tl"]):
            v = c[24 * t:24 * (t + 1)]
            for k in range(24):
                out[f"{name}_c{k}"] = v[k] / 24.0  # contribution to J (J = mean over colours)
                out[f"{name}_frac{k}"] = v[k] / v.sum() if v.sum() > 0 else float("nan")
        return out
    res["per_colour"] = jack(cols, colfrac)
    # consistency: per-colour sum equals J column
    jsum = np.concatenate(cols)[:, :24].mean(axis=0).sum() / 24
    res["check_colour_sum_J1"] = [float(jsum), res["pooled"]["J1"][0]]
    with open(d / "summary.json", "x") as fh:
        json.dump(res, fh, indent=1)
    p = res["pooled"]
    print(f"{tag}: n={n} minang={minang:.4f} spread={p['spread'][0]:.4f}({p['spread'][1]:.4f}) "
          f"var4={p['var4'][0]:.5f}({p['var4'][1]:.5f}) J4={p['J4'][0]:.6f}({p['J4'][1]:.6f}) "
          f"r1={p['ratio1'][0]:.4f}({p['ratio1'][1]:.4f}) r4={p['ratio4'][0]:.4f}({p['ratio4'][1]:.4f}) "
          f"b*r1={3.276133577*p['ratio1'][0]:.4f} T2 r1 z={t2['ratio1']['z']:.2f} r4 z={t2['ratio4']['z']:.2f}")


if __name__ == "__main__":
    for t in sys.argv[1:]:
        reduce(t)
