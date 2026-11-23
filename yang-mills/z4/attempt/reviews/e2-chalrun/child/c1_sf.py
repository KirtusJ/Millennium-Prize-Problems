"""c1(R;U(1)) for the compact U(1) Schroedinger functional, momentum-space blocks.
Predicates fixed BEFORE first run (tolerances: roundoff ~1e-12 for double LAPACK on
<=30x30 blocks; 1e-6 for FD checks since 5th-order Richardson error with h=1e-3 is ~1e-9
and k itself is ~1e1, so abs err in c1 ~1e-9; 1e-6 for quoted values = 6-decimal rounding 5e-7 plus slack):
 P1 control.txt == 0.541196
 P2 every H(p) Hermitian to 1e-12 (count blocks passing)
 P3 closed-form k equals central FD of S0(eta) to 1e-6 relative
 P4 trace formula tr[A^-1 H_t]/(2N_t) equals -Gamma1'/k (Richardson FD) to 1e-6 abs
 P5 ||H(p)D(p)|| < 1e-10 for every p (count blocks passing)
 P6 A(p) positive definite (min eigenvalue > 1e-10) for every p (count blocks)
 P7 |c1 - quoted| <= 1e-6 for each R with a quoted value
Result file results.txt is opened with mode 'x'. No randomness (no seed needed; seed 0 set anyway).
"""
import numpy as np, itertools, sys, math
np.random.seed(0)
ETA0 = math.pi/4
QUOTED = {2:.228751,3:.229316,4:.233057,5:.236059,6:.238253,8:.241119}

def setup(R, eta):
    T = R
    phi, phip = -eta, -(math.pi-eta)
    ang = lambda x0: (phi + (phip-phi)*x0/T)/R   # spatial link angle at time x0
    idx = {}
    for x0 in range(T): idx[(x0,0)] = len(idx)
    for x0 in range(1,T):
        for k in (1,2,3): idx[(x0,k)] = len(idx)
    return T, ang, idx

def plaq_list(R, eta, only_time=False):
    """list of (coef, [(linkindex, sign, rvec)]) for base site spatial 0, with cos(theta)"""
    T, ang, idx = setup(R, eta)
    e = {0:(0,0,0),1:(1,0,0),2:(0,1,0),3:(0,0,1)}
    out = []
    def lang(x0,mu): return 0.0 if mu==0 else ang(x0)
    for x0 in range(T+1):
        for mu in range(4):
            for nu in range(mu+1,4):
                if only_time and mu!=0: continue
                pos = lambda m,n: None
                # links: (x,mu),(x+mu,nu),(x+nu,mu)^-,(x,nu)^-
                def sh(x0_,m): return x0_+1 if m==0 else x0_
                links = [((x0,mu),+1,(0,0,0),x0),
                         ((sh(x0,mu),nu),+1,e[mu] if mu else (0,0,0),sh(x0,mu)),
                         ((sh(x0,nu),mu),-1,e[nu] if nu else (0,0,0),sh(x0,nu)),
                         ((x0,nu),-1,(0,0,0),x0)]
                if mu==0 and x0==T: continue
                th = sum(s*lang(l[1] if False else l[0][0], l[0][1]) if False else s*lang(lk[0],lk[1]) for lk,s,r,_ in links)
                dyn = [(idx[lk],s,r) for lk,s,r,_ in links if lk in idx]
                if not dyn: continue
                out.append((math.cos(th), dyn, th))
    return out, idx, T

def Hblock(R, eta, p, only_time=False):
    pl, idx, T = plaq_list(R, eta, only_time)
    n = len(idx); H = np.zeros((n,n),complex)
    for c, dyn, th in pl:
        w = 1.0 if only_time else c
        for (a,sa,ra) in dyn:
            for (b,sb,rb) in dyn:
                ph = np.exp(1j*sum(p[i]*(rb[i]-ra[i]) for i in range(3)))
                H[a,b] += w*sa*sb*ph
    return H, idx, T

def Dblock(R, p, idx, T, zero):
    nw = (T-1) + (1 if zero else 0)   # w(1..T-1) [, t]
    D = np.zeros((len(idx), nw), complex)
    def wcol(x0):
        if x0==0: return None
        if x0==T: return (T-1) if zero else None
        return x0-1
    for (x0,mu),a in idx.items():
        if mu==0:
            c0, c1 = wcol(x0), wcol(x0+1)
            if c0 is not None: D[a,c0] += 1
            if c1 is not None: D[a,c1] -= 1
        else:
            c0 = wcol(x0)
            D[a,c0] += 1 - np.exp(1j*p[mu-1])
    return D

def gamma1_and_trace(R, eta, want_trace=False):
    ps = [2*math.pi*n/R for n in range(R)]
    g = 0.0; tr = 0.0; stats = dict(herm=0,hd=0,pd=0,nb=0,maxhd=0.0,minev=1e9,maxherm=0.0)
    for n in itertools.product(range(R),repeat=3):
        p = [ps[i] for i in n]; zero = (n==(0,0,0))
        H, idx, T = Hblock(R, eta, p)
        D = Dblock(R, p, idx, T, zero)
        A = H + D@D.conj().T
        s, ld = np.linalg.slogdet(A); 
        _, ldD = np.linalg.slogdet(D.conj().T@D)
        g += 0.5*ld - ldD
        stats['nb']+=1
        e = np.abs(H-H.conj().T).max(); stats['maxherm']=max(stats['maxherm'],e); stats['herm']+= e<1e-12
        h = np.abs(H@D).max(); stats['maxhd']=max(stats['maxhd'],h); stats['hd']+= h<1e-10
        ev = np.linalg.eigvalsh((A+A.conj().T)/2).min(); stats['minev']=min(stats['minev'],ev); stats['pd']+= ev>1e-10
        if want_trace:
            Ht,_,_ = Hblock(R, eta, p, only_time=True)
            tr += np.trace(np.linalg.solve(A, Ht)).real
    return g, tr, stats

def S0(R, eta):
    pl, idx, T = plaq_list(R, eta)
    return R**3*sum(1-c for c,_,_ in pl)

if __name__=="__main__":
    Rs = [int(a) for a in sys.argv[1:]]
    out = open("results.txt","x")
    def log(s):
        print(s); out.write(s+"\n"); out.flush()
    ctl = open("control.txt").read().strip()
    log(f"P1 control {ctl} {'PASS' if ctl=='0.541196' else 'FAIL'}")
    for R in Rs:
        T = R; Nt = 3*R**3*T
        k = -2*3*R**2*math.sin((math.pi-2*ETA0)/R**2)
        h=1e-5; kfd = (S0(R,ETA0+h)-S0(R,ETA0-h))/(2*h)
        log(f"R={R} P3 k={k:.9f} kFD={kfd:.9f} rel={abs(k-kfd)/abs(k):.2e} {'PASS' if abs(k-kfd)/abs(k)<1e-6 else 'FAIL'}")
        g0, tr, st = gamma1_and_trace(R, ETA0, True)
        ctr = tr/(2*Nt)
        d = []
        for hh in (2e-3, 1e-3):
            gp,_,_ = gamma1_and_trace(R, ETA0+hh); gm,_,_ = gamma1_and_trace(R, ETA0-hh)
            d.append((gp-gm)/(2*hh))
        dr = (4*d[1]-d[0])/3
        cfd = -dr/k
        log(f"R={R} blocks={st['nb']} P2 herm {st['herm']}/{st['nb']} (max {st['maxherm']:.1e}); P5 HD {st['hd']}/{st['nb']} (max {st['maxhd']:.1e}); P6 posdef {st['pd']}/{st['nb']} (min ev {st['minev']:.3e})")
        log(f"R={R} Gamma1={g0:.9f} c1_trace={ctr:.9f} c1_FD={cfd:.9f} (h-pair {-d[0]/k:.9f},{-d[1]/k:.9f}) P4 diff={abs(ctr-cfd):.2e} {'PASS' if abs(ctr-cfd)<1e-6 else 'FAIL'}")
        if R in QUOTED:
            dq = ctr-QUOTED[R]
            log(f"R={R} P7 c1={ctr:.7f} quoted={QUOTED[R]:.6f} diff={dq:+.2e} {'PASS' if abs(dq)<=1e-6 else 'FAIL'}")
        else: log(f"R={R} c1={ctr:.7f} (no quoted value)")
