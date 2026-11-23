"""Exact finite checks of the local rotation certificate and periodic conflict count."""
from fractions import Fraction as F
from itertools import product


def mul(p, q):
    a, b, c, d = p
    e, f, g, h = q
    return (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)


def rotation(axis, sign):
    v = [F(4, 5), 0, 0, 0]
    v[axis + 1] = sign * F(3, 5)
    return tuple(v)


def rotation_test():
    A = (F(1,5), F(2,5), F(-2,5), F(4,5))
    B = (F(-4,5), F(1,5), F(2,5), F(2,5))
    terms = []
    for i,j in product(range(3), repeat=2):
        mixed = 0
        for s,t in product((-1,1), repeat=2):
            P = mul(rotation(i,s), A)
            Q = mul(rotation(j,-t), B)
            value = 2*mul(P,Q)[0] + 5*P[2] - 7*Q[1] + 13
            mixed += s*t*value/4
        terms.append(mixed**2)
    a = mul(A,B)[0]
    exact = 4*F(3,5)**4*(2+a*a)/9
    assert sum(terms)/9 == exact
    print("mixed coefficient, squared and averaged:", exact)


def conflict_test(n):
    origin = (0,0,0,0)
    def shift(p, axis, delta):
        q = list(p)
        q[axis] = (q[axis] + delta) % n
        return tuple(q)
    def block(p):
        return {p, shift(p,1,1)}  # origins of the two x-directed links
    # Every action face meeting a block through an x-link contains a second,
    # parallel x-link displaced by a unit step perpendicular to x.
    neighborhood = set(block(origin))
    for e in block(origin):
        for j,sign in product((1,2,3),(-1,1)):
            neighborhood.add(shift(e,j,sign))
    slice_points = [p+(0,) for p in product(range(n),repeat=3)]
    conflicts = {p for p in slice_points if block(p) & neighborhood}
    assert len(conflicts) <= 11
    assert [p for p in slice_points if block(p) == block(origin)] == [origin]
    print(f"{n}^4 torus: closed neighborhood {len(conflicts)}")


if __name__ == "__main__":
    rotation_test()
    for n in (3,4,5,8):
        conflict_test(n)
