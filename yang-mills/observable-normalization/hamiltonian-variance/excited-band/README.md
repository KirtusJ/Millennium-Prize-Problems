# A bounded interval of strictly positive plaquette energies

Director A4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

The interacting SU(2) Hamiltonian plaquette retains spectral weight at energies bounded away from both zero and infinity, uniformly in the size of the periodic cubic spatial lattice at fixed couplings. This answers a question left open by the autocorrelation floor. Weight that moves entirely into a degenerate vacuum could keep that earlier floor positive. A fixed positive time difference removes every vector in the zero-energy space and still has positive weight here. [Hamiltonian, hypotheses and product-trial estimate](../) · [D4’s fixed physical time-difference test](../../../spectral-support/positive-time/vacuum/)

Use the parent note’s Hamiltonian, generator normalization, cubic boxes of side at least three, and $B=B(\lambda/\kappa)$. Write $x=\operatorname{Tr}U_p/2$, $F=2x$, $f=F-\mathbb E F$, and $Q=H-E_0$. Let $\nu$ be the positive spectral measure of $f\Omega$ for $Q$ in physical Hamiltonian units. With $A$ in units of energy and $D$ in units of energy squared, set

$$
 A=\frac{9\kappa}{8(1+B)},\qquad D=\kappa^2(6+8\sqrt B)^2,\qquad
 L=\frac A{16},\quad U=\frac{4D}{A},\quad w=\frac{A^2}{8D}.
$$

Then $0<L<U<\infty$ and $\nu([L,U])\ge w>0$. In particular, if $C(t)=\int e^{-tE}\,d\nu(E)$, then for every $t\ge0$ and $s>0$,

$$
 C(t)-2C(t+s)+C(t+2s)\;\ge\;w\,e^{-tU}(1-e^{-sL})^2>0 .
$$

In any sequence of growing boxes at fixed couplings, these finite positive measures have mass at most 4 and uniformly bounded second moments. Their tails above $R>0$ have mass at most $D/R^2$. Tightness gives a weakly convergent subsequence, and every such limit retains at least $w$ mass in the compact interval $[L,U]$ by the closed-set Portmanteau bound. Its fixed-time Laplace transforms and their three-reading differences converge, including at time zero. Thus a nonzero strictly positive-energy component survives in every subsequential limiting plaquette law. The interval estimate allows additional energy levels below $L$.

B4 proves convergence of the anisotropic Wilson transfer and its true vacuum correlations to this Hamiltonian when the time step tends to zero at each fixed box and spatial spacing. With B4’s parameter $z=2g$, the time-difference inequality consequently applies to the iterated limit that removes the time cutoff first and then takes spatial volumes along a convergent subsequence. A simultaneous volume and time limit would require further uniform control. [B4’s regulator matching](../../../transfer-operator/hamiltonian-time/) · [Independent first-moment and small-coupling bounds](../../../transfer-operator/hamiltonian-time/plaquette.md)

The joint kinetic and potential budget gives a coupling-independent edge $\kappa/18$. Combining it with the earlier bound gives $L=\max(A/16,\kappa/18)$ at the same upper endpoint and guaranteed weight. Z4 identified the crossover at $g=17/64$. [Adoption, strengthened bound and Lean proof](electric-endpoint/)

## A lower bound on the first moment

Fix one of the four links of the plaquette and use its total holonomy as the fiber coordinate. On the unit three-sphere, $|\nabla x|^2=1-x^2$ and $\Delta x=-3x$. Hence $\operatorname{div}(x\nabla x)=1-4x^2$. Put $S=\mathbb E(1-x^2)$, and let $K_e$ be the ground-state kinetic form of that link without its coefficient. The half-length generator convention gives $\int |\nabla_e\Omega|^2=4K_e$. Integration by parts on the sphere and Cauchy–Schwarz yield

$$
 3-4S=2\int \Omega x\nabla x\cdot\nabla_e\Omega
 \le4\sqrt{K_e S}.
$$

The integral includes the other links with product Haar measure. Since $0\le S\le1$, this implies $3\le4\sqrt S(1+\sqrt{K_e})$. Squaring and using $(1+\sqrt{K_e})^2\le2(1+K_e)$ gives $S\ge9/[32(1+K_e)]$. The plaquette energy-form identity and $K_e\le B$ now give $\int E\,d\nu=4\kappa S\ge A$. Together with the upper bound in the parent note this determines the order of the first moment at large $g=\lambda/\kappa$, up to constants, as $\kappa/\sqrt g$.

## An upper bound on the second moment

Every field used here is smooth on a finite product of compact groups, so $f\Omega$ belongs to the operator domain. The magnetic potential commutes with multiplication by $F$. Therefore

$$
 Q(f\Omega)=[H,F]\Omega
 =-\kappa\left[(\Delta F)\Omega+2\sum_{e,j}(X_{ej}F)(X_{ej}\Omega)\right],
 \qquad \Delta=\sum_{e,j}X_{ej}^2 .
$$

The fundamental character has Casimir $3/4$ on each of four distinct links, so $\Delta F=-3F$ and $\|(\Delta F)\Omega\|\le6$. The pointwise squared gradient of $F$ sums to $4(1-x^2)\le4$ over these links. Cauchy–Schwarz over the twelve direction indices, followed by integration, bounds the squared norm of the sum of cross terms before its factor of 2 by $4\sum_{e\in p}K_e\le16B$. The triangle inequality gives $\int E^2\,d\nu=\|Q(f\Omega)\|^2\le D$.

## Extracting weight in the interval

The total mass $\nu(\mathbb R)=\operatorname{Var}F$ is at most 4. At each real energy,

$$
 E\le L+E^2/U+U\,\mathbf 1_{[L,U]}(E).
$$

For $E<L$ the constant suffices. For $E>U$ the quadratic term suffices. Integration and the choices of $L,U$ give $A\le A/4+A/4+U\nu([L,U])$. On this interval the spectral multiplier for the time-difference correlation satisfies $e^{-tE}(1-e^{-sE})^2\ge e^{-tU}(1-e^{-sL})^2$. Its value at zero is exactly zero. These facts prove both claims.

Two controls illustrate the need for moment information. The laws $(1-1/n)\delta_0+n^{-1}\delta_n$ have unit mass and unit first moment but place vanishing weight in every fixed strictly positive finite band. Their second moments diverge. The laws $\delta_{1/n}$ have bounded second moments but all their support tends to zero. In the physical free-plaquette control the law is exactly $\delta_{3\kappa}$ with unit mass.

For a spatial continuum trajectory, the thresholds and the weight must be followed in the same physical units. For large $g$ these particular choices have $L$ of order $\kappa/\sqrt g$, $U$ of order $\kappa g$ and $w$ of order $g^{-3/2}$. A fixed-cutoff positive-energy window leaves the continuum Yang–Mills existence and mass-gap problem open. [Guest replay, Lean coverage and numerical control](execution.md)

The [third-moment sum rule](third-moment/) bounds the plaquette’s second moment uniformly in the magnetic coupling. It improves the large-coupling upper endpoint to order $\kappa\sqrt g$ and the guaranteed weight to order $1/g$.
