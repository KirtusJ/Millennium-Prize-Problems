"""Check of the steps of the proof that, for the twice-averaged block plaquette field (onestep3.py), the constant of
I - P_r <= c_r a H satisfies c_r <= 1056 r for every factor r >= 2 and every side.
Notation: aliases p = k + 2 pi eta / r of the low momentum k in [-pi/r, pi/r)^3; s = multiplier; w = one-particle
energy; rho(k) = sum over eta != 0 of |s_eta|^2 tanh(w_eta/2), divided by |s_0|^2 tanh(w_k/2) w_k.
PREDICATES (fixed before the first run), for r in {2,3,4,6,8}, all coarse momenta k != 0 at N = 8r (r <= 4) or 4r:
 Q1 (identity used) |s_eta|^2 / |s_0|^2 = prod_l (sin(k_l/2)/sin(p_l/2))^4 over the components with k_l != 0 and
    equals 0 if some k_l = 0 with eta_l != 0, to 1e-9 relative.
 Q2 (step) the value c(k) = ||Q w^-1 Q|| at that momentum is at most rho(k) + 1/w(pi/r,0,0), tolerance 1e-9.
 Q3 (bound) rho(k) <= 1055 r.
 Q4 (constants) G0 = pi^8/1536, G1 = (pi/2)^4 (7 zeta(3)/8 + pi^4/48); the combination
    (2/pi)(5/4) [ 6 (G1 + 2 G0) + 12 (G1 H0 + G0 H1 + G0 H0) + 8 (G1 H0^2 + 2 G0 H0 H1) ] with H0 = 1 + G0 - (pi/2)^4,
    H1 = 3 + G1 - 3 (pi/2)^4 is below 1055.
Reported: the largest rho(k)/r found for each r (how lossy the proof is). Output onestep4_result.txt (not overwritten)."""
import numpy as np, itertools
from scipy.special import zeta
def omega(p): return np.arccosh(1+sum(4*np.sin(x/2)**2 for x in p)/2)
S=lambda x,r: sum(np.exp(1j*l*x) for l in range(r))
def one(N,r,q):
    k=np.array([2*np.pi*((q[i]+N//(2*r))%(N//r)-N//(2*r))/N for i in range(3)])     # low representative in [-pi/r, pi/r)
    Fs=[];ws=[];num=0;ok=True;s0=None;wk=None
    for eta in itertools.product(range(r),repeat=3):
        p=k+2*np.pi*np.array(eta)/r; d=np.exp(1j*p)-1; w=omega(p)
        U,_,_=np.linalg.svd(np.eye(3)-np.outer(d,d.conj())/np.vdot(d,d).real); Bp=U[:,:2]
        s=np.prod([S(x,r)**2/r for x in p])/r
        curl=np.array([[0,-d[2],d[1]],[d[2],0,-d[0]],[-d[1],d[0],0]])
        Fs.append(s*curl@Bp/np.sqrt(2*np.sinh(w))); ws+=[w]*2
        if not any(eta): s0=abs(s)**2; wk=w
        else: num+=abs(s)**2*np.tanh(w/2)
    for eta in itertools.product(range(r),repeat=3):
        if not any(eta): continue
        p=k+2*np.pi*np.array(eta)/r; s=np.prod([S(x,r)**2/r for x in p])/r
        pred=1.0
        for l in range(3):
            if abs(k[l])<1e-13: pred*= (0.0 if eta[l] else 1.0)
            else: pred*=(np.sin(k[l]/2)/np.sin(p[l]/2))**4
        ok&=abs(abs(s)**2/s0-pred)<=1e-9*max(1,pred)
    rho=num/(s0*np.tanh(wk/2)*wk)
    F=np.hstack(Fs); ws=np.array(ws)
    _,sv,Vh=np.linalg.svd(F); rank=int((sv>1e-10*max(sv.max(),1e-300)).sum())
    ker=Vh[rank:].conj().T; T=ker.conj().T@(ker/ws[:,None]); c=np.linalg.eigvalsh((T+T.conj().T)/2).max()
    return ok,rho,c
out=[]; Q1=Q2=Q3=True
for r in (2,3,4,6,8):
    N=8*r if r<=4 else 4*r; wedge=omega((np.pi/r,0,0)); big=0; worst2=-np.inf
    for q in itertools.product(range(N//r),repeat=3):
        if not any(q): continue
        ok,rho,c=one(N,r,q); Q1&=ok; Q2&=c<=rho+1/wedge+1e-9; Q3&=rho<=1055*r; big=max(big,rho/r); worst2=max(worst2,c-rho-1/wedge)
    out.append("r=%d N=%d: largest rho(k)/r = %.6f ; largest c(k) - rho(k) - 1/w(pi/r) = %.3e"%(r,N,big,worst2))
G0=np.pi**8/1536; G1=(np.pi/2)**4*(7*zeta(3)/8+np.pi**4/48); g1=(np.pi/2)**4; H0=1+G0-g1; H1=3+G1-3*g1
tot=(2/np.pi)*(5/4)*(6*(G1+2*G0)+12*(G1*H0+G0*H1+G0*H0)+8*(G1*H0**2+2*G0*H0*H1)); Q4=tot<1055
chk0=abs(sum((np.pi/(4*j-2))**4 for j in range(1,200000))-G0)<1e-9; chk1=abs(sum((2*j+1)*(np.pi/(4*j-2))**4 for j in range(1,2000000))-G1)<1e-5
out.append("G0=%.6f G1=%.6f H0=%.6f H1=%.6f (direct sums agree: %s %s) ; combination = %.3f"%(G0,G1,H0,H1,chk0,chk1,tot))
for n,m in zip(("Q1","Q2","Q3","Q4"),(Q1,Q2,Q3,Q4 and chk0 and chk1)): out.append("%s %s"%(n,"MET" if m else "FAILED"))
open('onestep4_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
