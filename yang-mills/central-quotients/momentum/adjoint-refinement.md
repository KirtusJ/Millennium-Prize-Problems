# Adjoint plaquettes at changing magnetic coupling

For \(SU(2)\) the heat-kernel comparison can be replaced by a polynomial estimate that holds for arbitrary spatial smearings of the adjoint trace, including all three complex polarizations at zero momentum. Use A4's convention \(H=-\kappa\sum X_{ej}^2+\lambda\sum_p(1-x_p)\), with \(i\sigma_j/2\) generators, \(x_p=\tfrac12\operatorname{Tr}U_p\), \(g=\lambda/\kappa\), and \(B=\min(g,17\sqrt g/8+3/16)\). Let \(A_p=4x_p^2-1\), \(n=\sum|c_p|^2>0\), and \(M_j(c)\) be the \(j\)-th spectral moment of the centered sum \(\sum c_p A_p\) in the positive vacuum. The result is
\[
 M_1(c)\ge a_A n,\qquad M_2(c)\le D_2\kappa^2 n,\qquad
 a_A=\frac{9\kappa}{16(1+\sqrt B)^2}.
\]
The constant \(D_2\) below is independent of the box, \(\kappa,\lambda\) and the coefficients. The proof uses A4's local energy estimate \(K_e\le B\) and \(gu\le B\), where \(u=\mathbb E(1-x_p)\). We also use \(S=\mathbb E(1-x_p^2)\le2u\) and \(S(1+B)\le18\). A4 established the small-support and averaged energy-weighted conclusions for the fundamental trace. D4 obtained a sharper energy-weighted estimate for a single adjoint plaquette. Here the possible interference of a whole family of adjoint insertions is included. [A4's fundamental smearing results](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/e49cee4f36d69be30d041c91e05afe4f7eb49b55/yang-mills/observable-normalization/smeared-plaquettes/moment-bounds) · [D4's single adjoint estimate](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7093164469)

## A shifted vector on the three-sphere

Write a unit quaternion \(q=(x,Z)\), \(Z\in\mathbb R^3\), and \(Y=xZ\). On the **unit round** sphere,
\[
 \Delta Y=-8Y,\qquad |Y|\le1/2,\qquad
 \|dY\|_{\rm op}\le1,\qquad \|dY\|_{\rm HS}^2=1-2x^2+4x^4\ge3/4 .
\]
The Laplace identity follows from the degree-two harmonic polynomials \(xZ_j\). For \(x=\cos\theta,\ Z=\sin\theta\,v\), the radial derivative has magnitude \(|\cos2\theta|\), and the two tangential singular values equal \(|\cos\theta|\). Their squares sum to the displayed polynomial. The formulas extend to the poles by continuity.

Fix an electric link \(e\), an incident face \(p\), and that face's opposite link \(b\). As \(b\) varies, the face quaternion can be used as the integration coordinate by a Haar isometry. Cycling the word or reversing it is permitted because the trace is real and inversion-even. The three half-speed \(e\)-derivatives of \(A_p\) then form \(4Y\) up to sign and an orthogonal frame change independent of \(b\). All other gradients incident on \(e\) are independent of \(b\). For any bounded exterior vector \(h\), apply integration by parts in \(b\) to \(|Y-h|^2/2\) with density \(\Omega^2\). Putting \(s^2=\mathbb E|Y-h|^2\), the Laplacian of this squared distance and Cauchy–Schwarz give
\[
 3/4\le 4s+2s\,\|\nabla_b^{\rm round}\Omega\|_2
        \le (4+4\sqrt B)s .
\]
No derivative of \(h\) enters. For real \(c_p\ne0\), choose \(h\) to absorb the three other incident gradients after division by \(4c_p\) and the frame change. The residual squared for the total \(e\)-gradient is at least \(16c_p^2s^2\ge9c_p^2/[16(1+\sqrt B)^2]\). Average these four bounds at \(e\), then sum over edges, so each plaquette is counted four times. Real and imaginary parts add for complex smearings. This proves the bound on \(M_1(c)\), including full cancellation tests at special spatial momenta.

## Upper moment with a coupling-independent constant

In the metric in which the half-speed generators are orthonormal, \(|\nabla_e A_p|=4|x_p||Z_p|\) and \(|\nabla_e(1-x_p)|=|Z_p|/2\). The first-moment row estimate therefore gives \(M_1(c)\le256\kappa S n\). Write \(H_A,H_v\) for the suprema of the operator norms of the full four-link Hessians of \(A_p\) and \(v_p=1-x_p\), in this metric. Let \(\alpha_0,\omega_0\) be the kinetic divergence-form coefficient bounds in the [third-moment proof](third-moment.md) at \(\kappa=1\). All four constants are fixed finite numbers on \(SU(2)^4\).

For \(Y_p=\nabla A_p\) on the product, the magnetic part of the diagonal double commutator is \(2\kappa^2\lambda\sum_{q\sim p}Y_p(Y_pv_q)\). The Hessian product rule gives
\[
 |Y_p(Y_pv_q)|\le64 H_v |Z_p|^2+8 H_A |Z_p||Z_q|.
\]
Indeed \(|Y_p|\le8|Z_p|\) and \(|\nabla v_q|\le|Z_q|\) on their four links. Translation and cubic symmetry give the same \(S\) for all faces, so both expectations on the right are bounded by \(S\). Since \(\lambda S\le2\kappa B\), the thirteen faces and the kinetic form give
\[
 M_{3,pp}\le\kappa^3 D_3(1+B),\qquad
 D_3=\omega_0+4\alpha_0+52(64H_v+8H_A).
\]
The kinetic coefficient scales as \(\kappa^3\), and the four-link ground-state kinetic form is at most \(4B\). The radius-two Schur estimate then gives \(M_3(c)\le63\kappa^3D_3(1+B)n\). Applying Cauchy–Schwarz to \(E^{1/2}\) and \(E^{3/2}\) in the positive spectral measure yields \(M_2(c)^2\le M_1(c)M_3(c)\). Thus one may take
\[
 D_2=\sqrt{256\cdot63\cdot18\,D_3}.
\]
These constants need no numerical fit to an eigenvalue or a sampled vacuum.

## Refinement, momentum and the measured spectral law

Let \(\nu_c\) be the raw centered spectral measure and \(P_c^{(1)}=E\nu_c/M_1(c)\) the energy-weighted probability law. Since \(A_p-3=-4(1-x_p^2)\), \(\mathrm{Var}(A_p)\le16 S\le576/(1+\sqrt B)^2\). By Cauchy–Schwarz the variance of a smearing is at most this number times \(\|c\|_1^2\). For \(N_c=\|c\|_1^2/\|c\|_2^2\),
\[
 P_c^{(1)}([0,E_*])\le1024\,E_*N_c/\kappa,\qquad
 \int e^{-tE}\,dP_c^{(1)}\le1024\,N_c/(e\kappa t)\quad(t>0).
\]
These bounds hold even when the coefficients or their signs change with cutoff. D4's constant 144 is stronger for one insertion. Parseval gives the corresponding average over a complete orthonormal basis of coefficient vectors with \(N_c\) replaced by one. Taking a supremum over all complex unit polarizations separately at each Fourier momentum costs a factor three, by the static trace bound.

For any \(0<\delta<1\), at least \((1-\delta)N\) momenta simultaneously have static mass in every unit polarization bounded by \(K_\delta=1728/[\delta(1+\sqrt B)^2]\). Set \(a=a_A,\ D=D_2\kappa^2\), and
\[
 \ell=\frac a{4K_\delta}=\frac{\delta\kappa}{12288},\qquad
 R=\frac{2D}{a}.
\]
At every such momentum \(a^2\le K_\delta D\) by Cauchy–Schwarz. For any unit polarization integrate \((E-\ell)(R-E)\), bounded above by \((R-\ell)^2/4\) inside the window and by zero outside. Its integral is at least \(-D+(\ell+R)a-\ell R K_\delta\ge D/2\). Since \(0<\ell<R\), this gives the matrix estimate
\[
        \mu_k([\ell,R])\succeq \frac{a_A^2}{2D_2\kappa^2}\,I_3 .
\]
The lower endpoint stays a fixed fraction of \(\kappa\) for the chosen fraction of momenta, uniformly in magnetic coupling. The upper endpoint is of order \(\kappa(1+B)\) and the guaranteed mass is of order \((1+B)^{-2}\). Along B4's bare tree-level matching, \(\kappa=2/(\beta b)\) and \(g=\beta^2/2\) for spatial spacing \(b\). If \(\beta\to\infty\) and \(\beta b\to0\), this band moves to ultraviolet physical energies. The estimates on \(P_c^{(1)}\) describe an energy-weighted law. Positive low-energy mass in the raw measure can coexist with that escape, and the conclusions exempt a shrinking physical momentum patch from a uniform positive-band assertion. [D4's quadratic-window argument](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7092973791) · [B4's Hamiltonian matching](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/6c086a6c4dd605a99869ed8c8c2ae3a1eaa6a2aa/yang-mills/transfer-operator/hamiltonian-time)
