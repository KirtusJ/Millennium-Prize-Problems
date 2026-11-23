# A Lorentz-covariance test for the total-energy normalization

Director A4 · November 22, 2026 research session · B.C. Pacific Time (PCT, UTC−07:00)

The spatial weights $b^2\varphi(x_i)$ in the [conserved-energy estimate](../spatial-limit.md) cannot give a nonzero vacuum excitation of a Lorentz-covariant symmetric conserved stress tensor in infinite Minkowski space. This conclusion already follows from a countable collection of triples of strictly positive Euclidean times. It holds for any overall prefactor $z_b$ whose ratio $|z_b|/b^2$ stays bounded on the subsequence under consideration.

The statement is conditional on identifying the *same* spatial tests and physical clocks with $T^{00}$ in a positive-energy, Poincaré-invariant vacuum theory with the usual covariant spectral resolution. It covers positive timelike invariant masses and the open forward light cone. A vacuum term is invisible to the measurements. Existence of a continuum theory, the appropriate stress-tensor renormalization, and the Yang–Mills mass gap remain open. In particular, this calculation gives a reason to change normalization or operators if a nonzero physical stress tensor is the objective.

## What the lattice forces at a fixed physical resolution

Use the cubic SU(2) Hamiltonian and bare trajectory of the [first-moment proof](../). Center
$O_{b,L}=z_b\sum_i \varphi(Lx_i)h_i$ in its vacuum, with $\varphi$ a real smooth test of compact support inside a cube of side $\ell$. Here $L$ is a spatial dilation in fixed reference units. Write $\nu_{b,L}$ for its raw spectral law and $C_{b,L}$ for its Laplace transform. Put
$$
 D_{b,L}(t)=C_{b,L}(t)-2C_{b,L}(2t)+C_{b,L}(3t),\qquad
 F(u)=e^{-u}(1-e^{-u})^2.
$$
For $u\ge0$, $0\le F(u)\le u$. Therefore $D_{b,L}(t)\le t M_{1,b,L}$. At $bL\le1$, when the support and its mesh neighbors fit inside the physical box, the earlier finite-mesh Lipschitz estimate gives
$$
 M_{1,b,L}\le\frac{A_\varphi}{L}\frac{|z_b|^2}{b^4},
 \qquad D_{b,L}(1/L)\le\frac{A_\varphi}{L^2}\frac{|z_b|^2}{b^4},
 \qquad A_\varphi=2400(\ell+2)^3\|\nabla\varphi\|_\infty^2 .
$$
Indeed $\varphi(Lx)$ has support side $\ell/L$ and Lipschitz constant at most $L\|\nabla\varphi\|_\infty$. The proof uses neither convergence of equal-time variances nor a bound on how fast the Wilson time spacing must shrink with $L$. B4 gives a fixed-box route from actual transfer readings to the Hamiltonian triples using bounded insertions. [B4’s transfer construction](../../../transfer-operator/joint-cutoff/energy-density.md)

## What a stress tensor forces on the same triples

Take metric signature $(+,-,-,-)$ and a unitary spatial Fourier transform. Overall spectral normalization constants can be absorbed into a positive invariant-mass measure $\alpha$. In the positive-energy vacuum two-point function of $T^{00}$, the contribution of a timelike mass band $I\subset (0,\infty)$ has the form
$$
 \int_{s\in I}\!d\alpha(s)\int_{\mathbb R^3}
 \frac{|\mathbf k|^4}{2E}\,|\widehat{\varphi_L}(\mathbf k)|^2\,F(tE)\,d^3\mathbf k,
 \qquad E=\sqrt{s+|\mathbf k|^2},\quad \varphi_L(x)=\varphi(Lx).
$$
The null-shell contribution has the same form at $s=0$. These formulas apply to vacuum Wightman spectral weights. They do not include time-ordered contact terms. The boost derivation, positivity assumptions and two control fields are given in the [shell calculation](shells.md).

Choose a nonzero bump with
$J_\varphi=\int_{1\le|q|\le2}|q|^4|\widehat\varphi(q)|^2\,d^3q>0$. For example a smooth radial bump of sufficiently small support and positive integral has a nonzero Fourier transform on this annulus. If $s\le s_{\max}$ and $L\ge\max(1,\sqrt{s_{\max}})$, then on $L\le|\mathbf k|\le2L$ we have $1\le E/L\le\sqrt 5<3$. Thus $F(E/L)\ge d_0=e^{-3}(1-e^{-1})^2>0$ and $2E\le6L$. Since $\widehat{\varphi_L}(\mathbf k)=L^{-3}\widehat\varphi(\mathbf k/L)$, the integral of $|\mathbf k|^4|\widehat{\varphi_L}|^2$ over that annulus is $L J_\varphi$. One band with $0<\alpha(I)<\infty$ forces
$$
 D_{T^{00},L}(1/L)\ge d_0 J_\varphi\alpha(I)/6
$$
for every sufficiently large $L$. Other bands contribute nonnegative amounts. Positive-energy spectral weight on the open null shell gives the same lower bound with its coefficient in place of $\alpha(I)$.

First pass to the proposed continuum limit at each fixed $L=2^n$. Each of the times $1/L,2/L,3/L$ is then strictly positive and fixed in physical units. Only after this passage send $n$ to infinity. The lattice upper bound goes to zero, whereas a nonzero band gives the fixed lower bound above. Thus all compact timelike mass bands have zero weight, by countable exhaustion, and so does the null coefficient. This route needs only one bump, its countable dilations and the stated positive-time identifications. No reconstruction from a finite collection of unrelated data is used.

## Consequences for amplitudes and other observables

For a nonzero $T^{00}$ positive-energy law along a full cutoff limit with just this multiplicative renormalization, $|z_b|/b^2\to\infty$ is necessary. Otherwise a bounded-ratio subsequence has the same limiting triples and gives the contradiction above. There is also a finite-resolution consequence. If at resolution $L$ the target triple has floor $d>0$, the measured cutoff triple differs from it by at most $d/2$, and $bL\le1$, then $|z_b|/b^2\ge L\sqrt{d/(2A_\varphi)}$. Inferring a rate in $b$ from this last inequality requires matching at a specified growing $L=L_b$. Fixed-test convergence supplies no such rate.

A different representation can survive the same first-moment estimate. A massive conserved vector current has a time-component weight proportional to $|\mathbf k|^2$, compatible with a spatial gradient norm. A nonzero limit of the lattice probe could therefore reflect different covariance properties. A physically normalized stress tensor with a larger prefactor, operator mixing, or a differently identified observable requires its own estimates. [Control fields and numerical check](shells.md) · [Formal coverage and guest replay](execution.md)

B4 subsequently constructed a single anisotropic sequence of periodic Wilson measures for the entire countable family. At each cutoff the clock, even period and Haar integration resolution are common to all tests included at that stage. This also covers mismatched electric and magnetic coefficients when the common part is $O(b^2)$, the residual is $O(b^3)$, and the sampling centers move by $O(b)$. A preassigned isotropic sequence still requires its own clock comparison. The [ten-direction polarization](shells.md#recovering-all-components-from-the-vanishing-energy-density) explains why a transverse null-shell component cannot survive if the time-time measure vanishes on every nonzero momentum. [B4’s Wilson clock and mixed-coefficient estimate](../../../transfer-operator/periodic-time/stress-test-review.md)
