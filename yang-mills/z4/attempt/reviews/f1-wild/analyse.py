"""analyse.py -- evaluates predicates P0..P4 fixed in the docstring of cyl.py (copied here verbatim in intent):
 P0 U(1) beta in {4,16}: m_eff(Pl, t=2) = -ln(I1/I0), m_eff(Q, t=2) = -ln(I2/I0), each within 3 jackknife sigma.
 P1 SU(2): exponent p of m_e ~ beta^-p over beta in {32,64,128,256} lies in [0.25, 0.42].
 P2 for every SU(2) beta available: m_e > -ln(I2/I0) by more than 3 sigma.
 P3 m_e*beta^(1/3) at beta=256 and 32 agree within 25%.
 P4 measured only: SU(2) center-odd effective masses.
m_e := min over observables E, Q of the plateau value (rule in cyl.py). Writes results to a new file (mode 'x').
"""
import json, sys, glob, math
import numpy as np

def bessel_ratio(n, x, N=20000):
    s = np.linspace(0, math.pi, N + 1)
    def I(k):
        f = np.exp(x * (np.cos(s) - 1)) * np.cos(k * s)
        return np.trapezoid(f, s)
    return I(n) / I(0)

def meff_curve(corr, mean, T):
    # corr: (R,T) per replica <o(t0)o(t0+t)>, mean: (R,)
    corr = np.array(corr); mean = np.array(mean); R = corr.shape[0]
    def curve(c, m):
        C = c - m**2
        out = []
        for t in range(1, T // 4 + 1):
            r = (C[t - 1] + C[t + 1]) / (2 * C[t])
            out.append(math.acosh(r) if r > 1 else float('nan'))
        return np.array(out)
    full = curve(corr.mean(0), mean.mean())
    jk = np.array([curve(np.delete(corr, k, 0).mean(0), np.delete(mean, k).mean()) for k in range(R)])
    err = np.sqrt((R - 1) * np.nanmean((jk - full) ** 2, axis=0))
    return full, err   # index k -> t = k+1

def plateau(full, err):
    best = None
    for k in range(1, len(full)):          # t >= 2
        if np.isfinite(full[k]) and err[k] / full[k] < 0.10:
            best = (k + 1, full[k], err[k])
        else:
            break
    return best

if __name__ == '__main__':
    outf = sys.argv[1]
    res = {}
    lines = []
    for fn in sorted(glob.glob('res/*_b*.json')):
        d = json.load(open(fn)); T = d['T']
        key = '%s_%g' % (d['group'], d['beta'])
        res[key] = {}
        for o in 'EQP':
            if d['group'] == 'u1' and o == 'E':
                continue
            f, e = meff_curve(d['corr_' + o], d['mean_' + o], T)
            res[key][o] = {'meff': f.tolist(), 'err': e.tolist(), 'plateau': plateau(f, e)}
            lines.append('%s %s meff(t=1..6)=%s +- %s plateau=%s' % (key, o, np.round(f[:6], 4).tolist(), np.round(e[:6], 4).tolist(), plateau(f, e)))
    verdict = {}
    # P0
    p0 = []
    for b in (4, 16):
        k = 'u1_%g' % b
        if k not in res: p0.append(None); continue
        for o, n in (('P', 1), ('Q', 2)):
            exact = -math.log(bessel_ratio(n, b))
            m, e = res[k][o]['meff'][1], res[k][o]['err'][1]
            ok = abs(m - exact) < 3 * e
            p0.append(ok); lines.append('P0 %s %s t=2: %.5f +- %.5f exact %.5f -> %s' % (k, o, m, e, exact, ok))
    verdict['P0'] = p0
    # m_e for SU(2)
    me = {}
    for k, v in res.items():
        if not k.startswith('su2'): continue
        b = float(k.split('_')[1])
        cands = [v[o]['plateau'] for o in 'EQ' if v[o]['plateau']]
        if cands:
            t, m, e = min(cands, key=lambda c: c[1]); me[b] = (m, e, t)
        pp = v['P']['plateau']
        lines.append('SU2 beta=%g m_e=%s  center-odd plateau=%s' % (b, me.get(b), pp))
    bs = sorted(b for b in me if b >= 32)
    if len(bs) >= 3:
        x = np.log(bs); y = np.log([me[b][0] for b in bs]); w = np.array([me[b][0] / me[b][1] for b in bs]) ** 2
        A = np.vstack([np.ones_like(x), x]).T
        coef = np.linalg.lstsq(A * np.sqrt(w)[:, None], y * np.sqrt(w), rcond=None)[0]
        p = -coef[1]; verdict['P1'] = (float(p), bool(0.25 <= p <= 0.42))
    p2 = []
    for b in sorted(me):
        u = -math.log(bessel_ratio(2, b)); m, e, _ = me[b]
        p2.append((b, m, e, u, bool(m - u > 3 * e)))
    verdict['P2'] = p2
    if 32 in me and 256 in me:
        a, c = me[32][0] * 32 ** (1 / 3), me[256][0] * 256 ** (1 / 3)
        verdict['P3'] = (a, c, bool(abs(a - c) / max(a, c) < 0.25))
    for b in sorted(me):
        lines.append('beta=%g m_e*beta^(1/3)=%.4f  m_e*beta=%.3f' % (b, me[b][0] * b ** (1 / 3), me[b][0] * b))
    txt = '\n'.join(lines) + '\nVERDICT ' + json.dumps(verdict)
    with open(outf, 'x') as f:
        f.write(txt + '\n')
    print(txt)
