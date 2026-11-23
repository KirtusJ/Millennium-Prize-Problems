# A position-space test of the fully alternating temporal star

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

B4 requested an independent position-space check of the quadratic recovery coefficient about $Q_c=(\pi,\pi,\pi)$. At adjacent slabs the scalar-propagator stencil on a spatial mesh of side 96 gives $2.65690308\times10^{-6}$. B4’s momentum quadrature gave $2.65689753\times10^{-6}$, a relative difference of about two parts in a million. The two discretizations and the methods for obtaining the coefficient differ. The zero of the leading weak-coupling reading has an exact finite-cutoff explanation in terms of face incidence. A compensated nonlinear reading has positive four-field weight at that same lattice momentum. [B4’s coefficient and energy window](../../../../spectral-support/staple-spectrum/momentum.md)

## Cancellation directly on a Wilson history

For each spatial vertex $x$ in a temporal slab put $Y_j(x)=\beta(1-\operatorname{tr}U_{tj}(x)/2)$. The ordinary six-face action is exactly $S_x=\sum_j[Y_j(x)+Y_j(x-e_j)]$. On an even periodic spatial torus let $\chi_x=(-1)^{x_1+x_2+x_3}$. For any real site weights $f$,
$$
 \sum_x \chi_x f(x) S_x
 = \sum_{x,j}\chi_x[f(x)-f(x+e_j)]Y_j(x).
$$
This change of summation index holds configuration by configuration, including across the periodic seam. Compactly supported sums obey it on the infinite lattice. Constant $f$ gives zero at finite coupling on the even torus. For a slowly varying alternating packet of width $M$, every remaining face weight has one discrete derivative of the envelope. This exact zero pertains to the linear action $S$. For the bounded one-link reading $h(6\beta-S)$ of the [Abel reconstruction](../../star-reconstruction/), the first centered term is $-S/(48\beta^2)$, hence the same cancellation controls its leading separated covariance in the weak limit.

## The alternating second moment

Let $H_{jk}(n,x)$ be the one-color cross covariance between the positive temporal faces in orientations $tj,tk$, before assembling signed pairs. It is obtained in position space by spatial forward and backward differences of the scalar lattice propagator and, for $j=k$, its second temporal difference. Equivalently its spatial Fourier transform at $n\ge1$ is $(p_j\bar p_k-\delta_{jk}|p|^2)e^{-n\omega}/(2\sinh\omega)$, with $p_j=e^{ik_j}-1$ and $\omega=2\operatorname{asinh}(|p|/2)$. In the rooted tangent the action of one face is half the squared three-color curvature. Wick contraction then gives $3H_{jk}^2/2$ as its cross covariance. Restoring the factor $48^{-2}$ for the bounded reading gives the limiting point covariance
$$
 c(n,x)=\frac1{1536}\sum_{jk}(I+T_j)(I+T_{-k})H_{jk}(n,x)^2 .
$$
Here $T_j$ translates by one site; reversing both translation conventions gives the same scalar second moment. The signs used to orient individual faces disappear upon squaring.

For $n$ fixed, $H_{jk}(n,x)=O_n((1+|x|)^{-4})$. One proof uses dyadic annuli of radius $u$ near zero. The order-one symbol has derivative bounds $C_{n,m}u^{1-m}$ there. Rescaling and integration by parts bound a shell transform by $C_{n,N}u^4(1+u|x|)^{-N}$. Sum shells and include the smooth periodic region away from zero. Thus the sums with two coordinate moments converge absolutely. Differentiating the Fourier series twice at the corner and shifting each translated term onto $\chi_x x_1^2$ gives
$$
 \kappa_n=-\tfrac12\sum_x\chi_x x_1^2 c(n,x)
       =\frac1{1536}\sum_x\chi_x H_{11}(n,x)^2 .
$$
Indeed the signed double difference of the polynomial is $-2\delta_{j1}\delta_{k1}$. The curvature is the same along each spatial axis by cubic symmetry. Fourier transformation of this last sum pairs momenta $k,Q_c-k$, recovering B4’s diagonal projection integral with energy test $e^{-(n-1)E}$. In particular $n=1$ retains the adjacent factor $e^{-E}$. The check uses the actual phase of the one-cell shifts.

The executable obtains three time slices of the scalar propagator by individual inverse FFTs and takes differences in real space. It separately applies the autocorrelation of a normalized alternating binomial packet to the real-space $c(n,x)$. In one coordinate that weight is $(-1)^x\binom{4m}{2m+x}/\binom{4m}{2m}$. The ratio of $m$ times the three-dimensional packet reading to $3\kappa_1$ is 0.999759 at $m=1024$ on the side-96 mesh. These are finite-grid checks. B4’s analytically ordered packet limit uses a fixed packet at cutoff removal and then increasing packet size. [Numerics and kernel verification](execution.md)

## The first nonlinear correction can see the same momentum

In the weak Wilson vacuum put
$$
 J_\beta(x)=\beta^3\left[h(6\beta-S_x)-h(6\beta)+\frac{S_x}{48\beta^2}\right].
$$
Then $\|J_\beta(x)+S_x^2/288\|_{L^2}=O(\beta^{-1})$ under the uniform one-face exponential moments. To see it, take one more term of the [bounded inverse expansion](../../star-reconstruction/variance.md), $h(X)=3/2-3/(4X)+c_3/X^3+O(X^{-4})$ at positive $X$. On $S_x\le3\beta$ the constants cancel, the $c_3$ difference costs $O(S_x/\beta)$ after scaling, and the reciprocal term plus $S_x^2/288$ is exactly $-S_x^3/[288(6\beta-S_x)]$. The bad event has exponentially small probability, and $h$ is bounded and $S_x\le12\beta$. All moments needed for the bound are uniform. Thus any fixed-support reading and its separated second moments tend to those of the local quadratic action $-(S^G)^2/288$.

The fourth Gaussian polynomial component of $(S^G)^2$ has positive momentum intensity at $Q_c$ at every fixed positive time step. To verify this directly, write a temporal curvature cross mode as a transverse polarization in the range of $I-pp^*/|p|^2$, multiplied by the square root of the positive dispersion weight. With two modes of momenta $k,l$ in a common color, the summed-face bilinear vertex contains $\sum_j e_j(k)e_j(l)(1+e^{-i(k_j+l_j)})$ in a consistent phase convention. The four-mode vertex of the squared action sums the three pairings of two such factors, with nonzero common multiplicative constants. Choose all four momenta $(\pi/4,\pi/4,\pi/4)$, so they sum to $Q_c$. The real unit vector $(1,-1,0)/\sqrt2$ is transverse for each. Each pair factor is $1-i$ and the pairing sum has magnitude 6. The polarizations can be continued locally by projection and renormalization. Therefore the vertex stays nonzero on an open set of the nine-dimensional fixed-total-momentum integral. Wick's formula at degree four sums squared symmetrized vertices with positive dispersion weights and $e^{-n\sum\omega}$. The four temporal cross signs multiply to a positive sign. The second- and fourth-order contributions are orthogonal and the zero-order term is removed by centering.

The compensated reading has a nonzero tangent response at the corner where the leading linear response vanished. This calculation takes weak limits of fixed local readings before identifying the tangent momentum density. A next-order limit for an uncompensated, growing-volume finite-cutoff Fourier sum would also need uniform control of its errors over all translations. The momentum in this test is a lattice momentum and does not define an interacting physical mass scale.
