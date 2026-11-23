"""T100 Monte Carlo: 1 site, 3 dirs, SU(2), periodic time T, Wilson action, gauge W(t)=1 for t<T-1, W(T-1) dynamic.
Usage: python3 mc3.py <beta> <nrep> <therm> <sweeps> <outfile>
Metropolis (symmetric left-multiplication by small random SU(2) element, Haar-reversible), parity-in-t updates.
Operators per slice: A=Q1-Q2, B=Q1+Q2-2Q3 (2-fold), S=Q1+Q2+Q3. Q_i=(Re u_i0)^2 (quaternion real part = 1/2 Tr).
Connected correlators C(tau)=<O(t)O(t+tau)>-<O>^2, jackknife over replicas (independent chains, seeds fixed).

PREDICATES (fixed before first run):
 P1 [beta=0 known answer] <Q_i> = 1/4 (Haar, E[(TrU)^2]=1): |mean Q - 0.25| < 5 sigma_jackknife (5 sigma: 1e-6 false alarm).
 P2 [beta=0] connected C_S(tau=1) consistent with 0 within 5 sigma.
 P3 acceptance rate of U updates in [0.2,0.8] (rule-of-thumb for Metropolis efficiency; MEASURED ONLY, not pass/fail of physics).
 P4 [beta=2] C_AA(tau) >0 for tau=1..3 (spectral positivity of a reflection-positive correlator).
 P5 [beta=2] degeneracy: |m_A(tau)-m_B(tau)| < 3 sigma_diff at tau=1,2 (3 sigma conventional).
 P6 [beta=2] cross <AB>_conn(tau=1) consistent with 0 within 3 sigma (2-fold irrep: A,B orthogonal).
 P7 [beta=2] plateau: exists tau<=3 with |m(tau)-m(tau+1)| < 2 sigma_diff for the 2-fold channel (C_AA+C_BB)/2; m_e = m at smallest such tau.
 P8 [beta=2] expectation: m_2fold < m_S (lowest level is the 2-fold) at tau=2 by >2 sigma_diff. (own expectation from task text)
"""
import sys, json, numpy as np
beta=float(sys.argv[1]); R=int(sys.argv[2]); therm=int(sys.argv[3]); sweeps=int(sys.argv[4]); out=sys.argv[5]
T=16; EPS=0.6
rng=np.random.default_rng(12345+int(beta*1000))
def conj(q): return q*np.array([1,-1,-1,-1.])
def qmul(a,b):
    a0,a1,a2,a3=[a[...,k] for k in range(4)]; b0,b1,b2,b3=[b[...,k] for k in range(4)]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0],-1)
def rnd(shape,eps):
    n=rng.normal(size=shape+(3,)); q=np.concatenate([np.ones(shape+(1,)),eps*n],-1)
    return q/np.linalg.norm(q,axis=-1,keepdims=True)
def haar(shape):
    q=rng.normal(size=shape+(4,)); return q/np.linalg.norm(q,axis=-1,keepdims=True)
def re4(a,b,c,d): return qmul(qmul(a,b),qmul(conj(c),conj(d)))[...,0]
U=haar((R,T,3)); W=np.zeros((R,T,4)); W[...,0]=1
def eloc(u,i,tt):
    e=0
    for j in range(3):
        if j!=i: e=e+1-re4(u,U[:,tt,j],u,U[:,tt,j])
    e=e+1-re4(u,W[:,tt],U[:,(tt+1)%T,i],W[:,tt])
    e=e+1-re4(U[:,(tt-1)%T,i],W[:,(tt-1)%T],u,W[:,(tt-1)%T])
    return beta*e
acc=[0,0]
def sweep():
    for par in (0,1):
        tt=np.arange(par,T,2)
        for i in range(3):
            u=U[:,tt,i]; new=qmul(rnd(u.shape[:-1],EPS),u)
            dE=eloc(new,i,tt)-eloc(u,i,tt)
            ok=rng.random(dE.shape)<np.exp(-dE)
            U[:,tt,i]=np.where(ok[...,None],new,u); acc[0]+=ok.sum(); acc[1]+=ok.size
    w=W[:,T-1]; new=qmul(rnd((R,),EPS),w)
    def ew(x): return beta*sum(1-re4(U[:,T-1,i],x,U[:,0,i],x) for i in range(3))
    ok=rng.random(R)<np.exp(-(ew(new)-ew(w))); W[:,T-1]=np.where(ok[:,None],new,w)
for _ in range(therm): sweep()
acc=[0,0]
H=T//2+1
sO=np.zeros((R,3)); sOO=np.zeros((R,3,3,H)); n=0  # ops A,B,S
for s in range(sweeps):
    sweep()
    Q=U[...,0]**2
    O=np.stack([Q[...,0]-Q[...,1],Q[...,0]+Q[...,1]-2*Q[...,2],Q.sum(-1)],-1)  # R,T,3
    sO+=O.mean(1)
    for tau in range(H):
        sOO[:,:,:,tau]+=np.einsum('rta,rtb->rab',O,np.roll(O,-tau,1))/T
    n+=1
sO/=n; sOO/=n
meanQ=np.array([ (U[...,0]**2).mean() ])
with open(out,"x") as f:
    json.dump(dict(beta=beta,R=R,T=T,sweeps=sweeps,therm=therm,acc=acc[0]/acc[1],sO=sO.tolist(),sOO=sOO.tolist()),f)
print("done acc",acc[0]/acc[1])
