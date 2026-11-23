"""eps_eff.py -- exact fibre ground energy eps_eff(a) = -log ||F_a||, F_a = e^{-V_a/2} K_2 e^{-V_a/2} on L^2(SU(2)),
V_a(U2) = 2 beta s^2 (x1^2+x2^2), s = sin a.
Reduction (derived in TUNNEL_THEOREM.md, Lemma R): top eigenfunction depends only on t = x0^2+x3^2-x1^2-x2^2 = cos(2chi),
t uniform on [-1,1]; invariant degree-2j functions sqrt(2j+1) P_j(t); K_2 eigenvalue l_j = I_{2j+1}(beta)/I_1(beta);
V_a = beta s^2 (1-t). M = L^{1/2} G L^{1/2}, G_jk = <P~_j, e^{-V} P~_k>_{dt/2}; eps_eff = -log lambda_max(M).
Quadrature: Gauss-Legendre in chi in [0, pi/2] with weight sin(2 chi) (dt/2 = sin 2chi dchi), split at chi0 = min(pi/4, 12/(s sqrt beta)).
Predicates (fixed before first run):
 E1 (convergence) for every (beta,a): |eps(J,Q) - eps(J+60, 2Q)| < 1e-9. Tolerance: well above double rounding (1e-13) times matrix size; far below the effects measured (>=1e-4).
 E2 (my expectation, harmonic approx error O(1/beta)): for a in {0.3,0.6,1.0,pi/2,2.2,2.8}: |eps_eff - eps| <= 5/beta. The 5 is my own guess.
 E3 (what Lemma F needs): for a in the same set: eps_eff >= eps - 5/beta.
 E4 symmetry a <-> pi-a: |eps_eff(a) - eps_eff(pi-a)| < 1e-12 (exact: depends on s only; tolerance = rounding).
 E5 (control of the reduction, exact) beta=64, s=0 (a=0): eps_eff = 0 to 1e-12 (F = K_2, top eigenvalue 1 on constants).
 measured only: a = 0.1 and a = 0.05; beta*(eps_eff-eps) and sqrt(beta)*(eps_eff-eps).
No randomness (no seed needed).
"""
import numpy as np, sys, json
from numpy.polynomial.legendre import leggauss

def bessel_ratios(beta, nmax):
    """l_n = I_{n}(beta)/I_1(beta) for n=0..nmax via backward continued fraction r_m = I_{m+1}/I_m (Miller), start depth nmax+400+beta."""
    N = nmax + 400 + int(beta)
    r = 0.0; rs = np.zeros(N+1)
    for m in range(N, 0, -1):
        r = 1.0/(2.0*m/beta + r)  # r = I_m/I_{m-1}
        rs[m-1] = r            # rs[k] = I_{k+1}/I_k
    out = np.ones(nmax+1)
    out[0] = 1.0/rs[0]
    for n in range(2, nmax+1): out[n] = out[n-1]*rs[n-1]
    return out

def legendre_rows(J, t):
    P = np.zeros((J+1, t.size)); P[0] = 1
    if J >= 1: P[1] = t
    for k in range(1, J): P[k+1] = ((2*k+1)*t*P[k] - k*P[k-1])/(k+1)
    return P*np.sqrt(2*np.arange(J+1)+1)[:, None]

def eps_eff(beta, a, J, Q):
    s = np.sin(a)
    chi0 = min(np.pi/4, 12/(max(s,1e-3)*np.sqrt(beta)))
    xs, ws = [], []
    for lo, hi in ((0, chi0), (chi0, np.pi/2)):
        x, w = leggauss(Q); xs.append(lo+(hi-lo)*(x+1)/2); ws.append(w*(hi-lo)/2)
    chi = np.concatenate(xs); w = np.concatenate(ws) * np.sin(2*chi)
    t = np.cos(2*chi)
    j = np.arange(J+1)
    P = legendre_rows(J, t)
    wv = w*np.exp(-beta*s*s*(1-t))
    G = (P*wv) @ P.T
    l = bessel_ratios(beta, 2*J+1)[2*j+1]
    M = np.sqrt(l)[:, None]*G*np.sqrt(l)[None, :]
    ev = np.linalg.eigvalsh(M)
    return -np.log(ev[-1])

def epsf(a): return 2*np.arcsinh(np.sin(a))

if __name__ == '__main__':
    tag = sys.argv[1] if len(sys.argv) > 1 else 'run1'
    A = [0.3, 0.6, 1.0, np.pi/2, 2.2, 2.8]; Ameas = [0.05, 0.1]
    rows = []; P = {}
    fail = []
    for beta in (64, 256, 1024):
        J = int(8*np.sqrt(beta)) + 40; Q = 400
        assert True
        for a in A + Ameas:
            e1 = eps_eff(beta, a, J, Q); e2 = eps_eff(beta, a, J+60, 2*Q)
            d = e2 - epsf(a)
            rows.append(dict(beta=beta, a=a, eps_eff=e2, eps=epsf(a), diff=d, beta_diff=beta*d, sqrtb_diff=np.sqrt(beta)*d, conv=abs(e1-e2)))
            P[f'E1 b={beta} a={a:.4f}'] = abs(e1-e2) < 1e-9
            if a in A:
                P[f'E2 b={beta} a={a:.4f}'] = abs(d) <= 5/beta
                P[f'E3 b={beta} a={a:.4f}'] = d >= -5/beta
            print(f'beta={beta:5d} a={a:.4f} eps_eff={e2:.10f} eps={epsf(a):.10f} diff={d:+.3e} beta*diff={beta*d:+.4f} conv={abs(e1-e2):.1e}', flush=True)
        P[f'E4 b={beta}'] = abs(eps_eff(beta, 1.0, J, Q) - eps_eff(beta, np.pi-1.0, J, Q)) < 1e-12
    P['E5'] = abs(eps_eff(64, 0.0, 100, 400)) < 1e-12
    met = sum(P.values()); failed = [k for k, v in P.items() if not v]
    out = dict(rows=rows, predicates=P, met=met, failed=failed, measured_only=2*3*2)
    with open(f'results/eps_eff_{tag}.json', 'x') as fh: json.dump(out, fh, indent=1, default=float)
    print('met', met, 'failed', len(failed), failed)
    sys.exit(0 if not failed else 1)
