"""check_tables.py  -- predicates fixed BEFORE the first run.

P1 (presence): for each (table, token, file) listed below, the token, after
   normalising typography (U+2212 -> '-', '±' / '+-' -> '+-', '·10' -> 'e'),
   occurs as a substring of the named file normalised the same way.
   Tokens are single numbers or 'value +- err' strings, exactly as the writer printed them.
   Tolerance: exact string identity (same digits, same stated uncertainty).
P2 (absence is a finding, not a crash): a token that is missing is reported ABSENT; exit 0.
   Expectation (mine, before running): all tokens present except those where the
   writer reformatted (e.g. 'L = 16' appended to a four-value list in c1-E).
P3 (derived, tolerance = rounding to printed digits, half unit of last digit):
   a) T1 counts 16+12+4 = 32; union of ranges = [-2.30,-1.12]; challenger total 20+4 = 24.
   b) T2 F4-F3 at beta=2.4 = 1.26, quadrature error 1.05 (to 2 decimals), 1.26/1.05 ~ 1.2.
   c) T3 z_SU2(6)/z_U1(6) = 11.7 (1 decimal).
   d) T6 q, xi, xi(1-q) to printed digits; exponent ln(.86/.53)/ln(1.40/.72) within 0.75 +- 0.05.
   e) T8/T7 none.
P4: for-all statements: 'for all' tokens counted: report n present / n total.
Result file opened with mode 'x'; no randomness (no seed needed).
"""
import math, re, sys

def norm(s):
    s = s.replace("−", "-").replace("±", "+-").replace("·", "").replace(" ", " ")
    s = re.sub(r"\s+", " ", s)
    return s

def load(f):
    return norm(open("src/" + f, encoding="utf8").read())

A = "a3-Acurv.PROOF.md"; AC = "a4-chalcurv.report.md"; AV = "a3-Avort.PROOF.md"; AVR = "a3-Avort.report.md"
AF = "a3-Afs.PROOF.md"; AFR = "a3-Afs.report.md"; W = "a7-wild.report.md"; C = "a3-C.PROOF.md"
M = "MATCHED_MEASUREMENT.md"; L = "A1_LEDGER.md"; E1 = "c1-E.report.md"; HE = "HYPOTHESIS_E.md"; X = "c1-excl.report.md"

T = []
def add(t, f, *toks):
    for k in toks: T.append((t, k, f))

add("T1", A, "-1.60", "-1.88", "-1.53", "-1.58", "-1.17", "-2.30", "0/8", "-6.4, -9.0, -12.2", "4.31", "76/76", "6.6")
add("T1", AC, "-1.46 to -1.79", "-1.39 to -1.96", "-1.12 to -1.52", "-1.12 to -1.93", "-1.55 to -2.04",
    "-1.77, -1.26", "-1.15, -1.67", "-1.67 to -2.40", "+0.16, -0.32, -0.04", "+3, +9.6, +23",
    "k = 2.62, 2.51", "0.38", "-1.62, -1.51", "k = 3.42, c0 = 0.44".replace("c0", "c₀"), "-2.28 vs -2.51 to -2.62", "0/24")
add("T1", L, "-1.1 and -2.3")
add("T2", AV, "0.69 +- 0.24", "-0.26 +- 0.28", "0.49 +- 0.40", "3.06 +- 0.42", "1.55 +- 0.45", "2.81 +- 0.95", "+1.26 +- 1.05")
add("T2", AVR, "0.0774", "0.0041", "0.0061", "3.205", "8.244", "15.84", "+1.26 +- 1.05", "0.0325242683", "0.6912790067")
add("T3", AF, "0.562 +- 0.016", "0.335 +- 0.024", "0.324", "2.12 +- 0.06", "0.553 +- 0.078", "0.422", "8.02 +- 0.40", "0.684 +- 0.068", "0.500", "0.217")
add("T3", AFR, "1.5 to 2.6", "11.7")
add("T4", W, "4 negative, 141 positive, 584 zero", "729", "-0.003086419753", "-0.002892 +- 0.000237", "seed 7", "N=4e7", "27/27")
add("T5", C, "0.963", "0.0373", "3.56, 4.13, 4.46, 4.64, 4.73, 4.78", "6.584, 5.921, 5.580, 5.522, 5.508, 5.505, 5.504", "5.503975", "30.2937")
add("T6", M, "0.3690(30)", "0.2660(20)", "0.1905(8)", "3.751(42)", "1.012(32)", "3.615(60)", "1.166(51)", "3.233(61)", "1.245(51)", "3.74(12)", "1500", "840", "834")
add("T6", L, "0.270, 0.323, 0.385", "0.72, 1.01, 1.40", "0.53, 0.68, 0.86", "ξ^0.75")
add("T7", E1, "0.007+-0.025", "4.023+-0.046", "-0.19+-0.07", "67+-9, 46+-8, 32+-7", "36+-2", "22+-2", "20+-3", "2001..2017", "0.6115(2), 0.6107(3)", "0.6111(5), 0.6098(7)", "0.61069", "2.2")
add("T7", HE, "0.007 +- 0.025", "0.34 +- 1.20", "4.023 +- 0.046", "-0.19 +- 0.07", "0.6115, 0.6107", "0.6111 +- 0.0005", "0.6098 +- 0.0007", "g_R ≈ 2.2".replace("≈", "≈"))
add("T7", E1, "12/3 = 4")
add("T8", X, "1.64", "0.090 +- 0.003", "0.018", "0.6925", "0.7273", "0.630", "0.684", "200 Metropolis", "below 0.002")

src = {}
rows = []
for t, k, f in T:
    src.setdefault(f, load(f))
    kk = norm(k)
    hit = kk in src[f] or kk.replace(" ", "") in src[f].replace(" ", "")
    rows.append((t, k, f, "present" if hit else "ABSENT"))

out = []
for r in rows: out.append(" | ".join(r))
n = len(rows); p = sum(r[3] == "present" for r in rows)
out.append(f"P4 presence: {p}/{n} tokens present (all {n} tested; no sampling)")

# derived
d = []
d.append(("T1 16+12+4", 16 + 12 + 4 == 32))
d.append(("T1 20+4", 20 + 4 == 24))
d.append(("T2 F4-F3", round(2.81 - 1.55, 2) == 1.26 and round(math.hypot(.45, .95), 2) == 1.05 and round(1.26 / 1.05, 1) == 1.2))
d.append(("T3 11.7", round(8.02 / 0.684, 1) == 11.7))
d.append(("T3 1/(2beta)", round(1 / 4.6, 3) == 0.217))
q = [1.012 / 3.751, 1.166 / 3.615, 1.245 / 3.233]
xi = [1 / (3.74 * a) for a in (0.3690, 0.2660, 0.1905)]
d.append(("T6 q", [round(x, 3) for x in q] == [0.270, 0.323, 0.385]))
d.append(("T6 xi", [round(x, 2) for x in xi] == [0.72, 1.01, 1.40]))
v = [x * (1 - y) for x, y in zip(xi, q)]
d.append(("T6 xi(1-q)", [round(x, 2) for x in v] == [0.53, 0.68, 0.86]))
ex = math.log(v[2] / v[0]) / math.log(xi[2] / xi[0])
d.append((f"T6 exponent {ex:.3f}", abs(ex - 0.75) <= 0.05))
for k, ok in d: out.append(f"DERIVED {k}: {'OK' if ok else 'FAIL'}")
with open("results_check_tables.txt", "x") as f:
    f.write("\n".join(out) + "\n")
print("\n".join(o for o in out if "ABSENT" in o or o.startswith(("P4", "DERIVED"))))
