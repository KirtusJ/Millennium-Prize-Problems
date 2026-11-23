"""Exact checks for the site-plane mask, reflected pairings and time-zero witness."""
from fractions import Fraction as Q
from itertools import product
import json


def mask_geometry(length, width):
    time = 3

    def step(x, direction, delta):
        y = list(x)
        y[direction] += delta
        if direction != time:
            y[direction] %= length
        return tuple(y)

    def reflected(x, direction):
        return (*x[:3], -x[time] - int(direction == time))

    def selected(x, direction):
        slab, offset = divmod(x[0], width)
        return ((slab + 1)*width <= length and 0 < offset < width-1
                and direction == slab % 4 and all(0 < k < length-1 for k in x[:3])
                and sum(x[j] for j in range(4) if j != direction) % 2 == 0)

    def guarded(x, direction):
        return selected(x, direction) and (direction == time or x[time] != 0)

    deleted = 0
    incident = 0
    for xyz in product(range(length), repeat=3):
        for t, i in product(range(-2, 3), range(4)):
            x = (*xyz, t)
            assert guarded(reflected(x, i), i) == guarded(x, i)
            if selected(x, i) and not guarded(x, i):
                deleted += 1
            if not guarded(x, i):
                continue
            for j in range(4):
                if j == i:
                    continue
                for root in (x, step(x, j, -1)):
                    edges = ((root, i), (step(root,j,1), i),
                             (root, j), (step(root,i,1), j))
                    assert sum(guarded(y,k) for y,k in edges) == 1
                    times = [v[time] for y,k in edges for v in (y,step(y,k,1))]
                    assert min(times) >= 0 if t >= 0 else max(times) <= 0
                    incident += 1
    assert deleted > 0 and incident > 0
    return {'side':length, 'deleted_plane_links':deleted, 'incident_checks':incident}


def reflected_model():
    # Retained signs a,b have correlation 1/2. The selected signs x,y are
    # conditionally independent, each with conditional mean half its retained sign.
    signs = (-1,1)
    joint = lambda a,b: Q(2+a*b,8)
    kernel = lambda a,x: Q(2+a*x,4)
    f = lambda a,x: 2*a - x + a*x
    g = lambda a,x: 1 + 3*x - a*x
    def mean(h,a):
        return sum(kernel(a,x)*h(a,x) for x in signs)
    raw = sum(joint(a,b)*kernel(a,x)*kernel(b,y)*f(a,x)*g(b,y)
              for a,b,x,y in product(signs,repeat=4))
    projected = sum(joint(a,b)*mean(f,a)*mean(g,b) for a,b in product(signs,repeat=2))
    # Incorrectly freezing reflection on the exterior replaces f(a,.) by f(b,.).
    frozen = sum(joint(a,b)*mean(f,b)*mean(g,b) for a,b in product(signs,repeat=2))
    assert raw == projected and raw != frozen
    return {'raw':str(raw), 'projected':str(projected), 'frozen_exterior':str(frozen)}


def witness_control():
    # X_k = A_k N_k. A is a stationary symmetric two-state chain, and the
    # independent signs N have mean rho. A_0 is a variance-one boundary witness.
    rho, n = Q(1,2), 8
    result = {}
    for name, lam in [('fixed_lattice',Q(1,2)), ('physical_mass',Q(n,n+1)),
                      ('zero_energy_limit',Q(n*n,n*n+1))]:
        transition = lambda a,b: (1 + lam*a*b)/2
        distribution = {1:Q(1),-1:Q(0)}
        for _ in range(n):
            distribution = {b:sum(distribution[a]*transition(a,b) for a in (-1,1))
                            for b in (-1,1)}
        conditional_mean = sum(a*v for a,v in distribution.items())
        overlap = rho*conditional_mean
        # The Markov property gives the later conditional mean by a second
        # independent n-step transition started at the intermediate sign.
        difference = rho*(conditional_mean - conditional_mean**2)
        assert overlap**2 == rho**2*lam**(2*n)
        assert difference**2 == rho**2*lam**(2*n)*(1-lam**n)**2
        result[name] = {'one_time':str(overlap**2),'difference':str(difference**2)}
    return result


def spectral_window():
    # Transfer eigenvalues 0 and 1 encode infinite and zero energy.
    measure = {Q(0):Q(1,4), Q(1,2):Q(1,2), Q(1):Q(1,4)}
    interval = (Q(1,16),Q(15,16))
    inside = sum(m for x,m in measure.items() if interval[0] <= x <= interval[1])
    overlap = sum(m*x*(1-x) for x,m in measure.items())
    energy = sum(m*x**2*(1-x)**2 for x,m in measure.items())
    a = max(interval[0]**2,(1-interval[1])**2)
    lower = (overlap**2 - a)/(1-a)
    assert (overlap**2,energy,lower,inside) == (Q(1,64),Q(1,32),Q(1,85),Q(1,2))
    return {'witness':str(overlap**2),'filtered_mass':str(energy),
            'window_floor':str(lower),'window_mass':str(inside)}


if __name__ == '__main__':
    print(json.dumps({'mask':[mask_geometry(n,4) for n in (16,17)],
                      'reflection':reflected_model(),'witness':witness_control(),
                      'window':spectral_window()},indent=2))
