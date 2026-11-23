"""Recover the Wilson-link time stencil from oriented faces and exercise its boundaries."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
import json


def oriented_faces(length, times, periodic):
    """times counts time slices; each boundary uses the positive axes i then j."""
    sides = (length, length, length, times)

    def forward(x, axis):
        y = list(x)
        y[axis] = (y[axis] + 1) % sides[axis]
        return tuple(y)

    for x in product(*(range(n) for n in sides)):
        for i, j in combinations(range(4), 2):
            if j == 3 and x[3] == times - 1 and not periodic:
                continue
            yield j == 3, [((x, i), 1), ((forward(x, i), j), 1),
                             ((forward(x, j), i), -1), ((x, j), -1)]


def lattice(length, times, periodic):
    neighbors = defaultdict(list)
    for timeface, boundary in oriented_faces(length, times, periodic):
        edges = [edge for edge, _ in boundary]
        for e in edges:
            neighbors[e].extend((timeface, f) for f in edges if f != e)
    return neighbors


def counts(e, pairs):
    x, _ = e
    return Counter((timeface, axis == 3, y[3] - x[3]) for timeface, (y, axis) in pairs)


def weighted_row(e, stencil):
    h = Fraction(26, 15)
    total = sum(n * Fraction(3) ** shift * (h if temporal else 1)
                for (_, temporal, shift), n in stencil.items())
    return total / (20 * (h if e[1] == 3 else 1))


def check_staples():
    # An exponent k denotes diag(exp(i*pi*k/3), exp(-i*pi*k/3)).
    # Entries below are twice the real part and 2/sqrt(3) times the imaginary part.
    roots = [(2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1), (1, -1)]
    n = 0
    for axis in range(4):
        e = ((0, 0, 0, 2), axis)
        staples = []
        for _, boundary in oriented_faces(3, 5, False):
            signs = dict(boundary)
            if e in signs:
                staples.append([(f, sign * signs[e]) for f, sign in boundary if f != e])
        if len({f for staple in staples for f, _ in staple}) != 18:
            raise ValueError("staples must have disjoint freely assignable links")
        for k, varied in enumerate(staples):
            others = [staple for index, staple in enumerate(staples) if index != k]
            background = {}
            for staple, target in zip(others, [0, 3, 0, 2, 4], strict=True):
                f, sign = staple[0]
                background[f] = sign * target
            for f, _ in varied:
                for exponent, expected in [(0, (2, 0)), (3, (-2, 0))]:
                    links = {**background, f: exponent}
                    phases = [sum(sign * links.get(g, 0) for g, sign in staple) % 6
                              for staple in staples]
                    if tuple(map(sum, zip(*(roots[j] for j in phases)))) != expected:
                        raise ValueError("background failed to leave precisely the signed unit staple")
                n += 1
    return n


def recover(out):
    audit = []
    reference = None
    for length, periodic in [(2, False), (3, False), (4, False), (3, True)]:
        geometry = lattice(length, 5, periodic)
        rows = {e: counts(e, pairs) for e, pairs in geometry.items()}
        bulk = [e for e in geometry if e[0][3] == 2]
        interior = [rows[((0, 0, 0, 2), axis)] for axis in (0, 3)]
        if any(rows[e] != interior[e[1] == 3] for e in bulk):
            raise ValueError("interior rows disagree by position or spatial axis")
        if reference is None:
            reference = interior
        elif reference != interior:
            raise ValueError("stencil changed with volume or time boundary")
        distinct = min(len(set(f for _, f in geometry[e])) for e in bulk)
        if any(len(geometry[e]) != 18 for e in bulk) or (distinct == 18) != (length >= 3):
            raise ValueError("unexpected overlap of the six staples")
        ratios = [max(weighted_row(e, row) for e, row in rows.items() if (e[1] == 3) == axis)
                  for axis in (False, True)]
        if periodic:
            if max(ratios) <= 1:
                raise ValueError("expected linear-time tilt to fail at the periodic seam")
        elif ratios != [Fraction(449, 450), Fraction(129, 130)]:
            raise ValueError("open-slab envelope disagrees with actual weighted incidence")
        audit.append(dict(length=length, periodic_time=periodic, links=len(rows),
                          min_distinct_in_bulk=distinct, max_weighted_rows=list(map(str, ratios))))
    spatial, temporal = reference
    # Synthesize the symmetric interior stencil. The zero and reverse-shift
    # multiplicities below are separately required before combining monomials.
    spatial_faces = spatial[False, False, 0]
    displaced = spatial[True, False, 1]
    mixed = spatial[True, True, 0]
    transverse, parallel = temporal[True, False, 0], temporal[True, True, 0]
    if (len(spatial) != 5 or len(temporal) != 3 or not all((spatial_faces, mixed, transverse, parallel))
            or displaced != 1 or spatial[True, False, -1] != displaced
            or spatial[True, True, -1] != mixed or temporal[True, False, 1] != transverse):
        raise ValueError("unpaired stencil coefficients")
    (out / "stencil").write_text(
        f"def spatial (s t R h : ℝ) : ℝ := {spatial_faces}*s + t*(R+1/R) + {mixed}*t*(1+1/R)*h\n"
        f"def temporal (t R h : ℝ) : ℝ := {transverse}*t*(1+R) + {parallel}*t*h\n")
    (out / "incidence.json").write_text(json.dumps(
        {"lattices": audit, "signed_staple_pairs": check_staples()}, indent=2) + "\n")
