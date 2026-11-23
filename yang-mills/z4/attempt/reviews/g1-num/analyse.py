"""analyse.py -- tables from results/spec_*.json (lattice) and results/cont_*.json (continuum).
Usage: python3 analyse.py OUTFILE_MD
PREDICATES (fixed before first run):
 A1 (convergence, item 1(iv)) for each beta, with runs r1=(N0,X0), r2=(N0+16,X0), r3=(N0+16,X0+40):
    every reported level E=-ln(lam/lam0) with E > 1e-6 satisfies |E(r2)-E(r1)| <= 1e-4 E and |E(r3)-E(r2)| <= 1e-4 E
    (4 digits, as demanded by the brief). Levels with E <= 1e-6 (center-odd tunnelling splittings) are judged
    on absolute precision: the floor is ~1e-15/E relative (double precision in lam/lam0); reported with that floor.
 A2 (variational monotonicity at fixed grid): lam0(r2) >= lam0(r1) * (1 - 1e-13)   (Cauchy interlacing; rounding).
 A3 (Lanczos) every reported eigenvalue has residual <= 1e-11 lam0 (else flagged in the table).
 A4 (continuum convergence) lowest 4 levels per sector of h agree between the two largest bases to 1e-4 relative;
    Rayleigh-Ritz monotone (larger basis lower or equal, tolerance 1e-10).
 Exponent: MEASURED ONLY. local exponent p(b1,b2) = -ln(m(b2)/m(b1))/ln(b2/b1).
 Hypothesis "exponent 1/3" is not given a pass/fail predicate (brief item 5: measured only).
"""
import json, glob, sys, re, math
import numpy as np

out = open(sys.argv[1], 'x')
P = lambda *a: print(*a, file=out)
fails = []
runs = {}
for f in glob.glob('results/spec_*.json'):
    r = json.load(open(f))
    runs.setdefault(r['beta'], []).append(r)
betas = sorted(runs)


def levels(r):
    l0 = max(max(s['lam']) for s in r['sectors'])
    L = []
    for s in r['sectors']:
        lab = ('ee' if s['center'] == [0, 0] else 'eo/oe' if s['center'] == [1, 0] else 'oo')
        for i, (l, res) in enumerate(zip(s['lam'], s['res'])):
            L.append(dict(lab=lab, Lpar='+' if s['Lpar'] == 0 else '-', ex={1: '+', -1: '-', 0: '.'}[s['exch']],
                          E=-math.log(l / l0), res=res / l0, i=i))
    return l0, sorted(L, key=lambda d: d['E'])


summary = {}
P('## Lattice spectrum (SU(2), 2 spatial directions, one site)\n')
for b in betas:
    rs = sorted(runs[b], key=lambda r: (r['N'], r['Nx']))
    if len(rs) < 3:
        P('beta=%g: only %d runs, convergence not judged' % (b, len(rs)))
    r1, r2, r3 = (rs + [rs[-1]] * 3)[:3]
    l01, L1 = levels(r1); l02, L2 = levels(r2); l03, L3 = levels(r3)
    if not l02 >= l01 * (1 - 1e-13):
        fails.append('A2 beta=%g' % b)
    key = lambda d: (d['lab'], d['Lpar'], d['ex'], d['i'])
    D2 = {key(d): d for d in L2}; D1 = {key(d): d for d in L1}
    P('### beta = %g   (runs N/Nx: %s)   ln lambda0 = %.12f\n' % (b, ', '.join('%d/%d' % (r['N'], r['Nx']) for r in rs), math.log(l03)))
    P('| # | center | L-par | exch | E=-ln(lam/lam0) (largest run) | dE(N) | dE(grid) | resid/lam0 |')
    P('|---|---|---|---|---|---|---|---|')
    # lowest levels: show 10 lowest of largest run
    met = 0; failed = 0; meas = 0
    for n, d in enumerate(L3[:10]):
        k = key(d)
        dn = abs(D2[k]['E'] - D1[k]['E']) if k in D1 else float('nan')
        dg = abs(d['E'] - D2[k]['E']) if k in D2 else float('nan')
        if d['E'] > 1e-6:
            ok = dn <= 1e-4 * d['E'] and dg <= 1e-4 * d['E']
            met += ok; failed += (not ok)
            if not ok: fails.append('A1 beta=%g level %s' % (b, k))
        else:
            meas += 1
        if d['res'] > 1e-11: fails.append('A3 beta=%g %s' % (b, k))
        P('| %d | %s | %s | %s | %.10g | %.1e | %.1e | %.0e |' % (n, d['lab'], d['Lpar'], d['ex'], d['E'], dn, dg, d['res']))
    me = min(d['E'] for d in L3 if d['lab'] == 'ee' and d['E'] > 1e-12)
    me2 = sorted(d['E'] for d in L3 if d['lab'] == 'ee' and d['E'] > 1e-12)[1]
    meo = min(d['E'] for d in L3 if d['lab'] == 'eo/oe')
    moo = min(d['E'] for d in L3 if d['lab'] == 'oo')
    meN = min(d['E'] for d in L1 if d['lab'] == 'ee' and d['E'] > 1e-12)
    # first excitation above the center-odd copies of the ground state, in the odd sectors
    eo1 = sorted(d['E'] for d in L3 if d['lab'] == 'eo/oe')[1]
    summary[b] = dict(me=me, me2=me2, meo=meo, moo=moo, eo1=eo1, dme=abs(me - meN))
    P('\nconvergence count (levels shown): met %d, failed %d, measured only %d\n' % (met, failed, meas))

P('## Gaps and exponents\n')
P('| beta | m_e | m_e beta^(1/3) | m_e beta | local exp p_e | 2nd ee gap | m_eo (eo/oe) | m_oo | -ln m_eo / sqrt(beta) | 1st excited eo/oe |')
P('|---|---|---|---|---|---|---|---|---|---|')
prev = None
for b in betas:
    s = summary[b]
    p = '' if prev is None else '%.4f' % (-math.log(s['me'] / summary[prev]['me']) / math.log(b / prev))
    fl = lambda x: ('%.4e' % x) if x > 1e-13 else 'below 1e-13 (double-precision floor)'
    P('| %g | %.8f | %.6f | %.5f | %s | %.8f | %s | %s | %s | %.6f |' % (
        b, s['me'], s['me'] * b ** (1 / 3), s['me'] * b, p, s['me2'], fl(s['meo']), fl(s['moo']),
        ('%.4f' % (-math.log(s['meo']) / math.sqrt(b))) if s['meo'] > 1e-13 else '-', s['eo1']))
    prev = b

# continuum
cf = sorted(glob.glob('results/cont_*.json'))
cont = [json.load(open(f)) for f in cf]
if cont:
    P('\n## Continuum h = -1/2 Lap + 2|Y1 x Y2|^2 (invariant states)\n')
    P('| K | Lmax | w | sector (Lpar,exch) | E_0..E_3 |')
    P('|---|---|---|---|---|')
    for c in cont:
        for s in c['sectors']:
            P('| %d | %d | %g | (%d,%+d) | %s |' % (c['K'], c['Lmax'], c['w'], s['Lpar'], s['exch'], ' '.join('%.7f' % x for x in s['E'][:4])))
    cs = sorted(cont, key=lambda c: (c['K'], c['Lmax']))
    a, bb = cs[-2], cs[-1]
    for sa, sb in zip(a['sectors'], bb['sectors']):
        for x, y in zip(sa['E'][:4], sb['E'][:4]):
            if not abs(x - y) <= 1e-4 * abs(y): fails.append('A4 conv')
            if not y <= x + 1e-10: fails.append('A4 RR monotone')
    allE = sorted(x for s in bb['sectors'] for x in s['E'])
    E0 = allE[0]
    gaps = sorted(set(round(x - E0, 7) for x in allE[1:]))[:4]
    P('\nE0 = %.7f ; invariant gaps E-E0 (largest basis): %s' % (E0, ', '.join('%.6f' % g for g in gaps)))
    E1 = gaps[0]
    P('\n| beta | m_e beta^(1/3) | ratio to E1=%.5f | 2nd ee gap * beta^(1/3) | ratio to E2=%.5f |' % (E1, gaps[1]))
    P('|---|---|---|---|---|')
    for b in betas:
        s = summary[b]
        P('| %g | %.6f | %.4f | %.6f | %.4f |' % (b, s['me'] * b ** (1 / 3), s['me'] * b ** (1 / 3) / E1, s['me2'] * b ** (1 / 3), s['me2'] * b ** (1 / 3) / gaps[1]))
    # measured only: fit m_e b^{1/3} = c0 + c1 b^{-1/3} + c2 b^{-2/3} on the largest betas
    bl = [b for b in betas if b >= 32]
    if len(bl) >= 3:
        X = np.array([[1, b ** (-1 / 3), b ** (-2 / 3)] for b in bl]); y = np.array([summary[b]['me'] * b ** (1 / 3) for b in bl])
        c, *_ = np.linalg.lstsq(X, y, rcond=None)
        P('\nmeasured only: fit m_e b^(1/3) = c0 + c1 b^(-1/3) + c2 b^(-2/3) on beta in %s: c0=%.4f c1=%.4f c2=%.4f (E1=%.5f)' % (bl, *c, E1))
        X2 = X[:, :2]; c2_, *_ = np.linalg.lstsq(X2[-3:], y[-3:], rcond=None)
        P('measured only: 2-term fit on the 3 largest betas: c0=%.4f c1=%.4f' % tuple(c2_))
P('\nFAILED predicates: %s' % (fails if fails else 'none'))
out.close()
print(open(sys.argv[1]).read())
sys.exit(1 if fails else 0)
