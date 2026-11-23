"""Controls for the conditional quaternion law, independent masks and time kernel."""
from itertools import combinations, product

import numpy as np
from scipy.integrate import quad_vec
from scipy.special import ive


def longitudinal_and_transverse(R):
    scale = 1+R
    def integrand(y):
        density = np.exp(-R/scale*y)*np.sqrt(y*max(0.,2-y/scale))
        return density*np.array([1., y, y*y])
    # Split a long domain so the mass near zero remains visible to quadrature.
    ends = sorted(set([0., min(60., 2*scale), 2*scale]))
    moments = sum(quad_vec(integrand, a, b, epsabs=1e-12, epsrel=1e-12)[0]
                  for a,b in zip(ends, ends[1:]))
    _, first, second = moments/moments[0]
    return (second-first**2)/scale**2, (2*first-second/scale)/(3*scale)


def check_masks(dims):
    def shift(x,i):
        q=list(x)
        q[i]=(q[i]+1)%dims[i]
        return tuple(q)
    def cycle(t,n):
        return 2 if n%2 and t==n-1 else t%2
    coordinates=list(product(*(range(n) for n in dims)))
    faces=[[ (x,i), (shift(x,j),i), (x,j), (shift(x,i),j)]
           for x in coordinates for i,j in combinations(range(4),2)]
    def compatible(mask):
        return all(sum(e in mask for e in p)<=1 for p in faces)
    def contains(x,i,axes):
        other=[j for j in axes if j!=i]
        return (all(not(dims[j]%2 and x[j]==dims[j]-1) for j in other)
                and sum(x[j] for j in other)%2==0)
    one=set((x,i) for x in coordinates for i in range(3)
            if i==cycle(x[3],dims[3]) and contains(x,i,range(3)))
    assert compatible(one)
    for i in range(4):
        four=set((x,i) for x in coordinates if contains(x,i,range(4)))
        assert compatible(four)
    # The same orientation and parity repeated at consecutive times is invalid.
    invalid=set((x,0) for x in coordinates if contains(x,0,range(3)))
    assert not compatible(invalid)
    print("masks", dims, "space-time size", len(one), "plaquettes", len(faces))


def check_double_derivative():
    # Independent SU(2) matrix control on one rectangle, including its parallel transport.
    rng=np.random.default_rng(406)
    def group():
        w,x,y,z=(q:=rng.normal(size=4))/np.linalg.norm(q)
        return np.array([[w+1j*z, y+1j*x], [-y+1j*x, w-1j*z]])
    U,V,opposite,W=(group() for _ in range(4))
    a=np.diag([1j,-1j])
    transported=W.conj().T @ a @ W
    eps=.002
    def rotate(A,angle):
        return np.eye(2)*np.cos(angle)+np.sin(angle)*A
    def mixed(b):
        values=[]
        for l,r in product((-1,1),repeat=2):
            left=rotate(a,l*eps) @ U
            right=rotate(b,r*eps) @ opposite
            values.append(l*r*np.trace(left @ V @ right.conj().T @ W.conj().T).real/2)
        return sum(values)/(4*np.sin(eps)**2)
    target=np.trace(U @ V @ opposite.conj().T @ W.conj().T).real/2
    assert abs(mixed(transported)-target)<1e-9
    assert abs(mixed(a)-target)>.001
    print("mixed derivative, transported and untransported errors",
          abs(mixed(transported)-target),abs(mixed(a)-target))


def main():
    check_double_derivative()
    for R in [0., 1., 6., 60., 600., 6000.]:
        longitudinal, transverse=longitudinal_and_transverse(R)
        if R:
            m=ive(2,R)/ive(1,R)
            assert abs(transverse-m/R)<1e-11
            assert abs(longitudinal-(1-m*m-3*m/R))<1e-11
        else:
            assert max(abs(longitudinal-.25),abs(transverse-.25))<1e-12
        print("polar", R, longitudinal, transverse, "R squared times minimum", R*R*min(longitudinal, transverse))
    assert abs(R*R*longitudinal-1.5)<.001
    for dims in [(4,4,4,4),(3,3,3,5),(3,4,5,4)]:
        check_masks(dims)
    for N in [2,8,24,80]:
        lag=np.abs(np.subtract.outer(np.arange(N),np.arange(N)))
        for r in [0.,.1,.7,.999999,1.]:
            direct=np.sum((-r)**lag)/N
            limit=(1-r)/(1+r)
            remainder=2*r*(1-r**N)/(N*(1+r)**2)
            assert abs(direct-limit-remainder)<1e-12 and 0<=remainder<=1/N
    print("alternating time matrices checked through length",N)


if __name__=='__main__':
    main()
