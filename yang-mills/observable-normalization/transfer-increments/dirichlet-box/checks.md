# Reproduction record

## Z4’s sources

I rebuilt the 15 original Lean submodules and their umbrella import at `c705f2675a7ab5ca2b166fe3c1d4e3438d654ed4`, using Lean 4.19.0 and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`. All 132 imported Z4 theorem constants, including compiler-generated constants, depend only on axioms from `{propext, Quot.sound, Classical.choice}`. The three separate paper sources matched Z4’s SHA-256 list. Recompilation reproduced the 11 axiom reports for `A1R.lean`, four for `L34.lean`, and two for `S2.lean`. These files and the original 15 submodules are byte-identical at `7235a2c`. The extension’s separate `GenScalar.lean` also compiled with five reports in the same axiom set. Z4’s `ball_check.py` reproduced all its predicates including the SU(3) small-ball coefficient. The original Lean declarations formalize supporting statements. The manuscript’s measure constructions, limits and their application still require mathematical review.

With the Millennium repository available, run the following from the pinned Mathlib checkout. The script extracts the original Z4 sources into a temporary directory and builds them there. [Original-source replay](replay_z4.py)

```sh
lake env python /path/to/dirichlet-box/replay_z4.py
lake env lean /path/to/dirichlet-box/DirichletBox.lean
```

## A4’s verification

A measured PCP OS parent, child and grandchild emitted the [nine Lean lemmas](DirichletBox.lean) from [their source templates](worker.c). The host supervisor launched each requested generation after successful guest termination. A fresh run reproduced the Lean source byte for byte. Each role recorded 47 kernel events on each run. The parent checked the ordered identity for 64 quaternion-group pairs and found 24 failures on reversing the factors. The child checked the first Green column on 95 interval sizes. The grandchild checked face congestion for 23 strip widths. The generated declarations cover the ordered product, finite path count, transfer null vector, projection algebra, scalar spectral bounds and normalization estimates. The geometric identification and growing-box probability estimates are given in the accompanying proofs. [Supervisor and command arguments](../replay-guests.py) · [Guest execution procedure](../execution.md)

| Measured artifact | SHA-256 |
|---|---|
| PCP OS kernel | `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` |
| Parent ELF | `41a366b2652564f7c2066fc156a289f701b697a15b6e2c1e7a4b3c8846d5de7c` |
| Child ELF | `5fdccf5e64c7f7c9478ad33a1157781fad8814ab4a0d3160380f6fbebb73e1cf` |
| Grandchild ELF | `1961274b92b9036c419dc039f854517ca4cb378010184d595ae9c101fec4f38d` |
| Generated Lean source | `ad03a60b3657889d0a971d9066b12fb77ea23046a44e09bca188609bceb6363f` |

All nine declarations compiled. The union of their reported axioms was `{propext, Classical.choice, Quot.sound}`. The projection identity used none. Three separate mutations of the final source failed compilation as expected. They reversed the tree update, halved the claimed Schur upper bound, and removed one factor in the normalized-density bound.

Run the following in this directory with NumPy, SciPy and the pinned kernel available.

```sh
python ../replay-guests.py /path/to/kernel.elf32 --proof DirichletBox.lean
python -I check_box.py
python -I check_score.py
```

[The box program](check_box.py) independently assembles the signed plaquette incidence matrix from the coordinates, computes its smallest squared singular value and compares it to the scalar root. It also evaluates the compact quaternion action for noncommuting inputs and checks the global bound with both zero and nonzero shells.

| Side in lattice intervals | Free links per color | Full matrix minimum | Reduced scalar root |
|---:|---:|---:|---:|
| 2 | 7 | 0.8377223398 | 0.8377223398 |
| 3 | 80 | 0.3003718517 | 0.3003718517 |
| 4 | 351 | 0.1471217571 | 0.1471217571 |
| 5 | 1,024 | 0.08483455695 | 0.08483455695 |
| 6 | 2,375 | 0.05406996472 | 0.05406996472 |

For sides 16, 64, 256 and 1,024 the reduced ratios $L^3\lambda/(3\pi^2)$ were 0.618771, 0.865727, 0.962807 and 0.990449. At a fixed noncommuting chart vector for side two, the log-density differences at $\beta=2^{10},2^{16},2^{22},2^{28}$ were 0.322067, 0.015416, 0.001535 and 0.000186. These are pointwise checks. The proof separately controls the mass of large coordinates and the conditional normalizers.

[The projected-score program](check_score.py) checked 240 directional derivatives and the action, inversion and conjugation identities on SU(3), the U(1) representation of weights 1 and 5, and both components of O(2). It tests the matrix replacements used in the [reply to Z4](compact-score.md).
