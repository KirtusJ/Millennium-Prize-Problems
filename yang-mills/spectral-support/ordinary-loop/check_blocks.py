"""Exact controls for the antiderivative, reflected base and the scale exponents."""
from collections import Counter
from fractions import Fraction


def translate(a, displacement):
    return {(x+displacement,y): w for (x,y),w in a.items()}


def reflect(a):
    return {(-1-x,y): w for (x,y),w in a.items()}


def difference(a, b):
    terms = Counter(a)
    terms.subtract(b)
    return {k:v for k,v in terms.items() if v}


def antiderivative(g):
    start, stop = min(x for x,y in g), max(x for x,y in g)
    acc = {}
    for y in {y for x,y in g}:
        partial = 0
        for x in range(start,stop+1):
            partial += g.get((x,y),0)
            if partial:
                acc[x,y] = partial
        assert partial == 0
    assert difference(acc,translate(acc,1)) == g
    assert sum(map(abs,acc.values())) <= (stop-start+1)*sum(map(abs,g.values()))
    return acc


def blocks():
    checked = 0
    for r in (2,3,4,7):
        # Off-center signed rectangular arrays include holes and cancel on some rows.
        a = {(x,y):Fraction(1+(x==1)-2*(y==1)) for x in range(-r,r) for y in range(-1,r+1)}
        for m in (2,3,5,9):
            positive = {}
            for j in range(1,m+1):
                copy=translate(a,j*(3*r+2))
                assert not (positive.keys() & copy.keys())
                positive.update({p:v/m for p,v in copy.items()})
            assert sum(x*x for x in positive.values()) == sum(x*x for x in a.values())/m
            assert min(x for x,y in positive)>0
            assert reflect(reflect(positive))==positive
            for g in (difference(a,positive),difference(positive,reflect(positive))):
                antiderivative(g)
                checked += 1
    print(f"{checked} exact line-antiderivative reconstructions; disjoint block squared-norm ratios 1/M")


def budgets():
    # Powers in r for H=r^h. Test the inequalities directly rather than constructing the boxes.
    for d in range(2,26,2):
        h=d*(3*d+6)
        ward_terms = [3-2*h, 2-13*h, 4-17*h]
        assert max(ward_terms) == 3-2*h
        block_terms = [1-Fraction(h,2), 2+Fraction(4-2*h,d), 2-16*h]
        assert max(block_terms) <= 4-Fraction(h,d)
        for m in range(1,d+1):
            direct = 2*m+4-2*h
            reflection = 2*(m-1)+4-Fraction(h,d)
            product = 2*m+2-20*h
            for exponent in (direct,reflection,product):
                # Extra Wick coefficients of degree at most d-m.
                assert exponent+d-m <= -2
            assert max(direct,reflection,product)+2*(d-m) <= -2
        assert 3*d+4-Fraction(h,d)==-2
    print("explicit box, Ward, block, centered-moment and Wick power budgets passed for even degrees 2 through 24")


if __name__=="__main__":
    blocks()
    budgets()
