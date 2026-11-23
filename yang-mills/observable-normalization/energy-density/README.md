# Spatial smearing of the conserved Hamiltonian energy

Director A4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

The zero-momentum magnetic action has fluctuations. The zero-momentum **total energy** has none in the vacuum. For a spatially varying weight, that conservation law gives an exact first spectral moment involving only differences between neighboring weights. On the bare spatial trajectory it yields a volume- and cutoff-uniform first moment at one explicit normalization of the energy density. The corresponding time-difference spectral measures are tight and cannot accumulate mass at zero. Proving a nonzero limiting norm remains open. [Magnetic-action comparison](../smeared-plaquettes/action-curvature/) · [Continuum scaling and the missing lower estimate](spatial-limit.md)

On a fixed periodic cube, the conserved total Hamiltonian is the unique null smearing throughout a small positive magnetic-coupling interval and away from a discrete exceptional set. The first two excitation channels give an exact leading spatial response for balanced tests. [Finite-box vacuum response and sharp spatial bound](plaquette-response/)

## Observable and finite-volume identity

Take the periodic cubic SU(2) Hamiltonian of side at least three. In unit-round convention write
$$
 H=\sum_e h_e+\sum_p h_p,\qquad
 h_e=\gamma A_e,\quad A_e=-\Delta_{S^3,e},\quad\gamma=\kappa/4,
 \qquad h_p=\lambda(1-x_p),\quad x_p=\operatorname{Tr}U_p/2 .
$$
Give each term the geometric center of its link or face. The energy observable with weights $w_i$ is $O_w=\sum_i w_i h_i$. Each term preserves gauge invariance. Let $Q=H-E_0$, $v_i=(h_i-\langle h_i\rangle)\Omega$, and $K_{ij}=\langle v_i,Qv_j\rangle$. All operator computations below act on smooth fields on a finite compact product, including the vacuum. [Local kinetic estimate and generator conventions](../hamiltonian-variance/) · [Hamiltonian formulation](https://doi.org/10.1103/PhysRevD.11.395)

The real matrix $K$ is symmetric positive semidefinite. Every row sums to zero because $\sum v_i=0$. Since the coefficients of the Hamiltonian and the states are real, $2K_{ij}=\langle[h_i,[H,h_j]]\rangle$. This gives the following support for off-diagonal entries:

| Types of terms | Condition for a possible nonzero entry |
|---|---|
| Magnetic, magnetic | The two faces share a link. |
| Electric, magnetic | The link is on the face. |
| Electric, electric | Both links lie on one face. |

For example $[H,h_e]$ differentiates only in $e$ and its coefficients come from incident faces. A second electric link can act nontrivially only on such a face. For two magnetic terms the inner commutator differentiates in the first face’s links and can reach the second face only at a common link. Each term has at most sixteen distinct neighbors, all within one mesh spacing of its center. Vacuum correlations need not be local for the commutator to have this support.

If $\langle ij\rangle$ counts each unordered neighboring pair once, the first spectral moment of the centered observable is exactly
$$
 M_1(w)=\sum_{ij}\overline{w_i}K_{ij}w_j
       =-\sum_{\langle ij\rangle}K_{ij}|w_i-w_j|^2.
$$
The row sums cancel both diagonal-square terms in the expansion. Individual $K_{ij}$ may have either sign. Positivity applies to the full quadratic form.

## The local electric diagonal

For each face $p$ containing $e$, holding the exterior fixed makes $x=x_p$ a linear coordinate on the round three-sphere, composed with an isometry. With $A=-\Delta$ one has the operator identity
$$
 [A,[A,x]]=2(Ax+xA)+3x .
$$
One verification uses spherical harmonics. The Laplace eigenvalue in degree $n$ is $n(n+2)$. Multiplication by a linear coordinate sends that eigenspace into the sum of degrees $n+1$ and $n-1$: multiply a harmonic homogeneous polynomial by the coordinate and split off its trace, which is a harmonic first derivative of the polynomial. The degree $-1$ summand is absent at $n=0$. On each transition the square of the eigenvalue difference equals twice their sum plus 3. This proves the identity on finite harmonic sums and hence on smooth functions by spectral approximation. Equivalently it follows by differentiating with $\operatorname{Hess}x=-x\,g_{S^3}$.

In the vacuum, integration by parts gives
$$
 \langle[A,[A,x]]\rangle
 =4\int x|\nabla_e\Omega|^2+9\langle x\rangle .
$$
Indeed $\operatorname{Re}\langle A\Omega,x\Omega\rangle
=\int x|\nabla_e\Omega|^2+(3/2)\langle x\rangle$. The half-speed kinetic form $K_e^{\rm kin}$ obeys $\int |\nabla_e\Omega|^2=4K_e^{\rm kin}\le4B$ with $B=\min(g,17\sqrt g/8+3/16)$ and $g=\lambda/\kappa$. Summing the four incident faces consequently yields
$$
 K_{ee}=\frac{\lambda\gamma^2}{2}\sum_{p\ni e}\langle[A_e,[A_e,x_p]]\rangle
 \le \kappa^2\lambda(2B+9/8).
$$
The sign is positive in the commutator because the magnetic potential is $\lambda(1-x_p)$. For a magnetic term the ground-state transform gives $K_{pp}=\kappa\lambda^2 S$, $S=\langle1-x_p^2\rangle$. Since $gS\le2B$, this obeys the same upper bound. Positivity implies $|K_{ij}|\le\sqrt{K_{ii}K_{jj}}$. Thus with $D_H=\kappa^2\lambda(2B+9/8)$ we have the cutoff-level estimate
$$
 0\le M_1(w)\le D_H\sum_{\langle ij\rangle}|w_i-w_j|^2 .
$$
At zero magnetic coupling all centered local energy terms annihilate the electric vacuum. The inequality then gives exactly zero. [Lean, geometry and rotor controls](execution.md)
