#!/usr/bin/env python3
"""ext_analyse.py -- Director Z4, 23 November 2026. Three-spacing reading of the matched measurement.
Predicates E1..E5 are those of PREDICATES.md (fixed before the runs); nothing is added here except the
table of R against tau/l. Uses load, tau_int, jack of the worker's analyse.py unchanged.
usage: ext_analyse.py <out file (never overwritten)> <coarse file> <mid file> <fine file> [more fine files]
E5: fine ensembles are combined (configurations concatenated, each file's first NSKIP dropped) only if their
means of Ebar agree pairwise within 2.5 sigma; otherwise they are reported separately and the first is used.
"""
import sys, math, numpy as np
import analyse as A

def est_factory(L):
    def est(D):
        Eb = D.mean()
        C = np.array([np.mean(D * np.roll(D, -t, axis=1)) for t in range(L)])
        return np.concatenate([[Eb], (C - Eb ** 2) / Eb ** 2])
    return est

def ens(E, L):
    obs = [E.mean(1)] + [np.mean(E * np.roll(E, -t, axis=1), axis=1) for t in (0, max(1, L // 6), L // 3)]
    ti = max(A.tau_int(o) for o in obs)
    bl = max(1, math.ceil(10 * ti))
    m, e, nb = A.jack(est_factory(L), E, bl)
    return m, e, nb, bl, ti

def main():
    out = open(sys.argv[1], "x")
    def log(s):
        print(s); out.write(s + "\n")
    files = sys.argv[2:]
    res = {}
    fine = []
    for fn in files:
        hdr, plaq, E, _, _ = A.load(fn)
        L = int(hdr["L"]); s = hdr["s"]; beta = hdr["beta"]
        m, e, nb, bl, ti = ens(E, L)
        log(f"== {fn}: L={L} beta={beta} s={s} ncfg used={len(E)} tau_int={ti:.2f} block={bl} blocks={nb}")
        log(f"   plaq={plaq.mean():.6f}  Ebar={m[0]:.6e}+-{e[0]:.1e}  Q0={s*s*4*m[0]:.5e}+-{s*s*4*e[0]:.1e}")
        log("   R(tau): " + "; ".join(f"{t}:{m[1+t]:.3e}+-{e[1+t]:.1e}" for t in range(L // 2 + 1)))
        if L == 12: fine.append((fn, E, m, e, s, beta))
        else: res[L] = (m, e, s, beta, nb)
    # E5
    ok = True
    for i in range(len(fine)):
        for j in range(i + 1, len(fine)):
            d = abs(fine[i][2][0] - fine[j][2][0]) / math.hypot(fine[i][3][0], fine[j][3][0])
            log(f"E5 Ebar {fine[i][0]} vs {fine[j][0]}: {d:.2f} sigma -> {'agree' if d <= 2.5 else 'DISAGREE'}")
            ok &= d <= 2.5
    if ok and len(fine) > 1:
        E = np.concatenate([f[1] for f in fine]); m, e, nb, bl, ti = ens(E, 12)
        log(f"== fine combined: ncfg={len(E)} tau_int={ti:.2f} block={bl} blocks={nb}")
        log("   R(tau): " + "; ".join(f"{t}:{m[1+t]:.3e}+-{e[1+t]:.1e}" for t in range(7)))
        res[12] = (m, e, fine[0][4], fine[0][5], nb)
    else:
        log("E5: fine ensembles NOT combined; first one used"); res[12] = (fine[0][2], fine[0][3], fine[0][4], fine[0][5], 0)
    # E1
    n_ok = n_all = 0
    for L, (m, e, s, beta, nb) in sorted(res.items()):
        for t in range(L // 2 + 1):
            n_all += 1; good = m[1 + t] >= -2 * e[1 + t]; n_ok += good
            if not good: log(f"E1 VIOLATION L={L} tau={t}: {m[1+t]:.3e}+-{e[1+t]:.1e}")
    log(f"E1 positivity within 2 sigma: {n_ok} of {n_all} -> {'MET' if n_ok == n_all else 'FAILED'}")
    # E2, E3
    x = {L: 1.0 / (8 * res[L][2]) for L in res}
    for name, val in (("Q0", lambda L: (res[L][2] ** 2 * 4 * res[L][0][0], res[L][2] ** 2 * 4 * res[L][1][0])),
                      ("R(0)", lambda L: (res[L][0][1], res[L][1][1]))):
        v = {L: val(L) for L in res}
        log(f"{name}: " + "; ".join(f"N={L} x={x[L]:.4f}: {v[L][0]:.5e}+-{v[L][1]:.1e}" for L in sorted(v)))
        if all(L in v for L in (6, 8, 12)):
            w = (x[8] - x[12]) / (x[6] - x[12])
            pred = v[12][0] + w * (v[6][0] - v[12][0]); perr = math.hypot((1 - w) * v[12][1], w * v[6][1])
            d = (v[8][0] - pred) / math.hypot(perr, v[8][1])
            x0 = v[12][0] - x[12] * (v[6][0] - v[12][0]) / (x[6] - x[12])
            log(f"   line through outer two predicts N=8: {pred:.5e}+-{perr:.1e}; measured minus predicted = {d:+.2f} sigma -> "
                f"{'consistent with a line in x' if abs(d) <= 2 else 'NOT a line in x'} (measured only); two-point intercept at x=0: {x0:.5e}")
    # E4 and the table against tau/l
    log("R against tau/l (measured only):")
    for frac, steps in ((1 / 12, {12: 1}), (1 / 8, {8: 1}), (1 / 6, {6: 1, 12: 2}), (1 / 4, {8: 2, 12: 3}), (1 / 3, {6: 2, 12: 4}),
                        (3 / 8, {8: 3}), (5 / 12, {12: 5}), (1 / 2, {6: 3, 8: 4, 12: 6})):
        log(f"   tau/l={frac:.4f}: " + "; ".join(f"N={L} ({t} steps): {res[L][0][1+t]:.3e}+-{res[L][1][1+t]:.1e}" for L, t in sorted(steps.items()) if L in res))
    def ratio(La, ta, Lb, tb):
        a, ea = res[La][0][1 + ta], res[La][1][1 + ta]; b, eb = res[Lb][0][1 + tb], res[Lb][1][1 + tb]
        r = a / b; er = abs(r) * math.hypot(ea / a, eb / b); return r, er
    for lab, args in (("E4 R(l/4) N=12/N=8", (12, 3, 8, 2)), ("E4 R(l/2) N=8/N=6", (8, 4, 6, 3)), ("E4 R(l/2) N=12/N=8", (12, 6, 8, 4)),
                      ("R(l/6) N=12/N=6", (12, 2, 6, 1)), ("R(l/3) N=12/N=6", (12, 4, 6, 2))):
        if args[0] in res and args[2] in res:
            r, er = ratio(*args); log(f"   {lab}: {r:.3f}+-{er:.3f}  ({abs(r-1)/er:.1f} sigma from 1)")
    out.close()

if __name__ == "__main__":
    main()
