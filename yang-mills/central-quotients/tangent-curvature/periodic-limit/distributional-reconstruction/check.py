"""Independent finite checks of the axial-chain counterexample and OS conventions."""
from fractions import Fraction as Q
from itertools import combinations_with_replacement, product
from math import e, exp, fsum


def conditional_mean(state, mask, rho):
    value = Q(0)
    for output in product((-1,1), repeat=len(state)):
        probability = Q(1)
        monomial = 1
        for axis,(x,y) in enumerate(zip(state,output)):
            probability *= (1+rho*x*y)/2
            if mask >> axis & 1:
                monomial *= y
        value += probability*monomial
    return value


def main():
    rho = Q(3,5)
    for state in product((-1,1),repeat=3):
        for mask in range(8):
            original = 1
            for axis,x in enumerate(state):
                if mask >> axis & 1:
                    original *= x
            assert conditional_mean(state,mask,rho) == original*rho**mask.bit_count()
    count=0
    for times in combinations_with_replacement(range(8), 4):
        shifted=[v+i+1 for i,v in enumerate(times)]
        assert 0<shifted[0] and all(x<y for x,y in zip(shifted,shifted[1:]))
        count+=1
    print("Ordered chamber shifts:", count, "finite transfer eigenvector checks:", 64)
    for L in (2,3,4):
        sites=list(product(range(L),repeat=4))
        pairs=sum(sum(x!=y for x,y in zip(a,b))<=1 for a in sites for b in sites)
        assert pairs == L**4*(1+4*(L-1))
        print("Box side",L,"supported ordered pairs",pairs)
    limit=e*(exp(-1)-exp(-2))**2
    for L in (16,64,256,1024):
        a=1/L
        time_sum=fsum(exp(-a*n) for n in range(L,2*L))
        norm=e*a**8*L**3*time_sum**2
        print("L",L,"clock 1; normalized box pairing",norm,"pairing / a³",norm/a**3)
    assert abs(norm/a**3-limit)<0.0002


if __name__ == "__main__":
    main()
