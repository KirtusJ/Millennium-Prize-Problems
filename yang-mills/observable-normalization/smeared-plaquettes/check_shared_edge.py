"""Check SU(2) shared-edge formulas against matrix differences on two adjacent plaquettes."""
import numpy as np

PAULI = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])
I = np.eye(2)
STEP = 0.0001


def haar(rng):
    coordinates = rng.normal(size=4)
    coordinates /= np.linalg.norm(coordinates)
    return coordinates[0] * I + 1j * np.einsum("a,aij->ij", coordinates[1:], PAULI)


def gradients(edge, left, right):
    # The physical plaquettes traverse their common link in opposite directions.
    result = []
    for axis in PAULI:
        changes = []
        for sign in (1, -1):
            varied = (np.cos(STEP / 2) * I + sign * 1j * np.sin(STEP / 2) * axis) @ edge
            changes.append(np.array([np.trace(varied @ left).real,
                                     np.trace(varied.conj().T @ right).real]))
        result.append((changes[0] - changes[1]) / (2 * STEP))
    return np.array(result).T


def main():
    rng = np.random.default_rng(20261122)
    max_error = 0.
    wrong_sign_error = 0.
    for _ in range(64):
        edge = haar(rng)
        left = haar(rng) @ haar(rng) @ haar(rng)
        right = haar(rng) @ haar(rng) @ haar(rng)
        p = edge @ left
        q = edge @ right.conj().T
        # Reversing the second loop preserves its real trace.
        f, g = np.trace(p).real, np.trace(q).real
        grad_p, grad_q = gradients(edge, left, right)
        cross = np.trace(p @ q.conj().T).real / 2 - f * g / 4
        mismatch = 2 - np.trace(p @ q).real - ((f - g) / 2) ** 2
        max_error = max(max_error, abs(grad_p @ grad_q - cross),
                        abs(np.sum((grad_p + grad_q) ** 2) - mismatch))
        wrong = np.trace(p @ q).real / 2 - f * g / 4
        wrong_sign_error = max(wrong_sign_error, abs(grad_p @ grad_q - wrong))
    print(f"maximum orientation-aware error {max_error:.4g}")
    print(f"maximum error after swapping the two trace words {wrong_sign_error:.4g}")
    if max_error > 1e-8 or wrong_sign_error < 0.1:
        raise ValueError("expected orientation controls failed")


if __name__ == "__main__":
    main()
