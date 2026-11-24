"""c2-grow Q2 analysis. usage: python3 an_q3.py <tag> -> results_q2/<tag>/summary.txt, summary.json (mode x)
Per chain sums over configurations of the q3 line. For a mark m (zero off-gate), N = number of (root, orientation, t0) sites
per configuration (15552 gated / 324 ungated), C(t) = S2[t]/(N nconf) - (S1/(N nconf))^2, R(t) = C(t)/C(0), t = 0..4.
Errors: delete-one-chain jackknife over 16 chains.
Predicates (fixed before the run):
  R1 (brief) a gated R(t) is reported only if the total number of gated pairs at t = 1 (all chains) is >= 200; otherwise 'not resolved'.
  T2 hot/cold: plaquette and ungated composite R(1): |cold - hot| <= 2 * (2 e_16) (prior T2 convention).
  T3 plaquette vs prior q2 .7500018(40): |z| <= 2.   T4 ungated single four-face mark R(1) vs prior .01354(9): |z| <= 2.
Measured only: gate fractions, pair counts, conditional correlation among gated pairs (S2[t] / sqrt(S2[0]...) not used).
"""
import json, sys, numpy as np
from pathlib import Path
ROOT = Path(__file__).resolve().parent
tag = sys.argv[1]; d = ROOT / "results_q2" / tag
ch = [np.loadtxt(d / f"c{i}.txt", comments="#", ndmin=2) for i in range(16)]
NG, NU = 27 * 48 * 12, 27 * 12
def blocks(A):  # column layout
    out = {}; c = 1
    for g in ("g0.6", "g1.2"):
        out[g + ".count"] = A[:, c]; c += 1
        for m in ("comp", "single"):
            out[f"{g}.{m}.S1"] = A[:, c]; out[f"{g}.{m}.S2"] = A[:, c + 1:c + 6]; c += 6
        out[g + ".I2"] = A[:, c:c + 5]; c += 5
    out["u.count"] = A[:, c]; c += 1
    for m in ("comp", "single"):
        out[f"u.{m}.S1"] = A[:, c]; out[f"u.{m}.S2"] = A[:, c + 1:c + 6]; c += 6
    assert c == A.shape[1], (c, A.shape)
    out["plaq"] = A[:, 0]; return out
B = [blocks(A) for A in ch]
def tot(key, idx): return sum(B[i][key].sum(0) for i in idx), sum(len(B[i]["plaq"]) for i in idx)
def R(prefix, m, N, idx):
    S1, nc = tot(f"{prefix}.{m}.S1", idx); S2, _ = tot(f"{prefix}.{m}.S2", idx)
    mu = S1 / (N * nc); C = S2 / (N * nc) - mu ** 2; return C / C[0]
def jack(f):
    full = f(list(range(16))); dr = np.array([f([j for j in range(16) if j != k]) for k in range(16)])
    return full, np.sqrt(15 / 16 * ((dr - dr.mean(0)) ** 2).sum(0))
res = {"nconf_per_chain": [len(b["plaq"]) for b in B]}
pl, ple = jack(lambda idx: np.array([np.concatenate([B[i]["plaq"] for i in idx]).mean()]))
res["plaq"] = [float(pl[0]), float(ple[0])]
lines = [f"tag {tag} chains 16 configs {sum(res['nconf_per_chain'])} plaquette {pl[0]:.7f}({ple[0]:.7f})"]
for g in ("g0.6", "g1.2"):
    cnt, nc = tot(g + ".count", range(16)); I2, _ = tot(g + ".I2", range(16))
    fr, fre = jack(lambda idx: np.array([tot(g + ".count", idx)[0] / (NG * tot(g + ".count", idx)[1])]))
    res[g] = {"gated_sites": float(cnt), "fraction": [float(fr[0]), float(fre[0])], "pairs_t": I2.tolist(), "R1_resolved": bool(I2[1] >= 200)}
    lines.append(f"{g}: gate fraction {fr[0]:.4e}({fre[0]:.1e}) gated sites {int(cnt)} pairs t=0..4 {I2.astype(int).tolist()} R1 resolved {I2[1] >= 200}")
    if I2[1] >= 200:
        for m in ("comp", "single"):
            r, e = jack(lambda idx: R(g, m, NG, idx)); res[g][m] = {"R": r.tolist(), "err": e.tolist()}
            lines.append(f"  {m}: R(t) " + " ".join(f"{a:.5f}({b:.5f})" for a, b in zip(r, e)))
    else:
        lines.append("  not resolved (fewer than 200 gated pairs at t=1): no R(t) reported")
for m in ("comp", "single"):
    r, e = jack(lambda idx: R("u", m, NU, idx)); res["u." + m] = {"R": r.tolist(), "err": e.tolist()}
    lines.append(f"ungated {m} (identity orientation, 324 sites/conf): R(t) " + " ".join(f"{a:.5f}({b:.5f})" for a, b in zip(r, e)))
# T2
t2 = {}
for lab, f in (("plaq", lambda idx: np.array([np.concatenate([B[i]["plaq"] for i in idx]).mean()])), ("u.comp.R1", lambda idx: R("u", "comp", NU, idx)[1:2])):
    full, e = jack(f); cold = f(list(range(0, 16, 2)))[0]; hot = f(list(range(1, 16, 2)))[0]; z = (cold - hot) / (2 * e[0])
    t2[lab] = {"cold": float(cold), "hot": float(hot), "z": float(z), "met": bool(abs(z) <= 2)}
res["T2"] = t2
z3 = (pl[0] - .7500018) / np.hypot(ple[0], .0000040); res["T3"] = {"z": float(z3), "met": bool(abs(z3) <= 2)}
r1 = res["u.single"]["R"][1]; e1 = res["u.single"]["err"][1]; z4 = (r1 - .01354) / np.hypot(e1, .00009)
res["T4"] = {"z": float(z4), "met": bool(abs(z4) <= 2)}
lines.append(f"T2 {t2}"); lines.append(f"T3 plaquette vs prior z {z3:.2f} met {abs(z3) <= 2}; T4 ungated single R(1) vs prior .01354(9) z {z4:.2f} met {abs(z4) <= 2}")
txt = "\n".join(lines); print(txt)
with open(d / "summary.txt", "x") as fh: fh.write(txt + "\n")
with open(d / "summary.json", "x") as fh: json.dump(res, fh, indent=1)
