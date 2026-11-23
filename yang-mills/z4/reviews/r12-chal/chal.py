"""
chal.py -- r12-chal challenger checks of THEOREMS_B (flowed free lattice Maxwell).
Usage: python3 chal.py <results.json>   (result file opened with mode "x"; never overwritten)
Fixed seeds: numpy default_rng(1), (2), (3). Single thread.

PREDICATES (fixed before the first run). Tolerances:
 TOL_ID = 1e-10 relative for identities: double precision, positive sums of <= 1e6 terms,
         round-off ~1e-13; 1e-10 leaves a 1000x margin.
 TOL_INEQ = 1e-12 relative slack for inequalities that may be tight (round-off only).
 Continuum sums truncated where the Gaussian factor < e^-50 (relative error < 1e-20).
P1  (A1) position-space C == momentum double sum, rel <= TOL_ID; N in {6,7}, l in {0.7,1,2},
         t in {0,0.1}, s = 0.02, my own non-symmetric f. Also FFT-convolution C == brute C.
P2  (A2) Parseval: sum_{q in BZ}|fhat_b(q)|^2 == l^3 b^3 sum_x f(bx)^2, rel <= TOL_ID.
P3  (A2) for all k in BZ\0: a(k)^2 <= (|k|^2/4) exp(-16 s|k|^2/pi^2).
P4  (A2) Schur: C_b <= (2/l^3) (b^3 sum f^2) sum_k a(k)^2.
P5  (A2) C_b <= V with Phi = l^3 sup f^2 (no hypothesis) in all cases, and with
         Phi_alias where b <= b0.
P6  (A3) for all k in BZ\0: P33 >= (4/pi^2)(k1^2+k2^2)/|k|^2.
P7  (A3) v1 <= C_b where b <= b0 and N >= 3.
P8  (A3) v2 <= C_b where b <= b0 and N >= 2M+1, M = ceil(l/(pi sqrt s)).
P9  (A3) boundary: with exact |fhat_b(0)|^2 in place of (int f)^2/4, the v2 sum with
         M = (N-1)/2 (odd N, boundary N = 2M+1) is <= C_b. Even N with M = N/2 (edge mode
         double counted, hypothesis violated): measured only.
P10 (A4) theta_j(c) <= bound, j = 0..4, 200 log-spaced c in [1e-3, 50]; U2,U4,U6 bound >= direct.
P11 (A5) |khat_i - k_i| <= b^2 |k_i|^3/24 for 10^5 random (b, k_i b in (-pi,pi]).
P12 (A5) |grad phi(p)| <= (3/2 + |p|(t+4s|p|)/2) e^{-t|p|-2s|p|^2}, 10^4 random p, central FD
         gradient (FD rel error ~1e-8; tolerance 1e-6).
P13 (A5) |C_b - C_s| <= K1 b^2 + K2 e^{-s/b^2} where b <= b0, including b just below b0.
P14 (A6) exact M1 <= (4/l^3) Phi sqrt(A0 A2), M2 <= (4/l^3) Phi (sqrt(A0 A4) + A2) with
         Phi = b^3 sum f^2 (sharpest), t = 0; and A_p <= (1/4)(2pi/l)^{2+p} U_{2+p}(64 s/l^2).
P15 (A8) r(s) = C_s(0) s^{5/2} / (sqrt(pi)/(640 pi^2) int f^2) -> 1: |r-1| decreasing as s
         decreases and < 0.05 at s = 0.0005 (my expectation; corrections O(s)).
P16 (A7) author's f: int f = 1.42213 (5 digits), b0 = 0.2537, Phi/int f^2 ~ 3.3,
         loss factor (pi/2)^5 (15/8) Phi/int f^2 ~ 60, table C(cont,s=.002,t=0) = 5633 and
         V(.002) = 6.63e5 to 3 digits. (Reproduction; measured.)
"""
import sys, json, math
import numpy as np
from math import gamma, pi, sqrt, exp, ceil

TOL_ID, TOL_INEQ = 1e-10, 1e-12
S4_UP = 16.5791  # PROOF_FREE_BOUNDS sec 0 (rigorous upper bound from bounds.py); not rederived
NF = 64

def F_mine(u1, u2, u3):
    return np.exp(0.6*np.cos(2*pi*u1+0.3) + 0.4*np.sin(2*pi*u2)*np.cos(2*pi*u3-0.7)
                  + 0.25*np.sin(2*pi*(u1+2*u3)) + 0.2*np.cos(4*pi*u2+1.1))

def F_auth(u1, u2, u3):
    return np.exp(0.8*np.cos(2*pi*u1) + 0.3*np.sin(4*pi*u1) + 0.6*np.cos(2*pi*u2-0.4)
                  + 0.5*np.sin(2*pi*u3) + 0.3*np.cos(2*pi*(u1-u3)))

def grid(N):
    u = np.arange(N)/N
    return np.meshgrid(u, u, u, indexing='ij')

def nfreq(N):  # BZ representatives -N/2 < n <= N/2
    j = np.arange(N); return np.where(j <= N//2, j, j-N)

def fdata(F, l):
    """continuum data of f(y)=F(y/l) on torus side l."""
    U = grid(NF); Fg = F(*U)
    n = np.fft.fftfreq(NF, 1.0/NF)
    n1, n2, n3 = np.meshgrid(n, n, n, indexing='ij'); lap = -(2*pi)**2*(n1**2+n2**2+n3**2)
    def D4(G):
        d = np.real(np.fft.ifftn(lap**2*np.fft.fftn(G)))
        return np.mean(np.abs(d))/l  # int |Lap_y^2 f| dy = l^3 * l^-4 * mean|Lap_u^2 F|
    d = dict(intf=l**3*Fg.mean(), intf2=l**3*(Fg**2).mean(), l1=l**3*np.abs(Fg).mean(),
             D4=D4(Fg), D4sq=D4(Fg**2), supf2=float((F(*grid(96))**2).max()))
    d['b0'] = min(l/3, 2*pi*(abs(d['intf'])/(2*S4_UP*d['D4']))**0.25)
    d['Phi_alias'] = d['intf2'] + S4_UP*(d['b0']/(2*pi))**4*d['D4sq']
    d['Phi_sup'] = l**3*d['supf2']
    d['ftilde'] = l**3*np.fft.fftn(Fg)/NF**3  # index n mod NF
    return d

def lattice(F, l, N, s, t):
    b = l/N; n = nfreq(N)
    n1, n2, n3 = np.meshgrid(n, n, n, indexing='ij')
    k = [2*pi*x/l for x in (n1, n2, n3)]
    kh = [(2/b)*np.sin(x*b/2) for x in k]
    kh2 = kh[0]**2+kh[1]**2+kh[2]**2; k2 = k[0]**2+k[1]**2+k[2]**2
    with np.errstate(invalid='ignore', divide='ignore'):
        P33 = np.where(kh2 > 0, (kh[0]**2+kh[1]**2)/kh2, 0.0)
    khn = np.sqrt(kh2)
    a = P33*khn/2*np.exp(-t*khn-2*s*kh2); a[0, 0, 0] = 0.0
    fg = F(*grid(N)); fhat = b**3*np.fft.fftn(fg)
    G = np.abs(fhat)**2
    return dict(b=b, k=k, kh=kh, kh2=kh2, k2=k2, P33=P33, khn=khn, a=a, fg=fg, fhat=fhat, G=G)

def conv(x, y):
    return np.real(np.fft.ifftn(np.fft.fftn(x)*np.fft.fftn(y)))

def C_fft(L, l):
    return 2/l**6*np.sum(L['G']*conv(L['a'], L['a']))

def theta_bound(j, c):
    if j == 0: return 1+sqrt(pi/c)
    return gamma(j+0.5)*c**(-j-0.5) + 2*(j/(e*c))**j
e = math.e

def theta_exact(j, c):
    mmax = int(sqrt(60/c))+5 + int(2*sqrt(j/c))
    m = np.arange(-mmax, mmax+1, dtype=float)
    return float(np.sum(m**(2*j)*np.exp(-c*m*m)))

def Uq(q, c, th):
    T = [th(j, c) for j in range(4)]
    if q == 2: return 3*T[1]*T[0]**2
    if q == 4: return 3*T[2]*T[0]**2 + 6*T[1]**2*T[0]
    if q == 6: return 3*T[3]*T[0]**2 + 18*T[2]*T[1]*T[0] + 6*T[1]**3
U = lambda q, c: Uq(q, c, theta_bound)
Uex = lambda q, c: Uq(q, c, theta_exact)

def V_of(l, s, Phi):
    return 2/l**3*Phi*(pi**2/l**2)*U(2, 64*s/l**2)

def v1_of(fd, l, s, t):
    k3 = 3*sqrt(3)/l
    m = min(k3**2*exp(-2*t*k3), (2*pi/l)**2*exp(-4*pi*t/l))
    return fd['intf']**2/(2*l**6)*m*exp(-16*pi**2*s/l**2)

def v2sum(l, s, t, M):
    n = np.arange(-M, M+1); n1, n2, n3 = np.meshgrid(n, n, n, indexing='ij')
    k1, k2, k3 = [2*pi*x/l for x in (n1, n2, n3)]; kk = k1**2+k2**2+k3**2; kk[M, M, M] = 1.0
    kn = np.sqrt(kk); term = (k1**2+k2**2)**2/kk*np.exp(-2*t*kn-4*s*kk); term[M, M, M] = 0.0
    return float(term.sum())

def v2_of(fd, l, s, t, M):
    return fd['intf']**2/(2*l**6)*(16/pi**6)*v2sum(l, s, t, M)

def C_cont(fd, l, s, t):
    """continuum C_s(t) = (2/l^6) sum_q |ftilde(q)|^2 sum_k a_c(k) a_c(q-k), all k in Z^3\\0."""
    R = int(ceil(sqrt(25/s)*l/(2*pi)))+1
    L = 4*R+4
    n = np.fft.fftfreq(L, 1.0/L)
    n1, n2, n3 = np.meshgrid(n, n, n, indexing='ij')
    k1, k2, k3 = [2*pi*x/l for x in (n1, n2, n3)]
    kk = k1**2+k2**2+k3**2; kn = np.sqrt(kk)
    with np.errstate(invalid='ignore', divide='ignore'):
        ac = np.where(kk > 0, (k1**2+k2**2)/(2*kn)*np.exp(-t*kn-2*s*kk), 0.0)
    ac[(np.abs(n1) > R) | (np.abs(n2) > R) | (np.abs(n3) > R)] = 0.0
    G = np.zeros((L, L, L))
    ft = fd["ftilde"]; h = min(NF//2 - 1, L//2 - 1)
    idx = np.r_[0:h+1, NF-h:NF]; tgt = np.r_[0:h+1, L-h:L]
    G[np.ix_(tgt, tgt, tgt)] = np.abs(ft[np.ix_(idx, idx, idx)])**2
    del n1, n2, n3, k1, k2, k3
    return 2/l**6*float(np.sum(G*conv(ac, ac)))

def brute(F, l, N, s, t):
    L = lattice(F, l, N, s, t); b = L['b']
    x = np.array(np.meshgrid(*[np.arange(N)]*3, indexing='ij')).reshape(3, -1).T*b  # positions
    kv = np.array([L['k'][i].ravel() for i in range(3)]).T
    a = L['a'].ravel(); fx = L['fg'].ravel()
    E = np.exp(1j*x@kv.T)  # [x,k]
    D = (E*a)@E.conj().T/l**3   # D(x-y)
    Cpos = 2*b**6*float(np.real(fx@(np.real(D)**2)@fx))
    # momentum: fhat_b(k+k') by explicit sum
    Cmom = 0.0
    for i in range(len(a)):
        if a[i] == 0: continue
        q = kv[i]+kv
        fh = b**3*(np.exp(-1j*q@x.T)@fx)
        Cmom += float(np.sum(np.abs(fh)**2*a[i]*a))
    Cmom *= 2/l**6
    return Cpos, Cmom, C_fft(L, l), float(np.max(np.abs(np.imag(D))))

def main():
    out = open(sys.argv[1], 'x')
    R = dict(fail=[], counts={}); np.seterr(over='ignore')
    def rec(name, ok, info):
        R['counts'].setdefault(name, [0, 0]); R['counts'][name][0 if ok else 1] += 1
        if not ok: R['fail'].append([name, info])
    Ls = [0.7, 1.0, 2.0]
    FD = {l: fdata(F_mine, l) for l in Ls}
    R['fdata'] = {str(l): {k: v for k, v in FD[l].items() if k != 'ftilde'} for l in Ls}
    print('fdata', R['fdata'], flush=True)
    # ---- A1
    R['A1'] = []
    for N in (6, 7):
        for l in Ls:
            for t in (0.0, 0.1):
                cp, cm, cf, im = brute(F_mine, l, N, 0.02, t)
                r1 = abs(cp-cm)/cm; r2 = abs(cf-cm)/cm
                rec('P1', r1 <= TOL_ID and r2 <= TOL_ID, [N, l, t, r1, r2])
                R['A1'].append([N, l, t, cp, cm, cf, r1, r2, im])
    print('A1 done', R['counts'], flush=True)
    # ---- A2, A3
    R['A23'] = []; nq = 0
    for l in Ls:
        fd = FD[l]
        for s in (0.002, 0.02, 0.2):
            M = int(ceil(l/(pi*sqrt(s))))
            for t in (0.0, 0.1):
                for N in (8, 9, 16, 17, 32):
                    L = lattice(F_mine, l, N, s, t); b = L['b']
                    pars = l**3*b**3*np.sum(L['fg']**2)
                    rp = abs(L['G'].sum()-pars)/pars; rec('P2', rp <= TOL_ID, [l, N, rp])
                    m = L['k2'] > 0
                    lhs = L['a'][m]**2; rhs = L['k2'][m]/4*np.exp(-16*s*L['k2'][m]/pi**2)
                    rec('P3', bool(np.all(lhs <= rhs*(1+TOL_INEQ))), [l, s, t, N])
                    lo = 4/pi**2*(L['k'][0][m]**2+L['k'][1][m]**2)/L['k2'][m]
                    rec('P6', bool(np.all(L['P33'][m] >= lo*(1-TOL_INEQ))), [l, N])
                    C = C_fft(L, l); Phi_true = b**3*np.sum(L['fg']**2)
                    schur = 2/l**3*Phi_true*np.sum(L['a']**2)
                    rec('P4', C <= schur*(1+TOL_INEQ), [l, s, t, N, C, schur])
                    Vs = V_of(l, s, fd['Phi_sup']); Va = V_of(l, s, fd['Phi_alias'])
                    qual = (b <= fd['b0']) and N >= 3; nq += qual
                    rec('P5sup', C <= Vs, [l, s, t, N, C, Vs])
                    if qual: rec('P5alias', C <= Va, [l, s, t, N, C, Va])
                    v1 = v1_of(fd, l, s, t)
                    if qual: rec('P7', v1 <= C, [l, s, t, N, v1, C])
                    q2 = qual and N >= 2*M+1
                    v2 = v2_of(fd, l, s, t, M) if q2 else None
                    if q2: rec('P8', v2 <= C, [l, s, t, N, v2, C])
                    # P9 boundary
                    g0 = L['G'][0, 0, 0]
                    if N % 2 == 1:
                        Mb = (N-1)//2
                        v2b = 2/l**6*g0*(4/pi**6)*v2sum(l, s, t, Mb)
                        diag = 2/l**6*g0*np.sum(L['a']**2)
                        rec('P9', v2b <= diag*(1+TOL_INEQ) and diag <= C*(1+TOL_INEQ), [l, s, t, N, v2b, diag, C])
                        p9 = [Mb, v2b, diag]
                    else:
                        Mb = N//2
                        v2b = 2/l**6*g0*(4/pi**6)*v2sum(l, s, t, Mb)
                        diag = 2/l**6*g0*np.sum(L['a']**2)
                        p9 = [Mb, v2b, diag, 'even N, M=N/2 measured only', v2b <= diag]
                    R['A23'].append(dict(l=l, s=s, t=t, N=N, b=b, qual=bool(qual), M=M, q2=bool(q2),
                        C=C, Vsup=Vs, Valias=Va, v1=v1, v2=v2, p9=p9, schur=schur,
                        fhat0_over_intf=float(abs(L['fhat'][0, 0, 0])/fd['intf'])))
    R['A23_qualifying'] = [nq, len(R['A23'])]
    print('A23 done', R['counts'], R['A23_qualifying'], flush=True)
    # ---- A4
    worst = {}
    for j in range(5):
        for c in np.logspace(-3, math.log10(50), 200):
            ex = theta_exact(j, c); bd = theta_bound(j, c)
            rec('P10', ex <= bd*(1+TOL_INEQ), [j, c, ex, bd]); worst[j] = max(worst.get(j, 0), ex/bd)
    for q in (2, 4, 6):
        for c in np.logspace(-3, math.log10(50), 40):
            mmax = int(sqrt(60/c))+8; m = np.arange(-mmax, mmax+1)
            n1, n2, n3 = np.meshgrid(m, m, m, indexing='ij') if mmax < 120 else (None,)*3
            if n1 is None: continue
            nn = (n1**2+n2**2+n3**2).astype(float); d = float(np.sum(nn**(q//2)*np.exp(-c*nn)))
            rec('P10U', d <= U(q, c)*(1+TOL_INEQ) and abs(d-Uex(q, c)) <= 1e-9*d, [q, c, d, U(q, c), Uex(q, c)])
    R['A4_max_ratio'] = worst
    print('A4 done', R['counts'], flush=True)
    # ---- A5 step1, gradient
    rng = np.random.default_rng(1)
    bb = rng.uniform(0.01, 1, 100000); y = rng.uniform(-pi, pi, 100000); y[:10] = pi
    kk = y/bb; khat = (2/bb)*np.sin(kk*bb/2)
    rec('P11', bool(np.all(np.abs(khat-kk) <= bb**2*np.abs(kk)**3/24*(1+TOL_INEQ))), 'step1')
    R['A5_step1_maxratio'] = float(np.max(np.abs(khat-kk)/(bb**2*np.abs(kk)**3/24)))
    rng = np.random.default_rng(2); mx = 0; mxg = 0
    def phi(p, t, s):
        r = np.linalg.norm(p); return (p[0]**2+p[1]**2)/(2*r)*exp(-t*r-2*s*r*r)
    for _ in range(10000):
        p = rng.normal(size=3)*rng.uniform(0.1, 30); t = rng.uniform(0, 1); s = rng.uniform(0, 0.3)
        r = np.linalg.norm(p); hh = 1e-6*r
        g = np.array([(phi(p+hh*ei, t, s)-phi(p-hh*ei, t, s))/(2*hh) for ei in np.eye(3)])
        gg = np.array([(phi(p+hh*ei, 0, 0)-phi(p-hh*ei, 0, 0))/(2*hh) for ei in np.eye(3)])
        bd = (1.5+r*(t+4*s*r)/2)*exp(-t*r-2*s*r*r)
        ok = np.linalg.norm(g) <= bd*(1+1e-6); rec('P12', ok, [list(p), t, s])
        mx = max(mx, np.linalg.norm(g)/bd); mxg = max(mxg, np.linalg.norm(gg))
    R['A5_grad_max_ratio'] = mx; R['A5_max_grad_g'] = mxg
    print('A5a done', R['counts'], flush=True)
    # ---- A5 final inequality (B2), A6 (B3)
    R['B2'] = []; R['B3'] = []
    for l in Ls:
        fd = FD[l]; Nb0 = int(ceil(l/fd['b0']))
        Fb = fd['l1'] + S4_UP*(fd['b0']/pi)**4*fd['D4']
        for s in (0.002, 0.02, 0.2):
            if s == 0.002 and l == 2.0: Ns = (Nb0, 16)
            else: Ns = (Nb0, 16, 32)
            for t in (0.0, 0.1):
                Cs = C_cont(fd, l, s, t)
                Rr = int(ceil(l*sqrt(12.5/s)/2))+2
                n = np.arange(-Rr, Rr+1); n1, n2, n3 = np.meshgrid(n, n, n, indexing='ij')
                kk = (2*pi/l)**2*(n1**2+n2**2+n3**2).astype(float); kn = np.sqrt(kk); del n1, n2, n3
                ab = kn/2*np.exp(-8*s*kk/pi**2); abs2 = kk/4*np.exp(-8*s*kk/pi**2)
                h = kn**3/24*(1.5+kn*(t+4*s*kn)/2)*np.exp(-8*s*kk/pi**2)
                Sa, Sa2, Sas2, Sh2 = ab.sum(), (ab**2).sum(), abs2.sum(), (h**2).sum()
                K1 = 2/l**6*((Fb+fd['l1'])*S4_UP*fd['D4']*fd['b0']**2/pi**4*Sa**2
                             + 2*l**3*fd['intf2']*sqrt(Sh2*Sa2))
                K2 = 2/l**6*2*l**3*(fd['Phi_alias']+2*fd['intf2'])*sqrt(Sas2*Sa2)
                for N in Ns:
                    L = lattice(F_mine, l, N, s, t); b = L['b']
                    if b > fd['b0']: continue
                    C = C_fft(L, l); err = abs(C-Cs); bd = K1*b*b+K2*exp(-s/b/b)
                    rec('P13', err <= bd, [l, s, t, N, err, bd])
                    R['B2'].append(dict(l=l, s=s, t=t, N=N, b=b, b0=fd['b0'], C=C, Cs=Cs, err=err,
                                        bound=bd, K1=K1, K2=K2, ratio=bd/err if err > 0 else None))
                    if t == 0.0:
                        a = L['a']; kh = L['khn']; G = L['G']; c2 = 2/l**6
                        M1 = c2*2*np.sum(G*conv(a*kh, a))
                        M2 = c2*(2*np.sum(G*conv(a*kh**2, a))+2*np.sum(G*conv(a*kh, a*kh)))
                        A0, A2, A4 = [float(np.sum(a**2*kh**p)) for p in (0, 2, 4)]
                        Phi = b**3*np.sum(L['fg']**2)
                        b1 = 4/l**3*Phi*sqrt(A0*A2); b2 = 4/l**3*Phi*(sqrt(A0*A4)+A2)
                        rec('P14', M1 <= b1*(1+TOL_INEQ) and M2 <= b2*(1+TOL_INEQ), [l, s, N, M1, b1, M2, b2])
                        for p, Ap in ((0, A0), (2, A2), (4, A4)):
                            rec('P14A', Ap <= 0.25*(2*pi/l)**(2+p)*U(2+p, 64*s/l**2), [l, s, N, p])
                        # finite-difference cross-check of M1 = -C'(0)
                        dt = 1e-5; Cp = C_fft(lattice(F_mine, l, N, s, dt), l)
                        R['B3'].append(dict(l=l, s=s, N=N, M1=M1, b1=b1, M2=M2, b2=b2,
                                            M1_fd=(C-Cp)/dt, M0=C))
                print('B2', l, s, t, R['counts'].get('P13'), flush=True)
    # ---- A8
    R['A8'] = []
    for l in (1.0, 0.7):
        fd = FD[l]; pref = sqrt(pi)/(640*pi**2)*fd['intf2']
        for s in (0.02, 0.005, 0.002, 0.001, 0.0005):
            Cs = C_cont(fd, l, s, 0.0); R['A8'].append([l, s, Cs, Cs*s**2.5/pref])
        rs = [abs(x[3]-1) for x in R['A8'] if x[0] == l]
        rec('P15', all(rs[i+1] < rs[i] for i in range(len(rs)-1)) and rs[-1] < 0.05, [l, rs])
    print('A8', R['A8'], flush=True)
    # ---- A7 / author's f
    fa = fdata(F_auth, 1.0)
    au = {k: v for k, v in fa.items() if k != 'ftilde'}
    au['Phi_over_intf2'] = fa['Phi_alias']/fa['intf2']
    au['loss'] = (pi/2)**5*15/8*au['Phi_over_intf2']
    au['V'] = {s: V_of(1.0, s, fa['Phi_alias']) for s in (0.002, 0.005, 0.02)}
    au['Ccont'] = {s: C_cont(fa, 1.0, s, 0.0) for s in (0.002, 0.005, 0.02)}
    au['v1'] = {s: v1_of(fa, 1.0, s, 0.0) for s in (0.002, 0.005, 0.02)}
    au['v2'] = {s: v2_of(fa, 1.0, s, 0.0, int(ceil(1/(pi*sqrt(s))))) for s in (0.002, 0.005, 0.02)}
    au['Vlead_over_Clead_check'] = {s: au['V'][s]/au['Ccont'][s] for s in au['V']}
    R['author'] = au
    ok = abs(au['intf']-1.42213) < 1e-5 and abs(au['b0']-0.2537) < 1e-4 and abs(au['Ccont'][0.002]/5633-1) < 1e-3 and abs(au['V'][0.002]/6.63e5-1) < 5e-3
    rec('P16', ok, au)
    print('author', au, flush=True)
    json.dump(R, out, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
    out.close()
    print('COUNTS', R['counts']); print('FAILS', len(R['fail']))
    for f in R['fail'][:40]: print(f)

if __name__ == '__main__':
    main()
