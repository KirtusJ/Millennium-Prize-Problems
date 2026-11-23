#!/usr/bin/env python3
"""ctrl0.py -- POST-HOC control analysis (written after the pre-registered t0=1 analysis failed at beta=1, see notes step6).
For D=3 runs at beta in {1,2,4}: E channel, GEVP with t0=0 (operators normalised to unit C_aa(0)), lowest level,
m_eff(t)=ln(lambda(t)/lambda(t+1)), jackknife over chains. Also single operator 1 (f_i = s_i, i.e. the Q_1-Q_2 combos).
PREDICATES (fixed before running this file):
  CTRL0-PLAT: smallest t_a >= 1 with window [t_a, t_a+1] (L=2) such that chi2/dof <= 1.5 and |m(t_a)-m(t_a+1)| <= 2 sigma;
              t_a+1 must have relative error of lambda(t_a+2) < 0.2.
  CTRL0: |m_plateau - m_exact| <= 3 sigma (Gaussian, 0.3% two-sided); m_exact = 2.876117, 1.621505, 0.96893.
  Measured only: single-operator m_eff(t=1), and the A1 and T2 GEVP (t0=0) m_eff(1) next to the exact next level
  1.928516 (beta=2) and 1.184132 (beta=4) of THREE_DIR_EXACT.md (channel of those levels not stated there).
Usage: python3 ctrl0.py OUT.md run1 run2 ...   (OUT.md opened with mode "x")
"""
import sys, math, numpy as np
sys.path.insert(0, '.')
from analyse3 import load, connected, gevp_levels, jk_err
EX = {1.0: 2.876117, 2.0: 1.621505, 4.0: 0.96893}
NEXT = {2.0: 1.928516, 4.0: 1.184132}
f = open(sys.argv[1], 'x')
met = fail = 0
for pref in sys.argv[2:]:
    info, data, _ = load(pref)
    beta = info['beta']
    f.write(f"\n## D=3 beta={beta:g} T={info['T']}\n")
    for ch in ('E', 'T2', 'A1'):
        for single in (False, True):
            C, M = data[ch]; R = C.shape[0]; idx = np.arange(R)
            Cf = connected(C, M, idx)
            if single: Cf = Cf[:1, :1]
            norm = np.sqrt(np.abs(np.diagonal(Cf[..., 0])))
            lf = gevp_levels(Cf, 0, norm)
            lj = []
            for r in range(R):
                Cj = connected(C, M, np.delete(idx, r))
                if single: Cj = Cj[:1, :1]
                lj.append(gevp_levels(Cj, 0, norm))
            lj = np.array(lj)
            with np.errstate(all='ignore'):
                me = np.log(lf[:-1] / lf[1:]); mj = np.log(lj[:, :-1] / lj[:, 1:])
            se = jk_err(mj); le = jk_err(lj)
            tag = ch + (' single op1' if single else ' GEVP t0=0')
            f.write(f"- {tag}: m_eff(t=0..4) = " + ', '.join(f"{me[t]:.4f}({se[t]:.4f})" for t in range(5)) + '\n')
            if ch == 'E' and not single:
                pl = None
                for ta in range(1, len(me) - 2):
                    if not (lf[ta + 2] > 0 and le[ta + 2] / lf[ta + 2] < 0.2): break
                    w = np.array([ta, ta + 1]); wt = 1 / se[w] ** 2
                    mb = (wt * me[w]).sum() / wt.sum(); chi = (((me[w] - mb) / se[w]) ** 2).sum()
                    if chi <= 1.5 and abs(me[ta] - me[ta + 1]) <= 2 * jk_err(mj[:, ta] - mj[:, ta + 1]):
                        pl = (ta, mb, jk_err((mj[:, w] * wt).sum(1) / wt.sum())); break
                if pl is None:
                    f.write(f"  CTRL0-PLAT FAILED; CTRL0 not evaluable\n"); fail += 2
                else:
                    z = (pl[1] - EX[beta]) / pl[2]; ok = abs(z) <= 3
                    f.write(f"  CTRL0-PLAT met (t_a={pl[0]}); m_E = {pl[1]:.5f} +- {pl[2]:.5f} vs exact {EX[beta]} z={z:+.2f}: CTRL0 {'met' if ok else 'FAILED'}\n")
                    met += 1; met += ok; fail += (not ok)
    if beta in NEXT: f.write(f"- exact next level (channel unstated): {NEXT[beta]}\n")
f.write(f"\npredicates: met {met}, failed {fail}\n"); f.close()
print(f"met {met}, failed {fail}")
