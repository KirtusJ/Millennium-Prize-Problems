"""Reread/rerun of grandchild's Schwinger-Bessel check by my own code (grandchild left no script). Predicate: |G1 - 0.0688747458|<1e-8
after Richardson in the cutoff S (tail ~ S^-2, assumed; checked by 3 cutoffs)."""
import numpy as np
N=1<<16; t=(np.arange(N)+.5)*2*np.pi/N
def f(n,s): return np.mean(np.exp(2*s*(np.cos(t)-1))*np.cos(n*t))
x,w=np.polynomial.legendre.leggauss(40)
def I(S):
    e=[0,1]+[1*2**j for j in range(1,40) if 2**j<S]+[S]; e=sorted(set(e)); tot=0
    for a,b in zip(e[:-1],e[1:]):
        for xi,wi in zip(x,w):
            s=a+(b-a)*(xi+1)/2; f0=f(0,s); f1=f(1,s)
            tot+=wi*(b-a)/2*2*2*(f0-f1)*f0**2*f1
    return tot
a,b,c=I(250),I(500),I(1000)
print(a,b,c,"Richardson",c+(c-b)/3, "ratio check",(b-a)/(c-b))
v=c+(c-b)/3
print("G1",v,"diff to 0.0688747458",v-0.0688747458)
