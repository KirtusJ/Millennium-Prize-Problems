# Local Haar comparison and the first spectral moment

## A conditional estimate for the interacting ground state

Fix a set \(S\) of \(m\) spatial links in the finite Hamiltonian of the [statement](README.md). Write the link tuple as \((x,y)\) on \(G^S\times G^{S^c}\). Put all potential terms touching \(S\) in \(V_S\), and all remaining terms in \(H_{\rm ext}\). Let \(d=\sup V_S-\inf V_S\), taking the extrema over both \(x,y\). For the normalized Haar heat kernel of the one-link Laplacian at time \(\kappa\tau>0\), denote its positive minimum and finite maximum by \(h_-\) and \(h_+\). For every exterior \(y\), the conditional ground-state density satisfies
\[
 r^{-2}\le
 \frac{\Omega(x,y)^2}{\int_{G^S}\Omega(z,y)^2\,dz}
 \le r^2,\qquad r=e^{\tau d}(h_+/h_-)^m .
\]

Here is a proof which keeps the exterior and its potential. Evolve the positive vacuum for a time \(\tau\). For \(A=K_S+H_{\rm ext}\), positivity and the bounded multiplication \(V_S\) give, on positive inputs,
\[
 e^{-\tau\sup V_S} e^{-\tau A}\Omega
 \ \le\ e^{-\tau H}\Omega=e^{-\tau E_0}\Omega
 \ \le\ e^{-\tau\inf V_S} e^{-\tau A}\Omega .
\]
This follows either from the positive Feynman–Kac weight or by bounding each multiplication in the Trotter product. These are order inequalities for positive functions. Since \(e^{-\tau A}\) factorizes, its value at \((x,y)\) lies between \(h_-^m J(y)\) and \(h_+^m J(y)\), where \(J(y)=(e^{-\tau H_{\rm ext}}\int\Omega(z,\cdot)\,dz)(y)>0\). Kernel smoothing and continuity give the comparisons pointwise. Taking the ratio of the maximum to the minimum in \(x\) cancels \(J(y)\) and the vacuum energy. Squaring and normalizing proves the displayed estimate. This argument uses the positive vacuum on the full product, which belongs to the physical space by gauge invariance and uniqueness. [Trotter product theorem](https://doi.org/10.1090/S0002-9939-1959-0108732-6)

For four specified links on a periodic cubic spatial lattice at most sixteen elementary faces touch the set. One can use \(d=16\lambda\,\operatorname{osc}(v)\) as an upper bound and any fixed \(\tau>0\). This gives one comparison constant for every edge neighborhood in every box. Although all four chosen variables are integrated together, their interacting conditional distribution is allowed to be correlated.

## Four independent integration variables for each edge

For coefficients \(z_p\in\mathbb C\) on all faces let \(F_z=\sum_p z_p(F_p-\langle F_p\rangle)\). The ground-state transform and polarizing the real identity give its first spectral moment as
\[
  \langle F_z\Omega,QF_z\Omega\rangle
       =\kappa\sum_e \mathbb E_{\Omega^2}\Big\|\sum_{p\ni e}z_p\nabla_e F_p\Big\|^2 .
\]
Choose the four links opposite \(e\) in its four incident faces as \(S\). For \(L\ge3\) they are distinct, and each occurs once on its own face and on none of the other three. Condition on the remaining links, including \(e\). Integration of these four variables against product Haar makes the four face holonomies independently Haar by translation and inversion.

To verify the gradients in a common tangent frame, vary the edge as \(U_e\mapsto\exp(sX)U_e\). By cyclic invariance of a class function the forward face word may start with \(U_e\), and the backward one may end with \(U_e^{-1}\). The resulting derivatives are the left and negative right derivatives of \(f\) on the face holonomy. Left and right directional derivatives agree for a class function since \(g\exp(sX)\) and \(\exp(sX)g\) are conjugate. Each Haar gradient vector has mean zero by translation invariance and mean squared norm
\[
 J_f=\int_G\|\nabla f(g)\|^2\,dg>0 .
\]
Positivity follows from nonconstancy on a connected group. Independence eliminates all mixed terms even for complex coefficients. The resulting Haar integral of the squared norm is \(J_f\sum_{p\ni e}|z_p|^2\). The conditional density floor gives at least \(r^{-2}\) times this result in the actual interacting vacuum.

Each face is counted on four edges. Cauchy–Schwarz at each edge gives the upper estimate since at most four faces meet it. Thus for all coefficients,
\[
 a\sum_p|z_p|^2\le\langle F_z\Omega,QF_z\Omega\rangle\le b\sum_p|z_p|^2,\qquad
 a=4\kappa r^{-2}J_f,\qquad b=16\kappa\|\nabla f\|_\infty^2 .
\]
Applying this to Fourier coefficients \(z_{x,j}=N^{-1/2}e^{ik\cdot x}u_j\) preserves the coefficient norm exactly. The private-link calculation prevents a polarization from cancelling out of the first moment at a special Fourier momentum. For \(L=2\) the two opposite links in the positive and negative transverse direction coincide. The independence step has no such justification in that geometry. [Exact incidence and side-two control](geometry.py)
