#!/usr/bin/env python3
"""analyse.py COARSE_FILE FINE_FILE OUT [--lsig_c 2.214 --lsig_f 2.286]
Reads measurement files written by ym.py run; writes OUT (mode "x").

Per ensemble (N = L): uses Ebar_n at the target flow time s (last block of L columns).
  Ebar      = <mean_n Ebar_n>
  C(tau)    = <mean_n Ebar_n Ebar_{n+tau}>  (all n, periodic)
  R(tau)    = (C(tau) - Ebar^2) / Ebar^2,  tau = 0, N/6, N/3 (and all tau for display)
  Q0        = s^2 * 4 * Ebar   [E_mag a^4 = (1/2) sum_{i<j} G^a_ij G^a_ij a^4 = 4 * sum_{i<j}(1-1/2TrU_ij), tree level, G = gF]
  Q0beta    = s^2 * beta * Ebar [magnetic ACTION density (1/g^2) E_mag a^4, the brief's beta-normalised form]
  m_eff*l   = 6 ln(R(N/6)/R(N/3)); also cosh form solving R1/R2 = cosh(m(N/6-N/2))/cosh(m(N/3-N/2)).
Errors: blocked jackknife. tau_int (Sokal window c=6) measured for mean Ebar and for the per-config
estimators O_tau = mean_n Ebar_n Ebar_{n+tau}, tau in {0,N/6,N/3}; block length = max(1, ceil(10*max tau_int)).
The first NSKIP=10 configurations after thermalisation are dropped (fixed before looking).

PREDICATES (fixed before first run)
 P1 per ensemble: R(0) > 0 significantly (> 2 sigma) and R(N/6), R(N/3) >= -2 sigma.
 P2 per ensemble: R(0) - R(N/6) > -2 sigma and R(N/6) - R(N/3) > -2 sigma (non-increasing within errors),
    and log-convexity  R(0)*R(N/3) - R(N/6)^2 > -2 sigma.
 P3 measured only: ratios fine/coarse of R(0), R(N/6), R(N/3), Q0, Q0beta; "consistent with 1" iff |r-1| < 2 sigma.
 P4 measured only: m_eff/sqrt(sigma) = (m_eff l)/(l sqrt(sigma)) vs 3.74(12) (Teper hep-th/9812187 Table 1).
 Plaquette: C2 of ym.py, FHK Table 8 interpolation.
"""
import sys, math, argparse
import numpy as np

NSKIP = 10

def load(fn):
    hdr = {}
    rows = []
    for line in open(fn):
        if line.startswith("# L="):
            for kv in line[2:].split():
                k, v = kv.split("="); hdr[k] = float(v)
        elif not line.startswith("#") and line.strip():
            rows.append([float(x) for x in line.split()])
    d = np.array(rows)
    L = int(hdr["L"])
    return hdr, d[NSKIP:, 1], d[NSKIP:, 2 + 2 * L: 2 + 3 * L], d[NSKIP:, 2 + L: 2 + 2 * L], d[NSKIP:, -1]

def tau_int(x, c=6.0):
    x = np.asarray(x) - np.mean(x); n = len(x)
    if x.var() == 0: return 0.5
    f = np.fft.rfft(x, 2 * n); acf = np.fft.irfft(f * np.conj(f))[:n] / x.var() / n
    t = 0.5
    for W in range(1, n // 2):
        t += acf[W]
        if W >= c * t: break
    return max(t, 0.5)

def jack(blocks_fn, data, bl):
    """data: per-config array (ncfg, ...). Returns mean (full), err over block jackknife."""
    n = len(data) // bl * bl; nb = n // bl
    full = blocks_fn(data[:n])
    js = np.array([blocks_fn(np.concatenate([data[:i * bl], data[(i + 1) * bl:n]])) for i in range(nb)])
    err = np.sqrt((nb - 1) / nb * ((js - js.mean(0)) ** 2).sum(0))
    return full, err, nb

def stats_for(E, L, s, beta):
    taus = [0, L // 6, L // 3]
    def est(D):
        Eb = D.mean()
        C = np.array([np.mean(D * np.roll(D, -t, axis=1)) for t in range(L)])
        R = (C - Eb ** 2) / Eb ** 2
        r1, r2 = R[taus[1]], R[taus[2]]
        meff = 6 * math.log(r1 / r2) if r1 > 0 and r2 > 0 else float("nan")
        # cosh form
        mc = float("nan")
        if r1 > 0 and r2 > 0 and r1 > r2:
            a, b = taus[1] - L / 2, taus[2] - L / 2
            lo, hi = 1e-6, 20.0
            g = lambda m: math.log(math.cosh(m * a) / math.cosh(m * b)) - math.log(r1 / r2)
            if g(lo) < 0 < g(hi):
                for _ in range(100):
                    mid = 0.5 * (lo + hi)
                    if g(mid) > 0: hi = mid
                    else: lo = mid
                mc = 0.5 * (lo + hi) * L
        conv = R[0] * R[taus[2]] - R[taus[1]] ** 2
        return np.concatenate([[Eb, s * s * 4 * Eb, s * s * beta * Eb, meff, mc, R[0] - R[taus[1]], R[taus[1]] - R[taus[2]], conv], R])
    obs = [E.mean(1)] + [np.mean(E * np.roll(E, -t, axis=1), axis=1) for t in taus]
    ti = [tau_int(o) for o in obs]
    bl = max(1, math.ceil(10 * max(ti)))
    m, e, nb = jack(est, E, bl)
    return m, e, nb, bl, ti, taus

def fhk_interp(beta):
    tb = [(1.88, .52637, 5e-5), (2.1768, .43158, 3e-5), (2.2986, .39746, 1e-5), (2.3726, .37661, 2e-5), (2.4265, .36352, 1e-5), (2.5115, .34564, 1e-5), (2.7395, .30869, 2e-5)]
    xs = np.array([t[0] for t in tb]); ys = np.array([t[1] for t in tb]); es = np.array([t[2] for t in tb])
    i = np.searchsorted(xs, beta) - 1
    lin = ys[i] + (ys[i + 1] - ys[i]) * (beta - xs[i]) / (xs[i + 1] - xs[i])
    j = i - 1 if i > 0 else i
    q = np.polyfit(xs[j:j + 3], ys[j:j + 3], 2); quad = np.polyval(q, beta)
    j2 = i if i + 2 < len(xs) else i - 1
    q2 = np.polyfit(xs[j2:j2 + 3], ys[j2:j2 + 3], 2); quad2 = np.polyval(q2, beta)
    sig_int = max(abs(lin - quad), abs(lin - quad2))
    return 1 - lin, math.hypot(max(es[i], es[i + 1]), sig_int)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("coarse"); ap.add_argument("fine"); ap.add_argument("out")
    ap.add_argument("--lsig_c", type=float, default=2.214); ap.add_argument("--lsig_f", type=float, default=2.286)
    a = ap.parse_args()
    f = open(a.out, "x")
    def log(s):
        print(s); f.write(s + "\n")
    names = ["Ebar", "Q0", "Q0beta", "meff_l", "meff_l_cosh", "R0-R1", "R1-R2", "R0R2-R1^2"]
    res = {}
    for tag, fn, lsig in [("coarse", a.coarse, a.lsig_c), ("fine", a.fine, a.lsig_f)]:
        hdr, plaq, E, Ehalf, sec = load(fn)
        L = int(hdr["L"]); s = hdr["s"]; beta = hdr["beta"]
        m, e, nb, bl, ti, taus = stats_for(E, L, s, beta)
        res[tag] = (m, e, L, taus)
        log(f"== {tag}: {fn}  L={L} beta={beta} s={s}  ncfg used={len(E)} (skip {NSKIP})  sec/cfg={np.median(sec):.2f}")
        log(f"   tau_int [Ebar, O(0), O({taus[1]}), O({taus[2]})] = " + ", ".join(f"{t:.2f}" for t in ti) + f"  block={bl} cfgs  independent blocks={nb}")
        pm = plaq.mean(); bpl = max(1, math.ceil(10 * tau_int(plaq))); _, pe, _ = jack(lambda D: D.mean(), plaq, bpl)
        pub, pube = fhk_interp(beta)
        tol = 3 * math.hypot(pube, pe)
        log(f"   C2 plaquette {pm:.6f}+-{pe:.6f} vs FHK-interp {pub:.6f}+-{pube:.6f}: diff {pm-pub:+.6f} tol(3 sigma comb) {tol:.6f} -> {'MET' if abs(pm-pub)<=tol else 'FAILED'}")
        for k, n in enumerate(names):
            log(f"   {n:12s} = {m[k]:.6e} +- {e[k]:.2e}")
        R, Re = m[len(names):], e[len(names):]
        log("   R(tau) all tau: " + "; ".join(f"{t}:{R[t]:.3e}+-{Re[t]:.1e}" for t in range(L)))
        # E at s/2 for local slope of s^2 E
        Eh = Ehalf.mean(); Ef = E.mean()
        slope = math.log((s * s * Ef) / ((s / 2) ** 2 * Eh)) / math.log(2)
        log(f"   d ln(s^2 Ebar)/d ln s between s/2 and s: {slope:+.3f}")
        # P1
        ok1 = R[0] > 2 * Re[0] and all(R[t] >= -2 * Re[t] for t in taus[1:])
        log(f"   P1 R(0)={R[0]:.3e}+-{Re[0]:.1e} ({R[0]/Re[0]:.1f} sig); R({taus[1]})={R[taus[1]]:.3e}+-{Re[taus[1]]:.1e} ({R[taus[1]]/Re[taus[1]]:.1f} sig); R({taus[2]})={R[taus[2]]:.3e}+-{Re[taus[2]]:.1e} ({R[taus[2]]/Re[taus[2]]:.1f} sig) -> {'MET' if ok1 else 'FAILED'}")
        c = [m[5] / e[5], m[6] / e[6], m[7] / e[7]]
        ok2 = all(x > -2 for x in c)
        log(f"   P2 (R0-R1)/sig={c[0]:.1f} (R1-R2)/sig={c[1]:.1f} (R0R2-R1^2)/sig={c[2]:.1f} -> {'MET' if ok2 else 'FAILED'}")
        log(f"   P4 m_eff/sqrt(sigma) = {m[3]/lsig:.3f}+-{e[3]/lsig:.3f} (log form), cosh form {m[4]/lsig:.3f}+-{e[4]/lsig:.3f}; l*sqrt(sigma)={lsig}; published 3.74(12)")
    (mc, ec, Lc, tc), (mf, ef, Lf, tf) = res["coarse"], res["fine"]
    nn = len(names)
    log("== P3 ratios fine/coarse (independent ensembles, errors in quadrature of relative errors)")
    pairs = [("R(0)", nn + 0, nn + 0), ("R(l/6)", nn + tc[1], nn + tf[1]), ("R(l/3)", nn + tc[2], nn + tf[2]), ("Q0", 1, 1), ("Q0beta", 2, 2), ("m_eff l", 3, 3)]
    for n, ic, jf in pairs:
        r = mf[jf] / mc[ic]; er = abs(r) * math.hypot(ef[jf] / mf[jf], ec[ic] / mc[ic])
        log(f"   {n:8s} ratio = {r:.4f} +- {er:.4f}  |r-1|/sig = {abs(r-1)/er:.1f}  consistent with 1 (2 sig): {'yes' if abs(r-1)<2*er else 'no'}")
    f.close()

if __name__ == "__main__":
    main()
