# p7-final (T54's parent, task T53): second-pass review of the revised paper

Control: control.txt = 0.272341 (= -ln tanh 1). The paper/main.pdf page count is 47 (pdfinfo); this is the child's control answer.
Reader caveat: I share a model family with the director, the reviser and the builder, so my agreement is not independent review. Lean was not used, and no Lean result is claimed.

## 1. Verdict table

| # | Item | Verdict | One line of evidence |
|---|---|---|---|
| R1 | Referee 1 (U(1) claims) | STANDS | main.tex:52 and :70 agree. The U(1) claims are now routed through the extension (Section gen:sec). |
| R2 | Referee 2 (§8.7, false review claim) | STANDS | sec_paperreview.tex:1-7 is filled. Its counts 9/7/2/5/3/1 and 13/1/17 match FIDELITY.md (rows recounted: 9+7+2+5+3+1 = 27). |
| R3 | Referee 3 (abstract) | STANDS | main.tex:8 has: free field "in three independent colours plus an independent random constant", "(G(n)/G(0))^2", "H0 to H4", and the review status. |
| R4 | Referee 4 (Sec. 7 vs Sec. 4) | STANDS | sec_negative.tex:657-661 cites "(Proposition pf:prop-L4(d))" and Lemma pf:lem-R, and says the "colours may be correlated". |
| R5 | Referee 5 (F_4 vs F_2) | STANDS | sec_negative.tex:229-233: "F_4−F_2=−0.20±0.47 … neither is resolved from zero". :240 says the Z_2 convention is "not stated in the source". |
| R6 | Referee 6 (H0 gap) | STANDS | sec_reduction.tex:388: RP "in the site planes of all four coordinate directions, for bounded continuous local functions, is Lemma pf:lem-rp … and Lemma pf:lem-limit(2)". |
| R7 | Referee 7 ((H1)-(H4) clash) | STANDS | sec_negative.tex:403-422 uses (U1)-(U4). :420 says "(U1) is a hypothesis of this lemma only". |
| R8 | Referee 8 (Obs 5.3) | STANDS | sec_negative.tex:102 has "κ_H<0 in every equilibrium sample: 56 of 56". The β=4, 6 samples are stated not to bear on S6. |
| R9 | Referee 9 (family of Obs 5.11) | STANDS | sec_negative.tex:428 gives ν_β := δ_{e^{-1}} + max(0, β−1)·2·1_{[1/2,1)} dx. |
| R10 | Referee 10 (Prop 4.14(e)) | STANDS | sec_proof.tex:353: "𝒢_R := σ(F_q : q∉P_R) … (no link variables enter) … Ψ := 𝖫F_sh". |
| R11 | Referee 11 (other groups' results) | STANDS, with one weakening | main.tex:55 is quarantined, with comment numbers. The second group's "d linearly independent" lost its "d" (see 2.1). |
| R12 | Referee 12 (direction, tables) | STANDS | main.tex:14: "We prove this necessary condition; it is an upper bound on the gap and holds whether or not the gap is positive." Status table at main.tex:31-47; notation table at :76-101. |
| R13 | Referee 13 (OS73/OS75 theorem numbers) | NOT DONE, honestly disclosed | sec_reduction.tex:175 says "We did not read OS73 or OS75". :185 says "as read in KQR21". :189 says "as recalled. It was not read." sec_provenance.tex:23 repeats this. The text does not claim a theorem number. |
| R14 | Referee 14 (k ≥ 2) | STANDS | sec_proof.tex:46 says "boxes of side 2 are excluded, which changes no limit point"; Lemma pf:lem-rp is for L ≥ 4 and the chessboard lemma for k ≥ 2. |
| R15 | Referee 15 (cuts, provenance chatter) | PARTLY | The Ising material is cut to 2 sentences (sec_negative.tex:676-680) and §3.6 is shortened. Worker chatter remains in §6/§7: sec_negative.tex:457 "argued in the worker report", :465 "Stated in the worker reports", :559 "The worker compiled", :683 "known to the workers". |
| F1 | Fidelity row 1 (WRONG) | STANDS | The sentence is deleted and §8.7 is filled. |
| F2 | Row 2 (OMITTED) | STANDS | sec_provenance.tex:15 has "6 wrong, 10 overstated, 3 unsupported and 9 omitted". |
| F3-5 | Rows 3-5 | STANDS | main.tex:55 matches the locators (see 2.1). It says "Neither the author nor the sessions … have read those proofs". |
| F6 | Row 6 | STANDS | Superseded by gen:sec; main.tex:52 and :70 are consistent. |
| F7-8 | Rows 7-8 | STANDS | sec_provenance.tex:20 and main.tex:58 give the scope with comment numbers 7102490558 and 7102590992, which match the locators. |
| F9-12 | Rows 9-12 | STANDS | sec_provenance.tex:9, 11 and 13 carry the suggested wording. |
| F14 | Row 14 | STANDS | sec_provenance.tex:33 has "case c=½ … general c is not formalized … L6 concerns a remark not printed". |
| F15 | Row 15 | STANDS (re-added honestly) | s2_power is out of the table. :52 adds "contains s2_power, which the text does not use". |
| F16 | Row 16 (commits) | NOT DEALT WITH (declared) | c44e0c8 and 92623fa are printed unchanged (sec_provenance.tex:26, :57). CHANGES.md says so. |
| F21 | Row 21 | STANDS (minor residue) | main.tex:69 names Weyl, Plancherel and Isserlis. sec_proof.tex:554 also lists "a residue computation", which item 5 omits. |
| F22 | Row 22 | STANDS | main.tex:23: "Consequently" is inside the theorem. |
| F24 | Row 24 | STANDS | "at all large couplings" is used at sec_reduction.tex:41, main.tex:29 and main.tex:39. "every coupling" now appears only at main.tex:14, for RP and the transfer matrix (correct). |
| F25-26 | Rows 25-26 | STANDS | sec_reduction.tex:388 cites the Lemmas. "ledger" and "director's" are gone from sec_negative. |
| D1 | Director: "Related results" (main.tex:55) | STANDS, minor | All 5 comment numbers match THREAD_LOCATORS.md, with the right content. Two problems: "d" is dropped for the second group, and the bib folders omit the locator subfolders "/block" and "/packet-bands" (refs.tex:118, :120). |
| D2 | Director: "Other gauge groups" (main.tex:52) | DEFECT | "For finite groups the conclusion is false" is unsupported. src claims it only for Z_2, as CLAIMED/NOT CHECKED (THEOREM_B_GENERAL N5; CHALLENGE A6), and no citation is given. |
| D3 | Director: What-is-not-claimed item 6 (main.tex:70) | DEFECT (same) | It repeats "where the conclusion is false". Its standing ("attacked once") agrees with :52, gen:sec:4 and provenance:17. |
| D4 | Director: abstract | STANDS | It is SU(2)-only and "three independent colours" is correct for SU(2). It is silent on the extension; that is not a contradiction, but see must-change 6. |
| D5 | Director: provenance, extension paragraph (sec_provenance.tex:17) | DEFECT (omission) | The class and the corrected defect match CHALLENGE_GENERAL.md. It omits the challenger's NOT CHECKED items: the Z_2/finite-group literature, the builder's B1-B7 and Lean L1-L5, and MC only on R_1 with a trivial shell. |
| D6 | Director: provenance, dropped result (sec_provenance.tex:17) | NOT CHECKED | No file in src/ concerns it. It is unsupported by src. |
| D7 | Director: Lean digests (sec_provenance.tex:40-52) | DEFECT | "reproduced in the folder lean beside the sources": paper/lean does not exist (Q9 failed). The declarations printed for A1R number 10 against the stated 11 (Q8). The digests themselves were NOT CHECKED (no Lean files available). |
| G1 | sec_general hypothesis class vs the challenge | STANDS | gen:7 has: compact Lie G, d ≥ 1, faithful continuous unitary ρ, and otherwise ρ(G) "provided dim ρ(G) ≥ 1; then d means dim ρ(G). For trivial ρ the statement is false". This is exactly the corrected class. |
| G2 | gen:thm formula vs Lemma pf:lem-wick at d=3 | STANDS | (d/2)G² = (3/2)G² and d/8 = 3/8 match sec_proof.tex:512-516 (Q4). |
| G3 | "Check" numbers | STANDS | 7d/48 = 7/6 (d=8), 0.4375 (d=3), 0.145833 → 0.1458 (d=1) (Q1-Q3). The MC values are at +1.21σ, −1.50σ and +0.33σ (Q6). 9√3/(8π) = 0.620245 checks (Q5). The MC numbers are the builder's (THEOREM_B_GENERAL N4); the paper does not say whose. |
| G4 | sec_general line 13: "for G=Z_2 the weak-coupling phase is known to be gapped" | DEFECT | Uncited. src says "cited, not checked … CLAIMED". |
| G5 | The \ref's of sec_general to Section 4 | STANDS, 1 omission | See table 3. Cor pf:cor-zero (it needs faithfulness) and Lemma pf:lem-R are not itemised. Lemma R is covered under (vi). |
| G6 | Global: SU(2)-only statement left in Section 3 | DEFECT | sec_reduction.tex:363: "For another compact simple group it requires H0–H4 for that group, and nothing is claimed about them here." gen:sec now asserts the analogues of H0 (Lemmas rp and limit verbatim) and of H2 (gen:thm) for every compact Lie G. |
| C1 | Counts: H0-H4, two proved | STANDS | 5 hypothesis environments. The table has H0 and H2 "proved" (Q7). |
| C2 | Four routes plus exclusion | STANDS | The subsections are curvature, vortices, finite-size, character expansion, and Exclusion (Q7). |
| C3 | Six properties | STANDS | P1-P6 (Q7). |
| C4 | Ten standard facts | STANDS | 10 \item in pf:sec-standard. main.tex:69 says "ten" (Q7). |
| C5 | Thm 1.1 (p.1) vs recall in eq. pf:eq-main | STANDS | Same inequality, same "for every n ≥ 1", "Consequently sup m → 0", G(0)=½, G>0 and asymptotics. |
| C6 | Notation table vs uses | STANDS, minor | H0-H4, (A)=H1, (B)=H2 and (U1)-(U4) match. (C), (C′), (E) and S6 are not listed. |
| M1 | Word scan (item 5) | STANDS | No must-change hit. See table 5. |
| M2 | Mechanics (item 6) | STANDS | 0 errors, 0 undefined references, 1 overfull box of 2.17pt (< 15pt), 47 pages, Theorem 1.1 on p.1. |

Counts over the 49 rows above:
- 39 STANDS (some with a minor note);
- 1 PARTLY (R15);
- 6 DEFECT (D2, D3, D5, D7, G4, G6);
- 3 NOT DONE / NOT DEALT WITH / NOT CHECKED: R13 (honestly disclosed), F16 (declared by the reviser), D6 (no source).
Predicates (mine, check.py): **7 met, 2 failed, 2 measured only**. Mechanics (mech.sh): 4 met, 0 failed.

## 2. Details

### 2.1 Director's "Related results" sentence by sentence (THREAD_LOCATORS.md)

| Sentence (main.tex:55) | Comment | Verdict |
|---|---|---|
| m ≤ Cβ^{-1/8} for every even-periodic limit state; subspace of dim ≥ M below C_Mβ^{-1/8} | 7102141403 | Matches |
| "linearly independent magnetic readings in an energy band between two fixed multiples of 1/R, R=⌊cβ^{1/8}⌋" | 7102153452 | Slightly weaker: the locator says "d linearly independent". The "d" is dropped (and d is undefined in the locator). |
| "the first report … implies the last sentence of Thm 1.1 with a rate" | inference | Acceptable as "if correct": the L_β states are even-periodic limits. |
| Background vanishes under the limit specification and dyadic moment bounds; "equality for every fixed lag"; "reported, not proved here" | 7102652403 | Matches. The locator adds "all 18 components". |
| Fourth group: covariance within Cβ^{-1/8} of (3/2)G(n,z)², uniformly in lag and \|z\|_1 ≤ β^{1/4} | 7103151190 | Matches ("thermodynamic state" becomes "limit state"; harmless). |
| "the record … now carries Cβ^{-1/7}" | 7103054156 | Matches ("merged record"). |
| "contain Theorem 1.1 with equality and a rate" | inference | Acceptable: lag 0 is among "all integer time lags". |
| Codex identity of the groups | 7102602440, 7102612280, 7102678495, 7102686597 | Cited at provenance:20, not in this paragraph. Acceptable. |

### 3. sec_general.tex \ref's to Section 4 (opened both)

| Ref (gen line) | Cited statement | Matches use? |
|---|---|---|
| pf:eq-main (10) | Ratio bound plus "Consequently sup m → 0" | Yes. O_p and L_β are redefined at gen:7. |
| pf:eq-alpha (15) | The four relations for α | Yes. a is ∞ off G_0, which is the challenger's nit (∞−∞); χ is used where it matters. |
| pf:lem-rp, pf:lem-limit, pf:lem-transfer, pf:lem-chess, pf:lem-forest, pf:lem-flat, pf:lem-G (25) | RP; limit states; transfer matrix; chessboard; forest gauge; flat connections (already "any group 𝔾"); free correlation (scalar) | Yes. rp's proof uses ½Tr U^{-1} = ½Tr U, and the general analogue s(U^{-1}) = s(U) is stated. |
| pf:prop-spectral (26) | Var > 0 via the level sets of a conjugacy class, plus the reduction | Yes. The replacement argument (real-analytic on G_0V^{-1}) addresses exactly the step that changes. |
| pf:lem-free, pf:cor-tail (27) | ẑ bound, βS ≤ 48\|Λ\|, D* | Yes. Recomputed: the β-terms give (2d/L)log β, which is 6/L at d=3. |
| pf:lem-E, pf:lem-shell (28) | E1-E3; K_N bound in α | Yes. E1 with N=2 gives χ² = 1−cos α = s. |
| pf:thm-L3 (29) | Uniform Laplace limit, with constants 48δ²e^{8δ} and η(δ) | Yes. |
| pf:prop-L4, pf:lem-D, pf:lem-R, pf:lem-wick (30) | Limit field (b), (d); Dirichlet; R; Wick | Yes. (d)'s error \|φ_β(t) − t²/2\| ≤ t⁴/(24β) is generalised with N_ρ. |
| (not cited) pf:cor-zero | Unique zero | Omitted. Its general form needs faithfulness (builder table "Cor zero (1)": V with faithful ρ). |

### 5. Word scan (child's scan_reviewed.tsv, re-run by my grep, which also caught "establish")

| Hit | Verdict |
|---|---|
| main.tex:5, :8, :73; sec_paperreview.tex:7: "reviewed" (all denials of review) | acceptable |
| main.tex:55: RepoC4, RepoB4 (citation keys, not printed) | acceptable |
| main.tex:58; sec_provenance.tex:6 (×3), :23: "director" (defined role, provenance) | acceptable |
| refs.tex:116, 118, 120: Millennium, Prize, z4, B4, C4 (bibliography) | acceptable |
| sec_provenance.tex:26: folder "z4/" and commit c44e0c8 (factual, provenance); :43, :45 (hex digests) | acceptable |
| sec_negative.tex:230, :233 (F_4, 2∣4); sec_proof.tex:307, :483, :488 (math) | acceptable (false positives) |
| sec_negative.tex:505, :507, :683; sec_reduction.tex:365: "established/establish(ing)" (negated, or quoting JW) | acceptable |
| verified, clearly, obviously, novel, remarkable, we believe | no hits |

### 6. Mechanics
These results are from my own rerun in rebuild/ (results/mech_direct1.txt), and they agree with the child's build/:
- 3× pdflatex: 0 "!" errors and 0 "undefined".
- One overfull \hbox of 2.17381pt at sec_general.tex's display (line 20 of the log context), which is below the brief's 15pt.
- 47 pages. CHANGES.md said 45 before sec_general and the director's edits.
- pdftotext page 1 contains "Theorem 1.1".

## 4. Hypotheses each statement uses, and where stated
- **Thm 1.1:** SU(2), d=4, Wilson action, periodic boxes 2^k with k ≥ 2, μ ∈ 𝓛_β, plaquette p_0 spatial, limits in the order box → β → n (main.tex:16-23; sec_proof.tex:5-17).
- **Thm gen:thm:** compact Lie G with d=dim G ≥ 1, possibly disconnected; faithful continuous unitary ρ (otherwise ρ(G) with dim ρ(G) ≥ 1); s = 1 − Re Tr ρ/N_ρ; everything else as in Thm 1.1 (sec_general.tex:7). Cited, not proved: the Haar density in the exponential chart, null level sets of real-analytic functions, Hopf-Rinow and the Z_2 gap (src THEOREM_B_GENERAL §6). Only the Z_2 gap appears in the paper as "known".
- **Thm R′:** (A), (B), (C) (sec_reduction.tex:41-55).
- **Thm S:** H0, H1=(A), H2=(B), H3, H4 (sec_reduction.tex:148-192).
- **Lemma neg:lem-usc:** (U1)-(U4) (sec_negative.tex:403-407).
- **Obs 6.1:** P1-P6 (sec_negative.tex:450-470).

## 5. Failed predicates
- **Q8 (check.py):** A1R declarations named in the table number 10 (L1-L7, L6_sharp', D_ge, mutation_false), but the text says "11". My expectation may be wrong if the file holds an unnamed eleventh declaration, as S2 holds s2_power. Either way the text does not say which declaration it is. This is a defect of the target's exposition.
- **Q9:** paper/lean does not exist, but sec_provenance.tex:40 says the files "are reproduced in the folder lean beside the sources". This is a defect of the target.
- **Child:** its scan heuristic gave 8 false "must change" hits. That is its own defect, overridden by reading. Its register K1 records `true` as a placeholder, and its programs were not run through the register. Its own defect: a weak record. I reran both of its tasks independently.

## 6. What I did not check
- The Lean digests, the Lean files, and commits c44e0c8, 92623fa, 34f97d2 and d801091.
- The dropped result (no source in src/).
- The truth of the "Z_2 gapped" claim.
- Any MC beyond arithmetic against the printed errors.
- The mathematical correctness of sec_general beyond the \ref's, the formulas and the numbers. I took the challenger's line-by-line check as a claim and did not repeat it.
- sec_negative beyond the lines quoted.
- Whether the paper is otherwise unchanged against orig/paper_before/, which is not in my directory.

## 7. Delegated questions and outcomes
- **Child T54** (admitted under T53, run as child-run1 in pcp/, exit 0 in 108 s, released). Questions: items 5 (word scan) and 6 (mechanics).
  - I graded the control first: child/control.txt = 47, which is correct (pdfinfo 47).
  - Its result: 19 hits, 0 must change; 0 errors, 0 undefined references, 1 overfull box (2.17pt), 47 pages, Thm 1.1 on p.1.
  - I reran both: mech.sh (results/mech_direct1.txt, register K3) and my own grep. Both agree. My grep found 4 extra "establish*" hits, all acceptable.
- **Grandchild T55** (admitted by the child under T54 at depth 3, released per the graph, event 111). Question: an independent recount of the overfull hboxes in build/main.log. Its control 7·3/48 = 0.4375 was correct. Its result: 1 box, max 2.17381pt. My rerun agrees.

## 8. Must change before this text is shown to anyone (in order of importance)
1. **sec_reduction.tex:363.** The text now contradicts §4.x. Replace it with: "\emph{Other groups.} The proof uses no property of SU(2). For another compact Lie group of positive dimension, the analogues of H0 and H2 follow from Section~\ref{gen:sec} (with the weaker standing stated there); H1, H3 and H4 are not claimed."
2. **main.tex:52 and :70, "For finite groups the conclusion is false".** Replace with: "For finite groups the proof gives nothing (the limit field vanishes); for $\Z_2$ the weak-coupling phase is reported to be gapped [citation], which we have not checked." In item 6, change "where the conclusion is false" to "where the proof gives nothing".
3. **sec_general.tex:13, "for $G=\Z_2$ the weak-coupling phase is known to be gapped".** Write "is reported to be gapped~\cite{…}; we have not checked this", or delete the clause.
4. **sec_provenance.tex:40, "The three files are reproduced in the folder lean beside the sources".** Add paper/lean/ with the files and axiom reports, or write: "The three files are in~\cite{Repo} at the paths above; they are not included with these sources." At :48, name the eleventh A1R declaration, or correct 11 to 10.
5. **sec_provenance.tex:17.** After "which is corrected", add: "The challenger did not check the finite-group literature, the builder's numerical tests or its Lean file, and its Monte Carlo covers only the smallest box with trivial boundary data." For the dropped result, either give a locator or keep the paragraph and mark it as unsupported by any file accompanying the paper.
6. **main.tex:8 (abstract).** Optional, for agreement with main.tex:52: add "An extension to compact Lie groups of positive dimension, with a weaker standing, is given in Section 4." Otherwise a reader of the abstract alone will not know the U(1)/SU(3) statement exists.
7. **sec_general.tex:33 ("Check").** Attribute the Monte Carlo: "(builder's program; the challenger's independent program gives 1.1650(20) for SU(3) and 0.1462(3) for U(1))", taken from CHALLENGE_GENERAL.md. sec_general.tex:25: add Corollary~\ref{pf:cor-zero} to (i), "with faithfulness of ρ".
8. **sec_negative.tex:457, :465, :559, :683.** Remove the worker chatter (referee item 15): "is argued from the Hamiltonian limit, not cited"; "Not written out in a source we read"; "The integer form of this chain was compiled in Lean"; "is known to us".
9. **main.tex:55.** Write "$d$ linearly independent magnetic readings" as in comment 7102153452. In refs.tex:118 and :120, add the subfolders "/packet-bands" and "/block" from THREAD_LOCATORS.md.
10. **main.tex:69, item 5.** Add "and a residue computation" so that it matches sec_proof.tex:554. Notation table (main.tex:96): add (C), (C′), (E) and S6.

## Register verification (last lines)
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- `pcpos verify child/pcp/register.jsonl`: the same line.

## Rerun commands (from /home/user/z4-workers/p7-final; outputs use mode "x", so use new names)
```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
pdfinfo paper/main.pdf | grep Pages
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos; G=/home/user/z4-work/graph/attempt.jsonl
$P init pcp --principal principal --principal-name "Kirtus Justus"
$R task-admit $G --by principal --label p7-final-child --parent T53
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T54
$P check --ws pcp --name check-run2 --expect-exit 0 -- python3 check.py results/check_run2.txt paper
rm -rf rebuild && cp -r paper rebuild && $P check --ws pcp --name mech-rerun2 --expect-exit 0 --timeout 280 -- bash mech.sh rebuild
bash mech.sh rebuild
grep -n -i -o -E ".{0,50}(verified|reviewed|establish|clearly|obviously|novel|remarkable|we believe|director|z4|a4|b4|c4|d4|g4|millennium|prize).{0,40}" paper/*.tex
$P verify --ws pcp
$R verify pcp/register.jsonl
```
