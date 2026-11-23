"""Formal series for the scalar magnetic response. Run with Python and SymPy."""
import sympy as sp

b, q = sp.symbols("b q")

def trunc(expr, var, degree):
    return sp.series(expr, var, 0, degree+1).removeO().expand()

def derivative_square(loop):
    return trunc(sp.diff(loop,b)**2,b,4)

# Normalized one-link character coefficient from the SU(2) Haar integral.
z = sum((b/2)**(2*j)/(sp.factorial(j)*sp.factorial(j+1)) for j in range(6))
single = trunc(sp.log(z),b,10)
u = sp.diff(single,b)
pressure = trunc(single+sp.Rational(4,3)*u**6,b,8)
v = 4*sp.diff(pressure,b,2)
endpoint = trunc(-sp.log(v),b,6)
rect = 2*u**2
chair = 2*(u**2+u**4)
skew = 4*u**3
score = 4*(2*derivative_square(rect)+4*derivative_square(chair)
           +sp.Rational(4,3)*derivative_square(skew))
correction = trunc(-score/v**2,b,4)
print("endpoint",endpoint)
print("order q^2",correction)
assert endpoint.coeff(b,4)==-sp.Rational(17,384)
assert endpoint.coeff(b,6)==sp.Rational(313,23040)
assert correction.coeff(b,4)==-sp.Rational(5,16)

# Revert u(b) and use Bessel recurrence t=1-4*q/b at equal couplings.
B=4*q
for j in (3,5,7):
    B-=4*trunc(u.subs(b,B)-q,q,j).coeff(q,j)*q**j
t=trunc(1-4*q/B,q,4)
def H(x):
    return (1+x/q**4)/(1-x/q**4)
h=(1+q**4)/(1-q**4)
J=(H(q**6)+3*H(q**6*t))/4-h
c2=-trunc((H(t**4)-2*h+24*J)/8,q,4)
c4=endpoint.coeff(b,4)+q**2*correction.coeff(b,4)
isotropic=trunc(c2*B**2+c4*B**4+endpoint.coeff(b,6)*B**6,q,6)
print("isotropic correction",isotropic)
assert isotropic==2*q**2-sp.Rational(98,3)*q**4-sp.Rational(20984,405)*q**6
