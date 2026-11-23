"""Rational enclosures for the original one-cube transfer at beta_s=1, beta_t=1/100."""
from fractions import Fraction as F
from math import factorial


def derivative_bounds(d, j, order):
    total = F(0)
    for k in range(order+1):
        n = d+2*k-1
        if n >= j:
            total += F(factorial(n)//factorial(n-j), 2**n*factorial(k)*factorial(d+k))
    tail = F(4, factorial(order+1)*factorial(d+order+1))
    return total, total+tail


def static_bounds(cut=7, order=8):
    lower, upper = [F(0)]*4, [F(0)]*4
    for d in range(1,cut+1):
        bounds = [derivative_bounds(d,j,order) for j in range(3)]
        for out, values in zip((lower,upper), zip(*bounds)):
            a, da, dda = values
            terms = [a**6, da*a**5, dda*a**5, da**2*a**4]
            for j, term in enumerate(terms):
                out[j] += d*d*term
    tail = F(4*3**6*(cut+1)**2, factorial(cut+1)**6)
    z, p, pp, pq = lower
    Z, P, PP, PQ = [x+tail for x in upper]
    transverse = (4*(pp/Z-PQ/z), 4*(PP/z-pq/Z))
    scalar = (4*((pp+5*pq)/Z-6*(P/z)**2), 4*((PP+5*PQ)/z-6*(p/Z)**2))
    return transverse, scalar


def certified_intervals():
    tr, sc = static_bounds()
    u = F(1,400)  # upper bound at beta_t=1/100
    D = 729       # exp(6)/Z < 3^6 by Jensen
    top = 1+24*u**4
    residual = D*u**6
    error = D*u**2
    assert sc[0]/top > tr[1] and top < 2
    assert F(8993,10000) < sc[0]/(top*(top+residual))
    assert sc[1]+error < F(9040,10000)
    assert F(8836,10000) < tr[0]/(top+residual)
    assert tr[1]+error < F(8883,10000)
    assert error < F(456,100000)
    return {"beta_s":"1", "beta_t":"1/100", "unit":"(I2/I1)^4",
            "first":["0.8993","0.9040"], "second_through_sixth":["0.8836","0.8883"],
            "later_upper":"0.00456", "dimension_cut":7, "power_index_cut":8}
