"""Count actual bridge-factor supports and check the transfer on a finite gauge circuit."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
import json
import math

import numpy as np
from scipy.special import ive


def spatial_faces(L):
    def neighbor(x, axis):
        return tuple((a+(i == axis)) % L for i, a in enumerate(x))

    for x in product(range(L), repeat=3):
        for i, j in combinations(range(3), 2):
            yield ((x, i), (neighbor(x, i), j), (neighbor(x, j), i), (x, j))


def counts(L):
    # Each site carries the endpoint and its own outgoing seed. Enumerate both
    # adjacent slabs. Count factors separately even when neighbors coincide.
    offsets = defaultdict(Counter)
    for face in spatial_faces(L):
        for t in (-1, 0):
            support = {(time, e) for time in (t, t+1) for e in face}
            assert len(support) == 8
            for edge in face:
                offsets[edge].update(time for time, other in support if (time, other) != (0, edge))
    rows = {tuple(row[t] for t in (-1, 0, 1)) for row in offsets.values()}
    if len(rows) != 1 or len(offsets) != 3*L**3:
        raise ValueError("inconsistent magnetic support")
    return rows.pop()


def kernel_check():
    angles = np.linspace(0., math.pi, 513)
    results = []
    for g in (4., 4.1, 8., 16., 32., 128., 1024.):
        m = math.ceil(3*g)
        chars = np.ones_like(angles)
        prev = np.zeros_like(angles)
        h = np.zeros_like(angles)
        for n in range(25):
            r = ive(n+1, g)/ive(1, g)
            h += (n+1)*r**m*chars
            prev, chars = chars, 2*np.cos(angles)*chars-prev
        if np.max(np.abs(h-1)) > 0.1:
            raise ValueError("endpoint heat window")
        results.append([g, m, float(h.min()), float(h.max())])
    return results


def bridge_check():
    # Three positive free Z2 Wilson steps on four distinct links, an exact
    # finite gauge circuit with a nonconstant plaquette potential.
    configs = np.array(list(product((0, 1), repeat=4)))
    k = np.array([[0.8, 0.2], [0.2, 0.8]])
    endpoint = np.linalg.matrix_power(k, 3)
    free = np.prod(k[configs[:, None, :], configs[None, :, :]], axis=2)
    a, lam = 0.25, 0.7
    potential = lam*(1-(-1.)**configs.sum(axis=1))
    half = np.exp(-a*potential/2)
    direct = np.linalg.matrix_power(half[:, None]*free*half[None, :], 3)
    blocked = np.zeros_like(direct)
    mag = np.exp(-a*potential)
    # Form the independent one-link bridge law explicitly for each endpoint
    # pair. Interior times share a path. Each spatial face uses all four paths.
    for i, left in enumerate(configs):
        for j, right in enumerate(configs):
            P = np.ones((len(configs), len(configs)))
            for e in range(4):
                u, v = configs[:, e], configs[:, e]
                P *= (k[left[e], u, None]*k[u[:, None], v]*k[v, right[e]][None, :]
                      / endpoint[left[e], right[e]])
            if abs(P.sum()-1) > 2e-13:
                raise ValueError("bridge normalization")
            blocked[i, j] = (np.prod(endpoint[left, right])*half[i]*half[j]
                             * np.sum(P*mag[:, None]*mag[None, :]))
    endpoint_only = np.linalg.matrix_power(free, 3)*np.outer(half**3, half**3)
    error = np.linalg.norm(blocked-direct, ord=2)
    wrong = np.linalg.norm(endpoint_only-direct, ord=2)
    if error > 2e-13 or wrong < 1e-3:
        raise ValueError("bridge transfer control")
    # Two adjacent faces in one two-step slab, all endpoints zero. Their
    # intermediate holonomies reuse one bridge link (coordinate zero).
    interior = np.array(list(product((0, 1), repeat=7)))
    link_law = k[0, :]*k[:, 0] / (k @ k)[0, 0]
    law = np.prod(link_law[interior], axis=1)
    face_a = np.exp(-a*lam*(1-(-1.)**interior[:, [0, 1, 2, 3]].sum(axis=1)))
    face_b = np.exp(-a*lam*(1-(-1.)**interior[:, [0, 4, 5, 6]].sum(axis=1)))
    factorization_error = np.dot(law, face_a*face_b)-np.dot(law, face_a)*np.dot(law, face_b)
    if factorization_error < 1e-3:
        raise ValueError("shared link correlation was lost")
    return {"matrix_size": len(configs), "bridge_error": float(error),
            "endpoint_potential_only_error": float(wrong),
            "separately_averaged_faces_error": float(factorization_error)}


def quotient_check():
    # SO(3) defining character. Its SU(2) pullback has a two-element kernel.
    theta = (np.arange(4096)+0.5)*math.pi/4096
    angles = np.linspace(0., math.pi, 513)
    records = []
    for g in (4., 16., 64., 256.):
        t = 2*g/3
        density = (1-np.cos(theta))*np.exp(t*(np.cos(theta)-1))
        d = ive(0, t)-ive(1, t)
        block = np.ones_like(angles)
        worst = 0.
        for n in range(1, 25):
            character = np.sin((n+0.5)*theta)/np.sin(theta/2)
            quadrature = np.dot(density, character)/((2*n+1)*density.sum())
            r = (ive(n, t)-ive(n+1, t))/((2*n+1)*d)
            worst = max(worst, abs(r-quadrature))
            chi = 1+2*np.cos(np.outer(np.arange(1, n+1), angles)).sum(axis=0)
            block += (2*n+1)*r**math.ceil(5*g)*chi
        odd_weight = np.sin(theta)**2*np.exp(t*(np.cos(2*theta)-1))
        odd = np.dot(odd_weight, np.cos(theta))/odd_weight.sum()
        if worst > 1e-10 or abs(odd) > 1e-10 or np.max(abs(block-1)) > 0.1:
            raise ValueError("quotient endpoint check")
        records.append([g, float(worst), float(block.min()), float(block.max()), float(odd)])
    return records


def recover(out):
    rows = {size: counts(size) for size in (2, 3, 4, 5)}
    left, mid, right = rows[2]
    if any(row != (left, mid, right) for row in rows.values()) or left != right:
        raise ValueError("spatial-period dependence")
    p = Fraction(13, 1536)
    tilt = Fraction(3)
    q = mid*p+(Fraction(1, 10)+left*p)*(tilt+1/tilt)
    limiting = mid*p+(Fraction(1, 10)+left*p)*(4+Fraction(1, 4))
    if not q < 1 < limiting:
        raise ValueError("tilt controls")
    (out/"counts.bin").write_bytes(bytes([left, mid, right]))
    proof = ("theorem rowAtTilt {δ p : ℝ} (heat : δ ≤ 1/10) (interaction : p ≤ 13/1536) :\n"
             f"    {mid}*p+(δ+{left}*p)*(3+1/3) ≤ {q} := by linarith\n")
    group_row = mid*Fraction(1, 120)+(Fraction(1, 10)+left*Fraction(1, 120))*(tilt+1/tilt)
    proof += ("theorem groupRowAtTilt {δ p : ℝ} (heat : δ ≤ 1/10) (interaction : p ≤ 1/120) :\n"
              f"    {mid}*p+(δ+{left}*p)*(3+1/3) ≤ {group_row} := by linarith\n")
    (out/"geometry").write_text(proof)
    record = {"magnetic_incidence_by_time_offset": rows, "tilt_three_row": str(q),
              "tilt_four_row": str(limiting), "endpoint_density": kernel_check(),
              "finite_bridge": bridge_check(), "SO3_and_lift": quotient_check()}
    (out/"incidence.json").write_text(json.dumps(record, indent=2)+"\n")
