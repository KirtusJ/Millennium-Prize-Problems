"""Exercise tree reduction and contraction on almost-flat noncommuting links."""
from itertools import combinations
import numpy as np
from check import I2, NEXT, BITS, PAULI, adj


def expq(v):
    theta = np.linalg.norm(v, axis=-1)
    return (np.cos(theta)[...,None,None]*I2
            + 1j*np.einsum("...c,cij->...ij", v, PAULI)*np.sinc(theta/np.pi)[...,None,None])


def distance(a,b):
    return np.linalg.norm(a-b, axis=(-1,-2))/np.sqrt(2)


def max_curvature(links):
    return max(distance(links[:,i] @ links[NEXT[:,i], j],
                        links[:,j] @ links[NEXT[:,j], i]).max()
               for i,j in combinations(range(3), 2))


def main():
    rng = np.random.default_rng(829)
    for s in (.03, .003, .0003):
        for _ in range(20):
            generators = rng.normal(size=(3, 3))*np.sqrt(s)
            signs = rng.choice([-1,1], size=3)
            hol = signs[:,None,None]*expq(generators)
            seam = np.where(BITS[...,None,None] == 1, hol[None], I2)
            noisy = expq(rng.normal(size=(8,3,3))*s) @ seam
            gauge = expq(rng.normal(size=(8,3)))
            original = gauge[:,None] @ noisy @ adj(gauge[NEXT])
            defect = max_curvature(original)
            tree = []
            for bits in BITS:
                x, p = 0, I2
                for i in np.flatnonzero(bits):
                    p = p @ original[x,i]
                    x = NEXT[x,i]
                tree.append(p)
            tree = np.array(tree)
            fixed = tree[:,None] @ original @ adj(tree[NEXT])
            cycles = original[0] @ original[NEXT[0],np.arange(3)]
            model = np.where(BITS[...,None,None] == 1, cycles[None], I2)
            assert distance(fixed,model).max() <= 49*defect
            # Recover an angle at most pi/2 in each cycle by removing its center.
            central = np.where(cycles.trace(axis1=-2,axis2=-1).real>=0,1,-1)
            signed = cycles*central[:,None,None]
            vec = np.array([np.trace(signed @ p, axis1=-2,axis2=-1).imag/2 for p in PAULI]).T
            size = np.linalg.norm(vec,axis=1)
            theta = np.arctan2(size,signed.trace(axis1=-2,axis2=-1).real/2)
            log = vec*(theta/size)[:,None]
            for t in np.linspace(0,1,11):
                path = central[:,None,None]*expq(t*log)
                candidate = np.where(BITS[...,None,None]==1,path[None],I2)
                assert max_curvature(candidate) <= 4*defect+2e-14
    print("60 perturbed, gauge-transformed cube configurations; 660 seam contraction checks passed")


if __name__ == "__main__":
    main()
