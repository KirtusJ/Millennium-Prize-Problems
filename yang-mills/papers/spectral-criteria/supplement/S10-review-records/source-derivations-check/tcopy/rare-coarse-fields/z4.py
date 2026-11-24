"""Exact two-state path control and size of the E3 tail witness."""
from fractions import Fraction as F
from math import asinh, exp, log, pi, sqrt

# Density with respect to the uniform reference measure on two points.
off_density = F(1, 4) / F(1, 2)
gap = 1 - (F(3, 4) - F(1, 4))
unsupported_bound = 2 * off_density
assert gap == F(1, 2) and unsupported_bound == 1
print("one-step actual gap", gap, "claimed lower bound", unsupported_bound)

# At a=pi/2, chi=1 and Psi'^2=4 asinh(1)+2 eta (lower lines 305–307).
assert 4*asinh(1) > 1
# Use tilt 1 in the lower bound.
# Integral of the radial envelope on [L+1/L,L+2/L], relative to L^3/sqrt(beta).
upper_z = pi**2.5 / 2**2.5
density_factor = 8 / (pi**3 * upper_z)
for L in (4, 8, 16, 32):
    assert (L+2/L)*exp(-L**2/2) < pi/2
    # For arcsin(x), arcsin(x) <= x/sqrt(1-x^2).
    assert L/sqrt(1-L**2*exp(-L**2)) < L+1/L
    log_ratio = log(density_factor) + L - 2 - 2/L**2 - 2*log(L)
    print(f"L={L}, certified lower ratio={exp(log_ratio):.6g}")
assert 8/pi**2 > .5
