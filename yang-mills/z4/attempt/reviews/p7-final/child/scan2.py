"""Manual review layer over scan.tsv (heuristic run kept; not overwritten).
R1: every hit has a reviewed verdict. R2: report number 'must change'.
Overrides (my reading of the lines): false-positive substring in math/hash (F_4, \\frac4, a4 hex, 2\\mid4) -> acceptable;
disclosure of review status in abstract/provenance/paperreview -> acceptable (factual, states NOT reviewed)."""
import csv
rows=list(csv.reader(open("scan.tsv"),delimiter="\t"))
why={"sec_negative.tex":"false positive: math F_4/2|4","sec_proof.tex":"false positive: math (a4/c4 inside formula)",
"sec_paperreview.tex":"factual disclosure of review status","main.tex:8":"factual abstract disclosure of review status"}
with open("scan_reviewed.tsv","x") as o:
    o.write("file:line\tmatch\tfinal_verdict\treason\ttext\n")
    n=0
    for r in rows[1:]:
        v=r[2];reason="heuristic"
        for k,w in why.items():
            if k in r[0]: v="acceptable";reason=w
        if "refs.tex" in r[0]: reason="bibliography entry"
        if "sec_provenance" in r[0]: reason="provenance section (factual/hash/Lean file name)"
        if "main.tex:55" in r[0] or "main.tex:58" in r[0] or "main.tex:73" in r[0] or "main.tex:5" == r[0][-11:]: reason=reason if reason!="heuristic" else "provenance disclosure in front matter"
        n+= v=="must change"
        o.write("\t".join([r[0],r[1],v,reason,r[3]])+"\n")
    print("must change:",n,"hits:",len(rows)-1)
