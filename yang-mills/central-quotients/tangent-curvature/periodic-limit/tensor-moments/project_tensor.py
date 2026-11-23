"""FOR DISPROOF: direct spin-two Ritz projection of the bounded tensor.

Run with OPENBLAS_NUM_THREADS=1. The normalized tensor inner product uses
trace on covariants. The common spatial orientation factor 1/10 cancels in
all normalized spectral fractions. Gradients act on all nine matrix entries.
"""
import numpy as np
from scipy.linalg import eigh

from estimate import integration_grid, scalar_basis


def whitened_eigensystem(hamiltonian, overlap, tolerance):
    norms = np.sqrt(np.diag(overlap))
    metric = overlap / norms[:, None] / norms
    eig, rotation = eigh(metric)
    keep = eig > tolerance
    transform = rotation[:, keep] / np.sqrt(eig[keep]) / norms[:, None]
    reduced = transform.T @ hamiltonian @ transform
    energy, vectors = eigh((reduced + reduced.T) / 2)
    return energy, transform @ vectors


def traceless(diagonal):
    return diagonal - diagonal.mean(axis=1, keepdims=True)


def weighted_product(columns, weight):
    return columns.T @ (weight[:, None] * columns)


def calculate(degree, precision, radial_order, angular_order, tolerance=1e-12):
    x, weight = integration_grid(precision, radial_order, angular_order)
    scalar, gradient, potential_half = scalar_basis(x, weight, precision, degree)
    potential = 2 * potential_half
    h = weighted_product(scalar, weight * potential)
    for i in range(3):
        h += weighted_product(gradient[:, :, i].T, weight / 2)
    energies, states = whitened_eigensystem(h, weighted_product(scalar, weight), tolerance)
    vacuum = scalar @ states[:, 0]

    # All covariants here are invariant under color reflections as well as rotations.
    # Use Q and Q^2 times the invariant polynomials, with equal total degree cutoff.
    q = x ** 2
    tensor = []
    for power in (1, 2):
        b, g, _ = scalar_basis(x, weight, precision, degree-power)
        tensor.append((power, b, g, traceless(q**power)))

    dimension = sum(b.shape[1] for _, b, _, _ in tensor)
    overlap = np.zeros((dimension, dimension))
    h = np.zeros_like(overlap)
    # Shape of each array of evaluated columns is (quadrature points, basis size).
    columns = []
    for j in range(3):
        values = np.column_stack([b * v[:, j, None] for _, b, _, v in tensor])
        columns.append(values)
        overlap += weighted_product(values, weight)
        h += weighted_product(values, weight * potential)
        for i in range(3):
            pieces = []
            for power, b, g, v in tensor:
                dv = 2*x[:, i]*power*q[:, i]**(power-1)*((i == j)-1/3)
                pieces.append(g[:, :, i].T*v[:, j, None] + b*dv[:, None])
            h += weighted_product(np.column_stack(pieces), weight / 2)

    # At diagonal x the derivative of Q^2 in entry ij is (q_i+q_j) dQ_ij.
    # Both off-diagonal tensor entries contribute to the Frobenius norm.
    for i, j in ((0, 1), (0, 2), (1, 2)):
        values = np.column_stack((tensor[0][1], tensor[1][1]*(q[:, i]+q[:, j])[:, None]))
        h += weighted_product(values, weight*(q[:, i]+q[:, j]))

    tensor_energies, vectors = whitened_eigensystem(h, overlap, tolerance)
    trace = q.sum(axis=1)
    probe = vacuum[:, None]*traceless(q)/(1+trace[:, None])

    def project(reading):
        moment = sum(values.T @ (weight * reading[:, j]) for j, values in enumerate(columns))
        return vectors.T @ moment

    norm = weight @ (probe*probe).sum(axis=1)
    amplitude = project(probe)
    radial = trace/(1+trace)
    modified = project(probe*radial[:, None])
    cancel = modified[0]/amplitude[0]
    return (tensor_energies[:2]-energies[0], amplitude[0]**2/norm,
            np.sum(amplitude**2)/norm, cancel, radial, probe, weight, project)


if __name__ == "__main__":
    training = calculate(5, 2., 48, 10)[3]
    for degree, a, nr, na in ((5,2.,48,10),(7,2.,56,12),(8,2.6,60,14),(9,2.,64,16)):
        gaps, fraction, captured, _, radial, probe, weight, project = calculate(degree,a,nr,na)
        control = probe*(radial-training)[:,None]
        control_fraction = project(control)[0]**2 / (weight @ (control**2).sum(axis=1))
        print(degree, a, "gaps", gaps, "p1", fraction, "captured", captured,
              "fixed control offset", training, "control p1", control_fraction)
