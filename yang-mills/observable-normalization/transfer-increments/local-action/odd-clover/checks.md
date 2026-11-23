# Verification of the odd clover calculation

Two measured PCP OS deployments each ran a parent, a child and a grandchild. The host relayed the two child requests and assembled the Lean declarations printed by the guests. Each role completed its arithmetic test before emitting its proof fragment and finished with 47 kernel-register events. The independent deployment reproduced the Lean source byte for byte. Lean 4.19.0 with Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked eight supporting declarations. Their reported axioms are drawn from `propext`, `Classical.choice` and `Quot.sound`. The Gibbs, Fourier comparison and infinite-volume arguments are written proofs. [Guest source](worker.c) · [Generated Lean](OddClover.lean) · [Execution convention](../../execution.md)

| Item | SHA-256 |
|---|---|
| Kernel ELF | `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` |
| Parent ELF | `823e0d06059adb7717a85f8ba6ccedadd29f465287bb1fa16b622b33ad2e7f80` |
| Child ELF | `d108b5ace3d7e3f8525bc8ea5a94868fc9de3b675255263ec5f4dd59ba037e2b` |
| Grandchild ELF | `3c8328fd1a3990d5373c7d5ea354ff3ceb4fc131d79bb580a7a634678ff2facf` |
| Emitted Lean | `dc0d5957dd3166ed605f5d32f7174d2c5da0b03df04e7758102cab92b9cbc34c` |

The parent checked the exterior identity on 4,096 binary input triples. The child checked all 64 reflected corners and 528 pairs of even-width translated intervals. The grandchild extracted the signed quaternion coefficient at 256 candidate roots with exact integer arithmetic. In four separate mutations Lean rejected a changed complementary-plane sign, a misplaced reflected endpoint, a changed upper-bound constant and an inflated cube-test lower bound.

The [independent Python checks](check_odd.py) compared site and cube totals on a periodic random quaternion field and checked both fields under all four reflections. Eight sign choices at each of three angles extracted the mixed odd part of the charge; at angle 0.015 the normalized finite difference was −0.06249296909, approaching −1/16. A free torus Fourier contraction gave the following site-reading values. The final column uses the shortest periodic coordinate distances and serves as a finite-period check on the surface coefficient.

| Torus side | Covariance at zero | Sum over torus | Distance-weighted surface estimate |
|---:|---:|---:|---:|
| 12 | 0.06587954 | 1.39e−17 | 0.24572774 |
| 18 | 0.06591098 | −1.04e−17 | 0.24783228 |
| 24 | 0.06591612 | 3.47e−17 | 0.24836916 |

Replacing the star by the identity makes the zero mode strictly positive in the same calculation. These controls check the Gaussian reference and finite quaternion algebra. The inference on the original Wilson measure uses the estimates in the research note.

Run the first two commands from this directory and the last from the pinned Mathlib checkout.

```sh
OPENBLAS_NUM_THREADS=1 python check_odd.py
python ../../replay-guests.py "$KERNEL" --proof OddClover.lean --qemu "$QEMU_WRAPPER" --firmware "$FIRMWARE"
lake env lean /path/to/OddClover.lean
```
