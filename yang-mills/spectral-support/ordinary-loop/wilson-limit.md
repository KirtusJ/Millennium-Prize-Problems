# From the Wilson vacuum to the contour current

At inverse coupling $\beta$ and spatial period $L$ in cells use the infinite-time transfer vacuum of the original isotropic Wilson law. At a time slice $W_C=\operatorname{Re}U_C=\tfrac12\operatorname{Tr} U_C$ for the path-ordered product of unit quaternions on an oriented contractible lattice path. An inverse traverse uses the inverse link. Open paths to a common vertex are included whenever several words at one slice are multiplied inside a trace.

**Microscopic input.** For each fixed finite list of lattice faces transported into a common frame along fixed paths, C4 derives joint convergence of $\sqrt\beta\,\operatorname{Im}U'_p$ to three independent centered lattice Gaussian curvature fields when $\beta,L\to\infty$. Each component has covariance $P=d(-\Delta)^{-1}d^*$. Kernel values at the zero Fourier mode are immaterial in infinite volume. The uniform bound on $\mathbb E\exp(\beta(1-\operatorname{Re}U_p)/8)$ supplies joint moment convergence. This lane depends on that written Wilson-law argument, including removal of the constant two-form by reflection. D4 previously rebuilt the accompanying Lean module and its controls. The derivation of the field limit is a mathematical dependency outside those formal checks. [Wilson law](../../central-quotients/tangent-curvature/wilson-law.md) · [Gaussian projection](../../central-quotients/tangent-curvature/gaussian.md) · [Reflection](../../central-quotients/tangent-curvature/reflection.md) · [Moments](../../central-quotients/tangent-curvature/moments.md)

**Exact ordered reduction.** Tile a contractible polygon by an oriented lattice disk, allowing repeated faces in a disk mapping into the lattice. Its boundary word is a product of transported elementary face words and their inverses: peel a face, inserting the path to the exposed edge and its inverse; backtracks cancel. More generally, the cubic lattice with all square relations is simply connected, by commuting coordinate steps past one another and cancelling inverse pairs. Either construction supplies a finite ordered list $A_1,\ldots,A_M$ equal in product to $U_C$. Let $F_\ell=\epsilon_\ell\sqrt\beta\,\operatorname{Im} U'_{p_\ell}$ be the oriented imaginary part. For each $p\ge1$, the exponential bound and $|A-1|^2=2(1-\operatorname{Re} A)$ give
$$
 \|A_\ell-1\|_{2p}\le c_p/\sqrt\beta,\qquad
 \|1-\operatorname{Re} A_\ell\|_p\le c_p/\beta .
$$
We use Euclidean quaternion norm and probability $L^p$ norm. Write $B_i=A_1\cdots A_i$. The telescoping error is $\sum_i(B_{i-1}-1)(A_i-1)$, with $|B_{i-1}-1|\le\sum_{h<i}|A_h-1|$. Hölder then yields, identifying a vector with a pure imaginary quaternion,
$$
 \left\|\sqrt\beta(B_M-1)-\sum F_\ell\right\|_p
       \le c_p M^2/\sqrt\beta .
$$
Since each of the two compared quantities has $L^{2p}$ norm at most $c_p M$, the unit-quaternion identity also gives
$$
 \left\|\beta(1-W_C)-\tfrac12|\sum F_\ell|^2\right\|_p
       \le c'_p M^3/\sqrt\beta .
$$
These bounds control the noncommutative product error. Approximation of the still-dependent $F_\ell$ by a Gaussian on a growing surface requires a separate limiting argument.

**Fixed mesh.** First keep every path and time difference fixed in cells. For several slices choose common temporal trunks to one overall root. This conjugates each trace without changing it, and the root paths are fixed for the microscopic input. The joint moments of $\sqrt\beta\,\operatorname{Im} U_C$ converge to those of the three-color Gaussian $X_C$ paired with the oriented filling. The boundary current determines its covariance by discrete integration by parts. Center the defect using its **actual vacuum expectation**. Then
$$
 Q_C^\beta=\beta(\mathbb EW_C-W_C)
     \longrightarrow \tfrac12\big(|X_C|^2-\mathbb E|X_C|^2\big)
$$
in joint moments. This convention fixes the sign of the three-point reading. For centered positive traces the two-point reading is identical and the three-point sign reverses.

**One simultaneous sequence.** Fix spatial meshes $b_j=2^{-j}$. Enumerate all finite tests formed from dyadic rectilinear contours, dyadic physical insertion times, polynomial degrees and common-root words. At stage $j$ impose the first $j$ tests whose coordinates already lie on the grid; each fixed test is eventually always included. Add the finite list of mixed moments at that mesh needed to form their centered products or to Wick-order a vertex. The cutoff Gaussian Wick coefficients may grow with $j$; choose the finite-moment tolerances small enough that the final error in *each polynomial reading*, including its coefficients, is below $2^{-j}$. Include the equal-time centered variance for the reference square and its unscaled trace mean. For each fixed stage every list is finite. The fixed-mesh limit supplies sufficiently large integers $\beta_j,L_j$ for all these conditions together. Impose also $\beta_j\ge b_j^{-j}$, $L_j b_j\ge j$, and increasing $\beta_j,L_j$. The resulting sequence approximates its infinite-lattice Gaussian comparison in absolute error for every enumerated reading. In particular $\mathbb EW_C\to1$ for each fixed physical polygon: a tiled surface has $M=O_C(b^{-2})$ and $\mathbb E(1-W_C)\le cM^2/\beta$.

The kernel limit in the next note is subsequently taken on this same sequence. Self-correlations at arbitrary positive times follow by monotonicity of the positive transfer spectrum between dyadic times; for two different time-slice vectors use polarization. Use the integer time lag $\lfloor t/b_j\rfloor$, or the fractional positive transfer power at strictly positive times; the two have the same limit by this sandwich. Multipoint limits asserted here concern the enumerated distinct dyadic times. No Wilson running-coupling formula, continuum mass scale or universal rate for comparison of growing Wilson surfaces with the Gaussian is assumed. [Continuum kernel](loop-kernel.md)
