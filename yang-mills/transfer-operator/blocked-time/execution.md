# Formal checks and execution

A PCP recursion desk ran four workers across three levels. The root delegated generation. The incidence grandchild enumerated the two adjacent time slabs and every positive spatial edge on cubic tori of sides 2, 3, 4 and 5. It recovered the magnetic counts $(16,24,16)$ at every edge, emitted two Lean row certificates, and passed the three count bytes to the certificate grandchild. That worker booted the pinned native PCP kernel, summed the counts and reduced the rational threshold from $2/10+56(13/4)z<1$. Its emitted theorem uses $z<2/455$. A second measured kernel assembled both streams into the director-supplied Lean basis. The root compared all source bytes, ran host Lean on the assembled file and tested five adverse changes. The finished desk, boot receipts, diagnostics, hashes and numerical controls are recorded in the run evidence. [Runner](replay.py) · [Incidence and matrix checks](block_checks.py) · [Native certificate worker](certificate.c) · [Read-back](readback.txt)

| Lean checks | Analytic steps supplied in the notes |
|---|---|
| Bernoulli bound at every $g\ge4$ and integer block size $m\ge3g$, normalized finite bridge cancellation | Consecutive Bessel ratio bound, Peter–Weyl expansion, conditional Wilson path law |
| Exact rational row bounds, arbitrary nonnegative influence-matrix iteration, finite propagation from a boundary, conversion of the gap to physical units | Dobrushin comparison, open time limit, spectral density of centered multipliers, spatial truncation |
| Scalar mixture error, local variance estimate under moment perturbations | Li–Yau heat bound, binomial heat minorization, fixed-box core and vacuum convergence, Dirichlet first moment |
| Finite Fourier sum estimate and cubic shell polynomial | Uniform spatial tail, real-analytic momentum response, tightness and convergence of energy measures |
| Crossing-face conjugacy in an arbitrary group | Open temporal gauge fixing, product-Haar invariance and reflection pairing |

The fourteen declarations passed Lean 4.19.0 without warnings. The crossing-face identity uses only `propext`. The other thirteen print `propext`, `Classical.choice` and `Quot.sound`. The full lattice transfer and continuum-limit arguments are given in the notes. [Lean source](BlockedTime.lean)

The adverse cases tested a denominator of 46 at $g=4,m=12$, reversal of the final temporal link in the crossing face, a time tilt of four at the stated row bound, inclusion of the strict endpoint $2/455$, and a larger physical gap coefficient under the same block-length hypothesis. Each failed in its own declaration. The row at tilt four on the conservative envelope was $2311/1920>1$. This failure limits that estimate; it does not furnish an excited eigenvalue.

## Independent numerical controls within the run

The incidence worker compared the original three-step transfer of a four-link $\mathbb Z_2$ gauge circuit with a direct sum over its conditional link bridges. All 256 matrix entries were included. The operator-norm discrepancy was $9.31\times10^{-17}$ or smaller. Replacing the internal plaquette weights by endpoint weights alone gave error $0.117585$. On two faces sharing an edge, averaging each face weight independently changed their joint expectation by $0.00227844$.

For SU(2) at seven $g$ values from 4 to 1024, the truncated one-link character sums on 513 class angles stayed within the analytic endpoint interval $[0.9,1.1]$. For SO(3) the radial Haar density is proportional to $1-\cos\vartheta$ on $[0,\pi]$. For defining Wilson action the spin-$j$ coefficient is $(I_j-I_{j+1})/[(2j+1)(I_0-I_1)]$ at Bessel argument $2g/3$. The worker compared 24 such coefficients to 4096-point Haar quadrature at four couplings. The largest discrepancy was below $5.1\times10^{-14}$. Pullback through the SU(2) double cover gave a vanishing odd fundamental coefficient to $1.2\times10^{-16}$. The compact-group theorem uses the analytic mixture argument and gives group-dependent constants. [Compact-group analysis](compact-groups.md)

## Replay

Use the pinned Lean/mathlib and PCP sources, kernel image, QEMU and firmware from the original transfer replay. The incidence worker additionally uses NumPy and SciPy. From this directory run the following with a new output directory. The run retains the emitted fragments, byte-matched source, all diagnostics, both full serial logs, worker binaries, positive and adverse numerical controls and the desk database. [Baseline preparation and pins](../execution.md)

```sh
(cd "$MATHLIB" && lake exe cache get Mathlib/Analysis/Convex/SpecificFunctions/Basic.lean Mathlib/Algebra/Order/BigOperators/Group/Finset.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/Ring.lean)
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python3 replay.py "$TRANSFER_RUN" "$PCP" ./blocked-time-run
```
