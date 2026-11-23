"""Check all face signatures and all offset maps, including the periodic seams."""
from itertools import combinations, product
import json


def step(v, axis, side):
    return tuple((a+1)%side if i==axis else a for i,a in enumerate(v))


def boundary(v,i,j,side):
    return frozenset(((v,i),(v,j),(step(v,i,side),j),(step(v,j,side),i)))


def check(side, mesh):
    coarse=side//mesh
    axes=tuple(combinations(range(3),2))
    signatures=set()
    for v in product(range(side),repeat=3):
        for i,j in axes:
            face=boundary(v,i,j,side)
            private=frozenset((w,a) for w,a in face if any(w[t]%mesh for t in range(3) if t!=a))
            assert len(private)>=2 and private not in signatures
            signatures.add(private)
            seen=set()
            for w,a in face-private:
                segment=(tuple(t//mesh for t in w),a)
                assert segment not in seen
                seen.add(segment)
    offsets=list(product(range(mesh),repeat=3))
    # Every starting cell is equivalent by coarse translation to one in the last coarse cube.
    # That cube includes each type of edge/face crossing the periodic seam.
    for v in product(range(side-mesh,side),repeat=3):
        for i,j in axes:
            survives=0
            for off in offsets:
                def snapped(w):
                    return tuple(((a+t)//mesh)%coarse for a,t in zip(w,off))
                img=set()
                for w,a in boundary(v,i,j,side):
                    start,end=snapped(w),snapped(step(w,a,side))
                    if start!=end:
                        assert end==step(start,a,coarse)
                        img.symmetric_difference_update(((start,a),))
                if img:
                    assert img==boundary(snapped(v),i,j,coarse)
                    survives+=1
            assert survives==mesh
    return {"side":side,"mesh":mesh,"private_signatures":len(signatures),"offsets":len(offsets)}


if __name__=="__main__":
    print(json.dumps([check(4*l,l) for l in (2,3,4)],indent=2))
