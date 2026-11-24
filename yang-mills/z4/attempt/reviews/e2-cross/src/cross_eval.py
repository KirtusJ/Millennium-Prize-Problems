"""Evaluate the frozen optima trained at one temporal circumference on the HELD chains of the other.
Usage: python3 -I src/cross_eval.py OUTFILE (mode x). No predicates beyond: coefficient files load, Var>0 on both lattices.
Same estimators and jackknife as src/analysis.py (imported)."""
import sys, numpy as np
sys.path.insert(0, "/home/user/z4-workers/e2-cross/src")
import analysis as A
o = open(sys.argv[1], "x")
R = "/home/user/z4-workers/e2-cross/results/"
coef = {"2l": np.loadtxt(R + "analysis-2l.txt.coef"), "4l": np.loadtxt(R + "analysis-4l.txt.coef")}
ens = {"2l": ("c2", "f2"), "4l": ("c4", "f4")}
data = {k: A.load(k) for k in ("c2", "f2", "c4", "f4")}
he = lambda ch: [c for c in ch if c["i"] % 4 in (2, 3)]
for tr in ("2l", "4l"):
    for ev in ("2l", "4l"):
        c, f = ens[ev]
        for nm, a in zip(("fine-opt", "coarse-opt", "ratio-opt"), coef[tr]):
            Rf = A.jk(a, he(data[f]), lambda q: q[2]); Rc = A.jk(a, he(data[c]), lambda q: q[2])
            Ef = A.jk(a, he(data[f]), lambda q: q[1]); Ec = A.jk(a, he(data[c]), lambda q: q[1])
            r = Rf[0] / Rc[0]; sr = r * np.hypot(Rf[1] / Rf[0], Rc[1] / Rc[0])
            e = Ef[0] / Ec[0]; se = e * np.hypot(Ef[1] / Ef[0], Ec[1] / Ec[0])
            s = f"trained {tr} evaluated {ev} {nm:10s}: R_f={Rf[0]:.5f}+-{Rf[1]:.5f} R_c={Rc[0]:.5f}+-{Rc[1]:.5f} R_f/R_c={r:.4f}+-{sr:.4f} E_f/E_c={e:.5f}+-{se:.5f}"
            print(s); o.write(s + "\n")
