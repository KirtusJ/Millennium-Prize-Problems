"""SU(2) single-rotor ground state in the character basis.

H/kappa: diag n(n+2)+g, offdiag -g/2, n = 0..M-1.

PREDICATES (written before the first run).
Basis of expectations: for g >> 1 the ground state is localized near U = 1,
1 - x ~ psi^2/2 (psi = class angle on unit S^3), so H ~ 3D harmonic oscillator
-Lap + (g/2) psi^2, omega = sqrt(2g). Hence E0 ~ 3*sqrt(g/2) = 2.1213*sqrt(g),
angular width psi ~ g^(-1/4), conjugate spread in n ~ g^(1/4).
 P1 truncation: |E0(M) - E0(2M)| < 1e-12*max(1,|E0|) and max|p_n(M)-p_n(2M)| < 1e-12
    for every g.  Tolerance: as requested by the task (double precision floor).
 P2 E0/sqrt(g) at g=1e6 within 1% of 3/sqrt(2).  Tolerance: leading correction is
    O(1) (constant shift) -> relative O(1/sqrt g)=1e-3 at 1e6; 1% gives 10x margin.
 P3 slope(<n>+1) = 0.25 +- 0.05.  Tolerance: corrections to scaling ~ g^(-1/4)
    (~0.3 at g=1e2, 0.1 at 1e4) affect the local slope at the ~0.05 level.
 P4 slope(N_q+1) = 0.25 +- 0.08 for q=0.9, 0.99.  Extra 0.03 for integer
    discreteness of N_q (N ~ 5-30 over the fit range).
 P5 slope(Dim_q) = 0.75 +- 0.2.  Dim ~ N^3/3 so slope ~3x P4 tolerance (~0.24),
    taken as 0.2 (plus subleading N^2 terms bias it upward at small N).
 P6 slope of S_tw vs log g = 0.75 +- 0.1.  S_tw ~ log(N^3)+const -> 3*(1/4);
    same correction-to-scaling argument as P3, tripled to ~0.1-0.15, take 0.1.
 P7 E0/sqrt(g) monotone approach: at g=1e4 within 3% of 3/sqrt(2).
    Tolerance: O(1)/sqrt(g)*few relative ~ 1e-2 times a few.
"""
import os
import numpy as np

def ground(g, M):
    n = np.arange(M)
    H = np.diag(n * (n + 2.0) + g) + np.diag(np.full(M - 1, -g / 2), 1) + np.diag(np.full(M - 1, -g / 2), -1)
    w, v = np.linalg.eigh(H)
    a = v[:, 0]
    return w[0], a * a

def stats(g, M=400):
    E, p = ground(g, M)
    E2, p2 = ground(g, 2 * M)
    trunc = max(abs(E - E2) / max(1, abs(E)), np.max(np.abs(p - p2[:M])), np.sum(p2[M:]))
    n = np.arange(M)
    c = np.cumsum(p)
    out = {"g": g, "E0s": E / np.sqrt(g), "nbar": float(np.dot(n, p)), "trunc": trunc}
    for q in (0.9, 0.99):
        N = int(np.argmax(c >= q))
        out[f"N{q}"] = N
        out[f"D{q}"] = int(np.sum((n[:N + 1] + 1) ** 2))
    pp = p[p > 0]
    nn = n[p > 0]
    out["S"] = float(-np.sum(pp * np.log(pp)) + np.sum(pp * np.log((nn + 1.0) ** 2)))
    return out

gs = list(np.logspace(0, 4, 17)) + [1e5, 1e6]
rows = [stats(g) for g in gs]
fit = [r for r in rows if 1e2 - 1e-9 <= r["g"] <= 1e4 + 1e-6]
lg = np.log([r["g"] for r in fit])
def slope(y):
    return np.polyfit(lg, y, 1)[0]
sl = {
    "N0.9+1": slope(np.log([r["N0.9"] + 1 for r in fit])),
    "N0.99+1": slope(np.log([r["N0.99"] + 1 for r in fit])),
    "Dim0.9": slope(np.log([r["D0.9"] for r in fit])),
    "Dim0.99": slope(np.log([r["D0.99"] for r in fit])),
    "<n>+1": slope(np.log([r["nbar"] + 1 for r in fit])),
    "S_tw": slope([r["S"] for r in fit]),
}
ref = 3 / np.sqrt(2)
r6 = rows[-1]
r4 = [r for r in rows if abs(r["g"] - 1e4) < 1e-6][0]
preds = [
    ("P1 truncation 1e-12", max(r["trunc"] for r in rows) < 1e-12),
    ("P2 E0/sqrt(g)@1e6 within 1%", abs(r6["E0s"] / ref - 1) < 0.01),
    ("P3 slope <n>+1 = 0.25+-0.05", abs(sl["<n>+1"] - 0.25) < 0.05),
    ("P4a slope N0.9+1 = 0.25+-0.08", abs(sl["N0.9+1"] - 0.25) < 0.08),
    ("P4b slope N0.99+1 = 0.25+-0.08", abs(sl["N0.99+1"] - 0.25) < 0.08),
    ("P5a slope Dim0.9 = 0.75+-0.2", abs(sl["Dim0.9"] - 0.75) < 0.2),
    ("P5b slope Dim0.99 = 0.75+-0.2", abs(sl["Dim0.99"] - 0.75) < 0.2),
    ("P6 slope S_tw = 0.75+-0.1", abs(sl["S_tw"] - 0.75) < 0.1),
    ("P7 E0/sqrt(g)@1e4 within 3%", abs(r4["E0s"] / ref - 1) < 0.03),
]
L = ["g        N.9 N.99   Dim.9  Dim.99    <n>     E0/sqrtg   S_tw     trunc"]
for r in rows:
    L.append(f"{r['g']:<8.3g} {r['N0.9']:3d} {r['N0.99']:4d} {r['D0.9']:7d} {r['D0.99']:7d} {r['nbar']:8.4f} {r['E0s']:9.6f} {r['S']:8.5f} {r['trunc']:.1e}")
L.append(f"ref 3/sqrt2 = {ref:.6f}")
L.append("slopes (fit g in [1e2,1e4]): " + ", ".join(f"{k}={v:.4f}" for k, v in sl.items()))
for name, ok in preds:
    L.append(f"{'PASS' if ok else 'FAIL'} {name}")
txt = "\n".join(L)
print(txt)
fn = "results_rotor.txt"
k = 2
while os.path.exists(fn):
    fn = f"results_rotor_{k}.txt"; k += 1
with open(fn, "w") as f:
    f.write(txt + "\n")
print("wrote", fn)
