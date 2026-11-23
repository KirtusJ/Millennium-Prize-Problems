# A separated Wilson correlation from the exterior of a single temporal link

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

At one temporal link $e$ of the original isotropic four-dimensional SU(2) Wilson measure, take the sum of its six incident scaled face actions $Y_p=\beta(1-\operatorname{tr}U_p/2)$. Subtract its conditional mean given all other links to obtain $W_e$. The one-step transfer insertion of $W_e$ vanishes at every finite coupling. Squaring before inserting it gives a positive-time response. Its entire transfer insertion is the conditional variance $V(R_e)$, a function of the six three-link paths around $e$.

In the infinite-time vacuum on a periodic spatial torus, the mean of that conditional variance satisfies, along every $\beta,L\to\infty$,
$$
 \mathbb E W_e^2=\frac32-\frac1{8\beta}-\frac3{32\beta^2}+o(\beta^{-2}).
$$
Freezing the surrounding links at the identity instead gives coefficient $-1/32$ at second order. The additional $-1/16$ comes from the mean angular spread of the staples in the Wilson vacuum.

For parallel temporal links at the same spatial point separated by $n\ge1$ lattice steps, let $C_{\beta,L}(n)=\operatorname{Cov}(W_e^2,W_{e+n}^2)$. Then
$$
 \lim_{\beta,L\to\infty}\beta^4 C_{\beta,L}(n)=c(n)>0,
 \qquad \lim_{n\to\infty}n^8c(n)=\frac1{128\pi^4}.
$$
These are successive limits. A diagonal selection below gives physical-time readings for certain trajectories. The interacting Yang–Mills construction and the physical mass gap on a trajectory with a nonzero renormalized interaction remain open. The inputs for the local law are C4's [rooted microscopic limit](../../../central-quotients/tangent-curvature/) and [uniform Wilson moment bound](../../../central-quotients/tangent-curvature/moments.md).

## An exact identity at fixed cutoff

Write the six face traces $x_p=U_e\cdot v_p$ with unit three-link quaternions $v_p$, and put $H=\beta\sum v_p$, $R=|H|$, $z=U_e\cdot H/R$, $D=R(1-z)$, $m=\mathbb E_R z$. At zero staple set $D=W_e=V(0)=0$. The conditional link density is proportional to $e^{Rz}$ times Haar, and
$$
 W_e=D-\mathbb E_R D,\qquad V(R)=R^2\operatorname{Var}_R z.
$$
Once the two spatial boundaries of this one-step slab and all its other temporal links are fixed, the only dependence on $U_e$ in the Boltzmann weight is its six-face exponential. Normalizing this one-link integral and reattaching its normalizer shows that any bounded insertion $h(W_e)$ gives the same boundary kernel as $\mathbb E_R h(W_e)$. This equality holds for each pair of boundary configurations, before the remaining integrals and vacuum limits. At fixed cutoff the polynomial readings used here are bounded. In particular the transfer kernels of $W_e$ and $W_e^2-V(R)$ vanish identically. The kernels of $W_e^2$ and $V(R)$ coincide. More generally on any cofacial-independent pair the two link laws factor conditional on their joint exterior, so
$$
 \operatorname{Cov}(W_e^2,W_f^2)=\operatorname{Cov}(V(R_e),V(R_f)).
$$
Aligned temporal links in adjacent slabs qualify even though the slabs share a spatial boundary. An equal-link fourth moment has no such factorization.

## The first environment correction

For the reference $G\sim\mathrm{Gamma}(3/2,1)$ use the radial tilt $l_R(y)=\sqrt{(1-y/(2R))_+}$. Its moments normalized by $\mathbb E l_R(G)$ give those of $D$. On $0\le y\le R$, Taylor's formula gives $l_R(y)=1-y/(4R)-y^2/(32R^2)+O(y^3/R^3)$ with an absolute constant. Beyond $R$ the exponential gamma tail bounds the integral of every term times any fixed power. In $\mathbb E[G^k l_R(G)]$, the first three coefficients for $k=0,1,2$ respectively are
$$
 (1,-3/8,-15/128),\quad(3/2,-15/16,-105/256),\quad
 (15/4,-105/32,-945/512).
$$
On dividing by the normalizer and subtracting the squared mean,
$$
 V(R)=3/2-3/(4R)-9/(8R^2)+O(R^{-3}).
$$
Write $\delta_e=6\beta-R_e$. The identity $\delta_e=\sum_{p\ni e}Y_p-D$ implies $0\le\delta_e\le\sum Y_p$. C4's exponential moment bounds control every moment of $\delta_e$ and give an exponentially small probability of $R<3\beta$. Also $D$ is stochastically bounded by $G$ conditionally and its moments tend to those of $G$ as $R\to\infty$. Thus $\mathbb E\delta_e\to6(3/4)-3/2=3$. On $R\ge3\beta$, expand the two reciprocals about $6\beta$. The remainder in the following identity in $L^2$ is bounded pointwise there by $C(1+\delta_e+\delta_e^2)/\beta$:
$$
 \beta^2[V(R_e)-3/2+1/(8\beta)]=-\delta_e/48-1/32+O_{L^2}(\beta^{-1}).
$$
On the exceptional event use $0\le V(R)\le\mathbb E_R D^2\le15/4$, $\delta_e\le6\beta$ and the exponential tail. Taking the mean proves the displayed second-order coefficient. Cauchy–Schwarz gives the uniform-in-separation comparison $\beta^4 C_{\beta,L}(n)=\operatorname{Cov}(\delta_e,\delta_{e+n})/48^2+O(\beta^{-1})$ for $n\ge1$ in these vacua. Further spatial or temporal decorrelation of the error would be needed to use this comparison at large separation on a slowly growing bare coupling.

## Identification of the coefficient

For six unit quaternions,
$$
 \delta_e=\frac{\beta\sum_{p<q}|v_p-v_q|^2}{6+|\sum_p v_p|}.
$$
Right multiplication by the inverse of the actual link takes each $v_p$ into the same endpoint frame. Its real part is $1-Y_p/\beta$; its imaginary part times $\sqrt\beta$ tends jointly on fixed patches to the appropriately signed face curvature $F_{p,e}$. Fixed local transports can be compared in the common rooted gauge of the tangent theorem. The denominator tends to 12. The real coordinate differences disappear after scaling. Uniform moment control upgrades joint convergence in law to convergence of each fixed mixed moment of the deficits. In the limiting three-color Gaussian field
$$
 \delta_e^G=\tfrac12\sum_{p=1}^6|F_{p,e}-\bar F_e|^2,
 \qquad \bar F_e=\tfrac16\sum_p F_{p,e}.
$$
Let $K(n)$ be the single-color $6\times6$ cross-covariance between the signed faces at the two links. For $P=I-\mathbf1\mathbf1^T/6$, Wick contraction in the three independent colors gives $\operatorname{Cov}(\delta_e^G,\delta_{e+n}^G)=\tfrac32\|P K(n)P\|_F^2$. Therefore $c(n)=\|P K(n)P\|_F^2/1536$. The calculation uses true covariance subtraction of the random environment. Retaining only the two independent gamma coordinates extracted in the [contact calculation](../contact-law/radial.md) gives zero separated covariance at every cutoff.

[Time kernel, physical-time selection and spectral consequences](positive-time.md) · [Execution and negative controls](execution.md)
