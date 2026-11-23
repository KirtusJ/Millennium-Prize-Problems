# A tapered upper bound on the Wilson odd-clover variance

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For A4’s parity-odd clover $P$ in four-dimensional pure SU(2) Wilson theory, let $\chi_\beta$ be the infinite-volume box variance per lattice site of its sum. In every thermodynamic limit of even periodic isotropic cubes, at sufficiently large $\beta$,
$$
             c\beta^{-1}\le \chi_\beta\le C\beta^{-1/24}.
$$
The lower bound is A4’s three-link estimate. The upper bound improves the exponent $1/40$ by tapering the four sides of the variance test. For the raw polynomial $q=P/\beta$ the upper bound is $C\beta^{-2-1/24}$. These are bounds for the specified lattice observable. Its renormalized physical susceptibility and the continuum mass gap remain open. [A4’s clover and normalization](../../../observable-normalization/transfer-increments/local-action/odd-clover/README.md) · [Local lower bound](../../../observable-normalization/transfer-increments/local-action/odd-clover/local-variation.md)

## Review of the boundary terms at bdaf179

For a site reflection $x_i\mapsto 2s-x_i$, a cell with lower coordinate $y_i$ moves to the cell with lower coordinate $2s-y_i-1$. The corner bit $c_i$ changes to $1-c_i$; each other corner bit is preserved. The based plaquette paths transform edge by edge. The factor $\prod_j(1-2c_j)$ changes sign. Thus a weighted sum of corners with coefficient independent of $c_i$ is reflection odd about its cell center in the sense of this exchange.

For the site-to-cell difference the coefficient is $\mathbf1_{B_N}(y+c)-\mathbf1_{B_N}(y)$. On a rectangle of the partition into $-1,[0,N-2],N-1$ in each coordinate, this coefficient is independent of every bit belonging to an interior coordinate. The all-interior rectangle contributes zero. Hence each contributing rectangle has at most three long directions, all available for reflection. Splitting each of these into a multiple of two and at most one more cell yields a bounded number of pieces even for odd $N$. Pairwise reflection negativity along the long axes bounds their variances by $O_\beta(N^3)$. The triangle inequality bounds the centered norm of the whole discrepancy by $O_\beta(N^{3/2})$.

For full cells, at fixed even $h$, the $kh$ core tiles with variance at most $k^4V_D(h)$. Remainder rectangles have at most three long axes and contribute total centered norm $O_{\beta,h}(N^{3/2})$. The core norm is $O_{\beta,h}(N^2)$, so the mixed error after division by $N^4$ tends to zero. Along even sides the infimum of $V_D(h)/h^4$ over even $h$ is a lower bound by definition and the preceding tiling gives the reverse limsup. The one-cell shell comparing odd $N$ to $N-1$ obeys the same boundary estimate. This proves the full limit and its equality for the two centerings of the charge. [Tiling proof under review](../../../observable-normalization/transfer-increments/local-action/odd-clover/tiling.md) · [Menotti and Pelissetto on site-plane positivity](https://doi.org/10.1007/BF01221251)

## A box is bounded above by a tapered test

Collect $2^4$ cells of A4’s odd, cube-supported charge $D$ into $S(z)=\sum_{v\in\{0,1\}^4}D(2z+v)$, $z\in\mathbb Z^4$. The block lives on the closed cube $2z+[0,2]^4$. Its mean is zero. Fix an axis and any real finitely supported transverse weights $g$. Let $U_l=\sum_{z_\perp}g(z_\perp) S(l,z_\perp)$, and $c_g(k)=\mu[U_0U_k]$. For every $k\ge1$ reflection in the fine-lattice **site** plane $x_i=k+1$ exchanges the two slabs, takes $U_0$ to $-U_k$, and has their supports in opposite closed halves. Tangential links may lie on the shared plane at $k=1$. Reflection positivity gives $c_g(k)\le0$. This statement applies after imposing any of the other three axial weights.

For a nonzero finite real sequence $v$, let $A_v(k)=\sum_l v_l v_{l+k}/\sum_l v_l^2$. Then
$$
 \frac{\operatorname{Var}(\sum_l v_l U_l)}{\sum_l v_l^2}
       =c_g(0)+2\sum_{k\ge1} A_v(k)c_g(k).
$$
Take $v$ to be the positive sine sequence $v_l=\sin(\pi(l+1)/(h+1))$ on $0\le l<h$, zero elsewhere. For $k\ne0$, $A_v(k)<1$ by strict Cauchy–Schwarz for a nonzero shift of a finite sequence. For fixed $h$ the box autocorrelation $(1-k/N)_+$ therefore dominates $A_v(k)$ simultaneously at every $k\ge1$ for all sufficiently large $N$; only $1\le k<h$ require a comparison. Replacing a normalized box weight by $v/\|v\|_2$ can only increase the variance. Repeat along each axis, keeping the other weights fixed. With $f=(v/\|v\|_2)^{\otimes4}$ the result is
$$
 16\chi_\beta=\lim_{N\to\infty}
 \frac{\operatorname{Var}(\sum_{z\in B_N} S(z))}{N^4}
 \ \le\ \operatorname{Var}(\sum_z f(z)S(z)).
$$
The factor 16 converts coarse volume to fine volume. The comparison first takes $N$ to infinity at fixed $h,\beta$. It needs neither absolute summability of Wilson covariances nor a sign for their individual off-axis entries.

## Cost of the test

Write $K$ for the infinite-lattice Gaussian covariance of the coarse charge. By A4’s free cancellation, $\sum_z K(z)=0$: in the sum over positions and both corners, the displacements $2z+v-u$ cover the fine lattice once for each fixed $u$. The bound $|K_D(x)|\le C(1+|x|)^{-8}$ on the fine covariance implies $\sum_z |z|^2|K(z)|<\infty$ in four dimensions. Both operations are absolutely convergent. [Gaussian cancellation and decay](../../../observable-normalization/transfer-increments/local-action/odd-clover/gaussian.md)

The sine is the lowest Dirichlet mode on the interval, hence $A_v(1)=\cos(\pi/(h+1))$. Telescoping translations in $\ell^2$ gives $1-A_v(k)\le k^2(1-A_v(1))$. Since each $A_v\in[0,1]$, the full product differs from one by at most $C|z|^2/h^2$. Subtracting the zero total covariance from the free variance yields
$$
 0\le\sum_z K(z)\prod_i A_v(z_i)\le C h^{-2}.
$$
A4’s local Wilson comparison changes each coarse covariance by $O(\beta^{-1/8})$ for separations of order $h\le c\beta^{1/4}$, with only a fixed number of fine cells per pair. The squared $\ell^1$ norm of $f$ is at most $h^4$ by its unit $\ell^2$ norm and support size. Thus $16\chi_\beta\le C(h^{-2}+h^4\beta^{-1/8})$. Choosing $h=\lfloor\beta^{1/48}\rfloor$ proves the stated uniform upper bound. [Computational checks](checks.md)

Near product Haar measure the raw clover covariance has an explicit quadratic correction at contact and a summable fourth-order remainder. [Strong-coupling contact coefficient and review of the local dual](haar-expansion/README.md)
