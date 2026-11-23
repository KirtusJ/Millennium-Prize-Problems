"""Integrate the flat-measure trial norm and full kinetic and potential forms."""
import numpy as np
from scipy.special import airy, ai_zeros, roots_genlaguerre, roots_legendre


def shifted_energy(radius, shear, order):
    # z - R in [0,16], y=2*z*|B|^2 has Gamma(2,1) density under g_z^2.
    t, weights = roots_legendre(order)
    z = radius + 8 * (1 + t[:, None])
    zero = ai_zeros(1)[0][0]
    a, derivative, _, _ = airy(2*(z-radius) + zero)
    derivative *= 2
    y, radial_weights = roots_genlaguerre(order, 1)
    d2 = y / (2*z)
    d = np.sqrt(d2)
    x = z - shear*d2/(2*radius)
    phase = np.pi/2 * np.clip(d-1, 0, 1)
    cutoff = np.where(d < 2, np.cos(phase), 0)
    cutoff_prime = np.where((d > 1) & (d < 2), -np.pi/2*np.sin(phase), 0)
    # Derivatives at fixed B in z, then at fixed physical x in the radial direction.
    dz = derivative + a*(1/z-d2)
    db = cutoff*d*(shear*dz/radius - 2*z*a) + a*cutoff_prime
    kinetic = 0.5*((cutoff*dz)**2 + db**2)
    norm = (cutoff*a)**2
    v, angular_weights = roots_legendre(12)
    mean_potential = np.zeros_like(x)
    for cosine, weight in zip(v, angular_weights):
        determinant_sq = d2**2 * cosine**2 / 4
        w = x**4 - x*x*d2 + determinant_sq
        grad_sq = ((4*x**3-2*x*d2)**2 + 4*x**4*d2
                   - 16*x*x*determinant_sq + 4*determinant_sq*d2)
        jacobian_potential = x*x/w - grad_sq/(8*w*w)
        mean_potential += weight/2*(2*x*x*d2 + 2*determinant_sq + jacobian_potential)
    quadrature = weights[:, None]*8*radial_weights
    # Subtract the two leading terms before the final reduction.
    return radius**2 * np.sum(quadrature*(kinetic+(mean_potential-4*radius+2*zero)*norm)) / np.sum(quadrature*norm)


if __name__ == '__main__':
    for radius in (16, 32, 64, 128):
        for shear in (0, .5, 1):
            first = shifted_energy(radius, shear, 64)
            second = shifted_energy(radius, shear, 96)
            print(f'{radius:3} {shear:.1f} {second:+.8f}  quadrature shift {second-first:+.2e}')
            assert abs(second-first) < 2e-6
