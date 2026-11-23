# Which part of the conditional-mean covariance is still unknown?

There is an exact way to read the distant part of the conditional-mean covariance directly from the raw measurements. For the $xy$ checkerboard on one slice write $\mu_x=\mathbb E[X_x\mid\mathcal B]$. Each $\mu_x$ integrates the one selected link in its own face. Under the common exterior two plaquettes assigned to different links are conditionally independent. Consequently
$$
 \operatorname{Cov}(\mu_x,\mu_y)=\operatorname{Cov}(X_x,X_y)
$$
for every pair except the identical face and the two faces on the same selected link. The latter bases differ by one step in $y$. This holds for each fixed choice of checkerboard and in particular for every pair at periodic maximum-coordinate distance at least two. It requires neither reflection positivity of a projected field nor a boundary extrapolation. In an open finite preparation it applies to the actual open Gibbs law at an interior time.

The consequence for physical refinement is an equivalence. Put $T_N=\sum_{|x|_{\infty,N}\ge2}C(x)$ for the raw connected covariance of a fixed orientation. Since $|C(x)|\le K$, the 27 sites in the contact and first shell give $|\chi-T_N|\le27K$. The full unfiltered variance is uniformly bounded above exactly when $T_N$ is uniformly bounded above along the same vacuum sequence. At every term of $T_N$ the conditional-mean covariance is identical. There is no need to rerun the chains to estimate the **ensemble** tail of the conditional means with a raw-field estimator. The [observed signed tails](measurements.md) range from −0.00362 to +0.00329 across five finite preparations, with stream errors from 0.0074 to 0.0116. Positive and negative terms can cancel; the [axial criterion](spatial.md) gives a stronger sufficient test using an absolute majorant.

### The exact correction at all momenta

For each of the two complementary checkerboards let $G_\mu$ be the covariance of its conditional means. Average these **covariance matrices** to obtain $\bar G_\mu$. The law is translation invariant in space and a unit step in $y$ or $z$ exchanges the colors. Total covariance gives a positive difference from $G$, supported only at offsets $0$ and $\pm e_y$. Write $b$ for the diagonal correction averaged over the colors, and $c$ for the expected conditional covariance of the two faces of a selected link. A given forward neighboring pair shares a selected link in exactly one of the two colors. The other color contributes zero. By translation and reflection the two off-diagonals are each $c/2$. Hence on the fine spatial torus,
$$
 \widehat G(k)-\widehat{\bar G}_\mu(k)=b+c\cos k_y,\qquad
 0\le b\pm c\le2b\le2K .
$$
Indeed $b$ is an average of conditional variances, at most the raw single-plaquette variance. The correction is positive semidefinite, and both $0$ and $\pi$ are allowed for even $N$. At $k=0$ it equals the local term $J$ in [the unfiltered variance identity](README.md). This gives a uniform absolute bound on the change at every momentum, including the whole infrared region. The averaged matrix is not in general the covariance of the average of two conditional means. A bound on the full isotropic tail of either field remains open. [Gaussian matrix and Fourier check](contact.py)
