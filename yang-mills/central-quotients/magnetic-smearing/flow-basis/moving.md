# What spatial flow times resolve at nonzero momentum

Fix external momentum magnitude $k>0$. In the centered two-gluon magnetic sector use $E=p+q$, $z=p-q$ for the two momentum magnitudes, so $E>k$, $-k<z<k$. Apart from a positive constant the unflowed measure is $W(E,z)dE\,dz$, where
$$
 W(E,z)=(E^2-k^2)^2+(k^2-z^2)^2 .
$$
A spatial-flow vector at time $s$ has amplitude $e^{-sQ/2}$ with $Q=E^2+z^2$. Its norm and its mixed-time inner products thus depend on two internal coordinates through a single variable. The observable fixes its transverse tensor structure. [Momentum measure and angular contraction](../flow-momentum/spectrum.md)

Allow arbitrary finite signed combinations of clock values in **any** interval $0<a<b$. Their closure is precisely the square-integrable functions of $Q$ in this scalar representation, using the closed isometric pullback from the pushforward measure. The argument by analytic uniqueness and polynomial density for the Laplace transform in $Q$ is the same as at rest. The tilted integrals are finite owing to the Gaussian and the polynomial density. At $k>0$ this space cannot select $E$ independently of $z$.

Given an energy window $J$, the supremum of the normalized spectral mass placed in it equals the essential supremum over $Q$ of the conditional fraction $p_J(Q)$. Indeed the fraction for any amplitude $h(Q)$ is a weighted average of $p_J$. Localizing $h$ on finite-measure subsets where $p_J$ is near its essential supremum attains the bound in the limit. Density of the original finite clock combinations and continuity of the bounded spectral projection justify the same supremum for the physical clock basis in the free control.

For $Q>k^2$, put $Z(Q)=\min(k,\sqrt{Q-k^2})$, $E(z)=\sqrt{Q-z^2}$, and
$$
 D(Q)=\int_0^{Z(Q)} W(E(z),z)\frac{dz}{E(z)} .
$$
Changing $E$ to $Q$ and adding the two signs of $z$ gives this continuous positive density. In $[E_0,E_0+\delta]$ the integral is restricted to
$$
 \sqrt{(Q-(E_0+\delta)^2)_+}\le z\le \sqrt{(Q-E_0^2)_+},\qquad 0\le z\le Z(Q),
$$
with zero contribution if the intervals do not overlap. Divide by $D(Q)$ to obtain $p_J(Q)$.

For any **interior energy** $E_0>k$, as $\delta\downarrow0$ the supremum over all radius mixtures is
$$
 \frac{W(E_0,0)\sqrt{2E_0}}{E_0D(E_0^2)}\sqrt{\delta}
       +o(\sqrt{\delta}).
$$
Only $Q\in[E_0^2,(E_0+\delta)^2+k^2]$ contributes. On that compact range the denominator has a positive lower bound. The width in $z$ is at most $\sqrt{(E_0+\delta)^2-E_0^2}$. If $Q$ stays bounded away from $E_0^2$, rationalizing the two square roots instead gives $O(\delta)$. If $Q\to E_0^2$, the integrand throughout the nonempty interval tends uniformly to $W(E_0,0)/E_0$. These bounds give the asserted leading upper constant. At $Q=(E_0+\delta)^2$ the interval begins at zero and attains the full square-root width for small $\delta$. Continuity supplies the same essential supremum lower asymptotic. At $k=1,E_0=2$ its coefficient is approximately 2.495247765. [Numerical test](check_window.py)

Two boundary cases matter. At **threshold** $E_0=k$, localizing $Q$ just above $k^2$ places all accessible energy in $[k,k+\delta]$ in the limit, since $k\le E\le\sqrt Q$. At **zero momentum** $Q=E^2$, and the supremum in every nonempty positive-width band is one. These conclusions refer to a free continuous spectrum without a bound-state pole.

If independent positive Euclidean transfer times $t$ are allowed, the basis gains products $e^{-tE-sQ/2}$. Varying each parameter in an open positive interval spans all square-integrable even amplitudes of $(E,z)$ in this same scalar tensor channel. Orthogonality implies the tilted two-variable Laplace transform vanishes, first by analytic uniqueness in $t$ at every specified $s$, then in $s$. Tilting at fixed positive values gives a finite signed measure. Evaluating at positive integer increments gives all mixed moments of $(e^{-E},e^{-Q/2})$, which determine it by polynomial density on the compact square. The map $(E,|z|)\mapsto(E,Q)$ is injective. This proves the claim about the extended basis, without a stability bound for that inverse problem.
