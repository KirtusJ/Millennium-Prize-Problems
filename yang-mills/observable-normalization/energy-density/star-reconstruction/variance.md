# Large-star asymptotics and the cost of retaining only ordinary plaquette traces

For the inverse in the [main result](README.md), $h(0)=0$ and
$$
 h(x)=\frac32-\frac{3}{4|x|}+O(|x|^{-3}).
$$
In particular it is bounded uniformly on the entire real line. This is a property of the inverse for this target. A general prescribed conditional mean can have a large or unbounded inverse.

Write $B(s)=Z(s)V(s)$, so $A''(s^2)=3B'(s)/(4s)+B''(s)/4$ for $s>0$. For fixed order the positive-real-axis expansions of $I_\nu(s)$, together with $I_\nu'=(I_{\nu-1}+I_{\nu+1})/2$, give $A''(s^2)=e^ss^{-3/2}$ times an asymptotic series in integer inverse powers, bounded after factoring this leading behavior for $s\ge1$. Indeed $Z$ has leading order $e^ss^{-3/2}$, and log derivatives may be computed as rational functions of the fixed-order Bessel functions before expanding to sufficiently high order to account for cancellations. Near zero $A''$ is bounded. [NIST DLMF, §10.40](https://dlmf.nist.gov/10.40)

In the inverse integral change $u=s^2$ and then $s=x-y$ for $x>0$. The factor multiplying $A''(s^2)$ is $2xs/(\cosh x\sqrt{y(2x-y)})$. The part $s<x/2$ is exponentially small up to a polynomial in $x$. On $0\le y\le x/2$ the rescaled integrand has a termwise expansion with weight $e^{-y}y^{-1/2}$; Taylor remainders for powers of $1-y/x$ and $1-y/(2x)$ are bounded by a polynomial in $y$ times the next inverse power of $x$, since the denominators there are bounded away from zero. This yields $h(x)=c_0+c_1/x+c_2/x^2+O(x^{-3})$, in particular boundedness. It is simpler to determine the coefficients from the exact forward equation.

Conditionally let $D=R-X$. Its law is the decreasing square-root tilt of a unit-rate gamma variable of shape $3/2$; it is stochastically dominated by that gamma. Its first moment is $3/2+O(R^{-1})$, by expanding the known tilt, and all its moments are bounded. On $D\le R/2$ expand $h(R-D)$ about $R$ and use the bounded moments for the remainder. The complement has exponentially small probability. Thus the coefficients of $\mathbb E_R h(X)$ are $c_0,c_1,c_2+3c_1/2$ through order two. The [direct polar calculation](../staple-response/) gives $3/2,-3/4,-9/8$ for $V$. Hence $c_2=0$.

## Variance on Wilson histories

In the infinite-time isotropic Wilson vacuum on periodic spatial tori put $S=6\beta-X=\sum_{p\ni e}Y_p$, $\delta=6\beta-R=S-D$. The [single-face exponential moment estimate](../../../central-quotients/tangent-curvature/moments.md) bounds every moment of $S$ and gives exponentially small probability of $S>3\beta$. On its complement $X\ge3\beta$. Expanding the reciprocal with its exact remainder gives
$$
 \beta^2[h(X)-3/2+1/(8\beta)]=-S/48+O_{L^p}(\beta^{-1})
$$
for every fixed finite $p\ge1$, uniformly at large $\beta$ across the spatial tori in the moment estimate. The good-event error is at most $C(1+S^2)/\beta$; on the tail use boundedness of $h$, $0\le S\le12\beta$ and exponential probability. Similarly, the prior one-link calculation gives
$$
 \beta^2[V(R)-3/2+1/(8\beta)]=-\delta/48-1/32+O_{L^2}(\beta^{-1}).
$$
Subtract these relations. Since $D$ converges in moments to $\mathrm{Gamma}(3/2,1)$ as $R\to\infty$ and $R\to\infty$ in probability, the mean conditional noise satisfies
$$
 \lim_{\beta,L\to\infty}\beta^4\mathbb E[(h(X)-V(R))^2]
 =\frac{\mathbb E(G-3/2)^2}{48^2}=\frac1{1536}.
$$
In comparison, $W^2$ has conditional mean $V(R)$ and $\mathbb E[(W^2-V(R))^2]\to27/2$, by the centered fourth gamma moment and convergence of $V(R)$ to $3/2$. Both readings retain exactly the same separated response at every cutoff.

## Equal-time normalization

Let $K(0)$ be the six-by-six single-color covariance of the six signed electric faces at one temporal link in the [rooted Gaussian limit](../../../central-quotients/tangent-curvature/). Then $S$ tends with all moments to one half the sum of squares of the six face vectors in three colors. Wick contraction gives
$$
 \lim\beta^4\operatorname{Var}(h(X))=\frac{\|K(0)\|_F^2}{1536},\qquad
 \lim\beta^4\operatorname{Var}(V(R))=\frac{\|K(0)\|_F^2-1}{1536}.
$$
The second relation also follows by orthogonal decomposition of the conditional prediction error.

The trace of $K(0)$ is three because each face has one-color variance $1/2$. In signed-face coordinates the uniform unit vector is an eigenvector of eigenvalue one: the incidence pattern of the six faces is the curl of a cochain supported on the common link, and the tangent covariance is the orthogonal projection onto exact two-forms. Split each opposite pair into its normalized sum and difference. Reflection in its transverse coordinate exchanges members of that pair while preserving the others, so different antisymmetric-pair modes are orthogonal to one another and to all pair sums. Cubic symmetry makes the three antisymmetric eigenvalues equal. For the pair sums the [oriented contact calculation](../contact-law/) gives eigenvalue $d/2$ on the two directions of zero total sum, accounting for the $1/\sqrt2$ pair normalization. The trace fixes the remaining triple eigenvalue $(2-d)/3$. Consequently
$$
 N=\|K(0)\|_F^2=1+d^2/2+(2-d)^2/3\simeq1.807266 .
$$
For the optimized ordinary-trace reading the irreducible conditional noise is about $55.33\%$ of the limiting equal-time variance. At fixed $n\ge1$, its variance-normalized separated reading tends to $\|K(n)\|_F^2/N>0$ in the conventions of the [temporal kernel](../staple-response/positive-time.md). For $W^2$ the same covariance divided by its own raw variance tends to zero. Even for the optimized reading the variance-normalized correlation at a fixed **physical** time tends to zero as $b\to0$ along arbitrary joint weak trajectories, by the fixed-step upper bound and monotonicity. The previously identified $t^{-8}$ law uses a further normalization on selected trajectories. An interacting continuum construction at a common nonzero physical scale remains open.
