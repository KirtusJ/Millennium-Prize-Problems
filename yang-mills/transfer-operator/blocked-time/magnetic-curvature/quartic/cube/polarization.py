"""Two independent cubic polarizations of the strong-coupling susceptibility."""
from itertools import combinations
import sympy as sp

b,q=sp.symbols("b q")
def trunc(expr,var,n):
    return sp.series(expr,var,0,n+1).removeO().expand()

z=sum((b/2)**(2*j)/(sp.factorial(j)*sp.factorial(j+1)) for j in range(6))
single=trunc(sp.log(z),b,10)
u=single.diff(b)
du=u.diff(b)
B=4*q
for k in (3,5,7):
    B-=4*trunc(u.subs(b,B)-q,q,k).coeff(q,k)*q**k
spin_one=trunc(1-4*q/B,q,4)
def H(y):
    return (1+y/q**4)/(1-y/q**4)
h=(1+q**4)/(1-q**4)
J=(H(q**6)+3*H(q**6*spin_one))/4-h
for weights,adjacency,expected6 in [((1,1,1),12,-20984),((1,-1,0),0,13036)]:
    norm=sp.Rational(3,sum(w*w for w in weights))
    pairs=[(i,j,3-i-j) for i,j in combinations(range(3),2)]
    diag=sum(w*w for w in weights)*(2*du**2+2*u*du.diff(b))*u**4
    cross=2*sum(weights[i]*weights[j] for i,j,k in pairs)*(2*u*du)**2*u**2
    v=trunc(4*single.diff(b,2)+sp.Rational(16,3)*norm*(diag+cross),b,6)
    rectangle=sum((4*u*du*w)**2 for w in weights)
    chair=sum((2*u*du*((weights[i]+weights[j])*(1+u**2)+2*weights[k]*u**2))**2
              for i,j,k in pairs)
    skew=(4*u**2*du*sum(weights))**2
    S=sp.Rational(4,3)*norm*(2*rectangle+4*chair+4*skew)
    endpoint=trunc(-sp.log(v),b,6)
    corr=trunc(-S/v**2,b,4)
    c2=-trunc((H(spin_one**4)-2*h+(12+adjacency)*J)/8,q,4)
    isotropic=trunc(c2*B**2+(endpoint.coeff(b,4)+q*q*corr.coeff(b,4))*B**4
                    +endpoint.coeff(b,6)*B**6,q,6)
    print(weights,endpoint,corr,isotropic)
    assert isotropic.coeff(q,6)==sp.Rational(expected6,405)
