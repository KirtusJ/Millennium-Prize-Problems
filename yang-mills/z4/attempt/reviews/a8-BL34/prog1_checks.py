"""prog1_checks.py  (a8-BL34)  -- algebraic/combinatorial checks used in L3_L4.md.

Predicates (fixed before first run):
 Q1 lambda_min(N) > 0 for the Dirichlet Maxwell form Q(phi;0) on unpinned interior links
    (one colour) of R=[-N,N]^4, N=1,2 (Lemma H, convention of PROOF_B_v2 s.3: interior
    links = links with an interior endpoint, pinned = +e0 links from interior sites).
    Measured only: lambda_min values and C_pp for p0=(1,2) plaquette at the origin.
 Q2 shell 'simple connectivity' over R: on the 2-complex of the shell of [-N,N]^4
    (sites with |x|_inf=N, links and plaquettes with all sites there), N=1,2,3:
    dim ker d1 == rank d0  (H^1 = 0), and the shell graph is connected (rank d0 = V-1).
 Q3 for all 20000 random 4-tuples of su(2) vectors x_i (|x_i| <= a, a in {0.05,0.3,1.0}):
    || e^{iA1}e^{iA2}e^{-iA3}e^{-iA4} - 1 - i(A1+A2-A3-A4) ||_op <= (s^2/2) e^s,
    s = sum|x_i|, A = sigma.x  (tolerance 1e-12: float64 rounding of 2x2 products).
 Q4 same samples, when alpha_p < pi: |log U_p - dx_p| <= s^2 e^s  (tolerance 1e-10).
 Q5 for all 10^6 grid points x in [-pi,pi]: 1-cos x >= (2/pi^2) x^2 - 1e-15.
(No scipy on this machine: closed-form SU(2) exp/log; run v1 failed on import, own defect.)
Seed 20261123. Output file opened with mode 'x'.
"""
import sys, itertools, numpy as np

sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
def A(x): return sum(c * s for c, s in zip(x, sig))
def expi(x):
    r = np.linalg.norm(x)
    if r == 0: return np.eye(2, dtype=complex)
    return np.cos(r) * np.eye(2) + 1j * np.sin(r) * A(x / r)
def su2log(U):
    # U = a0 + i sigma.b ; returns y with U = exp(i sigma.y)
    a0 = np.real(np.trace(U)) / 2
    b = np.array([np.real(np.trace(U @ si) / (2j)) for si in sig])
    al = np.arccos(np.clip(a0, -1, 1)); nb = np.linalg.norm(b)
    return np.zeros(3) if nb == 0 else al * b / nb

rng = np.random.default_rng(20261123)
out = open(sys.argv[1], "x")
def log(*a):
    s = " ".join(str(v) for v in a); print(s); out.write(s + "\n"); out.flush()
fails = []

def box(N):
    rng4 = range(-N, N + 1)
    sites = list(itertools.product(rng4, repeat=4))
    inter = [x for x in sites if max(map(abs, x)) < N]
    shell = [x for x in sites if max(map(abs, x)) == N]
    return sites, set(inter), set(shell)

def e(m):
    v = [0, 0, 0, 0]; v[m] = 1; return tuple(v)
def add(x, y, s=1): return tuple(a + s * b for a, b in zip(x, y))

def maxwell(N):
    sites, inter, shell = box(N); S = set(sites)
    links = [(x, m) for x in sites for m in range(4) if add(x, e(m)) in S]
    lint = [(x, m) for (x, m) in links if x in inter or add(x, e(m)) in inter]
    pinned = {(x, 0) for x in inter}
    free = [l for l in lint if l not in pinned]
    idx = {l: i for i, l in enumerate(free)}
    plaqs = []
    for x in sites:
        for m in range(4):
            for n in range(m + 1, 4):
                ls = [(x, m), (add(x, e(m)), n), (add(x, e(n)), m), (x, n)]
                if all(add(y, e(k)) in S for (y, k) in ls) and any(l in set(lint) for l in ls):
                    plaqs.append((x, m, n, ls))
    D = np.zeros((len(plaqs), len(free)))
    for r, (x, m, n, ls) in enumerate(plaqs):
        for l, sg in zip(ls, [1, 1, -1, -1]):
            if l in idx: D[r, idx[l]] += sg
    Qm = D.T @ D
    lam = np.linalg.eigvalsh(Qm)[0]
    r0 = [i for i, (x, m, n, _) in enumerate(plaqs) if x == (0, 0, 0, 0) and (m, n) == (1, 2)][0]
    C = D @ np.linalg.solve(Qm, D.T)
    return lam, C[r0, r0], len(free), len(plaqs)

for N in (1, 2):
    lam, cpp, nf, npq = maxwell(N)
    log(f"Q1 N={N} free links={nf} plaquettes={npq} lambda_min={lam:.6f} C_pp(p0)={cpp:.6f} (3/2)C_pp={1.5*cpp:.6f}")
    if not lam > 1e-9: fails.append(f"Q1 N={N}")

def shell_cohom(N):
    sites, inter, shell = box(N)
    V = sorted(shell); vi = {x: i for i, x in enumerate(V)}
    E = [(x, m) for x in V for m in range(4) if add(x, e(m)) in shell]
    ei = {l: i for i, l in enumerate(E)}
    P = []
    for x in V:
        for m in range(4):
            for n in range(m + 1, 4):
                ls = [(x, m), (add(x, e(m)), n), (add(x, e(n)), m), (x, n)]
                if all(l in ei for l in ls): P.append(ls)
    d0 = np.zeros((len(E), len(V))); d1 = np.zeros((len(P), len(E)))
    for (x, m), i in ei.items():
        d0[i, vi[add(x, e(m))]] += 1; d0[i, vi[x]] -= 1
    for r, ls in enumerate(P):
        for l, sg in zip(ls, [1, 1, -1, -1]): d1[r, ei[l]] += sg
    r0 = np.linalg.matrix_rank(d0); r1 = np.linalg.matrix_rank(d1)
    assert np.abs(d1 @ d0).max() == 0
    return len(V), len(E), len(P), r0, len(E) - r1

for N in (1, 2, 3):
    nV, nE, nP, r0, k1 = shell_cohom(N)
    ok = (k1 == r0) and (r0 == nV - 1)
    log(f"Q2 N={N} shell V={nV} E={nE} P={nP} rank d0={r0} dim ker d1={k1} H1=0:{k1==r0} connected:{r0==nV-1}")
    if not ok: fails.append(f"Q2 N={N}")

sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
def A(x): return sum(c * s for c, s in zip(x, sig))
for a in (0.05, 0.3, 1.0):
    worst3 = -np.inf; worst4 = -np.inf; n3 = n4 = 0
    for _ in range(20000 // 3 + 1):
        xs = rng.normal(size=(4, 3)); xs *= (a * rng.random((4, 1)) ** (1 / 3)) / np.linalg.norm(xs, axis=1, keepdims=True)
        As = [A(x) for x in xs]
        U = expi(xs[0]) @ expi(xs[1]) @ expi(-xs[2]) @ expi(-xs[3])
        dx = xs[0] + xs[1] - xs[2] - xs[3]
        s = np.linalg.norm(xs, axis=1).sum()
        R = U - np.eye(2) - 1j * A(dx)
        lhs = np.linalg.norm(R, 2); rhs = s * s / 2 * np.exp(s)
        worst3 = max(worst3, lhs - rhs); n3 += 1
        if lhs > rhs + 1e-12: fails.append(f"Q3 a={a}")
        alpha = np.arccos(np.clip(np.real(np.trace(U)) / 2, -1, 1))
        if alpha < np.pi - 1e-6:
            y = su2log(U)
            lhs4 = np.linalg.norm(y - dx); rhs4 = s * s * np.exp(s)
            worst4 = max(worst4, lhs4 - rhs4); n4 += 1
            if lhs4 > rhs4 + 1e-10: fails.append(f"Q4 a={a}")
    log(f"Q3/Q4 a={a}: cases {n3}/{n4} qualify; max(lhs-rhs) Q3={worst3:.3e} Q4={worst4:.3e}")

x = np.linspace(-np.pi, np.pi, 10**6)
m5 = np.min(1 - np.cos(x) - 2 / np.pi**2 * x**2)
log(f"Q5 min(1-cos x - 2x^2/pi^2) on grid = {m5:.3e}")
if m5 < -1e-15: fails.append("Q5")
log("FAILED:", sorted(set(fails)) if fails else "none")
sys.exit(1 if fails else 0)
