# Decay in all representations from one-link curvature

Fix an exterior and one marked spatial link of a finite Wilson lattice. Write $p(g)=e^{V(g)}/Z$ and $D_X V(g)=\partial_t V(g\exp(tX))|_{t=0}$. A spatial link belongs to four spatial and two temporal plaquettes. In a unitary action representation $\rho$, the second derivative of each normalized trace along a unit geodesic has magnitude at most $\|d\rho(X)\|_{\rm op}^2$. The same estimate holds for inverses and translated arguments. Fix $L=C_\rho B\ge1$ large enough that $|D_X^2\log p|\le L|X|^2$ for every link and exterior. No strictly positive lower Hessian bound is required.

## Translations and variance

Haar invariance gives $\int D_X^2p=0$. Expanding the derivative yields $\int |D_X\log p|^2p=-\int D_X^2\log p\,p\le L$ for $|X|=1$. Integrate the first derivative along a shortest geodesic and use Cauchy–Schwarz. Then $\|p(\cdot h)-p\|_1\le\sqrt L\,d(1,h)$. In particular $q_h(g)=\min(p(g),p(gh))$ has integral at least $1/2$ whenever $d(1,h)\le L^{-1/2}$.

Take any finite-dimensional unitary representation $\pi$, a unit vector $v$, $z=\int\pi(g)v p(g)\,dg$, and $D=1-\|z\|^2$. This is the integrated squared orbit distance to $z$. Compare $\pi(g)v$ and $\pi(gh)v$ to $z$. Their distance is $\|v-\pi(h)v\|$ at every $g$. Dominating $q_h$ by $p(g)$ in the first squared term and by $p(gh)$ in the second gives
$$\|v-\pi(h)v\|^2\int q_h\le4D.$$
For general $g$, compact connectedness and the bi-invariant metric give a shortest one-parameter geodesic to $g$. Take $k=\max(1,\lceil\sqrt L\,d(1,g)\rceil)$ equal steps. Telescoping $k$ isometries now implies $\|v-\pi(g)v\|^2\le8(1+\sqrt L\,d(1,g))^2D$. Averaging against Haar in a nontrivial irreducible representation already gives contraction $1-c/L$ in operator norm, uniformly in the representation.

## Heat comparison removes a logarithmic loss in the density estimate

Use the heat kernel of the fixed compact group for the generator $\Delta$, with $-\Delta$ positive. A smooth nonnegative function $F$ can be chosen with $F(1)=0$ and $F(g)\ge d(1,g)^2$: take squared distance in a normal neighborhood, interpolate smoothly to a constant majorizing the squared diameter inside that neighborhood, then keep the constant outside. Since $P_tF(1)=\int_0^t P_s\Delta F(1)\,ds$, the heat-kernel expectation of squared distance is at most $t\|\Delta F\|_\infty$.

In representation $\pi$ of Casimir $\lambda$, heat averaging of the squared displacement gives exactly $2(1-e^{-t\lambda})$. At $t=1/L$, the geodesic estimate and the preceding distance bound therefore yield
$$1-\left\|\int\pi(g)v p(g)\,dg\right\|^2\ge c(1-e^{-\lambda/L}).$$
Consequently the norm of the Fourier matrix is at most $\exp[-c'\min(\lambda/L,1)]$. Left and right translations contribute unitary factors and inversion takes the adjoint. Products of different one-link laws multiply the corresponding matrix bounds even when their directions differ.

For clarity, the low- and high-frequency estimates use different summability facts. When $0<\lambda\le L$, the contribution of the entire product of $m$ increments to the sup norm of its density minus one is at most $\sum_{0<\lambda\le L}d_\pi^2e^{-c'm\lambda/L}$. The positive first Casimir and the finite heat trace $\sum_\pi d_\pi^2e^{-s\lambda_\pi}<\infty$ at any fixed $s>0$ bound this sum by $C e^{-c''m/L}$ for $m\ge4L$. Here $d_\pi$ denotes the dimension and the sum counts irreducible representations.

At a maximum of $V$ its gradient vanishes. Taylor’s theorem on the ball of radius $L^{-1/2}$ and the small-ball volume bound give $\|p\|_\infty\le C L^{d/2}$, $d=\dim G$. Thus each endpoint density has $L^2$ norm at most $C L^{d/4}$. On $\lambda>L$ the intermediate $m-2$ convolutions have $L^2$ operator norm at most $e^{-c'(m-2)}$ by Plancherel. The spectral projection commutes with the convolutions. Cauchy–Schwarz on the endpoint coefficients, or $L^2*L^2\subset L^\infty$, bounds the high-frequency density by $C L^{d/2} e^{-c'(m-2)}$. For $m\ge4L$ the polynomial is absorbed by lowering the exponential constant. Combining the bounds gives
$$\|p_{e,x}-1\|_\infty\le C e^{-c m_e/B}\qquad(m_e\ge C_0 B).$$
All constants are independent of volume, edge count, chosen exterior, and cutoff. Compact-group heat kernels here provide harmonic analysis of one link. The energy estimate for the interacting theory uses the distinct Wilson vacuum transfer in the [main theorem](README.md).
