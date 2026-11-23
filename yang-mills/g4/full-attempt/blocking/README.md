# Spatial blocking in the electric Wilson measure

The [G4 construction attempt](../README.md) asks how much a time slab transfers between different resolutions of a physical spatial slice. For the electric $SU(2)$ Wilson measure, the proposed straight-link blocking has **zero coupling between resolutions**. Turning on the magnetic action gives a strictly positive, computable derivative for a square and its fine-link detour. This derivative gives a test of any claimed uniform perturbative bound.

### Exact reduction at zero spatial coupling

Use a periodic cubic spatial lattice of side $L$. The temporal coupling is $g>0$, and the spatial coupling is $b$. Take nested dyadic meshes $\ell$ dividing $L$, with all coarse periods $L/\ell\ge4$. Use an even spatial side and keep every link when $\ell=1$. A coarse link is the ordered product of $\ell$ fine links along the straight segment. Denote the full coarse vertex-orbit sigma algebra by $\mathcal A_\ell$. Let $P_{\ell,b}$ be its conditional expectation in the vacuum measure $\pi_b$. At $b=0$, $\pi_0$ is the gauge projection of product Haar. The fundamental one-link multiplier is $q=I_2(g)/I_1(g)$. [Electric spectrum](../electric.md) · [Lüscher’s transfer construction](https://bib-pubdb1.desy.de/record/396349)

The straight coarse links have independent Haar values before the orbit projection. Conditional on fine initial links, each fine link receives an independent central increment. Interleaving these increments with the fixed links and moving them to one end conjugates them by fixed group elements. Thus a coarse link receives central increment law $\mu_g^{*\ell}$, independently for the distinct coarse segments. Coarse observables evolve inside the same coarse orbit algebra. Equivalently a coarse spin network pulls back to constant representation labels along each segment, with the identity contraction at each internal vertex. Self-adjointness now gives $P_{\ell,0}K=KP_{\ell,0}$ for the electric transfer $K$. [Spin-network description](https://arxiv.org/abs/gr-qc/9411007)

On centered $\mathcal A_\ell$ the norm of $K^n$ is exactly $q^{4\ell n}$ by the coarse cycle bound and a fundamental square. It is also exactly $q^{4\ell n}$ on the detail $\operatorname{ran}(P_{\ell,0}-P_{2\ell,0})$ when that next coarser mesh is present. For attainment choose an $\ell$-square having an edge in a row omitted by the $2\ell$ grid. Integrating a private fine link makes its projection at $2\ell$ zero. Winding loops are retained. A coarse period of two would give shorter windings, which explains the side condition. Consequently the actual Wilson resolution spaces satisfy the [weighted form estimate](../resolutions.md) with $w_{ij}=0$ and $d_\ell=1-q^{4\ell n}$ at $b=0$.

### First derivative for one bend

Fix $2\le\ell\mid L$, $L/\ell\ge4$, and integer $n\ge1$. Let $f$ be the fundamental trace of an $\ell$-square in the $xy$ plane, of perimeter $k=4\ell$. Replace one fine edge by the other three edges of its unit $xz$ or $yz$ face on the positive $z$ side. Let $h$ be the trace of this bent loop. One elevated horizontal link is private to the fine readings, so $P_{\ell,0}h=0$. Both loops are simple. Their Haar means vanish, their norms are one and their kinetic eigenvalues are $r=q^k$ and $u=q^{k+2}$. For the *actual moving vacuum* define
$$
 B_n(b)=\langle h-P_{\ell,b}h,\ K_b^n(f-\pi_b f)\rangle_{\pi_b}.
$$
Here $K_b$ is the normalized Markov transfer on the full physical slice, and the field in the first slot can use every fine detail below $\ell$. Taking $\ell=2$ makes it the adjacent fine level. We obtain
$$
 B_n(0)=0,\qquad B_n'(0)=\frac{r^n q^2(1-q^{2n})}{4(1-q^4)}>0. \tag{1}
$$

To see why vacuum normalization matters, set $\lambda=q^4$, $A=\frac12\sum_p\mathrm{Tr}(U_p)$ and $T_b=\exp(bA/2)K\exp(bA/2)$. Write $\Omega_b,\Lambda_b$ for its positive unit vacuum and top eigenvalue. At fixed $g,L$, $\Lambda'_0=0$ and $\Omega'_0=(1+\lambda)A/[2(1-\lambda)]$. Differentiating $K_bF=\Lambda_b^{-1}\Omega_b^{-1}T_b(\Omega_b F)$ gives
$$
  K'_0 F=\frac{K(AF)-\lambda A KF}{1-\lambda}.
$$
This differentiation is legitimate for the bounded functions here. At finite volume the continuous strictly positive kernel smooths $L^2$ into $C$ on the compact link space. The simple-vacuum analytic eigenvector equation therefore upgrades $\Omega_b\to1$ and its derivative to the uniform norm near zero. The densities remain bounded away from zero. In particular $P_{\ell,b}h=\mathbb E_0[\Omega_b^2h\mid\mathcal A_\ell]/\mathbb E_0[\Omega_b^2\mid\mathcal A_\ell]$ tends uniformly to $P_{\ell,0}h$ (essential suprema suffice). [Vacuum and perturbation calculation](../magnetic.md)

For every $b$ the first slot of $B_n$ annihilates constants and $f$. One can therefore replace the second slot by $(K_b^n-r^n)f$. At $b=0$ this vanishes, so derivatives of the measure and moving projection have already been accounted for. The remaining derivative is $\langle h,(K_b^n)'_0 f\rangle_0$. Independent center signs of the links force the only contributory magnetic face in $\langle h,Af\rangle$ to be the chosen detour face. Haar integration of its shared fundamental edge projects the product of traces to $h/2$. The factor $1/2$ in $A$ gives $\langle h,Af\rangle=1/4$. The one-step derivative is $(u-\lambda r)/[4(1-\lambda)]$. Differentiating a product of $n$ transfers multiplies it by $\sum_{j=0}^{n-1}u^j r^{n-1-j}=(r^n-u^n)/(r-u)$ and yields (1). Individually normalizing the centered slots gives the same derivative because their initial norms are one and $B_n(0)=0$.

### A constraint on the multiscale repair

Each of the $k$ boundary edges permits a distinct outward detour towards positive $z$. Different detours have distinct center parities and their Haar-normalized characters are orthogonal. Their normalized sum $h_\Sigma=k^{-1/2}\sum h$ is a kinetic eigenvector with eigenvalue $u$ and has zero coarse conditional mean. Its derivative in (1) is larger by $\sqrt{k}$. If the off-diagonal matrix element is divided by the square root of the two actual diagonal defects $\langle F,(I-K_b^n)F\rangle_{\pi_b}$, its derivative at $b=0$ is exactly
$$
 \frac{\sqrt{k}\,r^n q^2(1-q^{2n})}
 {4(1-q^4)\sqrt{(1-r^n)(1-u^n)}}.
$$
Here the slots are $F=f-\pi_b f$ and $F=h_\Sigma-P_{\ell,b}h_\Sigma$. For **fixed $k,n,L$**, as $g\to\infty$ this slope is asymptotic to $1/[8\sqrt{k+2}(1-q)]\sim g/[12\sqrt{k+2}]$. Thus a bound on this relative cross-resolution form by $C|b|$ in a neighborhood of zero, with $C$ independent of $g$, already fails on these two states. The size of the neighborhood may depend on $g$, since the contradiction takes a derivative at each fixed $g$. Equation (1) does not rule out a bound in rescaled couplings, at other physical lags, or a nonperturbative bound in the isotropic limit. A spectral gap lower bound still requires an estimate on all normalized physical states.

B4’s independent Hamiltonian calculation evaluates the second derivative of the gap at fixed spatial spacing. The derivative here answers a separate question about mixing between *spatial readings* when the magnetic term is turned on. Both computations use the same vacuum transfer convention. [B4’s magnetic calculation](../../../transfer-operator/blocked-time/magnetic-curvature/README.md) · [Formal and numerical checks](checks.md)
