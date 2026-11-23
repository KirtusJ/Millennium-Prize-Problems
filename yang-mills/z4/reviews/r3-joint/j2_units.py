"""J2: physical units on the tree-level trajectory kappa = beta*b, lambda = beta/b, ell = L*b.

c(beta,b,ell) = 6*beta*ell^3/b^4 + 6/(beta*b);  a*c^2 = a*(6 beta ell^3/b^4 + 6/(beta b))^2.
Exact condition: a c^2 -> 0  <=>  a beta^2 ell^6/b^8 -> 0 AND a/(beta^2 b^2) -> 0.
d = exp(-s B) 2^-N / s with s = 2 beta b, B = 6 beta ell^3/b^3... (B = 6 lam L^3 = 6 beta ell^3/b^4),
s*B = 12 beta^2 ell^3/b^3, N = 3 ell^3/b^3.

Predicates (fixed before first run):
 Q1 symbolic identity check: c computed from (kappa,lambda,L) equals the (beta,b,ell) formula, rel 1e-40
    at 20 sample points (mpmath dps 60; tolerance = rounding).  met/failed.
 Q2 B4's sentence "a beta^2/b^8 -> 0 suffices" with beta -> infinity, ell = 1 fixed:
    sequence b=2^-k, beta=k, a = b^9: expect a c^2 -> 0 and a c <= 1/36 eventually. met/failed.
 Q3 counterexample when beta is not bounded below (beta = b^4, a = b): a beta^2/b^8 = b -> 0
    but a c^2 -> infinity.  Predicate: a c^2 at k=10 exceeds 1e6 (my expectation). met/failed.
 M1 measured only: log10 d and log10 of required a_n (finite-volume schedule, t0=1, n=1) along
    b = 2^-k, beta = 2 + log2(1/b)/4 (slowly growing), ell = 1, compared with 180 a c^2 at a=b^9.
"""
import sys, os, json
import mpmath as mp
mp.mp.dps = 60


def c_phys(beta, b, ell):
    return 6 * beta * ell ** 3 / b ** 4 + 6 / (beta * b)


def c_lat(kappa, lam, L):
    return 6 * lam * L ** 3 + 6 / kappa


def log10_d(beta, b, ell):
    s = 2 * beta * b
    sB = 12 * beta ** 2 * ell ** 3 / b ** 3
    N = 3 * ell ** 3 / b ** 3
    return (-sB - N * mp.log(2) - mp.log(s)) / mp.log(10)


def main(out):
    if os.path.exists(out):
        print('refuse to overwrite'); sys.exit(3)
    res = {}; fails = []
    ok = True
    for k in range(1, 21):
        beta = mp.mpf(k) / 3 + 1; b = mp.mpf(1) / (k + 1); ell = mp.mpf(k % 4 + 1) / 2
        L = ell / b
        lhs = c_lat(beta * b, beta / b, L); rhs = c_phys(beta, b, ell)
        ok &= abs(lhs - rhs) <= mp.mpf('1e-40') * rhs
    res['Q1'] = ok
    q2 = []
    for k in range(2, 31, 4):
        b = mp.mpf(2) ** -k; beta = mp.mpf(k); a = b ** 9; c = c_phys(beta, b, 1)
        q2.append({'k': k, 'a_beta2_b8': float(a * beta ** 2 / b ** 8), 'ac2': float(a * c * c), 'ac': float(a * c)})
    res['Q2_rows'] = q2
    res['Q2'] = q2[-1]['ac2'] < q2[0]['ac2'] and q2[-1]['ac'] <= 1 / 36 and q2[-1]['ac2'] < 1e-3
    q3 = []
    for k in range(2, 11, 2):
        b = mp.mpf(2) ** -k; beta = b ** 4; a = b; c = c_phys(beta, b, 1)
        q3.append({'k': k, 'a_beta2_b8': float(a * beta ** 2 / b ** 8), 'ac2': float(a * c * c)})
    res['Q3_rows'] = q3
    res['Q3'] = q3[-1]['ac2'] > 1e6
    m1 = []
    for k in range(1, 7):
        b = mp.mpf(2) ** -k; beta = 2 + mp.mpf(k) / 4; ell = 1
        c = c_phys(beta, b, ell); ld = log10_d(beta, b, ell)
        # schedule a_n = t0 2^{-n-8} / ((1+t0 c)^2 (1 + 1/(t0 d))) with t0=1, n=1 ; d tiny => a ~ 2^-9 d/(1+c)^2
        la = mp.log10(mp.mpf(2) ** -9) - 2 * mp.log10(1 + c) + ld - mp.log10(1 + mp.mpf(10) ** ld)
        a9 = b ** 9
        m1.append({'k': k, 'L': float(1 / b), 'beta': float(beta), 'c': float(c), 'log10_d': float(ld),
                   'log10_a_schedule': float(la), 'abs_gap_err_bound_at_a=b^9': float(180 * a9 * c * c)})
    res['M1_rows'] = m1
    with open(out, 'x') as f:
        json.dump(res, f, indent=1)
    print(json.dumps({k: res[k] for k in ('Q1', 'Q2', 'Q3')}))
    for r in q2 + q3 + m1: print(r)
    sys.exit(0 if res['Q1'] and res['Q2'] and res['Q3'] else 1)


if __name__ == '__main__':
    main(sys.argv[1])
