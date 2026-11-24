"""Heat-bath exact-law test. For density ~ sqrt(1-a^2) exp(k a) on [-1,1]: E[a] = I2(k)/I1(k).
Tests (a) wilson_mc.rs rng.heat (G4's, used by my sampler) via build/hbtest, (b) the child's numpy heatbath
(childcheck/mix6_cb.py, function heatbath with beta=1, staple norm k), n=400000 each, fixed seeds.
Predicate: |mean - exact| <= 4 standard errors for every k (4 sigma: 16 comparisons, keep family-wise false alarm small).
Rule 4: report how many k qualify. Writes results/hbtest.json (mode 'x')."""
import subprocess, json, importlib.util, sys
import numpy as np
from scipy.special import iv
res = {"rust": [], "child": []}
out = subprocess.run(["build/hbtest"], capture_output=True, text=True, check=True).stdout.split("\n")
for line in out:
    if not line.strip(): continue
    k, m1, m2, n = map(float, line.split()); ex = iv(2, k) / iv(1, k); se = np.sqrt((m2 - m1 ** 2) / n)
    res["rust"].append({"k": k, "mean": m1, "exact": ex, "z": (m1 - ex) / se})
spec = importlib.util.spec_from_file_location("cb", "childcheck/mix6_cb.py"); cb = importlib.util.module_from_spec(spec)
sys.argv = ["x"]; spec.loader.exec_module(cb)
rng = np.random.default_rng(2468)
for k in [0.5, 0.99, 1.01, 1.9, 2.1, 5.0, 10.0, 20.0]:
    n = 400000; V = np.tile(np.array([0.3, 0.4, 0.5, np.sqrt(0.5)]) * k, (n, 1))
    U = cb.heatbath(rng, V, beta=1.0)
    # Re(U V)/k is the cosine with the staple in the child's convention
    a = cb.qm(U, V)[:, 0] / k
    ex = iv(2, k) / iv(1, k); se = a.std() / np.sqrt(n)
    res["child"].append({"k": k, "mean": float(a.mean()), "exact": float(ex), "z": float((a.mean() - ex) / se)})
for who in res:
    q = sum(abs(r["z"]) <= 4 for r in res[who]); res[who + "_qualify"] = f"{q}/{len(res[who])}"
with open("results/hbtest.json", "x") as fh: json.dump(res, fh, indent=1)
for who in ("rust", "child"):
    print(who, res[who + "_qualify"], [(r["k"], round(r["mean"], 5), round(r["exact"], 5), round(r["z"], 2)) for r in res[who]])
