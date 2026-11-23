# The original compact transfer converges to a transverse Mehler operator

Let $G$ be compact and connected, $\rho$ faithful and unitary, $\tau(U)=\operatorname{Re}\operatorname{Tr}\rho(U)/\dim\rho$ and $D=\dim G$. Use the bi-invariant metric $\langle X,Y\rangle=\operatorname{Re}\operatorname{Tr}(d\rho(X)^*d\rho(Y))/\dim\rho$ on its Lie algebra. Then $1-\tau(e^X)=|X|^2/2+O(|X|^4)$ near zero. Globally it bounds a positive constant times the squared distance to identity, by faithfulness, the local expansion and compactness. SU(2) in the defining representation gives the round unit-quaternion metric and the ordinary half-trace Wilson action.

On a finite spatial cube with free spatial boundaries take the sum $V=\sum_p(1-\tau(U_p))$. Write $M_g=\exp[-\eta V/(2g^2)]$, $k_g(v)=e^{-(1-\tau(v))/(\eta g^2)}/Z_t$ with $Z_t$ its Haar integral. The one-step transfer is $M_g K_g M_g$ where $K_g$ convolves each link by $k_g$. In the original temporal-plaquette integral one independent temporal link per vertex inserts the vertex gauge projection. On the physical subspace this gives precisely this transfer. The scalar constants in the action and the one-link normalizations cancel in energy differences. Real normalized trace is a positive-type function (half the sum of the normalized characters of the representation and its conjugate); the exponential kernel is positive as an operator by the power series. Its strictly positive density gives a unique positive vacuum. [Lüscher's Wilson transfer construction](https://doi.org/10.1007/BF01614090) · [Original periodic-time gauge integral](../periodic-time/)

## Rooted coordinates retain the tree noise

Choose a rooted spanning tree, set its links to identity by the uniquely determined gauge transformation equal to identity at the root, and call the remaining $m=|E|-|V_0|+1$ chord holonomies $U_f$. Here $V_0$ denotes vertices. The anchored quotient measure is product Haar on the chords: with original tree links held fixed the change on every other link is left and right translation. Full vertex-gauge invariance is simultaneous root conjugation on this product. The spatial multiplier acts on these coordinates; the kinetic update still samples independent increments $v_e$ on **all** original edges.

Indeed start with tree links one, chord links $U_f$, and right-multiply by the independent increments. Let $h_x$ be the path product of the new tree links from root to $x$ (use inverses along reversed tree edges). The new anchored chord is $h_i U_f v_f h_j^{-1}$ for $f:i\to j$. Thus its joint transition density with respect to output chord Haar is
$$
 \int\prod_{e\in\mathcal T}k_g(v_e)\,dv_e
       \prod_{f:i\to j}k_g(U_f^{-1}h_i^{-1}Y_f h_j).
$$
It is a symmetric kernel because the original reversible convolution acts on the anchored invariant subspace. Multiplying by $M_g(U)M_g(Y)$ recovers the exact compact transfer. Omitting the new tree increments would change the kinetic metric.

Let $C$ be the chord-by-edge matrix with row equal to the signed root-to-tail path, then the chord, minus the root-to-head path. On the chord columns it is identity. Let $d$ be the oriented plaquette-by-chord curl and $d_1$ the original plaquette-by-edge curl. Path cancellation gives $dC=d_1$. The restriction $d$ is injective since the box is contractible and a gradient zero on the tree is zero. In the linear variables the chord increment is $C$ applied to independent Gaussian edge increments of covariance $\eta I$ per color. Consequently its covariance is $\eta B$, $B=CC^*>0$.

## An operator limit before projecting on color

Write $U_f=\exp(gx_f)$ in minimal normal coordinates. Up to the Haar-null cut locus these coordinates identify configurations with an expanding domain in $\mathfrak g^m$. Conjugation preserves it up to null sets. Multiply wavefunctions by the square root of the product Haar density in these coordinates, and extend by zero, to embed the compact transfer in a fixed Lebesgue Hilbert space. This embedding intertwines root conjugation with simultaneous adjoint action. The zero extension adds only zero spectrum.

The rescaled kernels converge in Hilbert–Schmidt norm at each fixed box to
$$
 T_* (x,y)=e^{-\eta |dx|^2/4}\,
      \varphi_{\eta B\otimes I_D}(y-x)\,
      e^{-\eta |dy|^2/4},
$$
where $\varphi$ is a *normalized* Euclidean Gaussian density. To see the normalization, let $J(X)$ be the single-link Haar density in normal coordinates. Then $Z_t/(g^D J(0))\to(2\pi\eta)^{D/2}$. In the tree integral put $v_e=e^{gz_e}$. Each tree increment tends to the corresponding normalized Gaussian. Each chord density contributes a factor $1/(g^D J(0))$ times the linearized Gaussian at $y_f-x_f$ minus the signed tree path noise. The two endpoint square roots of the chord Jacobians cancel exactly this constant. Integrating out the independent tree noises gives $\varphi_{\eta B\otimes I_D}$. The spatial multiplier follows by the quadratic expansion. Faithfulness and tree fixing give a unique flat configuration at identity and a positive quadratic Hessian for $V$. The global Gaussian majorant and expanding-box error are proved separately. [Majorant and quantitative comparison](uniform.md)

Whiten the chord variables by $x=B^{1/2}q$ with the unitary Lebesgue change of measure. The kinetic covariance is now $\eta I$ and the spatial Hessian is $B^{1/2}d^*d B^{1/2}$. Its positive frequencies squared are precisely the positive eigenvalues of $d_1d_1^*$, since $dB d^*=d_1d_1^*$. Orthogonal diagonalization reduces the kernel to one real factor per mode and color,
$$
 (2\pi\eta)^{-1/2}
 \exp[-(q-q')^2/(2\eta)-\eta\omega^2(q^2+q'^2)/4].
$$
Put $\theta=2\operatorname{arsinh}(\eta\omega/2)$ and $\nu=\omega\sqrt{1+\eta^2\omega^2/4}$. Then $\cosh\theta=1+\eta^2\omega^2/2$ and $\sinh\theta=\eta\nu$. Mehler's formula identifies this factor with the oscillator kernel having inverse squared length $\nu$ and eigenvalues $e^{-(n+1/2)\theta}$. Its normalized stationary coordinate covariance across $k$ steps is $e^{-k\theta}/(2\nu)$. [Mehler formula, DLMF 18.18.28](https://dlmf.nist.gov/18.18.E28)

The single-quantum ratio is also C4’s free transfer multiplier $q(v)$ at $v=\eta^2\omega^2$. Thus the Gaussian spatial-clock representation applies mode by mode in this open cavity without a flat zero-mode subtraction. [C4’s hitting-time representation](../../central-quotients/magnetic-smearing/transfer-clock/free.md)

The anchored vacuum is a product of color-rotation-invariant Gaussians. Restrict the norm limit to simultaneous adjoint invariants to obtain the physical spectrum. Ordered nonzero eigenvalues and the projections of separated finite clusters converge by min–max and the resolvent identity. The open boundary and full Gauss law are essential hypotheses. Periodic zero modes alter the small-volume problem treated by Lüscher. [Lüscher on spatial tori](https://doi.org/10.1016/0550-3213(83)90436-4) · [Kogut and Susskind's Hamiltonian formulation](https://doi.org/10.1103/PhysRevD.11.395)
