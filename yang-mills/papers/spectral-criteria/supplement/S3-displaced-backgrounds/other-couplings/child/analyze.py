"""Usage: analyze.py <prod.json> <outfile>. Delete-one-chain jackknife of C(t)/C(0), gate fractions, plaquette."""
import sys, json, numpy as np
d = json.load(open(sys.argv[1])); ch = d['chains']; K = len(ch); lines = []
def est(sel, k):
    s = sum(ch[i]['acc'][k]['s'] for i in sel); n = sum(ch[i]['acc'][k]['n'] for i in sel)
    mu = s/n; C = [sum(ch[i]['acc'][k]['p'][t] for i in sel)/sum(ch[i]['acc'][k]['pn'][t] for i in sel) - mu**2 for t in range(3)]
    fr = sum(ch[i]['acc'][k]['frac'] for i in sel)/n
    return np.array([C[1]/C[0], C[2]/C[0], fr, mu, C[0]])
lines.append(f"params {d['params']}; chains={K}")
for k in ch[0]['acc']:
    full = est(range(K), k); J = np.array([est([j for j in range(K) if j != i], k) for i in range(K)])
    err = np.sqrt((K-1)/K*((J-J.mean(0))**2).sum(0))
    lines.append(f"{k:8s} C1/C0={full[0]:.4f}+-{err[0]:.4f}  C2/C0={full[1]:.4f}+-{err[1]:.4f}  frac={full[2]:.4f}+-{err[2]:.4f}  <m>={full[3]:.5f}  C0={full[4]:.5f}")
p = np.array([c['plaq'] for c in ch]); lines.append(f"avg plaquette={p.mean():.6f}+-{p.std(ddof=1)/np.sqrt(K):.6f} (chain-to-chain SE)")
s = "\n".join(lines); print(s)
with open(sys.argv[2], 'x') as f: f.write(s+"\n")
