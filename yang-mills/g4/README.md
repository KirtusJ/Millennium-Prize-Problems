# Reflection positivity under a common limit

Director G4, November 22, 2026. This is a component of the Yang–Mills construction program, coordinated at [the destination rendezvous](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1). It supplies no solution of the Millennium problem. A4 owns observable nontriviality, B4 the regulator transfer operator, D4 continuum spectral support, and C4 the global gauge group.

The [local plaquette study](local-scalar-edge/README.md) applies the positive transfer representation to the weight visible near the strong-coupling lattice mass and its recovery from two vacuum lags.

The [opposite-slice spectrum estimate](paired-slice-spectrum/README.md) bounds finite-volume excitation energies and thermal occupation from a histogram of two complete spatial slices.

The [growing spatial block](spatial-block-criticality/README.md) gives a uniform comparison with the free magnetic profile and an upper bound on the weak-coupling SU(2) gap in lattice units.

## Exact question and result

Let `I` be a common set of test labels. For a finite type `J`, a map `i : J → I`, real coefficients `c`, and a real kernel `K`, define

\[
 Q_K(i,c)=\sum_{a\in J}\sum_{b\in J}c_a c_b K(i_a,i_b).
\]

Suppose `K_n(x,y) → K(x,y)` for every fixed pair of labels, and every regulator kernel has nonnegative `Q` for every finite test. Then the limit kernel has nonnegative `Q` for every finite test. Finite sums commute with the given limits, and `[0,∞)` is closed. Repeated labels are allowed. Taking `J = Fin m` for each natural `m` covers all finite lists; this is not a check of a selected finite sample.

[ReflectionPositivity.lean](ReflectionPositivity.lean) formalizes this statement over Mathlib's real numbers. It also proves preservation when each fixed test is only eventually nonnegative. The eventual threshold may depend on the test. Neither theorem assumes or establishes a common convergence rate or existence of a convergent regulator trajectory. A PCP-hosted model returned a draft; G4 narrowed imports and repaired the finite-sum proof after its first elaboration timed out. See [execution.md](execution.md) for the actual verification state and corrections.

The statement is elementary and no novelty is claimed. Its purpose is to fix the interface that a proposed Yang–Mills regulator must actually satisfy.

## Controls and the missing hypotheses

The zero kernel passes positivity and gives zero for every test. It cannot supply the nonzero physical observable required by A4's lane. The symmetric matrix `[[1,2],[2,1]]` has strictly positive entries but gives `Q(1,-1) = -2`. Entrywise positivity cannot replace reflection positivity. Both controls are represented in the Lean source.

Positivity, normalization and clustering also do not force a spectral gap. As an analytic control, for nonnegative times set

\[
 K(s,t)=\frac1{1+s+t}
       =\int_0^\infty e^{-\lambda}e^{-\lambda s}e^{-\lambda t}\,d\lambda.
\]

Its finite quadratic form is the integral of `e^{-λ}(Σ c_a e^{-λ t_a})²`, hence is nonnegative. Its normalized correlator is `C(t)=1/(1+t)`, which tends to zero. The positive spectral measure `e^{-λ}dλ` gives positive mass to every interval `(0,δ)`, so it has no positive lower support gap. For any `m>0`, `e^{mt}/(1+t)` is unbounded; the quadratic term in the exponential series already suffices. Thus no finite prefactor makes `C(t) ≤ A exp(-mt)` hold for all sufficiently large times. This analytic control is not yet formalized here. It is a time-kernel example, not a Yang–Mills theory or counterexample to the Clay problem.

Full Osterwalder–Schrader reflection positivity is a complex sesquilinear condition on a positive-time test algebra, with a specified time reflection and conjugation. This initial file handles real finite kernels. The subsequent [complex extension](complex/README.md) proves preservation of both the reality and nonnegativity conditions, the sesquilinear laws, reflected finite-sum expansion, and exact finite pushforward transport. It includes a Hermitian kernel that passes real tests and fails a complex test. Identification of the actual continuum positive-time test algebra and the remaining reconstruction hypotheses stays open.

The [cross-lane review](cross-lane-review.md) checks C4's finite quotient calculation independently and states the exact pushforward identity needed to transport reflection positivity. It also records the scope of G4's source review of D4's spectral criterion.

The [integral extension](integral/README.md) supplies the Bochner-integral finite-test expansion and exact measurable pushforward, compact continuous Wilson normalization, and a conditional finite-Gram reflection-positivity criterion. Its [analytic Wilson-kernel application](integral/wilson-kernel.md) proves positivity for an explicitly split compact-group holonomy action using matrix features and uniform exponential convergence. Lattice reflection-plane geometry and the continuum construction remain separate obligations.

## Shared construction contract

The [shared-boundary extension](site/README.md) proves the exact partition-weighted mixture of normalized compact fibers and transfers a supplied fiber reflection inequality to the original joint Wilson-type law. It includes an exact rooted-reversal identity and a [focused C4 cross-read](site/cross-review.md) covering odd site seams, four-copy geometry and physical-time limit order.

The [reflected-tail theorem](block-recovery/README.md) bounds a translated magnetic block using its reflected difference. The [ordinary-profile audit](block-recovery/disposition.md) checks the growing root paths, finite-line cancellations and the order of the cutoff and block limits used in C4's free magnetic scaling calculation.

The [contact-field audit](contact-blocks/README.md) checks A4's fixed even-shift averaging under the joint microscopic tangent and moment estimates. Lean proves the weighted averaging and covariance row bounds. The written argument extends conditional convergence to the full six-component residual in local negative Sobolev spaces. The [literature comparison](contact-blocks/literature.md) checks the observable in the published plaquette estimates and identifies the established two-copy criterion used for conditional convergence.

The [site-plane projection](exterior/README.md) characterizes which sparse Wilson link masks preserve the gauge-invariant half-cylinder quotient. Keeping the spatial links on the reflection slice gives exterior representatives with the same physical transfer spectrum. A [two-time boundary measurement](exterior/spectral-test.md) certifies weight in a compact positive energy interval and distinguishes C4's fast and slow magnetic-angle trajectories under their stated hypotheses.

The [full-flow audit](flow-audit/README.md) confirms C4's periodic-cube and fixed-time Lie–Euler estimates. At lattice flow time 20 the difference between two spatial plaquette deficits on slices 1 and 2 gives a negative original-plane form on sufficiently large even SU(2) Wilson cubes with inverse coupling equal to the side. The [periodic partition bound](flow-audit/cube-and-flow.md) retains seam plaquettes and reduces the unmatched one-link factors to four.

All lanes must refer to the same gauge group, regulator trajectory, physical units, observables and limit. The following are outstanding construction obligations, not assumptions proved by this file:

1. Construct the four-dimensional gauge-invariant regulator and specify its positive-time observable algebra and reflection.
2. Establish the full reflected quadratic-form inequalities at each cutoff. Positivity of a transfer operator or of kernel entries alone does not discharge this step.
3. Give maps from a common continuum test algebra to regulator observables and prove convergence of all required pairings on one compatible limit. Separately chosen subsequences for different tests do not automatically give a single field theory.
4. Establish the remaining axiomatic properties and control the null-space quotient; connect the resulting Hilbert space and Hamiltonian to B4/D4's operators and spectral measure.
5. Prove A4's nontriviality and B4/D4's uniform positive decay or spectral estimate in physical units for that same construction, with C4's group scope.

The previous research program's finite record and positive-weight constructions are potential inputs only after an explicit map to these objects. No earlier finite model, coordinate relabeling result, or successful PCP record is imported as evidence of a four-dimensional continuum field theory.

The [Jaffe–Witten problem description](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf), §§4 and 6.5, requires a nontrivial theory for every compact simple gauge group and discusses reflection positivity of Wilson approximations and the separate limiting requirements. The present theorem isolates one preservation step; it does not discharge those limiting requirements.

The [spatial momentum tail of the fourfold packet](momentum-tail/README.md) bounds the weight at large scaled lattice momentum and gives its sharp sixth-power decay in the limiting distribution. The [coordinate tails](momentum-tail/directions.md) distinguish momentum in the plaquette plane from momentum normal to it.

For the 24-plaquette Wilson site scalar, the [gap-clock covariance and midpoint test](site-clock/README.md) give a positive normalization and enclosures from earlier even-time correlations. The [degree and precision bounds](site-clock/certificate.md) specify which Wilson inputs would decide the midpoint condition.

The [two-sided estimate for the Wilson midpoint ratio](site-clock/envelope.md) gives a limit inferior of at least $\sqrt e$. A4’s short-distance estimate supplies the upper bound, and the paired spectral controls show how large it may be with the available information.

For fixed periodic $SU(2)$ Wilson boxes, the [compact zero-mode calculation](periodic-zero-modes/README.md) gives the leading partition function and the logarithmic correction to the mean plaquette. It determines the weak-coupling step for this observable at two fixed lattice sizes. The [large-box limit of the coefficient](periodic-zero-modes/box-size.md) relates its finite part to the determinant of the unit flat torus.

## Reproduction

Use Lean `4.19.0` and Mathlib commit `c44e0c8ee63ca166450922a373c7409c5d26b00b`. From that Mathlib checkout:

```text
lake env lean /absolute/path/to/ReflectionPositivity.lean
```

The `#print axioms` statements make the checked dependencies visible. `run_worker.py` launches the bounded text-only model through the PCP Python host. `check_proof.py` creates a separate recursive program-check hierarchy and compiles both the accepted source and an intentionally invalid sign mutation. `calibrate.py` checks the selected runtime's completion guards. All scripts require explicit runtime, method and output paths; they do not install or silently select a PCP release.
