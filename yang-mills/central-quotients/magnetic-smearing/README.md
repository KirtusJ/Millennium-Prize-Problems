# A free curvature limit and positive physical-time readings on the pure Wilson lattice

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00) · Yang–Mills existence and mass gap

In the original four-dimensional isotropic $SU(2)$ Wilson vacuum, a magnetic field smeared over a fixed physical region has a nonzero connected reading at every finite positive physical time on explicit weak-coupling trajectories. Sum the parallel-transported, scaled plaquette curvatures first and then take their squared norm. The cross terms between distinct faces survive. Both normalization by the variance and normalization by the square of the mean give positive signals.

Write $r=1/b$, where $b$ is the spacing, $L$ for the spatial torus side in lattice cells and $\beta$ for the inverse bare coupling. Take the infinite-time vacuum at each finite regulator. If
$$
 r\to\infty,\qquad L/(r^3\sqrt{\log(2+r)})\to\infty,\qquad
 \beta/(r^{16}\log(2+r))\to\infty ,
$$
the full spacetime rooted curvature, tested at physical scale, converges in law locally in $H^{-a}$ for every $a>2$. Its limit has three independent colors and the Gaussian Maxwell curvature covariance. The estimates control every joint sequence satisfying the bounds. For instance $\beta=r^{17}$ and $L=\lceil r^4\rceil$ suffice. A reflection-symmetric spatial profile already gives the positive-time and energy-band conclusions when $L/(r^2\sqrt{\log(2+r)})\to\infty$ and $\beta/(r^{12}\log(2+r))\to\infty$.

For a real spatial profile $\psi$ with $J=\int\psi\ne0$, let $X_r$ be the smeared $12$-curvature and $Q_r=|X_r|^2/2$. Its limiting connected spectral mass below physical energy $\epsilon$ is asymptotic to $3|J|^4\epsilon^8/(2\pi^4\,8!)$. The limiting connected correlation at physical time $t$ is $3C_0(t)^2/2$, where $C_0$ is the magnetic Maxwell covariance for that profile. The same construction gives a bounded observable $\exp(-\sigma |X_r|^2)$ with positive raw weight arbitrarily near zero. The finite-box gauge-invariant transfer gap consequently tends to zero **in physical units on the stated trajectories**. Without assigning a physical scale, $\min(\beta^{1/13},L^{1/3})\Delta_{\rm lattice}\to0$ along every sequence $\beta,L\to\infty$.

| Derivation | Result |
| --- | --- |
| [Rooted Ward identity](ward.md) | Quantitative change of moving color frame, quantitative closure and characteristic-function error |
| [Stopped-walk decomposition](smoothing.md) | Finite support and explicit joint conditions without wrapping the box |
| [Ordinary profiles](ordinary-profile.md) | Site reflection recovers undifferenced magnetic profiles and all fixed polynomial moments |
| [Spacetime field](field.md) | All six face orientations and local negative-Sobolev tightness |
| [Spectral measure](spectrum.md) | Bounded positive-time ratios and physical low-energy exponents eight, twelve or sixteen depending on the spatial profile |
| [PCP and computational evidence](execution.md) | Formal scope, independent original-link variations, negative controls and reproduction |

These trajectories produce a free field in the observed sector. A logarithmic bare-coupling trajectory with a fixed nonzero renormalized interaction scale lies outside the joint bounds. The existence and mass gap of interacting four-dimensional Yang–Mills theory remain open. The mathematical arguments here have been deposited for cross-review; the Lean verification covers the listed supporting results.

The starting estimate concerns the [actual isotropic Wilson vacuum](../tangent-curvature/moments.md). The [earlier fixed-cell analysis](../tangent-curvature/) found vanishing connected correlations at fixed physical time for individual local actions. This construction uses a growing number of coherently transported faces. As a literature comparison, Chatterjee's scaling-limit result concerns a gauge field coupled to a fundamental Higgs field and yields a massive Gaussian limit in its specified scaling. The present calculation uses the pure Wilson action. [Chatterjee, A scaling limit of SU(2) lattice Yang–Mills–Higgs theory](https://arxiv.org/abs/2401.10507)
