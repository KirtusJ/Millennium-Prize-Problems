"""mc_check.py -- independent momentum-space Monte Carlo of C(t), to cross-check the
full normalization chain (mode normalization, polarization sum, Wick factor 2, f*f)
against the position-space quadrature used in corr.py.

Momentum-space form (straight from the mode expansion + Wick, no position-space G used):
  C(t) = 1/(2 (2pi)^3) Int d^3k d^3q [P(k)/k][P(q)/q] exp(-|k+q|^2) exp(-(|k|+|q|) t),
  P(k) = k^2 - k3^2 = k^2 (1 - c_k^2),  |f~(p)|^2 = (2pi)^3 exp(-p^2).
Importance sampling: |k|,|q| ~ Gamma(shape 4, scale 1/t), directions uniform on S^2:
  C = (24 pi / t^4)^2 / (2 (2pi)^3) * E[(1-c_k^2)(1-c_q^2) exp(-|k+q|^2)].
N = 2e7 samples, numpy default_rng(seed=20261123) (fixed seed).

PREDICATE P_MC (fixed before first run): at t = 1 and t = 2,
  |C_MC - C_quad| < 4 sigma_MC  (sigma_MC = sample std / sqrt(N)), and sigma_MC/C < 1e-2.
Tolerance source: CLT; 4 sigma gives a false-fail probability ~6e-5 per point. The
quadrature error (~1e-20) is negligible. A normalization error (factor 2, pi, ...)
would be many hundreds of sigma.
Exit 0 iff P_MC passes at both t, else 1.
"""
import sys
import numpy as np
import mpmath as mp

mp.mp.dps = 20

def C_quad(t):
    t = mp.mpf(t)
    def inner(r):
        den = mp.pi**2 * (r*r + t*t)**3
        return mp.quad(lambda c: ((t*t + r*r*(2*c*c - 1)) / den)**2, [-1, 0, 1])
    return 4 * mp.pi**mp.mpf(2.5) * mp.quad(lambda r: r*r*mp.exp(-r*r/4)*inner(r), [0, t, 3, 8, 25, mp.inf])

def C_mc(t, N=20_000_000, chunk=1_000_000, seed=20261123):
    rng = np.random.default_rng(seed)
    s = 0.0; s2 = 0.0
    for _ in range(N // chunk):
        def vec():
            k = rng.gamma(4.0, 1.0 / t, chunk)
            c = rng.uniform(-1, 1, chunk); ph = rng.uniform(0, 2*np.pi, chunk)
            sn = np.sqrt(1 - c*c)
            return np.stack([k*sn*np.cos(ph), k*sn*np.sin(ph), k*c]), c
        kv, ck = vec(); qv, cq = vec()
        p2 = ((kv + qv)**2).sum(axis=0)
        w = (1 - ck**2) * (1 - cq**2) * np.exp(-p2)
        s += w.sum(); s2 += (w*w).sum()
    m = s / N; var = s2 / N - m*m
    pref = (24*np.pi / t**4)**2 / (2 * (2*np.pi)**3)
    return pref * m, pref * np.sqrt(var / N)

ok = True
for t in (1.0, 2.0):
    cm, sg = C_mc(t)
    cq = float(C_quad(t))
    dev = abs(cm - cq) / sg
    good = dev < 4 and sg / cq < 1e-2
    ok &= good
    print(f"t={t}: C_MC={cm:.8e} +- {sg:.2e}   C_quad={cq:.8e}   |dev|={dev:.2f} sigma  rel_sigma={sg/cq:.1e}  {'PASS' if good else 'FAIL'}")
print("P_MC:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
