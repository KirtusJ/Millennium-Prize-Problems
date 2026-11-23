# Positive transport of a time curve and its finite-data error

Let $C(t)=\int f_s(U,t)\,d\mu(s)$, where $\mu$ is any positive measure on $s\ge0$, $U>0$, and $C(t)$ is finite at every positive time. For each measured momentum in the mixing problem, freeze its own positive measure $\mu=U^2 A+2U X+B$. Only its dispersion will change.

## Exact identity

For $0\le a<U$ the operator $P_a$ in the [main note](README.md) obeys
$$
 (P_a C)(t)=\int f_s(U-a,t)\,d\mu(s).
$$
One proof uses a positive integral in an auxiliary variable $z$,
$$
 f_s(U,t)=\frac{1}{2\sqrt{\pi}}\int_0^\infty z^{-1/2}
        e^{-(s+U)z-t^2/(4z)}\,dz .
$$
For $s+U>0$ this is the Gaussian integral, or follows by integrating the Poisson semigroup subordination formula in time from $t$ to infinity and dividing by two. The time operator $K$ sends $e^{-t^2/(4z)}$ to $z e^{-t^2/(4z)}$. Tonelli applies at every iteration. Summing the exponential series therefore inserts $e^{az}$ into the integral and lowers $U$ by $a$. The identity holds for an infinite spectral measure with finite positive-time readings. [Poisson subordination formula, Eq. (1.1)](https://webs.um.es/gustavo.garrigos/papers/garrigos_antequera_proc_june2015.pdf)

Direct differentiation gives $\partial_U\partial_t f_s=tf_s/2$. On compact subsets of $U,t>0$, derivatives can be dominated by a constant times a positive shell at a smaller positive time, including at $s=0$. This proves the rectangle identity for a positive mixture with fixed coefficients. When the measured operator itself has $U$-dependent coefficients, first remove the known prefactor or transport the entire positive curve with its coefficients frozen.

## A finite positive-time interval from bounded readings

Choose $t=x_0<\cdots<x_m=X$, a truncation order $N$, and confidence or deterministic input intervals $L_j\le C(x_j)\le H_j$ valid jointly. Set $d_j=(x_j^2-t^2)/4$. The exact nonnegative weights are
$$
 w_j=\sum_{n=1}^{N}\frac{a^n}{(n!)^2}(d_j^n-d_{j-1}^n).
$$
Indeed for $n\ge1$ changing integration order gives
$$
 (K^n C)(t)=\int_t^\infty \frac{x}{2(n-1)!}
              \left(\frac{x^2-t^2}{4}\right)^{n-1} C(x)\,dx .
$$
Integrate the polynomial on each time cell and use monotonicity of $C$. An interval containing the ideal shifted reading is
$$
 \left[L_0+\sum_{j=1}^m w_j L_j,\quad
       H_0+\sum_{j=1}^m w_j H_{j-1}+R_N+R_X\right].
$$
For $0<a<U$ choose $a<r<U$ and put $p=\sqrt U$, $m_r=\sqrt{U-r}$ and $\delta=p-\sqrt a$. The remainders admit bounds using just the first upper reading,
$$
 R_N=(a/r)^{N+1}\frac{p}{m_r}e^{t(p-m_r)}H_0,\qquad
 R_X=\frac{a H_0}{2}e^{tp-X\delta}
              \left(\frac{X}{\delta}+\frac1{\delta^2}\right).
$$
At $a=0$ return the initial interval. Positivity bounds the tail of the series at $a$ by $(a/r)^{N+1}P_r C$. On each shell $E=\sqrt{s+U}$, both $E/\sqrt{E^2-r}$ and $E-\sqrt{E^2-r}$ are maximal at $E=p$. This gives the bound for $R_N$. For $R_X$, the entire positive integral kernel is bounded by $(ax/2)e^{\sqrt a\,x}$. To see this, expand the kernel as $(ax/2)\sum_{k\ge0}(a(x^2-t^2)/4)^k/[k!(k+1)!]$ and dominate the series by $e^{2\sqrt{a(x^2-t^2)/4}}$. Also $C(x)\le C(t)e^{-p(x-t)}$. Integration above $X$ gives the displayed bound. Double counting a positive remainder only increases the upper endpoint.

For exact numerical integration one may use the same kernel as $ax I_1(v)/v$, where $v=\sqrt{a(x^2-t^2)}$ and the ratio at zero is $1/2$. The finite-data enclosure above uses only positive weights, including for inputs whose underlying tensor–scalar cross measure is signed. If the three shifted values each have absolute error at most $\eta$, the error of the recovered tensor coefficient is at most $2\eta/h^2$. Errors in the other coefficients follow by interval arithmetic in the stated linear combinations. Small momentum spacing can magnify noise substantially.

These are bounds for the target covariant curves. A lattice transfer curve with spectral weight below its proposed relativistic momentum threshold requires a separate cutoff-to-target comparison. In particular the tail estimate cannot be imposed on a regulator solely from spatial translation invariance.
