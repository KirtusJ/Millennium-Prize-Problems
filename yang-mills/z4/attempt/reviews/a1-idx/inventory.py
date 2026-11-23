"""inventory.py - structural inventory of repo/yang-mills for INDEX.md (a1-idx).

Usage: python3 -I inventory.py <repo/yang-mills path> <child dir> <output file>

Predicates (fixed before the first run; no randomness, so no seed; no tolerances: all exact integer comparisons):
 H  (hypothesis test for P3, per case): for each director folder, does it contain README.md at top level?
    Report how many of the 7 folders qualify.
 P1 transfer-operator contains exactly 13 immediate sub-directories (my own `ls` count before delegation).
 P2 the child's control.txt equals the P1 count (grades the child's control).
 P3 for all director folders: a top-level README.md exists (expected 7 of 7).
 P4 for all .lean files outside */evidence/* : no token `sorry` appears (text grep, NOT a compile; expected 0 hits).
 P5 for all .lean files outside */evidence/* : file contains at least one `#print axioms` line
    (expectation only; a failure is an observation about the repository, not a defect claim).
Measured only: number of .lean files, number of .md files, per folder.
Result file is opened with mode "x" (never overwritten). Exit 0 if P1-P4 met, 1 otherwise (P5 is measured-with-expectation).
"""
import os, re, sys, json

root, child, out = sys.argv[1], sys.argv[2], sys.argv[3]
folders = ["observable-normalization", "transfer-operator", "central-quotients",
           "spectral-support", "g4", "volume-uniformity", "z4"]
res = {"predicates": {}, "measured": {}}

H = {f: os.path.isfile(os.path.join(root, f, "README.md")) for f in folders}
res["H_cases_qualifying"] = f"{sum(H.values())} of {len(H)}"

to = os.path.join(root, "transfer-operator")
n_sub = sum(1 for e in os.listdir(to) if os.path.isdir(os.path.join(to, e)))
res["predicates"]["P1"] = {"value": n_sub, "met": n_sub == 13}
cc = open(os.path.join(child, "control.txt")).read().strip()
res["predicates"]["P2"] = {"child": cc, "met": cc == str(n_sub)}
res["predicates"]["P3"] = {"missing": [f for f, v in H.items() if not v], "met": all(H.values())}

sorry_hits, no_axioms, nlean = [], [], {}
for f in folders:
    nl = nm = 0
    for dp, dn, fn in os.walk(os.path.join(root, f)):
        for x in fn:
            p = os.path.join(dp, x)
            if x.endswith(".md"): nm += 1
            if x.endswith(".lean") and "/evidence/" not in p + "/":
                nl += 1
                t = open(p, encoding="utf-8", errors="replace").read()
                body = re.sub(r"--[^\n]*|/-.*?-/", "", t, flags=re.S)
                if re.search(r"\bsorry\b", body): sorry_hits.append(os.path.relpath(p, root))
                if "#print axioms" not in t: no_axioms.append(os.path.relpath(p, root))
    nlean[f] = nl
    res["measured"][f] = {"lean_files_excl_evidence": nl, "md_files": nm}
res["predicates"]["P4"] = {"sorry_files": sorry_hits, "met": not sorry_hits}
res["predicates"]["P5"] = {"files_without_print_axioms": no_axioms, "met": not no_axioms}

with open(out, "x") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res["predicates"], indent=1)[:3000])
print("H:", res["H_cases_qualifying"])
ok = all(res["predicates"][k]["met"] for k in ("P1", "P2", "P3", "P4"))
sys.exit(0 if ok else 1)
