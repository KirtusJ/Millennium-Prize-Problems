"""Extra skeleton (outside the brief): delta = 4/beta, same convention as mkskel.py. Opened with 'x'."""
import math
N, BETA = 6, 3.276133577
d = 4.0 / BETA; W = (-math.cos(d), 0.0, 0.0, math.sin(d))
assert abs(math.acos(-W[0]) - d) < 1e-12
def frozen(x, i):
    c = (x % N, (x // N) % N, x // (N * N)); return all(k == i or c[k] % 2 == 0 for k in range(3))
with open("skeletons/d4.txt", "x") as fh:
    fh.write(f"# W=({W[0]!r},0,0,{W[3]!r}) delta={d!r} B=i side {N}\n")
    for x in range(N ** 3):
        for i in range(3):
            if frozen(x, i):
                q = W if (x, i) == (2, 1) else ((0.0, 1.0, 0.0, 0.0) if (x, i) == (2, 2) else (1.0, 0.0, 0.0, 0.0))
                fh.write(f"{x} {i} " + " ".join(f"{v:.17e}" for v in q) + "\n")
print(d, W)
