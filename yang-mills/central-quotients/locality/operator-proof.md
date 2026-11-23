# Operator proof

Work on $L^2(G^{E})$ with product Haar probability. An auxiliary copy of the representation space makes multiplication by the matrix $U_e(g)=\rho(g_e)$ unitary. Scalar observables act diagonally on this copy. Smooth functions on the compact product manifold form a common invariant core for the identities below. In finite volume the smooth bounded potential and ellipticity give equivalence of all integer graph norms of powers of a sufficiently large shift of $H$ with the corresponding even Sobolev norms. Hence $e^{itH}$ preserves smooth vectors and is continuous in their smooth topology. This permits weak differentiation there, even though link angular momenta are unbounded. Bounds on resulting matrix elements extend by density. Only the final constants must be volume independent. For background on unbounded on-site generators see [Nachtergaele–Sims](https://arxiv.org/abs/1410.8174) and [Nachtergaele–Raz–Schlein–Sims](https://arxiv.org/abs/0712.3820).

## Two commutators

Put $T_i=d\rho(X_i)$ and $D_i=D_{ei}$. The product rule $D_i U_e=U_e T_i$, interpreted as differentiation of the multiplier, gives on the core
$$
 U_e^* H U_e-H = Z_e=-\kappa\sum_i(2 T_i D_i+T_i^2).
$$
The scalar magnetic term commutes with $U_e$. The Casimir commutes with each $D_{ei}$ by bi-invariance. Write $U= \tau_t(U_e)$, $Z=\tau_t(Z_e)$, extending $\tau_t$ trivially to auxiliary matrices. Since $\dot U=iUZ$, differentiation of $UBU^*-B$ gives exactly
$$
 \frac{d}{dt}(UBU^*-B)= iU[Z,B]U^* .
$$
The derivative contains only the bounded commutators estimated below. Keeping the unitaries on either side is essential to obtaining constants independent of a spin cutoff.

Let $V=\lambda\sum_p(1-\operatorname{Re}\operatorname{tr}U_p)$. On the same core,
$$
 \tau_t(D_{ei})=D_{ei}-i\int_0^t \tau_s(D_{ei}V)\,ds,
$$
where $D_{ei}V$ on the right is a scalar multiplier. This integral is strongly defined and bounded in a fixed box. In particular $[\tau_t(D_{ei}),B]$ extends to a bounded operator with initial value multiplication by $D_{ei}B$. These identities require no operator-norm differentiation of a time-evolved unbounded generator.

Write $u_e(t)=\|[\tau_t(U_e),B]\|$, $p_e(t)=\sum_i m_i\|[\tau_t(D_{ei}),B]\|$. For $t\ge0$ the two identities give
$$
 u_e(t)\le 2\kappa\int_0^t p_e(s)\,ds,\qquad
 p_e(t)\le p_e(0)+\lambda S\sum_a A_{ea}\int_0^t u_a(s)\,ds .
$$
Here $A_{ea}$ is the number of faces containing both links, including $a=e$. To verify the second inequality, differentiating a face inserts $T_i$ beside the corresponding letter of its word. An inverse letter inserts $-T_i$ on the other side. Commuting the evolved word through $B$ costs at most $m_i$ times the sum of the four link commutator norms. All other factors have norm one. For an inverse letter use $[U^*,B]=-U^*[U,B]U^*$. Normalized partial trace is a contraction and intertwines the scalar time evolution. The real part of a trace is the half-sum of a word and the reversed adjoint word. Thus complex $B$ is allowed. Integrating backwards gives the same inequalities with $|t|$.

## The spatial paths

Let $g_e=p_e(0)$. Substitute the second inequality into the first and iterate. On a bounded time interval the leftover $n$-fold double integral is bounded by $2\|B\|(2\kappa\lambda S\|A\|_\infty)^n |t|^{2n}/(2n)!$, which tends to zero. Therefore
$$
 u_e(t)\le 2\kappa \sum_{n\ge0}
      \frac{(2\kappa\lambda S)^n |t|^{2n+1}}{(2n+1)!}(A^n g)_e .
$$
In the cofacial link graph $A^n g$ vanishes at graph distance greater than $n$ from the support of $g$. This also handles $\lambda=0$, when propagation to every disjoint link vanishes exactly.

Set $v_e=\exp[-\mu\,\operatorname{dist}(e,Y)/b]$. A row of $A$ at an interior link has four copies of its own midpoint, eight perpendicular midpoints at $b/\sqrt2$, and four parallel opposite midpoints at $b$. Boundary rows have a subset of these incidences. The triangle inequality on the torus or box gives $\sum_a A_{ea}v_a\le K(\mu)v_e$. Induction on $n$ yields $A^n g\le P_B K(\mu)^n v$. With $x=|t|\sqrt{2\kappa\lambda S K(\mu)}$, the remaining series satisfies $\sum_{n\ge0} x^{2n}/(2n+1)!\le e^x$. Telescoping the letters of $F$ proves the stated result. The proof uses the actual finite-dimensional representation matrices of the links on $L^2(G^E)$. A compression to a finite set of spins can destroy link unitarity.

## Changing a distant boundary

Embed two boxes in a common tensor product with the same link kinetic terms. Delete a set of faces $J$, leaving all other interactions unchanged. Free spectator links implement a smaller open box. For a loop $F$ common to both, Duhamel's formula for the bounded perturbation gives a difference in its time evolutions bounded by
$$
 \lambda |J|\kappa |t|^2\ell_F S
 \exp[-\mu r_J/b+|t|\sqrt{2\kappa\lambda S K(\mu)}],
$$
where $r_J$ is the minimum midpoint distance to a removed face. Indeed, the constant part of each interaction drops out and its normalized real trace has $P_B\le S$. Integrate the preceding bound over $0\le s\le |t|$. At fixed mesh a cubical exhaustion with boundaries receding and polynomially many removed surface faces gives a norm-Cauchy sequence of time-evolved local words, uniformly on compact time intervals. For nested boxes one can cut only the inner box boundary in the bigger box, allowing the outside to retain its own interactions. Under bare spatial refinement $\lambda\kappa=2/b^2$; a positive physical margin outside the cone therefore removes boundary sensitivity for polynomially many cut faces. The boundary statement compares dynamics. A comparison of vacuum states requires additional information.
