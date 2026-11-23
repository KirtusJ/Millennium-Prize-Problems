"""J1 test: one SU(2) plaquette degree of freedom, class-function character basis.

Model (adapted from README.md / hamiltonian-time): gauge-invariant states of one square of
4 links = class functions of U_p; orthonormal basis chi_n, n=0..NMAX-1.
  H0 = 4*n(n+2)/(2 kappa)  (each of 4 links carries label n; Laplace eigenvalue n(n+2))
  K_a = r_n^4, r_n = I_{n+1}(g)/I_1(g), g = kappa/a
  W = lam*(1 - chi_1/2) by multiplication: lam*(I - tridiag(1/2)); 0 <= W <= 2 lam (also truncated)
  T_a = M K_a M, M = exp(-a W/2);  e_j = -log(t_j)/a  (t_j descending eigenvalues of T_a,
  no further normalisation: r_0 = 1, W(identity)=0, as in README "physical log-transfer energy").
Adapted c (NOT forced by text, which states c = 6 lam L^3 + 6/kappa for an L>=2 cube):
  c = B + 6/kappa, B = (#plaquettes=1) * lam * range(1-phi_p)=2 -> c = 2 lam + 6/kappa.
  6/kappa = H0 of the fundamental plaquette character (4 links * 3/(2 kappa)), as in README.

Predicates (fixed before first run):
 P1 (hypotheses of README proof hold for this model): E1 <= c and 0 <= W <= B <= c (spectrum of
    truncated W). met/failed.
 P2 resolvent: ||(B_a+c)^-1 - (H+c)^-1|| <= 9a for every case with a*c <= 1. met/failed.
 P3 energies: |e_j - E_j| <= 90 a c^2, j=0,1, for every case with a*c <= 1/36. met/failed
    (given P1, a failure would be a defect of the target).
 P4 gap: |(e1-e0) - (E1-E0)| <= 180 a c^2 for cases with a*c <= 1/36. met/failed.
 P5 mu-level: |mu_j - E_j| <= 72 a c^2 (mu_j = (1-t_j)/a). met/failed.
 M1 measured only: ratio observed error / bound (how sharp), and observed error * 1/a (O(a) scaling).
 P6 truncation: E0,E1 at NMAX and NMAX+20 agree to 1e-20 relative (my own expectation).
Tolerances: all comparisons in 50-digit mpmath arithmetic; slack 1e-30 absolute (rounding of
mp.dps=50 eigen-solver, far below any bound tested).
Seeds: none (deterministic grid).
"""
import json, sys, os
import mpmath as mp

mp.mp.dps = 50
NMAX = 40
SLACK = mp.mpf('1e-30')


def mats(kappa, lam, a, nmax):
    n = range(nmax)
    H0 = [mp.mpf(4 * k * (k + 2)) / (2 * kappa) for k in n]
    W = mp.zeros(nmax, nmax)
    for i in n:
        W[i, i] = lam
        if i + 1 < nmax:
            W[i, i + 1] = W[i + 1, i] = -lam / 2
    H = W.copy()
    for i in n:
        H[i, i] += H0[i]
    out = {'H': H, 'W': W}
    if a is not None:
        g = mp.mpf(kappa) / a
        I1 = mp.besseli(1, g)
        r = [mp.besseli(k + 1, g) / I1 for k in n]
        ew, ev = mp.eigsy(W)
        M = ev * mp.diag([mp.exp(-a * x / 2) for x in ew]) * ev.T
        K = mp.diag([x ** 4 for x in r])
        out['T'] = M * K * M
    return out


def opnorm_sym(A):
    ew, _ = mp.eigsy(A)
    return max(abs(x) for x in ew)


def main(outpath):
    if os.path.exists(outpath):
        print('refuse to overwrite', outpath); sys.exit(3)
    cases = [(1, 1), (1, 5), (0.5, 2), (2, 0.25), (1, 20)]
    steps = [mp.mpf(1) / 2 ** k for k in range(4, 15)]
    res = {'cases': [], 'counts': {}}
    met = {k: 0 for k in 'P1 P2 P3 P4 P5 P6'.split()}
    fail = {k: 0 for k in met}
    qual = {k: 0 for k in met}
    for kappa, lam in cases:
        kappa, lam = mp.mpf(kappa), mp.mpf(lam)
        c = 2 * lam + 6 / kappa
        base = mats(kappa, lam, None, NMAX)
        E = sorted(mp.eigsy(base['H'])[0])
        Wsp = mp.eigsy(base['W'])[0]
        E2 = sorted(mp.eigsy(mats(kappa, lam, None, NMAX + 20)['H'])[0])
        ok6 = all(abs(E[j] - E2[j]) <= mp.mpf('1e-20') * (1 + abs(E[j])) for j in (0, 1))
        qual['P6'] += 1; (met if ok6 else fail)['P6'] += 1
        ok1 = E[1] <= c and min(Wsp) >= -SLACK and max(Wsp) <= 2 * lam + SLACK and 2 * lam <= c
        qual['P1'] += 1; (met if ok1 else fail)['P1'] += 1
        Hc_inv = (base['H'] + c * mp.eye(NMAX)) ** -1
        rows = []
        for a in steps:
            if a * c > 1:
                continue
            T = mats(kappa, lam, a, NMAX)['T']
            t = sorted(mp.eigsy(T)[0], reverse=True)
            Ba = (mp.eye(NMAX) - T) / a
            rdiff = opnorm_sym((Ba + c * mp.eye(NMAX)) ** -1 - Hc_inv)
            ok2 = rdiff <= 9 * a + SLACK
            qual['P2'] += 1; (met if ok2 else fail)['P2'] += 1
            e = [-mp.log(t[j]) / a for j in (0, 1)]
            mu = [(1 - t[j]) / a for j in (0, 1)]
            row = {'a': float(a), 'ac': float(a * c), 'resolvent_diff': float(rdiff),
                   'resolvent_over_9a': float(rdiff / (9 * a)), 'P2': ok2}
            if a * c <= mp.mpf(1) / 36:
                b90 = 90 * a * c ** 2
                err = [abs(e[j] - E[j]) for j in (0, 1)]
                gerr = abs((e[1] - e[0]) - (E[1] - E[0]))
                merr = [abs(mu[j] - E[j]) for j in (0, 1)]
                ok3 = all(x <= b90 + SLACK for x in err)
                ok4 = gerr <= 2 * b90 + SLACK
                ok5 = all(x <= 72 * a * c ** 2 + SLACK for x in merr)
                for k, ok in (('P3', ok3), ('P4', ok4), ('P5', ok5)):
                    qual[k] += 1; (met if ok else fail)[k] += 1
                row.update({'err_e0': float(err[0]), 'err_e1': float(err[1]), 'gap_err': float(gerr),
                            'bound90': float(b90), 'gap_err_over_180ac2': float(gerr / (2 * b90)),
                            'max_err_over_90ac2': float(max(err) / b90),
                            'gap_err_over_a': float(gerr / a), 'P3': ok3, 'P4': ok4, 'P5': ok5})
            rows.append(row)
        res['cases'].append({'kappa': float(kappa), 'lam': float(lam), 'c': float(c),
                             'E0': float(E[0]), 'E1': float(E[1]), 'gap': float(E[1] - E[0]),
                             'P1': ok1, 'P6': ok6, 'rows': rows})
        print(f'kappa={float(kappa)} lam={float(lam)} c={float(c)} E={float(E[0]):.6f},{float(E[1]):.6f}', flush=True)
    res['counts'] = {k: {'qualifying': qual[k], 'met': met[k], 'failed': fail[k]} for k in met}
    with open(outpath, 'x') as f:
        json.dump(res, f, indent=1)
    print(json.dumps(res['counts']))
    sys.exit(0 if all(v == 0 for v in fail.values()) else 1)


if __name__ == '__main__':
    main(sys.argv[1])
