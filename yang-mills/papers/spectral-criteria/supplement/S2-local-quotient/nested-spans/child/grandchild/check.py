"""T225 independent recomputation.
Predicates fixed BEFORE running:
 P1: top-left 15x15 block of C(TRAIN) is symmetric and positive definite (Cholesky succeeds).
 P2: quotient D(HELD)_kk / C(HELD)_kk for B.xy000.g00 is finite and positive.
Results written to results.txt (opened with mode 'x').
Rerun: rm -f results.txt; python3 check.py   (from grandchild/)
"""
import numpy as np, os
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
names = [l.strip() for l in open(f'{d}/names.txt') if l.strip()]
def load(i):
    m = float(np.loadtxt(f'{d}/s{i}.m.txt'))
    return (m, np.loadtxt(f'{d}/s{i}.sum1.txt').reshape(-1),
            np.loadtxt(f'{d}/s{i}.sum2.txt'), np.loadtxt(f'{d}/s{i}.D.txt'))
S = [load(i) for i in range(32)]
def agg(idx):
    M = sum(S[i][0] for i in idx)
    mu = sum(S[i][1] for i in idx) / M
    C = sum(S[i][2] for i in idx) / M - np.outer(mu, mu)
    D = sum(S[i][3] for i in idx) / len(idx)
    return C, D
Ct, _ = agg(range(16)); Ch, Dh = agg(range(16, 32))
k = names.index('B.xy000.g00')
q = Dh[k, k] / Ch[k, k]
B = Ct[:15, :15]
sym = np.allclose(B, B.T, rtol=1e-10, atol=0); asym = np.abs(B - B.T).max()
try: np.linalg.cholesky((B + B.T) / 2); pd = True
except np.linalg.LinAlgError: pd = False
Bs = (B + B.T) / 2
cond = np.linalg.cond(Bs, 2); ev = np.linalg.eigvalsh(Bs)
out = [f'k={k} D_kk={Dh[k,k]:.10g} C_kk={Ch[k,k]:.10g}',
       f'quotient={q:.10g}',
       f'cond2={cond:.10g}  eig min={ev[0]:.6g} max={ev[-1]:.6g}',
       f'P1 symmetric={sym} (max asym {asym:.3g}) cholesky_ok={pd}  -> {"PASS" if sym and pd else "FAIL"}',
       f'P2 finite&positive={bool(np.isfinite(q) and q>0)}']
with open('results.txt', 'x') as f: f.write('\n'.join(out) + '\n')
print('\n'.join(out))
