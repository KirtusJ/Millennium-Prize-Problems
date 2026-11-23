"""Exact local-kernel checks and numerical checks in the compact one-link law."""
from fractions import Fraction as Q
from itertools import product
import json
import math


def sqrt_upper(value, scale=10**10):
    """Rational upper endpoint for a square root, rounded outward."""
    integer = math.isqrt(value.numerator*scale**2//value.denominator)
    lower = Q(integer,scale)
    return lower if lower**2 == value else Q(integer+1,scale)


def bessel_one(order):
    """Enclose I_order(1) by the positive series with a geometric remainder."""
    term = Q(1,2**order*math.factorial(order))
    total = term
    for j in range(1,13):
        term /= 4*j*(order+j)
        total += term
    ratio = Q(1,4*13*(order+13))
    return total,total+term*ratio/(1-ratio)


def beta_one():
    stop = 18
    intervals = [bessel_one(n) for n in range(stop+3)]
    i1lo,i1hi = intervals[1]
    # Each term is (n+1)*I_(n+1)/sqrt(I_1 I_(n+2)).
    head = sum((n+1)*intervals[n+1][1] *
               sqrt_upper(1/(i1lo*intervals[n+2][0])) for n in range(stop))
    # Majorant for the rest: exp(3/8)*sqrt(2)<3, and successive ratios <1/2.
    first = 3*sqrt_upper(Q(math.factorial(stop+2),2**stop))/math.factorial(stop)
    assert Q(stop+3,2*(stop+1)**2)<Q(1,4)
    assert head+2*first < 8 and 2*i1hi < Q(6,5)
    budget = 4*8**8*4**4
    assert budget == 2**34
    assert Q(budget,2**43) < Q(3,800) and (Q(1,20)+Q(1,32))**2 < Q(3,400)
    return {"A1_below":8,"inverse_budget":budget,"bare_weight":"3/400",
            "short_flow_weight":"1/400"}


def matrix_vector(matrix, vector):
    return [sum(a*x for a,x in zip(row,vector)) for row in matrix]


def local_kernel_model():
    # Product of two reversible two-state kernels. A nonfactorizing positive
    # boundary amplitude induces the magnetic multiplication factor M²=b/Kb.
    states = list(product(range(2),repeat=2))
    P = [[Q(3,4),Q(1,4)],[Q(1,4),Q(3,4)]]
    invP = [[Q(3,2),Q(-1,2)],[Q(-1,2),Q(3,2)]]
    K = [[P[i][j]*P[e][z] for j,z in states] for i,e in states]
    invK = [[invP[i][j]*invP[e][z] for j,z in states] for i,e in states]
    b = [Q(1),Q(4),Q(3),Q(2)]
    kb = matrix_vector(K,b)
    den = sum(x*y for x,y in zip(b,kb))/4
    mean = sum(b[t]*kb[t]*i for t,(i,e) in enumerate(states))/(4*den)
    f = [-mean,1-mean]
    v = [f[i]*kb[t] for t,(i,e) in enumerate(states)]
    num = sum(x*y for x,y in zip(v,matrix_vector(invK,v)))/4
    # Patch kernel columns are densities with respect to the uniform law.
    cols = [[f[i]*2*P[i][j] for i in range(2)] for j in range(2)]
    gram = [[sum(x*y for x,y in zip(a,matrix_vector(invP,c)))/2
             for c in cols] for a in cols]
    exterior = sum(b[t]*b[r]*(2*P[e][z])/16
                   for t,(i,e) in enumerate(states) for r,(j,z) in enumerate(states))
    expanded = sum(b[t]*b[r]*(2*P[e][z])*gram[i][j]/16
                   for t,(i,e) in enumerate(states) for r,(j,z) in enumerate(states))
    assert num == expanded and den >= exterior/2
    H2 = max(gram[i][i] for i in range(2))
    assert num <= H2*exterior and num/den <= 2*H2
    # A positive definite matrix may have negative kernel entries. That alone
    # does not permit replacing a signed Gram matrix by its diagonal bound.
    signed = [[1,Q(-3,4)],[Q(-3,4),1]]
    gram_signs = [[1,-1],[-1,1]]
    assert 1-signed[0][1]**2 > 0
    assert sum(signed[i][j]*gram_signs[i][j] for i,j in states) > sum(map(sum,signed))
    return {"inverse_moment":str(num/den),"majorant":str(2*H2),
            "signed_kernel_replacement":"fails"}


def one_link_controls():
    grid = 4096
    angles = [(j+0.5)*math.pi/grid for j in range(grid)]
    coords = [math.cos(t) for t in angles]
    haar = [math.sin(t)**2 for t in angles]
    for k in (0.,0.125,1.,6.,24.,100.):
        weights = [w*math.exp(k*(x-1)) for w,x in zip(haar,coords)]
        z = sum(weights)
        mean = sum(w*x for w,x in zip(weights,coords))/z
        axial = sum(w*(x-mean)**2 for w,x in zip(weights,coords))/z
        trans = sum(w*(1-x*x) for w,x in zip(weights,coords))/(3*z)
        assert min(axial,trans) >= 1.5/(4+k)**2-1e-13
    for d in (0,1,8,32):
        weights = [w*((1+x)/2)**d for w,x in zip(haar,coords)]
        error = sum(w*2*(1-x) for w,x in zip(weights,coords))/sum(weights)
        assert abs(error-6/(d+3)) < 1e-12
    for m in (2,4,8,16,32):
        weights = [w*(math.sin(m*t/2)/math.sin(t/2))**6 for w,t in zip(haar,angles)]
        mean_chord = sum(w*2*math.sin(t/2) for w,t in zip(weights,angles))/sum(weights)
        assert 0 < m*mean_chord < 4
    return {"tilts":6,"quadrature_nodes":grid,"beta_kernels":4,"Jackson_kernels":5}


if __name__=="__main__":
    print(json.dumps({"finite_model":local_kernel_model(),"SU2_beta_one":beta_one(),
                      "SU2_quadrature":one_link_controls()},sort_keys=True))
