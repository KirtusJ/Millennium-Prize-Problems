"""check_refs.py -- verify refs.tex against the fetched records and compile it.

Usage: python3 check_refs.py <workdir_for_latex> <outfile>  (outfile mode "x")

PREDICATES (fixed before the first run):
 C1 the set of \\bibitem keys equals the 33 brief keys + 4 Repo keys (37), no duplicates.
 C2 the keys appear in case-insensitive alphabetical order.
 C3[key] every DOI and arXiv number written in the entry occurs (case-insensitively) in the
         fetched records (results_run1.json, results_run2.json, child/out1/records.json).
 C4[key] every number token of length >= 2 in the entry outside URLs/arXiv ids (volumes,
         pages, years, article numbers) occurs in that key's fetched records serialized to text.
         Exempt: JW (no record has its URL/date; both come from the brief) and Repo* (given text).
 C5 an amsart document loading hyperref with \\begin{thebibliography} + \\input{refs.tex} +
    \\nocite{*} compiles with pdflatex -halt-on-error, exit 0, and the log has no
    "Undefined control sequence", "Overfull" is allowed (layout, not error).
Tolerance: none; exact substring matches.
"""
import json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BRIEF = "JW OS73 OS75 KQR21 OS78 Lu77 GJ FILS78 SZZ23 Guth80 FS82 GM82 AC22 Ch21 Ch18 To07 IS07 IS08 KT02 TY85 BS83 ADC21 Sin81 CCK07 Cr79 FiveD11 LW86 FHK93 Te98 LTW04 LL10 BCH26 SS23".split()
REPO = ["Repo", "RepoC4", "RepoB4", "RepoThread"]
ALIAS = {"GJ": ["GJ", "GJ_book"], "LL10": ["LL10_book"], "JW": ["JW", "JW_book"],
         "GM82": ["GM82", "GM82_page"], "LW86": ["LW86", "LW86_page"], "OS73": ["OS73", "OS73_page"],
         "ADC21": ["ADC21", "ADC21_page"]}


def main():
    wd, outfile = sys.argv[1], sys.argv[2]
    out = open(outfile, "x")
    tex = open(os.path.join(HERE, "refs.tex")).read()
    body = re.sub(r"^%.*$", "", tex, flags=re.M)
    parts = re.split(r"\\bibitem\{([^}]+)\}", body)[1:]
    ent = dict(zip(parts[0::2], parts[1::2]))
    keys = parts[0::2]
    log, fails = [], []
    def p(name, ok, msg=""):
        log.append(f"{name}: {'MET' if ok else 'FAILED'} {msg}")
        if not ok:
            fails.append(name)
    p("C1", sorted(keys) == sorted(BRIEF + REPO) and len(keys) == len(set(keys)), f"n={len(keys)}")
    p("C2", keys == sorted(keys, key=str.lower))
    recs = {}
    for fn in ["results_run1.json", "results_run2.json"]:
        for k, v in json.load(open(os.path.join(HERE, fn)))["results"].items():
            recs.setdefault(k, []).append(json.dumps(v, ensure_ascii=False))
    child = open(os.path.join(HERE, "child/out1/records.json")).read() if os.path.exists(os.path.join(HERE, "child/out1/records.json")) else ""
    alltext = ("\n".join(sum(recs.values(), [])) + child).lower()
    for k in BRIEF:
        e = ent.get(k, "")
        ids = re.findall(r"doi\.org/([^}\s;]+)\}", e) + re.findall(r"arXiv:([\w./-]+[0-9])", e)
        p(f"C3[{k}]", all(i.lower() in alltext for i in ids), f"ids={ids}")
        if k == "JW":
            continue
        rt = "\n".join(sum((recs.get(a, []) for a in ALIAS.get(k, [k])), []))
        if k in ("FiveD11", "KT02", "CCK07", "BCH26"):
            rt += child
        e2 = re.sub(r"\\url\{[^}]*\}|arXiv:[\w./-]+", "", e)
        nums = [n for n in re.findall(r"\d+", e2) if len(n) >= 2]
        miss = [n for n in nums if n not in rt]
        p(f"C4[{k}]", not miss, f"missing={miss}")
    os.makedirs(wd, exist_ok=True)
    shutil.copy(os.path.join(HERE, "refs.tex"), os.path.join(wd, "refs.tex"))
    open(os.path.join(wd, "t.tex"), "w").write(
        "\\documentclass{amsart}\n\\usepackage[T1]{fontenc}\n\\usepackage{hyperref}\n\\begin{document}\nTest.\\nocite{*}\n"
        "\\begin{thebibliography}{99}\n\\input{refs.tex}\n\\end{thebibliography}\n\\end{document}\n")
    rc = 0
    for _ in range(2):
        rc = subprocess.run(["pdflatex", "-halt-on-error", "-interaction=nonstopmode", "t.tex"], cwd=wd,
                            capture_output=True).returncode
    lg = open(os.path.join(wd, "t.log"), errors="replace").read()
    p("C5", rc == 0 and "Undefined control sequence" not in lg and "LaTeX Error" not in lg,
      f"rc={rc} warnings={len(re.findall('Warning', lg))} overfull={lg.count('Overfull')}")
    out.write("\n".join(log) + f"\nFAILED: {fails}\n")
    out.close()
    print("\n".join(log)); print("FAILED:", fails)


if __name__ == "__main__":
    main()
