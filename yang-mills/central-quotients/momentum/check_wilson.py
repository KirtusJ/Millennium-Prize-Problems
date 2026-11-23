"""Finite-dimensional controls for the averaged Gram estimate and a coherent zero mode."""
import numpy as np


def centered_columns(operators, vacuum):
    raw = operators @ vacuum
    means = np.einsum("i,nji->nj", vacuum.conj(), raw)
    return (raw - means[..., None]*vacuum).transpose(0, 2, 1)


def check(count, time):
    angle = .04
    rot = np.array([[np.cos(angle), -np.sin(angle), 0.],
                    [np.sin(angle), np.cos(angle), 0.], [0., 0., 1.]])
    vacuum = np.eye(3)[:, 0]
    other = rot @ vacuum
    T = np.diag(np.exp(-time*np.array([0., 1., 2.])))
    U = rot @ np.diag(np.exp(-time*np.array([0., 1.03, 2.1]))) @ rot.T
    base = np.array([[.3,.5,.1],[.5,-.4,.2],[.1,.2,0.]])
    b = np.array([[.1,0.,.6],[0.,.3,.1],[.6,.1,-.4]])
    operators = np.array([[base, np.cos(2*np.pi*x/count)*b,
                           np.sin(2*np.pi*x/count)*base] for x in range(count)])
    M = max(np.linalg.norm(f, 2) for site in operators for f in site)
    A = np.fft.fft(centered_columns(operators, vacuum), axis=0, norm="ortho")
    B = np.fft.fft(centered_columns(operators, other), axis=0, norm="ortho")
    grams = B.conj().transpose(0,2,1) @ U @ B - A.conj().transpose(0,2,1) @ T @ A
    errors = np.linalg.svd(grams, compute_uv=False).sum(axis=1)
    v = np.linalg.norm(vacuum-other)
    h = np.linalg.norm(U-T, 2)
    bound = M*M*(12*v+3*h)
    if errors.mean() > bound + 1e-12 or abs(errors[0] - errors.max()) > 1e-10:
        raise ValueError("mean bound or coherent-mode control failed")
    return errors.mean(), errors.max(), bound


if __name__ == "__main__":
    for time in (0., .7, 2.):
        small = check(8, time)
        large = check(256, time)
        if not np.allclose([large[0],large[1]/32], small[:2]) or large[1] <= large[2]:
            raise ValueError("averaging could not be distinguished from a uniform mode estimate")
        print(f"t={time:g} average={large[0]:.8f} maximum={large[1]:.8f} bound={large[2]:.8f}")
