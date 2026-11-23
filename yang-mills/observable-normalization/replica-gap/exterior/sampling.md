# What does an endpoint measurement cost?

A positive reading built from *exact* transition probabilities can have bounded relative variance while estimating those probabilities from samples costs exponentially many draws. A two-state transfer makes that distinction quantitative. The four-dimensional electric $SU(2)$ Wilson regulator also gives a case where access to individual link increments permits a positive estimator with a polynomial sample bound, uniform in temporal coupling and spatial volume.

## An information bound for long slabs

Consider a two-state symmetric Markov transfer with eigenvalues $1,r$, $0<r<1$. In a row of the $n$-step kernel, the sign of agreement between starting and ending states has probabilities $(1\pm\theta)/2$, $\theta=r^n$. The squared subleading slab eigenvalue is $\theta^2$. It also sets the scale of the period-$2n$ thermal deficit, exactly $2\theta^2/(1+\theta^2)^2$. Suppose the available interface returns independent row samples, permitting either starting state on each request. Even an adaptive starting-state choice yields only a sequence of independent agreement signs, since their distribution is independent of that choice. The unknown transfer parameter is not provided to this interface.

For $0<\theta<1/2$, compare parameters $\theta$ and $2\theta$. An estimator of the squared eigenvalue with relative error at most $1/3$ and success probability at least $3/4$ under both parameters yields a test with total variation distance at least $1/2$, because the two success intervals are disjoint. For one sign the chi-squared divergence of the second law from the first is $\theta^2/(1-\theta^2)$. For $M$ independent signs, the second likelihood-ratio moment multiplies. Cauchy–Schwarz bounds total variation by half the square root of the chi-squared divergence. Consequently
$$
 M\ \ge\ \frac{\log 2}{-\log(1-\theta^2)} .
$$
At small $\theta$ this grows as $r^{-2n}\log 2$. The lower bound concerns unknown kernels and row samples at the specified slab length. Moreover a universally unbiased **nonnegative** statistic of a fixed finite sample cannot estimate $\theta^2$: the fair-coin law at zero assigns positive mass to every transcript, forcing the statistic to vanish on every transcript. Continuity of the finite expected value extends this obstruction to estimators claimed unbiased for all $0<\theta<1$. The same reasoning applies after conditioning out auxiliary randomization.

## A positive short-step estimator on the electric Wilson lattice

Take a cubic torus $L\ge5$, zero spatial coupling and temporal coupling $\gamma>0$. Its full first excited transfer ratio is $r=u^4$, where $u=I_2(\gamma)/I_1(\gamma)$. Thus the squared $n$-step eigenvalue is $u^{8n}$. Draw a single normalized Wilson kinetic increment and let $z=\operatorname{Tr}U/2$, with density proportional to $e^{\gamma z}\sqrt{1-z^2}$ on $[-1,1]$. Use the reading
$$
 X_\gamma=\begin{cases}
 \gamma(1-z^2)/3,&0<\gamma\le3,\\
 z\tanh(\gamma z),&\gamma>3 .
 \end{cases}
$$
Both branches are nonnegative and have mean $u$. For the first, integrate the derivative of $e^{\gamma z}(1-z^2)^{3/2}$ between the endpoints and use $\mathbb E z=u$. For the second, condition $z$ on $|z|$ and average the two possible signs. [One-link spectrum and Wilson derivation](../../../transfer-operator/) · [Four-dimensional electric spectrum](../electric.md)

In fact $\mathbb E X_\gamma^2/u^2<2$ **at every positive coupling**. For a reading bounded by $B$, this ratio is at most $B/u$. At $\gamma\le3$ use $B=\gamma/3$. Here $u/\gamma=\mathbb E(1-z^2)/3$ decreases: differentiating $\mathbb E z^2$ under the folded law gives the covariance of $|z|^2$ and $|z|\tanh(\gamma|z|)$, two increasing functions. Their covariance is nonnegative by the two-independent-copies identity. At $\gamma>3$ use $B=1$ and $u'=\operatorname{Var}z>0$. Both bounds peak at $1/u(3)<2$. To verify the strict inequality, the first three terms of the positive $I_2(3)$ series exceed 2. The first three $I_1(3)$ terms plus the next term divided by $1-9/80$ bound the entire sum below 4.

Put $p=8n$. Take $p$ independent blocks of $M=2p$ readings each and multiply their means. Independence gives an exactly unbiased positive estimator of $u^p$. Its relative variance is
$$
 \left(1+\frac{\operatorname{Var}X_\gamma}{M u^2}\right)^p-1 < e^{1/2}-1.
$$
The estimator uses $2p^2$ draws irrespective of the spatial volume or temporal coupling. Producing them also has uniformly bounded expected proposal count per accepted draw. For $\gamma\le3$, propose Haar $z$ and accept with probability $e^{\gamma(z-1)}\ge e^{-6}$. For $\gamma>3$, propose $y\sim\operatorname{Gamma}(3/2,1)$, and accept with probability $\sqrt{\max(0,1-y/(2\gamma))}$. The change of variable $z=1-y/\gamma$ gives the required density. The acceptance probability is at least $\Pr(y\le3)/\sqrt2$. These sample counts refer to real arithmetic. Logarithmic accumulation or additional numerical precision can be necessary to represent a tiny product.

The Wilson estimator uses the exactly identified eigenfunction and factorized electric transfer. Extending its cancellation and uniform variance control to nonzero spatial coupling remains open. The [reproducible control](check_cost.py) checks the switch-point bound in rationals, compares both expectations with Bessel ratios by radial quadrature and simulates products of independent block means at three couplings.
