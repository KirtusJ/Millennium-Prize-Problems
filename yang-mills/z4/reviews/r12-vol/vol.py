"""r12-vol numerics. Own program (Z4 worker r12-vol).

Quantities (t = 0):
  C      exact lattice C_{b,s}(0) by FFT (D in position space, D^2, quadratic form via FFT).
  L      new lower bound (2/l^3)[A P_b - B' Psi'_b] of report.md, Theorem V1, kappa = 2.
  V      upper bound of THEOREMS_B B1: (2/l^3) Phi (pi^2/l^2) U2(64 s/l^2), Phi = b^3 sum f^2 (exact
         lattice value; the Schur step needs only this), U2 = 3 theta1 theta0^2 with the 1-D bounds of B1.
  R      C s^(5/2) / P_b, compared with sqrt(pi)/(640 pi^2) = 2.806e-4.

PREDICATES (fixed before the first run):
 P0  FFT value equals momentum double sum at N=6, l=1, s=0.02 (both f): rel. diff <= 1e-10.
     Tolerance: double rounding over <= 6^6 terms is ~1e-13; 1e-10 leaves margin.
 P1  for every case: L <= C (theorem; holds for any b if the internal conditions Q^2 >= A/B', eps<1,
     Q<=K, K-Q/2-Delta >= 1/sqrt(4s) hold; L = max over a fixed grid of (kappa,theta), each a valid bound; hypothesis H_V = (b <= sqrt(s)/2 and these conditions) tested and counted first).
 P2  for every case: C <= V (theorem B1).
 P3  for every bump case with H_V: L > 0 (non-vacuous). Expectation of mine, not a theorem.
 P4  for every case: R <= 1.05 * 2.806e-4 (my expectation: G(q) <= G(0) by Cauchy-Schwarz and
     (2/l^3)G(0) s^{5/2} -> 2.806e-4; 5% allowance for lattice/finite-l corrections at b <= sqrt(s)/2).
 measured only: L/C, R/2.806e-4, s*Psi'/P.
Seeds: none needed (deterministic). Result file opened with mode "x".
"""
import numpy as np, math, json, sys, time

TRUE = math.sqrt(math.pi)/(640*math.pi**2)
SIG = np.array([0.15, 0.12, 0.18]); CEN = np.array([0.30, 0.40, 0.50])

def h(z, kind):
    g = np.exp(-sum(z[i]**2/(2*SIG[i]**2) for i in range(3)))
    if kind == 'bump':
        return g*(1+0.5*z[0]/SIG[0])
    # x1-derivative of the bump: int f = 0
    return g*(0.5/SIG[0] - (z[0]/SIG[0]**2)*(1+0.5*z[0]/SIG[0]))

def fgrid(N, l, kind):
    b = l/N; x = np.arange(N)*b
    X = np.meshgrid(x, x, x, indexing='ij')
    f = np.zeros((N,N,N))
    R = 2 if l < 2 else 1
    for m1 in range(-R,R+1):
        for m2 in range(-R,R+1):
            for m3 in range(-R,R+1):
                z = [X[0]-CEN[0]-m1*l, X[1]-CEN[1]-m2*l, X[2]-CEN[2]-m3*l]
                f += h(z, kind)
    return f

def kvec(N, l):
    return 2*np.pi/l*np.fft.fftfreq(N, d=1.0/N)

def a_of(N, l, s, t=0.0):
    b = l/N; k = kvec(N,l)
    kh2 = (2/b*np.sin(k*b/2))**2
    K1, K2, K3 = np.meshgrid(kh2, kh2, kh2, indexing='ij')
    kk = K1+K2+K3; kk[0,0,0] = 1.0
    kh = np.sqrt(kk)
    a = (K1+K2)/kk*kh/2*np.exp(-t*kh-2*s*kk)
    a[0,0,0] = 0.0
    return a

def C_fft(f, l, s):
    N = f.shape[0]; b = l/N
    a = a_of(N,l,s)
    D = np.fft.ifftn(a).real*(N**3/l**3); del a
    Kh = np.fft.rfftn(D*D).real; del D
    F2 = np.abs(np.fft.rfftn(f))**2
    w = np.full(F2.shape[2], 2.0); w[0] = 1.0
    if N % 2 == 0: w[-1] = 1.0
    return 2*b**6/N**3*np.sum(F2*Kh*w)

def C_brute(f, l, s):
    N = f.shape[0]; b = l/N
    a = a_of(N,l,s).ravel()
    fh = (b**3*np.fft.fftn(f)).ravel()   # fhat_b at q index (conj irrelevant for |.|^2)
    idx = np.array(np.unravel_index(np.arange(N**3),(N,N,N))).T
    tot = 0.0
    for i in range(N**3):
        q = (idx[i]+idx) % N
        qi = np.ravel_multi_index(q.T,(N,N,N))
        tot += a[i]*np.sum(a*np.abs(fh[qi])**2)
    return 2/l**6*tot

def psi_prime(f, l):
    N = f.shape[0]; b = l/N
    F2 = np.abs(b**3*np.fft.fftn(f))**2
    k = kvec(N,l)  # fftfreq: -N/2 for even N gives k b = -pi; |q|^2 is the same for +pi
    Q1,Q2,Q3 = np.meshgrid(k*k,k*k,k*k,indexing='ij')
    return np.sum((Q1+Q2+Q3)*F2)/l**3

def lower_consts(l, b, s, kappa, theta):
    """Constants A, B' of Theorem V1 for cutoffs K = min(kappa/sqrt s, pi/b), Q = theta/sqrt s.
    1-D full sums on any shifted grid of spacing Delta=2pi/l: Poisson summation (exact),
    truncation tails: decreasing-tail integral comparison."""
    D = 2*np.pi/l; al = 4*s
    K = min(kappa/math.sqrt(s), math.pi/b); Q = theta/math.sqrt(s)
    eps = K*K*b*b/24
    Kp = K - Q/2; Lt = Kp - D
    d0 = 2*sum(math.exp(-m*m*l*l/(4*al)) for m in range(1,6))
    d1 = 2*sum(abs(1-m*m*l*l/(2*al))*math.exp(-m*m*l*l/(4*al)) for m in range(1,6))
    g0 = math.sqrt(math.pi/al)/D; g1 = math.sqrt(math.pi)/(2*al**1.5)/D
    T0 = g0*math.erfc(math.sqrt(al)*Lt)
    T1 = g1*math.erfc(math.sqrt(al)*Lt) + Lt*math.exp(-al*Lt*Lt)/al/D
    L0 = g0*(1-d0) - T0; L1 = g1*(1-d1) - T1
    U0 = g0*(1+d0); U1 = g1*(1+d1)
    S1lo = 2*L1*L0*L0 - U1*U0*U0
    fac = (1-eps)**4
    A = fac*S1lo/4
    Bp = fac*3/16*U0**3 + s*A
    ok = (eps < 1) and (Lt >= 1/math.sqrt(al)) and (A > 0) and (Q*Q >= A/Bp) and (Q <= K)
    return dict(K=K, Q=Q, kappa=kappa, theta=theta, eps=eps, A=A, Bp=Bp, d0=d0, d1=d1, conds=bool(ok))

def best_lower(l, b, s, Pb, Ps):
    best = None
    for kappa in [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]:
        for theta in [0.4, 0.45, 0.5, 0.6, 0.7]:
            lc = lower_consts(l, b, s, kappa, theta)
            if not lc['conds']:
                continue
            L = 2/l**3*(lc['A']*Pb - lc['Bp']*Ps)
            if best is None or L > best[0]:
                best = (L, lc)
    return best

def V_B1(l, s, Phi):
    c = 64*s/l**2
    th0 = 1+math.sqrt(math.pi/c); th1 = math.gamma(1.5)*c**-1.5 + 2*(1/(math.e*c))
    U2 = 3*th1*th0**2
    return 2/l**3*Phi*(math.pi**2/l**2)*U2

def main(out):
    res = {'P0': [], 'cases': []}
    for kind in ['bump','dbump']:
        f = fgrid(6, 1.0, kind)
        c1, c2 = C_fft(f,1.0,0.02), C_brute(f,1.0,0.02)
        rd = abs(c1-c2)/abs(c2)
        res['P0'].append(dict(kind=kind, fft=c1, brute=c2, rel=rd, pass_=bool(rd <= 1e-10)))
        print('P0', kind, c1, c2, rd, flush=True)
    for l in [1.0, 2.0, 4.0]:
        for s in [0.001, 0.002, 0.005]:
            N = math.ceil(2*l/math.sqrt(s)); b = l/N
            for kind in ['bump','dbump']:
                t0 = time.time()
                f = fgrid(N,l,kind)
                Pb = b**3*np.sum(f*f)
                C = C_fft(f,l,s)
                Ps = psi_prime(f,l)
                bl = best_lower(l,b,s,Pb,Ps)
                if bl is None:
                    lc = dict(conds=False); L = float('nan')
                else:
                    L, lc = bl
                V = V_B1(l,s,Pb)
                R = C*s**2.5/Pb
                hyp = bool(b <= math.sqrt(s)/2 and lc['conds'])
                d = dict(l=l,s=s,N=N,b=b,kind=kind,int_f=b**3*float(np.sum(f)),P_b=Pb,Psi_p=Ps,
                         s_Psi_over_P=s*Ps/Pb,C=C,L=L,V=V,L_over_C=L/C,R=R,R_over_true=R/TRUE,
                         hyp=hyp, **{k:v for k,v in lc.items()},
                         P1=(bool(L<=C) if lc['conds'] else None), P2=bool(C<=V), P3=(bool(L>0) if kind=='bump' else None),
                         P4=bool(R <= 1.05*TRUE), secs=time.time()-t0)
                res['cases'].append(d)
                print(json.dumps(d), flush=True)
                del f
    with open(out,'x') as fh:
        json.dump(res, fh, indent=1)

if __name__ == '__main__':
    main(sys.argv[1])
