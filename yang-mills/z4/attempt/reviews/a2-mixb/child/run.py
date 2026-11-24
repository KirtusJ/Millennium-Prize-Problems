"""Production. Usage: run.py <outfile>. 6 independent hot-start chains (seeds 100..105), 300 thermalisation sweeps,
150 configurations per chain separated by 10 heat-bath sweeps. Per-chain accumulators written to <outfile> (mode 'x')."""
import sys, json, numpy as np
from lat import *
NCH, THERM, NCFG, SEP = 6, 300, 150, 10
GATES = {'ungated': None, 'g0.6': ('lt', 0.6), 'g1.2': ('lt', 1.2), 'clear': ('gt', 1.2)}
out = dict(params=dict(NCH=NCH, THERM=THERM, NCFG=NCFG, SEP=SEP, beta=BETA), chains=[])
for c in range(NCH):
    rng = np.random.default_rng(100+c); U = haar(rng, (4,)+DIMS)
    for _ in range(THERM): sweep(U, rng)
    acc = {k: dict(s=0.0, n=0, p=[0.0, 0.0, 0.0], pn=[0, 0, 0], frac=0.0) for k in GATES}; pl = []
    for i in range(NCFG):
        for _ in range(SEP): sweep(U, rng)
        pl.append(avg_plaq(U)); m1, th = marks(U)
        for k, g in GATES.items():
            ind = np.ones_like(m1) if g is None else ((th < g[1]) if g[0] == 'lt' else (th > g[1])).astype(float)
            m = m1*ind; a = acc[k]; a['s'] += m.sum(); a['n'] += m.size; a['frac'] += ind.sum()
            for t in range(3):
                a['p'][t] += (m*np.roll(m, -t, axis=3)).sum(); a['pn'][t] += m.size
    out['chains'].append(dict(acc=acc, plaq=float(np.mean(pl)), plaq_sd=float(np.std(pl))))
    print('chain', c, 'plaq', np.mean(pl), flush=True)
with open(sys.argv[1], 'x') as f: json.dump(out, f)
