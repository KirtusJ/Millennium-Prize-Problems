"""e13_recompute.py -- independent recomputation of E13.md's explicit Delta1 bound and checks.

Predicates (fixed before the first run; run1 died on missing scipy, my defect; v2 uses numpy Gauss-Legendre):
 EP1  log J: the SVD/closed form of E13 s3 agrees with the det/solve Gaussian formula to 1e-9 (abs)
      on 300 random tube points (tolerance: double precision with condition numbers <= 1e3).
 EP2  rho(beta) = sqrt(2 pi beta) e^-beta I1(beta) satisfies D <= rho <= 1 for beta in BETAS.
 EP3  Taylor remainder: |F - M| <= Err(x, lambda) on 20000 random (x in K, xi in product ball)
      samples at beta = 4096, L = 3 (non-vacuous points only; count qualifying points).
 EP4  recomputed sup_K Delta1 (my grid, formula of E13 s5) is within 25% of E13's table at
      beta = 16384 (13.8) and beta = 2.7e8 (0.167). Tolerance 25%: grid and L-grid unknown.
 EP5  sup_K Delta1 nonincreasing over BETAS (E13 P7).
Parameters from E13 s6: eta=0.25, eta'=0.5, theta0=0.5, ell=0.08, r0=0.15, M=2. Seed 12345.
"""
import numpy as np, sys
from math import erfc as _erfc
erfc = np.vectorize(_erfc)
_gx, _gw = np.polynomial.legendre.leggauss(200)
def quad(f, a, b, **k):
    x = 0.5*(b-a)*_gx + 0.5*(a+b); return (0.5*(b-a)*np.sum(_gw*f(x)), 0)
def ive(nu, z):  # e^-z I_1(z) = (1/pi) int_0^pi e^{z(cos t-1)} cos t dt (nu=1 only)
    T = min(np.pi, 60/np.sqrt(z)); x = 0.5*T*(_gx+1)
    return 0.5*T*np.sum(_gw*np.exp(z*(np.cos(x)-1))*np.cos(x))/np.pi
rng = np.random.default_rng(12345)
eta, etap, th0, ell, r0, M = 0.25, 0.5, 0.5, 0.08, 0.15, 2.0
eps = lambda s: 2*np.arcsinh(s)
def Psip(a): return np.sqrt(2*(eps(np.abs(np.sin(a))) + eta))
def Psipp(a, d=1e-6): return (Psip(a+d)-Psip(a-d))/(2*d)
aa = np.linspace(etap-0.1, np.pi-etap+0.1, 4001)
H_Psi = max(np.max(np.abs(Psipp(aa))), np.max(np.abs(Psip(aa)/np.tan(aa))))
Lam = Psip(np.pi/2)
def Theta(a): return th0*(np.sqrt(a*a+ell*ell)-ell)
def Thetap(a): return th0*a/np.sqrt(a*a+ell*ell)
H_Th = th0/ell
def Psi_diff(a, ap):  # Psi(ap)-Psi(a) by quadrature
    return quad(Psip, a, ap, epsabs=1e-13, epsrel=1e-12)[0]
def cross_mat(u):
    return np.array([[0,-u[2],u[1]],[u[2],0,-u[0]],[-u[1],u[0],0]])
def point(a1, a2, chi):
    s1, s2 = np.sin(a1), np.sin(a2)
    u1 = s1*np.array([1.,0,0]); u2 = s2*np.array([np.cos(chi), np.sin(chi), 0])
    return np.cos(a1), u1, np.cos(a2), u2
def ellmat(x01,u1,x02,u2):
    R1 = x01*np.eye(3)+cross_mat(u1); R2 = x02*np.eye(3)+cross_mat(u2)
    return np.hstack([-cross_mat(u2)@R1, cross_mat(u1)@R2])
def pvec(a1,a2,u1,u2):
    uh1 = u1/np.linalg.norm(u1)
    uh2 = u2/np.linalg.norm(u2) if np.linalg.norm(u2)>0 else np.array([0,0,1.])
    return -np.concatenate([Psip(a1)*uh1, Thetap(a2)*uh2])
def logJ_det(h,b,L,p):
    A = np.eye(6)+2*h*L.T@L; c = p-2*h*L.T@b
    return -0.5*np.linalg.slogdet(A)[1] + 0.5*c@np.linalg.solve(A,c) - h*b@b
def logJ_svd(h,b,L,p,w):
    U,sv,Vt = np.linalg.svd(L)
    nw = np.linalg.norm(w); bw = np.linalg.norm(b)
    sig2 = sv**2
    if nw == 0:
        return p@p/2 - 0.5*np.sum(np.log(1+2*h*sig2))
    # sigma_w: singular direction aligned with w
    j = np.argmax(np.abs(U.T@(w/nw)))
    sw = sv[j]
    kap_pw = (U[:,j]@(L@p))/sw  # = p_w
    pw = kap_pw
    return p@p/2 - 0.5*np.sum(np.log(1+2*h*sig2)) - (h*pw**2*sw**2 + 2*h*sw*pw*bw*np.sign(U[:,j]@w) + h*bw**2)/(1+2*h*sw**2)
def setup(a1,a2,chi,beta):
    x01,u1,x02,u2 = point(a1,a2,chi)
    w = np.cross(u1,u2); S2 = u1@u1+u2@u2; S = np.sqrt(S2)
    h = 1+np.sqrt(1+S2)/S; b = np.sqrt(beta)*w
    L = ellmat(x01,u1,x02,u2); p = pvec(a1,a2,u1,u2)
    return dict(x01=x01,u1=u1,x02=x02,u2=u2,w=w,S=S,h=h,b=b,L=L,p=p)
def Err(d, a1, a2, beta, lam):
    w = np.linalg.norm(d['w']); S = d['S']; h = d['h']
    m = w+np.sqrt(2)*S*lam; r = 2*lam**2*w+(lam+lam**2)**2
    EW = beta*(2*m*r+r*r); BW = beta*(m+r)**2
    dS2 = 2*sum(np.sin(a)*lam+lam**2 for a in (a1,a2))
    sm = S*S-dS2
    if sm <= 0 or lam > 0.5: return np.inf
    dh = dS2/(2*sm**2*np.sqrt(1+1/sm))
    lp = np.arcsin(lam); sb = np.sqrt(beta)
    return (h*EW + dh*BW + sb*(0.5*H_Psi*lp**2 + abs(Psip(a1))*(lp-lam))
            + sb*(0.5*H_Th*lp**2 + abs(Thetap(a2))*(lp-lam)))
def chi3_tail(r):
    r = np.maximum(r, 0.0)
    return erfc(r/np.sqrt(2)) + np.sqrt(2/np.pi)*r*np.exp(-r*r/2)
def gap(d):
    lJ = logJ_det(d['h'],d['b'],d['L'],d['p'])
    return (-eps(d['S']) + d['p']@d['p']/2) - ((d['h']-2)*d['b']@d['b'] + lJ), lJ
def Delta1(a1,a2,chi,beta,Ls):
    d = setup(a1,a2,chi,beta); g,_ = gap(d)
    lrho = np.log(np.sqrt(2*np.pi*beta)*ive(1,beta))
    best = np.inf
    for L in Ls:
        lam = L/np.sqrt(beta)
        e = Err(d,a1,a2,beta,lam)
        if not np.isfinite(e): continue
        tail = chi3_tail(L-abs(Psip(a1))) + chi3_tail(L-abs(Thetap(a2)))
        tj = np.exp(g+eps(d['S'])+(d['h']-2)*d['b']@d['b'])*tail
        if tj >= 1: continue
        best = min(best, g+e+L**4/beta+2*lrho-np.log1p(-tj))
    return best
def tube_grid(beta, n1=17, n2=6, nb=5):
    for a1 in np.linspace(etap, np.pi-etap, n1):
        for a2 in np.linspace(0, r0, n2):
            S = np.sqrt(np.sin(a1)**2+np.sin(a2)**2)
            bmax = M*np.sqrt(S/np.sqrt(1+S*S))*0.999
            wmax = np.sin(a1)*np.sin(a2)
            for fb in np.linspace(0,1,nb):
                bw = fb*bmax
                if a2 == 0:
                    if fb > 0: continue
                    chi = 0.0
                else:
                    sc = bw/(np.sqrt(beta)*wmax)
                    if sc > 1: continue
                    chi = np.arcsin(sc)
                yield a1,a2,chi
out = open(sys.argv[1], 'x')
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s+'\n'); out.flush()
log('H_Psi', H_Psi, 'Lambda', Lam, 'H_Theta', H_Th)
# EP1
mx = 0
for _ in range(300):
    a1 = rng.uniform(etap, np.pi-etap); a2 = rng.uniform(1e-3, r0); beta = 10**rng.uniform(2,6)
    S = np.sqrt(np.sin(a1)**2+np.sin(a2)**2); bmax = M*np.sqrt(S/np.sqrt(1+S*S))
    sc = min(1, rng.uniform(0,bmax)/(np.sqrt(beta)*np.sin(a1)*np.sin(a2)))
    d = setup(a1,a2,np.arcsin(sc),beta)
    mx = max(mx, abs(logJ_det(d['h'],d['b'],d['L'],d['p'])-logJ_svd(d['h'],d['b'],d['L'],d['p'],d['w'])))
log('EP1 max|logJ_det-logJ_svd| =', mx, 'MET' if mx < 1e-9 else 'FAILED')
# EP2
BETAS = [256,1024,4096,16384,65536,262144,1048576,4194304,16777216,67108864,268435456]
ok = 0
for beta in BETAS:
    rho = np.sqrt(2*np.pi*beta)*ive(1,beta); D = 1-1/(2*beta)-np.sqrt(2*np.pi*beta)*np.exp(-beta)/2
    ok += (D <= rho <= 1)
log('EP2 D<=rho<=1 at', ok, 'of', len(BETAS), 'MET' if ok == len(BETAS) else 'FAILED')
# EP3 Taylor remainder vs exact exponent
beta = 4096.0; Lt = 3.0; lam = Lt/np.sqrt(beta)
def qmul(a0,a,b0,b): return a0*b0-a@b, a0*b+b0*a+np.cross(a,b)
viol = 0; qual = 0; worst = 0
for it in range(20000):
    a1 = rng.uniform(etap, np.pi-etap); a2 = rng.uniform(0, r0)
    S = np.sqrt(np.sin(a1)**2+np.sin(a2)**2); bmax = M*np.sqrt(S/np.sqrt(1+S*S))
    wm = np.sin(a1)*np.sin(a2)
    sc = 0 if wm == 0 else min(1, rng.uniform(0,bmax)/(np.sqrt(beta)*wm))
    d = setup(a1,a2,np.arcsin(sc),beta)
    e = Err(d,a1,a2,beta,lam)
    if not np.isfinite(e): continue
    qual += 1
    xi = []
    for i in range(2):
        v = rng.normal(size=3); v /= np.linalg.norm(v); xi.append(v*lam*rng.uniform()**(1/3))
    xi = np.concatenate(xi)
    g01 = np.sqrt(1-xi[:3]@xi[:3]); g02 = np.sqrt(1-xi[3:]@xi[3:])
    y01,v1 = qmul(d['x01'],d['u1'],g01,xi[:3]); y02,v2 = qmul(d['x02'],d['u2'],g02,xi[3:])
    a1p = np.arccos(np.clip(y01,-1,1)); a2p = np.arccos(np.clip(y02,-1,1))
    Wp = np.cross(v1,v2)@np.cross(v1,v2); Sp = np.sqrt(v1@v1+v2@v2); hp = 1+np.sqrt(1+Sp*Sp)/Sp
    F = -hp*beta*Wp - np.sqrt(beta)*Psi_diff(a1,a1p) - np.sqrt(beta)*(Theta(a2p)-Theta(a2))
    z = d['b']+np.sqrt(beta)*d['L']@xi
    Mo = -d['h']*z@z + np.sqrt(beta)*d['p']@xi
    r = abs(F-Mo)/e; worst = max(worst, r); viol += (r > 1)
log('EP3 Taylor: qualifying', qual, 'of 20000; violations', viol, 'worst |F-M|/Err', worst, 'MET' if viol == 0 else 'FAILED')
# EP4/EP5
Ls = np.linspace(1.0, 12.0, 111)
sups = {}
for beta in [4096,16384,65536,262144,1048576,4194304,16777216,67108864,268435456]:
    vals = [(Delta1(a1,a2,chi,beta,Ls),a1,a2,chi) for a1,a2,chi in tube_grid(beta)]
    v = max(vals)
    sups[beta] = v[0]
    log('beta', beta, 'sup_K Delta1', round(v[0],4), 'at a1,a2,chi', [round(x,3) for x in v[1:]], 'npts', len(vals))
ep4 = abs(sups[16384]/13.8-1) < 0.25 and abs(sups[268435456]/0.167-1) < 0.25
log('EP4', 'MET' if ep4 else 'FAILED', sups[16384], sups[268435456])
bs = sorted(sups); mono = all(sups[bs[i+1]] <= sups[bs[i]] for i in range(len(bs)-1))
log('EP5', 'MET' if mono else 'FAILED')
