"""Two Haar charts for the diagonal coefficient and an oriented cubic control."""

import mpmath as mp
from sympy import Matrix, Rational, zeros


def cube_coefficients(root):
    sites = [x for x in range(8) if x != root]
    edges = [(x, x ^ (1 << i)) for x in range(8) for i in range(3)]
    incidence = Matrix([[int(x == z) - int(y == z) for z in sites] for x, y in edges])
    gram = incidence.T * incidence
    assert gram.det() == 49152
    cov = zeros(8)
    pinned = 4 * gram.inv()
    for i, x in enumerate(sites):
        for j, y in enumerate(sites):
            cov[x, y] = pinned[i, j]
    exp_chart = Rational(9) - cov.trace()/4
    imag_chart = Rational(9) + 3*cov.trace()/8
    for x, y in edges:
        a, b, c = cov[x,x], cov[y,y], cov[x,y]
        fourth = 15*(a*a+b*b)
        mixed = 9*a*b+6*c*c
        third_first = 15*c*(a+b)
        exp_chart += fourth/384 + mixed/64 - third_first/96
        imag_chart -= (fourth-2*mixed)/128
    assert exp_chart == imag_chart
    return exp_chart


def cubic_control():
    # Traverse 0 -> 1 -> 3 -> 2 -> 0 in one color. This link vector has
    # zero divergence even with both positive directions on the period-two cube.
    mp.mp.dps = 65
    rot = [mp.eye(2), mp.matrix([[0, 1], [1, 0]]),
           mp.matrix([[0, -1j], [1j, 0]]), mp.matrix([[1, 0], [0, -1]])]
    def group(axis, h):
        if not axis:
            return rot[0]
        return mp.cos(h/2)*rot[0] - mp.j*mp.sin(h/2)*rot[axis]
    cycle = {(0, 1), (1, 3), (3, 2), (2, 0)}
    axis = {1: 1, 3: 2}
    def cost(h):
        total = 0
        for x in range(8):
            for j in range(3):
                y = x ^ (1 << j)
                m = (group(3 if (x,y) in cycle else 0, h)
                     * group(axis.get(x,0), h) * group(axis.get(y,0), -h))
                total += 1-mp.re(m[0,0]+m[1,1])/2
        return total
    h = mp.mpf("1e-8")
    coefficient = 4*(cost(h)-cost(-h))/h**3
    assert abs(coefficient+1) < mp.mpf("1e-15")
    return mp.nstr(coefficient, 18)


if __name__ == "__main__":
    values = {cube_coefficients(root) for root in range(8)}
    assert values == {Rational(149, 16)}
    print("Both charts, all eight roots:", values.pop())
    print("Oriented Wilson cubic in 8F:", cubic_control())
