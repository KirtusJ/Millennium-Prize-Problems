"""Numerical checks on the analytic, quadratic Wilson transfer. Python 3.10+."""
from itertools import product
from math import asinh, cos, exp, fsum, log, log1p, pi, sin, sinh, sqrt


def modes(length):
    for n in product(range(length), repeat=3):
        if any(n):
            yield [2*pi*(v if v <= length//2 else v-length)/length for v in n]


def symbol(p):
    s = 4*sum(sin(x/2)**2 for x in p)
    return s, 2*asinh(sqrt(s)/2), sqrt(s+s*s/4)


def shifted(p, ang, length):
    return [v+u/length for v, u in zip(p, ang)]


def widths(a, b):
    r = log(b/a)/2
    return 2*log1p(2*sinh(r/2)**2)  # two charged polarizations, overlap amplitude


def values(length, alpha, delta):
    energy, amplitude, dressed, central, curvature, metric = [], [], [], [], [], []
    for p in modes(length):
        s, _, a = symbol(p)
        _, w, b = symbol(shifted(p, alpha, length))
        energy.append(2*log1p((a-b)**2/(2*a*exp(w))))
        amplitude.append(widths(a,b))
        for mid, output in ((alpha, dressed), ((0.,0.,0.), central)):
            endpoints = [[x+sign*y/2 for x,y in zip(mid,delta)] for sign in (-1,1)]
            a1,a2 = [symbol(shifted(p, ang, length))[2] for ang in endpoints]
            output.append(widths(a1,a2))
        q = sqrt(s*(s+4))
        curvature.append(2*cos(p[0])/q-4*sin(p[0])**2*(s+2)/q**3)
        dg = 2*sin(p[0])*(s+2)/(s*(s+4))
        metric.append(dg**2/(4*length**2))
    return (fsum(curvature)/length, fsum(energy), fsum(amplitude),
            fsum(dressed)-fsum(central), fsum(metric))


if __name__ == "__main__":
    print("L,gamma,D,Fcost,subtracted_adjacent_cost,central_directional_metric")
    for length in [2,3,4,8,16,32]:
        row=values(length,(.2,-.1,.05),(.08,.04,-.02))
        print(length, *(f"{v:.12g}" for v in row), sep=",")
        if length==2:
            assert abs(row[0]-(1/sqrt(32)-1/sqrt(96)-1/sqrt(192)))<1e-14
        if length==3:
            assert row[0]<0
