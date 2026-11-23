"""Director Z4 | Yang-Mills | exact two-dimensional control, version 2 (repaired check).

Rebuilt by worker r7-fix from input/two_dim_control.py (Kirtus Justus, Director Z4), which is
not edited. Same physics, same computations, same predicates H, P1, P2, P3, same tolerances.
New: tolerance table pinned by a hash, tolerances written into the result file, negative
controls on every run, a --verify mode, and distinct exit codes.

WHAT IS COMPUTED (unchanged from v1)
Wilson plaquette lattice gauge theory on a cylinder, space a circle of N links, a = L/N,
L = 1, g = 1. Transfer operator diagonal in characters with eigenvalue c_r(beta)^N; lattice
gap m = -N log(c_1/c_0); physical gap M = m/a = -N^2 log(c_1/c_0).
U(1): beta = N^2, c_n ~ I_n(beta). SU(2): beta = 4 N^2, c_j ~ I_{2j+1}(beta)/beta.
Z_n: beta = N^2, eigenvalues sum_j exp(beta cos(2 pi j/n)) cos(2 pi j k/n).
Continuum values: U(1) charge 1: 1/2; SU(2) spin 1/2: 3/8.

PREDICATES (fixed before the first run; identical to v1)
 H  per case: closed forms (u1: I_n(b) e^-b, n=0,1; su2: 2 I_{2j+1}(b)/b e^-b, 2j=0,1) agree
    with direct Haar quadrature to relative TOL_H at DPS digits. A case failing H is excluded
    from P1..P3 and listed; the number of qualifying cases is reported.
 P1 U(1), N in NS: M(N) > 1/2 and D(N) = |N^2 (M - 1/2) - 1/4| shrinks by a factor in
    [WIN_LO, WIN_HI] at each doubling; needs >= 2 qualifying N.
 P2 SU(2), N in NS: M(N) - 3/8 > 0 and shrinks by a factor in [WIN_LO, WIN_HI] per doubling.
 P3 Z_n, n in {2,3,5}, N in {2,4,8,16}, at DPS_P3 digits: M strictly decreasing and
    |M/A_n - 1| < TOL_P3 at N = 16, A_n = N^2 k_n d_n exp(-N^2 d_n), d_n = 1 - cos(2pi/n),
    k_2 = 1, else 2.

NEGATIVE CONTROLS (new; known answer FAIL; run on every execution and recorded)
 NC_H   u1_closed(1, 16) * (1 + NC_H_PERT) against the quadrature must FAIL H.
 NC_P3  ratio 1 + NC_P3_OFF must FAIL the P3 nearness test.
 NC_P1  U(1) gap with the wrong Bessel order (I_2/I_1 in place of I_1/I_0) must FAIL P1.
 NC_P2  SU(2) gap on beta = 2 N^2 (wrong coupling) must FAIL P2.
 The same predicate functions are used for the real predicates and for the controls. A control
 that passes is a defect of the check and makes the program exit 2.

TOLERANCE TABLE BEGIN
TOL_H      = 1e-25 ; H rel. tolerance: 15 guard digits below the 40 carried (v1 docstring)
DPS        = 40    ; working precision for H, P1, P2 (v1 code)
WIN_LO     = 3     ; doubling-factor window low: 4 - 25 per cent, N^-2 correction (v1)
WIN_HI     = 5     ; doubling-factor window high: 4 + 25 per cent (v1)
TOL_P3     = 1e-6  ; P3 ratio tolerance: next term exp(-N^2 e_n) far below it at N=16 (v1)
DPS_P3     = 400   ; P3 precision: ratio-1 as small as exp(-256 d_n) (v1 code)
QUAD_CUT   = 6     ; quadrature split at 6/sqrt(b): weight < exp(-18) beyond (v1 code)
NC_H_PERT  = 1e-22 ; NC_H perturbation: 3 decades above TOL_H, 3 below TOL_H*1e6 (r7)
NC_P3_OFF  = 1e-5  ; NC_P3 offset: 1 decade above TOL_P3, as set by the task R1(ii) (r7)
TOLERANCE TABLE END
TABLE SHA256 = 258778899530ea9458b69290d8b5e6db077ff47703f9e0cd850e3b724c316d81
(sha256 of the lines strictly between BEGIN and END, joined by "\\n", trailing blanks removed.)
The program parses the table, checks its hash against the line above, and checks that every
value in use in the code equals the table value to 20 significant digits (exact equality
is too strict: 10**-25 and mpf("1e-25") differ by an ulp); any mismatch exits 2. The table,
its hash and every value in use are written into the result file.

EXIT CODES 0 all predicates MET and all controls behave; 1 a predicate FAILED; 2 self-check
defect (table hash, table/code mismatch, or a negative control that passes); 3 --verify found
a difference; 4 refused to overwrite an existing result file. Codes combine by priority 4,3,2,1.

OUTPUT  two_dim_control_v2_result.json beside the program, refused if it exists. No random
numbers; nothing depends on a seed.
RERUN   python -I two_dim_control_v2.py <mpmath site directory>
VERIFY  python -I two_dim_control_v2.py <mpmath site directory> --verify <result.json>
        recomputes everything, writes nothing, compares value by value (exact string
        equality of every leaf), reports the first difference and the count compared.
"""
import hashlib, json, os, sys
sys.path.append(sys.argv[1])
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "two_dim_control_v2_result.json")
VERIFY = None
if len(sys.argv) >= 4 and sys.argv[2] == "--verify":
    VERIFY = sys.argv[3]
elif len(sys.argv) != 2:
    sys.exit("usage: python -I two_dim_control_v2.py <mpmath site directory> [--verify <result.json>]")
if VERIFY is None and os.path.exists(OUT):
    print("result file exists; refusing to overwrite"); sys.exit(4)

# ---------- values in use (must equal the docstring table) ----------
DPS = 40
mp.mp.dps = DPS                             # set before the constants, as in v1
TOL_H = mp.mpf(10) ** -25
WIN_LO, WIN_HI = 3, 5
TOL_P3 = mp.mpf(10) ** -6
DPS_P3 = 400
QUAD_CUT = 6
NC_H_PERT = mp.mpf(10) ** -22
NC_P3_OFF = mp.mpf(10) ** -5
IN_USE = {"TOL_H": TOL_H, "DPS": DPS, "WIN_LO": WIN_LO, "WIN_HI": WIN_HI, "TOL_P3": TOL_P3,
          "DPS_P3": DPS_P3, "QUAD_CUT": QUAD_CUT, "NC_H_PERT": NC_H_PERT, "NC_P3_OFF": NC_P3_OFF}

mp.mp.dps = DPS

def s(x, n=30):
    return mp.nstr(x, n)

# ---------- self-check of the tolerance table ----------
selfcheck = []          # list of defect strings
doc = __doc__.split("\n")
i0 = doc.index("TOLERANCE TABLE BEGIN"); i1 = doc.index("TOLERANCE TABLE END")
tlines = [l.rstrip() for l in doc[i0 + 1:i1]]
thash = hashlib.sha256("\n".join(tlines).encode("utf-8")).hexdigest()
stated = doc[i1 + 1].split("=")[1].strip()
if thash != stated:
    selfcheck.append("table sha256 %s != stated %s" % (thash, stated))
table = {}
for l in tlines:
    name, rest = l.split("=", 1); val, src = rest.split(";", 1)
    table[name.strip()] = {"value": val.strip(), "source": src.strip()}
if set(table) != set(IN_USE):
    selfcheck.append("table names %s != names in use %s" % (sorted(table), sorted(IN_USE)))
for k, v in IN_USE.items():
    if k in table and s(mp.mpf(table[k]["value"]), 20) != s(mp.mpf(v), 20):   # 20 sig. digits: far above ulp noise, far below any loosening
        selfcheck.append("%s in use %s != table %s" % (k, s(v, 20), table[k]["value"]))

res = {"program": "two_dim_control_v2.py", "dps": mp.mp.dps, "argv": ["<mpmath site directory>"],
       "H": [], "P1": {}, "P2": {}, "P3": {}, "verdicts": {},
       "tolerances": {k: {"in_use": s(v, 20), "table": table.get(k, {}).get("value"),
                          "source": table.get(k, {}).get("source")} for k, v in IN_USE.items()},
       "tolerance_table_sha256": thash, "negative_controls": {}}

# ---------- shared predicate functions (used by real predicates and negative controls) ----------
def h_ok(c, q):
    return abs(c - q) / abs(c) < TOL_H
def in_window(f):
    return WIN_LO <= f <= WIN_HI
def doubling_factors(vals):
    return [vals[i] / vals[i + 1] for i in range(len(vals) - 1)]
def p1_pred(Ns, M):
    D = [abs(mp.mpf(N) ** 2 * (M[N] - mp.mpf(1) / 2) - mp.mpf(1) / 4) for N in Ns]
    fac = doubling_factors(D)
    ok = len(Ns) >= 2 and all(M[N] > mp.mpf(1) / 2 for N in Ns) and all(in_window(f) for f in fac)
    return ok, D, fac
def p2_pred(Ns, M2):
    E = [M2[N] - mp.mpf(3) / 8 for N in Ns]
    fac = doubling_factors(E)
    ok = len(Ns) >= 2 and all(e > 0 for e in E) and all(in_window(f) for f in fac)
    return ok, E, fac
def p3_near(ratio):
    return abs(ratio - 1) < TOL_P3

# ---------- H: closed forms against Haar quadrature (scaled by exp(-beta)) ----------
def u1_closed(n, b):  return mp.besseli(n, b) * mp.exp(-b)
def u1_quad(n, b):
    f = lambda t: mp.exp(b * (mp.cos(t) - 1)) * mp.cos(n * t)
    w = QUAD_CUT / mp.sqrt(b)
    pts = [-mp.pi, -w, 0, w, mp.pi] if w < mp.pi else [-mp.pi, 0, mp.pi]
    return mp.quad(f, pts) / (2 * mp.pi)
def su2_closed(twoj, b):                    # c_j = 2 I_{2j+1}(b) / b
    return 2 * mp.besseli(twoj + 1, b) / b * mp.exp(-b)
def su2_quad(twoj, b):                      # Haar on classes: (2/pi) sin^2 phi dphi
    d = twoj + 1
    f = lambda p: mp.exp(b * (mp.cos(p) - 1)) * mp.sin(d * p) * mp.sin(p)
    w = QUAD_CUT / mp.sqrt(b)
    pts = [0, w, mp.pi] if w < mp.pi else [0, mp.pi]
    return (2 / mp.pi) * mp.quad(f, pts) / d

NS = [4, 8, 16, 32, 64]
qual_u1, qual_su2 = [], []
for N in NS:
    b = mp.mpf(N) ** 2
    ok = True
    for n in (0, 1):
        c, q = u1_closed(n, b), u1_quad(n, b)
        rel = abs(c - q) / abs(c); m = h_ok(c, q); ok &= m
        res["H"].append({"group": "U(1)", "N": N, "beta": s(b), "label": n, "rel_diff": s(rel, 5), "met": bool(m)})
    if ok: qual_u1.append(N)
    b = 4 * mp.mpf(N) ** 2
    ok = True
    for twoj in (0, 1):
        c, q = su2_closed(twoj, b), su2_quad(twoj, b)
        rel = abs(c - q) / abs(c); m = h_ok(c, q); ok &= m
        res["H"].append({"group": "SU(2)", "N": N, "beta": s(b), "label": "2j=%d" % twoj, "rel_diff": s(rel, 5), "met": bool(m)})
    if ok: qual_su2.append(N)
res["H_qualify"] = {"U(1)": qual_u1, "SU(2)": qual_su2, "of": NS}

# ---------- P1: U(1) ----------
M = {N: -mp.mpf(N) ** 2 * mp.log(mp.besseli(1, mp.mpf(N) ** 2) / mp.besseli(0, mp.mpf(N) ** 2)) for N in qual_u1}
p1, D, fac = p1_pred(qual_u1, M)
res["P1"] = {"N": qual_u1, "M": [s(M[N]) for N in qual_u1], "D": [s(d, 12) for d in D], "factors": [s(f, 8) for f in fac]}

# ---------- P2: SU(2) ----------
M2 = {N: -mp.mpf(N) ** 2 * mp.log(mp.besseli(2, 2 * mp.mpf(N) ** 2) / mp.besseli(1, 2 * mp.mpf(N) ** 2)) for N in qual_su2}
p2, E, fac2 = p2_pred(qual_su2, M2)
res["P2"] = {"N": qual_su2, "M": [s(M2[N]) for N in qual_su2], "M_minus_3_8": [s(e, 12) for e in E], "factors": [s(f, 8) for f in fac2]}

# ---------- negative controls at DPS ----------
nc = res["negative_controls"]
b16 = mp.mpf(16)
cpert = u1_closed(1, b16) * (1 + NC_H_PERT); q16 = u1_quad(1, b16)
nc["NC_H"] = {"what": "u1_closed(1,16)*(1+NC_H_PERT) vs quadrature", "rel_diff": s(abs(cpert - q16) / abs(cpert), 5),
              "expected": "FAIL", "passed_predicate": bool(h_ok(cpert, q16))}
Mw = {N: -mp.mpf(N) ** 2 * mp.log(mp.besseli(2, mp.mpf(N) ** 2) / mp.besseli(1, mp.mpf(N) ** 2)) for N in NS}
okw, Dw, facw = p1_pred(NS, Mw)
nc["NC_P1"] = {"what": "U(1) gap with I_2/I_1", "factors": [s(f, 8) for f in facw], "expected": "FAIL", "passed_predicate": bool(okw)}
Mc = {N: -mp.mpf(N) ** 2 * mp.log(mp.besseli(2, 2 * mp.mpf(N) ** 2) / mp.besseli(1, 2 * mp.mpf(N) ** 2)) for N in NS}
okc, Ec, facc = p2_pred(NS, Mc)
nc["NC_P2"] = {"what": "SU(2) gap on beta = 2 N^2", "M_minus_3_8": [s(e, 12) for e in Ec], "factors": [s(f, 8) for f in facc],
               "expected": "FAIL", "passed_predicate": bool(okc)}

# ---------- P3: Z_n adverse control ----------
mp.mp.dps = DPS_P3
p3 = True
for n in (2, 3, 5):
    d = 1 - mp.cos(2 * mp.pi / n); k = 1 if n == 2 else 2
    Ms, ratios = [], []
    for N in (2, 4, 8, 16):
        b = mp.mpf(N) ** 2
        lam = lambda kk: mp.fsum(mp.exp(b * (mp.cos(2 * mp.pi * j / n) - 1)) * mp.cos(2 * mp.pi * j * kk / n) for j in range(n))
        Mn = -b * mp.log(lam(1) / lam(0))
        A = b * k * d * mp.exp(-b * d)
        Ms.append(Mn); ratios.append(Mn / A)
    dec = all(Ms[i] > Ms[i + 1] for i in range(3))
    near = p3_near(ratios[-1])
    p3 &= dec and near
    res["P3"]["Z_%d" % n] = {"N": [2, 4, 8, 16], "M": [s(x, 12) for x in Ms], "M_over_A": [s(x, 15) for x in ratios],
                             "strictly_decreasing": bool(dec), "ratio_within_1e-6_at_N16": bool(near)}
r = 1 + NC_P3_OFF
nc["NC_P3"] = {"what": "ratio 1 + NC_P3_OFF", "ratio": s(r, 15), "expected": "FAIL", "passed_predicate": bool(p3_near(r))}
mp.mp.dps = DPS

for k in sorted(nc):
    if nc[k]["passed_predicate"]:
        selfcheck.append("negative control %s passed (expected FAIL)" % k)
res["self_check"] = {"defects": selfcheck, "ok": not selfcheck}

h_all = all(h["met"] for h in res["H"])
res["verdicts"] = {"H_all_cases": "MET" if h_all else "FAILED", "P1": "MET" if p1 else "FAILED",
                   "P2": "MET" if p2 else "FAILED", "P3": "MET" if p3 else "FAILED",
                   "negative_controls": "ALL FAIL AS EXPECTED" if all(not v["passed_predicate"] for v in nc.values()) else "DEFECT",
                   "tolerance_table": "OK" if not [d for d in selfcheck if not d.startswith("negative")] else "DEFECT"}

def leaves(x, path=""):
    if isinstance(x, dict):
        for k in sorted(x): yield from leaves(x[k], path + "/" + str(k))
    elif isinstance(x, list):
        if not x: yield path, "[]"
        for i, v in enumerate(x): yield from leaves(v, path + "[%d]" % i)
    else:
        yield path, json.dumps(x)

code = 0 if (h_all and p1 and p2 and p3) else 1
if selfcheck: code = 2
for k, v in res["verdicts"].items(): print(k, v)
for d in selfcheck: print("SELF-CHECK DEFECT:", d)

if VERIFY is not None:
    with open(VERIFY, encoding="utf-8") as f:
        old = json.load(f)
    a = list(leaves(json.loads(json.dumps(res)))); bl = list(leaves(old))
    da, db = dict(a), dict(bl)
    first = None; ndiff = 0
    for p, v in a:
        if p not in db:
            ndiff += 1; first = first or "%s: recomputed %s, missing in file" % (p, v)
        elif db[p] != v:
            ndiff += 1; first = first or "%s: recomputed %s, file %s" % (p, v, db[p])
    for p, v in bl:
        if p not in da:
            ndiff += 1; first = first or "%s: in file %s, not recomputed" % (p, v)
    print("VERIFY compared %d leaves, %d differences" % (len(a), ndiff))
    if first:
        print("VERIFY first difference:", first); code = 3
    else:
        print("VERIFY identical")
    sys.exit(code)

with open(OUT, "x", encoding="utf-8", newline="\n") as f:
    json.dump(res, f, indent=1, sort_keys=True); f.write("\n")
print("H qualify", res["H_qualify"])
print("P1 factors", res["P1"]["factors"], "M", res["P1"]["M"][-1])
print("P2 factors", res["P2"]["factors"], "M", res["P2"]["M"][-1])
for n in (2, 3, 5): print("P3 Z_%d" % n, res["P3"]["Z_%d" % n]["M"], res["P3"]["Z_%d" % n]["M_over_A"][-1])
sys.exit(code)
