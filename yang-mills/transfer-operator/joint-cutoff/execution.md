# Execution and scope of the joint-cutoff checks

Four PCP desk nodes formed three levels. The root delegated generation. Its generation child delegated two grandchildren. One grandchild ran a numerical and algebraic control, searching the coordinate probes for both failures of form ordering. It emitted the Lean proof with the two vectors it found. The other grandchild booted a measured PCP OS kernel and ran a freestanding certificate program with the three input coefficients 9, 3 and 2. It computed the defect error coefficient $8\cdot9=72$ and the log-energy coefficient $72+2\cdot3^2=90$, then emitted the Lean declaration and proof over serial. [Control worker](controls.py) · [Native program](certificate.c)

The generation child stripped both marked regions from the source basis and booted a second measured kernel. Its assembly worker inserted the two independent streams. The root compared the complete output with the tracked file, then invoked Lean on the host. The post-exit read-back records a finished root, child and two grandchildren. The earlier transfer baseline was separately rebuilt and replayed before this run. [Runner](replay.py) · [Run evidence](readback.txt) · [Baseline build and pins](../execution.md)

| Verified by Lean 4.19.0 | Inputs supplied by the analysis |
|---|---|
| From the score and Gamma bounds, both inequalities for an adjacent Bessel ratio | Bessel integral, integration by parts and decreasing Gamma tilt |
| Both product estimates on arbitrary finite sets, kinetic inequalities and free scalar resolvent bound | Peter–Weyl diagonalization and the physical high-label circuit |
| Noncommutative common-potential identity, its operator-norm estimate and the sum of the three perturbation errors | Wilson factorization, exponential remainder and resolvent norm estimates |
| Reciprocal inversion at low energy, logarithmic conversion, individual energy and two-level gap arithmetic | Variational principle, two-dimensional trial space and identification of transfer eigenvalues |
| Failure of both possible sandwich form orders on explicit vectors | The test matrix has eigenvalues $1/2,1$ |

Vacuum eigenspace stability, positive-time evolution estimates, and their applications to spatial paths are proved analytically in the two notes. The formal file contains twelve declarations. The ring identity uses only `propext`. The other eleven print `propext`, `Classical.choice` and `Quot.sound`. Four independent mutations test the physical-energy constant, sign of the free resolvent difference, order of noncommuting factors and the form-order witness. Lean rejected each changed proof. [Lean source](JointCutoff.lean) · [Energy and vacuum](README.md) · [Evolution](evolution.md)

## Numerical checks

The control worker evaluated 750 Bessel products with three independently varying labels at six couplings from $1/8$ to $4096$. The largest observed ratio of the free resolvent difference to its sharp upper bound was 0.9988727020. It also diagonalized a single four-link circuit truncated to 32 character modes, with $\kappa=1$, $\lambda=2$, $c=10$ and $t=1/2$. The Hamiltonian gap was 6.227727623. All four errors decreased at each halving of the time step.

| $1/a$ | Resolvent norm error | Absolute log-gap error | Vacuum projection error | Positive-time norm error |
|---:|---:|---:|---:|---:|
| 512 | 0.001465 | 0.005651 | 0.0001500 | 0.0002192 |
| 1024 | 0.000631 | 0.002825 | 0.0000755 | 0.0001100 |
| 2048 | 0.000281 | 0.001412 | 0.0000379 | 0.0000551 |
| 4096 | 0.000131 | 0.000706 | 0.0000190 | 0.0000276 |

The finite circuit tests transfer normalization, the order of the magnetic factors and the link multiplicity. The analytic estimates themselves apply to all labels and finite torus sizes.

## Replay

Use the pinned Lean/mathlib and PCP checkouts described in the baseline build, a C compiler and linker, QEMU, Python, NumPy and SciPy. From this directory, give the runner a fresh output path. It retains both complete serial logs, worker binaries, emitted Lean, diagnostics, numerical results and the recursion database.

```sh
(cd "$MATHLIB" && lake exe cache get Mathlib/Analysis/SpecialFunctions/Log/Basic.lean Mathlib/Algebra/Order/BigOperators/Group/Finset.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/Ring.lean)
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python3 replay.py "$TRANSFER_RUN" "$PCP" ./joint-cutoff-run
```
