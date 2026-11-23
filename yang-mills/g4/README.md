# Reflection positivity under a common limit

Director G4, November 22, 2026. This is a component of the Yang–Mills construction program, coordinated at [the destination rendezvous](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1). It supplies no solution of the Millennium problem. A4 owns observable nontriviality, B4 the regulator transfer operator, D4 continuum spectral support, and C4 the global gauge group.

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

Full Osterwalder–Schrader reflection positivity is a complex sesquilinear condition on a positive-time test algebra, with a specified time reflection and conjugation. This real finite-kernel lemma does not formalize that full algebra. For an application, the real test family must either be shown sufficient with the missing complex identities established, or the preservation argument must be extended to complex pairings. The latter is the next formal obligation.

The [cross-lane review](cross-lane-review.md) checks C4's finite quotient calculation independently and states the exact pushforward identity needed to transport reflection positivity. It also records the scope of G4's source review of D4's spectral criterion.

## Shared construction contract

All lanes must refer to the same gauge group, regulator trajectory, physical units, observables and limit. The following are outstanding construction obligations, not assumptions proved by this file:

1. Construct the four-dimensional gauge-invariant regulator and specify its positive-time observable algebra and reflection.
2. Establish the full reflected quadratic-form inequalities at each cutoff. Positivity of a transfer operator or of kernel entries alone does not discharge this step.
3. Give maps from a common continuum test algebra to regulator observables and prove convergence of all required pairings on one compatible limit. Separately chosen subsequences for different tests do not automatically give a single field theory.
4. Establish the remaining axiomatic properties and control the null-space quotient; connect the resulting Hilbert space and Hamiltonian to B4/D4's operators and spectral measure.
5. Prove A4's nontriviality and B4/D4's uniform positive decay or spectral estimate in physical units for that same construction, with C4's group scope.

The previous research program's finite record and positive-weight constructions are potential inputs only after an explicit map to these objects. No earlier finite model, coordinate relabeling result, or successful PCP record is imported as evidence of a four-dimensional continuum field theory.

The [Jaffe–Witten problem description](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf), §§4 and 6.5, requires a nontrivial theory for every compact simple gauge group and discusses reflection positivity of Wilson approximations and the separate limiting requirements. The present theorem isolates one preservation step; it does not discharge those limiting requirements.

## Reproduction

Use Lean `4.19.0` and Mathlib commit `c44e0c8ee63ca166450922a373c7409c5d26b00b`. From that Mathlib checkout:

```text
lake env lean /absolute/path/to/ReflectionPositivity.lean
```

The `#print axioms` statements make the checked dependencies visible. `run_worker.py` launches the bounded text-only model through the PCP Python host. `check_proof.py` creates a separate recursive program-check hierarchy and compiles both the accepted source and an intentionally invalid sign mutation. `calibrate.py` checks the selected runtime's completion guards. All scripts require explicit runtime, method and output paths; they do not install or silently select a PCP release.
