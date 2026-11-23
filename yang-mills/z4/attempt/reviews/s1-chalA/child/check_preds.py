"""Evaluates predicates P1-P5 (as fixed in run_main.py docstring) from results.json. Read-only. Deterministic."""
import json,numpy as np
r=json.load(open('results.json')); cs=r['cstar']; R=r['runs']
mono=lambda e:all(e[i+1]<=e[i] for i in range(len(e)-1))
for d in r['direct']: print('P1 beta',d['beta'],d['reldiff']<d['tol'],d['reldiff'],d['tol'])
print('P2',all(abs(x['A']-x['alt']['A'])<1e-3 for x in R),[abs(x['A']-x['alt']['A']) for x in R])
eA=[abs(x['A']-cs)/cs for x in R]; eC=[abs(x['C']-cs/2)/(cs/2) for x in R]
print('P3',eA[-1]<.15 and abs(R[-1]['A']-cs)<abs(R[-1]['A']-2*cs) and mono(eA),eA)
print('P4',eC[-1]<.15 and mono(eC),eC)
p5=[x['B']-x['A']-np.log(x['lam_e'])/np.sqrt(x['beta']) for x in R]
print('P5',all(abs(v)<1e-9 for v in p5),p5)
d=[cs-x['A'] for x in R]; print('c*-A',d,'ratios',[d[i+1]/d[i] for i in range(3)])
d=[cs/2-x['C'] for x in R]; print('c*/2-C',d,'ratios',[d[i+1]/d[i] for i in range(3)])
print('A/cs',[x['A']/cs for x in R])
