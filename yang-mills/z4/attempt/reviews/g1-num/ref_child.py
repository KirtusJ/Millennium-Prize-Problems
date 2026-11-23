"""ref_child.py: reference numbers for the child's tasks, computed before the child runs.
Predicates: none (measured only); used to grade the child.
I_n(b) = (1/pi) int_0^pi exp(b cos t) cos(n t) dt, trapezoid with 4000 points (periodic analytic integrand: error ~1e-16).
A = int dU1 dU2 chi_1(U1) chi_1(U2) (1/2)Tr(U1U2U1^-1U2^-1)  (Haar, normalized), chi_1 = 4cos^2 a - 1.
   Using invariant coordinates: measure (2/pi)sin^2 a1 da1 (2/pi) sin^2 a2 da2 (1/2) sin g dg, (1/2)Tr comm = 1 - 2 s1^2 s2^2 sin^2 g.
B = int dU1 dU2 exp(-4 (1 - (1/2)Tr comm)).
"""
import numpy as np
def I(n,b,M=4000):
    t=np.linspace(0,np.pi,M+1); f=np.exp(b*np.cos(t))*np.cos(n*t); w=np.full(M+1,np.pi/M); w[0]=w[-1]=np.pi/(2*M)
    return (f*w).sum()/np.pi
print("I1(1)/I0(1) = %.6f"%(I(1,1)/I(0,1)))
for b in (4.0,16.0):
    for n in (1,2):
        print("beta=%g n=%d -ln(I_n/I_0) = %.12f"%(b,n,-np.log(I(n,b)/I(0,b))))
# quadrature in invariant coords: a uniform midpoint high order, gamma Gauss-Legendre in cos
Na=400; a=(np.arange(Na)+0.5)*np.pi/Na; wa=(2/np.pi)*np.sin(a)**2*np.pi/Na
t,wt=np.polynomial.legendre.leggauss(200); wt=wt/2
s2=np.sin(a)**2; chi=4*np.cos(a)**2-1
A1=(wa*chi*s2).sum(); A=-2*A1**2*(wt*(1-t**2)).sum()
print("A = %.10f"%A)
V=2*4.0*s2[:,None,None]*s2[None,:,None]*(1-t**2)[None,None,:]
B=np.einsum('i,j,k,ijk->',wa,wa,wt,np.exp(-V))
print("B = %.10f"%B)
