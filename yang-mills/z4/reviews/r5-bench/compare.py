"""P2 second half: lattice C_b(t) (results_bench_1.json, N=64,128) vs child's continuum C(t) (child/results_3.txt,
my own rerun of child/corr.py).

PREDICATES (fixed before first run):
 P2-cont(R,t): |C_128 - C_cont| <= tol, tol = |C_128 - C_64| + 1e-10*C_cont.
   Origin: O(b^2) Richardson => remaining error of C_128 ~ |C_128-C_64|/3; tol is 3x that; 1e-10 is the child's
   declared convergence tolerance (observed 1e-12..6e-11).
 Measured only: Richardson C* = C128 + (C128-C64)/3 vs C_cont (relative deviation); -dlogC/dt at t=0.2 lattice N=128
   vs child.
Exit 0 iff all P2-cont met.
"""
import json, os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
lat = json.load(open(os.path.join(here, "results_bench_1.json")))
txt = open(os.path.join(here, "child", "results_3.txt")).read()
cont = {}
for R, t, C in re.findall(r"R=([0-9.]+)\s+t=([0-9.]+)\s+K=\d+\s+N=\d+\s+C=([0-9.eE+-]+)", txt):
    cont[(float(R), float(t))] = float(C)
rate = {float(R): float(v) for R, v in re.findall(r"R=([0-9.]+)\s+-dlogC/dt at t=0.2 \(analytic[^=]*= ([0-9.]+)", txt)}
lines = []; ok = True; met = failed = meas = 0
for R in (0.1, 0.05):
    for t in (0.05, 0.1, 0.2):
        c128 = lat[f"R={R},N=128"][str(t)][0]; c64 = lat[f"R={R},N=64"][str(t)][0]
        cc = cont[(R, t)]
        tol = abs(c128 - c64) + 1e-10 * cc
        good = abs(c128 - cc) <= tol
        met += good; failed += (not good); ok &= good
        rich = c128 + (c128 - c64) / 3
        meas += 1
        lines.append(f"P2-cont R={R} t={t}: {'MET' if good else 'FAILED'} C128={c128:.10e} Ccont={cc:.10e} |diff|={abs(c128-cc):.3e} tol={tol:.3e}; "
                     f"rel(C128/Ccont-1)={c128/cc-1:+.3e}; Richardson rel={rich/cc-1:+.3e} (measured)")
    l = lat[f"R={R},N=128"]["0.2"]; r_lat = -l[1] / l[0]
    meas += 1
    lines.append(f"measured R={R}: -dlogC/dt(0.2) lattice N=128 {r_lat:.6f}, continuum {rate[R]:.6f}, rel {r_lat/rate[R]-1:+.2e}")
lines.append(f"TALLY: met {met}, failed {failed}, measured only {meas}")
out = "\n".join(lines); print(out)
k = 1
while os.path.exists(os.path.join(here, f"results_compare_{k}.txt")):
    k += 1
open(os.path.join(here, f"results_compare_{k}.txt"), "w").write(out + "\n")
sys.exit(0 if ok else 1)
