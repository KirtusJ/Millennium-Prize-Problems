#!/usr/bin/env python3
"""dual_sign.py -- sign of the SU(2) plaquette-character (dual / spin-foam) amplitudes.

Route step under test (S2 of the chain in report.md):
  "For SU(2) Wilson theory, every dual amplitude
       A({j_p}) = int prod_links dU_l  prod_p chi_{j_p}(U_p)
   is >= 0, so that Z = sum_{j} prod_p c_{j_p}(beta) A({j}) is a positive
   random-surface model at every beta."
For U(1) and Z_2 this holds (the amplitude is an indicator, 0 or 1).

Method: exact. For each link, Haar average of (tensor product of D^j(U) and
conj D^j(U) over all its occurrences) = orthogonal projector onto the
SU(2)-invariant subspace (kernel of total Casimir). Plaquette traces are then
a tensor-network contraction (numpy.einsum). No sampling.

Lattices: periodic hypercubic L_1 x ... x L_d, plaquettes all (mu<nu) at every site,
holonomy U_x,mu U_{x+mu},nu U_{x+nu},mu^{-1} U_x,nu^{-1}.

PREDICATES (fixed before first run):
 C0 control: trace of the invariant projector on V_{1/2}^{x4} equals 2.  tol 1e-9
 C1 control: d=2, L=1: A(a) = 1/(2a+1) for a in {1/2,1,3/2}.           tol 1e-9
 C2 control: d=3, L=1: A(a,0,0) = 1/(2a+1) (one commutator, the others trivial). tol 1e-9
 K1 Wilson weight exp(beta/2 tr U): character coefficients c_j(beta) > 0 for
    j = 0..5 (half-integer steps), beta in {0.5,1,2,4,8,16}; and agree with
    (2j+1)*2*I_{2j+1}(beta)/beta to rel 1e-8 (quadrature with 4000 nodes, smooth periodic integrand).
 H  (hypothesis of the route, "for all"): A({j}) >= -1e-9 for every configuration
    enumerated (spins in {0,1/2,1} per plaquette, gauss-law-admissible or not).
    Reported per case: number of configurations, number with A < -1e-9, > 1e-9, |A|<=1e-9.
    My expectation: H FAILS (signed 6j-type recoupling) on d=3 L=1 or d=3 (2,1,1) or d=4 L=1.
 Tolerance 1e-9: float64 eigen-decomposition of matrices of size <= 729,
 errors ~1e-13 * size, then contraction of <= 24 indices; 1e-9 is a safe margin
 above that and far below the smallest nonzero |A| that can occur (>= 1e-4 here).
Seeds: none needed (deterministic).
Output: results file opened with mode "x" (argument 1).
"""
import sys, itertools, math
import numpy as np

def spin_mats(j):
    d = int(round(2*j+1)); m = [j - k for k in range(d)]
    Jz = np.diag(m).astype(complex)
    Jp = np.zeros((d, d), complex)
    for k in range(1, d):
        mm = m[k]
        Jp[k-1, k] = math.sqrt(j*(j+1) - mm*(mm+1))
    Jm = Jp.conj().T
    return (Jp+Jm)/2, (Jp-Jm)/(2j), Jz

_proj_cache = {}
def inv_projector(spec):
    """spec: tuple of (j, conj_flag). Returns projector on prod spaces as matrix."""
    if spec in _proj_cache: return _proj_cache[spec]
    dims = [int(round(2*j+1)) for j, _ in spec]
    N = int(np.prod(dims)) if dims else 1
    Jtot = [np.zeros((N, N), complex) for _ in range(3)]
    for k, (j, c) in enumerate(spec):
        gens = spin_mats(j)
        for a in range(3):
            g = -gens[a].T if c else gens[a]   # dual rep generator: -J^T
            op = np.array([[1.0]])
            for kk, dk in enumerate(dims):
                op = np.kron(op, g if kk == k else np.eye(dk))
            Jtot[a] += op
    Cas = sum(J @ J for J in Jtot)
    w, v = np.linalg.eigh(Cas)
    Q = v[:, np.abs(w) < 1e-8]
    P = Q @ Q.conj().T
    _proj_cache[spec] = P
    return P

def lattice(Ls):
    d = len(Ls); sites = list(itertools.product(*[range(L) for L in Ls]))
    def sh(x, mu): y = list(x); y[mu] = (y[mu]+1) % Ls[mu]; return tuple(y)
    links = {(x, mu): i for i, (x, mu) in enumerate((x, mu) for x in sites for mu in range(d))}
    plaqs = []
    for x in sites:
        for mu in range(d):
            for nu in range(mu+1, d):
                plaqs.append([(links[(x, mu)], +1), (links[(sh(x, mu), nu)], +1),
                              (links[(sh(x, nu), mu)], -1), (links[(x, nu)], -1)])
    return len(links), plaqs

LET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def amplitude(nlinks, plaqs, spins):
    # index labels: plaquette p, corner k -> label
    lab = {}; nl = 0
    for p in range(len(plaqs)):
        for k in range(4): lab[(p, k)] = LET[nl]; nl += 1
    occ = {l: [] for l in range(nlinks)}  # (j, conj, rowlabel, collabel)
    for p, pl in enumerate(plaqs):
        j = spins[p]
        if j == 0: continue
        for k, (l, s) in enumerate(pl):
            a, b = lab[(p, k)], lab[(p, (k+1) % 4)]
            if s == +1: occ[l].append((j, False, a, b))
            else:       occ[l].append((j, True, b, a))   # (D^dag)_{ab} = conj(D)_{ba}
    ops, subs = [], []
    for l, lst in occ.items():
        if not lst: continue
        spec = tuple((j, c) for j, c, _, _ in lst)
        dims = [int(round(2*j+1)) for j, _ in spec]
        P = inv_projector(spec).reshape(dims + dims)
        ops.append(P); subs.append(''.join(r for *_, r, _ in lst) + ''.join(c for *_, c in lst))
    # plaquettes with j=0 contribute chi_0 = 1; labels of nonzero plaquettes all used twice
    if not ops: return 1.0
    val = np.einsum(','.join(subs) + '->', *ops, optimize='greedy')
    return val

def bessel_I(n, x, terms=80):
    return sum((x/2)**(2*k+n)/(math.factorial(k)*math.factorial(k+n)) for k in range(terms))

def main(out):
    f = open(out, 'x'); W = lambda s: (print(s), f.write(s+'\n'), f.flush())
    ok_all = True
    # C0
    t = np.trace(inv_projector(((0.5, False),)*4)).real
    c0 = abs(t-2) < 1e-9; W(f"C0 trace P_inv(V1/2^x4) = {t:.12f}  expect 2  {'MET' if c0 else 'FAILED'}")
    # C1
    nl, pl = lattice((1, 1))
    for a in (0.5, 1, 1.5):
        A = amplitude(nl, pl, [a]).real; ok = abs(A - 1/(2*a+1)) < 1e-9
        W(f"C1 d=2 L=1 A({a}) = {A:.12f} expect {1/(2*a+1):.12f} {'MET' if ok else 'FAILED'}"); c0 &= ok
    nl, pl = lattice((1, 1, 1))
    for a in (0.5, 1):
        A = amplitude(nl, pl, [a, 0, 0]).real; ok = abs(A - 1/(2*a+1)) < 1e-9
        W(f"C2 d=3 L=1 A({a},0,0) = {A:.12f} expect {1/(2*a+1):.12f} {'MET' if ok else 'FAILED'}"); c0 &= ok
    # K1
    k1 = True
    nq = 4000
    for beta in (0.5, 1, 2, 4, 8, 16):
        for tj in range(11):
            j = tj/2
            # Weyl: int f dU = (2/pi) int_0^pi f(t) sin^2 t dt, tr U = 2cos t, chi_j = sin((2j+1)t)/sin t
            ts = (np.arange(nq)+0.5)*math.pi/nq
            cj = (2/math.pi)*np.sum(np.exp(beta*np.cos(ts))*np.sin((2*j+1)*ts)*np.sin(ts))*math.pi/nq
            form = (2*j+1)*2*bessel_I(int(2*j+1), beta)/beta
            ok = cj > 0 and abs(cj-form) <= 1e-8*abs(form)
            # note: c_j as coefficient of chi_j: exp(beta cos t) = sum_j c_j chi_j / ... see report
            if not ok: k1 = False; W(f"K1 beta={beta} j={j} quad={cj:.6e} formula={form:.6e} FAILED")
    W(f"K1 c_j(beta)>0 and = (2j+1)2I_(2j+1)(beta)/beta *[see note] : {'MET' if k1 else 'FAILED'}")
    # H
    cases = [((1, 1, 1), [0, 0.5, 1]), ((2, 1, 1), [0, 0.5, 1]), ((1, 1, 1, 1), [0, 0.5, 1])]
    worst = {}
    for Ls, sp in cases:
        nl, pl = lattice(Ls); npq = len(pl)
        neg = pos = zer = 0; mn = (1e9, None); imag = 0.0
        for conf in itertools.product(sp, repeat=npq):
            A = amplitude(nl, pl, list(conf)); imag = max(imag, abs(A.imag)); A = A.real
            if A < -1e-9: neg += 1
            elif A > 1e-9: pos += 1
            else: zer += 1
            if A < mn[0]: mn = (A, conf)
        W(f"H case Ls={Ls} plaquettes={npq} configs={neg+pos+zer}: A<0: {neg}, A>0: {pos}, A=0: {zer}; "
          f"min A = {mn[0]:.12f} at spins {mn[1]}; max|Im A| = {imag:.1e}")
        worst[Ls] = mn
        if neg: ok_all = False
    W(f"H (all A >= 0): {'MET' if ok_all else 'FAILED'}")
    # weight-level check for the most negative d=3 configuration: is it suppressed relative to
    # positive configurations at all beta? record c-product ratio at beta = 1, 4, 16
    f.close()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
