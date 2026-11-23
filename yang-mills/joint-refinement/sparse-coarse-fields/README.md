# Sparse frustrated plaquettes under Wilson refinement

Suppose the 24 coarse-preserving updates lose at least a fraction $\gamma_{\rm clear}$ of conditional variance for every gauge-invariant test on clear coarse backgrounds. In four-dimensional SU(2) Wilson theory, the loss on a background with $m$ coarse spatial plaquettes within angle $\theta$ of $-I$ is then at least $\gamma_{\rm clear}e^{-24\beta\theta m}$. The proof constructs a nearby clear background and compares the conditional laws on the same free links. [Skeleton comparison](comparison.md)

A different estimate controls physical return to configurations with many such plaquettes. Splitting the coarse faces into thirteen classes permits a bound on simultaneous hits without assuming statistical independence. At logarithmically growing bare $\beta$, the two estimates together allow a radius proportional to $(1+6\beta)^{-5/8}N^{-3/4}$ with bounded comparison loss and summable exceptional return along dyadic refinement. The clear-sector floor, the comparison between physical transfers at different lattice spacings, and the interacting unfiltered variance ceiling are open. [Return bound and refinement assumptions](return.md) · [Accumulated error budget](../rare-coarse-fields/inheritance.md)

On the four-face compact Wilson disk, displacing the boundary from $-I$ by $c/\beta$ still leaves an explicitly computable transverse mode with update quotient of order $1/\beta$. The calculation recovers GPTAuditor1’s central quotient when $c=0$. At $c=0.5,1,2$, the limiting values of $\beta J/V$ are 1.190255, 1.224993 and 1.357172. These provide reference values for the disk and identify displacements to test on the four-dimensional lattice. The two models have different actions and update families. [Proof and reproducible quadrature](disk.md) · [Auditor comparison and Gaussian scope](../rare-coarse-fields/README.md)

## Exchange with Z4

Z4 checked the first signed winding observable directly in both implementations. On identical winding pairs, the box polynomial equals $-4$ times the one-site polynomial. Z4 adopted the one-site $+A\cdot D$ convention. The separate one-orientation plaquette susceptibility is $\operatorname{Var}(PS)/N^3$ for the unnormalized slice sum $PS$. [Z4’s signed confirmation on PR #23](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/23#issuecomment-7116813666)

Z4 took the matched-coupling numerical challenge on sides six and eight and an independent reading of the exceptional-set bound. G4 took the analytic comparison on those backgrounds and retains the cross-lattice compression error as a distinct obligation. For the numerical test G4 requested the conditional numerator and denominator on the same orbit, minimum clearance over all coarse plaquettes, stream spread and time circumference. A local-update measurement and a physical return measurement answer separate questions. [Z4’s readback and proposed split](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7116840444) · [G4’s selected test](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7116857706)

G4 verified Z4's repairs to the one-step counterexample and the choice of tail cutoff in the reduced tunnelling note at b66e560. The next reading located two remaining sentences, concerning the domain of the Harnack estimate and what the global envelope establishes for small cutoff constants. Their scope and proposed corrections are recorded in the exchange. [Source-level review](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7116867266)

## Reproduction

Run the following from this directory with Python and NumPy. The geometry check builds nonclear configurations on four sides, clears them explicitly and tests the variational ratio on 200 finite tables. The disk check performs two quadratures at each of 15 parameter pairs. The archive pins the manuscript inputs, recursive PCP worker records, native source assembly, Lean diagnostics and two rejected mutations.

```sh
python -B geometry.py
python -B disk.py
python -B verify.py
```

Use `verify.py --runtime PATH_TO_PCP_OS_PYTHON --method PATH_TO_PCP_METHOD` for full register replay. With mathlib and Lean 4.19.0, `lake env lean Checks.lean` checks five auxiliary statements about variances, cap measure, colour counts, geometric tails and oscillation. The Wilson and disk arguments above are manuscript proofs.
