# Reconstructing a free transfer step with spatial flow

Work in the transverse Gaussian tangent of the Wilson action, with periodic space and infinite discrete Euclidean time. Remove any flat zero mode before forming the Gaussian vacuum. Spatial curls annihilate that mode. Write $B_s$ for a magnetic component evolved on a single slice by the linear spatial flow. Its multiplier is $e^{-sv}$, where $v(\mathbf p)=4\sum_{i=1}^3\sin^2(p_i/2)$. A shift of the plaquette base point only adds a Fourier phase. The free temporal propagator has denominator $2+v-2\cos p_0$. For $v>0$ its covariance at lag $n$, divided by its equal-time value, is $q(v)^n$ with
$$
q(v)=\frac{2}{2+v+\sqrt{v(v+4)}}=\exp\{-2\operatorname{arsinh}(\sqrt v/2)\}.
$$
Indeed the propagator solves the nearest-neighbor difference equation away from its source. Its decaying root solves $q^2-(2+v)q+1=0$. Set $q(0)=1$ by continuity. [Magnetic spectrum and conventions](../flow-momentum/spectrum.md)

## An exact positive clock law

Start a continuous-time simple symmetric walk at zero with rate one in each direction, and let $T_n$ be its first visit to $n\ge1$. Recurrence gives finite hitting time almost surely. The strong Markov property gives independent identically distributed increments between successive levels. A first-step decomposition for $T_1$ gives $(2+v)f=1+f^2$ for its Laplace transform. For $v>0$, $f<1$ selects $q(v)$. Thus $E e^{-vT_n}=q(v)^n$. The density on the positive half-line is
$$
 k_n(u)=n\,e^{-2u}I_n(2u)/u .
$$
For $j\ge n$ with $j-n$ even, the ballot count gives first passage on jump $j$ with probability $(n/j)2^{-j}\binom{j}{(j+n)/2}$. Multiplication by the rate-two Erlang density for the time of that jump and summation yields the Bessel series above. This also fixes the factor of two when translating a unit-total-rate convention. [Kovchegov, Meredith and Nir, *Occupation times and Bessel densities*, introduction](https://sites.science.oregonstate.edu/~kovchegy/web/papers/OccupationTimes.pdf)

For any baseline $s_0\ge0$, form $\bar B=\int B_{s_0+u}\,k_n(u)\,du$ on the initial slice. Sum squared components to form $\bar H=\frac12\sum_{i,a}\bar B_{i,a}^2$. Use $H_{s_0}=\frac12\sum_{i,a}B_{s_0,i,a}^2$ with the same choices of components. Superscript $c$ denotes subtraction of the vacuum mean. For the normalized transfer $\widehat T$ and vacuum $\Omega$,
$$
 \bar H^c\Omega=\widehat T^{\,n} H_{s_0}^c\Omega .
$$
Each transverse mode of the future field has conditional mean $q(v)^n$ times its present value. The future field is the sum of this mean and an independent centered Gaussian innovation. The conditional second moment at the chosen site adds a deterministic innovation variance, which cancels after vacuum centering. The identity holds before spatial averaging and hence also after an arbitrary finite spatial packet. In the quadratic observable the two field legs have **independent** clocks drawn from $k_n$. One common random time for the two fields gives a multiplier depending only on $v+w$. At rest the two symbols agree, and a common clock of law $T_{2n}/2$ works there. The positive representation fits on a single Euclidean slice. It requires access to arbitrarily large spatial flow times.

With mesh $a$, $a^2T_{\lfloor t/a\rfloor}$ converges in distribution for $t>0$ to the positive time with density $t e^{-t^2/(4u)}/(2\sqrt{\pi}u^{3/2})$. Its Laplace transform follows by substituting $a^2\lambda$ in $q$ and taking the power $\lfloor t/a\rfloor$. The continuum transform is $e^{-t\sqrt\lambda}$, the spatial Poisson semigroup. A positive physical baseline makes the continuum local squared field integrable in the vacuum. [Stinga and Torrea, extension and Poisson formulas](https://arxiv.org/abs/0910.2569)

## How long must a positive spatial clock run?

For $U\ge1$, let $\epsilon_n(U)$ be the infimum, over probability measures supported in $[0,U]$, of their maximum Laplace-transform error against $q(v)^n$ for $0\le v\le12$. Then
$$
 \frac1{64}\min(1,n/\sqrt U)\ \le\ \epsilon_n(U)\
 \le\ \min\!\left(1,\frac{n}{(1-e^{-1})\sqrt U}\right).
$$
Clipping $T_n$ at $U$ gives error at most $P(T_n>U)$. Bounding this by $(1-q(1/U)^n)/(1-e^{-1})$ and using $2\operatorname{arsinh}(\sqrt v/2)\le\sqrt v$ proves the upper estimate. Discretizing the clipped clock into bins of width $\eta$ costs at most $12\eta$ uniformly, by the derivative bound in the clock variable.

For the converse put $M=\max(U,n^2)$, $x=1/(16M)$, $A=1+e^{-Ux}$. For a candidate law with deficit $d_\mu(x)=1-\int e^{-xu}\,d\mu(u)$, factoring $1-e^{-2xu}$ gives $d_\mu(2x)\ge A d_\mu(x)$. For the target deficit $d=1-q^n$, concavity of both $\operatorname{arsinh}$ and $1-e^{-y}$ on positive inputs gives $d(2x)\le\sqrt2\,d(x)$. Thus an error $e$ must satisfy $(1+A)e\ge(A-\sqrt2)d(x)$. Here $31/16\le A\le2$ and $\sqrt2<3/2$. On $[0,1/16]$, integration of the derivative of $\operatorname{arsinh}$ gives $3\sqrt{x}/4\le-\log q(x)\le\sqrt{x}$. Since $-n\log q(x)\le1/4$, the inequality $1-e^{-y}\ge3y/4$ on this range yields $d(x)\ge(9/64)\min(1,n/\sqrt U)$. Combining gives the stated constant. The lower bound tests a *continuous* range of spatial frequencies. The union of periodic Fourier symbols over increasing volumes is dense in that range. A single fixed finite Fourier set need not contain these two test points. [Independent Bessel and tridiagonal checks](check_clock.py)

## Why two independent spatial times change the moving channel

In the free continuum let $k=|\mathbf p+\mathbf q|>0$, $p=|\mathbf p|$, $q=|\mathbf q|$. The magnetic tensor contraction fixes the scalar measure. Write $E=p+q$, $z=p-q$ with $E>k$ and $|z|<k$. Its positive density is proportional to $(E^2-k^2)^2+(k^2-z^2)^2$. For the bilinear reading $\tfrac12\sum B_{s,i,a} B_{u,i,a}$ the scalar multiplier on the two-particle vector is the symmetric part of $e^{-sp^2-uq^2}$. Independent $s,u$ in any common open positive interval span densely **all symmetric scalar amplitudes in this channel**. To prove this take a symmetric orthogonal amplitude $f$. Its joint Laplace transform against the scalar measure vanishes on the product interval. Cauchy–Schwarz and Gaussian damping give separate holomorphy for positive real parts, so uniqueness in each variable extends vanishing to all positive pairs. After a fixed positive tilt, the signed or complex measure is finite. All mixed polynomial moments of $(e^{-p^2},e^{-q^2})$ vanish, including the constant. Polynomial density on the compact square and injectivity on the finite momentum domain imply $f=0$ almost everywhere. In particular, finite signed two-clock readings can concentrate an arbitrarily large fraction of their norm in any bounded energy band of positive measure. This argument supplies no bound on their coefficient sizes.

The common-time family has closed scalar span $L^2(Q)$ with $Q=E^2+z^2$. At baseline $s_0>0$ the least squared error in reconstructing the transferred common-time vector at physical lag $t>0$ from that family equals
$$
 \int e^{-s_0Q}\operatorname{Var}(e^{-tE}\mid Q)\,d\nu_Q .
$$
Here $\nu_Q$ is the pushforward of the unflowed scalar measure. Its conditional law of $|z|$ has positive density throughout an interval of positive length for $Q>k^2$. The conditional variance is strictly positive since $E=\sqrt{Q-z^2}$ varies across it. At $k=0$, $z=0$ and this residual vanishes. This distinction holds even if the two free fields are observed at the same site and time. [One-clock projection and fixed-momentum measure](../flow-basis/moving.md)
