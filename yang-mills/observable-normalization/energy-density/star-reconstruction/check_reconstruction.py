"""SU(2) one-link Abel inversion, checked against a second geometry and exact series."""
import argparse
from fractions import Fraction
from math import comb, factorial

import numpy as np
from scipy.special import roots_chebyu, roots_legendre, ive


# Fixed quadrature on unweighted Haar. All derivatives use centered cumulants,
# evaluated before taking the combinations in the inverse transform.
z, haar = roots_chebyu(256)
haar *= 2/np.pi
inner, inner_weights = roots_legendre(64)
inner = (inner+1)/2
inner_weights /= 2


def scaled_second(s):
    """exp(-s) A''(s^2), s>0, from one-link Haar moments."""
    D = s[:,None]*(1-z)
    w = haar*np.exp(-D)
    Z = w.sum(axis=1)
    w /= Z[:,None]
    mean_D = (w*D).sum(axis=1)
    centered = D-mean_D[:,None]
    V = (w*centered**2).sum(axis=1)
    k3 = (w*centered**3).sum(axis=1)
    k4 = (w*centered**4).sum(axis=1)-3*V**2
    first = (2*V-k3)/s
    second = (2*V-4*k3+k4)/s**2
    m = 1-mean_D/s
    z2 = (w*z**2).sum(axis=1)
    return Z*((z2*V+2*m*first+second)/4+3*(m*V+first)/(4*s))


def inverse(x):
    x = abs(float(x))
    if x == 0:
        return 0.
    # s=x-v^2 removes the endpoint singularity. After scaling, exp(-v^2)
    # suppresses the omitted tail beyond v=10 at large x.
    end = min(np.sqrt(x),10.)
    v = end*inner
    s = x-v*v
    numerator = 4*s*scaled_second(s)*np.exp(-v*v)
    return 2*x*end*np.dot(inner_weights,numerator/np.sqrt(x+s))/(1+np.exp(-2*x))


def exact_series(order):
    # Coefficients of Z, Z*r^2*(log Z)'', and cosh(x)*h(x) in powers of r^2.
    # The normalized S^3 marginal moment is Catalan(n)/4^n.
    moment = [Fraction(comb(2*n,n),(n+1)*4**n) for n in range(order+1)]
    Z = [moment[n]/factorial(2*n) for n in range(order+1)]
    a = [(2*n)*Z[n] for n in range(order+1)]
    prod = [sum(a[j]*a[n-j] for j in range(n+1)) for n in range(order+1)]
    quotient = []
    for n in range(order+1):
        quotient.append(prod[n]-sum(Z[j]*quotient[n-j] for j in range(1,n+1)))
    return [((2*n)*(2*n-1)*Z[n]-quotient[n])/moment[n] for n in range(order+1)]


def forward(R):
    # Independent polar integration with a Legendre rule in the deficit
    # rather than the semicircle rule used inside the inverse.
    # For large R parameterize y=R(1-cos theta)=t^2; truncate only the tail.
    t,w = roots_legendre(72)
    t = (1+t)*min(np.sqrt(2*R),9.)/2
    y = t*t
    prob = w*t*t*np.sqrt(np.maximum(0.,1-y/(2*R)))*np.exp(-y)
    prob /= prob.sum()
    values = np.array([inverse(R-yy) for yy in y])
    m = ive(2,R)/ive(1,R)
    exact = R*R*(1-m*m-3*m/R)
    calibrated = prob@values
    return calibrated,exact,prob@((values-calibrated)**2)


def main():
    coeff = exact_series(20)
    assert coeff[0]==0 and coeff[1]==1
    for x in (.05,.3,.65,1.):
        truth=sum(float(c)*x**(2*i) for i,c in enumerate(coeff))/np.cosh(x)
        assert abs(inverse(x)-truth)<2e-13
    # Nontrivial even projection of a signed kernel with zero Boltzmann mean.
    x=.82
    p=1/(1+np.exp(-2*x))
    h=inverse(x)
    plus,minus=h+x*np.exp(-x),h-x*np.exp(x)
    assert abs(p*plus+(1-p)*minus-h)<2e-15
    assert abs(p*(plus-h)**2+(1-p)*(minus-h)**2-x*x)<2e-15
    for R in (1.,4.,15.,60.,180.,500.):
        read,truth,noise=forward(R)
        print("R, reconstructed mean, absolute mean error, R^4 variance",R,read,abs(read-truth),R**4*noise)
        # At small R the parameterization has a square-root endpoint. The
        # independent semicircle rule below resolves that endpoint exactly.
        assert abs(read-truth)<7e-6
        if R>=180: assert abs(R**4*noise-27/32)<.08
    zz,ww=roots_chebyu(40)
    for R in (.35,2.,7.):
        proba=ww*np.exp(R*zz)
        proba/=sum(proba)
        read=proba@np.array([inverse(R*t) for t in zz])
        m=ive(2,R)/ive(1,R)
        assert abs(read-R**2*(1-m*m-3*m/R))<5e-12
    for x in (20.,80.,250.,750.):
        error=x*x*(inverse(x)-1.5+.75/x)
        print("x, inverse x^-2 residual",x,error)
        tolerance=1/x if x>80 else .09
        assert abs(error)<tolerance


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--table",help="write a uniform inverse table for check_wilson.cpp")
    args=parser.parse_args()
    if args.table:
        step=.01
        x=step*np.arange(7202)
        h=np.array([inverse(t) for t in x])
        mid=x[:7200:13]+step/2
        error=max(abs(np.interp(mid,x,h)-np.array([inverse(t) for t in mid])))
        assert error<3e-5
        with open(args.table,"w") as out:
            print(step,file=out)
            np.savetxt(out,h)
        print("largest checked midpoint interpolation error",error)
    else:
        main()
