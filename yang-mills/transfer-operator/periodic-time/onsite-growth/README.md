# All-order growth of the bounded on-site scalar in the two-mass control

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

C4’s light-mode overlap threshold for the time-axis two-point function also characterizes **all orders and all distinct lattice sites** for the specified bounded on-site field. Fix $K\ge0$ and write $d=M/m\to\infty$ with $M\to0$. For C4’s two-mass Gaussian action the following are equivalent.

1. The light weight satisfies $w\ge c d^{-K}$ eventually for some $c>0$.
2. The normalized centered moments of the on-site scalar satisfy Z4’s H3(b) with field exponent $2+K$. One may take factorial exponent 6, independently of $K$ and of the number of points.

There is a second distinction at fixed physical separation. The weaker condition $\log(1/w)=o(d)$ already gives convergence of every fixed-order off-diagonal moment to that of the **negative normalized Wick square of three independent free fields of mass one**. Thus $w=e^{-\sqrt d}$ has these same off-diagonal limits while violating every polynomial H3(b) bound. This statement concerns C4’s Gaussian control. Establishing comparable bounds for the Wilson site scalar remains open. [C4’s action, definitions and two-point criterion](../../../central-quotients/tangent-curvature/periodic-limit/local-overlap/README.md) · [Z4’s H3(b)](../../../z4/attempt/reviews/c1-OS/THEOREM_S.md)

## From the axis to a covariance bound at each endpoint

Use C4’s on-site field $F_i=e^{-\lambda |X_i|^2}-\mathbb E e^{-\lambda |X_i|^2}$, $\lambda>0$. Its three colors are independent with common covariance $B_{ij}=wG_m(n_i-n_j)+(1-w)G_M(n_i-n_j)$, now with **scalar** propagators (no curl numerator). Let $V=B_{ii}$ and $Z^2=\mathbb E F_0 F_{Ne_0}$ for the nearest even unit clock $N=1/m+O(1)$. Set $x_i=mn_i$, $r_i=\min(1,\min_{j\ne i}|x_i-x_j|)$.

For distinct sites, choose the largest displacement coordinate as Euclidean time, so its magnitude $l$ is at least half the Euclidean lattice distance. Taking the modulus of the spatial Fourier phase gives $|G_a(n_i-n_j)|\le G_a(le_0)$. Splitting the time exponential in half and bounding the remaining integral by the massless one gives $G_a(le_0)\le C l^{-2} e^{-al/2}$ for $l\ge1$. Here $\omega_0(p)\gtrsim |p|$ and $1/\sinh\omega_0(p)\lesssim1/|p|$ on the momentum cube. Under condition 1 the clock reading gives $Z\asymp wm^2$ by C4’s scalar calculation. Writing $u=ml$, division by $Z$ thus bounds the covariance by $C u^{-2}(1+d^K e^{-du/2})$, at most $C\max(1,u^{-(2+K)})$. Also $|B_{ij}|\le V\le C$. Both endpoints obey the pair bound, so with $a_i=\min(1,\sqrt Z\,r_i^{-(2+K)/2})$,
$$
 |B_{ij}|\le C\min(a_i^2,a_j^2)\le C a_i a_j .
$$

## A centered even insertion requires two covariance endpoints

For $k\ge2$ attach a parameter $t_i\in[0,1]$ to every site. Preserve all diagonal variances and replace off-diagonal $B_{ij}$ by $t_i t_j B_{ij}$ in each color. This is the covariance of $t_i X_i+\sqrt{1-t_i^2}\,Y_i$ with independent $Y_i$ of variance $V$ per color. The covariance is positive definite throughout the cube: the original scalar lattice density is strictly positive, and a nonzero finite linear combination on distinct sites has positive variance. Let $P(t)$ be the expectation of the product of the $k$ centered insertions. When $t_i=0$ the insertion is independent and centered, so $P=0$. It is even in each $t_i$ by sign symmetry of the insertion. Integrating the one-variable Taylor remainder at every site gives
$$
 P(1,\ldots,1)=\int_{[0,1]^k}\prod_i(1-t_i)\, \partial_1^2\cdots\partial_k^2 P(t)\,dt .
$$
Covariance differentiation for a symmetric off-diagonal variable gives one field derivative at each endpoint. Each $t_i$ derivative can create one edge $ij$ with coefficient $t_j B_{ij}$ and a field derivative at both $i$ and $j$ in one of three colors. Alternatively it can differentiate a remaining endpoint factor $t_i$ of a previously created edge. In either case each differentiation uses a distinct endpoint at its own vertex. After $2k$ differentiations each term has $k\le h\le2k$ edges counting multiplicity, with degree at least two at every vertex. This argument needs no sign condition on the covariance or the product of derivatives. [Voigtlaender, A General Version of Price’s Theorem](https://arxiv.org/abs/1710.03576)

There are at most $(5k)^{2k}$ differentiated terms if repeated occurrences are counted individually: each step has at most $3(k-1)$ new-edge choices and at most $2k$ unused endpoint factors. Each term contributes covariance factors bounded by $C^{2k}\prod_i a_i^2$ after enlarging $C\ge1$. The expectation of the product of site derivatives is bounded by $C_\lambda^k(4k)!$: on the complex unit polydisc about any real color vector the centered insertion has modulus at most $e^{3\lambda}+1$, and Cauchy’s bound gives the multi-index factorial at each site. The total derivative order is $2h\le4k$. Since $(4k)!\le4^{4k}(k!)^4$ and $k^k\le e^k k!$, division by $Z^k$ yields
$$
 \left|Z^{-k}\mathbb E\prod_{i=1}^k F_i\right|
 \le C^k(k!)^6\prod_i r_i^{-(2+K)}.
$$
The one-point moment vanishes. Conversely the asserted bound at order two and time $n$ nearest $1/M$ requires $w\gtrsim d^{-K}$ by C4’s moving-separation test: there the unnormalized connected reading is comparable to $M^4$, and the unit-clock reading is at most $C m^4(w+d^{1/2}e^{-d})^2$. This proves equivalence with the same field exponent.

## Fixed off-diagonal limits under subexponential loss of overlap

Let $m n_i\to x_i$ with fixed distinct physical $x_i$. Write $g(x)$ for the Euclidean massive scalar propagator in four dimensions with mass one. For a coordinate chosen as time, its Fourier representation is
$$
 g(x)=\int \frac{e^{ip\cdot x_\perp-|x_0|\sqrt{1+|p|^2}}}{2\sqrt{1+|p|^2}}\,\frac{d^3p}{(2\pi)^3},\qquad x_0\ne0 .
$$
Time can be chosen along any nonzero component; the four-dimensional rotational symmetry follows equivalently from the Fourier multiplier $(1+|p|^2)^{-1}$ in four dimensions. In the light lattice propagator substitute spatial momentum $p=mq$; for a nonzero limiting time component the rescaled integrand is dominated by $C e^{-c|q|}/|q|$. The heavy contribution is at most $C m^2 e^{-c d}$ by the previous axis estimate. Thus with $\epsilon=wm^2$, the off-diagonal covariances satisfy $B_{ij}/\epsilon\to g(x_i-x_j)$ whenever $\log(1/w)=o(d)$. The same calculation gives $B_{0,N}/\epsilon\to g(e_0)>0$. The one-site variance tends to the massless lattice variance $V_0$ by dominated convergence.

To see which terms survive, multiply all off-diagonal covariances by a single parameter $s$ from 0 to 1, keeping $V$ fixed. Expand the product expectation in $s$ through degree $k$ using the same covariance derivative formula. The remainder is $O_k(\epsilon^{k+1})$ since all off-diagonal entries are $O_k(\epsilon)$ and site derivatives are uniformly bounded at fixed order. At zero the sites are independent. Isolated vertices have zero mean, and degree-one vertices have zero expected derivative. At degree $k$ every surviving vertex therefore has degree two. Its expected derivative is
$$
 \mathbb E\,\partial_a\partial_b F_i=-2\lambda(1+2\lambda V)^{-5/2}\delta_{ab}.
$$
These derivatives coincide exactly with those of $c_V (|X_i|^2-3V)$, $c_V=-\lambda(1+2\lambda V)^{-5/2}$. Repeating the expansion with that quadratic polynomial reproduces the whole leading coefficient by Wick pairing, with no within-site pairs and no higher powers. This also gives $Z/\epsilon\to\sqrt6\,|c_{V_0}|g(e_0)$. Hence the limit of each normalized moment equals the off-diagonal moment of
$$
 -\frac{\sum_{c=1}^3 :\!\varphi_c^2\!:}{\sqrt6\,g(e_0)} ,
$$
where the three mass-one fields have covariance $g$. At $w=e^{-\sqrt d}$, times near $1/M$ still violate H3(b) for every finite field exponent by the two-point lower test. No exchange of the fixed-configuration limit with integration through a coincidence is used. [Execution record](checks.md)
