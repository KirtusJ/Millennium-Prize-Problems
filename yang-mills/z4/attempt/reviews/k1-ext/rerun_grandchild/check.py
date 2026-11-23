import numpy as np

# Analytic Gaussian ansatz: alpha = 1/sqrt2, lambda = 1/sqrt(8A), A = 3/8 + alpha/2
alpha = 1 / np.sqrt(2)
A = 3 / 8 + alpha / 2
lam = 1 / np.sqrt(8 * A)
claimed = np.sqrt(2) - 1
# residual check of the u^2 coefficient: -3/8 + 1/(64A) should equal -alpha/2
resid = (-3 / 8 + 1 / (64 * A)) + alpha / 2


def grid(L, h):
    u = np.arange(-L, L + h / 2, h)
    U, V = np.meshgrid(u, u, indexing="ij")
    K = np.exp(-(U - V) ** 2 / 8 - (U**2 + V**2) / 4) / np.sqrt(8 * np.pi)
    return np.linalg.eigvalsh(K * h)[-1]  # symmetric kernel, uniform weights h


rows = []
for L, h in [(10, 0.2), (12, 0.1), (12, 0.05), (14, 0.05)]:
    rows.append((L, h, grid(L, h)))

lines = [f"alpha={alpha:.10f} A={A:.10f} resid={resid:.2e}",
         f"lambda_analytic={lam:.12f} claimed={claimed:.12f} diff={lam-claimed:.2e}"]
for L, h, g in rows:
    lines.append(f"L={L} h={h} grid={g:.12f} grid-analytic={g-lam:.2e}")
out = "\n".join(lines) + "\n"
print(out)
with open("check_output.txt", "x") as f:
    f.write(out)
