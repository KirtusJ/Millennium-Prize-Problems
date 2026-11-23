# A family that concentrates the inverse response at one coupling

Can the coupling-window conclusion be asserted at every selected coupling using just the scalar moment estimates and the curvature identity? The following pair of two-level systems gives a counterexample. It is a control on that inference, separate from the Wilson model.

For $G\ge1$ put $r=\sqrt G$, $g_0=3G/2$ and $\epsilon=G^{-2}$. On a tensor product of two qubits let the Hamiltonian be the sum of the following two factor Hamiltonians. $X,Z$ denote Pauli matrices.

$$
 H_1(g)=r(I+X)+\frac{g}{r}(I+Z),\qquad
 H_2(g)=\begin{pmatrix}g/r&\epsilon\\\epsilon&g_0/r\end{pmatrix}+\epsilon I .
$$

Each is affine in $g$, with nonnegative electric part, nonnegative bounded magnetic part and simple ground state. For the action probe take $-2\partial_g(H_1+H_2)$, centered in the product ground state. Its spectral law is the sum of the two single-factor laws since the two single excitations are orthogonal. The same inverse-energy/ground-energy curvature identity holds with one unit of normalization.

The first factor has gap $2r\sqrt{1+(g/G)^2}$ and raw weight $4/[G(1+(g/G)^2)]$. Its weight is of order $G^{-1}$ and its first moment of order $G^{-1/2}$ throughout the window. For the second factor the gap is $h=\sqrt{((g-g_0)/r)^2+4\epsilon^2}$ and the raw weight is $4\epsilon^2/(G h^2)$. In particular its second moment is $4\epsilon^2/G$. The sum therefore has the uniform first-moment lower bound of order $1/r$, bounded second moment, and a variance floor of order $1/G$. Its mean action per unit is nonnegative and bounded by $3/r$ throughout. Its integrated inverse-moment budget is of order at most $1/r$.

At the precise coupling $g=g_0$, the two transition energies are $r\sqrt{13}$ and $2\epsilon$. The raw weights are $16/(13G)$ and $1/G$. Thus a fraction **13/29** of the normalized raw spectral mass goes to energy zero along those centers. The slow factor gives a pointwise inverse moment $1/(2G\epsilon)$, although the width in coupling over which it is this large shrinks on the scale $r\epsilon$. The analytic curvature and the window estimate coexist with the exceptional couplings. The family changes with $G$; it challenges a uniform inference from these scalar inputs across families. It provides no evidence that such an exceptional trajectory exists for the cubic Wilson Hamiltonian.

The separate single-plaquette Wilson rotor tests the normalization on an actual SU(2) character Hilbert space. The tridiagonal kinetic matrix at electric coefficient one has entries $n(n+2)$ and the potential has diagonal $g$ and off-diagonal $-g/2$. The code evaluates the inverse moment from transition weights, integrates it over each window, and independently compares it with twice the endpoint drop in the mean action. It also differentiates the mean action by a centered finite difference at the midpoint, checks $V^2\le mJ$, doubles the character cutoff, and diagonalizes both factors of the avoided-crossing control. [Code](check_response.py) · [Numerical read-back](execution.md)
