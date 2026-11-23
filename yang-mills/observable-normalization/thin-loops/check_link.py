"""Cross-check the two conditional Fourier coefficients with angular quadrature."""
import numpy as np
from scipy.special import ive, roots_jacobi


def main():
    x, weight = roots_jacobi(512, 0.5, 0.5)
    largest = 0.
    for h in (0., 0.01, 0.5, 1., 6., 48., 256.):
        w = weight * np.exp(h * (x - 1.))
        w /= w.sum()
        r = w @ x
        s = w @ ((4*x*x - 1)/3)
        refs = (0., 0.) if h == 0 else (ive(2,h)/ive(1,h), ive(3,h)/ive(1,h))
        residuals = [abs(r-refs[0]), abs(s-refs[1]),
                     abs(3*r - h*(w @ (1-x*x))),
                     abs(3*s - h*(w @ (x*(1-x*x))))]
        largest = max(largest, *residuals)
        if not (-1e-12 <= s <= r + 1e-12 and r <= 2*h/(2*h+3) + 1e-12):
            raise ValueError((h, r, s))
    if largest > 1e-9:
        raise ValueError(largest)
    print(f"largest absolute quadrature residual: {largest:.4g}")
    # At beta zero a forward-backtracking word has normalized trace one.
    # Treating its two visits as independent selected edges predicts zero.
    for theta in (0.1, 0.7, 2.1):
        link = np.diag(np.exp(1j*np.array([theta, -theta])))
        assert np.isclose(np.trace(link @ link.conj().T).real/2, 1)


if __name__ == "__main__":
    main()
