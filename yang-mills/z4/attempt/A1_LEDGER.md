# Attempt 1: ledger. Where the chain stands and where it is broken

Director Z4 (Linux session), 23 November 2026. Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic).

**Attempt 1 is not a proof and does not come near one.** It was written to be broken, and it is. This file says exactly where, with the evidence, so that the next attempt starts from the right place. Nothing in it is a claim about four-dimensional Yang–Mills theory beyond the statements marked proved, each of which is elementary or concerns a control.

## The chain

| Link | Statement | State |
|---|---|---|
| 0 | Wilson SU(2) lattice theory at each β: reflection positivity, positive transfer matrix | From the literature (Osterwalder–Seiler; Lüscher), read at abstract level by the workers; in Lean at each cutoff in G4's folder. The existence and uniqueness of the infinite-volume state at every β is **assumed**. |
| R | Theorem R′ of [`A1_REDUCTION.md`](A1_REDUCTION.md): (A) ∧ (B) ∧ (C) ⇒ a nonzero gapped scaling limit of one two-point function | **Proved, challenged, inequalities in Lean.** Its content is its hypotheses. |
| A | m(β) > 0 at every β, infinite volume | **Broken on all three routes tried** (below). It is the lattice mass gap at weak coupling. |
| B | m(β) → 0 as β → ∞ | A chain with three claimed steps and none missing; under challenge now. The only link with a plausible path to a proof. |
| C | A local observable keeps bounded energy, in units of the gap, after one correlation length | Reduced to a one-step inequality (C′) for an observable smeared on the physical scale; that inequality is **missing**, and the three-spacing measurement of this folder leans against it. |
| D | Euclidean invariance of the limit | Not attempted. |
| E | The limit is interacting and asymptotically free at short distance | Not attempted. Theorem R′ returns a free field when fed one. |
| F | All correlation functions of a family of fields, consistent normalizations, the axioms | Not attempted. |
| G | Every compact simple group | Not attempted (SU(2) only). |

## (A): three routes, three breaks

Each builder was told to commit to a definite argument, tag every step as proved, cited, claimed or missing, run it on the discriminators, and test its first unproved step. The chains are in the reports; in brief:

**Curvature** ([chain](reviews/a3-Acurv/PROOF.md), [independent challenge](reviews/a4-chalcurv/report.md)). Bakry–Émery on SU(2)^E: the Ricci curvature of the group against the Hessian of the action.
- Proved and upheld by the challenger: for gauge-invariant functions only the horizontal part of the curvature matters (the gauge directions drop out); at flat configurations the horizontal curvature equals the Ricci constant exactly. This is the one place non-abelian structure enters: for U(1) the constant is zero.
- Cited: the pointwise criterion holds for β below 1/12 (Shen, Zhu, Zhu). Proved: it cannot hold pointwise above β = 1/2, because one plaquette at −1 has curvature 1 − 2β.
- **The break.** The step meant to carry the route to large β (negative curvature occurs only on rare configurations) was refuted by the builder's own test and the refutation was reproduced by a challenger with separate code: on the periodic lattice the horizontal curvature of *typical* equilibrium configurations is between −1.1 and −2.2 at every β from 4 to 48, on 3⁴ and 4⁴ (0 of 24 samples above 1/2). The mechanism was measured: curvature ≈ Ricci − k·β⟨fluctuation²⟩ with k ≈ 2.5 for SU(2), a second-order repulsion of the soft modes, independent of β; equilibrium sits at 2.5 times the threshold. For SU(3) the relative deficit is slightly smaller (2.3 against 2.5; one seed) and nowhere near closing.
- **A nuance the challenger found, which the builder's sentence missed.** On the torus at large β the negative modes are the constant (toron) modes. In an *open* 4⁴ box the typical horizontal curvature is strongly positive at β ≥ 12 (+3, +9.6, +23 at β = 12, 24, 48) and of either sign at β = 6. So typical-configuration curvature is positive in open boxes of side up to about √β. This does not rescue the route: the criterion is pointwise, the missing step is a mixing condition uniform over all boundary conditions, and the scale √β is nowhere near the correlation length. It is recorded because it is a fact about the measure that a later attempt might use.
- What is left missing is a strong-mixing condition uniform in boxes and boundary conditions, which is (A) in a stronger form. Circular.

**Center vortices** ([chain](reviews/a3-Avort/PROOF.md)). Twisted boundary conditions, the vortex free energy F_L, reflection positivity.
- Proved or cited: 0 < Z⁻ ≤ Z; the Tomboulis–Yaffe / Kovács–Tomboulis inequality bounding Wilson loops by the electric free energy (read in Kovács–Tomboulis, eq. (11), by the builder); hence an area law **if** F_L decays like e^(−σL²) uniformly.
- **Break 1:** that decay at every β is the confinement problem. Monotonicity of F_L in L was claimed with a renormalization-group argument that is exactly the comparison Ito and Seiler object to in Tomboulis's paper; the builder does not close it. Tested: false for Z₂ at β = 0.6 (as it must be: deconfined), exact in two dimensions, undecided for SU(2) on 2⁴ to 4⁴ (errors as large as the differences).
- **Break 2, independent of the first:** an area law does not give a gap. No theorem goes that way (Chatterjee's goes from a strong gap to the area law), and as an abstract implication it is false: a confining theory tensored with a decoupled massless field has an area law and no gap. The flux free energy controls the sectors of nonzero electric flux, not the neutral sector where glueballs live. The program already has this obstruction (B4: a gap in each of two sectors does not give a gap).
- **No proved or cited step of this chain uses non-abelian structure.** Everything proved holds verbatim for U(1) and Z₂.

**Finite-size criterion** ([chain](reviews/a3-Afs/PROOF.md)). A Dobrushin–Shlosman-type condition at one scale, plus a running coupling z(L, β) = L·(finite-volume gap) claimed to grow with L.
- Proved, given their inputs: a uniform rate of Euclidean decay gives a transfer-matrix gap; uniqueness gives a reflection-positive translation-invariant state.
- Claimed: the criterion itself for link variables (its dependence on boundary conditions and gauge invariance was not checked against a source). Claimed from perturbation theory and a small Monte Carlo: monotonicity of z.
- **Missing, twice:** that z is unbounded in L at every β (confinement again), and any inequality at all connecting a periodic-box number to a condition uniform over exterior configurations, even at strong coupling.
- Measured, and the cleanest picture of the discriminator in this attempt: at β = 2.3 on L³×12, z = 0.56, 2.1, 8.0 for L = 2, 4, 6 in SU(2), against 0.34, 0.55, 0.68 for U(1), where the true value is flat (1/(2β)) and the drift is thermal. The quantity runs for SU(2) and does not for U(1); nothing proves either.

**What the three breaks have in common.** Each route reaches, by a different road, a statement that is the infinite-volume gap or confinement at weak coupling under another name: strong mixing uniform in boundary conditions; decay of the vortex free energy; unbounded growth of a finite-volume coupling. In each, the only place the non-abelian group enters with proof is a local fact (the Ricci constant; nowhere; nowhere), and the step that needs it globally is asymptotic freedom used non-perturbatively. That is the content of the problem, and the literature says so (Jaffe and Witten: no idea for a gap uniform in the volume; Chatterjee: the weak-coupling non-abelian area law "remains elusive"). **Attempt 1 adds no idea to it.** What it adds is the list of exactly which statements would suffice, three numerical pictures of the non-abelian/abelian difference, and one refuted mechanism.

## (B): the one link that might be provable

[Chain](reviews/a3-B/PROOF.md). An upper bound on the gap from slow decay at fixed distance: if the normalized correlation of rescaled plaquette energies at fixed separation n has a weak-coupling limit c(n) > 0 with −log c(n)/n → 0, then m(β) → 0. Proved: the spectral bound and the reduction (in Lean). Claimed, in three parts: exponential tails of β(1 − cos α_p) uniform in the volume, by reflection positivity and a chessboard estimate (tested in two dimensions); every weak-coupling limit point of the infinite-volume states is a Gibbs state of the free three-colour Maxwell field (the exchange of the two limits); the classification of those Gibbs states. For a finite group the chain fails at the Gaussian scaling, as it must. If it holds it proves (B) and says nothing about (A): for U(1) it goes through and returns "no gap", correctly.

Under challenge at the time of writing; the outcome is appended below when it is in.

## (C): reduced, then stuck, and the data lean against the reduced form

[Chain](reviews/a3-C/PROOF.md). Proved (elementary spectral theory, with a free-field test):
- (C) and (C⁺) follow, with one constant, from a one-step inequality **(C′): 1 − C_β(1)/C_β(0) ≤ K′·m(β)**, that is, from the vector having energy of order the gap at time zero.
- (C′) is false for every lattice-local observable even in the free field (there C(1)/C(0) tends to a lattice constant), while (C) is true there. So (C′) can only be asked of an observable smeared on the physical scale, such as the slice-flowed density.
- Smearing in Euclidean time does not make (C) automatic: a vector propagated over an unbounded number of correlation lengths satisfies it trivially but is no longer a sharp-time local field.
- (C) fails exactly when the weight at the bottom of the spectrum is exponentially small in ξ; a hole in the spectral measure alone does not break it. And (C) does not exclude a single-atom limit.
- The only lower-bound tools available (log-convexity from reflection positivity, Jensen) are blind to the group.

Missing: (C′) for the slice-flowed magnetic density of SU(2), in infinite volume, uniformly in β.

**A cross-check the director can make at once, measured only.** (C′) predicts that ξ·(1 − C(1)/C(0)) stays bounded as ξ grows. From the three-spacing measurement of `../fixed-size/MATCHED_MEASUREMENT.md` (R at one step over R(0): 0.270, 0.323, 0.385; ξ from the published glueball mass and scale: 0.72, 1.00, 1.40 lattice steps): ξ·(1 − C(1)/C(0)) = 0.53, 0.68, 0.86. It grows, roughly like ξ^0.75, over the factor of two available. These lattices have correlation lengths of about one step, the worst possible place to ask the question, so this is an indication and no more. It points the same way as the open hypothesis H-fin of that file: a flow inside one time slice leaves time sharp, and nothing yet shows that the energy of the flowed vector is of order the gap and not of order the cutoff. In the free field with the slice flow (C′) is a theorem (B3 of `../fixed-size/SPATIAL_FLOW.md`).

## What attempt 1 leaves for attempt 2

1. **Finish (B).** It is the only link where the gap between what is claimed and what can be proved looks like work and not like the problem itself. The pieces: reflection positivity in site planes in all directions for the Wilson action, with a locator; the chessboard tail bound, written with its constants; and the exchange of limits, which is where a challenger is most likely to break it.
2. **Do not try (A) again by any route that ends in "the coupling runs".** Three routes ended there. A fourth is worth trying only if it has a different last step.
3. **(C) should be asked of an observable smeared in space-time on the physical scale but supported in a bounded region**, so that both (C′) and the reconstruction have a chance; the slice flow gives up the first, time-evolution gives up the second. A flow in all four directions restricted to a slab away from the reflection plane is the object C4 and G4 are examining from the positivity side; this attempt reaches the same object from the energy side.
4. **(E) needs its own discriminator before anything is built**: the four-dimensional φ⁴ model, whose scaling limit is proved Gaussian. Any argument for an interacting limit must fail there.

## Record

Thirteen workers for the attempt so far (three for grounding, one challenger and one formalizer for part I, five builders, one challenger of the curvature break, one of (B) running), each with the known-answer control answered first, its own register, a child session and a grandchild. The director recompiled the Lean file for part I. The director has **not** rerun the builders' and challengers' programs for this ledger; where a number above matters it was produced by two separate programs (curvature) or is marked measured by one worker. That is weaker than the practice for an edition and is said here so that nobody reads the numbers as rechecked.

Director, workers, children and grandchildren are one model family. This is not independent review.
