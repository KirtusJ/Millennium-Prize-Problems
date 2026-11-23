"""Independently compute the surface covariance from elementary grounded cycles."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import sys
import sympy as sp
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_patch import GROUND, BONDS


def main():
    # Index ground faces first, then horizontal and vertical bonds, unlike the divergence check.
    side = 8
    cells = list(product(range(side), repeat=2))
    bonds = [(u, (u[0]+dx, u[1]+dy)) for dx,dy in [(0,1),(1,0)] for u in cells
             if u[0]+dx<side and u[1]+dy<side]
    nc, nb = len(cells), len(bonds)
    C = sp.zeros(nc+nb, nb)
    weights = [GROUND[min(x,7-x)][min(y,7-y)] for x,y in cells]
    for k,(u,v) in enumerate(bonds):
        C[cells.index(u),k] = -1
        C[cells.index(v),k] = 1
        C[nc+k,k] = 1
        x,y=u
        if v[1]!=y:
            x,y=y,x
        weights.append(BONDS[min(x,6-x)][min(y,7-y)])
    # tr[(C^T D_w C (C^T C)^-1)^2] is the full weighted square of the projector.
    Q = (C.T*C).to_DM()
    inv, den = Q.inv_den(method='charpoly')
    R = (C.T*sp.diag(*weights)*C)*inv.to_Matrix()
    E = Fraction(6*sum(R[i,j]*R[j,i] for i in range(nb) for j in range(nb)), int(den)**2)
    w2 = sum(x*x for x in weights)
    g00 = 1 - Fraction((C.row(0)*inv.to_Matrix()*C.row(0).T)[0],int(den))
    data = json.loads(Path(__file__).with_name('evidence').joinpath('patch.json').read_text())
    assert (Fraction(data['ground_entry']),Fraction(data['norm']),Fraction(data['energy']))==(g00,w2,E)
    print('112 independent cycles, exact normalized quotient', E/w2)
    print('ground Green entry, norm, energy match the direct divergence calculation')


if __name__ == '__main__':
    main()
