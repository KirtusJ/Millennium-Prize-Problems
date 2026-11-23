"""T156 Monte Carlo of delta1, delta3. PREDICATES FIXED BEFORE FIRST RUN:
 C0 (qualification, "for all" hypothesis): a case qualifies if mean of the ratio sample is finite and >0
    and SE finite; report count qualified out of 48. Predicates C1,C2 are evaluated on qualified cases only.
 C1: delta1 >= -4/sqrt(beta) - 4*SE   at every point (48 cases). Tolerance 4/sqrt(beta): the claimed O(beta^-1/2) size with
     constant 4 (task's suggestion); 4*SE: 4-sigma Monte Carlo allowance.
 C2: delta3 <=  4/sqrt(beta) + 4*SE   at every point.
 C3: measured only: max over points of sqrt(beta)*|delta1|, |delta3| per beta.
 C4: sampler: |mean Re g - I2(beta)/I1(beta)| <= 4*SE (SE from pair means), per beta. Exact value: density of x0=cos th on S^3
     is prop. exp(beta cos th) sin^2 th; int e^{b cos}sin^2 = pi I1(b)/b, d/db gives pi I2(b)/b, ratio I2/I1.
 Settings: N=200000 antithetic pairs per beta, seed 20261123+beta index; same draws for all 12 points of a beta.
 SE: delta method, SE(log mean)=SE(mean of pair values)/mean (pair value = average of the two antithetic samples).
 Output file written with mode 'x' (never overwritten)."""
import numpy as np, json, sys
def i2i1(b):
    th=np.linspace(0,np.pi,2000001); w=np.exp(b*(np.cos(th)-1))*np.sin(th)**2
    return np.trapezoid(np.cos(th)*w,th)/np.trapezoid(w,th)
N=200000; eta=0.25; th0=0.5; l=0.08
xg,wg=np.polynomial.legendre.leggauss(12)
def eps(s): return 2*np.arcsinh(s)
def Pp(a): return np.sqrt(2*(eps(np.sin(a))+eta))
def Tp(a): return th0*a/np.sqrt(a*a+l*l)
def Th(a): return th0*(np.sqrt(a*a+l*l)-l)
def dPsi(a,b):
    m=(b-a)[:,None]/2*xg[None,:]+(a[:,None]+b[:,None])/2 if np.ndim(a) else None
    return (b-a)/2*(Pp(m)*wg).sum(1)
def sample(rng,beta,n):
    out=np.empty(0)
    while out.size<n:
        t=rng.gamma(1.5,1/beta,int(1.3*(n-out.size))+100)
        acc=(t<2)&(rng.random(t.size)<np.sqrt(np.clip(1-t/2,0,None)))
        out=np.concatenate([out,t[acc]])
    t=out[:n]; v=rng.normal(size=(n,3)); v/=np.linalg.norm(v,axis=1)[:,None]
    return np.column_stack([1-t,np.sqrt(np.clip(1-(1-t)**2,0,None))[:,None]*v]) if False else np.concatenate([(1-t)[:,None],np.sqrt(np.clip(1-(1-t)**2,0,None))[:,None]*v],1)
def qmul(p,q):
    p0=p[...,0];q0=q[...,0];u=p[...,1:];v=q[...,1:]
    return np.concatenate([(p0*q0-(u*v).sum(-1))[...,None],p0[...,None]*v+q0[...,None]*u+np.cross(u,v)],-1)
conj=lambda g: g*np.array([1,-1,-1,-1.])
def ratio_logs(beta,U1,U2,g1,g2):
    sb=np.sqrt(beta)
    x1=qmul(U1,g1);x2=qmul(U2,g2)
    u1=x1[:,1:];u2=x2[:,1:]
    cr=np.cross(u1,u2);q2=(cr**2).sum(1);S2=(u1**2).sum(1)+(u2**2).sum(1)
    S=np.sqrt(S2);V=2*beta*q2;G=-beta*2*S*np.sqrt(1+S2)*q2/S2/2
    a1n=np.arccos(np.clip(x1[:,0],-1,1));a2n=np.arccos(np.clip(x2[:,0],-1,1))
    a1=np.arccos(np.clip(U1[0],-1,1));a2=np.arccos(np.clip(U2[0],-1,1))
    dP=dPsi(np.full(a1n.shape,a1),a1n)
    return -V/2-sb*dP+G, -sb*(Th(a2n)-Th(a2)), G  # base(f3-part, without G0), E-ratio part, G'
def point(a1,c,y,beta):
    d=y/(np.sqrt(beta)*np.sin(a1)); r=np.hypot(c,d)
    U1=np.array([np.cos(a1),0,0,np.sin(a1)])
    U2=np.array([1.,0,0,0]) if r==0 else np.array([np.cos(r),np.sin(r)*d/r,0,np.sin(r)*c/r])
    return U1,U2
def stat(L):  # L shape (2,N): antithetic samples of log-weights -> log mean, SE
    m=L.max(); w=np.exp(L-m).mean(0)   # pair values
    mu=w.mean(); se=w.std(ddof=1)/np.sqrt(w.size)
    return m+np.log(mu), se/mu, mu
res=[];samp=[]
out=open("results_mc2.json","x")
for ib,beta in enumerate([256,1024,4096,16384]):
    rng=np.random.default_rng(20261123+ib)
    g1=sample(rng,beta,N);g2=sample(rng,beta,N)
    x0=np.concatenate([g1[:,0],g2[:,0]]); 
    # pair means for sampler: antithetic partner has same Re, so SE from the 2N iid draws
    ex=i2i1(beta)
    se0=x0.std(ddof=1)/np.sqrt(x0.size)
    samp.append(dict(beta=beta,mean=x0.mean(),exact=ex,se=se0,z=(x0.mean()-ex)/se0))
    for a1 in [0.5,np.pi/2,2.6]:
      for c in [0,0.07]:
        for y in [0,1.5]:
            U1,U2=point(a1,c,y,beta); sb=np.sqrt(beta)
            Lb=[];Le=[]
            for (h1,h2) in [(g1,g2),(conj(g1),conj(g2))]:
                b,e,_=ratio_logs(beta,U1,U2,h1,h2); Lb.append(b);Le.append(b+e)
            L3=np.array(Lb);L1=np.array(Le)
            # point quantities
            x1=U1;x2=U2
            u1=U1[1:];u2=U2[1:];cr=np.cross(u1,u2);q2=cr@cr;S2=u1@u1+u2@u2;S=np.sqrt(S2)
            V=2*beta*q2;G0=-beta*S*np.sqrt(1+S2)*q2/S2
            A1=np.arccos(U1[0]);A2=np.arccos(U2[0])
            base=-V/2-G0   # log[exp(-V/2)/G(x)]; E(x) factor handled: f1(x)=..G E -> -log E0 = +sb*Th(A2)
            res_p={}
            for name,L,extra,pred in [("delta1",L1,0.0,(Pp(A1)**2+Tp(A2)**2)/2),("delta3",L3,0.0,Pp(A1)**2/2)]:
                lm,se,mu=stat(L)
                lr=base+extra+lm
                res_p[name]=lr-(-eps(S)+pred); res_p[name+"_se"]=se; res_p[name+"_mu"]=mu
            res.append(dict(beta=beta,a1=a1,c=c,y=y,**res_p))
json.dump(dict(points=res,sampler=samp),out,default=float,indent=1);out.close()
