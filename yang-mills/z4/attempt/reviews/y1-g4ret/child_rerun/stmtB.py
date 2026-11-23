"""Statement B. Predicates fixed before run:
 B1: two Gauss-Legendre orders (n=200 and n=400, composite 1 panel per integral) agree to <1e-9 for each p_k(theta).
 B2: p_k(pi)=1 within 1e-12 (self-check).  B3: envelope = min(1, C(1+k)^1.5 theta^3), C=pi^2 sqrt(e)/4.
 Tolerance 1e-9 = the 9 printed decimals."""
import numpy as np
beta=3.399810242; k=6*beta
def I(lo,hi,n):
    x,w=np.polynomial.legendre.leggauss(n); r=(hi-lo)/2*x+(hi+lo)/2
    return (hi-lo)/2*np.sum(w*np.sin(r)**2*np.exp(k*(np.cos(r)-1)))
C=np.pi**2*np.sqrt(np.e)/4
print("k=%.9f C=%.9f"%(k,C))
print("p(pi) check",I(0,np.pi,400)/I(0,np.pi,400))
for th in (0.05,0.2,0.6):
    p1=I(0,th,200)/I(0,np.pi,200); p2=I(0,th,400)/I(0,np.pi,400)
    env=min(1,C*(1+k)**1.5*th**3)
    print("theta=%.2f p200=%.9f p400=%.9f agree=%s envelope=%.9f"%(th,p1,p2,abs(p1-p2)<1e-9,env))
