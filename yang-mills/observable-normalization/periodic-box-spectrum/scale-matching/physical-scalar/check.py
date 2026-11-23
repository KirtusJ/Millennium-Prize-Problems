"""SU(2) scalar spectroscopy in flow units. Inputs and conventions are in README.md."""
from dataclasses import dataclass
from math import exp, hypot, isclose, sqrt


@dataclass(frozen=True)
class Point:
    beta: float
    side: int
    mass: float          # aM
    mass_error: float
    flow: float          # t0 / a^2
    flow_error: float

    @property
    def radius(self):
        return sqrt(8 * self.flow)

    @property
    def y(self):
        return self.mass * self.radius

    @property
    def y_error(self):
        return self.y * hypot(self.mass_error / self.mass, self.flow_error / (2 * self.flow))

    @property
    def ell(self):
        return self.side / self.radius


coarse = Point(2.60, 30, 0.5001, 0.0041, 3.522, 0.010)
fine = Point(2.70, 40, 0.3652, 0.0035, 6.628, 0.036)
for point in (coarse, fine):
    print(f"beta {point.beta:.2f}: tau/a={point.radius:.6f}  L/tau={point.ell:.6f}  "
          f"M tau={point.y:.6f} +/- {point.y_error:.6f}")

c, f = 1 / coarse.flow, 1 / fine.flow
w = f / (c - f)
intercept = fine.y + w * (fine.y - coarse.y)
volume_cost = w * abs(coarse.ell - fine.ell)
curvature_cost = c * f / 2
print(f"refinement: a/tau change={coarse.radius / fine.radius - 1:.6%}  "
      f"L/tau change={fine.ell / coarse.ell - 1:.6%}  "
      f"mass change={fine.y - coarse.y:.6f} +/- {hypot(coarse.y_error, fine.y_error):.6f}")
print(f"I={intercept:.8f}  w={w:.8f}  B coefficient={volume_cost:.8f}  "
      f"K coefficient={curvature_cost:.8f}  critical K (B=0)={intercept/curvature_cost:.6f}")


# Enclose all coefficients when each of the four reported inputs varies by
# three printed errors. Rectangular sensitivity only, with no coverage claim.
tc_low, tc_high = coarse.flow - 3 * coarse.flow_error, coarse.flow + 3 * coarse.flow_error
tf_low, tf_high = fine.flow - 3 * fine.flow_error, fine.flow + 3 * fine.flow_error
w_low = tc_low / (tf_high - tc_low)
w_high = tc_high / (tf_low - tc_high)
yf_low = (fine.mass - 3 * fine.mass_error) * sqrt(8 * tf_low)
yc_high = (coarse.mass + 3 * coarse.mass_error) * sqrt(8 * tc_high)
intercept_low = yf_low + min(w_low * (yf_low - yc_high), w_high * (yf_low - yc_high))
ell_difference = max(abs(coarse.side/sqrt(8*tc_low) - fine.side/sqrt(8*tf_high)),
                     abs(coarse.side/sqrt(8*tc_high) - fine.side/sqrt(8*tf_low)))
print(f"three-error rectangle: I >= {intercept_low:.8f}  "
      f"B coefficient <= {w_high*ell_difference:.8f}  "
      f"K coefficient <= {1/(2*tc_low*tf_low):.8f}")


def zero_intercept_quadratic(x):
    line = intercept + (coarse.y - fine.y) / (c - f) * x
    return line - intercept * (x - c) * (x - f) / (c * f)


for x, observed in ((0, 0), (c, coarse.y), (f, fine.y)):
    assert isclose(zero_intercept_quadratic(x), observed, abs_tol=1e-12)

# Check the same quadratic outside the two-point interval with the journal's
# interpolating scale formula at the third spectroscopy coupling.
beta_other = 2.509
offset = beta_other - 2.600
flow_other = exp(1.258 + 6.409 * offset - 0.7411 * offset**2)
print(f"beta {beta_other} (interpolated flow): L/tau={22/sqrt(8*flow_other):.6f}  "
      f"observed M tau={0.6563*sqrt(8*flow_other):.6f}  "
      f"global volume-independent quadratic={zero_intercept_quadratic(1/flow_other):.6f}")

# Table B1 changes the flow convention while reusing each coupling's mass measurement.
for reference, tc, tf in ((0.08, 2.612, 4.881), (0.09, 3.075, 5.770),
                          (0.10, 3.522, 6.628), (0.12, 4.370, 8.247)):
    ratio = fine.mass / coarse.mass * sqrt(tf / tc)
    print(f"reference {reference:.2f}: fine/coarse mass in flow units={ratio:.6f}")

# Effective scalar energies from t=2a at fixed beta=2.427 and Nt=16.
volumes = [(12, 0.840, 0.011), (14, 0.854, 0.008), (20, 0.847, 0.008)]
n0, e0, error0 = volumes[0]
for n, e, error in volumes[1:]:
    residual = e - n0 / n * e0
    print(f"side {n}: inverse-side residual={residual:.6f}  "
          f"SE (independent)={hypot(error,n0/n*error0):.6f}  "
          f"upper SE (any correlation)={error+n0/n*error0:.6f}")
