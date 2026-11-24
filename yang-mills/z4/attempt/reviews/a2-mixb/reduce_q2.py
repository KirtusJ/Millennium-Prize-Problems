"""Q2 reduction (a2-mixb). usage: python3 reduce_q2.py <tag> -> results_q2/<tag>/summary.json (mode 'x')
Columns per configuration: plaq; for gate g = 0..4 (all, <0.3, <0.6, <1.2, >1.2): count, S1, S2[0..6];
then for g = 1..4: I2[0..6]. Nsq = 324 marks per configuration (27 squares x 12 slices).
C_g(t) = mean(S2_g[t])/Nsq - (mean(S1_g)/Nsq)^2 (pooled over chains), R_g(t) = C_g(t)/C_g(0).
Indicator (measured only): CI_g(t) = mean(I2_g[t])/Nsq - frac_g^2, normalised by CI_g(0).
Errors: delete-one-chain jackknife. Predicates Q2-T1..T4 fixed in run_q2.py.
"""
import json, sys
import numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve().parent
NSQ = 324.0
GN = ["all", "lt0.3", "lt0.6", "lt1.2", "clear"]

def est(chains):
    d = np.concatenate(chains); m = d.mean(axis=0); out = {"plaq": m[0]}
    for g in range(5):
        b = 1 + 9 * g; f = m[b] / NSQ; mu = m[b + 1] / NSQ; C = m[b + 2:b + 9] / NSQ - mu ** 2
        out[f"frac_{GN[g]}"] = f; out[f"mean_{GN[g]}"] = mu; out[f"C0_{GN[g]}"] = C[0]
        for t in range(7): out[f"R{t}_{GN[g]}"] = C[t] / C[0]
    for g in range(1, 5):
        b = 46 + 7 * (g - 1); f = m[1 + 9 * g] / NSQ; CI = m[b:b + 7] / NSQ - f ** 2
        for t in range(7): out[f"RI{t}_{GN[g]}"] = CI[t] / CI[0]
    for g in range(1, 5):
        for t in (1, 2):
            out[f"D{t}_{GN[g]}-clear"] = out[f"R{t}_{GN[g]}"] - out[f"R{t}_clear"]
            out[f"D{t}_{GN[g]}-all"] = out[f"R{t}_{GN[g]}"] - out[f"R{t}_all"]
    return out

def jack(items):
    full = est(items); n = len(items); drops = [est(items[:i] + items[i + 1:]) for i in range(n)]
    return {k: [float(full[k]), float(np.sqrt((n - 1) / n * sum((dd[k] - np.mean([e[k] for e in drops])) ** 2 for dd in drops)))] for k in full}

def tau_int(x, c=6.0):
    x = x - x.mean(); n = len(x); v = x.var()
    if v == 0: return 0.5
    f = np.fft.rfft(x, 2 * n); acf = np.fft.irfft(f * np.conj(f))[:n] / (v * np.arange(n, 0, -1))
    tau = 0.5
    for w in range(1, n):
        tau += acf[w]
        if w >= c * tau: break
    return float(tau)

def main(tag):
    d = ROOT / "results_q2" / tag
    idx = sorted(int(p.stem[1:]) for p in d.glob("c[0-9]*.txt"))
    ch = [np.loadtxt(d / f"c{i}.txt", comments="#") for i in idx]
    n = len(ch); nconf = min(len(c) for c in ch)
    res = {"tag": tag, "chains": n, "nconf": [len(c) for c in ch], "pooled": jack(ch)}
    per = [est([c]) for c in ch]
    chk = {"Q2-T1": "MET" if n >= 8 and sum(i % 2 for i in idx) == n // 2 else "FAILED"}
    for k in ("plaq", "R1_all", "frac_lt1.2"):
        c = np.array([p[k] for i, p in zip(idx, per) if i % 2 == 0]); h = np.array([p[k] for i, p in zip(idx, per) if i % 2 == 1])
        z = (c.mean() - h.mean()) / np.sqrt(c.var(ddof=1) / len(c) + h.var(ddof=1) / len(h))
        chk[f"Q2-T2_{k}"] = {"z": float(z), "verdict": "MET" if abs(z) <= 2 else "FAILED"}
    cols = {"plaq": 0, "S2all0": 3, "S2all1": 4, "S2lt1.2_1": 1 + 27 + 3, "cnt_lt1.2": 28}
    taus = {k: [tau_int(c[:, j]) for c in ch] for k, j in cols.items()}
    mx = max(max(v) for v in taus.values())
    chk["Q2-T3_tau"] = {"max_tau_int": mx, "taus_max_per_series": {k: max(v) for k, v in taus.items()},
                        "verdict": "MET" if 2 * mx <= nconf / 100 else "FAILED"}
    dif = np.array([c[: len(c) // 2, 0].mean() - c[len(c) // 2:, 0].mean() for c in ch])
    z = dif.mean() / (dif.std(ddof=1) / np.sqrt(n))
    chk["Q2-T4_burnin"] = {"z": float(z), "verdict": "MET" if abs(z) <= 2 else "FAILED"}
    res["checks"] = chk
    res["per_chain_R1"] = {g: [float(p[f"R1_{g}"]) for p in per] for g in GN}
    with open(d / "summary.json", "x") as fh: json.dump(res, fh, indent=1)
    p = res["pooled"]
    print(f"{tag}: chains={n} nconf={nconf} plaq={p['plaq'][0]:.6f}({p['plaq'][1]:.6f})")
    for g in GN:
        print(f" {g:6s} frac={p['frac_'+g][0]:.6f}({p['frac_'+g][1]:.6f}) C0={p['C0_'+g][0]:.4e} "
              + " ".join(f"R{t}={p[f'R{t}_{g}'][0]:.4f}({p[f'R{t}_{g}'][1]:.4f})" for t in range(1, 7))
              + ("" if g == "all" else " | ind " + " ".join(f"RI{t}={p[f'RI{t}_{g}'][0]:.4f}({p[f'RI{t}_{g}'][1]:.4f})" for t in (1, 2))))
    for g in GN[1:]:
        for t in (1, 2):
            for ref in ("clear", "all"):
                k = f"D{t}_{g}-{ref}"
                if k in p: print(f" {k}: {p[k][0]:+.4f}({p[k][1]:.4f}) z={p[k][0]/p[k][1] if p[k][1]>0 else float('nan'):+.2f}")
    print(json.dumps(chk))

if __name__ == "__main__":
    main(sys.argv[1])
