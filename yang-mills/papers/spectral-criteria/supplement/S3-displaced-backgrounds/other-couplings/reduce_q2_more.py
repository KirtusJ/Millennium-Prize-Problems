"""Q2 extra reduction (a2-mixb): same data and jackknife as reduce_q2.py, printed with more digits, plus a
measured-only conditional correlation per gate: Rc_g(t) = (S2_g[t]/I2_g[t] - mu^2)/(S2_g[0]/I2_g[0] - mu^2),
mu = S1_g/count_g (correlation of m1 among pairs whose square is in the gate at both times).
Also z of R_gate(t) - R_clear(t). Writes results_q2/<tag>/more.txt (mode 'x')."""
import sys, numpy as np
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from reduce_q2 import est as est0, GN
def est(ch):
    o = est0(ch); m = np.concatenate(ch).mean(axis=0)
    for g in range(1, 5):
        b = 1 + 9 * g; mu = m[b + 1] / m[b]; I = m[46 + 7 * (g - 1): 53 + 7 * (g - 1)]
        c = [m[b + 2 + t] / I[t] - mu ** 2 for t in range(3)]
        for t in (1, 2): o[f"Rc{t}_{GN[g]}"] = c[t] / c[0]
        o[f"pairs1_{GN[g]}"] = I[1]  # mean number of (square, t0) pairs in gate at t0 and t0+1 per configuration
    return o
tag = sys.argv[1]; d = Path(__file__).resolve().parent / "results_q2" / tag
ch = [np.loadtxt(d / f"c{i}.txt", comments="#") for i in range(16)]
full = est(ch); n = len(ch); drops = [est(ch[:i] + ch[i + 1:]) for i in range(n)]
err = {k: float(np.sqrt((n - 1) / n * sum((dd[k] - np.mean([e[k] for e in drops])) ** 2 for dd in drops))) for k in full}
L = []
for g in GN:
    L.append(f"{g:6s} frac={full['frac_'+g]:.6e}({err['frac_'+g]:.1e}) R1={full['R1_'+g]:.5f}({err['R1_'+g]:.5f}) R2={full['R2_'+g]:.5f}({err['R2_'+g]:.5f}) "
             + " ".join(f"R{t}={full[f'R{t}_{g}']:.5f}({err[f'R{t}_{g}']:.5f})" for t in range(3, 7)))
    if g != "all":
        L.append(f"       indicator RI1={full['RI1_'+g]:.5f}({err['RI1_'+g]:.5f}) RI2={full['RI2_'+g]:.5f}({err['RI2_'+g]:.5f}); "
                 f"conditional Rc1={full['Rc1_'+g]:.4f}({err['Rc1_'+g]:.4f}) Rc2={full['Rc2_'+g]:.4f}({err['Rc2_'+g]:.4f}); pairs(t,t+1)/config={full['pairs1_'+g]:.4g}")
for g in GN[1:4]:
    for t in (1, 2):
        k = f"D{t}_{g}-clear"; L.append(f"{k}: {full[k]:+.5f}({err[k]:.5f}) z={full[k]/err[k]:+.1f}")
        # conditional differences vs clear conditional
        dk = full[f"Rc{t}_{g}"] - full[f"Rc{t}_clear"]
        de = np.sqrt((n - 1) / n * sum(((dd[f"Rc{t}_{g}"] - dd[f"Rc{t}_clear"]) - np.mean([e[f"Rc{t}_{g}"] - e[f"Rc{t}_clear"] for e in drops])) ** 2 for dd in drops))
        L.append(f"  conditional Rc{t}_{g} - Rc{t}_clear: {dk:+.4f}({de:.4f}) z={dk/de:+.1f}")
s = "\n".join(L); print(s); open(d / "more.txt", "x").write(s + "\n")
