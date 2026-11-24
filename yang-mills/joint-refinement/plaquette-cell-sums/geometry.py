"""Enumerate coarse spoke ownership and test couplings through fine action faces."""
from itertools import combinations, product
from collections import Counter


def check(n):
    sites=list(product(range(n),repeat=3))
    orient=list(combinations(range(3),2))
    owners={}
    sites_even=list(product(range(0,n,2),repeat=3))
    def move(v,i,amount=1):
        return tuple((x+amount*(i==j))%n for j,x in enumerate(v))
    for o,(i,j) in enumerate(orient):
        for base in sites_even:
            edge_i=move(base,j)
            edge_j=move(base,i)
            spokes=[(edge_i,i),(move(edge_i,i),i),(edge_j,j),(move(edge_j,j),j)]
            for e in spokes:
                assert e not in owners
                owners[e]=(o,base)
    assert len(owners)==12*len(sites_even)
    cross=0
    active=set()
    for v in sites:
        parity=sum((x%2)<<i for i,x in enumerate(v))
        for o,(i,j) in enumerate(orient):
            u=(v if v[j]%2 else move(v,j),i)
            w=(v if v[i]%2 else move(v,i),j)
            if u in owners or w in owners:
                assert owners[u]==owners[w] and owners[u][0]==o
                key=(8*o+parity,owners[u])
                assert key not in active
                active.add(key)
    per_cell=Counter(cell for _,cell in active)
    assert set(per_cell)==set(owners.values()) and set(per_cell.values())=={4}
    assert len({colour for colour,_ in active})==12
    for v in sites:
        for i,j in orient:
            edges=((v,i),(move(v,i),j),(move(v,j),i),(v,j))
            cells={owners[e] for e in edges if e in owners}
            assert len({o for o,_ in cells})==len(cells)
            cross+=len(cells)>1
    # At a time-like face only the single spatial link at the tested slice can belong.
    print(f"fine side {n}, {len(owners)} spokes, cross-orientation faces {cross}")
    assert cross>0


if __name__=="__main__":
    for n in (6,8,10,12,16):
        check(n)
