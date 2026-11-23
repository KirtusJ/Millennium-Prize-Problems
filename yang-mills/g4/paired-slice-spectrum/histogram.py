"""Enclose the first two Gibbs probabilities from a finite opposite-slice table.

Input JSON has probabilities (a square normalized table of rational strings),
diameters (orbit chord bounds), beta_t, half_period and optionally hellinger
(an externally established bound on the unscaled root-histogram distance).
The excitation interval reported is for the probability ratio; take
-log(ratio)/(2*half_period) for an energy in one-step units.
"""
from fractions import Fraction as Q
from math import isqrt
import argparse
import json


def characteristic(matrix):
    """Faddeev–LeVerrier in integer arithmetic, coefficients in descending order."""
    size = len(matrix)
    prev = [[int(i == j) for j in range(size)] for i in range(size)]
    coeff = [1]
    for degree in range(1,size+1):
        columns = list(zip(*prev))
        prev = [[sum(x*y for x,y in zip(row,col)) for col in columns] for row in matrix]
        trace = sum(prev[i][i] for i in range(size))
        assert trace % degree == 0
        c = -trace//degree
        coeff.append(c)
        for i in range(size):
            prev[i][i] += c
    return coeff


def count_above(coeff, t):
    """Sign variations of the translated real-rooted polynomial, ignoring zero roots."""
    poly = [coeff[0]]  # ascending, in the new variable
    for c in coeff[1:]:
        poly = [t*poly[0]+c]+[a+t*b for a,b in zip(poly,poly[1:])]+[poly[-1]]
    nonzero = [v for v in poly if v]
    return sum((a>0) != (b>0) for a,b in zip(nonzero,nonzero[1:]))


def spectrum_brackets(table, bits):
    size,scale = len(table),1 << bits
    integer = [[isqrt(v.numerator*scale**2//v.denominator) for v in row] for row in table]
    gram = [[sum(a*b for a,b in zip(row,col)) for col in integer] for row in integer]
    coeff = characteristic(gram)
    bounds = []
    for rank in (1,2):
        if rank > size:
            bounds.append((Q(0),Q(0)))
            continue
        lo,hi = 0,scale
        while hi-lo > 1:
            mid = (lo+hi)//2
            if count_above(coeff,mid**2) >= rank:
                lo = mid
            else:
                hi = mid
        # Entries were rounded down by less than 1/scale. Allow size/scale in norm.
        bounds.append((max(Q(0),Q(lo-size,scale)),min(Q(1),Q(hi+size,scale))))
    return bounds


def sqrt_upper(q, bits):
    scale = 1 << bits
    m = isqrt(q.numerator*scale**2//q.denominator)
    return Q(m+int(m*m*q.denominator < q.numerator*scale**2),scale)


def estimate(data,bits=48):
    if not 2 <= bits <= 256:
        raise ValueError("Use 2 through 256 precision bits")
    table = [[Q(str(x)) for x in row] for row in data["probabilities"]]
    delta = [Q(str(x)) for x in data["diameters"]]
    beta = Q(str(data["beta_t"]))
    eta = Q(str(data.get("hellinger",0)))
    n = data["half_period"]
    size = len(table)
    if (size == 0 or any(len(row)!=size for row in table) or len(delta)!=size
            or any(x<0 for row in table for x in row) or sum(map(sum,table))!=1
            or any(x<0 for x in delta) or beta<=0 or eta<0 or type(n)!=int or n<1):
        raise ValueError("Invalid normalized table, geometry, error bound, or half-period")
    # Pair-time reversal symmetrization contracts root-histogram distance.
    prob = [[(table[i][j]+table[j][i])/2 for j in range(size)] for i in range(size)]
    h = [[max(Q(0),1-(beta*(a+b)/2)**2/2) for b in delta] for a in delta]
    ell = min(Q(1),2*eta+sum(prob[i][j]*(1-h[i][j]**2) for i in range(size) for j in range(size)))
    dsq = sum(prob[i][j]*(1-h[i][j])**2 for i in range(size) for j in range(size))
    d = min(Q(1),sqrt_upper(dsq,bits)+eta)
    spec = spectrum_brackets(prob,bits)
    intervals = [(max(Q(0),lo-eta-d)**2,min(Q(1),(hi+eta+d)**2+ell)) for lo,hi in spec]
    first,second = intervals
    low = min(map(min,h))*max(Q(0),spec[0][0]-eta)
    first = (max(first[0],low**2),min(first[1],(spec[0][1]+eta)**2,1-second[0]))
    second = (second[0],min(second[1],1-first[0]))
    ratio = (second[0]/first[1],min(Q(1),second[1]/first[0]) if first[0] else Q(1))
    return {"vacuum":[str(x) for x in first],"first_excited":[str(x) for x in second],
            "probability_ratio":[str(x) for x in ratio],"energy_log_divisor":2*n,
            "ordered_l1_error":str(min(Q(2),ell+2*d+2*eta)),"tail_after_bins":str(ell)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input",type=argparse.FileType("r",encoding="utf8"))
    parser.add_argument("--bits",type=int,default=48)
    args = parser.parse_args()
    print(json.dumps(estimate(json.load(args.input),args.bits),indent=2))
