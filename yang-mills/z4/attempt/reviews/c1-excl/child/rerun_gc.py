"""SU(2) Wilson gauge theory, periodic 4^5, beta=0.4, heat bath (rejection-sampled a0).

PREDICATES (stated before running):
 P1 control: I2(1)/I1(1) via power series equals independent numerical quadrature
    of <x> with Haar weight sqrt(1-x^2) e^{x}, |diff| < 1e-6.
 P2 sampler check: mean a0 of the single-link sampler at alpha=1 (2e5 draws)
    equals I2(1)/I1(1) within 5 standard errors.
 P3 main: |P - I2(b)/I1(b)| < 5*sigma_stat + 3e-3.
    sigma_stat = binned (bin=10) error of the 100 measurements.
    Tolerance origin: leading strong coupling term u=I2/I1 (~0.0995 at b=0.4);
    corrections start at O(u^5)-ish ~1e-5 times a combinatorial factor
    (5D has many plaquette cubes), guessed up to ~100 -> ~1e-3; 3e-3 chosen
    generously. A 5D bulk-transition region is far away (beta_c~0.8+), so no
    large deviation is expected at beta=0.4.
Note: checkerboard (parity of x) update required since a plaquette holds two mu-links.
Rerun: OMP_NUM_THREADS=1 python3 su2_plaq.py   (result files opened 'x'; delete or change TAG to rerun)
"""
import numpy as np, math, sys
L=4; D=5; BETA=0.4; SEED=12345; NTH=100; NMEAS=100; TAG="parent_rerun"

def bessel_I(n,x):
    return sum((x/2)**(2*m+n)/(math.factorial(m)*math.factorial(m+n)) for m in range(60))
def u_lead(b): return bessel_I(2,b)/bessel_I(1,b)

def qmul(a,b):
    a0,a1=a[...,0],a[...,1:]; b0,b1=b[...,0],b[...,1:]
    v=a0[...,None]*b1+b0[...,None]*a1-np.cross(a1,b1)
    return np.concatenate([(a0*b0-(a1*b1).sum(-1))[...,None],v],-1)
def qd(a):
    r=a.copy(); r[...,1:]*=-1; return r

def sample_a0(alpha,rng):
    """a0 ~ sqrt(1-x^2) exp(alpha x) on [-1,1]; inverse-CDF of exp part + rejection."""
    alpha=np.asarray(alpha,float); out=np.empty(alpha.shape); todo=np.ones(alpha.shape,bool)
    a=np.maximum(alpha,1e-12)
    while todo.any():
        idx=np.nonzero(todo)
        al=a[idx]; r=rng.random(al.shape)
        x=np.log(np.exp(-al)+r*(np.exp(al)-np.exp(-al)))/al
        acc=rng.random(al.shape)<np.sqrt(np.maximum(1-x*x,0))
        sel=tuple(i[acc] for i in idx); out[sel]=x[acc]; todo[sel]=False
    return out

def randunit(shape,rng):
    v=rng.normal(size=shape+(3,)); return v/np.linalg.norm(v,axis=-1,keepdims=True)

def staple(U,mu):
    S=0
    for nu in range(D):
        if nu==mu: continue
        Unu_xm=np.roll(U[nu],-1,axis=mu)           # U_nu(x+mu)
        Umu_xn=np.roll(U[mu],-1,axis=nu)           # U_mu(x+nu)
        f=qmul(qmul(Unu_xm,qd(Umu_xn)),qd(U[nu]))
        Unu_b=np.roll(np.roll(U[nu],-1,axis=mu),1,axis=nu)  # U_nu(x+mu-nu)
        Umu_b=np.roll(U[mu],1,axis=nu)             # U_mu(x-nu)
        Unu_c=np.roll(U[nu],1,axis=nu)             # U_nu(x-nu)
        bk=qmul(qmul(qd(Unu_b),qd(Umu_b)),Unu_c)
        S=S+f+bk
    return S

def sweep(U,beta,rng):
    par=np.indices((L,)*D).sum(0)%2
    for mu in range(D):
        for p in (0,1):
            m=par==p
            V=staple(U,mu)[m]; k=np.linalg.norm(V,axis=-1); V0=V/k[...,None]
            a0=sample_a0(beta*k,rng)
            s=np.sqrt(1-a0*a0)
            W=np.concatenate([a0[...,None],s[...,None]*randunit(a0.shape,rng)],-1)
            U[mu][m]=qmul(W,qd(V0))

def plaq(U):
    tot=0.0;n=0
    for mu in range(D):
        for nu in range(mu+1,D):
            p=qmul(qmul(U[mu],np.roll(U[nu],-1,axis=mu)),qmul(qd(np.roll(U[mu],-1,axis=nu)),qd(U[nu])))
            tot+=p[...,0].sum(); n+=p[...,0].size
    return tot/n

if __name__=="__main__":
    # P1
    xs=np.linspace(-1,1,2000001); w=np.sqrt(1-xs**2)*np.exp(xs)
    quad=np.trapezoid(xs*w,xs)/np.trapezoid(w,xs)
    ctrl=u_lead(1.0); p1=abs(ctrl-quad)<1e-6
    rng=np.random.default_rng(SEED)
    # P2
    d=sample_a0(np.full(200000,1.0),rng); se=d.std()/math.sqrt(d.size)
    p2=abs(d.mean()-ctrl)<5*se
    U=np.zeros((D,)+(L,)*D+(4,)); U[...,0]=1.0
    for _ in range(NTH): sweep(U,BETA,rng)
    meas=[]
    for _ in range(NMEAS):
        sweep(U,BETA,rng); meas.append(plaq(U))
    meas=np.array(meas); P=meas.mean()
    naive=meas.std(ddof=1)/math.sqrt(NMEAS)
    bins=meas.reshape(10,10).mean(1); sig=bins.std(ddof=1)/math.sqrt(10)
    lead=u_lead(BETA); tol=5*sig+3e-3; p3=abs(P-lead)<tol
    out=dict(control=ctrl,quad=quad,p1=p1,sampler_mean=d.mean(),sampler_se=se,p2=p2,P=P,naive_err=naive,binned_err=sig,lead=lead,diff=P-lead,tol=tol,p3=p3)
    with open(f"result_{TAG}.txt","x") as f:
        for k,v in out.items(): f.write(f"{k} = {v}\n")
        f.write("meas = "+" ".join(f"{m:.6f}" for m in meas)+"\n")
    print(out)
