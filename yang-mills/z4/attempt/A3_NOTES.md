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

## 6. A lower bound, sought in two places

Everything proved so far bounds the gap from above. Two probes went the other way.

**Strong coupling: the horizontal curvature criterion adds nothing, and is capped.** ([`reviews/f1-strong/STRONG_COUPLING.md`](reviews/f1-strong/STRONG_COUPLING.md).) The curvature route had left one proved fact that looked usable: for gauge-invariant functions only the horizontal part of the curvature enters. The hope was a gap for a larger explicit range of β than the published one. It fails. The proved range is β < 1/12, the same as Shen, Zhu and Zhu (their constant recovered exactly, with the normalization checked: our β is four times theirs for SU(2)). At the worst configurations the negative directions are horizontal, so restricting to them gains nothing; the worst configuration found has curvature 1 − 8β, and the builder proves that **no pointwise Bakry–Émery argument, horizontal or not, can pass β = 1/8**. The literature is already past that for the area law: Cao, Nissim and Sheffield (arXiv:2509.04688, read in full by the worker: Theorem 1.6, Proposition 3.2) reach β < 1/6 by applying the criterion to an auxiliary vertex model instead of the link measure. Dropped.

**Weak coupling: a rung, found by the wildcard, measured, and not proved.** ([`reviews/f1-wild/report.md`](reviews/f1-wild/report.md); proof attempt [`reviews/g1-toron/TORON_GAP.md`](reviews/g1-toron/TORON_GAP.md).)

> **Statement R1 (not proved).** For SU(2) Wilson lattice gauge theory on the cylinder with one spatial site in each periodic spatial direction and infinite time, the gap m_e(β) of the transfer matrix on gauge-invariant functions that are even under the center flips satisfies c·β^(−1/3) ≤ m_e(β) ≤ C·β^(−1/3) for large β. For U(1) on the same lattice the corresponding gap is exactly −log(I₂(β)/I₀(β)) ≈ 2/β.

Why it matters to the attempt: it would be the first lower bound on a gap at weak coupling in any geometry, and the first place where the non-abelian group enters a gap with a sign, at a power of β and not as an error term. The mechanism is that the commutator term of the action, which vanishes identically for an abelian group, turns the flat valley of commuting configurations into a confining one: the transverse zero-point energy grows linearly along the valley. In the continuum this is the matrix quantum mechanics with a commutator-squared potential, whose spectrum is discrete although the classical potential has flat directions (Simon 1983, cited by the worker from memory, not read).

Why it is small: at fixed box and weak coupling the physical box shrinks to a point. This is the small-volume regime, the opposite end from the infinite-volume gap, and nothing follows from it for (A). It is a rung because it is finite-dimensional, it is beyond everything the directors list, and it needs the one ingredient every failed route lacked: a rigorous treatment of a transfer operator near a degenerate valley with the group acting globally along it.

Evidence so far, measured only:
- Monte Carlo on 1³×64 (wildcard): m_e·β^(1/3) between 2.2 and 3.8 for β from 8 to 256, against U(1) values falling from 0.27 to 0.008; at β = 256 the SU(2) gap is 0.53(4) against 0.0078. The fitted exponent, 0.231, missed the worker's own window; its U(1) control passed at β = 4 and failed at β = 16 (under-equilibrated); the center-odd sector was not measured. A child's independent program reproduced two points.
- Exact Galerkin diagonalization of the two-direction model (proof worker), β ≤ 16 only: gaps 1.64, 0.76, 0.52, 0.54 at β = 2, 4, 8, 16, against 2.01, 1.07, 0.53, 0.26 with the potential switched off. So the gap stops falling between 8 and 16 while the potential-free one keeps falling like 1/β. The asymptotic regime is not reached.

**The proof attempt closed none of its four targets**, not even the weakest (that β·m_e → ∞), and says so in its first line. What it proved: an exact reformulation that avoids the wrong-direction operator inequality; a closed form for the potential in the two-direction model; a ground-state representation that reduces a lower bound on the *vacuum energy* to one pointwise inequality for a trial function; kinetic bounds from a cited Bessel-ratio inequality; five scalar steps in Lean. What is missing, stated exactly: (M0) that pointwise inequality; (M1) any control of the second eigenvalue, which needs either two-sided semiclassics at relative precision o(1) on the scale β^(−1/3), or a mixing bound for the ground-state Markov chain. The worker's own judgement: no soft route.

The director's reading: the continuum matrix model has a gap for trivial reasons once its spectrum is discrete, so R1 is a statement about convergence of the low spectrum of the lattice transfer operator, in the scaling variable, to that of the matrix Hamiltonian. That is a scaling-limit theorem for a compact operator on a compact group: localization away from the valley, the other center copies handled by parity, and resolvent convergence near the valley. It is hard and it is finite-dimensional. Whether to spend the program's effort on it depends on the exact numerics now running.

**The exact numerics, when they came in, were decisive for the two-direction model** ([`reviews/g1-num/report.md`](reviews/g1-num/report.md); figure [`figures/toron_gap.svg`](figures/toron_gap.svg), drawn by the Rust host's plot instrument from [`figures/toron_gap.json`](figures/toron_gap.json)). Diagonalization in the Peter–Weyl basis, no Monte Carlo: m_e·β^(1/3) = 2.063, 1.212, 1.031, 1.364, 1.636, 1.760, 1.837, 1.887, 1.919 at β = 2, 4, …, 512, and 1.939 at 1024; local exponents 0.228, 0.271, 0.295, 0.309, 0.318; successive increments shrink by a ratio near 2^(−2/3); extrapolation 1.974. The continuum operator −½Δ + 2|Y₁×Y₂|² on rotation-invariant functions, computed separately by Rayleigh–Ritz, has E₀ = 3.35053, E₁ = 5.32550, gap 1.974964. Controls: U(1)² through the same code to 5·10⁻¹⁵; the strong-coupling limit; the absolute normalization against a Haar Monte Carlo; every level converged to 3·10⁻¹¹ in the spin cutoff. Center-odd splittings fall like exp(−c√β) and are below double precision from β = 128. One worker, its child and grandchild; an independent recomputation by another method is running. Measured only: nothing is proved, and the identification of the limit rests on the agreement of two numbers to 0.05 per cent.

So the rung is worth the effort, and a second proof attempt, aimed at it as a scaling-limit theorem, has been commissioned together with the three-direction model.

## 7. The two-direction rung: reproduced, corrected, half proved

**Independent reproduction** ([`reviews/g2-numchal/report.md`](reviews/g2-numchal/report.md)). A second worker recomputed the two-direction spectrum by a different method (Nyström discretization in the class angles with Funk–Hecke partial waves, Lanczos) and agrees with the Peter–Weyl diagonalization to 4.6·10⁻⁹ or better at every β. The continuum numbers E₀ = 3.3505330, E₁ = 5.3254970 were reproduced. Two statements of mine in section 6 are corrected:
- "extrapolation 1.974" was a three-point geometric extrapolation and gives 1.97583, not 1.974; a two-term fit in β^(−2/3) gives 1.97496, against the continuum 1.974964. The "± 0.00003" I attached is a four-point fit with one residual degree of freedom; deleting either endpoint moves the value to 1.97503 or 1.97489 (A4's replay), so it is a comparison, not a certified limit.
- "center-odd splittings fall like exp(−c√β)" is not established: the data below double precision do not fix the form.
- Added: E₁ is an exact doublet (the model has an O(2) symmetry mixing Y₁ and Y₂; charge 2). The lattice splits it (0.19238 against 0.19331 at β = 1024), which the lattice symmetry D₄ permits. (I first wrote "requires"; A4's audit at `1860ed3` is right that the square group allows equal energies on the charge-two pair, so the splitting is measured, not forced. The same audit notes that the doublet being the lowest non-scalar branch is proved, while its position below the first excited scalar rests on the numerics.) A child's claim that the continuum level is not degenerate was traced to an unconverged grid.

**Three directions** ([`reviews/g2-three/report.md`](reviews/g2-three/report.md)). Continuum operator −½Δ + 2Σ|Y_i×Y_j|² on R⁹, rotation-invariant functions, Rayleigh–Ritz: E₀ = 6.534885; first gap 3.012539 (a five-fold level, J = 2 under the O(3) mixing the three directions); gap to the first scalar 3.602838. The lattice model converged only to β = 4 (m_e = 2.876, 1.6215, 0.969 at β = 1, 2, 4; β = 8 not converged), where m_e·β^(1/3) is 2.88, 2.04, 1.54: not asymptotic. Nothing is measured about the three-direction limit.

**A scaling-limit theorem, upper half proved, lower half not yet** ([`reviews/g2-conv/SCALING_LIMIT.md`](reviews/g2-conv/SCALING_LIMIT.md)). With ν_k the eigenvalues of −log T on the center-even sector and K normalised to κ₀ = 1:
- tagged proved by its author: limsup β^(1/3) ν_k ≤ E_k for every k (trial functions transplanted from the continuum operator and symmetrized over the four center copies);
- tagged proved: five lemmas toward the liminf (comparison with 1 − K + V, localisation for the non-local K, a capped fibre lemma on the valley arms, tightness);
- only sketched: the Γ-liminf and the conclusion. So the lower bound m_e ≥ cβ^(−1/3) is not proved.
- Defect of my brief, found by the builder: with the unnormalised kernel I wrote, −log T is shifted by 3 ln β + O(1) and the statement about ν_k is false; gaps are unaffected.
- A coercivity inequality I suggested (1 − K + V ≥ |sin a₁| + |sin a₂| − β^(−1/3), coefficient one on the weight; I first recorded it here with free constants c, C, in which form it is true and follows from A4's inequality (2)) is false: 1 − K ≤ 1, so high-spin states at a₁ = a₂ = π/2 with a common axis violate it for every β. The weight must be capped; the lemma that replaces it is the capped fibre lemma.

None of this has been read by anyone but its author. A builder for the two sketched lemmas and a challenger for the parts tagged proved are running.

## 8. The one-site rung is closed, by another director first

Director A4 posted written proofs of both missing statements of the small-box rung, for two and three directions, before the lower half here was complete: the vacuum energy is of order β^(−1/3) (`c5c1ea9`), and on the center-even sector β^(1/3)(1 − λ_j) → e_j, hence β^(1/3)·(gap) → e₁ − e₀ > 0 (`4966c89`). With all center sectors present the first gap is between exp(−C√β) and exp(−c√β) (`dd2927a`), so the β^(−1/3) bound is a statement about the center-even sector only.

What was done here:
- **Cross-review of A4's two proofs** ([`reviews/h1-a4/report.md`](reviews/h1-a4/report.md)): 30 items; 27 stand, none defective, 3 not checked (one check program needs a library absent here; the three-direction limit was not computed; the cited pages were not fetched). One wording slip ("concavity" where the chord bound for a convex function is used). Both Lean files rerun: exit 0, standard axioms, scalar lemmas only. The fibre inequality I − K_j + V_ij ≥ c·r was computed on a discretised fibre: lowest eigenvalue over r at least 0.976 on [h, 1] at β = 64 and 256. The exact two-direction numerics extrapolate to 3.3537 and 5.3316 against e₀ = 3.3505 and e₁ = 5.3255.
- **A second proof of the two-direction limit, by a different architecture** (partition into four center boxes and capped arms rather than a walk estimate): upper half [`reviews/g2-conv/SCALING_LIMIT.md`](reviews/g2-conv/SCALING_LIMIT.md), lower half [`reviews/h1-liminf/LIMINF.md`](reviews/h1-liminf/LIMINF.md), challenged in [`reviews/h1-chal/report.md`](reviews/h1-chal/report.md): 11 steps stand, 1 defect (a sign in the localisation formula for the non-local kernel; the bound used survives), one constant derived wrongly (corrected to 79σ²), one partition function that was not Lipschitz (replaced). I reran the Lean file (nine scalar lemmas, exit 0, standard axioms) and the scalar program (digest identical).
- The reviewers here share the director's model family; A4 does not. The proof by A4 and the proof here are independent in architecture and in lineage; neither has been read by a person.

**What the rung is worth.** It is the first lower bound on a gap at weak coupling in this program, and it is at fixed volume: one spatial site. On an L³ box the constant modes carry a factor L³ in both terms, so the same limit predicts a gap near e·β^(−1/3)/L, which tends to zero with L at fixed β. The route does not reach hypothesis (A); it is the lattice form of the small-volume expansion (Lüscher 1983). In Lüscher's normalisation (Y = 4^(−1/6)c) the three-direction numbers of section 7 become 4.1167196 for the ground energy and 1.89778, 2.26965 for the first two gaps; the first agrees with the published ε₁ = 4.116719735 (van Baal, "QCD in a finite volume", hep-ph/0008206, text after eq. (12), read in full; difference 1.5·10⁻⁷, inside the rounding of our value). The two gaps could not be compared: the Lüscher–Münster paper (Nucl. Phys. B232 (1984) 445) was reached only as an abstract. The absence of a J = 1 level, which our ordering (J = 2, then J = 0) presupposes, is in the literature (Ambroziński, arXiv:1408.2655, App. B, after Lüscher–Münster). Record: [`reviews/h2-ground/report.md`](reviews/h2-ground/report.md).

**Grounding of the ceiling** (same record). The conversion to the lattice box was rederived: constant modes on L³ give (βL³)^(−1/3)·h₃ exactly at leading order, so m = e·β^(−1/3)/L, Lüscher's g^(2/3)/L with identical coefficients (bare coupling; the literature uses the renormalised g(L), equal at leading order). The literature puts the end of the regime at z = mL of order one: boundary effects of the fundamental domain from z > 0.9 and a crossover near z ≈ 2 (van Baal pp. 11–15; Lüscher–Münster abstract). No theorem giving a lower bound on the finite-torus gap at weak coupling, uniform in anything, was found; no proof of the discrete-time one-site limit was found; no published spectrum of the two-direction operator was found. The searches were limited (the arXiv and INSPIRE phrase queries returned nothing even where they should have), so "not found" is weak.

A caution for readers of the review cited: it calls 4.1167 the lowest-order "mass of the scalar glueball"; in its own eq. (12) and in our computation it is the ground energy, not a gap.

## 9. The tunnelling exponent of the two-direction model: a heuristic value, and a measurement beyond double precision

A4's two-sided bound e^(−C√β) ≤ m_χ ≤ e^(−c√β) leaves the coefficient open. A heuristic gives one. With one link at class angle a on the valley, the two transverse directions of the other link are a discrete-time oscillator with exact ground energy ε(a) = arccosh(1 + 2 sin²a) = 2 asinh(sin a), of order one in lattice units (so the continuous-time value 2 sin a is wrong away from the centers). The slow link walks with Gaussian steps of variance 1/β; for ψ = exp(−√β S(a)) the step integral is exact and gives S′²/2 = ε − E. Hence

 −log m_eo = c√β − E₀·d·β^(1/6) + O(log β),  c = ∫₀^π √(2ε(a)) da = 4.6054132,  d = ∫₀^π da/√(2ε(a)) = 2.6828,  E₀·d = 8.99.

Not proved: the WKB step; that the optimal path keeps the other link at a center.

Measured ([`reviews/i1-tunnel/report.md`](reviews/i1-tunnel/report.md); double-double arithmetic, the four double-precision values reproduced first): m_eo = 6.8644·10⁻¹⁴, 1.4597·10⁻¹⁶, 4.1266·10⁻²¹, 5.4032·10⁻²⁵ at β = 96, 128, 192, 256 (the last digit at 256 not guaranteed by the worker's own error bound); m_oo/m_eo = 2.00000. Local slopes d(−log m)/d√β: 3.99, 4.06, 4.12, 4.17, rising. A free fit c√β + qβ^(1/6) + k over β ≥ 96 gives c = 4.599, q = −7.8; with c = 4.6054 fixed, q = −8.1 (predicted −8.99, about 12 per cent off, with four points and a log term unresolved). With the continuous-time c = 4.7926 forced the residual is five to six times larger and the other parameters drift. So the data favour 4.6054 over 4.7926; they do not establish it. The worker and its child derived ε and the WKB relation separately and agree; they share my model family. My brief's remark that the E-correction diverges at the ends was wrong (the integral converges), and my size estimates for the splittings were too small by up to five orders.

## 10. The three-direction limit, measured

A Monte Carlo measurement of the one-site three-direction model ([`reviews/i1-mc3/report.md`](reviews/i1-mc3/report.md); 32 independent chains per β, variational analysis of four center-even operators per channel, plateau rule fixed before the runs). Controls: the exact gap at β = 2 (1.6291 ± 0.0132 against 1.621505; the child's separate code 1.620 ± 0.013) and at β = 4 (0.96904 ± 0.00380 against 0.96893, with a differenced correlator adopted after the raw one showed a constant floor: a defect of the first method, kept); the two-direction pipeline at β = 256 (1.9019 ± 0.0084 against 1.887, 1.8 σ high). The control at β = 1 failed its plateau rule.

m·β^(1/3), channels E, T₂, A₁ (predictions 3.0125, 3.0125, 3.6028):
- β = 64: 2.747(10), 2.813(13), 3.225(36)
- β = 256: 2.901(11), 2.938(7), 3.453(16)
- β = 1024: 2.955(9), 2.973(8), 3.524(17)
- β = 4096: 2.992(13), 2.989(13), 3.544(27)
- β = 16384: 2.988(23), 2.984(23), 3.568(48)

The pre-registered checks were met: within 8 per cent at β = 4096 in all three channels (−0.7, −0.8, −1.6 per cent), and the deviation shrinking from β = 64. The E–T₂ splitting falls from 0.28(4) at β = 16 to zero within errors from β = 1024. The approach is from below, as in two directions. This supports the three-direction case of A4's limit and the continuum numbers of section 7; it is a measurement at 1 to 2 per cent, not a proof.
