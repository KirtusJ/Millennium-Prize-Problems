"""Enumerate each root orbit using simple reflections and exact rational arithmetic."""
from collections import deque
from sympy import Matrix, Rational, diag


def simple_gram(family, n):
    lengths = [2]*n
    if family == "B":
        lengths[-1] = 1
    if family == "C":
        lengths[:-1] = [1]*(n-1)
    if family == "F":
        lengths = [2, 2, 1, 1]
    if family == "G":
        lengths = [2, Rational(2, 3)]
    gram = diag(*lengths)
    edges = [(i, i+1) for i in range(n-1)]
    if family in ("D", "E"):
        edges[-1] = (n-3 if family == "D" else 2, n-1)
    for i, j in edges:
        gram[i, j] = gram[j, i] = -Rational(max(lengths[i], lengths[j]), 2)
    return gram


def costs(family, rank):
    gram = simple_gram(family, rank)
    reflections = [[int(2*gram[i, j]/gram[i, i]) for j in range(rank)]
                   for i in range(rank)]
    simple = [tuple(int(i == j) for j in range(rank)) for i in range(rank)]
    roots = set(simple)
    pending = deque(simple)
    while pending:
        root = pending.popleft()
        for i, row in enumerate(reflections):
            reflected = list(root)
            reflected[i] -= sum(a*b for a, b in zip(root, row))
            other = tuple(reflected)
            if other not in roots:
                roots.add(other)
                pending.append(other)
    positive = [r for r in roots if min(r) >= 0]
    assert len(roots) == 2*len(positive)
    target = {"A":rank*(rank+1), "B":2*rank**2, "C":2*rank**2,
              "D":2*rank*(rank-1), "E":{6:72,7:126,8:240}.get(rank),
              "F":48, "G":12}[family]
    assert len(roots) == target
    coeff = Matrix([sum(r[i] for r in positive) for i in range(rank)])
    inverse = gram.inv()
    assert coeff == inverse*gram.diagonal().T
    squares = [coeff[i]**2/inverse[i, i] for i in range(rank)]
    return min(squares), [i+1 for i,s in enumerate(squares) if s == min(squares)]


if __name__ == "__main__":
    for n in range(1, 13):
        m2, _ = costs("A", n)
        assert m2 == n*(n+1)
        if n >= 2:
            assert costs("B",n)[0] == min((2*n-1)**2,n**3)
            assert costs("C",n)[0] == 2*n*n
        if n >= 4:
            assert costs("D",n)[0] == (2*n-2)**2
    for family, n in (("E",6),("E",7),("E",8),("F",4),("G",2)):
        print(f"{family}{n}: minimum squared and minimizing nodes", costs(family,n))
