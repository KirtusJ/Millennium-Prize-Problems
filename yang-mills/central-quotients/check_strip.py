"""Exact edge-sign pushforward on the open cube strips in cube-strip.md."""
from collections import Counter
from fractions import Fraction


def cube_face(x, normal, side):
    base = [x, 0, 0]
    base[normal] += side
    u, v = [axis for axis in range(3) if axis != normal]
    corners = []
    for i, j in ((0, 0), (1, 0), (1, 1), (0, 1)):
        point = base.copy()
        point[u] += i
        point[v] += j
        corners.append(tuple(point))
    return frozenset(tuple(sorted((corners[k], corners[(k + 1) % 4]))) for k in range(4))


def direct_ratios(length):
    faces = sorted({cube_face(x, d, s) for x in range(length) for d in range(3)
                    for s in range(2)}, key=sorted)
    edges = sorted(set().union(*faces))
    patterns = Counter({0: 1})
    top_edges = {edge for edge in edges if edge[0][1:] == edge[1][1:] == (1, 1)}
    for edge in edges:
        flips = sum(1 << i for i, face in enumerate(faces) if edge in face)
        before = patterns.copy()
        for mask, count in before.items():
            patterns[mask ^ flips] += count
    if sum(patterns.values()) != 2**len(edges):
        raise ValueError("edge assignment count changed")
    # These faces have trace zero for the second configuration. Every other
    # face has identity holonomy. The cube geometry gives at most one marked edge per face.
    marked = [len(face & top_edges) for face in faces]
    if max(marked) != 1:
        raise ValueError("unexpected upper-edge incidence")
    untouched = sum(1 << i for i, count in enumerate(marked) if count == 0)
    ratios = []
    for active in ((1 << len(faces)) - 1, untouched):
        size = active.bit_count()
        total = sum(count * Fraction(2)**(size - 2*(mask & active).bit_count())
                    for mask, count in patterns.items())
        ratios.append(total / 2**len(edges) / Fraction(5, 4)**size)
    return len(edges), len(faces), len(patterns), ratios


if __name__ == "__main__":
    h = Fraction(3, 5)
    previous, current = Fraction(1), 1 + h**6
    for length in range(1, 4):
        edges, faces, count, ratios = direct_ratios(length)
        if ratios != [current, 1]:
            raise ValueError(f"strip {length}: direct ratios {ratios}, recurrence {current}")
        print(length, edges, faces, count, *ratios)
        previous, current = current, (1 + h**4)*current - (h**4 - h**6)*previous
