# Which flat tests detect a vanishing light-mode weight?

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

In C4’s two-mass Gaussian lattice control, let $m$ and $M$ be the light and heavy masses, with $M\to0$ and $d=M/m\to\infty$. For the centered, bounded on-site scalar and its unit-clock normalization $Z$, the following conditions are equivalent along the chosen sequence.

1. For some finite $K\ge0$ and $c>0$, the weight $w$ of the light mode satisfies $w\ge c d^{-K}$ eventually.
2. At each fixed order, the normalized lattice moments converge on every Schwartz test flat on all coincidence diagonals to the corresponding moments of the negative normalized mass-one Wick square of three independent colors.
3. The normalized two-point readings stay bounded on each fixed nonnegative, smooth, compactly supported test flat on the coincidence diagonal.

A test is **flat** if its value and all derivatives vanish there. If condition 1 fails, one fixed test in condition 3 has readings tending to infinity on a subsequence. The test may depend on the family of weights. For the particular family $w=e^{-\sqrt d}$, a fixed one-parameter collection of tests below has a sharp transition at $a=1/2$, including convergence at equality. These statements concern the Gaussian control and the flat test space used in the program. The corresponding Wilson estimates at its actual gap scale remain open. [Definitions, normalization and pointwise limit](../README.md) · [C4’s two-mass example](../../../../central-quotients/tangent-curvature/periodic-limit/local-overlap/README.md) · [Osterwalder–Schrader test space](https://doi.org/10.1007/BF01645738)

## A fixed test for an arbitrary superpolynomial subsequence

For condition 1 implying 2, use the parent all-order bound at exponent $2+K$. At fixed order $k$ it costs at most $C_k\delta^{-k(2+K)}$ near the diagonals, where $\delta$ is the smallest pair distance. Taylor expansion of a flat test at a closest diagonal supplies an arbitrarily high power of $\delta$ with a Schwartz weight, uniformly for $\delta\le1$. This gives an integrable majorant with mesh sums uniformly bounded and an $O_f(\eta)$ contribution for $\delta\le\eta<1$ after retaining one extra Taylor power. Exact coincidences contribute zero. Outside that region, the fixed-configuration limit holds for every convergent sequence of mesh points and hence uniformly on separated compacts. Mesh summation and the Schwartz tail give 2, which implies 3.

For the converse, set $A(d)=d^{1/2}e^{-d}$. The clock bound is $Z^2\le C m^4(w+A(d))^2$. At displacements $z$ with $Mz$ in a fixed small four-dimensional box around the unit time vector $e_0$, the one-color covariance is at least $cM^2$, uniformly in the mixture. In fact $G_M(z)/M^2$ and $G_m(z)/M^2$ converge uniformly on this box to the positive mass-one and mass-zero propagators respectively. Scale the time-exact Fourier integral by $p=Mq$, use $C|q|^{-1}e^{-c|q|}$ for domination and keep the spatial phase. Uniformity follows by taking a convergent subsequence in the box. The connected bounded reading is comparable to the square of this mixed covariance by the Gaussian determinant formula. At every separation it is nonnegative.

When 1 fails, select parameters indexed by $j\ge1$ with $d_j$ increasing at least fourfold and $w_j+A(d_j)\le d_j^{-2j}$; this follows by using a higher power first and taking $d_j$ large. Take $h$ nonnegative and smooth, supported in that box and equal to one on a smaller box. The box can be chosen so its dilation supports below are disjoint. Define
$$
 b(u)=\sum_{j\ge1} d_j^{-j} h(d_j u),\qquad f(x,y)=\chi(x)b(y-x),
$$
where $\chi\ge0$ is compactly supported and smooth with positive integral. Derivatives of order $q$ in the $j$th term are $O_q(d_j^{q-j})$ and the support has $|u|\asymp 1/d_j$. After division by any fixed power of $|u|$ these bounds still tend to zero. Extending by zero at the origin gives a single compactly supported smooth test flat on $x=y$. If permutation symmetry is desired, averaging $f(x,y)$ and $f(y,x)$ preserves its reading.

In physical mesh units the smaller separation box has four-volume of order $d_j^{-4}$. Each side contains order $M_j^{-1}$ points, so the mesh sum has the same lower bound independently of how fast $m_j$ tends to zero. The sum over the anchored first site tends to $\int\chi>0$. In this box the normalized reading is at least $c d_j^4/(w_j+A(d_j))^2$. Positivity lets us keep this box alone. Its contribution to the smeared reading is at least $c d_j^{-j}/(w_j+A(d_j))^2\ge c d_j^{3j}$. This disproves 3 and proves the equivalence. In particular convergence at every fixed distinct configuration can coexist with divergence on a single positive flat test.

## An explicit threshold for temporal flatness

Fix $w=e^{-\sqrt d}$. Write a relative displacement in physical coordinates as $(t,\mathbf x)$. Let $\chi$ be as above, and let $\theta(t)$ and $\psi(\mathbf x)$ be nonnegative smooth compact cutoffs, at most one and equal to one near zero. Use
$$
 f_a(x,y)=\chi(x)\,\theta(t)\psi(\mathbf x)e^{-a/|t|},\qquad a>0,
$$
extended by zero at $t=0$. For **$0<a<1/2$** the normalized two-point reading tends to $+\infty$. For **$a\ge1/2$** it converges to the mass-one Wick-square reading of this same test. The constant is specific to the time coordinate in gap units and the specified weight.

Here is the time-slice estimate underlying the threshold. Use $n\ge1$ for lattice time and $y=Mn$ in the rest of the calculation. With $\widehat p_i=2\sin(p_i/2)$ put $\cosh\omega=\cosh M+|\widehat p|^2/2$. Plancherel gives
$$
 S_M(n)=\sum_z G_M(n,z)^2=\int_{[-\pi,\pi]^3}\frac{e^{-2n\omega}}{4\sinh^2\omega}\frac{dp}{(2\pi)^3},\qquad z\in\mathbb Z^3 .
$$
For $y\ge1$, $S_M(n)\asymp M y^{-3/2}e^{-2y}$, with constants uniform for small $M$. Substitute $p=Mq/\sqrt y$. The exponent difference $n(\omega-M)$ is comparable to $|q|^2/(1+|q|/\sqrt y)$, by the exact dispersion and the bounds on $\widehat p$ in the representative cube. The upper integrand after scaling is bounded by $C\exp[-c|q|^2/(1+|q|)]$; a fixed unit ball gives the lower bound. For $y\le1$, the massless integral instead gives $S_M(n)\le C/n$ by $\omega\gtrsim|p|$ and $\sinh\omega\gtrsim|p|$.

The spatial cutoff preserves a fixed positive fraction in the dominant time range. Indeed $\sum_z |z|^2G_M(n,z)^2$ is the squared gradient integral of $e^{-n\omega}/(2\sinh\omega)$. Its logarithmic gradient has norm at most $C(n+1/M)|p|/M$ because $|\nabla\omega|\le C|p|/M$. With the same scaled majorant, the moment divided by $S_M(n)$ is at most $C y/M^2$ for $y\ge1$. The mean squared physical displacement is therefore at most $Cy/d^2$. On $y\asymp\sqrt d$ this tends to zero, so both cutoffs retain asymptotically the full time-slice mass there.

After the center-site sum, the physical separation volume $m^4$ cancels the $m^4$ in $Z^2\asymp w^2m^4$. The normalized heavy covariance squared, including the asymptotically unit coefficient $(1-w)^2$, thus contributes to the quadratic comparison an amount of order
$$
 w^{-2}(ad)^{-1/2}\exp[-2\sqrt{2ad}]
   =(ad)^{-1/2}\exp[(2-2\sqrt{2a})\sqrt d].
$$
To verify the order, for $y\ge1$ sum $M y^{-3/2}e^{-2y-ad/y}$ on the mesh $M\mathbb N$. The integral over the positive half-line equals $\sqrt{\pi/(ad)}\,e^{-2\sqrt{2ad}}$. The integrand is unimodal, so the absolute error of its full mesh Riemann sum is at most twice $M$ times the maximum. The maximum is $O_a(d^{-3/4}e^{-2\sqrt{2ad}})$ (differentiate its logarithm). For a lower bound restrict to $|y-y_*|\le d^{1/4}$ about $y_*=\sqrt{ad/2}$, where the exponent exceeds its minimum by at most a fixed constant, by $2y+ad/y-4y_*=2(y-y_*)^2/y$. This interval supplies the same order and the cutoffs retain it. For $y\le1$, $M y^{-1}e^{-ad/y}$ sums to $O(e^{-ad})$ since $y^{-1}e^{-ad/y}$ increases on $(0,1]$ for large $d$. Both time signs obey these bounds. [Bessel integral](https://dlmf.nist.gov/10.32.E10) · [Half-integer evaluation](https://dlmf.nist.gov/10.39.E2)

Finally, the full connected reading is $H_V(B^2)$, where $H_V(0)=0$ and $0<c\le H'_V\le C$ on the realized range. Both component propagators are nonnegative, as follows by the nearest-neighbor walk expansion of the massive inverse lattice Laplacian. Thus divergence of the heavy square implies divergence of the full reading. For $a\ge1/2$ the heavy-square contribution vanishes, including at equality because of the $d^{-1/2}$ factor. The term containing the light covariance alone, $H_V((wG_m)^2)/Z^2$, converges on this flat test by the separated limit and the uniform majorant $C\max(1,|(t,\mathbf x)|^{-4})$ from the light-axis bound. The mixed term is then negligible by Cauchy–Schwarz against the nonnegative test and the bounded derivative of $H_V$. [Checks](checks.md)
