"""Recompute both source-table checks and the conditional SU(2) two-level continuation."""
from math import exp, expm1, hypot, isclose, sqrt

# (spatial sites, lower E energy, its error, single winding energy, its error)
SU2 = [(12, 1.220, .009, .5804, .0038), (14, 1.254, .014, .7140, .0041)]
SU3 = [(8, .519, .004, .2107, .0013), (9, .583, .016, .2526, .0019),
       (10, .670, .010, .3057, .0019), (11, .883, .016, .3485, .0028),
       (12, .910, .010, .4035, .0039), (16, 1.060, .006, .6781, .0033)]


def weight_floors(threshold, free_pair):
    """Mean energy and one-step transfer moment are two different hypotheses."""
    energy = max(0, 1 - free_pair / threshold)
    transfer = max(0, (exp(-free_pair) - exp(-threshold)) / (-expm1(-threshold)))
    return energy, transfer


def print_rows(group, rows):
    for n, e, se, flux, sf in rows:
        deficit = e - 2 * flux
        energy, transfer = weight_floors(e, 2 * flux)
        print(f"{group} {n:2d}: e-2F={deficit:+.4f}  independent SE={hypot(se,2*sf):.4f}  "
              f"largest SE={se+2*sf:.4f}  "
              f"conditional low weight: energy={energy:.2%}, transfer={transfer:.2%}")
    print()


def two_volume_model(inputs):
    a, b, c, d, flux12, flux14, flux20, observed20 = inputs
    g = (c*d - a*b) / (c+d-a-b)
    h_squared = (g-a) * (b-g)
    assert isclose(h_squared, (g-c)*(d-g), abs_tol=1e-12)
    h = sqrt(h_squared)
    shift = a + b - g - 2 * flux12
    trace_residual = c + d - a - b - 2 * (flux14-flux12)
    pair20 = 2 * flux20 + shift
    lower20 = (g + pair20 - hypot(g-pair20, 2*h)) / 2
    return (g, h, shift, trace_residual, lower20, observed20-lower20,
            (g-a)/(b-a), (g-c)/(d-c))


def propagated_errors(inputs, errors, step):
    changes = []
    for i, sigma in enumerate(errors):
        left, right = list(inputs), list(inputs)
        left[i] -= step
        right[i] += step
        changes.append([(b-a)*sigma/(2*step)
                        for a, b in zip(two_volume_model(left), two_volume_model(right))])
    return [(hypot(*terms), sum(abs(t) for t in terms)) for terms in zip(*changes)]


if __name__ == "__main__":
    print_rows("SU2", SU2)
    print_rows("SU3", SU3)
    _, e, se, flux, sf = SU2[0]
    e_low, pair_high = e-3*se, 2*(flux+3*sf)
    print("SU2 side 12, worst corner of three-error rectangle:",
          f"deficit={e_low-pair_high:.4f}; weights={weight_floors(e_low, pair_high)}")

    m, q = exp(-2*flux), exp(-e)
    curvature = expm1(-(e - 2*flux))**2
    # Equal weights at q and 2m-q realize the 50% threshold.
    upper = 2*m-q
    assert q < upper <= 1
    z = (q*q + upper*upper) / 2
    assert isclose(z/m**2-1, curvature, rel_tol=1e-12)
    print(f"half-weight threshold: C0 C2 / C1^2 - 1 <= {curvature:.8f}")

    # Only the last component is held out as a spectral target; flux20 is an input.
    inputs = (1.220, 1.317, 1.254, 1.549, .5804, .7140, 1.0996, 1.284)
    errors = (.009, .017, .014, .020, .0038, .0041, .0039, .013)
    labels = ("glueball diagonal", "mixing magnitude", "pair diagonal shift",
              "trace residual at 14", "predicted lower level at 20", "observed minus predicted",
              "pair fraction at 12", "pair fraction at 14")
    widths = propagated_errors(inputs, errors, 1e-5)
    finer = propagated_errors(inputs, errors, 1e-6)
    for label, value, (indep, worst), fine in zip(labels, two_volume_model(inputs), widths, finer):
        assert isclose(indep, fine[0], rel_tol=1e-5)
        assert isclose(worst, fine[1], rel_tol=1e-5)
        print(f"{label}: {value:.6f}  independent SE={indep:.6f}  largest linearized SE={worst:.6f}")
