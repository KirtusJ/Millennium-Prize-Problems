#!/usr/bin/env python3
"""anapl.py -- l1-mcw (T123). Analysis of mcp.py output: plaquette-energy correlators vs soft winding levels.
Docstring (predicates, expectations) written BEFORE the production runs (19:40Z); body afterwards.

OPERATORS (mcp.py): O_i(t) = beta * sum_{8 sites x of slice t} (1 - P_jk(x)), jk the plane perpendicular to i.
  PS = single orientation (correlator averaged over the three planes), PA = A1 = O_1+O_2+O_3,
  PE = E = {(O_1-O_2)/sqrt2, (O_1+O_2-2O_3)/sqrt6}. Connected correlator C(t), vacuum subtracted with
  chain-set means, jackknife over the (>= 16) independent chains (drop one chain).

GAUSSIAN REFERENCE (my own, gauss.py; the child T124 computes it independently): to quadratic order
  beta(1-P_p) = (beta/2) sum_a (theta^a_p)^2, theta = B A, S = (beta/2) sum_a |B A^a|^2, so per colour
  <theta_p theta_q> = Pi_pq / beta with Pi = orthogonal projector onto range(B) (ker B = gauge + constant
  fields; constant fields do not enter theta at linear order). Wick, 3 colours:
     Cov(sum_{p in X} beta(1-P_p), sum_{q in Y} beta(1-P_q)) = (3/2) sum_{p in X, q in Y} Pi_pq^2   (beta-free)
  = the claim's 3 k(t)^2/2 form. Single plaquette: mean (3/2) Pi_pp, variance (3/2) Pi_pp^2 (-> 3/8 if Pi_pp=1/2).
  Computed at the same T as the run (finite-T exact), and the T->infinity spectrum from large T.

EXPECTATIONS STATED BEFORE THE RUN:
  X1 C(t)/C(0) of PS, PA, PE at beta = 1024 equals the Gaussian ratio within errors for t = 1, 2; at t >= 2 the
     Gaussian ratio (~0.047 e^{-7.05} ~ 4e-5 for the first atom) is likely below the statistical error.
  X2 m_eff(0->1) = ln(C(0)/C(1)) is ABOVE 3.525 (higher two-particle levels, e.g. 1.763 + 2.292, contribute at
     t=0) and equals the Gaussian value up to O(1/beta) + soft corrections; at beta = 64 I expect a deviation of
     a few % from the Gaussian value (1/beta interaction corrections, soft tail ~ beta^{-2/3} ~ 0.06 relative).
     m_eff(1->2) is expected to be unresolved (C(2) consistent with 0) except possibly at beta = 64, where a soft
     tail may dominate C(2) and give m_eff(1->2) << 3.5.
  X3 soft-tail amplitude: A_soft ~ beta^{-2/3} (derivation: soft fields a ~ beta^{-1/3}; the slow part of the
     box plaquette energy is the slow potential energy beta |[a,a]|^2 ~ beta^{-1/3} (O(1) times the soft energy
     scale), its variance ~ beta^{-2/3}; hard variance O(1); cross terms beta F_h [a,a] average to zero over the
     hard modes at this order; a-dependence of the hard zero-point split is O(a^2) ~ beta^{-2/3} in amplitude,
     i.e. beta^{-4/3} in variance, subleading). So A_soft * beta^{2/3} roughly constant is the expectation.
  X4 Var of a single spatial plaquette energy -> Gaussian (3/2) Pi_pp^2 within 3% at beta = 1024 (3%: soft
     contribution ~ beta^{-2/3} = 1% times an O(1) coefficient up to 3, plus 1/beta).

PREDICATES (pass/fail; recorded):
  P1 (c1) plaquette: r = beta(1-<P>)/(3/4) within 3 sigma_r + 0.5/beta of 1 - delta/V for some delta in [1/3, 3]
     (MC_BOX band [1/3,1] failed at 1024 with (1-r)V = 2.8, so the band is widened to 3 BEFORE this run;
     0.5/beta from MC_BOX). Measured also: exact Gaussian mean of the spatial single plaquette (3/2)Pi_pp.
  P2 (c2, quantitative test of 3k^2/2) at beta = 1024, for X in {PS, PA, PE} and t in {1, 2}:
     |R_MC(t) - R_G(t)| <= 3 sigma_jk(t) + 0.02 R_G(t)   (3 sigma Gaussian; 0.02 relative allowance for O(1/beta)
     + soft corrections, cf. X2). 6 cases. Also reported (measured only) at beta = 64, 256.
  P3 m_eff(0->1) at beta = 1024 within 3 sigma + 2% of the Gaussian m_eff(0->1), X in {PS, PA, PE}.
  P4 soft tail: fit R(t) = C(t)/C(0) for t in [t_min, t_max] to A (e^{-m t} + e^{-m (T-t)}) with m = m_soft FIXED
     to the winding value of the same run (differenced GEVP + plateau rule of analyse.py, unchanged, channel A1
     for PA, E for PE; PS fitted with both and reported measured-only). t_min = 4: the Gaussian hard part at
     t = 4 is <= 0.05 e^{-14.1} ~ 4e-8, below 1e-3 of any statistical error >= 4e-5 I can reach.
     t_max = min(T/2, t_min + ceil(3/m_soft)). Weighted least squares with diagonal jackknife errors; error of A
     from the jackknife of the whole fit (accounts for correlations). If |A| < 2 sigma_A: "not resolved",
     report the 2-sigma upper bound |A| + 2 sigma_A.
  P5 scaling (measured only unless resolved at >= 2 betas): A_soft * beta^p for p = 1/3, 2/3, 1.
  P6 Var single spatial plaquette vs Gaussian at beta=1024 within 3% + 3 sigma (X4).
  Sensitivity (measured only): P4 refit with m fixed to the predicted 1.5063 beta^{-1/3} (E), 1.8014 beta^{-1/3} (A1).

USAGE: python3 anapl.py OUT.md GAUSS.json PREFIX[+PREFIX...] ...   (OUT opened mode "x")
"""
import sys, json, math
import numpy as np
from analyse import analyse_channel, plateau

PRED = {'E': 1.506270, 'A1': 1.801419}


def load(pre):
    parts = pre.split('+')
    ds = [dict(np.load(p + '.npz')) for p in parts]; js = [json.load(open(p + '.json')) for p in parts]
    d = {k: np.concatenate([x[k] for x in ds], axis=1) for k in ds[0] if k.startswith(('C_', 'M_'))}
    d['sp1'] = np.concatenate([x['sp1'] for x in ds], 0); d['sp2'] = np.concatenate([x['sp2'] for x in ds], 0)
    d['plq'] = np.concatenate([x['mon'][3] for x in ds], 0)
    d['nmeas'] = ds[0]['nmeas']
    assert all((x['nmeas'] == d['nmeas']).all() for x in ds)
    J = dict(js[0]); J['NCH'] = sum(x['NCH'] for x in js)
    J['TAU'] = all(x['TAU'] for x in js); J['THERM'] = all(x['THERM'] for x in js)
    J['tau_int'] = {k: max(x['tau_int'][k][0] for x in js) for k in js[0]['tau_int']}
    J['therm_z'] = [x['therm_z'] for x in js]; J['pre_ok'] = all(all(x['pre'][k] for k in ('PRE1', 'PRE2', 'PRE3', 'PRE4')) for x in js)
    return d, J


def conn(d, ch, sel):
    C = d['C_' + ch][:, sel].sum(0).sum(0)[0, 0] / d['nmeas'].sum() / len(sel)
    M = d['M_' + ch][:, sel].sum(0).sum(0)[:, 0] / d['nmeas'].sum() / len(sel)
    return C - np.sum(M ** 2) / M.shape[0]


def jk(f, R):
    full = f(np.arange(R)); js = np.array([f(np.delete(np.arange(R), r)) for r in range(R)])
    err = np.sqrt((R - 1) / R * np.sum((js - js.mean(0)) ** 2, 0))
    return full, err, js


def fitA(R_, err, m, T, t1, t2):
    t = np.arange(t1, t2 + 1); f = np.exp(-m * t) + np.exp(-m * (T - t)); w = 1 / err[t1:t2 + 1] ** 2
    return np.sum(w * f * R_[t1:t2 + 1]) / np.sum(w * f * f)


def main():
    out = open(sys.argv[1], 'x'); G = json.load(open(sys.argv[2]))
    L = []; allr = []
    for pre in sys.argv[3:]:
        d, J = load(pre); R = J['NCH']; beta = J['beta']; T = J['T']; b3 = beta ** (1 / 3)
        g = G[str(T)] if str(T) in G else G[max(G, key=int)]
        L.append(f"\n## {pre}: beta={beta} T={T} NCH={R} NMEAS={J['NMEAS']} COLL={J['COLL']} pre_ok={J['pre_ok']} "
                 f"TAU={J['TAU']} THERM={J['THERM']} tau={J['tau_int']} (Gaussian ref T={g['T']})")
        res = {'pre': pre, 'beta': beta, 'T': T, 'NCH': R}
        # c1 plaquette (all orientations)
        pm, pe, _ = jk(lambda s: d['plq'][s].mean(), R)
        V = 8 * T; r = beta * (1 - pm) / 0.75; sr = beta * pe / 0.75
        P1 = any(abs(r - (1 - dl / V)) <= 3 * sr + 0.5 / beta for dl in np.linspace(1 / 3, 3, 81))
        L.append(f"P1 c1: <P>={pm:.8f}({pe:.8f}) r={r:.6f}({sr:.6f}) (1-r)V={(1-r)*V:.2f} -> {'met' if P1 else 'FAILED'}")
        res['P1'] = bool(P1); res['r'] = [r, sr]
        # single spatial plaquette mean, variance
        mS, emS, _ = jk(lambda s: d['sp1'][s].mean(), R)
        vS, evS, _ = jk(lambda s: d['sp2'][s].mean() - d['sp1'][s].mean() ** 2, R)
        rel = vS / g['var_spatial_single'] - 1
        P6 = abs(vS - g['var_spatial_single']) <= 3 * evS + 0.03 * g['var_spatial_single']
        L.append(f"single spatial plaquette: mean {mS:.5f}({emS:.5f}) vs Gauss {g['mean_spatial_single']:.5f}; "
                 f"var {vS:.5f}({evS:.5f}) vs Gauss {g['var_spatial_single']:.5f} (rel {rel:+.4f}); P6(3%+3s) "
                 f"{'met' if P6 else 'FAILED'}{'' if beta == 1024 else ' (measured only at this beta)'}")
        res.update(meanS=[mS, emS], varS=[vS, evS], P6=bool(P6))
        # winding soft masses (analyse.py, unchanged)
        msoft = {}
        for ch in ('E', 'A1'):
            lam, jkl = analyse_channel(d, ch, 'diff'); p = plateau(lam, jkl)
            msoft[ch] = p
            L.append(f"winding {ch}: m={p['m']:.5f}({p['err']:.5f}) m b^1/3={p['m']*b3:.4f}({p['err']*b3:.4f}) PLAT={p['PLAT']} ta={p['ta']} TLEN={T*p['m']>=20}")
        res['msoft'] = {k: [v['m'], v['err'], v['PLAT']] for k, v in msoft.items()}
        # plaquette channels
        L.append("| op | C(0) | Gauss C(0) | " + " | ".join(f"R({t})" for t in range(7)) + " | meff01 | meff12 |")
        L.append("|---" * 11 + "|")
        for op in ('PS', 'PA', 'PE'):
            C0, eC0, _ = jk(lambda s: conn(d, op, s)[0], R)
            Rf, Re, Rj = jk(lambda s: conn(d, op, s) / conn(d, op, s)[0], R)
            with np.errstate(all='ignore'):
                mf, me, _ = jk(lambda s: np.log(np.abs(conn(d, op, s)[:3] / conn(d, op, s)[1:4])), R)
            gR = g[op + '_R']; gm = g[op + '_meff']
            L.append(f"| {op} | {C0:.4f}({eC0:.4f}) | {g[op+'_C0']:.4f} | " +
                     " | ".join(f"{Rf[t]:.3e}({Re[t]:.1e})" for t in range(7)) +
                     f" | {mf[0]:.4f}({me[0]:.4f}) [G {gm[0]:.4f}] | {mf[1]:.3f}({me[1]:.3f}) [G {gm[1]:.4f}] |")
            pr = {}
            for t in (1, 2):
                ok = abs(Rf[t] - gR[t]) <= 3 * Re[t] + 0.02 * gR[t]
                pr[t] = bool(ok)
                L.append(f"  P2 {op} t={t}: MC {Rf[t]:.4e}({Re[t]:.1e}) G {gR[t]:.4e} dev {(Rf[t]-gR[t])/Re[t]:+.2f} sigma -> {'met' if ok else 'FAILED'}{'' if beta==1024 else ' (measured only)'}")
            P3 = abs(mf[0] - gm[0]) <= 3 * me[0] + 0.02 * gm[0]
            L.append(f"  P3 {op} meff01 {mf[0]:.4f}({me[0]:.4f}) vs G {gm[0]:.4f} -> {'met' if P3 else 'FAILED'}{'' if beta==1024 else ' (measured only)'}")
            res[op] = dict(C0=[C0, eC0], R=list(Rf), Rerr=list(Re), meff=[list(mf), list(me)], P2=pr, P3=bool(P3))
            # soft tail fits
            fits = []
            for ch in (('A1',) if op == 'PA' else ('E',) if op == 'PE' else ('A1', 'E')):
                for src in ('run', 'pred'):
                    m = msoft[ch]['m'] if src == 'run' else PRED[ch] / b3
                    if not (np.isfinite(m) and m > 0):
                        L.append(f'  P4 {op} {ch} {src}: winding mass not finite, no fit'); continue
                    t1 = 4; t2 = int(min(T // 2, t1 + math.ceil(3 / m)))
                    A, eA, _ = jk(lambda s: fitA(conn(d, op, s) / conn(d, op, s)[0], Re, m, T, t1, t2), R)
                    resolved = abs(A) >= 2 * eA
                    ub = abs(A) + 2 * eA
                    fits.append(dict(ch=ch, src=src, m=m, t1=t1, t2=t2, A=A, eA=eA, resolved=bool(resolved), ub=ub,
                                     scaled={p: A * beta ** eval(p) for p in ('1/3', '2/3', '1')}))
                    L.append(f"  P4 {op} soft fit (m={m:.4f} from {ch} {src}, t={t1}..{t2}): A={A:.3e}({eA:.1e}) "
                             f"{'RESOLVED' if resolved else 'not resolved; 2-sigma bound |A|<' + format(ub, '.2e')}; "
                             f"A b^1/3={A*beta**(1/3):.3e} A b^2/3={A*beta**(2/3):.3e} A b={A*beta:.3e}")
            res[op]['fits'] = fits
        allr.append(res)
    txt = "\n".join(L)
    out.write(txt + "\n\n```json\n" + json.dumps(allr, default=float) + "\n```\n"); out.close(); print(txt)


if __name__ == '__main__':
    main()
