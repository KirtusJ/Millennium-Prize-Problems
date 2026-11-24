"""QA reproduction of the f2-cross2 frozen test Z:ratio-opt from the deposited per-chain files alone.

Usage: python3 -I reproduce_f2.py SRC_DIR RESULTS_ROOT OUT_DIR
  SRC_DIR       deposit .../attempt/reviews/f2-cross2/src (analysis2.py, cross_eval2.py), read as text, not modified
  RESULTS_ROOT  directory holding c2/ f2/ c4/ f4b/ (results.tgz unpacked), must end with '/'
  OUT_DIR       fresh directory for the regenerated text outputs (opened create-new) and the JSON vector

The deposited programs hard-code ROOT and one sys.path entry of the worker's directory. This driver executes
their text with exactly two substitutions made in memory (the ROOT assignment; the sys.path.insert line), and
wraps analysis2.ratio_min only to record what it returns. No other line is changed. No Monte Carlo is run.

Predicates (fixed before the run):
  Q1 regenerated cross-eval-2l-frozen-on-4l.txt is byte-identical to the deposited text.
  Q2 regenerated analysis-2l.txt and analysis-4l.txt are byte-identical to the deposited texts.
  Q3 the vector read back from the JSON file gives held R_f/R_c and eval R_f/R_c equal (to the last bit) to the
     values computed in memory, and they print as 0.94092(0.00490) and 0.93574(0.00271).
  Q4 the eight leading standardised coefficients recomputed from the JSON vector equal the deposited printed line.
"""
import sys, os, json, types, hashlib
import numpy as np

src, root, outd = sys.argv[1:4]
assert root.endswith("/")
os.makedirs(outd, exist_ok=False)


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


a_txt = open(os.path.join(src, "analysis2.py")).read()
old_root = 'ROOT = "/home/user/z4-workers/f2-cross2/results/"'
assert a_txt.count(old_root) == 1
A = types.ModuleType("analysis2")
exec(compile(a_txt.replace(old_root, f"ROOT = {root!r}"), "analysis2.py", "exec"), A.__dict__)
sys.modules["analysis2"] = A

captured = []
_orig = A.ratio_min


def _wrapped(*args, **kw):
    r = _orig(*args, **kw)
    captured.append(np.array(r[0], float).copy())
    return r


res = {}
# Q2: analysis-2l and analysis-4l (main() of the deposited program)
for name, (c, f) in (("analysis-2l.txt", ("c2", "f2")), ("analysis-4l.txt", ("c4", "f4b"))):
    sys.argv = ["analysis2.py", c, f, os.path.join(outd, name)]
    A.main()

# Q1: cross_eval2.py
A.ratio_min = _wrapped
c_txt = open(os.path.join(src, "cross_eval2.py")).read()
old_path = 'import sys; sys.path.insert(0, "/home/user/z4-workers/f2-cross2/src")'
assert c_txt.count(old_path) == 1
sys.argv = ["cross_eval2.py", "c2", "f2", "c4", "f4b", os.path.join(outd, "cross-eval-2l-frozen-on-4l.txt")]
ns = {"__name__": "cross_eval2"}
exec(compile(c_txt.replace(old_path, "import sys"), "cross_eval2.py", "exec"), ns)
A.ratio_min = _orig
assert len(captured) == 5 and A.CLASSES[1] == "Z"
vec = captured[1]

for name in ("analysis-2l.txt", "analysis-4l.txt", "cross-eval-2l-frozen-on-4l.txt"):
    res[name] = {"regenerated_sha256": sha(os.path.join(outd, name)),
                 "deposited_sha256": sha(os.path.join(os.path.dirname(root.rstrip("/")), "results", name))
                 if os.path.exists(os.path.join(root, name)) else sha(os.path.join(root, name))}
    res[name]["identical"] = res[name]["regenerated_sha256"] == res[name]["deposited_sha256"]

# the frozen vector, written and read back
C = A.load("c2"); F = A.load("f2"); EC = A.load("c4"); EF = A.load("f4b")
Ct, Ch = A.split(C); Ft, Fh = A.split(F)
Vf, Ef = A.mats(Ft, "Z"); Vc, Ec = A.mats(Ct, "Z")
sd = np.sqrt(np.maximum(np.diag(Vf + Vc) / 2, 0))
z = vec * sd; z = z / np.abs(z).max()
ev = ns["ev"]
h_mem = ev(vec, "Z", Fh, Ch); e_mem = ev(vec, "Z", EF, EC)
doc = {
    "test": "Z:ratio-opt",
    "what": "frozen coefficient vector a (length 54) of the test f = sum_i a_i F_i, class Z (zero spatial momentum, "
            "slice-averaged), in the raw (unstandardised) basis of analysis2.NAMES; selected on TRAIN chains "
            "(i%4 in {0,1}) of c2 (N=5,T=10) and f2 (N=10,T=20) by analysis2.ratio_min, rng seed 239 (second class "
            "in the order L,Z,P0,P1,P2, so the generator has already served class L)",
    "normalisation": "as returned by the program (B @ y with |y|=1 in the reduced basis); R is invariant under scaling",
    "names": list(A.NAMES),
    "coefficients": [float(x) for x in vec],
    "coefficients_hex": [float(x).hex() for x in vec],
    "standardised": {"definition": "z_i = a_i * sqrt((Vf_ii + Vc_ii)/2) on TRAIN, divided by max |z|",
                     "values": [float(x) for x in z]},
    "by_name": {n: {"a": float(a), "z": float(zz)} for n, a, zz in zip(A.NAMES, vec, z)},
}
jp = os.path.join(outd, "frozen_vector_Z_ratio_opt.json")
with open(jp, "x") as fo:
    json.dump(doc, fo, indent=1)
back = np.array(json.load(open(jp))["coefficients"], float)
h = ev(back, "Z", Fh, Ch); e = ev(back, "Z", EF, EC)
top = np.argsort(-np.abs(z))[:8]
lead = ", ".join(f"{A.NAMES[i]} {z[i]:+.2f}" for i in top)
dep_line = [l for l in open(os.path.join(root, "cross-eval-2l-frozen-on-4l.txt")) if "[Z:ratio-opt]" in l][0]
summary = {
    "files": res,
    "json_roundtrip_bit_identical": bool(np.array_equal(back, vec)) and h == h_mem and e == e_mem,
    "held_2l": {"R_f(R_10)": f"{h[0]:.5f}({h[1]:.5f})", "R_c(R_5)": f"{h[2]:.5f}({h[3]:.5f})",
                "ratio": f"{h[4]:.5f}({h[5]:.5f})", "ratio+2SE": f"{h[4]+2*h[5]:.5f}", "Vf/Vc": f"{h[6]:.4f}"},
    "eval_4l": {"R_f(R_10)": f"{e[0]:.5f}({e[1]:.5f})", "R_c(R_5)": f"{e[2]:.5f}({e[3]:.5f})",
                "ratio": f"{e[4]:.5f}({e[5]:.5f})", "ratio+2SE": f"{e[4]+2*e[5]:.5f}", "Vf/Vc": f"{e[6]:.4f}"},
    "leading8": lead,
    "leading8_matches_deposited_line": lead in dep_line,
    "nonzero_coefficients": int(np.count_nonzero(vec)),
    "predicates": {},
}
P = summary["predicates"]
P["Q1"] = res["cross-eval-2l-frozen-on-4l.txt"]["identical"]
P["Q2"] = res["analysis-2l.txt"]["identical"] and res["analysis-4l.txt"]["identical"]
P["Q3"] = summary["json_roundtrip_bit_identical"] and summary["held_2l"]["ratio"] == "0.94092(0.00490)" \
    and summary["eval_4l"]["ratio"] == "0.93574(0.00271)"
P["Q4"] = summary["leading8_matches_deposited_line"]
with open(os.path.join(outd, "qa_summary.json"), "x") as fo:
    json.dump(summary, fo, indent=1)
print(json.dumps(summary, indent=1))
sys.exit(0 if all(P.values()) else 1)
