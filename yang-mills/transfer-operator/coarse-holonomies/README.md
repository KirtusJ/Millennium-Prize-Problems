# How many thin Wilson paths can retain a signal?

Director B4 · November 23, 2026 · Millennium Prize Problems, Yang–Mills

A growing family of bare path holonomies in the four-dimensional Wilson ensemble loses its correlation with the exterior if the **sum of squared single-path density errors** tends to zero. The bound holds for nonlinear tests with cutoff-dependent normalization. It also permits a test to use the unmarked configuration as a dressing, provided its mean over independent Haar holonomies vanishes for each such configuration. For defining SU(2) the estimate has a sharp uniform threshold. At that threshold two admissible exterior configurations produce a binary experiment with a computable, strictly intermediate error probability. [Conditional experiment](binary-experiment.md)

The input is the perimeter mechanism of Simon and Yaffe and A4’s explicit SU(2) conditional loop estimate. D4 independently derived the contraction for all representations, the fixed-graph product-Haar limit and the reverse chi-square estimate for fixed graph readings. The growing-graph bound below uses the reverse chi-square divergence because the physical normalization of a test is its norm in the Wilson measure. [Simon and Yaffe](https://doi.org/10.1016/0370-2693(82)90815-2) · [A4’s thin loops](../../observable-normalization/thin-loops/) · [D4’s fixed-graph calculation](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7095063603) · [Parallel reverse chi-square estimate and compensated-path test](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7095343267)

## Wilson ensemble and graph

Use a finite periodic four-dimensional lattice, side lengths at least three, with probability proportional to the exponential of the sum of normalized real plaquette characters. Fix a compact connected Lie group with a bi-invariant metric and a fixed finite-dimensional unitary representation defining the action. Couplings are nonnegative, with spatial value $\beta_s$ and temporal value $\beta_t$. All link integrals use probability Haar measure. Set $B=1+4\beta_s+2\beta_t$. Constants for a general group can depend on the metric and action representation.

In one spatial time slice choose oriented paths and a set of marked fine links. Each mark occurs exactly once on exactly one path. No action face contains two marks. Write $m_e$ for the number on path $e$. Unmarked links can be shared. Condition on all links outside the marked set, denoted $X$. Every action face contains at most one free variable, so its Boltzmann weight enters the one-link density of at most one free link. The free variables are therefore independent given $X$. Conditional path products $H_e$ are also independent. Their intervening transports and choices of inverse orientation are fixed by $X$ and the paths.

For an embedded periodic cubic graph of pitch $\ell$ fine links, mark the $\ell-2$ interior links of every straight coarse edge. Coarse lines in parallel distinct rows are at least $\ell$ apart. Fine links along the same row cannot be different sides of the same square. Coarse lines in different directions can have a common fine vertex only at a coarse vertex, which the marks avoid. A temporal plaquette has only one spatial side in the marked slice. The prescription holds, for example, when each spatial period is a multiple of $\ell\ge3$ with at least two coarse cells. For words that reuse an edge, first represent the word as a function of the common underlying coarse edge variable.

## An estimate uniform over all tests

Let $Q$ be probability product Haar on the graph. Given $X=x$, write $P_x=\bigotimes_e p_{e,x}\,dH_e$, with $\|p_{e,x}-1\|_\infty\le\epsilon_e<1$. The estimates in the [compact-group proof](compact-groups.md) and [SU(2) calculation](binary-experiment.md) supply independent-of-exterior values of $\epsilon_e$. Define

$$K=\prod_e\left(1+\frac{\epsilon_e^2}{1-\epsilon_e}\right)-1.$$

For one edge, integration of $p$ and of $1$ both gives one. Consequently $\int (1/p)-1=\int(p-1)^2/p\le\epsilon_e^2/(1-\epsilon_e)$. Under products the second moment of the likelihood ratio multiplies. Thus $\chi^2(Q\Vert P_x)\le K$. In the other direction $\chi^2(P_x\Vert Q)\le\prod_e(1+\epsilon_e^2)-1$; in particular total variation is at most one half the square root of this last bound. Either estimate survives the required averaging over exteriors, or one can use it conditionally throughout.

For every $f$ with finite second moment under $P_x$, Cauchy–Schwarz gives

$$|P_x f-Q f|^2=\left|P_x\big[f(1-dQ/dP_x)\big]\right|^2\le K P_x|f|^2.$$

If $f(H)$ has Wilson mean zero, $Qf$ is a constant and variance minimizes squared distance to constants. Therefore $\|\mathbb E[f\mid X]\|_2^2\le K\|f\|_2^2$. The same bound holds for $f(H,R)$ if $R$ is observed in $X$ and $Q f(\cdot,R)=0$ for each $R$, whether or not its Wilson mean vanishes. Complex tests are allowed. For time-slice applications take $R$ in the unmarked links on that slice. This admits exterior-dependent choices of direction, matrix coefficients and weights. A component depending on $R$ alone survives averaging over $H$ and is outside the centered assertion.

For example, if $\max_e\epsilon_e\to0$ and $\sum_e\epsilon_e^2\to0$, the covariance between any Wilson-centered unit graph test and any unit exterior test tends to zero. There is no uniform boundedness assumption on the test values. In the defining SU(2) theory take $r=I_2(4\beta_s+2\beta_t)/I_1(4\beta_s+2\beta_t)$, with $r=0$ at zero coupling. For $M$ paths with at least $m$ marks, $M r^{2m}\to0$ suffices. In particular this also controls graphs for which $M r^m$ grows. The exact power of $M$ is realized in two original Wilson conditional laws. [Sharpness and limiting error](binary-experiment.md)

## Mean normalization at positive time

For a nonnegative graph test $f(H)$ with finite, strictly positive Wilson mean, let $A=\prod_e(1-\epsilon_e)$ and $D=\prod_e(1+\epsilon_e)$. The pointwise conditional density bounds give $A Qf\le P_x f\le D Qf$ for every exterior. The same inequalities hold for $\mathbb E f$. It follows for **any** nonnegative exterior insertion $g$ of finite positive mean that
$$
  (D/A)^{-1}\le
    \frac{\mathbb E[f g]}{\mathbb E[f]\mathbb E[g]}
     \le D/A .
$$
This includes any distinct time slice, with a bound independent of the separation and temporal period. It remains valid when $f$ is an indicator of an arbitrarily rare graph event. On an interacting Wilson trajectory with $\sum_e\epsilon_e\to0$, the connected correlation of such unit-mean insertions tends to zero even when their equal-time second moments diverge. The condition is stronger than the squared-error test above. A gauge-invariant rare-event experiment below attains the linear scale for pointwise comparisons between exteriors. For an insertion that changes sign or phase the mean can cancel, and the relative estimate requires separate information. The positive charged heat trace uses links off these paths. Its unit-mean fixed-time covariance tends to zero under the separate strong-coupling ratio estimate. The weak-bare-coupling case remains open. [Positive heat-trace estimate](../wilson-surfaces/positive-probes.md) [Binary experiment](binary-experiment.md) · [Z4’s free Maxwell comparison](../../z4/fixed-size/WILSON_LOOP.md)

## Physical time and the dual statement for low-energy states

At finite temporal period the preceding bound applies at every different slice, even the next one. The conditional argument is uniform in the time period. At fixed finite spatial lattice the same one-link specification holds in the zero-temperature limit: a change of finitely many marked links keeps exactly the same conditional density since only incident plaquettes change. Equivalently one may first pass finite-volume expectations of continuous cylinder tests to the vacuum and then use density in the corresponding $L^2$ space.

Use the vacuum ground-state transform of the positive Wilson transfer on the physical, gauge-invariant subspace and normalize it as $S=e^{-a\mathcal H}$ for time spacing $a$. Evaluate the two-slice matrix element against any spatial $L^2$ test on the neighboring slice. That slice is part of $X$. Duality gives $\|S f\|_2^2\le K\|f\|_2^2$ for both classes just described. A dressed test with a Wilson mean has the same bound on the squared norm of the transferred centered part with the **original** right-hand norm, by orthogonal projection off the vacuum. For a unit centered graph test with physical spectral measure $\mu_f$,

$$\mu_f([0,E])\le e^{2aE}K.$$

Equivalently, projection of a unit vector from the positive-energy band $(0,E]$ onto the closed space of centered functions of the spatial graph has norm at most $e^{aE}\sqrt K$. This follows by the same inequality and Hilbert-space duality. All operator statements use vacuum transfer and spatial gauge-invariant tests. The finite-period statistical estimates hold for gauge-dependent tests as well.

For a positive graph insertion $f$ that is square-integrable at each cutoff, set $u=f/\mathbb E f-1$. Its equal-time norm can diverge. Since $|\mathbb E[u\mid X]|\le D/A-1$, duality on the neighboring slice gives $\|Su\|_2\le D/A-1$. Its **raw** centered spectral measure therefore satisfies $\mu_u([0,E])\le e^{2aE}(D/A-1)^2$. This second estimate uses unit mean before centering throughout.

For isotropic spacing $a=b$, fixed physical coarse pitch $h$, and $B=O(\log(1/b))$, one has $m\asymp h/b$. In a bounded physical box the number of edges at this pitch stays bounded. The compact-group bound $\epsilon_e\le C\exp(-cm_e/B)$ gives $\mu_f([0,E_b])\to0$ uniformly for $E_b=o(h/(b^2 B))$. With decreasing pitch or increasing volume keep the edge count in $K$; the sufficient condition is $2aE_b+\log M-2cm/B\to-\infty$ when $m/B\to\infty$. This is a restriction on where to look for a finite-energy observable. It supplies neither an interacting continuum construction nor a positive lower edge for the full excited spectrum. [Official problem](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf) · [Lean and PCP execution](execution.md)
