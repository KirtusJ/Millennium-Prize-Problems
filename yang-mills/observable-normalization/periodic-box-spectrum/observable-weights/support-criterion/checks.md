# Support-criterion verification

The [written proof](README.md) derives the optimal overlap in the true Wilson vacuum, including the total-variation and conditional-expectation steps. The [independent controls](check.py) build the periodic links with direction labels, choose a spanning tree, form its fundamental cycle matrix and project onto the orthogonal complement of gradients and constants. On the cut-open $2^3$, $3^3$ and $3\times2\times4$ boxes, all cycle rows survive this projection and the smallest row-Gram eigenvalue is one. Adding one seam link gives winding rank one. Projecting out that one winding combination again leaves full row rank on the hard space.

An exact SU(2) link-product check on the cut-open two-site cube uses a noncommuting constant triple and a transverse fluctuation field. For $h=0.04,0.01,0.0025,0.000625$, the maximum absolute differences between rescaled chord logs and linear cycle coordinates were 0.06647, 0.02621, 0.01156 and 0.00549. The corresponding directional errors in their hard derivatives were 0.15237, 0.03620, 0.00883 and 0.00218. This exercises the derivative control needed for varying measurable filters; it does not estimate a Wilson spectral weight.

A separate Gaussian observation model tests the optimization against a rare event. For an equiprobable sign $X$ observed through $Y=Z+\epsilon X$ with $Z$ standard normal, the unit-norm overlap supremum is exactly $\|\tanh(\epsilon Y)\|_2$. At $\epsilon=0.1$ quadrature gives 0.0995069. The normalized event $Y>4$ gives only 0.0023400. The Wilson proof uses a bounded-target approximation before passing to unrestricted unit-variance probes.

Three native [PCP OS proof-template workers](worker.c) emitted the [Lean file](SupportCriterion.lean) with the host following parent and child requests. Generation and a separate replay produced identical Lean bytes, SHA-256 `db5a093785ce1fcbeb1502e045923b2be2b21114d5be959919603fc5a1d8e405`. Each boot recorded 47 kernel-register events with measured kernel `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`.

| Guest | Finite control | ELF SHA-256 |
|---|---|---|
| Parent | Cut-open cycle count for cube sides 2 through 12 | `388457cf886d7fc5607de1d490d608281752095f09d007936cf20d568071d7bc` |
| Child | Bounded signed-cell density implies the squared conditional-mean bound | `93fe3c7217c510a6a6e06130bfc698ec61fb4d3b3e87d6ebccdaa424b72f1a61` |
| Grandchild | Neutrality under a common sign on the real and imaginary chord factors | `d19291fa2eb5a3b511078017e77ebc4756260f508d3e8c784711d5f17142b96b` |

Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked six scalar statements, including the chord-Gram lower bound in two dimensions, the oscillator bound, the bounded conditional-mean inequality and center-sign arithmetic. The reported axioms are standard. Doubling the left side of the conditional-square bound and retaining an extra sign in the neutral product each failed compilation. The optimization and subgraph criterion have a written proof, without end-to-end Lean verification. Run the [replay driver](../../../transfer-increments/replay-guests.py) and controls from this directory.

```sh
python ../../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof SupportCriterion.lean
lake env lean SupportCriterion.lean
python check.py
```
