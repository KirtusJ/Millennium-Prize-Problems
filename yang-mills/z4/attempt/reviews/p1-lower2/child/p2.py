"""P1 and P2 predicates (see mc.py docstring). Writes checks.txt (mode x)."""
import numpy as np
from mc import sample_g
x,w=np.polynomial.legendre.leggauss(800); u=(x+1)/2; a=np.pi*u**2*(3-2*u); da=np.pi*(6*u-6*u**2)
c=((np.sqrt(4*np.arcsinh(np.sin(a)))*da)*w).sum()/2
ok1=('%.6g'%c)==open('control.txt').read().strip()
beta=256.; N=200000
g,t=sample_g(np.random.default_rng(777),beta,N); cs=1-t
m=cs.mean(); se=cs.std(ddof=1)/np.sqrt(N)
# exact: density ~ exp(beta(c-1)) sqrt(1-c^2) ; c=cos th, integrate in th: weight sin^2 th
th=np.pi*(1-np.cos(np.pi*(x+1)/2))/2*0+ (np.pi*u**2*(3-2*u)); dth=np.pi*(6*u-6*u**2)
wt=np.exp(beta*(np.cos(th)-1))*np.sin(th)**2*dth*w
ex=(wt*np.cos(th)).sum()/wt.sum()
ok2=abs(m-ex)<=4*se
with open('checks.txt','x') as f:
    f.write(f"P1 control recomputed {c:.9g} file {open('control.txt').read().strip()} met={ok1}\nP2 mean={m:.6f} exact={ex:.6f} SE={se:.2e} z={(m-ex)/se:.2f} met={ok2}\n")
print(open('checks.txt').read())
