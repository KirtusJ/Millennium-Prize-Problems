# Observable-weight checks

The [analytic argument](README.md) uses the full ordered fixed-box spectrum, convergence of its eigenspaces, propagation of vacuum insertions and uniform integrability of the scaled local action. Those steps have written proofs; the finite computations here test normalizations and limiting formulas.

The [position-space and quaternion control](check.py) constructs all periodic finite differences, assembles the full one-color curl matrix, and independently diagonalizes its square. The variance and lagged covariance in a fixed 12 plaquette agree with the finite Fourier sums at times 0, 1, 3 and 8. On boxes of side lengths $(2,2,2)$, $(3,3,3)$ and $(3,2,5)$ the one-color equal-time variances are 0.45306962, 0.49085147 and 0.46651745. The last box has the same first visible energy as the side-three cube. Its longer third direction produces lower one-particle frequencies annihilated by the selected curl. The first-atom mass multiplied by $N^8$ is 233.8636621 at $N=32$ and 236.8586154 at $N=512$, tending to $24\pi^2$ after taking the weak-coupling limit first.

An exact link-product control uses a noncommuting background and a nonconstant field on a three-site-per-direction cube. It evaluates the local plaquette, the squared sine of a winding angle, and a transported plane average in the same configuration. At $h=0.04$ their absolute errors against their three distinct scaled limits are 0.02060, 0.00556 and 0.01365. At $h=0.000625$ these fall to 0.00205, 0.00045 and 0.00157. These pointwise checks test the expansions; they do not sample the interacting vacuum.

Three native [PCP OS proof-template workers](worker.c) emitted the [Lean source](ObservableWeights.lean) through a host-mediated parent, child and grandchild sequence. Two boot sequences reproduced the same guest executable hashes and emitted source SHA-256 `0897fdf45f3f31223cc4169e02574f5ee69581100bcfa002b0dd22bf87758891`. The measured kernel was `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`; each boot recorded 47 register events.

| Guest | Finite control | ELF SHA-256 |
|---|---|---|
| Parent | Multiplicity of first active momenta on cubes of sides 2 through 9 | `11e89390b4cb28bd4a8e28c12ac08540204cc4055bfa25fefa3ccbe8607395e2` |
| Child | Six connected three-color Wick contractions | `d22ff70d976689ab2eec6840b476afed9e103b7549cf1f16e57d6d96059ad16b` |
| Grandchild | Oriented curl cancellation across a periodic spatial plane | `c5f54082aff76f1ea898b3a377d835832f063788b215ee8bdb4cc6614cbfc662` |

Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked seven scalar statements, including the color factor, pair-atom arithmetic and a window-mass bound. All axiom reports list standard Lean axioms only. Doubling the Wick coefficient and using the side-two multiplicity in the limiting shell coefficient each failed compilation. From this directory run the [worker replay](../../transfer-increments/replay-guests.py) and numerical checks.

```sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof ObservableWeights.lean
lake env lean ObservableWeights.lean
python check.py
```
