"""Step 2: Metropolis MC, 2D U(1), beta=2.3, periodic LxT, T=16, usage: prog2_mc.py L [--dry]
Seed fixed: 1000+L. R=1000 independent replicas (vectorised), hot start, 300 thermalisation sweeps,
NS=2500 measured sweeps, 2 Metropolis hits/link (delta uniform in [-1.2,1.2]). Jackknife over G=20 blocks of replicas
(whole replicas are independent => autocorrelation handled).
Observable p(t)=cos(sum_x theta_x(t,x)); C(t)=mean over t0 of p(t0)p(t0+t mod T).
Exact finite-T reference (my derivation from character expansion, to be tested too):
  C(t)=1/2 sum_n lam_n^(T-t) lam_{n+1}^t / sum_n lam_n^T, lam_n=I_|n|(beta)^L  (n in Z)
Formula: m = -L ln(I1/I0).
Predicates (fixed before first run), tolerance k=3 jackknife sigma (~99.7% Gaussian; G=20 -> t19 ~99.2%):
 P1: for each L and t=1,2,3: |m_eff(t) - m_formula| <= 3 sigma_jk   (6 cases total over L=2,3)
 P2: for each L, t=0..4: |C(t) - C_exact(t)| <= 3 sigma_jk
 P3: plaquette independence (hint): for each L: |<cos p> - a| , |<cos p(t,x) cos p(t+1,x)> - a^2|, |<cos p(t,x) cos p(t,x+1)> - a^2| each <= 3 sigma_jk
 P4: sigma_jk of m_eff(t) must be < 0.25*m_formula at t=1..3 (the test has power; else inconclusive, not a pass)
Result file opened with mode 'x'.
"""
import sys,time,numpy as np
L=int(sys.argv[1]); dry='--dry' in sys.argv
T=16; beta=2.3; R=1000; G=20
NS=20 if dry else 2500; NT=0 if dry else 300
rng=np.random.default_rng(1000+L)
th=rng.uniform(-np.pi,np.pi,(R,T,L,2))
def plaq(t,x): return th[:,t,x,0]+th[:,t,(x+1)%L,1]-th[:,(t+1)%T,x,0]-th[:,t,x,1]
def sweep():
    for t in range(T):
        for x in range(L):
            for mu in (0,1):
                # (plaquette index, sign of link in that plaquette)
                if mu==0: pl=((t,x,1),((t-1)%T,x,-1))
                else: pl=((t,x,-1),(t,(x-1)%L,1))
                for _ in range(2):
                    d=rng.uniform(-1.2,1.2,R)
                    dS=0
                    for (pt,px,s) in pl:
                        p=plaq(pt,px)
                        dS=dS+np.cos(p+s*d)-np.cos(p)
                    acc=np.log(rng.uniform(size=R))<beta*dS
                    th[:,t,x,mu]+=np.where(acc,d,0.0)
def meas():
    p=np.cos(th[:,:,:,0].sum(axis=2))             # R,T
    C=np.stack([ (p*np.roll(p,-k,axis=1)).mean(axis=1) for k in range(9)],axis=1)  # R,9
    cp=np.stack([np.cos(plaq(t,x)) for t in range(T) for x in range(L)],axis=1).reshape(R,T,L)
    m1=cp.mean(axis=(1,2)); At=(cp*np.roll(cp,-1,axis=1)).mean(axis=(1,2)); Ax=(cp*np.roll(cp,-1,axis=2)).mean(axis=(1,2))
    return C,m1,At,Ax
t0=time.time()
for _ in range(NT): sweep()
SC=np.zeros((R,9));S1=np.zeros(R);SA=np.zeros(R);SB=np.zeros(R)
for _ in range(NS):
    sweep(); C,m1,At,Ax=meas(); SC+=C;S1+=m1;SA+=At;SB+=Ax
SC/=NS;S1/=NS;SA/=NS;SB/=NS
if dry: print("time per sweep",(time.time()-t0)/NS); sys.exit()
from numpy import pi
tt=np.linspace(0,pi,400001)
def I(n,x): return np.trapezoid(np.exp(x*np.cos(tt))*np.cos(n*tt),tt)/pi
a=I(1,beta)/I(0,beta); mform=-L*np.log(a)
lam=lambda n: I(abs(n),beta)**L
ns=range(-6,7)
Z=sum(lam(n)**T for n in ns)
Cex=[0.5*sum(lam(n)**(T-t)*lam(n+1)**t for n in ns)/Z for t in range(9)]
bl=SC.reshape(G,R//G,9).mean(axis=1)           # G,9
def jk(f,data):
    n=len(data); est=f(data.mean(axis=0))
    vals=np.array([f(np.delete(data,i,axis=0).mean(axis=0)) for i in range(n)])
    return est,np.sqrt((n-1)/n*((vals-vals.mean())**2).sum())
out=[f"L={L} T={T} beta={beta} R={R} NS={NS} NT={NT} a={a:.8f} m_formula={mform:.6f}"]
P1=[];P2=[];P3=[];P4=[]
for t in range(5):
    e,s=jk(lambda c:c[t],bl); ok=abs(e-Cex[t])<=3*s; P2.append(ok)
    out.append(f"C({t})={e:.6f} +- {s:.6f}  exact={Cex[t]:.6f}  pull={(e-Cex[t])/s:+.2f}  {'ok' if ok else 'FAIL'}")
for t in (1,2,3):
    f=lambda c:np.arccosh((c[t-1]+c[t+1])/(2*c[t]))
    e,s=jk(f,bl); ok=abs(e-mform)<=3*s; P1.append(ok); P4.append(s<0.25*mform)
    ex=np.arccosh((Cex[t-1]+Cex[t+1])/(2*Cex[t]))
    out.append(f"m_eff({t})={e:.5f} +- {s:.5f}  formula={mform:.5f} pull={(e-mform)/s:+.2f} {'ok' if ok else 'FAIL'}  exact-T m_eff={ex:.5f}  sigma<0.25m:{s<0.25*mform}")
for name,arr,ref in (("<cos p>",S1,a),("<cc'>_time",SA,a*a),("<cc'>_space",SB,a*a)):
    d=arr.reshape(G,R//G).mean(axis=1); e=d.mean(); s=d.std(ddof=1)/np.sqrt(G); ok=abs(e-ref)<=3*s; P3.append(ok)
    out.append(f"{name}={e:.6f} +- {s:.6f} ref={ref:.6f} pull={(e-ref)/s:+.2f} {'ok' if ok else 'FAIL'}")
out.append(f"P1 {sum(P1)}/3  P2 {sum(P2)}/5  P3 {sum(P3)}/3  P4 {sum(P4)}/3  runtime {time.time()-t0:.0f}s")
s="\n".join(out); print(s)
with open(f"mc_L{L}.txt","x") as f: f.write(s+"\n")
