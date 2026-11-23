# Checks for the local action comparison

Three native PCP OS programs ran in a parent, child and grandchild sequence with a host relay. Each included a finite arithmetic control. A fresh replay booted all three again and reproduced the assembled Lean source byte for byte. Each of the six boots logged 47 kernel events. Lean 4.19.0 with Mathlib commit `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked all six declarations. The axiom reports contain only `propext`, `Quot.sound` and, for five declarations, `Classical.choice`. [Native source](worker.c) · [Emitted Lean source](LocalAction.lean) · [Replay environment](../execution.md)

| Item | SHA-256 |
|---|---|
| Kernel ELF | `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` |
| Parent ELF | `0a20048786f7ccb4663a468ead4a20452f3890ce62e0e1d3445a22eccc3e767a` |
| Child ELF | `e3ca78970cb52c207d4b9852f361a0ab579ea5780b4f336f3a73abfff3bafd56` |
| Grandchild ELF | `5f99db1de921febde6f12661edcf4b83ebd83a73a39ec24fdd84fe58fcd0f27a` |
| Generated source | `cc67a9b3d1d29226ea5a5f193bc789d7978aebf6e798d8e8a1d7cf222e30b963` |

The formal statements cover the reflected pair indices, the diagonal bound for a sum of blocks with nonpositive off-diagonal inner products in expectation, the quaternion action remainder, the three-color Wick coefficient, the balancing identity, and propagation of errors through a tilted ratio. Changing the reflected base by one cell, reversing the sign of the off-diagonal hypothesis, and doubling the Wick coefficient each caused its altered declaration to fail. With two identical unit blocks the reversed-sign version would bound four by two. The Wilson applications of reflection positivity and the Haar identity, and the limiting spectral measure, have written proofs.

The [independent Python checks](check_local.py) compare reflected face words with inverses by free reduction before taking a trace. They checked 156 individual faces and verified all three zero moments and the exact primitive mass for twelve even averaging lengths. Two Gauss–Legendre meshes with 56 and 84 nodes per coordinate agreed to $2\times10^{-6}$ in $n^4G(n,0)$ at seven lags. At $n=128$ the computed $n^8$ times the free action covariance was $0.0154083783$, against its limit $3/(2\pi^4)=0.0153989734$. The free tilt ratio at $n=64$ was $0.003899091$, against $2^{-8}=0.003906250$. These cubatures evaluate the free integral. The constants in the Wilson error remain unspecified.

From this directory run the following. Run the Lean command from the pinned Mathlib checkout.

```sh
OPENBLAS_NUM_THREADS=1 python check_local.py
python ../replay-guests.py "$KERNEL" --proof LocalAction.lean --qemu "$QEMU_WRAPPER" --firmware "$FIRMWARE"
lake env lean /path/to/LocalAction.lean
```
