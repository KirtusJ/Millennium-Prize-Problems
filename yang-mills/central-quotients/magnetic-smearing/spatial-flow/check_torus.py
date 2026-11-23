"""Outward interval evaluation of the 16^4 abelian Wilson tangent reflection form."""
from itertools import product
from mpmath import iv

iv.dps = 35
one = iv.mpf(1)
two = 2*one


def cosines():
    root = iv.sqrt(two)
    a, b, c = iv.sqrt(2+root)/2, root/2, iv.sqrt(2-root)/2
    return [one,a,b,c,0*one,-c,-b,-a,-one,-a,-b,-c,0*one,c,b,a]


def run():
    co = cosines()
    # Collapse +/- momenta only after counting their independent multiplicities.
    weight = [1]+[2]*7+[1]
    eigen = [2*(1-v) for v in co[:9]]
    basis = [iv.exp(-12*x) for x in eigen]
    by_time = [0*one for _ in range(9)]
    for x,y,z,t in product(range(9), repeat=4):
        if x==0 and y==0:
            continue
        A = eigen[x]+eigen[y]+eigen[z]+eigen[t]
        mult = weight[x]*weight[y]*weight[z]*weight[t]
        by_time[t] += mult*(eigen[x]+eigen[y])/A*basis[x]*basis[y]*basis[z]*basis[t]
    s0 = sum(by_time)
    sq = [ (sum(c*co[(lag*t)%16] for t,c in enumerate(by_time))/s0)**2 for lag in (2,3,4)]
    bounds = [(913457,913459),(822440,822442),(721557,721559)]
    for value, (lo, hi) in zip(sq,bounds):
        assert lo*one/10**6 < value and value < hi*one/10**6
    delta = sq[0]-2*sq[1]+sq[2]
    assert -9866*one/10**6 < delta and delta < -9862*one/10**6
    for lag, value in zip((2,3,4),sq):
        print("normalized quadratic C",lag,value)
    print("reflected difference",delta)
    # Remove temporal diffusion alone: check a spatial-flow history on the SAME periodic cube.
    # At fixed spatial mode use the exact periodic one-dimensional Green function in time.
    # Every mode is a positive combination of x^n and x^(16-n), so is its square and their sums.
    spatial = [0*one for _ in range(5)]
    for x,y,z in product(range(9), repeat=3):
        if x==0 and y==0:
            continue
        lam = eigen[x]+eigen[y]+eigen[z]
        decay = 2/(2+lam+iv.sqrt(lam*(4+lam)))
        pref = (weight[x]*weight[y]*weight[z]*basis[x]*basis[y]*basis[z]*
                (eigen[x]+eigen[y])/(iv.sqrt(lam*(4+lam))*(1-decay**16)))
        for n in (0,2,3,4):
            spatial[n] += pref*(decay**n+decay**(16-n))
    scaled = [(spatial[n]/spatial[0])**2 for n in (2,3,4)]
    diff = scaled[0]-2*scaled[1]+scaled[2]
    assert diff>0
    print("spatial-flow reflected difference",diff)


if __name__ == "__main__":
    run()
