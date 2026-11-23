"""Point calculations of the static term, midpoint and signed four-lag contrast."""
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import eigh

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from spectrum import integrate, states

SECTORS = ((0,0,0),(1,0,0),(0,1,1),(1,1,1))
MULTIPLICITIES = (1,3,3,1)


def spectra(cutoff, order):
    output = []
    for matrix, *insertions in integrate([states(p,cutoff) for p in SECTORS],order):
        eig, vectors = eigh(matrix)
        assert eig[0]>0
        gram = sum((vectors.T@op@vectors)**2 for op in insertions)/(2*np.outer(eig,eig))
        output.append((eig,gram))
    return output


def report(values, period):
    lam = values[0][0][-1]
    Z = 0
    static = midpoint = 0
    parts = []
    for k,((eig,gram),mult) in enumerate(zip(values,MULTIPLICITIES)):
        u = eig/lam
        Z += mult*sum(u**period)
        static += mult*u[-1]**period*gram[-1,-1] if k in (1,2) else 0
        midpoint += mult*((u**(period//2))@gram@(u**(period//2)))
        # Four fixed lags. Circle time includes both orientations of every transition.
        weights = [np.outer(u**(period-t),u**t) for t in (1,2,3,4)]
        kernel = -weights[0]+(13/3)*weights[1]-(13/3)*weights[2]+weights[3]
        terms = mult*gram*kernel
        if k==0:
            vacuum = terms[-1,:-1].sum()+terms[:-1,-1].sum()
            parts += [vacuum,terms.sum()-vacuum]
        else:
            parts.append(terms.sum())
    parts=np.array(parts)/Z
    print(f"T={period} top static {static/Z:.9f} midpoint {midpoint/Z:.9f} signed W {sum(parts):.9f}")
    print("  W vacuum, other neutral, one/two/three odd:", " ".join(f"{x:+.9f}" for x in parts))


if __name__=="__main__":
    for cutoff,order in ((0.0003,32),(0.0001,36)):
        print(f"electric cutoff {cutoff}, quadrature {order}")
        values=spectra(cutoff,order)
        for T in (16,24,48):
            report(values,T)
