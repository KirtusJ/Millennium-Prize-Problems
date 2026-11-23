# Which local energy smearings excite the finite-box SU(2) vacuum?

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

On a fixed periodic cubic SU(2) lattice with side $L\ge5$, the only linear combination of local electric and magnetic energies whose centered vacuum vector vanishes is the conserved Hamiltonian, for every sufficiently small positive magnetic coupling. The same result holds for every positive magnetic coupling outside a discrete set depending on the box and the kinetic coefficient. At these couplings every nonconstant smearing has a strictly positive three-time detector at every positive time. The proof gives the first two excitation channels for the smearings that suppress the entire leading plaquette response.

The statement concerns the finite box. Its small-coupling interval and the generic-coupling conclusion supply no uniform spectral weight at a fixed physical energy under spatial refinement. The limit here expands about the **electric vacuum**. In the program’s bare trajectory $g=\lambda/\kappa=\beta^2/2$, this is small $g$. The weak bare gauge coupling relevant to continuum Yang–Mills corresponds to growing $g$. [Hamiltonian and local energies](../README.md) · [Kogut–Susskind Hamiltonian](https://doi.org/10.1103/PhysRevD.11.395)

## The first visible channel

Write $K_e=-\Delta_{S^3,e}/4$, $x_p=\operatorname{Tr}U_p/2$, $H_0=\kappa\sum_e K_e$, $S=\sum_p x_p$, and $H=H_0-\lambda S$ after dropping an additive constant. Link weights are $w_e$, face weights are $v_p$. Define $W=\kappa\sum_e w_e K_e$, $S_v=\sum_p v_p x_p$, and $O=W-\lambda S_v$. Real weights suffice. Center $O$ in its actual normalized vacuum $\Omega_\lambda$. Denote its positive-energy spectral law relative to the vacuum energy by $\nu_\lambda$. Put $h=3\kappa$ and $a_p=\frac14\sum_{e\in p}w_e$.

As $\lambda\downarrow0$ at fixed box and $\kappa>0$,
$$
\lambda^{-2}\nu_\lambda\ \Longrightarrow\
 \frac14\sum_p |a_p-v_p|^2\,\delta_h .
$$
The product Haar vacuum is the constant function. Each of the four fundamental links of a plaquette contributes Casimir $3/4$. Thus $H_0x_p=h x_p$ and $Wx_p=h a_p x_p$. Distinct face functions are orthogonal by integrating a link used by just one of them, and $\|x_p\|^2=1/4$. The first vacuum correction is $\lambda S/h$. Acting on it with $W$ and on the constant with the weighted magnetic energy gives $\lambda\sum_p(a_p-v_p)x_p$. This proves the formula and explains the cancellation when all $v_p=a_p$.

## What survives when every face is balanced

For adjacent distinct faces $p,q$ with shared link $e$, put $d_{pq}=w_e-(a_p+a_q)/2$. Sum once over unordered pairs and write $J(w)=\sum_{p\sim q}|d_{pq}|^2$. When $v_p=a_p$,
$$
\lambda^{-4}\nu_\lambda\ \Longrightarrow\
 \frac{J(w)}{h^2}\left(\frac{1}{144}\delta_{9\kappa/2}
                          +\frac{3}{2704}\delta_{13\kappa/2}\right),\qquad
\lim_{\lambda\downarrow0}\lambda^{-4}\int E\,d\nu_\lambda=\frac{J(w)}{234\kappa}.
$$
The first band comes from spin zero on the shared link and the second from spin one. Both have six exterior spin-$1/2$ links. Distinct face pairs have orthogonal contributions. The two limiting masses are strictly positive for every nonconstant balanced smearing. Testing the displayed measure against $F(tE)=e^{-tE}(1-e^{-tE})^2$ gives the leading coefficient of the actual positive-time detector. Its integral against $dt/t^2$ agrees with the [first-moment sum rule](../positive-time-sum-rule/). [Perturbation, projections and Haar factors](channels.md)

## Rank at fixed volume

At a fixed link $e$ four faces meet. If $J=0$, each pair of incident faces satisfies $a_p+a_q=2w_e$. Using three of the four equations for a triple of distinct faces gives $a_p=a_q=a_r=w_e$. Applying this to the remaining face gives $a_s=w_e$ there as well. The link-face incidence graph is connected, so all link and face weights are the same. Conversely a constant smearing is the Hamiltonian and annihilates the vacuum after centering.

There is also a simultaneous statement for all weights, including weights that could vary with the coupling. Quotient the finite-dimensional smearing space by the constant Hamiltonian direction. Split it into independent face residuals and balanced link weights modulo constants. For each $\lambda>0$, form the map to centered vacuum vectors with its first block divided by $\lambda$ and its second by $\lambda^2$. In operator norm this tends to the two coefficient maps just computed. They are each injective, and their ranges are orthogonal by the link representations. The limit has a strictly positive minimum norm on the unit sphere. Hence the rescaled map, and therefore the original map, is injective for all sufficiently small positive $\lambda$ in this box.

Choose a basis of the quotient. The equal-time Gram determinant is real analytic on the connected interval $(0,\infty)$ because the finite-box ground state is everywhere simple and locally analytic in the domain of each kinetic term. It is positive in the small interval just proved. Its zero set therefore has no accumulation point inside $(0,\infty)$. The covariance rank and first-moment rank are both $6L^3-1$ outside this exceptional set. Indeed the finite-box ground state is simple and isolated, and the shifted Hamiltonian is strictly positive on its orthogonal complement. Likewise $F(tE)>0$ on every positive energy. The argument does not locate exceptional points or show that any exist.

For samples $w_e=\varphi(x_e)$ of a smooth periodic test or a compact test inside a padded box on a mesh $b$, the coefficient itself has a spatial interpretation:
$$
\lim_{b\to0} b\,J(w)=\tfrac12\int |\nabla\varphi(x)|^2\,dx .
$$
At an edge the two coplanar opposed face pairs cancel to first order in $b$. For the four perpendicular pairs the first differences are $-b(\pm\partial_i\varphi\pm\partial_j\varphi)/4+O(b^2)$ for the two transverse axes. Summing their squares gives $b^2[(\partial_i\varphi)^2+(\partial_j\varphi)^2]/4+O(b^3)$. Summing the three edge directions and using Riemann sums proves the limit. Multiplying the sampled link weights by $b^2$ makes $J(b^2 w)$ asymptotic to $b^3\int|\nabla\varphi|^2/2$ when the gradient is nonzero. This identifies an iterated perturbative coefficient. No interchange of a spatial limit and an expansion at fixed coupling enters. [Independent finite-volume and two-face controls](execution.md)

The balanced response also has a sharp finite-box lower bound. The least spatial eigenvalue of $J$ away from constants is asymptotic to $2\pi^2/(3L^2)$ and is attained at the lowest axial momentum. The positive-time Gram determinant has an explicit leading coefficient. [Spatial spectrum and detector determinant](spatial-spectrum.md)
