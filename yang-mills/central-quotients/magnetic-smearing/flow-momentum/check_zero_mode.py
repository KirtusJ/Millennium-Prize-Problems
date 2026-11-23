"""Interval check of the spatially summed compact U(1) Wilson tangent on the 16^4 torus."""
import sys
from itertools import combinations_with_replacement
from math import factorial, prod
from pathlib import Path
from mpmath import iv

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "spatial-flow"))
from check_torus import cosines

iv.dps = 40


def run():
    co = cosines()
    lam = [2*(1-v) for v in co[:9]]
    multiplicity = [1]+[2]*7+[1]
    temporal_heat = [iv.exp(-12*x) for x in lam]
    lags = (0,2,3,4)
    full, spatial = ([iv.mpf(0) for _ in lags] for _ in range(2))
    for triple in combinations_with_replacement(range(9),3):
        if triple == (0,0,0):
            continue
        permutations = factorial(3)//prod(factorial(triple.count(j)) for j in set(triple))
        count = permutations*prod(multiplicity[j] for j in triple)
        q2 = sum(lam[j] for j in triple)
        # Two transverse magnetic eigenvalues. Their common factor 2 cancels in the ratio.
        common = count*q2**2*iv.exp(-24*q2)
        for i,n in enumerate(lags):
            terms = [multiplicity[j]*co[(n*j)%16]/(q2+lam[j]) for j in range(9)]
            full[i] += common*(sum(v*w for v,w in zip(terms,temporal_heat))/16)**2
            spatial[i] += common*(sum(terms)/16)**2
    for name, cv in (("full",full),("spatial",spatial)):
        readings = [v/cv[0] for v in cv[1:]]
        q = readings[0]-2*readings[1]+readings[2]
        print(name, "normalized zero-momentum C(2),C(3),C(4)", *(str(x) for x in readings))
        print(name, "normalized reflected form", q)
        if name == "full":
            for value, low, high in zip(readings, (918685,832895,737429), (918686,832896,737430)):
                assert iv.mpf(low)/10**6 < value < iv.mpf(high)/10**6
            assert iv.mpf(-9676)/10**6 < q < iv.mpf(-9674)/10**6
        else:
            assert iv.mpf(60388)/10**6 < q < iv.mpf(60389)/10**6


if __name__ == "__main__":
    run()
