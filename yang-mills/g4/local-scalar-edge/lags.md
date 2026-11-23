# From Fourier weight to a fixed plaquette

Keep the notation of the [momentum proof](momentum.md). The local measure is the **average**, over all $L^3$ momenta, of the measures of the $L^{-3/2}$-normalized modes. Its total is $O(1)$.

## Absolute spectral weight

For $0<r\le\kappa$, every mode with $|k|\le r$ puts weight at least $1/8$ in
$$[b_*-C\beta^6-C\beta^4r^2,\ b_*+C\beta^6].$$
A Euclidean ball of radius $r$ contains between constant multiples of $\max\{1,(Lr)^3\}$ grid points, by inscribed and circumscribed coordinate cubes (and inclusion of zero). Thus the local weight there is at least $c\max\{L^{-3},r^3\}$. Take $r=\beta$ and fix a sufficiently large $K$ to contain the entire displayed interval in $I=[b_*-K\beta^6,b_*+K\beta^6]$.

Conversely, (2) confines even the enlarged open interval $J=(b_*-2K\beta^6,b_*+2K\beta^6)$ to momenta with $|k|\le C_K\beta$. Each mode contributes at most its uniformly bounded total mass. Counting again gives $\mu_L(J)\le C_K\max\{L^{-3},\beta^3\}$. For fixed $\beta$ the local measures converge weakly by convergence of all fixed-lag local correlations on the common compact transfer interval. Portmanteau for the **closed** $I$ supplies the bulk lower bound. Portmanteau for the **open** $J\supset I$ supplies the upper bound. The full edge is itself within $O(\beta^6)$ of $b_*$ in $x$. Since $b_*$ tends to one, the logarithm converts these distances to $O(\beta^6)$ in lattice energy.

The upper bound on the **full bulk spectrum** uses a separate density argument. At fixed coupling every centered local reflected half-history vector has transfer moments converging from the tori, with support in the common closed interval $[0,t(b_*+C\beta^6)]$. Its bulk measure has the same support bound by weak convergence. These half-history vectors span a dense subspace of the reconstructed vacuum complement, so the spectral projection above that interval vanishes on the full complement. The local lower bound then locates the full bulk edge to the stated accuracy. [A4’s full-spectrum passage](../../observable-normalization/uniform-band/README.md) · [Half-history construction and density](../../transfer-operator/connected-rectangles/gap.md)

For one oriented face, the Fourier-mode total mass is also uniformly bounded by the common disk's spatial covariance sum for that local trace. Its support obeys the same full-spectrum upper bound (2). For the lower bound apply a spectral projection $P$ to the three centered local traces. Axis permutations about the base site send any one trace to another; orientation reversal leaves the $SU(2)$ trace invariant. Their projected norms are equal. Cauchy–Schwarz gives $\|P g_0\Omega\|^2\le3\|P f_{0,i}\Omega\|^2$. This proves the same two-sided order for any individual face. Taking $S^{j/2}$ in place of $P$ gives the corresponding lower lag comparison.

## Two-sided lag bounds

Let $s_\pm=t(b_*\pm C\beta^6)$, using a common $C$ large enough for the bounds above. Set $a=j\beta^4$ and $H_j=\max\{L^{-3},(1+a)^{-3/2}\}$. There are positive constants $c_1,c_2$ such that for either local observable
$$c_1 H_j s_-^j\le q_j\le c_2 H_j s_+^j. \tag{3}$$
For the lower bound choose $r=\kappa/\sqrt{1+a}$. On the selected branch the additional factor relative to $s_-^j$ is at least $(1-C'\beta^4r^2)^j\ge\exp(-2C'j\beta^4r^2)$, bounded below independently of lag. Reduce $\beta_0$ so $C'\beta^4r^2\le1/2$. For the upper bound, (2) bounds each mode's contribution by $C's_+^j\exp(-c'a|k|^2)$. For $a\ge1$ the normalized one-dimensional sum is at most $L^{-1}+C a^{-1/2}$ by comparison of a decreasing Gaussian with its integral. Cube this bound. For $a<1$ use the total mass bound. This proves (3) in every torus. Fixed-$j,\beta$ weak convergence gives (3) in the bulk with $H_j=(1+a)^{-3/2}$.

Write $\rho$ for the upper endpoint of the full centered transfer spectrum and $\Delta=-\log\rho$. The lower overlap and the full support bound give $s_-\le\rho\le s_+$ (in the bulk take $j$th roots in (3) for the lower bound). The ratio $q_{2j}/q_j$ is a weighted average of $\lambda^j$ and is at most $\rho^j$. Also $H_{2j}/H_j\ge2^{-3/2}$. Dividing the lower bound in (3) at $2j$ by its upper bound at $j$ gives $q_{2j}/q_j\ge c(s_-^2/s_+)^j$. Hence
$$0\le-j^{-1}\log(q_{2j}/q_j)-\Delta
\le 2\log(s_+/s_-)+C'/j=O(\beta^6+j^{-1}).$$
All these comparisons use infinite-time connected correlations. Periodic thermal histories have a different spectral representation.

## Joint strong-coupling and long-lag limit

For $g_0$, let $\beta\downarrow0$ with $a=j\beta^4\to\infty$ and $j\beta^6\to0$. Divide each mode's lag contribution by $(tb_*)^j$. On bounded sets of $p=\sqrt a\,k$, the simple-top weight tends uniformly to one. Its eigenvalue power tends uniformly to $\exp(-D|p|^2)$ for $D=7/768$. Indeed the logarithm uses $b_*\to1$, $j\beta^4|k|^4=O(|p|^4/a)$, $j\beta^6=o(1)$, and the square of the relative shift times $j$ tends to zero there. The remaining upper branches near zero contribute $O(\exp(-c a))$ and the low cluster contributes at most $C(C'\beta^2)^j$. Across the zone the normalized contribution is bounded by $C'\exp(-c'|p|^2)$ by (2). This proof uses the absolute scalar weight for the leading coefficient.

* If $L/\sqrt a\to\infty$, the mesh $h=2\pi\sqrt a/L$ in $p$ tends to zero. After multiplication by $a^{3/2}$ the sum has element $h^3/(2\pi)^3$. On compact sets use uniform convergence; outside, the Gaussian grid tails tend to zero uniformly as the compact sets grow (bound each grid cube by an integrable wider Gaussian once $h\le1$). The limit is $(2\pi)^{-3}\int_{\mathbb R^3}e^{-D|p|^2}\,dp=(4\pi D)^{-3/2}$. For infinite space, at each fixed $(\beta,j)$ approximate its local correlation by a torus large enough to make the rescaled error arbitrarily small and $L/\sqrt a$ arbitrarily large.
* If $L/\sqrt a\to\ell\in(0,\infty)$, after multiplication by $L^3$ the normalized correlation tends to $\sum_{n\in\mathbb Z^3}\exp(-4\pi^2 D|n|^2/\ell^2)$. Here $h$ stays bounded below, the representatives exhaust the integer grid, and the envelope is summable in $n$.
* If $L/\sqrt a\to0$, the same $L^3$ normalization gives limit one. The nonzero grid points have total Gaussian bound tending to zero; the zero mode has limiting weight one. This includes a fixed allowed box.

The conditions on $j$ keep the accumulated sixth-order dispersion uncertainty small while resolving momentum curvature. They differ from the $j$ of order $\beta^{-6}$ used for the **error bound** on a mass estimate. The explicit Gaussian asymptotic is for the sum of the three faces. It describes propagation in the strong-coupling regulator at fixed mesh.
