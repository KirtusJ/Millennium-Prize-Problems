"""t_pos.py -- step 8 of Theorem S: does site-plane RP alone (H0) give F(t+s) <= e^{-ms} F(t)?
Model: antiferromagnetic Ising chain (time = Z, spins +-1, weight exp(J sum s_t s_{t+1}), J = -0.5), the
simplest reversible chain. Site-reflection RP: <Theta F . F> = sum_x0 p(x0) E[F|x0]^2 >= 0 for any reversible chain.
Transfer matrix K = [[e^J, e^-J],[e^-J, e^J]], eigenvalues e^J+e^-J (vacuum) and e^J-e^-J < 0.
m := -log(|lambda_2|/lambda_1) (H1's definition: -log of the norm of T on Omega-perp).
PREDICATES (fixed before run):
 T1  site RP holds: min eigenvalue of the matrix M_{ab} = <Theta F_a F_b> over the basis of functions of
     (s_0, s_1, s_2) is >= -1e-12 (float tolerance for 8x8 sums of O(1) numbers).
 T2  (expected to FAIL -- this is the defect being exhibited) monotone form of step 8:
     F(t+1) <= e^{-m} F(t) for t = 1..6, with F(t) = <s_0 s_t> (connected; <s>=0), F(t) = 2-point of v = s.
 T3  repaired form |F(t)| <= e^{-m t} F(0) for t = 0..10 (holds for any self-adjoint T, ||T|_perp|| = e^{-m}),
     tolerance 1e-12.
 T4  link RP fails: <Theta_link s . s> = <s_0 s_1> < 0 (link reflection maps s_1 -> s_0).
Output t_pos.out (mode "x").
"""
import itertools, math, numpy as np
J = -0.5
K = np.array([[math.exp(J), math.exp(-J)], [math.exp(-J), math.exp(J)]])
ev = np.linalg.eigvalsh(K); l1, l2 = max(ev), min(ev)
m = -math.log(abs(l2) / l1)
F = lambda t: (l2 / l1) ** t   # <s_0 s_t> for the infinite chain, exact
out = open("t_pos.out", "x")
def w(s): print(s); out.write(s + "\n")
w(f"eigenvalues {l1:.6f} {l2:.6f}; m = {m:.6f}")
# T1: exact site RP on functions of (s0,s1,s2) about site 0: Theta maps s_k -> s_{-k}
vals = [1, -1]
basis = list(itertools.product(vals, repeat=3))  # indicator functions of (s0,s1,s2)
def p_pair(a, b): return K[(a < 0), (b < 0)] / (l1 * 2)  # joint stationary prob of neighbours, p(s)=1/2
# <Theta 1_{(a0,a1,a2)} 1_{(b0,b1,b2)}> = [a0==b0] * P(s0=a0) P(s1=b1|s0) P(s2=b2|s1) P(s_-1=a1|s0) P(s_-2=a2|s_-1)
def cond(x, y): return K[(x < 0), (y < 0)] / l1
M = np.zeros((8, 8))
for i, a in enumerate(basis):
    for j, b in enumerate(basis):
        if a[0] == b[0]:
            M[i, j] = 0.5 * cond(b[0], b[1]) * cond(b[1], b[2]) * cond(a[0], a[1]) * cond(a[1], a[2])
mine = np.linalg.eigvalsh(M).min()
w(f"T1 min eigenvalue of site-RP matrix: {mine:.3e}")
t2 = []
for t in range(1, 7):
    ok = F(t + 1) <= math.exp(-m) * F(t) + 1e-15
    t2.append(ok); w(f"T2 t={t}: F(t)={F(t):+.6f} F(t+1)={F(t+1):+.6f} e^-m F(t)={math.exp(-m)*F(t):+.6f} holds={ok}")
t3 = [abs(F(t)) <= math.exp(-m * t) * F(0) + 1e-12 for t in range(11)]
w(f"T3 per t: {t3}")
w(f"T4 <s0 s1> = {F(1):+.6f}")
r = {"T1": mine >= -1e-12, "T2": all(t2), "T3": all(t3), "T4": F(1) < 0}
w(f"T2 cases holding: {sum(t2)} of {len(t2)}")
for k in r: w(f"PREDICATE {k}: {'MET' if r[k] else 'FAILED'}")
out.close()
