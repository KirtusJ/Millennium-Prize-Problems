# Joint energy and momentum of the squared temporal insertion

Write $C(n,y)$ for A4's connected squared temporal-link reading with $n\ge1$ slabs of displacement and spatial displacement $y$ in cells. For the limiting Gaussian comparison, use the same six signed electric faces and the same scalar coefficient as A4. At spatial frequency $\theta$, set $p_j=e^{i\theta_j}-1$, $a=|p|^2$, $\omega=2\operatorname{asinh}(\sqrt a/2)$ and $D_{2j,j}=-1,\ D_{2j+1,j}=e^{-i\theta_j}$, with all other entries zero and indices starting at zero. The six-by-six cross-covariance is the spatial Fourier coefficient
$$
 K(n,y)=\int e^{i\theta\cdot y} D(pp^*-aI)D^*
 \frac{e^{-n\omega}}{2\sinh\omega}\frac{d^3\theta}{(2\pi)^3}.
$$
The matrix is real by Fourier conjugation. Since $D^*\mathbf1=p$, the all-face mean projects out identically, also for nonzero $y$. Wick contraction of the three independent colors gives $c(n,y)=\|K(n,y)\|_F^2/1536$. The sign of the unsquared electric tensor matters for its angular structure. [A4's fixed-displacement electric kernel](../../observable-normalization/energy-density/staple-response/positive-time.md)

Let $n/r\to t>0$ and $y/r\to x\in\mathbb R^3$. With $\theta=u/r$, the integrand for $r^4 K$ is bounded by $C|u|e^{-c t|u|}$ uniformly away from $t=0$. This follows from the Brillouin-cube bound $\omega(\theta)\ge c|\theta|$. The two rows of each $D$ component approach $(-1,1)$. In spatial indices the limiting electric tensor is
$$
 H_{ij}(t,x)=(\delta_{ij}\Delta_x-\partial_i\partial_j)
     \frac1{4\pi^2(t^2+|x|^2)}
 =\frac{(|x|^2-t^2)\delta_{ij}-2x_ix_j}
        {\pi^2(t^2+|x|^2)^3}.
$$
Indeed the scalar function is the inverse spatial Fourier transform of $e^{-t|p|}/(2|p|)$. The tensor has one radial eigenvalue $-1/[\pi^2(t^2+|x|^2)^2]$ and two transverse eigenvalues $(|x|^2-t^2)/[\pi^2(t^2+|x|^2)^3]$, with the common value at the origin obtained by continuity. Squaring contributes a factor four from the two signed faces in each component. On the [explicit trajectories](local-moments.md), writing $s=|x|^2$,
$$
 \lim\beta^4r^8 C(n,y)=F(t,x)=
 \frac{(t^2+s)^2+2(s-t^2)^2}{384\pi^4(t^2+s)^6}.
$$
The convergence holds uniformly for $t$ in compact positive intervals and $x$ in compact sets by the uniform local moment bound and dominated convergence for every convergent sequence of scaled coordinates. At $|x|=t$ only the radial polarization contributes. At $x=0$ this recovers A4's normalization.

**Two-particle density.** The transform convention is $F(t,x)=\int e^{ip\cdot x}d^3p/(2\pi)^3\int e^{-tE}\rho(E,p)\,dE$. In the square of $H$, the contraction of transverse projectors for the two momenta is $1+(\hat q\cdot\hat q')^2$. Each electric factor contributes $-|q|/2$. Hence at fixed $p=q+q'$ the density integral before its overall factor $1/[1536(2\pi)^3]$ is
$$
 \int_{\mathbb R^3} |q||p-q|\,\big(1+(\hat q\cdot\widehat{p-q})^2\big)
       \delta(E-|q|-|p-q|)\,d^3q .
$$
Equivalently this defines a pushforward of ordinary Lebesgue measure; the delta notation denotes its one-dimensional density. Put $k=|p|>0$, $a=|q|$, $b=|p-q|$. The polar change of variables has Jacobian $2\pi ab/k$. For $E>k$ integrate $a$ from $(E-k)/2$ to $(E+k)/2$ with $b=E-a$. For $E<k$ the triangle constraints give empty support. Since $2ab\,\hat q\cdot\widehat{p-q}=k^2-a^2-b^2$, the substitution $z=(2a-E)/k$ leaves
$$
 \frac{\pi}{16}\int_{-1}^1
 [(E^2-k^2z^2)^2+(2k^2-E^2-k^2z^2)^2]\,dz
 =\frac\pi4\left[(E^2-k^2)^2+\frac8{15}k^4\right].
$$
The edge has no atom: equality in the triangle relation is a collinearity set of zero volume. The case $k=0$ follows either from the radial integral at $p=0$ or by continuity of the density for $E>0$. This yields the stated $\rho$. At fixed $k>0$ its one-sided threshold value is $k^4/(92160\pi^2)$, so the time kernel in that momentum fiber is asymptotic to $k^4e^{-kt}/(92160\pi^2t)$ at large $t$. At zero momentum the density instead starts with $E^4/(49152\pi^2)$. Integrated over all momenta, $\int_0^1 z^2[(1-z^2)^2+8z^4/15]dz=16/105$ gives the energy density $E^7/(128\pi^4\,7!)$. Tilting by $e^{-t_0E}$ and normalizing yields A4's gamma law of shape eight. [Lean polynomial integrals](ElectricSlab.lean)

**Convergence of joint regulator measures.** Spatial translations commute with the positive transfer. For the centered slab vector use their joint spectral measure, representing each torus momentum in the first Brillouin cube $[-\pi r,\pi r)^3$ and putting $E=-r\log\lambda$ for positive transfer values $\lambda$. For fixed $t_0>0$, multiply by $\beta^4r^8\lambda^{\lfloor rt_0\rfloor-1}$. Zero transfer modes drop out eventually. The resulting positive measures have total mass tending to $F(t_0,0)>0$. Their energy tails are uniformly tight by the reading at $t_0/2$ and the exponential bound. Spatial tightness requires a separate argument because only translations by whole cells are given.

Average the measured spatial Fourier coefficients at lag $\lfloor rt_0\rfloor$ over the integer cube $[-N,N]^3$, with $N=\lfloor\epsilon r\rfloor$. Its multiplier is the product of normalized Dirichlet kernels. Its absolute value is at most one. Above $|p|\ge M$ one component has magnitude at least $M/\sqrt3$, and the normalized geometric sum in that component is bounded by $C/(\epsilon M)$ using $|p_i|\le\pi r$. Choose $M$ sufficiently large given $\epsilon$. Twice the difference between total mass and this real Fourier average then bounds the momentum tail. By uniform physical convergence the difference tends to $F(t_0,0)$ minus the cube average of $F(t_0,\cdot)$, which tends to zero with $\epsilon$. This proves tightness in momentum.

On any jointly convergent subsequence, Fourier factors at rounded spatial locations may now be replaced by $e^{ip\cdot x}$, first on a bounded momentum set and then by tightness. The additional time lag gives the factor $e^{-uE}$ for any $u\ge0$, with rounding harmless by energy tightness. Fourier and Laplace uniqueness identify the joint weak limit as $e^{-t_0 E}\rho(E,p)\,dE\,d^3p/(2\pi)^3$. For example, at each $u$ Fourier uniqueness identifies the spatial measure after the extra Laplace weight; then Laplace uniqueness on products of spatial test functions identifies the joint measure. The tilt can be removed on bounded energy windows. Every open energy–momentum box contained in $E>|p|$ has positive limiting weight, and relatively compact sets at positive distance below the cone have vanishing weight. Weak convergence alone gives no occupation at a specified single torus momentum. This is a statement about the spectral measures seen by one electric observable, with other cutoff sectors outside its scope.

B4 independently identified the entire lattice-unit slab measure, including a staggered zero at the corner of the momentum torus. Its untwisted wide-packet coefficient matches this physical continuum fiber: integrating $E^4 e^{-tE}/(49152\pi^2)$ gives $1/(2048\pi^2 t^5)$. The scalar orientation carries that zero-momentum reading and the traceless temporal density vanishes there. B4's lattice corner concerns momenta of order the inverse spacing. [B4 lattice thresholds and packets](../staple-spectrum/)
