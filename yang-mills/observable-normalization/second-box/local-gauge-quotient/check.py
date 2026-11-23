"""Independent position-space Jacobian and exact one-cycle Wilson kernel controls."""
import numpy as np
from scipy.linalg import null_space
from scipy.special import ive

I3 = np.eye(3)
EDGES = [(x, x ^ (1 << i), i) for x in range(8) for i in range(3)]


def wedge(a):
    x, y, z = a
    return np.array([[0, -z, y], [z, 0, -x], [-y, x, 0]])


def orbit(a):
    mat = np.zeros((72, 24))
    for e, (x, y, _) in enumerate(EDGES):
        ad = wedge(a[e])
        r = np.linalg.norm(a[e])
        # Stable near zero through order r^4.
        factor = (1/12 + r*r/720 if r < .01 else
                  (1 - r/2 / np.tan(r/2)) / r**2)
        even = I3 + factor * ad @ ad
        rows = slice(3*e, 3*e+3)
        mat[rows, 3*x:3*x+3] = even - ad/2
        mat[rows, 3*y:3*y+3] = -even - ad/2
    return mat


D = orbit(np.zeros((24, 3)))[:, 3:]
SLICE = null_space(D.T)
BASE = np.linalg.slogdet(D.T @ D)[1]


def log_jacobian(a):
    sign, logabs = np.linalg.slogdet(D.T @ orbit(a)[:, 3:])
    assert sign > 0
    return logabs - BASE + 2*np.log(np.sinc(np.linalg.norm(a, axis=1)/(2*np.pi))).sum()


def quat(a):
    r = np.linalg.norm(a)
    return np.r_[np.cos(r/2), np.sinc(r/(2*np.pi))*a/2]


def multiply(u, v):
    return np.r_[u[0]*v[0] - u[1:]@v[1:],
                 u[0]*v[1:] + v[0]*u[1:] + np.cross(u[1:], v[1:])]


def moved_logs(a, t):
    def log_link(q):
        radius = np.linalg.norm(q[1:])
        if radius == 0:
            return np.zeros(3)
        return (2*np.arctan2(radius, q[0])/radius)*q[1:]
    return np.array([log_link(multiply(multiply(quat(t[x]), quat(a[e])), quat(-t[y])))
                     for e, (x, y, _) in enumerate(EDGES)])


def log_cycle_ratio(beta, a, b):
    # Exact based SU(2) integration for a two-link cycle. Its sole holonomy is exp(2a).
    uinv = quat(-a)
    v = quat(b)
    left, right = multiply(uinv, v), multiply(v, uinv)
    radius = np.linalg.norm(np.r_[left[0]+right[0], left[1:]-right[1:]])
    def scaled_log_z(x):
        return np.log(2*ive(1, x)/x)
    log_kernel = (beta*(radius-2) + scaled_log_z(beta*radius) - 2*scaled_log_z(beta)
                  + np.log(np.sinc(np.linalg.norm(a)/np.pi)*np.sinc(np.linalg.norm(b)/np.pi))
                  - np.log(2*np.pi**2))
    log_gaussian = 1.5*np.log(beta/(4*np.pi)) - beta*np.linalg.norm(a-b)**2/4
    return log_kernel - log_gaussian


def main():
    rng = np.random.default_rng(311)
    c = rng.normal(size=(3, 3))
    c /= np.linalg.norm(c)
    hard = (SLICE @ rng.normal(size=51)).reshape(8,3,3)
    hard -= np.mean(hard, axis=0)
    hard /= np.linalg.norm(hard)
    for t in (.08, .04, .02):
        a = np.tile(t*c, (8,1))
        curvature = log_jacobian(a)/t**2
        assert abs(curvature + 19/18) < .05*t**2
        y = .001*hard.reshape(24,3)
        assert abs(log_jacobian(a+y) - log_jacobian(a-y)) < 1e-9
        # Differentiate actual endpoint rotations in quaternion coordinates.
        direction = rng.normal(size=(8,3))
        direction[0] = 0
        step = 1e-6
        field = a + y
        derivative = (moved_logs(field, step*direction) -
                      moved_logs(field, -step*direction)) / (2*step)
        np.testing.assert_allclose(derivative.ravel(), orbit(field) @ direction.ravel(),
                                   atol=2e-10, rtol=2e-10)
        # Independent full-column coordinate volume, including the 51 slice columns.
        cols = np.column_stack((orbit(a+y)[:,3:], SLICE))
        ratio = np.linalg.slogdet(cols)[1] - BASE/2
        ratio += 2*np.log(np.sinc(np.linalg.norm(a+y, axis=1)/(2*np.pi))).sum()
        assert abs(ratio-log_jacobian(a+y)) < 1e-12
    for beta in (125., 1000., 8000., 64000.):
        h = beta**(-1/3)
        a = h*np.array([.9,-.2,.4])
        b = a + np.array([-.1,.7,.2])/np.sqrt(beta)
        error = abs(np.expm1(log_cycle_ratio(beta,a,b)))
        assert error < 2*h*h
        print(f"cycle beta={beta:g}  relative kernel error={error:.8g}")
    print("Cube rank, slice density and noncommuting background checks passed.")


if __name__ == "__main__":
    main()
