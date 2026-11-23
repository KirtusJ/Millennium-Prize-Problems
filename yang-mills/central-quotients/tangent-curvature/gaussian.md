# The microscopic law up to a constant mode

Let $F$ be any joint limit from the [original Wilson measure](wilson-law.md). It is closed, has uniformly bounded component second moments, and satisfies the compactly supported Haar variation identity. For a finite real colored test $g$ on faces write $F(g)=\langle F,g\rangle$ and $\phi(g)=\mathbb E e^{iF(g)}$. For $u=dh$, inserting the characteristic function test with argument $g+tu$ into that identity and differentiating in $t$ gives
$$
 \frac d{dt}\phi(g+tu)=-(\langle g,u\rangle+t\|u\|_2^2)\phi(g+tu).
$$
The finite first moment of $F(u)$ justifies the derivative. Integration at zero gives $\phi(g+tu)=\phi(g)\exp[-t\langle g,u\rangle-t^2\|u\|_2^2/2]$. In particular all compact exact test variables are jointly centered Gaussian with covariance the ordinary $\ell^2$ inner product.

Let $\mathcal E=\overline{d C_c^1}^{\,\ell^2}$ in three-color two-cochains and let $P$ be orthogonal projection onto $\mathcal E$. The isometry $Z(dh)=F(dh)$ extends into $L^2$ of the same probability space for all $u\in\mathcal E$. Its joint laws stay Gaussian by $L^2$ approximation. Put $G(g)=Z(Pg)$ and $R(g)=F(g)-G(g)$ for finite $g$. Then $d^*R=0$ since $R(dh)=0$. Also $dR=0$ since $F$ is closed and $P d^*k=0$ for every finite three-cochain $k$. These assertions hold simultaneously on all cells by countability.

The cubical Hodge Laplacian $dd^*+d^*d$ is the scalar nearest-neighbor Laplacian on every component. Indeed the Fourier symbols of $d$ and $d^*$ are exterior multiplication by $p=(e^{ik_j}-1)_j$ and contraction with its conjugate. Their anticommutator is $|p|^2 I$. This is an identity of finite-difference operators and so applies to $R$ without any summability at infinity. Thus each component of $R$ is harmonic. Its coordinate second moments are uniformly bounded by the curvature estimate and $\|P\|\le1$.

For any real $Y\in L^2$, the scalar function $x\mapsto\mathbb E[R_{ij,c}(x)Y]$ is bounded and harmonic on $\mathbb Z^4$, hence constant. One proof uses a lazy walk which chooses a coordinate uniformly and moves by $-1,0,1$ with probabilities $1/4,1/2,1/4$. Couple two walks starting at adjacent sites. Synchronize all other coordinates. When the differing coordinate is chosen, use increment pairs $(-1,0),(0,-1),(1,0),(0,1)$ equiprobably until meeting. The difference performs a recurrent one-dimensional simple walk at those updates. Synchronize after meeting. Bounded harmonic functions have the same mean at all times under this walk, and the probability of failure to meet tends to zero. Taking $Y=R_{ij,c}(x)-R_{ij,c}(0)$ proves $R_{ij,c}(x)=R_{ij,c}(0)$ almost surely. Write this random constant two-form as $H$.

Passing the characteristic identity by $L^2$ approximation to $u\in\mathcal E$, then replacing $u$ by $u-Pg$, yields
$$
 \mathbb E e^{iR(g)+iZ(u)}
   = \phi(g)e^{\|Pg\|^2/2}e^{-\|u\|^2/2}
   = \mathbb E e^{iR(g)}\,\mathbb E e^{iZ(u)} .
$$
Taking arbitrary finite linear combinations proves independence of $H$ and the entire Gaussian field. Each subsequential law is therefore a lattice Gaussian curvature plus an independent constant random two-form. At this stage the law of $H$ is undetermined. [Site reflection](reflection.md) fixes it in the Wilson vacuum. Every finite group of tests whose coefficients sum to zero separately in each orientation and color has a unique limit along the **whole** sequence. For such tests the mean is zero and the joint limiting covariance is $\langle g,Pg'\rangle$. This is a statement of convergence in distribution. Unbounded moments along the cutoff sequence require separate uniform integrability.

For $k\ne0$ the Fourier multiplier of $P$ is
$$
 P(k)=\frac{p\wedge\iota_{\bar p}}{|p|^2}.
$$
Its range is that of exterior multiplication by $p$ from one-forms and its rank is three per color. Projection onto the closure of the finite exact forms has precisely this multiplier. To see the reverse inclusion, first exclude a small neighborhood of $k=0$ from a square-integrable range section; there $(\iota_{\bar p}/|p|^2)$ supplies a bounded one-form preimage. Approximate that preimage in $L^2$ by trigonometric polynomials, apply the bounded exterior multiplier and then remove the excluded neighborhood. The diagonal multiplier in orientation $ij$ is $(|p_i|^2+|p_j|^2)/|p|^2$. Its normalized torus integral is $1/2$ by permutation symmetry. Thus each single-face limiting vector is $N(0,I_3/2)+H_{ij}$. Truncation and $2(1-x_p)\ge|\operatorname{Im}U_p|^2$ imply, for each spatial or temporal orientation,
$$
 \liminf_{\beta,L\to\infty}\beta\,\mathbb E(1-x_p)\ge 3/4 .
$$
For this inequality take a sequence realizing the liminf, extract a curvature limit and apply the lower semicontinuity of the second moment. Independence and centering of the Gaussian make the cross term zero.

A second check uses $F(dh)$ with $h$ supported on a single oriented edge and one unit color. The six incident faces give variance six. For the resulting three-color vector $j$, $\mathbb E e^{-s|j^\beta|^2}\to(1+12s)^{-3/2}$ for $s\ge0$ when the incident faces are transported into the same local frame with their incidence signs. A bounded time-slice observable with a nonlocal-in-time spectral response is computed in the [dipole calculation](dipole.md).
