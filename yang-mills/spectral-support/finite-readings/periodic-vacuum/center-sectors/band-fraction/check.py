"""A posteriori bound on the fraction of one-site vacuum tensor weight in the band."""
import sys
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, prod
from pathlib import Path

import numpy as np
from scipy.linalg import eigh

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import certify as c
from enclosure import I, mat
from spectrum import harmonics, moment, states


def pairings(n):
    """Number of ways of pairing n distinguishable slots, n even."""
    return factorial(n) // (2**(n//2) * factorial(n//2))


def sphere_moment(i, j, k):
    # First integrate the direction shared by the last two scalar products.
    if (j+k) % 2:
        return F(0)
    numerator = F(0)
    for r in range(j%2, min(j,k)+1, 2):
        if (i+r) % 2 == 0:
            ways = comb(j,r)*comb(k,r)*factorial(r)*pairings(j-r)*pairings(k-r)
            numerator += F(ways, i+r+1)
    return numerator / prod(range(1,j+k+2,2))


def check_moments(even, odd):
    labels = sorted({ls for _,ls,_ in even+odd}, key=lambda ls:(sum(ls),ls))
    shapes, _ = harmonics(labels)
    terms = {key for shape in shapes for key in shape}
    pairs = {(i+a,j+b,k+c_) for i,j,k in terms for a,b,c_ in terms}
    support = {(i+2*a,j+2*b,k+2*d) for i,j,k in pairs
               for a in range(19) for b in range(19-a) for d in range(19-a-b)}
    assert all((i+k)%2 == (j+k)%2 == 0 for i,j,k in support)
    degree = max(max(i+k,j+k,k) for i,j,k in support)
    assert degree <= 63
    for key in support:
        assert sphere_moment(*key) == moment(*key), key
    assert sphere_moment(1,1,1)==F(1,9) and sphere_moment(0,1,0)==0
    print(f"{len(support)} exact angular moments agree; maximum coordinate degree {degree}",flush=True)


def check_tail(even):
    # The original membership check establishes completeness for every retained n triple.
    degrees = {ns for ns,_,_ in even}
    weights = {i:c.kinetic(i+1)[1] for i in range(0,17,2)}
    worst, index = max((prod(weights[i] for i in ns),ns)
                       for ns in product(range(0,16,2),repeat=3) if ns not in degrees)
    assert worst < F(22,100000) and weights[16] < F(22,100000)
    print(f"largest omitted even product below {float(worst):.12g} (rounded), degrees {index}",flush=True)


def bound():
    if not __debug__:
        raise RuntimeError("enable assertions")
    np.seterr(over="raise",invalid="raise",divide="raise")
    even,odd = [states(p,float(c.CUTOFF)) for p in ((0,0,0),(1,0,0))]
    kin = c.verify_selection((0,0,0),even)
    check_moments(even,odd)
    check_tail(even)
    matrices, = c.interval_matrices([even],[kin],include_square=True)
    M,J,H = (matrices[i] for i in range(3))
    mid = lambda a:(a.lo+a.hi)/2
    Q = eigh(mid(M))[1]
    dim = len(even)
    identity = I(np.eye(dim))
    unit = lambda v:c.quad(v,identity,v)
    # Strict upper bound on twice the polynomial error used for M, J and H.
    eta = I.rational(F(2,20000)*F(6**19,factorial(19))/(1-F(6,20))*2)
    def magnitude(v):
        return I(c.norm(v))
    q0 = I(Q[:,-1,None].copy())
    doublet = Q[:,-3:-1]
    direction = doublet @ (doublet.T @ mid(J) @ q0.lo)
    q1 = I(direction / np.linalg.norm(direction))
    def length(v):
        value = c.quad(v,M,v)
        error = eta*unit(v)
        return I((value-error).lo,(value+error).hi).sqrt()
    l0,l1 = length(q0),length(q1)
    rational = lambda decimal:I.rational(F(decimal))
    # The unshifted finite compressed bounds on M come from the parent certificate.
    tail = rational(".00022")
    lam_max = rational(".0529")+tail
    lam_next = rational(".0204")+tail
    lam_min = rational(".0526")
    a0,a1 = rational(".052695"),rational(".0200")
    def centered_residual(v,l,a):
        raw = (magnitude(mat(M,v)-a*v)+eta*magnitude(v))/l
        return rational(".23")*raw+tail/2
    t = centered_residual(q0,l0,a0)/(a0+tail/2-lam_next)
    # Uniform upper bounds on t suffice. The singular part of the square root is avoided.
    t = I(t.hi)
    phase = t*(I(2)/(1+(1-t.square()).sqrt())).sqrt()
    b1 = a1+tail/2
    dist = I(min((b1-lam_max/3).lo,(3*lam_min/7-b1).lo))
    # The orthogonal vacuum complement lies strictly below the upper band edge.
    assert lam_next.hi < (3*lam_min/7).lo
    d = I((centered_residual(q1,l1,a1)/dist).hi)
    assert 0<dist.lo and 0<d.lo<1
    amplitude = c.quad(q1,J,q0)
    positive_amp = I(amplitude.lo if amplitude.lo>0 else -amplitude.hi)
    assert positive_amp.lo>0
    overlap = (positive_amp-eta*magnitude(q0)*magnitude(q1))/(l0*l1)
    m = I((overlap-phase/I(2).sqrt()).lo)
    var = (c.quad(q0,H,q0)+eta*unit(q0))/l0.square()
    U = I((var.sqrt()+phase/I(2).sqrt()).hi)
    # The angle from the band to O vacuum cannot exceed the sum of the two trial angles.
    assert 0<m.lo<U.lo
    z = m/U
    cos_d = (1-d.square()).sqrt()
    rel = z*cos_d - d*(1-z.square()).sqrt()
    abs_amp = m*cos_d - d*(U.square()-m.square()).sqrt()
    assert rel.lo>0 and abs_amp.lo>0
    print(f"trial O² upper {var.hi:.9f}, phase distance upper {phase.hi:.9f}")
    print(f"vacuum overlap lower {m.lo:.9f}, total norm upper {U.hi:.9f}, band leakage upper {d.hi:.9f}")
    print(f"absolute weight lower {abs_amp.square().lo:.9f}, fraction lower {rel.square().lo:.9f}")
    assert F.from_float(float(rel.square().lo))>F(888,1000)
    assert F.from_float(float(abs_amp.square().lo))>F(736,10000)


if __name__ == "__main__":
    bound()
