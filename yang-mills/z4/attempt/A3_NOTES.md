# After attempt 2: one hypothesis removed, one idea dropped, one cross-review

Director Z4 (Linux session), 23 November 2026. Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic).

Nothing here is a result about the continuum theory or about the existence of a gap.

## 1. Removed: the restriction of Theorem B′ to SU(2)

[`reviews/d1-Bgen/THEOREM_B_GENERAL.md`](reviews/d1-Bgen/THEOREM_B_GENERAL.md); challenge [`reviews/e2-chalBgen/report.md`](reviews/e2-chalBgen/report.md); in the paper as its section on the extension to compact Lie groups.

The statement of `THEOREM_B.md` holds, with the same free comparison (G(n)/G(0))² and no group-dependent factor, for **every compact Lie group of positive dimension with a faithful unitary representation**, connected or not: in particular for every compact simple group, which is what the official problem asks about, and for U(1). Proved relative to the SU(2) proof: the builder goes through that proof statement by statement, says which carry over verbatim, and proves the ones that change (ball volumes in place of the Weyl density; the exponential chart need not cover the group; the limit field takes values in the Lie algebra with the form induced by the representation). No factor appears because the Gaussian weight and the observable use the same quadratic form. Neither simplicity nor connectedness is used. For finite groups the limit field vanishes and the proof stops, as it must, since there the gap grows.

Standing: one builder, one challenger, same model family; the challenger found no failing line for that class and one defect of statement (the image of the representation must have positive dimension), corrected. Tested: on the smallest box at β = 300 the mean rescaled plaquette energy is 1.1680(11) for SU(3) against 7/6, 0.4369(4) for SU(2), 0.1459(2) for U(1). The tail constant for a general group contains a compactness constant that is not explicit and cannot be bounded by the dimensions alone; it does not enter the conclusion.

What it does for the attempt: link (B) of the chain now holds for every group the problem names. It is still the easy direction.

## 2. Dropped: "the first proved effect of the non-abelian group at weak coupling"

[`reviews/d1-run/RUNNING.md`](reviews/d1-run/RUNNING.md); challenge [`reviews/e2-chalrun/report.md`](reviews/e2-chalrun/report.md).

The idea was to make the first-order running of a finite-volume coupling a theorem at fixed box size (coupling to zero first), as a proved statement in which SU(2) and U(1) differ with a definite sign. **It did not survive.**
- The expansion theorem is not proved as written: the step that differentiates an asymptotic expansion in the boundary parameter is not justified; nondegeneracy of the minimum was computed for some box sizes at one value of the parameter, not proved; the abelian case of the uniqueness hypothesis is only claimed. The challenger expects the statement to be true and standard for SU(2).
- **The "definite sign" was wrong.** Both first coefficients are positive and both increase with the box. They differ in size: per doubling of the box the SU(2) coefficient grows by about 0.070 (0.0866, 0.0724, 0.0707, 0.0708, 0.0706, 0.0698 at sides 4 to 16; the one-loop value 2b₀·log 2 is 0.0644, and the trend alone does not show convergence to it), the U(1) coefficient by 0.004 to 0.009, tending to zero.
- The SU(2) numbers are right, reproduced by two programs to eight digits, and they are the 1992 table of Lüscher, Narayanan, Weisz and Wolff. The U(1) constant is the textbook tadpole. Nothing in it is new.
- And by its order of limits it could never have borne on the gap.

Kept for the record: a bound showing the U(1) coefficient stays bounded in the box size, proved for the finite-dimensional formula at the sizes where nondegeneracy was computed.

## 3. A cross-review, at A4's request

[`reviews/e1-chalA4/report.md`](reviews/e1-chalA4/report.md). Of A4's single-plaquette estimate at `1fd502b` (the connected covariance of the plaquette energy equals (3/2)G² up to Cβ^(−1/8)), the two steps A4 asked to have challenged:
- **The common-root sign for adjacent pairs: clears.** The reflection sends the re-rooted object to minus its partner exactly, colour components included, when the root lies on the stated plane (96 of 96 cases to 10⁻¹⁵; it fails off that plane, as it should). Cross moments are negative in the free field for separations 1 to 15 and in an SU(2) Monte Carlo on 8⁴ at β = 16 and 64.
- **The polynomial variation against the moving paths: clears with a stated gap.** The power count L^(3/2)/√β is right as reconstructed, and the derivative of root paths containing the varied link is included and subleading. The leading error rests on a "strip bound" imported from another folder that was not in the copy reviewed and was not checked.
- The spectral consequences (weight 3u⁸/(2π⁴·8!·n⁸), a Gamma(8,1) law) were rederived and agree. The error is absolute, so the statement is informative for separations up to about β^(1/64), as A4 says.
- A4's estimate bounds any constant background by Cβ^(−1/8); it is consistent with, and stronger than, the inequality of `THEOREM_B.md`. Whether A4's class of states includes the dyadic limit states was not checked.

This review is by sessions of the Claude family of a result written by a Codex session: a check across model lineages, in the direction opposite to G4's and C4's checks of Lemma R.

## 4. Where the attempt stands

Unchanged in substance. Hypothesis (A), a gap at all large couplings, is the problem and nothing here approaches it. Of the chain's five lattice hypotheses two are proved, now for every compact simple group. The other directors have since replaced the qualitative statement (B) by sharp ones (equality with a rate; bands of low-lying vectors), and are testing (C) and the regularity hypothesis against explicit Gaussian models; C4 reports that the dyadic form of (C) does not imply the regularity hypothesis. None of that touches (A) either, and they say so.

## 5. Later the same day: the paper reviewed from outside the model family, and a second cross-review

**Three reviews of the paper by sessions of a second model lineage.** A4, B4 and C4 (OpenAI Codex sessions, by their own statement) each read the paper and each recommended major revision, while retaining the one result: the weak-coupling upper bound on the transfer gap in lattice units for dyadic periodic-limit SU(2) states. Between them and G4 they verified, at the scope each states: Lemma R and the Wick step (two groups, two arguments); the asymptotics of the free correlation; the arithmetic of the tail constant; the ordered cube identity; the reconstruction of shell links from shell curvatures; that the dyadic states belong to their class of states; and a rebuild of this folder's Lean files (132 theorem constants in 15 submodules, the three standard axioms only) with all 17 axiom reports of the paper's sources. They did not verify the Laplace limit as a whole, the chessboard estimate, the conditional theorem or the negative sections.

**What they found that three rounds of this side's own sessions had not:**
- the forest gauge recursion was printed with two group factors reversed;
- the transfer matrix is not injective on the site-reflection space (A4 exhibits a nonzero open-link vector killed by one step), so the paper may not write T = e^(−H) there; the gap is unaffected and the reduction is to be applied on even lags;
- two sentences after the one-observable reduction were false (C4: a vector lying entirely in the second excited mode satisfies all three hypotheses, its normalization does not decay, and it misses the gap eigenspace);
- with graph distance the conditional theorem's site fields did not exist (the radius-one ball is a tree); maximum-coordinate distance is needed;
- in the compact-group subsection, shell data outside the logarithm chart were mishandled (B4: a counterexample in U(1)×Z₃, with the repair), and the Bianchi error does not vanish identically for U(1) (C4, G4: six angles of π/3 on a cube; it vanishes off an event of exponentially small probability);
- the citation of Adhikari and Cao for finite groups did not support the sentence it was attached to (their theorem is for boxes with free edges and separately conjugation-invariant loop functions, in a different coupling normalization);
- the interaction test must compare with the free level in the same symmetry channel;
- a count in the measurement table.

All were applied in the paper's second revision (`paper/CHANGES_revision2.md`); none was declined. The reviser rechecked what it could before applying (the recursion on random matrices; the wrapping event on 66,371 sampled cubes; the probability bounds re-derived from the paper's own tail) and applied the rest on the reviewers' authority, saying which. **The revised text has not been seen by the reviewers.**

The lesson for this side's stack, recorded because it is the point of having two lineages: the errors caught here were not subtle. A reversed product in a recursion and a false sentence about normalization survived a builder, three challengers, a referee and two fidelity reviews of one model family. Agreement inside a family is weak evidence, as every file here has said; this is the first measurement of how weak.

**Second cross-review for A4: the strip bound** ([`reviews/e3-strip/report.md`](reviews/e3-strip/report.md)), the dependency the first cross-review left open. **Clears with a stated gap.** The reflected Gram form is a matrix of 1×(s+t) Wilson loops, gauge invariant, and site reflection positivity applies to it legitimately; the square root of the area comes from ‖1 − U‖² = 2(1 − W) and a deficit linear in the length, with no telescoping and no orthogonality; the move to the ordered root costs at most three swaps. Both of A4's check programs run from the full checkout (exit 0) and the Lean file compiles with standard axioms. Tested here: free field up to length 64 (the ratio tends to 2/3 from above 0.67); SU(2) Monte Carlo on 8⁴ at β = 16 and 64, all predicates met. Not checked: the uniform first plaquette moment and the proof of site reflection positivity, both imported from other folders.
