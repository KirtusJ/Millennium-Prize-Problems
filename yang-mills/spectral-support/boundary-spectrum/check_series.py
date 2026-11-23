"""Rational bounds on the flat-side trial using closed walks on the square lattice."""
from fractions import Fraction as F
from math import comb


def main():
    r=F(16,25)
    terms=[F(comb(2*k,k)**2,5**(2*k+1)) for k in range(17)]
    mu_upper=sum(terms)+r**17/(5*(1-r))
    nu_lower=sum((2*k+1)*t/5 for k,t in enumerate(terms))
    assert mu_upper < F(25433,100000) and nu_lower > F(9024,100000)
    m=2048
    limit=6*(34-20*mu_upper+4*nu_lower)/43
    q=6*(34-F(18,m)-20*(mu_upper+F(2,m))+4*nu_lower)/(43-F(18,m))
    assert limit>F(40848,10000) and q>F(40816,10000)
    print('closed-walk bounds: mean Green <',mu_upper,'second moment >',nu_lower)
    print('limiting surface quotient >',float(limit),'2048-square quotient >',float(q))


if __name__=='__main__':
    main()
