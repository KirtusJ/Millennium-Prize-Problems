# T31 report

**Control:** `control.txt` = 8 (`\section`: main.tex:13, :43; sec_reduction:1; sec_proof:3; sec_negative:4, :420, :500; sec_provenance:1). `sec_paperreview.tex` (input at sec_provenance:44) has none.

## Q1 (pdflatex x2 in build/, exit 0 both)
| Item | Result |
|---|---|
| Overfull >10pt | 34.41pt sec_reduction.tex:113--114; 57.50pt sec_reduction.tex:288--289; 104.70pt sec_provenance.tex:24--25 (3 total) |
| Overfull <=10pt (not reported by brief) | 3.78pt sec_proof.tex:135--136 |
| Undefined refs/cites | none (final run) |
| Multiply defined labels | none (log and independent source scan) |
| Bibitems never cited | none (31 bibitems, 31 cited keys) |
| Cited keys with no bibitem | none |

## Q2 (counts claimed / counted)
| Item | Claimed / counted | Where |
|---|---|---|
| (a) hypotheses used by Thm S (thm:conditional) | 5 / 5 | H0 sec_reduction:142; A :41; B :45; H3 :148; H4 :159; theorem :185 |
| (a) stated proved | 2 / 2 | H0 and B(=H2), table rows :395, :397; A, H3, H4 "open" (:396, :398, :399) |
| (b) routes in sec:routes (unit: subsection) | 5 / 5 | sec_negative:28, 167, 263, 328, 379 |
| (c) properties in sec:shared (unit: \item[P_n]) | 6 / 6 | sec_negative:426, 427, 431, 434, 437, 440 |
| (d) standard facts in pf:sec-standard (unit: \item) | 10 / 10 | sec_proof:543-552 |

Notes: Theorem R' (thm:reduction, :65) uses a different set, (A),(B),(C), 3 hypotheses. sec_proof:554 names 3-4 further tools beyond the list (Weyl formula, Plancherel/residue, Isserlis); they are outside the "ten".

## Failed predicates
1. My file attribution of overfull boxes via paren-stack parsing returned "?" (my parser's defect; the log's parens are unbalanced by TeX output). Fixed by checking source lines by hand against the log order; the 4 attributions were confirmed by reading the source line.
2. My "status row" regex also matched the free-field table (sec_reduction:371-376), my own loose expectation, not a defect of the paper. The real status table is :395-399.
3. Grandchild: its "3 prose facts" line is hardcoded, not parsed (disclosed by it).

Tolerances: 10pt threshold from the brief; no other tolerance used.

## Grandchild
Task id **T32** (p5-fid-grandchild, parent T31), released after return. Question: independently recount the pf:sec-standard items. Control (`\input` lines in main.tex) = 6, matched. Outcome: 10 items, lines 543-552, two methods agree. I reread count.py and reran it under `pcp check` (exit 0, same output).

## Verify lines
result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
