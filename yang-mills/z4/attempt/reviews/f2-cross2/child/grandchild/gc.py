import numpy as np, glob, os
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','data')
x=np.arange(1,6.);m=x.mean()
C=lambda k:np.mean((x-m)*(np.roll(x,-k)-m))
R=1-C(2)/C(0)
open('control.txt','x').write("%.6f\n"%R)
def load(n):
    J=np.zeros((4,4))
    for l in open(f'{D}/chain-{n}.txt'):
        if l.startswith('J,'):
            p=l.strip().split(',');J[int(p[1])]=[float(v) for v in p[2:6]]
    return J
ids=[2,3,6,7,10,11,14,15]
Js={n:load(n) for n in ids}
def mat(J):
    S=(J+J.T)/2;v=S.sum(1);return S/np.sqrt(np.outer(v,v)),v
def l2(J):
    M,v=mat(J);e=np.sort(np.linalg.eigh(M)[0])[::-1]
    # alt: deflation + power iteration on shifted matrix
    u=np.sqrt(v);u/=np.linalg.norm(u);B=M-np.outer(u,u)
    # eigenvalues of B via char poly
    r=np.sort(np.roots(np.poly(M)).real)[::-1]
    return e,r
P=sum(Js.values());e,r=l2(P)
M,v=mat(P);u=np.sqrt(v);u/=np.linalg.norm(u);B=M-np.outer(u,u)
w=np.ones(4)+np.arange(4)*.1;w-=u*(u@w)
for _ in range(100000):
    w=B@w;w/=np.linalg.norm(w)
# power iteration on B+I (shift) to handle sign issues
Bs=B+np.eye(4);w=np.random.default_rng(0).normal(size=4);w-=u*(u@w)
for _ in range(200000):
    w=Bs@w;w/=np.linalg.norm(w)
pw=w@Bs@w-1
out=[f"control R = {R:.6f}","eigh eigenvalues: "+", ".join(repr(float(a)) for a in e),
"charpoly roots: "+", ".join(repr(float(a)) for a in r),
f"lambda2 eigh = {e[1]!r}",f"lambda2 charpoly = {r[1]!r}",f"lambda2 deflated power = {pw!r}",
f"diff eigh-charpoly = {e[1]-r[1]:.3e}; eigh-power = {e[1]-pw:.3e}"]
xs=[]
for n in ids:
    Q=sum(J for k,J in Js.items() if k!=n);a=l2(Q)[0][1];b=l2(Q)[1][1];xs.append(a)
    out.append(f"LOO remove chain-{n}: eigh {a!r} charpoly {b!r}")
xs=np.array(xs);se=np.sqrt(7/8*((xs-xs.mean())**2).sum())
out+= [f"LOO mean {xs.mean()!r}",f"jackknife SE {se!r}"]
s="\n".join(out);print(s)
open('findings.md','x').write("# Findings\n\n```\n"+s+"\n```\n")
