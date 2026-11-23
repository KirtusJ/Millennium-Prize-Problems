"""Control: c* = integral_0^pi sqrt(4 asinh(sin a)) da. Integrand is sqrt(4*asinh(sin a)) for a in[0,pi]; asinh(sin a)>=0 there.
Gauss-Legendre with sqrt endpoint singularity handled by substitution a=t^2 style on each half (symmetric about pi/2)."""
import numpy as np
# integral = 2*int_0^{pi/2}; substitute a = u^2 (pi/2)... use a=(pi/2)*u^2, da=pi*u du, integrand ~ sqrt(a) ~ u -> smooth
def f(a): return np.sqrt(4*np.arcsinh(np.sin(a)))
def val(n):
    x,w=np.polynomial.legendre.leggauss(n); u=(x+1)/2; w=w/2
    a=(np.pi/2)*u**2
    return 2*np.sum(w*f(a)*np.pi*u)
for n in (200,400,800): print(n,repr(val(n)))
with open("control.txt","x") as fh: fh.write("%.7g\n"%val(800))
