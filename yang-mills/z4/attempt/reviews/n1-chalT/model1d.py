"""model1d.py -- 1-D circle model of the tunnelling mechanism of TUNNEL_THEOREM.md, sections 4-5.

Model: T(a,a') = e^{-eps(a)/2} G_beta(a-a') e^{-eps(a')/2} on the circle, G_beta = wrapped N(0,1/beta) density,
eps(a) = 2 asinh|sin a|, discretised on a midpoint grid of step h (Riemann weight h). Wells at a=0, pi.
Sector reduction to [0,pi/2] (functions even under a->-a, sign sigma under a->pi-a):
  T_sigma = A + sigma C, A from images {a', -a'}, C from images {pi-a', pi+a'}. Both symmetric.
Exact identity (symmetric T_+, T_-, eigvecs g_+, g_-):  lambda_+ - lambda_- = 2 <g_-, C g_+> / <g_-, g_+>.
Eigenvectors are computed for W = D T D^{-1}, D = diag e^{sqrt(beta) theta phi(a)}, phi(a) = int_0^a sqrt(2 eps),
so that u = D g is O(1)-balanced and the tiny tails of g near pi/2 are obtained with RELATIVE accuracy.
m = log(lambda_+/lambda_-) = log1p(Delta/lambda_-).

Predicates (fixed before the first run):
 M1 c* = int_0^pi sqrt(2 eps) = 4.6054132 within 1e-6 (tolerance: 7 printed digits of the claim).
 M2 validation (independent route): for beta in {4, 9, 16} the identity value Delta agrees with the direct difference of
    the two largest eigenvalues of the FULL-circle symmetric matrix (numpy eigh) to relative 1e-5.
    Tolerance: eigh absolute error ~1e-15*N, Delta >= ~1e-8 at beta=16 -> relative ~1e-6; 1e-5 leaves margin.
 M3 weight independence: theta = 1.0 and theta = 0.9 give log m agreeing to 1e-6 absolute for every beta in the main
    list (identity is exact; only round-off differs; theta=0.9 tails are ~e^{-0.1 sqrt(beta) c*/2} smaller in u,
    i.e. >= 1e-7 relative at beta=4096, double eig error 1e-16 absolute -> 1e-9 relative).
 M4 grid convergence: h = 1/(5 sqrt beta) vs h = 1/(8 sqrt beta) give log m agreeing to 1e-6 absolute (Riemann sum
    of a Gaussian of width sigma=5h has relative error ~ e^{-2 pi^2 25} -> negligible; 1e-6 is round-off margin).
 M5 (my expectation that c* is the right constant) for all beta in {64,256,1024,4096}: least-squares fit
    -log m = c sqrt(beta) + b log(beta) + c0 over these 4 points gives |c - c*| / c* < 0.01.
 M6 for all beta in main list: -log m / sqrt(beta) < c* + 1/... (measured) -- replaced by: local slopes
    s_k = (-log m_{k+1} + log m_k)/(sqrt(beta_{k+1}) - sqrt(beta_k)) are within 3% of c* at the last pair.
 M7 sign-trial identity (Sec.5): at beta = 16 on the full circle, lambda_e - <sg,T sg> (g normalised) equals
    4 <g 1_A, T g 1_{A^c}> to relative 1e-6 (and hence NOT 2<...>), A = {cos a > 0} two-arc version adapted to the
    circle: s = sign(cos a) (odd under a -> pi - a). Tolerance: double cancellation of 1 - 1e-8 -> 1e-7.
 M8 variational: lambda_e - lambda_o <= lambda_e - <sg,T sg> at beta=16 (exact inequality; tolerance 1e-12).
 measured only: -log m / sqrt(beta), b, c0, local slopes.
No randomness (no seed needed).
"""
import numpy as np, sys, json, math

def eps(a): return 2*np.arcsinh(np.abs(np.sin(a)))

def cstar(n=200000):
    # int_0^pi sqrt(2 eps) = 2 int_0^{pi/2}; substitute a = u^2 (integrand ~ 2 sqrt(a) near 0)
    U = math.sqrt(math.pi/2); u = (np.arange(n)+0.5)*U/n; a = u*u
    return 2*np.sum(2*u*np.sqrt(2*eps(a)))*U/n

def phi_grid(a, n=4000):
    # phi(a) = int_0^a sqrt(2 eps), via u-substitution, vectorised by cumulative fine grid
    U = np.sqrt(a)
    out = np.empty_like(a)
    for i, Ui in enumerate(U):
        u = (np.arange(n)+0.5)*Ui/n
        out[i] = np.sum(2*u*np.sqrt(2*eps(u*u)))*Ui/n
    return out

def logG(d, beta, nimg):
    # log of wrapped Gaussian density, sum over images n in [-nimg, nimg], via logsumexp
    terms = np.stack([-beta*(d+2*np.pi*n)**2/2 for n in range(-nimg, nimg+1)])
    mx = terms.max(axis=0)
    return mx + np.log(np.exp(terms-mx).sum(axis=0)) + 0.5*np.log(beta/(2*np.pi))

def lse2(x, y):
    m = np.maximum(x, y); return m + np.log(np.exp(x-m)+np.exp(y-m))

def split_identity(beta, kfac=5, theta=1.0, nimg=2):
    h0 = 1/(kfac*np.sqrt(beta)); M = int(np.ceil((np.pi/2)/h0)); h = (np.pi/2)/M
    a = (np.arange(M)+0.5)*h
    e = eps(a); ph = theta*phi_grid(a); sb = np.sqrt(beta)
    ai, aj = a[:, None], a[None, :]
    lA = lse2(logG(ai-aj, beta, nimg), logG(ai+aj, beta, nimg))
    lC = lse2(logG(ai-(np.pi-aj), beta, nimg), logG(ai-(np.pi+aj), beta, nimg))
    base = np.log(h) - e[:, None]/2 - e[None, :]/2
    sh = sb*(ph[:, None]-ph[None, :])
    WA = np.exp(base+lA+sh); WC = np.exp(base+lC+sh)
    res = {}
    for sg, W in (('+', WA+WC), ('-', WA-WC)):
        w, V = np.linalg.eig(W); k = np.argmax(w.real); u = V[:, k].real
        if u.sum() < 0: u = -u
        res[sg] = (w[k].real, u)
    lp, up = res['+']; lm, um = res['-']
    # Delta = 2 <g_-, C g_+>/<g_-, g_+>, g = e^{-sb ph} u
    Ct = np.exp(base+lC - sb*(ph[:, None]+ph[None, :]))
    num = 2*um @ Ct @ up
    den = np.sum(um*up*np.exp(-2*sb*ph))
    Delta = num/den
    return dict(M=M, lam_p=lp, lam_m=lm, Delta=Delta, logm=float(np.log(np.log1p(Delta/lm))),
                minu_p=float(up.min()/up.max()), minu_m=float(um.min()/um.max()))

def full_circle(beta, kfac=5, nimg=4):
    h0 = 1/(kfac*np.sqrt(beta)); N = 4*int(np.ceil((np.pi/2)/h0)); h = 2*np.pi/N
    a = (np.arange(N)+0.5)*h; e = eps(a)
    T = h*np.exp(-e[:, None]/2 - e[None, :]/2 + logG(a[:, None]-a[None, :], beta, nimg))
    return a, T

def full_check(beta):
    a, T = full_circle(beta)
    w, V = np.linalg.eigh(T)
    # identify sectors: flip a -> pi - a; reflection a->-a
    N = len(a)
    idx_flip = np.array([np.argmin(np.abs(((np.pi-x) % (2*np.pi)) - a)) for x in a])
    top = []
    for k in range(N-1, N-12, -1):
        v = V[:, k]; par = np.dot(v, v[idx_flip])
        top.append((w[k], par))
    le = next(l for l, p in top if p > 0.5); lo = next(l for l, p in top if p < -0.5)
    g = V[:, -1]; g = g/np.linalg.norm(g)
    s = np.sign(np.cos(a)); sg = s*g
    rq = sg @ T @ sg
    Amask = s > 0
    cross = g[Amask] @ T[np.ix_(Amask, ~Amask)] @ g[~Amask]
    return dict(le=le, lo=lo, direct=le-lo, signtrial=w[-1]-rq, four_cross=4*cross, two_cross=2*cross)

if __name__ == '__main__':
    tag = sys.argv[1]
    P = {}; out = {}
    c = cstar(); out['cstar'] = c
    P['M1'] = abs(c-4.6054132) < 1e-6
    print('c*', c, flush=True)
    for beta in (4, 9, 16):
        fc = full_check(beta); si = split_identity(beta, nimg=4)
        rel = abs(si['Delta']/fc['direct']-1)
        P[f'M2 b={beta}'] = rel < 1e-5
        out[f'val{beta}'] = dict(direct=fc['direct'], identity=si['Delta'], rel=rel)
        print('val', beta, fc['direct'], si['Delta'], rel, flush=True)
        if beta == 16:
            r7 = abs(fc['signtrial']/fc['four_cross']-1)
            P['M7'] = r7 < 1e-6
            P['M8'] = fc['direct'] <= fc['signtrial'] + 1e-12
            out['signtrial16'] = dict(fc, rel4=r7, ratio_to_2cross=fc['signtrial']/fc['two_cross'])
            print('signtrial', fc, flush=True)
    betas = [64, 256, 1024, 4096]; rows = []
    for beta in betas:
        r1 = split_identity(beta); r2 = split_identity(beta, theta=0.9); r3 = split_identity(beta, kfac=8)
        P[f'M3 b={beta}'] = abs(r1['logm']-r2['logm']) < 1e-6
        P[f'M4 b={beta}'] = abs(r1['logm']-r3['logm']) < 1e-6
        row = dict(beta=beta, M=r1['M'], lam_p=r1['lam_p'], lam_m=r1['lam_m'], logm=r1['logm'],
                   logm_theta09=r2['logm'], logm_k8=r3['logm'], ratio=-r1['logm']/np.sqrt(beta),
                   minu=(r1['minu_p'], r1['minu_m']))
        rows.append(row); print(row, flush=True)
    y = np.array([-r['logm'] for r in rows]); X = np.array([[np.sqrt(b), np.log(b), 1] for b in betas])
    coef = np.linalg.lstsq(X, y, rcond=None)[0]
    P['M5'] = abs(coef[0]-c)/c < 0.01
    slopes = [(y[k+1]-y[k])/(np.sqrt(betas[k+1])-np.sqrt(betas[k])) for k in range(3)]
    P['M6'] = abs(slopes[-1]-c)/c < 0.03
    out.update(rows=rows, fit=dict(c=coef[0], b=coef[1], c0=coef[2]), slopes=slopes, predicates=P,
               met=sum(P.values()), failed=[k for k, v in P.items() if not v])
    print('fit', coef, 'slopes', slopes)
    print('met', out['met'], 'failed', out['failed'])
    with open(f'results/model1d_{tag}.json', 'x') as fh: json.dump(out, fh, indent=1, default=float)
    sys.exit(0 if not out['failed'] else 1)
