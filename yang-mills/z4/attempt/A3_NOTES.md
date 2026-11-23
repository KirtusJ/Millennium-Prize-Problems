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
- "extrapolation 1.974" was a three-point geometric extrapolation and gives 1.97583, not 1.974; a two-term fit in β^(−2/3) gives 1.97496 ± 0.00003, against the continuum 1.974964.
- "center-odd splittings fall like exp(−c√β)" is not established: the data below double precision do not fix the form.
- Added: E₁ is an exact doublet (the model has an O(2) symmetry mixing Y₁ and Y₂; charge 2). The lattice splits it (0.19238 against 0.19331 at β = 1024), as the lattice symmetry D₄ requires. A child's claim that the continuum level is not degenerate was traced to an unconverged grid.

**Three directions** ([`reviews/g2-three/report.md`](reviews/g2-three/report.md)). Continuum operator −½Δ + 2Σ|Y_i×Y_j|² on R⁹, rotation-invariant functions, Rayleigh–Ritz: E₀ = 6.534885; first gap 3.012539 (a five-fold level, J = 2 under the O(3) mixing the three directions); gap to the first scalar 3.602838. The lattice model converged only to β = 4 (m_e = 2.876, 1.6215, 0.969 at β = 1, 2, 4; β = 8 not converged), where m_e·β^(1/3) is 2.88, 2.04, 1.54: not asymptotic. Nothing is measured about the three-direction limit.

**A scaling-limit theorem, upper half proved, lower half not yet** ([`reviews/g2-conv/SCALING_LIMIT.md`](reviews/g2-conv/SCALING_LIMIT.md)). With ν_k the eigenvalues of −log T on the center-even sector and K normalised to κ₀ = 1:
- tagged proved by its author: limsup β^(1/3) ν_k ≤ E_k for every k (trial functions transplanted from the continuum operator and symmetrized over the four center copies);
- tagged proved: five lemmas toward the liminf (comparison with 1 − K + V, localisation for the non-local K, a capped fibre lemma on the valley arms, tightness);
- only sketched: the Γ-liminf and the conclusion. So the lower bound m_e ≥ cβ^(−1/3) is not proved.
- Defect of my brief, found by the builder: with the unnormalised kernel I wrote, −log T is shifted by 3 ln β + O(1) and the statement about ν_k is false; gaps are unaffected.
- A coercivity inequality I suggested (1 − K + V ≥ β^(−1/3)(c(|sin a₁| + |sin a₂|) − C)) is false: 1 − K ≤ 1, so high-spin states at a₁ = a₂ = π/2 with a common axis violate it for every β. The weight must be capped; the lemma that replaces it is the capped fibre lemma.

None of this has been read by anyone but its author. A builder for the two sketched lemmas and a challenger for the parts tagged proved are running.
