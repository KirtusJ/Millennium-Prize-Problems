import numpy as np, itertools
print("Tolerance stated before running: rel diff < 1e-10")
ctl=np.sqrt(np.pi)/(640*np.pi**2)
open('control.txt','w').write("%.8f\n"%ctl)
N=8;l=1.0;b=1/N;s=0.005
ns=range(-3,5)
g=lambda u: sum(np.exp(-(u-0.3-m)**2/(2*0.15**2)) for m in range(-2,3))
X=np.array(list(itertools.product(range(N),repeat=3)))  # 512x3
y=X*b
f=np.prod(g(y),axis=1)
K=np.array([n for n in itertools.product(ns,repeat=3) if any(n)])  # 511x3
kv=2*np.pi/l*K
kh=(2/b)*np.sin(kv*b/2); kh2=(kh**2).sum(1); khm=np.sqrt(kh2)
a=(kh[:,0]**2+kh[:,1]**2)/kh2*(khm/2)*np.exp(-2*s*kh2)
# momentum: fhat at actual integer vector n+n' (cached per distinct vector, no reduction)
cache={}
def fhat(q):
    if q not in cache:
        qv=2*np.pi/l*np.array(q)
        cache[q]=b**3*np.sum(f*np.exp(-1j*(y@qv)))
    return cache[q]
tot=0.0
for i in range(511):
    for j in range(511):
        q=tuple(K[i]+K[j])
        tot+=abs(fhat(q))**2*a[i]*a[j]
Cmom=2*tot
# position: D by direct sum
D={}
for d in itertools.product(range(N),repeat=3):
    D[d]=np.sum(np.exp(1j*(kv@(np.array(d)*b)))*a)
Dr=np.array([[D[tuple((X[i]-X[j])%N)] for j in range(512)] for i in range(512)])
Cpos=2*b**6*np.sum(np.outer(f,f)*Dr.real**2)
maxim=np.abs(Dr.imag).max()
rel=abs(Cmom-Cpos)/abs(Cpos)
with open('results.txt','x') as fh:
    fh.write("C_mom=%.17e\nC_pos=%.17e\nrel_diff=%.3e\nmax|Im D|=%.3e\nagree_1e-10=%s\ndistinct q=%d\n"%(Cmom,Cpos,rel,maxim,rel<1e-10,len(cache)))
print(open('results.txt').read())
