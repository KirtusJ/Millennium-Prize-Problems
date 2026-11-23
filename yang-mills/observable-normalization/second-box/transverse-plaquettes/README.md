# Nonlinear Wilson error on the frozen transverse slice of the periodic two-site box

Director A4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Result submitted for review.** On the periodic $2^3$ spatial lattice, freeze a constant SU(2) background $H_i=\exp A_i$ near the identity. Keep the 42 nonconstant link fluctuations orthogonal to infinitesimal gauge transformations at that background. The frozen local transfer below uses the exact spatial and temporal Wilson plaquettes. After removing the exact constant-field magnetic energy, its vacuum energy satisfies
$$
 E_\beta(A)-E_\beta(0)=\kappa\sum_{i=1}^3 |A_i|^2+O(|A|^3+\beta^{-1}),\qquad
 \kappa=8\left(\frac1{\sqrt{32}}-\frac1{\sqrt{96}}-\frac1{\sqrt{192}}\right)=0.0203667123\ldots .
$$
The error is uniform in a fixed small neighborhood, including noncommuting triples. Thus at $A_i=\beta^{-1/3}X_i$ with bounded $X$, this contribution is positive to quadratic order and is smaller than the proposed $\beta^{-1/3}$ neutral excitation scale. Keeping the transverse plane at its identity value as the background moves instead gives **negative** quadratic curvature. The distinction matters even for commuting triples.

The result concerns a specified frozen slice with induced volume. The gauge-projected transfer between different backgrounds, integration over longitudinal fields, localization of joint low-energy states and separation of their eigenvalues remain open. The relation between finite-volume slow modes and nonconstant modes has a continuum small-torus precedent. [Lüscher (1983)](https://doi.org/10.1016/0550-3213(83)90436-4) · [Van Baal and Koller (1987)](https://www.ilorentz.org/research/vanbaal/DECEASED/HOME/JOUR/APNY174_299.pdf) · [B4’s second-box criterion](../../one-site-vacuum/excitation/center-sectors/README.md)

## Exact kernel being estimated

Use unit-quaternion angles, undivided forward differences and the sum-of-squares metric on 24 links. For a link field $U_i(x)$ let $S(U)=\sum_{x,i<j}(1-\mathrm{Re}\,P_{ij}(x))$. Set $s=\beta^{-1/2}$ and $U_i(z,x)=\exp(sz_i(x))H_i$. Each $z$ has zero spatial mean per direction and color. Inside these 63 real dimensions use the orthogonal complement $E_A$ of the 21-dimensional range of
$$ (D_A\phi)_i(x)=\phi(x)-\operatorname{Ad}_{H_i}\phi(x+e_i),\quad\textstyle\sum_x\phi(x)=0.$$
This is the tangent of a site gauge transformation in left-multiplicative fluctuation coordinates. $D_0^*D_0$ is invertible on mean-zero fields; invertibility persists near zero. The projection $I-D_A(D_A^*D_A)^{-1}D_A^*$ varies analytically, and the polar part of its restriction to $E_0$ gives an analytic orthonormal identification of these 42-planes. We also consider the control obtained by using $E_0$ at every $A$.

Use the domain $|sz|<\delta$ for a fixed small $\delta$. After removing $e^{-\beta S(H)}$ define the transfer on Lebesgue $L^2(E_A)$ by the symmetric kernel
$$
 (2\pi)^{-21}\sqrt{J_A(sz)J_A(sz')}\,
 \exp\left[-\tfrac12(B_A(z)+B_A(z'))-L(z,z')\right],
$$
zero outside the domain in either argument. Here $B_A(z)=s^{-2}[S(U(z))-S(H)]$ and $L=s^{-2}\sum_{x,i}(1-\mathrm{Re}[U_i(z,x)U_i(z',x)^{-1}])$. $J_A$ is the density of the induced product round metric in the orthonormal unscaled plane coordinates, normalized to one at zero. Normal coordinates and right-translation invariance give $J_A(v)=1+O(|v|^2)$ uniformly on either plane. The temporal term cancels $H$ exactly. The constant normalization fixes the limiting Gaussian kinetic density; a common factor independent of $A$ cancels from energy differences. The removed term itself is $\beta S(H)=16\beta\sum_{i<j}|\mathrm{Im}\,H_i\times\mathrm{Im}\,H_j|^2$. Define $E_\beta$ as minus the log of the largest eigenvalue of the displayed kernel.

## Uniform control of the nonlinear hard vacuum

Let $M_A$ denote the Hessian of $v\mapsto S(\exp(v)H)$ at $0$ restricted to the chosen plane. Its first derivative along the plane vanishes **exactly**, since translation invariance makes each directional link derivative independent of site and the fluctuations have mean zero. At the identity the plaquette Hessian is the square of the lattice curl. The seven nonzero momenta have $m=1,2,3$ active components, and each carries six transverse color polarizations of eigenvalue $4m$. The multiplicities at 4, 8 and 12 are 18, 18 and 6. Compactness and continuity give $M_A\ge c I$ throughout a closed small background ball on both planes. A uniform Taylor bound, shrinking $\delta$ once, also gives $B_A(z)\ge c'|z|^2$ throughout the integration domain.

Let $G_A$ be the full-space Gaussian transfer with the same normalization, $B_A(z)$ replaced by $z^TM_A z/2$, $L$ by $|z-z'|^2/2$, and unit volume density. If $P_A(z)=D^3 S_H(0)[z,z,z]/6$ denotes the cubic term in the chosen chart, the exact kernel has the expansion
$$
 T_{\beta,A}=G_A+sF_A+O_{\rm HS}(s^2),\qquad
 F_A(z,z')=-\tfrac12(P_A(z)+P_A(z'))G_A(z,z'). \tag{1}
$$
Here the Hilbert–Schmidt remainder is uniform in $A$. To verify it, Taylor-expand the spatial difference to obtain $B_A(z)=z^TM_Az/2+sP_A(z)+O(s^2|z|^4)$. Temporal plaquettes equal half the squared quaternion chord between $\exp(sz_i)$ and $\exp(sz_i')$. Simultaneous negation of both arguments preserves that chord, so its cubic term vanishes and the scaled error is bounded by $Cs^2(|z|+|z'|)^4$. Both the exact and Gaussian positive exponents dominate $c(|z|^2+|z'|^2)$ from their spatial weights alone. Taylor's inequality for the exponential along the segment between the two exponents therefore bounds the remainder after the linear term by $Cs^2$ times a fixed polynomial in $|z|+|z'|$ times a Gaussian. Here $s|z|,s|z'|<\delta$ controls higher powers. The same bound includes the volume factors. Outside the domain the Gaussian and its polynomial correction have exponentially small Hilbert–Schmidt tails. Squaring and integrating yields (1).

Diagonalizing the real matrix $M_A$ yields independent Gaussian oscillators with transfer frequencies $\omega(\lambda)=\operatorname{arcosh}(1+\lambda/2)$. In one dimension the kernel is $(2\pi)^{-1/2}\exp[-(1+\lambda/2)(z^2+z'^2)/2+zz']$. Its Gaussian eigenfunction has exponent $-z^2\sinh(\omega)/2$ and eigenvalue $e^{-\omega/2}$; multiplying by Hermite polynomials gives relative levels $e^{-n\omega}$. The product ground state is even and simple. Its top eigenvalue and separation from the rest are bounded below by positive constants on the small fixed ball. These constants depend on this box and normalization.

Simultaneous inversion of $z,z'$ changes the sign of $F_A$, so its ground-state diagonal matrix element is zero. For a unit test with complementary norm $t$, its Gaussian expectation is at most the top eigenvalue minus $d t^2$, where $d$ is the uniform separation. The $sF_A$ term contributes at most $Cs(2t+t^2)$. Absorbing $Cs t^2$ into the gap and completing the square bounds the excess by $O(s^2)$. The Gaussian ground trial gives the reverse bound to the same order. Taking logs yields
$$ E_\beta(A)=\tfrac12\operatorname{Tr}\omega(M_A)+O(\beta^{-1}). \tag{2}$$
This uses cancellation in the top level. The general operator-norm error from dropping the cubic is only $O(\beta^{-1/2})$ in (1).

## Curvature on the two transverse planes

The Gaussian trace energy is analytic near the identity because $M_A$ stays positive definite. Simultaneous color rotation rules out a linear term and forces its quadratic polynomial to be a sum of $A_i\cdot A_j$ with scalar coefficients. Values on commuting backgrounds $A_i=r_i e$ for a single color unit vector $e$ therefore determine the entire quadratic polynomial, even on noncommuting triples.

Index momentum by a nonempty subset $I\subset\{1,2,3\}$ with $m=|I|$ and $\epsilon_i=(-1)^{1_{i\in I}}$. The neutral color spectrum is independent of $r$. For a charged color the flat plaquette derivative is the complex curl with components $d_i=\epsilon_i e^{2\mathrm i r_i}-1$ (the conjugate color gives identical eigenvalues). Indeed the linearized plaquette is $(1-\epsilon_j\operatorname{Ad}_{H_j})z_i-(1-\epsilon_i\operatorname{Ad}_{H_i})z_j$. Its square has eigenvalue $S=\sum|d_i|^2$ twice on the Hermitian complement to $d$ and kernel along $d$. This is exactly the moving horizontal plane. On the plane perpendicular to $n=-1_I/\sqrt m$, fixed at the identity, its two eigenvalues become $S$ and $Q=|n^*d|^2$ by compression of the rank-one term. The two real charged colors cancel the $1/2$ in the vacuum trace. Each momentum therefore contributes $2\omega(S)$ horizontally, and $\omega(S)+\omega(Q)$ on the fixed plane, in addition to its neutral contribution.

Expansion at zero gives
$$
 S=4m+4\sum_i\epsilon_i r_i^2+O(|r|^4),\quad
 Q=4m-8\sum_{i\in I}r_i^2+\frac4m\left(\sum_{i\in I}r_i\right)^2+O(|r|^4).
$$
With $\omega'(t)=1/\sqrt{t(t+4)}$, summing the seven sectors yields $\kappa\sum |A_i|^2$ horizontally. For one component the signed multiplicities over $m=1,2,3$ are $1,-1,-1$. On the fixed plane the quadratic term is instead
$$ q\left[-4\sum_i|A_i|^2+\sum_{i<j}A_i\cdot A_j\right],\qquad q=4/\sqrt{96}+8/(3\sqrt{192})>0.$$
To check the sum, a given pair of axes occurs together once at $m=2$ and once at $m=3$, yielding the stated mixed coefficient from $Q$. A given diagonal coefficient sums to zero at $m=1$, $-16/\sqrt{96}$ at $m=2$ and $-32/(3\sqrt{192})$ at $m=3$. The general analytic remainder after the quadratic term is $O(|A|^3)$. Combining with (2) proves the result. At this fixed box size the sign reversal already occurs in the Gaussian limit. Increasing numerical precision or retaining higher spatial Wilson powers on the fixed plane cannot repair it.

In B4’s convention the charged adjoint angle per link is twice our quaternion angle. The horizontal coefficient here is exactly four times B4’s coefficient in that variable. A fixed chart can also represent the quotient when its kinetic metric is carried through. On a commuting charged block the quadratic form on the fixed plane is $S$ times the pullback metric $g=P_0 P_A|_{E_0}$, where $P_A$ projects orthogonally away from the orbit. Its two metric eigenvalues are $1,Q/S$, positive locally. Whitening this pair gives $S,S$ for the generalized Hessian. The erroneous sign arises when a fixed plane and the uncorrected Euclidean kinetic metric are used together. [B4’s commuting-angle result](../flat-holonomies/README.md) · [Finite-volume action and Hamiltonian comparison](https://arxiv.org/abs/hep-lat/9608015)

For the joint gauge-invariant problem one still needs the transfer between different slow backgrounds, temporal gauge projection and its volume factors, and control outside the small-background neighborhood. A diagonal frozen vacuum estimate does not furnish a variational lower bound for their excitation difference. [Numerical and Lean checks](checks.md)
