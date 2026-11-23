"""Direct two-particle window integration on the Wilson dipole tangent law."""
from math import asinh, pi, sin, sqrt

import numpy as np
from numpy.polynomial.legendre import leggauss


def sine_norm(q):
    return np.linalg.norm(np.sin(q/2), axis=-1)


def omega(q):
    return 2*np.arcsinh(sine_norm(q))


def spectral_weight(q):
    h = 2*np.sin(q/2)
    numerator = h[..., 2]**2 * (h[..., 0]**2+h[..., 1]**2)
    denominator = 2*np.sinh(omega(q))
    return np.divide(numerator, denominator, out=np.zeros_like(numerator), where=denominator>0)


def angular_rule(order):
    z, weight = leggauss(order)
    angles = np.arange(2*order)*pi/order
    radius = np.sqrt(1-z**2)[:, None]
    theta = np.stack([radius*np.cos(angles), radius*np.sin(angles),
                      np.broadcast_to(z[:, None], (order,2*order))], axis=-1)
    return theta.reshape(-1,3), np.repeat(weight*pi/order, 2*order)


def coefficient(k, theta, weights, node):
    a = theta[:,2]**2 * (theta[:,0]**2+theta[:,1]**2)/2
    if node == "rest":
        return 9, 6*(weights @ a**2)/(9*2**9*(2*pi)**3)
    h = 2*np.sin(k/2)
    den = 2*np.sinh(omega(k))
    velocity = np.sin(k)/np.sinh(omega(k))
    if node == "plane":
        power, hard = 8, theta[:,2]**2*(h[0]**2+h[1]**2)/den
    elif node == "axis":
        power, hard = 8, (theta[:,0]**2+theta[:,1]**2)*h[2]**2/den
    else:
        power, hard = 6, spectral_weight(k)
    value = weights @ (a*hard/(1-theta@velocity)**power)
    return power, 12*value/(power*(2*pi)**3)


def window(k, theta, weights, width):
    # Outside these one or two balls the strict dispersion separation exceeds width.
    radius = .2
    rest = bool(np.all(k == 0))
    small = radius/pi
    large = max(small, sine_norm(k)/2)
    separation = 2*(asinh(small)+asinh(large)-asinh(small+large))
    assert width < (4*asinh(small) if rest else separation)
    if not rest:
        assert np.linalg.norm(k) > 2*radius  # k is in the principal cube
        radial_slope = sin(radius)/radius/sqrt(1+radius**2/4)
        assert radial_slope > 1/sqrt(1+(sine_norm(k)-radius/2)**2)
        assert sine_norm(k) > radius/2
    lo = np.zeros(len(theta))
    hi = np.full(len(theta), radius)
    edge = omega(k)
    for _ in range(48):
        mid = (lo+hi)/2
        q = mid[:,None]*theta
        inside = omega(q)+omega(k-q) <= edge+width
        lo = np.where(inside, mid, lo)
        hi = np.where(inside, hi, mid)
    limits = (lo+hi)/2
    nodes, radial_weights = leggauss(18)
    r = limits[:,None]*(nodes+1)/2
    q = r[:,:,None]*theta[:,None,:]
    radial = (r**2 * spectral_weight(q) * spectral_weight(k-q)) @ radial_weights
    return 6*(1 if rest else 2)*(weights @ (limits*radial/2))/(2*pi)**3


def momentum_convolution():
    side = 10
    coordinates = np.indices((side,)*3).transpose(1,2,3,0)
    k = coordinates*(2*pi/side)
    for t in (0, 1, 3):
        measure = spectral_weight(k)*np.exp(-t*omega(k))
        covariance = np.fft.ifftn(measure)
        squared = np.fft.fftn(6*covariance**2)
        for point in ((0,0,0), (3,1,2), (2,2,0), (0,0,4)):
            complement = (np.array(point)-coordinates)%side
            partner = measure[tuple(complement.transpose(3,0,1,2))]
            direct = 6*np.mean(measure*partner)
            np.testing.assert_allclose(squared[point], direct, atol=1e-14)
    print("Twelve momentum/lag projections agree before and after spatial Fourier transform.")


def main():
    momentum_convolution()
    theta, weights = angular_rule(42)
    rng = np.random.default_rng(4112)
    p, q = rng.uniform(-pi,pi,(2,8000,3))
    assert np.min(omega(p)+omega(q)-omega(p+q)) > 0
    for node, coords in [("generic",(1.5,.7,1.2)), ("plane",(1.5,.7,0)),
                         ("axis",(0,0,1.8)), ("rest",(0,0,0))]:
        k = np.array(coords)
        power, exact = coefficient(k, theta, weights, node)
        finer = coefficient(k, *angular_rule(64), node)[1]
        np.testing.assert_allclose(exact,finer,rtol=1e-9,atol=0)
        if node == "rest":
            np.testing.assert_allclose(exact,1/(241920*pi**2),rtol=1e-12,atol=0)
        ratios = []
        for width in (.002, .001, .0005):
            actual = window(k, theta, weights, width)
            ratios.append(actual/(width**power*exact))
        assert abs(ratios[-1]-1) < .02
        print(node, coords, power, f"{exact:.10g}", *[f"{r:.7f}" for r in ratios])


if __name__ == "__main__":
    main()
