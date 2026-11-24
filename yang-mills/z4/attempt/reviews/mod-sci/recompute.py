"""mod-sci recomputation (science + statistics module review of infrared/main.tex, Measurements).
Predicates fixed before the first run (each prints MET/FAILED; failed ones are kept):
 T1 table: each manuscript entry v(e) equals round(record value), round(record se) at the printed digit   [8 entries]
 T2 steps: manuscript 20, 5, 3 per cent equal round(100*(q_n - q_{n+1})/q_n) on the -I background         [3]
 T3 share: face shares of the three -I faces (L4, -I) sum to 0.81 at two decimals                            [1]
 T4 paired: |paired z| > 2.95 (two-sided 1 % point of t with 15 d.f., the jackknife's d.f.) for all 6 steps  [6]
 X1 cross: R_f/R_c recomputed from R_f, R_c equals the printed ratio to 2e-5; se by quadrature on the log
           equals the printed se to 2e-5; ratio + 2 se equals printed bound to 2e-5 (2l held, 4l all)       [2x3]
 X2 cross: max of the two bounds rounds to 0.951                                                            [1]
 X3 cross: 1-R: manuscript 'about 1' and 'about 7' per cent equal round(100(1-R)) at 2l                      [2]
 X4 energy: Var_f/Var_c * R_f/R_c equals E_f/E_c (e2-cross ratio-opt, 2l) to 1e-5; E + 2se < 0.0042 -> 'c >= 0.0042' [2]
 D1 time: -p/(N-p-1) with p = 308, N = 16*1152 rounds to -0.017                                              [1]
Usage: python3 -I recompute.py <reviews dir> <out file>   (out file must not exist)
Tool: CPython 3, standard library only. Inputs are read from the archives in memory; nothing is extracted or executed.
"""
import sys, json, tarfile, re, math
R, OUT = sys.argv[1], sys.argv[2]
out = []; met = failed = 0
def P(name, ok, info):
    global met, failed
    met += ok; failed += (not ok); out.append(f"{name}: {'MET' if ok else 'FAILED'} {info}")
def tget(arc, member):
    with tarfile.open(arc) as t: return t.extractfile(member).read().decode()
def rnd(v, e, nd): return round(v, nd), round(e * 10**nd)
# ---- local quotient (c2-grow)
man = {"G-d0": [(.0208, 5), (.0167, 4), (.0159, 4), (.0154, 4)], "G-clear0": [(.0589, 8), (.0533, 5), (.0510, 4), (.0428, 4)]}
q = {}
for tag in man:
    d = json.loads(tget(f"{R}/c2-grow/results_summaries.tgz", f"results/{tag}/an4.json")); q[tag] = d
    for L, (mv, me) in zip(("L1", "L2", "L3", "L4"), man[tag]):
        v, e = d[L]["held_q"]; rv, re_ = rnd(v, e, 4)
        P(f"T1 {tag} {L}", abs(rv - mv) < 1e-9 and re_ == me, f"record {v:.6f}({e:.6f}) -> {rv:.4f}({re_}) manuscript {mv:.4f}({me}) train {d[L]['train_lambda']:.5f}")
    hs = [d[L]["held_q"][0] for L in ("L1", "L2", "L3", "L4")]
    steps = [100 * (hs[i] - hs[i + 1]) / hs[i] for i in range(3)]
    out.append(f"   {tag} steps per cent {[round(s, 2) for s in steps]}; A4 hot/cold {[(k, round(x['all32'][0], 5), round(x['all32'][1], 5), round(x['z'], 2), x['met']) for k, x in d['A4'].items()]}")
    if tag == "G-d0":
        for s, m in zip(steps, (20, 5, 3)): P("T2 step", round(s) == m, f"{s:.2f} vs {m}")
        fs = d["L4"]["face_share"]; s3 = fs["yz204"] + fs["xy200"] + fs["xy000"]
        P("T3 share", round(s3, 2) == 0.81, f"{s3:.4f}")
    for k, g in d["G1"].items():
        P(f"T4 {tag} {k}", abs(g["paired_z"]) > 2.95, f"paired z {g['paired_z']:.2f} (paired se {g['paired_jack_se']:.2e}); unpaired z {g['z']:.2f}; pre-fixed G1 'stopped falling' met: {g['stopped_falling_met']}")
out.append(f"   contrast clear/-I: L1 {q['G-clear0']['L1']['held_q'][0]/q['G-d0']['L1']['held_q'][0]:.3f}, L4 {q['G-clear0']['L4']['held_q'][0]/q['G-d0']['L4']['held_q'][0]:.3f}")
# ---- cross lattice (f2-cross2)
txt = open(f"{R}/f2-cross2/results_text/cross-eval-2l-frozen-on-4l.txt").read()
line = [l for l in txt.splitlines() if l.startswith("Z:ratio-opt")][0]
nums = [float(x) for x in re.findall(r"-?\d+\.\d+", line)]
h_ratio, h_se, h_bound, e_Rf, e_Rfse, e_Rc, e_Rcse, e_ratio, e_se, e_var, e_bound, mx = nums
a2 = open(f"{R}/f2-cross2/results_text/analysis-2l.txt").read()
l2 = [l for l in a2.splitlines() if l.startswith("Z:ratio-opt")][0]
n2 = [float(x) for x in re.findall(r"-?\d+\.\d+", l2)]
Rf, Rfse, Rc, Rcse, rat, ratse, var2, E2, bnd2, omr, omrse = n2
def chk(lbl, Rf, Rfse, Rc, Rcse, rat, ratse, bnd):
    r = Rf / Rc; se = r * math.hypot(Rfse / Rf, Rcse / Rc); b = rat + 2 * ratse
    P(f"X1 {lbl} ratio", abs(r - rat) < 2e-5, f"{r:.5f} vs {rat:.5f}")
    P(f"X1 {lbl} se", abs(se - ratse) < 2e-5, f"{se:.5f} vs {ratse:.5f}")
    P(f"X1 {lbl} bound", abs(b - bnd) < 2e-5, f"{b:.5f} vs {bnd:.5f}; z below 1 = {(1 - rat) / ratse:.1f}; 1-R_f {1 - Rf:.4f}({Rfse:.4f}) 1-R_c {1 - Rc:.4f}({Rcse:.4f})")
chk("2l held (8+8 chains)", Rf, Rfse, Rc, Rcse, rat, ratse, bnd2)
chk("4l all (16+16 chains)", e_Rf, e_Rfse, e_Rc, e_Rcse, e_ratio, e_se, e_bound)
P("X2 threshold", round(max(bnd2, e_bound), 3) == 0.951, f"max bound {max(bnd2, e_bound):.5f}; 4l bound {e_bound:.5f}")
P("X3 1-R_5", round(100 * (1 - Rc)) == 1, f"2l {100 * (1 - Rc):.2f} per cent; 4l {100 * (1 - e_Rc):.2f} per cent")
P("X3 1-R_10", round(100 * (1 - Rf)) == 7, f"2l {100 * (1 - Rf):.2f} per cent; 4l {100 * (1 - e_Rf):.2f} per cent")
tests = [l for l in a2.splitlines() if re.match(r"^(L|Z|P\d):", l) and len(re.findall(r"-?\d+\.\d+", l)) >= 11]
b = sorted((float(re.findall(r"-?\d+\.\d+", l)[8]), l.split()[0]) for l in tests)
out.append(f"   f2-cross2 2l: {len(tests)} frozen tests; three smallest ratio+2SE: {b[:3]}")
# ---- energy form (e2-cross)
ce = tget(f"{R}/e2-cross/results.tgz", "results/cross-eval.txt")
an = tget(f"{R}/e2-cross/results.tgz", "results/analysis-2l.txt")
ro = [l for l in an.splitlines() if l.startswith("ratio-opt")][0]
v = [float(x) for x in re.findall(r"-?\d+\.?\d*(?:e-?\d+)?", ro)]
Rr, Rrse, E, Ese, V, Vse = v[4], v[5], v[6], v[7], v[8], v[9]
P("X4 E = Var*R", abs(V * Rr - E) < 1e-5, f"Var ratio {V} x R ratio {Rr} = {V * Rr:.6f} vs E ratio {E}")
P("X4 E + 2se", E + 2 * Ese < 0.0042, f"{E + 2 * Ese:.6f} (4l lines: {[l.split('E_f/E_c=')[1] for l in ce.splitlines() if 'ratio-opt' in l]})")
n_e2 = len([l for l in an.splitlines() if "|" in l and "+-" in l])
out.append(f"   e2-cross 2l: {n_e2} frozen tests in the 16-function span")
# ---- time test
p, N = 308, 16 * 1152
P("D1 offset", round(-p / (N - p - 1), 3) == -0.017, f"-p/(N-p-1) = {-p / (N - p - 1):.4f}; p/N = {p / N:.4f}; record R2_train at lag 3: .0165, .0168; held: -.0161(16), -.0189(16)")
for lbl, r2 in (("loc", -0.0133), ("tr", -0.0023)): out.append(f"   time: R2_held({lbl}) + p/(N-p-1) = {r2 + p / (N - p - 1):+.4f} (rough offset-corrected value; not an estimator with a stated error)")
out.append(f"   time: rho difference .0834(56) - .0321(50) = {0.0834 - 0.0321:.4f}({math.hypot(.0056, .0050):.4f}); rho^2 = {0.0834**2:.4f}; 15-mark R2 at +1/-1: .0113(17)/.0052(19), z = {(0.0113 - 0.0052) / math.hypot(.0017, .0019):.2f}")
out.append(f"   repair: Q1 {0.06269 / 0.06246:.4f}  Q4 {0.04891 / 0.04733:.4f}  (z of Q4 above 1: {(1.0335 - 1) / 0.0128:.2f})")
out.append(f"counts: met {met}, failed {failed}")
s = "\n".join(out) + "\n"
open(OUT, "x").write(s); print(s)
