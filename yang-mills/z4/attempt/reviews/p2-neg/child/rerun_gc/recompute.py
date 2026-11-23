"""Fixed predicates (before running):
P1: q = R(1 step)/R(0) per N; writer's q matches if round(q,3) equals the printed value.
P2: xi = 1/(3.74*a*sqrt(sigma)); matches if round(xi,2) equals the printed value.
P3: xi*(1-q) (unrounded q, xi); matches if round(.,2) equals the printed value.
Inputs only from MATCHED_MEASUREMENT.md extension table (R(0), R 1 step) and a*sqrt(sigma).
"""
data = {6: (0.3690, 3.751e-2, 1.012e-2, (0.270, 0.72, 0.53)),
        8: (0.2660, 3.615e-2, 1.166e-2, (0.323, 1.01, 0.68)),
        12: (0.1905, 3.233e-2, 1.245e-2, (0.385, 1.40, 0.86))}
lines = []
for N, (a, r0, r1, (wq, wx, wxq)) in data.items():
    q = r1 / r0; xi = 1 / (3.74 * a); v = xi * (1 - q)
    for name, val, w, d in (("q", q, wq, 3), ("xi", xi, wx, 2), ("xi(1-q)", v, wxq, 2)):
        lines.append(f"N={N} {name} unrounded={val:.6f} rounded={round(val,d):.{d}f} writer={w:.{d}f} match={round(val,d)==w}")
with open("results.txt", "x") as f:
    f.write("\n".join(lines) + "\n")
print("\n".join(lines))
