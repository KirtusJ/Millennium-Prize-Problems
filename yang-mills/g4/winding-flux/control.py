"""Exact finite controls for the electric-flux projection and minimal spin networks."""
from collections import defaultdict, Counter
from fractions import Fraction as Q
from itertools import product
from math import comb
import json


# The signed integers ±1, ±2, ±3, ±4 represent ±1, ±i, ±j, ±k.
Q8 = (1,-1,2,-2,3,-3,4,-4)
TABLE = ((1,2,3,4),(2,-1,4,-3),(3,-4,-1,2),(4,3,-2,-1))


def mul(a,b):
    return (1 if a*b>0 else -1)*TABLE[abs(a)-1][abs(b)-1]


def inv(a):
    return a if abs(a)==1 else -a


def character(a,b):
    return (-1)**((a & b).bit_count() % 2)


def slab_control():
    # Two vertices joined by four links with three independent cycle windings.
    # Normalizations common to every twist cancel in Fourier ratios.
    winds = (0,1,2,4)
    p = Q(3,4)  # exp(beta_t)=2
    classes, bernoulli = {}, {}
    for mask in range(16):
        occupied = [i for i in range(4) if mask & (1<<i)]
        span = {0}
        for i in occupied[1:]:
            cycle = winds[occupied[0]] ^ winds[i]
            span |= {c ^ cycle for c in span}
        classes[mask] = span
        bernoulli[mask] = p**len(occupied)*(1-p)**(4-len(occupied))
    forbidden, negative, nonzero = 0, False, set()
    answers = []
    for U,external_twist in product(((1,1,1,1),(1,2,3,4)),(0,7)):
        V = [character(external_twist,w)*u for w,u in zip(winds,U)]
        rows = [[0]*8 for _ in range(16)]
        direct = [0]*8
        for z,gx,gy in product(range(8),Q8,Q8):
            factors = []
            for w,u,v in zip(winds,U,V):
                hol = mul(mul(mul(inv(u),gx),character(z,w)*v),inv(gy))
                x = hol if abs(hol)==1 else 0
                factors.append(2**(1+x)-1)
            weights = [1]
            for b in factors:
                weights += [b*n for n in weights]
            direct[z] += (1+factors[0])*(1+factors[1])*(1+factors[2])*(1+factors[3])
            for mask,n in enumerate(weights):
                rows[mask][z] += n
        assert all(direct[z]==sum(row[z] for row in rows) for z in range(8))
        ratios = []
        for h in range(1,8):
            projected = 0
            for mask,row in enumerate(rows):
                val = sum(character(h,z)*v for z,v in enumerate(row))
                if h not in classes[mask]:
                    assert val == 0
                    forbidden += 1
                projected += val
            ratio = Q(projected,sum(direct))
            bound = sum(w for mask,w in bernoulli.items() if h in classes[mask])
            assert abs(ratio) <= bound
            if ratio:
                nonzero.add(h)
            negative |= ratio < 0
            ratios.append(str(ratio))
        answers.append(ratios)
    assert nonzero == set(range(1,8)) and negative
    return {"cancelled_coefficients":forbidden,"signed_fourier_ratios":answers}


def axis_choices(L,axis):
    # Pick one occupied link in every parallel cut. Store odd- and double-
    # incidence vertices as bit masks. No use of the closed loop count formula.
    loc = range(L)
    ends = []
    for s in loc:
        pairs = []
        for t,z in product(loc,repeat=2):
            x,y = (s,t) if axis==0 else (t,s)
            a = x+L*(y+L*z)
            b = (x+1)%L+L*(y+L*z) if axis==0 else x+L*((y+1)%L+L*z)
            pairs.append((1<<a)|(1<<b))
        ends.append(pairs)
    for choice in product(*ends):
        odd, double = 0, 0
        for pair in choice:
            double |= odd & pair
            odd ^= pair
        yield odd, double


def two_charge_count(L):
    boundary = defaultdict(list)
    for odd,double in axis_choices(L,0):
        boundary[odd].append(double)
    supports = Counter()
    for odd,double in axis_choices(L,1):
        for xdouble in boundary.get(odd,()):
            supports[(xdouble & double).bit_count()] += 1
    dimension = sum(count*2**junctions for junctions,count in supports.items())
    assert dimension == L**2*comb(2*L,L)+L**4-L**3
    return {"dimension":dimension,"supports_by_four_valent_vertices":dict(supports)}


def haar_partition(t):
    """Enclose SU(2) Haar integral of exp(t Re g) by its positive series."""
    term = total = Q(1)
    for j in range(1,7):
        term *= t*t/(4*j*(j+1))
        total += term
    ratio = t*t/(4*7*8)
    return total,total+term*ratio/(1-ratio)


def continuous_slab():
    # For identity boundary fields on the same two-site graph, gx gy^-1 is Haar.
    # Every twisted slab entry is exactly a one-link partition integral.
    beta = Q(1,40)
    entries = [haar_partition(beta*(4-2*z.bit_count())) for z in range(8)]
    den_lo = sum(lo for lo,hi in entries)
    den_hi = sum(hi for lo,hi in entries)
    bond_lo = 2*beta-(2*beta)**2/2
    counts = {}
    for h in range(1,8):
        lower = sum(lo if character(h,z)>0 else -hi for z,(lo,hi) in enumerate(entries))
        upper = sum(hi if character(h,z)>0 else -lo for z,(lo,hi) in enumerate(entries))
        needed = h.bit_count() + h.bit_count()%2
        # The unique Eulerian subset on these four parallel edges with class h
        # consists of the chosen twisted edges plus the reference edge for odd parity.
        assert lower/den_hi > 0 and upper/den_lo < bond_lo**needed
        counts[h] = needed
    return {"beta":"1/40","verified_characters":len(counts),"witness_sizes":list(counts.values())}


def rooted_bound():
    # beta_t <= 1/40 implies 5(1-exp(-2 beta_t)) <= 1/4.
    rows = {}
    for L in (4,8,16):
        q = Q(1,4)
        upper = L**2*q**L/(5*(1-q))
        assert upper <= Q(4,15)*Q(1,2)**L
        rows[str(L)] = str(upper)
    return rows


if __name__ == "__main__":
    print(json.dumps({"quaternion_slab":slab_control(),"SU2_slab":continuous_slab(),"two_charge":two_charge_count(4),
                      "charged_norm_upper":rooted_bound()},sort_keys=True))
