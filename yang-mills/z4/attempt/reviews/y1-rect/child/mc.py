"""SU(2) 4D Wilson MC, heatbath (KP / rejection) + overrelaxation, numpy only.
Usage: mc.py L beta nther nmeas seed outfile
PREDICATES (fixed before first run):
 P0 (sanity, beta=0.5, L=4): |W11 - u| < 3*sigma + 1e-3, u=I2/I1 (tol 1e-3 = my allowance for
    O(u^5)~3e-5 strong-coupling corrections and binning error underestimate).
 P1 (hypothesis per case): W12 > 3*sigma_W12 (and >0) at each beta in {0.5,1,2,2.3,3.4}; count qualifying cases.
 P2 (beta=0.5): |W12 - u^2| < 3*sigma + 1e-3 (allowance for higher-order corrections; my expectation).
 P3: W11 monotone increasing in beta; 0<W12<W11 for all beta.
 P4 (update correctness): beta=0.5 hot start and cold start agree within 3 sigma combined (run in check.py).
Errors: blocking, report error at plateau (max over block sizes giving >=32 blocks).
"""
import sys, numpy as np

def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3,
                     a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1,
                     a0*b3+a1*b2-a2*b1+a3*b0], -1)
CONJ = np.array([1., -1, -1, -1])
def dag(a): return a*CONJ

def randsu2(rng, shape):
    q = rng.normal(size=shape+(4,))
    return q/np.linalg.norm(q, axis=-1, keepdims=True)

def sample_a0(rng, alpha):
    """a0 ~ sqrt(1-a0^2) exp(alpha a0), vectorised. alpha array."""
    n = alpha.shape[0]; a0 = np.zeros(n); todo = np.arange(n)
    while todo.size:
        al = alpha[todo]
        # KP
        x = rng.random((4, todo.size)) + 1e-300
        d = -(np.log(x[0]) + np.cos(2*np.pi*x[1])**2*np.log(x[2]))/al
        okkp = (x[3]**2 <= 1 - d/2)
        # plain rejection for small alpha: propose uniform a in[-1,1], accept w.p. sqrt(1-a^2)exp(al(a-1))
        a = 2*rng.random(todo.size)-1
        okr = rng.random(todo.size) <= np.sqrt(1-a*a)*np.exp(al*(a-1))
        small = al < 2.0
        ok = np.where(small, okr, okkp)
        val = np.where(small, a, 1-d)
        a0[todo[ok]] = val[ok]
        todo = todo[~ok]
    return a0

class Lat:
    def __init__(s, L, rng, hot=True):
        s.L, s.rng = L, rng
        sh = (L,)*4
        if hot: s.U = [randsu2(rng, sh) for _ in range(4)]
        else:
            s.U = [np.zeros(sh+(4,)) for _ in range(4)]
            for u in s.U: u[..., 0] = 1
        idx = np.indices(sh)
        s.par = (idx.sum(0) % 2)
    def sh(s, A, mu, n=1):  # A(x+n mu)
        return np.roll(A, -n, axis=mu)
    def staple(s, mu):
        U = s.U; V = 0
        for nu in range(4):
            if nu == mu: continue
            up = qmul(qmul(s.sh(U[nu], mu), dag(s.sh(U[mu], nu))), dag(U[nu]))
            a = s.sh(U[nu], mu); a = np.roll(a, 1, axis=nu)       # U_nu(x+mu-nu)
            b = np.roll(U[mu], 1, axis=nu)                         # U_mu(x-nu)
            c = np.roll(U[nu], 1, axis=nu)                         # U_nu(x-nu)
            dn = qmul(qmul(dag(a), dag(b)), c)
            V = V + up + dn
        return V
    def update(s, mu, beta, over=False):
        for p in (0, 1):
            m = (s.par == p)
            V = s.staple(mu)[m]
            k = np.linalg.norm(V, axis=-1)
            V0 = V/k[:, None]
            U = s.U[mu][m]
            if over:
                # U' = V0^dag U^dag V0^dag  (reflect): keeps Tr(U V) fixed
                new = qmul(qmul(dag(V0), dag(U)), dag(V0))
            else:
                a0 = sample_a0(s.rng, beta*k)
                r = np.sqrt(np.maximum(1-a0*a0, 0))
                v = s.rng.normal(size=(k.size, 3)); v /= np.linalg.norm(v, axis=1, keepdims=True)
                X = np.concatenate([a0[:, None], r[:, None]*v], 1)
                new = qmul(X, dag(V0))
            new /= np.linalg.norm(new, axis=-1, keepdims=True)
            s.U[mu][m] = new
    def sweep(s, beta, nover=2):
        for mu in range(4): s.update(mu, beta)
        for _ in range(nover):
            for mu in range(4): s.update(mu, beta, over=True)
    def obs(s):
        U = s.U; w11 = 0; w12 = 0
        for mu in range(4):
            for nu in range(4):
                if mu == nu: continue
                if mu < nu:
                    P = qmul(qmul(U[mu], s.sh(U[nu], mu)), qmul(dag(s.sh(U[mu], nu)), dag(U[nu])))
                    w11 += P[..., 0].mean()
                # rect: 2 in mu, 1 in nu
                A = qmul(U[mu], s.sh(U[mu], mu))
                B = qmul(s.sh(U[nu], mu, 2), dag(s.sh(U[mu], nu)))   # U_nu(x+2mu) U_mu(x+nu)^dag ... need U_mu(x+mu+nu)^dag too
                B = qmul(s.sh(U[nu], mu, 2), dag(s.sh(s.sh(U[mu], mu), nu)))
                C = qmul(dag(s.sh(U[mu], nu)), dag(U[nu]))
                R = qmul(qmul(A, B), C)
                w12 += R[..., 0].mean()
        return w11/6, w12/12

def block_err(x):
    x = np.asarray(x); best = x.std(ddof=1)/np.sqrt(len(x)); b = 1
    while len(x)//b >= 32:
        n = len(x)//b; y = x[:n*b].reshape(n, b).mean(1)
        best = max(best, y.std(ddof=1)/np.sqrt(n)); b *= 2
    return best

def run(L, beta, nth, nme, seed, hot=True):
    rng = np.random.default_rng(seed)
    lat = Lat(L, rng, hot)
    for _ in range(nth): lat.sweep(beta)
    d = np.empty((nme, 2))
    for i in range(nme):
        lat.sweep(beta); d[i] = lat.obs()
    return d

if __name__ == "__main__":
    L, beta, nth, nme, seed = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    d = run(L, beta, nth, nme, seed)
    out = "L=%d beta=%g nth=%d nme=%d seed=%d W11=%.6f +- %.6f W12=%.6f +- %.6f\n" % (
        L, beta, nth, nme, seed, d[:, 0].mean(), block_err(d[:, 0]), d[:, 1].mean(), block_err(d[:, 1]))
    with open(sys.argv[6], "x") as f: f.write(out)
    print(out, end="")
