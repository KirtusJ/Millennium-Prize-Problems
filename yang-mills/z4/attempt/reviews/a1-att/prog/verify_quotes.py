"""verify_quotes.py -- checks quotations used in report.md against the fetched texts.
Predicates (fixed before first run):
 P1 (for all quotes): the quote, after whitespace normalisation (all runs of whitespace -> single space,
    strip ligatures fi/fl, and remove spaces adjacent to hyphen line breaks), occurs verbatim in its source file.
 P2 (for all quotes): the quote has at most two sentences (count of '. ' sentence terminators followed by
    uppercase letter, plus final terminator, <= 2). Tolerance: none (exact string match); source of tolerance:
    the brief's two-sentence rule.
Per-case results are reported (rule 4) before the "for all" verdict. No randomness (no seed needed).
Usage: python3 -I verify_quotes.py <quotes.tsv> <srcdir> <outfile>   (outfile opened with mode 'x')
Exit 0 iff all P1 and P2 hold, else 1.
"""
import sys, re, html
qf, src, out = sys.argv[1], sys.argv[2], sys.argv[3]
def norm(s):
    s = html.unescape(s).replace('ﬁ','fi').replace('ﬂ','fl').replace('ﬀ','ff')
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'- ', '-', s)   # hyphenated line breaks
    return s
cache = {}
rows = []; ok_all = True
for line in open(qf, encoding='utf-8'):
    if not line.strip(): continue
    qid, fn, q = line.rstrip('\n').split('\t')
    if fn not in cache:
        cache[fn] = norm(open(f"{src}/{fn}", encoding='utf-8', errors='replace').read())
    p1 = norm(q) in cache[fn]
    nsent = len(re.findall(r'[.!?] +(?=[A-Z])', q.strip())) + 1
    p2 = nsent <= 2
    ok_all &= p1 and p2
    rows.append(f"{qid}\t{fn}\tP1_found={p1}\tP2_sentences={nsent}<=2:{p2}")
n = len(rows); m1 = sum('P1_found=True' in r for r in rows); m2 = sum(':True' in r for r in rows)
with open(out, 'x') as f:
    f.write('\n'.join(rows) + f"\nSUMMARY cases={n} P1_met={m1} P2_met={m2} ALL={'PASS' if ok_all else 'FAIL'}\n")
print(open(out).read())
sys.exit(0 if ok_all else 1)
