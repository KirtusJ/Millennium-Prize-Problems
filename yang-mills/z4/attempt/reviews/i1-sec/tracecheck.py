"""tracecheck.py -- check the trace comments of paper/sec_smallbox.tex against inputs/ (task T99).
Predicates (fixed before the first run):
 T1 (for all cited (file, line) pairs): the file exists in inputs/ and the line number is <= its length.
 T2 (for all table rows and lines carrying decimal numbers with >= 3 decimals, followed by a trace comment
     on the same source line): every such number (as printed, stripped of $ and spaces) occurs, as a
     substring, in at least one cited line or cited range of the same comment, allowing the cited
     file's Unicode text. Tolerance: exact string match (no rounding allowed), because the brief
     requires numbers to be traceable as printed. Lines whose comment is on the following line are
     handled by attaching the next comment line.
Exit code = number of failures. Output opened with mode "x".
"""
import re, sys, os
sec = open("paper/sec_smallbox.tex").read().splitlines()
files = {f: open(os.path.join("inputs", f)).read().splitlines() for f in os.listdir("inputs")}
out = open(sys.argv[1], "x")
fails = 0; npairs = 0; nnum = 0; qual = 0
cite_re = re.compile(r"([A-Za-z0-9_]+\.md)((?:\s*l\.\d+(?:-\d+)?,?)+)")
def cited(comment):
    res = []
    for m in cite_re.finditer(comment):
        f = m.group(1)
        for a, b in re.findall(r"l\.(\d+)(?:-(\d+))?", m.group(2)):
            res.append((f, int(a), int(b or a)))
    return res
for i, line in enumerate(sec):
    if "%" not in line: continue
    body, _, com = line.partition("%")
    if body.endswith("\\"): continue
    cs = cited(com)
    for f, a, b in cs:
        npairs += 1
        ok = f in files and b <= len(files[f])
        if not ok:
            fails += 1; print(f"T1 FAIL line {i+1}: {f} l.{a}-{b}", file=out)
    # numbers: on this line's body, or the previous non-comment line if this is a pure comment
    tgt = body if body.strip() else (sec[i-1] if i > 0 else "")
    nums = re.findall(r"\d+\.\d{3,}", tgt.replace("$", ""))
    for n in nums:
        nnum += 1
        if not cs: continue
        qual += 1
        txt = "\n".join("\n".join(files[f][a-1:b]) for f, a, b in cs if f in files)
        if n not in txt:
            fails += 1; print(f"T2 FAIL line {i+1}: {n} not in {cs}", file=out)
print(f"pairs {npairs}; numbers {nnum}, qualifying (with a citation) {qual}; failures {fails}", file=out)
out.close(); print(open(sys.argv[1]).read()); sys.exit(fails)
