"""CONTROL for z1-mix6: G4's replicas.rs, built unchanged, side 6, T=12, beta=3.276133577, W=-I.

Predicates fixed before the first run:
 C1 (bit replay): with G4's seeds (base 1700451 + 7919 i, hot = i%2, 288 burn, 144 samples)
    the four output CSVs are byte-identical to g4/full-complement/unz_fixed/minus6-s{i}.csv.
    Tolerance: none (deterministic integer RNG, same code; only compiler/libm could differ;
    if bytes differ we fall back to max abs difference <= 1e-9 and say so).
 C2 (independent-seed replay): new seeds base 7700451 + 7919 i, same design; the four-face ratio
    J/Var agrees with G4's 0.0464(55) within 2 combined sigma, sigma_c = sqrt(s_mine^2 + 0.0055^2).
    2 sigma: conventional ~95% two-sided band; s from the delete-one-stream jackknife (G4's estimator).
 C3 same for the one-face ratio 0.0639(23).
 C4 (thermalisation, my run): hot-start and cold-start stratified four-face ratios agree within
    2 sigma where sigma is estimated as the delete-one-stream error of the pooled estimate times sqrt(2)
    (each stratum has half the streams). Measured, reported.
Result files are opened with mode "x". Exit code 0 if script completed (predicate outcomes printed,
not encoded in the exit code).
"""
import subprocess, sys, json, os
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXE = ROOT / "build" / "g4_replicas"
BETA = "3.276133577"


def run(base, tag):
    out = ROOT / "results" / tag
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    for i in range(4):
        cmd = [str(EXE), "fixed", BETA, str(base + 7919 * i), str(i % 2), "288", "144", "6", "12", "-1"]
        r = subprocess.run(cmd, capture_output=True, check=True)
        with open(out / f"minus6-s{i}.csv", "xb") as fh:
            fh.write(r.stdout)
        with open(out / f"minus6-s{i}.cmd", "x") as fh:
            fh.write(" ".join(cmd) + "\n")
        rows.append(np.loadtxt(out / f"minus6-s{i}.csv", skiprows=1, delimiter=","))
    return rows


def estimate(rows):  # G4's estimator from fixed.py
    data = np.concatenate(rows)
    var = data[:, :2].var(axis=0)
    j = data[:, 3:5].mean(axis=0)
    return np.r_[data[:, 2].mean(), var, j, j / var]


def jack(rows):
    full = estimate(rows)
    n = len(rows)
    drops = np.stack([estimate(rows[:i] + rows[i + 1:]) for i in range(n)])
    err = np.sqrt((n - 1) * np.mean((drops - drops.mean(axis=0)) ** 2, axis=0))
    return full, err


NAMES = ["spread", "var1", "var4", "J1", "J4", "ratio1", "ratio4"]


def main():
    res = {}
    # C1
    rows = run(1700451, "ctl_g4seeds")
    same = []
    for i in range(4):
        a = (ROOT / "results/ctl_g4seeds" / f"minus6-s{i}.csv").read_bytes()
        b = (ROOT / "g4/full-complement/unz_fixed" / f"minus6-s{i}.csv").read_bytes()
        same.append(a == b)
    g = [np.loadtxt(ROOT / "g4/full-complement/unz_fixed" / f"minus6-s{i}.csv", skiprows=1, delimiter=",") for i in range(4)]
    maxdiff = max(float(np.abs(x - y).max()) for x, y in zip(rows, g))
    res["C1_bytes_identical_per_stream"] = same
    res["C1_maxabsdiff"] = maxdiff
    res["C1"] = "MET" if all(same) else ("MET(numeric)" if maxdiff <= 1e-9 else "FAILED")
    f, e = jack(rows)
    res["g4seeds"] = {k: [float(v), float(s)] for k, v, s in zip(NAMES, f, e)}
    # C2/C3
    rows2 = run(7700451, "ctl_newseeds")
    f, e = jack(rows2)
    res["newseeds"] = {k: [float(v), float(s)] for k, v, s in zip(NAMES, f, e)}
    for name, ref, rs, idx in (("C2", 0.0464, 0.0055, 6), ("C3", 0.0639, 0.0023, 5)):
        sc = np.hypot(e[idx], rs)
        z = (f[idx] - ref) / sc
        res[name] = {"value": float(f[idx]), "err": float(e[idx]), "ref": ref, "z": float(z),
                     "verdict": "MET" if abs(z) <= 2 else "FAILED"}
    cold = estimate(rows2[0::2]); hot = estimate(rows2[1::2])
    z4 = (cold[6] - hot[6]) / (np.sqrt(2) * e[6] * np.sqrt(2))
    res["C4"] = {"cold_ratio4": float(cold[6]), "hot_ratio4": float(hot[6]), "z": float(z4),
                 "verdict": "MET" if abs(z4) <= 2 else "FAILED"}
    res["per_stream_newseeds"] = [{"stream": i, "hot": i % 2, **{k: float(v) for k, v in zip(NAMES, estimate([r]))}} for i, r in enumerate(rows2)]
    with open(ROOT / "results" / "ctl_summary.json", "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
