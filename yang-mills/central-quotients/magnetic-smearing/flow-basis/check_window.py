"""Conditional energy-window fraction after fixing external momentum and the flow variable."""
from math import sqrt
from scipy.integrate import quad
from scipy.optimize import minimize_scalar


def weight(q,z,k):
    E = sqrt(q-z*z)
    return ((E*E-k*k)**2+(k*k-z*z)**2)/E


def integral(q,k,low,high):
    return quad(lambda z:weight(q,z,k),low,high,epsabs=2e-13,epsrel=2e-13)[0]


def fraction(q,k,E,delta):
    limit = min(k,sqrt(max(0,q-k*k)))
    low = min(limit,sqrt(max(0,q-(E+delta)**2)))
    high = min(limit,sqrt(max(0,q-E*E)))
    return integral(q,k,low,high)/integral(q,k,0,limit)


if __name__=="__main__":
    k, E = 1.,2.
    den = integral(E**2,k,0,min(k,sqrt(E**2-k*k)))
    constant = weight(E**2,0,k)*sqrt(2*E)/den
    print(f"Predicted sup / sqrt(delta) -> {constant:.12g}")
    for d in (0.05,0.01,0.001,0.0001,0.000001):
        breaks=sorted({E**2,(E+d)**2,E**2+k*k,(E+d)**2+k*k})
        best=max(fraction(q,k,E,d) for q in breaks)
        for a,b in zip(breaks,breaks[1:]):
            estimate=minimize_scalar(lambda q:-fraction(q,k,E,d),bounds=(a,b),method="bounded")
            best=max(best,-estimate.fun)
        print(f"width={d:g}, computed supremum={best:.10g}, ratio={best/sqrt(d):.10g}")
    assert abs(best/sqrt(d)/constant-1)<2e-5
