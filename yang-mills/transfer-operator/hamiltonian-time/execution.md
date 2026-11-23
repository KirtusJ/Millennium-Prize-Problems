# Execution and scope

The PCP recursion desk ran a root verifier, its generation child and two grandchildren. The geometry worker constructed periodic directed edges and plaquettes at spatial sides 2 through 6, removed each edge in turn to find the shortest cycle through it, and counted the sites supporting the three anchored plaquette factors. From the fourfold coverage it emitted the translated-sum theorem and proof. At every size an excitation in a neighboring site cost zero for the anchor-only electric block and one for the redistributed block. The same worker integrated the normalized SU(2) characters against the transfer density using 4,096 angular midpoints. [Geometry worker](geometry.py)

The certificate worker booted the measured PCP OS kernel with a target variance of $5/9$ and a maximum scaled energy quotient of 12. Its freestanding program searched integer reciprocals $n$ for a trace distance at most $1/n$. From the lowest allowed second moment and largest squared mean it required
$$9(n^2-4n-16)\ge5n^2,\qquad 2(3n^2+4n)\le12(n^2-4n-16).$$
It selected $n=12$ and emitted the Lean proof with the reduced fractions. The generation worker booted a second measured kernel, supplied the other director-authored declarations as a basis and assembled the two generated parts. The root compared all 5,869 source bytes before running Lean on the host. The post-exit desk had four finished nodes at revision 8. [Certificate program](witness.c) · [Native receipts, geometry, Lean and adverse output](readback.txt)

| Item | Observed result |
|---|---|
| Kernel | SHA-256 `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`. Both boot records matched the independently pinned code and read-only-data measurement. |
| Certificate worker | ELF SHA-256 `920eaae107abc827a6de3f6810ec3dc9e7894b32e7b3e3b2939669e5a7d0ec3a`. |
| Assembly worker | ELF SHA-256 `1cb649a9954be008a7f74ada3fb1494f1949d7947b85bf221875c655ea59afcd`. |
| Checked source | SHA-256 `7949d43bc58f4ba3d01ea1566ee13cb5864d1b0498e7d939839ad920bc946b87`. |
| Lean | Lean 4.19.0, mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`. All eleven declarations passed without warnings. Each printed exactly `propext`, `Classical.choice` and `Quot.sound`. |
| Four false changes | Lowering the block coverage from four to three, relaxing $1/384$ to $1/128$, demanding a trial defect constant of one, and changing the Casimir to $n(n+1)/2$ each failed in its own declaration. |

The formal checks cover the Casimir coefficient, a product bound given a lower support count, translation reindexing, block normalization and excitation cost, projection leakage, variance and energy arithmetic, the exponential tangent, the two weak-coupling inequalities under their displayed hypotheses, and the diagonal smearing sum. Peter–Weyl theory, gauge-invariant cycle support, Chernoff convergence, compactness of cutoff ground states, applicability of the external stability theorem, Haar integration and the physical interpretations are analytic arguments in the two notes. The finite enumeration and quadrature are controls. At one-link couplings 64, 256 and 1,024 the measured label-four energies were 12.088732, 12.023136 and 12.005841 at $\kappa=1$, against the analytic limit 12. [Lean declarations](HamiltonianTime.lean)

## Reproduce

From this directory, with the original completed transfer run and its pinned PCP checkout, execute the following. The runner requires a fresh output directory and keeps the desk database, both serials, the exact generated file, host Lean output and rejected mutations. [Original calibration, dependency revisions and build instructions](../execution.md)

```sh
(cd "$MATHLIB" && lake exe cache get Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean Mathlib/Analysis/SpecialFunctions/Exp.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/Ring.lean)
PYTHONDONTWRITEBYTECODE=1 python3 replay.py "$TRANSFER_RUN" "$PCP" ./hamiltonian-time-run
```
