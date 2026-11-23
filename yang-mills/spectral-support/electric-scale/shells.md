# Sharp low-shell leakage and subsequential electric profiles

Use normalized Haar measure on each link, $x_p=\tfrac12\operatorname{Tr}U_p$, $\epsilon=\langle1-x_p\rangle$, $K=\langle-\Delta_e\rangle$ for the unit round $S^3$. On a periodic cubic box, symmetry of the positive vacuum and equal face and link counts give
$$K/4+g\epsilon=E_0/(N_e\kappa)\le B(g)=\min(g,17\sqrt g/8+3/16).$$
Here $g=\lambda/\kappa$. At the bare matching $g=\beta^2/2$. The joint energy budget is stronger than using each of the two individual estimates. [A4's trial and metric convention](../../observable-normalization/hamiltonian-variance/) · [Bare Hamiltonian matching](../../observable-normalization/energy-density/spatial-limit.md)

## An uncertainty inequality at each incident plaquette

For any normalized state on the full link product write $a_n=\|\Pi_{e,n}\psi\|$, with $n=2j\ge0$ the Peter–Weyl shell and $a_{-1}=0$. Fix the other links and use the plaquette holonomy as the one-link coordinate. Left and right group translations, and inversion when needed, preserve Haar and the electric shells. In polar coordinates on $S^3$, the degree $n$ spherical harmonics are proportional to $(\sin\theta)^\ell C_{n-\ell}^{\ell+1}(\cos\theta)Y_{\ell m}$, $0\le\ell\le n$. Multiplication by $x=\cos\theta$ couples successive $n$ at fixed $\ell,m$. The normalized Gegenbauer recurrence gives the upward coefficient
$$\frac12\sqrt{1-\frac{\ell(\ell+1)}{(n+1)(n+2)}}.$$
For example this follows by inserting $k=n-\ell$, $\alpha=\ell+1$ in the off-diagonal Jacobi coefficient $\tfrac12\sqrt{(k+1)(k+2\alpha)/[(k+\alpha)(k+\alpha+1)]}$. The coefficient is $1/2$ throughout the radial sector. The fiber operator norm is consequently $1/2$, uniformly in the spectators. Cauchy–Schwarz and the sum of the two adjacent blocks give
$$\langle x_p\rangle\le\sum_{n\ge0}a_na_{n+1},\qquad D=\sum_{n\ge0}(a_n-a_{n-1})^2\le 2\epsilon.$$
The sums converge by $\sum a_n^2=1$. [Gegenbauer recurrence](https://dlmf.nist.gov/18.9) · [Orthogonality and norms](https://dlmf.nist.gov/18.3)

Keep the first $J+1$ terms of $D/2$. The tridiagonal matrix has entries $-1/2$ between neighbors, diagonal $1$ except for $1/2$ at the right endpoint. Its positive ground vector is $u_n=\sin((n+1)\theta)$, $\theta=\pi/(2J+3)$, with $u_{-1}=0$ and $u_{J+1}=u_J$. Its eigenvalue is $1-\cos\theta$. One can prove minimality by summing the squares $u_nu_{n+1}(a_n/u_n-a_{n+1}/u_{n+1})^2$ with the endpoint terms. Thus
$$\Pr(n\le J)\le\frac{\epsilon}{1-\cos(\pi/(2J+3))},\qquad
\Pr(n\ge k)\le\frac{4B(g)}{k(k+2)}\quad(k\ge1)$$
for the vacuum; the first inequality holds for every state. The second uses $K=\sum n(n+2)a_n^2$. The first constant is best possible as a one-link form inequality. Use radial character coefficients $u_n$ through $J$, then decrease linearly to zero over $L$ more edges. Both sides scale quadratically before normalization and the excess in $D$ is $u_J^2/L$. No assertion of saturation by the interacting vacuum is needed.

A state *supported* on $0,\ldots,J$ also has $a_{J+1}=0$. Its optimal lower bound on $\epsilon$ is $1-\cos(\pi/(J+2))$ by the two-Dirichlet-end matrix. Replacing the leakage constant by that number for general states fails. At $J=0$ normalized radial amplitudes $(2,1)/\sqrt5$ give $p_0=4/5$ and $\epsilon=3/5$.

## Compactness along spatial refinement

Let $h=g^{-1/4}$. Put $b_h(y)=a_n/\sqrt h$ on $[nh,(n+1)h)$, and let $f_h$ linearly interpolate $f_h(0)=0$, $f_h((n+1)h)=a_n/\sqrt h$. Direct integration gives
$$\|b_h\|_2=1,\quad \|b_h-f_h\|_2^2=D/3,\quad
\|f_h'\|_2^2=D/h^2,\quad \|y b_h\|_2^2\le h^2(K+1).$$
As $g\to\infty$ the energy inequality bounds the derivative and the moment uniformly, and $D=O(h^2)$. Local Rellich compactness and the moment tail estimate give a subsequence with both amplitudes strongly convergent in $L^2(0,\infty)$. Their common limit $f\ge0$ has norm one, zero trace at zero, and belongs to $H^1_0$. Strong convergence gives $b_h^2\to f^2$ in $L^1$. Replacing a point at $hn$ by its cell changes any bounded Lipschitz test by at most its Lipschitz constant times $h$. Hence the actual label measures converge weakly on this subsequence to $f(y)^2dy$. No mass escapes to infinity or collapses at the origin. This applies to an arbitrary sequence of volumes and couplings with $g\to\infty$.

Lower semicontinuity of the derivative and of the moment (first truncate $y$) and the joint energy budget imply, along the chosen subsequence,
$$\tfrac12\|f'\|_2^2+\tfrac14\|yf\|_2^2\le\liminf\frac{E_0}{N_e\kappa\sqrt g}\le17/8.$$
In particular the Dirichlet half-line harmonic oscillator gives the lower bound $3/(2\sqrt2)$ on the liminf of the rescaled energy per link on **every** sequence. Take a subsequence realizing the liminf before the compactness extraction. The spectral constant follows by odd reflection and the first odd Hermite eigenfunction of $-\tfrac12\partial_y^2+y^2/4$. Neither uniqueness of the rescaled density nor convergence of the four-dimensional dynamics follows from this estimate.
