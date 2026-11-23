"""Walk oriented Wilson words without identifying them by their occupied cells."""
from collections import Counter, defaultdict
from math import comb, prod


def canonical(word):
    # A pinched final walk can revisit a vertex. Preserve the ordered word.
    anchor = min(word)
    return min(word[i:] + word[:i] for i, v in enumerate(word) if v == anchor)


def moves(word):
    hits = defaultdict(list)
    for i, ((x, y), (u, v)) in enumerate(zip(word, word[1:] + word[:1])):
        if y == v:
            hits[min(x, u), y].append(i)
            hits[min(x, u), y-1].append(i)
        else:
            hits[x, min(y, v)].append(i)
            hits[x-1, min(y, v)].append(i)
    for (x, y), edges in hits.items():
        if len(edges) == 1:
            continue
        starts = [i for i in edges if (i-1) % len(word) not in edges]
        assert len(starts) == 1 and len(edges) in (2, 3)
        if len(edges) == 3:
            yield None
            continue
        i = starts[0]
        a, b, c = (word[(i+j) % len(word)] for j in range(3))
        assert a[0] != c[0] and a[1] != c[1]
        other = (a[0] + c[0] - b[0], a[1] + c[1] - b[1])
        idx = (i+1) % len(word)
        yield canonical(word[:idx] + (other,) + word[idx+1:])


def check(side):
    word = tuple([(x, 0) for x in range(side)] +
                 [(side, y) for y in range(side)] +
                 [(x, side) for x in range(side, 0, -1)] +
                 [(0, y) for y in range(side, 0, -1)])
    walks = Counter({canonical(word): 1})
    for depth in range(1, side+1):
        after = Counter()
        blocked = weighted = 0
        for word, count in walks.items():
            assert len(set(word)) == len(word)
            for nxt in moves(word):
                if nxt is None:
                    blocked += 1
                    weighted += count
                else:
                    after[nxt] += count
        expected = 4**depth * prod(range(1, 2*depth, 2))
        if depth == side:
            expected -= 4 * comb(2*side, side)
            assert (blocked, weighted) == (4*side, 4*2**(side-1))
        else:
            assert blocked == weighted == 0
        assert sum(v*v for v in after.values()) == expected
        walks = after
    pinched = [count for word, count in walks.items() if len(set(word)) < len(word)]
    assert pinched == ([2, 2] if side == 2 else [])
    print(f"side {side}: {len(walks)} words, {blocked} blocked contacts, squared count {expected}")


if __name__ == "__main__":
    for size in range(2, 10):
        check(size)
