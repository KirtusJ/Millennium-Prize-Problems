"""Free theory, blocking factor 2: checks made after the audit of the version of 24 November (later).
Coordinates: whitened transverse potentials at the eight (seven at k=0) fine momenta of one coarse momentum;
S = diag(1/(2 sinh w_p)) (covariance of a slice, units 1/beta), R = diag(exp(-w_p)) (time step),
Q = projection on the kernel of the coarse observation F (fine detail).
PREDICATES (fixed before the first run):
 M1 for N in {4,8,16,32,64} and every coarse momentum: with fibre covariance Mc = S^(1/2) Q S^(1/2) and
    next-slice covariance Sigma = R (both in units 1/beta, unwhitened coordinates),
    1/(1+||Sigma^(1/2) Mc Sigma^(1/2)||) equals gamma_opt = 1/||Q (I-R^2)^(-1) Q|| to 1e-10.
 M2 (known answer, values reported by a reviewer) at N=64 over all coarse momenta:
    beta*P = 0.567142, beta*L = 0.906562, scalar bound 0.660437, gamma_opt 0.712724, each to 1e-6.
 M3 lambda_max( diag(1/(2 sqrt8), 1/(2 sqrt8), 1/(2 sqrt24)) + v v^T/4 ) = 0.61760078 to 1e-7, with
    v = (sqrt(2/sqrt8), sqrt(2/sqrt8), sqrt(2/sqrt24)); and beta*P at coarse momentum (1,0,0), N = 2^20,
    within 1e-5 of it; scalar bound there within 1e-5 of 1/(1+0.61760078) = 0.6181995.
 M4 for N in {8,16,32,64}: the maximum over coarse momenta of beta*P, and the minimum of gamma_opt, are
    attained at a lowest axial momentum (a permutation of (1,0,0) up to sign), to 1e-12.
 M5 one-particle compressed spectral weight: w(k) = ||Q E_low Q|| with E_low the projection on the low
    alias. For every coarse momentum k != 0 at N in {8,16,32}:
    w(k) <= c sinh(w_k)/(1 + c sinh(w_k)), c = 14/sqrt3 (this follows from the proof of the uniform
    mixing bound), tolerance 1e-10.
 M6 along (1,0,0), N = 2^12 and 2^16: the slope d log w / d log sinh(w_k) between the two sides is within
    0.01 of 1 (the weight is linear in the energy, not of higher order). Basis of the tolerance: the
    corrections are of relative order w_k, which is 1.5e-3 at N = 2^12.
No random numbers. Output matrixbridge_result.txt (not overwritten). Command: python3 matrixbridge.py"""
import numpy as np, itertools
def omega(p): return np.arccosh(1+0.5*sum(4*np.sin(x/2)**2 for x in p))
def islow(p): return all(((x+np.pi/2)%(2*np.pi))<np.pi for x in p)
def blk(N,q):
    k=np.array([2*np.pi*q[i]/N for i in range(3)]); d2=np.exp(2j*k)-1
    PT=None if np.linalg.norm(d2)<1e-11 else np.eye(3)-np.outer(d2,d2.conj())/np.vdot(d2,d2).real
    Fs=[];Rs=[];cs=[];low=[];wk=None
    for eta in itertools.product(range(2),repeat=3):
        p=k+np.pi*np.array(eta)
        if all(abs(np.sin(x/2))<1e-12 for x in p): continue
        d=np.exp(1j*p)-1; w=omega(p)
        U,_,_=np.linalg.svd(np.eye(3)-np.outer(d,d.conj())/np.vdot(d,d).real); Bp=U[:,:2]
        D=np.diag(1+np.exp(1j*p))
        Fs.append(np.zeros((3,2),complex) if PT is None else PT@D@Bp/np.sqrt(2*np.sinh(w)))
        Rs+=[np.exp(-w)]*2; cs+=[1/(2*np.sinh(w))]*2; low+=[islow(p)]*2
        if islow(p): wk=w
    F=np.hstack(Fs); Rs=np.array(Rs); cs=np.array(cs); low=np.array(low)
    _,s,Vh=np.linalg.svd(F); rank=int((s>1e-10*max(s.max(),1e-300)).sum()) if s.max()>0 else 0
    ker=Vh[rank:].conj().T; Q=ker@ker.conj().T
    h=lambda A: np.linalg.eigvalsh((A+A.conj().T)/2).max()
    gam=1/h(ker.conj().T@np.diag(1/(1-Rs**2))@ker)
    P=h(ker.conj().T@np.diag(cs)@ker)
    Mc=np.diag(np.sqrt(cs))@Q@np.diag(np.sqrt(cs)); J=h(np.diag(np.sqrt(Rs))@Mc@np.diag(np.sqrt(Rs)))
    wl=h(ker.conj().T@np.diag(low.astype(float))@ker) if low.any() else 0.0
    return gam,P,Rs.max(),1/(1+J),wl,wk
out=[];res={}
for N in (4,8,16,32,64):
    g=np.inf;P=0;L=0;dm=0;gq=[];Pq=[];m5=-np.inf
    for q in itertools.product(range(N//2),repeat=3):
        a,b,c,gm,wl,wk=blk(N,q); dm=max(dm,abs(gm-a)); L=max(L,c)
        if a<g-1e-12: g=a;gq=[q]
        elif abs(a-g)<=1e-12: gq.append(q)
        if b>P+1e-12: P=b;Pq=[q]
        elif abs(b-P)<=1e-12: Pq.append(q)
        if any(q) and wk is not None and N in (8,16,32):
            c1=14/np.sqrt(3)*np.sinh(wk); m5=max(m5,wl-c1/(1+c1))
    res[N]=(g,P,L,dm,gq,Pq,m5)
    out.append("N=%d beta*P=%.6f beta*L=%.6f scalar bound=%.6f gamma_opt=%.6f max|gamma_matrix-gamma_opt|=%.2e argmin gamma %s argmax P %s"%(N,P,L,1/(1+P*L),g,dm,gq,Pq))
M1=all(res[N][3]<1e-10 for N in res)
g,P,L=res[64][:3]
M2=abs(P-0.567142)<1e-6 and abs(L-0.906562)<1e-6 and abs(1/(1+P*L)-0.660437)<1e-6 and abs(g-0.712724)<1e-6
v=np.array([np.sqrt(2/np.sqrt(8)),np.sqrt(2/np.sqrt(8)),np.sqrt(2/np.sqrt(24))])
lam=np.linalg.eigvalsh(np.diag([1/(2*np.sqrt(8)),1/(2*np.sqrt(8)),1/(2*np.sqrt(24))])+np.outer(v,v)/4).max()
a,b,c,gm,wl,wk=blk(2**20,(1,0,0))
out.append("axial limit matrix: lambda_max=%.9f ; N=2^20 (1,0,0): beta*P=%.9f beta*L(this momentum)=%.9f scalar bound=%.7f gamma_opt=%.7f"%(lam,b,c,1/(1+b*c),a))
M3=abs(lam-0.61760078)<1e-7 and abs(b-lam)<1e-5 and abs(1/(1+b*c)-0.6181995)<1e-5
lowest=lambda q: sorted(q)==[0,0,1]
M4=all(any(lowest(q) for q in res[N][4]) and any(lowest(q) for q in res[N][5]) for N in (8,16,32,64))
M5=all(res[N][6]<=1e-10 for N in (8,16,32))
out.append("M5 worst excess of w(k) over c sinh/(1+c sinh): "+" ".join("N=%d %.3e"%(N,res[N][6]) for N in (8,16,32)))
pts=[]
for e in (4,8,12,16):
    a,b,c,gm,wl,wk=blk(2**e,(1,0,0)); pts.append((np.sinh(wk),wl))
    out.append("(1,0,0) N=2^%d sinh(w_k)=%.6e one-particle weight w=%.6e ratio=%.6f"%(e,np.sinh(wk),wl,wl/np.sinh(wk)))
slope=np.log(pts[3][1]/pts[2][1])/np.log(pts[3][0]/pts[2][0]); out.append("slope between 2^12 and 2^16: %.6f"%slope)
M6=abs(slope-1)<0.01
for n,m in zip("M1 M2 M3 M4 M5 M6".split(),(M1,M2,M3,M4,M5,M6)): out.append("%s %s"%(n,"MET" if m else "FAILED"))
open('matrixbridge_result.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
