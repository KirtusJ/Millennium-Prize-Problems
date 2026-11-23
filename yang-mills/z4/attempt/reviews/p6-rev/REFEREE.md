# Referee report: "An upper bound on the lattice mass gap at weak coupling" (paper/, 43 pp.)

Worker p5-ref, task T30. Control: control.txt = 0.272341 (= -ln tanh 1).
Reader caveat: I share the authors' model family, so my agreement is not independent review. Where I say a proof "stands", I mean I read every line and found no failing step. That is weaker than a mathematician's review.

## Verdict table

| # | Item | Verdict | One line of evidence |
|---|------|---------|----------------------|
| 1 | Lemma 4.1 (site-plane RP), sec_proof.tex:78-88 | STANDS (nit) | The half-weight on in-plane plaquettes is correct. The proof is ill-posed for L=2 (k=1): on the 2-torus both direction-j links join the same two sites, so the E_0/E_+/E_- partition fails. This does not affect limit points. |
| 2 | Lemma 4.2 (limit states), :90-101 | STANDS | Standard weak-limit argument. RP is shown only for continuous local F in {x_0>=0}. |
| 3 | Lemma 4.3 / Prop 4.4 (transfer matrix, spectral bound), :107-131 | STANDS | The doubling Cauchy-Schwarz argument gives a contraction. The norm bound holds for all n without needing T>=0. |
| 4 | Lemma 4.5 chessboard (dyadic), :137-154 | STANDS | The reflection identity theta_a∘vartheta_t = vartheta_{t'} checks out. A face in a reflection plane is shared by f∘vartheta_t and f∘vartheta_{t'}, which is harmless: products are allowed, and the 4-fold hits are absorbed by idempotence in Cor 4.8. The d=2 U(1) analogue tested exactly: 0 violations (P6, mine). |
| 5 | Lemma 4.7 free-energy bounds, D* = 60.1922, :168-190 | STANDS | Recomputed: D* = 60.192240, c_H = 0.1502578 (P1). The β-terms cancel to (6/L) log β. |
| 6 | Cor 4.8 uniform tail e^{60.2-t/8}, :192-206 | STANDS | The count of images (L^4/4 plaquettes, each hit 4 times) and the exponent t/8 are correct. The constant is useful only for t > 481. |
| 7 | Lemmas 4.10-4.11 + Cor 4.12 (flat connections, shell simply connected, unique zero, nondegeneracy), :230-268 | STANDS | The tree induction and face gluing are correct. The unique zero with trivial shell data and T_int = 1 follows. λ_1 = 0.8377223 and λ_2 = 0.1471218 recomputed (P4; child B5). |
| 8 | Thm 4.13 uniform Laplace limit, :290-324 | STANDS | The global bound βS_R ≥ c|φ|² − 7M² holds on the whole chart (near region via E1-E2, far region via compactness and a Lipschitz shell perturbation). The TV limit is uniform in |ψ|≤M. η(δ) and K_N are not explicit, as the paper says. |
| 9 | Prop 4.14 (a) path/base-point independence, (c) invariances, (d) moments | STANDS | The random-gauge argument for the base point is correct and uses only gauge invariance of μ. |
| 10 | Prop 4.14 (b) Bianchi from the cube word | STANDS | The six words reduce to the empty word, checked symbolically (P5). The signs match the incidence numbers of d. |
| 11 | Prop 4.14 (e) Gaussian DLR in the limit | STANDS (presentation gap) | Conditioning at finite β is on links outside Λ'_R. In the limit it is on σ(F_q : q∉P_R), i.e. on curvatures only. Step 5 (ψ = 𝖫 dψ, 𝖫 injective) bridges the two. The paper says so only in a remark after the proof (:416). It should be part of the statement. |
| 12 | Lemma 4.16 (Dirichlet covariances increase to P) | STANDS | 7/24, 0.4926748 (mine and the child's) and 0.4991560 (child) reproduce the printed values. The sequence is monotone and below 1/2. |
| 13 | Lemma 4.17 (free field + constant background, independence) | STANDS | Lévy's downward theorem gives h. The characteristic-function identity with G_∞-measurable Y gives independence of ξ and h. The constancy argument is correct: Σ_e‖v_e−u‖² = 0 from harmonicity and equal L² norms. |
| 14 | Lemma 4.19 Wick inequality with random background | STANDS | Cov = (3/2)G(n)² + G(n)E\|f\|² + (1/4)Var\|f\|² rederived. Each term ≥ c(n) × its n=0 counterpart, because 0 < G(n)/G(0) ≤ 1. |
| 15 | Lemma 4.18 G(n) and its asymptotics | STANDS | G(0)=0.5, G(1)=0.06887475, π²8⁴G(8)=1.09244. The sequence is monotone for n=0..20. n⁶\|G−1/(π²n⁴)\| ≤ 0.86 for n ≤ 10 and the printed bound holds (it is ~4000× loose). Mine (P2, P3) and the child (A1-A8). |
| 16 | Assembly and "Consequently sup m_μ → 0" | STANDS | Contradiction argument plus Prop 4.4. |
| 17 | Theorem 3.5 (R′) | STANDS (trivial) | Laplace-transform facts. Requires 0 < T_β, which is not proved in the paper (cited to Lu77, "not read"). |
| 18 | Lemma 3.16 (density of ⟨W_4, R_ϑ⟩ in O(4)) | STANDS | Kronecker, conjugation, inverse-function theorem, connectedness and one reflection. Complete. |
| 19 | Theorem 3.11 (S) conditional chain | STANDS conditionally | Steps 1-8 are correct. Step 9 rests on a description of the reconstructed space that is "recalled, not read". Theorem 3.10 is read in a secondary source (KQR21). |
| 20 | Status table: "H0 proved" (sec_reduction.tex:395) | DEFECT (gap) | H0 asks RP for every bounded F in a half-space, in every site plane. Lemma 4.2(2) proves it only for continuous local F and only for {x_0=0}. The extension (L² approximation plus rotation invariance) is easy but not written. :405 instead cites OS78 "passes to weak limits", which is not immediate for non-local F. |
| 21 | Internal consistency: U(1) claims | DEFECT | main.tex:35 and :41 assert Thm 1.1 "holds, with the same proof, for U(1)" and "Both hold for U(1) as well". Section 2 item 6 (main.tex:57) says "Nothing is proved about gauge groups other than SU(2)". No U(1) proof is written, and the SU(2) constants (Weyl density, c_H, D*) change. |
| 22 | Internal consistency: Sec. 7 vs Sec. 4 | DEFECT | sec_negative.tex:623-627 calls the limit β(1−cos α_p) → ½Σ(F^a)² "a claimed step" and colour independence "not checked". Section 4 proves the first (Prop 4.14(d)). Lemma 4.17 says the background colours "may be correlated". |
| 23 | Lemma 5.12 hypotheses "(H1)-(H4)" | DEFECT | The names clash with H0-H4 of Thm 3.11. :403 says "(H1) [unique Gibbs state] is the standing assumption of the paper". That is false: the paper works with arbitrary limit points in 𝓛_β. |
| 24 | Section 8.7 "Review of this paper" | DEFECT | sec_paperreview.tex is the placeholder "(to be filled after the review of the assembled paper)". sec_provenance.tex:20 nevertheless says "The paper itself has had the corresponding review". |
| 25 | Observation 5.3 (S6 false) | DEFECT (overclaims) | S6 is a "for large β" statement and is itself imprecise ("a local perturbation argument applies"). At β=4 the negative-trace fraction 0.002 on a 3⁴ torus (486 plaquettes) means about one excluded plaquette per sample, where S6 asserts nothing. Several table rows lack sample counts. "False on every periodic box tested" should read "κ_H<0 on all 56 samples". |
| 26 | Observation 5.7 (vortex route) | DEFECT (wrong evidence) | The step under test is F_{L'} ≤ F_L for L \| L'. The SU(2) evidence quoted is F_4 − F_3 (3∤4, and L=3 is odd, outside Lemma 5.4). The relevant SU(2) comparison, F_4 vs F_2, has the predicted sign at both β. The Z_2 convention for β is not stated. |
| 27 | Observation 5.11 (abstract family) | DEFECT (not checkable) | The "abstract continuous family of spectral measures" is never given. |
| 28 | Observation 5.9 (negative amplitude) | STANDS (underspecified) | It does not say which direction has length 2, or that the 729 configurations are spins {0,½,1}⁶. Under the natural reading my independent MC gives −0.00318±0.00072 vs −1/324 (P7). |
| 29 | Observations 5.8, 6.1, 6.2 | STANDS as heuristic, imprecise | "No inequality of any kind is known" (5.8(2)) and "no argument that uses only P1-P6" (6.1) are not checkable statements. 6.2's headline "fails" rests on item (1), which is cited at abstract level only. Item (2) is numerical and the masslessness is not established. |
| 30 | Observations 3.6, 7.3, 7.7, 7.9 | STANDS | Precise and adequately qualified. 7.9 (Ising calibration) is off-topic. |
| 31 | Page 1 / direction-of-bound warning | STANDS on warning; DEFECT on layout | PDF p.1 holds only title, abstract and table of contents, so the theorem is on p.2. The abstract carries the warning ("upper bound … does not address whether the gap is positive"), and §1 states it right after the theorem. But main.tex:13 ends "the gap … must close. We prove that it does." This frames the result as progress before the warning. |
| 32 | Abstract/title vs content | DEFECT (understatement) | Lemma 4.17 is not in the abstract: every weak-coupling limit of the rescaled curvature field is a free Maxwell field plus an independent random constant. That is the strongest mathematical content and is hidden. The abstract also omits the review status and the shared-properties no-go. |

Counts (met, failed, measured only):
- Verdict table: 23 STANDS (some with nits), 9 DEFECT, 0 NOT CHECKED among the items listed. Items not checked are in a separate section below.
- My predicates P1-P7: 7 met, 0 failed, 0 measured only.
- Child predicates (A1-A8, B1-B5, C1-C2): see Delegation.

## 1. Summary (five lines)

1. Theorem 1.1 covers 4-d SU(2) Wilson theory and every weak limit μ of periodic dyadic-box states. As β → ∞, the normalized plaquette-energy correlation at time n is asymptotically at least (2G(n))², where G is the free lattice Maxwell field-strength correlation. Hence sup_μ m_μ(β) → 0: the transfer-matrix gap closes, an upper bound.
2. The method shows that every limit of the rescaled lasso curvature field is a free Maxwell field plus an independent random constant background (Lemma 4.17). Wick's theorem then gives the bound.
3. Two conditional theorems are included. Theorem R′ is trivial Laplace-transform facts. Theorem S states that H0-H4 imply OS-axiom Schwinger functions with gap ≥ 1. H0 and H2 are claimed proved, and H1 (= the lattice gap) is open.
4. Five routes to H1 are recorded with the step at which each fails, together with a no-go observation: U(1) shares P1-P6 and has no gap.
5. The paper was produced by AI sessions of one model family, with no mathematician review.

Do the title, abstract and introduction say exactly this?
- The direction of the bound is stated correctly in the abstract.
- The abstract understates: it omits the free-field-plus-constant-background structure, the explicit bound (G(n)/G(0))², the no-go observation and the AI/no-review status (which appears only in the date line and in §1).
- The introduction overstates on U(1) (item 21).
- The abstract's "five lattice hypotheses" are H0-H4. The paper also carries (A), (B), (C) and an undefined (E), and the reader must work out the mapping (H1 = (A), H2 = (B)). "Five attempted routes" matches §5.

## 2. Correctness of Section 4: details and named gaps

Overall I find the proof of Theorem 1.1 correct as printed, up to the minor gaps below. I found no step that fails.

- **Chessboard with plaquettes in reflection planes (Lemma 4.5, Cor 4.8).** The block function f = 1{O_{p0} > t} depends on a face lying in the planes x_3 = 0 and x_0 = 0. In each doubling, F ∈ 𝓗_+ for θ_a because blocks with t_j = a+L/2−1 reach the far plane, which is allowed (E_0 ⊂ 𝓗_+). Faces shared by S and θ_aS make the product contain repeated factors. The paper handles this only at the end: "each hit 4 times, and since indicators are idempotent" (sec_proof.tex:201). That is correct for indicators. The lemma itself is stated for general f ≥ 0, where the product carries powers, and that is also fine. Gap (nit): the case L = 2 is degenerate (item 1).
- **Free energy (Lemma 4.7).** Correct. The constant 60.2 is wasteful: the tail is vacuous for t < 481. Harmless for the proof.
- **Unique zero in the box gauge (Cor 4.12(1)).** Correct. Lemma 4.10's induction reaches T_ax, and T_int columns end at a single shell site.
- **Uniform Laplace limit (Thm 4.13).** The global lower bound is proved on the whole chart. It splits into 𝓝 (|x_l| ≤ δ) and 𝓝^c (compactness of 𝓚_δ, plus the shell perturbation |ΔS_R| ≤ 6√ν_s M/√β). It is uniform in |ψ| ≤ M because β_0(M) absorbs both requirements. I checked every constant (48δ²e^{8δ}, 24|ψ|², 7M², 12M²).
- **Limit field.** (b): the cube word reduces to the empty word (P5). The O_P(β^{-1/2}) transport correction uses (a). (c) and (d) are correct.
- **DLR in the limit.** What is conditioned on is σ(F_q : q ∉ P_R). This is curvature data, not links. The proof bridges the two via 𝖫F_sh (Step 5), and this is legitimate. Required change: state in Prop 4.14(e) itself that the limit σ-field is generated by curvatures only and that Ψ = 𝖫F_sh. Move the remark at :416 into the statement.
- **Free field + constant background.** Independence of ξ and f comes from conditioning on the tail σ-field G_∞ ⊂ G_{R_N} (:458). This is correct. Constancy (the Hodge Laplacian as a scalar operator, then the L² argument) is correct. It is attributed to "an independent check", so the source should be named.
- **Wick inequality with random background.** Correct. Its key point is that p_0 and p_n see the same f_12. The sentence at :461 ("for a background with f_{p_n} = −f_{p_0} the ratio can be negative") is good and should stay.
- **G(n).** Correct. The bound 14400/(π²n⁶) is about 4000 times larger than the true deviation for n ≤ 10 (P3). π²n⁴G(n) is not monotone (it peaks at 1.81 at n=3), so "1.092 at n=8" gives the reader no sense of the approach.

Numerical tests (mine, results/referee_checks_run1.txt): P1 D*, P2 G(0) and G(1), P3 asymptotics and the printed bound, P4 Dirichlet N=1,2 and λ_N, P5 cube word, P6 d=2 torus chessboard analogue, P7 amplitude. All 7 met.

## 3. Theorems 3.x

- **Theorem R′** is a correct conditional statement but nearly empty: the paper itself says "moves nothing" (:25, :100). It could be a remark. It needs T_β > 0 (Lüscher), which is cited and "not read".
- **Lemma 3.16** is complete.
- **Theorem S** is correct as a conditional. Steps 1-8 are proved in the text. The appeal to reconstruction (Thm 3.10, OS75 with E0′) matches the standard statement, as far as I know it from memory, not re-read; KQR21 is the secondary source. Two weaknesses:
  1. The identification ⟨Ψ, e^{-sH}Ψ⟩ = F_f(s) in Step 9 uses a description "taken from [OS73 §4] as recalled. It was not read" (:183). A journal would require the primary-source citation, with theorem number.
  2. s = D+6 must be an integer for E0′. Take D integer (nit).
- H0 is "proved" only with the gap in item 20.

## 4. Negative sections

Precision and evidence for each Observation are in items 25-30. The main faults:
- Obs 5.3: S6 is not precise enough to be refuted. The tested β includes samples outside S6's hypothesis, and 3⁴/4⁴ data are presented as "false on every box tested".
- Obs 5.7: the SU(2) evidence compares the wrong pair of sizes.
- Obs 5.11: the counterexample family is not given.
- Obs 6.1-6.2 are meta-statements about "arguments" and cannot be checked as written.
- Obs 7.9 (Ising calibration) does not bear on the paper's claims.
- Many observations carry provenance detail ("builder", "challenger", "the director's ledger", "another director's audit", "IDs 40-42") that belongs in §8, not in mathematical statements.

## 5. Presentation against the style sheet (STYLE_REPORT.md §4-5), and fit

- **Departures with good reason:** a "What is not claimed" section; heavy provenance; a status-word scheme for evidence.
- **Departures without reason:**
  - the abstract lacks the review-status sentence (rule 3 S4);
  - the title omits "and routes that fail" (rule 1);
  - the Jaffe-Witten clause is paraphrased, not quoted (rule 6);
  - no heuristic or outline section readable without the body (rule 9; §4.2 is inside the proof);
  - the hypothesis status table sits at p.15, not near the start;
  - Lean entries lack the per-file commit/sha and the verbatim axioms line (rule 16), and the Lean files are not in paper/;
  - references to internal repositories and an issue thread are cited for mathematical claims ([RepoB4], [RepoC4], [RepoThread]) by an author who "has not read their proofs" (main.tex:44). Remove the claim that the background vanishes, or move it to a clearly marked note.
- **Misleading by position:** PDF p.1 holds title, abstract and table of contents only. The theorem is on p.2. The warning is present (abstract, §1), but main.tex:13 "We prove that it does" precedes it with progress-like framing.
- **Length:** 43 pp. is too long for one theorem plus negative results. Cut §3.6 (free-field table), Theorem R′ (to a remark), §7.2 with Table 7 (Ising), and the provenance chatter inside §5. Shorten §3.3-3.4.
- **Missing:** a notation table. Symbols clash:
  - D: Lemma 4.16 matrix, D*, H3 exponent, constant in (C);
  - G: free correlation, G_β(t), test function g;
  - H1-H4: Thm 3.11 vs Lemma 5.12;
  - a: lattice unit vs reflection parameter vs a(k⃗);
  - μ: measure vs direction;
  - Λ_k vs Λ_L.

  Also missing: the precise official problem statement, quoted, and a hypothesis/status table on p.2.

## 6. Recommendation: MAJOR REVISION

The main theorem appears correct and is the paper's real content. The surrounding text has internal contradictions, an unfilled section, misstated evidence, and an abstract that hides the strongest result. Required changes, in order of importance:

1. paper/main.tex:35 and :41 vs :57. Remove "holds, with the same proof, for U(1)" and "Both hold for U(1) as well", or write the U(1) proof.
2. paper/sec_paperreview.tex:1 and sec_provenance.tex:20. Fill §8.7, or delete the claim that the paper has had the review.
3. paper/main.tex:8 (abstract). Add the free-field-plus-constant-background structure (Lemma 4.17), the explicit bound (G(n)/G(0))², and the AI/no-review status. State that the five hypotheses are H0-H4.
4. paper/sec_negative.tex:623-627. Delete "a claimed step" and "not checked", and cite Prop 4.14(d) and Lemma 4.17.
5. paper/sec_negative.tex:221-223. Replace F_4 − F_3 by F_4 vs F_2, which agrees with monotonicity. Withdraw "the wrong sign".
6. paper/sec_reduction.tex:395 and :405. Prove H0 as stated (all site planes, bounded F), or restrict H0.
7. paper/sec_negative.tex:387-404. Rename (H1)-(H4) of Lemma 5.12, and delete "standing assumption of the paper".
8. paper/sec_negative.tex:98-106. Restate Obs 5.3 as a measured fact (κ_H < 0 in 56/56 samples). Drop "false", or make S6 precise.
9. paper/sec_negative.tex:406-412. Give the spectral family of Obs 5.11 explicitly.
10. paper/sec_proof.tex:341 and :416. Put "conditioning on curvatures only; Ψ = 𝖫F_sh" into the statement of Prop 4.14(e).
11. paper/main.tex:44-45. Remove or quarantine the unread results of other groups ([RepoC4], [RepoB4], [RepoThread]).
12. paper/main.tex:13. Replace "We prove that it does." with a sentence carrying the direction warning, and add a notation table and the hypothesis-status table near p.2.
13. paper/sec_reduction.tex:183. Cite OS73/OS75 by theorem number from the primary source.
14. paper/sec_proof.tex:75-79. Exclude L=2 (start at k≥2).
15. Cuts: sec_reduction.tex:358-384 (§3.6), sec_negative.tex:640-670 (Ising), and provenance chatter in §5.

## Hypotheses each statement uses, and where stated

- **Thm 1.1:** SU(2), d=4, Wilson action, periodic boxes of side 2^k, μ ∈ 𝓛_β, plaquette p_0 spatial at time 0, order of limits box → β → n (main.tex:16-28; sec_proof.tex:5-17).
- **Thm R′:** abstract data with 0 < T_β ≤ 1, plus (A), (B), (C) (sec_reduction.tex:29-53).
- **Thm S:** H0, H1 = (A), H2 = (B), H3(a-c), H4, site-scalar fields, a = m (sec_reduction.tex:124-165, 185).
- **Lemma 3.16:** ϑ/π irrational.
- **Lemma 5.12:** its own (H1)-(H4) (sec_negative.tex:388-391).
- **Prop 5.2:** periodic torus, one plaquette.
- **Lemma 5.4:** even L.
- **Prop 5.5:** L/R and L/T powers of 2, KT02 plane placement.
- **Prop 7.1:** (C′).
- **Thm 3.10:** E0′, E1-E3 as read in KQR21.

## Failed predicates

None of mine (P1-P7: 7 met). Child predicates: see Delegation. The child reported two of its own run defects, a crash in A6 code and a too-slow C, with no predicate failure. Its notes classify both as its own defects, not defects of the target.

## What I did not check

- Lean files: not in paper/. Lean was READY at /home/user/z4-lean/READY, but I ran no Lean.
- Any cited source; no network was used. Checks I could not make include:
  - KQR21 §9.2.1 and eq. (9.18);
  - OS75;
  - FS82 (Z_N massless phase);
  - KT02 (11);
  - SZZ23 Thm 1.4;
  - literature priority. A referee would ask for comparison with known weak-coupling Gaussian approximations, e.g. Chatterjee's work on the leading term of the Yang-Mills free energy. That is from memory, not checked.
- The Monte Carlo tables of §5 and §7, except P7.
- Prop 5.2(ii) eigenvalues.
- Lemma 5.1's Bakry-Émery argument: read only.
- The free-field Table 6.
- The constant 14400 derivation: read and recomputed by hand only.

## Delegated questions and outcomes

- **Child T33** (admitted, log child_admit.log), sonnet, child/. Question: numerical tests of Section 4:
  - (A) G(n): both formulas, G(0), G(1), monotonicity, asymptotics, the printed bound, |g−g0| ≤ 3|k|³;
  - (B) Dirichlet C^N for N=1,2,3 and λ_N;
  - (C) d=2 U(1) torus chessboard analogue.
  - Control 1/(16π²): the child answered 0.006333, which is correct. I graded this before reading anything else.
- **Grandchild T34** (child's): independent recomputation of G(1). It returned 0.0688747458. The child reran it, getting 0.06887474584, a match to 4e-11, and released T34.
- **Outcome:** child/report.md reports 18 PASS and 0 FAIL.
  - Test A has 10 rows and test B has 6 rows.
  - Test C has 2 rows on the d=2 U(1) torus (L = 2, 4, 8; β = 0.5, 1, 2, 4; 144 points each):
    - C1: P(O_p>t) ≤ P(all)^{1/V}, met at 144/144. There are 26 ties within 1e-9, and the smallest margin is −2.2e-16 (roundoff).
    - C2: the free-energy form, met at 144/144. It is non-vacuous at 106 of them.
  - Counts: 18 met, 0 failed, 0 measured only. The A5b limit fit c0 = 1.00061 is an extrapolation; the child says so itself.
- **Grandchild T34:** released, per the child.
- **Rerun by me:** I reread and reran testA.py and testB.py (tag parentrerun, recorded as rerun-child-testA and rerun-child-testB in pcp/). All claims came out true, with numbers identical to the child's and to my P2-P4. I did not rerun testC.py; my own P6 tests the same statement independently (L = 2, 4; β = 1, 4) with 0 violations.
- **The child's own defects:** the first run of A crashed, and two attempts at C were too slow and were killed. No result file was left by those runs. These are its defects, not the target's.
- **Child task:** T33 released (child_release.log, event 70).

## Register verification (last lines)

- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.` The line before it is `guards replayed: 0 problem(s)`, and the register SHA-256 is 2313eb47….
- `pcpos verify child/pcp/register.jsonl`: same last line; SHA-256 9ce6fe45….

## Rerun commands (from /home/user/z4-workers/p5-ref)

```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name referee-checks-run2 --expect-exit 0 -- python3 referee_checks.py results/referee_checks_run2.txt
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
pdftotext -f 1 -l 2 -layout paper/main.pdf -
```
