"""compare.py -- lattice G_b(t) (results_L1.txt, my program) against the continuum mode sum
(rerun/results_continuum.txt, the sub-agent's program rerun by me in a fresh directory).

PREDICATES (fixed before the first run)
C0 the rerun continuum file is identical to child/results_continuum.txt (byte-for-byte) [determinism].
C1 for t in {0.05, 0.1, 0.2}, both R: Richardson value with N=128,256, G256 + (G256-G128)/3, agrees with the
   continuum G(t) to relative 1e-3 [my tolerance; O(b^4) remainder estimated from d256/d128 ratios ~ 4-5].
C2 same for t = 0.02 (EXPECTED TO FAIL: lattice not in the O(b^2) regime, d128/d256 ~ 2).
C3 for t in {0.05, 0.1, 0.2}: |G256 - Gcont| < |G128 - Gcont| (lattice approaches the continuum value).
C4 measured only: lattice rate(5->6)=2N sin(pi/N) and continuum rate(t=3) ~ 2pi + O(e^{-2.6 t}).
"""
import re, sys, os
B = "C:/Users/donke/z4-workers/r6-loop/"
OUT = B + "results_compare.txt"
if os.path.exists(OUT): print("exists"); sys.exit(3)
lat = {}
for line in open(B + "results_L1.txt"):
    m = re.match(r"^(0\.25|0\.125) (\d+) (.+)$", line.strip())
    if m:
        vals = [float(v) for v in m.group(3).split()]
        for t, v in zip([0.0, 0.02, 0.05, 0.1, 0.2], vals): lat[(float(m.group(1)), int(m.group(2)), t)] = v
cont = {}
for line in open(B + "rerun/results_continuum.txt"):
    if line.startswith("#"): continue
    p = line.split(); cont[(float(p[0]), float(p[1]))] = float(p[2])
L = []; met = fail = 0
def pred(n, ok, s):
    global met, fail
    met += ok; fail += (not ok); L.append(f"[{'MET' if ok else 'FAIL'}] {n} {s}")
pred("C0 rerun identical", open(B + "rerun/results_continuum.txt", "rb").read() == open(B + "child/results_continuum.txt", "rb").read(), "")
for R in [0.25, 0.125]:
    for t in [0.02, 0.05, 0.1, 0.2]:
        g1, g2, gc = lat[(R, 128, t)], lat[(R, 256, t)], cont[(R, t)]
        ext = g2 + (g2 - g1) / 3; rel = abs(ext - gc) / gc
        name = "C2" if t == 0.02 else "C1"
        pred(f"{name} R={R} t={t}", rel < 1e-3, f"G128={g1:.8e} G256={g2:.8e} ext={ext:.8e} cont={gc:.8e} rel={rel:.2e}")
        if t != 0.02:
            pred(f"C3 R={R} t={t}", abs(g2 - gc) < abs(g1 - gc), f"err128={(g1-gc)/gc:.2e} err256={(g2-gc)/gc:.2e}")
L.append(f"COUNTS met={met} failed={fail} measured_only=1")
open(OUT, "w").write("\n".join(L) + "\n"); print("\n".join(L))
sys.exit(0 if fail == 0 else 1)
