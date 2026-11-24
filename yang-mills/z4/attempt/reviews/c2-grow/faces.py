"""Enumerate coarse faces (side 6, coarse sites with even coords) containing the changed coarse edges
E_y = ((2,0,0), y) [W] and E_z = ((2,0,0), z) [B] (ring 1), and the next ring (sharing a coarse edge with ring 1)."""
import itertools
N=6
def edges(f):
    b,(a,c)=f
    def sh(p,d): p=list(p); p[d]=(p[d]+2)%N; return tuple(p)
    return {(b,a),(b,c),(sh(b,a),c),(sh(b,c),a)}
faces=[(b,pl) for b in itertools.product(range(0,N,2),repeat=3) for pl in ((0,1),(0,2),(1,2))]
EY=((2,0,0),1); EZ=((2,0,0),2)
r1=[f for f in faces if EY in edges(f) or EZ in edges(f)]
E1=set().union(*[edges(f) for f in r1])
r2=[f for f in faces if f not in r1 and edges(f)&E1]
if __name__=="__main__":
    print(len(faces),len(r1),r1); print(len(r2),r2)
