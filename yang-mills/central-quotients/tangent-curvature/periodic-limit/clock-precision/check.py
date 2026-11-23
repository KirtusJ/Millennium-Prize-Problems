"""Exact checks for ambiguous input data and strided certificates."""
from fractions import Fraction as Q
from math import prod
from stride import enclose, strided
from clock import approximation, moment_interval


def check_indistinguishability():
    nodes = (Q(0), Q(3,16), Q(9,16), Q(3,4))
    b = Q(7,8)
    weights = [prod((b-y)/(x-y) for y in nodes if y!=x) for x in nodes]
    norm = 1 + sum(map(abs, weights))
    for j in range(80):
        difference = b**j - sum(w*x**j for x,w in zip(nodes,weights))
        _, tail = approximation(j, min(3,j))
        assert abs(difference) <= norm*tail
        if j <= 3:
            assert difference == 0
    assert b**4 != sum(w*x**4 for x,w in zip(nodes,weights))


def check_enclosures():
    atoms = [(Q(1,4),Q(0)), (Q(1,2),Q(2,3)), (Q(1,4),Q(9,10))]
    def moment(j):
        return sum(mass*x**j for mass,x in atoms)
    count = 0
    for j in (3,7,14,23,31):
        for D in range(1,j+1):
            known = [(max(Q(0),moment(i)-Q(1,10000)), moment(i)+Q(1,10000))
                     for i in range(D+1)]
            for s in range(1,D+2):
                lo,hi = strided(j,known,s)
                assert lo <= moment(j) <= hi
                if s==1:
                    assert (lo,hi) == moment_interval(j,known)
                count += 1
    print("Exact rational interval checks:", count)


def large_clock():
    # Uniform measure on [0,1] has M_i=1/(i+1). The targets have different residues.
    J, D, s = 4099, 1100, 8
    delta = Q(1,10**120)
    moments = [[str(Q(1,i+1)-delta),str(Q(1,i+1)+delta)] for i in range(D+1)]
    result = enclose({"target_index":J, "stride":s, "moments":moments})
    h = (J-1)//2
    low,high = map(Q,result["midpoint_ratio"])
    assert low <= Q(J+1,h+1) <= high and high/low-1 < Q(1,10**8)
    print("J, h, last input, stride:", J,h,D,s)
    print("Ratio interval relative width:",float(high/low-1))


if __name__ == "__main__":
    check_indistinguishability()
    check_enclosures()
    large_clock()
    zero = enclose({"target_index":8,"stride":2,"moments":[[0,0],[0,0]]})
    assert zero["midpoint_ratio"] is None and zero["clock_moment"] == ["0","0"]
