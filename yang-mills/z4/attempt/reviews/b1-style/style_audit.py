"""style_audit.py -- measure format facts of navier-stokes.pdf from its pdftotext -layout output.

Usage: python3 -I style_audit.py <path to ns.txt> <path to ns.pdf> <result file (created with mode 'x')>

Predicates fixed BEFORE the first run (expectations are MY expectations from the brief and a first read):
 P1  the PDF has more than 100 pages (pdfinfo).                                    expect TRUE
 P2  the abstract (text between 'Abstract.' and 'Contents') is exactly 1 sentence.  expect TRUE
 P3  the title (first non-empty line) contains none of: SOLV, MILLENNIUM, PRIZE, CLAY. expect TRUE
 P4  the abstract contains none of: solve, Millennium, prize, Clay, Fefferman.      expect TRUE
 P5  the body text contains the token 'Lean' at least once (the brief says a Lean
     formalization accompanies the paper and asks how it is cited).               expect TRUE (brief)
 P6  the body text contains a statement on AI use: any of ' AI ', 'GPT', 'language model',
     'artificial intelligence', 'Acknowledg'.                                     expect TRUE (brief)
 P7  the word 'Millennium' occurs at least once outside the reference list.        expect TRUE
 P8  FOR ALL TOC sections: page span (next start - start) >= 1. Per-case test first:
     report how many sections qualify.                                            expect TRUE
 P9  the number of numbered references is 22 (as read on the last page).          expect TRUE
Measured only (no predicate): section page spans, counts of Theorem/Proposition/Lemma/Corollary/
 Remark/Definition headers, footnote-like markers, 'Figure N.' captions, 'Table' captions,
 occurrences of hedge words.
Tolerances: none; all predicates are exact string/integer tests. Page numbers come from the
 printed table of contents (its own numbering, page 1 = first page of the PDF).
No randomness is used (seed fixed at 0 for form).
"""
import re, subprocess, sys, random
random.seed(0)
txt_path, pdf_path, out_path = sys.argv[1:4]
T = open(txt_path, encoding="utf8").read()
out = open(out_path, "x", encoding="utf8")
res = {}
def say(s):
    print(s); out.write(s + "\n")

info = subprocess.run(["pdfinfo", pdf_path], capture_output=True, text=True).stdout
pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
res["P1"] = pages > 100; say(f"pages={pages}")

abstract = re.search(r"Abstract\.(.*?)Contents", T, re.S).group(1)
abstract = " ".join(abstract.split())
sentences = [s for s in re.split(r"(?<=[.!?])\s+", abstract) if s.strip()]
res["P2"] = len(sentences) == 1
say(f"abstract words={len(abstract.split())} sentences={len(sentences)}")

title = next(l.strip() for l in T.splitlines() if l.strip())
res["P3"] = not any(w in title.upper() for w in ["SOLV", "MILLENNIUM", "PRIZE", "CLAY"])
say(f"title='{title}'")
res["P4"] = not any(w.lower() in abstract.lower() for w in ["solve", "Millennium", "prize", "Clay", "Fefferman"])

refstart = T.rfind("References")
body = T[:refstart]
res["P5"] = re.search(r"\bLean\b", body) is not None
res["P6"] = any(w in body for w in [" AI ", "GPT", "language model", "artificial intelligence", "Acknowledg"])
res["P7"] = "Millennium" in body
say(f"Lean in body: {len(re.findall(r'\\bLean\\b', body))}; Millennium in body: {body.count('Millennium')}")

toc = re.search(r"Contents(.*?)\n\s*1\. Introduction\s*\n", T, re.S).group(1)
entries = re.findall(r"^\s*((?:\d+\.|Appendix [A-Z]\.|References)[^\n]*?)\s+(\d+)\s*$", toc, re.M)
starts = [(name.strip(), int(p)) for name, p in entries]
qual = 0
for i, (name, p) in enumerate(starts):
    nxt = starts[i + 1][1] if i + 1 < len(starts) else pages + 1
    span = nxt - p
    qual += span >= 1
    say(f"  section '{name}' starts p{p}, span {span} pp")
res["P8"] = qual == len(starts)
say(f"P8 per-case: {qual} of {len(starts)} sections qualify")

refs = re.findall(r"^\s*(\d+)\.\s+[A-Z]", T[refstart:], re.M)
res["P9"] = len(refs) == 22
say(f"numbered references={len(refs)} (max label {max(map(int, refs))})")

for kind in ["Theorem", "Proposition", "Lemma", "Corollary", "Remark", "Definition", "Figure", "Table"]:
    heads = re.findall(rf"^\s*{kind} ([A-Z]?\d+(?:\.\d+)?)\.", T, re.M)
    say(f"measured: '{kind} N.' headers={len(heads)} distinct={len(set(heads))}")
for w in ["we expect", "we believe", "we conjecture", "it seems", "perhaps", "might", "may ", "remarkabl", "breakthrough", "first ", "novel", "Consequently", "establish"]:
    say(f"measured: '{w}' count={T.count(w)}")

met = sum(res.values()); failed = len(res) - met
for k in sorted(res): say(f"{k}: {'MET' if res[k] else 'FAILED'}")
say(f"SUMMARY met={met} failed={failed}")
out.close()
sys.exit(0 if failed == 0 else 1)
