"""Check A4's flat-vacuum overlap using real site and color coordinates."""
from pathlib import Path
import importlib.util
import numpy as np
from scipy.linalg import block_diag, expm, expm_frechet, null_space, polar


def charged_link(delta):
    """Right-trivialized orbit rotation and additive-to-link derivative in SU(2)."""
    background = np.diag([0.5j * delta, -0.5j * delta])
    link = expm(background)
    generators = [np.array([[0, z], [-z.conjugate(), 0]]) for z in (1., 1j)]
    orbit = []
    tangent = []
    for generator in generators:
        rotated = (link @ generator @ link.conj().T)[0, 1]
        derivative = expm_frechet(background, generator, compute_expm=False)
        shifted = (derivative @ link.conj().T)[0, 1]
        orbit.append([rotated.real, rotated.imag])
        tangent.append([shifted.real, shifted.imag])
    return np.array(orbit).T, np.array(tangent).T


def hard_plane(shifts, rotation):
    identity = np.eye(shifts[0].shape[0] * 2)
    differences = [identity - np.kron(shift, color)
                   for shift, color in zip(shifts, [rotation, np.eye(2), np.eye(2)])]
    orbit = np.vstack(differences)
    transverse = null_space(orbit.T)
    assert transverse.shape[1] == 2 * identity.shape[0]
    values, vectors = np.linalg.eigh(orbit.T @ orbit)
    assert min(values) > 0
    width = (vectors * np.sqrt(values * (1 + values / 4))) @ vectors.T
    return transverse, transverse.T @ np.kron(np.eye(3), width) @ transverse


def loss(first, second):
    """Negative log of the unsquared overlap of two normalized real Gaussians."""
    def logdet(matrix):
        sign, value = np.linalg.slogdet(matrix)
        assert sign > 0
        return value
    return (2 * logdet((first + second) / 2) - logdet(first) - logdet(second)) / 4


def readback(size, theta):
    count = size**3
    sites = np.arange(count).reshape((size,) * 3)
    mean_zero = null_space(np.ones((1, count)))
    shifts = [mean_zero.T @ mean_zero[np.roll(sites, -1, axis=j).ravel()] for j in range(3)]
    rotation, differential = charged_link(theta / size)
    plane0, width0 = hard_plane(shifts, np.eye(2))
    plane1, width1 = hard_plane(shifts, rotation)
    identity = np.eye(2 * (count - 1))
    def correction(link_map):
        derivative = block_diag(np.kron(np.eye(count - 1), link_map), identity, identity)
        projected = plane1.T @ derivative @ plane0
        isometry, _ = polar(projected)
        return loss(width0, projected.T @ width1 @ projected) - loss(width0, isometry.T @ width1 @ isometry)
    return plane0.shape[1], correction(differential), correction(differential.T)


if __name__ == "__main__":
    source = (Path(__file__).resolve().parents[1] / "observable-normalization"
              / "periodic-box-spectrum" / "plane-overlap" / "check.py")
    spec = importlib.util.spec_from_file_location("a4_planes", source)
    a4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(a4)
    for size in (2, 3, 4):
        for theta in (-0.5, 0.25, 0.5):
            dimension, actual, wrong_phase = readback(size, theta)
            expected = a4.lattice(size, theta)
            print(f"N={size} theta={theta:+.2f} dim={dimension} D={actual:.10g} "
                  f"error={abs(actual - expected):.2g} reversed_phase_error={abs(wrong_phase - expected):.2g}")
            assert abs(actual - expected) < 2e-12
            assert abs(wrong_phase - expected) > 1e-7
