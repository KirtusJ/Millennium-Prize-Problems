# notes p5-fid (T29)
step0: control.txt = 0.272341 (-ln tanh 1)
step1: sections counted = 8 (main 2, reduction 1, proof 1, negative 3, provenance 1). child T31 admitted; PROMPT written; child gets copy of paper/
step2 (provenance vs challengers/ledgers):
- chalR: 16 STANDS/8 DEFECT/1 NC; paper "eight statements were wrong and were corrected" — defects incl. wording/omission; "corrected" not stated in A1 ledger for R.
- a5: 17/1/1 -> paper faithful. a8: 12/2/2 (labels; L4 quantifier + 2 undefined symbols) -> paper drops 2 not checked. a9: 11 stand, 1 non-fatal defect, Lean not rerun, Lemma D/G not re-audited -> paper "found no failing line" omits provisos.
- c2: 12/3/2 -> paper names only step-8 defect; omits wording + status-line defects and 2 NC.
- "six wrong and ten overstated" vs A1 ledger "6 wrong, 10 overstated, 3 unsupported, 9 omitted" -> OMITTED.
- "paper itself has had the corresponding review (sec:paperreview)" but sec_paperreview.tex = "(to be filled ...)" -> WRONG/premature.
- No src mention of Codex, commit 34f97d2/92623fa/c44e0c8, beta^{-1/8}, O(n^-6), s2_power: unsupported by src. src (THEOREM_B) gives C4 rate beta^(-1/32)(log)^(1/16).
- INCONSISTENT: intro "holds with the same proof for U(1)", "Both hold for U(1)" vs notclaimed item 6 "Nothing is proved about gauge groups other than SU(2)".
step3: child control = 8, expected 8 -> CORRECT (graded before reading output). child-run1 = K1 exit 0, 80 s
step4: released T31; grandchild T32 in graph (see report). child Q1: 3 overfull>10pt (34.41 red:113-114, 57.50 red:288-289, 104.70 prov:24-25); no undef/dup labels; 31/31 bib. Q2: 5/2/5/6/10 all as claimed.
step5: fidcheck run1 (K2): Q1,Q2,Q4 FAILED = my defect (arccosh underflow -> inf); Q3 spuriously MET; Q10 FAILED = target defect (paperreview placeholder). fixed m formula; run2
step6: own pdflatex x2 (K4) reproduces child's 4 overfull (3 >10pt); own bib/label scan 31/31, no dups. overclaim/alias scan done; remaining -> report
step7: report.md written. FAITHFUL 9, OVERSTATED 7, WRONG 2, OMITTED 5, INCONSISTENT 3, NOT CHECKED 1
