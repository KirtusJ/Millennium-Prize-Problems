"""v2 (after K1): Q3/Q6 use log1p (K1 underflow, my defect); Q1d remainder redefined as N^2(M-1/2)-1/4 (K1 failure was my reading). Predicates otherwise unchanged.
Challenger program for Z4 README (2D controls, Z_n adverse control, T2 sequences).

Usage: python challenge.py <outfile>   (refuses to overwrite an existing file)
No randomness except Q2's test vector: random.seed(20261122).

PREDICATES (fixed before first run). Tolerance sources given in [brackets].

Q1 (U(1), T3). Character ratio r1(beta) = <cos th>_w with w = exp(beta cos th),
    computed by trapezoidal Haar quadrature on K points (mpmath, dps=50), NOT Bessel.
    Q1a: quadrature converged: |r1(K) - r1(2K)| < 1e-35 for every N in {4,8,16,32,64}
         [trapezoid is exponentially convergent for periodic analytic integrands;
          1e-35 is far below the 1e-12 digits quoted in README].
    Q1b: M(N) = -N^2 ln r1(N^2) agrees with README M(64)=0.500061048820 to 1e-12
         [README quotes 12 digits].
    Q1c: N^2 (M(N) - 1/2) -> 1/4: |64^2 (M(64)-1/2) - 1/4| < 1e-3
         [next correction is O(1/N^2) ~ 2.4e-4 times O(1)].
    Q1d: the remainder ratios per doubling (N=4..64) equal README's 4.29, 4.07, 4.02, 4.00
         to 0.005 [README rounds to 2 decimals].
    Q1e: M(N) strictly decreasing in N on {4,...,64} (used by README "bounded by M(4)").
Q2 (structure, T3). On an actual N-link lattice with gauge group Z_K (K=5, N=3), the
    temporal-gauge transfer matrix T(U',U) = K^-N sum_V prod_x w(U_x+V_{x+1}-U'_x-V_x)
    maps psi_r = exp(2 pi i r sum_x U_x / K) to lambda_r psi_r with
    lambda_r/lambda_0 = (w_r/w_0)^N, w_r = sum_j w(j) cos(2 pi r j/K). Residual < 1e-12
    [double precision, ~10^3 summed terms of size O(1)]; beta = 1.3.
    Also: T applied to a seeded random vector, minus its projection on the psi_r, is < 1e-12
    (gauge-variant states are annihilated, so the psi_r carry the whole spectrum).
Q3 (Z_n table, T4). Recompute M(N) = -N^2 ln r_1 for Z_2,Z_3,Z_5 at beta=N^2, using
    1 - r_1 = sum w_j (1-cos)/sum w_j (no cancellation). Each of the 12 table entries agrees
    with README to relative 5e-3 [README prints 3 significant digits]. Asymptote
    N^2 k delta exp(-N^2 delta) agrees to RELATIVE 1e-6 at N=16 [README's 1e-6].
Q4 (T4 objection, expected by me to be MET, i.e. README defect). For each Z_n (n=2,3,5)
    a trajectory beta_N exists with M(N) = 1/2 exactly for N = 4..64 (bisection), and along it
    the charge-k levels M_k(N) converge to (1-cos(2 pi k/n))/(1-cos(2 pi/n)) * 1/2:
    |ratio(N=64) - limit| < 1e-2 [leading correction exp(-beta(delta_2-delta_1)) ~ N^-2c].
    beta_N grows like ln N, not N^2.
Q5 (T5). Numerically x(-ln tanh x) <= 1/(1+x) on a grid of 400 x in (0, 50]   [exact check
    with mpmath dps 50]. Measured only: max of ratio.
Q6 (T2, counterexample sequence, MEASURED ONLY): product family U(1) x Z_2 on beta=N^2:
    full lattice gap m_n = min(gap_U1, gap_Z2) violates c a_n <= m_n for every c>0, while
    the spectrum above the (asymptotically two-fold) vacuum converges to 1/2.
"""
import sys, os, math, cmath, random
import mpmath as mp

out = sys.argv[1]
if os.path.exists(out):
    print("refusing to overwrite", out); sys.exit(3)
lines = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s); lines.append(s)
res = {}

mp.mp.dps = 50
def r1_u1(beta, K):
    # trapezoid on [0,2pi), weights shifted by exp(-beta)
    beta = mp.mpf(beta); num = mp.mpf(0); den = mp.mpf(0)
    for j in range(K):
        c = mp.cos(2*mp.pi*j/K); w = mp.exp(beta*(c-1))
        num += w*(1-c); den += w
    return num/den  # = 1 - r1

Ns = [4, 8, 16, 32, 64]
M = {}
conv_ok = True
for N in Ns:
    K = int(40*N) + 64
    a = r1_u1(N*N, K); b = r1_u1(N*N, 2*K)
    if abs(a-b) >= mp.mpf('1e-35'): conv_ok = False
    M[N] = -N*N*mp.log(1-b)
    P(f"U1 N={N} K={K} |dq|={mp.nstr(abs(a-b),3)} M={mp.nstr(M[N],20)} N^2(M-1/2)={mp.nstr(N*N*(M[N]-mp.mpf(1)/2),12)}")
res['Q1a'] = conv_ok
res['Q1b'] = abs(M[64] - mp.mpf('0.500061048820')) < 1e-12
res['Q1c'] = abs(64**2*(M[64]-0.5) - 0.25) < 1e-3
rats = [(Ns[i]**2*(M[Ns[i]]-0.5)-0.25)/(Ns[i+1]**2*(M[Ns[i+1]]-0.5)-0.25) for i in range(4)]
P("U1 remainder ratios", [mp.nstr(x, 6) for x in rats])
res['Q1d'] = all(abs(x - y) < 0.005 for x, y in zip(rats, [4.29, 4.07, 4.02, 4.00]))
Mall = [-N*N*mp.log(1-r1_u1(N*N, 40*N+64)) for N in range(4, 65)]
res['Q1e'] = all(Mall[i] > Mall[i+1] for i in range(len(Mall)-1))

# Q2 small lattice Z_K
K, N, beta = 5, 3, 1.3
w = [math.exp(beta*math.cos(2*math.pi*j/K)) for j in range(K)]
confs = [(i, j, k) for i in range(K) for j in range(K) for k in range(K)]
idx = {c: n for n, c in enumerate(confs)}
T = [[0.0]*len(confs) for _ in confs]
for p, Up in enumerate(confs):
    for q, U in enumerate(confs):
        s = 0.0
        for V in confs:
            pr = 1.0
            for x in range(N):
                pr *= w[(U[x] + V[(x+1) % N] - Up[x] - V[x]) % K]
            s += pr
        T[p][q] = s / K**N
def apply(T, v): return [sum(T[p][q]*v[q] for q in range(len(v))) for p in range(len(v))]
psi = {r: [cmath.exp(2j*math.pi*r*sum(c)/K) for c in confs] for r in range(K)}
lam = {}; maxres = 0.0
for r in range(K):
    Tv = apply(T, psi[r]); l = Tv[0]/psi[r][0]; lam[r] = l
    maxres = max(maxres, max(abs(Tv[i]-l*psi[r][i]) for i in range(len(confs))))
wr = [sum(w[j]*math.cos(2*math.pi*r*j/K) for j in range(K)) for r in range(K)]
dev = max(abs(lam[r]/lam[0] - (wr[r]/wr[0])**N) for r in range(K))
random.seed(20261122)
v = [random.random() for _ in confs]
Tv = apply(T, v); D = len(confs)
proj = [0j]*D
for r in range(K):
    co = sum(psi[r][i].conjugate()*Tv[i] for i in range(D))/D
    for i in range(D): proj[i] += co*psi[r][i]
orth = max(abs(Tv[i]-proj[i]) for i in range(D))
P(f"Q2 Z{K} N={N} beta={beta}: eigvec residual {maxres:.2e}, ratio dev {dev:.2e}, gauge-variant remainder {orth:.2e}")
P("Q2 lambda_r/lambda_0", [round((lam[r]/lam[0]).real, 12) for r in range(K)])
res['Q2'] = maxres < 1e-12 and dev < 1e-12 and orth < 1e-12

# Q3 Z_n table
def one_minus_r(n, beta, k=1):
    beta = mp.mpf(beta); num = mp.mpf(0); den = mp.mpf(0)
    for j in range(n):
        c = mp.cos(2*mp.pi*j/n); ww = mp.exp(beta*(c-1))
        num += ww*(1-mp.cos(2*mp.pi*j*k/n)); den += ww
    return num/den
def Mz(n, beta, Nn, k=1): return -Nn*Nn*mp.log1p(-one_minus_r(n, beta, k))
table = {2: [2.68e-3, 4.05e-13, 3.29e-54, 2.24e-220], 3: [2.97e-2, 1.81e-9, 3.90e-40, 1.31e-164],
         5: [3.32e-1, 3.49e-4, 5.51e-18, 5.32e-75]}
ok3 = True
for n in (2, 3, 5):
    vals = [Mz(n, N*N, N) for N in (2, 4, 8, 16)]
    d = 1-mp.cos(2*mp.pi/n); k = 1 if n == 2 else 2
    asy = 16**2*k*d*mp.exp(-256*d)
    relasy = abs(vals[3]/asy - 1)
    rel = [abs(vals[i]/table[n][i]-1) for i in range(4)]
    if max(rel) > 5e-3 or relasy > 1e-6: ok3 = False
    if not all(vals[i] > vals[i+1] for i in range(3)): ok3 = False
    P(f"Z{n}: M=", [mp.nstr(x, 4) for x in vals], "max rel dev vs table", mp.nstr(max(rel), 3),
      "rel dev asymptote N=16", mp.nstr(relasy, 3), "abs dev", mp.nstr(abs(vals[3]-asy), 3))
res['Q3'] = ok3

# Q4 tuned trajectory
ok4 = True
for n in (2, 3, 5):
    row = []
    for N in Ns:
        lo, hi = mp.mpf('1e-6'), mp.mpf(200)
        for _ in range(200):
            mid = (lo+hi)/2
            if Mz(n, mid, N) > 0.5: lo = mid
            else: hi = mid
        b = (lo+hi)/2
        lev = [Mz(n, b, N, k) for k in range(1, n//2+1)]
        row.append((N, b, lev))
    for N, b, lev in row:
        P(f"Z{n} tuned N={N}: beta={mp.nstr(b,8)} (N^2={N*N}) levels M_k={[mp.nstr(x,8) for x in lev]}")
    N, b, lev = row[-1]
    d1 = 1-math.cos(2*math.pi/n)
    for k, x in enumerate(lev, start=1):
        lim = 0.5*(1-math.cos(2*math.pi*k/n))/d1
        if abs(x - lim) > 1e-2: ok4 = False
res['Q4'] = ok4

# Q5
mp.mp.dps = 50
worst = mp.mpf(0); ok5 = True
for i in range(1, 401):
    x = mp.mpf(i)/8
    lhs = x*(-mp.log(mp.tanh(x))); rhs = 1/(1+x)
    if lhs > rhs: ok5 = False
    worst = max(worst, lhs/rhs)
res['Q5'] = ok5
P("Q5 max x(-ln tanh x)/(1/(1+x)) on grid:", mp.nstr(worst, 6))

# Q6 measured only
for N in Ns:
    g1 = -N*mp.log(1-r1_u1(N*N, 40*N+64)); g2 = -N*mp.log1p(-one_minus_r(2, N*N)); a = mp.mpf(1)/N
    P(f"Q6 N={N}: m_U1/a={mp.nstr(g1/a,8)} m_Z2/a={mp.nstr(g2/a,4)} full gap m/a={mp.nstr(min(g1,g2)/a,4)}")

P("PREDICATES", res)
met = sum(1 for v in res.values() if v); P(f"met {met}, failed {len(res)-met}, measured only 1")
with open(out, "x") as f: f.write("\n".join(lines) + "\n")
sys.exit(0)
