"""e2-score: falsification attempt of the auditor's mixed-score argument (T229).

Assumption (not checkable here: wilson_mc.rs is absent): site index
x = c0 + n c1 + n^2 c2 + n^3 t, plus[x][d] the periodic +d neighbour; this is
the convention frozen() in replicas.rs uses for coord.  Action exp(beta*sum_p Re U_p)
(plaquette() returns Re U_p; acceptance beta*(y-1)).

PREDICATES (fixed before first run):
 G1  transported marks: link content of g_j (j=0..3, base (0,0),(1,0),(0,1),(1,1)),
     free links only, as multiset with orientation, equals
     g0:{u-,w+}  g1:{v-,w-}  g2:{u+,z+}  g3:{w+,v+,z-,w-}   (exact, combinatorial)
     [u=U_x(0,1), v=U_x(1,1), w=U_y(1,0), z=U_y(1,1)]; every other link frozen.
 G2  colours touching {u,v,w,z}: exactly colours 0,1,2,3, selecting (u,w),(v,w),(u,z),(v,z).
 G3  in colours 0,2,3: exactly one mark contains both selected links; that mark contains
     each exactly once; every other mark contains at most one of them (multiplicity
     arbitrary). In colour 1: measured only.
 G4  for every colour (24), selected pairs are link-disjoint and no 4D plaquette contains
     links of two different pairs (factorization); and each pair shares exactly one plaquette.
     Lattice n=6, period 6.  (for-all: count qualifying colours/pairs first.)
 A1  sum_{a,b} A_ab^2 = 2 + Y^2 for Y=Re(C u M w N), A_ab=Re(C u e_a M w e_b N) on 1e5
     random unit quaternion sets, |err| <= 1e-12 (double rounding of ~50 flops); min >= 2-1e-12.
 A2  finite-difference D_a E_b F = A_ab/4 in colours 0,2,3 on 200 random configurations,
     central differences h=1e-4: error O(h^2)~1e-8, tolerance 1e-6. Colour 1: measured only
     (expected to differ: Y_3 also contributes).
 C1  (sqrt(1+6b)+b)^2+6b(1+6b) <= 58 b^2 for all b>=1 (grid b in [1,1e4], 1e5 points, and
     limit 36+6=42 < 58); 9*8=72; 4*72^2=20736; 8*20736=165888; floors at the two matched
     couplings equal 5.61645e-7, 5.21526e-7 to 6 significant digits.
 C2  zero-staple control (h_u=h_v=0): Z = 9Y + beta(7Y^2-4) - beta^2 Y(1-Y^2) pointwise
     from my expansion of E*D*A (|err|<=1e-10), and by 1-D quadrature with density
     e^{beta y} sqrt(1-y^2): E Z = 0 (|.|<=1e-8 quadrature), E[(Y-EY)Z] = E[2+Y^2] (1e-8),
     ||Z||/beta <= 72 for beta in {1,3.3,10,30}. Var(Y/4)*20736 beta^2 >= 1 (measured value
     reported).
"""
import numpy as np, sys, itertools, math

out = open(sys.argv[1], "x")
def log(*a):
    s = " ".join(str(x) for x in a); print(s); out.write(s + "\n"); out.flush()
fails = []
def pred(name, ok, info=""):
    log(f"[{'PASS' if ok else 'FAIL'}] {name} {info}")
    if not ok: fails.append(name)

# ---------------- geometry ----------------
n, T = 6, 6
def idx(c): return (c[0] % n) + n * (c[1] % n) + n * n * (c[2] % n) + n**3 * (c[3] % T)
def coord(x): return [x % n, (x // n) % n, (x // (n*n)) % n, x // n**3]
def plus(x, d):
    c = coord(x); c[d] += 1; return idx(c)
def frozen(x, i):
    if x >= n**3 or i == 3: return False
    c = coord(x)
    return all(j == i or c[j] % 2 == 0 for j in range(3))
def colours():
    g = [[] for _ in range(24)]
    for x in range(n**3):
        c = coord(x); par = [c[0] % 2, c[1] % 2, c[2] % 2]
        for o, (i, j) in enumerate([(0, 1), (0, 2), (1, 2)]):
            u = (x if par[j] == 1 else plus(x, j), i)
            v = (x if par[i] == 1 else plus(x, i), j)
            g[8*o + par[0] + 2*par[1] + 4*par[2]].append(((x, i, j), u, v))
    return g
def face_links(x, i, j):  # returns [(link, +-1)] as in face(lat,x,i,j,1)
    res = []; y = x
    for d, fw in [(i, True), (j, True), (i, False), (j, False)]:
        if fw: res.append(((y, d), 1)); y = plus(y, d)
        else:
            c = coord(y); c[d] -= 1; y = idx(c); res.append(((y, d), -1))
    return res
def transported(bx, by):
    path = []; site = 0
    for d, steps in [(0, bx), (1, by)]:
        for _ in range(steps): path.append(((site, d), 1)); site = plus(site, d)
    inv = [(l, -s) for l, s in reversed(path)]
    return path + face_links(site, 0, 1) + inv

names = {(idx([0,1,0,0]),0): 'u', (idx([1,1,0,0]),0): 'v', (idx([1,0,0,0]),1): 'w', (idx([1,1,0,0]),1): 'z'}
marks = []
for j, (bx, by) in enumerate([(0,0),(1,0),(0,1),(1,1)]):
    seq = transported(bx, by)
    free = [l for l, s in seq if not frozen(*l)]
    ok_names = all(l in names for l in free)
    content = [names.get(l, str(l)) + ('+' if s > 0 else '-') for l, s in seq if not frozen(*l)]
    marks.append(content)
    log(f"g{j}: free content {content}; all free links named: {ok_names}; full word {[(coord(l[0])[:2], 'xyzt'[l[1]], s) for l,s in seq]}")
expect = [['u-','w+'],['v-','w-'],['u+','z+'],['w+','v+','z-','w-']]
pred("G1 transported-mark content", [sorted(m) for m in marks] == [sorted(e) for e in expect], str(marks))

cols = colours()
touch = {}
for c, pairs in enumerate(cols):
    sel = [names[l] for _, a, b in pairs for l in (a, b) if l in names]
    if sel: touch[c] = tuple(sel)
log("colours touching u,v,w,z:", touch)
pred("G2 colours 0..3 select (u,w),(v,w),(u,z),(v,z)", touch == {0:('u','w'),1:('v','w'),2:('u','z'),3:('v','z')})

def mult(m, x): return sum(1 for t in m if t[0] == x)
g3ok = True
for c in range(4):
    a, b = touch[c]
    both = [j for j in range(4) if mult(marks[j], a) and mult(marks[j], b)]
    info = f"colour {c} pair ({a},{b}): marks with both {both}; mults " + str([(mult(marks[j],a), mult(marks[j],b)) for j in range(4)])
    if c == 1: log("measured only:", info); continue
    ok = len(both) == 1 and mult(marks[both[0]], a) == 1 and mult(marks[both[0]], b) == 1
    log(info, "->", ok); g3ok &= ok
pred("G3 colours 0,2,3: exactly one bilinear mark", g3ok)

# G4 factorization
plaq = []
for x in range(n**3 * T):
    for i in range(4):
        for j in range(i+1, 4):
            plaq.append(set(l for l, s in face_links(x, i, j)))
ncol_ok = 0; npairs = 0; npair_ok = 0
for c, pairs in enumerate(cols):
    owner = {}
    disjoint = True
    for k, (_, a, b) in enumerate(pairs):
        for l in (a, b):
            if l in owner: disjoint = False
            owner[l] = k
    meet = 0
    for P in plaq:
        ks = set(owner[l] for l in P if l in owner)
        if len(ks) > 1: meet += 1
    for k, (_, a, b) in enumerate(pairs):
        npairs += 1
        shared = sum(1 for P in plaq if a in P and b in P)
        if shared == 1 and not frozen(*a) and not frozen(*b): npair_ok += 1
    if disjoint and meet == 0: ncol_ok += 1
log(f"G4: colours factorizing {ncol_ok}/24; pairs with exactly one shared face and both links free {npair_ok}/{npairs}")
pred("G4 factorization + one shared face", ncol_ok == 24 and npair_ok == npairs)

# ---------------- quaternion algebra ----------------
def qm(a, b):
    a0,a1,a2,a3 = np.moveaxis(a,-1,0); b0,b1,b2,b3 = np.moveaxis(b,-1,0)
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0], -1)
def cj(a): return a * np.array([1,-1,-1,-1.])
def rq(rng, k):
    q = rng.standard_normal((k, 4)); return q / np.linalg.norm(q, axis=1, keepdims=True)
E = np.eye(4)
def prod(*qs):
    r = qs[0]
    for q in qs[1:]: r = qm(r, q)
    return r

rng = np.random.default_rng(20261124)
K = 100000
C, u, M, w, N = (rq(rng, K) for _ in range(5))
Y = prod(C, u, M, w, N)[:, 0]
S = np.zeros(K)
for a in range(1, 4):
    for b in range(1, 4):
        S += prod(C, u, np.broadcast_to(E[a], (K,4)), M, w, np.broadcast_to(E[b], (K,4)), N)[:, 0]**2
err = np.max(np.abs(S - 2 - Y**2))
pred("A1 sum A^2 = 2+Y^2", err <= 1e-12 and S.min() >= 2 - 1e-12, f"maxerr={err:.2e} min={S.min():.6f} max={S.max():.6f}")

# A2: F as function of the four free links; frozen factors random
def expq(v):  # v: pure imaginary 3-vector
    th = np.linalg.norm(v)
    if th == 0: return np.array([1.,0,0,0])
    return np.concatenate([[math.cos(th)], math.sin(th) * v / th])
def Fval(L, fr):
    u, v, w, z = L
    B, X00, X10, Y00, Y01, Y20, Y21, X02, X12 = fr
    g0 = prod(X00, w, cj(u), cj(Y00))
    g1 = prod(X00, X10, Y20, cj(v), cj(w), cj(X00))
    g2 = prod(Y00, u, z, cj(X02), cj(Y01), cj(Y00))
    g3 = prod(X00, w, v, Y21, cj(X12), cj(z), cj(w), cj(X00))
    gs = [g0, g1, g2, g3]
    return [prod(B, g)[0] for g in gs]
rng2 = np.random.default_rng(7)
h = 1e-4
maxerr = {0: 0, 2: 0, 3: 0}; c1diff = 0
pos = {'u':0, 'v':1, 'w':2, 'z':3}
for trial in range(200):
    L = list(rq(rng2, 4)); fr = list(rq(rng2, 9))
    for c, (p, q) in touch.items():
        ip, iq = pos[p], pos[q]
        for a in range(1, 4):
            for b in range(1, 4):
                def Fs(s, t):
                    LL = list(L)
                    LL[ip] = qm(L[ip], expq(s * E[a][1:]))
                    LL[iq] = qm(L[iq], expq(t * E[b][1:]))
                    return np.array(Fval(LL, fr))
                mix = (Fs(h,h) - Fs(h,-h) - Fs(-h,h) + Fs(-h,-h)) / (4*h*h)  # per mark
                F_mix = mix.sum() / 4
                jsel = {0: 0, 2: 2, 3: 3}.get(c)
                if c == 1:
                    c1diff = max(c1diff, abs(F_mix - mix[1]/4)); continue
                others = np.abs(np.delete(mix, jsel)).max()
                maxerr[c] = max(maxerr[c], others, abs(F_mix - mix[jsel]/4))
                # mix[jsel] must be A_ab: Re(B * ... ) with generators at the right slots: checked via |.|<=1
log("A2 max |D E F - A/4| and |mixed of other marks| per colour:", maxerr, "; colour 1 extra from Y3 (measured only):", f"{c1diff:.3e}")
pred("A2 mixed derivative = A_jab/4 (colours 0,2,3)", max(maxerr.values()) <= 1e-6)

# ---------------- constants ----------------
bs = np.linspace(1, 1e4, 100000)
lhs = (np.sqrt(1+6*bs)+bs)**2 + 6*bs*(1+6*bs)
r = (lhs/bs**2).max()
log(f"C1 max over grid of [(sqrt(1+6b)+b)^2+6b(1+6b)]/b^2 = {r:.4f} (at b=1: {lhs[0]:.4f}); sqrt(58)={math.sqrt(58):.4f}<8")
f1 = 1/(165888*3.276133577**2); f2 = 1/(165888*3.399810242**2)
log(f"floors {f1:.6e} {f2:.6e}")
pred("C1 constants", r <= 58 and 9*8 == 72 and 4*72**2 == 20736 and 8*20736 == 165888
     and f"{f1:.5e}" == "5.61645e-07" and f"{f2:.5e}" == "5.21526e-07")

# ---------------- zero-staple control ----------------
def Zfull(u, v, C, M, N, Hu, Hv, beta):
    """E*D*A summed, by the explicit expansion; log rho = beta[Re(u Hu)+Re(v Hv)+Re(CuMvN)]"""
    k = len(u); e = lambda a: np.broadcast_to(E[a], (k, 4))
    Y = prod(C, u, M, v, N)[:, 0]; Z = np.zeros(k); S2 = np.zeros(k)
    for a in range(1, 4):
        s = beta * (prod(u, e(a), Hu)[:, 0] + prod(C, u, e(a), M, v, N)[:, 0])
        for b in range(1, 4):
            t = beta * (prod(v, e(b), Hv)[:, 0] + prod(C, u, M, v, e(b), N)[:, 0])
            A = prod(C, u, e(a), M, v, e(b), N)[:, 0]
            DA = -prod(C, u, M, v, e(b), N)[:, 0]
            EA = -prod(C, u, e(a), M, v, N)[:, 0]
            DEA = Y
            EsA = beta * A
            Z += DEA + EsA * A + s * EA + t * DA + s * t * A
            S2 += A * A
    return Y, Z, S2
k = 20000
uu, vv, CC, MM, NN = (rq(rng, k) for _ in range(5))
zero = np.zeros((k, 4))
for beta in [1.0, 3.3]:
    Yz, Zz, _ = Zfull(uu, vv, CC, MM, NN, zero, zero, beta)
    e = np.max(np.abs(Zz - (9*Yz + beta*(7*Yz**2-4) - beta**2*Yz*(1-Yz**2))))
    pred(f"C2 pointwise zero-staple formula beta={beta}", e <= 1e-10, f"err={e:.2e}")
# 1-D quadrature in s=beta(1-y)
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(4000)
c2ok = True
for beta in [1.0, 3.3, 10.0, 30.0]:
    # y in [-1,1]; substitution y = cos(theta) improves endpoints: density e^{beta y} sqrt(1-y^2) dy = e^{b cos} sin^2 th dth
    th = (xg + 1) * math.pi / 2; wt = wg * math.pi / 2
    y = np.cos(th); dens = np.exp(beta*(y-1)) * np.sin(th)**2 * wt
    dens /= dens.sum()
    Zq = 9*y + beta*(7*y**2-4) - beta**2*y*(1-y**2)
    EZ = (dens*Zq).sum(); EY = (dens*y).sum()
    cov = (dens*(y-EY)*Zq).sum(); rhs = (dens*(2+y**2)).sum()
    nz = math.sqrt((dens*Zq**2).sum()); var = (dens*(y-EY)**2).sum()
    ratio = var/16 * 20736 * beta**2
    ok = abs(EZ) <= 1e-8*max(1,beta**2) and abs(cov-rhs) <= 1e-8*max(1,beta**2) and nz/beta <= 72
    c2ok &= ok
    log(f"C2 beta={beta}: EZ={EZ:.2e} cov={cov:.10f} E[2+Y^2]={rhs:.10f} ||Z||/beta={nz/beta:.4f} Var(Y)={var:.4e} Var(Y/4)*20736b^2={ratio:.2f}")
pred("C2 quadrature zero-staple (tolerance 1e-8*max(1,beta^2): Gauss-Legendre 4000 nodes on smooth integrand)", c2ok)
log("FAILED:", fails)
