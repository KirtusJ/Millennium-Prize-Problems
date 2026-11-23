# Checks on the local dual and the Haar contact

Two measured PCP OS deployments with a parent, child and grandchild independently emitted the same Lean source. The host relayed the guest requests. Each complete worker run recorded 47 kernel events. Lean 4.19.0 with Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked eight supporting declarations with the standard axioms `propext`, `Classical.choice` and `Quot.sound`. These declarations cover the normalization, density cancellation, diagonal pairing, covariance bound and the quadratic error budget for arbitrary finite smearings. The conditional integration and infinite-volume estimates are written proofs. [Worker](worker.c) · [Generated Lean](HaarDual.lean) · [Execution convention](../../../execution.md)

| Item | SHA-256 |
|---|---|
| Kernel ELF | `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` |
| Parent ELF | `90e93d2ed062c975b232391366b2022fd51b7a7591feea69e4630d1cffe8b16f` |
| Child ELF | `887617c498e306c67b1c6c1dc8715b3df329f4c32f21bc95305f83c2124d66e4` |
| Grandchild ELF | `d964ce4c709bcf49c4705c446e82f7d12c3574103e51e67c4152f372c82994f9` |
| Emitted Lean | `a622ded40cd44dc47274e344e84add6d77ba350be478f9bb3ac30b9fae1814f9` |

The parent enumerated all 48 signed complementary pairs, compared their edge sets and located their unique degree-four vertex. The child found 38 distinct action plaquettes meeting each of those eight-edge sets. The grandchild checked cancellation of an exact nonuniform conditional weight in four states. Three mutations changed the Haar normalization, inflated the variance lower bound or reduced the allowed mixed-coefficient error. Lean rejected each one.

The [host check](check.py) located 30,000 distinct figure-eight supports on a periodic side-five lattice and counted 48 in every cell. A separate rational calculation using the eight quaternion units, whose first two coordinate moments equal the Haar ones, gave a mixed pairing of 3/4096 under a nonuniform two-holonomy weight. The ordinary squared norm under that same weight was 15/20096. The finite model checks the normalization and the role of the inverse density; the Wilson argument uses its actual eight-link specification.

Run the first two commands from this directory and the last from the pinned Mathlib checkout.

```sh
python check.py
python ../../../replay-guests.py "$KERNEL" --proof HaarDual.lean --qemu "$QEMU_WRAPPER" --firmware "$FIRMWARE"
lake env lean /path/to/HaarDual.lean
```
