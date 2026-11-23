# Checks on the site scalar and its normalization

Two PCP OS deployments each booted a measured parent, child and grandchild program, with the host relaying child requests. Each guest ran its arithmetic checks and produced a 47-event kernel register. The two runs emitted byte-identical Lean. Lean 4.19.0 with Mathlib commit `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked seven declarations. The axiom reports contain only `propext`, `Classical.choice` and `Quot.sound`; the noncommutative paired-product declaration uses only `propext`. [Worker](worker.c) · [Generated source](SiteScalar.lean) · [Replay convention](../../execution.md)

| Item | SHA-256 |
|---|---|
| Kernel ELF | `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` |
| Parent ELF | `a34cdf3a77c35298c3ba43da440b14586a640a4294b3be56a9f8a35c4d9212da` |
| Child ELF | `20301d1230c31d5f78c9719b6d05fb5dffc4997c12899c2e95e8c52885318f61` |
| Grandchild ELF | `d9bcb1805c71a227d68637a68c69763074e2a2e1a293c153012617dfc373d8a1` |
| Generated source | `1761bb55d78b54391b641415cd29551cb772a5118832d2ddd4ab6bc882eeb5ab` |

The formal results bound an edge by its two nearest-distance factors, center the trace sum with the correct sign, propagate the Hodge sign through a noncommuting product, cancel the invariant trace of an odd cycle, compute the two- and four-point coefficients, and propagate a positive ratio along integer strides of a log-convex correlation. The four altered versions halve the edge bound, replace the odd factor by an invariant one, triple the four-cycle coefficient, and reverse the initial ratio inequality. Each altered proof failed. At a constant unit correlation the reversed ratio hypothesis would allow $q=2$ and incorrectly give $2^n\le1$. The reflection, mixed-orientation Haar comparison, distributional limit and positive mass representation have written mathematical proofs.

The [Python checks](check_scalar.py) reduced 192 individual reflected face words across all six plane orientations and compared 972 displaced four-dimensional root paths with their rectangular exchanges. Quadrature for four positive mass-squared integrals recovered the unit-normalized continuum power law. Another check computed the infinite **free lattice** clover covariance by twice differencing the Bessel heat integral of the scalar Green function and summing all 576 face pairs. For the three equal-length directions proportional to $(5,0,0,0)$, $(4,3,0,0)$ and $(4,2,2,1)$ it gave the following values of $|z|^8\pi^4 C_G(z)/9$.

| Lattice distance | Axis | Two components | Four components |
|---|---:|---:|---:|
| 5 | 2.65741772 | 1.57658738 | 1.17904867 |
| 10 | 1.19440411 | 1.07910561 | 1.05023725 |
| 20 | 1.04183593 | 1.01758381 | 1.01297513 |
| 40 | 1.01011096 | 1.00427793 | 1.00327088 |

At 128 random quadrilateral geometries, rotating all four points preserved the fourth cumulant to the stated numerical tolerance. The largest magnitude of the triangle trace was $2.2\times10^{-15}$. Removing one orientation gave a collinear triangle trace of magnitude one. The full collinear four-cycle ratio was $2/9$. Exact rational arithmetic verified 182 clock bounds on both point and mixed positive spectra, including time lags between integer strides. These numerical results test the geometry and the free reference. The estimates on compact Wilson measures use the proofs in the [research note](README.md).

Run the first two commands from this directory. Run the last from the pinned Mathlib checkout.

```sh
OPENBLAS_NUM_THREADS=1 python check_scalar.py
python ../../replay-guests.py "$KERNEL" --proof SiteScalar.lean --qemu "$QEMU_WRAPPER" --firmware "$FIRMWARE"
lake env lean /path/to/SiteScalar.lean
```
