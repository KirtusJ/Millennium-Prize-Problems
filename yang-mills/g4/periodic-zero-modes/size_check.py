"""Check the torus determinant's finite part without estimating its bulk density."""
from itertools import combinations_with_replacement
import json
from math import factorial, fsum, log, pi, prod, sin


def log_gram(side):
    # Fold opposite momenta, then sort the four axes and restore multiplicities.
    symbols = [4 * sin(pi * k / side)**2 for k in range(side // 2 + 1)]
    signs = [1 if k == 0 or 2*k == side else 2 for k in range(len(symbols))]
    terms = []
    modes = 0
    for ks in combinations_with_replacement(range(len(symbols)), 4):
        if ks[-1] == 0:
            continue
        permutations = 24 // prod(factorial(ks.count(k)) for k in set(ks))
        multiplicity = permutations * prod(signs[k] for k in ks)
        modes += multiplicity
        terms.append(multiplicity * log(fsum(symbols[k] for k in ks)))
    assert modes == side**4 - 1
    return 2*fsum(terms) - 4*log(side)


def continuum_constant():
    # Euler–Maclaurin for zeta'(−1), differentiated at s = −1.
    n = 32
    zeta_prime = fsum([-fsum(k*log(k) for k in range(1, n)),
                       n**2*(log(n)/2 - 1/4), -n*log(n)/2, (1+log(n))/12,
                       1/(720*n**2), -1/(1260*n**4)])
    return -log(2*pi) - (4/3)*log(4) - 12*zeta_prime


if __name__ == "__main__":
    expected = continuum_constant()
    sizes = (4, 8, 16, 32, 64)
    grams = {side: log_gram(side) for side in sizes}
    finite = [(16*grams[side]-grams[2*side])/30 for side in sizes[:-1]]
    errors = [abs(value-expected) for value in finite]
    assert all(a > b for a,b in zip(errors, errors[1:]))
    assert errors[-1] < 0.02
    print(json.dumps({"sides": sizes[:-1], "spectral_finite_parts": [round(x, 7) for x in finite],
                      "unit_torus_log_determinant": round(expected, 7)}, indent=2))
