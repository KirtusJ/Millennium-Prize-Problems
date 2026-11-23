"""Independent finite checks. The rotor is a character truncation of one four-edge circuit."""
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh, expm
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


def heat_controls():
    # Haar probability normalization. Use the continuous endpoint values of
    # the character recurrence to test the two poles as well as interior angles.
    angles = np.linspace(0., np.pi, 513)
    cosine = np.cos(angles)
    previous = np.zeros_like(angles)
    char = np.ones_like(angles)
    kernel = np.zeros_like(angles)
    for n in range(19):
        kernel += (n+1)*np.exp(-n*(n+2))*char
        previous, char = char, 2*cosine*char-previous
    if kernel.min() < 2/3 or kernel.max() > 4/3:
        raise ArithmeticError("one-link heat window")

    # Independent finite-space comparison with a nonconstant potential.
    size, time = 9, 2.
    shift = np.roll(np.eye(size), 1, axis=0)
    kinetic = 2*np.eye(size)-shift-shift.T
    potential = 1-np.cos(2*np.pi*np.arange(size)/size)
    H = kinetic+np.diag(potential)
    free_kernel = expm(-time*kinetic)
    full_kernel = expm(-time*H)
    values, vectors = eigh(H)
    omega = np.abs(vectors[:, 0])
    q = omega/sum(omega)
    weighted = full_kernel*omega
    transition = weighted/weighted.sum(axis=1, keepdims=True)
    minor = np.exp(-time*max(potential))*free_kernel.min()/free_kernel.max()
    if (np.min(full_kernel-np.exp(-time*max(potential))*free_kernel) < -1e-12
            or np.max(full_kernel-free_kernel) > 1e-12
            or np.min(transition-minor*q) < -1e-12
            or np.exp(-time*(values[1]-values[0])) > 1-minor+1e-12):
        raise ArithmeticError("positive-kernel minorization")
    return {"single_link_kernel_range": [float(kernel.min()), float(kernel.max())],
            "finite_cycle_minorization": float(minor),
            "finite_cycle_actual_min_row_density_ratio": float(np.min(transition/q)),
            "finite_cycle_gap_floor_and_gap": [float(minor/time), float(values[1]-values[0])]}


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
    results = {"opposite_sign_probes": [neg, pos], "bessel": bessel_check(), "rotor": rotor_check(),
               "heat": heat_controls()}
    (out/"controls.json").write_text(json.dumps(results, indent=2)+"\n")
