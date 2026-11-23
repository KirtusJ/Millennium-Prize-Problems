# Energy and variance of a spatially smeared plaquette

Director A4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

A linear combination of neighboring Wilson loops has an energy cross term even though the Hamiltonian differentiates one link at a time. For parallel elementary SU(2) plaquettes, only nearest neighbors within the same plane contribute to that cross term. The variance can involve plaquettes at every separation. This yields an equal-time test with a local numerator and a covariance measured using the same smearing.

Use the [finite-volume Hamiltonian and normalization](../wilson-loop/) with positive kinetic coefficient $\kappa$, a smooth real gauge-invariant multiplication potential and a normalized real smooth ground state. Expectations are in its squared ground-state measure. Take all plaquettes in the $xy$ orientation on a periodic cubic lattice with each side at least three links. Write $F_p=\operatorname{Tr}W_p$, choose real weights $c_p$ (zero weights are allowed), and center $\sum_p c_p F_p$. Its variance and first energy moment are

$$V(c)=\sum_{p,q}c_pc_q\operatorname{Cov}(F_p,F_q),\qquad
M(c)=\kappa\sum_e\mathbb E\left|\sum_{p\ni e}c_p\nabla_e F_p\right|^2.$$

The second equality follows from the ground-state transform; it holds for the interacting vacuum. Each contributing edge has exactly two incident plaquettes of the selected orientation.

## Which trace gives the cross term?

For a shared edge $e$, reverse a loop if necessary and cycle its factors so **both** holonomies $P,Q$ start with the same forward oriented link. The trace is real and invariant under inversion. Under a left variation the two quaternion vectors $\mathbf x,\mathbf y$ of $P=(x_0,\mathbf x)$ and $Q=(y_0,\mathbf y)$ give the gradients $-\mathbf x,-\mathbf y$. Hence

$$\nabla_e F_p\cdot\nabla_e F_q
=\tfrac12\operatorname{Tr}(P Q^{-1})-\tfrac14 F_p F_q.$$

In the first trace the common link cancels by cyclicity. By contrast, the cost of **adding** the two gradients is

$$|\nabla_e F_p+\nabla_e F_q|^2
=2-\operatorname{Tr}(P Q)-(F_p-F_q)^2/4.$$

Swapping the two trace words in the cross term reverses its sign. Both formulas follow by quaternion multiplication and the two unit norms. The accompanying matrix-difference check varies the actual shared link with the original plaquettes traversing it in opposite directions. [Related trace-pairing formulas in Goldman, §1](https://math.umd.edu/~wmg/InvariantFunctions.pdf)

## Exact smearing formula under translations

Assume a translation-invariant vacuum measure. Put $A=1-\mathbb E F_p^2/4$. For neighbors in direction $j\in\{x,y\}$ let $B_j$ be the expectation of the shared-edge cross term, and $J_j=2A+2B_j$. Thus $J_j$ is the measured mean squared gradient sum, so $0\le J_j\le4A$. Summing over bonds once gives

$$M(c)/\kappa=A\sum_{p,j}(c_p-c_{p+j})^2+
\sum_j J_j\sum_p c_p c_{p+j}.$$

Indeed the original contribution per bond is $A(c_p^2+c_{p+j}^2)+2B_j c_p c_{p+j}$. Its sum is positive for signed weights even if individual terms in the rewritten expression have different signs. The coefficient bound $|B_j|\le A$ follows by Cauchy–Schwarz. In particular $M(c)\le8\kappa A\sum_p c_p^2$. The exact formula can improve substantially on this bound when neighboring gradients cancel.

For constant weights $c_p=N^{-1/2}$ on all $N$ plaquettes of this orientation, $V(c)=\chi=\sum_r\operatorname{Cov}(F_0,F_r)$ and $M(c)=\kappa(J_x+J_y)$. Whenever $\chi>0$, the exact finite-volume Rayleigh quotient is $\kappa(J_x+J_y)/\chi$. This mode averages over the whole torus. For a local continuum test fix a compactly supported physical smearing and use **its own** $V(c)$ and discrete differences. Plane sums alone do not certify a local field. For either choice the positive-measure tangent gives $C_c(t)\ge V(c)\exp[-tM(c)/V(c)]$. A regulator-independent upper bound on this quotient, positive consistently renormalized variance, and convergence of the time-separated correlator on the same trajectory would witness a nonzero continuum vector.

## Exact interacting control for the sign and covariance

Take two adjacent plaquettes on a patch. Under product Haar the two based holonomies $P,Q$ are independent Haar: conditional on the common edge, each remaining three-edge word is independent Haar. Regard their quaternions $X,Y$ as independent uniform points on the unit three-sphere. Reweight the link measure by $1+\eta X\cdot Y$, $|\eta|<1$, where $X\cdot Y=\operatorname{Tr}(PQ^{-1})/2$. The density is gauge invariant, normalized, positive and leaves each single-plaquette marginal Haar. It is the squared ground state of a finite interacting Hamiltonian of the specified form: take $\Omega=\sqrt{1+\eta X\cdot Y}$ and $V=\kappa\sum X_{ej}^2\Omega/\Omega$. The ground-state transform gives nonnegative energy on its form domain and $H\Omega=0$. This deliberately chosen potential is a control for shared links; the spatial Wilson plaquette potential has its own vacuum.

Haar symmetry gives $\mathbb E_0 X_iX_j=\delta_{ij}/4$. With the new weight, $\mathbb E X_iY_j=\eta\delta_{ij}/16$. Therefore each trace has variance one, their covariance is $\eta/4$, and their shared-edge gradient cross term is $3\eta/16$. Each diagonal energy is $3\kappa$. At $\eta=1/2$ the Rayleigh quotients for $F_p+F_q$ and $F_p-F_q$ are respectively $11\kappa/4$ and $93\kappa/28$. Keeping only the single-plaquette moments would assign $3\kappa$ to both. Changing the sign of $\eta$ interchanges the two answers.

## Remaining Yang–Mills estimate

The formulas specify which equal-time quantities to bound on an interacting physical trajectory. For a prescribed family $c$, determine $A,J_x,J_y$ and $V(c)$ with the same coupling, boundary conditions, spatial resolution, volume and smearing. The unresolved step is a joint analytic estimate on these quantities as the regulator is removed. Neither the two-plaquette example nor the conditional Rayleigh bound proves continuum existence or a mass gap.

[All spatial smearings and the energy-weighted spectral law](moment-bounds/) gives a uniform lower bound on the first moment even for signed coefficients, derives an equal-time covariance floor, and tests how spatial support must grow to retain energy-weighted spectral mass on refinement.

[The energy scale of the homogeneous action](action-curvature/) uses the curvature of the ground energy to control the raw spectral law at zero momentum when the magnetic coupling is averaged over a dyadic window.
