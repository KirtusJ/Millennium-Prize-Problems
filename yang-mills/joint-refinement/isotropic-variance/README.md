# The unfiltered Wilson plaquette sum at isotropic coupling

G4 for joint review with Z4, following [PR #23](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/23). Fix a spatial orientation, a periodic even spatial side $N\ge6$, $V=N^3$, and isotropic Wilson coupling $\beta\ge1$ for SU(2) in four dimensions. In the infinite-time vacuum let $F=V^{-1/2}\sum_x X_x$ with $X_x=\beta(1-\operatorname{Tr}U_{p_x}/2)$. The target is $\chi=\operatorname{Var}F$ along the prescribed refinement. The sum contains **every** plaquette of that orientation, including its zero spatial momentum.

Integrating out half the links of one orientation on the measurement slice gives the exact identity
$$
 \chi=\operatorname{Var}M+J,\qquad 2^{-22}/49\ \le J\le 2K,\qquad K=14\,905\,840.64 .
$$
The bounds on $J$ hold at each isotropic regulator independently of side and coupling. $M$ is an explicit sum of local staple functions defined below. Thus a divergence of $\chi$ must occur in $\operatorname{Var}M$. The identity supplies no uniform ceiling for that term yet. A [spatial-transfer estimate](spatial.md) isolates the relevant low energies by testing only local plaquettes on coordinate axes. A [direct small-coupling proof and its failure test](influence.md) give a pointwise uniform bound in a different coupling interval. [Matched isotropic measurements and signed normalization](measurements.md)

### Integrating every plaquette on the slice

Take faces in the $xy$ direction. Among all $x$-links on the measured slice select those with $y+z$ even. A face containing two parallel $x$-links separates them by one step in $y$, $z$ or time. It therefore contains at most one selected link. Every measured $xy$ face contains exactly one, including across a periodic seam. Each selected link accounts for the two measured faces that meet it. Condition on the exterior $\mathcal B$ of this set of $V/2$ links in spacetime. At finite temporal period the conditional law is a product. The same disintegration holds in the time vacuum by taking a cylinder with one extra layer on either side of the measured links and ground-state weights in the exterior.

Use real unit quaternions for the link variables. For a selected link let $a_+,a_-$ be the two three-link staples joining its endpoints around the measured faces, $A=a_++a_-$, and $H$ the sum of all six incident staples in the same orientation. Each measured half-trace is $u\cdot a_\pm$. The pair contributes $Y=\beta(2-u\cdot A)$. Conditionally $u$ has density proportional to $\exp(\beta u\cdot H)$ with respect to Haar probability. Put $k=\beta|H|$, $R(k)=I_2(k)/I_1(k)$, and $h=H/|H|$ when $H\ne0$. The conditional pair mean and variance are
$$
 m_e=\beta(2-R(k)\,h\cdot A),\qquad
 j_e=\beta^2\big[R'(k)(h\cdot A)^2+(R(k)/k)(|A|^2-(h\cdot A)^2)\big].
$$
At $H=0$ use $m_e=2\beta$ and $j_e=\beta^2|A|^2/4$. Haar integration gives $Z(k)=2I_1(k)/k$. The mean and covariance of $u$ are the gradient and Hessian of $\log Z(|v|)$ at $v=\beta H$, which gives the formulas including $R'=1-3R/k-R^2$. Rotations of the endpoint gauge frames act orthogonally on $u,H,A$ and leave these scalars invariant. This is analytic one-link integration at the full Wilson coupling. [Parisi, Petronzio and Rapuano](https://doi.org/10.1016/0370-2693(83)90930-9) · [NIST Bessel recurrences](https://dlmf.nist.gov/10.29)

Set $M=V^{-1/2}\sum_e m_e$ and $J=V^{-1}\sum_e\mathbb E j_e$. Then $M=\mathbb E[F\mid\mathcal B]$. Conditional independence gives $V^{-1}\sum j_e$ for the conditional variance. Total variance proves the identity. For the upper bound, $\mathbb E j_e\le\operatorname{Var}Y\le4K$ by Cauchy–Schwarz on the two centered plaquettes and the [uniform local moment](../low-spin/plaquette.md). There are $V/2$ pairs.

For the lower bound the [tilted Haar variance lemma](../low-spin/plaquette.md) gives $j_e\ge 2^{-22}\beta^2 |A|^2/(1+k)^2$. Since $k\le6\beta$, the coefficient is at least $2^{-22}/49$. Moreover $\mathbb E|A|^2=2+2\mathbb E(a_+\cdot a_-)\ge2$. To check the sign, reflect through the spatial plane containing the selected link and normal to $y$. Fix all tangential links on it and on the opposite plane. On the periodic cylinder the two open halves then have independent reflected conditional laws. Each staple is a function of its respective half and their shared endpoints. Reflection takes the path of $a_+$ into the path of $a_-$ with the same endpoints. Pairing their four real components gives the squared norm of the conditional mean. Equivalently the inner product is the half-trace of the $1\times2$ rectangle. This proof uses the unreduced positive Wilson measure. Take the periodic time limit at fixed $N,\beta$ for the bounded rectangle before applying the uniform claim.

### What passes through a fixed physical time

For two insertions at lattice lag $d\ge2$, integrate both checkerboards at once. No action face contains selected links from both endpoints. The two conditional means are still the same local functions, because each needs only its own slice and its immediate time neighbors. Consequently
$$
 \operatorname{Cov}(F_0,F_d)=\operatorname{Cov}(M_0,M_d),\qquad
 0\le\operatorname{Cov}(F_0,F_d)\le\chi-J .
$$
The first inequality uses positivity of the physical transfer for $F$. The second is ordinary Cauchy–Schwarz in the common stationary law. The function $M_t$ uses more than one time slice. This identity does not interpret it as a one-slice transfer insertion. One may fix a positive physical time $t_0$ and use $d=\max(2,\lceil t_0/a_t\rceil)$. A uniform upper bound on $\operatorname{Var}M$ would now give a strict uniform normalized deficit for the full zero-mode observable. The checkerboard can erase coarse links, so this conditioning does not by itself prove a joint bound for arbitrary coarse additions. A bound on raw $\chi$ would separately supply the covariance hypothesis for the private packings in [the coarse-coupling argument](../plaquette-covariance/README.md).

**Remaining step.** Repeating the same conditional integration fixes $M$ exactly. Local integration alone gives no further decay of its spatial correlations. The reduced measure includes the factor $\prod_e 2I_1(\beta|H_e|)/(\beta|H_e|)$ times all unintegrated Wilson weights. Replacing it by independent staples changes the zero mode. The strict upper bound for the unfiltered variance at the matched couplings, the all-state continuum gap and the group extension remain open. [Quadratic comparison](quadratic.md) · [Lean, controls and reproduction](replay.md)
