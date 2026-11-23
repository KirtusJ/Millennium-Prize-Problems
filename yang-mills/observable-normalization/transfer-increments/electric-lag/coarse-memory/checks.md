# Checks of the three-slice calculation

Three PCP OS guests ran in parent, child and grandchild order, following the child requests emitted by the first two guests. The measured kernel SHA-256 was `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`. The initial native run and an independent replay each gave 47 events per guest and identical executable and source hashes.

| Guest | Finite check | ELF SHA-256 |
|---|---|---|
| Parent | Compared the two expressions for a weighted conditional variance on integer two-point fibers. | `d624d308e26b9b14f95888e3ce3cccc5dcef98c3f55f4aeedc275103612c2618` |
| Child | Enumerated true binary endpoint pair counts from a shared hidden state and compared each bin with the product of the marginals. | `7edb82e69c95a03b1bc3bfe76a2b7a2b5a3a19412b4fb218356d7fd2420de572` |
| Grandchild | Evaluated a two-step reversible transfer directly and by the squared fine residual for an unequal partition of four states. | `0d009b4f4474a7cfa0d3104f2732634731dc42fcb0d081789c87b3a6c36763cd` |

The [generated Lean source](CoarseMemory.lean) has SHA-256 `076733c8e5da0b7120f5be09b210cf3594261df79f4225b92c5bb678dd178f37`. Five declarations passed on Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`. Axiom reports list only the standard Lean axioms. Two mutations that doubled the conditional variance or the binary residual failed to compile. The Wilson and relative entropy expansions are [written proofs](README.md).

**Direct binary chain.** The [Python check](check.py) uses signs for the coarse loop and perturbing face on a four-state orbit space. At zero coupling their three characters have multipliers $r=q^k$, $\lambda=q^4$, and $t=q^{k+4-2d}$ for $d$ shared edges. A magnetic insertion is the face sign. The code diagonalizes the perturbed transfer, recomputes its stationary vacuum, conditions on both possible middle coarse signs, and sums the eight endpoint/middle bins in 55-digit arithmetic. In this model the memory coefficient is $D_n(t)^2$. The quartic information coefficient is $D_n(t)^4/[2(1-r^{2n})^2]$: given the middle sign $y$, the electric conditional endpoint mean is $r^ny$, and the deviation of the joint conditional probability at $(z,w)$ from the product is $zw$ times the conditional covariance divided by four. Direct evaluation at $b=0.0005$, $q=0.85$, $k=8$, $n=3$ gave scaled information $6.587742945\times10^{-8}$ for one shared edge and $6.792410268\times10^{-6}$ for two. Omitting the entropy factor of two failed the numerical check.

**Continuous SU(2).** A separate seeded control constructs all faces touching a side-two square, traverses the detoured cycles, and samples their joint link holonomies under Haar measure. Across 16,384 independent configurations at $g=9,n=2$, the squared first-derivative reading had mean 0.00681157 with batch standard error 0.00009119. The coefficient from the singlet and triplet sum is 0.00680723. Doubling the predicted coefficient failed this independent reading test. This check integrates the exact first-derivative observable at the electric point; the finite-$b$ three-time computation above is for the binary chain.

From this directory, run the [host replay](../../replay-guests.py) with the supported kernel and compiler, then use the pinned Lean environment. The Python calculations require NumPy, SciPy and mpmath. [Native guest source](worker.c)

```sh
python ../../replay-guests.py /path/to/kernel.elf32 --proof CoarseMemory.lean
lake env lean CoarseMemory.lean
python check.py
```
