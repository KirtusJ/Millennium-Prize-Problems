# The same heat trace in the Hamiltonian vacuum

Let the spatial Hamiltonian be $H=H_0+W$ with $H_0=\gamma\sum_e(-\Delta_{S^3,e})$, $\gamma=1/(2\kappa_B)$ and an arbitrary finite smooth real Wilson magnetic potential $W$. In each finite box the vacuum $\Omega$ is positive and normalized. The scalar observable $F_s=\operatorname{Tr}e^{-sA_U}$ from the [main note](README.md) acts by multiplication. Under gauge transformations $A_U$ is unitarily conjugate, so $F_s$ maps the physical vacuum to a physical state. Its dependence on the spatial links is smooth.

## A deterministic estimate on all compact-link backgrounds

Use $D_e f=f(x)-U_{xy}f(y)$ and $K=e^{-sA_U}$. For a single link generator $X$ with $\|X\|_{\rm op}\le1$, left variation gives $D_e'f=-X U_{xy} f(y)$. Cyclicity of the finite matrix trace reduces differentiation of the exponential to
$$
 \partial_{e,X}F_s=-2s b^{-2}\operatorname{ReTr}(D_e' K D_e^*).
$$
Hilbert–Schmidt Cauchy–Schwarz on $D'_e K^{1/2}$ and $D_e K^{1/2}$ yields
$$
 |\partial_{e,X}F_s|^2\le 4s^2 b^{-4}
 \operatorname{Tr} K(y,y)\, \operatorname{Tr}(D_e K D_e^*).
$$
There are three such orthonormal generators in the unit-round SU(2) metric, the imaginary unit quaternions. For each interior edge the energy contribution is positive. The full sum including Dirichlet boundary edges is exactly $b^2\operatorname{Tr}(A_UK)$. Boundary edges have zero derivative of the form after exterior values are set to zero. The heat-kernel diagonal is bounded by $d b^3 s^{-3/2}$ with $d=2$. Since $z e^{-sz}\le 2(es)^{-1}e^{-sz/2}$ for $z\ge0$,
$$
 \sum_{e}\|\nabla_e F_s\|^2
 \le \frac{24\,2^{3/2}}{e}\,\frac{d^2 V b}{s^2}
 \le 72\,\frac{d^2 V b}{s^2}.
$$
Retaining the edge Dirichlet energy inside the sum gains two spatial powers compared with the estimate obtained by bounding individual adjacency entries without using their endpoint difference. The proof holds pointwise on every configuration without any independence or typicality assumption. For another unitary representation replace the factor three contributed by the generator count by $\sum_\alpha\|d\pi(X_\alpha)\|_{\rm op}^2$ in the preceding calculation. [Heat diagonal proof](wilson-law.md)

The vacuum ground-state transform gives $M_1(F_s)=\langle F_s\Omega,(H-E_0)F_s\Omega\rangle=\gamma\int \sum_e\|\nabla_eF_s\|^2|\Omega|^2$. It follows directly by integration by parts against $H\Omega=E_0\Omega$. For the bare electric clock $\kappa_B=\beta b$,
$$
 M_1(F_s/\sqrt V)\le 36d^2/(\beta s^2).
$$
At every fixed $s>0$, including along $\beta\to\infty$, this estimate is uniform in volume and mesh. Let $\nu$ be the raw Hamiltonian spectral measure of $(F_s/\sqrt V)\Omega$ in energy relative to the vacuum. For any $\epsilon>0$, $\nu([\epsilon,\infty))\le36d^2/(\epsilon\beta s^2)$. Centering changes only the vacuum atom. The Euclidean change $C(0)-C(t)$ is at most $tM_1$. In real time $\|(e^{-it(H-E_0)}-I)(F_s/\sqrt V)\Omega\|^2\le2|t|M_1$, since $1-\cos u\le |u|$. These are statements about the spectral weight excited by this probe. They permit zero-energy weight. A multiplicative coefficient $o(\sqrt\beta)$ still has vanishing positive-energy weight at fixed $s$. [Ground-state form and established electric conventions](../hamiltonian-time/README.md)

## Two different ways to reach Wilson readings

The ground-state estimate applies to Hamiltonians. For each specified finite box and coupling, the [positive-time Wilson comparison](../joint-cutoff/evolution.md) and [vacuum estimate](../joint-cutoff/finite-volume-vacuum.md) apply to this bounded spatial multiplier as well. Its norm divided by $\sqrt V$ is at most $d\sqrt V s^{-3/2}$. At each spatial cutoff first fix $V,\beta,b,s$ and the positive physical time $t$. Then halve the temporal spacing until the bounded-observable comparison for both $C(0)$ and $C(t)$ costs at most the chosen tolerance. One can make the tolerance tend to zero for any sequence of boxes and finite lists of tests. The discrete positive-time difference then vanishes when $\beta\to\infty$. A uniform positive-energy tail of the vacuum-normalized discrete log-transfer measure is bounded by this difference divided by $1-e^{-\lfloor t/a\rfloor a\epsilon}$.

The [separate direct four-dimensional result](README.md) bounds the **whole** unrenormalized heat trace in the original Wilson measure, with $B=1+4\beta_s+2\beta_t$. It applies directly on isotropic weak-bare trajectories with $b^2B\to0$. A temporal refinement could instead take $\beta_t$ so large that the direct bound loses content, which is where the Hamiltonian comparison supplies a distinct conclusion. Neither clock argument establishes a nonzero renormalized heat observable with finite physical excitation energy.
