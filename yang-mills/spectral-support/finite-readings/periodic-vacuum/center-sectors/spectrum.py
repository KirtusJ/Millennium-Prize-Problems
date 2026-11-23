"""One-site SU(2) electric cutoff with the full magnetic weight in each matrix element."""
from functools import lru_cache
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, sqrt, log
import argparse

import numpy as np
from scipy.special import eval_gegenbauer, iv
from scipy.linalg import eigh

BETA = 4


@lru_cache(None)
def polar(n, k):
    if n % 2:
        return F(0)
    return sum(F((-1)**j * comb(k, j), n+2*j+1) for j in range(k+1))


@lru_cache(None)
def moment(a, b, c):
    """Average of the scalar products (n1.n2)^a (n1.n3)^b (n2.n3)^c."""
    return sum(comb(c, k)*F(comb(k,k//2), 2**k)*polar(a+c-k,k//2)*polar(b+c-k,k//2)
               for k in range(0,c+1,2))


def inner(f, g):
    return sum(cv*dv*moment(i+a,j+b,k+c)
               for (i,j,k),cv in f.items() for (a,b,c),dv in g.items())


def harmonics(labels):
    # The monomial of degrees (l1,l2,l3) contains one singlet at the top.
    # Subtract lower singlets with rational Haar moments.
    shapes, norms = [], []
    for i,j,k in labels:
        power = ((i+j-k)//2,(i+k-j)//2,(j+k-i)//2)
        f = {power: F(1)}
        for prev, norm in zip(shapes,norms):
            overlap = inner(f,prev)/norm
            if overlap:
                for key,val in prev.items():
                    f[key] = f.get(key,F(0))-overlap*val
        f = {k:v for k,v in f.items() if v}
        shapes.append(f)
        norms.append(inner(f,f))
        assert norms[-1]>0 and all(inner(f,g)==0 for g in shapes[:-1])
    return shapes, norms


def states(parity, eps):
    # For beta=4 the defining positive Bessel series gives I_(n+1)/I_n <= 2/(n+1).
    # At n=16 the individual kinetic value is already below every cutoff used here.
    kin = {n:iv(n+1,BETA)/iv(1,BETA) for n in range(17)}
    if kin[16] >= eps:
        raise ValueError("increase the one-link search range")
    links = [[(n,l) for n in range(p,16,2) for l in range(0,n+1,2)] for p in parity]
    basis = []
    for row in product(*links):
        ns,ls = zip(*row)
        weight = np.prod([kin[n] for n in ns])
        if weight > eps and abs(ls[0]-ls[1]) <= ls[2] <= ls[0]+ls[1]:
            basis.append((ns,ls,weight))
    return basis


def angular_grid(order, phi_order, labels):
    v, w = np.polynomial.legendre.leggauss(order)
    v, w = v[order//2:], w[order//2:]
    z = np.cos(np.pi*(np.arange(phi_order)+0.5)/phi_order)
    x,y,z = [a.ravel() for a in np.meshgrid(v,v,z,indexing="ij")]
    cross = x*y+np.sqrt((1-x*x)*(1-y*y))*z
    weights = np.broadcast_to(w[:,None,None]*w[None,:,None]/phi_order,
                              (len(w),len(w),phi_order)).ravel()
    shapes,norms = harmonics(labels)
    cols = [sum(float(c)*x**i*y**j*cross**k for (i,j,k),c in f.items())/sqrt(float(norm))
            for f,norm in zip(shapes,norms)]
    ang = np.asarray(cols)
    assert np.max(abs((ang*weights)@ang.T-np.eye(len(labels)))) < 1e-10
    ai,aj = np.tril_indices(len(labels))
    return np.stack([1-x*x,1-y*y,1-cross*cross]), (ang[ai]*ang[aj]*weights).T.copy(), ai,aj


def radial_grid(order):
    theta = np.pi*np.arange(1,order//2+1)/(order+1)
    x, w = np.cos(theta), 4*np.sin(theta)**2/(order+1)
    points = np.array(np.meshgrid(x,x,x,indexing="ij")).reshape(3,-1)
    weights = np.einsum("i,j,k->ijk",w,w,w).ravel()
    return points,weights


def radial_factor(n,l,x):
    square_norm = F(factorial(n+l+1),4**l*factorial(n-l)*(n+1)*factorial(l)**2)
    return (1-x*x)**(l//2)*eval_gegenbauer(n-l,l+1,x)/sqrt(float(square_norm))


def integrate(bases, order):
    if order % 2 or order < 12:
        raise ValueError("use an even order of at least 12")
    labels = sorted({ls for basis in bases for _,ls,_ in basis},key=lambda ls:(sum(ls),ls))
    label_index = {ls:i for i,ls in enumerate(labels)}
    points,weights = radial_grid(order)
    s = 1-points**2
    pairs = np.column_stack([s[0]*s[1],s[0]*s[2],s[1]*s[2]])
    angles, aw, ai,aj = angular_grid(order,order,labels)
    integrals = np.empty((len(weights),len(ai)))
    for start in range(0,len(weights),64):
        sl = slice(start,start+64)
        integrals[sl] = np.exp((-2*BETA*pairs[sl])@angles)@aw
    slots = np.empty((len(labels),len(labels)),dtype=int)
    slots[ai,aj] = slots[aj,ai] = np.arange(len(ai))
    O = [(s[0]-s[1])/sqrt(2),(s[0]+s[1]-2*s[2])/sqrt(6)]
    out = []
    for basis in bases:
        radial = np.array([np.prod([radial_factor(n,l,x) for n,l,x in zip(ns,ls,points)],axis=0)
                           for ns,ls,_ in basis])
        tags = np.array([label_index[ls] for _,ls,_ in basis])
        unit = (radial*weights)@radial.T * (tags[:,None]==tags)
        assert np.max(abs(unit-np.eye(len(basis)))) < 1e-10
        weighted = radial*np.sqrt(weights)[None,:]*np.sqrt([k for _,_,k in basis])[:,None]
        matrices = np.empty((3,len(basis),len(basis)))
        for i in np.unique(tags):
            rows = np.flatnonzero(tags==i)
            for j in np.unique(tags[tags<=i]):
                cols = np.flatnonzero(tags==j)
                block = integrals[:,slots[i,j]]*weighted[rows]
                for n, op in enumerate([1,*O]):
                    value = (block*op)@weighted[cols].T
                    matrices[n][np.ix_(rows,cols)] = value
                    matrices[n][np.ix_(cols,rows)] = value.T
        out.append(matrices)
    return out


def run(eps,order):
    parities = [(0,0,0),(1,0,0),(1,1,0),(1,1,1)]
    bases = [states(p,eps) for p in parities]
    sectors = integrate(bases,order)
    roots = []
    for p, basis, (M,O1,O2) in zip(parities,bases,sectors):
        vals, vecs = eigh(M)
        roots.append(vals[-1])
        if p == (0,0,0):
            energies = -np.log(vals[-3:-1]/vals[-1])
            weights = [sum((vecs[:,-3:-1].T@O@vecs[:,-1])**2/(vals[-3:-1]*vals[-1])) for O in (O1,O2)]
            print(f"even tensor doublet {energies}  mean overlap squared {np.mean(weights):.9f}")
        print(f"{p} dimension {len(basis)} top {vals[-1]:.10f} energy {log(roots[0]/roots[-1]):.8f}")
    for T in (24,48):
        odds = sum(mult*(lam/roots[0])**T for mult,lam in zip([3,3,1],roots[1:]))
        print(f"T={T} first seven excited states give occupation >= {odds/(1+odds):.8f} within approximation")
    return bases, sectors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cutoff",type=float,default=0.0003)
    parser.add_argument("--order",type=int,default=32)
    args = parser.parse_args()
    run(args.cutoff,args.order)
