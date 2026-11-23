from itertools import product
from math import cosh, exp, fsum, isclose, prod, tanh

beta = 0.8
configs = tuple(product((-1, 1), repeat=4))
next_vertex = (1, 2, 3, 0)
scale = cosh(beta) ** 8


def seam_average(edge_products, couplings, polyakov_factor=False):
    terms = []
    for temporal in configs:
        exponent = sum(
            coupling * edge_sign * temporal[a] * temporal[b]
            for a, (b, edge_sign, coupling) in enumerate(
                zip(next_vertex, edge_products, couplings)
            )
        )
        observable = temporal[0] if polyakov_factor else 1
        terms.append(observable * exp(exponent))
    return fsum(terms) / len(configs)


def close(actual, expected):
    assert isclose(actual, expected, rel_tol=1e-12, abs_tol=1e-12), (
        actual, expected
    )


positive = (beta,) * 4
negative_control = (-beta, beta, beta, beta)
projected_weights = []
naive_weights = []
polyakov_weights = []
positive_quadratic = []
negative_quadratic = []

for x, y in product(configs, repeat=2):
    edge_products = tuple(a * b for a, b in zip(x, y))
    parity = prod(edge_products)
    seam = seam_average(edge_products, positive)
    close(seam, cosh(beta)**4 * (1 + tanh(beta)**4 * parity))
    seam_with_sign = seam_average(edge_products, positive, polyakov_factor=True)
    seam_negative = seam_average(edge_products, negative_control)
    projected_weights.append(seam**2)
    naive_weights.append(exp(2 * beta * sum(edge_products)))
    polyakov_weights.append(seam_with_sign**2)
    positive_quadratic.append(parity * seam**2)
    negative_quadratic.append(parity * seam_negative**2)

pair_count = len(configs) ** 2
projected_ratio = fsum(projected_weights) / pair_count / scale
naive_ratio = fsum(naive_weights) / pair_count / scale
projected_polyakov = fsum(polyakov_weights) / fsum(projected_weights)
naive_polyakov = fsum(naive_weights) / fsum(naive_weights)
q_positive = fsum(positive_quadratic) / pair_count / scale
q_negative = fsum(negative_quadratic) / pair_count / scale

t = tanh(beta)
close(projected_ratio, 1 + t**8)
close(naive_ratio, (1 + t**2) ** 4)
close(projected_polyakov, 0.0)
close(naive_polyakov, 1.0)
close(q_positive, 2 * t**4)
close(q_negative, -2 * t**4)

print("Scaled partition functions", projected_ratio, naive_ratio)
print("Polyakov moments", projected_polyakov, naive_polyakov)
print("Scaled parity quadratics", q_positive, q_negative)
