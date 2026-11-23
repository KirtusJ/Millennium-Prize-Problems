# Verification of the two-lag calculation

Three PCP OS guests ran in a parent, child and grandchild chain with the measured kernel SHA-256 `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`. Each guest completed its finite check before emitting its segment of the Lean source. A fresh replay produced the same three binaries and the same source. Each guest recorded 47 events per run.

| Guest | Finite check | ELF SHA-256 |
|---|---|---|
| Parent | Each of three face orientations has twelve edge-sharing neighbours and at most one common edge with each, on tori of side 4, 6, 8 and 10 | `17d3417679411c002b50d2d6f2837c4fbc06f54632a783f30c3cd3d17bbc511f` |
| Child | Enumerated all ordered fourth-moment index quadruples for 1 through 16 faces using the weights proved in the note | `f61d08002c3c0023d0857b08309af756a284ec8cf9aecee74441803e488c7969` |
| Grandchild | Compared signed log-likelihood differences and midpoint decisions for integer shifts and scores including ties | `8106b5dffda7c3104bb542e9c3a12721aced4daef13ee75ed68751fad2444d4b` |

The [generated source](ElectricLag.lean) has SHA-256 `0bd50a0de5286570bc6ccfa394961464a674bed53af6f4e0015fb02217266994`. Lean 4.19.0 and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked six declarations. Each axiom report lists only `propext`, `Classical.choice` and `Quot.sound`. Three separate mutations failed compilation as intended. They changed the sign of the fourth-count correction, reversed the midpoint test and changed the translated normal’s quadratic denominator. The physical trace estimate, signed-polynomial expansion, Gaussian convergence and relative-entropy limit are written proofs. [Guest source](worker.c) · [Replay driver](../replay-guests.py)

From this directory, run the following with the supported kernel, QEMU and a C compiler available. Run Lean with the pinned Mathlib environment.

```sh
python ../replay-guests.py /path/to/kernel.elf32 --proof ElectricLag.lean
lake env lean ElectricLag.lean
python check.py
```

The [Python control](check.py) integrates the first five fundamental Haar trace moments and tests the two-shift decision rule in an independent binary model whose tilted distribution is exactly binomial. At 16,384 readings, shifts 0.95 and 0.25 gave total variation 0.27366194 and the midpoint attained the same value to eight decimal places. The larger shift had forward relative entropy 0.45123757 nats against the symmetric law, approaching 0.45125. The script also checks an unshifted comparator and identical shifts. G4’s finite gauge and product-profile controls reproduced at the reviewed revision. These numerical comparisons test constants and decision conventions. The SU(2) asymptotic claim uses the orbit likelihood in the [proof](README.md).
