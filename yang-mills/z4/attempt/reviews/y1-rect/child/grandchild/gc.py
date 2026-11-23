"""T198 independent check, 4D SU(2) Wilson, 2^4 periodic. Own code, numpy only.
PASS PREDICATES (fixed before running):
 P1 u(0.5)=I2/I1 from power series, sanity: |u - 0.5/4*(1+...)| not used; just report u,u^2.
 P2 beta=0 Haar: |W11-0| < 4 sigma.
 P3 beta=0 Haar: |W12-0| < 4 sigma (2-step wraps on L=2).
 P4 beta=0.5 MC: |W11-u| < 4 sigma  (informational; 2^4 double covering may legitimately
    break this, a FAIL here is reported, not hidden).
 P5 MC sanity: 0 < W11(0.5) < 0.5 and cold-start vs hot-start means agree within 4 combined sigma.
Seeds fixed. Heatbath: a0=cos(theta), density sin^2(th) exp(lam cos th) via inverse CDF on a 4000 grid.
"""
import numpy as np, math
rng = np.random.default_rng(198)

def bessel(n, x):
    return sum((x/2)**(2*k+n)/(math.factorial(k)*math.factorial(k+n)) for k in range(40))
beta = 0.5
u = bessel(2, beta)/bessel(1, beta)

def qmul(a, b):
    a0,a1,a2,a3 = [a[...,i] for i in range(4)]
    b0,b1,b2,b3 = [b[...,i] for i in range(4)]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3,
                     a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1,
                     a0*b3+a1*b2-a2*b1+a3*b0], -1)
def qd(a): return a*np.array([1,-1,-1,-1.])
def haar(shape):
    q = rng.normal(size=shape+(4,)); return q/np.linalg.norm(q,axis=-1,keepdims=True)
# U shape (B,4,2,2,2,2,4); lattice axis of direction m is 2+m
def sh(A, m, s):  # A at x+s*m, A has shape (B,2,2,2,2,4)
    return np.roll(A, -s, axis=1+m)
def L(U, m): return U[:, m]
def plaq(U, m, n):
    return qmul(qmul(L(U,m), sh(L(U,n),m,1)), qmul(qd(sh(L(U,m),n,1)), qd(L(U,n))))
def w11(U):
    return np.mean([plaq(U,m,n)[...,0].mean(axis=(1,2,3,4)) for m in range(4) for n in range(m+1,4)],axis=0)
def w12(U):
    r=[]
    for m in range(4):
        for n in range(4):
            if m==n: continue
            Um=L(U,m); Un=L(U,n)
            a=qmul(Um, sh(Um,m,1))
            b=qmul(sh(Un,m,2), qd(sh(sh(Um,n,1),m,1)))
            c=qmul(qd(sh(Um,n,1)), qd(Un))
            r.append(qmul(qmul(a,b),c)[...,0].mean(axis=(1,2,3,4)))
    return np.mean(r,axis=0)

# ---- (c) beta=0
N=20000
a11=[];a12=[]
for i in range(10):
    U=haar((N//10,4,2,2,2,2)); a11.append(w11(U)); a12.append(w12(U))
a11=np.concatenate(a11); a12=np.concatenate(a12)
m11,e11=a11.mean(),a11.std(ddof=1)/math.sqrt(N); m12,e12=a12.mean(),a12.std(ddof=1)/math.sqrt(N)

# ---- (b) heatbath
th=np.linspace(0,math.pi,4001)
par=np.indices((2,2,2,2)).sum(0)%2
def staple(U,m):
    S=np.zeros((1,2,2,2,2,4))
    for n in range(4):
        if n==m: continue
        Um=L(U,m);Un=L(U,n)
        S+=qmul(qmul(sh(Un,m,1),qd(sh(Um,n,1))),qd(Un))
        Unb=sh(Un,n,-1)
        S+=qmul(qmul(qd(sh(Unb,m,1)),qd(sh(Um,n,-1))),Unb)
    return S
def sweep(U):
    for m in range(4):
        for p in (0,1):
            S=staple(U,m); k=np.linalg.norm(S,axis=-1)
            sel=(par==p)
            Ss=S[0][sel]; ks=k[0][sel]
            V=Ss/ks[:,None]
            lam=beta*ks
            w=np.sin(th)[None,:]**2*np.exp(lam[:,None]*(np.cos(th)[None,:]-1))
            c=np.cumsum(w,axis=1); c/=c[:,-1:]
            r=rng.random(len(ks))
            t=np.array([np.interp(r[i],c[i],th) for i in range(len(ks))])
            a0=np.cos(t); d=rng.normal(size=(len(ks),3)); d/=np.linalg.norm(d,axis=1,keepdims=True)
            X=np.concatenate([a0[:,None],np.sin(t)[:,None]*d],1)
            Unew=qmul(X,qd(V))
            Um=U[0,m]; Um[sel]=Unew
    return U
def run(U,ns,nt):
    for _ in range(nt): U=sweep(U)
    out=[]
    for _ in range(ns): U=sweep(U); out.append(w11(U)[0])
    return np.array(out)
def binned(x,nb=20):
    b=x[:len(x)//nb*nb].reshape(nb,-1).mean(1); return x.mean(), b.std(ddof=1)/math.sqrt(nb)
ns=4000
hot=run(haar((1,4,2,2,2,2)),ns,300)
cold0=np.zeros((1,4,2,2,2,2,4)); cold0[...,0]=1
cold=run(cold0,ns,300)
mh,eh=binned(hot); mc,ec=binned(cold)
W=np.concatenate([hot,cold]); mW=W.mean(); eW=math.sqrt(eh**2+ec**2)/2

P2=abs(m11)<4*e11; P3=abs(m12)<4*e12
dsig=(mW-u)/eW; P4=abs(dsig)<4
P5=(0<mW<0.5) and abs(mh-mc)<4*math.hypot(eh,ec)
with open("result.md","x") as f:
    f.write(f"""# T198 result
u(0.5)=I2/I1={u:.8f}  u^2={u*u:.8f}
## beta=0.5, 2^4 periodic, heatbath, {ns} sweeps hot + {ns} cold (300 thermalization each), 20 bins
hot  W11={mh:.5f} +- {eh:.5f}
cold W11={mc:.5f} +- {ec:.5f}
combined W11={mW:.5f} +- {eW:.5f}
W11-u = {mW-u:+.5f} = {dsig:+.2f} sigma
## beta=0 Haar, {N} samples
W11={m11:+.5f} +- {e11:.5f}
W12={m12:+.5f} +- {e12:.5f}  (on L=2 the 2-step wraps: U_nu(x+2mu)=U_nu(x), so the nu legs cancel and W12 is a trace of 4 distinct links; expectation still 0)
## predicates
P2 beta=0 W11~0 (4 sigma): {'PASS' if P2 else 'FAIL'}
P3 beta=0 W12~0 (4 sigma): {'PASS' if P3 else 'FAIL'}
P4 beta=0.5 W11==u (4 sigma): {'PASS' if P4 else 'FAIL'}
P5 sanity hot/cold agree, 0<W11<0.5: {'PASS' if P5 else 'FAIL'}
""")
print(open("result.md").read())
