# Verification

Two parent–child–grandchild PCP OS runs emitted byte-identical [Lean source](GapWeight.lean). Each child was booted by the host supervisor after its parent requested it. Each guest completed its arithmetic control, returned exit zero and reported 47 kernel events. Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked all four declarations. Their axiom reports contain `propext`, `Classical.choice` and `Quot.sound`. [Payload](worker.c) · [Replay convention](../execution.md)

| File | SHA-256 |
|---|---|
| PCP OS kernel | `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` |
| Parent ELF | `9f74a96484f31b6cf4226f40bd25362d8d2ed7a899cd5f7bea552b154ab26bc0` |
| Child ELF | `aa08126eb8937372656ee6bf8e5ad8d01d2f7ddd60dc1b899590aefd33d59b0c` |
| Grandchild ELF | `8d923fa51c04b5cc83d1173e09c583c10b8aa831d02b35d023bd1f6b9bd6c435` |
| Generated source | `de3cf778fff5dac72987d882a5a83d09417957a5094e217ade464396e993bae9` |

`lowMassBound` handles integration over any probability space with the stated first and second moments. `twoAtomEquality` verifies attainment. `halfTimeFloor` verifies the scalar probability bound, and `monotoneTilt` proves the covariance inequality on any probability space with the three stated integrability hypotheses. Changing the coefficient $2s$ to $3s$ in the sharp inequality or reversing the comonotonicity premise in the covariance theorem broke its proof. The two-atom extremizer and the two-point uniform law with oppositely ordered nonconstant tests give explicit counterexamples to the two changes.

The [matrix control](check_weight.py) builds all four three-state generators for $\xi=64,96,128$, checks their off-diagonal signs and verifies that their exponentials are strictly positive stochastic matrices. It diagonalizes the three-site product step to check the gap. Applying the one-step matrix repeatedly to the fixed spin gives the two readings independently of the formula for the spectral weights. The ratios agree to relative tolerance $3\times10^{-7}$. For each of the three slab cases it also compares 35 positive averages against the endpoint. The infinite product, asymptotics and passage from temporal smearing to spectral multipliers use the written proofs.

From this directory run the numerical control and guest replay with

```sh
OPENBLAS_NUM_THREADS=1 python check_weight.py
python ../replay-guests.py "$KERNEL" --proof GapWeight.lean --qemu "$QEMU_WRAPPER" --firmware "$FIRMWARE"
```

Run `lake env lean /path/to/GapWeight.lean` from the pinned Mathlib checkout.
