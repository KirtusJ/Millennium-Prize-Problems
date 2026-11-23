# Verification of the one-site estimate

Three PCP OS guests ran under kernel SHA-256 `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`. The host followed the parent and child requests. A separate replay reproduced all guest binaries and the emitted Lean source. Each boot recorded 47 events.

| Guest | Finite control | ELF SHA-256 |
|---|---|---|
| Parent | Counted the descending Bessel recurrence pairs for all indices 8 through 2048. | `987b942873d02ed1cb44b4cb9cb7740d3c0eab8fa682662f945cd07131e5af4d` |
| Child | Counted late time slots and visits in deterministic occupancy patterns. | `90c1fbc402cbd21e503335846fe8d13bccb2b4a0870eecaf144e6e545a55caf5` |
| Grandchild | Multiplied a three-state killed transition with exact integer arithmetic and tested the five-step survival telescoping identity. | `c06e908fe97344366da4501f9d31a6f7146ea2bc287b1c59554150d29090bebc` |

The [generated Lean source](ToronVacuum.lean) has SHA-256 `9178ba5ed0b6db64c470ddef29a8f1c95457580c57594c18843bb57f043e9102`. Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` accepted six declarations covering scalar comparisons and the finite survival sum for an additive operator. Reports contain only standard Lean axioms. Reversing the telescoping difference and lowering the power of the block length in the scale identity each failed compilation. The Fourier sum bound, uniform tube estimate, supersolution construction and trial functions are [written proofs](README.md).

The seeded [Wilson-walk check](check.py) uses actual SU(2) increments. Their trace deficit has density proportional to $e^{-\beta s}\sqrt{s(2-s)}$; gamma rejection sampling gives that density and an independent uniform axis gives the increment. At $\beta=64,1000,32768$ the sampled block survival from two central links was respectively 0.4011, 0.2634 and 0.2147, with standard errors below 0.004. The script also samples a noncentral commuting start and a noncommuting start, and checks scaled Fourier partial sums at identity. The trials use 4,096 paths per case. They test the commutator and time-step conventions. Uniformity over all starts and identification of the absolute-energy order come from the proof.

From this directory run the [host replay](../transfer-increments/replay-guests.py) with the supported kernel and compiler, then use the pinned Lean environment. The Python control needs NumPy and SciPy. [Guest source](worker.c)

```sh
python ../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof ToronVacuum.lean
lake env lean ToronVacuum.lean
python check.py
```
