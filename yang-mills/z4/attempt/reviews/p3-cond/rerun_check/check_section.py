"""check_section.py -- compile and text checks of sec_reduction.tex (p3-cond, T21).

Predicates (fixed before the first run):
 S1 control.txt is exactly the line 0.272341.
 S2 pdflatex run twice on main_test.tex (in a fresh copy dir build_check/) exits 0 both times and the log has no line starting with "!".
 S3 the final log has no "undefined" reference/citation warning.
 S4 the labels thm:reduction, thm:conditional, hyp:A, hyp:B, hyp:C, hyp:H0, hyp:H3, hyp:H4 occur exactly once each,
    each hyp:* label sits inside a hypothesis environment, and every other \\label in the section starts with "red:" or is sec:reduction.
 S5 every \\cite key is in {JW, OS73, OS75, KQR21, OS78, Lu77, GJ, GM82, ADC21}.
 S6 none of the banned words occurs (case-insensitive, whole word): novel, remarkable, "we believe", breakthrough, solve, solves, resolves,
    verified, reviewed, perhaps, possibly, probably, arguably, likely, clearly, obviously, essentially; and no \\footnote.
 S7 section length (pages from label zz:start to zz:end in the aux file, inclusive) is between 8 and 12 (brief's expectation).
 M1 (measured only) total page count of main_test.pdf; number of remark environments; occurrences of the word "first".
"""
import os, re, shutil, subprocess, sys
out = open("check_section.out", "x")
def w(s): print(s); out.write(s + "\n")
res = {}
res["S1"] = open("control.txt").read() == "0.272341\n"; w(f"S1 {res['S1']}")
os.makedirs("build_check", exist_ok=False)
for f in ("preamble.tex", "sec_reduction.tex", "main_test.tex"):
    shutil.copy(f, "build_check/")
codes = []
for _ in range(2):
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "main_test.tex"], cwd="build_check", capture_output=True, text=True)
    codes.append(r.returncode)
log = open("build_check/main_test.log", errors="replace").read()
errs = [l for l in log.splitlines() if l.startswith("!")]
res["S2"] = codes == [0, 0] and not errs; w(f"S2 exit codes {codes}, error lines {len(errs)} -> {res['S2']}")
und = [l for l in log.splitlines() if "undefined" in l.lower()]
res["S3"] = not und; w(f"S3 undefined warnings {len(und)} {und[:3]} -> {res['S3']}")
tex = open("sec_reduction.tex").read()
labels = re.findall(r"\\label\{([^}]*)\}", tex)
req = ["thm:reduction", "thm:conditional", "hyp:A", "hyp:B", "hyp:C", "hyp:H0", "hyp:H3", "hyp:H4"]
ok = all(labels.count(l) == 1 for l in req)
for h in [l for l in req if l.startswith("hyp:")]:
    m = re.search(r"\\begin\{hypothesis\}(\[[^\]]*\])?\\label\{" + re.escape(h) + r"\}", tex)
    ok = ok and m is not None
    if m is None: w(f"S4 {h} not directly inside a hypothesis environment")
others = [l for l in labels if l not in req and l != "sec:reduction" and not l.startswith("red:")]
res["S4"] = ok and not others; w(f"S4 required ok={ok}, stray labels {others} -> {res['S4']}")
keys = set(k.strip() for c in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]*)\}", tex) for k in c.split(","))
allowed = {"JW", "OS73", "OS75", "KQR21", "OS78", "Lu77", "GJ", "GM82", "ADC21"}
res["S5"] = keys <= allowed; w(f"S5 keys used {sorted(keys)} -> {res['S5']}")
banned = ["novel", "remarkable", "we believe", "breakthrough", "solve", "solves", "resolves", "verified", "reviewed",
          "perhaps", "possibly", "probably", "arguably", "likely", "clearly", "obviously", "essentially"]
hits = [b for b in banned if re.search(r"\b" + b + r"\b", tex, re.I)]
fn = "\\footnote" in tex
res["S6"] = not hits and not fn; w(f"S6 banned hits {hits}, footnote {fn} -> {res['S6']}")
aux = open("build_check/main_test.aux").read()
ps = int(re.search(r"\\newlabel\{zz:start\}\{\{[^}]*\}\{(\d+)\}", aux).group(1))
pe = int(re.search(r"\\newlabel\{zz:end\}\{\{[^}]*\}\{(\d+)\}", aux).group(1))
res["S7"] = 8 <= pe - ps + 1 <= 12; w(f"S7 section pages {ps}..{pe} = {pe-ps+1} -> {res['S7']}")
npages = re.search(r"Output written on main_test.pdf \((\d+) pages", log)
w(f"M1 total pages {npages.group(1) if npages else '?'}; remark envs {tex.count('begin{remark}')}; word 'first' {len(re.findall(r'\\bfirst\\b', tex, re.I))}")
met = sum(res.values()); w(f"SUMMARY met={met} failed={len(res)-met} measured_only=1")
out.close(); sys.exit(0 if met == len(res) else 1)
