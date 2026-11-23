"""prog1b_barta.py -- rerun of predicate P5 of prog1_fibre.py, whose run1 produced NaN for s=0.3,0.6,1.0 because of
exp overflow in MY program (own defect, kept in res_prog1_run1.txt). Same predicates, log-space evaluation:
 P5a sup_r B(r) >= ||F_a|| (Barta, Lemma tu:U-barta), i.e. -log sup B <= eps_eff + 1e-9 [rounding].
 P5  Remark tu:U-F-num claim: at b=4096, s>=0.1: -log sup B - eps in [-4.1e-4, -2e-4] (+-1e-5 for the 2-digit claim).
 P5c resolution: N=700 vs N=1000 change of -log supB <= 1e-7.
Also reported (measured): sup over r in [0,1] of B vs the master-bound interior/outer split at r=tau.
Result file opened with mode 'x'. Deterministic.
"""
import numpy as np, math, sys
sys.path.insert(0, '.')
out = open(sys.argv[1], 'x')
def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.write(s + '\n'); out.flush()
def ive_asym(nu, x, K=12):
    x = np.asarray(x, float); s = np.ones_like(x); term = np.ones_like(x)
    for k in range(1, K + 1):
        term = term * (-(4 * nu * nu - (2 * k - 1) ** 2)) / (k * 8 * x); s = s + term
    return s / np.sqrt(2 * np.pi * x)
def logive0(x):
    x = np.asarray(x, float); o = np.empty_like(x); sm = x < 60
    o[sm] = np.log(np.i0(x[sm])) - x[sm]; o[~sm] = np.log(ive_asym(0, x[~sm])); return o
def run(b, s, N):
    xg, w = np.polynomial.legendre.leggauss(N); v = (xg + 1) / 2; r = v * v; wr = 2 * v * w / 2
    lpre = math.log(b / (2 * float(ive_asym(1, np.array([b]))[0])))
    rr = np.sqrt(np.outer(r, r)); qq = np.sqrt(np.outer(1 - r, 1 - r))
    lk = lpre + logive0(b * rr) + logive0(b * qq) + b * (rr + qq - 1) - b * s * s * (r[:, None] + r[None, :])
    S = np.exp(lk + 0.5 * np.log(wr)[:, None] + 0.5 * np.log(wr)[None, :])
    epsf = -math.log(np.linalg.eigvalsh(S)[-1])
    al = 2 * s * math.sqrt(1 + s * s)
    lt = lk + np.log(wr)[None, :] - b * al * (r[None, :] - r[:, None]) / 2
    m = lt.max(1); lB = m + np.log(np.exp(lt - m[:, None]).sum(1))
    return epsf, lB, r
cnt = {'P5a': [0, 0], 'P5': [0, 0], 'P5c': [0, 0]}
b = 4096
for s in (0.1, 0.3, 0.6, 1.0):
    e1, lB1, r1 = run(b, s, 700); e2, lB2, r2 = run(b, s, 1000)
    eps = 2 * math.asinh(s); nls = -lB2.max(); m = nls - eps
    a = nls <= e2 + 1e-9; c = abs(nls - (-lB1.max())) <= 1e-7; p = -4.1e-4 - 1e-5 <= m <= -2e-4 + 1e-5
    cnt['P5a'][0 if a else 1] += 1; cnt['P5c'][0 if c else 1] += 1; cnt['P5'][0 if p else 1] += 1
    tau = b ** (-1 / 3)
    P(f's={s} eps={eps:.8f} eps_eff={e2:.8f} -log supB={nls:.8f} diff={m:.3e} P5a={a} P5c={c} P5={p} '
      f'argmax r={r2[lB2.argmax()]:.5f}; -log sup_(r<=tau) B={-lB2[r2<=tau].max():.6f}, -log sup_(r>tau) B={-lB2[r2>tau].max():.6f}')
P('counts', cnt)
