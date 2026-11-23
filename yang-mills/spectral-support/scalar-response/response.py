"""Exact mixed-source derivatives of the open-box SU(2) Wilson Laplace coefficient."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import gcd, prod
import numpy as np
from sympy import Matrix


def box(lengths, reverse=False):
    sites = list(product(*(range(n + 1) for n in lengths)))
    def shift(x, a, step):
        return x[:a] + (x[a] + step,) + x[a+1:]
    edges = [(x, a) for x in sites for a, n in enumerate(lengths) if x[a] < n]
    tree = set()
    for x in sites[1:]:
        dirs = [a for a, v in enumerate(x) if v]
        a = dirs[-1] if reverse else dirs[0]
        tree.add((shift(x, a, -1), a))
    chords = {e: i for i, e in enumerate(e for e in edges if e not in tree)}
    faces, words = [], []
    for x in sites:
        for a, b in combinations(range(len(lengths)), 2):
            if x[a] == lengths[a] or x[b] == lengths[b]:
                continue
            faces.append((x, a, b))
            path = [(x, a, 1), (shift(x,a,1), b, 1),
                    (shift(x,b,1), a, -1), (x, b, -1)]
            words.append([(chords[(y,d)], s) for y,d,s in path if (y,d) in chords])
    B = np.zeros((len(faces), len(chords)), dtype=int)
    for p, word in enumerate(words):
        for edge, sign in word:
            B[p, edge] += sign
    return faces, words, B


def cube_sources(faces, origins):
    """All 24 positive square faces of each specified elementary four-cube."""
    return np.array([[int(all(lo <= v and v + (i in (a,b)) <= lo + 1
                              for i,(lo,v) in enumerate(zip(origin, x))))
                      for x,a,b in faces] for origin in origins], dtype=int)


def cell_sources(faces, times):
    return cube_sources(faces, [(t,0,0,0) for t in times])


def multiply(left, right):
    """Coefficients of a product modulo s_i^2, one row per subset of {1,2,3}."""
    out = []
    for mask in range(8):
        sub = mask
        value = left[sub] * right[0]
        while sub:
            sub = (sub - 1) & mask
            value = value + left[sub] * right[mask ^ sub]
        out.append(value)
    return np.array(out, dtype=object)


def inverse_jets(B, sources):
    H = B.T @ B
    numerator, den = Matrix(H).to_DM().inv_den()
    Q = np.array(numerator.to_Matrix().tolist(), dtype=object)
    Q = np.vectorize(int, otypes=[object])(Q)
    D = int(den)
    g = gcd(D, *(int(v) for v in Q.flat))
    if D < 0:
        g = -g
    D, Q = D // g, Q // g
    assert np.array_equal(H @ Q, D * np.eye(H.shape[0], dtype=object))
    Hi = [B.T @ (f[:,None]*B) for f in sources]
    step = [Q @ h for h in Hi]
    jets = [Q]
    for mask in range(1,8):
        jets.append(-sum(step[i] @ jets[mask ^ (1 << i)]
                         for i in range(3) if mask & (1 << i)))
    return D, np.array(jets, dtype=object), step


def parity(seq):
    return (-1)**sum(a>b for a,b in combinations(seq,2))


def terms(words):
    quartic = defaultdict(int)
    cubic = defaultdict(lambda: defaultdict(int))
    for p,word in enumerate(words):
        def add(scale, i,j,k,l):
            edges, signs = zip(*(word[t] for t in (i,j,k,l)))
            a,b,c,d = edges
            for weight,(u,v),(w,x) in [(9,(a,b),(c,d)), (3,(a,c),(b,d)), (3,(a,d),(b,c))]:
                pairs = tuple(sorted([tuple(sorted((u,v))),tuple(sorted((w,x)))]))
                quartic[(p,*pairs)] += weight * scale * prod(signs)
        slots = range(len(word))
        for i in slots:
            add(1,i,i,i,i)
        for i,j in combinations(slots,2):
            add(6,i,i,j,j)
            add(4,i,j,i,i)
            add(4,i,j,j,j)
            for k in slots:
                if k not in (i,j):
                    add(12,i,j,k,k)
        for i,j,k,l in combinations(slots,4):
            add(24,i,j,k,l)
            add(-24,i,k,j,l)
            add(24,i,l,j,k)
        for triple in combinations(word,3):
            edges, signs = zip(*triple)
            if len(set(edges)) == 3:
                cubic[tuple(sorted(edges))][p] += parity(edges)*prod(signs)
    return quartic, cubic


def actions(B, words, W, C, D):
    # C[mask] represents D^(1+|mask|) times that inverse-matrix derivative.
    quartic, cubic = terms(words)
    entries = [(p,*a,*b,k) for (p,a,b),k in quartic.items() if k]
    p,i,j,k,l,coef = np.array(entries, dtype=int).T
    quart = multiply(W[:,p], multiply(C[:,i,j], C[:,k,l])) @ coef
    haar = -np.trace(C, axis1=1, axis2=2)
    triple = np.zeros(8,dtype=object)
    if cubic:
        triples = np.array(list(cubic))
        V = np.stack([sum(W[:,p]*c for p,c in weights.items()) for weights in cubic.values()], axis=1)
        for start in range(0,len(triples),8):
            sel = slice(start,start+8)
            rows = triples[sel]
            det = 0
            for perm in permutations(range(3)):
                a,b,c = [C[:, rows[:,r,None], triples[None,:,s]] for r,s in enumerate(perm)]
                det = det + parity(perm)*multiply(a,multiply(b,c))
            triple += multiply(multiply(V[:,sel,None], V[:,None,:]), det).sum(axis=(1,2))
    var = np.stack([np.sum((B @ c) * B, axis=1) for c in C])
    bench = multiply(W,multiply(var,var)).sum(axis=1)
    numerators = {'haar':24*D**2*haar,'quartic':D*quart,'cubic':72*triple,
                  'abelian':9*D*bench}
    numerators['wilson'] = sum(numerators[k] for k in ('haar','quartic','cubic'))
    numerators['matched'] = -numerators['abelian']
    return {k:[F(int(x),24*D**(3+m.bit_count())) for m,x in enumerate(xs)]
            for k,xs in numerators.items()}


def evaluate(lengths, make_sources, reverse=False):
    faces, words, B = box(lengths, reverse)
    sources = make_sources(faces)
    assert sources.shape == (3,len(faces))
    D,C,step = inverse_jets(B,sources)
    W = np.zeros((8,len(faces)),dtype=object)
    W[0] = 1
    for i,f in enumerate(sources):
        W[1<<i] = D*f.astype(object)
    A = actions(B,words,W,C,D)
    def gaussian_pair(i,j):
        return F(3*int(np.sum(step[i]*step[j].T)),2*D**2)
    pairs = [gaussian_pair(i,j) for i,j in combinations(range(3),2)]
    variances = [gaussian_pair(i,i) for i in range(3)]
    triangle = F(3*int(np.sum((step[0]@step[1])*step[2].T)),D**3)
    return dict(chords=B.shape[1], faces=len(faces), supports=sources.sum(axis=1).tolist(),
                A=A, pairs=pairs, variances=variances, triangle=triangle)
