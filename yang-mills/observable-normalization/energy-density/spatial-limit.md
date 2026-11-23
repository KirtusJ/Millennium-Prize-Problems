# A local first-moment form in the spatial limit

On the bare tree-level trajectory $\kappa=2/(\beta b)$, $\lambda=\beta/b$, $g=\beta^2/2$, take $\beta\ge1$ and let the spatial mesh $b$ decrease to zero. The [local diagonal estimate](README.md) gives $b^3D_H\le25$ because $B\le5\beta/2$. No prescribed running law or derivative of $\beta$ enters. Take a fixed smooth compactly supported real test function $\varphi$ in a cube of side $\ell$, with its support and the neighboring cells embedded in the physical torus. The box may grow. Alternatively use a smooth periodic test on a fixed physical torus, with periodic sampling throughout. [B4’s bare regulator matching](../../transfer-operator/hamiltonian-time/)

Use $w_i=b^2\varphi(x_i)$ at the link and face centers. The power $b^2$ is a normalization that the bound permits. Its identification with a physically normalized stress-energy tensor would require further evidence. On an active pair $|w_i-w_j|\le b^3\|\nabla\varphi\|_\infty$. At most $6(\ell/b+2)^3$ terms meet the support, with at most sixteen pairs per such term. Hence
$$
 M_1(w)\le2400(\ell+2b)^3\|\nabla\varphi\|_\infty^2.
$$
For general scalar prefactor $\alpha_b$ in place of $b^2$, multiply the right side by $|\alpha_b|^2/b^4$. The cancellation of the constant mode gains two spatial powers in the energy form over an estimate from absolute weights.

## Which local quantity has to be evaluated?

Use one reference cell, containing six term types $a$. For each ordered allowed neighbor let $d$ be its center displacement in mesh units and $K_{a,j}$ its mixed first moment. Translation invariance around the cubic torus makes the coefficients independent of the cell. Define
$$
 T_b=-\frac{b^3}{2}\sum_{a,j}K_{a,j}\,d d^{\mathsf T},\qquad
 \rho_b=-\frac{b^3}{6}\sum_{a,j} K_{a,j}|d|^2 .
$$
The sum is over at most 96 ordered pairs in the reference cell. Reflections and coordinate permutations preserve the energy terms and the unique positive vacuum, including under a change of basepoint of a face. They permute the term types and the displacements up to a lattice translation. The symmetric matrix $T_b$ therefore equals $\rho_b I$. Also $|\rho_b|\le400$.

For the spatial test above the [exact difference identity](README.md) gives
$$
 M_1(b^2\varphi)=\rho_b\int|\nabla\varphi(x)|^2\,dx+O_\varphi(b).
$$
To check the remainder, replace each squared unscaled difference by $b^2(d\cdot\nabla\varphi)^2+O_\varphi(b^3)$. The bound on third-order error uses two bounded derivatives and $|d|\le1$. There are $O_\varphi(b^{-3})$ active terms, the squared prefactor is $b^4$ and $|K_{a,j}|\le25/b^3$. Their errors sum to $O_\varphi(b)$. The shifted lattice Riemann sum for each squared derivative has error $O_\varphi(b)$ after multiplication by $b^3$, uniformly over the finitely many term types. This proves the expansion even when the vacuum coefficients vary with $b$. For each subsequential limit of $\rho_b$, nonnegativity of the first moment for any test with nonzero gradient forces $0\le\rho\le400$. This identifies the candidate first-moment form. It does not identify it with the first moment of a limiting raw field; high-energy first moments can escape in a weak limit.

## Positive-time compactness

Fix a physical time $s>0$. For the centered $O_w$ vector with raw spectral measure $\nu_b$ use D4’s filter $d\nu_{b,s}=(1-e^{-sE})^2d\nu_b$. Let $C$ be a common first-moment ceiling for the chosen test along the sequence. Then
$$
 \nu_{b,s}([0,\infty))\le s C,\qquad
 \nu_{b,s}([0,\epsilon])\le s^2\epsilon C,\qquad
 \nu_{b,s}([R,\infty))\le C/R .
$$
Indeed $0\le1-e^{-sE}\le\min(1,sE)$. Its square is at most $sE$ everywhere, at most $s^2\epsilon E$ below $\epsilon$, and at most $E/R$ above $R$. These estimates give weakly convergent subsequences of the filtered measures and zero mass at zero in every limit. The latter follows, for example, by testing continuous cutoffs supported in $[0,\epsilon]$ and then sending $\epsilon$ to zero. Their Laplace correlations are equi-Lipschitz with constant $C$. A diagonal subsequence works for a countable collection of tests and their pairwise sums and differences. [D4’s time-difference observable](../../spectral-support/positive-time/vacuum/)

The bounds permit the zero limit. For a nonzero limiting filtered vector one needs raw **first-moment weight** on a compact interval of strictly positive physical energies. This criterion is quantitative. On such an interval $[l,R]$ the continuous multiplier $(1-e^{-sE})^2/E$ has a positive minimum. Conversely, given a positive lower bound on the filtered total along a sequence, choose $l$ small and $R$ large so the two bounds above account for less than half of it. The bounded multiplier on $[l,R]$ then gives a positive lower bound on $\int_{[l,R]} E\,d\nu_b$. If $\rho_b\to0$, the first-moment identity already forces every such filtered norm to zero. Even $\rho>0$ alone does not resolve the band condition: both $n^{-1}\delta_n$ and $n\delta_{1/n}$ have first moment one and vanishing filtered norm. The nonzero continuum vector and the lower gap remain open.
