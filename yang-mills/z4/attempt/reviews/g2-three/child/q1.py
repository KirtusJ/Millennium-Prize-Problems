"""Q1. Predicates (fixed before first run):
P1: for beta=2, j=1/2 and 1, quadrature ratio k_j/k_0 equals I_{2j+1}(2)/I_1(2) to abs 1e-10
    (tolerance: 400-pt Gauss-Legendre on an entire periodic-type integrand is ~1e-14; 1e-10 is generous).
P2: -ln(k_1/k_0) printed to 10 digits.
k_j = (1/d_j)(2/pi) int_0^pi exp(beta cos a) sin((2j+1)a) sin(a) da, d_j=2j+1  (Weyl: chi_j=sin((2j+1)a)/sin a)."""
import numpy as np
from math import factorial as f, log
def I(n,x): return sum((x/2)**(2*m+n)/(f(m)*f(m+n)) for m in range(60))
b=2.0
x,w=np.polynomial.legendre.leggauss(400); a=(x+1)*np.pi/2; w=w*np.pi/2
def k(j2):  # j2=2j
    d=j2+1
    return (2/np.pi)*np.sum(w*np.exp(b*np.cos(a))*np.sin(d*a)*np.sin(a))/d
out=[]
ok=True
for j2 in (1,2):
    r=k(j2)/k(0); ex=I(j2+1,b)/I(1,b); p=abs(r-ex)<1e-10; ok&=p
    out.append(f"j={j2/2}: quad ratio {r:.14f} Bessel I_{j2+1}/I_1 {ex:.14f} diff {abs(r-ex):.2e} {'PASS' if p else 'FAIL'}")
r1=k(2)/k(0)
out.append("k_0 quad %.12f vs (2/beta)I_1 %.12f"%(k(0),2/b*I(1,b)))
out.append("-ln(k_1/k_0) at beta=2 = %.10f  (Bessel: %.10f)"%(-log(r1),-log(I(3,b)/I(1,b))))
out.append("P1 "+("PASS" if ok else "FAIL"))
open("q1_result.txt","x").write("\n".join(out)+"\n"); print("\n".join(out))
