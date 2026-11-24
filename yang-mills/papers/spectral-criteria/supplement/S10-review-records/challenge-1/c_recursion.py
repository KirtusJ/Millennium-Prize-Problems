#!/usr/bin/env python3
"""Items (c), (a-toy), (d): Corollary c:acc, Remark r:budget, Theorem t:inh, toy for Corollary c:vac,
and matrix examples for the plain-words sentences.

PREDICATES (fixed before the first run):
 C1  Finite inequality of Cor. c:acc on 20000 random sequences (n in 1..12; K_i in (0,3];
     kappa_i, eps_i, b_i, d_i real, signs unrestricted, d_0>=0), generated WITHOUT forcing the
     hypotheses; per instance test  d_i >= (b_i-kappa_i)/K_i  and  b_i >= d_{i-1}-eps_i for all i;
     report how many qualify; on qualifying ones
        d_n >= M_n^{-1}(d_0 - sum M_{i-1}(eps_i+kappa_i)) - 1e-9*(scale).
     A second batch of 20000 is generated to satisfy the hypotheses with random slack
     (half of them with zero slack = equality), same check.
 C2  Remark r:budget in exact rationals, i=1..60: recurrence holds with equality; partial sums
     of M_{i-1}kappa_i equal d_0(1-2^-n) (so the sum is d_0 exactly, budget's strict inequality
     fails); d_i strictly decreasing with d_60 < 1e-17; M_60 < 2.5; the corollary's bound equals
     d_n exactly (bound tight).
 C3  liminf statement: 2000 random infinite-type sequences truncated at n=200 with
     K_i=1+2/(m_i g_i), m_i = m_0 2^i, g_i in (0.05,1], kappa_i,eps_i >=0 scaled so that
     sum_{i<=200} M_{i-1}(eps_i+kappa_i) = s < d_0 (hypothesis tested per instance), equality
     recursion: d_n >= (d_0-s)/M_200 for all n<=200.
 C4  Theorem t:inh on 4000 random instances (dim 4..9; A random 0<=A<=I, some with eigenvalue
     exactly 1 or 0; P random projection; B random projection inside ran Q, possibly 0 or Q;
     m in 1..8, 1<=j<=m). gamma = largest admissible (inf of <f,(I-A^2)f>/||Gf||^2, computed as
     1/lambda_max(G (I-A^2)^+ G) when I-A^2 > 0 on ran... else 0 -> instance not qualifying),
     kappa = ||B A^j B||, b = 1-||P A^m P||.  Qualifying = gamma > 1e-9.
     Check 1-||A^m|| >= (b-kappa)_+/(1+2/(m gamma)) - 1e-10.  Report the smallest slack.
 C5  Indexing variants that the text does NOT claim, to see whether a slip would be detectable
     (each is expected to fail on some instance; they are kept as failed predicates if they do):
     (i) bound with M_i in place of M_{i-1} in the sum but K_i<1 allowed; (ii) Theorem t:inh
     with lag j > m allowed (j in m+1..2m): kappa = ||B A^j B||.
 A1  Toy for Cor. c:vac: 2000 random reversible Markov kernels S on 12..30 points (symmetric
     in L^2(pi)), a random partition into "coarse" classes, Gamma a union of classes.
     p := max_x P(y in Gamma | x).  Check ||chi S^n chi|| <= p (n=1,2,3; note S>=0 is forced by
     using S = R^2 with R reversible), B = chi(I-P) is an orthogonal projection
     (B^2=B, B self-adjoint in L^2(pi)), ran B inside ran(I-P), ||B S^n B|| <= p,
     B1 = 0, P1 = 1.  Also a control with Gamma NOT a union of coarse classes: count how often
     chi(I-P) fails to be a projection (expected: almost always).
 D1  Sentence of the Introduction ("the predictable part decays ... and the remainder decays
     within a few lattice steps. Then the fine lattice inherits the coarse decay"): 2x2 example
     A = |v><v|, v=(1,1)/sqrt2, P=diag(1,0), Q=diag(0,1), B=0: report ||P A^m P||, ||Q A^2 Q||,
     ||A^m|| and the largest gamma admissible in Theorem t:inh.  Predicate: ||PA^mP||=1/2,
     ||QA^2Q||=1/2, ||A^m||=1, gamma_max=0 (so the theorem is not contradicted, and the loose
     sentence read as "Q-part decays" is false).
Command: python3 /home/user/z4-workers/chal5/c_recursion.py   (no arguments; seed 20261124)
Result file: /home/user/z4-workers/chal5/c_recursion_result.txt (mode 'x').
"""
import math
from fractions import Fraction as F
import numpy as np
SEED = 20261124
rng = np.random.default_rng(SEED)
out = open('/home/user/z4-workers/chal5/c_recursion_result.txt', 'x')
def P(*a):
    s = ' '.join(str(x) for x in a)
    print(s); out.write(s + '\n'); out.flush()

def check_seq(d0, K, kap, eps, b, d):
    n = len(K)
    dd = [d0] + list(d)
    hyp = all(dd[i+1] >= (b[i]-kap[i])/K[i] and b[i] >= dd[i]-eps[i] for i in range(n))
    M = [1.0]
    for k in K: M.append(M[-1]*k)
    bound = (d0 - sum(M[i]*(eps[i]+kap[i]) for i in range(n)))/M[n]
    bound_wrong = (d0 - sum(M[i+1]*(eps[i]+kap[i]) for i in range(n)))/M[n]
    scale = 1+abs(bound)+abs(dd[n])
    return hyp, dd[n] >= bound - 1e-9*scale, dd[n] >= bound_wrong - 1e-9*scale

# C1 unforced
q = f = 0
for _ in range(20000):
    n = int(rng.integers(1, 13))
    K = rng.uniform(1e-3, 3, n); kap = rng.normal(size=n); eps = rng.normal(size=n)
    b = rng.normal(size=n); d = rng.normal(size=n)+1.0; d0 = abs(rng.normal())
    h, ok, _ = check_seq(d0, K, kap, eps, b, d)
    if h:
        q += 1
        if not ok: f += 1
P(f'C1 unforced: 20000 instances, qualifying {q}, failures {f}', 'PASS' if f == 0 else 'FAIL')
q = f = fw = 0
for t in range(20000):
    n = int(rng.integers(1, 13))
    K = rng.uniform(1e-3, 3, n); kap = rng.normal(size=n); eps = rng.normal(size=n)
    d0 = abs(rng.normal()); b = np.zeros(n); d = np.zeros(n); prev = d0
    for i in range(n):
        s1, s2 = (0.0, 0.0) if t % 2 == 0 else (rng.exponential(), rng.exponential())
        b[i] = prev - eps[i] + s1
        d[i] = (b[i]-kap[i])/K[i] + s2
        prev = d[i]
    h, ok, okw = check_seq(d0, K, kap, eps, b, d)
    if h:
        q += 1
        if not ok: f += 1
        if not okw: fw += 1
P(f'C1 forced: 20000 instances, qualifying {q}, failures {f}', 'PASS' if f == 0 else 'FAIL')
P(f'C5(i) variant with M_i in the sum (not claimed): failures {fw} of {q}', 'FAILED PREDICATE (kept)' if fw else 'no failure found')

# C2 exact
d0 = F(1, 2); M = [F(1)]; d = [d0]; s = F(0); ok = True
for i in range(1, 61):
    K = 1 + F(1, 2**i); M.append(M[-1]*K)
    bi = d[i-1]; ki = d[i-1]/2
    di = d0/(2**i*M[i])
    ok = ok and di == (bi-ki)/K and bi == d[i-1]
    s += M[i-1]*ki
    ok = ok and s == d0*(1-F(1, 2**i))
    ok = ok and (d0-s)/M[i] == di and di < d[i-1]
    d.append(di)
P(f'C2 exact: all equalities {ok}; d_60={float(d[60]):.3e}; M_60={float(M[60]):.6f}; sum_60/d_0={float(s/d0)!r}',
  'PASS' if ok and d[60] < F(1, 10**17) and M[60] < F(5, 2) else 'FAIL')

# C3
q = f = 0; minratio = 1e9
for _ in range(2000):
    n = 200; m0 = int(rng.integers(1, 5))
    g = rng.uniform(0.05, 1, n)
    K = np.array([1+2/(m0*2.0**(i+1)*g[i]) for i in range(n)])
    M = np.concatenate([[1.0], np.cumprod(K)])
    raw = rng.exponential(size=n)*0.5**(np.arange(n)*rng.uniform(0, 1))
    d0 = rng.uniform(0.05, 1)
    s = d0*rng.uniform(0.0, 1.2)           # some instances violate the budget on purpose
    tot = raw*s/np.sum(M[:-1]*raw)
    split = rng.uniform(size=n); kap = tot*split; eps = tot*(1-split)
    hyp = np.sum(M[:-1]*(eps+kap)) < d0
    if not hyp: continue
    q += 1
    dd = d0; lo = (d0-np.sum(M[:-1]*(eps+kap)))/M[-1]
    for i in range(n):
        dd = (dd-eps[i]-kap[i])/K[i]
        minratio = min(minratio, dd/lo)
        if dd < lo*(1-1e-9): f += 1; break
P(f'C3: 2000 instances, qualifying {q}, failures {f}, smallest d_n/((d0-s)/M_200) = {minratio:.6f}', 'PASS' if f == 0 else 'FAIL')

# C4 / C5(ii)
def randproj(n, r):
    if r == 0: return np.zeros((n, n))
    Qm, _ = np.linalg.qr(rng.normal(size=(n, r)))
    return Qm@Qm.T
def opnorm(X): return np.linalg.norm(X, 2)
q = f = 0; minslack = 1e9; q5 = f5 = 0; worst5 = 0.0
for it in range(4000):
    n = int(rng.integers(4, 10))
    ev = rng.uniform(0, 1, n)**rng.choice([0.2, 1, 3])
    if it % 5 == 0: ev[0] = 1.0
    if it % 7 == 0: ev[1] = 0.0
    if it % 3 == 0: ev = 1-(1-ev)*rng.uniform(0.001, 0.3)      # near-identity regime
    O, _ = np.linalg.qr(rng.normal(size=(n, n)))
    A = O@np.diag(ev)@O.T
    rP = int(rng.integers(1, n)); Pm = randproj(n, rP)
    w, V = np.linalg.eigh(np.eye(n)-Pm); Qb = V[:, w > 0.5]         # basis of ran Q
    rB = int(rng.integers(0, Qb.shape[1]+1))
    if rB:
        Z, _ = np.linalg.qr(rng.normal(size=(Qb.shape[1], rB))); Bb = Qb@Z; Bm = Bb@Bb.T
    else: Bm = np.zeros((n, n))
    G = np.eye(n)-Pm-Bm
    # gamma_max = inf <f,(I-A^2)f>/||Gf||^2
    X = np.eye(n)-A@A
    wx, Vx = np.linalg.eigh(X)
    if opnorm(G) < 1e-9: gamma = 1e6       # G = 0: any gamma admissible
    elif wx.min() < 1e-12:
        # kernel of X (eigenvalue 1 of A): admissible gamma>0 only if G kills that kernel
        ker = Vx[:, wx < 1e-12]
        if opnorm(G@ker) > 1e-9: continue
        gamma = None
    else: gamma = None
    if gamma is None:
        pos = wx > 1e-12
        Xp = Vx[:, pos]@np.diag(1/wx[pos])@Vx[:, pos].T
        lam = np.linalg.eigvalsh(G@Xp@G).max()
        gamma = 1/lam
    if gamma <= 1e-9: continue
    m = int(rng.integers(1, 9)); j = int(rng.integers(1, m+1))
    Am = np.linalg.matrix_power(A, m)
    b = 1-opnorm(Pm@Am@Pm)
    kap = opnorm(Bm@np.linalg.matrix_power(A, j)@Bm)
    lhs = 1-opnorm(Am); rhs = max(b-kap, 0)/(1+2/(m*gamma))
    q += 1; minslack = min(minslack, lhs-rhs)
    if lhs < rhs-1e-10: f += 1
    j2 = int(rng.integers(m+1, 2*m+1))
    kap2 = opnorm(Bm@np.linalg.matrix_power(A, j2)@Bm)
    rhs2 = max(b-kap2, 0)/(1+2/(m*gamma)); q5 += 1
    worst5 = min(worst5, lhs-rhs2)
    if lhs < rhs2-1e-10: f5 += 1
P(f'C4: 4000 instances, qualifying {q}, failures {f}, smallest slack {minslack:.3e}', 'PASS' if f == 0 else 'FAIL')
P(f'C5(ii) variant j in m+1..2m (not claimed): failures {f5} of {q5}, most negative slack {worst5:.3e}',
  'FAILED PREDICATE (kept)' if f5 else 'no failure found in this sample')

# A1 toy
fails = dict(chi=0, proj=0, rng_=0, B=0, const=0); ctrl_notproj = 0; N_A = 2000; minslackA = 1e9
for it in range(N_A):
    n = int(rng.integers(12, 31))
    Wm = rng.exponential(size=(n, n))**3; Wm = Wm+Wm.T
    pi = Wm.sum(1)/Wm.sum(); R = Wm/Wm.sum(1, keepdims=True)
    S = R@R                                   # reversible w.r.t. pi and >= 0 in L^2(pi)
    D = np.diag(np.sqrt(pi)); Di = np.diag(1/np.sqrt(pi))
    sym = lambda X: D@X@Di                    # similarity to the flat inner product
    ncl = int(rng.integers(3, 7)); lab = rng.integers(0, ncl, n); lab[:ncl] = np.arange(ncl)
    Pc = np.zeros((n, n))
    for c in range(ncl):
        idx = np.where(lab == c)[0]
        Pc[np.ix_(idx, idx)] = pi[idx][None, :]/pi[idx].sum()
    gam = (lab == 0) | ((lab == 1) & (it % 2 == 0))
    chi = np.diag(gam.astype(float))
    Bm = chi@(np.eye(n)-Pc)
    Bs = sym(Bm)
    if opnorm(Bs@Bs-Bs) > 1e-10 or opnorm(Bs-Bs.T) > 1e-10: fails['proj'] += 1
    if opnorm((np.eye(n)-Pc)@Bm-Bm) > 1e-10: fails['rng_'] += 1
    if np.abs(Bm@np.ones(n)).max() > 1e-10 or np.abs(Pc@np.ones(n)-1).max() > 1e-10: fails['const'] += 1
    for k in (1, 2, 3):
        Sk = np.linalg.matrix_power(S, k)
        p = (Sk@gam.astype(float)).max()      # max_x P(y in Gamma | x) at lag k
        a = opnorm(sym(chi@Sk@chi)); bb = opnorm(sym(Bm@Sk@Bm))
        minslackA = min(minslackA, p-a)
        if a > p+1e-10: fails['chi'] += 1
        if bb > p+1e-10: fails['B'] += 1
    g2 = gam.copy(); i0 = np.where(lab == 2)[0]
    if len(i0) >= 2:
        g2[i0[0]] = True
        B2 = sym(np.diag(g2.astype(float))@(np.eye(n)-Pc))
        if opnorm(B2@B2-B2) > 1e-8 or opnorm(B2-B2.T) > 1e-8: ctrl_notproj += 1
P(f'A1: {N_A} kernels; failures {fails}; smallest (p - ||chi S^n chi||) = {minslackA:.3e}',
  'PASS' if not any(fails.values()) else 'FAIL')
P(f'A1 control (Gamma not coarse-measurable): chi(I-P) not a projection in {ctrl_notproj} cases')

# D1
v = np.array([1, 1])/math.sqrt(2); A = np.outer(v, v); Pm = np.diag([1.0, 0]); Qm = np.diag([0, 1.0])
m = 6; Am = np.linalg.matrix_power(A, m)
a1, a2, a3 = opnorm(Pm@Am@Pm), opnorm(Qm@A@A@Qm), opnorm(Am)
loss_v = v@(np.eye(2)-A@A)@v; Gv = np.linalg.norm(Qm@v)**2
P(f'D1: ||PA^mP||={a1:.6f} ||QA^2Q||={a2:.6f} ||A^m||={a3:.6f}; <v,(I-A^2)v>={loss_v:.2e}, ||Gv||^2={Gv:.3f} -> gamma_max=0',
  'PASS' if abs(a1-.5) < 1e-12 and abs(a2-.5) < 1e-12 and abs(a3-1) < 1e-12 and abs(loss_v) < 1e-12 else 'FAIL')
out.close()
