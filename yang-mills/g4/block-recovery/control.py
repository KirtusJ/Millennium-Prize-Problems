"""Exact controls for reflected tails, ordered root paths and lattice sampling."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json


def threshold_controls():
    grid = [Fraction(i, 4) for i in range(-16, 17)]
    trials = 0
    for u, x, z in product(map(Fraction, [0, 1, 2]), grid, grid):
        def cut(a):
            return int(a > u / 2) - int(a < -u / 2)
        assert int(abs(x) > 3*u/2) <= 2*int(abs(x-z) > u) + cut(x)*cut(z)
        trials += 1
    # Independent Rademacher half-variables. Swap is a reflection with
    # E[f(Y) f(Y o swap)] = E[f(Y)]^2 for every scalar half-test.
    pairs = [(x,y) for x,y in product((-2,2), repeat=2)]
    left = Fraction(sum(abs(x) > Fraction(3,2) for x,y in pairs), len(pairs))
    right = Fraction(sum(abs(x+y) > 1 for x,y in pairs), len(pairs))
    assert left == 2*right == 1
    # Reflection swaps the two entries. Positive raw covariance can coexist
    # with a negative threshold product and failure of the probability bound.
    law = [(5,5,Fraction(1,4)),(2,-2,Fraction(3,8)),(-2,2,Fraction(3,8))]
    mean = sum(m*x for x,y,m in law)
    covariance = sum(m*x*y for x,y,m in law) - mean**2
    cut_product = sum(m*(1 if x*y>0 else -1) for x,y,m in law)
    bad_left = sum(m for x,y,m in law if abs(x)>Fraction(3,2))
    bad_right = sum(m for x,y,m in law if abs(x+y)>1)
    assert covariance==Fraction(27,16) and cut_product==Fraction(-1,2)
    assert bad_left==1 and 2*bad_right==Fraction(1,2)
    return {'grid_cases':trials,'left_probability':str(left),'difference_probability':str(right),
            'positive_covariance_counterexample':str(covariance),'its_cut_product':str(cut_product)}


def invert(word):
    return [(edge,-sign) for edge,sign in reversed(word)]


def reduce_word(word):
    stack = []
    for edge,sign in word:
        if stack and stack[-1] == (edge,-sign):
            stack.pop()
        else:
            stack.append((edge,sign))
    return stack


def step(point, axis, sign):
    end = tuple(v + (sign if i == axis else 0) for i,v in enumerate(point))
    return end, [((point if sign == 1 else end, axis), sign)]


def root_path(point):
    here = (0,0,0,0)
    path = []
    for axis, count in enumerate(point):
        for _ in range(abs(count)):
            here, edge = step(here,axis,1 if count>0 else -1)
            path.extend(edge)
    assert here == point
    return path


def square(point,i,j,si=1,sj=1):
    here = point
    path = []
    for axis,sign in [(i,si),(j,sj),(i,-si),(j,-sj)]:
        here,edge = step(here,axis,sign)
        path.extend(edge)
    assert here == point
    return path


def geometry_controls():
    total = bare_mismatches = 0
    for i,j in combinations(range(4),2):
        for axis in {i,j} - {0}:
            for x in product((-1,0,1),repeat=4):
                b = tuple(-v if k==axis else v for k,v in enumerate(x))
                a, inverse_edge = step(b,axis,-1)
                edge = invert(inverse_edge)
                pb, pa = root_path(b), root_path(a)
                reflected = pb + square(b,i,j,-1 if axis==i else 1,-1 if axis==j else 1) + invert(pb)
                positive = pa + square(a,i,j) + invert(pa)
                gauged_edge = pa + edge + invert(pb)
                transported = invert(gauged_edge) + invert(positive) + gauged_edge
                assert reduce_word(reflected) == reduce_word(transported)
                bare_mismatches += reduce_word(reflected) != reduce_word(invert(positive))
                total += 1
    assert 0 < bare_mismatches < total
    return {'rooted_word_cases':total,'bare_inverse_mismatches':bare_mismatches}


def signed_block(line):
    block = Counter()
    for x, mass in line.items():
        block[x+6] += 2*mass
        block[x+12] -= mass
    return block


def reflected_difference_moments(line):
    w = signed_block(line)
    return [sum(m*(x**k-(-1-x)**k) for x,m in w.items()) for k in (0,1)]


if __name__ == '__main__':
    center = reflected_difference_moments({-2:1,-1:3,0:3,1:1})
    node = reflected_difference_moments({-1:1,0:3,1:1})
    assert center == [0,0] and node == [0,5]
    print(json.dumps({**threshold_controls(),**geometry_controls(),
                      'center_moments':center,'node_moments':node},indent=2))
