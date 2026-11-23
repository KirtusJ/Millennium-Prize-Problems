"""Reproduce the exact face, edge and corner Rayleigh witnesses on spatial cubes."""
import argparse
from fractions import Fraction
from itertools import combinations_with_replacement, product
from math import gcd
from pathlib import Path
import sympy as sp

SIDE = 8
DEN = 1180392368175873615
ENERGY = 154952838044275900019970202595409844665096
NORM = 27720
GROUND = ((2, 4, 5, 6), (4, 9, 14, 17), (5, 14, 22, 27), (6, 17, 27, 32))
BONDS = ((2, 4, 5, 6), (3, 7, 11, 13), (4, 9, 14, 17), (4, 10, 16, 19))


def surface():
    cells = list(product(range(SIDE), repeat=2))
    edges, weights = [], []
    for u, (x, y) in enumerate(cells):
        rx, ry = min(x, 7-x), min(y, 7-y)
        edges.append((u, -1))
        weights.append(GROUND[rx][ry])
        if x < 7:
            edges.append((u, u+8))
            weights.append(BONDS[min(x, 6-x)][ry])
        if y < 7:
            edges.append((u, u+1))
            weights.append(BONDS[min(y, 6-y)][rx])
    H = sp.zeros(64, len(edges))
    for j, (u, v) in enumerate(edges):
        H[u, j] = 1
        if v >= 0:
            H[v, j] = -1
    A = H * H.T
    inverse, den = A.to_DM().inv_den(method='charpoly')
    inverse, den = inverse.to_Matrix(), int(den)
    common = gcd(den, *map(int, inverse))
    inverse, den = inverse / common, den // common
    assert den == DEN and A * inverse == den * sp.eye(64)
    P = den * sp.eye(len(edges)) - H.T * inverse * H
    assert H * P == sp.zeros(64, len(edges)) and P.is_symmetric()
    w = sp.Matrix(weights)
    energy = int((w.T * (6 * P.multiply_elementwise(P)) * w)[0])
    assert (energy, int(w.dot(w))) == (ENERGY, NORM)
    q = Fraction(energy, den**2 * NORM)
    assert q > Fraction(40119, 10000)
    print('surface: 64 cells, 176 faces; exact quotient', q, float(q))
    return inverse, edges, weights


def green(representatives, canonical, valid, ground):
    index = {p: i for i, p in enumerate(representatives)}
    A = sp.zeros(len(index))
    for i, p in enumerate(representatives):
        for axis, step in product(range(3), [-1, 1]):
            v = list(p)
            v[axis] += step
            v = tuple(v)
            if valid(v):
                A[i, i] += 1
                A[i, index[canonical(v)]] -= 1
            elif ground(v):
                A[i, i] += 1
    b = sp.zeros(len(index), 1)
    b[index[(0, 0, 0)]] = 1
    u, den = A.to_DM().solve_den(b.to_DM())
    u = u.to_Matrix() / den
    assert A*u == b
    return Fraction(u[index[(0, 0, 0)]])


def emit_rows(path, inv, edges, weights):
    reps = [(8*x+y, -1, 4 if x==y else 8) for x,y in combinations_with_replacement(range(4),2)]
    reps += [(8*x+y, 8*x+y+8, 4 if x==3 else 8) for x,y in product(range(4), repeat=2)]
    parts, balances, energies, rewrites, vertices = [], [], [], [], []
    for i,(u,v,m) in enumerate(reps):
        label=f'{i:02}'
        row=[int(inv[u,z]) - (0 if v<0 else int(inv[v,z])) for z in range(64)]+[0]
        p=edges.index((u,v))
        e=6*m*weights[p]*sum(w*((DEN if p==q else 0)-row[a]+row[b])**2
                             for q,((a,b),w) in enumerate(zip(edges,weights)))
        point=f'({u},{64 if v<0 else v})'
        pot='potential'+label
        term=f'work {point} {m} {pot}'
        eq=f'balanced {point} {pot}'
        name='checkedRow'+label
        parts.append('def '+pot+' : Array Int := #['+', '.join(map(str,row))+']')
        parts.append(f'theorem {name} : {eq}=true ∧ {term}={e} := by decide')
        balances.append(eq);energies.append(term);rewrites.append(name);vertices.append(f'({point},{m})')
    parts.append('theorem patchLayout : orbitRows = ['+', '.join(vertices)+'] := by decide')
    parts.append('theorem inverseEquations : (['+', '.join(balances)+'].all id)=true := by\n  rw ['+
                 ', '.join(n+'.1' for n in rewrites)+']\n  decide')
    parts.append('def patchEnergy : Int :=\n  '+' +\n  '.join(energies))
    parts.append(f'theorem patchNumerator : patchEnergy={ENERGY} := by\n  unfold patchEnergy\n  rw ['+
                 ', '.join(n+'.2' for n in rewrites)+']\n  decide')
    path.write_text('\n\n'.join(parts)+'\n\n')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--emit-rows', type=Path, help='write exact Lean certificates for the 26 potential and energy rows')
    args = p.parse_args()
    inv, edges, weights = surface()
    if args.emit_rows:
        emit_rows(args.emit_rows, inv, edges, weights)
    edge_reps = [(x,y,t) for x,y in combinations_with_replacement(range(3),2) for t in range(4)]
    e = green(edge_reps, lambda p: (*sorted(p[:2]), abs(p[2])),
              lambda p: all(0<=x<3 for x in p[:2]) and abs(p[2])<=3, lambda p: min(p[:2])<0)
    corner_reps = list(combinations_with_replacement(range(6),3))
    c = green(corner_reps, lambda p: tuple(sorted(p)),
              lambda p: all(0<=x<6 for x in p), lambda p: min(p)<0)
    assert e == Fraction(981403623,4993731821)
    assert c == Fraction(6682304780825183191939141957321,36006679442822741156466775925235)
    for label, g, copies, threshold in [('edge', e, 2, Fraction(4105,1000)),
                                        ('corner', c, 3, Fraction(43929,10000))]:
        q = 6*((1-g)**2 + (copies-1)*g**2)
        assert q > threshold
        print(label, 'grounded Green entry', g, 'quotient', q, float(q))


if __name__=='__main__':
    main()
