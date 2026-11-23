# Checks on center tunneling

The [analytic argument](README.md) supplies the weighted estimate, corner-to-corner kernel bound and spectral conclusion. The [Lean file](CenterSectors.lean) checks five scalar steps: the pairwise weighted remainder, absorption of exterior mass, the sign-change identity, signed-mass cancellation after integration, and the passage from powers to one-step eigenvalues. Lean 4.19.0 with Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b` reports only `propext`, `Classical.choice` and `Quot.sound`. Doubling the weighted remainder and removing the factor $N$ in the one-step inequality each failed compilation in a separate mutation. For the latter, $a=1$, $b=1/2$, $N=2$ gives $3/4>1/2$.

Three native [proof-template workers](worker.c) executed in separate PCP OS guests. The host followed the requests emitted by the parent and child. Two runs with measured kernel SHA-256 `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` emitted identical Lean bytes, SHA-256 `a8222ee01b95ec4708e2d893a79f625e3c463816c1840cbf45b262ddc5996272`. Each boot reported 47 register events.

| Guest | Test preceding proof emission | ELF SHA-256 |
|---|---|---|
| Parent | Exhaustive weighted-pair identity on bounded integers | `7f07d554315a6557e93e03017913bdd3359f5db97b561fa444c6f5b8399dcf5f` |
| Child | All pairs on a 64-point meridian, testing both endpoints of short equator crossings | `44218b7de9daa4366d1fe00a0960370cc5679e0b5f360e71f8e26b001a5a383d` |
| Grandchild | Cancellation over all center corners for each nontrivial character in two and three directions | `3256da8cd86693b162327100378d7062600bc322c962ba7130a13def9018db8f` |

The [quadrature and geometry control](check.py) uses the actual SU(2) radial Wilson law and commutator potential. The second column is the weight-tilt error $\mathbb E[\cosh(a d/s)-1]/a^2$ at $a=1/4$. The third is the one-link probability Haar volume of a ball of radius $s/4$ times the one-link Wilson density at distance $3s/2$. A midpoint with one active link and two transverse perturbations of length $\sin(s/4)$ has bounded potential. Flipping two links together along orthogonal axes instead incurs exactly $2\beta$ there.

| $\beta$ | Tilt error | One-step density × volume | Sequential midpoint $V$ | Simultaneous midpoint $V$ |
|---:|---:|---:|---:|---:|
| 64 | 1.543942 | 0.0013613 | 0.2500406 | 128 |
| 4096 | 1.539706 | 0.0013493 | 0.2500006 | 8192 |
| 262144 | 1.539639 | 0.0013491 | 0.2500000 | 524288 |

The numerical checks probe individual estimates. The proof uses uniform inequalities over all sufficiently large couplings. Run the [host replay](../../transfer-increments/replay-guests.py), Lean and SciPy controls from this directory.

```sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof CenterSectors.lean
lake env lean CenterSectors.lean
python check.py
```
