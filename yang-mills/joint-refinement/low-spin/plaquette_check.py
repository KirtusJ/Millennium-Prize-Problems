"""Local pair and rectangular dissemination checks. Requires NumPy."""
from itertools import product
from math import floor, log2
import numpy as np


def mul(q, p):
    return np.r_[q[0]*p[0]-q[1:]@p[1:],
                 q[0]*p[1:]+p[0]*q[1:]+np.cross(q[1:],p[1:])]


def inv(q):
    return q * np.array([1,-1,-1,-1])


def loop(field, pos, i, j):
    def step(axis):
        where=list(pos)
        where[axis]=(where[axis]+1)%field.shape[axis]
        return tuple(where)
    ab=mul(field[pos+(i,)],field[step(i)+(j,)])
    ba=mul(field[pos+(j,)],field[step(j)+(i,)])
    return ab@ba


def pair_test():
    rng=np.random.default_rng(552019)
    n=6
    field=rng.normal(size=(n,n,n,4,4,4))
    field/=np.linalg.norm(field,axis=-1,keepdims=True)
    pos=(2,1,0,1)
    second=(3,1,0,1)
    edges=[pos+(0,), second+(0,)]
    product_uv=mul(field[edges[0]],field[edges[1]])
    terms=[]
    for x in (pos,second):
        for j in range(1,4):
            y=list(x)
            y[j]=(y[j]-1)%field.shape[j]
            terms.extend([(x,j),(tuple(y),j)])
    assert len(set(terms))==12

    def readings(q):
        field[edges[0]]=q
        field[edges[1]]=mul(inv(q),product_uv)
        np.testing.assert_allclose(mul(field[edges[0]],field[edges[1]]),product_uv,atol=2e-15)
        return sum(loop(field,x,0,j) for x,j in terms), loop(field,pos,0,1), loop(field,second,0,1)

    basis=np.array([readings(q) for q in np.eye(4)])
    assert np.linalg.norm(basis[:,0]) <= 12
    np.testing.assert_allclose(np.linalg.norm(basis[:,1:],axis=0),1,atol=2e-15)
    for q in rng.normal(size=(30,4)):
        q=q/np.linalg.norm(q)
        np.testing.assert_allclose(readings(q),q@basis,rtol=0,atol=1e-14)


def rectangular_count():
    for n in (6,8,10,14,16):
        m=16
        d=2**floor(log2(n))
        blocks=list(product(range(1-d,1),range(1-d,1),range(1-d,1),range(1-m,1)))
        # Face in directions 0 and 1 of a reflected cube. Its transverse
        # coordinate is the even endpoint of the interval in each other axis.
        faces=[(i%n,j%n,(k+k%2)%n,(t+t%2)%m) for i,j,k,t in blocks]
        assert len(set(faces))*4 == len(blocks)
        assert (n/d)**3 < 8


def tilted_covariance():
    angle=np.arange(1,1025)*np.pi/1025
    t=np.cos(angle)
    for x in (0,0.5,1,4,12,48,240,1200):
        w=np.sin(angle)**2*np.exp(-x*(1-t))
        w/=w.sum()
        radial=w@((t-w@t)**2)
        transverse=w@(1-t*t)/3
        assert min(radial,transverse)*(1+x)**2 >= 2**-22
    print("Paired links, rectangular face counts and tilted Haar variance checked.")


if __name__ == "__main__":
    pair_test()
    rectangular_count()
    tilted_covariance()
