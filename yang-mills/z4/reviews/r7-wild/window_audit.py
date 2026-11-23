"""window_audit.py -- r7-wild, Z4 wildcard worker.

Question. Z4's trajectory audit (z4/README.md l.143-171) states that A4's plaquette window [L,U],
L = A/16, leaves every fixed physical window iff beta^2 b -> 0 ("the exact condition beta^2 b bounded
below"). A4's own estimates (hamiltonian-variance/README.md l.39: K_e + g u <= B, u = E(1-x_p))
give Var F <= 4 Var x <= 4 E(1-x)^2 <= 8u <= 8B/g, i.e. M0 <= K_F := min(4, 8B/g) (K_F = 4 at g = 0;
this is exactly A4's M_*/kappa). Using M0 <= K_F instead of M0 <= 4 in A4's own extraction
inequality  E <= L + E^2/U + U 1_[L,U](E)  gives
    nu([L', U]) >= w,  L' = A/(4 K_F),  U = 4D/A,  w = A^2/(8D)   (U, w unchanged),
and L'/kappa = 9/(32 K_F (1+B)) is bounded below uniformly in g.

Conventions (A4 = Z4 table): A = 9 kappa/(8(1+B)), D = kappa^2 (6+8 sqrt B)^2,
B = min(g, 17 sqrt g/8 + 3/16). Tree level (Z4 README l.145): kappa_A = 2/(beta b), g = beta^2/2.

PREDICATES (fixed before the first run):
 P1 for all g in grid G (g=0 and 4001 log-spaced points in [1e-6, 1e10]): 0 < L' < U and L' >= L_A4.
    (hypothesis test per case first: count grid points where A^2 <= 16 K_F D, needed for L'<U)
 P2 sup over G of K_F(1+B) <= 43.  Tolerance source: hand bound in report (g<=16: 4(1+B(16))=38.75;
    g>=16: 8*(139/64)*(155/64) = 42.08 < 43). Measured sup reported.
 P3 for all g in G: L'/kappa >= 9/(32*43).
 P4 extraction lemma on random discrete measures (seed 20261123, 100000 measures, 1..8 atoms,
    energies log-uniform in [1e-3,1e3], masses uniform): with K=M0, a=M1, D=M2,
    (A4 form)  nu([a/(4K), 4D/a]) >= a^2/(8D)  and (D4/C4 form) nu([a/(4K), 2D/a]) >= a^2/(2D).
    Tolerance 1e-12 relative (double rounding).
 P5 on beta = b^(-p), p in {0.25,0.5,0.6,0.75,0.9}, b in 10^-2..10^-12: L' at b=1e-12 exceeds L' at
    b=1e-2 for every p (escape whenever beta b -> 0); L_A4 at 1e-12 is BELOW its value at 1e-2 for
    p in {0.6,0.75,0.9} (A4's endpoint does not escape there).
 P6 on beta = 1/b (beta b = 1): max/min of L' over b in 10^-2..10^-12 is <= 2 (L' bounded, so the
    condition for L' is beta b -> 0, not beta^2 b -> 0).
 P7 (Z4-claim check) "L bounded forces beta^2 b bounded below" holds for L_A4 but FAILS for L':
    on beta=1/b^0.75, beta^2 b = b^-0.5 -> inf is not the issue; instead test beta = b^-0.4:
    beta^2 b = b^0.2 -> 0 and L' -> inf (consistent); and beta = 1/b: L' bounded while beta b = 1.
    Predicate: exists a trajectory with L' bounded and beta b bounded (p=1) -- same as P6, recorded
    as the refutation of the transfer of Z4's "exact condition" to L'.
Result file results/run1.json is never overwritten (program refuses).
"""
import json, math, os, random, sys

OUT = os.path.join("results", "run1.json")
if os.path.exists(OUT):
    sys.exit("refusing to overwrite " + OUT)
os.makedirs("results", exist_ok=True)

def B(g): return min(g, 17 * math.sqrt(g) / 8 + 3 / 16)
def KF(g): return 4.0 if g == 0 else min(4.0, 8 * B(g) / g)
def AD(kap, g):
    b_ = B(g); return 9 * kap / (8 * (1 + b_)), kap ** 2 * (6 + 8 * math.sqrt(b_)) ** 2

res = {"met": [], "failed": [], "measured": {}}
def pred(name, ok, info):
    (res["met"] if ok else res["failed"]).append({"name": name, "info": info}); print(name, "MET" if ok else "FAILED", info)

G = [0.0] + [10 ** (-6 + 16 * i / 4000) for i in range(4001)]
hyp = sum(1 for g in G if AD(1, g)[0] ** 2 <= 16 * KF(g) * AD(1, g)[1])
ok1 = 0; sup = 0; argsup = None; minratio = 1e9
for g in G:
    A, D = AD(1.0, g); Lp = A / (4 * KF(g)); U = 4 * D / A; La = A / 16
    if 0 < Lp < U and Lp >= La: ok1 += 1
    v = KF(g) * (1 + B(g))
    if v > sup: sup, argsup = v, g
    minratio = min(minratio, Lp)
res["measured"]["hypothesis_A2_le_16KD"] = f"{hyp}/{len(G)}"
pred("P1", ok1 == len(G), f"{ok1}/{len(G)} grid points")
res["measured"]["sup_KF_1pB"] = [sup, argsup]
pred("P2", sup <= 43, f"sup={sup:.6f} at g={argsup:.6g}")
pred("P3", minratio >= 9 / (32 * 43), f"min L'/kappa={minratio:.6g} vs {9/(32*43):.6g}")

rng = random.Random(20261123); bad4 = bad2 = 0; worst = 1e9
for _ in range(100000):
    n = rng.randint(1, 8)
    E = [10 ** rng.uniform(-3, 3) for _ in range(n)]; m = [rng.random() for _ in range(n)]
    K = sum(m); a = sum(mi * e for mi, e in zip(m, E)); D = sum(mi * e * e for mi, e in zip(m, E))
    l = a / (4 * K)
    w4 = sum(mi for mi, e in zip(m, E) if l <= e <= 4 * D / a)
    w2 = sum(mi for mi, e in zip(m, E) if l <= e <= 2 * D / a)
    if w4 < a * a / (8 * D) * (1 - 1e-12): bad4 += 1
    if w2 < a * a / (2 * D) * (1 - 1e-12): bad2 += 1
    worst = min(worst, w2 / (a * a / (2 * D)))
pred("P4", bad4 == 0 and bad2 == 0, f"violations A4-form {bad4}, D4-form {bad2}; min ratio D4-form {worst:.4f}")

bs = [10 ** -k for k in range(2, 13)]
traj = {}
def ends(beta, b):
    kap = 2 / (beta * b); g = beta ** 2 / 2; A, D = AD(kap, g)
    return A / (4 * KF(g)), A / 16, 4 * D / A, A * A / (8 * D)
for p in [0.25, 0.5, 0.6, 0.75, 0.9, 1.0]:
    traj[str(p)] = [[b, *ends(b ** -p, b)] for b in bs]
res["measured"]["trajectories[b,Lprime,L_A4,U,w]"] = traj
okL = all(traj[str(p)][-1][1] > traj[str(p)][0][1] for p in [0.25, 0.5, 0.6, 0.75, 0.9])
okA = all(traj[str(p)][-1][2] < traj[str(p)][0][2] for p in [0.6, 0.75, 0.9])
pred("P5", okL and okA, f"L' escapes all p<1: {okL}; L_A4 shrinks for p>1/2: {okA}")
Lp1 = [r[1] for r in traj["1.0"]]
pred("P6/P7", max(Lp1) / min(Lp1) <= 2, f"beta=1/b: L' in [{min(Lp1):.4g},{max(Lp1):.4g}]")

with open(OUT, "w") as f: json.dump(res, f, indent=1)
print("counts met,failed:", len(res["met"]), len(res["failed"]))
sys.exit(0 if not res["failed"] else 1)
