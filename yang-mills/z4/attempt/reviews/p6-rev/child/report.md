# T42 report: are REFEREE section 6 and non-FAITHFUL FIDELITY rows addressed in input/paper/?

Control: control.txt = 15 (items 1-15 in REFEREE.md §6, lines 122-137), written first. Verdicts below are my reading of the quoted lines; predicates (check_items.py, 93 of them) only confirm the wording. "Addressed" means the text now says what the item asked for. It does not mean the new text is correct.

## 1. Referee items (file:line in input/paper/)

| # | Verdict | file:line | Evidence |
|---|---|---|---|
| 1 U(1) | ADDRESSED | main.tex:53, 69 | "We expect the argument to adapt to U(1) and have not written it"; "same proof" / "Both hold" absent from main.tex. |
| 2 §8.7 / review claim | ADDRESSED | sec_paperreview.tex:1-7; sec_provenance.tex:15 | placeholder gone; "It has not been re-reviewed"; the "paper itself has had the review" sentence is absent. |
| 3 abstract | ADDRESSED | main.tex:8 | "plus an independent random constant", "(G(n)/G(0))^2", "H0 to H4", "has not been reviewed by a mathematician". Lemma 4.17 is not cited by number; the structure is described. |
| 4 "claimed step" | ADDRESSED | sec_negative.tex:655-665 | cites "Proposition pf:prop-L4(d)" and "Lemma pf:lem-R"; "colours may be correlated". |
| 5 F4 vs F2 | ADDRESSED | sec_negative.tex:229-233 | "F_4-F_2=-0.20±0.47"; "neither is resolved from zero"; "wrong sign" gone. |
| 6 H0 | ADDRESSED (by restricting H0, which the referee allowed) | sec_reduction.tex:148-150; sec_proof.tex:94 | "all four coordinate directions"; "bounded continuous F ... {x_j>=c}". The restricted H0 is proved from Lemmas rp and limit. |
| 7 (H1)-(H4) names | ADDRESSED | sec_negative.tex:402-410, 420-421 | "(U1) a unique infinite-volume Gibbs state ..."; "(U1) is a hypothesis of this lemma only". "standing assumption" absent. |
| 8 Obs 5.3 | ADDRESSED | sec_negative.tex:91-94, 100-113 | "κ_H<0 ... 56 of 56"; S6 precise, "κ_H(U)≥1/2"; "false" dropped. |
| 9 spectral family | ADDRESSED | sec_negative.tex:424-440 | "ν_β:=δ_{e^{-1}}+max(0,β-1)2·1_{[1/2,1)}dx", moments given. |
| 10 Prop 4.14(e) | ADDRESSED | sec_proof.tex:341, 416 | "limit curvatures outside the box only"; "Ψ:=LF_sh"; remark at 416 now points to (e). |
| 11 other groups | ADDRESSED (quarantined) | main.tex:55-56 | "Related results, not used here"; "Neither the author nor the sessions ... have read those proofs". |
| 12 direction / tables | ADDRESSED | main.tex:15, 32-47, 75-100 | "necessary condition; it is an upper bound"; status table; notation table. "We prove that it does" absent. |
| 13 OS73/OS75 theorem no. | DECLARED NOT DONE | sec_reduction.tex:185 | "as read in [KQR21]"; no theorem number from OS73/OS75 (CHANGES.md says NOT DONE; the text agrees). |
| 14 L=2 | ADDRESSED | sec_proof.tex:46, 79 | "k≥2"; "boxes of side 2 are excluded, which changes no limit point"; "even L≥4". |
| 15 cuts | PARTLY | sec_reduction.tex:367-384; sec_negative.tex:676-680 | §3.6 shrunk to a paragraph and a 3-row table, not removed; Ising now two sentences, not removed. Builder/challenger/ledger wording is gone from §5 (grep); Section 4 is untouched, as the referee wanted. |

## 1b. Fidelity rows that are not FAITHFUL (18 rows)

| Row (verdict) | Verdict | file:line | Evidence |
|---|---|---|---|
| 1 WRONG | ADDRESSED | sec_provenance.tex:15; sec_paperreview.tex:7 | sentence absent; "has not been re-reviewed". |
| 2 OMITTED | ADDRESSED | sec_provenance.tex:15 | "6 wrong, 10 overstated, 3 unsupported and 9 omitted". |
| 3 WRONG | ADDRESSED (wording only; the comment locator is not checkable offline) | main.tex:56 | "β^{-1/8}" with "comment 7102141403". |
| 4 OVERSTATED | ADDRESSED | main.tex:56 | "reported, not proved here". |
| 5 OVERSTATED | ADDRESSED | main.tex:56 | "Neither the author nor the sessions". |
| 6 INCONSISTENT | ADDRESSED | main.tex:53, 69 | as referee 1. |
| 7 OVERSTATED | ADDRESSED | sec_provenance.tex:17-19; main.tex:59 | scope with "comment 7102590992". Tail constant kept and attributed. |
| 8 OVERSTATED | ADDRESSED | main.tex:59 | lists Lemma R, Wick, G asymptotics and "tail constant" with comment numbers. |
| 9 OVERSTATED | ADDRESSED | sec_provenance.tex:9 | "Eight defects"; "not re-challenged". |
| 10 OMITTED | ADDRESSED | sec_provenance.tex:11 | "two undefined symbols"; "did not check the details of the DLR". |
| 11 OMITTED | ADDRESSED | sec_provenance.tex:11 | "one declared non-fatal defect"; "did not re-audit Lemmas". |
| 12 OMITTED | ADDRESSED | sec_provenance.tex:13 | "three defects"; "discriminators and the joint satisfiability ... not checked". |
| 14 OVERSTATED | ADDRESSED | sec_provenance.tex:31 | "general c is not formalized". |
| 15 OVERSTATED | ADDRESSED | sec_provenance.tex:32 | only s2_gap_le; "s2_power" absent. |
| 16 NOT CHECKED | DECLARED NOT DONE | sec_provenance.tex:24, 41 | commits c44e0c8 and 92623fa are still printed as before. |
| 21 OMITTED | ADDRESSED | sec_proof.tex:554; main.tex:68 | "Weyl's integration formula ..., Plancherel's theorem ... Isserlis' theorem". |
| 22 INCONSISTENT | ADDRESSED | main.tex:24 | "Consequently" is inside the theorem environment (19-25). |
| 24 INCONSISTENT | ADDRESSED | sec_reduction.tex:41; main.tex:30, 40 | "a gap at all large couplings"; "gap at every coupling" absent. |

**Counts, 15 referee items + 18 fidelity rows = 33 items: ADDRESSED 30 (13 + 17), PARTLY 1, NOT ADDRESSED 0, DECLARED NOT DONE 2 (referee 13, fidelity 16).**
Referee alone: 13 / 1 / 0 / 1. Fidelity alone: 17 / 0 / 0 / 1.

## 2. CHANGES.md citations that do not match the text (checked against the cited lines)
Of 26 cited ranges checked as predicates, three do not match:
- Item 14 cites main.tex:79 for the k≥2 notation. Line 79 is `\small`. The row is at main.tex:84.
- Fidelity row 24 cites main.tex:41. Line 41 is the H2 row. The H1/(A) row ("a gap at all large couplings") is at :40.
- Fidelity row 25 cites main.tex:41 for the pointer to Lemmas rp/limit. That pointer is in the H0 row, :39.
Other notes:
- Item 2 cites sec_provenance.tex:15 for a sentence that was deleted. That line now holds the "6 wrong, 10 overstated ..." sentence, so the pointer is to the neighbourhood, not to the change.
- Item 15's remark that "nothing was cut from Section 4", and the page counts and "0 overfull boxes" (D-list), were not checked.
- CHANGES.md "Referee verdict-table items 20-32" refer to the referee's own table, which I did not read. I did not check them item by item.

## 3. Failed predicates
Run 1 (results_run1.txt): met 86, failed 7, measured only 0. All kept. Run 2 (results_run2.txt): met 93, failed 0.
- R4 (my own expectation): the regex "not checked" also hit sec_negative.tex:296, which is unrelated ("its hypotheses for link variables were not checked"). Run 2 uses the narrower "a claimed step|is not checked|was not checked here". This narrowing is a weaker predicate. I read 655-665 directly, and the removal is real.
- R10, R10b (my own window): I looked at 410-420, but (e) is at :341; 416 holds the remark. Run 2 uses :341.
- C:14 main:79, C:24 main:41, C:25 main:41: **defects of the target (CHANGES.md)**. Run 2 shows the actual lines (84, 40, 39).
- C:15 reduction:100-104: I expected the cut text "D>=" to be absent, so the present-predicate failed by design. Run 2 replaces it by the absent-form, met.
- F16 is trivially met and is NOT evidence (nothing to check). Treat as measured only.
No numeric tolerances. Line windows are those cited in CHANGES.md, or the range I read.
"For all" predicates: R1a, R2a, R4, R5a, R7b/c, R11c, R12a, R15b/d, F1, F15, F24b are "nowhere in the file". The cases that qualify are the whole files (main.tex, the sec_*.tex), 8 files scanned.

## 4. Not checked
- Whether the new text is mathematically right (Lemma pf:lem-rp for all planes, the sup-norm closure, the (U1) argument).
- The comment numbers in [RepoThread] (no network). That a −1/8 rate is in comment 7102141403 is the author's claim.
- A compile or PDF: no LaTeX run, page count, overfull boxes, or whether \ref/\cite resolve.
- orig/paper_before is not in input/, so I cannot diff old against new, only read the new text.
- Referee's verdict-table items 20-32 and the referee's other sections (1-5).
- Whether main.tex:8's first sentence is proved by Prop pf:prop-L4 and Lemma pf:lem-R, as CHANGES.md item 3 says it was checked.
- The three "FAITHFUL" rows CHANGES.md revisits (19, 25, 26) apart from the line cites above.

## 5. Delegated question
- Grandchild task T43 (label p6-rev-grandchild, parent T42), admitted by the Rust host before it started (event 83) and released after it returned (event 84).
- Control: asked 7*8+6*4; grandchild/control.txt = 80. Known answer 80: correct.
- Question: independent recount of the sample counts in neg:tab-curv against the claim 56 in neg:obs-curv.
- Result (grandchild/result.md): program 1 = 16+12+2+2 = 32 (rows at sec_negative.tex:122-125); program 2 = 20 (caption, lines 139-140, for the five "not recorded" 3^4 rows, 126-130) + 2 + 2 (lines 131-132) = 24; total 56. Open-box rows (15 samples, 134-136) excluded, since the observation is about periodic boxes.
- My reread: I read result.md and sec_negative.tex:100-145 myself. The row arithmetic is confirmed. I also reran it (pcp check recount-56, `8*2+4*3+2+2, 20+2+2` → 32, 24, 56). The caveat stands: the 20 comes from the caption alone and cannot be checked row by row, so "56 of 56" depends on that caption number.

## 6. Rerun
```
cd /home/user/z4-workers/p6-rev/child
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name check-items-run1 --expect-exit 0 -- python3 check_items.py results_run1.txt
$P check --ws pcp --name check-items-run2 --expect-exit 0 -- python3 check_items2.py results_run2.txt
$P check --ws pcp --name recount-56 --expect-exit 0 -- python3 -c "print(8*2+4*3+2+2, 20+2+2, 8*2+4*3+2+2+20+2+2)"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
(Result files are opened with mode "x"; rerun into new names, e.g. results_run3.txt.)

## 7. Register verification (last lines)
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
