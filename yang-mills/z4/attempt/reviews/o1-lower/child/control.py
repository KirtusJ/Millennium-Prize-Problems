"""Control: c* = int_0^pi sqrt(2 eps(a)) da, eps=2 asinh(sin a).
Predicates (fixed before run): (C1) two independent quadratures (Gauss-Legendre with a=t^2
substitution on [0,pi/2] doubled by symmetry; composite Simpson with a=t^2 split) agree to 1e-9;
(C2) result written with 6 decimals to control.txt (mode 'x')."""
import numpy as np
f=lambda a: np.sqrt(4*np.arcsinh(np.abs(np.sin(a))))
t,w=np.polynomial.legendre.leggauss(300); T=np.sqrt(np.pi/2)
tt=(t+1)/2*T; c1=2*np.sum(w*T/2*f(tt**2)*2*tt)
n=200000; s=np.linspace(0,T,n+1); y=f(s**2)*2*s
c2=2*(T/n/3)*(y[0]+y[-1]+4*y[1:-1:2].sum()+2*y[2:-1:2].sum())
print(c1,c2,abs(c1-c2)); assert abs(c1-c2)<1e-9
with open("control.txt","x") as fh: fh.write("%.6f\n"%c1)
