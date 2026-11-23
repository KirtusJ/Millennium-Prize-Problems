# The spectrum of a thin center shift

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Flipping one spatial $SU(2)$ link by its central sign produces a gauge-invariant unit vector whose spectral energy concentrates at **$8\lambda$** as the magnetic-to-electric ratio $g=\lambda/\kappa$ tends to infinity. More generally, a pattern of flips that changes the signs of $n>0$ plaquettes has energy concentrated at $2\lambda n$. The error is uniform in the spatial volume, the positions of the flips and $n$. This gives a nonzero spectral band, a lower bound on the dimension of its spectral subspace, and an original Wilson-history measurement using two modified transitions.

For example, at $g=2^{20}$ each single-link shifted vacuum has at least $489469/524288>93.35\%$ of its raw mass between $6\lambda$ and $10\lambda$. On the side-four torus this band contains **at least 94 physical eigenstates**, counted with multiplicity. On the bare weak-coupling path $\lambda=\beta/b$ these states move to ultraviolet energies. The result leaves the lowest physical excitation and the four-dimensional mass gap open. [Multiplicity proof](multiplicity.md) · [Wilson readings](wilson-readings.md)

D4 independently published the Hamiltonian center-shift residual and its fixed-time consequence during this calculation. D4’s Hilbert–Schmidt argument also covers nonscalar central matrices in reducible representations. The rank estimates, transport of a low-energy subspace and direct isotropic Wilson bounds below are additional conclusions. [D4 center-flux theorem](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/04d91694bc7fe596af502913e1902ea5fcb92313/yang-mills/spectral-support/electric-scale/center.md)

## Exact vacuum residual

Use a cubic spatial torus of side $L\ge3$, normalized Haar measure, the half-speed generators $i\sigma_j/2$, and
$$
 H=-\kappa\sum_{e,j}D_{ej}^2+\lambda\sum_p(1-x_p),\quad
 x_p=\tfrac12\operatorname{Tr}U_p,\quad Q=H-E_0,\quad \lambda>0 .
$$
The normalized vacuum $\Omega$ is strictly positive, unique and physical. For central link signs $\eta_e$, define $(D_\eta\psi)(U)=\psi(\eta^{-1}U)$. This unitary commutes with gauge transformations and with the kinetic operator. Let $F_\eta$ consist of the plaquettes with negative product of the oriented signs around their boundary. Set $n=|F_\eta|$, $v_\eta=D_\eta\Omega$. On the untruncated link space one has
$$
 D_\eta^*HD_\eta-H=2\lambda\sum_{p\in F_\eta} x_p .
$$
In particular for $n>0$, $E_\eta=2\lambda n$,
$$
 (Q/E_\eta-1)v_\eta=-D_\eta\!\left[\frac1n
             \sum_{p\in F_\eta}(1-x_p)\Omega\right].
$$
Left translations preserve the elliptic domain. All terms on the right are bounded multipliers. When $n=0$, $D_\eta$ preserves the Hamiltonian and the positive normalized vacuum, so $v_\eta=\Omega$ exactly. This includes nontrivial flat central twists on a torus. For background on gauge disorder operators and center twists see [Mathur and Rathor](https://doi.org/10.1103/PhysRevD.108.114507) and [de Forcrand and von Smekal](https://arxiv.org/abs/hep-lat/0110135).

Let $u=\langle1-x_p\rangle_{\Omega}$, the same on every face. The average deficit in brackets is pointwise between zero and two, so its square is bounded by twice itself. Thus the **raw probability spectral measure** of $Q/E_\eta$ in $v_\eta$ has first moment $1-u$ and squared deviation about one at most $2u$. No spatial independence assumption enters. A4's trial energy gives
$$
 u\le\frac{E_0}{3\lambda L^3}\le\frac{B(g)}g,\qquad
 B(g)=\min(g,17\sqrt g/8+3/16).
$$
Consequently the mass outside the open relative band $|E/E_\eta-1|<\delta$ is at most $2u/\delta^2$ for every $\delta>0$, including any mass at the vacuum when $\delta\le1$. The vacuum overlap itself obeys $|\langle\Omega,v_\eta\rangle|^2\le2u$. [A4's trial and normalization](../../observable-normalization/hamiltonian-variance/)

For $s\ge0$ the unit-time Laplace reading differs from $e^{-s}$ by at most $s\sqrt{2u}$ at physical time $s/E_\eta$; the corresponding real-time phase obeys the same Lipschitz bound. At fixed physical time $t>0$ the raw reading is bounded above by $8u+e^{-tE_\eta/2}$, by splitting the spectrum at $E_\eta/2$. Thus the raw and connected readings both tend to zero at separated fixed times whenever $g\to\infty$ and $E_\eta\to\infty$. On the bare path the dual lattice length of a frustrated plaquette boundary is $nb$. The concentration scale is $2\beta(nb)/b^2$. This describes the energy of the specified thin insertion. A renormalized disorder operator and a physical string tension require separate definitions and estimates.

## A disjoint electric correlation that survives at equal time

At a vertex, translating each of its six incident links by $-I$ is a site gauge transformation. On physical vectors the sign flip of one incident edge therefore equals the product of the flips on the other five. The two operators have disjoint link supports. Their connected equal-time covariance is $1-|\langle\Omega,D_e\Omega\rangle|^2\ge1-2u$. Both readings consequently approach perfect correlation on the weak bare trajectory, while their fixed-positive-time correlation vanishes. Their nearest midpoint distance is only $b/\sqrt2$. Using this pair as a positive-distance continuum reading in the [spatial inverse test](../clustering/) would give an incorrect conclusion.

The same method covers fixed compact connected groups and representations on which the chosen finite center acts by scalars. Averaging shifts over lattice symmetries also controls an entire low-energy input subspace. [Group extension and subspace estimate](multiplicity.md) · [PCP, Lean and independent controls](execution.md)

On the original $SU(2)$ Wilson transfer, a volume-uniform spatial plaquette estimate $u_a=O(1/\beta)$ holds for every $0<a\le b$, including isotropic spacing. For these spacings the raw probability below $(1-\delta)2\lambda n$ tends to zero for each fixed $0<\delta<1$. Both sides of the band are controlled when $2a\lambda n$ stays bounded. At $a=b$ the full upper tail remains open, while the lower-tail probability is $O_\delta(1/\beta)$. These conclusions use the Wilson vacuum at each regulator without a Hamiltonian time-limit assumption. [Direct Wilson proof and physical readings](wilson-readings.md)
