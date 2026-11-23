"""Outward binary64 intervals. Matrix products are reduced to bounded integer dot products."""
from fractions import Fraction as F
import numpy as np


def down(x):
    return np.nextafter(x,-np.inf)


def up(x):
    return np.nextafter(x,np.inf)


class I:
    __array_priority__ = 1000

    def __init__(self, lo, hi=None):
        self.lo = np.asarray(lo, dtype=np.float64)
        self.hi = self.lo if hi is None else np.asarray(hi, dtype=np.float64)

    @classmethod
    def rational(cls, value):
        v = float(value)
        return cls(down(v),up(v))

    def __add__(self, other):
        b = box(other)
        return I(down(self.lo+b.lo),up(self.hi+b.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi,-self.lo)

    def __sub__(self, other):
        return self + (-box(other))

    def __rsub__(self, other):
        return box(other) + (-self)

    def __mul__(self, other):
        b = box(other)
        a,c,d,e = self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi
        return I(down(np.minimum(np.minimum(a,c),np.minimum(d,e))),
                 up(np.maximum(np.maximum(a,c),np.maximum(d,e))))

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = box(other)
        assert np.all((b.lo>0) | (b.hi<0))
        return self*I(down(1/b.hi),up(1/b.lo))

    def __pow__(self, n):
        if n == 0:
            return I(np.ones_like(self.lo))
        if n == 1:
            return self
        half = self**(n//2)
        sq = half.square()
        return sq if n%2 == 0 else sq*self

    def square(self):
        a,b = self.lo*self.lo,self.hi*self.hi
        return I(np.where((self.lo<=0)&(self.hi>=0),0,down(np.minimum(a,b))),up(np.maximum(a,b)))

    def sqrt(self):
        assert np.all(self.lo>=0)
        return I(down(np.sqrt(self.lo)),up(np.sqrt(self.hi)))

    def __getitem__(self,key):
        return I(self.lo[key],self.hi[key])

    @property
    def T(self):
        return I(self.lo.T,self.hi.T)

    def reshape(self,*shape):
        return I(self.lo.reshape(*shape),self.hi.reshape(*shape))


def box(a):
    return a if isinstance(a,I) else I(a)


def stack(values,axis=0):
    return I(np.stack([v.lo for v in values],axis=axis),
             np.stack([v.hi for v in values],axis=axis))


def fixed(a, bits):
    """Enclose entries by (integer midpoint ± integer radius) times a dyadic scale."""
    bound = max(np.abs(a.lo).max(),np.abs(a.hi).max())
    scale = 2.0**(int(np.frexp(bound)[1])-bits)
    low = np.floor(a.lo/scale).astype('int64')
    high = np.ceil(a.hi/scale).astype('int64')
    center = (low+high)//2
    return center, np.maximum(center-low,high-center), scale


def mat(a,b):
    # Each matrix product is over integers, including the center-radius propagation.
    # Bound individual absolute dot sums to preclude overflow before any multiplication.
    a,b=box(a),box(b)
    k=a.lo.shape[1]
    bits=(60-(k-1).bit_length())//2-1
    x,rx,sx=fixed(a,bits)
    y,ry,sy=fixed(b,bits)
    assert k*int((abs(x)+rx).max())*int((abs(y)+ry).max()) < 2**60
    mid=x@y
    rad=rx@(abs(y)+ry)+abs(x)@ry
    return I(down((mid-rad).astype(float))*(sx*sy),up((mid+rad).astype(float))*(sx*sy))


def exp_negative(a):
    """Taylor of exp(a/256) with rigorous absolute remainder, then eight squarings."""
    assert np.min(a.lo)>-25 and np.max(a.hi)<1
    z=a/256
    p=I(np.ones_like(z.lo))
    for j in range(9,0,-1):
        p=1+z*p/j
    # |z| < 1/10, exp(|z|)<2, 2*10^-10 / 10! < 2^-53.
    p=p+I(-2.0**-53,2.0**-53)
    for _ in range(8):
        p=p.square()
    return p
