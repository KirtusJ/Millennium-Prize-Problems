# Proof coverage and reproducible controls

The research result is the finite Wilson-law bound and its two-sided exponent under the spatial and coupling hypotheses. The full proof is in the mathematical notes. Lean checks the isometric path inequality and the finite algebra and probability estimates listed below. The numerical controls use finite matrices, conditional Wilson integrals and original compact link configurations.

| Checked in Lean 4.19.0 | Analytic step using that result |
|---|---|
| Telescoping along a walk for any isometric monoid action, the complex SU(2) spinor defect identity, four-edge square bound | Spinor transport around an oriented plaquette and cell coercivity |
| Iteration of conditional event bounds, majority-event coefficient | Haar small balls and domination by one-link conditional laws |
| Small and large cell estimates, scalar good-site fraction | Scalar Neumann Poincaré inequality and comparison of quadratic forms |
| Finite derivative sum, physical-clock cancellation, positive-band and eigenvalue-count estimates | Covariant finite-matrix derivatives, scalar heat domination, min–max, Golden–Thompson and the Hamiltonian vacuum form |
| Rare-cube cost balance, taking logarithms of the two-sided $3/5$ estimate, and weighted Cauchy–Schwarz on a rare event and the budget for an outside test after conditioning | Sine trial, two-sided exponent, probability-zero limit after normalization and moment growth |

The compact Lie group sublevel argument, the finite-volume spectral tail and the limiting rates remain analytic. The stronger estimates are for the charged particle's spatial operator in the actual Wilson ensemble. The nontrivial continuum gauge theory and its physical mass gap remain open.

## Worker roles and integrity

The root of the hosted PCP OS recursion desk delegated generation to a child, which delegated to two grandchildren. The compact-links worker recomputed the cube geometry, conditional laws and spectral controls. It emitted the small-cube Lean certificate and sent three geometry bytes to the second grandchild. The latter booted the pinned native PCP kernel, computed the two anchor constants from the vertex, path and face counts, and emitted its Lean proof. A second measured kernel boot assembled both outputs into a basis with the two regions removed. The root checked source byte equality and then invoked host Lean. The final post-exit desk lists all four workers as finished. [Desk runner](replay.py) · [Compact-link worker](controls.py) · [Native worker](certificate.c) · [Machine read-back](readback.txt)

All sixteen printed declarations use only the three standard axioms recorded in the read-back. The run rejected five changes inside the affected declarations. They replaced four by three on the four-edge path, charged four rather than five variances in the good-site bound, reduced the rare-cube cost constant from five to four, reduced the small-cube constant from 256 to 255 under its stated scalar premises, and dropped the factor of four from the large-block anchor. For the rare-cube change, take $u=L=1,m=1/2,x=1$; the actual cost is $4+1/8$. The 256 rejection tests the stated comparison inequalities and makes no assertion of optimality on a real gauge cube. [Formal source](HeatTrace.lean)

## Independent controls

- **Original four-dimensional weights.** On a $3^4$ periodic spacetime SU(2) lattice, the worker changed nine individual spatial links. It compared the difference of two complete Wilson exponents with the prediction from the six incident staples and four quaternion basis evaluations. The largest discrepancy was $3.2\times10^{-14}$. Direct one-link radial integration from staple strength zero to 6000 checked the conditional small-ball normalization, including at strong concentration.
- **Spatial covariant derivatives.** On a unit cube all 36 generator derivatives of the Dirichlet heat trace were compared to central differences. Maximum discrepancy was $1.5\times10^{-11}$. Independent rotations at each vertex changed the trace by less than $7\times10^{-16}$. The full Dirichlet energy exceeded the internal-edge energy, as required by the boundary convention.
- **Free-boundary coercivity.** An unrestricted SU(2) Neumann matrix on $4^3$ sites had lowest eigenvalue 0.865426 in lattice units, against a conservative floor 0.0022584 derived from the observed half of the disjoint small cubes. In the adjoint control one holonomy defect Gram has minimum zero and two orthogonal half-turns give four. On three nearly flat Dirichlet cubes the sine-spinor Rayleigh quotient lay between the observed least eigenvalue and its analytic upper bound.
- **Nonconstant response and normalization.** With physical diffusion time 0.04 in an embedded Abelian magnetic field of strength 18, the curved-to-flat heat-trace ratio on grids with 6, 12 and 24 interior sites per spatial side was 0.952655, 0.935157 and 0.930355. The observable can distinguish smooth configurations. A separate one-square Wilson control used Haar radial quadrature and all four twisted Fourier modes per color. From $b=1/4$ to $b=1/32$ its mean heat trace decreased from 0.649885 to 0.00968687, while its mean-normalized second moment rose from 1.64778 to 74.7260. Its physical support shrinks; these values do not estimate the fixed-domain exponents. The latter are consequences of the upper and lower bounds.

An adverse two-state example with arbitrarily small marginal event probability gives correlation one between identical inside/outside unit tests when the outside completely reveals the event. Enforcing the conditional probability bound restores the quantitative outside-test estimate. [Positive-time deduction](positive-time.md)

## Replay

Use the pinned baseline [transfer toolchain and original native assembly worker](../execution.md). Its completed run directory provides the kernel, firmware, QEMU, hosted desk binaries, Lean and Mathlib paths. This worker additionally uses NumPy and SciPy. With a new empty output path, run the following from this directory.

```sh
(cd "$MATHLIB" && lake exe cache get Mathlib/Topology/MetricSpace/IsometricSMul.lean Mathlib/Analysis/SpecialFunctions/Pow/Real.lean Mathlib/Algebra/Order/BigOperators/Ring/Finset.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/Ring.lean)
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python3 replay.py "$TRANSFER_RUN" "$PCP" ./heat-trace-run
```
