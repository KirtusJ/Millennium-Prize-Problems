"""T42 predicate script RUN2 (same predicates as run1 except 6 windows/regexes corrected after run1 failures; see report). Predicates fixed BEFORE first run.
Each predicate = (id, file, regex that must match within the stated line window [lo,hi] of input/paper/<file>,
 or, for kind 'absent', must match NOWHERE in the file/paper).
Kinds: present(file,lo,hi,regex)  -> MET if regex found in lines lo..hi
       absent(files,regex)        -> MET if regex found nowhere in those files
Item ids R1..R15 = referee items; F<n> = fidelity row n; C:<tag> = CHANGES.md line citation checks.
Tolerance: none numeric; line windows are exactly the ranges CHANGES.md cites (no slack) for C: predicates;
for R/F predicates the window is the range I actually read (stated in the report).
Verdict per item is a human judgement from the predicates plus reading; script only measures wording.
Output file is opened with mode 'x' (never overwritten): python3 check_items.py results_runN.txt
"""
import re, sys, os
D = "input/paper/"
L = {f: open(D+f, encoding="utf8").read().split("\n") for f in os.listdir(D) if f.endswith(".tex")}
def win(f, lo, hi): return "\n".join(L[f][lo-1:hi])
P = []
def present(i, f, lo, hi, rx): P.append((i, "present", f, lo, hi, rx))
def absent(i, files, rx): P.append((i, "absent", files, 0, 0, rx))
ALL = list(L)
# referee items
absent("R1a", ["main.tex"], r"with the same proof, for \$?\\U|Both hold for \$?\\U")
present("R1b", "main.tex", 53, 53, r"have not written it")
absent("R2a", ["sec_provenance.tex"], r"paper itself has had the corresponding review")
absent("R2b", ["sec_paperreview.tex"], r"to be filled")
present("R2c", "sec_paperreview.tex", 7, 7, r"has not been re-reviewed")
present("R3a", "main.tex", 8, 8, r"plus an independent random constant")
present("R3b", "main.tex", 8, 8, r"G\(n\)/G\(0\)\)\^\{?2")
present("R3c", "main.tex", 8, 8, r"has not been reviewed by a mathematician")
present("R3d", "main.tex", 8, 8, r"H0 to H4")
absent("R4", ["sec_negative.tex"], r"a claimed step|is not checked|was not checked here")
present("R4b", "sec_negative.tex", 655, 665, r"Proposition~\\ref\{pf:prop-L4\}\(d\)")
present("R4c", "sec_negative.tex", 655, 665, r"Lemma~\\ref\{pf:lem-R\}")
absent("R5a", ["sec_negative.tex"], r"F_4-F_3|wrong sign")
present("R5b", "sec_negative.tex", 229, 233, r"F_4-F_2")
present("R6a", "sec_reduction.tex", 148, 150, r"all four coordinate directions")
present("R6b", "sec_proof.tex", 94, 100, r"\\theta F\\cdot F\)\\ge0")
present("R7a", "sec_negative.tex", 402, 410, r"\\textup\{\(U1\)\}")
absent("R7b", ["sec_negative.tex"], r"standing assumption")
absent("R7c", ["sec_negative.tex"], r"\(H1\)")
present("R8a", "sec_negative.tex", 100, 113, r"56\$? of \$?56")
present("R8b", "sec_negative.tex", 91, 94, r"\\kappa_H\(U\)\\ge 1/2")
absent("R8c", ["sec_negative.tex"], r"\bfalse\b.*S6|S6.*\bfalse\b")
present("R9", "sec_negative.tex", 424, 440, r"\\delta_\{e\^\{-1\}\}")
present("R10", "sec_proof.tex", 341, 341, r"limit curvatures outside the box only")
present("R10b", "sec_proof.tex", 341, 341, r"\\Psi:=\\mathsf LF_\{\\rm sh\}")
present("R11a", "main.tex", 55, 56, r"Related results, not used here|not read those proofs|have read those proofs")
present("R11b", "main.tex", 56, 56, r"RepoC4")
absent("R11c", ["main.tex"], r"three groups|Ward identity")
absent("R12a", ["main.tex"], r"We prove that it does")
present("R12b", "main.tex", 15, 15, r"necessary condition; it is an upper bound")
present("R12c", "main.tex", 32, 47, r"Hypothesis & Content & Status")
present("R12d", "main.tex", 75, 100, r"Symbol & Meaning")
present("R13", "sec_reduction.tex", 185, 185, r"as read in \\cite\{KQR21\}")
absent("R13b", ["sec_reduction.tex"], r"Theorem\s*\d+\s*of\s*\\cite\{OS7[35]\}|\\cite\[Theorem[^\]]*\]\{OS7[35]\}")
present("R14a", "sec_proof.tex", 79, 79, r"even \$L\\ge4\$")
present("R14b", "sec_proof.tex", 46, 46, r"k\\ge2")
present("R15a", "sec_negative.tex", 676, 680, r"Ising")
absent("R15b", ["sec_negative.tex","sec_reduction.tex","sec_proof.tex"], r"\bbuilder|\bchallenger|\bledger")
present("R15c", "sec_reduction.tex", 367, 384, r"A test of the chain on a free field|red:freetab")
absent("R15d", ["sec_reduction.tex"], r"Every admissible constant")
# fidelity
absent("F1", ["sec_provenance.tex"], r"paper itself has had the corresponding review")
present("F2", "sec_provenance.tex", 15, 15, r"\$6\$ wrong, \$10\$ overstated, \$3\$ unsupported and \$9\$ omitted")
present("F3", "main.tex", 56, 56, r"\\beta\^\{-1/8\}")
present("F3b", "main.tex", 56, 56, r"comment 7102141403")
present("F4", "main.tex", 56, 56, r"reported, not proved here")
present("F5", "main.tex", 56, 56, r"Neither the author nor the sessions")
present("F6", "main.tex", 53, 53, r"have not written it")
present("F7", "sec_provenance.tex", 17, 19, r"comments? 7102590992")
present("F8", "main.tex", 59, 59, r"tail constant")
present("F9", "sec_provenance.tex", 9, 9, r"Eight defects")
present("F9b", "sec_provenance.tex", 9, 9, r"not re-challenged")
present("F10", "sec_provenance.tex", 11, 11, r"two undefined symbols")
present("F11", "sec_provenance.tex", 11, 11, r"not a re-audit|did not re-audit")
present("F12", "sec_provenance.tex", 13, 13, r"three defects")
present("F12b", "sec_provenance.tex", 13, 13, r"discriminators and the joint satisfiability")
present("F14", "sec_provenance.tex", 31, 31, r"general \$c\$ is not formalized")
absent("F15", ["sec_provenance.tex","sec_proof.tex"], r"s2\\_power|s2_power")
absent("F16", ["sec_provenance.tex"], r"NO-SUCH-TEXT-checks-of-c44e0c8-against-src")  # row 16 declared nothing done; this absent-pred is trivially met and is NOT evidence
present("F21", "sec_proof.tex", 554, 554, r"Weyl's integration formula.*Plancherel.*Isserlis")
present("F22", "main.tex", 24, 24, r"Consequently")
present("F24", "sec_reduction.tex", 41, 41, r"gap at all large couplings")
absent("F24b", ["main.tex"], r"gap at every coupling")
# CHANGES.md line-citation checks (exact windows cited)
present("C:1 main:69", "main.tex", 69, 69, r"Nothing is proved about gauge groups")
present("C:11 main:58-59", "main.tex", 58, 59, r"Disclosure")
present("C:14 main:84 (actual)", "main.tex", 84, 84, r"k\\ge ?2")
present("C:14 main:66", "main.tex", 66, 66, r"k\\ge2")
present("C:14 main:17", "main.tex", 17, 17, r"k\\ge2")
present("C:24 main:40 (actual)", "main.tex", 40, 40, r"m\(\\beta\)>0|large couplings")
present("C:25 main:39 (actual)", "main.tex", 39, 39, r"lem-rp|H0")
present("C:6 reduction:15", "sec_reduction.tex", 15, 15, r"sup-norm|supremum|closure")
present("C:6 reduction:130", "sec_reduction.tex", 130, 130, r"continuous")
present("C:6 proof:94", "sec_proof.tex", 94, 94, r"continuous")
present("C:6 proof:100", "sec_proof.tex", 100, 100, r"continuous|lem-rp")
present("C:10 proof:341", "sec_proof.tex", 341, 341, r"limit curvatures outside the box only|Gaussian DLR")
present("C:10 proof:416", "sec_proof.tex", 416, 416, r"as \(e\) states|Psi|conditioning|curvatures only")
present("C:proof:465", "sec_proof.tex", 465, 465, r"7102490558")
present("C:21 proof:554", "sec_proof.tex", 554, 554, r"without proof or citation")
present("C:15 neg:676-680", "sec_negative.tex", 676, 680, r"two and")
present("C:26 neg:142", "sec_negative.tex", 142, 142, r"earlier summary")
present("C:26 neg:605", "sec_negative.tex", 605, 605, r"earlier summary|ledger|director")
present("C:28 neg:367-374", "sec_negative.tex", 367, 374, r"729")
present("C:29 neg:303-306", "sec_negative.tex", 303, 306, r"no systematic literature search|sources read")
present("C:29 neg:471-474", "sec_negative.tex", 471, 474, r"U\(1\)|\\U\(1\)")
present("C:29 neg:490-491", "sec_negative.tex", 490, 491, r"sources read|systematic")
present("C:29 neg:499-500", "sec_negative.tex", 499, 500, r"sources read|systematic|Status")
present("C:29 neg:504-508", "sec_negative.tex", 504, 508, r"not establish|massless")
present("C:19 neg:6", "sec_negative.tex", 6, 6, r"four|exclusion")
present("C:19 main:51", "main.tex", 51, 51, r"four routes")
absent("C:15 reduction cut", ["sec_reduction.tex"], r"Every admissible constant")
present("C:2 prov:15", "sec_provenance.tex", 15, 15, r"wrong")
present("C:12 main:15", "main.tex", 15, 15, r"necessary condition")
present("C:5 neg:240", "sec_negative.tex", 240, 240, r"not stated in the source")
present("C:3 main:2,7-9", "main.tex", 2, 2, r"upper bound")
out = open(sys.argv[1], "x")
met = failed = 0
for i, k, f, lo, hi, rx in P:
    if k == "present":
        ok = re.search(rx, win(f, lo, hi), re.S) is not None
        loc = f"{f}:{lo}-{hi}"
    else:
        hits = [(g, n+1) for g in f for n, ln in enumerate(L[g]) if re.search(rx, ln)]
        ok = not hits
        loc = ",".join(f) + (" hits=" + str(hits[:4]) if hits else "")
    met += ok; failed += (not ok)
    out.write(f"{'MET   ' if ok else 'FAILED'} {i:22s} {loc}  /{rx}/\n")
out.write(f"TOTAL predicates {len(P)}: met {met}, failed {failed}, measured only 0\n")
out.close()
print(open(sys.argv[1]).read())
