"""G4 independent exact check, using geometric cube vertices and quaternion products."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json

vertices = list(product(range(2), repeat=3))
edges = [(a,b) for a,b in combinations(vertices,2)
         if sum(x!=y for x,y in zip(a,b))==1]
faces = [[i for i,(a,b) in enumerate(edges) if a[axis]==b[axis]==side]
         for axis in range(3) for side in range(2)]
assert len(edges)==12 and all(len(f)==4 for f in faces)
counts=Counter()
weight=Fraction(0)
for bits in product(range(2), repeat=len(edges)):
    parity=tuple(sum(bits[e] for e in f)%2 for f in faces)
    counts[parity]+=1
    weight+=Fraction(2)**(6-2*sum(parity))
weight/=2**len(edges)
independent=Fraction(5,4)**6
assert weight==Fraction(8177,2048)
assert weight-independent==Fraction(729,4096)
assert len(counts)==32 and set(counts.values())=={128}
assert all(sum(pattern)%2==0 for pattern in counts)

def mul(p,q):
    a,b,c,d=p
    e,f,g,h=q
    return (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)

basis=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
commuting=0
patterns=Counter()
for row in product(range(4), repeat=4):
    qs=[basis[x] for x in row]
    pattern=tuple(mul(qs[i],qs[j])!=mul(qs[j],qs[i]) for i,j in combinations(range(4),2))
    patterns[pattern]+=1
    can_lift=False
    for signs in product((-1,1),repeat=4):
        lifts=[tuple(s*x for x in q) for s,q in zip(signs,qs)]
        good=all(mul(lifts[i],lifts[j])==mul(lifts[j],lifts[i]) for i,j in combinations(range(4),2))
        assert good == (not any(pattern))
        can_lift |= good
    commuting+=can_lift
assert commuting==46 and len(patterns)==36
assert patterns[(False,)*6]==46
assert all(v==6 for k,v in patterns.items() if any(k))
result={'cube':{'edge_assignments':4096,'face_patterns':len(counts),
                'multiplicity':128,'pushforward':str(weight),
                'independent_face_weight':str(independent),'difference':str(weight-independent)},
        'flat_lifts':{'tuples':256,'commuting':commuting,'noncommuting':256-commuting,
                      'flux_patterns':len(patterns),'nonzero_pattern_multiplicity':6},
        'limits':'Finite exact checks. No continuum field theory or spectral gap conclusion.'}
print(json.dumps(result,indent=2))
