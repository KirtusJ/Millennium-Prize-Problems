"""Integrate the pinned Wilson fluctuations and the residual S^3 orientation separately."""
import sys
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.linalg import null_space
from scipy.special import hyp1f1, i0e, ndtri
from scipy.stats import qmc

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "central-quotients" / "tangent-curvature" /
                       "periodic-limit" / "flat-electric-kernel"))
from check_kernel import BITS, FOURIER, NEIGHBORS, blocks, links


def product(a, b):
    return np.concatenate(((a[..., :1]*b[..., :1] -
                            (a[..., 1:]*b[..., 1:]).sum(axis=-1, keepdims=True)),
                           a[..., :1]*b[..., 1:] + b[..., :1]*a[..., 1:] +
                           np.cross(a[..., 1:], b[..., 1:])), axis=-1)


def fields(beta, seed):
    # Exact north chart of seven site quaternions pinned at site zero.
    incidence = (np.eye(8)[:, None, :] - np.eye(8)[NEIGHBORS]).reshape(24,8)[:,1:]
    precision = incidence.T @ incidence
    points = qmc.Sobol(21, scramble=True, seed=seed).random_base2(13)
    white = ndtri(points).reshape(-1,7,3)
    tangent = np.linalg.inv(np.linalg.cholesky(precision).T) @ white / np.sqrt(beta)
    tangent = np.pad(tangent, ((0,0),(1,0),(0,0)))
    radius2 = (tangent**2).sum(axis=-1)
    assert np.max(radius2) < 1
    scalars = np.sqrt(1-radius2)
    pinned = np.concatenate((scalars[...,None], tangent), axis=-1)
    # Exact S0 differs from the proposal's quadratic action only in the scalar coordinate.
    scalar_cost = .5*((scalars[:,:,None] - scalars[:,NEIGHBORS])**2).sum(axis=(1,2))
    weights = np.exp(-beta*scalar_cost)/np.prod(scalars, axis=1)
    mean = pinned.mean(axis=1)
    inverse = mean / np.linalg.norm(mean, axis=1)[:,None]
    inverse[:,1:] *= -1
    return product(inverse[:,None,:], pinned), weights


def orientation(eigenvalues, beta):
    # Separate the squared radii of two complex coordinates. Return log F stably.
    l0,l1,l2,l3 = np.sort(eigenvalues)
    alpha, gap, gamma = 4*beta*(l1-l0), 8*beta*(l2-l0), 4*beta*(l3-l2)
    val = quad(lambda p: np.exp(-gap*p)*i0e(alpha*(1-p))*i0e(gamma*p),
               0, 1, epsabs=1e-14)[0]
    return -8*beta*l0 + np.log(val)


def main():
    rng = np.random.default_rng(503)
    cases = [(np.eye(3)*1.4, np.eye(3)*.6),
             (rng.normal(size=(3,3)), rng.normal(size=(3,3))),
             (np.eye(3), np.zeros((3,3)))]
    orientations = np.array([[1.,0,0,0], [.5,.5,-.5,.5]])
    linear_errors, determinant_errors = [], []
    for beta in (128., 2048.):
        mean_frame, weights = fields(beta, seed=463)
        linear, determinant = [], []
        for x,y in cases:
            h = beta**(-1/3)
            H, _ = blocks(links(h*x),links(h*y))
            residual = H[1:] - np.eye(4)*((2*BITS[1:].sum(axis=1))[:,None,None])
            for u in orientations:
                modes = FOURIER @ product(u, mean_frame)
                a = u @ H[0] @ u
                diff = np.einsum("nki,kij,nkj->n", modes[:,1:],
                                 residual-a*np.eye(4), modes[:,1:])
                ratio_minus_one = np.average(np.expm1(-beta*diff), weights=weights)
                predicted = (88*a-np.trace(H[0]))/24
                err = abs(ratio_minus_one-predicted)/h**2
                tangent = null_space(u[None,:])
                gram = tangent.T @ (residual-a*np.eye(4)) @ tangent
                gram /= (2*BITS[1:].sum(axis=1))[:,None,None]
                log_prefactor = -.5*np.linalg.slogdet(np.eye(3)+gram)[1].sum()
                linear.append(err)
                determinant.append(abs(ratio_minus_one-np.expm1(log_prefactor))/h**2)
        linear_errors.append(max(linear))
        determinant_errors.append(max(determinant))
    # The first correction resolves the direction of change, and resumming the
    # quadratic determinant resolves the finite-beta nonlinear deviation.
    assert linear_errors[1] < linear_errors[0]/3
    assert max(determinant_errors) < min(linear_errors)
    for t in (0.,1.,20.,200.):
        # Two-dimensional and isolated minima, and a common action that underflows.
        for mult in (2, 1):
            vals = np.array([0]*mult+[1]*(4-mult), dtype=float)
            expected = np.log(hyp1f1((4-mult)/2,2,-t))
            assert abs(orientation(vals+60,t/8) + 60*t - expected) < 3e-12
    print("Maximum discrepancy / h² at beta=128,2048:", linear_errors, determinant_errors)
    print("Eight orientation quadratures passed, including equal and isolated minima.")


if __name__ == "__main__":
    main()
