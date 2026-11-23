"""Check the walk clock by Bessel quadrature, a killed tridiagonal walk and cap inequalities."""
import math
from scipy.integrate import quad
from scipy.linalg import solve_banded
from scipy.special import ive
import numpy as np


def root(lam):
    return 2/(2+lam+math.sqrt(lam*(lam+4)))


def density(u,n):
    return n*ive(n,2*u)/u if u else float(n==1)


def run():
    for n in (1,2,4,8):
        # u=y/(1-y)^2 removes the inverse-square-root tail in the mass integral.
        def mass(y):
            if y==1:
                return n/math.sqrt(math.pi)
            u=y/(1-y)**2
            if u>1e6:
                # First two terms of exp(-z) I_n(z); this branch is a numerical control.
                return n*(1+y)/(math.sqrt(4*math.pi)*y**1.5)*(1-(4*n*n-1)/(16*u))
            return density(u,n)*(1+y)/(1-y)**3
        norm=quad(mass,0,1,epsabs=1e-12)[0]
        assert abs(norm-1)<2e-10
        for lam in (0.1,1.,4.,12.):
            expected=root(lam)**n
            actual=quad(lambda u: math.exp(-lam*u)*density(u,n),0,np.inf,
                        epsabs=1e-17,epsrel=1e-10)[0]
            # Walk starts distance n from absorbing zero. At the distant endpoint impose killing.
            size=160
            mat=np.zeros((3,size))
            mat[0,1:]=mat[2,:-1]=-1
            mat[1,:]=2+lam
            rhs=np.zeros(size)
            rhs[0]=1
            killed=solve_banded((1,1),mat,rhs)[n-1]
            assert abs(actual/expected-1)<2e-9 and abs(killed/expected-1)<1e-12
        print(f"n={n}: integrated probability {norm:.12g}, four transforms agree")
    n=2
    for U in (16,64,256,1024):
        x=1/(16*max(U,n*n))
        A=1+math.exp(-x*U)
        deficit=lambda t:-math.expm1(-2*n*math.asinh(math.sqrt(t)/2))
        cert=(A*deficit(x)-deficit(2*x))/(A+1)
        tail=1-quad(lambda u:density(u,n),0,U,epsabs=1e-13)[0]
        assert cert>=min(1,n/math.sqrt(U))/64
        print(f"U={U}: lower bound {cert:.9g}, tail upper {tail:.9g}, scaled {cert*math.sqrt(U)/n:.6g}/{tail*math.sqrt(U)/n:.6g}")


if __name__=="__main__":
    run()
