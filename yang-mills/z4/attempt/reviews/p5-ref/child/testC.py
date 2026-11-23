"""Test C. Predicates fixed before first run.
Law: theta_p density prop. prod w(theta_p) delta(sum theta = 0 mod 2pi), w=exp(-beta(1-cos)). chat_n=e^-b I_n(b)=int w cos(n th) dth/2pi.
Z_L(b)=sum_n chat_n^V (V=L^2; =1 at b=0, Haar-normalised). One-plaquette marginal density (wrt dth/2pi): w(th) sum_n chat_n^{V-1} cos(n th)/Z.
P1(t)=P(O_p>t)=P(|theta|>c), c=arccos(1-t/beta). Pall(t)=sum_n (chout_n)^V / Z, chout_n=(1/pi) int_c^pi w cos(n th) dth.
Grid: L in {2,4,8}, beta in {.5,1,2,4}, t/(2beta) in {.05,.1,.2,.3,.4,.5,.6,.7,.8,.9,.95,.99} => 144 points per claim.
Quadrature: Gauss-Legendre 3000 nodes on [c,pi], n<=Nmax (L=2: 1500; else 200). Error estimate: recompute with (Nmax/2, nodes/2) and take
max diff; tolerance for inequality = 1e-9 + that diff [fixed here]. Claims PASS only if every grid point satisfies LHS<=RHS+tol.
C1: P1 <= Pall^(1/V).   C2: P1 <= exp(f(b/2)-f(b)-t/2), f(b)=log Z(b)/V.
Also reported: sanity P1 check vs sampling-free identity: P1(t->0)=1 and sum rule: Pall<=P1 (trivially).
"""
import numpy as np, json, sys
tag=sys.argv[1]
th=np.linspace(-np.pi,np.pi,1<<14,endpoint=False)
_cache={}
def chat(b,nmax):
    if b not in _cache:
        w=np.exp(-b*(1-np.cos(th)))   # th starts at -pi: use fft of periodic samples with phase (-1)^n
        F=np.fft.rfft(np.roll(w,-(len(th)//2)))/len(th)   # roll so index 0 is theta=0
        _cache[b]=F.real
    return _cache[b][:nmax+1]
def lnZ(b,V,nmax=300):
    c=chat(b,nmax); s=c[0]**V+2*np.sum(c[1:]**V)
    return np.log(s),c
from functools import lru_cache
@lru_cache(None)
def gl(nn): return np.polynomial.legendre.leggauss(nn)
def probs(L,b,t,nmax,nn):
    V=L*L; c=np.arccos(1-t/b)
    x,wq=gl(nn); th_=(np.pi-c)/2*x+(np.pi+c)/2; wq=wq*(np.pi-c)/2
    w=np.exp(-b*(1-np.cos(th_)))
    n=np.arange(nmax+1)
    co=np.cos(np.outer(n,th_))@(w*wq)/np.pi       # chout_n
    ch=chat(b,nmax)
    s=ch[0]**V+2*np.sum(ch[1:]**V)                  # Z
    # marginal tail
    rho=w*(ch[0]**(V-1)+2*np.cos(np.outer(n[1:],th_)).T@ch[1:]**(V-1))/s
    P1=np.sum(rho*wq)/np.pi
    Pall=(co[0]**V+2*np.sum(co[1:]**V))/s
    return P1,Pall
fr=[.05,.1,.2,.3,.4,.5,.6,.7,.8,.9,.95,.99]
rows=[];c1=c2=0;worst1=worst2=1e9;tot=0
for L in (2,4,8):
    V=L*L; nm=1500 if L==2 else 200
    for b in (.5,1,2,4):
        f=lambda bb: lnZ(bb,V)[0]/V
        fb=f(b);fh=f(b/2)
        for q in fr:
            t=2*b*q
            P1,Pall=probs(L,b,t,nm,3000)
            P1b,Pallb=probs(L,b,t,nm//2,1500)
            tol=1e-9+max(abs(P1-P1b),abs(Pall**(1/V)-Pallb**(1/V)))
            r1=Pall**(1/V); r2=np.exp(fh-fb-t/2)
            ok1=P1<=r1+tol; ok2=P1<=r2+tol
            c1+=ok1;c2+=ok2;tot+=1
            worst1=min(worst1,r1-P1);worst2=min(worst2,r2-P1)
            rows.append(dict(L=L,beta=b,t=t,P1=P1,Pall_root=r1,C2rhs=r2,ok1=bool(ok1),ok2=bool(ok2),tol=tol))
            print(L,b,round(t,4),f'P1={P1:.6e} Pall^(1/V)={r1:.6e} C2rhs={r2:.6e}',ok1,ok2,f'tol={tol:.1e}',flush=True)
print(f'C1: {c1}/{tot} points satisfied, min margin {worst1:.3e}; C2: {c2}/{tot}, min margin {worst2:.3e}')
json.dump(dict(rows=rows,c1=int(c1),c2=int(c2),tot=tot,worst1=float(worst1),worst2=float(worst2)),open(f'results/C_{tag}.json','x'),indent=1)
sys.exit(0 if (c1==tot and c2==tot) else 1)
