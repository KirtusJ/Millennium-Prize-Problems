"""Write skeleton files for the perturbed -I backgrounds (side 6).
W_delta = -cos(delta) + e_z sin(delta) = quaternion (-cos d, 0, 0, sin d) on the y-link at (2,0,0);
B = e_x = i = (0,1,0,0) on the z-link at (2,0,0); every other frozen link = I.
Convention from g4/sparse-coarse-fields/disk.md (B = e_x, W_delta = -cos delta + e_z sin delta).
Predicate: round distance of W_delta from -I equals delta to 1e-12 (arccos(-Re W)); files opened with 'x'.
"""
import math, os
N, BETA = 6, 3.276133577
os.makedirs("skeletons", exist_ok=False)
def frozen(x, i):
    c = (x % N, (x // N) % N, x // (N * N))
    return all(k == i or c[k] % 2 == 0 for k in range(3))
for name, d in (("d0", 0.0), ("d0.5", 0.5 / BETA), ("d1", 1.0 / BETA), ("d2", 2.0 / BETA)):
    W = (-math.cos(d), 0.0, 0.0, math.sin(d))
    assert abs(math.acos(-W[0]) - d) < 1e-12 if d > 0 else W[0] == -1.0
    with open(f"skeletons/{name}.txt", "x") as fh:
        fh.write(f"# W=({W[0]!r},0,0,{W[1]!r}...) delta={d!r} B=i side {N}\n")
        for x in range(N ** 3):
            for i in range(3):
                if frozen(x, i):
                    q = (1.0, 0.0, 0.0, 0.0)
                    if (x, i) == (2, 1): q = W
                    if (x, i) == (2, 2): q = (0.0, 1.0, 0.0, 0.0)
                    fh.write(f"{x} {i} " + " ".join(f"{v:.17e}" for v in q) + "\n")
    print(name, d, W)
