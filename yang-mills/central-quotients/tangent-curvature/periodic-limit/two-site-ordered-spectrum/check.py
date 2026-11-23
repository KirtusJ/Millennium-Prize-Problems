"""Test the large singular-value cluster, constant block and Wilson half-weight."""
import importlib.util
from itertools import combinations
from pathlib import Path

import numpy as np

spec = importlib.util.spec_from_file_location("wilson", Path(__file__).resolve().parents[1]/"two-site-exterior/check.py")
wilson = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wilson)
BASIS = np.tile(np.eye(9), (8,1))/np.sqrt(8)
E_STAR = 18*np.arcsinh(1.) + 18*np.arcsinh(np.sqrt(2.)) + 6*np.arcsinh(np.sqrt(3.))


def uniform_links(c):
    norm = np.linalg.norm(c,axis=1)
    vals = (np.cos(norm)[:,None,None]*wilson.I2
            + 1j*np.sinc(norm/np.pi)[:,None,None]*np.einsum("ic,cab->iab",c,wilson.PAULI))
    return np.tile(vals,(8,1,1,1))


def main():
    rng = np.random.default_rng(4221)
    shapes = [np.diag([1.,0.,0.]), np.diag([1.,1.,0.]), np.eye(3),
              np.array([[1.,0.,0.],[.4,.001,0.],[.2,0.,0.]])]
    shapes.extend(rng.normal(size=(3,3)) for _ in range(8))
    hard_max, soft_min = 0., np.inf
    weight_max = 0.
    for shape in shapes:
        shape = shape / np.linalg.norm(shape)
        for radius in (.12, .06, .03, .015):
            c = radius * shape
            links = uniform_links(c)
            jac = wilson.tangent(links)
            sigma = np.linalg.svd(jac,compute_uv=False)
            hard = np.arcsinh(sigma[:42]).sum()
            soft = np.linalg.norm(jac @ BASIS,ord=2)
            hard_max = max(hard_max, abs(hard-E_STAR)/radius**2)
            soft_min = min(soft_min, soft/radius)
            # Orthogonality of the entire spatially constant block to the high cluster.
            # Compare singular values on an explicitly projected nonconstant space.
            nonconstant = jac - jac @ BASIS @ BASIS.T
            high = np.linalg.svd(nonconstant,compute_uv=False)[:42]
            assert np.max(abs(sigma[:42]-high)) < 1e-12
            assert np.arcsinh(sigma).sum() >= hard + np.arcsinh(soft) - 2e-13
            quartic = 16*sum(np.linalg.norm(np.cross(c[i],c[j]))**2 for i,j in combinations(range(3),2))
            flat = np.tile(wilson.I2, (8,3,1,1))
            actual = np.sum((wilson.plaquettes(links)-wilson.plaquettes(flat))**2)/2
            for beta in (10., 1/radius**4, 100/radius**4):
                err = abs(np.exp(-beta*actual/2)-np.exp(-beta*quartic/2))
                weight_max = max(weight_max, err/radius**2)
    assert hard_max < 10 and soft_min > .3 and weight_max < 1
    print(f"48 constant triples; max hard drift/r² {hard_max:.8f}; "
          f"min soft norm/r {soft_min:.8f}; max multiplier error/r² {weight_max:.8f}")


if __name__ == "__main__":
    main()
