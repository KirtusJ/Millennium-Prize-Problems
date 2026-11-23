"""Enumerate actual perimeter-preserving face changes and independent Young walks."""
from collections import Counter
from math import prod


def lattice(side, depth):
    # One outer rim includes every face that can touch the initial boundary.
    # The test rejects any permitted move outside the initial square.
    cells = [(x,y) for x in range(-1,side+1) for y in range(-1,side+1)]
    def edge(x,y,axis):
        return 1 << (2*((x+1)*(side+3)+y+1)+axis)
    masks = {}
    for x,y in cells:
        masks[x,y] = edge(x,y,0)|edge(x,y+1,0)|edge(x,y,1)|edge(x+1,y,1)
    start = 0
    for (x,y), mask in masks.items():
        if 0<=x<side and 0<=y<side:
            start ^= mask
    assert start.bit_count()==4*side
    walks = Counter({start:1})
    for level in range(1,depth+1):
        after = Counter()
        for word, mult in walks.items():
            for (x,y), mask in masks.items():
                overlap = word & mask
                d = overlap.bit_count()
                assert d <= 2
                if d != 2:
                    continue
                assert 0<=x<side and 0<=y<side
                assert overlap & (edge(x,y,0)|edge(x,y+1,0))
                assert overlap & (edge(x,y,1)|edge(x+1,y,1))
                after[word ^ mask] += mult
        walks = after
        norm = sum(v*v for v in walks.values())
        expected = 4**level * prod(range(1,2*level,2))
        assert norm == expected
    return walks, start, masks


def toggle(part):
    for row, width in enumerate(part):
        if row==0 or part[row-1]>width:
            yield part[:row]+(width+1,)+part[row+1:]
        if row+1==len(part) or width>part[row+1]:
            yield part[:row]+((width-1,) if width>1 else ())+part[row+1:]
    yield part+(1,)


def compare(side, depth):
    walks, start, masks = lattice(side, depth)
    diagrams = Counter({((),(),(),()):1})
    for _ in range(depth):
        after = Counter()
        for shapes, mult in diagrams.items():
            for corner, part in enumerate(shapes):
                for other in toggle(part):
                    after[shapes[:corner]+(other,)+shapes[corner+1:]] += mult
        diagrams = after
    independent = Counter()
    for shapes, mult in diagrams.items():
        word = start
        for c, part in enumerate(shapes):
            for i,width in enumerate(part):
                for j in range(width):
                    x,y = (i if c%2==0 else side-1-i), (j if c<2 else side-1-j)
                    word ^= masks[x,y]
        independent[word] += mult
    assert len(independent)==len(diagrams) and independent==walks
    print(f"side {side}, depth {depth}, {len(walks)} loop states, "
          f"squared walk norm {sum(v*v for v in walks.values())}")


if __name__ == "__main__":
    for side,depth in ((4,2),(8,2),(10,3),(12,4),(14,5),(16,6)):
        compare(side,depth)
