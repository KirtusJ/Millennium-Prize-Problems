# Site reflection fixes the constant curvature

The loop equations and closedness determine a candidate field $F=G+H$, where $G$ is centered Gaussian curvature and $H$ is an independent random constant two-form. In the original Wilson vacuum, reflection positivity forces $H=0$ for all six orientations and all three colors. The position of the color root and the reflected orientation are essential here. [Decomposition](gaussian.md)

## Reflection at a layer of lattice sites

Begin with a finite periodic lattice. Reflect an axis $i$ through its layer of sites $x_i=0$. Reflection maps an oriented link to the geometrically reflected link, taking its inverse when necessary. For every real bounded function $f$ of links on the positive side (it may use links tangent to layer zero), supported short of the opposite seam,
$$
                 \mathbb E[f\,\theta f]\ \ge\ 0.
$$
The function need not be gauge invariant. To prove this, treat $i$ as the transfer direction and call the variables on its transverse slices $U$. All measures on the original links are product Haar before weighting. For even extent $2m$, fix the tangential links at slices $0,m$ and give each half one half of the tangential action on those two slices. The remaining integrals then factor into identical real quantities by reflection, and their product is a square. This argument allows unequal extents in all the other directions.

For odd extent $2m+1$, keep slice zero fixed and cut between slices $m$ and $-m$. Integrating the positive half up to $m$ with $f$ gives a real function of the last slice. Its reflected half gives the same function on $-m$. Conditional on slice zero the remaining quadratic form uses the kernel of the one step crossing the far cut, including its group integrations. More explicitly the endpoint tangential actions can be shared as positive multipliers $M$ and the middle operator, up to a positive constant, is $M K\Pi M$. Here $K$ is the product of identical one-link convolutions and $\Pi$ averages the site-gauge action on the transverse slice. This identity follows by integrating each normal link on that cut as the gauge variable at its transverse vertex. The one-link kernel is proportional to $\exp(\beta\,q\cdot q')$ on $S^3$; its power series has positive coefficients multiplying dot-product tensor powers. It defines a positive operator on the full link space. The tensor product commutes with $\Pi$ by invariance under simultaneous endpoint rotations, so $K\Pi=\Pi K\Pi$ is positive even on gauge-dependent endpoint functions. The two $M$ factors preserve positivity. The fixed slice-zero factors left outside the form are positive. This proves the inequality also for odd spatial sides. In the time direction one can always take even periods before the vacuum limit. For a continuous half-test used below, Haar-average the full product $f\,\theta f$ over the finite product of site gauge groups at vertices in its support. Gauge invariance of the original probability keeps its expectation unchanged, and the averaged function is a continuous gauge-invariant cylinder function. Fixed-box vacuum convergence applies to that average and therefore transfers the original inequality. This argument concerns the product; separately averaging each factor could change the expectation. [Periodic transfer and gauge projection](../../transfer-operator/periodic-time/) · [Wilson reflection analysis](../../g4/wilson/)

## The odd test

Fix an orientation $ij$ and color $c$. Place the root at zero on the reflecting plane perpendicular to axis $i$. For $n\ge1$ take the positively oriented $ij$ plaquette based at $n e_i$, transported to the root by the straight positive half-axis path. Use
$$
 f=\sin\bigl(t [\sqrt\beta\,\operatorname{Im} U_p^{\rm rooted}]_c\bigr).
$$
For each fixed $n$ and real $t$, this is a bounded positive-half test at all sufficiently large extents. It transforms under a change of color frame at the root; the reflection inequality above applies to it before quotienting by gauge. Its reflected plaquette has the opposite orientation at the reflected square. For these straight axis paths, changing to the positive base cancels the conjugation exactly. Write $b=-n e_i$, $a=b-e_i$, let $E$ point from $a$ to $b$, and let $P_a$ be the positively oriented plaquette at $a$. The reflected word at $b$ is $E^{-1}P_a^{-1}E$. Its straight root transports obey $R_a=R_bE^{-1}$, hence $R_b(E^{-1}P_a^{-1}E)R_b^{-1}=(R_aP_aR_a^{-1})^{-1}$. For comparison with a different fixed system of root paths use the local holonomy estimate from the original-link proof. Inverting a unit quaternion negates its imaginary part exactly. Consequently, writing $p_n$ and $p_{-n-1}$ for the two positively oriented squares, the limiting inequality is
$$
 0\ge \mathbb E[\sin(tF_{p_n,c})\sin(tF_{p_{-n-1},c})].
$$
Both factors are bounded, so weak convergence suffices. Now send $n\to\infty$ **in the already identified tangent law**. The Fourier multiplier of $G$ is bounded on the Brillouin torus. Its Fourier coefficients at this growing separation tend to zero by the Riemann–Lebesgue lemma. The two Gaussian components converge jointly to independent $N(0,1/2)$ variables and remain independent of $H$. Conditionally on $H$, the limiting mean of each sine is $e^{-t^2/4}\sin(tH_{ij,c})$. Hence
$$
           0\ge e^{-t^2/2}\mathbb E[\sin^2(tH_{ij,c})].
$$
Taking the countably many $t=1/m$, $m\ge1$, proves $H_{ij,c}=0$ almost surely: for any nonzero finite value, sufficiently large $m$ gives a nonzero sine. The finite set of components can be treated simultaneously. This proves the whole-sequence Gaussian law for every finite set of rooted faces.

## Single-plaquette Wilson action

The exact quaternion identity
$$
 2\beta(1-x_p)=|F_p^\beta|^2+\beta(1-x_p)^2
$$
and tightness of $\beta(1-x_p)$ imply that the last term tends to zero in probability. Thus $\beta(1-x_p)$ converges in distribution to $\chi_3^2/4$ at any fixed face. Bounded continuous functions of this local action have convergent expectations, as do bounded measurable functions whose discontinuities have probability zero in the limiting law. The separate [uniform exponential moment bound](moments.md) proves convergence of its unbounded mean to $3/4$ and of all higher moments.

For the bounded one-slice observable $O_s^\beta=\exp[-2s\beta(1-x_{12})]$, the same determinant and convolution formulas as for the [two-plaquette difference](dipole.md) apply with the factor $\widehat k_3^2$ **removed** from the spatial integral. Denote the resulting positive measure by $\mu_1$, its Laplace transform by $C_1(n)$, and put $D_1=1+2s C_1(0)=1+s$. The two-slice Gaussian limit now concerns the curvature of the single spatial face. Its centered correlation is
$$
 B_{s,1}(n)=[(1+s)^2-4s^2 C_1(n)^2]^{-3/2}-(1+s)^{-3}.
$$
The angular integral of $\theta_1^2+\theta_2^2$ is $8\pi/3$, giving $\mu_1(dE)=[E^3/(6\pi^2)+O(E^5)]dE$ at zero and $C_1(n)\sim1/(\pi^2 n^4)$. The positive convolution series with $\mu_1,D_1$ has no atoms. Its first term yields
$$
 B_{s,1}(n)\sim\frac{6s^2}{(1+s)^5\pi^4}n^{-8},\qquad
 \rho_{s,1}([0,\epsilon])\sim\frac{6s^2}{(1+s)^5\pi^4\,8!}\epsilon^8.
$$
The weak convergence and successive limits have the same meaning as for the dipole. In particular, the gauge-invariant vacuum sector sampled by this *single* bounded Wilson action has spectral weight approaching arbitrarily small positive energies measured in lattice steps. A gap lower bound in physical units is still a separate question.

## Fixed positive physical time and normalization

There is also a conclusion at physical separations, without a rate. For either bounded observable let $B_\beta(n)$ denote its actual connected transfer correlation on the chosen finite box. Positivity of the normalized transfer gives $0\le B_\beta(n')\le B_\beta(n)$ for $n'\ge n$. On **every** admissible joint sequence and for **any** integers $n_\beta\to\infty$ this gives
$$
 0\le \limsup B_\beta(n_\beta)\le B_s(N)\quad\text{for every fixed }N .
$$
The appropriate single-face or dipole limiting correlation tends to zero with $N$. Thus the connected correlation tends to zero whenever $n_\beta$ diverges, including $n_\beta=\lfloor t/b\rfloor$ for fixed physical $t>0$ and $b\downarrow0$. The mean tends to $D^{-3/2}>0$ and the variance tends to $B_s(0)>0$, with $D$ for the chosen probe. Hence both the variance-normalized correlation and $\langle O_s^\beta(0)O_s^\beta(n_\beta)\rangle/\langle O_s^\beta\rangle^2-1$ tend to zero. Equivalently, the raw connected spectral weight below any fixed physical energy tends to zero, by weak convergence and the absence of an atom at zero lattice energy. These statements concern these two specific local probes.

If one normalizes by the connected reading at the positive time itself, its magnitude has just been shown to vanish. A fixed number of *additional lattice steps* has a well-defined ratio nevertheless. For any $\delta>0$ sufficiently small, the weight in $(\delta/4,\delta/2)$ tends to a positive number. After tilting the spectral measure by $\exp(-n_\beta E)$ and dividing by its mass, the fraction at $E\ge\delta$ is therefore at most $C_\delta e^{-n_\beta\delta/2}$ for sufficiently large regulators along the sequence. The tilted probability concentrates at zero in lattice units. For fixed $k\ge0$ this proves $B_\beta(n_\beta+k)/B_\beta(n_\beta)\to1$. A second separation differing by a fixed **physical** time corresponds to $k$ growing with the cutoff and is outside this ratio estimate.
