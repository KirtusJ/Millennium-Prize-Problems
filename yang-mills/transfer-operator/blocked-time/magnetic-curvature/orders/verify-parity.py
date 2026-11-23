from collections import Counter
from itertools import combinations, product

def edges(p,L):
    xyz,a,b=p
    def add(i):
        return tuple((v+(d==i))%L for d,v in enumerate(xyz))
    return [(xyz,a),(add(b),a),(xyz,b),(add(a),b)]

def audit(faces,L):
    counts=Counter(e for p in faces for e in edges(p,L))
    assert all(x%2==0 for x in counts.values())
    for d in range(3):
        slabs=Counter(x[d] for x,a,b in faces if d in (a,b))
        assert all(v>=2 for v in slabs.values())
        assert 2*len(slabs)<=len(faces)
        if len(faces)<2*L: assert len(slabs)<L

for L in (6,8):
    for base in product(range(L), repeat=3):
        cube=[]
        for a,b in combinations(range(3),2):
            d=3-a-b
            for s in (0,1):
                x=tuple((v+s*(i==d))%L for i,v in enumerate(base))
                cube.append((x,a,b))
        audit(cube,L)
    ring=[((i,0,0),0,1) for i in range(L)]
    audit(ring*2,L)
    assert len({p[0][0] for p in ring})==L
    print(f'{L**3} closed cube masks and a doubled winding strip on side {L}')
