"""PREDICATES (fixed before first run):
P0 control: MC E[(trU)^4] within 4 SE of 2 (SE from sample std/sqrt(N)).
P1 sanity: E[chi_a(U1U2U1^-1U2^-1)] within 4 SE of 1/(2a+1), a=1/2,1. (4 SE: ~6e-5 false-fail rate)
P2 for all 8 (a,b,c) in {1/2,1}^3: sign verdict at 4 SE (pos/neg/zero-compatible); report how many cases are decided.
Tolerance origin: Gaussian CLT standard error, N=4e6 samples, seed 20240601.
Haar SU(2): normalized 4-d Gaussian quaternion; tr = 2*real part; inverse = conjugate."""
import numpy as np, itertools, json
rng=np.random.default_rng(20240601)
N=4_000_000; CH=500_000
def haar(n):
    q=rng.normal(size=(n,4)); return q/np.linalg.norm(q,axis=1,keepdims=True)
def mul(p,q):
    a1,b1,c1,d1=p.T; a2,b2,c2,d2=q.T
    return np.stack([a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2,
                     a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2],1)
def inv(q): return q*np.array([1,-1,-1,-1])
def comm(x,y): return mul(mul(x,y),mul(inv(x),inv(y)))
def chi(j,q):
    t=np.arccos(np.clip(q[:,0],-1,1)); s=np.sin(t)
    k=int(round(2*j+1))
    return np.where(s<1e-12,k*np.cos(t)**(k-1)*np.sign(np.cos(t))**0 if False else k*np.sign(np.cos(t))**(k-1),np.sin(k*t)/np.where(s<1e-12,1,s))
class Acc:
    def __init__(s): s.n=0;s.s=0.;s.s2=0.
    def add(s,x): s.n+=len(x);s.s+=x.sum();s.s2+=(x*x).sum()
    def res(s):
        m=s.s/s.n; se=np.sqrt((s.s2/s.n-m*m)/(s.n-1)); return m,se
acc={k:Acc() for k in itertools.product([.5,1],repeat=3)}
c4=Acc(); san={.5:Acc(),1:Acc()}
for _ in range(N//CH):
    U1,U2,U3=haar(CH),haar(CH),haar(CH)
    c4.add((2*haar(CH)[:,0])**4)
    P12,P13,P23=comm(U1,U2),comm(U1,U3),comm(U2,U3)
    for a in (.5,1): san[a].add(chi(a,P12))
    C={j:(chi(j,P12),chi(j,P13),chi(j,P23)) for j in (.5,1)}
    for (a,b,c),A in acc.items(): A.add(C[a][0]*C[b][1]*C[c][2])
out={}
def verdict(m,se): return "positive" if m>4*se else "negative" if m<-4*se else "compatible with zero"
m,se=c4.res(); out["control_trU4"]=(m,se,abs(m-2)<4*se); print("P0",m,se,abs(m-2)<4*se)
for a,A in san.items():
    m,se=A.res(); ok=abs(m-1/(2*a+1))<4*se; out[f"sanity_{a}"]=(m,se,ok); print("P1",a,m,se,ok)
dec=0
for k,A in acc.items():
    m,se=A.res(); v=verdict(m,se); dec+= v!="compatible with zero"
    out[str(k)]=(m,se,v); print(k,f"{m:.6f} +- {se:.6f}",v)
print("decided",dec,"of 8")
with open("results_v2.json","x") as f: json.dump(out,f,indent=1,default=lambda o: o.item())
