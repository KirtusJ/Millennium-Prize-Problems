"""T3b (retuned step 0.5/sqrt(beta) after run t3 had 5% acceptance; same predicates P4,P5 as t3). T3. usage: python3 t3.py BETA. Metropolis, psi=0 (all shell links identity), 7 unknown links, 64 parallel chains, seed 8000+int(beta).
Move: q_l -> q_l * exp(i sigma.eps), eps ~ N(0, step^2 I3), step = 1.5/sqrt(beta)... (tuned to give acceptance ~30-60%; acceptance is reported).
Symmetric w.r.t. Haar (eps -> -eps is the inverse move, right-multiplication preserves Haar), so accept with min(1,exp(-beta*dS)).
Observable: beta*(1-cos alpha_p), p=(1,2,+1,+1) = beta*(1 - q_a.q_b). Since shell=identity, cos alpha_p = q_a.q_b exactly.
Burn-in 2000 sweeps; then 20000 sweeps measured every sweep; 20 time blocks x 64 chains = 1280 batch means, SE = std/sqrt(1280).
Predicates (fixed before first run), target T=(3/2)*C_pp = 0.4375 from t1 (C_pp=7/24):
 P4: at beta=1000, |mean-T| <= max(4*SE, 0.05*T).   [5% = expected O(beta^-1/2) bias allowance given in the task]
 P5: relative deviation |mean-T|/T at beta=1000 < that at beta=10.
Tolerance sources: 4 SE = ~99.99% Gaussian band; 5% from task statement."""
import numpy as np, sys
from su2lib import *
beta = float(sys.argv[1]); T = 1.5*7/24
rng = np.random.default_rng(8000+int(beta)); C = 64
nb = [[] for _ in range(8)]   # neighbour link ids (different direction)
for a, b in zip(PA, PB): nb[a].append(b); nb[b].append(a)
assert all(len(n) == 6 for n in nb)
q = np.zeros((8, C, 4)); q[..., 0] = 1
pa = plaq_index(1, 2, 1, 1); la, lb = PA[pa], PB[pa]
step = 0.5/np.sqrt(beta)
acc = 0; tot = 0
def sweep(count):
    global acc, tot
    for l in range(1, 8):
        h = sum(q[n] for n in nb[l])
        eps = rng.normal(size=(C, 3))*step
        qn = qmul(q[l], qexp(eps))
        dS = -((qn-q[l])*h).sum(-1)
        ok = rng.random(C) < np.exp(np.minimum(0, -beta*dS))
        q[l] = np.where(ok[:, None], qn, q[l])
        if count: acc += ok.sum(); tot += C
for _ in range(2000): sweep(False)
NS, NB = 20000, 20
obs = np.zeros((NS, C))
for i in range(NS):
    sweep(True); obs[i] = beta*(1-(q[la]*q[lb]).sum(-1))
bm = obs.reshape(NB, NS//NB, C).mean(1).ravel()
mean = obs.mean(); se = bm.std(ddof=1)/np.sqrt(len(bm))
# lag-1 autocorr of chain-average series as a diagnostic
s = obs.mean(1); s = s-s.mean(); ac1 = (s[1:]*s[:-1]).mean()/s.var()
dev = abs(mean-T)
res = f"beta={beta:g} mean={mean:.6f} SE={se:.6f} target={T:.6f} dev={dev:.6f} reldev={dev/T:.4f} acc={acc/tot:.3f} ac1(chain-avg)={ac1:.3f} within max(4SE,5%T)={dev<=max(4*se,0.05*T)}"
with open(f"out/t3b_beta{int(beta)}.txt", "x") as f: f.write(res+"\n")
print(res)
