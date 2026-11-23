"""Exact values on a binary gauge graph, and a full SU(2) cube upper certificate."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[3]/"transfer-operator/girth-shell"))
from cube_bounds import certified_intervals


def binary():
    states = list(product((1,-1), repeat=2))
    # Character ratios 1,u^4,u^4,u^6 on the two-square theta graph, u=1/2.
    def kernel(x,y):
        a,b = x[0]*y[0], x[1]*y[1]
        return F(2)**((sum(x)+sum(y))//2)*(1+F(a+b,16)+F(a*b,64))/4
    k = [[kernel(x,y) for y in states] for x in states]
    def square(m):
        return [[sum(a*b for a,b in zip(row,col)) for col in zip(*m)] for row in m]
    for n in (1,2):
        t = square(k)
        z = sum(t[i][i] for i in range(4))
        # Newton identities use the ordinary partition at each multiple of 2n.
        trace = [None]
        mat = t
        for _ in range(4):
            trace.append(sum(mat[i][i] for i in range(4)))
            mat = [[sum(a*b for a,b in zip(row,col)) for col in zip(*t)] for row in mat]
        e = [F(1)]
        for m in range(1,5):
            e.append(sum((-1)**(j-1)*trace[j]*e[m-j] for j in range(1,m+1))/m)
        for m in (2,3,4):
            total = 0
            for x in combinations(range(4),m):
                for y in combinations(range(4),m):
                    terms = []
                    det = 0
                    for perm in permutations(range(m)):
                        term = 1
                        for i,j in enumerate(perm):
                            term *= k[x[i]][y[j]]
                        parity = sum(i>j for i,j in combinations(perm,2))%2
                        det += (-1)**parity*term
                        terms.append(term**2)
                    h = det**2/(factorial(m)*sum(terms))
                    assert 0 <= h <= 1
                    # All orderings of x, then all assignments of y to ordered x.
                    total += factorial(m)*sum(term*h for term in terms)
            assert total == e[m]
            print("period, copies, mean",2*n,m,float(total/z**m))
        k = t


def cube():
    certified_intervals()
    for n,limit in ((200,F("0.996")),(400,F("0.990")),(600,F("0.9892"))):
        h = (F("0.8883")/F("0.8993"))**n
        tail = 10**6*(F(11,10)/F(9,10)**3)**12*(729/(400**2*F("0.8993")))**n
        assert tail < F(1,10**15)
        s = 5*h+F(1,10**15)
        v = 5*h*h+F(1,10**30)
        a = F(1,10**16)
        assert (F("0.9040")/400**4)**n < a
        upper_squared = ((v+v*v/2+a*a*(v*v/2+v**3/6))*(1+a*a*(1+v))*
                         (1+s+a*(s+s*s/2))**4)
        assert upper_squared < limit**(2*n)
        print("Wilson period, certified ratio below", n,float(limit))


if __name__ == "__main__":
    binary()
    cube()
