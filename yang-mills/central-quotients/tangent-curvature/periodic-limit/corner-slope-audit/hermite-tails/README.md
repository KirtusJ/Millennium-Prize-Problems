# Gaussian tail probabilities for the energy slopes seen by a square Wilson loop

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Let $\nu$ be the square-weighted law of the first magnetic derivatives of the electric energy levels, with the normalization in A4’s calculation. Let $n=\ell$ be the square side in fine links, and $\gamma=N(0,1/4)$. Write $\bar\gamma(x)=\gamma([x,\infty))$. As $n\to\infty$,
$$
\sup_{0\le x\le b_n}\left|\frac{\nu([x,\infty))}{\bar\gamma(x)}-1\right|
=O\!\left(\frac{1+b_n}{\sqrt n}\right)
\quad\text{whenever }0\le b_n=o(\sqrt n).
$$
Thus the Gaussian gives the rare-event probability itself to vanishing relative error throughout that range. Farther out, at each fixed fraction $0<u<1$,
$$
\log \nu([u\sqrt n,\infty))=-2u^2 n-\tfrac12\log n+O_u(1).
$$
The same estimate holds on the interval $[u\sqrt n,u\sqrt n+4]$ and for its reflection. The constants are uniform in the allowed even box sides $L\ge4n$ and temporal couplings $g>0$. The magnetic derivative is taken separately in each finite box. [A4’s electric-cluster calculation](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/d4f8b7f2e209db4532086579a4ff5c00df8183fb/yang-mills/observable-normalization/transfer-increments/electric-lag/corner-spectrum/README.md) · [B4’s finite-side proof](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/b0d0cad842ffc2758c482605eebc6da5af059dfb/yang-mills/observable-normalization/transfer-increments/electric-lag/corner-spectrum/b4-review/README.md) · [Earlier moment bounds](../README.md)

## Why a finite list of moments bounds a rare probability

B4’s range gives equality of even moments through degree $2n-2$. Both laws are symmetric, giving equality through degree $2n-1$. No additional Wilson moment is assumed. Let $t_1<\cdots<t_n$ be the zeros of $\mathrm{He}_n(2s)$, using the probabilists’ Hermite convention. Let $w_i$ be the positive $n$-node Gaussian quadrature weights for $\gamma$, normalized to sum to one, and $W_i=\sum_{k\le i}w_k$, $W_0=0$. The nodes and weights depend only on the matched moments. For either measure $\mu$ the Chebyshev–Markov–Stieltjes inequalities give
$$
W_{i-1}\le F_\mu(t_i^-)\le F_\mu(t_i)\le W_i .
$$
These weak inequalities include a measure supported exactly on the quadrature nodes. One can also obtain the endpoint conventions by mixing a positive fraction of $\gamma$ into $\mu$, applying the separation inequalities to the mixture and its reflection, and taking that fraction to zero. The mixture preserves every matched moment. [Ismail, §2.4, separation and quadrature](https://api.pageplace.de/preview/DT0400.9781107109322_A23760161/preview-9781107109322_A23760161.pdf) · [Hürlimann, Theorem 4.1](https://link.springer.com/article/10.1186/s13660-015-0709-1) · [NIST DLMF, Gaussian quadrature](https://dlmf.nist.gov/3.5#vi)

For $t_i\le x<t_{i+1}$ with $2\le i\le n-2$, applying the bounds first to one law and then to the other gives
$$
F_\gamma(t_{i-1})\le W_{i-1}\le F_\nu(x^-)\le F_\nu(x)
\le W_{i+1}\le F_\gamma(t_{i+2}).
$$
The slack is controlled by the distance to a nearby Hermite zero on either side of $x$. This avoids estimating individual quadrature weights or assuming a continuous Wilson slope law.

## How far the threshold moves

For $p(s)=\mathrm{He}_n(2s)$ the Hermite equation is $p''-4sp'+4np=0$. Thus $v(s)=e^{-s^2}p(s)$ satisfies
$$
v''+(4n+2-4s^2)v=0.
$$
Fix $0<\epsilon<1$. On $|s|\le(1-\epsilon/2)\sqrt n$ the coefficient is strictly greater than $k^2=4n[1-(1-\epsilon/2)^2]$. By Sturm comparison with a sine wave, each open interval of length $h=\pi/k$ inside that band contains a zero. Indeed, if $v$ had constant positive sign on such an open interval, compare with the positive sine arch $w$. Integrating $(v'w-vw')'=(k^2-(4n+2-4s^2))vw<0$ gives a contradiction because the endpoint difference is $k$ times the sum of the two nonnegative endpoint values of $v$. The negative-sign case follows by negation.

For all sufficiently large $n$ and $|x|\le(1-\epsilon)\sqrt n$, two consecutive test intervals of length $h$ fit on each side of $x$ inside the larger band. Hence $t_{i-1}\ge x-2h$ and $t_{i+2}\le x+2h$ in the preceding bracket, including when $x$ is itself a node. With $\Delta=2h$ we obtain
$$
\bar\gamma(x+\Delta)\le\nu((x,\infty))\le\nu([x,\infty))
\le\bar\gamma(x-\Delta),\qquad \Delta=O_\epsilon(n^{-1/2}).
$$
[NIST DLMF, classical differential equations](https://dlmf.nist.gov/18.8) · [Boyer, Sturm comparison, Appendix A.5](https://www.math.univ-toulouse.fr/~fboyer/_media/enseignements/m2_lecture_notes_fboyer.pdf)

The Gaussian density is proportional to $e^{-2x^2}$. Integrating it over $[x,x+(1+x)^{-1}]$ shows that the logarithmic derivative of its survival function is bounded in magnitude by $C(1+x)$ for $x\ge0$; it is also bounded on $[-1,0]$. Therefore throughout the positive inner band
$$
\left|\log\frac{\nu([x,\infty))}{\bar\gamma(x)}\right|
\le C_\epsilon(1+x)/\sqrt n .
$$
The same holds for the strict tail. Taking $\epsilon=1/2$ gives the relative estimate in the opening statement. Taking $x=u\sqrt n$ and using the Gaussian tail estimate $\bar\gamma(x)\asymp e^{-2x^2}/(1+x)$ gives the second statement. For $x\ge1$ the upper Gaussian bound follows by integrating $e^{-2x^2-4x(s-x)}$ on $s\ge x$, and the preceding short interval gives the lower bound. Subtract the strict tail at $x+4$ to obtain the window result: its ratio to the lower bound for the tail at $x$ decays exponentially in $x$ when $x=u\sqrt n$. Exact symmetry transfers the bounds to negative slopes.

## What the known moments leave undetermined

The $n$-node quadrature measure $\sum_i w_i\delta_{t_i}$ and the continuous Gaussian are two positive symmetric measures with the same moments through $2n-1$. The quadrature nodes are the eigenvalues of the zero-diagonal Jacobi matrix with off-diagonal entries $\sqrt h/2$, $1\le h\le n-1$. Its maximum row sum is at most $\sqrt{n-1}$. Consequently the discrete measure gives exactly zero to $[\sqrt n,\infty)$, whereas the Gaussian gives it positive weight. This identifies a limit on deductions from this moment list. Whether the Wilson slope law has weight there is a question about its additional structure. [NIST DLMF, Jacobi matrix and quadrature nodes](https://dlmf.nist.gov/3.5.E31)

### Including B4’s first non-Gaussian moment

B4 has since computed the first collision of the corner diagrams. For the standardized slope $Y=2s$ the order-$2n$ moment is $(2n-1)!!-d_n$, where $d_n=4\binom{2n}{n}/4^n$. Even this additional datum, together with exact symmetry, permits either zero or positive weight above $\sqrt n$ in slope units. [B4’s first-collision formula](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/5e5c1bda792c0dc214ad9020df661795d2c677a4/yang-mills/observable-normalization/transfer-increments/electric-lag/corner-spectrum/first-collision/README.md)

To see this, take a zero-diagonal symmetric tridiagonal matrix of size $n+1$ in **standardized** coordinates. Its off-diagonals are $\sqrt1,\ldots,\sqrt{n-1}$ and $\sqrt{n-d_n/(n-1)!}$. The last entry is positive: $d_2=3/2$ and $d_{n+1}/d_n=(2n+1)/(2n+2)<1$. The spectral law of the first coordinate has all the required moments. In its walk expansion the last edge first contributes at length $2n$, on the unique walk straight out and straight back. Its original contribution of $n!$ is reduced by precisely $d_n$. All odd moments vanish by sign symmetry. Every row sum is strictly smaller than $2\sqrt n$, so half the matrix has no spectral weight at or past $\sqrt n$.

Now append one row and column with zero diagonal and a new off-diagonal $4\sqrt n$. A walk from the first coordinate needs $2n+2$ steps to cross that edge and return. Hence every moment through $2n+1$ still agrees, including B4’s correction. The last two coordinates give a Rayleigh quotient $4\sqrt n$ for the enlarged matrix. Every eigenvector has nonzero first coordinate, since all off-diagonals are positive and the eigenvector recurrence would otherwise force the whole vector to vanish. After rescaling by $1/2$, the new law therefore has positive weight at or above $2\sqrt n$. Both constructed laws are comparison measures. Deciding which slopes the Wilson transfer actually realizes beyond the cutoff requires physical information beyond these moments.

The spectrum here belongs to the square’s excited perimeter cluster at zero magnetic coupling. Uniform control at finite magnetic coupling and a lower bound on the continuum mass gap remain open.

## Reproducible controls

Three linked PCP OS guests checked the 91 coefficient identities for the scaled Hermite equation through degree 12, the open and closed distribution bounds on a three-node quadrature and a different moment-matched atomic law, and 135 positive leading minors at the proposed cutoff in dimensions 2 through 16. The last guest also compared both corrected Jacobi matrices against B4’s exact moment on sides 2, 3 and 4. For the atomic test in standardized coordinates, the three-node law has mass $2/3$ at zero and $1/6$ at each of $\pm\sqrt3$. The second law puts $9/22$ at each of $\pm1/\sqrt3$ and $1/11$ at each of $\pm2$. The laws agree through degree five but differ at individual thresholds. The generated Lean proof also checks a polynomial majorant for the signed-threshold test on the entire real line. With threshold zero and nodes scaled to $-1,0,1$, that majorant is $(2z^4+z^3-4z^2-3z+4)/4$. It dominates the indicator of $(-\infty,0]$, including its jump. Lean accepted four declarations. The verifier rejected an invalid delegation and three altered declarations. The general quadrature and tail bounds are proved above. [Native workers](worker.c) · [Replay](verify.py) · [Lean declarations](HermiteTail.lean)
