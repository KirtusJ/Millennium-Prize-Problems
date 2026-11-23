"""Check the magnetic expansion in additive slice coordinates on actual cube links."""
import importlib.util
from pathlib import Path
import numpy as np

spec = importlib.util.spec_from_file_location(
    "cube", Path(__file__).resolve().parents[1] / "transverse-plaquettes" / "check.py")
cube = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cube)
zero = np.zeros((3, 3))


def curl_energy(z):
    total = 0.0
    for i, j in cube.pairs:
        forward_i = np.arange(8) ^ (1 << (2-i))
        forward_j = np.arange(8) ^ (1 << (2-j))
        curl = z[:, i] + z[forward_i, j] - z[forward_j, i] - z[:, j]
        total += np.sum(curl**2)/2
    return total


def additive_hessian(background, fields):
    eps = 0.0002
    rows = []
    for f in fields:
        d, e = eps*(f+fields), eps*(f-fields)
        rows.append((cube.action(background+d, zero)+cube.action(background-d, zero)
                     -cube.action(background+e, zero)-cube.action(background-e, zero))/(4*eps**2))
    return np.array(rows)


def main():
    x = np.array([[0.21, -0.13, 0.1], [0.07, 0.12, -0.19], [-0.15, 0.09, 0.14]])
    z = np.tensordot(np.random.default_rng(812).normal(size=42), cube.basis(), axes=1)
    z /= np.linalg.norm(z)
    v = 16*sum(np.linalg.norm(np.cross(x[i], x[j]))**2 for i, j in cube.pairs)
    # Averaging over these four proper color rotations kills every linear covector.
    rotations = np.array([[1,1,1], [1,-1,-1], [-1,1,-1], [-1,-1,1]])
    previous = None
    for h in [0.08, 0.04, 0.02, 0.01, 0.005]:
        s = h**1.5
        slopes = []
        for signs in rotations:
            # Symmetrize the hard field to isolate a possible background-linear Hessian.
            p = cube.action(h*x + s*z*signs, zero)
            m = cube.action(h*x - s*z*signs, zero)
            slopes.append(((p+m)/(2*s*s)-curl_energy(z))/h-v)
        mean = np.mean(slopes)
        print(f"h={h:.3f}  slope={slopes[0]:+.7f}  rotated mean={mean:+.7f}")
        if previous is not None:
            assert np.all(np.abs(slopes) < 0.65*np.abs(previous))
        previous = slopes
    # Raw directions as well as their color average tend to zero.
    assert max(np.abs(slopes)) < 0.002
    fields = cube.basis()
    central = additive_hessian(np.zeros((3,3)), fields)
    np.testing.assert_allclose(np.linalg.eigvalsh(central), np.repeat([4,8,12],[18,18,6]),
                               rtol=0, atol=5e-7)
    quotients = []
    for t in (0.2,0.1,0.05):
        delta = additive_hessian(t*x, fields)-central
        quotients.append(np.linalg.norm(delta,2)/t**2)
    print("hard Hessian norm difference/t²:", quotients)
    assert 0.97 < quotients[2]/quotients[0] < 1.03
    r = 0.0001
    derivative = lambda p: (abs(np.exp(1j*(p+2*r))-1)**2
                            - abs(np.exp(1j*(p-2*r))-1)**2)/(2*r)
    np.testing.assert_allclose([derivative(0), derivative(np.pi), derivative(np.pi/2)],
                               [0,0,4], atol=1e-6)


if __name__ == '__main__':
    main()
