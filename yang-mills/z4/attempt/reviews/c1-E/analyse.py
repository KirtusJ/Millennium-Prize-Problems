"""analyse.py -- worker c1-E (T6). Evaluates predicates P2a, P2a', P2b, P2c (stated in
ising_wolff.c header, fixed before the recorded runs) on results/d4v2_*.txt.
Interpolation: linear in K between the two grid points bracketing the target xi2/L (g and its error
interpolated linearly; errors of neighbouring K treated as independent -> conservative-ish, not exact).
If a target is not bracketed for a given L, that case is reported as NOT MEASURABLE and the predicate fails.
Per rule 4 the per-case count of qualifying sizes is printed first.
Output written to results/analysis_v2.txt (mode "x"). Exit 0 always (it reports; predicates are data).
"""
import glob, math
rows = {}
for f in glob.glob("results/d4v2_*.txt"):
    t = open(f).read().split()
    d, L, K = int(t[0]), int(t[1]), float(t[2])
    U, Ue, x, xe, g, ge = map(float, t[8:14]); P0 = t[-1]
    rows.setdefault(L, []).append((K, U, Ue, x, xe, g, ge, P0))
out = []
def interp(L, target):
    r = sorted(rows.get(L, []))
    for a, b in zip(r, r[1:]):
        if (a[3]-target)*(b[3]-target) <= 0 and a[3] != b[3]:
            w = (target-a[3])/(b[3]-a[3])
            g = a[5]+w*(b[5]-a[5]); ge = math.hypot((1-w)*a[6], w*b[6])
            U = a[1]+w*(b[1]-a[1]); Ue = math.hypot((1-w)*a[2], w*b[2])
            return g, ge, U, Ue
    return None
for L in sorted(rows):
    for r in sorted(rows[L]):
        out.append(f"raw L={L} K={r[0]} U4={r[1]:.4f}({r[2]:.4f}) xi/L={r[3]:.4f}({r[4]:.4f}) gR={r[5]:.3f}({r[6]:.3f}) P0={r[7]}")
res = {}
for target, Ls in ((0.25, [6, 8, 12]), (0.5, [6, 8, 12, 16])):
    vals = {L: interp(L, target) for L in Ls}
    q = [L for L in Ls if vals[L] is not None]
    out.append(f"xi/L={target}: sizes bracketed {len(q)} of {len(Ls)}: {q}")
    for L in Ls:
        v = vals[L]
        out.append(f"  L={L}: " + ("NOT MEASURABLE" if v is None else f"gR={v[0]:.3f}+-{v[1]:.3f}  U4={v[2]:.4f}+-{v[3]:.4f}"))
    ok = len(q) == len(Ls)
    steps = []
    for a, b in zip(Ls, Ls[1:]):
        if vals[a] and vals[b]:
            s = vals[b][0] <= vals[a][0] + 2*math.hypot(vals[a][1], vals[b][1]); steps.append(s)
            out.append(f"  step {a}->{b}: non-increasing within 2 sigma: {s}")
    res[target] = (ok and all(steps), vals)
out.append(f"P2a  (xi/L=0.25, non-increasing L=6,8,12): {'MET' if res[0.25][0] else 'FAILED'}")
out.append(f"P2a' (xi/L=0.5, non-increasing L=6,8,12,16): {'MET' if res[0.5][0] else 'FAILED'}")
v = res[0.25][1].get(12)
out.append(f"P2b  gR(12,0.25) > 5 sigma: {'MET' if v and v[0] > 5*v[1] else 'FAILED'}" + ("" if v else " (not measurable)"))
a, b = res[0.5][1].get(6), res[0.5][1].get(16)
out.append(f"P2c  gR(16,0.5) < gR(6,0.5) by > 2 sigma: {'MET' if a and b and a[0]-b[0] > 2*math.hypot(a[1], b[1]) else 'FAILED'}")
txt = "\n".join(out)
print(txt)
with open("results/analysis_v2.txt", "x") as fh:
    fh.write(txt+"\n")
