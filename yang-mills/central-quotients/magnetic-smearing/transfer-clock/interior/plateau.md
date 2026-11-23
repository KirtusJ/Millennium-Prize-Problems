# A finite plateau above a continuous spectral threshold

For the [explicit filtered magnetic observable](cost.md#a-rank-one-construction-attaining-the-order) fix $k>0$, $E_0>k$, $0<a<b$ and time step $\tau>0$. Write $\mu_m$ for its normalized free energy measure. Its autocorrelator and effective energy are
$$
 R_m(t)=\int e^{-tE}\,d\mu_m(E),\qquad
 M_m(t,\tau)=-\frac1{\tau}\log\frac{R_m(t+\tau)}{R_m(t)} .
$$
Each $\mu_m$ is positive and absolutely continuous. Each finite-order field filter is a nonzero real analytic function of the momentum. It is nonzero almost everywhere, so every open interval above $k$ has positive mass. The bottom of its support is always $k$.

For every level $k<\lambda<E_0$, the first time at which $M_m(t,\tau)$ drops to $\lambda$ is $\Theta(\log m)$ as $m\to\infty$, in fixed time units. Throughout $0\le t\le c_0\log m$ the effective energy approaches $E_0$ uniformly for every $0<c_0<1/[2(E_0-k)]$. At $t/\log m\to\infty$ it approaches $k$. The estimates below establish the order of the crossover. A4 subsequently derived the leading coefficient for every crossing level and a second plateau at $E_0-k$ when $2k<E_0<3k$. [A4's independent leakage and crossing analysis](../../../../observable-normalization/energy-density/maxwell-benchmark/interior-leakage/README.md)

## Initial plateau

By the mean value theorem, $E\ge k$, and the second-moment estimate,
$$
 |e^{tE_0}R_m(t)-1|
 \le t e^{(E_0-k)t}\int|E-E_0|\,d\mu_m
 \le C t e^{(E_0-k)t}/\sqrt m .
$$
The right side tends uniformly to zero up to $c_0\log m+\tau$ in the stated range of $c_0$. Taking the logarithm of the ratio at the two time points proves the assertion. In particular a finite series of increasingly accurate measurements can follow a single exponential at any chosen $E_0>k$ in this model.

## Return to threshold

Fix small $\delta>0$ with $k+\delta<E_0$. Choose a closed interval $J$ of positive length inside $(k/2,(k+\delta)/2)$ so narrow that $|p-q|<k$ on $J^2$. There $k<E<k+\delta$ and the magnetic weight has a strictly positive minimum. On $J$, the phase $m(\theta(p)-\theta_0)/2$ is increasing with derivative between two positive multiples of $\sqrt m$. Its range contains order $\sqrt m$ complete periods. The portion of $J$ where the absolute sine of the phase exceeds $1/2$ has length bounded below independently of large $m$, by the derivative bounds and integration over those periods. The squared denominator $m^2\sin^2((\theta(p)-\theta_0)/2)$ is at most $Cm$ because $p$ and $p_0$ stay bounded. Consequently the positive kernel $H_m$ is at least $c/m$ on this portion. The baseline is bounded away from zero there, so $L_m(p)^2\ge c/m^4$.

Integrating on the product of the two good subsets and dividing by $\|F_m\|^2\asymp m^{-1}$ proves $\mu_m([k,k+\delta])\ge c_\delta m^{-7}$. For the probability tilted by $e^{-tE}$ it follows that
$$
 \mu_{m,t}([k+2\delta,\infty))\le C_\delta m^7e^{-t\delta}.
$$
When $t/\log m\to\infty$ this tends to zero. The ratio defining $M_m$ is the tilted expectation of the bounded function $e^{-\tau E}$. Letting $\delta\downarrow0$ proves convergence to $k$. For fixed $\lambda$ choose $k+2\delta<\lambda$ and take $t=(8/\delta)\log m$ to obtain $M_m(t,\tau)<\lambda$ for large $m$. The early estimate places it above $\lambda$ at $c_0\log m$. The function decreases continuously since $\log R_m$ is strictly convex for this nondegenerate law. These bounds give the claimed first-crossing order. For each fixed $m$, the positive mass of every near-threshold interval gives $\lim_{t\to\infty}M_m(t,\tau)=k$ by the same tilt argument.

Iritani et al. studied misleading plateaus in two-baryon calculations and Blossier et al. analyzed corrections in variational lattice correlators. Here the filter appears on both ends of an autocorrelator. The spectral weights are positive, the target is arbitrary and the continuum model has no spectral atom. These properties allow the duration and the eventual drift to be calculated in the same example. [Iritani et al.](https://arxiv.org/abs/1607.06371) · [Blossier et al.](https://arxiv.org/abs/0902.1265)

## What passes to a compact Wilson packet

Use the program's ordered weak limit of the four-dimensional $SU(2)$ Wilson vacuum. At a common site sum the flowed magnetic fields over clocks for each spatial plaquette orientation. Squaring and summing over the orientations gives the local scalar
$$
 \frac{\beta r^4}{2}\sum_{\alpha<\gamma}
 \left|\sum_j c_j\operatorname{Im}U_{\alpha\gamma}^{\rm sp}(s_jr^2)\right|^2 .
$$
Here $1/r$ is the lattice spacing and $s_j$ are the physical clocks from the construction. All terms in a squared norm transform in the same adjoint frame. Smear the scalar with a common spatial packet at momentum $k$ and subtract its vacuum mean. The coefficient norm uses the centered, packet-smeared bilinear atoms obtained by expanding this expression. [Joint-clock comparison](../wilson.md) · [Momentum packets and positive transfer](../../flow-momentum/spectrum.md)

For fixed $m$ and fixed packet and mesh there are finitely many clock values, positions and pair products. In a common rooted frame the fixed-clock comparison and Hölder's inequality give convergence of all the required second and fourth moments as the even side $L=\beta\to\infty$. Next refine the mesh at fixed packet, then increase its extent to select $k$. The positive baseline $a$ dominates the finite sums in momentum space, including the equal-time Gram entries. Sampling a physical lag $t$ with lattice lag $\lfloor rt\rfloor$ gives the corresponding Laplace test. Total masses and the positive integer time tests imply weak convergence of the spectral laws via polynomials in $e^{-E}$. The limiting free law has zero mass at the band boundaries.

For a shrinking sequence of widths, choose the free filters with retained fraction strictly larger than $\eta$. At each index choose the packet extent first, then mesh, then sufficiently large $L=\beta$, so the band fraction stays at least $\eta$ and all atomic norms and the combined norm approximate their free values to prescribed relative accuracy. One may include any prescribed finite list of effective-energy tests at each index. The two positive Laplace readings in each ratio can be required accurate to a relative tolerance even when they are small, since all choices at that index are finite. This proves $\log\chi=O(\epsilon^{-2})$ along selected compact regulators and transports the observed values at those finite times. The free lower cost, the compact late-time endpoint and a physical interacting mass gap require separate arguments. [Clay problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
