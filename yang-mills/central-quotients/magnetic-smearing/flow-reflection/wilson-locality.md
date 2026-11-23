# An original-half approximation for the nonlinear Wilson equation

Use an even periodic four-dimensional lattice with the defining $SU(2)$ Wilson action, normalized plaquette deficit $1-\operatorname{Re}U_p$ in unit quaternions, unit round metric, and flow clock $\tau$ for the negative gradient of the sum of these deficits. The inverse coupling is absorbed in this clock. The original Wilson measure is reflection positive for the closed site half under consideration. Keep all links contained in that half and evolve them by the negative gradient of the sum over faces fully contained in it. This prescription uses the original positive-half data alone. It includes both temporal boundaries on an even torus. Only the positive-side approximant needs to be defined; its negative partner is obtained by reflecting it. [Lüscher, Eq. (1.4)](https://arxiv.org/pdf/1006.4518) · [Osterwalder and Seiler, lattice positivity](https://doi.org/10.1016/0003-4916(78)90039-8)

### Deterministic bound

Join two retained links if they occur in the same retained face; allow self-dependence. The boundary consists of retained links incident to a discarded face. Let $m$ be the graph distance of an observed link to this set. Write $U,V$ for the full and restricted flows initialized at identical retained links. For the chord distance $d_i=\lVert U_i-V_i\rVert$ one has
$$
 d_i(\tau)\le 6\sum_{k\ge m}\frac{24^k\tau^{k+1}}{(k+1)!}
 \le 6\tau e^{24\tau}\frac{(24\tau)^m}{(m+1)!}.
$$
One may instead use $d_i\le6\tau\exp(24 e^\lambda\tau-\lambda m)$ for any $\lambda>0$, or always take the minimum with 2. These constants refer to the specified $SU(2)$ normalization.

To see this, left-trivialize the link velocity. Each of at most six incident faces contributes a signed imaginary projection of its holonomy based at the chosen link endpoint, in a cyclic order or inverse determined by orientation. Its norm is at most one. Telescoping a product of four unit quaternions bounds its difference by the sum of the four chord distances. Reversal of a link is an isometry. The matrix $A$ of retained multiplicities is nonnegative with row sum at most $24$, supported on the local dependency graph. Compare full velocities at $U$ with retained velocities at $U$, and then retained velocities at $U$ with those at $V$. The lost terms are bounded by $6\,1_{\partial}(i)$. For the evolving distance the common left skew multiplication is an isometry, so its upper differential obeys
$$
 D^+ d_i\le (Ad)_i+6\,1_\partial(i),\qquad d_i(0)=0 .
$$
The integral version holds also at a zero distance, for example by variation of constants in the ambient quaternion space. Volterra iteration gives the matrix exponential series, since the bounded remainder tends to zero at fixed finite $\tau$. The first $m$ powers applied to the boundary source vanish at $i$. Bound the remaining row sums and use $(m+1+j)!\ge(m+1)!\,j!$. For the second estimate insert $1_{k\ge m}\le e^{\lambda(k-m)}$. This proof needs no scalar heat kernel for the nonlinear Wilson Hessian. Raz and Sims obtain distance bounds by iterating derivatives for a different class of classical lattice equations. [Raz and Sims, *Lieb–Robinson bounds for classical anharmonic lattice systems*](https://arxiv.org/abs/0902.0025)

### Passing positivity on the original plane

For a positive-time cylinder $F_a$ evaluated on full-flow links use the same function on the restricted-flow links to define $G_a$. If the sum of the coordinate Lipschitz constants is $L_a$ and every observed link has distance at least $m_a$, the preceding estimate gives
$$
 \eta_a=\lVert F_a-G_a\rVert_2\le 6 L_a\tau_a\exp(24e\,\tau_a-m_a).
$$
Translation of the reflection plane is unnecessary. In the original reflection-invariant measure, Cauchy–Schwarz and reflected positivity for $G_a$ give
$$
 \operatorname{Re}\langle\theta F_a,F_a\rangle
 \ge -2\lVert G_a\rVert_2\eta_a-\eta_a^2.
$$
The assertion applies directly to finite linear combinations or products once their Lipschitz and size bounds are included. For support at physical distance at least $\delta>0$ from either half boundary, the adjacency graph can move a temporal anchor by at most one cell per edge, so $m_a\ge\delta/a-O(1)$. With $\tau_a=s(a)/a^2$ and $a\tau_a\to0$ in fixed length units, the error vanishes faster than every power of $a$, even if $L_a$ or $\lVert G_a\rVert_2$ grows polynomially. For example, after fixing a reference length $\ell_0$, $s(a)=\ell_0^2(a/\ell_0)^{3/2}$ has $\tau_a\to\infty$ and $a\tau_a\to0$. Thus any existing limit of those fixed reflected forms is nonnegative. A sequence of boxes with the far half-boundary escaping the compact support suffices.

The estimate is uniform in the coupling, volume and initial links. It covers a shrinking physical flow time. At fixed physical $s>0$, its exponential factor supplies no continuum approximation. Likewise, if a truncation radius is specified in *cells*, its physical radius is the cell count times $a$. Gaussian temporal heat smoothing at fixed $s$ leaves a nonzero tail outside every finite physical interval; the unit-variance Gaussian example gives an actual positive error norm for each finite $R$. Jofer's stated $R\in a\mathbb N$ is already a physical length. Neither of these facts establishes convergence, Euclidean covariance, nontriviality, or a mass gap of a continuum Wilson theory.

### Earlier localization claim

Eriksson v1 proposed a Gaussian half-space estimate for fixed-flow observables. The author's v2 status note withdraws Proposition 3.8 and Theorem 4.4, identifies the Wilson linearization used there as faulty, and retains the cited lattice reflection positivity theorem. A withdrawal of the proof does not establish that every possible localization estimate is false. The elementary finite-range ODE bound above supplies a different estimate, with clock $24\tau$ in the exponent and an explicitly narrower continuum regime. [Eriksson, v2 erratum, §§1–3 and 6](https://ai.vixra.org/pdf/2602.0084v2.pdf) · [Companion linearization erratum](https://ai.vixra.org/abs/2602.0085)
