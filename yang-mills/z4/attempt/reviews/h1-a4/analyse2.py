"""analyse2.py -- h1-a4 item (d): compare the k=2 exact transfer with the continuum levels.
Inputs: results/t2_b*_N*_M*.json (largest N per beta used; pairs give the N-error).
Continuum (NUMERICS.md, brief): e0 = 3.3505330, e1 = 5.3254970 (e1 is the doublet; lattice lambda1, lambda2).
PREDICATES (fixed before this program's first run):
 D1 log(l0/l1) equals NUMERICS m_e (0.51516418, 0.43994233, 0.36450079, 0.29712330, 0.23982321, 0.19238313
    for beta 32..1024) to 1e-7 absolute (NUMERICS quotes 8 decimals).
 D2 N-convergence: max_j<=3 |l_j(N) - l_j(N')| < 1e-8 for each beta with two runs.
 D3 |-log l_j/h - e_j| strictly decreasing in beta, j = 0, 1.
 D4 |(1-l_j)/h - e_j| strictly decreasing in beta, j = 0, 1.
 D5 at the largest beta: |-log l_j/h - e_j| / e_j < 0.05, j = 0, 1.
 D6 at the largest beta: |(1-l_j)/h - (e_j - e_j^2 h/2)| / e_j < 0.05  (first-order consistency of the
    two forms: 1 - exp(-e h) = e h - e^2 h^2/2 + ...).
 D7 quadratic fit e + a h + b h^2 of -log l_j/h on the three largest beta gives e_j within 1%.
 Measured only: raw (1-l_j)/h - e_j at the largest beta; the l1/l2 splitting times beta^{1/3}.
"""
import json, glob, re, sys, numpy as np
e = [3.3505330, 5.3254970]
ref = {32: 0.51516418, 64: 0.43994233, 128: 0.36450079, 256: 0.29712330, 512: 0.23982321, 1024: 0.19238313}
runs = {}
for f in glob.glob("results/t2_b*_N*_M*.json"):
    r = json.load(open(f)); runs.setdefault(int(r["beta"]), []).append(r)
out = open(sys.argv[1], "x"); lines = []; met = fail = 0; failed = []
def pred(name, ok, txt):
    global met, fail
    lines.append(f"{name}: {'MET' if ok else 'FAILED'}  {txt}")
    if ok: met += 1
    else: fail += 1; failed.append(name)
betas = sorted(runs); best = {}
for b in betas:
    rs = sorted(runs[b], key=lambda r: r["N"]); best[b] = rs[-1]
    g = rs[-1]["gap_log_ratio"][0]
    pred(f"D1 beta={b}", abs(g-ref[b]) < 1e-7, f"gap={g:.10f} ref={ref[b]}")
    if len(rs) > 1:
        dl = max(abs(x-y) for x, y in zip(rs[-1]["lambda"][:4], rs[-2]["lambda"][:4]))
        pred(f"D2 beta={b}", dl < 1e-8, f"N {rs[-2]['N']}->{rs[-1]['N']} max dl={dl:.2e}")
tab = ["beta h  l0  l1  l2  (1-l0)/h  -log l0/h  (1-l1)/h  -log l1/h  (l1-l2 split)/h"]
for b in betas:
    r = best[b]; h = r["h"]; l = r["lambda"]
    tab.append(f"{b} {h:.5f} {l[0]:.10f} {l[1]:.10f} {l[2]:.10f} {(1-l[0])/h:.5f} {-np.log(l[0])/h:.5f} {(1-l[1])/h:.5f} {-np.log(l[1])/h:.5f} {np.log(l[1]/l[2])/h:.5f}")
for j in (0, 1):
    dl = [abs(-np.log(best[b]["lambda"][j])/best[b]["h"]-e[j]) for b in betas]
    pred(f"D3 j={j}", all(dl[i+1] < dl[i] for i in range(len(dl)-1)), "devs " + " ".join(f"{x:.4f}" for x in dl))
    d1 = [abs((1-best[b]["lambda"][j])/best[b]["h"]-e[j]) for b in betas]
    pred(f"D4 j={j}", all(d1[i+1] < d1[i] for i in range(len(d1)-1)), "devs " + " ".join(f"{x:.4f}" for x in d1))
    bl = betas[-1]; h = best[bl]["h"]; lj = best[bl]["lambda"][j]
    pred(f"D5 j={j}", abs(-np.log(lj)/h-e[j])/e[j] < 0.05, f"beta={bl}: {-np.log(lj)/h:.5f} vs {e[j]}")
    pred(f"D6 j={j}", abs((1-lj)/h-(e[j]-e[j]**2*h/2))/e[j] < 0.05, f"beta={bl}: {(1-lj)/h:.5f} vs e-e^2h/2={e[j]-e[j]**2*h/2:.5f}")
    lines.append(f"measured: beta={bl} raw (1-l{j})/h - e{j} = {(1-lj)/h-e[j]:.5f} (relative {((1-lj)/h-e[j])/e[j]:.3f})")
    hs = np.array([best[b]["h"] for b in betas[-3:]]); ys = np.array([-np.log(best[b]["lambda"][j])/best[b]["h"] for b in betas[-3:]])
    c = np.polyfit(hs, ys, 2)
    pred(f"D7 j={j}", abs(c[-1]-e[j])/e[j] < 0.01, f"extrapolated {c[-1]:.5f} vs {e[j]} (betas {betas[-3:]})")
txt = "\n".join(tab+lines+[f"COUNTS met={met} failed={fail}", f"FAILED: {failed}"])
out.write(txt+"\n"); out.close(); print(txt)
