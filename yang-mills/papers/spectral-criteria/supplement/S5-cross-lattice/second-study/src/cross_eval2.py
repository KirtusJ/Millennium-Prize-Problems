"""f2-cross2 cross-evaluation (worker T239). Usage: python3 -I src/cross_eval2.py TRAINC TRAINF EVALC EVALF OUTFILE
Retrains (deterministically, seed 239, same code as analysis2.py) the frozen tests on TRAIN chains (i%4 in {0,1}) of
TRAINC/TRAINF, prints the leading standardised coefficients of each optimum, and evaluates the frozen vectors on
(a) HELD chains of TRAINC/TRAINF and (b) ALL 16 chains of EVALC/EVALF (independent ensembles), delete-one-chain jackknife.
PREDICATE D (fixed before the runs, from the brief): a frozen test defeats alpha if HELD R_f/R_c + 2SE < alpha at 2l AND
  (same frozen vector) R_f/R_c + 2SE < alpha at 4l. Reported: for each test, max(2l bound, 4l bound) and the minimum over tests.
"""
import sys; sys.path.insert(0, "/home/user/z4-workers/f2-cross2/src")
import numpy as np, analysis2 as A

tc, tf, ec, ef, outf = sys.argv[1:6]
fo = open(outf, "x")
def out(s): print(s); fo.write(s + "\n"); fo.flush()
C = A.load(tc); F = A.load(tf); EC = A.load(ec); EF = A.load(ef)
Ct, Ch = A.split(C); Ft, Fh = A.split(F)
rng = np.random.default_rng(239)
PLANES = [(1, 2), (0, 2), (0, 1)]
PAIRS = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
PERMS = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
def rotmap(sig):
    """index map m with field i -> field m[i] under the axis relabelling mu -> sig[mu] (a lattice rotation)."""
    m = [0] * A.K
    for mu in range(3):
        m[mu] = sig[mu]; m[3 + mu] = 3 + sig[mu]; m[30 + mu] = 30 + sig[mu]; m[33 + mu] = 33 + sig[mu]; m[36 + mu] = 36 + sig[mu]
        for b in range(4): m[42 + 4 * mu + b] = 42 + 4 * sig[mu] + b
    for k, (mu, nu) in enumerate(PLANES):
        k2 = sig[k]; first = sig[mu] < sig[nu]
        m[6 + 2 * k] = 6 + 2 * k2 + (0 if first else 1); m[7 + 2 * k] = 6 + 2 * k2 + (1 if first else 0)
    for k, p in enumerate(PERMS): m[12 + k] = 12 + PERMS.index(tuple(sig[x] for x in p))
    for k, (mu, nu) in enumerate(PAIRS):
        j = PAIRS.index((sig[mu], sig[nu])); m[18 + k] = 18 + j; m[24 + k] = 24 + j
    pp = [(0, 1), (0, 2), (1, 2)]
    for k, (i, j) in enumerate(pp): m[39 + k] = 39 + pp.index(tuple(sorted((sig[i], sig[j]))))
    assert sorted(m) == list(range(A.K))
    return m
def rotate(a, sig):
    b = np.zeros_like(a); m = rotmap(sig)
    for i in range(A.K): b[m[i]] = a[i]
    return b
def ev(a, c, Fs, Cs):
    f_f = lambda ch: np.array(A.quant(a, ch, c))
    (vf, ef_, rf), (_, _, srf) = A.jk(f_f, Fs); (vc, ec_, rc), (_, _, src) = A.jk(f_f, Cs)
    rat = rf / rc; srat = rat * np.sqrt((srf / rf) ** 2 + (src / rc) ** 2)
    return rf, srf, rc, src, rat, srat, vf / vc
out(f"train {tc}/{tf} TRAIN; eval HELD of same, and ALL of {ec}/{ef}")
out(f"{'test':16s} | {'held R_f/R_c':>17s} {'bound':>8s} | {'eval R_f':>17s} {'eval R_c':>17s} {'eval R_f/R_c':>17s} {'Vf/Vc':>7s} {'bound':>8s} | max")
res = []
for c in A.CLASSES:
    Vf, Ef = A.mats(Ft, c); Vc, Ec = A.mats(Ct, c)
    B = A.reduced_basis(Vf, Vc)
    af, _ = A.gen_min(Ef, Vf, B); ac, _ = A.gen_min(Ec, Vc, B)
    ar, _ = A.ratio_min(Ef, Vf, Ec, Vc, B, [af, ac], rng)
    aW = np.zeros(A.K); aW[0:3] = 1; aP = np.zeros(A.K); aP[3:6] = 1
    for nm, a in (("fine-opt", af), ("coarse-opt", ac), ("ratio-opt", ar), ("Wsum", aW), ("Psum", aP)):
        if A.quant(a, Fh, c)[0] <= 0: continue
        if nm.endswith("opt"):
            sd = np.sqrt(np.maximum(np.diag(Vf + Vc) / 2, 0)); z = a * sd; z /= np.abs(z).max()
            top = np.argsort(-np.abs(z))[:8]
            out(f"  [{c}:{nm}] leading standardised coefficients: " + ", ".join(f"{A.NAMES[i]} {z[i]:+.2f}" for i in top))
        h = ev(a, c, Fh, Ch); e = ev(a, c, EF, EC)
        b2 = h[4] + 2 * h[5]; b4 = e[4] + 2 * e[5]
        res.append((f"{c}:{nm}", max(b2, b4)))
        if nm.endswith("opt") and c in ("L", "Z"):   # rotations only where momentum direction plays no role
            rr = []
            for sig in ((1, 2, 0), (2, 0, 1)):
                b = rotate(a, sig); hh = ev(b, c, Fh, Ch); ee = ev(b, c, EF, EC)
                rr.append(f"rot{sig}: held {hh[4]:.5f}({hh[5]:.5f}) eval {ee[4]:.5f}({ee[5]:.5f})")
            out(f"    measured only, rotated copies of {c}:{nm}: " + "; ".join(rr))
        out(f"{c+':'+nm:16s} | {h[4]:9.5f}({h[5]:.5f}) {b2:8.5f} | {e[0]:9.5f}({e[1]:.5f}) {e[2]:9.5f}({e[3]:.5f}) {e[4]:9.5f}({e[5]:.5f}) {e[6]:7.4f} {b4:8.5f} | {max(b2,b4):8.5f}")
best = min(res, key=lambda r: r[1])
out(f"\nPREDICATE D (both circumferences): min over {len(res)} frozen tests of max(bound_2l, bound_4l) = {best[1]:.5f} ({best[0]}) -> " +
    (f"alpha > {best[1]:.5f} defeated at both" if best[1] < 1 else "no alpha <= 1 defeated at both"))
fo.close()
