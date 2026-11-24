"""d2-time: clear-skeleton weights. usage: python3 fitw.py
Runs build/z1mx5 'fixed' on results/gen/chain.skel0.txt with the prior G-clear0 design (32 streams, seed 11300001 + 7919 i,
hot = i % 2, burn 576, 1152 samples, spacing 6) into results/F-clear0 (a reproduction of prior G-clear0), then fits the L4 (308)
and L1 (15) weights on TRAIN 0..15 exactly as prior an4.py (C-whitening, truncation 1e-10, w normalised to max|w| = 1).
Writes weights/w_clear.txt (rows w_L4, w_L1 embedded, f4) and results/F-clear0/fitw.txt (mode 'x').
Predicates (fixed before the run):
 RP1 train lambda and held q for L4 and L1 equal the prior record (L4 .04097 / .04283; L1 .05874 / .05894) within half a unit of
     the last printed digit (5e-6): same chain, same estimator. Tolerance = rounding of the prior printout.
Also writes, for the -I prior weights, nothing: they are taken from prior_weights/ unchanged.
"""
import subprocess, sys
import numpy as np
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
R = Path(__file__).resolve().parent; out = R / "results" / "F-clear0"
def one(i):
    out_i = out / f"s{i}"
    if not (out / f"s{i}.Dc.txt").exists():
        subprocess.run([str(R / "build/z1mx5"), "fixed", "3.276133577", str(11300001 + 7919 * i), str(i % 2), "576", "1152", "6", "6", "12",
                        str(R / "results/gen/chain.skel0.txt"), str(out_i)], check=True)
if len(sys.argv) < 2 or sys.argv[1] != "fitonly":
    out.mkdir(parents=True, exist_ok=False)
    with ThreadPoolExecutor(2) as ex: list(ex.map(one, range(32)))
names = (out / "s0.X.csv").read_text().splitlines()[0].split(",")
assert names == [l.strip() for l in open(R / "prior_weights/names.txt")]
st = []
for i in range(32):
    X = np.loadtxt(out / f"s{i}.X.csv", delimiter=",", skiprows=1)
    D = np.array([float(v) for v in [l for l in (out / f"s{i}.Dc.txt").read_text().splitlines() if not l.startswith("#")][0].split()]).reshape(308, 308)
    st.append((len(X), X.sum(0), X.T @ X, D))
def CD(idx, sel):
    m = sum(st[i][0] for i in idx); s1 = sum(st[i][1] for i in idx)[sel]; s2 = sum(st[i][2] for i in idx)[np.ix_(sel, sel)]
    mu = s1 / m; return s2 / m - np.outer(mu, mu), np.mean([st[i][3][np.ix_(sel, sel)] for i in idx], axis=0)
def gsolve(C, D, rel=1e-10):
    l, V = np.linalg.eigh(C); keep = l > rel * l.max(); T = V[:, keep] / np.sqrt(l[keep]); M = T.T @ D @ T; M = (M + M.T) / 2
    mu, U = np.linalg.eigh(M); w = T @ U[:, 0]; return float(mu[0]), w / w[np.argmax(np.abs(w))], int((~keep).sum())
L1 = [names.index(n) for n in ["B.xy000.g00", "B.xy000.g10", "B.xy000.g01", "B.xy000.g11", "B.xy000.Rv", "B.xy000.Rh", "B.xy000.L_no11"]
      + [f"B.xy200.g{a}" for a in ("00", "10", "01", "11")] + [f"B.yz204.g{a}" for a in ("00", "10", "01", "11")]]
w1names = [l.split()[0] for l in open(R / "prior_weights/w_L1.txt")]
assert [names[k] for k in L1] == w1names, "L1 order"
TR, HE = list(range(16)), list(range(16, 32)); rows = []; txt = []; ok = True
for lab, sel, pl, pq in (("L4", list(range(308)), .04097, .04283), ("L1", L1, .05874, .05894)):
    C, D = CD(TR, sel); lam, w, nt = gsolve(C, D); Ch, Dh = CD(HE, sel); q = float(w @ Dh @ w / (w @ Ch @ w))
    met = abs(lam - pl) <= 5e-6 and abs(q - pq) <= 5e-6; ok &= met
    txt.append(f"RP1 {lab}: train lambda {lam:.7f} (prior {pl}) held q {q:.7f} (prior {pq}) truncated {nt}: {'MET' if met else 'FAILED'}")
    full = np.zeros(308); full[sel] = w; rows.append(full)
f4 = np.zeros(308); f4[:4] = .25; rows.append(f4)
with open(R / "weights/w_clear.txt", "x") as fh:
    fh.write("# rows: w_L4 (clear, fitw.py on F-clear0 TRAIN), w_L1 (embedded), f4\n")
    for w in rows: fh.write(" ".join(f"{v:.13e}" for v in w) + "\n")
with open(out / "fitw.txt", "x") as fh: fh.write("\n".join(txt) + "\n")
print("\n".join(txt)); sys.exit(0 if ok else 1)
