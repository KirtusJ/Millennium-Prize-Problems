"""prog_a1: zero set / local minima of the conditional action, and the constants of L3 (attack items A1, A2).

Box R=[-N,N]^4 (z=0). Interior sites |x|_inf<N. Lambda' = links with an interior endpoint. T_int = +e0 links
leaving interior sites. Lambda'' = Lambda' \\ T_int (free). P_R = plaquettes containing a link of Lambda'.
Shell links: links with both endpoints on the shell. S_R(U) = sum_{p in P_R} (1 - 1/2 Tr U_p).

PREDICATES (fixed before the first run):
 Q1  lambda := lowest eigenvalue of Q(phi;0) = sum_{p in P_R}|d phi_p|^2 on Lambda'' (one colour):
     |lambda - 0.837722| < 1e-6 for N=1 and |lambda - 0.147122| < 1e-6 for N=2 (author's values; tolerance =
     author's 6 printed decimals).
 Q2  C = D Q^{-1} D^T: every diagonal entry for N=1 equals 7/24 within 1e-12 (float round-off of a 7x7 solve).
 Q3  (zero set, flat shell) For N=1, 400 random Haar starts, each cooled (exact link-wise minimisation) to
     convergence: every run that ends with S < 1e-10 ends at U = 1 on all free links (max class angle < 1e-4).
     Tolerances: 1e-10 / 1e-4 are cooling-convergence levels (S ~ angle^2).
 Q4  (my expectation, not a claim of the target) for N=1, flat shell: no cooled end state has 1e-10 < S < 0.5,
     i.e. every non-global stationary end state found has action >= 0.5.  [measured: the list of distinct end values]
 Q5  (zero set, N=2, flat shell) 4 random starts, cooled for at most 1500 sweeps (time budget: 0.037 s/sweep): all end at S < 1e-8 with max angle < 1e-3, OR any
     end state with S > 1e-8 is reported (measured).  Predicate: no end state with S < 1e-8 and max angle > 1e-3.
 Q6  (center / -1 question) N=1, flat shell: with one free link forced to U_l = -1 (for each of the 7 free links)
     and the others cooled from 50 random starts, the minimum action is > 0.  Measured: the min value.
     Also with a "center flip" at the interior site (all 8 links -> -1, T_int link then violates the gauge):
     reported action S of the configuration with the 7 free links = -1 and T_int = +1 (measured).
 Q7  (eta(delta) proxy) N=1 and delta = 0.03 (the author's admissible delta for lambda(N=1)): forcing one free
     link to class angle delta (random axis, 20 axes x 7 links) and cooling the rest gives min S > 0;
     measured: min S / delta^2.
 Q8  (near-flat shell) N=1: shell links random with class angle <= 0.05 (seed 7); 200 starts cooled; the lowest
     end state has max interior angle <= 0.5 (i.e. lies in the near region of the identity) and every end state
     with S below (lowest + 0.5) has max interior angle <= 0.5.  Tolerance 0.5 = my choice (far from pi).
Seeds fixed (numpy default_rng(12345) unless stated).  Output: a1_results_N{N}.txt opened with mode "x".
Usage: python3 prog_a1.py
"""
import itertools, sys
import numpy as np

def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return np.array([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0])
def qinv(a): return np.array([a[0], -a[1], -a[2], -a[3]])
def angle(q): return float(np.arccos(np.clip(q[0], -1, 1)))
def qexp(v):
    t = np.linalg.norm(v)
    if t < 1e-15: return np.array([1., 0, 0, 0])
    return np.concatenate([[np.cos(t)], np.sin(t)*v/t])
def haar(rng):
    q = rng.normal(size=4); return q/np.linalg.norm(q)

def build(N):
    R = range(-N, N+1)
    sites = list(itertools.product(R, repeat=4))
    S = set(sites)
    inter = lambda x: max(map(abs, x)) < N
    def sh(x, m): y = list(x); y[m] += 1; return tuple(y)
    links = [(x, m) for x in sites for m in range(4) if sh(x, m) in S]
    lid = {l: i for i, l in enumerate(links)}
    lamp = [i for i, (x, m) in enumerate(links) if inter(x) or inter(sh(x, m))]
    tint = set(lid[(x, 0)] for x in sites if inter(x))
    free = [i for i in lamp if i not in tint]
    lamp_set = set(lamp)
    plaq = []
    for x in sites:
        for m in range(4):
            for n in range(m+1, 4):
                a, b, c = sh(x, m), sh(sh(x, m), n), sh(x, n)
                if a in S and b in S and c in S:
                    ls = [(lid[(x, m)], 1), (lid[(a, n)], 1), (lid[(c, m)], -1), (lid[(x, n)], -1)]
                    if any(l in lamp_set for l, _ in ls): plaq.append(ls)
    return links, lamp, tint, free, plaq

def constants(N, free, plaq):
    fi = {l: k for k, l in enumerate(free)}
    D = np.zeros((len(plaq), len(free)))
    for r, ls in enumerate(plaq):
        for l, s in ls:
            if l in fi: D[r, fi[l]] += s
    Q = D.T @ D
    lam = np.linalg.eigvalsh(Q)[0]
    C = D @ np.linalg.solve(Q, D.T)
    return lam, np.diag(C)

class Sys:
    def __init__(self, N, links, free, plaq):
        self.U = np.zeros((len(links), 4)); self.U[:, 0] = 1
        self.free = free; self.plaq = plaq
        self.byl = {l: [] for l in free}
        for p, ls in enumerate(plaq):
            for k, (l, s) in enumerate(ls):
                if l in self.byl: self.byl[l].append((p, k))
    def Up(self, ls):
        q = np.array([1., 0, 0, 0])
        for l, s in ls: q = qmul(q, self.U[l] if s > 0 else qinv(self.U[l]))
        return q
    def action(self): return sum(1 - self.Up(ls)[0] for ls in self.plaq)
    def staple(self, l):
        Y = np.zeros(4)
        for p, k in self.byl[l]:
            ls = self.plaq[p]; s = ls[k][1]
            X = np.array([1., 0, 0, 0])
            for j in range(1, 4):
                l2, s2 = ls[(k+j) % 4]; X = qmul(X, self.U[l2] if s2 > 0 else qinv(self.U[l2]))
            Y += X if s > 0 else qinv(X)
        return Y   # Re Tr-part: sum_p 1/2 Tr U_p = Re(U_l * Y) summed  (Re(q*y) = q . conj(y))
    def cool(self, fixed=(), sweeps=4000, tol=1e-13):
        last = self.action()
        for it in range(sweeps):
            for l in self.free:
                if l in fixed: continue
                Y = self.staple(l); ny = np.linalg.norm(Y)
                if ny > 1e-14: self.U[l] = qinv(Y)/ny
            a = self.action()
            if abs(last - a) < tol: break
            last = a
        return self.action(), it

def main():
    rng = np.random.default_rng(12345)
    for N in (1, 2):
        links, lamp, tint, free, plaq = build(N)
        out = open(f"a1_results_N{N}.txt", "x")
        def w(s): print(s); out.write(s+"\n"); out.flush()
        w(f"N={N} |links|={len(links)} |Lambda'|={len(lamp)} |T_int|={len(tint)} |Lambda''|={len(free)} |P_R|={len(plaq)}")
        lam, cdiag = constants(N, free, plaq)
        ref = {1: 0.837722, 2: 0.147122}[N]
        w(f"Q1 lambda={lam:.8f} author={ref} pass={abs(lam-ref)<1e-6}")
        w(f"   C_pp min={cdiag.min():.12f} max={cdiag.max():.12f} (7/24={7/24:.12f})")
        if N == 1: w(f"Q2 pass={np.max(np.abs(cdiag-7/24))<1e-12}")
        Sy = Sys(N, links, free, plaq)
        if N == 1:
            ends = []
            for r in range(400):
                for l in free: Sy.U[l] = haar(rng)
                a, it = Sy.cool()
                ma = max(angle(Sy.U[l]) for l in free)
                ends.append((a, ma))
            bad3 = [e for e in ends if e[0] < 1e-10 and e[1] >= 1e-4]
            w(f"Q3 runs=400 qualifying(S<1e-10)={sum(e[0]<1e-10 for e in ends)} violations={len(bad3)} pass={len(bad3)==0}")
            vals = sorted(set(round(e[0], 6) for e in ends))
            w(f"   distinct end actions (rounded 1e-6): {vals[:20]}")
            mid = [e for e in ends if 1e-10 < e[0] < 0.5]
            w(f"Q4 end states with 1e-10<S<0.5: {len(mid)} pass={len(mid)==0}")
            # Q6
            mins = []
            for l0 in free:
                best = 1e9
                for r in range(50):
                    for l in free: Sy.U[l] = haar(rng)
                    Sy.U[l0] = np.array([-1., 0, 0, 0])
                    a, _ = Sy.cool(fixed=(l0,)); best = min(best, a)
                mins.append(best)
            w(f"Q6 min action with one free link = -1, per link: {[round(m,6) for m in mins]} pass={min(mins)>0}")
            for l in free: Sy.U[l] = np.array([-1., 0, 0, 0])
            w(f"   centre flip of the 7 free links (T_int link kept = +1): S={Sy.action():.6f}")
            # Q7
            delta = 0.03; mins7 = []
            for l0 in free:
                for r in range(20):
                    ax = rng.normal(size=3); ax /= np.linalg.norm(ax)
                    for l in free: Sy.U[l] = haar(rng)
                    Sy.U[l0] = qexp(delta*ax)
                    a, _ = Sy.cool(fixed=(l0,)); mins7.append(a)
            m7 = min(mins7)
            w(f"Q7 delta={delta} min S={m7:.3e} min S/delta^2={m7/delta**2:.6f} pass={m7>0}")
            # Q8 near-flat shell
            r8 = np.random.default_rng(7)
            shell = [i for i in range(len(links)) if i not in set(lamp)]
            for l in shell:
                ax = r8.normal(size=3); ax /= np.linalg.norm(ax); Sy.U[l] = qexp(0.05*r8.uniform()*ax)
            ends8 = []
            for r in range(200):
                for l in free: Sy.U[l] = haar(rng)
                a, _ = Sy.cool(); ends8.append((a, max(angle(Sy.U[l]) for l in free)))
            lo = min(e[0] for e in ends8)
            low = [e for e in ends8 if e[0] < lo + 0.5]
            w(f"Q8 lowest S={lo:.6e}; end states within lowest+0.5: {len(low)}, max interior angle among them={max(e[1] for e in low):.4f}; pass={all(e[1]<=0.5 for e in low)}")
            w(f"   distinct end actions: {sorted(set(round(e[0],5) for e in ends8))[:20]}")
            for l in shell: Sy.U[l] = np.array([1., 0, 0, 0])
        else:
            ends = []
            for r in range(4):
                for l in free: Sy.U[l] = haar(rng)
                a, it = Sy.cool(sweeps=1500, tol=1e-12)
                ma = max(angle(Sy.U[l]) for l in free)
                ends.append((a, ma, it)); w(f"   start {r}: end S={a:.3e} max angle={ma:.3e} sweeps={it}")
            bad = [e for e in ends if e[0] < 1e-8 and e[1] > 1e-3]
            w(f"Q5 runs=4 qualifying(S<1e-8)={sum(e[0]<1e-8 for e in ends)} violations={len(bad)} pass={len(bad)==0}")
        out.close()

if __name__ == "__main__":
    main()
