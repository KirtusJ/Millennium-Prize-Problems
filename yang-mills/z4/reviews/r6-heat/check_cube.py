"""Z4 challenger r6-heat: numerical check of two SU(2) cube inequalities of B4. Seed 20261123 (numpy).

Predicates fixed BEFORE first run:
 Q1 [wilson-law l.13-21] Small cube 2^3, free boundary, SU(2) defining rep. For the plaquette p = face z=0
    based at o=(0,0,0) with r_p = |1-U_p| (quaternion chord, r_p^2 = 2 - Tr U_p):
    lambda_min(E_C) >= r_p^2/256 (E_C = sum over 12 cube edges ||f(x)-U_xy f(y)||^2, 16x16 matrix).
    Tested per case on 3000 configurations: 1000 Haar, 1000 near-flat (links exp(i eps sigma), eps=0.05),
    1000 with p near-trivial. Tolerance 1e-10 absolute [eigh double precision on 16x16].
    Hypothesis per case (rule 4): all cases qualify (no hypothesis beyond SU(2)); count reported.
 Q2 [rare-cubes l.7-13] Dirichlet cube of m^3 sites (m=3,4,5), all internal links with ||I-U||_op <= 1/m
    (sampled as exp(i theta n.sigma) with theta uniform in [0, 2 arcsin(1/(2m))] so that ||I-U|| = 2 sin(theta/2) <= 1/m):
    lambda_min <= (6 pi^2 + 6)/m^2 in lattice units, Dirichlet edges to outside included. 200 configs per m.
    Tolerance 1e-10.
 Measured only: min over Q1 cases of lambda_min/(r_p^2) (how loose 1/256 is).
"""
import numpy as np, math, os, sys
rng = np.random.default_rng(20261123)
sig = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex)]
def su2_haar():
    q = rng.normal(size=4); q /= np.linalg.norm(q)
    return q[0]*np.eye(2) + 1j*(q[1]*sig[0]+q[2]*sig[1]+q[3]*sig[2])
def su2_angle(theta):
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    return math.cos(theta)*np.eye(2) + 1j*math.sin(theta)*(n[0]*sig[0]+n[1]*sig[1]+n[2]*sig[2])

def build(sites, edges, U, dirichlet_deg=None):
    idx = {s:i for i,s in enumerate(sites)}; N = len(sites)
    M = np.zeros((2*N,2*N), complex)
    for (x,y) in edges:
        i,j = idx[x], idx[y]; u = U[(x,y)]
        M[2*i:2*i+2,2*i:2*i+2] += np.eye(2); M[2*j:2*j+2,2*j:2*j+2] += np.eye(2)
        M[2*i:2*i+2,2*j:2*j+2] -= u; M[2*j:2*j+2,2*i:2*i+2] -= u.conj().T
    if dirichlet_deg is not None:
        for s,dg in dirichlet_deg.items():
            i = idx[s]; M[2*i:2*i+2,2*i:2*i+2] += dg*np.eye(2)
    return M

def cube_edges(m):
    sites = [(a,b,c) for a in range(m) for b in range(m) for c in range(m)]
    E = []
    for s in sites:
        for d in range(3):
            t = list(s); t[d] += 1; t = tuple(t)
            if t[d] < m: E.append((s,t))
    return sites, E

fails, met = [], []
sites, E = cube_edges(2)
o,X,Y,XY = (0,0,0),(1,0,0),(0,1,0),(1,1,0)
worst = 1e9; ok = True; ncase = 0
for mode in range(3):
    for _ in range(1000):
        if mode == 0: U = {e: su2_haar() for e in E}
        elif mode == 1: U = {e: su2_angle(0.05*rng.random()) for e in E}
        else:
            U = {e: su2_haar() for e in E}
            # make plaquette nearly trivial: set U[(Y,XY)] so that holonomy ~ exp(small)
            # holonomy o->X->XY->Y->o : U_oX U_X,XY U_XY,Y U_Y,o with U_yx = U_xy^*
            A = U[(o,X)] @ U[(X,XY)]
            R = su2_angle(0.01*rng.random())
            U[(Y,XY)] = U[(o,Y)].conj().T @ R.conj().T @ A   # then U_p = R
        Up = U[(o,X)] @ U[(X,XY)] @ U[(Y,XY)].conj().T @ U[(o,Y)].conj().T
        rp2 = 2 - np.trace(Up).real
        lam = np.linalg.eigvalsh(build(sites,E,U))[0]
        ncase += 1
        if rp2 > 1e-14: worst = min(worst, lam/rp2)
        if lam < rp2/256 - 1e-10: ok = False
met.append(f"Q1 ({ncase} cases qualify)") if ok else fails.append("Q1")
ok2 = True; info = []
for m in (3,4,5):
    sites_m, E_m = cube_edges(m)
    deg = {s: sum((s[d]==0)+(s[d]==m-1) for d in range(3)) for s in sites_m}
    th = 2*math.asin(1/(2*m))
    mx = 0
    for _ in range(200):
        # angle theta in su2_angle is half rotation: ||I-U|| = 2 sin(theta/2) with U eigenvalues e^{+-i theta}
        U = {e: su2_angle(th*rng.random()) for e in E_m}
        lam = np.linalg.eigvalsh(build(sites_m,E_m,U,deg))[0]
        mx = max(mx, lam*m*m/(6*math.pi**2+6))
        if lam > (6*math.pi**2+6)/m**2 + 1e-10: ok2 = False
    info.append(f"m={m}: max lam/bound={mx:.4f}")
(met if ok2 else fails).append("Q2 (600 cases qualify) " + "; ".join(info))
n = 1
while os.path.exists(f"results_cube_{n}.txt"): n += 1
txt = "met:\n"+"\n".join(met)+"\nfailed:\n"+"\n".join(fails)+f"\nmeasured: min lam/r_p^2 over Q1 = {worst:.5f} (stated floor 1/256={1/256:.5f})\n"
open(f"results_cube_{n}.txt","x").write(txt); print(txt)
sys.exit(1 if fails else 0)
