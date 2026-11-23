"""prog_a8: minimal-box Monte Carlo (attack item A8). Own code; nothing of the author's is used.

Box N=1: one interior site z, its 8 links are sampled (no gauge fixing: the observables are gauge invariant and
fixing T_int is a Haar change of variables), all shell links = 1 (flat boundary). 24 plaquettes in P_R.
Weight exp(-beta * sum_p (1 - 1/2 Tr U_p)) x Haar. Kennedy-Pendleton heatbath, one link at a time.
Observables per configuration: O_bar = mean over the 24 plaquettes of beta(1-cos alpha_p); X = beta*alpha_{p0}^2/3
for the first plaquette p0 (per-colour variance of the rescaled curvature of p0).

PREDICATES (fixed before the first run). C_pp = 7/24 (Dirichlet value for N=1, computed exactly in prog_a1 Q2).
 M1 beta=500: |mean(O_bar) - (3/2) C_pp| <= 4 SE + 0.5/beta.
 M2 beta=50 : |mean(O_bar) - (3/2) C_pp| <= 4 SE + 0.5/beta.
 M3 beta=500: |mean(X) - C_pp| <= 4 SE_X + 0.5/beta.
 (SE: batch means, 100 batches. 4 SE = statistical allowance. 0.5/beta = my own allowance for the O(1/beta)
  corrections of the Laplace limit (Haar Jacobian, cos vs quadratic); it is a guess of the scale, not derived.)
 Measured only: the same at beta=50 for X; integrated autocorrelation not estimated beyond batch means.
Seed: numpy default_rng(2026). Sweeps: 2000 thermalisation + 100000 measured per beta. Output a8_results.txt (mode "x").
Usage: python3 prog_a8.py
"""
import numpy as np, sys
sys.path.insert(0, ".")
from prog_a1 import build, Sys, qmul, qinv

def kp(a, rng):
    while True:
        r1, r2, r3, r4 = 1-rng.random(), rng.random(), 1-rng.random(), rng.random()
        x = -(np.log(r1) + np.cos(2*np.pi*r2)**2*np.log(r3))/a
        if x <= 2 and r4*r4 <= 1 - x/2: return 1 - x

def main():
    rng = np.random.default_rng(2026)
    links, lamp, tint, free, plaq = build(1)
    S = Sys(1, links, lamp, plaq)            # all 8 links at z are updated
    Cpp = 7/24
    out = open("a8_results.txt", "x")
    def w(s): print(s); out.write(s+"\n"); out.flush()
    for beta in (500.0, 50.0):
        for l in lamp: S.U[l] = np.array([1., 0, 0, 0])
        ob, xs = [], []
        for sw in range(102000):
            for l in lamp:
                Y = S.staple(l); ny = np.linalg.norm(Y); yh = Y/ny
                # weight exp(beta*Re(U*Y)) = exp(beta*ny*Re(U*yh)); w := U*yh has density ~ exp(beta*ny*w0)
                w0 = kp(beta*ny, rng)
                v = rng.normal(size=3); v /= np.linalg.norm(v)
                wq = np.concatenate([[w0], np.sqrt(max(0., 1-w0*w0))*v])
                S.U[l] = qmul(wq, qinv(yh))
            if sw >= 2000:
                q0s = np.array([S.Up(ls)[0] for ls in plaq])
                ob.append(beta*np.mean(1-q0s))
                xs.append(beta*np.arccos(np.clip(q0s[0], -1, 1))**2/3)
        def bm(a):
            a = np.array(a).reshape(100, -1).mean(1); return a.mean(), a.std(ddof=1)/10
        m, se = bm(ob); mx, sex = bm(xs)
        tol = 4*se + 0.5/beta; tolx = 4*sex + 0.5/beta
        w(f"beta={beta}: mean O_bar={m:.6f} +- {se:.6f}  target (3/2)C_pp={1.5*Cpp:.6f}  diff={m-1.5*Cpp:+.6f}  tol={tol:.6f}  pass={abs(m-1.5*Cpp)<=tol}")
        w(f"beta={beta}: mean X={mx:.6f} +- {sex:.6f}  target C_pp={Cpp:.6f}  diff={mx-Cpp:+.6f}  tol={tolx:.6f}  pass={abs(mx-Cpp)<=tolx}")
    out.close()

if __name__ == "__main__":
    main()
