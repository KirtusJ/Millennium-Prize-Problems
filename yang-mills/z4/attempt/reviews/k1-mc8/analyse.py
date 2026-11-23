#!/usr/bin/env python3
"""analyse.py -- k1-mc8 (T117) analysis of mcbox.py output. Written (docstring = predicates) BEFORE production.

PRIMARY ANALYSIS (fixed before the first production run): DIFFERENCED correlator matrix
  D_ab(t) = C_ab(t) - C_ab(t+1) (removes any t-independent floor, e.g. from frozen center sectors; the one-site
  work found such a floor in raw correlators). GEVP D(t) v = lambda(t) D(t0) v, t0 = 1 (D symmetrised;
  operators normalised to unit C_aa(0)); lowest-energy level = largest eigenvalue; m_eff(t) = ln(lam(t)/lam(t+1)).
  Also reported: single-operator differenced m_eff of operator 0 (measured only).
SECONDARY: the same GEVP on the raw vacuum-subtracted matrix C_ab(t) (vacuum subtraction with chain-set means).
ERRORS: jackknife over the NCH independent chains (each chain one block; jackknife sample = drop one chain).
PLATEAU RULE (PLAT): t_max = last t (consecutive from t0+1) with jackknife relative error of lam(t+1) < 0.25.
  Window length Lw = 3 (= max(3, round(0.5/m_pred)), m_pred = 1.5 beta^-1/3: 3 at beta = 64, 256, 1024).
  t_a = smallest t >= t0+1 with t_a+Lw-1 <= t_max such that chi2/dof of a constant over [t_a, t_a+Lw-1]
  (diagonal jackknife errors) <= 1.5 and |m_eff(t_a) - m_eff(t_a+Lw-1)| <= 2 sigma (jackknife of difference).
  m = mean of m_eff over the window (computed on each jackknife sample -> error). If no window: PLAT failed,
  m reported as m_eff(t0+1), measured only, and no number is claimed.
TLEN: T * m_lowest >= 20 (brief).  TAU, THERM, NCH: from the run JSON (mcbox.py docstring).
A channel/beta number is CLAIMED only if PLAT, TLEN, TAU, THERM, NCH are all met (brief: if the autocorrelation
  rule cannot be met, NO number).
CONTROL c1 (L=1, beta=64): |m_E beta^1/3 - 2.747| <= 3 sqrt(err^2 + 0.010^2) (one-site reference 2.747(10),
  pre-registered GEVP there; their differenced value 2.741(11); 3 sigma Gaussian 0.3 %).
CONTROL c2 (weak-coupling plaquette, equipartition, derivation in report.md): r = beta (1 - <P>) / (3/4);
  predicate |r - 1| <= 3 sigma_r + 1/(3V)... precisely: |r - (1 - delta/V)| <= 3 sigma_r + 0.5/beta for some
  delta in [1/3, 1] (zero-mode count band) where V = L^3 T; 0.5/beta bounds the O(1/beta) next-order term
  (SU(2) second coefficient is O(0.1)/beta^2 in 1-<P>, relative ~0.15/beta; 0.5 is a generous bound).
  Checked at beta = 256 and 1024.
COMPARISON (measured only, not a pass/fail of the claim): m beta^1/3 vs 1.506270 (E, T2), 1.801419 (A1),
  and 2 m beta^1/3 vs the one-site numbers.

USAGE: python3 analyse.py OUTFILE.md PREFIX1 [PREFIX2 ...]   (OUTFILE opened mode "x")
"""
import sys, json, math
import numpy as np

EPRED = {'E': 1.506270, 'T2': 1.506270, 'A1': 1.801419}


def gevp_lams(Cm, t0):
    """Cm (nop,nop,TM) -> lam (TM,) largest generalized eigenvalue, nan where ill-defined."""
    nop, _, TM = Cm.shape
    Cm = 0.5 * (Cm + np.transpose(Cm, (1, 0, 2)))
    B = Cm[:, :, t0]
    w, v = np.linalg.eigh(B)
    if np.any(w <= 0):
        return np.full(TM, np.nan)
    Bm = v @ np.diag(w ** -0.5) @ v.T
    lam = np.full(TM, np.nan)
    for t in range(TM):
        lam[t] = np.linalg.eigvalsh(Bm @ Cm[:, :, t] @ Bm).max()
    return lam


def corr_matrix(C, Mm, nm, sel, ncomp):
    """C (2,R,nop,nop,TM) summed over halves; returns per-chain-set average connected correlator for chains sel."""
    Cs = C[:, sel].sum(0).sum(0) / nm.sum() / len(sel)               # (nop,nop,TM)
    Ms = Mm[:, sel].sum(0).sum(0) / nm.sum() / len(sel)              # (ncomp,nop)
    vac = np.einsum('ca,cb->ab', Ms, Ms) / ncomp
    return Cs - vac[:, :, None]


def analyse_channel(d, ch, kind):
    C = d['C_' + ch]; Mm = d['M_' + ch]; nm = d['nmeas']
    R = C.shape[1]; ncomp = Mm.shape[2]
    def lam_of(sel):
        Cm = corr_matrix(C, Mm, nm, sel, ncomp)
        nrm = np.sqrt(np.diag(Cm[:, :, 0]))
        Cm = Cm / nrm[:, None, None] / nrm[None, :, None]
        if kind == 'diff':
            Cm = Cm[:, :, :-1] - Cm[:, :, 1:]
        elif kind == 'single':
            Cm = (Cm[:1, :1, :-1] - Cm[:1, :1, 1:])
            return Cm[0, 0]
        return gevp_lams(Cm, 1)
    full = lam_of(np.arange(R))
    jk = np.array([lam_of(np.delete(np.arange(R), r)) for r in range(R)])
    return full, jk


def meff(l):
    with np.errstate(all='ignore'):
        return np.log(l[..., :-1] / l[..., 1:])


def plateau(lam, jk, t0=1, Lw=3):
    R = jk.shape[0]
    jkf = lambda x: math.sqrt((R - 1) / R * np.sum((x - x.mean(0)) ** 2, 0)) if np.ndim(x) == 1 else \
        np.sqrt((R - 1) / R * np.sum((x - x.mean(0)) ** 2, 0))
    m = meff(lam); mj = meff(jk)
    with np.errstate(all='ignore'):
        rel = jkf(jk) / np.abs(lam)
    tmax = t0
    for t in range(t0 + 1, len(lam) - 1):
        if np.isfinite(rel[t + 1]) and rel[t + 1] < 0.25 and lam[t + 1] > 0:
            tmax = t
        else:
            break
    em = jkf(mj)
    out = {'meff': [float(x) for x in m[:min(len(m), tmax + 3)]],
           'meff_err': [float(x) for x in em[:min(len(m), tmax + 3)]], 'tmax': int(tmax)}
    for ta in range(t0 + 1, tmax - Lw + 2):
        w = slice(ta, ta + Lw)
        mm = m[w]; ee = em[w]
        if not np.all(np.isfinite(mm)) or not np.all(np.isfinite(mj[:, w])):
            continue
        mean = np.sum(mm / ee ** 2) / np.sum(1 / ee ** 2)
        chi2 = np.sum((mm - mean) ** 2 / ee ** 2) / (Lw - 1)
        dd = mj[:, ta] - mj[:, ta + Lw - 1]
        sd = jkf(dd)
        if chi2 <= 1.5 and abs(m[ta] - m[ta + Lw - 1]) <= 2 * sd:
            val = mm.mean(); vj = mj[:, w].mean(1)
            return dict(out, PLAT=True, ta=ta, m=float(val), err=float(jkf(vj)), chi2=float(chi2))
    return dict(out, PLAT=False, ta=None, m=float(m[t0 + 1]), err=float(em[t0 + 1]), chi2=None)


def main():
    outf = open(sys.argv[1], 'x')
    lines = []
    allres = []
    for pre in sys.argv[2:]:
        if '+' in pre:   # merge independent runs (same L, beta, T) along the chain axis; run flags must all hold
            parts = pre.split('+')
            ds = [dict(np.load(p + '.npz')) for p in parts]; jss = [json.load(open(p + '.json')) for p in parts]
            d = {k: np.concatenate([x[k] for x in ds], axis=1) for k in ds[0] if k.startswith(('C_', 'M_'))}
            d['nmeas'] = ds[0]['nmeas']
            assert all((x['nmeas'] == d['nmeas']).all() for x in ds)
            js = dict(jss[0]); js['NCH'] = sum(x['NCH'] for x in jss)
            for k in ('TAU', 'THERM'):
                js[k] = all(x[k] for x in jss)
            js['NCH_rule'] = js['NCH'] >= 16
            js['tau_int'] = {k: max(x['tau_int'][k][0] for x in jss) for k in jss[0]['tau_int']}
            js['therm_z'] = [x['therm_z'] for x in jss]
            pm = np.array([x['plaq_mean'] for x in jss]); pe = np.array([x['plaq_err'] for x in jss])
            w = 1 / pe ** 2; js['plaq_mean'] = float(np.sum(w * pm) / w.sum()); js['plaq_err'] = float(w.sum() ** -0.5)
            js['acc'] = [x['acc'] for x in jss]
        else:
            d = np.load(pre + '.npz'); js = json.load(open(pre + '.json'))
        beta = js['beta']; T = js['T']; L = js['L']; b3 = beta ** (1 / 3)
        lines.append(f"\n## {pre}: L={L} beta={beta} T={T} NCH={js['NCH']} NMEAS={js['NMEAS']} NOR={js['NOR']} COLL={js['COLL']}")
        lines.append(f"tau_int: {js['tau_int']}; TAU={js['TAU']} THERM={js['THERM']} (z {js['therm_z']}) NCH={js['NCH_rule']}; acc {js['acc']}")
        lines.append(f"plaquette <P> = {js['plaq_mean']:.8f} +- {js['plaq_err']:.8f}")
        V = L ** 3 * T
        r = beta * (1 - js['plaq_mean']) / 0.75; sr = beta * js['plaq_err'] / 0.75
        okc2 = any(abs(r - (1 - dl / V)) <= 3 * sr + 0.5 / beta for dl in np.linspace(1 / 3, 1, 21))
        lines.append(f"c2: r = beta(1-<P>)/(3/4) = {r:.6f} +- {sr:.6f}; 1-1/V = {1-1/V:.6f}, 1-1/(3V) = {1-1/(3*V):.6f}; "
                     f"(r-1)*beta = {(r-1)*beta:.3f}; C2 predicate {'met' if okc2 else 'FAILED'}")
        lines.append("| channel | analysis | m | err | m b^1/3 | 2 m b^1/3 | PLAT | ta | T m | claimed |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|")
        for ch in ('E', 'T2', 'A1'):
            for kind in ('diff', 'raw', 'single'):
                lam, jk = analyse_channel(d, ch, kind)
                p = plateau(lam, jk)
                tl = T * p['m'] >= 20
                claimed = bool(kind == 'diff' and p['PLAT'] and tl and js['TAU'] and js['THERM'] and js['NCH_rule'])
                allres.append(dict(pre=pre, beta=beta, L=L, ch=ch, kind=kind, **p, TLEN=bool(tl), claimed=claimed))
                lines.append(f"| {ch} | {kind} | {p['m']:.5f} | {p['err']:.5f} | {p['m']*b3:.4f} +- {p['err']*b3:.4f} | "
                             f"{2*p['m']*b3:.4f} | {'met' if p['PLAT'] else 'FAILED'} | {p['ta']} | {T*p['m']:.1f} | {claimed} |")
            lines.append(f"  {ch} diff meff: " + ", ".join(f"{a:.4f}({b:.4f})" for a, b in
                                                          zip(allres[-3]['meff'], allres[-3]['meff_err'])))
    txt = "\n".join(lines)
    outf.write(txt + "\n\n```json\n" + json.dumps(allres, indent=0) + "\n```\n"); outf.close()
    print(txt)


if __name__ == '__main__':
    main()
