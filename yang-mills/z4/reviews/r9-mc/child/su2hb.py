"""Simple, slow reference SU(2) lattice gauge theory in 4D (pure Python loops).

Lattice: periodic L^4, L=4. Links U_mu(x) in SU(2) stored as unit quaternions
(a0,a1,a2,a3) <-> a0*1 + i*(a1 s1 + a2 s2 + a3 s3); (1/2)Tr U = a0.
Action weight exp(beta * sum_p (1/2) Tr U_p). Creutz heat bath, one link at a
time, sequential lexicographic site order, mu = 0..3 at each site.
Measurement: P = average over all sites and all 6 planes of (1/2) Tr U_p,
recorded once per sweep after thermalization.

Usage: python su2hb.py BETA START(cold|hot) NTHERM NMEAS SEED OUTFILE
OUTFILE must not exist (never overwritten). Writes one per-sweep plaquette per line,
with a '#' header.

PREDICATES (fixed before the first run):
  P1  every measured per-sweep plaquette is finite and lies in [0,1]
      (for beta>0 averages; individual (1/2)Tr is in [-1,1], the sweep average
      is expected in [0,1]).
  P2  link unitarity preserved: max | |U|^2 - 1 | < 1e-10 at the end of the run.
  P3  (analysis script) cold and hot starts at the same beta agree:
      |P_cold - P_hot| < 3 * sqrt(err_cold^2 + err_hot^2), errors by binning
      with bin size 20 sweeps.
  P4  (analysis script) P(beta=8.0) > P(beta=2.3).
Exit code 0 iff P1 and P2 hold; 2 on predicate failure.
"""
import math
import random
import sys
import os

L = 4
D = 4
V = L ** D


def qmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    # (a0 + i a.s)(b0 + i b.s) = a0b0 - a.b + i(a0 b + b0 a - a x b)
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
            a0 * b1 + b0 * a1 - (a2 * b3 - a3 * b2),
            a0 * b2 + b0 * a2 - (a3 * b1 - a1 * b3),
            a0 * b3 + b0 * a3 - (a1 * b2 - a2 * b1))


def qdag(a):
    return (a[0], -a[1], -a[2], -a[3])


def site_index(c):
    return ((c[0] * L + c[1]) * L + c[2]) * L + c[3]


COORDS = [(i // 64, (i // 16) % 4, (i // 4) % 4, i % 4) for i in range(V)]
UP = [[0] * D for _ in range(V)]
DN = [[0] * D for _ in range(V)]
for s in range(V):
    c = COORDS[s]
    for mu in range(D):
        cu = list(c); cu[mu] = (cu[mu] + 1) % L
        cd = list(c); cd[mu] = (cd[mu] - 1) % L
        UP[s][mu] = site_index(cu)
        DN[s][mu] = site_index(cd)


def random_su2(rng):
    while True:
        x = [rng.uniform(-1, 1) for _ in range(4)]
        n = sum(t * t for t in x)
        if 1e-6 < n <= 1.0:
            n = math.sqrt(n)
            return tuple(t / n for t in x)


def staple(U, s, mu):
    A = [0.0, 0.0, 0.0, 0.0]
    smu = UP[s][mu]
    for nu in range(D):
        if nu == mu:
            continue
        snu = UP[s][nu]
        # forward: U_nu(x+mu) U_mu(x+nu)^dag U_nu(x)^dag
        t = qmul(qmul(U[smu][nu], qdag(U[snu][mu])), qdag(U[s][nu]))
        # backward: U_nu(x+mu-nu)^dag U_mu(x-nu)^dag U_nu(x-nu)
        sdn = DN[s][nu]
        smudn = DN[smu][nu]
        b = qmul(qmul(qdag(U[smudn][nu]), qdag(U[sdn][mu])), U[sdn][nu])
        for k in range(4):
            A[k] += t[k] + b[k]
    return A


def heatbath_link(U, s, mu, beta, rng):
    A = staple(U, s, mu)
    k = math.sqrt(sum(t * t for t in A))
    if k < 1e-12:
        U[s][mu] = random_su2(rng)
        return
    Vq = (A[0] / k, A[1] / k, A[2] / k, A[3] / k)
    bk = beta * k
    emin = math.exp(-2.0 * bk)
    # Creutz: x0 with density ~ sqrt(1-x0^2) exp(bk x0)
    while True:
        z = emin + (1.0 - emin) * rng.random()
        x0 = 1.0 + math.log(z) / bk
        if rng.random() <= math.sqrt(max(0.0, 1.0 - x0 * x0)):
            break
    r = math.sqrt(max(0.0, 1.0 - x0 * x0))
    cth = rng.uniform(-1.0, 1.0)
    sth = math.sqrt(1.0 - cth * cth)
    ph = rng.uniform(0.0, 2.0 * math.pi)
    X = (x0, r * sth * math.cos(ph), r * sth * math.sin(ph), r * cth)
    # Tr(U A) = k Tr(X V^dag V) for U = X V^dag
    U[s][mu] = qmul(X, qdag(Vq))


def sweep(U, beta, rng):
    for s in range(V):
        for mu in range(D):
            heatbath_link(U, s, mu, beta, rng)


def plaquette(U):
    tot = 0.0
    for s in range(V):
        for mu in range(D):
            smu = UP[s][mu]
            for nu in range(mu + 1, D):
                snu = UP[s][nu]
                p = qmul(qmul(U[s][mu], U[smu][nu]),
                         qmul(qdag(U[snu][mu]), qdag(U[s][nu])))
                tot += p[0]
    return tot / (V * 6)


def main():
    beta = float(sys.argv[1]); start = sys.argv[2]
    ntherm = int(sys.argv[3]); nmeas = int(sys.argv[4]); seed = int(sys.argv[5])
    out = sys.argv[6]
    if os.path.exists(out):
        print("refusing to overwrite", out); sys.exit(3)
    rng = random.Random(seed)
    if start == "cold":
        U = [[(1.0, 0.0, 0.0, 0.0) for _ in range(D)] for _ in range(V)]
    else:
        U = [[random_su2(rng) for _ in range(D)] for _ in range(V)]
    print("initial P =", plaquette(U))
    for _ in range(ntherm):
        sweep(U, beta, rng)
    vals = []
    for _ in range(nmeas):
        sweep(U, beta, rng)
        vals.append(plaquette(U))
    with open(out, "x") as f:
        f.write(f"# beta={beta} start={start} L={L} ntherm={ntherm} nmeas={nmeas} seed={seed}\n")
        for v in vals:
            f.write(f"{v:.12f}\n")
    ok1 = all(math.isfinite(v) and 0.0 <= v <= 1.0 for v in vals)
    dev = max(abs(sum(t * t for t in U[s][mu]) - 1.0) for s in range(V) for mu in range(D))
    ok2 = dev < 1e-10
    mean = sum(vals) / len(vals) if vals else float("nan")
    print(f"beta={beta} start={start} nmeas={nmeas} mean P={mean:.6f}")
    print(f"P1 finite&[0,1]: {ok1}  P2 unitarity dev={dev:.2e}: {ok2}")
    sys.exit(0 if (ok1 and ok2) else 2)


if __name__ == "__main__":
    main()
