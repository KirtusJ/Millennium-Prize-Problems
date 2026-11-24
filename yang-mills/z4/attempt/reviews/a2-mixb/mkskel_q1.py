"""Q1 skeletons (a2-mixb). Same convention as mkskel.py (prior worker): W_delta = (-cos d, 0, 0, sin d) on the
y-link at site 2 = (2,0,0), B = i = (0,1,0,0) on the z-link at site 2, every other frozen link = I.
Displacements: for beta in {6, 12}: d = k/beta, k in {1,2,4} (tags b6-k1 ...), plus fixed round distances
equal to the side-6 matched-point values k/3.276133577 (0.30524, 0.61048, 1.22095; tags fix-k1 ...), plus d0.
Fixed-distance skeletons do not depend on beta (one file each).
Predicate S1: arccos(-W[0]) equals d to 1e-12. Files opened with 'x'.
"""
import math, os
N = 6
os.makedirs("skeletons_q1", exist_ok=False)
def frozen(x, i):
    c = (x % N, (x // N) % N, x // (N * N))
    return all(k == i or c[k] % 2 == 0 for k in range(3))
tags = [("d0", 0.0)]
for b in (6, 12):
    for k in (1, 2, 4): tags.append((f"b{b}-k{k}", k / b))
for k in (1, 2, 4): tags.append((f"fix-k{k}", k / 3.276133577))
for name, d in tags:
    W = (-math.cos(d), 0.0, 0.0, math.sin(d))
    assert (abs(math.acos(-W[0]) - d) < 1e-12) if d > 0 else W[0] == -1.0
    with open(f"skeletons_q1/{name}.txt", "x") as fh:
        fh.write(f"# W=({W[0]!r},0,0,{W[3]!r}) delta={d!r} B=i side {N}\n")
        for x in range(N ** 3):
            for i in range(3):
                if frozen(x, i):
                    q = W if (x, i) == (2, 1) else ((0.0, 1.0, 0.0, 0.0) if (x, i) == (2, 2) else (1.0, 0.0, 0.0, 0.0))
                    fh.write(f"{x} {i} " + " ".join(f"{v:.17e}" for v in q) + "\n")
    print(name, d)
