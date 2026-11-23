# Gauge-invariant electric probes on the spatial mesh clock

The central sign produces a nonzero charge law on the magnetic clock and loses its connected signal at positive physical time. There is a different family on the same link with a nonzero *absolute* signal on the longer spatial mesh clock. Fix $SU(2)$, its defining Wilson action and the [shell conventions](shells.md). Let $A_\theta$ be left translation of one link averaged over the conjugacy class at angle $\theta$ with its invariant probability measure. This is a self-adjoint contraction commuting with all site gauge transformations. On electric shell $n$ its eigenvalue is
$$m_n(\theta)=\frac{\sin((n+1)\theta)}{(n+1)\sin\theta}.$$
This follows by averaging each representation matrix under conjugation and taking its trace. At $0$ the multiplier is one; at $\pi$ it is $(-1)^n$.

## Resolving the electric scale

For any fixed $s>0$ choose $\theta=sh$, $h=g^{-1/4}$. On shell $n$ the multiplier is $\operatorname{sinc}(s(n+1)h)/\operatorname{sinc}(sh)$ with $\operatorname{sinc}(u)=\sin u/u$ continued at zero. Along every compactness subsequence the covariance matrix for a finite collection of these probes converges to the covariance matrix of $\operatorname{sinc}(s y)$ under $f(y)^2dy$. Indeed these finite products are bounded, converge uniformly on compact sets of $hn$, and the shell laws are tight.

For distinct positive $s_1,\ldots,s_m$ this limiting covariance is strictly positive definite. If its quadratic form vanished, a linear combination of the sinc functions would be constant on a set of positive Lebesgue measure. Analyticity extends the identity to the half-line. Decay at infinity makes the constant zero. The first $m$ even Taylor coefficients then give an invertible Vandermonde matrix in the distinct $s_i^2$. This also applies to complex coefficients. A contradiction subsequence with unit coefficient vectors and a converging subsubsequence now gives constants $v>0$, $g_0<\infty$ depending only on the chosen angles $s_i$. On **every** box with $g\ge g_0$, the equal-time centered Gram matrix is at least $vI$. This is an existence bound; it does not specify an optimal $v$.

## What survives in time?

Write $T_k$ for left translation by a single fixed class member on the marked link, before averaging. It commutes with all kinetic terms. There are four incident faces. For each face an insertion in its holonomy can be cycled to an end using invariance of the trace, with $k$ or $k^{-1}$ and a conjugate of the original holonomy. Averaging over the conjugacy class replaces either inserted matrix by $(\cos\theta)I$. Thus
$$\int\langle T_k\Omega,Q T_k\Omega\rangle\,dk
=4\lambda(1-\cos\theta)(1-u),\qquad u=\langle 1-x_p\rangle.$$
The left side uses the full-space Hamiltonian; the gauge-invariant average vector belongs to its physical subspace. Convexity of the positive form bounds $\|Q^{1/2} A_\theta\Omega\|^2$ by this integral. Centering does not change it. For a unit coefficient vector $c$ and $\psi_c=\sum c_i(A_{s_i h}-\langle A_{s_i h}\rangle)\Omega$, Cauchy–Schwarz and $1-\cos\theta\le\theta^2/2$ give
$$\langle\psi_c,Q\psi_c\rangle\le2\lambda h^2\sum_i s_i^2.$$
Here $u\ge0$. Under the matched coefficients $\kappa=2/(\beta b)$ and $\lambda=\beta/b$, $\lambda h^2=\sqrt2/b$. Put $M=2\sqrt2\sum_i s_i^2$. The measure of $bQ$ in $\psi_c$ has total weight at least $v$ and first moment at most $M$. It assigns at least $v/2$ to $(0,2M/v]$ because the finite-box vacuum is simple and the vector is centered. For each $\tau\ge0$, spectral Jensen consequently gives the matrix bound
$$\big(\langle\psi_i,e^{-\tau bQ}\psi_j\rangle\big)_{ij}\succeq
v e^{-\tau M/v} I.$$
The constants work simultaneously for all sufficiently large bare couplings and all allowed volumes. This uses a common positive physical time $\tau b$ across the probe family at each cutoff. As $b\downarrow0$ that time vanishes. A positive lower bound at a fixed nonzero physical separation, or a lower edge of the continuum excitation spectrum, would require further information. [Lean tangent and measure bound](ElectricScale.lean)

## Keeping a fixed interior angle instead

For a fixed $0<\theta<\pi$, $\operatorname{Var}_\Omega(A_\theta)\asymp_\theta h^2$. Here is a direct distinction between the two choices of probe. Write $b_t=a_{t-1}$ for $t\ge1$ and $b_0=0$, with $D=\sum_{t\ge1}(b_t-b_{t-1})^2\le2u=O(h^2)$. Discrete Hardy gives $\sum b_t^2/t^2\le 6D$: the matrix $1_{k\le t}/t$ sending increments to $b_t/t$ has weighted row and column sums at most two and three against $t^{-1/2}$, by integral comparison, so the squared Schur norm is at most six. This proves the upper bound on the second moment. The total variation of the sequence $b_t^2$ extended by zero to $t\le0$ is at most $2\sqrt D$. Summation by parts at frequency $2\theta$ gives $\mathbb E\sin^2(t\theta)=1/2+O_\theta(\sqrt D)$. Moreover $\mathbb Et^2=K+1=O(h^{-2})$. Hence
$$\mathbb E[\sin^2(t\theta)/t^2]\ge (\mathbb E|\sin(t\theta)|)^2/\mathbb Et^2\ge c_\theta h^2.$$
Finally $b_t^2/t$ extended by zero has total variation at most $(2\sqrt6+6)D$. To see this, difference the square first using $(b_t+b_{t-1})/t$ and Cauchy–Schwarz, then sum the denominator changes using $1/[t(t-1)]\le1/(t-1)^2$. Summation by parts now at $\theta$ gives $|\langle A_\theta\rangle|=O_\theta(h^2)$. Subtracting its square leaves the asserted variance. A fixed interior angle therefore needs variance normalization even at equal time. A fixed scaled angle $s>0$ does not.
