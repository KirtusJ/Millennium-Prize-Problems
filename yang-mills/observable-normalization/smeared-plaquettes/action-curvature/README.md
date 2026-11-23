# The energy scale of the homogeneous magnetic action

Director A4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Consider the equal-weight sum of the fundamental plaquette traces over all faces and orientations, at zero spatial momentum. For each cubic volume, sample the dimensionless magnetic coupling $g$ uniformly on $[G,2G]$, then sample an excitation from this observable’s **raw spectral measure divided by its variance**. In units of $\kappa\sqrt G$, the sampled energy has uniformly bounded first and inverse moments. Its distribution stays away from zero and infinity in probability, uniformly in $G\ge1$ and in the box size. On the bare spatial trajectory these are energies of order $1/b$, where $b$ is the spatial lattice spacing. The result uses an average in the coupling. A prescribed exceptional coupling can have a different spectrum.

The normalized spectral measure here belongs to the centered observable itself. The [earlier estimate for general smearings](../moment-bounds/refinement.md) concerns an additional energy weight. Its support-size bound does not resolve the raw law of this extensive zero-momentum probe.

## The inverse-energy sum rule

Use the [SU(2) Hamiltonian conventions](../../hamiltonian-variance/). Divide the Hamiltonian by its electric coefficient $\kappa$ and write $H(g)=T+gW$, where $W=\sum_p(1-x_p)$, $x_p=\operatorname{Tr}U_p/2$. The time clock is restored below. Fix any periodic cubic torus of side at least three and let $N$ be its number of faces. Write $e(g)=E_0(g)/N$ and $u(g)=\mathbb E_g(1-x_p)$. The probe is

$$
 f_g=\frac{1}{\sqrt N}\sum_p(2x_p-\mathbb E_g2x_p)
     =-\frac{2}{\sqrt N}(W-\langle W\rangle_g).
$$

Let $\nu_g$ be the spectral measure of $f_g\Omega_g$ for $Q_g=H(g)-E_0(g)$, with dimensionless energy $x$. Write $V=\int d\nu_g$, $m=\int x\,d\nu_g$, $d_2=\int x^2\,d\nu_g$, and $J=\int x^{-1}\,d\nu_g$. At finite volume the positive ground state is simple and the resolvent compact. The centered measure has zero mass at energy zero, and its inverse moment is finite.

Since $W$ is bounded at each finite volume, a small change of $g$ gives a convergent resolvent expansion on a circle isolating the ground eigenvalue. The associated rank-one projection and a locally normalized real eigenvector are analytic. Differentiating in the phase convention $\langle\Omega,\Omega'\rangle=0$ gives $E_0'=\langle W\rangle$, $Q_g\Omega'=-(W-\langle W\rangle)\Omega$, and $E_0''=-2\langle (W-\langle W\rangle)\Omega,Q_g^{-1}(W-\langle W\rangle)\Omega\rangle$, using the inverse on the vacuum complement. The exact normalized identities are

$$
 e'(g)=u(g),\qquad J(g)=-2u'(g),\qquad
 \int_G^{2G}J(g)\,dg=2[u(G)-u(2G)] .
$$

The factor 2 in the last identities uses the unnormalized trace in $f_g$. This is the static-response or inverse-energy-weighted sum rule in the present normalization. No volume-uniform perturbation radius or spectral gap enters the identity. [External grounding for the inverse-energy sum rule](https://www0.mi.infn.it/~jroca/doc/seminars/2025-jun-10-bcn.pdf)

## Size of the fluctuations and both energy tails

Put $r=\sqrt G$, $D=2{,}100{,}000$ and $v_*=1/(1024D)$. Throughout the window, the product-trial bound gives $1+B(g)\le5r$, $S=\mathbb E_g(1-x_p^2)\le5/r$ and $u(G)\le5/(2r)$. The [all-smearing theorem](../moment-bounds/) at unit electric coefficient and $\sum c_p^2=1$ gives

$$
 \frac{1}{32r}\le m\le\frac{80}{r},\qquad d_2\le D,\qquad V\ge\frac{v_*}{G}.
$$

In particular $\int_G^{2G}J\le5/r$. Spectral Cauchy–Schwarz gives $V^2\le mJ$ and $m^2\le Vd_2$. Thus $J\ge m^3/d_2^2$ pointwise, so the inverse response is strictly positive and its coupling average has order $G^{-3/2}$. Writing $\mathbb E_G$ for $G^{-1}\int_G^{2G} dg$, the zero-momentum equal-time variance obeys

$$
 G V(g)\ge v_*\quad\text{for every }g,\qquad
 \mathbb E_G[(G V)^2]\le400.
$$

The upper estimate follows from $G\int_G^{2G}mJ\le G(80/r)(5/r)$. These are statements about the susceptibility of the whole coherent action sum, whose variance includes every cross-plaquette covariance.

Given $g$, normalize by $V(g)$ and set $y=x/r$. For the resulting joint sampling of $g$ and $y$,

$$
 \mathbb E[y]\le80/v_*,\qquad \mathbb E[y^{-1}]\le5/v_* .
$$

Indeed $m/(rV)\le80/v_*$ pointwise. For the reciprocal moment, use $rJ/V\le rGJ/v_*$ and integrate over the coupling window. Markov’s inequality then gives $\Pr(y>R)\le80/(v_*R)$ and $\Pr(y\le\epsilon)\le5\epsilon/v_*$. In particular the averaged laws are tight on $(0,\infty)$. One can convert each averaged tail bound into an exceptional fraction of couplings by a second application of Markov’s inequality. No individual energy level, spectral gap or limiting spectral shape is determined.

## The physical clock and the order of limits

Allow a positive measurable electric coefficient $\kappa(g)$ and let $K_G=\inf_{g\in[G,2G]}\kappa(g)\sqrt G$. A sample has physical energy $E=\kappa(g)r y$. If $K_G>0$, then for a fixed physical threshold $E_*>0$ and time $t>0$ the averaged normalized raw law satisfies

$$
 \Pr(E\le E_*)\le\frac{5E_*}{v_* K_G},\qquad
 \mathbb E[e^{-tE}]\le\frac{5}{e\,v_*tK_G}.
$$

The second inequality uses $e^{-z}\le1/(ez)$ for positive $z$. For the unnormalized probe multiplied by $\sqrt G$, the corresponding averaged low-energy mass is at most $5E_*/K_G$, by integrating $G(E_*/\kappa)J$ directly. Its averaged equal-time squared norm lies between $v_*$ and 20. In particular the vanishing at low energy does not arise merely from an overall vanishing equal-time normalization.

With B4’s bare coefficients $g=\beta^2/2$, $\kappa=2/(\beta b)$, one has $1/b\le\kappa\sqrt G\le\sqrt2/b$ on the window. Thus $\sup_{[G,2G]} b\to0$ implies loss of all averaged raw normalized weight at fixed physical energies and loss of every averaged fixed-positive-time autocorrelation of this probe. A full positive-time limit along all real $g\to\infty$, if it exists in this order of limits, must therefore be zero. A sparse trajectory can select exceptional values. [B4’s temporal matching and bare spatial scaling](../../../transfer-operator/hamiltonian-time/)

All scans hold the volume fixed within each window. The volume may vary arbitrarily **between** windows. If the normalized positive-time correlations converge almost everywhere along a common volume subsequence within a window, dominated convergence passes the averaged estimate to that limit. Finite-volume spectral projectors give measurable tails by bounded approximation in the spectral calculus, and the normalized correlations are bounded by one. The estimates do not permit choosing a different exceptional volume at every coupling inside the same scan. They also do not treat a fixed compactly supported spatial smearing, establish four-dimensional reconstruction, or give a lower mass gap. [Sharp avoided-crossing control](controls.md) · [Verification](execution.md)
