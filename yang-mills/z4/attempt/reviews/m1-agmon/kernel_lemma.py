"""kernel_lemma.py -- numerical check of Lemma K (TUNNEL_THEOREM.md) on SU(2).
k_beta(g) = e^{beta cos theta}/Z, theta = class angle of g, dg Haar = (2/pi) sin^2 theta dtheta x (uniform direction).
Exact quantities (1-D quadrature, direction average done analytically):
 R_lin(beta,p,H) = int k cosh(sqrt(beta) p.X) e^{sqrt(beta) H theta^2/2} dg, X = theta*n; direction average of cosh(q theta cos phi)
                   = sinh(q theta)/(q theta), q = sqrt(beta) p.
 R_rad(beta,p)   = int k e^{sqrt(beta) p theta} dg   (the brief's 'needed bound' with d(g) = theta).
Lemma K bound, for 0 < eta <= 1, beta' = beta(1 - 5 eta^2/48) - sqrt(beta) H > 0:
 B = [ (beta/beta')^{3/2} e^{p^2 beta/(2 beta')} + (beta/(2 pi))^{3/2} 2 pi^2 e^{-beta(1-cos eta) + sqrt(beta)(p pi + H pi^2/2)} ] / (1 - 1/beta).
Predicates (fixed before first run):
 K1 for all (beta,p,H) in grid beta in {16,64,256,1024,4096}, p in {0.25,0.5,1,1.88,3}, H in {0,1}, and all eta in grid
    {0.05k : k=1..20} with beta'>0: R_lin <= B (count qualifying cases first). Tolerance: none (bound is rigorous), quadrature
    error checked by K3.
 K2 (my expectation) the best bound min_eta B satisfies log(min_eta B)/(p^2/2) <= 1.5 for beta >= 1024, p <= 1.88, H in {0,1}.
 K3 quadrature: R_lin with 2000 vs 4000 Gauss-Legendre nodes per panel agree to 1e-10 relative (double rounding x condition).
    [Amended after run1, which was killed before writing any result: 4000/8000 nodes too slow (numpy leggauss O(n^3)). Own defect.]
 K4 (brief's radial form is FALSE at small p, my expectation): R_rad(beta, 0.25) > e^{0.25^2/2} for every beta in grid.
 K5 (exact Gaussian fact): log R_lin(beta,p,0)/(p^2/2) -> 1: |.-1| < 0.05 at beta=4096 for p<=1.88.
 measured only: log R_lin/(p^2/2) for all, and log R_rad/(p^2/2).
No randomness.
"""
import numpy as np, sys, json
from numpy.polynomial.legendre import leggauss as _lg
_cache = {}
def leggauss(n):
    # cached: numpy's leggauss is O(n^3); run1 was killed for this (own defect)
    if n not in _cache: _cache[n] = _lg(n)
    return _cache[n]

def quad(beta, f, n):
    x, w = leggauss(n); th = np.pi*(x+1)/2; w = w*np.pi/2
    # integrate only up to where e^{beta(cos-1)} relevant but keep full range: split [0, c] and [c, pi]
    c = min(np.pi, 12/np.sqrt(beta)+0.0)
    out = 0.0
    for lo, hi in ((0, c), (c, np.pi)):
        if hi <= lo: continue
        t = lo + (hi-lo)*(x+1)/2; ww = w*(hi-lo)/np.pi
        out += np.sum(ww*f(t))
    return out

def R(beta, p, H, n=2000, kind='lin'):
    q = np.sqrt(beta)*p
    base = lambda t: np.exp(beta*(np.cos(t)-1))*np.sin(t)**2
    if kind == 'lin':
        def ang(t):
            z = q*t
            with np.errstate(over='ignore', invalid='ignore'):
                r = np.where(z > 1e-8, np.sinh(np.minimum(z, 700))/np.where(z > 1e-8, z, 1), 1.0)
            return r
        num = quad(beta, lambda t: base(t)*ang(t)*np.exp(np.sqrt(beta)*H*t*t/2), n)
    else:
        num = quad(beta, lambda t: base(t)*np.exp(q*t), n)
    return num/quad(beta, base, n)

def bound(beta, p, H, eta):
    bp = beta*(1-5*eta**2/48) - np.sqrt(beta)*H
    if bp <= 0: return np.inf
    inner = (beta/bp)**1.5*np.exp(p*p*beta/(2*bp))
    outer = (beta/(2*np.pi))**1.5*2*np.pi**2*np.exp(-beta*(1-np.cos(eta)) + np.sqrt(beta)*(p*np.pi + H*np.pi**2/2))
    return (inner+outer)/(1-1/beta)

if __name__ == '__main__':
    tag = sys.argv[1]
    P = {}; rows = []; cases = 0; qual = 0
    for beta in (16, 64, 256, 1024, 4096):
        for p in (0.25, 0.5, 1.0, 1.88, 3.0):
            for H in (0.0, 1.0):
                r = R(beta, p, H); r2 = R(beta, p, H, n=4000)
                P[f'K3 b={beta} p={p} H={H}'] = abs(r/r2-1) < 1e-10
                Bs = [bound(beta, p, H, 0.05*k) for k in range(1, 21)]
                ok = [r <= b for b in Bs if np.isfinite(b)]
                cases += 1; qual += int(len(ok) > 0)
                P[f'K1 b={beta} p={p} H={H}'] = all(ok)
                Bmin = min(Bs)
                if beta >= 1024 and p <= 1.88: P[f'K2 b={beta} p={p} H={H}'] = np.log(Bmin)/(p*p/2) <= 1.5
                if beta == 4096 and H == 0 and p <= 1.88: P[f'K5 p={p}'] = abs(np.log(r)/(p*p/2)-1) < 0.05
                rows.append(dict(beta=beta, p=p, H=H, R_lin=r, ratio_lin=np.log(r)/(p*p/2), Bmin=Bmin, ratio_B=np.log(Bmin)/(p*p/2)))
                print(f'b={beta:5d} p={p:4.2f} H={H} logR/(p^2/2)={np.log(r)/(p*p/2):.4f} logBmin/(p^2/2)={np.log(Bmin)/(p*p/2):.4f} K1={all(ok)}', flush=True)
        rr = R(beta, 0.25, 0, kind='rad')
        P[f'K4 b={beta}'] = rr > np.exp(0.25**2/2)
        rows.append(dict(beta=beta, p=0.25, R_rad=rr, ratio_rad=np.log(rr)/(0.25**2/2)))
        print(f'b={beta} radial p=0.25: logR_rad/(p^2/2) = {np.log(rr)/(0.03125):.3f}')
    failed = [k for k, v in P.items() if not v]
    out = dict(rows=rows, predicates=P, met=sum(P.values()), failed=failed, K1_cases=cases, K1_qualifying=qual)
    with open(f'results/kernel_{tag}.json', 'x') as fh: json.dump(out, fh, indent=1, default=float)
    print('K1 cases', cases, 'qualifying (some eta with beta\'>0)', qual)
    print('met', sum(P.values()), 'failed', len(failed), failed)
    sys.exit(0 if not failed else 1)
