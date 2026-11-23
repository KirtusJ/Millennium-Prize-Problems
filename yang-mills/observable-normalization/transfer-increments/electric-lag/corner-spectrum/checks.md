# Checking the energy-slope calculation

Three PCP OS guests ran under kernel SHA-256 `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`. The host followed the child request in each of the first two guests. A fresh replay reproduced the three executable hashes below and every byte of the Lean source. All six boots recorded 47 register events.

| Guest | Independent finite check | ELF SHA-256 |
|---|---|---|
| Parent | Enumerated first and second plaquette changes by neighboring cell occupancies on sides 4 through 10. Each square gave four first moves, 24 two-step paths and squared multiplicity sum 48. | `77e6807edeb34664942d799e019c60c79a58567c6794f863558a67b1aa9a3a36` |
| Child | Enumerated diagrams of size at most three in a four-by-four box, testing the diagonal and off-diagonal one-diagram commutator. | `5851f0608ba9d941066d2783c2593c0bcef46e8c393ae8c698045dace2078c66` |
| Grandchild | Enumerated return weights through order twelve using raising and lowering on the empty-state powers. | `c2ead70b4c2e86ac84cd56cd1b297f512c29b8a0e498ead9f395dc30bd370c6c` |

The [generated Lean file](CornerSpectrum.lean) has SHA-256 `a27a819ab1f6ca8cc2b85ab2811d358861a0fda914cba4c6e15a8a1ce4911238`. Lean 4.19.0 and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked six theorems. They include the additive-operator induction that passes from the four-corner commutator to the vacuum return recurrence, the scalar moment recursion and the inequality for support from a moment ratio. Replacing the fourth moment by $1/16$ or omitting half the extended-notch states failed compilation. The representation projection, the validity of the diagram identification through the stated depth, analytic perturbation and weak convergence are written arguments in the [research note](README.md).

The separate [Python check](check.py) builds loop boundaries as fine-edge bit sets. It enumerates all reachable words and amplitudes by changing faces. Independently it grows four integer partitions, maps each diagram quadruple back to its physical boundary and compares every amplitude. For a side-sixteen square at depth six both procedures gave 694 distinct loops with squared unnormalized amplitude sum 42,577,920. Dropping one corner from the partition model failed the comparison. These computations test the finite geometry in the argument; they do not numerically diagonalize the full Wilson transfer.

Run from this directory with a supported kernel, QEMU, C compiler, Python and the pinned Lean environment. [Guest source](worker.c) · [Host replay driver](../../replay-guests.py)

```sh
python ../../replay-guests.py /path/to/kernel.elf32 --proof CornerSpectrum.lean
lake env lean CornerSpectrum.lean
python check.py
```
