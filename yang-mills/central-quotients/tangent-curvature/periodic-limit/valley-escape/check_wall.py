"""Independent angular divergence and Airy trial checks in nine dimensions."""
import numpy as np
from scipy.integrate import quad
from scipy.special import airy, ai_zeros


def field(point):
    rows = point.reshape(3, 3)
    radius = np.linalg.norm(rows[0])
    axis = rows[0]/radius
    normal = rows[1:] - (rows[1:] @ axis)[:, None]*axis
    vector = np.vstack((np.zeros(3), 2*radius*normal)).ravel()
    unit = point/np.linalg.norm(point)
    return vector-(vector@unit)*unit, 8*radius-20*radius*np.sum(normal**2)/(point@point)


def check_divergence():
    rng = np.random.default_rng(913)
    worst = 0.
    for point in rng.normal(size=(120, 9)):
        unit = point/np.linalg.norm(point)
        projection = np.eye(9)-np.outer(unit, unit)
        derivatives = []
        for direction in np.eye(9):
            step = 2e-5*direction
            derivatives.append((field(point+step)[0]-field(point-step)[0])/(4e-5))
        error = abs(np.trace(np.asarray(derivatives) @ projection)-field(point)[1])
        worst = max(worst, error)
    assert worst < 1e-7
    print("maximum angular divergence discrepancy", worst)


def check_airy():
    zero = ai_zeros(1)[0][0]
    def integrate(observable):
        return quad(lambda x: observable(x, *airy(2*x+zero)[:2]),
                    0, 18, epsabs=1e-12)[0]
    norm = integrate(lambda x, f, fp: f*f)
    energy = integrate(lambda x, f, fp: 2*fp*fp+4*x*f*f)/norm
    second = integrate(lambda x, f, fp: x*x*f*f)/norm
    assert abs(energy+2*zero) < 1e-10
    print("half-line energy", energy, "second moment", second)
    for radius in (4, 16, 64, 256):
        omega, gamma = 2*radius, radius**-0.5
        inverse_square = integrate(lambda x, f, fp: f*f/(radius+x)**2)/norm
        excess = (2*second/radius + gamma/2 + 1/omega**2 + 2/(omega*gamma)
                  + (omega-gamma)**2*inverse_square/(2*omega*gamma))
        print(radius, "trial energy minus 4R", energy+excess)


if __name__ == "__main__":
    check_divergence()
    check_airy()
