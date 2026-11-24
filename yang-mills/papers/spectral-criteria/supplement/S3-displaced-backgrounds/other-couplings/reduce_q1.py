"""Q1 reduction (a2-mixb). usage: python3 reduce_q1.py <beta> <tag> [...] -> results_q1/<tag>/summary.json (mode 'x')
Estimators as the prior reduce.py (G4's fixed.py): pooled plug-in variance (ddof 0), J = mean, ratio = J/Var,
delete-one-stream jackknife errors. Predicates (fixed in run_q1.py before the runs): T1, T2, T2p, T2s, T5.
"""
import json, sys
import numpy as np
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from reduce import est, jack
ROOT = Path(__file__).resolve().parent

def red(beta, tag):
    d = ROOT / "results_q1" / tag
    idx = sorted(int(p.name[1:].split(".")[0]) for p in d.glob("s*.csv") if not p.name.endswith("colours.csv"))
    main = [np.loadtxt(d / f"s{i}.csv", skiprows=1, delimiter=",") for i in idx]
    meta = (d / "s0.meta.txt").read_text().splitlines()
    minang = float([l for l in meta if l.startswith("min_angle")][0].split()[1])
    n = len(main)
    res = {"tag": tag, "beta": beta, "streams": n, "meas": [len(m) for m in main], "min_angle": minang}
    res["pooled"] = jack(main, lambda it: {**est([x[:, :10] for x in it]), "plaq": np.concatenate(it)[:, 10].mean()})
    ps = [{"stream": i, "hot": i % 2, **{k: float(v) for k, v in est([m[:, :10]]).items()}, "plaq": float(m[:, 10].mean())} for i, m in zip(idx, main)]
    res["per_stream"] = ps
    cold, hot = est([m[:, :10] for m in main[0::2]]), est([m[:, :10] for m in main[1::2]])
    chk = {}
    for k in ("ratio1", "ratio4"):
        e = res["pooled"][k][1]; z = (cold[k] - hot[k]) / (2 * e)
        chk["T2_" + k] = {"z": float(z), "verdict": "MET" if abs(z) <= 2 else "FAILED"}
    for k, nm in (("plaq", "T2p"), ("spread", "T2s")):
        c = np.array([p[k] for p in ps if p["hot"] == 0]); h = np.array([p[k] for p in ps if p["hot"] == 1])
        sd = np.sqrt(c.var(ddof=1) / len(c) + h.var(ddof=1) / len(h)); z = (c.mean() - h.mean()) / sd
        chk[nm] = {"z": float(z), "cold": float(c.mean()), "hot": float(h.mean()), "verdict": "MET" if abs(z) <= 2 else "FAILED"}
    chk["T1"] = "MET" if n >= 8 else "FAILED"
    chk["T5_tries"] = {"mean_tries": float(res["pooled"]["mean_tries"][0]), "verdict": "MET" if res["pooled"]["mean_tries"][0] < 1000 else "FAILED"}
    res["checks"] = chk
    res["stream_sd"] = {k: float(np.std([p[k] for p in ps], ddof=1)) for k in ("ratio1", "ratio4", "spread")}
    import os
    with open(d / os.environ.get("SUMMARY", "summary.json"), "x") as fh: json.dump(res, fh, indent=1)
    p = res["pooled"]
    print(f"{tag} b={beta} minang={minang:.4f} J1={p['J1'][0]:.6f}({p['J1'][1]:.6f}) V1={p['var1'][0]:.5f}({p['var1'][1]:.5f}) "
          f"J4={p['J4'][0]:.6f}({p['J4'][1]:.6f}) V4={p['var4'][0]:.5f}({p['var4'][1]:.5f}) r1={p['ratio1'][0]:.4f}({p['ratio1'][1]:.4f}) "
          f"r4={p['ratio4'][0]:.4f}({p['ratio4'][1]:.4f}) b*r1={beta*p['ratio1'][0]:.4f}({beta*p['ratio1'][1]:.4f}) "
          f"b*r4={beta*p['ratio4'][0]:.4f}({beta*p['ratio4'][1]:.4f}) spread={p['spread'][0]:.4f}({p['spread'][1]:.4f}) "
          f"plaq={p['plaq'][0]:.5f} tries={p['mean_tries'][0]:.1f} sd(r1,r4)={res['stream_sd']['ratio1']:.4f},{res['stream_sd']['ratio4']:.4f} "
          + " ".join(f"{k}:{v['z']:.2f}{'' if v['verdict']=='MET' else '!FAIL'}" for k, v in chk.items() if isinstance(v, dict) and 'z' in v))

if __name__ == "__main__":
    b = float(sys.argv[1])
    for t in sys.argv[2:]: red(b, t)
