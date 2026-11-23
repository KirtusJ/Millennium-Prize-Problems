"""Cross-period source bound on G4's frozen one-site E-channel chain summaries."""
import argparse
import hashlib
import io
import math
from fractions import Fraction as F
from pathlib import Path
from zipfile import ZipFile

import numpy as np
from scipy.optimize import brentq

SHA = '279fd2d20c36f3cb1c9bfc1729adaf171785d1ac2ccb8b0d618415b3c19bd952'


def geometric_ratio(x, n):
    return (1-x**43)/(1-x**n) if x != 1 else F(43,n)


def envelope(s, cells=1024):
    r = F(1,3)
    candidates = []
    for i in range(cells):
        a, b = (r+(1-r)*F(j,cells) for j in (i,i+1))
        candidates.append((r+1/r-b-1/b)*a**(2-s)*geometric_ratio(b,23-2*s))
    return max(candidates)


def controls():
    # Rational, unnormalized traces for a decoupled vacuum with one excited pair.
    # The mean subtraction cancels in all differences.
    r = F(1,3)
    for origin in (F(3,4),F(15,16)):
        for x in (F(1,4), r, F(1,2), F(5,6), F(63,64), F(1)):
            def corr(T, j):
                return origin**T*(x**j+x**(T-j))
            def diff(T, j):
                return corr(T,j)-corr(T,j+1)
            W = (r+1/r)*diff(48,2)-diff(48,1)-diff(48,3)
            paired = origin**48*(r+1/r-x-1/x)*(1-x)*x**2*(1-x**43)
            assert W == paired
            for s in (2,4,6):
                upper = bounds[s]*origin**24*diff(24,s)
                assert W <= upper
                if W>0 and x==F(1,2):
                    # The source attenuation corresponds to doubling 24 to 48.
                    ratio = (r+1/r-x-1/x)*x**(2-s)*geometric_ratio(x,23-2*s)
                    assert W == ratio*origin**24*diff(24,s)


def load(path):
    data = path.read_bytes()
    assert hashlib.sha256(data).hexdigest() == SHA
    curves = []
    with ZipFile(io.BytesIO(data)) as z:
        for name in ('d3_b4','d3_b4_T48'):
            with np.load(io.BytesIO(z.read(f'rerun/{name}.npz')),allow_pickle=False) as a:
                curves.append(a['C_E'][:,:,0,0,:].sum(axis=0)/a['nmeas'].sum())
    assert [c.shape for c in curves]==[(32,13),(32,25)]
    return curves


def margin(samples, nse):
    return samples.mean()+nse*samples.std(ddof=1)/math.sqrt(len(samples))


def exp_upper(q):
    """Strict rational upper bound on exp(-q), q>0."""
    return 1/sum(q**j/math.factorial(j) for j in range(65))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive',type=Path)
    args=parser.parse_args()
    bounds={s:envelope(s) for s in range(2,9)}
    controls()
    short,long=load(args.archive)
    d=long[:,:-1]-long[:,1:]
    W=margin((10/3)*d[:,2]-d[:,1]-d[:,3],-3)
    print('three-SE W48 lower',format(W,'.12g'))
    for s,h in bounds.items():
        D=margin(short[:,s]-short[:,s+1],3)
        def tax(g):
            return float(h)*D*math.exp(-24*g)*(1+1727*math.exp(-23*g))
        cutoff=brentq(lambda g:tax(g)-W,0,1)
        print(s,format(float(h),'.9g'),format(D,'.10f'),format(cutoff,'.8f'))
    w_floor, d_ceiling = F(162,100000), F(157,1000000)
    assert float(w_floor)<W and margin(short[:,6]-short[:,7],3)<float(d_ceiling)
    def charged(g):
        return bounds[6]*d_ceiling*exp_upper(24*g)*(1+1727*exp_upper(23*g))
    assert charged(F(171,1000))<w_floor
    print('g=0.171 charged upper',float(charged(F(171,1000))))
    print('g=0.2 unassigned positive contrast at least',float(w_floor-charged(F(1,5))))
