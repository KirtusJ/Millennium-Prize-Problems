import numpy as np, os
d=os.path.dirname(os.path.abspath(__file__))
def G(L,ns):
    k=-np.pi+2*np.pi*(np.arange(L)+0.5)/L
    h=4*np.sin(k/2)**2
    k0=k[:,None,None,None]; c0=h[:,None,None,None]
    h1=h[None,:,None,None]; h2=h[None,None,:,None]; h3=h[None,None,None,:]
    num=h1+h2; den=c0+h1+h2+h3
    f=num/den
    return [float((f*np.cos(n*k0)).mean()) for n in ns]
# control first
c=G(24,[0])[0]
assert abs(c-0.5)<1e-9, c
with open(os.path.join(d,'control.txt'),'x') as f: f.write("G(0) at L=24 = %.15f ; expected 0.5 ; diff %.2e\n"%(c,c-0.5))
r={L:G(L,[0,1,2]) for L in (24,32)}
with open(os.path.join(d,'result.txt'),'x') as f:
    for L in r: f.write("L=%d G0=%.12f G1=%.12f G2=%.12f\n"%((L,)+tuple(r[L])))
    f.write("diff(L32-L24) "+" ".join("G%d=%.3e"%(n,r[32][n]-r[24][n]) for n in range(3))+"\n")
