"""revcheck.py -- checks of the revision of paper/ (worker p6-rev, T35).

Usage: python3 revcheck.py RESULTFILE PAPERDIR ORIGDIR CLAYTXT BUILDDIR
RESULTFILE is opened with mode "x" (never overwritten); BUILDDIR must not exist (fresh compile).

PREDICATES (fixed before the first run):
 P1  control: | -ln tanh 1 - 0.272341 | <= 5e-7.  Tolerance: half a unit of the 6th decimal.
 P2  vortex numbers printed in sec_negative.tex: from the table neg:tab-vort rows SU(2),
     d = F4 - F2 and e = sqrt(e2^2 + e4^2) at beta = 1.8 and 2.4 equal the printed
     -0.20+-0.47 and -0.25+-1.04 within 0.005 (2-decimal printing), and d < 0 at both (predicted sign),
     and |d| < e at both ("not resolved").  For-all over 2 cases; report how many qualify.
 P3  curvature sample count: sum of the explicit per-row counts of periodic rows of neg:tab-curv
     ("8 each" counts 8 per beta listed, "4 each" likewise, "$2$" counts 2) plus 20 for the program-2
     rows marked "not recorded" equals 56; program 1 gives 32 and program 2 gives 24.
 P4  usc family nu_beta = delta_{e^-1} + max(0,beta-1) * 2 * 1_[1/2,1) dx:
     (a) closed form a_n(beta) = e^-n + max(0,beta-1)*2(1-2^{-n-1})/(n+1) agrees with a midpoint quadrature
         (200000 nodes) to 1e-8 relative for n in {0,1,2,10,50}, beta in {0.5,1,1.5,3}.  Tolerance: midpoint
         error ~ h^2 n^2 / 24 <= 3e-9 for n = 50, h = 2.5e-6; 1e-8 leaves margin.
     (b) for all n in {0,2,10,50}: max |a_n(b+h)-a_n(b)| over a grid of step h=1e-3 on [0.5,1.5] <= 2h.
     (c) -log(max supp) is 1 at beta = 1 and 0 at beta = 1.001.
 P5  compile: pdflatex three times in a fresh copy: every run exits 0; final log has no line starting with "!",
     no "undefined" reference/citation warning, no "multiply defined", and no Overfull hbox wider than 15pt.
     Page count: measured only.
 P6  removed phrases are absent from the revised sources (for all, 14 phrases): see PHRASES below.
 P7  "Consequently $\sup" appears inside the theorem environment thm:main in main.tex.
 P8  the quoted sentence of the official problem statement in main.tex equals, after whitespace and
     math-markup normalization, the text of the Clay PDF page 6 extraction (CLAYTXT).
 P9  measured only: hits of the forbidden-word list (whole words, case-insensitive) with file:line.
 P10 measured only: number of changed lines in sec_proof.tex (Section 4) against ORIGDIR.
 P11 the abstract has exactly 4 sentences (split at '. ' followed by an upper-case letter, outside math).
"""
import sys, os, re, math, shutil, subprocess, difflib

res, paper, orig, claytxt, build = sys.argv[1:6]
out = open(res, "x")
met = failed = measured = 0
def log(s):
    print(s); out.write(s + "\n")
def pred(name, ok, info=""):
    global met, failed
    if ok: met += 1
    else: failed += 1
    log(f"{name}: {'MET' if ok else 'FAILED'}  {info}")
def meas(name, info):
    global measured
    measured += 1; log(f"{name}: MEASURED  {info}")
def rd(f): return open(os.path.join(paper, f)).read()

# P1
v = -math.log(math.tanh(1.0)); c = float(open("control.txt").read().strip())
pred("P1", abs(v - c) <= 5e-7, f"-ln tanh 1 = {v:.9f}, control.txt = {c}")

# P2
neg = rd("sec_negative.tex")
rows = {}
for m in re.finditer(r"\\SU\(2\)\$ & \$([\d.]+)\$ & \$([-\d.]+)\\pm([\d.]+)\$ & \$([-\d.]+)\\pm([\d.]+)\$ & \$([-\d.]+)\\pm([\d.]+)\$", neg):
    b = m.group(1); vals = list(map(float, m.groups()[1:])); rows[b] = vals
printed = {"1.8": (-0.20, 0.47), "2.4": (-0.25, 1.04)}
q = 0; ok2 = True
for b, (pd, pe) in printed.items():
    if b not in rows: ok2 = False; log(f"P2 row beta={b} not found"); continue
    q += 1
    F2, e2, F3, e3, F4, e4 = rows[b]
    d = F4 - F2; e = math.hypot(e2, e4)
    good = abs(d - pd) <= 0.005 and abs(e - pe) <= 0.005 and d < 0 and abs(d) < e
    ok2 &= good
    log(f"P2 beta={b}: F4-F2 = {d:+.4f} +- {e:.4f} (printed {pd:+.2f} +- {pe:.2f}) ok={good}")
pred("P2", ok2 and q == 2, f"cases qualifying {q} of 2; also printed in text: {'-0.20\\pm0.47' in neg and '-0.25\\pm1.04' in neg}")

# P3
a = neg.index(r"\label{neg:obs-curv}"); tab = neg[neg.index(r"\begin{tabular}{@{}lllll@{}}"):neg.index(r"\label{neg:tab-curv}")]
p1 = p2 = 0; notrec = 0
for line in tab.split("\n"):
    if "periodic" not in line or "&" not in line: continue  # run1 defect: caption line matched
    cells = [x.strip() for x in line.split("&")]
    prog, betas, cnt = cells[0], cells[2], cells[3]
    nb = len(re.findall(r"\$\d+\$", betas))
    if "not recorded" in cnt: notrec += 1; continue
    m = re.match(r"\$(\d+)\$( each)?", cnt); k = int(m.group(1)) * (nb if m.group(2) else 1)
    if prog == "1": p1 += k
    else: p2 += k
p2 += 20 if notrec == 5 else 0
pred("P3", p1 == 32 and p2 == 24 and p1 + p2 == 56 and "$56$ of $56$" in neg, f"program1={p1}, program2={p2} (incl. 20 for {notrec} not-recorded rows), total={p1+p2}")

# P4
def an(beta, n): return math.exp(-n) + max(0.0, beta - 1) * 2 * (1 - 2.0 ** (-n - 1)) / (n + 1)
def an_quad(beta, n, N=200000):
    h = 0.5 / N; s = sum(((0.5 + (i + 0.5) * h) ** n) for i in range(N)) * h * 2
    return math.exp(-n) + max(0.0, beta - 1) * s
worst = 0
for beta in (0.5, 1.0, 1.5, 3.0):
    for n in (0, 1, 2, 10, 50):
        x, y = an(beta, n), an_quad(beta, n); worst = max(worst, abs(x - y) / abs(x))
okb = True; h = 1e-3; grid = [0.5 + i * h for i in range(1001)]
for n in (0, 2, 10, 50):
    mx = max(abs(an(grid[i + 1], n) - an(grid[i], n)) for i in range(1000)); okb &= mx <= 2 * h
def m_of(beta): return -math.log(1.0 if beta > 1 else math.exp(-1))
okc = abs(m_of(1.0) - 1) < 1e-15 and m_of(1.001) == 0.0
pred("P4", worst <= 1e-8 and okb and okc, f"max rel diff closed form vs quadrature {worst:.2e}; continuity {okb}; jump {okc}")

# P5
shutil.copytree(paper, build)
codes = []
for i in range(3):
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "main.tex"], cwd=build, capture_output=True, text=True, timeout=200)
    codes.append(r.returncode)
lg = open(os.path.join(build, "main.log"), errors="replace").read()
errs = [l for l in lg.split("\n") if l.startswith("!")]
undef = len(re.findall(r"undefined", lg)); mult = len(re.findall(r"multiply defined", lg))
over = [float(x) for x in re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\)", lg)]
pages = re.search(r"Output written on main.pdf \((\d+) pages", lg)
pred("P5", codes == [0, 0, 0] and not errs and undef == 0 and mult == 0 and all(o <= 15 for o in over),
     f"exit codes {codes}; errors {len(errs)}; undefined {undef}; multiply {mult}; overfull widths {over}")
meas("P5-pages", f"pages = {pages.group(1) if pages else '?'}")

# P6
allsrc = {f: rd(f) for f in os.listdir(paper) if f.endswith(".tex")}
PHRASES = ["holds, with the same proof", "Both hold for $\\U(1)$", "has had the corresponding review",
           "to be filled after the review", "a claimed\nstep", "(not checked)", "standing assumption of the paper",
           "F_4-F_3", "the wrong sign", "director's ledger", "s2\\_power", "We prove that it does.",
           "gap at every coupling", "No inequality of any kind is known"]
hits = [(p, f) for p in PHRASES for f, s in allsrc.items() if p in s or p.replace("\n", " ") in s]
pred("P6", not hits, f"14 phrases checked; hits: {hits}")

# P7
mt = allsrc["main.tex"]; th = mt[mt.index(r"\begin{theorem}\label{thm:main}"):mt.index(r"\end{theorem}")]
pred("P7", r"Consequently $\sup" in th)

# P8
qm = re.search(r"asks: ``(.*?)''", mt, re.S); quote = qm.group(1) if qm else ""
def norm(s):
    s = s.replace("$G$", "G").replace(r"$\R^4$", "R4").replace(r"$\Delta>0$", "∆ > 0").replace("--", "–")
    return re.sub(r"\s+", " ", s).strip()
clay = re.sub(r"\s+", " ", open(claytxt).read())
pred("P8", bool(quote) and norm(quote) in clay, f"quote normalized: {norm(quote)!r}")

# P9
words = ["verified", "reviewed", "establishes", "clearly", "obviously", "novel", "remarkable", "Director", "Z4", "A4", "B4", "C4", "G4"]
hl = []
for f, s in sorted(allsrc.items()):
    for i, line in enumerate(s.split("\n"), 1):
        for w in words:
            if re.search(r"(?<![A-Za-z0-9])" + w + r"(?![A-Za-z0-9])", line, re.I): hl.append(f"{f}:{i}:{w}")
meas("P9", f"{len(hl)} hits: {hl}")

# P10
a_ = open(os.path.join(orig, "sec_proof.tex")).read().split("\n"); b_ = allsrc["sec_proof.tex"].split("\n")
ch = [l for l in difflib.unified_diff(a_, b_, lineterm="", n=0) if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))]
meas("P10", f"sec_proof.tex changed lines (+/-): {len(ch)}")

# P11
ab = mt[mt.index(r"\begin{abstract}") + 16:mt.index(r"\end{abstract}")]
ab_nomath = re.sub(r"\$[^$]*\$", "X", ab)
sents = [s for s in re.split(r"(?<=\.)\s+(?=[A-Z])", ab_nomath.strip()) if s]
pred("P11", len(sents) == 4, f"{len(sents)} sentences")

log(f"COUNTS: met {met}, failed {failed}, measured only {measured}")
out.close()
sys.exit(0 if failed == 0 else 1)
