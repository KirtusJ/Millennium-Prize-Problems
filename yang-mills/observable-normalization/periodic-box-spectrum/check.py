"""Wilson plaquette Hessian on real helical fields and a Gaussian corrector control."""
from itertools import combinations
from pathlib import Path
import importlib.util
import numpy as np

spec = importlib.util.spec_from_file_location(
    "cube", Path(__file__).resolve().parents[1] / "second-box/transverse-plaquettes/check.py")
cube = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cube)


def action(logs):
    links = cube.qexp(logs)
    total = 0.0
    for i, j in combinations(range(3), 2):
        ui, uj = links[..., i, :], links[..., j, :]
        left = cube.multiply(ui, np.roll(uj, -1, axis=i))
        right = cube.multiply(uj, np.roll(ui, -1, axis=j))
        total += 0.5*np.sum((left-right)**2)
    return total


def helix_slopes(shape):
    phase = 2*np.pi*np.indices(shape)[0]/shape[0]
    unit = np.zeros((*shape, 3, 3))
    unit[..., 0, 2] = 1.0
    e, r = 2e-4, 1e-4
    measured = []
    for sign in (1, -1):
        field = np.zeros_like(unit)
        field[..., 1, 0] = np.cos(phase)/np.sqrt(np.prod(shape))
        field[..., 1, 1] = sign*np.sin(phase)/np.sqrt(np.prod(shape))

        def hessian(t):
            return (action(t*unit+e*field)+action(t*unit-e*field)-2*action(t*unit))/e**2

        measured.append((hessian(r)-hessian(-r))/(2*r))
    expected = 4*np.sin(2*np.pi/shape[0])*np.array([1.,-1.])
    np.testing.assert_allclose(measured,expected,atol=2e-7)
    print(shape,"Wilson slopes", *[f"{x:+.7f}" for x in measured])


def corrector_control():
    # Exact integration of the pair of Gaussian kernels against a Gaussian
    # times a quadratic. Values below are divided by the central ground state.
    p = 2*np.pi/3
    freq = np.arccosh(2-np.cos(p))
    sigma = np.sinh(freq)
    g = np.exp(-freq)
    a = 4*np.sin(p)
    corr = -a/(4*np.tanh(freq))
    points = np.array([[1.,0.], [0.,1.], [0.,0.], [0.5,1.3]])
    squares = points**2
    prev = None
    for t in (.02,.01,.005,.0025):
        weights = 2-np.cos(p+np.array([2*t,-2*t]))
        denom = weights+sigma
        exponent = weights-1/denom-sigma
        out = np.exp(-0.5*(squares@exponent))/np.sqrt(np.prod(denom))
        moments = 1/denom+squares/denom**2
        propagated = out*(1+t*corr*(moments[:,0]-moments[:,1]))
        expected = g*(1+t*corr*(squares[:,0]-squares[:,1]))
        errors = np.array([max(abs(out-g)),max(abs(propagated-expected))])
        print(f"t={t:.4f} uncorrected={errors[0]:.9g} corrected={errors[1]:.9g}")
        if prev is not None:
            ratios = errors/prev
            assert 0.47 < ratios[0] < 0.53 and 0.23 < ratios[1] < 0.27
        prev = errors


if __name__ == '__main__':
    for lengths in [(2,2,2),(3,3,3),(4,3,2),(5,2,2)]:
        helix_slopes(lengths)
    corrector_control()
