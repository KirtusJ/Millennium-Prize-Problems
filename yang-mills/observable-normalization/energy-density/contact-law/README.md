# White noise in the conditionally centered Wilson action

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Consider the defining four-dimensional isotropic SU(2) Wilson action on a hypercubic lattice. Put $Y_p=\beta(1-\operatorname{tr}U_p/2)$. At spacing $b$, give face $p$ of orientation $ij$ the weight $b^2 f_{ij}(x_p)$, where $x_p$ is its physical center and the six profiles are real, smooth and compactly supported. Write $A_b(f)$ for the resulting sum. Choose the deterministic link mask below and let $P_M$ denote conditional expectation given all links outside it.

In the infinite-time Wilson vacuum on periodic spatial tori, as $b\to0$, $\beta,L\to\infty$, $bL\to\infty$, the residual $A_b-P_M A_b$ converges on finite families of tests to a centered six-component spatial and temporal white noise. Its conditional characteristic functions given the exterior converge in $L^1$ to the deterministic Gaussian characteristic functions. Thus the limit factors even against bounded, cutoff-dependent exterior readings. The argument uses the program's [microscopic tangent law](../../../central-quotients/tangent-curvature/) and [exponential moments](../../../central-quotients/tangent-curvature/moments.md) as analytical inputs.

With $r_i(f)=\sum_{j\ne i}f_{ij}$ (extend edge labels symmetrically), the covariance is
$$
 \int_{\mathbb R^4}\sum_{i=1}^4\left[
 \frac{r_i(f)r_i(g)}{48}+\frac d{16}\sum_{j\ne i}
 (f_{ij}-r_i(f)/3)(g_{ij}-r_i(g)/3)\right]dx .
$$
Here $a_j=2-2\cos k_j$, $A=\sum a_j$ and $d=\int a_1^2/A\,dk/(2\pi)^4\simeq0.70662424$, over the Brillouin torus. The covariance matrix has eigenvalues $1/8,(1+2d)/24,d/8$ with multiplicities $1,3,2$. The equal-profile sum has coefficient $3/4$. Every orientation mode carries a positive contact component. Construction of a continuum interacting action field or physical mass gap still requires control of the exterior part.

Faria da Veiga and O’Carroll give uniform generating-function bounds for scaled plaquette fields on periodic lattices in Theorem 4. Their Eq. (30) uses the imaginary trace of the holonomy minus the identity. In the defining SU(2) representation the eigenvalues are a conjugate pair, so that scalar vanishes exactly. The real action used here has nonzero fluctuations, and the transfer-vacuum inputs for its moments are specified above. [Full text, Eq. (30) and Theorem 4](https://arxiv.org/pdf/2205.07376)

## The conditional covariance of one link

Fix a direction $i$. For each transverse direction $j$ the two incident face traces are $x_{j\pm}=U_e\cdot v_{j\pm}$ with unit exterior three-link transporters in quaternion coordinates. Set $s_j=v_{j+}+v_{j-}$, $H=\beta\sum s_j$, $R=|H|$, $h=H/R$. At fixed exterior the density of $U_e$ is proportional to $\exp(U_e\cdot H)$. Write $z=U_e\cdot h$ and $m=\mathbb E_R z=I_2(R)/I_1(R)$. The three pair actions $Y_{j+}+Y_{j-}$ have conditional covariance matrix
$$
 V_{jk}=\beta^2\left[\operatorname{Var}_R(z)(s_j\cdot h)(s_k\cdot h)
        +(m/R)s_j^\perp\cdot s_k^\perp\right].
$$
At zero staple use the isotropic covariance $I_4/4$. The formula follows by rotations fixing $h$ and a one-dimensional integration by parts. [Finite-cutoff calculation](../wilson-contact/conditional.md)

Write $\delta=6\beta-R$. The triangle inequality gives $0\le\delta\le\sum Y_p$. The vacuum moment bound therefore gives $R/\beta\to6$ in probability. In the link frame $U_e=1$ the real parts of the six transporters are $1-Y_p/\beta$; their imaginary parts times $\sqrt\beta$ are the signed rooted tangent curvatures at the two faces of each pair. For a fixed patch, changing the bounded root paths changes their limiting frame by a common rotation or a vanishing holonomy error. Thus jointly $s_j\cdot h\to2$ and $\sqrt\beta\,s_j^\perp$ in this frame tends to $C_j-\bar C$, where $C_j=F_{ij}(x-\hat j)-F_{ij}(x)$ up to a common sign and $\bar C=\sum C_j/3$. This also follows by expanding $h=(\sum s_j)/|\sum s_j|$ to first order about the real unit. Gram entries of this limit are independent of the root frame. The radial and transverse eigenvalues satisfy $R^2\operatorname{Var}_R(z)\to3/2$ and $m\to1$.

For one color, the exact-curl Fourier projection gives $\mathbb E C_j C_k=\int(\mathbf1_{j=k}a_i a_j+a_j a_k)/A$. Permutation symmetry makes this matrix constant on and off the diagonal, with diagonal minus off-diagonal $d$. Subtracting the three-coordinate mean therefore gives covariance $dP_3$, $P_3=I-\mathbf1\mathbf1^T/3$. Cauchy–Schwarz gives $d>(\int a_1)^2/\int A=1/2$ strictly, and $a_1^2/A<a_1$ almost everywhere gives $d<2$. The resulting mean conditional matrix is $\mathbf1\mathbf1^T/6+(d/2)P_3$, including all three colors. Convergence of expectations and fixed-offset covariance products follows from uniform moments of each $V_{jk}$: conditional Cauchy–Schwarz bounds these by conditional moments of the incident actions, and Jensen transfers the uniform moment estimates.

## From a single link to a continuum test

Partition the first spatial axis in lattice cells into slabs of width $m_b\to\infty$, $bm_b\to0$. Cycle link orientations through the four directions, one per slab. Omit the first and last layer of each slab. Within a slab use even parity on the sum of the three coordinates transverse to its link direction. Place the periodic cut outside the support and omit its boundary layers in the periodic directions (including any incomplete end slab). No face contains two selected links. The selected links have density $1/8$ per orientation in physical Riemann sums. A mask stable across arbitrarily large compact sets can use centered fundamental boxes. Conditional on the exterior of the mask the selected links are independent. Only finitely many contribute for any compact test. On the infinite-time cylinder the same factorization follows by conditioning first on a finite set of sites and using the one-link Gibbs specification.

Within each star replace both face-center weights by their link-center value. After conditional centering the variance of the difference is at most $C b^4\sum_{e\text{ in support}} b^2=O(b^2)$ by conditional independence and uniform action second moments. The conditional variance of the replaced sum is $b^4\sum_{e\in M} f_e^TV_e f_e$.

Here microscopic convergence alone does not permit substituting the spatial average by its expectation over a growing box. For each fixed even shift $u\in(2\mathbb Z)^4$, translating each coefficient mask times its test products changes their normalized discrete $L^1$ norm by $o(1)$, from smoothness and the $O(|u|/m_b)$ fraction of stripes meeting a boundary. Uniform local second moments bound the resulting error in $L^2$. Hence replace the centered covariance field for each orientation by its average over a fixed even-shift cube of side $K$. By the triangle inequality the weighted sum's $L^2$ norm is bounded by a constant times the block average's $L^2$ norm. Stationarity and fixed-block convergence allow taking the cutoff limit first. In the tangent law the localized Gram fields are quadratics of finitely many Gaussian curls. Their covariance tends to zero at large displacement by the Riemann–Lebesgue lemma for the bounded projection symbol and Wick's formula. Consequently the limiting block-average variance tends to zero as $K\to\infty$. This proves concentration of the conditional variance at the displayed integral without a cutoff-uniform mixing estimate.

For any real linear combination of the tests let $X_e$ be the corresponding centered one-link contribution with the factor $b^2$ included, and $v_e=\mathbb E[X_e^2\mid\mathrm{ext}]$. The conditional characteristic function at argument one differs from $\exp(-\sum v_e/2)$ by at most $C\sum\mathbb E[|X_e|^3\mid\mathrm{ext}]+\sum v_e^2/8$. Taylor expand each factor through order two, use the nonnegative-real exponential remainder bound and telescope products of contractions. The two sums have expectations $O(b^2)$ and $O(b^4)$ respectively. This gives the stated conditional convergence. Along every tight exterior subsequence the joint limiting laws of the exterior tests and the residual are independent. For test supports separated by more than a star diameter, the residual terms have zero cross covariance at finite cutoff and projection preserves the original separated two-point reading.

For the spectrum, if $B$ is the unsigned vertex-edge incidence matrix of the complete graph on four vertices, the covariance density is $(d/8)I+((1-d)/48)B^TB$. The matrix $BB^T=2I+\mathbf1\mathbf1^T$ gives the three claimed eigenspaces. The smallest eigenvalue exceeds $1/16$.

## Sharp spatial slice

For the earlier single spatial-face test, normalize by $b^{3/2}\sum fY_p$ and use the three spatial orientations of the [single-slice mask](../wilson-contact/). Two out of three orientations hit the face, each with link density $1/2$. The mean local diagonal tends to $1/6+d/3$. The exact mask-averaged squared prediction error therefore tends to $(1/18+d/9)\int f^2$, or about $0.13406936\int f^2$. This concerns the average of the individual conditional variances. Averaging the predictors before computing variance loss adds the dispersion of those predictors. The [free Gaussian calculation by Z4](../../../z4/reviews/r8-contact/report.md) independently gives the same coefficient for its regulator. Its full sharp variance has a different coefficient.

[Exact gamma coupling on finite Wilson histories](radial.md) · [Proof and numerical checks](execution.md)
