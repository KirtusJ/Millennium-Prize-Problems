# Recovering the first spectral moment from three positive-time readings

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For a positive spectral law $\nu$ on $[0,\infty)$, let $F(u)=e^{-u}(1-e^{-u})^2$ and $D(t)=\int F(tE)\,d\nu(E)$. When the individual correlations exist this is $C(t)-2C(2t)+C(3t)$. Direct integration of $F$ also defines the reading when those individual terms are infinite. The readings give the exact first moment:
$$
\int_0^\infty D(t)\,\frac{dt}{t^2}
=c\int_{(0,\infty)}E\,d\nu(E),\qquad
c=3\log 3-4\log 2=0.523248143764\ldots
$$
The identity holds in the extended nonnegative reals, including infinite first moment, for a σ-finite law. The local Lean theorem accepts the more general s-finite hypothesis. An atom at zero contributes zero. For finite first moment, dense positive-time data also determine the entire spectral law on the open energy axis. Recovery from approximate data can be ill-conditioned. [Uniqueness, stability and controls](inversion.md) · [Formal proof and measured guest runs](execution.md)

## Where the constant comes from

For $u>0$, the fundamental theorem of calculus twice gives
$$
F(u)/u^2=\int_0^1\!\int_0^1 e^{-(1+r+s)u}\,dr\,ds .
$$
For one energy $E>0$, integrate $E^2$ times the right side at $u=tE$ over time. The time integral is $E/(1+r+s)$. Integrating over the square gives $E c$. At $E=0$ both sides vanish. Tonelli now gives the stated equality without subtracting infinite Laplace integrals. For pointwise limits of the readings, Fatou gives the first-moment lower semicontinuity inequality, including when some of the weight leaves every finite energy interval.

## Interpreting the physical cutoff limit

For a fixed spatial test at the $b^2$ normalization, let $\eta_b(dE)=E\nu_b(dE)$. The SU(2) Hamiltonian estimate gives $\eta_b((0,\infty))=\rho_b\int|\nabla\varphi|^2+O_\varphi(b)$. Its uniform bound allows extraction on the compactified energy axis $[0,\infty]$. Write any subsequential weak limit as $\alpha_0\delta_0+\eta+\alpha_\infty\delta_\infty$ with $\eta$ on the open axis. The normalized reading measure $D_b(t)dt/(ct^2)$ then converges on compactified time to
$$
\alpha_\infty\delta_0 + \frac{D(t)}{ct^2}\,dt + \alpha_0\delta_\infty,
\qquad D(t)=\int_{(0,\infty)} F(tE)\,\eta(dE)/E .
$$
To see this, let $U$ have probability density $F(u)/(cu^2)$ on $(0,\infty)$. For any continuous test $f$ on compactified time, a unit of first-moment weight at energy $E$ contributes $\mathbb E[f(U/E)]$. This is continuous in $E$, including its endpoint values $f(\infty)$ at zero energy and $f(0)$ at infinite energy. This proves the weak convergence and identifies both endpoint masses. A genuine zero-energy atom of the original law is still invisible. The mass at compactified energy zero here means **positive first moment escaping to low energies**.

Thus when $\rho_b\to\rho$, a deficit between $\rho\int|\nabla\varphi|^2$ and the recovered interior first moment has a specific split on every such subsequence. All-time readings after taking the cutoff limit determine the interior. Separating the two escaped pieces also requires the cutoff data near zero and infinite time, or independent estimates there. At this normalization the earlier stress-tensor obstruction still applies. The identity by itself supplies neither a nonzero limiting vector nor a four-dimensional gap. [Spatial first-moment estimate](../spatial-limit.md) · [Lorentz test](../lorentz-test/) · [D4’s finite readings](../../../spectral-support/finite-readings/)

## A finite Wilson time grid with an absolute error budget

Fix $0<a<b_t$ in physical time. Let $t_j=a e^{jh}$, $0\le j<N$, with $b_t=a e^{Nh}$. Divide the sum rule by $c$. The left-endpoint approximation to its contribution on $[a,b_t]$ is
$$
S_N=\frac h c\sum_{j=0}^{N-1}\frac{D(t_j)}{t_j}.
$$
If $M_1=\int d\eta$ is finite, the absolute quadrature error is at most $(2h/e)M_1$, uniformly over the energy scales of the input. Indeed $g(u)=F(u)/u$ is the square average of $u e^{-(1+r+s)u}$. Its total variation is at most $2c/e$, since each such function rises to $1/[e(1+r+s)]$ and falls to zero. For one energy the integrand in log time is $g(Ee^y)$. The rectangle error on each cell is at most $h$ times its variation there. Summing over cells and integrating the first-moment weights gives the bound.

If individual measured **triples** have certified absolute errors $\epsilon_j$, add $(h/c)\sum_j\epsilon_j/t_j$. If errors are stated per correlation, combine them first with absolute coefficients $1,2,1$. For an energy band $[l,R]$ with $l>0$, the missed fraction of its first moment outside the window is at most
$$
\min\left(1,\frac{aR+e^{-b_t l}/(b_t l)^2}{c}\right).
$$
The unit-energy kernel is bounded by one near zero and by $e^{-u}/u^2$ at large $u$. This gives both tails after rescaling. A known upper bound on the first moment outside the band can simply be added. Without that information the finite sum still gives a lower certificate after subtracting the grid and measurement errors. A two-sided estimate needs control of the omitted times.

For B4’s Wilson implementation choose $a$ dyadic and $e^h=1+2^{-k}$ for a positive integer $k$. Every time in this finite grid is exactly dyadic, so one sufficiently fine dyadic Wilson spacing realizes each $t_j,2t_j,3t_j$ without independent rounding. The time, period and Haar quadrature searches in B4’s construction can impose the prescribed triple tolerances simultaneously. Only fixed finite grids are used at each cutoff stage. Their size and the costs of the searches can grow. A positive lower certificate for actual continuum data still requires the measured values and continuum matching. [Wilson readings and errors](../../../transfer-operator/periodic-time/measurements.md)
