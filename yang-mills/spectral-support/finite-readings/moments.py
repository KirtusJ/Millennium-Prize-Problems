"""Exact finite transfer-moment tests for Gaussian-rational Hermitian input.

Times are consecutive multiples of one positive step. A failure is with
respect to these exact entries. No rounding or eigenvalue tolerance is used.
"""
from dataclasses import dataclass

import sympy as sp


class Incompatible(ValueError):
    """An exact positivity or support condition failed."""


def _checked(entries):
    blocks = [sp.Matrix(block).applyfunc(sp.expand) for block in entries]
    if not blocks or blocks[0].rows == 0:
        raise ValueError("at least one nonempty matrix is required")
    size = blocks[0].rows
    for block in blocks:
        if block.shape != (size, size) or block != block.H:
            raise ValueError("supply Hermitian matrices of the same size")
        if any(not all(part.is_Rational for part in z.as_real_imag()) for z in block):
            raise ValueError("supply exact rational real and imaginary parts")
    return blocks


def _interval(low, high, *, vacuum=True):
    low, high = sp.sympify(low), sp.sympify(high)
    if not all(x.is_Rational for x in (low, high)):
        raise ValueError("transfer bounds must be exact rationals")
    if not (0 <= low < high <= 1) or (vacuum and high == 1):
        raise ValueError("require 0 <= low < high, with high strictly below the vacuum")
    return low, high


def psd(matrix):
    """Hermitian PSD, including singular pivots, by exact Schur elimination."""
    matrix = matrix.applyfunc(sp.expand)
    if matrix != matrix.H:
        return False
    while matrix.rows:
        pivot = matrix[0, 0]
        column = matrix[1:, 0]
        if pivot < 0 or (pivot == 0 and any(column)):
            return False
        matrix = matrix[1:, 1:]
        if pivot:
            matrix = (matrix - column*column.H/pivot).applyfunc(sp.expand)
    return True


def _require(matrix, condition):
    if not psd(matrix):
        raise Incompatible(condition)


def _hankel(blocks, count, offset=0):
    return sp.Matrix.vstack(*(sp.Matrix.hstack(*blocks[i+offset:i+offset+count])
                              for i in range(count)))


@dataclass
class Realization:
    metric: sp.Matrix
    transfer: sp.Matrix
    probes: sp.Matrix
    vacuum: sp.Matrix
    zero_atom: sp.Matrix

    def reading(self, k):
        if not isinstance(k, int) or k < 0:
            raise ValueError("time index must be a nonnegative integer")
        answer = self.vacuum + self.probes.H*self.metric*(self.transfer**k)*self.probes
        if k == 0:
            answer += self.zero_atom
        return answer.applyfunc(sp.expand)

    def has_finite_energies(self):
        return self.transfer.rank() == self.transfer.rows and not any(self.zero_atom)


def _interval_model(blocks, low, high):
    """Odd truncation supported on [low, high], with no separate vacuum."""
    count = len(blocks)//2
    if not count or len(blocks) != 2*count:
        raise ValueError("need readings numbered 0 through an odd index")
    h = _hankel(blocks, count)
    k = _hankel(blocks, count, 1)
    _require(k-low*h, "lower interval pencil")
    _require(high*h-k, "upper interval pencil")
    pivots = list(h.rref()[1])
    size = blocks[0].rows
    metric = h.extract(pivots, pivots)
    inverse = metric.inv()
    transfer = (inverse*k.extract(pivots, pivots)).applyfunc(sp.expand)
    probes = (inverse*h.extract(pivots, list(range(size)))).applyfunc(sp.expand)
    return Realization(metric, transfer, probes, sp.zeros(size), sp.zeros(size))


def odd_completion(entries, high, *, low=0, vacuum=None):
    """Fit 2r+2 readings on [low,high] union {1}. Maximize the vacuum Gram
    in Loewner order if it is unspecified. A positive low enforces finite energies.
    """
    blocks = _checked(entries)
    low, high = _interval(low, high)
    count = len(blocks)//2
    if not count or 2*count != len(blocks):
        raise ValueError("need readings numbered 0 through an odd index")
    m = blocks[0].rows
    if vacuum is None:
        lower = _hankel(blocks, count, 1) - low*_hankel(blocks, count)
        _require(lower, "raw lower interval pencil")
        # In the basis 1, (1-u), u(1-u), ... only the first block sees the vacuum.
        change = sp.zeros(count)
        change[0, 0] = 1
        for i in range(1, count):
            change[i-1, i], change[i, i] = 1, -1
        transform = sp.kronecker_product(change, sp.eye(m))
        mixed = transform.H*lower*transform
        trailing = mixed[m:, m:]
        pivots = list(trailing.rref()[1])
        center = trailing.extract(pivots, pivots)
        cross = mixed[:m, m:].extract(list(range(m)), pivots)
        vacuum = ((mixed[:m, :m]-cross*center.inv()*cross.H)/(1-low)).applyfunc(sp.expand)
    else:
        vacuum = _checked([vacuum])[0]
        if vacuum.shape != (m, m):
            raise ValueError("vacuum Gram size mismatch")
    _require(vacuum, "vacuum Gram")
    model = _interval_model([block-vacuum for block in blocks], low, high)
    model.vacuum = vacuum
    return model


def even_completion(entries, high, *, low=0):
    """Fit 2r+1 readings, r >= 1, including an unknown vacuum. This also
    constructs the maximum allowable vacuum for a feasible dataset.
    """
    blocks = _checked(entries)
    low, high = _interval(low, high)
    r = (len(blocks)-1)//2
    if not r or len(blocks) != 2*r+1:
        raise ValueError("need readings 0 through a positive even index")
    _require(_hankel(blocks, r+1), "raw equal-time Gram")
    differences = [a-b for a, b in zip(blocks, blocks[1:])]
    model = _interval_model(differences, low, high)
    transfer = model.transfer
    model.metric = (model.metric*(sp.eye(transfer.rows)-transfer).inv()).applyfunc(sp.expand)
    model.vacuum = (blocks[0]-model.probes.H*model.metric*model.probes).applyfunc(sp.expand)
    _require(model.vacuum, "residual vacuum Gram")
    return model


def lobatto_completion(entries, high):
    """Independent odd-order construction with explicit endpoint weights.
    Requires only a rational trial high strictly between zero and one.
    """
    blocks = _checked(entries)
    _, high = _interval(0, high)
    _interval_model(blocks, 0, 1)  # admissibility on the full compact interval
    size = blocks[0].rows
    if len(blocks) == 2:
        return Realization(sp.zeros(0), sp.zeros(0), sp.zeros(0, size),
                           blocks[1], blocks[0]-blocks[1])
    weighted = [blocks[i+1]-blocks[i+2] for i in range(len(blocks)-2)]
    model = _interval_model(weighted, 0, high)
    t, j, g = model.transfer, model.probes, model.metric
    one_minus_t = sp.eye(t.rows)-t
    mass = (g*(t*one_minus_t).inv()).applyfunc(sp.expand)
    model.vacuum = (blocks[1]-j.H*g*one_minus_t.inv()*j).applyfunc(sp.expand)
    model.zero_atom = (blocks[0]-blocks[1]-j.H*g*t.inv()*j).applyfunc(sp.expand)
    _require(model.vacuum, "upper endpoint Gram")
    _require(model.zero_atom, "lower endpoint Gram")
    model.metric = mass
    return model
