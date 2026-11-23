# When a positive magnetic autocorrelation leaves a false plateau

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

C4 constructed a free two-particle magnetic observable with continuous spectrum down to momentum threshold $k>0$ and effective energy initially near any prescribed $e>k$. For C4's explicit filter of order $m$, the first time at which the effective energy reaches a level $k<\lambda<e$ has an exact leading coefficient on the $\log m$ time scale. If $2k<e<3k$, the reading visits a second plateau at $s=e-k$ before reaching the threshold. Both plateaus occur in the same positive autocorrelation with no spectral atoms. [Filter and magnetic measure](../../../../central-quotients/magnetic-smearing/transfer-clock/interior/cost.md) · [C4's logarithmic-order estimate](../../../../central-quotients/magnetic-smearing/transfer-clock/interior/plateau.md)

Write $d=7/2$. Let $R_m(t)$ denote the normalized positive-time correlation, $M_m(t,\tau)=-\tau^{-1}\log(R_m(t+\tau)/R_m(t))$ for a fixed $\tau>0$, and $T_m(\lambda)$ the first crossing. Then

| Target energy | Crossing level | Limit of $T_m(\lambda)/\log m$ |
|---|---|---|
| $k<e\le 2k$ | all $k<\lambda<e$ | $d/(e-k)$ |
| $2k<e<3k$ | $e-k<\lambda<e$ | $d/k$ |
| $2k<e<3k$ | $k<\lambda\le e-k$ | $d/(e-2k)$ |
| $e\ge3k$ | all $k<\lambda<e$ | $2d/(e-k)$ |

For example, set $k=1$ and $e=2.5$. At times $c\log m$ the limiting energies are $2.5$ for $0<c<3.5$, $1.5$ for $3.5<c<7$, and $1$ for $c>7$. At order 4096 the corresponding unit-step effective energies for $c=2,5,12$ are $2.497705,1.524410,1.011707$. These are deterministic free-model quadratures. The proof uses the actual filtered magnetic density. No spectrum was fitted to these numbers. The four-dimensional interacting continuum gap remains open. [Numerical and formal checks](checks.md) · [Related lattice-QCD plateau study](https://arxiv.org/abs/1607.06371)

## Mass near the momentum threshold

Put $r=e/2$, and let $p,q$ be the magnitudes of the two momenta. Their domain is $|p-q|<k<p+q$. The normalized law has density proportional to $L_m(p)^2L_m(q)^2 W(p,q)$, where
$$
 W=((p+q)^2-k^2)^2+(k^2-(p-q)^2)^2 .
$$
The positive Gaussian clocks $0<a<b$ are fixed. The filter is $L_m(p)=e^{-ap^2}[D_m(\theta(p)-\theta(r))+D_m(\theta(p)+\theta(r))]^2$, with $D_m(u)=[\sin(mu/2)/(m\sin(u/2))]^2$, $h=(b-a)/(2(m-1))$, and $\cos(\theta(p)/2)=e^{-hp^2/2}$. Use the continuous values at removable singularities.

The cost of displacing one momentum a fixed distance from $r$ is $m^{-d}$ after normalization. The following estimates make this precise.

* The integral of $(1+p)^4 L_m(p)^2$ is $O(m^{-1/2})$. For $0\le p\le\sqrt m$, the derivative of $\theta$ lies between two positive constants times $m^{-1/2}$, including its right derivative at zero. Here $|\sin((\theta(p)-\theta(r))/2)|\gtrsim |p-r|/\sqrt m$. The reflected squared sine is at least as large. The elementary bound $D_m\le1$ therefore gives $L_m(p)^2\le C e^{-2ap^2}(1+m(p-r)^2)^{-4}$. Above $\sqrt m$, both denominator sines are bounded below for large $m$ and the Gaussian absorbs every polynomial. In particular, outside $|p-r|<\rho$ the same weighted integral is $O(m^{-4}\rho^{-8})$ for $0<\rho\le1$.
* On $|p-r|<u/\sqrt m$ for fixed sufficiently small $u>0$, $L_m(p)^2$ is bounded below by a positive constant. On any fixed compact interval of positive length away from $r$, $L_m(p)^2\ge C m^{-4}$ on a subset occupying a fixed positive fraction. Indeed the phase $m(\theta(p)-\theta(r))/2$ has derivative comparable to $\sqrt m$. Take the portion of each complete period where the absolute numerator sine exceeds $1/2$. Its squared denominator $m^2\sin^2((\theta(p)-\theta(r))/2)$ is at most $C m$ on a compact interval, and both terms in the filter are nonnegative. This fraction bound also holds for intervals in the same compact set whose lengths times $\sqrt m$ tend to infinity.
* The two-variable normalization is $\Theta(m^{-1})$. The upper bound follows by the first estimate and $W\le C(1+p)^4(1+q)^4$. For the lower bound take both momenta in their $u/\sqrt m$ intervals. The point $(r,r)$ is strictly inside the triangle and $W(r,r)>0$.

For every sufficiently small fixed $\delta>0$, the probability of $k<E<k+\delta$ is $\Theta(m^{-7/2})$ when $e\le2k$ and $\Theta(m^{-7})$ when $e>2k$. To see why, fixing $p=r$ gives the infimum $s=r+|k-r|=\max(k,e-k)$ over admissible $q$. If $s=k$, take $p$ inside its peak and $q$ in a fixed interior interval just above $|k-r|$. This includes $r=k$ by taking $q>0$. One peak and one displaced interval give mass at least a constant times $m^{-7/2}$. At least one leg must be a fixed distance from $r$ when $\delta<e-k$, giving the matching upper bound. If $s>k$, choose $\delta<s-k$. Both legs must then stay away from $r$ by the one-leg inequality below. A fixed interior rectangle with both legs near, and above, $k/2$ gives the lower bound. C4's $m^{-7}$ lower bound holds in both regimes. It is sharp in the second.

## The three contributions at logarithmic times

For each $c\ge0$ the normalized law satisfies
$$
 -\frac{\log R_m(c\log m)}{\log m}\longrightarrow
 f(c)=\min\{ce,\ d+cs,\ 2d+ck\}.
$$
Fix a small $\rho>0$. With both legs within $\rho$ of $r$, $E\ge e-2\rho$ and mass is at most one. With exactly one near $r$, $E\ge s-2\rho$, since $p+q\ge k$ and $p+q\ge2p-k$ for the near leg $p$. This region has mass $O_\rho(m^{-d})$. With both away, $E\ge k$ and the mass is $O_\rho(m^{-2d})$. Integrating the three upper estimates and then sending $\rho$ to zero gives $\liminf\ge f(c)$.

For the converse, the two-peak rectangle has positive normalized mass and $E=e+O(m^{-1/2})$. For any $\epsilon>0$, a narrow interior $q$ interval immediately above $|k-r|$ and a shrinking $p$ peak give mass $\gtrsim_\epsilon m^{-d}$ with $E<s+\epsilon$. The interval can be chosen disjoint from the peak since $e>k$ and $k>0$. A fixed rectangle with both legs just above $k/2$ gives mass $\gtrsim_\epsilon m^{-2d}$ with $E<k+\epsilon$. Each rectangle has a positive lower bound on $W$ for all sufficiently large $m$. Taking the best of the three lower contributions and then $\epsilon\downarrow0$ proves the limit.

The functions on the left are concave in $c$, by Hölder's inequality for the Laplace integral. Their secants over $[c,c+\tau/\log m]$ are exactly $M_m(c\log m,\tau)$. Between corners these secants tend to the slope of $f$: bound them by secants to fixed points $c-\gamma$ and $c+\gamma$, then let $\gamma$ decrease to zero. The effective energy is continuous and strictly decreasing for each $m$ because the law has a nonconstant energy. For fixed $m$ it tends to $k$ as $t\to\infty$ by the positive mass in each threshold interval. At any sufficiently small fixed positive $c$ its limit as $m\to\infty$ is $e$. Thus the first crossing exists for large $m$, and slopes on the two sides squeeze its leading time unless $\lambda$ equals an intermediate slope. Comparing the three affine functions gives the four ranges in the table. At $e=3k$ all three meet at one point.

## Crossing the intermediate level itself

Suppose $2k<e<3k$, so $s=e-k>k$. Fix $d/k<c<d/(s-k)$, let $t=c\log m$, $\ell=1/\log m$ and $\rho=\ell^2$. We show $M_m(t,\tau)>s$ for sufficiently large $m$. Its sign relative to $s$ is the sign of
$$
 \int e^{-t(E-s)}(1-e^{-\tau(E-s)})\,d\mu_m(E).
$$
Take $|p-r|<u/\sqrt m$ and $q\in[r-k+2\ell,r-k+3\ell]$. This lies inside the triangle, $W$ is bounded below since $s>k$, and $E-s$ lies between $\ell$ and $4\ell$. The interval contains order $\ell\sqrt m$ oscillations. The earlier lower estimates give a positive contribution $\gtrsim m^{-d}\ell^2$.

For the negative contribution with one leg within $\rho$ of $r$, the conditions $p-k<q<s-p$ force $q$ within $\rho$ of $r-k$, a fixed distance from its own peak. Then $s-E\le2\rho$, the tilted multiplier has absolute value $O(\rho)$, and the normalized mass here is $O(m^{-d}\rho)$, including the symmetric region. With both legs away by $\rho$, the total mass is $O(m^{-2d}\rho^{-16})$. The multiplier on $k<E<s$ costs at most $C m^{c(s-k)}$. These two negative bounds are $o(m^{-d}\ell^2)$ because $c(s-k)<d$. This proves the sign assertion. Just after $d/(s-k)$ the limiting energy is $k<s$, so the intermediate level itself crosses at this second corner. The theorem leaves the effective energy at the precise corner times unspecified.
