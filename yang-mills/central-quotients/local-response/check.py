"""Exact checks from oriented link holonomies and the full edge-sign pushforward."""
from collections import Counter
from fractions import Fraction as F
from itertools import product

ONE = (1, 0, 0, 0)
I = (0, 1, 0, 0)
U = (F(1, 2),) * 4


def mul(q, r):
    a, b, c, d = q
    e, f, g, h = r
    return (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)


def oriented_square(base, axes):
    path = [base]
    for axis, step in zip((*axes, *axes), (1, 1, -1, -1)):
        point = list(path[-1])
        point[axis] += step
        path.append(tuple(point))
    return list(zip(path, path[1:]))


def geometry(length):
    transverse = [oriented_square((x, 0, 0), (1, 2)) for x in range(length + 1)]
    lateral = []
    for x in range(length):
        for axis in (1, 2):
            for side in (0, 1):
                base = [x, 0, 0]
                base[3-axis] = side
                lateral.append(oriented_square(tuple(base), (0, axis)))
    return transverse + lateral


def holonomy(face, links):
    value = ONE
    for a, b in face:
        forward = a < b
        q = links.get((a, b) if forward else (b, a), ONE)
        value = mul(value, q if forward else (q[0], -q[1], -q[2], -q[3]))
    return value


def edge_fibres(faces):
    incidence = Counter()
    for i, loop in enumerate(faces):
        for a, b in loop:
            incidence[tuple(sorted((a, b)))] |= 1 << i
    counts = Counter({0: 1})
    for toggle in incidence.values():
        flipped = {bits ^ toggle: count for bits, count in counts.items()}
        counts.update(flipped)
    if len(set(counts.values())) != 1 or sum(counts.values()) != 2**len(incidence):
        raise ValueError("edge law did not have equal fibres")
    return counts


def strip_statistics(length, faces, counts, links):
    traces = [holonomy(face, links)[0] for face in faces]
    integer_traces = [int(t*2) for t in traces]
    if any(2*t != k for t, k in zip(traces, integer_traces)):
        raise ValueError("this integer-weight check needs half-integral traces")
    scale = sum(abs(k) for k in integer_traces)
    mass = left = right = both = 0
    for mask, count in counts.items():
        signs = [1 - 2*((mask >> i) & 1) for i in range(len(faces))]
        # At beta=log(4), exp(beta*t*s)=2^(2*t*s). Use a common shift.
        weight = count << (scale + sum(s*k for s, k in zip(signs, integer_traces)))
        mass += weight
        left += weight * signs[0]
        right += weight * signs[length]
        both += weight * signs[0]*signs[length]
    covariance = F(both, mass) - F(left, mass)*F(right, mass)
    return traces, covariance, traces[0]*traces[length]*covariance


def check_strip(length):
    faces = geometry(length)
    counts = edge_fibres(faces)
    if len(counts) != 2**(4*length+1):
        raise ValueError("incomplete face patterns")
    marks = [((x, 0, 0), (x, 1, 0)) for x in range(length+1)]
    links = dict.fromkeys(marks, I)
    h, m = F(15, 17), F(3, 5)
    q = h**4
    t, cov, physical = strip_statistics(length, faces, counts, links)
    if t != [0]*(length+1) + [1]*(4*length) or cov != q**length or physical:
        raise ValueError("zero-field control failed")
    if length == 1:
        return len(counts), cov, physical
    links[marks[0]] = links[marks[-1]] = U
    t, cov, physical = strip_statistics(length, faces, counts, links)
    if (t[:length+1] != [F(1, 2)] + [0]*(length-1) + [F(1, 2)] or
            t[length+1:] != ([F(1, 2), 1, 1, 1] + [1]*(4*(length-2)) + [F(1, 2), 1, 1, 1])):
        raise ValueError("endpoint or lateral holonomy mismatch")
    k = (h**3*m)**2 * q**(length-2)
    predicted = k*(1-m*m)**2/(4*(1+k*m*m)**2)
    if physical != predicted or cov != 4*predicted:
        raise ValueError("physical covariance mismatch")
    links[marks[0]] = tuple(-v for v in U)
    _, changed, invariant = strip_statistics(length, faces, counts, links)
    if changed != -cov or invariant != physical:
        raise ValueError("physical answer depended on the chosen lift")
    return len(counts), cov, physical


def check_center_moments(order):
    # Two square boundaries share edge a. The other two edge coordinates b,c
    # occur on just one of the squares, so the characters are distinct.
    # The real normalized center traces at the identity are integral or halves.
    cosines = {2: (1, -1), 3: (1, F(-1, 2), F(-1, 2))}[order]
    sums = [0, 0, 0]
    for a, b, c in product(range(order), repeat=3):
        x, y = cosines[(a+b) % order], cosines[(a+c) % order]
        for i, moment in enumerate((x, x*x, x*y)):
            sums[i] += moment
    result = tuple(F(value, order**3) for value in sums)
    if result != (0, 1 if order == 2 else F(1, 2), 0):
        raise ValueError("center character moments failed")
    return result


if __name__ == "__main__":
    for n in (1, 2, 3):
        print("strip", n, *check_strip(n))
    for k in (2, 3):
        print("center order", k, *check_center_moments(k))
