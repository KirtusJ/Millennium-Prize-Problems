import math
from fractions import Fraction
g=0.57721566490153286061
z=1.0
def H(n): return sum(1.0/k for k in range(1,n+1))
def I(nu,z,N=40): return sum((z/2)**(2*k+nu)/(math.factorial(k)*math.factorial(k+nu)) for k in range(N))
I0,I1=I(0,z),I(1,z)
# Method A: series
K0=-(math.log(z/2)+g)*I0+sum((z/2)**(2*k)/math.factorial(k)**2*H(k) for k in range(1,40))
K1=(1/z)+math.log(z/2)*I1-(z/4)*sum((-(-g) if False else 1)*((psi:=0) or 0) for _ in [0]) if False else None
# K1 = 1/z + ln(z/2) I1 - (z/4) sum (psi(k+1)+psi(k+2)) (z^2/4)^k/(k!(k+1)!)
def psi(n): return -g+H(n-1)
K1=1/z+math.log(z/2)*I1-(z/4)*sum((psi(k+1)+psi(k+2))*(z*z/4)**k/(math.factorial(k)*math.factorial(k+1)) for k in range(40))
# Method B: K0 by trapezoid of exp(-z cosh t), then Wronskian
h=1/64;K0q=h*(0.5*math.exp(-z)+sum(math.exp(-z*math.cosh(k*h)) for k in range(1,400)))
K1w=(1/z-I1*K0q)/I0
A=K1/(4*math.pi**2);B=K1w/(4*math.pi**2)
s=f"K0(1) series={K0:.12f} quad={K0q:.12f}\nK1(1) series={K1:.12f} wronskian={K1w:.12f}\nK1/(4pi^2) A={A:.12e} B={B:.12e} diff={A-B:.2e}\n"
print(s)
open('out.txt','x').write(s)
