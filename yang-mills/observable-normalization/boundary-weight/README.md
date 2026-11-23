# Boundary weight of the excess static spectrum

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

In D4's open spatial cube, every normalized vector in the spectral subspace of the static covariance above $4+\delta$ has a positive fraction of its squared norm within a boundary layer of thickness independent of the box size. This holds for arbitrary superpositions in that subspace. The bound quantifies where the area-order excess can be measured. [D4's multiplicity theorem](../../spectral-support/boundary-spectrum/) · [B4's static reduction and row bound](../../transfer-operator/girth-shell/open-box.md)

Let the cube occupy $[0,N]^3$ in lattice units. For an integer $r\ge1$, call a plaquette interior if its entire closed square lies in $[r,N-r]^3$. Write $B_r$ for coordinate restriction to all remaining plaquettes. Let $K_N=6(P_N\circ P_N)$ in the oriented face basis. Set $e_r=2/(r+1)$. For $e_r<\delta\le1$, the upper spectral space $V=\mathbf1_{[4+\delta,\infty)}(K_N)\mathbb R^{F_N}$ satisfies
$$
 \|B_r v\|^2\ \ge\ \frac{\delta-e_r}{1-e_r}\,\|v\|^2\qquad(v\in V).
$$
For instance, $r+1\ge4/\delta$ gives squared boundary weight at least $\delta/(2-\delta)$, uniformly in $N$. If the interior is empty the assertion holds directly. The coordinate map restricted to $V$ is injective with inverse norm on its image at most $\sqrt{(1-e_r)/(\delta-e_r)}$.

## Comparison with translated smaller cubes

Extend each face projection by the identity on exterior faces of the infinite cubic lattice. Its complementary projection has range the span of the oriented boundaries of the included three-cells. Inclusion of cell sets gives reverse order of the extended face projections. In particular, if $p$ is interior and $q$ is **any** parallel face of an $r$-cell-per-side cube, translate the small cube so $q$ coincides with $p$. This translated cube lies inside the large one, since no point of the small cube extends more than $r$ along any coordinate beyond the matched square. Thus $(P_N)_{pp}\le(P_r)_{qq}$ for each such $q$, including exterior small-cube faces. Orientation signs do not affect diagonals.

Average over $q$. The three orientation classes have equal cardinality and equal diagonal sum by cubic symmetry. Incidence has full row rank, so $F_r=3r^2(r+1)$ and $\operatorname{tr}P_r=F_r-r^3$. Hence every interior row of $K_N$ has sum
$$
 6(P_N)_{pp}\le6(F_r-r^3)/F_r=4+2/(r+1).
$$
All rows have sum at most five by B4's one-cell variational test. Since the entries of $K_N$ are nonnegative and symmetric, its quadratic form is bounded by that of its diagonal matrix of row sums (subtract the forms and sum the weighted squared coordinate differences). For a unit vector with boundary weight $w$ this gives $\langle v,K_Nv\rangle\le5w+(4+e_r)(1-w)$. On $V$ the left side is at least $4+\delta$. Rearranging proves the estimate. The same inequality bounds the norm of the compression to interior coordinates by $4+e_r$.

The layer estimate applies after the temporal strong-coupling and spatial weak-coupling limits in that order at each fixed box. It gives neither exponential decay of individual eigenvectors nor uniform convergence from finite couplings. The four-dimensional continuum problem remains open.

## Four layers suffice for the 4.01 threshold

A single well-placed small-cube face gives a sharper row bound. In a cube of even side $s=2m$, choose the interior face separating dual cells $(m-1,m-1,m-1)$ and $(m,m-1,m-1)$, using zero-based indices. With any target face at clearance $m$ the translated cube fits, after permuting the axes. Write $h$ for the signed dipole on those cells and $A=HH^T$ for the grounded cube Laplacian (diagonal six). For any integer array $g$ and positive integer $D$,
$$
 h^T A^{-1}h\ge 2h^T g/D-g^TAg/D^2 .
$$
This follows by completing the square. Since $P_{qq}=1-h^TA^{-1}h$, a lower certificate for the resistance gives an upper certificate for the row sum. The [reproducible trial](check.py) rounds a sine-transform solution to propose $g$ and evaluates the dipole and all squared bond differences with integer arithmetic. The following rational upper bounds on the excess over four were obtained in that computation.

| Boundary thickness | Excess upper bound |
|---:|---:|
| 2 | 718467154919 / 25000000000000 |
| 4 | 19056398149 / 5000000000000 |
| 8 | 13292005661 / 25000000000000 |
| 16 | 1788301067 / 25000000000000 |

With four layers one may use $e=0.003812$ in the boundary-weight inequality. At threshold 4.01 every normalized vector in the excess spectral subspace therefore has squared boundary weight greater than 0.0062. This quantitative bound holds throughout the subspace even when the number of excess directions grows proportionally to surface area.

## Verification

Three nested PCP OS guests, dispatched by the host, emitted [BoundaryWeight.lean](BoundaryWeight.lean) from [worker.c](worker.c). A separate three-boot replay reproduced SHA-256 `455bdc70e6c89f0e7451b7ed68b94f2c32f67c0ffb66d802ba6cf5e24c6f4e0a`. Under Lean 4.19.0 and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`, all three supporting declarations compiled with standard axioms. They check averaging, the boundary-fraction inequality and the cube trace arithmetic. The translated projection comparison and resistance witness construction are in the text. The [guest replay](../transfer-increments/replay-guests.py) accepts the same measured kernel as the [first-band packet](../uniform-band/execution.md).
