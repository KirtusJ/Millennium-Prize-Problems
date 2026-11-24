"""Measured only (no predicate): paired delete-one-chain jackknife of R_comp(t) - R_single(t), ungated, t = 1, 2. Output results_q2/main/diff.txt (mode x)."""
import numpy as np, runpy, sys
sys.argv = ["an_q3.py", "main"]
src = open("an_q3.py").read().split("res = {")[0]          # reuse loaders/definitions only (no output files)
ns = {"__file__": "an_q3.py"}; exec(src, ns)
R, jack, NU = ns["R"], ns["jack"], ns["NU"]
d, e = jack(lambda idx: R("u", "comp", NU, idx)[1:3] - R("u", "single", NU, idx)[1:3])
txt = f"ungated R_comp - R_single: t=1 {d[0]:+.5f}({e[0]:.5f}) z {d[0]/e[0]:+.2f}; t=2 {d[1]:+.5f}({e[1]:.5f}) z {d[1]/e[1]:+.2f}"
print(txt); open("results_q2/main/diff.txt", "x").write(txt + "\n")
