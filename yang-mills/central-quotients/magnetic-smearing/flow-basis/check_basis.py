"""Exact coefficient and rational interval checks, with independent continuous quadrature."""
from fractions import Fraction as F
from math import exp, expm1, isqrt, log10, pi, sin, sqrt, asin
from scipy.integrate import quad


def multiply(a,b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out


def coefficients(m):
    # T_m(2x-1) in increasing powers of x.
    prev, cur = [1], [-1,2]
    for _ in range(1,m):
        nxt = multiply([-2,4],cur)
        for i,v in enumerate(prev):
            nxt[i] -= v
        prev, cur = cur, nxt
    numerator = [-v for v in cur]
    numerator[0] += 1
    assert sum(numerator)==0
    partial, divided = 0,[]
    for v in numerator[:-1]:
        partial += v
        divided.append(partial)
    # The omitted denominator (2m^2)^2 cancels in ratios.
    out = multiply(divided,divided)
    assert sum(out)==4*m**4
    assert sum(map(abs,out))==abs(sum((-1)**j*v for j,v in enumerate(out)))
    return out


def half_power(u,j,scale):
    """Integer interval for scale * u^(-j-1/2), for positive rational u."""
    squared = F(scale**2,1) / u**(2*j+1)
    lo = isqrt(squared.numerator//squared.denominator)
    return lo,lo+1


def enclosed(c,power,scale):
    grouped = multiply(c,c)
    N = len(c)-1
    lo = hi = 0
    for n,w in enumerate(grouped):
        u = 1+F(3*n,2*N)   # half the sum of the two physical flow times
        a,b = half_power(u,power,scale)
        lo += min(w*a,w*b)
        hi += max(w*a,w*b)
    assert 0<lo<=hi
    return F(lo,scale),F(hi,scale)


def direct(m):
    N = 2*(m-1)
    def squared(E):
        root = sqrt(-expm1(-3*E*E/(2*N)))
        if root==0:
            return 1.
        return exp(-E*E)*(sin(m*asin(root))/(m*root))**8
    # Fixed quadrature subintervals also resolve the polynomial zeros.
    def moment(j):
        return sum(quad(lambda e: e**(4+j)*squared(e),i/2,(i+1)/2,
                        epsabs=2e-17,epsrel=5e-12)[0] for i in range(28))
    return moment(0),moment(2)


def run():
    print("m, grid clocks, nonzero readings, m<E^2>, log10(chi), relative moment discrepancy")
    for m in (3,4,8,16,32,64,128):
        c=coefficients(m)
        scale=10**(4*m+60)
        lo0,hi0=enclosed(c,2,scale)
        lo2,hi2=enclosed(c,3,scale)
        lo=F(5*m,2)*lo2/hi0
        hi=F(5*m,2)*hi2/lo0
        assert hi-lo < F(1,10**18)
        m0,m2=direct(m)
        ratio=float((lo+hi)/2)
        assert abs(m*m2/m0-ratio)<3e-9
        expected=float(lo0/sum(c)**2)*3*sqrt(pi)/8
        rel=abs(m0/expected-1)
        assert rel<2e-10
        # The conditioning shown here uses numerical fourth roots; the
        # coefficient signs and the second-moment enclosure above use exact arithmetic.
        N=len(c)-1
        l1norm=sum(float(F(abs(v),sum(c)))*(1+3*j/N)**(-1.25) for j,v in enumerate(c))
        chi=l1norm/sqrt(float(lo0/sum(c)**2))
        print(f"{m:3d} {N+1:3d} {sum(v != 0 for v in c):3d} {ratio:.10f} {log10(chi):.6f} {rel:.2g}")
        if m==128:
            assert hi < F(8,3)
    print("limiting m<E^2> for [1,4]: 5/2")


if __name__=="__main__":
    run()
