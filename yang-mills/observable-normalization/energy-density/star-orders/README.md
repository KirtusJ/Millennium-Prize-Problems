# Bounded Wilson star observables of prescribed Gaussian order

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

On a four-dimensional isotropic SU(2) Wilson history let $S=\sum_{p\ni e}\beta(1-\operatorname{tr}U_p/2)$ be the ordinary action of the six faces incident to one temporal link. For every integer $q\ge1$ there is an explicit bounded function $\Psi_q(S)$ whose centered microscopic Gaussian limit has Hermite rank exactly $2q$. Hermite rank is the smallest degree with a nonzero coefficient in the orthogonal Gaussian polynomial expansion. In particular a single bounded reading can have zero covariance with **every quadratic tangent observable** even at coincident support and retain strictly positive separated autocorrelation.

The limiting positive-time correlation on selected weak Wilson regimes is proportional to $t^{-8q}$. The underlying transfer is the same for all the observables. Increasing the exponent changes the low-energy weight seen by a probe. At any fixed positive reference time $t_0$, its limiting normalized energy law is gamma of shape $8q$ and rate $t_0$, with support reaching zero. The result gives no interacting Yang–Mills construction on a trajectory with nonzero renormalized interaction. [Wilson comparison and explicit rates](physical-limit.md)

For $q=2$, four Laplace sources of the ordinary action remove its entire degree-two Gaussian component. Three suffice if only positive-time propagation is to be filtered. Both counts are optimal among finite linear combinations with distinct positive Laplace parameters under the specified cancellation requirements. With inverse source strengths $1/2,1,2,4$ and the normalization below, the $t^{-16}$ coefficient is about $1.98423\times10^{-7}$. A finite-box simulation at $\beta=2.3$ measured a residual one-step covariance with the ordinary action of $0.000268\pm0.000079$ on a periodic $4^4$ box. At $\beta=8$ this reading was $0.000123\pm0.000099$. The errors are blocked Monte Carlo estimates. The exact cancellation applies in the tangent law. [Numerical and formal scope](execution.md)

## The three one-link variances

Let $d=\int a_1^2/A$ on the normalized four-dimensional Brillouin torus, with $a_j=2-2\cos k_j$ and $A=\sum a_j$. The [equal-time Wilson star](../star-reconstruction/variance.md) has one-color covariance eigenvalues $1$, $a=d/2$ and $b=(2-d)/3$. The eigenvectors are the total signed-face sum, the two contrasts of normalized pair sums, and the three pair differences, respectively. Including three colors gives respective multiplicities $3,6,9$. Thus $S$ tends to $\sum_{\lambda}\lambda |Z_\lambda|^2/2$ with independent standard normal blocks $Z_\lambda$. This uses the [original-link tangent and moment estimates](../../../central-quotients/tangent-curvature/) in the infinite-time vacuum followed by $\beta,L\to\infty$ in any order relative to one another.

Distinctness matters in designing a filter. One can certify it without floating-point quadrature. Put $u=1-A/16$ and $x=a_1$. The integrand $x^2/A$ is bounded below by $x^2(1+u+u^2+u^3)/16$ and above by the same expression plus $xu^4$, since $0\le x\le A\le16$. At $A=0$ take the integrand to be zero. The one-dimensional moments are $\int a_j^k=\binom{2k}{k}$ by taking the constant Fourier coefficient. Independence of the four integration coordinates gives $\int x^2 A^j=6,56,562,5976$ for $j=0,1,2,3$, and $\int x A^j=2,18,176,1834,20112$ for $0\le j\le4$. Consequently
$$
 5285/8192\le d\le6439/8192<4/5,\qquad 0<a<b<1.
$$

## Constructing the reading

Let $E=\{1,a,b\}$, $m=3(q-1)+1$. Choose any distinct $r_i>0$ and set
$$
 P(z)=\prod_{\lambda\in E}(z-\lambda)^{q-1},\quad
 D(z)=\prod_{i=1}^m(z+r_i),\quad
 w_i=\frac{P(-r_i)}{\prod_{j\ne i}(r_j-r_i)},\quad
 L_i=(1+1/r_i)^{-3/2}(1+a/r_i)^{-3}(1+b/r_i)^{-9/2}.
$$
The observable at every cutoff is
$$
 \Psi_q(S)=\sum_i w_i\big[e^{-S/r_i}/L_i-1\big].
$$
The subtracted constant centers the tangent reading. Use the actual vacuum mean for a connected Wilson correlation. Since $S\ge0$, each fixed-$q$ reading is bounded uniformly in $\beta$ and volume. Lagrange interpolation at the $m$ distinct poles gives $P(z)/D(z)=\sum_i w_i/(z+r_i)$, denoted by $R(z)$.

A Gaussian shift makes all the cancellations explicit. Multiply the normalized exponential by $\exp(t\cdot Z-|t|^2/2)$ and integrate in the independent normal blocks. Completing squares gives
$$
 \mathbb E\left[\frac{e^{-S^G/r_i}}{L_i}\,e^{t\cdot Z-|t|^2/2}\right]
   =\exp\left[-\frac12\sum_\lambda\frac{\lambda |t_\lambda|^2}{r_i+\lambda}\right].
$$
Its Taylor coefficients are the Hermite coefficients. In the combination, a term with $k_\lambda$ contractions in each block is proportional to $\sum_i w_i\prod_\lambda(r_i+\lambda)^{-k_\lambda}$. For a pure block and power $j\ge1$, this sum is $(-1)^{j-1}R^{(j-1)}(\lambda)/(j-1)!$. For a mixed term, partial fractions in $r_i$ reduce it to pure powers no higher than the corresponding $k_\lambda$. All degrees $2,4,\ldots,2q-2$ therefore vanish, as do the mixed terms of degree $2q$. The pure $b$ coefficient at degree $2q$ survives because $R$ has a zero of exactly order $q-1$ there (for $q=1$, its value there is nonzero). These statements about a local observable also hold in the surrounding Gaussian field, by conditioning the Gaussian generating function on its local coordinates.

Conversely, cancellation through degree $2q-2$ forces all pure-block conditions, hence the three zeros of multiplicity $q-1$. A linear combination of $m$ distinct poles has numerator degree at most $m-1$. A nonzero reading requires $m\ge3(q-1)+1$. An arbitrary additive constant affects only degree zero. This minimality is for this Laplace-source family.

## Positive times and the first quartic channel

At the same spatial point, write $u_n,v_n$ for the one-color cross eigenvalues of the pair-sum contrasts and pair differences, $n\ge1$. The uniform component has zero cross covariance at every positive step. The [electric integral](time-kernel.md) gives $u_n\sim-3/(\pi^2 n^6)$ and $v_n\sim-2/(\pi^2 n^4)$, with both strictly negative for every $n\ge1$.

Let $M_{ij}=\sum_k w_k/(r_k+a)^i(r_k+b)^j$. The fixed-step limiting connected autocorrelation is
$$
 C_q(n)=\sum_{i+j>0}\frac{(3)_i(9/2)_j}{i!j!}\,u_n^{2i}v_n^{2j} M_{ij}^2,
$$
where $(x)_i$ is the rising factorial. Indeed the cross moment of two normalized exponentials is the product of $(1-u_n^2/[(r_k+a)(r_l+a)])^{-3}$ and $(1-v_n^2/[(r_k+b)(r_l+b)])^{-9/2}$. This follows from the two-by-two joint Gaussian determinant for each pair of coordinates. Its binomial series is absolutely convergent because the cross eigenvalues are bounded by the equal-time variances and the poles are strictly positive. Summing over sources gives the squares above. The pure $j=q$ term is strictly positive.

Set $M=M_{0q}$. Then
$$
 n^{8q} C_q(n)\longrightarrow
 K_q=\frac{(9/2)_q}{q!}\left(\frac4{\pi^4}\right)^q M^2,
 \qquad
 |M|=\frac{|(b-1)(b-a)|^{q-1}}{D(b)} .
$$
Higher total orders are $O((|u_n|+|v_n|)^{2(q+1)})$ by analyticity on a fixed neighborhood of zero. For $q=2$, $K_2=198R'(b)^2/\pi^8$.

At a strictly positive step only two local variances propagate. Repeating the construction with $E=\{a,b\}$ and $2(q-1)+1$ poles removes all propagating terms of total order less than $q$, while the equal-time observable can retain degree two on the uniform component. Conversely the terms in the displayed series are nonnegative and $u_n,v_n$ are nonzero. Suppressing every lower order (equivalently its coefficients after a common auxiliary rescaling of the cross covariance) forces the two sets of pure zeros. The same degree count proves optimality. The [time-kernel note](time-kernel.md) distinguishes this order requirement from asking only for a given time exponent and quantifies leakage under imperfect cancellation.
