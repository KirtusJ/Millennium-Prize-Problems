"""MC of -log R(x) for Wilson-kernel transfer operator on SU(2)^2.
Predicates fixed BEFORE first run:
 P1 control.txt == 4.60541 recomputed with 800-pt GL (6 sig. digits).
 P2 sampler: mean cos(theta) at beta=256, 2e5 draws, within 4 SE of the numerically integrated
    Haar-density mean (4 SE: ~6e-5 normal false alarm).
 P3 (per point, 36 cases; hypothesis 'ESS>=1000' tested first, count reported): |diff| <= 5*SE + 2/sqrt(beta).
    5*SE: statistical; the constant 2 in 2/sqrt(beta) is MY OWN expectation (no derivation) for the O(beta^-1/2) correction.
 P4 boundedness: max_points sqrt(b)|diff| at beta=4096 <= 1.5 * max at beta=256 + 3*SE-scaled slack (1.5 is my own choice).
 P5 ESS of weights >= 1000 for each point (importance weights exp(logw)).
Measured only: the table values. Seed fixed 20260001+index. Output files mode 'x'."""
import numpy as np, sys
N=400000; CH=100000
def qmul(a,b):
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
            a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
def sample_g(rng,beta,n):
    out=[]; m=0
    while m<n:
        t=rng.gamma(1.5,1/beta,size=2*n)
        ok=(t<2)&(rng.random(2*n)<np.sqrt(np.clip(1-t/2,0,1)))
        t=t[ok]; out.append(t); m+=len(t)
    t=np.concatenate(out)[:n]; c=1-t; s=np.sqrt(np.clip(1-c*c,0,None))
    z=rng.normal(size=(3,n)); z/=np.linalg.norm(z,axis=0)
    return (c,s*z[0],s*z[1],s*z[2]), t
GX,GW=np.polynomial.legendre.leggauss(32)
def dPsi(a0,a1):  # Psi(a1)-Psi(a0), vectorised, integrand sqrt(2*eps(sin t))
    mid=(a0+a1)/2; h=(a1-a0)/2
    T=mid[:,None]+h[:,None]*GX[None,:]
    f=np.sqrt(4*np.arcsinh(np.abs(np.sin(T))))
    return h*(f*GW).sum(1)
def eps(s): return 2*np.arcsinh(s)
def alpha(S): return 2*S*np.sqrt(1+S*S)
def cross2(x):
    U1=x[0];U2=x[1]
    u=np.array(U1[1:]);v=np.array(U2[1:])
    return np.cross(u,v,axis=0)
def point(beta,a1,c,y,seed):
    rng=np.random.default_rng(seed)
    d=y/np.sqrt(beta); r=np.hypot(c,d)
    U1=(np.cos(a1),0.,0.,np.sin(a1))
    U2=(1.,0.,0.,0.) if r==0 else (np.cos(r),np.sin(r)*d/r,0.,np.sin(r)*c/r)
    # note exp(c e3 + d e1): vector (d,0,c)
    def stats(U1,U2):
        a1_=np.arccos(np.clip(U1[0],-1,1)); a2_=np.arccos(np.clip(U2[0],-1,1))
        u=np.stack([np.asarray(U1[1])+0*U1[0],np.asarray(U1[2])+0*U1[0],np.asarray(U1[3])+0*U1[0]])
        v=np.stack([np.asarray(U2[1])+0*U2[0],np.asarray(U2[2])+0*U2[0],np.asarray(U2[3])+0*U2[0]])
        cr=np.cross(u,v,axis=0); cc=(cr**2).sum(0)
        S2=np.sin(a1_)**2+np.sin(a2_)**2
        return a1_,a2_,cc,S2
    a1_0,a2_0,cc0,S20=stats(tuple(np.array([z]) for z in U1),tuple(np.array([z]) for z in U2))
    a1_0,a2_0,cc0,S20=[float(z[0]) for z in (a1_0,a2_0,cc0,S20)]
    V0=2*beta*cc0; S0=np.sqrt(S20); q0=cc0/S20
    logphi0_tail=beta*alpha(S0)*q0/2
    lw=[]
    for _ in range(N//CH):
        g1,_t=sample_g(rng,beta,CH); g2,_t=sample_g(rng,beta,CH)
        V1=tuple(np.full(CH,z) for z in U1); V2=tuple(np.full(CH,z) for z in U2)
        W1=qmul(V1,g1); W2=qmul(V2,g2)
        a1p,a2p,cc,S2=stats(W1,W2)
        S2=np.maximum(S2,1e-300); S=np.sqrt(S2); q=cc/S2
        l=-beta*cc - np.sqrt(beta)*dPsi(np.full(CH,a1_0),a1p) - beta*alpha(S)*q/2 + logphi0_tail
        lw.append(l)
    l=np.concatenate(lw); m=l.max(); w=np.exp(l-m)
    mean=w.mean(); logR=-V0/2+m+np.log(mean)
    se=w.std(ddof=1)/(mean*np.sqrt(len(w)))
    ess=w.sum()**2/(w**2).sum()
    pred=eps(S0)-eps(np.sin(a1_0))
    return -logR,pred,se,ess
if __name__=="__main__":
    out=open("results.csv","x"); out.write("beta,a1,c,y,mlogR,pred,diff,sqrtb_diff,SE,ESS\n")
    k=0
    for beta in (256,1024,4096):
        for a1 in (0.5,np.pi/2,2.5):
            for c in (0,0.1):
                for y in (0,1):
                    k+=1
                    m,p,se,ess=point(beta,a1,c,y,20260000+k)
                    out.write(f"{beta},{a1:.6f},{c},{y},{m:.6f},{p:.6f},{m-p:.6f},{np.sqrt(beta)*(m-p):.4f},{se:.6f},{ess:.0f}\n"); out.flush()
