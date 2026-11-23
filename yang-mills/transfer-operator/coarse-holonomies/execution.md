# Formal coverage and replay

The [Lean module](CoarseHolonomies.lean) verifies components of the written estimates. It treats the translation-overlap comparison as an actual integral over a measure, the reverse chi-square identity for any reference probability, the second moment on a product measure, and the reverse likelihood Cauchy–Schwarz inequality for real integrable inputs. It also verifies the integral inequality for a positive mean-normalized insertion tested against a nonnegative exterior observable. Their use with the Wilson specification is explained in the [main proof](README.md).

| Lean declarations | Mathematical role |
|---|---|
| `faceFactorization`, `interiorLinks` | Boltzmann factorization when each face misses one of two varied links, and the endpoint trim on subdivided edges |
| `overlapVariance`, `powerDisplacement`, `shiftScore`, `displacementFloor`, `heatSteps` | Metric variance on the common part of two translated laws, repeated isometries, a finite score estimate, and the constants in the compact-group comparison |
| `iterateBound`, `productDensity`, `productSecondMoment`, `inverseDensity` | Products of contraction factors, pointwise relative density error and tensorization of likelihood moments |
| `reverseBias`, `exteriorBound`, `positiveInsertion`, `spectralWindow` | Conditional bias in the actual squared norm, positivity under exterior weighting and a finite spectral-window bound |
| `scoreMoments`, `centerParity` | Mean and variance coefficients of the scaled trace score and cancellation of its even part |

The continuous Fisher calculation, compact-group heat comparison, Wilson vacuum limit, SU(2) Fourier expansion and limit experiment are written proofs. They are outside the formal declarations. The project has no construction of a continuum theory or its mass gap from these estimates.

## Execution

A three-level PCP OS desk ran a root, its generation worker and two grandchildren. The first grandchild enumerated the marked-link geometry, checked the original Wilson action, evaluated the conditional binary experiment, and generated the endpoint declaration. The second grandchild booted the measured native kernel. Its program computed the scalar coefficients implied by the overlap, triangle and Haar displacement factors and emitted the `displacementFloor` declaration. A second native kernel boot assembled both generated regions into the Lean basis. The root compared the assembled output byte for byte with the tracked source, invoked host Lean and checked the axioms individually. The desk read-back was taken after every worker exited. [Control worker](controls.py) · [Native generator](certificate.c) · [Desk launcher](replay.py) · [Evidence](readback.txt)

The adverse runs strengthen the reverse-bias constant from one to one half, tighten the displacement floor from four to three, remove one unit from the heat step estimate, halve the linear odd coefficient in the parity identity, and remove an extra link from the endpoint count. The launcher requires a Lean rejection in the modified declaration for each variant. For the reverse-bias constant, take a unit-probability space with $f=1$, $r=0$, and $K=u-v=1$ to attain equality under the stated premises.

The numerical checks include the 2,520 plaquettes of a four-dimensional SU(2) torus. Flipping a distant closing link in each rectangle leaves the conditional action on eight marked links invariant and reverses the two gauge-invariant traces. Two changed links on one plaquette instead give mixed action difference four. An independent multimodal circle density checks integration by parts and 256 frequency responses. Radial quadrature of the original central SU(2) law and numerical inversion of the log-likelihood distribution give the error rates in the evidence. The integration-range and grid change is a convergence diagnostic. The asymptotic constants come from the character expansion and the central limit theorem.

Use the [pinned transfer toolchain](../execution.md), NumPy and SciPy. A completed baseline run supplies the kernel, assembly worker, firmware and executable paths. From this directory use a new output path.

```sh
(cd "$MATHLIB" && lake exe cache get Mathlib/Algebra/QuadraticDiscriminant.lean Mathlib/MeasureTheory/Integral/Prod.lean Mathlib/Topology/MetricSpace/IsometricSMul.lean Mathlib/Analysis/SpecialFunctions/Pow/Real.lean Mathlib/Algebra/Order/BigOperators/Ring/Finset.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/Ring.lean)
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python3 replay.py "$TRANSFER_RUN" "$PCP" ./coarse-holonomy-run
```
