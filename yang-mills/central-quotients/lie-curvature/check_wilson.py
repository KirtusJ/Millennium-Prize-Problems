"""Mixed fundamental/adjoint SU(3) Wilson Ward identity on a compact Haar orbit."""
from itertools import product
import numpy as np
from scipy.linalg import expm
from check_algebra import basis


def star(m):
    return np.swapaxes(m.conj(), -1, -2)


def random_su(rng):
    a = rng.normal(size=(3, 3))+1j*rng.normal(size=(3, 3))
    u, _ = np.linalg.qr(a)
    u[:, 0] /= np.linalg.det(u)
    return u


def shift(site, axis, delta):
    x = list(site)
    x[axis] = (x[axis]+delta+1)%3-1
    return tuple(x)


def face(x, i, j):
    return [(x, i, 1), (shift(x, i, 1), j, 1), (shift(x, j, 1), i, -1), (x, j, -1)]


def path(x):
    at, steps = (0, 0, 0, 0), []
    for i, s in enumerate(x):
        if s:
            nxt = shift(at, i, s)
            steps.append((at if s > 0 else nxt, i, s))
            at = nxt
    return steps


def trace(a):
    return np.trace(a, axis1=-2, axis2=-1)


W, A = 0.7, 0.3
METRIC = W + A*18/8


def value(u):
    z = trace(u)
    return W*(1-z.real/3)+A*(1-(abs(z)**2-1)/8)


def derivative(u, du):
    z, dz = trace(u), trace(du)
    return -W*dz.real/3-A*(z.conj()*dz).real/4


def orbit(sign, samples):
    beta = 2.3
    rng = np.random.default_rng(134)
    fixed = {(x, i): random_su(rng) for x in product((-1, 0, 1), repeat=4) for i in range(4)}
    base = (0, 0, 0, 0) if sign > 0 else (-1, 0, 0, 0)
    axis = 0
    angle = 2*np.pi*np.arange(samples)/samples
    diagonal = np.stack([np.exp(1j*angle), np.exp(-1j*angle), np.ones(samples)], axis=1)
    rot = random_su(rng)
    orbit_matrix = (rot[None, :, :]*diagonal[:, None, :]) @ star(rot)
    generator = rot @ np.diag([1j, -1j, 0]) @ star(rot)
    link = orbit_matrix @ fixed[base, axis] if sign > 0 else fixed[base, axis] @ orbit_matrix
    dlink = generator @ link if sign > 0 else link @ generator

    def word(steps):
        u, du = np.eye(3), np.zeros((3, 3))
        for site, i, orient in steps:
            selected = site == base and i == axis
            l = link if selected else fixed[site, i]
            dl = dlink if selected else np.zeros((3, 3))
            if orient < 0:
                l, dl = star(l), star(dl)
            du, u = du @ l+u @ dl, u @ l
        return u, du

    potential, score = np.zeros(samples), np.zeros(samples)
    arg, darg, frame = (np.zeros(samples) for _ in range(3))
    for i in (1, 2, 3):
        for site in (base, shift(base, i, -1)):
            u, du = word(face(site, 0, i))
            potential += value(u)
            score += derivative(u, du)
    colors = basis(3)/np.sqrt(METRIC)
    for q, (site, i, j) in enumerate([(base, 0, 1), (shift(base, 2, -1), 0, 2),
                                      ((sign, 0, 0, 0), 1, 3), ((sign, 1, 0, 0), 2, 3)]):
        p, dp = word(path(site))
        u, du = word(face(site, i, j))
        h = p @ u @ star(p)
        inside = p @ du @ star(p)
        outside = dp @ u @ star(p)+p @ u @ star(dp)
        color = colors[q+1]
        z, x = trace(h), trace(color @ h)
        arg += np.sqrt(beta)*(-W*x.real/3-A*(z.conj()*x).real/4)
        def d_coordinate(dh):
            dz, dx = trace(dh), trace(color @ dh)
            return np.sqrt(beta)*(-W*dx.real/3-A*(dz.conj()*x+z.conj()*dx).real/4)
        darg += d_coordinate(inside)+d_coordinate(outside)
        frame += d_coordinate(outside)
    prob = np.exp(-beta*(potential-potential.min()))
    prob /= prob.sum()
    return np.array([np.dot(prob, np.cos(arg)*darg), beta*np.dot(prob, np.sin(arg)*score),
                     np.dot(prob, np.cos(arg)*(darg-frame))])


def metric_check():
    t = basis(3)
    x = t[2]+0.37*t[6]
    eps = 0.0003
    u = expm(eps*x)
    observed = 2*value(u)/eps**2
    target = METRIC*np.vdot(x, x).real/3
    np.testing.assert_allclose(observed, target, rtol=1e-6)
    print("mixed Hessian", observed, target, "metric factor", METRIC)


if __name__ == "__main__":
    metric_check()
    for direction in (1, -1):
        lo, hi = orbit(direction, 128), orbit(direction, 256)
        np.testing.assert_allclose(lo, hi, atol=1e-12)
        assert abs(hi[0]-hi[1]) < 1e-12
        assert abs(hi[0]-hi[2]) > 0.001
        print("endpoint, full frame, score, frozen frame", direction, *hi)
