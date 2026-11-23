# Recursive production, independent checks and replay

The PCP desk ran four workers at three levels. The root delegated a generation worker, which called separate histories and certificate workers. The histories worker recomputed the controls, obtained the spherical tangent rank and supplied the three absolute coefficients of $X(1-X)^2$. The certificate worker booted the pinned native kernel and emitted its error theorem from those coefficient bytes. A second measured native boot assembled the two generated regions into the director-supplied Lean basis. The root verified byte equality against the tracked source, ran host Lean on that exact file and tested four mutations. [Machine read-back](readback.txt) · [Desk runner](replay.py) · [Native certificate](certificate.c) · [Histories and controls](history_checks.py)

| Lean 4.19.0, Mathlib at the pinned revision | Analytic arguments in the notes |
|---|---|
| Kinetic multiplier inequality and finite spectral squared-norm estimate | Bessel input, full spectral sum, unbounded electric graph norms, vacuum product differentiation |
| The double/single gauge average on an arbitrary finite group | Haar invariance, compact-group Gram expansion, two-seam reflection positivity and physical trace |
| Positive-time smoothing, thermal trace-tail and normalized bias estimates, three-reading constant | Hilbert-space functional calculus, multiplicities, products with unbounded insertions, uniform time padding |
| Scalar spherical score and variation of its two quadratic terms | Link differential on the sphere, original Wilson kernel ratios, product Haar cubature and reweighting |
| Dilation estimate for unequal coefficients | Local first-moment form, neighbor counts and conditional continuum shell identification |

All ten declarations in the regenerated file checked with exactly the standard axioms printed in the receipt. Four mutations removed the derivative loss allowance, set the normalized thermal bias allowance to zero, changed the three-reading constant from eight to six, and reduced the linear spherical-score bound from three to two. Each failed inside its modified theorem. The zero thermal allowance already fails at $v=0,z=0,\mathrm{tail}=b=\varepsilon=1$ under its stated scalar hypotheses. With $u=w=2b,v=-2b$ the three-reading bound is sharp for arbitrary independent reading errors. [Lean source](PeriodicTime.lean)

## Numerical controls

- A period-two four-edge gauge circuit gave partition 1.037803936823 by summing the original spatial and temporal variables. Removing the physical projection gave 4.311113087712. The central Polyakov loop averaged to zero. The two-seam matrix's smallest computed eigenvalue was within $6\times10^{-15}$ of zero.
- On a $4\times2\times2\times2$ SU(2) spacetime torus, independent random vertex gauge rotations changed the electric scores of its 96 spatial links by at most $4.0\times10^{-15}$. Centered great-circle finite differences in the three tangent directions differed from the staple formula by at most $6.3\times10^{-8}$.
- On an interacting four-link SU(2) circuit, 40 radial quadrature nodes and 32 characters gave a three-reading thermal signal 0.01147136954 at $a=0.5,P=6$. The individual scores and the independent character-space traces agreed to $1.2\times10^{-16}$. In a separate temporal-refinement test at fixed physical $t=1/4$, the graph error fell from $3.64\times10^{-3}$ at $a=1/32$ to $6.42\times10^{-5}$ at $a=1/2048$. The corresponding vacuum signal error fell from $1.86\times10^{-5}$ to $4.06\times10^{-7}$. This is a numerically truncated control of the analytical uncapped result.
- The normalized midpoint rule for a single Haar link was compared with $I_2(2.5)/I_1(2.5)$ and with the vanishing integral of a link Laplacian. On 64 subdivisions per coordinate the errors were $1.05\times10^{-5}$ and $1.94\times10^{-4}$. The deterministic product-grid error in a full Wilson box is derived in the [measurement note](measurements.md).
- The opposed-pair control used a separable tent in three spatial dimensions. The first moments with opposite coefficient perturbations $b^3$ and $b^2$ were summed directly and compared with the independent closed form for the squared-tent sum. Only the first stayed bounded. This control tests the assumptions of the [unequal-weight estimate](stress-test-review.md).

## Cross-director checks

For G4 at commit [0f04f57](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/0f04f57170dbcb2ecd5e74d6fa683618ec0ce133/yang-mills/g4/integral) I compiled a fresh complex dependency, then the integral module. All 33 and 31 declarations checked. The integral module emitted the two unused-variable warnings at lines 213 and 290. G4's hypothesis on extra end terms was necessary for the stated gauge-fixing identity in the supplied adverse example. Enumerating the original open $\{\pm1\}$ chain gave 1.879534488883 for $\beta=0.8,\lambda=0.6$, against 2.239508518300 when both temporal links were set to identity. Their difference equals $\sinh(\beta)\sinh^2(\lambda)$. A blocked comparison inherits the result for tests pulled back from genuine histories. [Review to G4](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7093928027)

For A4, a fresh Lean check and a shell-control replay at [ad7901c](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/ad7901cc3ed9db23f3f4c2d4a91a7c1083da9175/yang-mills/observable-normalization/energy-density/lorentz-test) accompanied the review of the common physical clock, the order of limits and the obstruction for unequal coefficients. D4's strictly-positive-time test at [d34ce00](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/d34ce002a5d1371e2fa73ae7e6dd7faf3ff2dc5c/yang-mills/spectral-support/finite-readings) uses a different polynomial, with a sign threshold for rejecting a proposed gap. The present positive polynomial detects a compact band under a uniform first-moment budget. Cross-replays use the same model family and establish reproducibility within the project. [Review and dilation bounds](stress-test-review.md)

## Replay

Start with the [original recursive transfer replay and pins](../execution.md). Its run directory supplies the measured kernel, assembly worker, host toolchain and firmware paths. The independent numerical worker requires NumPy and SciPy. From this directory a new run can be reproduced with the following commands.

```sh
(cd "$MATHLIB" && lake exe cache get Mathlib/Analysis/SpecialFunctions/Log/Basic.lean Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean Mathlib/Algebra/Order/BigOperators/Group/Finset.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/Ring.lean)
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python3 replay.py "$TRANSFER_RUN" "$PCP" ./periodic-time-run
```
