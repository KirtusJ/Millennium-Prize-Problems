"""Evaluate the complete smooth, sheared Airy-Gaussian trial in flat measure."""
import numpy as np
from scipy.special import airy, ai_zeros, roots_genlaguerre, roots_legendre


def trial(radius, order):
    node, weight = roots_legendre(order)
    m, radial_weight = roots_genlaguerre(order, 1)
    # For a uniform direction on S^3, 2 det(B)/|B|^2 is uniform on [-1,1].
    orientation = node[None, :]
    z = 9*(1+node)
    zero = ai_zeros(1)[0][0]
    f, fp = airy(2*z+zero)[:2]
    fp *= 2
    mass = shifted_energy = 0.
    for y, value, deriv, longitudinal_weight in zip(radius+z, f, fp, 9*weight):
        h = m/(2*y)
        ratio = h/(radius*y)
        keep = ratio < 1/16
        h, ratio = h[keep], ratio[keep]
        phase = np.pi/2*np.clip(32*ratio-1, 0, 1)
        cutoff = np.cos(phase)
        dc = -16*np.pi*np.sin(phase)*(ratio > 1/32)
        state = value*cutoff
        dx = cutoff*(deriv+(1/y-h)*value) - value*dc*ratio/y
        db = -2*y*state + 2*value*dc/(radius*y) + dx/radius
        x = y-h/(2*radius)
        det2 = (h[:, None]*orientation/2)**2
        jac = (x**4-x*x*h)[:, None]+det2
        grad2 = ((4*x**3-2*x*h)[:, None])**2 + (4*x**4*h)[:, None]
        grad2 = grad2 + (4*h-16*x*x)[:, None]*det2
        geom = x[:, None]**2/jac - grad2/(8*jac**2)
        pot = (2*x*x*h-4*radius)[:, None]+2*det2+geom
        energy = (dx*dx+h*db*db)/2 + state**2*(pot @ (weight/2))
        mass += longitudinal_weight*(radial_weight[keep] @ state**2)
        shifted_energy += longitudinal_weight*(radial_weight[keep] @ energy)
    return radius**2*(shifted_energy/mass+2*zero)


if __name__ == "__main__":
    for radius in (8, 16, 32, 64, 128):
        values = [trial(radius, order) for order in (48, 72)]
        assert abs(values[0]-values[1]) < 1e-6
        print(radius, *(f"{x:.8f}" for x in values))
