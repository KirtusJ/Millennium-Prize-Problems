"""err_const.py -- check the explicit Err bound (tu:L-err-explicit) of the patched Prop tu:L-E13.

Err(x,r_b) := h E_W + Dh B_W + sqrt(beta)(H_Psi r'^2/2 + P_Psi (r'-r_b)) + sqrt(beta)(H_Th r'^2/2 + P_Th (r'-r_b)),
m = |w| + sqrt2 S r_b, r = 2 r_b^2|w| + (r_b+r_b^2)^2, E_W = beta(2mr+r^2), B_W = beta(m+r)^2, r' = arcsin r_b,
Dh = 5 r_b/S^2 (the explicit bound, itself checked in gap_dh.py H3), h = h(S).
PREDICATES (fixed before first run), seed 99, N=10^6 random samples:
  s_- in U[0.01,1], S in U[s_-, sqrt2], |b| in U[0,M], M in U[0.1,20], L in U[0.1,10], beta such that r_b=L/sqrt(beta) in U[1e-8, s_-/8],
  |w| = |b|/sqrt(beta), H's in U[0,100], P_Psi <= Lambda in U[0,3], P_Th <= theta0 in U[0,1]:
  E1  sqrt(beta) m <= M+2L ; E2 sqrt(beta) r <= r_b (M+2L) ; E3 E_W <= 17/8 r_b (M+2L)^2 ; E4 B_W <= 81/64 (M+2L)^2
  E5  arcsin(r)/r <= 1.003 and (arcsin r - r)/r^3 <= 0.17 for r <= 1/8 (grid of 10^5 points)
  E6  Err <= RHS of (tu:L-err-explicit) with h_- = h(s_-)
  tolerance 1e-12 relative (rounding). Output results/err_const.txt (mode "x").
"""
import math, sys, os
import numpy as np

def main():
    out = open(os.path.join("results", "err_const.txt"), "x")
    rng = np.random.default_rng(99)
    N = 10**6
    sm = rng.uniform(0.01, 1, N)
    S = rng.uniform(sm, math.sqrt(2))
    M = rng.uniform(0.1, 20, N); L = rng.uniform(0.1, 10, N)
    b = rng.uniform(0, 1, N) * M
    rb = rng.uniform(1e-8, 1, N) * sm / 8
    beta = (L / rb)**2
    w = b / np.sqrt(beta)
    HP, HT = rng.uniform(0, 100, N), rng.uniform(0, 100, N)
    Lam, th0 = rng.uniform(0, 3, N), rng.uniform(0, 1, N)
    PP, PT = rng.uniform(0, 1, N) * Lam, rng.uniform(0, 1, N) * th0
    h = 1 + np.sqrt(1 + S**2) / S; hm = 1 + np.sqrt(1 + sm**2) / sm
    m = w + math.sqrt(2) * S * rb
    r = 2 * rb**2 * w + (rb + rb**2)**2
    EW = beta * (2 * m * r + r**2); BW = beta * (m + r)**2
    rp = np.arcsin(rb)
    Dh = 5 * rb / S**2
    Err = h * EW + Dh * BW + np.sqrt(beta) * (HP * rp**2 / 2 + PP * (rp - rb)) + np.sqrt(beta) * (HT * rp**2 / 2 + PT * (rp - rb))
    RHS = (L * (M + 2 * L)**2 * (2.2 * hm + 6.4 / sm**2) + L**2 * (0.51 * (HP + HT) + 0.03 * (Lam + th0))) / np.sqrt(beta)
    tol = 1e-12
    res = {}
    res["E1"] = np.sqrt(beta) * m / (M + 2 * L)
    res["E2"] = np.sqrt(beta) * r / (rb * (M + 2 * L))
    res["E3"] = EW / (17 / 8 * rb * (M + 2 * L)**2)
    res["E4"] = BW / (81 / 64 * (M + 2 * L)**2)
    rr = np.linspace(1e-4, 0.125, 100000)
    res["E5a"] = np.arcsin(rr) / rr / 1.003
    res["E5b"] = (np.arcsin(rr) - rr) / rr**3 / 0.17
    res["E6"] = Err / RHS
    fails = []
    for k, v in res.items():
        nf = int(np.sum(v > 1 + tol))
        line = f"{k}: n={v.size} met={v.size - nf} failed={nf} max ratio={v.max():.6f}"
        print(line); out.write(line + "\n")
        if nf: fails.append(k)
    out.write(f"FAILED: {fails}\n"); print("FAILED:", fails)
    out.close()
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
