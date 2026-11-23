"""Word scan of paper/*.tex. Predicates (fixed before first run):
S1: every hit gets a verdict in {acceptable, must change}.
S2: count of 'must change' hits reported (measured only; no pass threshold).
Verdict heuristics (my own, then manually reviewed): acceptable if file is refs.tex,
sec_provenance.tex, or line is LaTeX command/option (a4paper, \\label, \\cite, \\input ...);
else must change. Output scan.tsv opened with mode 'x'."""
import re,glob
words=["verified","reviewed","establishes","clearly","obviously","novel","remarkable","we believe","Director","Z4","A4","B4","C4","D4","G4","Millennium","prize"]
pat=re.compile("|".join(re.escape(w) for w in words),re.I)
with open("scan.tsv","x") as out:
    out.write("file:line\tmatch\tverdict\ttext\n")
    for f in sorted(glob.glob("paper/*.tex")):
        for i,l in enumerate(open(f,encoding="utf8",errors="replace"),1):
            ms=pat.findall(l)
            if not ms: continue
            acc = f.endswith(("refs.tex","sec_provenance.tex")) or bool(re.search(r"a4paper|\\(label|ref|cite|input)\{",l))
            out.write(f"{f}:{i}\t{','.join(ms)}\t{'acceptable' if acc else 'must change'}\t{l.strip()}\n")
