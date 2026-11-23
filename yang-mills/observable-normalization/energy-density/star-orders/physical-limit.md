# An explicit joint trajectory for each bounded reading

Use the isotropic four-dimensional SU(2) Wilson vacuum on periodic spatial tori of side $L$ in cells. Take infinite temporal extent at each fixed regulator. Write $r$ for inverse physical spacing, distinct from the fixed source radii $r_i$. For fixed $q$ and the full-rank filter in the [main note](README.md), if
$$
 r\to\infty,\qquad L/(r^{12q}\sqrt{\log(2+r)})\to\infty,\qquad
 \beta/(r^{64q}\log(2+r))\to\infty ,
$$
then for every $t>0$,
$$
 r^{8q}\operatorname{Cov}_{\beta,L}(\Psi_q(S_0),\Psi_q(S_{\lfloor rt\rfloor}))
          \longrightarrow K_q t^{-8q}.
$$
For $q=2$, $L=\lceil r^{25}\rceil$, $\beta=r^{129}$ is one example. A common choice growing faster than every power for both $L$ and $\beta$ works for every fixed $q$. Constants need not be uniform in $q$.

## Comparing bounded exponential tests

Moment convergence at each fixed degree alone does not provide a rate for a bounded nonlinear function on growing patches. Instead the Gaussian Fourier identity linearizes each Laplace reading. For any finite list of scaled rooted face curvatures $F_j=\sqrt\beta\operatorname{Im} U_j$ and nonnegative fixed strengths $s_j$, the physical and quadratic exponents differ by
$$
 0\le \sum_j s_jY_j-\tfrac12\sum_j s_j |F_j|^2
      =\frac1{2\beta}\sum_j s_jY_j^2.
$$
This is an exact SU(2) identity. The map $x\mapsto e^{-x}$ is 1-Lipschitz on $x\ge0$. C4’s uniform action moments therefore give an $O(\beta^{-1})$ error in the mean of the exponential. Using separate strengths on two stars covers the joint mean as well. The squared norms do not depend on how the faces were transported.

Let $Z_j$ be independent standard three-dimensional Gaussian auxiliaries. For fixed curvatures, $\exp[-\sum s_j |F_j|^2/2]=\mathbb E_Z\exp(i\sum\sqrt{s_j}Z_j\cdot F_j)$. A draw of the auxiliaries gives a test cochain $g$ on a bounded number of faces within a patch of radius $O(r)$. Put $T=\sum_j\sqrt{s_j}|Z_j|$ so all its coefficient norms are at most $T$, even with repeated coordinates. To control the characteristic function choose an integer $h\ge r$ and use D4’s truncated Green kernel to write $g=dA+d^*B+w$ in a patch of radius $O(h)$. Its bounds, with homogeneity restored, are $\|A\|_1+\|B\|_1\le ChT$, $\|w\|_2\le Ch^{-2}T$ and $\|F(w)\|_{L^2}\le Ch^{-2}T$. The last estimate is in the Wilson law, using C4’s uniform bound for arbitrary bounded space-time weights at physical scale $h$, under $L/(h^3\sqrt{\log(2+h)})\to\infty$ and $\beta/(h^{16}\log(2+h))\to\infty$. The supported patch embeds in the torus.

In the rooted Haar identity for $e^{itF(g)}$, $0\le t\le1$, use $\mathbb E|F(w)|$ for the residual. The score term costs at most $C\|A\|_1[h(1+\|g\|_\infty)+\|g\|_1]/\sqrt\beta$, and the Bianchi term costs $Ch\|B\|_1/\sqrt\beta$. The exact-cochain Gaussian variance is $\|Pg\|_2^2$ and replacing $\langle g,dA\rangle$ by this variance costs at most $\|Pg\|_2\|w\|_2$. Integrating the scalar characteristic-function differential equation on $[0,1]$ has attenuation at most one. Together these give the absolute comparison error
$$
 C(T+T^2)(h^{-2}+h^2/\sqrt\beta).
$$
The Gaussian auxiliary has finite first and second moments of $T$. Fubini and absolute integration now compare the bounded Wilson exponential and its exact lattice Gaussian counterpart with error $O(h^{-2}+h^2/\sqrt\beta+\beta^{-1})$. Products of means in a covariance have the same absolute error since all of the original exponentials lie in $[0,1]$. A fixed finite source combination multiplies the constants by finite factors depending on the chosen probe. [C4’s rooted Ward identity](../../../central-quotients/magnetic-smearing/ward.md) · [C4’s uniform spacetime test estimate](../../../central-quotients/magnetic-smearing/field.md) · [D4’s compact Green decomposition](../../../spectral-support/electric-slab/local-moments.md)

Choose $h=\lceil r^{4q}\ell_r\rceil$, where $\ell_r\to\infty$ sufficiently slowly. For example take the minimum of $\log(2+r)$, the sixth root of $L/(r^{12q}\sqrt{\log(2+r)})$, and the thirty-second root of $\beta/(r^{64q}\log(2+r))$, for large $r$. This satisfies the two patch conditions and makes the absolute error $o(r^{-8q})$. The limiting time-power formula follows from the infinite-lattice Gaussian calculation since $\lfloor rt\rfloor/r\to t$. The comparison error is uniform for time displacements between one and any fixed multiple of $r$. On a logarithmic bare trajectory the same use of the theorem applies to sufficiently slowly growing lattice lags and does not reach fixed positive physical time.

## Positive energy measurements

Each ordinary trace sum is real, gauge invariant and invariant under reversing its slab. At fixed cutoff the bounded function of that sum defines a self-adjoint one-step insertion $B$ with the same half-spatial weights as the transfer. With $T$ the positive transfer normalized by its top eigenvalue, $v=(B-\langle\Omega,B\Omega\rangle)\Omega$, its connected time covariance is $\langle v,T^{n-1}v\rangle$ for $n\ge1$. This includes adjacent slabs. [Original slab argument](../staple-response/positive-time.md) · [D4’s adjacency audit](../../../spectral-support/electric-slab/adjacency.md)

At $n_0=\lfloor rt_0\rfloor$, $t_0>0$, tilt this spectral measure by $T^{n_0-1}$ and divide by the positive reading. The Laplace transform in physical energy at an increment $s\ge0$ tends to $(t_0/(t_0+s))^{8q}$ by the positive-time formula. Neighboring steps squeeze any rounding difference. The limit is the gamma law of shape $8q$ and rate $t_0$. This family illustrates an observable dependence of the power with which a gapless transfer spectrum is sampled. The scaled norm, the exponent, and the existence of a transfer gap are distinct quantities.

## The microscopic lower edge on every joint weak trajectory

There is also a statement without any relation between $L$ and $\beta$. The measures of the finite-box slab vectors on the compact transfer-value interval $[0,1]$ converge weakly as $L,\beta\to\infty$. Indeed their total mass and each integer moment of order $j$ converge to $C_q(j+1)$ by fixed-patch convergence and the adjacent-slab identity. Bounded masses and polynomial density on $[0,1]$ give existence and uniqueness of the limiting measure. Write $\mu_q$ for it in lattice energy $E=-\log x$, allowing $E=\infty$ at $x=0$. With $\alpha=8q$, its low-energy weight is
$$
   \mu_q([0,\eta])\sim K_q\,\eta^{\alpha}/\Gamma(\alpha+1)
   \qquad(\eta\downarrow0),
$$
where $\eta$ is an energy threshold. In particular each of these distinct orders still sees the same zero threshold.

For a direct derivation tilt the limiting measure by $\exp[-(m-1)E]/C_q(m)$ and consider the rescaled variable $y=mE$. At $s\ge0$ its Laplace transform tends to $(1+s)^{-\alpha}$ by the large-step formula and monotonic interpolation between integer steps. The limit is a unit-rate gamma variable. Integrating $e^{(1-1/m)y}\mathbf1_{[0,1]}(y)$ undoes the tilt on $[0,1/m]$. The test is bounded there, converges uniformly on the interval, and the limiting law has no atom at 1. Its limiting integral is $1/\Gamma(\alpha+1)$. Using $C_q(m)\sim K_qm^{-\alpha}$ and squeezing arbitrary positive thresholds between consecutive reciprocal integers proves the claim.
