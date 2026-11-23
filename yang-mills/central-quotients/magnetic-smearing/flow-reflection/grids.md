# A negative reflected form on every buffered arithmetic grid

Fix full four-dimensional heat flow at physical time $s>0$. Use the centered free magnetic energy at one spatial point. For $d$ independent real colors, its ordinary covariance at time separation $t>0$ is
$$
 C_s(t)=B t^{-8}[1-(1+u)e^{-u}]^2,\qquad
 u=t^2/(8s),\qquad B=3d/(2\pi^4).
$$
The derivation differentiates the doubly flowed propagator and then uses Wick's rule. The positive constant cancels from every sign test. The squared single-plaquette tangent has the same profile up to a positive factor. [Derivation and conventions](../spatial-flow/spectrum.md) · [Eller and Moore, §§2–3](https://arxiv.org/pdf/1802.04562)

### Arbitrary buffer and mesh

For **every** $T,h>0$ there are finitely many integer coefficients $c_0,\ldots,c_k$ for which
$$
 Q=\sum_{i,j=0}^k c_i c_j C_s(T+(i+j)h)<0.
$$
Place the original readings at $T/2+jh$ and reflect about zero. This is an ordinary site-reflection test. Equivalently, for a fixed shifted plane $-R$, choose positive nominal times $T/2-R+jh$ with $T>2R$. The theorem permits any prescribed positive lower bound on distance from the plane.

**Proof.** Put $m_n=C_s(T+nh)$, $p_n=B(T+nh)^{-8}$, and $b_n=m_n-p_n$. Every $b_n<0$. Writing $v=(1+u)e^{-u}$, one has $0<v<1$ and $0<2v-v^2\le 2v$. Thus $\limsup |b_n|^{1/n}=0$. The sequence $p_n$ is the moment sequence on $[0,1]$ of the pushforward by $x=e^{-hE}$ of the finite measure $B E^7 e^{-TE}\,dE/7!$.

Suppose every finite Hankel form for $m$ is positive semidefinite. Hamburger's theorem gives a finite positive measure $\mu$ on the real line with these moments. Since its even moments are bounded, for every $\epsilon>0$ its mass on $|x|>1+\epsilon$ is bounded by $m_{2n}(1+\epsilon)^{-2n}$ and hence vanishes. Subtract the representing measure for $p$ to obtain a finite real signed measure $\sigma$ on $[-1,1]$ with moments $b_n$. This step allows a negative part of the coordinate spectrum. No additional shifted-Hankel positivity assumption enters. [Schmüdgen, *Ten Lectures on the Moment Problem*, Thm. 1.12](https://arxiv.org/pdf/2008.12698)

For $|z|>1$, its Cauchy transform is $G(z)=\int (z-x)^{-1}d\sigma(x)=\sum_{n\ge0} b_n z^{-n-1}$. This series is holomorphic on the punctured plane and real on the punctured real axis. The identity theorem gives the continuation from both half-planes. For a real continuous $\phi$ compactly supported away from zero, $-\pi^{-1}\int\phi(y)\operatorname{Im}G(y+i\eta)\,dy$ tends to zero by uniform continuation on its support. By Fubini this is also the integral against $\sigma$ of $\phi$ convolved with the Poisson kernel of width $\eta$. It tends to $\int\phi\,d\sigma$ by the approximate-identity property and finiteness of $|\sigma|$. Hence $\sigma$ is supported at zero, which gives $b_1=0$, a contradiction. A strict negative real form persists on approximating its finite vector by rationals. Clearing denominators gives the integer test. Continuity of the positive-flow covariance in spacetime permits replacing each point test by a sufficiently narrow smooth test within the same positive half-space. □

The comparison with $p$ also gives, for **any** real coefficients of total absolute value one at arbitrary times $t_i\ge T/2$,
$$
 Q\ge -2B T^{-8}(1+T^2/(8s))e^{-T^2/(8s)}.
$$
Indeed the unflowed reflected form is an integral of a square and the difference is bounded entrywise using the decreasing heat tail. A finite buffer permits exponentially accurate approximate positivity. Exact positivity fails for at least one finite test on each grid. No uniform bound on the necessary number of readings is asserted.

### Finite certificates

The table uses $T^8 Q/(B\|c\|_1^2)$. Entries displayed with a tilde are rounded. The script certifies outward-rounded intervals for them and separately checks that the unflowed forms are strictly positive in exact rational arithmetic. Grouping integer products by $i+j$ avoids double precision cancellation. For an exponential, it halves the argument to at most $1/2$, encloses the alternating Taylor series between consecutive partial sums, then squares outward-rounded nonnegative endpoints. All reported signs use integers and rational arithmetic. The negative tests were found using high-precision elimination and rounding of coefficient vectors. Certification uses only the deposited integers. [Coefficients](grids.json) · [Independent calculator](check_grids.py)

| $s$ | $T$ | $h$ | Readings | Normalized reflected form |
| ---: | ---: | ---: | ---: | ---: |
| $1/8$ | 1 | 1 | 3 | $\sim-1.312\,10^{-6}$ |
| 1 | 4 | $1/2$ | 2 | $\sim-9.097\,10^{-4}$ |
| 1 | 6 | $1/2$ | 3 | $\sim-2.347\,10^{-5}$ |
| 1 | 8 | $1/2$ | 4 | $\sim-4.613\,10^{-8}$ |
| 1 | 10 | $1/2$ | 6 | $\sim-3.598\,10^{-11}$ |
| 1 | 12 | $1/2$ | 7 | $\sim-3.217\,10^{-14}$ |
| 1 | 16 | $1/2$ | 11 | $\sim-2.050\,10^{-23}$ |
| 1 | 20 | 1 | 29 | $\sim-4.406\,10^{-51}$ |

For the first row, use $(3,-64,25)$ at times $1/2,3/2,5/2$. With $m(k)=k^{-8}[1-(1+k^2)e^{-k^2}]^2$ the collected form is $9m(1)-384m(2)+4246m(3)-3200m(4)+625m(5)$. Lean proves directly from the exponential function that it is at most $-100151644/10^{10}$. This is the unnormalized sum with $B$ divided out. Its interval arithmetic inside Lean uses Mathlib's proved bounds on $e$. The other seven explicit signs are rational computer certificates. The all-grids conclusion uses the written moment theorem above. [Generated Lean proof](FlowReflection.lean)

### Ordered transfer to compact Wilson regulators

Fix $s,T,h$ first, including the finite test supplied by the theorem. Put the center of each reading on a sliced even periodic $SU(2)$ cube at the nearest lattice time to $r(T/2+jh)$; flow for $sr^2$ lattice units. Use centered real plaquette deficits. At each **fixed** $r$ apply the earlier cube tangent and fixed-time Lie–Euler argument as $\ell=\beta\to\infty$. Then send $r\to\infty$ in the Gaussian Brillouin-zone expression, after multiplying the connected form of the scaled deficits by $r^8$. The positive constant differs from the magnetic energy sum but the profile is the same. Dominated convergence with the full heat factor works at every one of the finitely many rounded separations. Consequently there are finite values of $r$ and all sufficiently large even $\ell=\beta$ at that $r$ with a strictly negative reflected form for the original bounded plaquette functions. Centering uses a constant, admissible at each regulator. The proof gives eventual existence with test-dependent cutoffs. It makes no uniform estimate on a specified interacting bare trajectory. G4 independently confirmed the partition powers and fixed-flow $L^p$ estimate and reported a separate short-buffer, fixed-flow-time witness. [Cube argument](../spatial-flow/wilson.md) · [G4 review](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7097228864)
