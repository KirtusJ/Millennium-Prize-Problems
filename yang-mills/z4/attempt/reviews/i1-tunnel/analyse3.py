"""analyse3.py -- as analyse2.py but fits use ALL betas>=32 incl. 192, 256 (whose S predicate failed, see report). Predicates as analyse2.
Predicates (fixed before first run):
 C  controls: m_eo at beta=8,16,32,64 round to the printed 1.4768e-02, 3.2111e-04, 7.6936e-07, 8.9923e-11 (5 sig. digits).
 NC convergence: for each beta with two runs, |m(N2)-m(N1)|/m < 1e-3 (3 significant digits demanded by the brief), m_eo and m_oo.
 S  every run's own predicates (selftest D1-D3, residual R, RQ-error E) met.
 Fits are MEASURED ONLY: -log m = c sqrt(b) + p log b + k ; = c sqrt(b) + q b^{1/6} + k (least squares over the largest betas);
 fixed-c variants with c = 4.605413 and 4.792561; prediction with q = -8.9888 fixed.
"""
import json, glob, math, sys
import numpy as np
runs = {}
for f in sorted(glob.glob('results/dd_b*.json')):
    d = json.load(open(f)); runs.setdefault(d['beta'], []).append(d)
out = []; P = {}
pr = {8: 1.4768e-02, 16: 3.2111e-04, 32: 7.6936e-07, 64: 8.9923e-11}
for b, v in pr.items():
    m = max(runs[b], key=lambda d: d['N'])['m_eo']
    P[f'C@{b}'] = float(f'{m:.4e}') == v
    out.append(f'control beta={b}: m_eo={m:.6e} printed {v:.4e} -> {P[f"C@{b}"]}')
tab = []
for b in sorted(runs):
    rs = sorted(runs[b], key=lambda d: d['N']); d = rs[-1]
    ok = all(r['selftest']['D1'] and r['selftest']['D2ok'] and r['selftest']['D3ok'] and r['E_oe']['ok'] and r['E_oo']['ok']
             and all(s['R'] for s in r['sectors'].values()) for r in rs)
    P[f'S@{b}'] = ok
    if len(rs) > 1:
        ce = abs(rs[-1]['m_eo'] - rs[-2]['m_eo']) / rs[-1]['m_eo']; co = abs(rs[-1]['m_oo'] - rs[-2]['m_oo']) / rs[-1]['m_oo']
        P[f'NC@{b}'] = bool(ce < 1e-3 and co < 1e-3)
    else:
        ce = co = float('nan')
    tab.append((b, d['m_eo'], d['m_oo'], ce, co, d['N'], d['M'], max(d['E_oe']['err_est'], d['E_oo']['err_est'])))
out.append('\n| beta | N,M | m_eo | -log m_eo | -log m_eo/sqrt(b) | local slope d(-log m)/d sqrt(b) | m_oo/m_eo | rel dN (eo, oo) | RQ err est |')
out.append('|---|---|---|---|---|---|---|---|---|')
for i, (b, me, mo, ce, co, N, M, ee) in enumerate(tab):
    sl = '' if i == 0 else f'{(math.log(tab[i-1][1]) - math.log(me)) / (math.sqrt(b) - math.sqrt(tab[i-1][0])):.4f}'
    out.append(f'| {b:g} | {N},{M} | {me:.5e} | {-math.log(me):.4f} | {-math.log(me)/math.sqrt(b):.4f} | {sl} | {mo/me:.5f} | {ce:.1e}, {co:.1e} | {ee:.1e} |')
good = [t for t in tab if t[0] >= 32]
B = np.array([t[0] for t in good]); Y = -np.log(np.array([t[1] for t in good]))
out.append(f'\nfits use betas {B.tolist()} (runs meeting S and NC)')
def lsq(cols, y):
    A = np.array(cols).T; x, *_ = np.linalg.lstsq(A, y, rcond=None); return x, np.max(np.abs(A @ x - y))
for lo in (32, 64, 96):
    sel = B >= lo; b = B[sel]; y = Y[sel]
    if len(b) < 3: continue
    x, r = lsq([np.sqrt(b), np.log(b), np.ones_like(b)], y)
    out.append(f'beta>={lo}: c sqrt+p log+k: c={x[0]:.4f} p={x[1]:.3f} k={x[2]:.3f} maxres={r:.1e}')
    x, r = lsq([np.sqrt(b), b**(1/6), np.ones_like(b)], y)
    out.append(f'beta>={lo}: c sqrt+q b^1/6+k: c={x[0]:.4f} q={x[1]:.3f} k={x[2]:.3f} maxres={r:.1e}')
    for c in (4.605413, 4.792561):
        x, r = lsq([b**(1/6), np.log(b), np.ones_like(b)], y - c*np.sqrt(b))
        out.append(f'beta>={lo}: c={c} fixed: q={x[0]:.3f} p={x[1]:.3f} k={x[2]:.3f} maxres={r:.1e}')
    x, r = lsq([np.log(b), np.ones_like(b)], y - 4.605413*np.sqrt(b) + 8.9888*b**(1/6))
    out.append(f'beta>={lo}: prediction c=4.605413,q=-8.9888 fixed: p={x[0]:.3f} k={x[1]:.3f} maxres={r:.1e}')
    if len(b) >= 4:
        x, r = lsq([np.sqrt(b), b**(1/6), np.log(b), np.ones_like(b)], y)
        out.append(f'beta>={lo}: 4-param c sqrt+q b^1/6+p log+k: c={x[0]:.4f} q={x[1]:.3f} p={x[2]:.3f} k={x[3]:.3f} maxres={r:.1e}')
out.append('\npredicates: ' + json.dumps(P))
txt = '\n'.join(out)
with open(sys.argv[1], 'x') as fh: fh.write(txt + '\n')
print(txt)
sys.exit(0 if all(P.values()) else 1)
