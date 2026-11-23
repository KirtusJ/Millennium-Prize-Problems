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
