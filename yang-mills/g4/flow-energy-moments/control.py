"""Exact controls for the spatial Wilson time jets and finite energy moment tests."""
from fractions import Fraction as Q
from itertools import product
import json
import math


def mul(a, b, limit=None):
    stop = len(a) + len(b) - 1
    size = min(stop, limit + 1) if limit is not None else stop
    out = [Q(0)] * size
    for i, x in enumerate(a):
        for j, y in enumerate(b[:max(0, size-i)]):
            out[i+j] += x*y
    return out


def add(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for terms in (a, b):
        for j, c in enumerate(terms):
            out[j] += c
    return out


def evaluate(a, x):
    return sum(c*x**i for i, c in enumerate(a))


def quaternion_counts():
    # Absolute counts suffice because conjugation and order change only signs.
    # The output basis label of unit quaternion basis factors is their bitwise XOR.
    def label(word):
        result = 0
        for component in word:
            result ^= component
        return result
    plaquette = [0]*4
    projected_force = [0]*4
    for word in product(range(4), repeat=4):
        target = label(word)
        plaquette[target] += 1
        if target:
            for link in range(4):
                projected_force[target ^ link] += 1
    assert plaquette == [64]*4 and [4*n for n in projected_force] == [768]*4
    return {"deficit_coefficient_bound":65, "four_face_force_bound":768}


def staggered_flow():
    # On this invariant Wilson configuration the deficit obeys F' = 4F(F-2).
    # Compose its time jets with (atanh z)/4 using rational coefficients.
    n = 12
    clock = [Q(1,4*j) if j % 2 else Q(0) for j in range(n+1)]
    for initial in (Q(1), Q(2,3), Q(3,2)):
        result, power, jet = [Q(0)], [Q(1)], [Q(0),Q(1)]
        for k in range(n+1):
            weight = evaluate(jet, initial)/math.factorial(k)
            result = add(result, [weight*c for c in power])
            power = mul(power, clock, n)
            derivative = [i*c for i,c in enumerate(jet) if i]
            jet = mul(derivative, [0,-8,4])
        # The exact conjugated deficit is F0 (1-z)/(1+(1-F0)z).
        recovered = mul(result,[1,1-initial],n)
        assert recovered == [initial,-initial]+[0]*(n-1)
    return {"orders_through":n, "initial_deficits":["1","2/3","3/2"]}


def low_mean(poly):
    # Uniform probability on (0,1/2).
    return sum(c*Q(1,(j+1)*2**j) for j,c in enumerate(poly))


def chebyshev_shifted(n):
    prev, current = [Q(1)], [3,-2]
    for _ in range(1,n):
        prev, current = current, add(mul([6,-4], current), [-c for c in prev])
    return current


def interpolation_control(nodes, chebyshev):
    weights = []
    for j,x in enumerate(nodes):
        cardinal = [Q(1)]
        for i,y in enumerate(nodes):
            if i != j:
                cardinal = mul(cardinal,[-y/(x-y),1/(x-y)])
        weights.append(low_mean(cardinal))
    degree = len(nodes)-1
    assert all((-1)**j*w > 0 for j,w in enumerate(weights))
    total = sum(abs(w) for w in weights)
    mass = (1+total)/2
    assert mass == sum(weights[::2])
    if chebyshev:
        assert total == low_mean(chebyshev_shifted(degree))
    def pair(test):
        low = low_mean(test) - sum(w*evaluate(test,x) for x,w in zip(nodes[1::2], weights[1::2]))
        high = sum(w*evaluate(test,x) for x,w in zip(nodes[::2], weights[::2]))
        return low/mass, high/mass
    for j in range(degree+1):
        low, high = pair([0]*j+[1])
        assert low == high
    if degree == 2:
        test = mul([-1,1],mul([-Q(3,2),1],[-Q(3,2),1]))
        low, high = pair(test)
        assert low < 0 < high and 1/mass == Q(3,19)
        return {"low_weight":str(1/mass),"shifted_forms":[str(low),str(high)]}
    return str(1/mass)


def moment_controls():
    rows = {}
    for n in (1,2,3,4,8):
        if n == 3:
            nodes = [Q(1),Q(5,4),Q(7,4),Q(2)]
        else:
            nodes = [1+Q(i,n) for i in range(n+1)]
        rows[str(n)] = interpolation_control(nodes,n<=3)
    return rows


def bare_edge():
    # Lower Taylor sum for exp(28), with the known beta-one inverse budget.
    ratio = Q(2**34 * 200, 3)
    assert sum(Q(28**j, math.factorial(j)) for j in range(49)) > ratio
    return {"coupling":1,"lattice_energy_upper_bound":28}


if __name__ == "__main__":
    print(json.dumps({"quaternions":quaternion_counts(),"time_jets":staggered_flow(),"bare_edge":bare_edge(),
                      "matched_energy_moments":moment_controls()},sort_keys=True))
