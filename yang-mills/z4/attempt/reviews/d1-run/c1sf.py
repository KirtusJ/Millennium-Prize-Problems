"""c1sf.py -- one-loop coefficient c1(R;G) of the Schrodinger-functional coupling.

Setting (own definition, follows Luscher-Weisz-Wolff 1991 / LNWW 1992 abelian boundary fields):
  lattice x0 = 0..T (T=R), d-1 periodic spatial directions of length R, Wilson action
  S = sum_p (1 - (1/N) Re tr U_p) over plaquettes with >= 1 dynamical link, N=2 (SU(2)) or N=1 (U(1)).
  Boundary spatial links exp(i phi(x0)/R * Q), Q = sigma3 (SU2) or 1 (U1), phi(0)=-eta, phi(T)=-(pi-eta).
  Background V: time links 1, spatial links exp(i phi(x0) Q / R), phi linear in x0.
  beta = 4/g0^2 (SU2), 1/g0^2 (U1) [both give (1/2g0^2) sum f_a^2 at quadratic order]; k = g0^2 beta dS0/deta ; c1 = -Gamma1'(eta)/k at eta=pi/4,
  Gamma1 = 1/2 sum_p logdet(H(p)+D(p)D(p)^+) - sum_p logdet(D(p)^+ D(p))  (p = spatial momenta).
  Gauge directions: omega at sites 1<=x0<=T-1 (all colours), plus at p=0 one generator at x0=T
  in the centraliser of the boundary field (sigma3 resp. 1).

PREDICATES (fixed before first run):
  P1 gradient of S at V vanishes: max |grad| <= 1e-12 (double rounding of O(1) entries, O(10) terms).
  P2 H(p) D(p) = 0 for all p: max |.| <= 1e-12 (same origin).
  P3 H(p)+D(p)D(p)^+ positive definite for all p: min eigenvalue > 1e-8 (well above rounding 1e-13;
     a genuine zero mode would show up at ~1e-14). Report min eigenvalue.
  P4 Hermiticity of H(p): max |H-H^+| <= 1e-12.
  P5 tree level: k computed from finite difference of S(V(eta)) agrees with analytic k to 1e-6 relative
     (central difference h=1e-4: truncation ~h^2 ~1e-8, rounding ~1e-16*S/h).
  P6 derivative stability: Gamma1' from step h=1e-3 and h=5e-4 agree to 1e-7 absolute
     (truncation O(h^2)*|Gamma1'''| ; Richardson estimate printed).
  P7 (SU2, d=4) slope: c1(R)-c1(R/2) within 25% of 2 b0 ln 2 = 0.0644 for R>=8 (my expectation,
     O(a/L) artefacts unimproved; failure would be my expectation, unless gross).
  P8 (U1) |c1(R)-c1(R/2)| < 0.01 for R>=8 (my expectation: only lattice artefacts).
Usage: python3 c1sf.py GROUP d R1 R2 ... outfile
"""
import sys, itertools, math
import numpy as np

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)

def setup(group):
    if group == 'SU2':
        T = [1j * s / 2 for s in (s1, s2, s3)]
        return dict(N=2, T=T, Q=s3, metric=lambda A: -2 * A, I=np.eye(2, dtype=complex), cent=[2])
    if group == 'U1':
        return dict(N=1, T=[np.array([[1j]])], Q=np.array([[1.0 + 0j]]), metric=lambda A: A,
                    I=np.eye(1, dtype=complex), cent=[0])
    raise ValueError

def expm_diag(Q, a):  # Q diagonal hermitian
    return np.diag(np.exp(1j * a * np.diag(Q)))

def comp(g, A):  # components of Lie algebra element A in basis T (orthonormal for metric -2tr / tr)
    if g['N'] == 2: return np.array([np.real(-2 * np.trace(Ta @ A)) for Ta in g['T']])
    return np.array([np.real(-1j * A[0, 0])])

def geometry(d, R):
    T = R
    links = []  # (x0, mu)
    for x0 in range(T): links.append((x0, 0))
    for x0 in range(1, T):
        for k in range(1, d): links.append((x0, k))
    lid = {l: i for i, l in enumerate(links)}
    sites = list(range(1, T))
    return T, links, lid, sites

def phi(x0, T, eta):
    return -eta - (math.pi - 2 * eta) * x0 / T

def Vlink(g, x0, mu, T, R, eta):
    if mu == 0: return g['I']
    return expm_diag(g['Q'], phi(x0, T, eta) / R)

def plaquettes(d, T):
    """plaquettes with base spatial position 0: list of factors (x0, mu, spatial offset tuple, sign)."""
    sp = d - 1
    def e(mu):
        v = [0] * sp
        if mu > 0: v[mu - 1] = 1
        return tuple(v)
    out = []
    z = tuple([0] * sp)
    for mu in range(d):
        for nu in range(mu + 1, d):
            for x0 in range(T + 1):
                # U(x,mu)U(x+mu,nu)U(x+nu,mu)^-1U(x,nu)^-1
                fs = [(x0, mu, z, +1), (x0 + (mu == 0), nu, e(mu), +1),
                      (x0 + (nu == 0), mu, e(nu), -1), (x0, nu, z, -1)]
                if any(f[0] > T or (f[1] == 0 and f[0] >= T) for f in fs): continue
                out.append(fs)
    return out

def is_dyn(f, T):
    x0, mu = f[0], f[1]
    if mu == 0: return 0 <= x0 <= T - 1
    return 1 <= x0 <= T - 1

def action_density(g, d, R, eta):
    T = R; tot = 0.0
    for fs in plaquettes(d, T):
        if not any(is_dyn(f, T) for f in fs): continue
        M = g['I']
        for (x0, mu, off, s) in fs:
            V = Vlink(g, x0, mu, T, R, eta)
            M = M @ (V if s > 0 else V.conj().T)
        tot += 1 - np.real(np.trace(M)) / g['N']
    return tot * R ** (d - 1)  # translations

def local_hessian(g, d, R, eta):
    """returns list of (i_link, off_i, j_link, off_j, block[a,b]) and gradient contributions."""
    T, links, lid, sites = geometry(d, R)
    nA = len(g['T']); Ts = g['T']
    entries = []; grad = {}
    for fs in plaquettes(d, T):
        dyn = [is_dyn(f, T) for f in fs]
        if not any(dyn): continue
        Vs = [Vlink(g, f[0], f[1], T, R, eta) for f in fs]
        F = [V if f[3] > 0 else V.conj().T for f, V in zip(fs, Vs)]
        def d1(i, a):
            return Ts[a] @ Vs[i] if fs[i][3] > 0 else -Vs[i].conj().T @ Ts[a]
        def d2(i, a, b):
            S2 = 0.5 * (Ts[a] @ Ts[b] + Ts[b] @ Ts[a])
            return S2 @ Vs[i] if fs[i][3] > 0 else Vs[i].conj().T @ S2
        def prod(rep):
            M = g['I']
            for i in range(4): M = M @ rep.get(i, F[i])
            return M
        for i in range(4):
            if not dyn[i]: continue
            for a in range(nA):
                key = (lid[(fs[i][0], fs[i][1])], a)
                grad[key] = grad.get(key, 0) - np.real(np.trace(prod({i: d1(i, a)}))) / g['N']
        for i in range(4):
            if not dyn[i]: continue
            for j in range(4):
                if not dyn[j]: continue
                B = np.zeros((nA, nA))
                for a in range(nA):
                    for b in range(nA):
                        rep = {i: d2(i, a, b)} if i == j else {i: d1(i, a), j: d1(j, b)}
                        B[a, b] = -np.real(np.trace(prod(rep))) / g['N']
                entries.append((lid[(fs[i][0], fs[i][1])], fs[i][2], lid[(fs[j][0], fs[j][1])], fs[j][2], B))
    return entries, grad, links, sites

def Ad(g, V):
    nA = len(g['T'])
    M = np.zeros((nA, nA))
    for b in range(nA):
        M[:, b] = comp(g, V @ g['T'][b] @ V.conj().T)
    return M

def momenta(d, R):
    return list(itertools.product(range(R), repeat=d - 1))

def hparts(g, entries, links):
    nA = len(g['T']); nL = len(links); parts = {}
    for (li, oi, lj, oj, B) in entries:
        r = tuple(np.array(oj) - np.array(oi))
        if r not in parts: parts[r] = np.zeros((nL * nA, nL * nA))
        parts[r][li * nA:(li + 1) * nA, lj * nA:(lj + 1) * nA] += B
    return [(np.array(r), M) for r, M in parts.items()]

def build_p(g, d, R, eta, hp, links, sites, p):
    T = R; nA = len(g['T']); nL = len(links)
    pv = 2 * math.pi * np.array(p) / R
    H = np.zeros((nL * nA, nL * nA), complex)
    for r, M in hp:
        H += M * np.exp(1j * pv @ r)
    zero = all(q == 0 for q in p)
    cols = len(sites) * nA + (len(g['cent']) if zero else 0)
    D = np.zeros((nL * nA, cols), complex)
    sidx = {x0: i for i, x0 in enumerate(sites)}
    for l, (x0, mu) in enumerate(links):
        x1 = x0 + (mu == 0)
        ph = np.exp(1j * pv[mu - 1]) if mu > 0 else 1.0
        V = Vlink(g, x0, mu, T, R, eta)
        A = Ad(g, V)
        if x0 in sidx:
            for a in range(nA): D[l * nA + a, sidx[x0] * nA + a] += 1.0
        if x1 in sidx:
            D[l * nA:(l + 1) * nA, sidx[x1] * nA:(sidx[x1] + 1) * nA] -= A * ph
        if x1 == T and zero:
            for c, a in enumerate(g['cent']):
                D[l * nA:(l + 1) * nA, len(sites) * nA + c] -= A[:, a]
    return H, D

def logdets(g, d, R, eta, checks=False):
    entries, grad, links, sites = local_hessian(g, d, R, eta)
    out = dict(gradmax=max(abs(v) for v in grad.values()), HDmax=0.0, herm=0.0, mineig=np.inf)
    G = 0.0
    hp = hparts(g, entries, links)
    for p in momenta(d, R):
        H, D = build_p(g, d, R, eta, hp, links, sites, p)
        A = H + D @ D.conj().T
        Gh = D.conj().T @ D
        if checks:
            out['HDmax'] = max(out['HDmax'], np.abs(H @ D).max())
            out['herm'] = max(out['herm'], np.abs(H - H.conj().T).max())
            out['mineig'] = min(out['mineig'], np.linalg.eigvalsh(A).min())
        s1_, l1 = np.linalg.slogdet(A); s2_, l2 = np.linalg.slogdet(Gh)
        G += 0.5 * l1 - l2
    return G, out

def c1(group, d, R, eta=math.pi / 4, hs=(1e-3, 5e-4)):
    g = setup(group)
    N = g['N']; bf = 4 if group == 'SU2' else 1  # beta = bf/g0^2
    # analytic tree level: (d-1) R^(d-1) T (1-cos theta), theta = (pi-2eta)/R^2
    S0 = lambda e: action_density(g, d, R, e)
    h0 = 1e-4
    kfd = bf * (S0(eta + h0) - S0(eta - h0)) / (2 * h0)
    th = (math.pi - 2 * eta) / R ** 2
    kan = bf * (d - 1) * R ** (d - 1) * R * math.sin(th) * (-2 / R ** 2)
    _, chk = logdets(g, d, R, eta, checks=True)
    ders = []
    for h in hs:
        ders.append((logdets(g, d, R, eta + h)[0] - logdets(g, d, R, eta - h)[0]) / (2 * h))
    G1p = ders[-1] + (ders[-1] - ders[0]) / 3  # Richardson
    return dict(group=group, d=d, R=R, k_fd=kfd, k_an=kan, G1p_h=ders, G1p=G1p, c1=-G1p / kan, **chk)

if __name__ == '__main__':
    group, d = sys.argv[1], int(sys.argv[2]); Rs = [int(x) for x in sys.argv[3:-1]]; outf = sys.argv[-1]
    with open(outf, 'x') as fo:
        for R in Rs:
            r = c1(group, d, R)
            line = ' '.join(f'{k}={v}' for k, v in r.items())
            print(line, flush=True); fo.write(line + '\n'); fo.flush()
