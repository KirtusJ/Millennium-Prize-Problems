"""Independent finite checks. The rotor is a character truncation of one four-edge circuit."""
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh
from scipy.special import ive


def bessel_check():
    cases = 0
    largest = 0.0
    for g in (0.125, 1., 8., 64., 512., 4096.):
        for labels in itertools.product((0, 1, 3, 12, 30), repeat=3):
            x = sum(n*(n+2)/2 for n in labels)
            r = math.prod(ive(n+1, g)/ive(1, g) for n in labels)
            d = g*(1-r)
            if not x/(1+x/g)-2e-10 <= d <= x+2e-10:
                raise ArithmeticError((g, labels, d))
            c = 1.5
            difference = 1/(c+d)-1/(c+x)
            normalized = difference*(g+c)
            if not -2e-10 <= normalized <= 1+2e-10:
                raise ArithmeticError("free resolvent bound")
            largest = max(largest, normalized)
            cases += 1
    return {"label_cases": cases, "max_fraction_of_sharp_resolvent_bound": largest}


def spectral_function(matrix, f):
    values, basis = eigh(matrix)
    return (basis*f(values)) @ basis.T


def rotor_check():
    size, kappa, coupling = 32, 1., 2.
    n = np.arange(size)
    identity = np.eye(size)
    trace_half = (np.eye(size, k=1) + np.eye(size, k=-1))/2
    potential = coupling*(identity-trace_half)
    H0 = 4*n*(n+2)/(2*kappa)
    H = np.diag(H0) + potential
    c = 2*coupling+6/kappa
    exact, vec = eigh(H)
    threshold = exact[1]-exact[0]
    t = 0.5
    evolution = spectral_function(H-exact[0]*identity, lambda x: np.exp(-t*x))
    rows = []
    for g in (512, 1024, 2048, 4096):
        a = kappa/g
        r = ive(n+1, g)/ive(1, g)
        M = spectral_function(potential, lambda x: np.exp(-a*x/2))
        T = (M*(r**4)) @ M
        B = (identity-T)/a
        resolvent = np.linalg.solve(B+c*identity, identity) - np.linalg.solve(H+c*identity, identity)
        s, u = eigh(T)
        gap = -math.log(s[-2]/s[-1])/a
        angle = np.linalg.norm(u[:,-1]-np.dot(vec[:,0], u[:,-1])*vec[:,0])
        evolved = (u*((s/s[-1])**round(t/a))) @ u.T
        errors = [np.linalg.norm(resolvent, 2), abs(gap-threshold), angle, np.linalg.norm(evolved-evolution, 2)]
        if not errors[0] <= 9*a or not errors[1] <= 180*a*c*c:
            raise ArithmeticError("absolute cutoff certificate failed on the finite rotor")
        if rows and not all(x < y for x, y in zip(errors, rows[-1][1:])):
            raise ArithmeticError("expected convergence failed at the tested steps")
        rows.append([g, *map(float, errors)])
    return {"character_dimension": size, "hamiltonian_gap": threshold,
            "g_resolvent_gap_vacuum_evolution_errors": rows}


def generate(out: Path):
    # Positive contraction M has eigenvalues 1/2 and 1. Test both possible
    # incorrect orderings using the smallest nonnegative coordinate probes.
    probes = list(itertools.product(range(2), repeat=2))
    loss = lambda x, y: y*y-((x+3*y)/4)**2
    neg = next(p for p in probes if loss(*p) < 0)
    pos = next(p for p in probes if loss(*p) > 0)
    proof = ("/-- A positive contraction with diagonal entries 3/4 and off-diagonal 1/4.\n"
             "    Rescaling its kinetic form by multiplication has neither order on all vectors. -/\n"
             "theorem sandwichControl :\n    (¬ ∀ x y : ℝ, ((x+3*y)/4)^2 ≤ y^2) ∧\n"
             "    (¬ ∀ x y : ℝ, y^2 ≤ ((x+3*y)/4)^2) := by\n  constructor\n")
    for x, y in (neg, pos):
        proof += f"  · intro h\n    have bad := h {x} {y}\n    norm_num at bad\n"
    (out/"control").write_text(proof)
    results = {"opposite_sign_probes": [neg, pos], "bessel": bessel_check(), "rotor": rotor_check()}
    (out/"controls.json").write_text(json.dumps(results, indent=2)+"\n")
