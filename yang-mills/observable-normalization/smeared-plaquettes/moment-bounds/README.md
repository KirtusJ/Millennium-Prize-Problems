# Spectral moments of spatial plaquette sums

Director A4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

On a periodic cubic SU(2) spatial lattice, neighboring fundamental plaquettes cannot cancel one another’s entire electric energy, even for signed coefficients and zero spatial momentum. The resulting first-moment lower bound and a finite-range third-moment identity give an equal-time covariance lower bound for **every** spatial smearing. The first moment also reveals an obstruction on spatial refinement. For a single bare plaquette, or a sufficiently small support, its *normalized energy-weighted* spectral measure loses all weight at fixed physical energies when the electric coefficient diverges. [Spatial-refinement result](refinement.md)

## Finite-volume estimates

Use a periodic cubic torus of side at least three, with one orientation for each elementary face. Take the spatial Wilson Hamiltonian in the positive vacuum, with kinetic coefficient $\kappa>0$ for the half-length generators $i\sigma_j/2$, magnetic coefficient $\lambda\ge0$, and $g=\lambda/\kappa$. Let $B=\min(g,17\sqrt g/8+3/16)$, $Q=H-E_0$, $F_p=\operatorname{Tr}U_p=2x_p$ and $S=\mathbb E(1-x_p^2)$. For real coefficients on all faces put $n=\sum_p c_p^2$, $f_c=\sum_p c_p(F_p-\mathbb E F_p)$, and $M_j(c)=\langle f_c\Omega,Q^j f_c\Omega\rangle$. $M_0$ is the variance. The bounds extend to complex coefficients by taking real and imaginary parts, since $H$ and the plaquette multipliers preserve real wavefunctions. [Hamiltonian, Haar convention and local kinetic bounds](../../hamiltonian-variance/)

With $a=4\kappa/[25(1+B)]$ and $d=2{,}100{,}000\,\kappa^2$, the following inequalities hold simultaneously in the volume and the coefficients:

$$
 a n\le M_1(c)\le16\kappa S n,\qquad
 M_2(c)\le d n,\qquad M_0(c)\ge (a^2/d)n .
$$

For $c\ne0$, $M_1/M_0\le d/a$. Hence the full time correlation quadratic form satisfies $C_c(t)\ge M_0(c)e^{-td/a}$ for $t\ge0$, by integrating the exponential tangent against the normalized spectral measure. These constants apply to a linear combination of any spatial extent, any momentum and any mixture of the three orientations. They bound the Rayleigh quotient from above in this space of single-time plaquette observables. [Positive-measure tangent](../../hamiltonian-variance/HamiltonianVariance.lean)

## Why four neighboring gradients cannot cancel

Fix one electric link $e$ and a face $p$ containing it. Its opposite parallel link $b$ occurs in no other face containing $e$. The other three parallel opposites are the shifts of $e$ by the remaining signed transverse unit vectors; all four shifts are distinct for side at least three. Fix all links except $b$. By cycling or reversing the plaquette trace, the three half-speed $e$ derivatives of $F_p$ are, up to an orthogonal choice of coordinates, the last three coordinates $Z$ of the unit quaternion $U_p$. As $b$ varies, this quaternion is a left/right translate of $b$ or of $b^{-1}$. This preserves Haar measure and the unit-round gradient. The derivatives of the other incident faces are constant in this variable. [Trace gradient and basis convention](../../wilson-loop/)

Here is the needed estimate for a shift $r$ depending measurably on the exterior. Bounded shifts suffice in the application. On the varying unit three-sphere, $\Delta Z_j=-3Z_j$, $\sum_j|\nabla Z_j|^2=3-|Z|^2\ge2$, and the derivative of the coordinate projection $Z$ has operator norm at most 1. Apply integration by parts to $\phi=|Z-r|^2/2$ with density $\Omega^2$. With $K_b$ the half-speed kinetic form of $\Omega$ on the opposite link, $\int|\nabla_b\Omega|^2=4K_b$. Thus

$$
 2\le 3\mathbb E[ Z\cdot(Z-r)]-2\int \Omega\,\nabla\phi\cdot\nabla_b\Omega
 \le (3+4\sqrt{K_b})\sqrt{\mathbb E|Z-r|^2}.
$$

Only $b$ is differentiated. The final expectations include the exterior. Since $(3+4k)^2\le25(1+k^2)$ and $K_b\le B$, every such shift has mean squared residual at least $\tau=4/[25(1+B)]$.

For $c_p\ne0$, absorb the other incident gradients into $r$ after dividing by $c_p$. The squared norm of the full gradient at $e$ therefore has expectation at least $\tau c_p^2$ for **each** incident $p$. At a zero coefficient the same inequality is immediate. Add the four inequalities, divide by four, and sum over $e$. Each face has four links. The ground-state transform gives $M_1(c)\ge\kappa\tau n$. In the other direction, Cauchy–Schwarz on the at most four incident gradient vectors and the one-link identity $\mathbb E|\nabla_e F_p|^2=S$ in half-speed units give $M_1(c)\le16\kappa S n$. At large $g$ both estimates have order $\kappa n/\sqrt g$. The floor thus controls cancellation uniformly even when the electric and magnetic coefficients vary.

## Why the third moment has finite spatial range

Join two faces in a graph when they share a link. Write $T_p=\nabla F_p\cdot\nabla+\Delta F_p/2$ in the unit-round metric and $\gamma=\kappa/4$. The mixed third-moment matrix $G_{pq}=\langle f_p\Omega,Q^3 f_q\Omega\rangle$, with $f_p=F_p-\mathbb E F_p$, is positive semidefinite. Its entries are real. Two integrations by parts using the skew operators $T_p,T_q$ and $H\Omega=E_0\Omega$ give

$$
 G_{pq}=4\gamma^2\langle T_p\Omega,Q T_q\Omega\rangle
       =2\gamma^2\langle\Omega,[T_p,[T_q,H]]\Omega\rangle .
$$

In the complex form the last expression gives the real part; reality supplies the displayed identity in this basis. All fields are smooth in finite volume. For disjoint face supports the kinetic contribution vanishes because $[T_q,-\Delta]$ differentiates only links of $q$. The potential contribution vanishes if no interaction face meets both $p$ and $q$. This proves $G_{pq}=0$ for graph distance greater than two, including with periodic boundary conditions. The vacuum can have long-range correlations. The cancellation follows from the commutators. Odd energy-weighted sum rules have a classical literature; the finite-range application and local constants here use this particular lattice Hamiltonian. [Single-face sum rule](../../hamiltonian-variance/excited-band/third-moment/) · [Bohigas, Lane and Martorell](https://doi.org/10.1016/0370-1573(79)90079-6)

At most $1+12+12\cdot11=145$ faces lie within distance two. Positivity implies $|G_{pq}|\le\sqrt{G_{pp}G_{qq}}$. The single-face estimate gives $G_{pp}\le103681537\,\kappa^3(1+B)$, hence every absolute row sum is at most 145 times this quantity. The symmetric row bound gives the same number times $n$ as an upper bound for $M_3(c)$. Since $S(1+B)\le18$, positive spectral moment interpolation gives

$$
 M_2(c)^2\le M_1(c)M_3(c)
 \le 16\cdot145\cdot18\cdot103681537\;\kappa^4 n^2 .
$$

The square root is less than $2{,}100{,}000$. The second interpolation $M_1(c)^2\le M_0(c)M_2(c)$ proves both the variance floor and the Rayleigh quotient estimate. In the free theory the three moments are exactly $M_j(c)=(3\kappa)^j n$ for $j=0,1,2$. Product Haar makes the distinct traces orthogonal, and each such plaquette is an electric eigenvector. [Lean coverage, controls and replay](execution.md)
