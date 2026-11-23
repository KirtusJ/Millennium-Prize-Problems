"""Finite even-torus site cuts, shared-face multiplicities, and a direct Wilson sum."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json
from random import Random


def shifted(pos, axis, distance, side):
    q = list(pos)
    q[axis] = (q[axis]+distance) % side
    return tuple(q)


def reflected(pos, axis, side):
    return shifted(pos,axis,-2*pos[axis],side)


def qmul(x,y):
    # Signed indices 1,2,3,4 represent the quaternion units 1,i,j,k.
    table = ((1,2,3,4),(2,-1,4,-3),(3,-4,-1,2),(4,3,-2,-1))
    return (1 if x*y>0 else -1)*table[abs(x)-1][abs(y)-1]


def inv(q):
    return q if abs(q)==1 else -q


def action(link, pos, i, j, side):
    word = qmul(qmul(link(pos,i),link(shifted(pos,i,1,side),j)),
                qmul(inv(link(shifted(pos,j,1,side),i)),inv(link(pos,j))))
    return 1 - (word if abs(word)==1 else 0)


def quaternion_cuts(side):
    pts = list(product(range(side),repeat=4))
    rng = Random(45+side)
    values = {(x,a):rng.choice((-4,-3,-2,-1,1,2,3,4)) for x in pts for a in range(4)}
    get = lambda x,a: values[x,a]
    counts = []
    rejected = 0
    for axis in range(4):
        def mirrored(x,a, shift_normal=True):
            y = reflected(x,axis,side)
            if a==axis:
                return inv(get(shifted(y,a,-1,side) if shift_normal else y,a))
            return get(y,a)
        parts = Counter()
        for x in pts:
            for i,j in combinations(range(4),2):
                normal = axis in (i,j)
                t = x[axis]
                piece = "boundary" if not normal and t in (0,side//2) else ("plus" if t<side//2 else "minus")
                parts[piece] += 1
                face = reflected(x,axis,side)
                if normal:
                    face = shifted(face,axis,-1,side)
                expected = action(get,face,i,j,side)
                assert action(mirrored,x,i,j,side) == expected
                if normal and action(lambda v,a:mirrored(v,a,False),x,i,j,side)!=expected:
                    rejected += 1
        assert parts["boundary"]==6*side**3 and parts["plus"]==parts["minus"]
        assert sum(parts.values())==6*side**4
        counts.append(dict(parts))
    assert rejected>0
    return {"side":side,"cuts":len(counts),"faces_per_plane_pair":counts[0]["boundary"],
            "wrong_normal_anchor_mismatches":rejected}


def multiplicity(side, orient):
    # An assigned face is represented by its canonical lower site and two
    # positive directions. Unwrapped cube anchors stay in [0,k) in each axis.
    zero = (0,)*4
    cells = [(zero,zero)]
    k = 1 << (side.bit_length()-1)
    for a in range(4):
        w = 1
        while 2*w <= side:
            doubled = []
            for c,f in cells:
                u,v = list(c),list(f)
                u[a] = 2*w-1-c[a]
                v[a] = (2*w-f[a]-int(a in orient))%side
                doubled.append((tuple(u),tuple(v)))
            cells += doubled
            w *= 2
    assert len(cells)==k**4==len({c for c,f in cells})
    assert 16*len(cells)>side**4
    count = Counter()
    for c,f in cells:
        for a in range(4):
            assert (f[a]-c[a])%side in ((0,) if a in orient else (0,1))
        count[f]+=1
    assert max(count.values())<=4
    return max(count.values())


def z2_exact():
    # Four time layers and two spatial sites. Keep all 16 directed positive
    # links labelled, with independent Haar signs. plaquette weights are 2 or 1.
    def face(s,n,t,x):
        return s[2*t+x]*s[2*((t+1)%4)+x]*n[2*t+x]*n[2*t+1-x]
    def weight(s,n,t):
        return (1+int(face(s,n,t,0)>0))*(1+int(face(s,n,t,1)>0))
    def test(s,n):
        return 1+s[0]+2*s[4]+s[2]*n[0]+face(s,n,0,0), s[5]-n[3]+s[3]*n[2]
    real = imag = partition = haar_numerator = 0
    for links in product((-1,1),repeat=16):
        s,n = links[:8],links[8:]
        w = weight(s,n,0)*weight(s,n,1)*weight(s,n,2)*weight(s,n,3)
        rs = tuple(s[2*((-t)%4)+x] for t in range(4) for x in range(2))
        rn = tuple(n[2*((-t-1)%4)+x] for t in range(4) for x in range(2))
        a,b = test(rs,rn)
        c,d = test(s,n)
        real += w*(a*c+b*d)
        haar_numerator += a*c+b*d
        imag += w*(a*d-b*c)
        partition += w
    squares = norm = 0
    for boundary in product((-1,1),repeat=4):
        r = i = h = 0
        for interior in product((-1,1),repeat=6):
            s = [*boundary[:2],*interior[:2],*boundary[2:],0,0]
            n = [*interior[2:],0,0,0,0]
            w = weight(s,n,0)*weight(s,n,1)
            a,b = test(s,n)
            h += w
            r += w*a
            i += w*b
        norm += h*h
        squares += r*r+i*i
    assert real==squares and imag==0 and partition==norm and real>0
    assert Fraction(haar_numerator,2**16) != Fraction(real,partition)
    return {"configurations":2**16,"expectation":str(Fraction(real,partition)),
            "uncoupled_expectation":str(Fraction(haar_numerator,2**16)),
            "imaginary_numerator":imag,"full_partition_sum":partition}


def rooted_score():
    def scalar(q):
        return q if abs(q)==1 else 0
    units = (-4,-3,-2,-1,1,2,3,4)
    checks = bad = 0
    for a,u,b,x,sign in product(units,units,units,(2,3,4),(-1,1)):
        edge = u if sign==1 else inv(u)
        word = qmul(qmul(a,edge),b)
        v = a if sign==1 else qmul(a,edge)
        derivative = qmul(x,u) if sign==1 else -qmul(edge,x)
        actual = -scalar(qmul(qmul(a,derivative),b))
        conjugate = qmul(qmul(inv(v),word),v)
        assert actual == -sign*scalar(qmul(x,conjugate))
        bad += actual != -sign*scalar(qmul(x,word))
        checks += 1
    assert bad>0
    return {"score_incidences":checks,"wrong_unrooted_score_mismatches":bad}


def gaussian_checks():
    Q = Fraction
    for rho in (Q(1,2),Q(2,3),Q(3,5)):
        s = (1-rho)**2/rho
        for length in (4,8,16):
            kernel = [(rho**n+rho**(length-n))/((1/rho-rho)*(1-rho**length))
                      for n in range(length)]
            for n in range(length):
                assert (2+s)*kernel[n]-kernel[n-1]-kernel[(n+1)%length]==int(n==0)
    # A rational quadrature matching the first four standard Gaussian moments.
    weights = {0:Q(1,2),1:Q(1,6),-1:Q(1,6),2:Q(1,12),-2:Q(1,12)}
    rho = Q(3,5)
    lhs = mean = variance2 = 0
    for x,y,h in product(weights,weights,(-1,2)):
        w = weights[x]*weights[y]/2
        first,second = Q((x+h)**2,2),(rho*x+Q(4,5)*y+h)**2/2
        mean += w*first
        variance2 += w*first**2
        lhs += w*first*second
    a,b = Q(5,2),Q(9,16)  # E H², Var(H²/2)
    assert lhs-mean**2==rho**2/2+a*rho+b
    assert variance2-mean**2==Q(1,2)+a+b
    assert (lhs-mean**2)/(variance2-mean**2)>=rho**2
    return {"periodic_green_recurrences":84,"shifted_covariance":str(lhs-mean**2),
            "shifted_variance":str(variance2-mean**2)}


def main():
    overlap = {str(side):max(multiplicity(side,o) for o in combinations(range(4),2))
               for side in (4,6,8,10,14)}
    assert max(overlap.values()) == 4
    return {"nonabelian_link_cuts":[quaternion_cuts(side) for side in (4,6)],
            "largest_repeated_face":overlap,"z2":z2_exact(),
            "rooted_score":rooted_score(),"gaussian":gaussian_checks()}


if __name__=="__main__":
    print(json.dumps(main(),indent=2))
