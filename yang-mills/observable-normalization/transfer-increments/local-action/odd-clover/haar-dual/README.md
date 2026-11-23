# A covariance lower bound for every smearing of the Wilson pseudoscalar

Director A4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Use the **raw** site density $q=P/\beta$ of the [odd-clover theorem](../README.md), defined directly by the same loop polynomial also at $\beta=0$. For any finite real smearing $f$ on $\mathbb Z^4$ put $Q_f=\sum_x f(x)q(x)$. In each isotropic even-periodic thermodynamic limit,
$$
 \operatorname{Var}_\mu Q_f\ge
 \frac{9}{256\cdot48\cdot 7^4}\, e^{-76\beta}\|f\|_2^2
 \qquad(\beta\ge0).
$$
At sufficiently large coupling the lower bound improves to $c\beta^{-3}\|f\|_2^2$ with a state-independent $c>0$. Equivalently the translation spectral measure of the raw Euclidean covariance dominates the indicated multiple of normalized Haar measure on the Brillouin torus. The bound holds for oscillating and spatially localized tests alike. It controls a local variance contribution and leaves the transfer mass gap open.

At product Haar measure ($\beta=0$) one has the exact identity $\operatorname{Var}Q_f=(9/256)\|f\|_2^2$. As $\beta\downarrow0$ the raw bulk susceptibility satisfies $\chi_{\mathrm{bare}}=9/256+O(\beta)$, uniformly over the states. The estimates below require only the finite Wilson specifications, elementary Haar integration, and for the bulk upper bound, site reflection positivity.

## Haar orthogonality of the figure-eight loops

At each site there are 48 summands $h_\alpha$ in $q$, one for each of three plane pairings and 16 sign choices. Include their coefficients $\pm1/16$ in $h_\alpha$. Its support $E_\alpha$ consists of the eight distinct edges of two elementary faces meeting only at their root. Distinct summands, including at different sites, have distinct supports. The root is the unique vertex of degree four, and deleting it separates the two three-vertex paths, determining the two squares and their signs of displacement. With the order of axes in each face prescribed, this specifies the summand.

At fixed exterior links, Haar integration in any one of these eight edges annihilates $h_\alpha$ since its dependence on that link is linear in the four real quaternion coordinates. Therefore integration against $h_\alpha$ over $E_\alpha$ kills every other summand, even for arbitrary exterior values. On the eight independent Haar links the two face holonomies are independent Haar quaternions. Their imaginary coordinates have second moment matrix $I_3/4$ by spherical symmetry. Thus the Haar squared norm of a single weighted summand is $v=3/4096$ and $v_0=48v=9/256$. This computes the site covariance at $\beta=0$, including the normalization at contact. It also computes the cube covariance after redistribution, since each summand belongs to exactly one cube and 48 belong to each cube.

## An exactly local dual at every coupling

Let $\rho_\alpha$ be the conditional density of the links of $E_\alpha$ relative to eight normalized Haar measures, given their exterior. The continuous finite Wilson specification is valid in the periodic limit as in the [three-link proof](../local-variation.md). Only action plaquettes touching these edges enter the normalized density. There are 38 such plaquettes. The eight edges have 48 incidences in all. Each of the two chosen faces accounts for three repeated incidences, and the four cross-plane pairs of incident edges at the root each produce one further repetition. Define $g_\alpha=h_\alpha/\rho_\alpha$ and $G_x=\sum_{\alpha\text{ at }x}g_\alpha$. These functions are bounded at every fixed coupling and gauge invariant. The normalized density is determined by links within sup distance two of the root.

Conditional integration cancels $\rho_\alpha$ exactly. In particular $\mu[g_\alpha\mid E_\alpha^{\rm exterior}]=0$ and
$$
 \mu[h_\gamma g_\alpha]=v\,\mathbf1_{\gamma=\alpha},\qquad
 \mu[q(y)G_x]=v_0\,\mathbf1_{x=y}.
$$
Moreover $\mu[G_xG_y]=0$ for $|x-y|_\infty>3$. For each $\alpha$ at $x$, every $g_\gamma$ at such a $y$ is measurable outside $E_\alpha$. This exact finite range concerns the auxiliary dual's covariance.

Each of the 38 deficits belongs to $[0,2]$. The normalizer relative to product Haar is at most one, hence $\rho_\alpha\ge e^{-76\beta}$. Conditioning in $E_\alpha$ gives $\mu[g_\alpha^2]\le e^{76\beta}v$. By Cauchy–Schwarz, $\mu[G_x^2]\le48v_0e^{76\beta}$. Summing the finite-range covariance and using $2|f_x f_y|\le f_x^2+f_y^2$ gives
$$
 \operatorname{Var}\sum_x f_xG_x\le7^4\,48v_0e^{76\beta}\|f\|_2^2 .
$$
Its exact covariance with $Q_f$ is $v_0\|f\|_2^2$. Cauchy–Schwarz proves the first variance floor. By complexification and approximation of nonnegative continuous torus tests by squares of trigonometric polynomials, the same form inequality gives the stated measure domination.

## A linear error bound near the Haar value

Uniformly for small $\beta$, the finite specification gives $\rho_\alpha=1+O(\beta)$, so $g_\alpha=h_\alpha+O(\beta)$ in sup norm. On any fixed finite link set the conditional density relative to Haar similarly lies between $\exp(-2n\beta)$ and $\exp(2n\beta)$, with $n$ the number of action faces touching that set. Consequently each of the finitely many dual covariances with $|x-y|_\infty\le3$ equals its product Haar value plus $O(\beta)$, with a uniform constant. All other dual covariances vanish exactly. This gives
$$
 \operatorname{Var}\sum_x f_xG_x\le(v_0+C\beta)\|f\|_2^2,\qquad
 \operatorname{Var} Q_f\ge\frac{v_0^2}{v_0+C\beta}\|f\|_2^2
                         \ge(v_0-C\beta)\|f\|_2^2 .
$$
For the matching bulk upper bound use the [even-tile infimum](../tiling.md) for the raw cell density, with fixed side two. At $\beta=0$ its box variance is $2^4 v_0$ by support orthogonality. This finite box is a bounded cylinder observable and its variance changes by $O(\beta)$ under the local density bound. The site and cube bulk limits agree, proving the claim about $\chi_{\mathrm{bare}}$.

## Polynomial bound for every smearing at weak coupling

Apply the [three-link mixed derivative](../local-variation.md) to the *scaled* sum $\beta Q_f$, extending $f$ by zero off its support. For a triple rooted at $x$, all possibly affected sites lie in a fixed finite neighborhood $x+B$. The cubic coefficient at identity is supported only at $x$. On the good exterior event of probability at least $1/2$, the inner product against the centered cubic chart test on the uniform cube is therefore
$$
 -\frac{f(x)}{432\sqrt\beta}+
 O_M\!\left(\beta^{-1}\sum_{y\in x+B}|f(y)|\right).
$$
This follows by the same bounded Taylor remainder and coefficient continuity term by term, with the fixed choice of $M$. For one residue class modulo 12 in each coordinate, condition on the exterior of its finitely many triples rooted in the support of $f$. Each local interaction and each site charge monomial meets at most one chosen triple. Conditional independence adds their variances. Uniform minorization, the cube-test Cauchy–Schwarz bound, $(a+b)^2\ge a^2/2-b^2$ and the marginal good-event probabilities give
$$
 \operatorname{Var}(\beta Q_f)\ \ge\
 c\beta^{-1}\sum_{x\text{ chosen}}f(x)^2
 -C_M\beta^{-2}\sum_{x\text{ chosen}}
          \left(\sum_{y\in x+B}|f(y)|\right)^2.
$$
Sum over all $12^4$ residue classes. The convolution on the right has squared norm at most $|B|^2\|f\|_2^2$. Absorb the $O_M(\beta^{-2})$ loss into the leading term for sufficiently large $\beta$, then divide by $12^4\beta^2$. This yields the raw $c\beta^{-3}\|f\|_2^2$ bound with the same threshold for every smearing. In particular no smoothness, sign or size condition on $f$ is needed. [Lean and guest checks](checks.md)
