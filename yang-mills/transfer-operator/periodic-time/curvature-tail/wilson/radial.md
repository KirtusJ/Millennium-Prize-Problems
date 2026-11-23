# Total variation of a Gaussian radius and the order of limits

Let $k=3$ and $H,Z$ be independent $N(0,I_k)$. Write $\rho=\sqrt u$, $W=\rho H+\sqrt{1-\rho^2}Z$ and $X=|W|^2$. Both $X$ and $|H|^2$ have law $\chi_k^2$. Since the conditional radius law depends on $H$ only through $|H|$, $A(u)$ is the total variation distance of $(H,X)$ from its product law. In dimension three its likelihood ratio at $h=|H|^2$, $x=X$ is
$$
 (1-u)^{-3/2}\exp[-u(h+x)/(2(1-u))]
 \frac{\sinh(\sqrt{uhx}/(1-u))}{\sqrt{uhx}/(1-u)} .
$$
Indeed conditionally on its radius, a standard three-dimensional Gaussian has uniform direction, whose cosine with any fixed axis is uniform on $[-1,1]$. This also shows $A(u)>0$ when $u>0$, since the conditional mean of $X$ depends on $h$.

For the first-order coefficient, expand the Gaussian joint density of $(H,W)$ with correlation $\rho$ in each corresponding coordinate. Relative to the independent density its linear coefficient is $H\cdot W$, and the coefficient of $\rho^2$ is
$$
 \tfrac12\big[k-|H|^2-|W|^2+(H\cdot W)^2\big].
$$
Averaging over the direction of $W$ at fixed $X=x$ replaces $(H\cdot W)^2$ by $|H|^2 x/k$. The radial law is even in $\rho$, so its first and third derivatives vanish at zero. The Taylor error after the quadratic term is $O(\rho^4)$ in the $L^1$ norm of signed densities: for $|\rho|\le1/2$, the covariance eigenvalues belong to $[1/2,3/2]$, and each of the first four derivatives of the joint density is bounded by a fixed integrable polynomial times a Gaussian in $(H,W)$. Pushing forward to $(H,X)$ is a contraction of that norm. The signed leading term relative to the product law is $u(|H|^2-k)(x-k)/(2k)$. Taking half its absolute integral gives
$$
 A(u)=c_k u+O(u^2),\qquad
 c_k=\frac{(\mathbb E|\chi_k^2-k|)^2}{4k}>0.
$$
For $k=3$, $c_3=18 e^{-3}/\pi$ by integration of the chi-square density. This coefficient uses the action (a squared radius). A colored Gaussian component in a particular frame retains its linear correlation, which the conjugacy-class measurement integrates out.

## Uniform statement across radii

The exterior sigma fields decrease with the radius. Conditional Jensen for the absolute measure norm gives $A_{\beta,\mu}(R')\le A_{\beta,\mu}(R)$ for $R'\ge R$; equivalently, discard links from both the joint and product laws. The conditional-expectation projection gives the same inequality for $D_{\beta,\mu}$. Their pointwise limits $A(u_R)$ and $3v_R^2/2$ are therefore decreasing and tend to zero, since $v_R\asymp R^{-4}$ by the finite-box projection estimate. Fix $\epsilon>0$ and choose $M$ with both limits at $M$ below $\epsilon$. Fixed-radius convergence is uniform in the state at the finitely many integers up to $M$. Beyond $M$ each of the four nonnegative quantities is bounded by its own value at $M$. This proves convergence in absolute error uniformly in every integer radius, and convergence to zero along any diverging radii. [Sharp exterior estimate](../exterior.md)

For each $R$, both limiting numbers are strictly positive. There also exists an unspecified integer $L(\beta)\to\infty$ for which relative convergence holds uniformly for $1\le R\le L(\beta)$. To see this, for each integer $j$ choose an increasing coupling threshold beyond which the relative errors on $1,\ldots,j$ are at most $1/j$. Take $L(\beta)$ to be the largest qualifying $j$, requiring the thresholds also to grow at least as fast as $j$. This yields no prescribed power or logarithmic scale. Absolute convergence alone cannot give a relative asymptotic at the inverse lattice gap.

In particular, for the original Wilson measures and every square-integrable exterior observable $B$,
$$
 |\operatorname{Cov}_\mu(Y,B)|\le\sqrt{D_{\beta,\mu}(R)\operatorname{Var}_\mu B}.
$$
Taking the supremum over all such exterior observables of unit variance gives equality when the predictor has positive variance. Thus even the optimal exterior reading of unit variance loses its covariance with the unnormalized central action along every diverging-radius weak-coupling sequence. The total variation statement also treats bounded tests that change with the coupling or with the observed exterior data. It gives no ratio between correlations measured at two different diverging times. [Program condition (C)](../../../../z4/attempt/A1_REDUCTION.md)
