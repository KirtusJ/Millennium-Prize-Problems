#!/usr/bin/env python3
"""analyse3.py -- GEVP / effective-mass / plateau analysis of mc3.py output, and the run-level predicates.
Predicates PLAT, TLEN, THERM, TAU, CTRL, LIM, MONO are those fixed in the mc3.py docstring (before the first run);
this file only implements them. Usage: python3 analyse3.py OUT.md OUT.json run1 run2 ...  (run = prefix of mc3 output)
Writes OUT.md and OUT.json with mode "x".
"""
import sys, json, math
import numpy as np

EXACT3 = {1.0: 2.876117, 2.0: 1.621505, 4.0: 0.96893}
EXACT2 = {256.0: 1.887}            # m_e beta^(1/3) in two directions
ECONT = {'E': 3.012539, 'T2': 3.012539, 'A1': 3.602838}


def jk_err(samples):
    n = samples.shape[0]
    return np.sqrt((n - 1) / n * np.sum((samples - samples.mean(0)) ** 2, 0))


def load(prefix):
    z = np.load(prefix + '.npz')
    info = json.load(open(prefix + '.json'))
    nm = z['nmeas'].astype(float)
    out = {}
    for ch in ('A1', 'E', 'T2'):
        C = z['C_' + ch].sum(0) / nm.sum()          # (R, nop, nop, TM)
        M = z['M_' + ch].sum(0) / nm.sum()          # (R, nc, nop)
        out[ch] = (C, M)
    therm = z['M_A1'][:, :, 0, 0] / nm[:, None]    # (2, R)
    return info, out, therm


def connected(C, M, idx):
    Cb = C[idx].mean(0); Mb = M[idx].mean(0)
    nc = Mb.shape[0]
    return Cb - (np.einsum('ca,cb->ab', Mb, Mb) / nc)[..., None]


def gevp_levels(Cc, t0, norm):
    """Cc (nop,nop,TM). returns largest eigenvalue lambda(t) for t=0..TM-1 (nan if fails)."""
    Cn = Cc / np.sqrt(np.outer(norm, norm))[..., None]
    Cn = 0.5 * (Cn + Cn.transpose(1, 0, 2))
    try:
        L = np.linalg.cholesky(Cn[..., t0])
    except np.linalg.LinAlgError:
        return np.full(Cc.shape[-1], np.nan)
    Li = np.linalg.inv(L)
    lam = np.empty(Cc.shape[-1])
    for t in range(Cc.shape[-1]):
        Mt = Li @ Cn[..., t] @ Li.T
        lam[t] = np.linalg.eigvalsh(0.5 * (Mt + Mt.T))[-1]
    return lam


def analyse_channel(C, M, beta, single=False):
    R = C.shape[0]
    xi0 = beta ** (1 / 3) / 3
    t0 = max(1, int(round(xi0 / 2)))
    L = max(3, int(round(xi0)))
    allidx = np.arange(R)
    Cfull = connected(C, M, allidx)
    if single:
        Cfull = Cfull[:1, :1]
    norm = np.sqrt(np.abs(np.diagonal(Cfull[..., 0])))
    lam_full = gevp_levels(Cfull, t0, norm)
    lam_jk = []
    for r in range(R):
        idx = np.delete(allidx, r)
        Cj = connected(C, M, idx)
        if single:
            Cj = Cj[:1, :1]
        lam_jk.append(gevp_levels(Cj, t0, norm))
    lam_jk = np.array(lam_jk)
    TM = C.shape[-1]
    lam_err = jk_err(lam_jk)
    # t_max: consecutive from t0+1, relative error of lambda(t+1) < 0.2
    tmax = t0
    for t in range(t0 + 1, TM - 1):
        if lam_full[t + 1] > 0 and np.isfinite(lam_err[t + 1]) and lam_err[t + 1] / lam_full[t + 1] < 0.2:
            tmax = t
        else:
            break
    with np.errstate(divide='ignore', invalid='ignore'):
        meff = np.log(lam_full[:-1] / lam_full[1:])
        meff_jk = np.log(lam_jk[:, :-1] / lam_jk[:, 1:])
    meff_err = jk_err(meff_jk)
    plat = None
    for ta in range(t0 + 1, tmax - L + 2):
        w = np.arange(ta, ta + L)
        mw, ew = meff[w], meff_err[w]
        if not (np.all(np.isfinite(mw)) and np.all(ew > 0)):
            continue
        wt = 1 / ew ** 2
        mbar = np.sum(wt * mw) / wt.sum()
        chi2 = np.sum(((mw - mbar) / ew) ** 2) / (L - 1)
        dif_jk = meff_jk[:, ta] - meff_jk[:, ta + L - 1]
        sd = jk_err(dif_jk)
        if chi2 <= 1.5 and abs(mw[0] - mw[-1]) <= 2 * sd:
            mjk = (meff_jk[:, w] * wt).sum(1) / wt.sum()
            plat = {'t_a': int(ta), 'L': L, 'chi2dof': float(chi2), 'm': float(mbar), 'err': float(jk_err(mjk)),
                    'm_jk': mjk}
            break
    res = {'t0': t0, 'tmax': int(tmax), 'L': L,
           'meff': [None if not np.isfinite(x) else round(float(x), 5) for x in meff[:min(TM - 1, tmax + 3)]],
           'meff_err': [None if not np.isfinite(x) else round(float(x), 5) for x in meff_err[:min(TM - 1, tmax + 3)]]}
    if plat is not None:
        res.update({'PLAT': True, 'm': plat['m'], 'err': plat['err'], 't_a': plat['t_a'], 'chi2dof': plat['chi2dof']})
        mjk = plat['m_jk']
    else:
        res.update({'PLAT': False, 'm': float(meff[t0 + 1]) if t0 + 1 < TM - 1 else float('nan'),
                    'err': float(meff_err[t0 + 1]) if t0 + 1 < TM - 1 else float('nan')})
        mjk = meff_jk[:, t0 + 1] if t0 + 1 < TM - 1 else None
    return res, mjk


def main():
    outmd, outjs = sys.argv[1], sys.argv[2]
    fm = open(outmd, 'x'); fj = open(outjs, 'x')
    runs = sys.argv[3:]
    allres = []
    lines = ['| D | beta | T | channel | m | err | m beta^1/3 | err | t0 | t_a | tmax | PLAT | single-op m (t0+1) | tau_int (sum_s, E1, T2_12) | TAU | THERM z |',
             '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for pref in runs:
        info, data, therm = load(pref)
        beta = info['beta']; D = info['D']; T = info['T']
        R = therm.shape[1]
        dth = therm[1] - therm[0]
        thz = float(dth.mean() / (dth.std(ddof=1) / math.sqrt(R)))
        rr = {'run': pref, 'D': D, 'beta': beta, 'T': T, 'tau_int': info['tau_int'], 'TAU': info['TAU'],
              'acc': info['acc'], 'THERM_z': thz, 'THERM': abs(thz) <= 3, 'ch': {}}
        mjks = {}
        for ch in ('E', 'T2', 'A1'):
            C, M = data[ch]
            res, mjk = analyse_channel(C, M, beta)
            single, _ = analyse_channel(C, M, beta, single=True)
            res['single_m'] = single['meff'][single['t0'] + 1] if len(single['meff']) > single['t0'] + 1 else None
            res['single_PLAT'] = single['PLAT']; res['single_plat_m'] = single['m'] if single['PLAT'] else None
            res['single_plat_err'] = single['err'] if single['PLAT'] else None
            b3 = beta ** (1 / 3)
            res['mb3'] = res['m'] * b3; res['mb3_err'] = res['err'] * b3
            rr['ch'][ch] = res
            mjks[ch] = mjk
            tau = info['tau_int']
            lines.append(f"| {D} | {beta:g} | {T} | {ch} | {res['m']:.5f} | {res['err']:.5f} | {res['mb3']:.4f} | {res['mb3_err']:.4f} | "
                         f"{res['t0']} | {res.get('t_a', '-')} | {res['tmax']} | {'met' if res['PLAT'] else 'FAILED'} | {res['single_m']} | "
                         f"{tau['sum_s'][0]:.1f}, {tau['E1'][0]:.1f}, {tau['T2_12'][0]:.1f} | {'met' if info['TAU'] else 'FAILED'} | {thz:+.2f} |")
        if mjks['E'] is not None and mjks['T2'] is not None:
            d = mjks['T2'] - mjks['E']
            rr['split_T2_minus_E'] = float(rr['ch']['T2']['m'] - rr['ch']['E']['m'])
            rr['split_err'] = float(jk_err(d))
        mlow = min(rr['ch'][c]['m'] for c in rr['ch'])
        rr['TLEN'] = bool(T * mlow >= 20); rr['T_m_lowest'] = T * mlow
        allres.append(rr)
    preds = []
    for rr in allres:
        if rr['D'] == 3 and rr['beta'] in EXACT3:
            e = rr['ch']['E']
            z = (e['m'] - EXACT3[rr['beta']]) / e['err']
            preds.append(('CTRL D=3 beta=%g' % rr['beta'], bool(abs(z) <= 3), f"m_E = {e['m']:.5f} +- {e['err']:.5f} vs {EXACT3[rr['beta']]}, z = {z:+.2f}"))
        if rr['D'] == 2 and rr['beta'] in EXACT2:
            c = min(rr['ch'], key=lambda k: rr['ch'][k]['m'])
            e = rr['ch'][c]
            z = (e['mb3'] - EXACT2[rr['beta']]) / e['mb3_err']
            preds.append(('CTRL D=2 beta=%g' % rr['beta'], bool(abs(z) <= 3), f"lowest channel {c}: m b^1/3 = {e['mb3']:.4f} +- {e['mb3_err']:.4f} vs 1.887, z = {z:+.2f}"))
    prod = sorted([rr for rr in allres if rr['D'] == 3 and rr['beta'] >= 64], key=lambda r: r['beta'])
    if prod:
        top = prod[-1]; low = prod[0]
        for ch in ('E', 'T2', 'A1'):
            e = top['ch'][ch]
            dev = e['mb3'] / ECONT[ch] - 1
            preds.append((f'LIM {ch} beta={top["beta"]:g}', bool(abs(dev) <= 0.08), f"m b^1/3 = {e['mb3']:.4f} +- {e['mb3_err']:.4f}, rel dev {dev:+.4f}"))
            if len(prod) > 1:
                d1 = abs(top['ch'][ch]['mb3'] - ECONT[ch]); d0 = abs(low['ch'][ch]['mb3'] - ECONT[ch])
                sig = math.hypot(top['ch'][ch]['mb3_err'], low['ch'][ch]['mb3_err'])
                ok = bool(d0 - d1 > 2 * sig)
                preds.append((f'MONO {ch}' + (' (measured only)' if ch == 'A1' else ''), ok,
                              f"|dev| {d0:.4f} (beta={low['beta']:g}) -> {d1:.4f} (beta={top['beta']:g}), 2 sigma = {2*sig:.4f}"))
    for rr in allres:
        for ch in rr['ch']:
            preds.append((f"PLAT D={rr['D']} beta={rr['beta']:g} {ch}", rr['ch'][ch]['PLAT'], f"t_a={rr['ch'][ch].get('t_a')}, tmax={rr['ch'][ch]['tmax']}"))
        preds.append((f"TLEN D={rr['D']} beta={rr['beta']:g}", rr['TLEN'], f"T m_lowest = {rr['T_m_lowest']:.1f}"))
        preds.append((f"THERM D={rr['D']} beta={rr['beta']:g}", rr['THERM'], f"z = {rr['THERM_z']:+.2f}"))
        preds.append((f"TAU D={rr['D']} beta={rr['beta']:g}", rr['TAU'], str(rr['tau_int'])))
    fm.write('# analysis\n\n' + '\n'.join(lines) + '\n\n## splittings T2 - E\n\n')
    for rr in allres:
        if 'split_err' in rr:
            fm.write(f"- D={rr['D']} beta={rr['beta']:g}: m_T2 - m_E = {rr['split_T2_minus_E']:+.5f} +- {rr['split_err']:.5f}; in units beta^-1/3: {rr['split_T2_minus_E']*rr['beta']**(1/3):+.4f} +- {rr['split_err']*rr['beta']**(1/3):.4f}\n")
    fm.write('\n## predicates\n\n| predicate | result | evidence |\n|---|---|---|\n')
    for n, ok, ev in preds:
        fm.write(f'| {n} | {"met" if ok else "FAILED"} | {ev} |\n')
    fm.write('\n## effective masses (GEVP lowest level), t = 0..\n\n')
    for rr in allres:
        for ch in rr['ch']:
            e = rr['ch'][ch]
            fm.write(f"- D={rr['D']} b={rr['beta']:g} {ch} (t0={e['t0']}): " + ', '.join(
                f"{m}({s})" for m, s in zip(e['meff'], e['meff_err'])) + '\n')
    fm.close()
    json.dump({'runs': allres, 'predicates': [(n, bool(o), ev) for n, o, ev in preds]}, fj, indent=1, default=float)
    fj.close()
    nmet = sum(1 for _, o, _ in preds if o)
    print(f'predicates met {nmet}, failed {len(preds) - nmet}')


if __name__ == '__main__':
    main()
