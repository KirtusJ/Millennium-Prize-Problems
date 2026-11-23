"""Check the signed cube word in SU(2) and evaluate the finite-torus tangent law."""
from itertools import product

import numpy as np

# (normal direction, shifted face, orientation in the ordered cube word)
FACES = ((0, 0, -1), (1, 1, -1), (2, 0, -1),
         (0, 1, 1), (1, 0, 1), (2, 1, 1))
PAULI = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])


def axes(normal):
    return [a for a in range(3) if a != normal]


def spin_exp(v):
    angle = np.linalg.norm(v)
    return np.cos(angle)*np.eye(2) + 1j*np.sinc(angle/np.pi)*(v @ PAULI.reshape(3, 4)).reshape(2, 2)


def spin_log(u):
    vec = np.einsum("aij,ji->a", PAULI, u).imag / 2
    norm = np.linalg.norm(vec)
    return vec * (np.arctan2(norm, np.trace(u).real/2)/norm) if norm else vec


def cube_check():
    rng = np.random.default_rng(44397)
    logs = {(v, j): rng.normal(size=3) for v, j in product(range(8), range(3)) if not v & (1 << j)}
    for eps in (0.01, 0.005, 0.0025):
        u = {e: spin_exp(eps*g) for e, g in logs.items()}
        word = np.eye(2)
        scaled = []
        for n, upper, sign in FACES:
            i, j = axes(n)
            v = upper << n
            h = u[v, i] @ u[v+(1 << i), j] @ u[v+(1 << j), i].conj().T @ u[v, j].conj().T
            if upper:
                h = u[0, n] @ h @ u[0, n].conj().T
            h = h if sign == 1 else h.conj().T
            word = word @ h
            scaled.append(spin_log(h)/eps)
        assert np.linalg.norm(word-np.eye(2)) < 1e-12
        q = sum(np.cross(x, y) for i, x in enumerate(scaled) for y in scaled[i+1:])
        residual = np.linalg.norm(np.sum(scaled, axis=0)/eps-q)
        assert residual <= eps * sum(map(np.linalg.norm, scaled))**3/6
        print(f"eps={eps:g} defect={np.linalg.norm(np.sum(scaled, axis=0)/eps):.7f} remainder={residual:.7f}")


def periodic_covariance(size):
    # For each frequency use curl times independent link polarizations / |d|.
    phase = np.exp(2j*np.pi*np.arange(size)/size)
    xyz = np.stack(np.meshgrid(phase, phase, phase, indexing="ij"), axis=-1).reshape(-1, 3)
    diff = xyz-1
    weights = np.zeros((len(xyz), 6, 3), complex)
    for f, (n, upper, sign) in enumerate(FACES):
        i, j = axes(n)
        factor = sign * xyz[:, n]**upper
        weights[:, f, j] = factor*diff[:, i]
        weights[:, f, i] = -factor*diff[:, j]
    spatial = np.sum(abs(diff)**2, axis=1)
    inverse = np.zeros(len(xyz))
    for p in phase:
        total = spatial + abs(p-1)**2
        inverse += np.divide(1, total, out=np.zeros_like(total), where=total>0)
    gram = np.einsum("kfi,kgi,k->fg", weights, weights.conj(), inverse).real / size**4
    eigen, basis = np.linalg.eigh(gram)
    assert abs(eigen[0]) < 1e-12 and eigen[1] > 0.1
    assert np.max(abs(gram.sum(axis=1))) < 1e-12
    root = (basis*np.sqrt(np.maximum(eigen, 0))) @ basis.T
    upper = np.triu(np.ones((6, 6)), 1)
    singular = np.linalg.svd(root @ (upper-upper.T) @ root, compute_uv=False)
    assert np.max(abs(singular[::2]-singular[1::2])) < 1e-12 and singular[4] < 1e-7
    scales = singular[[0, 2]]
    print(f"M={size} scales={scales[0]:.8f},{scales[1]:.8f} variance={2*(scales @ scales):.8f}")


if __name__ == "__main__":
    cube_check()
    for m in (8, 16, 32, 48):
        periodic_covariance(m)
