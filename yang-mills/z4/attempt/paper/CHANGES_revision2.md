# CHANGES — revision p8-rev2 (T56), in response to DIRECTORS_REVIEW.md

The originals are kept in `orig/`. Line numbers are those of the revised files in `paper/`. `diff orig/X.tex paper/X.tex` shows every change.

## Corrections

| Item | Files:lines | What was done |
|---|---|---|
| C1 forest recursion | sec_proof.tex:165 | `g_y:=U_{yx}^{-1}g_x` replaced by `g_y:=g_xU_{xy}`, with `(U^g)_{xy}=g_xU_{xy}g_y^{-1}=1` written out; credited (comments 7105447358, 7105348719, 7105100783). Convention checked at sec_proof.tex:26. Other uses (lines 235, 251, 274) are consistent already: line 235 builds `g` as the holonomy from the corner, which is `g_y=g_xU_xy`. Checked numerically (P1, P2; child A). |
| C2 T not injective | sec_reduction.tex:15, 39; sec_proof.tex:115; sec_negative.tex:293–303, 555–562 | Recommended repair used. Site-reflection space kept. `T=e^{-H}` is never written there (new sentences at sec_reduction:15 and sec_proof:115 report the vector of squared norm 1/4 killed by one step, and the gauge-averaging projection P with PT=T=TP; credited 7105447358, 7104999220). Gap stays `-log‖T|Ω⊥‖`. Theorem R' stays abstract (positive injective operator). The application paragraph (sec_reduction:39) now applies R' to `T²` on the closure of the range of T, with `H:=-(1/2)log T²`, even lags; odd lags need the reviewer's extra condition (credited 7105014262). Lemma neg:lem-decaygap is rewritten without H (conclusion `‖T|Ω⊥‖≤e^{-m}`, proof via spectral measure of T). The (C) paragraph of Section 7 uses `H=-(1/2)log T²` and says which lags are lattice correlations. Checked for consistency: Lemma red:gap (Theorem S Step 7) uses only self-adjointness, valid for all n; Step 9 uses `|F(s)|≤e^{-s}F(0)` in the reconstructed space; Prop. pf:prop-spectral is valid for all n. Not changed. |
| C3.1 sentences after R' | sec_reduction.tex:102, 104 | Removed "C_β(ξ) tends to zero" and "overlap the lightest states". Added the reviewer's three-eigenvalue example and the remark that for a fixed local gauge-invariant Wilson observable the variance does tend to zero (tail + flatness on a box). Credited 7105014262. Observation red:twomass kept. Checked (P6). |
| C3.2 even lags | sec_reduction.tex:39 | See C2. |
| C3.3 / C12 support metric | sec_reduction.tex:130 | "lattice distance 1" → "maximum-coordinate distance 1 (n+{-1,0,1}^4)". This is the only support radius in Theorem S. Step 6's one-slice buffer is kept: sites with t≥1 have all edges in {t≥0}. H1, H3, H4 stay open (Table intro:status unchanged). |
| C4 OS II | sec_reduction.tex:175, 185–186, 349, 355; sec_provenance.tex:31 | Theorem red:OS is now cited as [OS75, Section IV.1] with hypotheses E0′ and E1–E4. Text: the paper's own sessions read it only in KQR21; a session of the second lineage read the primary source (7104829352, 7105100783). Step 9 says E4 is proved in Step 7; "Where each hypothesis enters" lists Step 7 for Step 9. |
| C5 smeared-norm variant | main.tex:55 | One sentence in Related results, reported and not read (7104829352). |
| C6 (E*) | sec_negative.tex:688–698 | (E*) now compares with the free two-particle level `E_2^free(L)` in the same symmetry channel. "In some symmetry channel" is gone. Credited 7104999220, 7105100783, 7103655841. |
| C7 off-chart shell data | sec_general.tex:28–33 (new item (iv′)) | Shell links stay group elements until inside the chart. The U(1)×Z_3 example is given. Bound `μ(chord off chart) ≤ n_R e^{D*_G − βη*/(8K_N²)}` is re-derived in the text from the shell filling bound (χ form of Lemma pf:lem-shell) and the tail of Cor. pf:cor-tail (strict→non-strict by t↑). Probability is charged in the passage to the fixed-box limit. Credited 7105348719. |
| C8 U(1) wrapping | sec_general.tex:35 | "errors in (E3) and in (b) vanish identically" replaced. (E3) is exact; (b) vanishes on {m_c=0}. Six angles π/3 give the example. `μ(m_c≠0) ≤ 6e^{D*_G−β/16}` is derived in the text. Credited 7105257573, 7105296546. Checked (P3, P4, P5; child B1). |
| C9 details | sec_general.tex:13, 27 | Hessian on (X,X) is |X|²_ρ; the factor 1/2 is in the Taylor term. The weighted-circle example "rules out a uniform ratio of the two global Haar-volume constants". The SU(3) coefficient 9√3/(8π) is kept. The uniform-constants result is in Related results (main.tex:55). Credited 7105396100. |
| C10 finite groups | main.tex:52; sec_general.tex:13; sec_negative.tex:20–23 | "The conclusion cannot hold [AC22]" removed. Now: the Z_2 sign-representation result (gap ≥ β; general finite abelian m ≥ βδ/2) is reported by a second-lineage session (7105523430) and was not read by the paper's sessions. AC22 is cited only for what it states (free-edge boxes, separately conjugation-invariant loop functions, coupling β/N_ρ). Checked δ=2 (P8). |
| C11 count | sec_negative.tex:637 | 1500 → 1490 at 8⁴. Other counts: 2990 (6⁴) and 840 = 260+290+290 (12⁴, 834 distinct) agree with the sources (P9). No sentence repeated the count. |
| C12 | see C3.3 | Also: H1, H3, H4 stay open. |
| C13 related results | main.tex:55 | Seventh root: SU(2) (7103054156, 7105296546). Eighth root for general compact Lie groups: reported, awaiting review (7105257573). |
| C14 | none | No change and nothing in the paper, as instructed. |

## Verifications (credited where used; full account in sec_provenance.tex:20–28)

| Item | Where credited |
|---|---|
| V1 Lemma R / Wick (two groups); G asymptotics; D* | sec_proof.tex:189 (D* = 60.19224006), 486 (G asymptotics); Lemma R constancy credit already at sec_proof (Constancy paragraph); provenance V1 |
| V2 cube identity, β^{-1/2} sharp | sec_proof.tex:373; provenance V2 |
| V3 shell reconstruction, 16(L+1)² | sec_proof.tex:416; provenance V3 |
| V4 Lean rebuild (132 constants, 17 axiom reports) | sec_provenance.tex:34 (Formal checks); provenance V4 |
| V5 state class | main.tex:55; provenance V5 |
| V6 attribution confirmed | main.tex:55; provenance V6 |

## Other

- R2: main.tex:58 Disclosure rewritten (specific steps reviewed; whole-proof certification open; three recommendations of major revision, each retaining the upper bound; this revision not seen by them). sec_provenance.tex:20–28 now has a new subsection "Checks by a second model lineage" (V1–V6, not verified, dispositions with commits c705f26, 7235a2c, 4d77e30, revision unseen).
- R3: sec_paperreview.tex:10–11 has a third paragraph, which ends "The text after this revision has not been reviewed by anyone."
- main.tex:73 ("not claimed" item 9) is now accurate: no whole-proof certification; specific steps reviewed; this revision unreviewed.
- refs.tex:118, 120 and main.tex:55: bib keys `RepoB4` → `RepoPackets` and `RepoC4` → `RepoBlock`, so no alias remains in the sources. Printed output is unchanged.
- sec_negative.tex:121: the branch name `director-g/science-math-svg` is removed from the figure caption because it contains a group letter. The commit `e8d62e4b` is kept.
- sec_general.tex:4: one sentence says three errors found by the second lineage are corrected there.
