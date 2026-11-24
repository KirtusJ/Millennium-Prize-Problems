"""Corrected reducer for z1-mix6-format runs (e2-repair, T230).

usage:
  python3 reduce_fixed.py stream <results dir> <out json>        reduce one run directory
  python3 reduce_fixed.py ratio <summaryA json> <summaryB json> <out json>   Q = r(A)/r(B)

Data: <dir>/s<i>.csv (columns single, average, spread, j_single, j_average, single_tl, average_tl, j_single_tl,
j_average_tl, mean_tries), <dir>/s<i>.meta.txt with line "args fixed <beta> <seed> <hot> ...".

Estimators (unchanged from reduce.py / G4): pooled ddof-0 variance over all measurements of all streams, J = pooled
mean, r = J/Var, error = delete-one-stream jackknife sqrt((n-1)/n sum (drop - mean)^2).

FIX: streams are ordered by NUMERICAL ID (int after 's'); stratum hot = ID % 2 == 1. reduce.py sorted filenames
lexically (s0,s1,s10,s11,...,s19,s2,s20,...) and took list positions 0::2 as cold, 1::2 as hot; for 24 streams that
assigns e.g. s10 (cold start) to "hot". For <= 10 streams the lexical and numeric orders coincide.

Predicates (fixed before the first run of this program):
 F1 (hard assertion): for every stream the hot flag recorded in meta "args" (token 4) equals ID % 2.
 F2 hot/cold: z = (r_hot - r_cold)/(2 SE_pooled), |z| <= 2, for r1, r4, r1_tl, r4_tl. Tolerance 2 = prior
    preregistered tolerance (z1-mix6 run.py T2). Sign convention hot - cold (G4's); reduce.py reported cold - hot.
 F3 drift (new runs): first half vs second half of each stream's measurements, d = (r2 - r1)/sqrt(e1^2+e2^2),
    |d| <= 2 (conventional ~95%); halves treated as independent.
 Also reported (measured only): the legacy (lexical) z, computed exactly as reduce.py did, to show the defect.
 ratio: Q = rA/rB, independent-arm error e_Q = Q sqrt((eA/rA)^2+(eB/rB)^2); paired-by-index jackknife as sensitivity
    (only meaningful if arm streams are paired; here they are not, seeds independent).
Output files opened with mode 'x' (never overwritten).
"""
import json, sys
import numpy as np
from pathlib import Path


def est(items):
    d = np.concatenate(items)
    v1, v4, v1t, v4t = d[:, 0].var(), d[:, 1].var(), d[:, 5].var(), d[:, 6].var()
    j1, j4, j1t, j4t = d[:, 3].mean(), d[:, 4].mean(), d[:, 7].mean(), d[:, 8].mean()
    return {"J1": j1, "Var1": v1, "J4": j4, "Var4": v4, "r1": j1 / v1, "r4": j4 / v4,
            "J1_tl": j1t, "Var1_tl": v1t, "J4_tl": j4t, "Var4_tl": v4t,
            "r1_tl": j1t / v1t if v1t > 0 else float("nan"), "r4_tl": j4t / v4t if v4t > 0 else float("nan")}


def jack(items, f=est):
    full = f(items); n = len(items)
    drops = [f(items[:i] + items[i + 1:]) for i in range(n)]
    out = {}
    for k in full:
        x = np.array([dd[k] for dd in drops], dtype=float)
        out[k] = [float(full[k]), float(np.sqrt((n - 1) / n * np.sum((x - x.mean()) ** 2)))]
    return out


def load(d):
    d = Path(d)
    ids = sorted(int(p.name[1:-4]) for p in d.glob("s*.csv") if not p.name.endswith("colours.csv"))
    data, flags, seeds = [], [], []
    for i in ids:
        data.append(np.loadtxt(d / f"s{i}.csv", skiprows=1, delimiter=",", ndmin=2))
        args = [l for l in (d / f"s{i}.meta.txt").read_text().splitlines() if l.startswith("args")][0].split()
        flags.append(int(args[4])); seeds.append(int(args[3]))
    return ids, data, flags, seeds


def hotcold(ids, data, pooled):
    hot = est([m for i, m in zip(ids, data) if i % 2 == 1]); cold = est([m for i, m in zip(ids, data) if i % 2 == 0])
    z = {}
    for k in ("r1", "r4", "r1_tl", "r4_tl"):
        e = pooled[k][1]
        z[k] = {"z_hot_minus_cold": float((hot[k] - cold[k]) / (2 * e)), "r_hot": float(hot[k]), "r_cold": float(cold[k])}
        z[k]["verdict"] = "MET" if abs(z[k]["z_hot_minus_cold"]) <= 2 else "FAILED"
    return z


def legacy(d, pooled):
    files = sorted([p for p in Path(d).glob("s*.csv") if not p.name.endswith("colours.csv")], key=lambda p: p.name)
    main = [np.loadtxt(p, skiprows=1, delimiter=",", ndmin=2) for p in files]
    cold = est(main[0::2]); hot = est(main[1::2])
    return {"lexical_order": [p.name for p in files],
            **{k: float((cold[k] - hot[k]) / (2 * pooled[k][1])) for k in ("r1", "r4", "r1_tl", "r4_tl")}}


def stream(d, out):
    ids, data, flags, seeds = load(d)
    for i, f in zip(ids, flags):
        assert f == i % 2, f"F1 violated: stream s{i} recorded hot={f}, ID parity {i % 2}"
    pooled = jack(data)
    res = {"dir": str(Path(d).resolve()), "ids": ids, "seeds": seeds, "n_streams": len(ids),
           "n_hot": int(sum(i % 2 for i in ids)), "measurements": sorted(set(len(m) for m in data)),
           "F1_split_matches_meta": "MET", "pooled": pooled, "hotcold_numeric": hotcold(ids, data, pooled),
           "legacy_lexical_cold_minus_hot_z": legacy(d, pooled)}
    nm = min(len(m) for m in data); h = nm // 2
    first = jack([m[:h] for m in data]); second = jack([m[h:nm] for m in data])
    dr = {}
    for k in ("r1", "r4", "J1", "J4", "Var1", "Var4"):
        dd = (second[k][0] - first[k][0]) / np.hypot(first[k][1], second[k][1])
        dr[k] = {"first": first[k], "second": second[k], "d": float(dd)}
        if k in ("r1", "r4"):
            dr[k]["verdict"] = "MET" if abs(dd) <= 2 else "FAILED"
    res["drift_halves"] = dr
    with open(out, "x") as fh:
        json.dump(res, fh, indent=1)
    p = pooled; hc = res["hotcold_numeric"]; lg = res["legacy_lexical_cold_minus_hot_z"]
    print(f"{d}: n={len(ids)} hot={res['n_hot']} J1={p['J1'][0]:.6f}({p['J1'][1]:.6f}) Var1={p['Var1'][0]:.5f}({p['Var1'][1]:.5f}) "
          f"J4={p['J4'][0]:.7f}({p['J4'][1]:.7f}) Var4={p['Var4'][0]:.5f}({p['Var4'][1]:.5f}) "
          f"r1={p['r1'][0]:.5f}({p['r1'][1]:.5f}) r4={p['r4'][0]:.5f}({p['r4'][1]:.5f}) "
          f"r1tl={p['r1_tl'][0]:.5f}({p['r1_tl'][1]:.5f}) r4tl={p['r4_tl'][0]:.5f}({p['r4_tl'][1]:.5f})")
    print(f"   hot-cold z numeric: r1 {hc['r1']['z_hot_minus_cold']:+.2f} {hc['r1']['verdict']}, r4 {hc['r4']['z_hot_minus_cold']:+.2f} {hc['r4']['verdict']}, "
          f"r1tl {hc['r1_tl']['z_hot_minus_cold']:+.2f}, r4tl {hc['r4_tl']['z_hot_minus_cold']:+.2f} | legacy cold-hot r1 {lg['r1']:+.2f} r4 {lg['r4']:+.2f}")
    print(f"   drift d: r1 {dr['r1']['d']:+.2f} {dr['r1']['verdict']}, r4 {dr['r4']['d']:+.2f} {dr['r4']['verdict']}")


def ratio(a, b, out):
    A, B = json.load(open(a)), json.load(open(b))
    res = {"A": a, "B": b}
    da = load(A["dir"])[1]; db = load(B["dir"])[1]
    n = min(len(da), len(db))
    for k in ("r1", "r4", "r1_tl", "r4_tl"):
        ra, ea = A["pooled"][k]; rb, eb = B["pooled"][k]
        q = ra / rb; e = q * np.hypot(ea / ra, eb / rb)
        drops = np.array([est(da[:i] + da[i + 1:n])[k] / est(db[:i] + db[i + 1:n])[k] for i in range(n)])
        ep = float(np.sqrt((n - 1) / n * np.sum((drops - drops.mean()) ** 2)))
        res[k] = {"Q": float(q), "err_independent": float(e), "err_paired_by_index_sensitivity": ep}
    with open(out, "x") as fh:
        json.dump(res, fh, indent=1)
    for k in ("r1", "r4", "r1_tl", "r4_tl"):
        print(f"Q_{k} = {res[k]['Q']:.4f} +- {res[k]['err_independent']:.4f} (indep)  [paired-index {res[k]['err_paired_by_index_sensitivity']:.4f}]")


if __name__ == "__main__":
    if sys.argv[1] == "stream":
        stream(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "ratio":
        ratio(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        raise SystemExit(__doc__)
